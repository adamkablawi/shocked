"""
stacking.py
===========
Per-family LDA STACK for the EMS intensity decoder -- the winning architecture.

One regularised shrinkage-LDA is trained per feature family (erp, bp, tf, riem).
Their class-probability outputs are fused by a multinomial logistic meta-learner.
Each base model stays low-dimensional relative to its own family, and the meta-
learner learns how much to trust each family -- so diverse-but-individually-weak
views (tf, riem) add complementary signal instead of diluting the strong ones,
which is what beat the plain erp+bp concatenation.

Validation (both reported, as per the rest of the project)
----------------------------------------------------------
  within : per-subject RepeatedStratifiedKFold. Inner StratifiedKFold over the
           subject's own trials makes the out-of-fold (OOF) meta-features.
  loso   : LeaveOneSubjectOut, per-subject z-scored then pooled. Inner GroupKFold
           over the TRAIN subjects makes the OOF meta-features.

Both are leakage-safe: the held-out rows/subject never produce a meta-feature
they are then scored on, and never enter a base or meta fit.

Outputs (-> ./results/)
-----------------------
  stacking.json  : within + loso, each with acc + balanced acc (mean/std),
                   per-subject scores, aggregate confusion, per-class recall,
                   and the mean meta-learner weight per family.
  confusion.png  : aggregate LOSO confusion matrix of the stack.

Run from the repo root:
    PYTHONPATH=Models/LDA-Stacking python Models/LDA-Stacking/stacking.py
"""

from __future__ import annotations
import os, json, warnings
import numpy as np

warnings.filterwarnings("ignore")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import (LeaveOneGroupOut, GroupKFold,
                                     StratifiedKFold, RepeatedStratifiedKFold)
from sklearn.metrics import balanced_accuracy_score, confusion_matrix

from train_combined import load_dataset, ModularFeatureExtractor

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
CONFIG = {
    "output_dir":  "Models/LDA-Stacking/results",
    "data_folder": "data/og-ds-t-3c",

    # One base LDA per family; the meta-learner fuses them.
    "stack_families": ["erp", "bp", "tf", "riem"],
    "feature_opts": {
        "erp":  {"feature_set": "full"},
        "bp":   {"channel_set": "all60"},
        "tf":   {"channel_set": "all60"},
        "riem": {"channel_set": "all60"},
    },

    "validation":   ["within", "loso"],
    "n_splits":     5,        # within-subject outer folds
    "n_repeats":    5,        # within-subject repeats
    "inner_splits": 5,        # inner CV for OOF meta-features
    "meta_C":       1.0,      # meta logistic-regression regularisation
    "artifact_filter":  True,
    "per_subject_norm": True, # LOSO only
}


# ─────────────────────────────────────────────
# EXTRACTION  (one pooled RAW matrix PER family)
# ─────────────────────────────────────────────
def extract_family_matrices(subjects, families, feature_opts):
    mats = {f: [] for f in families}
    ys, groups, sids = [], [], []
    for gi, s in enumerate(subjects):
        for f in families:
            fx = ModularFeatureExtractor([f], feature_opts).set_meta(s["meta"])
            mats[f].append(fx.fit_transform(s["X"]))
        ys.append(s["y"]); groups.append(np.full(len(s["y"]), gi))
        sids.append(s["subject_id"])
    for f in families:
        mats[f] = np.concatenate(mats[f])
    return mats, np.concatenate(ys), np.concatenate(groups), sids


def per_subject_zscore(mats, groups):
    out = {}
    for f, F in mats.items():
        Z = F.copy()
        for g in np.unique(groups):
            gm = groups == g
            mu = F[gm].mean(axis=0); sd = F[gm].std(axis=0) + 1e-12
            Z[gm] = (F[gm] - mu) / sd
        out[f] = Z
    return out


# ─────────────────────────────────────────────
# BASE / META helpers
# ─────────────────────────────────────────────
def base_model():
    return make_pipeline(
        StandardScaler(),
        LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto"),
    )


def _aligned_proba(model, F, classes):
    """predict_proba re-ordered into the global class column order."""
    proba = model.predict_proba(F)
    out = np.zeros((F.shape[0], len(classes)))
    lda = model.named_steps["lineardiscriminantanalysis"]
    for j, c in enumerate(lda.classes_):
        out[:, list(classes).index(c)] = proba[:, j]
    return out


