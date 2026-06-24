"""
feature_trends.py
=================
Dose-response trends for the most important LDA features, fully modular: it
ranks and plots over WHATEVER feature families you choose, via the in-file
CONFIG (no command line).

Pipeline:
  1. Build features for every subject using ModularFeatureExtractor (the same
     registry as train_combined.py), per-subject z-score, pool.
  2. Rank features by FOLD-STABLE LDA weight: refit shrinkage-LDA on each LOSO
     fold, average |coef| across folds. Robust to single-subject quirks.
  3. Take the top-N. For EACH, average the RAW extracted value per condition
     across all trials/subjects (real units, NOT z-scored) and bar-plot the
     3/4 condition means, with faint per-subject lines behind.

Edit CONFIG and run:  python feature_trends.py
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

from train_combined import load_dataset, ModularFeatureExtractor, FEATURE_REGISTRY

# ─────────────────────────────────────────────
# CONFIG  (everything in-file; no CLI)
# ─────────────────────────────────────────────
CONFIG = {
    "output_dir":   "Results/LDA_3c/trends_3c",

    "data_folder":  "data/og-ds-t-3c",
    "families":     ["erp", "bp"],
    "feature_opts": {
        "erp": {"feature_set": "full"},
        "bp":  {"channel_set": "all60"},
    },

    "top_n":           8,
    "artifact_filter": True,
}

COND_COLORS = ["#9EB3C2", "#1C7293", "#21295C", "#B85042"]
MID = "#21295C"; GREY = "#64748B"


def extract_all(subjects, families, feature_opts):
    """RAW features per subject + pooled raw/z-scored matrices."""
    raw_list, ys, groups = [], [], []
    names = None
    for gi, s in enumerate(subjects):
        fx = ModularFeatureExtractor(families, feature_opts).set_meta(s["meta"])
        F = fx.fit_transform(s["X"])
        if names is None:
            names = list(fx.feature_names_)
        raw_list.append(F); ys.append(s["y"]); groups.append(np.full(len(s["y"]), gi))
    raw_F = np.concatenate(raw_list); y = np.concatenate(ys); groups = np.concatenate(groups)
    z_F = raw_F.copy()
    for g in np.unique(groups):
        gm = groups == g
        mu = raw_F[gm].mean(axis=0); sd = raw_F[gm].std(axis=0) + 1e-12
        z_F[gm] = (raw_F[gm] - mu) / sd
    return raw_F, z_F, y, groups, names


def fold_stable_ranking(z_F, y, groups):
    logo = LeaveOneGroupOut()
    imp_sum = np.zeros(z_F.shape[1]); n = 0
    for tr, te in logo.split(z_F, y, groups):
        scaler = StandardScaler().fit(z_F[tr])
        lda = LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")
        lda.fit(scaler.transform(z_F[tr]), y[tr])
        imp_sum += np.abs(lda.coef_).max(axis=0); n += 1
    return np.argsort(imp_sum / max(n, 1))[::-1], imp_sum / max(n, 1), n


def condition_means_raw(raw_F, y, groups, fi):
    classes = np.unique(y)
    overall = {int(c): float(raw_F[y == c, fi].mean()) for c in classes}
    per_subject = []
    for g in np.unique(groups):
        gm = groups == g
        per_subject.append({int(c): float(raw_F[gm & (y == c), fi].mean())
                            for c in classes if (gm & (y == c)).any()})
    return classes, overall, per_subject


def plot_grid(raw_F, y, groups, names, top_idx, class_names, out_png, n_classes, top_n):
    classes = np.unique(y)
    cond_labels = [class_names[int(c)] if class_names else str(c) for c in classes]
    ncol = 4; nrow = int(np.ceil(top_n / ncol))
    fig, axes = plt.subplots(nrow, ncol, figsize=(3.75 * ncol, 3.6 * nrow), dpi=160)
    axes = np.array(axes).ravel()
    records = []
    for k, fi in enumerate(top_idx[:top_n]):
        ax = axes[k]
        _, overall, per_subject = condition_means_raw(raw_F, y, groups, fi)
        xpos = np.arange(len(classes)); vals = [overall[int(c)] for c in classes]
        for sm in per_subject:
            ax.plot(xpos, [sm.get(int(c), np.nan) for c in classes],
                    color=GREY, alpha=0.18, lw=0.8, zorder=1)
        ax.bar(xpos, vals, color=[COND_COLORS[i % 4] for i in range(len(classes))],
               edgecolor="white", linewidth=0.8, zorder=2, width=0.62)
        ax.set_title(names[fi], fontsize=10, fontweight="bold", color=MID)
        ax.set_xticks(xpos)
        ax.set_xticklabels([c.replace("_", "\n") for c in cond_labels], fontsize=7.5)
        ax.tick_params(labelsize=8); ax.spines[["top", "right"]].set_visible(False)
        fam = names[fi].split(":", 1)[0]
        ax.set_ylabel(f"{fam} (raw)", fontsize=8, color=GREY)
        records.append({"rank": k + 1, "feature": names[fi], "condition_means": overall,
                        "per_subject_means": per_subject})
    for k in range(len(top_idx[:top_n]), len(axes)):
        axes[k].axis("off")
    fig.suptitle(f"Dose-response of top-{top_n} fold-stable LDA features ({n_classes}-class)\n"
                 f"families: {', '.join(sorted(set(n.split(':',1)[0] for n in names)))}  |  "
                 f"bars = condition mean of RAW feature; faint lines = subjects",
                 fontsize=12.5, fontweight="bold", color=MID, y=1.02)
    fig.tight_layout(); fig.savefig(out_png, bbox_inches="tight"); plt.close()
    return records, cond_labels


def main(cfg=CONFIG):
    os.makedirs(cfg["output_dir"], exist_ok=True)
    subjects = load_dataset(cfg["data_folder"], artifact_filter=cfg["artifact_filter"])
    n_classes = len(np.unique(subjects[0]["y"]))
    class_names = subjects[0]["meta"].get("class_names")
    print(f"Loaded {len(subjects)} subjects | {n_classes} classes | "
          f"families={cfg['families']} (registered: {list(FEATURE_REGISTRY)})")

    raw_F, z_F, y, groups, names = extract_all(subjects, cfg["families"], cfg["feature_opts"])
    if len(np.unique(groups)) < 2:
        raise SystemExit("Need >=2 subjects for fold-stable LOSO ranking.")
    print(f"Feature matrix: {raw_F.shape} ({len(names)} features)")

    top_idx, mean_imp, n_folds = fold_stable_ranking(z_F, y, groups)
    top_n = cfg["top_n"]
    print(f"Ranked over {n_folds} LOSO folds. Top {top_n}:")
    for k, fi in enumerate(top_idx[:top_n]):
        print(f"  {k+1}. {names[fi]:>26s}  |w|={mean_imp[fi]:.3f}")

    out_png = os.path.join(cfg["output_dir"], f"feature_trends_{n_classes}c.png")
    records, cond_labels = plot_grid(raw_F, y, groups, names, top_idx, class_names,
                                     out_png, n_classes, top_n)
    jpath = os.path.join(cfg["output_dir"], f"feature_trends_{n_classes}c.json")
    with open(jpath, "w") as f:
        json.dump({"n_classes": n_classes, "n_subjects": len(subjects), "n_folds": n_folds,
                   "families": cfg["families"], "conditions": cond_labels,
                   "top_features": records}, f, indent=2)
    print(f"\nSaved -> {out_png}\n         {jpath}")


if __name__ == "__main__":
    main()
