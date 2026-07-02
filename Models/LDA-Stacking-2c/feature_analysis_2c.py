"""
feature_analysis_2c.py
======================
Feature importance + analytic trace for the 2-class tolerance decoder
(data/og-ds-t-2c-tol : tolerable vs INTOLERABLE, 120/40). Goal: surface the
features / neural markers most indicative of INTOLERABLE (high-intensity) EMS.

Consistent with the 2c model, all LDAs use UNIFORM priors [0.5, 0.5] and the
meta-learner uses class_weight='balanced' (Option 2 de-biasing), so the imbalance
does not bias the boundary or the importances toward `tolerable`.

Part 1 — FEATURE IMPORTANCE (interpretable erp + bp combined LDA)
  * ANOVA F-score per feature (univariate discriminability).
  * Fold-stable LDA weight across LOSO folds (multivariate importance).
  * For every top feature we report DIRECTION: standardized mean difference
    (intolerable - tolerable), so + = elevated in intolerable, - = reduced.
  * Figures: per-band discriminability (band-power signature) + top features.

Part 2 — ANALYTIC TRACE (the 4-family stack)
  * Meta-learner family weights + per-family coefficient on the "intolerable" vote.
  * Top feature drivers inside each base expert (with direction).
  * One worked trial.

Outputs -> Results/LDA_2c/
Run:  PYTHONPATH=Models/LDA-Stacking-2c python Models/LDA-Stacking-2c/feature_analysis_2c.py
"""
from __future__ import annotations
import os, json, warnings
import numpy as np
warnings.filterwarnings("ignore")
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import LeaveOneGroupOut, GroupKFold
from sklearn.feature_selection import f_classif

from train_combined import load_dataset, ModularFeatureExtractor

OUT = "Results/LDA_2c"
DATA = "data/og-ds-t-2c-tol"
FEAT_OPTS = {"erp": {"feature_set": "full"}, "bp": {"channel_set": "all60"},
             "tf": {"channel_set": "all60"}, "riem": {"channel_set": "all60"}}
PRIORS = [0.5, 0.5]
BANDS = ["delta", "theta", "alpha", "beta", "gamma"]
NAVY = "#21295C"; TEAL = "#1C7293"; RED = "#B85042"


def extract(subjects, families):
    mats = {f: [] for f in families}; names = {f: None for f in families}
    ys, groups = [], []
    for gi, s in enumerate(subjects):
        for f in families:
            fx = ModularFeatureExtractor([f], FEAT_OPTS).set_meta(s["meta"]).fit(s["X"])
            mats[f].append(fx.transform(s["X"]))
            if names[f] is None:
                names[f] = [n.split(":", 1)[1] for n in fx.feature_names_]
        ys.append(s["y"]); groups.append(np.full(len(s["y"]), gi))
    y = np.concatenate(ys); groups = np.concatenate(groups)
    for f in families:
        F = np.concatenate(mats[f])
        for g in np.unique(groups):          # per-subject z-score
            gm = groups == g
            F[gm] = (F[gm] - F[gm].mean(0)) / (F[gm].std(0) + 1e-12)
        mats[f] = F
    return mats, y, groups, names


def direction(F, y, pos):
    """Standardized mean difference (pos - neg) per feature. + = higher in intolerable."""
    Fz = (F - F.mean(0)) / (F.std(0) + 1e-12)
    return Fz[y == pos].mean(0) - Fz[y != pos].mean(0)


