"""
train_lda.py
============
Production-grade training & validation pipeline for the ERP -> shrinkage-LDA
stimulation-intensity decoder.

Pipeline (per the spec):
    epoched EEG -> ERPFeatureExtractor -> StandardScaler -> shrinkage-LDA

Validation modes:
    within     : per-subject repeated stratified K-fold (default 5x5), then
                 aggregate across subjects. Tests "decode this person's trials."
    loso       : leave-one-subject-out. Tests "decode an unseen person"
                 (calibration-free), with per-subject feature normalization to
                 control inter-subject variability (spec section 6).

Everything is leakage-safe: feature extraction parameters are fixed (not fit on
labels), the scaler and LDA are fit inside each training fold only, and LOSO
normalization statistics are computed per subject independently.

Usage (as a script): edit the CONFIG block at the bottom and run
    python train_lda.py

Usage (as a library):
    from train_lda import run_within_subject, run_loso, load_dataset
    subjects = load_dataset("ds_trimmed/")
    res = run_within_subject(subjects, feature_set="recommended")
"""

from __future__ import annotations
import glob, os, warnings
import numpy as np
from pathlib import Path

warnings.filterwarnings("ignore")

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import RepeatedStratifiedKFold, LeaveOneGroupOut
from sklearn.metrics import balanced_accuracy_score, confusion_matrix

from erp_features import (ERPFeatureExtractor, load_npz_for_features,
                          baseline_sd_outlier_mask, FEATURE_SETS)


# ─────────────────────────────────────────────
# DATA LOADING
# ─────────────────────────────────────────────
def load_dataset(folder, artifact_filter=True):
    """
    Load every .npz subject in `folder`.

    Returns a list of dicts: {X, y, meta, subject_id}. Subjects may differ in
    epoch length / class scheme; that is fine for within-subject. For LOSO we
    check consistency at run time.
    """
    files = sorted(glob.glob(os.path.join(folder, "*.npz")))
    if not files:
        raise FileNotFoundError(f"No .npz files in {folder}")
    subjects = []
    for f in files:
        X, y, meta = load_npz_for_features(f)
        if artifact_filter:
            keep = baseline_sd_outlier_mask(X, meta)
            if keep.sum() < len(keep):
                X, y = X[keep], y[keep]
        subjects.append({"X": X, "y": y, "meta": meta,
                         "subject_id": meta["subject_id"]})
    return subjects


