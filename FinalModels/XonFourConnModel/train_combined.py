"""
train_combined.py
=================
Modular feature -> shrinkage-LDA training & validation. Replaces the old fixed
ERP+band-power CombinedExtractor with a config-driven feature union: you pick
ANY set of feature families per run, with per-family options.

A "feature family" is any sklearn-compatible extractor registered in
FEATURE_REGISTRY. Out of the box: "erp", "bp" (and "tf" if tf_features.py is
present). Add your own by registering its class.

The runner (run_combined.py) supplies, via CONFIG:
    feature_sets : { label -> [family, ...] }    e.g. {"combined": ["erp","bp"]}
    feature_opts : { family -> {kwargs} }         e.g. {"bp": {"channel_set":"all60"}}

Validation is leakage-safe: within-subject repeated stratified k-fold and LOSO
with per-subject z-scoring. Works on 3- or 4-class data (auto-detected).

Import:
    from train_combined import load_dataset, compare_feature_modes, summary_table
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

try:
    from sklearn.base import BaseEstimator, TransformerMixin
except Exception:
    class BaseEstimator: ...
    class TransformerMixin: ...

from features.erp_features import (load_npz_for_features, baseline_sd_outlier_mask,
                          ERPFeatureExtractor)
from features.bandpower_features import BandPowerExtractor
from features.tf_features import TFExtractor
from features.riemann_features import RiemannTangentExtractor
from features.conn_features import ConnFeatureExtractor

# ─────────────────────────────────────────────
# FEATURE REGISTRY  (name -> extractor class)
# Add a new family by registering its sklearn-compatible extractor here.
# Each extractor must support: __init__(**opts), set_meta(meta), fit(X, y),
# transform(X), and expose .feature_names_.
# ─────────────────────────────────────────────
FEATURE_REGISTRY = {
    "erp":  ERPFeatureExtractor,
    "bp":   BandPowerExtractor,
    "tf":   TFExtractor,
    "riem": RiemannTangentExtractor,
    "conn": ConnFeatureExtractor,
}


class ModularFeatureExtractor(BaseEstimator, TransformerMixin):
    """
    Concatenate any set of registered feature families into one vector.

    Parameters
    ----------
    families : list[str]
        Names from FEATURE_REGISTRY, e.g. ["erp", "bp"].
    feature_opts : dict[str, dict]
        Per-family constructor kwargs, e.g. {"bp": {"channel_set": "all60"}}.
        Keys must match the extractor's __init__ params.

    Feature names are prefixed with the family ("erp:", "bp:", ...) so the
    combined vector stays interpretable.
    """

    def __init__(self, families, feature_opts=None):
        self.families = families
        self.feature_opts = feature_opts or {}
        self._meta = None

    def set_meta(self, meta):
        self._meta = meta
        return self

    def fit(self, X, y=None, meta=None):
        m = meta if meta is not None else self._meta
        if m is None:
            raise ValueError("meta must be provided (channel_names, sfreq, times).")
        if not self.families:
            raise ValueError("families is empty; specify at least one feature family.")
        self.extractors_, names = [], []
        for fam in self.families:
            if fam not in FEATURE_REGISTRY:
                raise ValueError(f"Unknown feature family '{fam}'. "
                                 f"Registered: {list(FEATURE_REGISTRY)}")
            opts = self.feature_opts.get(fam, {})
            ex = FEATURE_REGISTRY[fam](**opts).set_meta(m)
            ex.fit(X, y)
            self.extractors_.append((fam, ex))
            names += [f"{fam}:{n}" for n in ex.feature_names_]
        self.feature_names_ = names
        return self

    def transform(self, X, meta=None):
        if not hasattr(self, "extractors_"):
            raise RuntimeError("Call fit before transform.")
        return np.concatenate([ex.transform(X) for _, ex in self.extractors_], axis=1)


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


def _pipe(families, feature_opts, meta):
    fx = ModularFeatureExtractor(families, feature_opts).set_meta(meta)
    return Pipeline([
        ("feat", fx),
        ("scale", StandardScaler()),
        ("lda", LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")),
    ])


# ─────────────────────────────────────────────
# WITHIN-SUBJECT
# ─────────────────────────────────────────────
def run_within_subject(subjects, families, feature_opts=None, label=None,
                       n_splits=5, n_repeats=5, random_state=0, verbose=True):
    label = label or "+".join(families)
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
            pipe = _pipe(families, feature_opts, meta)
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
        "mode": f"within/{label}", "families": list(families),
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
def _extract_all(subjects, families, feature_opts):
    Fs, ys, groups = [], [], []
    for gi, s in enumerate(subjects):
        fx = ModularFeatureExtractor(families, feature_opts).set_meta(s["meta"])
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


def run_loso(subjects, families, feature_opts=None, label=None,
             per_subject_norm=True, verbose=True):
    label = label or "+".join(families)
    n_times = {s["X"].shape[2] for s in subjects}
    classes = {tuple(np.unique(s["y"]).tolist()) for s in subjects}
    if len(n_times) > 1:
        raise ValueError(f"LOSO needs equal epoch lengths, got {n_times}")
    if len(classes) > 1:
        raise ValueError(f"LOSO needs the same class set, got {classes}")

    F, y, groups, sids = _extract_all(subjects, families, feature_opts)
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
        "mode": f"loso/{label}", "families": list(families),
        "per_subject_norm": per_subject_norm, "n_subjects": len(rows),
        "acc_mean": float(accs.mean()), "acc_std": float(accs.std()),
        "bal_mean": float(bals.mean()), "chance": 1.0 / n_classes,
        "per_subject": rows,
    }


# ─────────────────────────────────────────────
# COMPARISON across named feature sets
# ─────────────────────────────────────────────
def compare_feature_modes(subjects, feature_sets, feature_opts=None,
                          validation=("within", "loso"),
                          n_splits=5, n_repeats=5, per_subject_norm=True):
    """
    feature_sets : { label -> [family, ...] }, e.g.
                   {"erp_only": ["erp"], "combined": ["erp", "bp"]}
    feature_opts : { family -> {kwargs} }
    """
    out = {}
    for label, families in feature_sets.items():
        out[label] = {}
        print(f"\n{'#'*60}\n# FEATURE SET: {label}  ({'+'.join(families)})\n{'#'*60}")
        if "within" in validation:
            print(f"\n--- within-subject ({label}) ---")
            r = run_within_subject(subjects, families, feature_opts, label,
                                   n_splits=n_splits, n_repeats=n_repeats, verbose=True)
            out[label]["within"] = r
            print(f"  POOLED within: acc={r['acc_mean']*100:.1f}% +/-{r['acc_std']*100:.1f} "
                  f"| bal={r['bal_mean']*100:.1f}% | chance={r['chance']*100:.0f}%")
        if "loso" in validation:
            print(f"\n--- LOSO ({label}) ---")
            try:
                r = run_loso(subjects, families, feature_opts, label,
                             per_subject_norm=per_subject_norm, verbose=True)
                out[label]["loso"] = r
                print(f"  POOLED LOSO: acc={r['acc_mean']*100:.1f}% +/-{r['acc_std']*100:.1f} "
                      f"| bal={r['bal_mean']*100:.1f}% | chance={r['chance']*100:.0f}%")
            except ValueError as e:
                print(f"  [LOSO skipped] {e}")
                out[label]["loso"] = None
    return out


def summary_table(results):
    lines = [f"{'feature_set':>14s} {'within':>10s} {'loso':>10s} {'chance':>8s}"]
    for label, d in results.items():
        w = d.get("within"); l = d.get("loso")
        wv = f"{w['acc_mean']*100:.1f}%" if w else "-"
        lv = f"{l['acc_mean']*100:.1f}%" if l else "-"
        ch = f"{(w or l)['chance']*100:.0f}%" if (w or l) else "-"
        lines.append(f"{label:>14s} {wv:>10s} {lv:>10s} {ch:>8s}")
    return "\n".join(lines)