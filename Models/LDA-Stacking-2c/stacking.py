"""
stacking.py  (2-class TOLERANCE variant)
========================================
Per-family LDA stack for the 2-class "tolerable vs intolerable" question
(dataset data/og-ds-t-2c-tol, an unbalanced 120 / 40 split: the bottom three
intensities merged into `tolerable`, the top intensity as `intolerable`).

The goal is to surface the features that mark INTOLERABLE (high-intensity) EMS.
Because the set is 75 / 25 imbalanced, two imbalance treatments are built in:

  Option 1 — measure it honestly.  Balanced accuracy, per-class recall, the
             confusion matrix, and (2-class) ROC-AUC + PR-AUC (average precision)
             for the positive = intolerable class. Raw accuracy is reported but
             is NOT the headline (a majority predictor already scores 75%).

  Option 2 — de-bias the classifiers.  Base LDAs use UNIFORM priors [0.5, 0.5]
             instead of the empirical 75/25 prior (so the boundary is not pulled
             toward `tolerable`), and the logistic meta-learner uses
             class_weight='balanced'.

Same leakage-safe within-subject (RepeatedStratifiedKFold) and LOSO (per-subject
z-score, inner GroupKFold OOF) protocol as the 3-class stack.

Run from the repo root:
    PYTHONPATH=Models/LDA-Stacking-2c python Models/LDA-Stacking-2c/stacking.py
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
from sklearn.metrics import (balanced_accuracy_score, confusion_matrix,
                             roc_auc_score, average_precision_score)

from train_combined import load_dataset, ModularFeatureExtractor

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
CONFIG = {
    "output_dir":  "Results/LDA_2c",
    "data_folder": "data/og-ds-t-2c-tol",

    "stack_families": ["erp", "bp", "tf", "riem"],
    "feature_opts": {
        "erp":  {"feature_set": "full"},
        "bp":   {"channel_set": "all60"},
        "tf":   {"channel_set": "all60"},
        "riem": {"channel_set": "all60"},
    },

    "validation":      ["within", "loso"],
    "n_splits":        5,
    "n_repeats":       5,
    "inner_splits":    5,
    "meta_C":          1.0,
    "uniform_priors":  True,     # Option 2: de-bias the base LDAs
    "balanced_meta":   True,     # Option 2: balance the meta-learner
    "artifact_filter": True,
    "per_subject_norm": True,
}

# set in main() once n_classes is known (Option 2: uniform LDA priors)
BASE_PRIORS = None
META_CLASS_WEIGHT = "balanced"


# ─────────────────────────────────────────────
# EXTRACTION
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
# BASE / META helpers  (Option 2 de-biasing applied here)
# ─────────────────────────────────────────────
def base_model():
    return make_pipeline(
        StandardScaler(),
        LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto", priors=BASE_PRIORS),
    )


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
        F_tr, F_te = fam_mats[f][tr], fam_mats[f][te]
        meta_tr.append(_oof(F_tr, y_tr, classes, oof_splitter, oof_args))
        meta_te.append(_aligned_proba(base_model().fit(F_tr, y_tr), F_te, classes))
    meta = LogisticRegression(max_iter=1000, C=meta_C, class_weight=META_CLASS_WEIGHT)
    meta.fit(np.hstack(meta_tr), y_tr)
    Mte = np.hstack(meta_te)
    pred = meta.predict(Mte)
    proba = meta.predict_proba(Mte)            # columns in meta.classes_ order
    pos_col = list(meta.classes_).index(classes[-1])   # intolerable = highest label
    coef = np.abs(meta.coef_)
    coef = coef.reshape(coef.shape[0], len(families), len(classes))
    w = coef.sum(axis=(0, 2)); w = w / (w.sum() + 1e-12)
    return pred, proba[:, pos_col], w


def _auc_block(y_true, p_pos):
    """Pooled ROC-AUC and PR-AUC (average precision) for the positive class."""
    y_true = np.asarray(y_true); p_pos = np.asarray(p_pos)
    if len(np.unique(y_true)) < 2:
        return None, None
    return float(roc_auc_score(y_true, p_pos)), float(average_precision_score(y_true, p_pos))


# ─────────────────────────────────────────────
# LOSO
# ─────────────────────────────────────────────
def run_stack_loso(fam_mats, y, groups, sids, families, inner_splits, meta_C, pos_label):
    classes = np.unique(y)
    logo = LeaveOneGroupOut()
    per_subject, meta_weights = [], []
    agg_cm = np.zeros((len(classes), len(classes)), dtype=int)
    all_yt, all_pp = [], []
    n_total = len(np.unique(groups))
    for fold, (tr, te) in enumerate(logo.split(fam_mats[families[0]], y, groups), 1):
        held = sids[int(groups[te][0])]
        print(f"  [LOSO fold {fold}/{n_total}] holding out {held} ...", flush=True)
        inner = GroupKFold(n_splits=min(inner_splits, len(np.unique(groups[tr]))))
        pred, p_pos, w = _fit_meta_predict(fam_mats, tr, te, y, families, classes,
                                           inner, (groups[tr],), meta_C)
        yt = y[te]
        roc, ap = _auc_block(yt, p_pos)
        per_subject.append({"subject_id": held,
                            "acc": float((pred == yt).mean()),
                            "bal": float(balanced_accuracy_score(yt, pred)),
                            "roc_auc": roc, "pr_auc": ap})
        print(f"  [LOSO fold {fold}/{n_total}] {held}: bal={per_subject[-1]['bal']*100:.1f}% "
              f"roc={roc if roc is None else round(roc,3)}", flush=True)
        agg_cm += confusion_matrix(yt, pred, labels=classes)
        meta_weights.append(w); all_yt.append(yt); all_pp.append(p_pos)
    return _summarise(per_subject, agg_cm, classes, families, meta_weights,
                      "loso", np.concatenate(all_yt), np.concatenate(all_pp), pos_label)


# ─────────────────────────────────────────────
# WITHIN-SUBJECT
# ─────────────────────────────────────────────
def run_stack_within(fam_mats, y, groups, sids, families,
                     n_splits, n_repeats, inner_splits, meta_C, pos_label):
    classes = np.unique(y)
    per_subject, meta_weights = [], []
    agg_cm = np.zeros((len(classes), len(classes)), dtype=int)
    all_yt, all_pp = [], []
    uniq = np.unique(groups)
    n_total = len(uniq)
    for si, g in enumerate(uniq, 1):
        gm = groups == g; yg = y[gm]
        counts = np.unique(yg, return_counts=True)[1]
        splits = min(n_splits, int(counts.min()))
        if splits < 2:
            continue
        print(f"  [within subject {si}/{n_total}] {sids[int(g)]} ...", flush=True)
        fam_g = {f: fam_mats[f][gm] for f in families}
        cv = RepeatedStratifiedKFold(n_splits=splits, n_repeats=n_repeats, random_state=0)
        accs, bals, pp_s, yt_s = [], [], [], []
        for tr, te in cv.split(fam_g[families[0]], yg):
            inner_n = min(inner_splits, int(np.unique(yg[tr], return_counts=True)[1].min()))
            inner = StratifiedKFold(n_splits=max(2, inner_n), shuffle=True, random_state=0)
            pred, p_pos, w = _fit_meta_predict(fam_g, tr, te, yg, families, classes,
                                               inner, (), meta_C)
            accs.append(float((pred == yg[te]).mean()))
            bals.append(float(balanced_accuracy_score(yg[te], pred)))
            agg_cm += confusion_matrix(yg[te], pred, labels=classes)
            meta_weights.append(w); pp_s.append(p_pos); yt_s.append(yg[te])
        yt_all = np.concatenate(yt_s); pp_all = np.concatenate(pp_s)
        roc, ap = _auc_block(yt_all, pp_all)
        per_subject.append({"subject_id": sids[int(g)],
                            "acc_mean": float(np.mean(accs)), "acc_std": float(np.std(accs)),
                            "bal_mean": float(np.mean(bals)), "roc_auc": roc, "pr_auc": ap})
        print(f"  [within subject {si}/{n_total}] {sids[int(g)]}: bal={np.mean(bals)*100:.1f}% "
              f"roc={roc if roc is None else round(roc,3)}", flush=True)
        all_yt.append(yt_all); all_pp.append(pp_all)
    return _summarise(per_subject, agg_cm, classes, families, meta_weights,
                      "within", np.concatenate(all_yt), np.concatenate(all_pp), pos_label)


def _summarise(per_subject, agg_cm, classes, families, meta_weights, kind,
               yt_all, pp_all, pos_label):
    accs = np.array([p.get("acc_mean", p.get("acc")) for p in per_subject])
    bals = np.array([p.get("bal_mean", p.get("bal")) for p in per_subject])
    recall = (agg_cm.diagonal() / np.maximum(agg_cm.sum(axis=1), 1)).tolist()
    roc, ap = _auc_block(yt_all, pp_all)
    return {
        "mode": kind, "n_subjects": len(per_subject), "n_classes": len(classes),
        "acc_mean": float(accs.mean()), "acc_std": float(accs.std()),
        "bal_mean": float(bals.mean()), "bal_std": float(bals.std()),
        "chance": 1.0 / len(classes),
        "majority_baseline": float(agg_cm.sum(axis=1).max() / agg_cm.sum()),
        "roc_auc_pooled": roc, "pr_auc_pooled": ap,
        "positive_class": pos_label,
        "meta_family_weights": {f: float(np.mean(meta_weights, axis=0)[i])
                                for i, f in enumerate(families)},
        "aggregate_confusion": agg_cm.tolist(), "per_class_recall": recall,
        "per_subject": per_subject,
    }


def plot_confusion(cm, class_names, out_png, n_classes, title):
    cm = np.array(cm, dtype=float)
    norm = cm / np.maximum(cm.sum(axis=1, keepdims=True), 1)
    fig, ax = plt.subplots(figsize=(4.4, 3.9), dpi=160)
    im = ax.imshow(norm, cmap="Blues", vmin=0, vmax=1)
    for i in range(n_classes):
        for j in range(n_classes):
            ax.text(j, i, f"{norm[i, j]*100:.0f}%", ha="center", va="center",
                    color="white" if norm[i, j] > 0.5 else "#21295C", fontsize=11)
    ax.set_xticks(range(n_classes)); ax.set_yticks(range(n_classes))
    ax.set_xticklabels(class_names, rotation=20, ha="right", fontsize=9)
    ax.set_yticklabels(class_names, fontsize=9)
    ax.set_xlabel("predicted"); ax.set_ylabel("true")
    ax.set_title(title, fontsize=11, fontweight="bold", color="#21295C")
    fig.colorbar(im, fraction=0.046, pad=0.04)
    plt.tight_layout(); plt.savefig(out_png, bbox_inches="tight"); plt.close()


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
def main(cfg=CONFIG):
    global BASE_PRIORS, META_CLASS_WEIGHT
    os.makedirs(cfg["output_dir"], exist_ok=True)
    subjects = load_dataset(cfg["data_folder"], artifact_filter=cfg["artifact_filter"])
    fams = cfg["stack_families"]
    classes = np.unique(subjects[0]["y"])
    n_classes = len(classes)
    class_names = subjects[0]["meta"].get("class_names") or [str(c) for c in classes]
    pos_label = class_names[int(classes[-1])]   # intolerable = highest label

    # Option 2 wiring
    BASE_PRIORS = (np.ones(n_classes) / n_classes) if cfg["uniform_priors"] else None
    META_CLASS_WEIGHT = "balanced" if cfg["balanced_meta"] else None
    print(f"Loaded {len(subjects)} subjects | {n_classes} classes {class_names} | "
          f"positive='{pos_label}'")
    print(f"Option 2: base priors={'uniform' if cfg['uniform_priors'] else 'empirical'}, "
          f"meta class_weight={META_CLASS_WEIGHT}")

    raw, y, groups, sids = extract_family_matrices(subjects, fams, cfg["feature_opts"])
    for f in fams:
        print(f"  base {f:>5}: {raw[f].shape[1]} features")
    print(f"  pooled class dist: {dict(zip(*np.unique(y, return_counts=True)))}")

    results = {}
    if "within" in cfg["validation"]:
        print("\n--- within-subject ---")
        r = run_stack_within(raw, y, groups, sids, fams, cfg["n_splits"],
                             cfg["n_repeats"], cfg["inner_splits"], cfg["meta_C"], pos_label)
        results["within"] = r
        print(f"  WITHIN: bal={r['bal_mean']*100:.1f}%  acc={r['acc_mean']*100:.1f}% "
              f"(majority {r['majority_baseline']*100:.0f}%)  ROC-AUC={r['roc_auc_pooled']:.3f} "
              f"PR-AUC={r['pr_auc_pooled']:.3f}")
        print(f"  recall {dict(zip(class_names, np.round(r['per_class_recall'],3)))}")

    if "loso" in cfg["validation"]:
        print("\n--- LOSO ---")
        loso_mats = per_subject_zscore(raw, groups) if cfg["per_subject_norm"] else raw
        r = run_stack_loso(loso_mats, y, groups, sids, fams,
                           cfg["inner_splits"], cfg["meta_C"], pos_label)
        results["loso"] = r
        print(f"  LOSO: bal={r['bal_mean']*100:.1f}%  acc={r['acc_mean']*100:.1f}% "
              f"(majority {r['majority_baseline']*100:.0f}%)  ROC-AUC={r['roc_auc_pooled']:.3f} "
              f"PR-AUC={r['pr_auc_pooled']:.3f}")
        print(f"  recall {dict(zip(class_names, np.round(r['per_class_recall'],3)))}")
        print(f"  meta weights {{ {', '.join(f'{f}: {r['meta_family_weights'][f]:.2f}' for f in fams)} }}")
        plot_confusion(r["aggregate_confusion"], class_names,
                       os.path.join(cfg["output_dir"], "confusion_2c.png"),
                       n_classes, "Stack (2-class) — LOSO confusion")

    out = {"data_folder": cfg["data_folder"], "stack_families": fams,
           "class_names": class_names, "options": {"uniform_priors": cfg["uniform_priors"],
           "balanced_meta": cfg["balanced_meta"]}, **results}
    with open(os.path.join(cfg["output_dir"], "stacking_2c.json"), "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nSaved -> {cfg['output_dir']}/stacking_2c.json + confusion_2c.png")


if __name__ == "__main__":
    main()
