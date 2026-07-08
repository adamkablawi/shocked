"""
train_final_model.py
====================
Trains and saves the PROJECT'S FINAL MODEL: the 4-family per-family-LDA stacking
ensemble (erp + bp + tf + riem, fused by a logistic meta-learner) — the best
decoder found (3-class intensity: no_stim / medium / max).

What it does
------------
  1. Loads data/og-ds-t-3c and extracts the four feature families PER SUBJECT,
     IN PARALLEL across subjects (joblib) — feature extraction (esp. the
     Riemannian tangent-space and ERD/ERS families) is the run-time bottleneck,
     so this is where parallelism pays off.
  2. Fits the deployable stack on ALL subjects:
        - one shrinkage-LDA (StandardScaler + LDA) per family,
        - a logistic meta-learner trained on leakage-safe out-of-fold base
          probabilities.
  3. Estimates generalisation with leave-one-subject-out (LOSO), the 29 folds
     run IN PARALLEL.
  4. **Saves the trained model + all weights to THIS directory**:
        FinalModel/final_stacking_ensemble.joblib   (fitted base pipelines + meta)
        FinalModel/model_card.json                  (config + LOSO metrics)

The saved .joblib is self-describing (families, feature_opts, class names, the
per-subject-normalisation note) so it can be reloaded for inference on new epochs.

Run from the repo root:
    PYTHONPATH=FinalModel python FinalModel/train_final_model.py [--jobs N]
"""
from __future__ import annotations
import os, json, argparse, time
import numpy as np
import joblib
from joblib import Parallel, delayed

from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import LeaveOneGroupOut, GroupKFold
from sklearn.metrics import balanced_accuracy_score, confusion_matrix

from train_combined import load_dataset, ModularFeatureExtractor

HERE = os.path.dirname(os.path.abspath(__file__))

CONFIG = {
    "data_folder": "data/og-ds-t-3c",
    "families":    ["erp", "bp", "tf", "riem"],
    "feature_opts": {
        "erp":  {"feature_set": "full"},
        "bp":   {"channel_set": "all60"},
        "tf":   {"channel_set": "all60"},
        "riem": {"channel_set": "all60"},
    },
    "inner_splits":     5,
    "meta_C":           1.0,
    "artifact_filter":  True,
    "per_subject_norm": True,
    "model_path":  os.path.join(HERE, "final_stacking_ensemble.joblib"),
    "card_path":   os.path.join(HERE, "model_card.json"),
}


# ── base / meta ──
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


# ── parallel feature extraction (the bottleneck) ──
# Each worker LOADS ITS OWN .npz (only a path is pickled), so the large raw EEG
# arrays are never written to temp / shipped between processes — important on a
# nearly-full disk.
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
    results = Parallel(n_jobs=n_jobs, verbose=5, max_nbytes=None)(
        delayed(_extract_from_path)(p, families, feature_opts, artifact_filter) for p in files)
    mats = {f: np.concatenate([r[0][f] for r in results]) for f in families}
    y = np.concatenate([r[1] for r in results])
    groups = np.concatenate([np.full(len(r[1]), gi) for gi, r in enumerate(results)])
    sids = [r[2] for r in results]
    class_names = next((r[3] for r in results if r[3]), None)
    print(f"  extraction done in {time.time()-t0:.1f}s "
          f"({', '.join(f'{f}:{mats[f].shape[1]}' for f in families)} features)")
    return mats, y, groups, sids, class_names


def per_subject_zscore(mats, groups):
    out = {}
    for f, F in mats.items():
        Z = F.copy()
        for g in np.unique(groups):
            gm = groups == g
            Z[gm] = (F[gm] - F[gm].mean(0)) / (F[gm].std(0) + 1e-12)
        out[f] = Z
    return out


# ── fit the deployable stack on ALL data ──
def fit_final_stack(mats, y, groups, families, classes, inner_splits, meta_C):
    base_fitted = {f: base_model().fit(mats[f], y) for f in families}
    meta_tr = [_oof(mats[f], y, groups, classes, inner_splits) for f in families]
    meta = LogisticRegression(max_iter=1000, C=meta_C).fit(np.hstack(meta_tr), y)
    fam_w = {}
    coef = np.abs(meta.coef_).reshape(meta.coef_.shape[0], len(families), len(classes)).sum(axis=(0, 2))
    tot = coef.sum() + 1e-12
    for i, f in enumerate(families):
        fam_w[f] = float(coef[i] / tot)
    return base_fitted, meta, fam_w