def _oof(F, y, classes, splitter, split_args):
    """Generic out-of-fold predict_proba for the rows of F."""
    oof = np.zeros((len(y), len(classes)))
    for tr, va in splitter.split(F, y, *split_args):
        m = base_model().fit(F[tr], y[tr])
        oof[va] = _aligned_proba(m, F[va], classes)
    return oof


def _fit_meta_predict(fam_mats, tr, te, y, families, classes, oof_splitter, oof_args, meta_C):
    """Build OOF meta-features on `tr`, refit bases, predict `te` via meta-LR."""
    y_tr = y[tr]
    meta_tr, meta_te = [], []
    for f in families:
        F_tr, F_te = fam_mats[f][tr], fam_mats[f][te]
        meta_tr.append(_oof(F_tr, y_tr, classes, oof_splitter, oof_args))
        meta_te.append(_aligned_proba(base_model().fit(F_tr, y_tr), F_te, classes))
    meta = LogisticRegression(max_iter=1000, C=meta_C)
    meta.fit(np.hstack(meta_tr), y_tr)
    pred = meta.predict(np.hstack(meta_te))
    coef = np.abs(meta.coef_).reshape(meta.coef_.shape[0], len(families), len(classes))
    blk = coef.sum(axis=(0, 2))
    return pred, blk / (blk.sum() + 1e-12)


def _summarise(per_subject, agg_cm, classes, families, meta_weights, kind):
    accs = np.array([p["acc_mean" if "acc_mean" in p else "acc"] for p in per_subject])
    bals = np.array([p["bal_mean" if "bal_mean" in p else "bal"] for p in per_subject])
    recall = (agg_cm.diagonal() / np.maximum(agg_cm.sum(axis=1), 1)).tolist()
    return {
        "mode": kind, "n_subjects": len(per_subject), "n_classes": len(classes),
        "acc_mean": float(accs.mean()), "acc_std": float(accs.std()),
        "bal_mean": float(bals.mean()), "bal_std": float(bals.std()),
        "chance": 1.0 / len(classes),
        "meta_family_weights": {f: float(np.mean(meta_weights, axis=0)[i])
                                for i, f in enumerate(families)},
        "aggregate_confusion": agg_cm.tolist(), "per_class_recall": recall,
        "per_subject": per_subject,
    }


# ─────────────────────────────────────────────
# LOSO stack
# ─────────────────────────────────────────────
def run_stack_loso(fam_mats, y, groups, sids, families, inner_splits, meta_C):
    classes = np.unique(y)
    logo = LeaveOneGroupOut()
    per_subject, meta_weights = [], []
    agg_cm = np.zeros((len(classes), len(classes)), dtype=int)
    for tr, te in logo.split(fam_mats[families[0]], y, groups):
        inner = GroupKFold(n_splits=min(inner_splits, len(np.unique(groups[tr]))))
        pred, w = _fit_meta_predict(fam_mats, tr, te, y, families, classes,
                                    inner, (groups[tr],), meta_C)
        held = sids[int(groups[te][0])]
        per_subject.append({"subject_id": held, "acc": float((pred == y[te]).mean()),
                            "bal": float(balanced_accuracy_score(y[te], pred))})
        agg_cm += confusion_matrix(y[te], pred, labels=classes)
        meta_weights.append(w)
    return _summarise(per_subject, agg_cm, classes, families, meta_weights, "loso")


# ─────────────────────────────────────────────
# WITHIN-SUBJECT stack
# ─────────────────────────────────────────────
def run_stack_within(fam_mats, y, groups, sids, families,
                     n_splits, n_repeats, inner_splits, meta_C):
    classes = np.unique(y)
    per_subject, meta_weights = [], []
    agg_cm = np.zeros((len(classes), len(classes)), dtype=int)
    for g in np.unique(groups):
        gm = groups == g
        yg = y[gm]
        idx = np.where(gm)[0]
        counts = np.unique(yg, return_counts=True)[1]
        splits = min(n_splits, int(counts.min()))
        if splits < 2:
            continue
        fam_g = {f: fam_mats[f][gm] for f in families}
        cv = RepeatedStratifiedKFold(n_splits=splits, n_repeats=n_repeats, random_state=0)
        accs, bals = [], []
        for tr, te in cv.split(fam_g[families[0]], yg):
            inner_n = min(inner_splits, int(np.unique(yg[tr], return_counts=True)[1].min()))
            inner = StratifiedKFold(n_splits=max(2, inner_n), shuffle=True, random_state=0)
            pred, w = _fit_meta_predict(fam_g, tr, te, yg, families, classes,
                                        inner, (), meta_C)
            accs.append(float((pred == yg[te]).mean()))
            bals.append(float(balanced_accuracy_score(yg[te], pred)))
            agg_cm += confusion_matrix(yg[te], pred, labels=classes)
            meta_weights.append(w)
        per_subject.append({"subject_id": sids[int(g)],
                            "acc_mean": float(np.mean(accs)), "acc_std": float(np.std(accs)),
                            "bal_mean": float(np.mean(bals))})
    return _summarise(per_subject, agg_cm, classes, families, meta_weights, "within")


