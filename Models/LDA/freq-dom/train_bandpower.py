"""
train_bandpower.py
==================
Training & validation for the band-power -> shrinkage-LDA decoder, reconstructing
the spectral pipeline that achieved the higher multi-class accuracy.

Same validation design as train_lda.py (leakage-safe within-subject repeated
k-fold and LOSO), but using BandPowerExtractor. Adds a channel-set comparison
(all60 / sensorimotor / central_fc) so you can see which spatial coverage drives
accuracy.

Run as a script: edit CONFIG at the bottom and `python train_bandpower.py`.
Or import: from train_bandpower import compare_channel_sets, load_dataset
"""

from __future__ import annotations
import glob, os, json, warnings
import numpy as np

warnings.filterwarnings("ignore")

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import RepeatedStratifiedKFold, LeaveOneGroupOut
from sklearn.metrics import balanced_accuracy_score

from erp_features import load_npz_for_features, baseline_sd_outlier_mask
from bandpower_features import BandPowerExtractor


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


def _pipe(channel_set, meta, relative=False):
    fx = BandPowerExtractor(channel_set=channel_set, relative=relative).set_meta(meta)
    return Pipeline([
        ("bp", fx),
        ("scale", StandardScaler()),
        ("lda", LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")),
    ])


# ─────────────────────────────────────────────
# WITHIN-SUBJECT
# ─────────────────────────────────────────────
def run_within_subject(subjects, channel_set="all60", relative=False,
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
            pipe = _pipe(channel_set, meta, relative)
            pipe.fit(X[tr], y[tr])
            pred = pipe.predict(X[te])
            accs.append((pred == y[te]).mean())
            bals.append(balanced_accuracy_score(y[te], pred))
        per_subject.append({
            "subject_id": s["subject_id"],
            "chance": 1.0 / len(classes),
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
        "mode": "within_subject", "channel_set": channel_set, "relative": relative,
        "n_subjects": len(per_subject),
        "acc_mean": float(accs.mean()) if len(accs) else float("nan"),
        "acc_std": float(accs.std()) if len(accs) else float("nan"),
        "bal_mean": float(bals.mean()) if len(bals) else float("nan"),
        "chance": per_subject[0]["chance"] if per_subject else None,
        "per_subject": per_subject,
    }


# ─────────────────────────────────────────────
# LOSO
# ─────────────────────────────────────────────
def _extract_all(subjects, channel_set, relative):
    Fs, ys, groups = [], [], []
    for gi, s in enumerate(subjects):
        fx = BandPowerExtractor(channel_set=channel_set, relative=relative).set_meta(s["meta"])
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


def run_loso(subjects, channel_set="all60", relative=False,
             per_subject_norm=True, verbose=True):
    n_times = {s["X"].shape[2] for s in subjects}
    classes = {tuple(np.unique(s["y"]).tolist()) for s in subjects}
    if len(n_times) > 1:
        raise ValueError(f"LOSO needs equal epoch lengths, got {n_times}")
    if len(classes) > 1:
        raise ValueError(f"LOSO needs the same class set, got {classes}")

    F, y, groups, sids = _extract_all(subjects, channel_set, relative)
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
        "mode": "loso", "channel_set": channel_set, "relative": relative,
        "per_subject_norm": per_subject_norm, "n_subjects": len(rows),
        "acc_mean": float(accs.mean()), "acc_std": float(accs.std()),
        "bal_mean": float(bals.mean()), "chance": 1.0 / n_classes,
        "per_subject": rows,
    }


# ─────────────────────────────────────────────
# CHANNEL-SET COMPARISON
# ─────────────────────────────────────────────
def compare_channel_sets(subjects, channel_sets=("all60", "sensorimotor", "central_fc"),
                         modes=("within", "loso"), relative=False,
                         n_splits=5, n_repeats=5):
    """Run within and/or LOSO for each channel set and return a results table."""
    out = {}
    for cs in channel_sets:
        out[cs] = {}
        print(f"\n{'#'*60}\n# CHANNEL SET: {cs}\n{'#'*60}")
        if "within" in modes:
            print(f"\n--- within-subject ({cs}) ---")
            out[cs]["within"] = run_within_subject(
                subjects, channel_set=cs, relative=relative,
                n_splits=n_splits, n_repeats=n_repeats, verbose=True)
            r = out[cs]["within"]
            print(f"  POOLED within: acc={r['acc_mean']*100:.1f}% "
                  f"+/-{r['acc_std']*100:.1f} | bal={r['bal_mean']*100:.1f}% "
                  f"| chance={r['chance']*100:.0f}%")
        if "loso" in modes:
            print(f"\n--- LOSO ({cs}) ---")
            try:
                out[cs]["loso"] = run_loso(subjects, channel_set=cs,
                                           relative=relative, verbose=True)
                r = out[cs]["loso"]
                print(f"  POOLED LOSO: acc={r['acc_mean']*100:.1f}% "
                      f"+/-{r['acc_std']*100:.1f} | bal={r['bal_mean']*100:.1f}% "
                      f"| chance={r['chance']*100:.0f}%")
            except ValueError as e:
                print(f"  [LOSO skipped] {e}")
                out[cs]["loso"] = None
    return out


def summary_table(results):
    """Compact text table of pooled accuracy per channel set & mode."""
    lines = [f"{'channel_set':>14s} {'within':>10s} {'loso':>10s} {'chance':>8s}"]
    for cs, d in results.items():
        w = d.get("within"); l = d.get("loso")
        wv = f"{w['acc_mean']*100:.1f}%" if w else "-"
        lv = f"{l['acc_mean']*100:.1f}%" if l else "-"
        ch = f"{(w or l)['chance']*100:.0f}%" if (w or l) else "-"
        lines.append(f"{cs:>14s} {wv:>10s} {lv:>10s} {ch:>8s}")
    return "\n".join(lines)
