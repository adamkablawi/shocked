"""
stacking_xon.py  (CONNECTIVITY variant)
=======================================
Standard within-subject + LOSO validation of the 4-family stacking ensemble
restricted to the 7-electrode XON montage:  F3, F4, C3, Cz, C4, P3, P4.

Identical architecture and protocol to XonModel, but the 4th family is
CONNECTIVITY (`conn`, phase-based PLV/iPLV between Frontal / Central / Parietal
regions) INSTEAD of Riemannian covariance. On 7 electrodes the regions are:
    F = F3, F4    C = C3, Cz, C4    P = P3, P4
so `conn` measures inter-region phase coupling among the XON channels — one
shrinkage-LDA per family (erp, bp, tf, conn) fused by a logistic meta-learner.

Validation (same as the rest of the project):
  within : per-subject RepeatedStratifiedKFold (5 x 5); inner StratifiedKFold
           over the subject's own trials builds the OOF meta-features.
  loso   : leave-one-subject-out, per-subject z-scored then pooled; inner
           GroupKFold over the TRAIN subjects builds the OOF meta-features.

Both are leakage-safe. Extraction + both validation loops run in parallel
(path-based loading, disk-safe). Reports acc / balanced acc / per-class recall /
confusion / meta-weights. Saves stats only (no model weights).

Run from repo root:
    PYTHONPATH=XonModel python XonModel/stacking_xon.py [--jobs 4]
"""
from __future__ import annotations
import os, json, argparse, time, glob
import numpy as np
from joblib import Parallel, delayed

from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import (LeaveOneGroupOut, GroupKFold,
                                     StratifiedKFold, RepeatedStratifiedKFold)
from sklearn.metrics import balanced_accuracy_score, confusion_matrix

from train_combined import ModularFeatureExtractor

HERE = os.path.dirname(os.path.abspath(__file__))
XON = ["F3", "F4", "C3", "Cz", "C4", "P3", "P4"]
# XON channels grouped into regions for the connectivity family:
XON_REGIONS = {"F": ["F3", "F4"], "C": ["C3", "Cz", "C4"], "P": ["P3", "P4"]}
XON_PAIRS = [("F", "C"), ("F", "P"), ("C", "P"), ("F", "F"), ("C", "C"), ("P", "P")]

