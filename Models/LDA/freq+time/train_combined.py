"""
train_combined.py
=================
Training & validation for the combined (ERP + band-power) -> shrinkage-LDA
decoder. Same leakage-safe design as train_lda.py / train_bandpower.py:
within-subject repeated stratified k-fold and leave-one-subject-out.

Lets you compare, under identical folds:
    erp_only | bp_only | combined

so the question "does combining actually beat either alone?" gets an
apples-to-apples answer on your data (3-class or 4-class, auto-detected).

Run via run_combined.py, or import:
    from train_combined import load_dataset, compare_feature_modes
"""

from __future__ import annotations
import glob, os, warnings
import numpy as np

warnings.filterwarnings("ignore")

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import RepeatedStratifiedKFold, LeaveOneGroupOut
from sklearn.metrics import balanced_accuracy_score

from erp_features import load_npz_for_features, baseline_sd_outlier_mask
from combined_features import CombinedExtractor


# ─────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────
def load_dataset(folder, artifact_filter=True):
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
        subjects.append({"X": X, "y": y, "meta": meta, "subject_id": meta["subject_id"]})
    return subjects


# Feature "modes" -> CombinedExtractor kwargs
def _mode_kwargs(mode, erp_set, bp_channel_set, bp_relative):
    if mode == "erp_only":
        return dict(use_erp=True, use_bp=False, erp_set=erp_set)
    if mode == "bp_only":
        return dict(use_erp=False, use_bp=True,
                    bp_channel_set=bp_channel_set, bp_relative=bp_relative)
    if mode == "combined":
        return dict(use_erp=True, use_bp=True, erp_set=erp_set,
                    bp_channel_set=bp_channel_set, bp_relative=bp_relative)
    raise ValueError(f"Unknown mode '{mode}'")