def base_lda():
    return make_pipeline(StandardScaler(),
                         LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto", priors=PRIORS))


# ───────────── PART 1: importance on combined erp+bp ─────────────
def feature_importance(mats, y, groups, names, pos):
    F = np.hstack([mats["erp"], mats["bp"]])
    nm = [f"erp:{n}" for n in names["erp"]] + [f"bp:{n}" for n in names["bp"]]
    d = direction(F, y, pos)

    # Method A: ANOVA F-score
    Fstat, _ = f_classif(F, y); Fstat = np.nan_to_num(Fstat)
    a_order = np.argsort(Fstat)[::-1]
    rank_a = [{"feature": nm[i], "f_score": float(Fstat[i]),
               "direction_intolerable": float(d[i])} for i in a_order]

    # Method B: fold-stable LDA weights (LOSO)
    logo = LeaveOneGroupOut(); imp = np.zeros(F.shape[1]); hits = np.zeros(F.shape[1], int); n = 0
    for tr, te in logo.split(F, y, groups):
        m = base_lda().fit(F[tr], y[tr])
        w = np.abs(m.named_steps["lineardiscriminantanalysis"].coef_).max(0)
        imp += w; hits[np.argsort(w)[::-1][:15]] += 1; n += 1
    imp /= n; hitrate = hits / n
    b_order = np.argsort(imp)[::-1]
    rank_b = [{"feature": nm[i], "mean_abs_weight": float(imp[i]),
               "topk_stability": float(hitrate[i]),
               "direction_intolerable": float(d[i])} for i in b_order]

    # signature: per-band mean F-score over bp features
    perband = {b: [] for b in BANDS}
    for name, fv in zip(nm, Fstat):
        if name.startswith("bp:"):
            band = name.split(":")[1].split("@")[0]
            if band in perband: perband[band].append(fv)
    means = [np.mean(perband[b]) if perband[b] else 0 for b in BANDS]
    fig, ax = plt.subplots(figsize=(5.4, 3.2), dpi=200)
    ax.bar(BANDS, means, color=TEAL, edgecolor="white")
    for i, m in enumerate(means):
        ax.text(i, m, f"{m:.0f}", ha="center", va="bottom", fontsize=9, fontweight="bold", color=NAVY)
    ax.set_ylabel("mean F-score across channels"); ax.set_title(
        "Band-power discriminability — intolerable vs tolerable", fontsize=11, fontweight="bold", color=NAVY)
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout(); plt.savefig(f"{OUT}/signature_bandpower_2c.png", bbox_inches="tight"); plt.close()

    # top features figure (fold-stable), coloured by direction
    top = rank_b[:15][::-1]
    fig, ax = plt.subplots(figsize=(7, 5), dpi=200)
    yv = np.arange(len(top))
    cols = [RED if t["direction_intolerable"] > 0 else "#4C72B0" for t in top]
    ax.barh(yv, [t["mean_abs_weight"] for t in top], color=cols, edgecolor="white")
    ax.set_yticks(yv); ax.set_yticklabels([t["feature"] for t in top], fontsize=8)
    ax.set_xlabel("mean |LDA weight| across LOSO folds")
    ax.set_title("Top features for intolerable stimulation\n(red = elevated in intolerable, blue = reduced)",
                 fontsize=11, fontweight="bold", color=NAVY)
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout(); plt.savefig(f"{OUT}/top_features_2c.png", bbox_inches="tight"); plt.close()

    return {"n_features": F.shape[1], "method_a_fscore": rank_a, "method_b_fold_stability": rank_b}


# ───────────── PART 2: analytic trace of the stack ─────────────
def aligned(m, F, classes):
    p = m.predict_proba(F); out = np.zeros((len(F), len(classes)))
    for j, c in enumerate(m.named_steps["lineardiscriminantanalysis"].classes_):
        out[:, list(classes).index(c)] = p[:, j]
    return out


def oof(F, y, groups, classes):
    o = np.zeros((len(y), len(classes)))
    for tr, va in GroupKFold(5).split(F, y, groups):
        o[va] = aligned(base_lda().fit(F[tr], y[tr]), F[va], classes)
    return o


def trace(mats, y, groups, names, classes, pos, fams):
    base = {f: base_lda().fit(mats[f], y) for f in fams}
    M = np.hstack([oof(mats[f], y, groups, classes) for f in fams])
    cols = [(f, int(c)) for f in fams for c in classes]
    meta = LogisticRegression(max_iter=1000, class_weight="balanced").fit(M, y)
    coef = np.abs(meta.coef_).ravel()                       # binary -> (8,)
    fam_w = {f: float(coef[[i for i, (ff, _) in enumerate(cols) if ff == f]].sum()) for f in fams}
    tot = sum(fam_w.values()); fam_w = {f: fam_w[f] / tot for f in fams}
    # signed coefficient on each family's P(intolerable) vote
    intol_vote = {f: float(meta.coef_.ravel()[cols.index((f, pos))]) for f in fams}
    # top features per base with direction
    drivers = {}
    for f in fams:
        w = np.abs(base[f].named_steps["lineardiscriminantanalysis"].coef_).max(0)
        d = direction(mats[f], y, pos)
        order = np.argsort(w)[::-1][:6]
        drivers[f] = [{"feature": names[f][i], "weight": float(w[i]),
                       "direction_intolerable": float(d[i])} for i in order]
    # worked example: a true-intolerable trial where a family errs but stack is right
    probs = {f: base[f].predict_proba(mats[f]) for f in fams}
    stackpred = meta.predict(M)
    ex = None
    for i in np.where(y == pos)[0]:
        calls = {f: classes[int(np.argmax(probs[f][i]))] for f in fams}
        if stackpred[i] == pos and any(calls[f] != pos for f in fams):
            ex = int(i); break
    example = None
    if ex is not None:
        example = {"trial": ex, "true": "intolerable",
                   "votes": {f: [round(float(probs[f][ex][j]), 2) for j in range(len(classes))] for f in fams},
                   "stack": "intolerable"}
    return {"family_weight": fam_w, "coef_on_intolerable_vote": intol_vote,
            "top_drivers": drivers, "worked_example": example}


def main():
    os.makedirs(OUT, exist_ok=True)
    subs = load_dataset(DATA, artifact_filter=True)
    classes = np.unique(subs[0]["y"]); pos = int(classes[-1])
    cls_names = subs[0]["meta"]["class_names"]
    print(f"Loaded {len(subs)} subjects | classes {cls_names} | positive={cls_names[pos]}")
    fams = ["erp", "bp", "tf", "riem"]
    mats, y, groups, names = extract(subs, fams)
    print(f"pooled dist {dict(zip(*np.unique(y, return_counts=True)))}")

    print("\n[Part 1] feature importance (erp+bp, uniform priors)")
    imp = feature_importance(mats, y, groups, names, pos)
    print("  top 8 by F-score (dir + = elevated in intolerable):")
    for r in imp["method_a_fscore"][:8]:
        print(f"    {r['feature']:>26} F={r['f_score']:7.1f}  dir={r['direction_intolerable']:+.2f}")
    print("  top 8 by fold-stable LDA weight:")
    for r in imp["method_b_fold_stability"][:8]:
        print(f"    {r['feature']:>26} |w|={r['mean_abs_weight']:.3f}  dir={r['direction_intolerable']:+.2f}")

    print("\n[Part 2] analytic trace (4-family stack)")
    tr = trace(mats, y, groups, names, classes, pos, fams)
    print("  family weights:", {k: round(v, 2) for k, v in tr["family_weight"].items()})
    print("  coef on P(intolerable):", {k: round(v, 2) for k, v in tr["coef_on_intolerable_vote"].items()})
    for f in fams:
        print(f"  {f} drivers:", ", ".join(f"{d['feature']}({d['direction_intolerable']:+.1f})"
                                           for d in tr["top_drivers"][f][:4]))

    json.dump({"data": DATA, "class_names": cls_names, "positive_class": cls_names[pos],
               "options": {"uniform_priors": True, "balanced_meta": True},
               "feature_importance": imp, "trace": tr},
              open(f"{OUT}/feature_analysis_2c.json", "w"), indent=2)
    print(f"\nSaved -> {OUT}/feature_analysis_2c.json + signature_bandpower_2c.png + top_features_2c.png")


if __name__ == "__main__":
    main()