CONFIG = {
    "data_folder": "data/og-ds-t-3c",
    "families":    ["erp", "bp", "tf", "riem", "conn"],   # 5-family (riem AND conn) on XON
    "feature_opts": {
        "erp":  {"feature_set": "full", "channels": XON},
        "bp":   {"channel_set": "custom", "channels": XON},
        "tf":   {"channel_set": "custom", "channels": XON},
        "riem": {"channel_set": "custom", "channels": XON},
        "conn": {"regions": XON_REGIONS, "pairs": XON_PAIRS},
    },
    "validation":       ["within", "loso"],
    "n_splits":         5,
    "n_repeats":        5,
    "inner_splits":     5,
    "meta_C":           1.0,
    "artifact_filter":  True,
    "per_subject_norm": True,
    "stats_path": os.path.join(HERE, "xon_full_stacking.json"),
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


def _oof(F, y, classes, splitter, split_args):
    oof = np.zeros((len(y), len(classes)))
    for tr, va in splitter.split(F, y, *split_args):
        m = base_model().fit(F[tr], y[tr])
        oof[va] = _aligned_proba(m, F[va], classes)
    return oof


def _fit_meta_predict(fam_mats, tr, te, y, families, classes, oof_splitter, oof_args, meta_C):
    y_tr = y[tr]
    meta_tr, meta_te = [], []
    for f in families:
        meta_tr.append(_oof(fam_mats[f][tr], y_tr, classes, oof_splitter, oof_args))
        meta_te.append(_aligned_proba(base_model().fit(fam_mats[f][tr], y_tr),
                                      fam_mats[f][te], classes))
    meta = LogisticRegression(max_iter=1000, C=meta_C).fit(np.hstack(meta_tr), y_tr)
    pred = meta.predict(np.hstack(meta_te))
    coef = np.abs(meta.coef_).reshape(meta.coef_.shape[0], len(families), len(classes)).sum(axis=(0, 2))
    return pred, coef / (coef.sum() + 1e-12)


# ── path-based parallel extraction ──
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
    sids = [r[2] for r in res]
    cn = next((r[3] for r in res if r[3]), None)
    print(f"  extraction {time.time()-t0:.1f}s | "
          f"{', '.join(f'{f}:{mats[f].shape[1]}' for f in families)}")
    return mats, y, groups, sids, cn


def per_subject_zscore(mats, groups):
    out = {}
    for f, F in mats.items():
        Z = F.copy()
        for g in np.unique(groups):
            gm = groups == g
            Z[gm] = (F[gm] - F[gm].mean(0)) / (F[gm].std(0) + 1e-12)
        out[f] = Z
    return out


# ── within-subject worker (one subject) ──
def _within_one(fam_g, yg, sid, families, classes, n_splits, n_repeats, inner_splits, meta_C):
    counts = np.unique(yg, return_counts=True)[1]
    splits = min(n_splits, int(counts.min()))
    if splits < 2:
        return None
    cv = RepeatedStratifiedKFold(n_splits=splits, n_repeats=n_repeats, random_state=0)
    accs, bals, ws = [], [], []
    cm = np.zeros((len(classes), len(classes)), dtype=int)
    for tr, te in cv.split(fam_g[families[0]], yg):
        inner_n = min(inner_splits, int(np.unique(yg[tr], return_counts=True)[1].min()))
        inner = StratifiedKFold(n_splits=max(2, inner_n), shuffle=True, random_state=0)
        pred, w = _fit_meta_predict(fam_g, tr, te, yg, families, classes, inner, (), meta_C)
        accs.append(float((pred == yg[te]).mean()))
        bals.append(float(balanced_accuracy_score(yg[te], pred)))
        cm += confusion_matrix(yg[te], pred, labels=classes); ws.append(w)
    return {"subject_id": sid, "acc_mean": float(np.mean(accs)), "acc_std": float(np.std(accs)),
            "bal_mean": float(np.mean(bals))}, cm, np.mean(ws, axis=0)


def run_within(mats, y, groups, sids, families, classes, cfg, n_jobs):
    jobs = [(({f: mats[f][groups == g] for f in families}), y[groups == g], sids[int(g)])
            for g in np.unique(groups)]
    res = Parallel(n_jobs=n_jobs, verbose=5)(
        delayed(_within_one)(fam_g, yg, sid, families, classes, cfg["n_splits"],
                             cfg["n_repeats"], cfg["inner_splits"], cfg["meta_C"])
        for fam_g, yg, sid in jobs)
    res = [r for r in res if r is not None]
    per = [r[0] for r in res]; cm = sum(r[1] for r in res); w = np.mean([r[2] for r in res], axis=0)
    return _summ(per, cm, classes, families, w, "within")


# ── LOSO worker (one fold) ──
def _loso_one(tr, te, mats, y, groups, sid, families, classes, inner_splits, meta_C):
    inner = GroupKFold(n_splits=min(inner_splits, len(np.unique(groups[tr]))))
    pred, w = _fit_meta_predict(mats, tr, te, y, families, classes, inner, (groups[tr],), meta_C)
    yt = y[te]
    return ({"subject_id": sid, "acc": float((pred == yt).mean()),
             "bal": float(balanced_accuracy_score(yt, pred))},
            confusion_matrix(yt, pred, labels=classes), w)


def run_loso(mats, y, groups, sids, families, classes, cfg, n_jobs):
    logo = LeaveOneGroupOut()
    folds = [(tr, te, sids[int(groups[te][0])]) for tr, te in logo.split(mats[families[0]], y, groups)]
    res = Parallel(n_jobs=n_jobs, verbose=5)(
        delayed(_loso_one)(tr, te, mats, y, groups, sid, families, classes,
                           cfg["inner_splits"], cfg["meta_C"]) for tr, te, sid in folds)
    per = [r[0] for r in res]; cm = sum(r[1] for r in res); w = np.mean([r[2] for r in res], axis=0)
    return _summ(per, cm, classes, families, w, "loso")


def _summ(per, cm, classes, families, w, kind):
    accs = np.array([p.get("acc_mean", p.get("acc")) for p in per])
    bals = np.array([p.get("bal_mean", p.get("bal")) for p in per])
    return {"mode": kind, "n_subjects": len(per), "n_classes": len(classes),
            "acc_mean": float(accs.mean()), "acc_std": float(accs.std()),
            "bal_mean": float(bals.mean()), "bal_std": float(bals.std()),
            "chance": 1.0 / len(classes),
            "per_class_recall": (cm.diagonal() / np.maximum(cm.sum(1), 1)).tolist(),
            "confusion": cm.tolist(),
            "meta_family_weights": {f: float(w[i]) for i, f in enumerate(families)},
            "per_subject": per}


def main(cfg=CONFIG, n_jobs=4):
    files = sorted(glob.glob(os.path.join(cfg["data_folder"], "*.npz")))
    if not files:
        raise FileNotFoundError(f"No .npz files in {cfg['data_folder']}")
    fams = cfg["families"]
    print(f"XON 7-channel stack | {len(files)} subjects | channels {XON} | n_jobs={n_jobs}")

    print("\n[extract] parallel ...")
    raw, y, groups, sids, class_names = extract_parallel(
        files, fams, cfg["feature_opts"], cfg["artifact_filter"], n_jobs)
    classes = np.unique(y)
    if class_names is None:
        class_names = [str(c) for c in classes]
    print(f"  classes {class_names} | dist {dict(zip(*np.unique(y, return_counts=True)))}")

    results = {}
    if "within" in cfg["validation"]:
        print("\n[within] parallel across subjects ...")
        t0 = time.time()
        results["within"] = run_within(raw, y, groups, sids, fams, classes, cfg, n_jobs)
        r = results["within"]
        print(f"  WITHIN ({time.time()-t0:.1f}s): acc={r['acc_mean']*100:.1f}% "
              f"bal={r['bal_mean']*100:.1f}%  weights {{ {', '.join(f'{f}:{r['meta_family_weights'][f]:.2f}' for f in fams)} }}")

    if "loso" in cfg["validation"]:
        print("\n[loso] parallel across folds ...")
        t0 = time.time()
        mz = per_subject_zscore(raw, groups) if cfg["per_subject_norm"] else raw
        results["loso"] = run_loso(mz, y, groups, sids, fams, classes, cfg, n_jobs)
        r = results["loso"]
        print(f"  LOSO ({time.time()-t0:.1f}s): acc={r['acc_mean']*100:.1f}% "
              f"bal={r['bal_mean']*100:.1f}%  weights {{ {', '.join(f'{f}:{r['meta_family_weights'][f]:.2f}' for f in fams)} }}")

    out = {"montage": XON, "n_channels": len(XON), "data": cfg["data_folder"],
           "class_names": class_names,
           "n_features_per_family": {f: int(raw[f].shape[1]) for f in fams}, **results}
    json.dump(out, open(cfg["stats_path"], "w"), indent=2)

    print("\n" + "=" * 54)
    print(f"XON 7-CHANNEL STACK — {len(classes)}-class (chance {100/len(classes):.0f}%)")
    print("=" * 54)
    for m in ("within", "loso"):
        if m in results:
            r = results[m]
            print(f"  {m:>6}: acc {r['acc_mean']*100:5.1f}% | bal {r['bal_mean']*100:5.1f}% | "
                  f"recall {dict(zip(class_names, np.round(r['per_class_recall'],2)))}")
    print(f"\nSaved stats -> {cfg['stats_path']}  (no model weights, as requested)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--jobs", type=int, default=4)
    main(n_jobs=ap.parse_args().jobs)