def _pipe(mode, meta, erp_set, bp_channel_set, bp_relative):
    fx = CombinedExtractor(**_mode_kwargs(mode, erp_set, bp_channel_set, bp_relative)).set_meta(meta)
    return Pipeline([
        ("feat", fx),
        ("scale", StandardScaler()),
        ("lda", LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")),
    ])


# ─────────────────────────────────────────────
# WITHIN-SUBJECT
# ─────────────────────────────────────────────
def run_within_subject(subjects, mode="combined", erp_set="recommended",
                       bp_channel_set="all60", bp_relative=False,
                       n_splits=5, n_repeats=5, random_state=0, verbose=True):
    per_subject = []
    for s in subjects:
        X, y, meta = s["X"], s["y"], s["meta"]
        classes, counts = np.unique(y, return_counts=True)
        splits = min(n_splits, int(counts.min()))
        if splits < 2:
            continue
        cv = RepeatedStratifiedKFold(n_splits=splits, n_repeats=n_repeats,
                                     random_state=random_state)
        accs, bals = [], []
        for tr, te in cv.split(X, y):
            pipe = _pipe(mode, meta, erp_set, bp_channel_set, bp_relative)
            pipe.fit(X[tr], y[tr])
            pred = pipe.predict(X[te])
            accs.append((pred == y[te]).mean())
            bals.append(balanced_accuracy_score(y[te], pred))
        per_subject.append({
            "subject_id": s["subject_id"], "chance": 1.0 / len(classes),
            "acc_mean": float(np.mean(accs)), "acc_std": float(np.std(accs)),
            "bal_mean": float(np.mean(bals)),
        })
        if verbose:
            r = per_subject[-1]
            print(f"  {r['subject_id']:>10s}: acc={r['acc_mean']*100:5.1f}% "
                  f"+/-{r['acc_std']*100:4.1f}  bal={r['bal_mean']*100:5.1f}%")
    accs = np.array([p["acc_mean"] for p in per_subject])
    bals = np.array([p["bal_mean"] for p in per_subject])
    return {
        "mode": f"within/{mode}", "n_subjects": len(per_subject),
        "acc_mean": float(accs.mean()) if len(accs) else float("nan"),
        "acc_std": float(accs.std()) if len(accs) else float("nan"),
        "bal_mean": float(bals.mean()) if len(bals) else float("nan"),
        "chance": per_subject[0]["chance"] if per_subject else None,
        "per_subject": per_subject,
    }


# ─────────────────────────────────────────────
# LOSO
# ─────────────────────────────────────────────
def _extract_all(subjects, mode, erp_set, bp_channel_set, bp_relative):
    Fs, ys, groups = [], [], []
    for gi, s in enumerate(subjects):
        fx = CombinedExtractor(**_mode_kwargs(mode, erp_set, bp_channel_set, bp_relative)).set_meta(s["meta"])
        F = fx.fit_transform(s["X"])
        Fs.append(F); ys.append(s["y"]); groups.append(np.full(len(s["y"]), gi))
    return (np.concatenate(Fs), np.concatenate(ys), np.concatenate(groups),
            [s["subject_id"] for s in subjects])


def _per_group_zscore(F, groups):
    Fn = F.copy()
    for g in np.unique(groups):
        gm = groups == g
        mu = F[gm].mean(axis=0); sd = F[gm].std(axis=0) + 1e-12
        Fn[gm] = (F[gm] - mu) / sd
    return Fn


def run_loso(subjects, mode="combined", erp_set="recommended",
             bp_channel_set="all60", bp_relative=False,
             per_subject_norm=True, verbose=True):
    n_times = {s["X"].shape[2] for s in subjects}
    classes = {tuple(np.unique(s["y"]).tolist()) for s in subjects}
    if len(n_times) > 1:
        raise ValueError(f"LOSO needs equal epoch lengths, got {n_times}")
    if len(classes) > 1:
        raise ValueError(f"LOSO needs the same class set, got {classes}")

    F, y, groups, sids = _extract_all(subjects, mode, erp_set, bp_channel_set, bp_relative)
    if per_subject_norm:
        F = _per_group_zscore(F, groups)
    logo = LeaveOneGroupOut()
    rows = []
    n_classes = len(np.unique(y))
    for tr, te in logo.split(F, y, groups):
        scaler = StandardScaler().fit(F[tr])
        lda = LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")
        lda.fit(scaler.transform(F[tr]), y[tr])
        pred = lda.predict(scaler.transform(F[te]))
        held = int(groups[te][0])
        rows.append({"subject_id": sids[held],
                     "acc": float((pred == y[te]).mean()),
                     "bal": float(balanced_accuracy_score(y[te], pred))})
        if verbose:
            r = rows[-1]
            print(f"  held-out {r['subject_id']:>10s}: acc={r['acc']*100:5.1f}%  "
                  f"bal={r['bal']*100:5.1f}%")
    accs = np.array([r["acc"] for r in rows]); bals = np.array([r["bal"] for r in rows])
    return {
        "mode": f"loso/{mode}", "per_subject_norm": per_subject_norm,
        "n_subjects": len(rows),
        "acc_mean": float(accs.mean()), "acc_std": float(accs.std()),
        "bal_mean": float(bals.mean()), "chance": 1.0 / n_classes,
        "per_subject": rows,
    }


# ─────────────────────────────────────────────
# COMPARISON: erp_only vs bp_only vs combined
# ─────────────────────────────────────────────
def compare_feature_modes(subjects, modes=("erp_only", "bp_only", "combined"),
                          validation=("within", "loso"),
                          erp_set="recommended", bp_channel_set="all60",
                          bp_relative=False, n_splits=5, n_repeats=5):
    out = {}
    for mode in modes:
        out[mode] = {}
        print(f"\n{'#'*60}\n# FEATURE MODE: {mode}"
              f"  (erp_set={erp_set}, bp_channels={bp_channel_set})\n{'#'*60}")
        if "within" in validation:
            print(f"\n--- within-subject ({mode}) ---")
            r = run_within_subject(subjects, mode=mode, erp_set=erp_set,
                                   bp_channel_set=bp_channel_set, bp_relative=bp_relative,
                                   n_splits=n_splits, n_repeats=n_repeats, verbose=True)
            out[mode]["within"] = r
            print(f"  POOLED within: acc={r['acc_mean']*100:.1f}% +/-{r['acc_std']*100:.1f} "
                  f"| bal={r['bal_mean']*100:.1f}% | chance={r['chance']*100:.0f}%")
        if "loso" in validation:
            print(f"\n--- LOSO ({mode}) ---")
            try:
                r = run_loso(subjects, mode=mode, erp_set=erp_set,
                             bp_channel_set=bp_channel_set, bp_relative=bp_relative, verbose=True)
                out[mode]["loso"] = r
                print(f"  POOLED LOSO: acc={r['acc_mean']*100:.1f}% +/-{r['acc_std']*100:.1f} "
                      f"| bal={r['bal_mean']*100:.1f}% | chance={r['chance']*100:.0f}%")
            except ValueError as e:
                print(f"  [LOSO skipped] {e}")
                out[mode]["loso"] = None
    return out


def summary_table(results):
    lines = [f"{'feature_mode':>14s} {'within':>10s} {'loso':>10s} {'chance':>8s}"]
    for mode, d in results.items():
        w = d.get("within"); l = d.get("loso")
        wv = f"{w['acc_mean']*100:.1f}%" if w else "-"
        lv = f"{l['acc_mean']*100:.1f}%" if l else "-"
        ch = f"{(w or l)['chance']*100:.0f}%" if (w or l) else "-"
        lines.append(f"{mode:>14s} {wv:>10s} {lv:>10s} {ch:>8s}")
    return "\n".join(lines)