def _make_pipeline(feature_set, meta):
    """ERP features -> scale -> shrinkage LDA. meta is bound into the extractor."""
    fx = ERPFeatureExtractor(feature_set=feature_set).set_meta(meta)
    return Pipeline([
        ("erp", fx),
        ("scale", StandardScaler()),
        ("lda", LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")),
    ])


# ─────────────────────────────────────────────
# WITHIN-SUBJECT VALIDATION
# ─────────────────────────────────────────────
def run_within_subject(subjects, feature_set="recommended",
                        n_splits=5, n_repeats=5, random_state=0, verbose=True):
    """
    Per-subject repeated stratified K-fold. Returns per-subject and pooled stats.

    For each subject the full Pipeline (features+scaler+LDA) is refit on each
    training fold, so there is no leakage. Feature extraction is identity w.r.t.
    labels, so fitting it inside the fold is safe and kept for strict hygiene.
    """
    per_subject = []
    for s in subjects:
        X, y, meta = s["X"], s["y"], s["meta"]
        classes, counts = np.unique(y, return_counts=True)
        min_count = counts.min()
        splits = min(n_splits, int(min_count))     # guard tiny classes
        if splits < 2:
            if verbose:
                print(f"  [skip] {s['subject_id']}: too few trials per class")
            continue
        cv = RepeatedStratifiedKFold(n_splits=splits, n_repeats=n_repeats,
                                     random_state=random_state)
        fold_acc, fold_bal = [], []
        for tr, te in cv.split(X, y):
            pipe = _make_pipeline(feature_set, meta)
            pipe.fit(X[tr], y[tr])
            pred = pipe.predict(X[te])
            fold_acc.append((pred == y[te]).mean())
            fold_bal.append(balanced_accuracy_score(y[te], pred))
        per_subject.append({
            "subject_id": s["subject_id"],
            "n_classes": len(classes),
            "chance": 1.0 / len(classes),
            "acc_mean": float(np.mean(fold_acc)),
            "acc_std":  float(np.std(fold_acc)),
            "bal_mean": float(np.mean(fold_bal)),
        })
        if verbose:
            r = per_subject[-1]
            print(f"  {r['subject_id']:>10s}: acc={r['acc_mean']*100:5.1f}% "
                  f"+/-{r['acc_std']*100:4.1f}  bal={r['bal_mean']*100:5.1f}%  "
                  f"(chance {r['chance']*100:.0f}%)")
    accs = np.array([p["acc_mean"] for p in per_subject])
    bals = np.array([p["bal_mean"] for p in per_subject])
    summary = {
        "mode": "within_subject",
        "feature_set": feature_set,
        "n_subjects": len(per_subject),
        "cv": f"{n_splits}x{n_repeats} repeated stratified k-fold",
        "acc_mean": float(accs.mean()) if len(accs) else float("nan"),
        "acc_std":  float(accs.std()) if len(accs) else float("nan"),
        "bal_mean": float(bals.mean()) if len(bals) else float("nan"),
        "chance":   per_subject[0]["chance"] if per_subject else None,
        "per_subject": per_subject,
    }
    return summary


# ─────────────────────────────────────────────
# LEAVE-ONE-SUBJECT-OUT VALIDATION
# ─────────────────────────────────────────────
def _extract_all(subjects, feature_set):
    """
    Extract features for every subject (fixed params, no label use), returning
    pooled F, y, group ids, and the per-subject row index ranges. Done once,
    reused across LOSO folds.
    """
    Fs, ys, groups = [], [], []
    ref_meta = subjects[0]["meta"]
    for gi, s in enumerate(subjects):
        fx = ERPFeatureExtractor(feature_set=feature_set).set_meta(s["meta"])
        F = fx.fit_transform(s["X"])      # extraction is label-free
        Fs.append(F); ys.append(s["y"]); groups.append(np.full(len(s["y"]), gi))
    return (np.concatenate(Fs), np.concatenate(ys), np.concatenate(groups),
            [s["subject_id"] for s in subjects])


def _per_group_zscore(F, groups, train_mask):
    """
    Per-subject z-score normalization (spec section 6). Stats are computed within
    each subject independently, which is valid for cross-subject transfer and
    does not leak label info. Applied to all rows; train/test share only the
    subject's own stats (and each test subject is normalized by its own stats,
    which is legitimate since it uses no labels).
    """
    Fn = F.copy()
    for g in np.unique(groups):
        gm = groups == g
        mu = F[gm].mean(axis=0)
        sd = F[gm].std(axis=0) + 1e-12
        Fn[gm] = (F[gm] - mu) / sd
    return Fn


def run_loso(subjects, feature_set="recommended",
             per_subject_norm=True, verbose=True):
    """
    Leave-one-subject-out. Trains on N-1 subjects, tests on the held-out one.

    per_subject_norm: apply per-subject z-score so inter-subject amplitude/
    latency differences do not swamp the intensity signal (spec section 6).
    """
    # Consistency check: LOSO needs a shared feature space
    n_times = {s["X"].shape[2] for s in subjects}
    classes = {tuple(np.unique(s["y"]).tolist()) for s in subjects}
    if len(n_times) > 1:
        raise ValueError(f"LOSO needs equal epoch lengths across subjects, got {n_times}")
    if len(classes) > 1:
        raise ValueError(f"LOSO needs the same class set across subjects, got {classes}")

    F, y, groups, sids = _extract_all(subjects, feature_set)
    if per_subject_norm:
        F = _per_group_zscore(F, groups, None)

    logo = LeaveOneGroupOut()
    rows = []
    n_classes = len(np.unique(y))
    for tr, te in logo.split(F, y, groups):
        # Scaler + LDA fit on training subjects only
        scaler = StandardScaler().fit(F[tr])
        lda = LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")
        lda.fit(scaler.transform(F[tr]), y[tr])
        pred = lda.predict(scaler.transform(F[te]))
        held = int(groups[te][0])
        rows.append({
            "subject_id": sids[held],
            "acc": float((pred == y[te]).mean()),
            "bal": float(balanced_accuracy_score(y[te], pred)),
        })
        if verbose:
            r = rows[-1]
            print(f"  held-out {r['subject_id']:>10s}: acc={r['acc']*100:5.1f}%  "
                  f"bal={r['bal']*100:5.1f}%")
    accs = np.array([r["acc"] for r in rows])
    bals = np.array([r["bal"] for r in rows])
    return {
        "mode": "loso",
        "feature_set": feature_set,
        "per_subject_norm": per_subject_norm,
        "n_subjects": len(rows),
        "acc_mean": float(accs.mean()),
        "acc_std":  float(accs.std()),
        "bal_mean": float(bals.mean()),
        "chance":   1.0 / n_classes,
        "per_subject": rows,
    }


# ─────────────────────────────────────────────
# FINAL MODEL FIT (for deployment)
# ─────────────────────────────────────────────
def fit_final_model(subjects, feature_set="recommended"):
    """
    Fit one deployable pipeline on ALL trials of ALL subjects pooled.
    Returns the fitted Pipeline plus the feature names for interpretability.
    Use only after validation; this is the artifact you would ship.
    """
    ref_meta = subjects[0]["meta"]
    Xs = [s["X"] for s in subjects]; ys = [s["y"] for s in subjects]
    # All subjects must share epoch length to pool raw epochs
    if len({x.shape[2] for x in Xs}) > 1:
        raise ValueError("Cannot pool raw epochs of differing length for a single model.")
    X = np.concatenate(Xs); y = np.concatenate(ys)
    pipe = _make_pipeline(feature_set, ref_meta)
    pipe.fit(X, y)
    fx = pipe.named_steps["erp"]
    return pipe, fx.feature_names_


def lda_weight_report(pipe, feature_names, top_k=12):
    """
    Human-readable summary of the LDA's largest-magnitude weights, for the
    interpretability check in the spec (weights should match the predicted
    directions: amplitude up, latency down for higher intensity).
    """
    lda = pipe.named_steps["lda"]
    coef = lda.coef_                      # (n_classes, n_features) for multiclass
    lines = []
    classes = lda.classes_
    for ci, cls in enumerate(classes):
        w = coef[ci]
        order = np.argsort(np.abs(w))[::-1][:top_k]
        lines.append(f"Class {cls}: top weighted features")
        for j in order:
            lines.append(f"    {feature_names[j]:>22s}  {w[j]:+.3f}")
    return "\n".join(lines)
