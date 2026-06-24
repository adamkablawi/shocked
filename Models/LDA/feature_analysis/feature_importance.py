"""
feature_importance.py
=====================
Two readings of "which features matter", fully modular over whatever feature
families you choose via the in-file CONFIG (no command line).

  (A) Univariate discriminability -- ANOVA F-score per feature (model-free).
      If "bp" is among the families, also draws a per-band band-power
      discriminability figure (the honest activation signature).
  (B) Fold-stable LDA weights -- refit shrinkage-LDA per LOSO fold, mean |coef|
      across folds, plus how often each feature lands in the top-k.

Same registry/extractor as train_combined.py, so features match what the LDA
trains on. Edit CONFIG and run:  python feature_importance.py
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
from sklearn.model_selection import LeaveOneGroupOut
from sklearn.feature_selection import f_classif

from train_combined import load_dataset, ModularFeatureExtractor, FEATURE_REGISTRY

# ─────────────────────────────────────────────
# CONFIG  (in-file; no CLI)
# ─────────────────────────────────────────────
CONFIG = {
    "output_dir":   "Results/LDA_3c/importance_3c",
    "data_folder":  "data/og-ds-t-3c",
    "families":     ["erp", "bp"],
    "feature_opts": {
        "erp": {"feature_set": "full"},
        "bp":  {"channel_set": "all60"},
    },

    "top_k":           15,
    "artifact_filter": True,
}

BANDS = ["delta", "theta", "alpha", "beta", "gamma"]
TEAL = "#1C7293"; MID = "#21295C"; GREY = "#64748B"; NAVY = "#21295C"


def extract_all(subjects, families, feature_opts):
    Fs, ys, groups = [], [], []
    names = None
    for gi, s in enumerate(subjects):
        fx = ModularFeatureExtractor(families, feature_opts).set_meta(s["meta"])
        F = fx.fit_transform(s["X"])
        if names is None:
            names = list(fx.feature_names_)
        Fs.append(F); ys.append(s["y"]); groups.append(np.full(len(s["y"]), gi))
    F = np.concatenate(Fs); y = np.concatenate(ys); groups = np.concatenate(groups)
    z = F.copy()
    for g in np.unique(groups):
        gm = groups == g
        mu = F[gm].mean(axis=0); sd = F[gm].std(axis=0) + 1e-12
        z[gm] = (F[gm] - mu) / sd
    return z, y, groups, names


def method_a_fscore(F, y, names):
    Fval, pval = f_classif(F, y)
    Fval = np.nan_to_num(Fval, nan=0.0)
    order = np.argsort(Fval)[::-1]
    return ([{"feature": names[i], "f_score": float(Fval[i]), "p_value": float(pval[i])}
             for i in order], Fval)


def method_b_fold_stability(F, y, groups, names, top_k):
    logo = LeaveOneGroupOut()
    imp_sum = np.zeros(F.shape[1]); hits = np.zeros(F.shape[1], dtype=int); n = 0
    for tr, te in logo.split(F, y, groups):
        scaler = StandardScaler().fit(F[tr])
        lda = LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")
        lda.fit(scaler.transform(F[tr]), y[tr])
        imp = np.abs(lda.coef_).max(axis=0)
        imp_sum += imp
        hits[np.argsort(imp)[::-1][:top_k]] += 1
        n += 1
    mean_imp = imp_sum / max(n, 1); hit_rate = hits / max(n, 1)
    order = np.argsort(mean_imp)[::-1]
    return ([{"feature": names[i], "mean_abs_weight": float(mean_imp[i]),
              "topk_hit_rate": float(hit_rate[i]), "topk_hits": int(hits[i])}
             for i in order], mean_imp, n)


def parse_feature(name):
    fam, rest = name.split(":", 1)
    tok, ch = rest.split("@", 1) if "@" in rest else (rest, "")
    return fam, tok, ch


def signature_figure(fscore, names, out_path, n_classes):
    """Per-band mean F-score over channels (band-power family only)."""
    per_band = {b: [] for b in BANDS}
    for nm, fv in zip(names, fscore):
        fam, tok, ch = parse_feature(nm)
        if fam == "bp" and tok in per_band:
            per_band[tok].append(fv)
    if not any(per_band.values()):
        return False
    means = [np.mean(per_band[b]) if per_band[b] else 0.0 for b in BANDS]
    fig, ax = plt.subplots(figsize=(5.6, 3.4), dpi=200)
    bars = ax.bar(BANDS, means, color=TEAL, edgecolor="white", linewidth=0.8)
    for b, m in zip(bars, means):
        ax.text(b.get_x()+b.get_width()/2, m, f"{m:.1f}", ha="center", va="bottom",
                fontsize=9, fontweight="bold", color=MID)
    ax.set_ylabel("Mean F-score across channels", fontsize=10)
    ax.set_title(f"Band-power discriminability ({n_classes}-class)\n"
                 f"higher = better at separating intensities",
                 fontsize=11.5, fontweight="bold", color=MID, pad=8)
    ax.spines[["top", "right"]].set_visible(False); ax.tick_params(labelsize=10)
    plt.tight_layout(); plt.savefig(out_path, bbox_inches="tight"); plt.close()
    return True


def top_features_figure(ranking_b, out_path, n_classes, top_k):
    top = ranking_b[:top_k][::-1]
    labels = [r["feature"] for r in top]
    vals = [r["mean_abs_weight"] for r in top]
    hits = [r["topk_hit_rate"] for r in top]
    fams = sorted(set(r["feature"].split(":", 1)[0] for r in top))
    cmap = {f: c for f, c in zip(fams, ["#1C7293", "#21295C", "#B85042", "#2A9D8F"])}
    colors = [cmap[r["feature"].split(":", 1)[0]] for r in top]
    fig, ax = plt.subplots(figsize=(6.8, max(3.2, top_k * 0.34)), dpi=200)
    yv = np.arange(len(top))
    ax.barh(yv, vals, color=colors, edgecolor="white", linewidth=0.6)
    for i, h in enumerate(hits):
        ax.text(vals[i], i, f"  {h*100:.0f}% folds", va="center", fontsize=7.5, color=GREY)
    ax.set_yticks(yv); ax.set_yticklabels(labels, fontsize=8)
    ax.set_xlabel("Mean |LDA weight| across LOSO folds", fontsize=10)
    legend = "  ".join(f"{f}" for f in fams)
    ax.set_title(f"Top {top_k} features ({n_classes}-class)\ncolored by family: {legend}",
                 fontsize=11, fontweight="bold", color=MID, pad=8)
    ax.spines[["top", "right"]].set_visible(False); ax.tick_params(labelsize=8)
    plt.tight_layout(); plt.savefig(out_path, bbox_inches="tight"); plt.close()


def main(cfg=CONFIG):
    os.makedirs(cfg["output_dir"], exist_ok=True)
    subjects = load_dataset(cfg["data_folder"], artifact_filter=cfg["artifact_filter"])
    n_classes = len(np.unique(subjects[0]["y"]))
    print(f"Loaded {len(subjects)} subjects | {n_classes} classes | "
          f"families={cfg['families']} (registered: {list(FEATURE_REGISTRY)})")

    F, y, groups, names = extract_all(subjects, cfg["families"], cfg["feature_opts"])
    print(f"Feature matrix: {F.shape} ({len(names)} features)")

    rank_a, fscore = method_a_fscore(F, y, names)
    n_groups = len(np.unique(groups))
    if n_groups >= 2:
        rank_b, mean_imp, n_folds = method_b_fold_stability(F, y, groups, names, cfg["top_k"])
    else:
        rank_b, n_folds = [], 0
        print("WARNING: <2 subjects, skipping fold-stability.")

    sig_path = os.path.join(cfg["output_dir"], f"signature_bandpower_{n_classes}c.png")
    drew_sig = signature_figure(fscore, names, sig_path, n_classes)
    if not drew_sig:
        print("(no 'bp' family in selection -> skipping band-power signature figure)")
    if rank_b:
        top_path = os.path.join(cfg["output_dir"], f"top_features_{n_classes}c.png")
        top_features_figure(rank_b, top_path, n_classes, cfg["top_k"])

    jpath = os.path.join(cfg["output_dir"], f"feature_importance_{n_classes}c.json")
    with open(jpath, "w") as f:
        json.dump({"n_classes": n_classes, "n_subjects": len(subjects), "n_folds": n_folds,
                   "n_features": len(names), "families": cfg["families"],
                   "method_a_fscore": rank_a, "method_b_fold_stability": rank_b}, f, indent=2)

    print(f"\nTop 10 by F-score:")
    for r in rank_a[:10]:
        print(f"  {r['feature']:>26s}  F={r['f_score']:8.2f}")
    if rank_b:
        print(f"\nTop 10 by fold-stable LDA weight ({n_folds} folds):")
        for r in rank_b[:10]:
            print(f"  {r['feature']:>26s}  |w|={r['mean_abs_weight']:.3f}  "
                  f"stable={r['topk_hit_rate']*100:.0f}%")
    print(f"\nSaved -> {jpath}")


if __name__ == "__main__":
    main()
