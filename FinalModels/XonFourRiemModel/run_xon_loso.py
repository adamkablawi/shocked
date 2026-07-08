"""
run_xon_loso.py
===============
LOSO accuracy of the FINAL MODEL architecture (4-family per-family-LDA stacking
ensemble) restricted to a 7-electrode montage:

        F3, F4, C3, Cz, C4, P3, P4      ("XON" channels)

Goal: keep as much decoding fidelity as possible with only 7 electrodes. The
architecture is IDENTICAL to the 60-channel final model — the only change is
that every feature family is computed on the 7 channels instead of all 60:

    erp  : ERP/SEP features on the 7 channels
    bp   : Welch band-power on the 7 channels        (5 bands x 7  = 35)
    tf   : ERD/ERS on the 7 channels                 (4 x 5 x 7   = 140)
    riem : covariance / tangent-space on 7 channels  (7*8/2       = 28)

The meta-learner then re-weights these (much smaller) families automatically,
so no manual tuning is needed to preserve fidelity.

This script ONLY runs leave-one-subject-out (LOSO) to report accuracy — it does
NOT fit or save a deployable model. Extraction and the 29 LOSO folds run in
parallel (path-based loading, so nothing large hits the disk).

Run from the repo root:
    PYTHONPATH=XonModel python XonModel/run_xon_loso.py [--jobs 4]
"""
from __future__ import annotations
import os, json, argparse, time, glob
import numpy as np
from joblib import Parallel, delayed

from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import LeaveOneGroupOut, GroupKFold
from sklearn.metrics import balanced_accuracy_score, confusion_matrix

from train_combined import ModularFeatureExtractor

HERE = os.path.dirname(os.path.abspath(__file__))
XON = ["F3", "F4", "C3", "Cz", "C4", "P3", "P4"]

CONFIG = {
    "data_folder": "data/og-ds-t-3c",
    "families":    ["erp", "bp", "tf", "riem"],
    "feature_opts": {
        "erp":  {"feature_set": "full", "channels": XON},
        "bp":   {"channel_set": "custom", "channels": XON},
        "tf":   {"channel_set": "custom", "channels": XON},
        "riem": {"channel_set": "custom", "channels": XON},
    },
    "inner_splits":     5,
    "meta_C":           1.0,
    "artifact_filter":  True,
    "per_subject_norm": True,
    "stats_path": os.path.join(HERE, "xon_loso_stats.json"),
}