# ── one LOSO fold (run in parallel) ──
def _loso_fold(tr, te, mats, y, groups, families, classes, inner_splits, meta_C):
    y_tr, y_te = y[tr], y[te]
    meta_tr, meta_te = [], []
    for f in families:
        F_tr, F_te = mats[f][tr], mats[f][te]
        meta_tr.append(_oof(F_tr, y_tr, groups[tr], classes, inner_splits))
        meta_te.append(_aligned_proba(base_model().fit(F_tr, y_tr), F_te, classes))
    meta = LogisticRegression(max_iter=1000, C=meta_C).fit(np.hstack(meta_tr), y_tr)
    pred = meta.predict(np.hstack(meta_te))
    return (float((pred == y_te).mean()), float(balanced_accuracy_score(y_te, pred)),
            confusion_matrix(y_te, pred, labels=classes))


def loso_eval(mats, y, groups, families, classes, inner_splits, meta_C, n_jobs):
    logo = LeaveOneGroupOut()
    folds = list(logo.split(mats[families[0]], y, groups))
    t0 = time.time()
    res = Parallel(n_jobs=n_jobs, verbose=5)(
        delayed(_loso_fold)(tr, te, mats, y, groups, families, classes, inner_splits, meta_C)
        for tr, te in folds)
    accs = np.array([r[0] for r in res]); bals = np.array([r[1] for r in res])
    cm = sum(r[2] for r in res)
    print(f"  LOSO ({len(folds)} folds) done in {time.time()-t0:.1f}s")
    return {"acc_mean": float(accs.mean()), "acc_std": float(accs.std()),
            "bal_mean": float(bals.mean()), "bal_std": float(bals.std()),
            "per_class_recall": (cm.diagonal() / np.maximum(cm.sum(1), 1)).tolist(),
            "confusion": cm.tolist()}


def main(cfg=CONFIG, n_jobs=-1):
    import glob
    files = sorted(glob.glob(os.path.join(cfg["data_folder"], "*.npz")))
    if not files:
        raise FileNotFoundError(f"No .npz files in {cfg['data_folder']}")
    fams = cfg["families"]
    print(f"FINAL MODEL: 4-family stack | {len(files)} subjects | n_jobs={n_jobs}")

    print("\n[1/3] Parallel feature extraction ...")
    raw, y, groups, sids, class_names = extract_parallel(
        files, fams, cfg["feature_opts"], cfg["artifact_filter"], n_jobs)
    classes = np.unique(y)
    if class_names is None:
        class_names = [str(c) for c in classes]
    print(f"  classes {class_names} | pooled dist {dict(zip(*np.unique(y, return_counts=True)))}")
    mats = per_subject_zscore(raw, groups) if cfg["per_subject_norm"] else raw

    print("\n[2/3] Fitting deployable stack on ALL subjects ...")
    base_fitted, meta, fam_w = fit_final_stack(mats, y, groups, fams, classes,
                                               cfg["inner_splits"], cfg["meta_C"])
    print(f"  meta-learner family weights: {{ {', '.join(f'{f}: {fam_w[f]:.2f}' for f in fams)} }}")

    print("\n[3/3] Parallel LOSO generalisation estimate ...")
    loso = loso_eval(mats, y, groups, fams, classes, cfg["inner_splits"], cfg["meta_C"], n_jobs)
    print(f"  LOSO: acc={loso['acc_mean']*100:.1f}%  bal={loso['bal_mean']*100:.1f}%  "
          f"recall={dict(zip(class_names, np.round(loso['per_class_recall'],3)))}")

    # ── SAVE the final model + weights to THIS directory ──
    artifact = {
        "model_type": "per-family LDA stacking ensemble",
        "families": fams, "feature_opts": cfg["feature_opts"],
        "classes": classes.tolist(), "class_names": class_names,
        "base_models": base_fitted,          # fitted StandardScaler+LDA per family
        "meta_learner": meta,                # fitted logistic meta-learner
        "meta_family_weights": fam_w,
        "per_subject_norm": cfg["per_subject_norm"],
        "note": ("Inference: extract the same 4 families per epoch, per-subject "
                 "z-score, get each base model's predict_proba, hstack in `families` "
                 "order, then meta_learner.predict."),
    }
    joblib.dump(artifact, cfg["model_path"])
    card = {"model": "final_stacking_ensemble", "data": cfg["data_folder"],
            "families": fams, "class_names": class_names,
            "meta_family_weights": fam_w, "loso": loso,
            "saved_to": cfg["model_path"]}
    json.dump(card, open(cfg["card_path"], "w"), indent=2)

    print(f"\nSAVED final model -> {cfg['model_path']}")
    print(f"      model card  -> {cfg['card_path']}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=-1, help="parallel workers (-1 = all cores)")
    args = ap.parse_args()
    main(n_jobs=args.jobs)