def plot_confusion(cm, class_names, out_png, n_classes, title):
    cm = np.array(cm, dtype=float)
    norm = cm / np.maximum(cm.sum(axis=1, keepdims=True), 1)
    fig, ax = plt.subplots(figsize=(4.6, 4), dpi=160)
    im = ax.imshow(norm, cmap="Blues", vmin=0, vmax=1)
    for i in range(n_classes):
        for j in range(n_classes):
            ax.text(j, i, f"{norm[i, j]*100:.0f}%", ha="center", va="center",
                    color="white" if norm[i, j] > 0.5 else "#21295C", fontsize=10)
    ax.set_xticks(range(n_classes)); ax.set_yticks(range(n_classes))
    ax.set_xticklabels(class_names, rotation=30, ha="right", fontsize=8)
    ax.set_yticklabels(class_names, fontsize=8)
    ax.set_xlabel("predicted"); ax.set_ylabel("true")
    ax.set_title(title, fontsize=11, fontweight="bold", color="#21295C")
    fig.colorbar(im, fraction=0.046, pad=0.04)
    plt.tight_layout(); plt.savefig(out_png, bbox_inches="tight"); plt.close()


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
def main(cfg=CONFIG):
    os.makedirs(cfg["output_dir"], exist_ok=True)
    subjects = load_dataset(cfg["data_folder"], artifact_filter=cfg["artifact_filter"])
    fams = cfg["stack_families"]
    class_names = subjects[0]["meta"].get("class_names") or \
        [str(c) for c in np.unique(subjects[0]["y"])]
    print(f"Loaded {len(subjects)} subjects | {len(class_names)} classes | families={fams}")

    raw, y, groups, sids = extract_family_matrices(subjects, fams, cfg["feature_opts"])
    for f in fams:
        print(f"  base {f:>5}: {raw[f].shape[1]} features")

    results = {}
    if "within" in cfg["validation"]:
        print("\n--- within-subject ---")
        results["within"] = run_stack_within(raw, y, groups, sids, fams,
                                             cfg["n_splits"], cfg["n_repeats"],
                                             cfg["inner_splits"], cfg["meta_C"])
        r = results["within"]
        print(f"  WITHIN: acc={r['acc_mean']*100:.1f}% +/-{r['acc_std']*100:.1f}  "
              f"bal={r['bal_mean']*100:.1f}%  (chance {r['chance']*100:.0f}%)")
        print(f"  meta weights: {{ {', '.join(f'{f}: {r['meta_family_weights'][f]:.2f}' for f in fams)} }}")

    if "loso" in cfg["validation"]:
        print("\n--- LOSO ---")
        loso_mats = per_subject_zscore(raw, groups) if cfg["per_subject_norm"] else raw
        results["loso"] = run_stack_loso(loso_mats, y, groups, sids, fams,
                                         cfg["inner_splits"], cfg["meta_C"])
        r = results["loso"]
        print(f"  LOSO: acc={r['acc_mean']*100:.1f}% +/-{r['acc_std']*100:.1f}  "
              f"bal={r['bal_mean']*100:.1f}% +/-{r['bal_std']*100:.1f}  "
              f"(chance {r['chance']*100:.0f}%)")
        print(f"  meta weights: {{ {', '.join(f'{f}: {r['meta_family_weights'][f]:.2f}' for f in fams)} }}")
        plot_confusion(r["aggregate_confusion"], class_names,
                       os.path.join(cfg["output_dir"], "confusion.png"),
                       len(class_names), "Stack -- LOSO confusion (row-normalised)")

    out = {"data_folder": cfg["data_folder"], "stack_families": fams,
           "class_names": class_names, **results}
    with open(os.path.join(cfg["output_dir"], "stacking.json"), "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nSaved -> {cfg['output_dir']}/stacking.json + confusion.png")


if __name__ == "__main__":
    main()