def base_model():
    return make_pipeline(StandardScaler(),
                         LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto"))


def _aligned_proba(model, F, classes):
    proba = model.predict_proba(F)
    out = np.zeros((F.shape[0], len(classes)))
    lda = model.named_steps["lineardiscriminantanalysis"]
    for j, c in enumerate(lda.classes_):
        out[:, list(classes).index(c)] = proba[:, j]
    return out


def _oof(F, y, groups, classes, n_splits):
    oof = np.zeros((len(y), len(classes)))
    gkf = GroupKFold(n_splits=min(n_splits, len(np.unique(groups))))
    for tr, va in gkf.split(F, y, groups):
        m = base_model().fit(F[tr], y[tr])
        oof[va] = _aligned_proba(m, F[va], classes)
    return oof


# ── path-based parallel extraction (disk-safe) ──
def _extract_from_path(path, families, feature_opts, artifact_filter):
    from features.erp_features import load_npz_for_features, baseline_sd_outlier_mask
    X, y, meta = load_npz_for_features(path)
    if artifact_filter:
        keep = baseline_sd_outlier_mask(X, meta)
        X, y = X[keep], y[keep]
    out = {f: ModularFeatureExtractor([f], feature_opts).set_meta(meta).fit_transform(X)
           for f in families}
    cn = [str(c) for c in meta["class_names"]] if meta.get("class_names") is not None else None
    return out, y, str(meta["subject_id"]), cn


def extract_parallel(files, families, feature_opts, artifact_filter, n_jobs):
    t0 = time.time()
    res = Parallel(n_jobs=n_jobs, verbose=5, max_nbytes=None)(
        delayed(_extract_from_path)(p, families, feature_opts, artifact_filter) for p in files)
    mats = {f: np.concatenate([r[0][f] for r in res]) for f in families}
    y = np.concatenate([r[1] for r in res])
    groups = np.concatenate([np.full(len(r[1]), gi) for gi, r in enumerate(res)])
    cn = next((r[3] for r in res if r[3]), None)
    print(f"  extraction {time.time()-t0:.1f}s | "
          f"{', '.join(f'{f}:{mats[f].shape[1]}' for f in families)} "
          f"(total {sum(m.shape[1] for m in mats.values())} features on {len(XON)} channels)")
    return mats, y, groups, cn


def per_subject_zscore(mats, groups):
    out = {}
    for f, F in mats.items():
        Z = F.copy()
        for g in np.unique(groups):
            gm = groups == g
            Z[gm] = (F[gm] - F[gm].mean(0)) / (F[gm].std(0) + 1e-12)
        out[f] = Z
    return out


def _loso_fold(tr, te, mats, y, groups, families, classes, inner_splits, meta_C):
    y_tr, y_te = y[tr], y[te]
    meta_tr, meta_te, w_blocks = [], [], []
    for f in families:
        F_tr, F_te = mats[f][tr], mats[f][te]
        meta_tr.append(_oof(F_tr, y_tr, groups[tr], classes, inner_splits))
        meta_te.append(_aligned_proba(base_model().fit(F_tr, y_tr), F_te, classes))
    meta = LogisticRegression(max_iter=1000, C=meta_C).fit(np.hstack(meta_tr), y_tr)
    pred = meta.predict(np.hstack(meta_te))
    coef = np.abs(meta.coef_).reshape(meta.coef_.shape[0], len(families), len(classes)).sum(axis=(0, 2))
    return (float((pred == y_te).mean()), float(balanced_accuracy_score(y_te, pred)),
            confusion_matrix(y_te, pred, labels=classes), coef / (coef.sum() + 1e-12))


def main(cfg=CONFIG, n_jobs=4):
    files = sorted(glob.glob(os.path.join(cfg["data_folder"], "*.npz")))
    if not files:
        raise FileNotFoundError(f"No .npz files in {cfg['data_folder']}")
    fams = cfg["families"]
    print(f"XON 7-channel stack | {len(files)} subjects | channels {XON} | n_jobs={n_jobs}")

    print("\n[1/2] Parallel feature extraction ...")
    raw, y, groups, class_names = extract_parallel(
        files, fams, cfg["feature_opts"], cfg["artifact_filter"], n_jobs)
    classes = np.unique(y)
    if class_names is None:
        class_names = [str(c) for c in classes]
    mats = per_subject_zscore(raw, groups) if cfg["per_subject_norm"] else raw
    print(f"  classes {class_names} | dist {dict(zip(*np.unique(y, return_counts=True)))}")

    print("\n[2/2] Parallel LOSO ...")
    logo = LeaveOneGroupOut()
    folds = list(logo.split(mats[fams[0]], y, groups))
    t0 = time.time()
    res = Parallel(n_jobs=n_jobs, verbose=5)(
        delayed(_loso_fold)(tr, te, mats, y, groups, fams, classes,
                            cfg["inner_splits"], cfg["meta_C"]) for tr, te in folds)
    accs = np.array([r[0] for r in res]); bals = np.array([r[1] for r in res])
    cm = sum(r[2] for r in res); wmean = np.mean([r[3] for r in res], axis=0)
    recall = (cm.diagonal() / np.maximum(cm.sum(1), 1)).tolist()
    print(f"  LOSO ({len(folds)} folds) in {time.time()-t0:.1f}s")

    out = {"montage": XON, "n_channels": len(XON), "data": cfg["data_folder"],
           "class_names": class_names, "n_classes": len(classes),
           "acc_mean": float(accs.mean()), "acc_std": float(accs.std()),
           "bal_mean": float(bals.mean()), "bal_std": float(bals.std()),
           "chance": 1.0 / len(classes),
           "per_class_recall": recall, "confusion": cm.tolist(),
           "meta_family_weights": {f: float(wmean[i]) for i, f in enumerate(fams)},
           "n_features_per_family": {f: int(mats[f].shape[1]) for f in fams}}
    json.dump(out, open(cfg["stats_path"], "w"), indent=2)

    print("\n" + "=" * 52)
    print(f"XON 7-CHANNEL STACK — LOSO ({len(classes)}-class, chance {100/len(classes):.0f}%)")
    print("=" * 52)
    print(f"  accuracy         : {accs.mean()*100:.1f}% +/- {accs.std()*100:.1f}")
    print(f"  balanced accuracy: {bals.mean()*100:.1f}% +/- {bals.std()*100:.1f}")
    print(f"  per-class recall : {dict(zip(class_names, np.round(recall,3)))}")
    print(f"  meta weights     : {{ {', '.join(f'{f}: {wmean[i]:.2f}' for i,f in enumerate(fams))} }}")
    print(f"\nSaved stats -> {cfg['stats_path']}  (no model weights produced, as requested)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--jobs", type=int, default=4)
    main(n_jobs=ap.parse_args().jobs)
