"""
feature_importance.py
=====================
Two complementary readings of "which features matter" for the combined
ERP + band-power LDA, for either class count (3 or 4, auto-detected).

  (A) Univariate discriminability  -- ANOVA F-score per feature (f_classif).
      Model-free: how separated are the class means relative to within-class
      spread. Pooled across subjects on per-subject z-scored features. This is
      the honest "activation signature": it answers "does this channel x band
      separate intensities?" independent of the LDA. Used for the band-power
      signature figure (replaces the hand-drawn one).

  (B) LDA-weight fold-stability  -- refit the real pipeline on each LOSO fold's
      training subjects, record |coef| per feature each fold, then report the
      mean importance AND how often each feature lands in the top-k. A feature
      that is top-k in nearly every fold is robust signal; one that only shows
      up for particular training subjects is noise. This directly addresses
      "is this importance trustworthy across subjects?".

Both use the SAME extractors and the SAME per-subject z-score + StandardScaler
as train_combined.py, so the features are identical to what the LDA trains on.

Outputs (to --output_dir):
  feature_importance_{N}c.json   -- full rankings, both methods
  signature_bandpower_{N}c.png   -- per-band x (mean over channels) F-score
  top_features_{N}c.png          -- top-k features by fold-stable LDA weight

Usage:
    python feature_importance.py --data_folder data_3c --output_dir out_3c
    python feature_importance.py --data_folder data_4c --output_dir out_4c
    # top-k and channel set are configurable:
    python feature_importance.py --data_folder data_3c --output_dir out_3c --top_k 20
"""

from __future__ import annotations
import argparse, glob, os, json, warnings
import numpy as np

warnings.filterwarnings("ignore")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import LeaveOneGroupOut
from sklearn.feature_selection import f_classif

from erp_features import load_npz_for_features, baseline_sd_outlier_mask
from combined_features import CombinedExtractor

# Band order for the signature figure (must match bandpower_features.BANDS)
BANDS = ["delta", "theta", "alpha", "beta", "gamma"]
PALETTE = {"pos": "#1C7293", "neg": "#B85042", "mid": "#21295C", "grey": "#64748B"}


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


def extract_all(subjects, erp_set, bp_channel_set, bp_relative):
    """Combined features for every subject; returns pooled F, y, groups, names."""
    Fs, ys, groups = [], [], []
    names = None
    for gi, s in enumerate(subjects):
        fx = CombinedExtractor(erp_set=erp_set, bp_channel_set=bp_channel_set,
                               bp_relative=bp_relative, use_erp=True, use_bp=True
                               ).set_meta(s["meta"])
        F = fx.fit_transform(s["X"])
        if names is None:
            names = list(fx.feature_names_)
        Fs.append(F); ys.append(s["y"])
        groups.append(np.full(len(s["y"]), gi))
    return (np.concatenate(Fs), np.concatenate(ys),
            np.concatenate(groups), names)


def per_group_zscore(F, groups):
    Fn = F.copy()
    for g in np.unique(groups):
        gm = groups == g
        mu = F[gm].mean(axis=0); sd = F[gm].std(axis=0) + 1e-12
        Fn[gm] = (F[gm] - mu) / sd
    return Fn


def method_a_fscore(F, y, names):
    """ANOVA F-score per feature (model-free discriminability)."""
    Fval, pval = f_classif(F, y)
    Fval = np.nan_to_num(Fval, nan=0.0)
    order = np.argsort(Fval)[::-1]
    ranking = [{"feature": names[i], "f_score": float(Fval[i]),
                "p_value": float(pval[i])} for i in order]
    return ranking, Fval


def method_b_fold_stability(F, y, groups, names, top_k):
    """Refit LDA per LOSO fold; mean |coef| and top-k hit-rate per feature."""
    logo = LeaveOneGroupOut()
    n_feat = F.shape[1]
    imp_sum = np.zeros(n_feat)
    topk_hits = np.zeros(n_feat, dtype=int)
    n_folds = 0
    for tr, te in logo.split(F, y, groups):
        scaler = StandardScaler().fit(F[tr])
        lda = LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")
        lda.fit(scaler.transform(F[tr]), y[tr])
        # multiclass coef_: (n_classes, n_feat) -> aggregate by max |w| across classes
        imp = np.abs(lda.coef_).max(axis=0)
        imp_sum += imp
        topk_idx = np.argsort(imp)[::-1][:top_k]
        topk_hits[topk_idx] += 1
        n_folds += 1
    mean_imp = imp_sum / max(n_folds, 1)
    hit_rate = topk_hits / max(n_folds, 1)
    # rank by mean importance, but report stability alongside
    order = np.argsort(mean_imp)[::-1]
    ranking = [{"feature": names[i], "mean_abs_weight": float(mean_imp[i]),
                "topk_hit_rate": float(hit_rate[i]),
                "topk_hits": int(topk_hits[i])} for i in order]
    return ranking, mean_imp, hit_rate, n_folds


def parse_feature(name):
    """'bp:gamma@Cz' -> ('bp','gamma','Cz'); 'erp:peak_to_peak@C3' -> ('erp','peak_to_peak','C3')."""
    half, rest = name.split(":", 1)
    tok, ch = rest.split("@", 1) if "@" in rest else (rest, "")
    return half, tok, ch


def signature_figure(fscore, names, out_path, n_classes):
    """Mean F-score per band, averaged over channels (band-power half only)."""
    per_band = {b: [] for b in BANDS}
    for nm, fv in zip(names, fscore):
        half, tok, ch = parse_feature(nm)
        if half == "bp" and tok in per_band:
            per_band[tok].append(fv)
    means = [np.mean(per_band[b]) if per_band[b] else 0.0 for b in BANDS]
    fig, ax = plt.subplots(figsize=(5.6, 3.4), dpi=200)
    colors = [PALETTE["pos"] for _ in BANDS]
    bars = ax.bar(BANDS, means, color=colors, edgecolor="white", linewidth=0.8)
    for b, m in zip(bars, means):
        ax.text(b.get_x()+b.get_width()/2, m, f"{m:.1f}", ha="center",
                va="bottom", fontsize=9, fontweight="bold", color=PALETTE["mid"])
    ax.set_ylabel("Mean F-score across channels", fontsize=10)
    ax.set_title(f"Band-power discriminability ({n_classes}-class)\nhigher = better at separating intensities",
                 fontsize=11.5, fontweight="bold", color=PALETTE["mid"], pad=8)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=10)
    plt.tight_layout(); plt.savefig(out_path, bbox_inches="tight"); plt.close()


def top_features_figure(ranking_b, out_path, n_classes, top_k):
    top = ranking_b[:top_k][::-1]
    labels = [r["feature"].replace("bp:", "").replace("erp:", "") for r in top]
    vals = [r["mean_abs_weight"] for r in top]
    hits = [r["topk_hit_rate"] for r in top]
    # color erp vs bp
    colors = [PALETTE["mid"] if r["feature"].startswith("erp:") else PALETTE["pos"] for r in top]
    fig, ax = plt.subplots(figsize=(6.4, max(3.2, top_k*0.32)), dpi=200)
    y = np.arange(len(top))
    ax.barh(y, vals, color=colors, edgecolor="white", linewidth=0.6)
    for i, (v, h) in enumerate(zip(vals, hits)):
        ax.text(v, i, f"  {h*100:.0f}% folds", va="center", fontsize=7.5, color=PALETTE["grey"])
    ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=8)
    ax.set_xlabel("Mean |LDA weight| across LOSO folds", fontsize=10)
    ax.set_title(f"Top {top_k} features ({n_classes}-class)\nteal = band-power, navy = ERP; label shows fold-stability",
                 fontsize=11, fontweight="bold", color=PALETTE["mid"], pad=8)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=8)
    plt.tight_layout(); plt.savefig(out_path, bbox_inches="tight"); plt.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data_folder", required=True)
    ap.add_argument("--output_dir", required=True)
    ap.add_argument("--erp_set", default="recommended")
    ap.add_argument("--bp_channel_set", default="all60")
    ap.add_argument("--bp_relative", action="store_true")
    ap.add_argument("--top_k", type=int, default=15)
    ap.add_argument("--no_artifact_filter", action="store_true")
    args = ap.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    subjects = load_dataset(args.data_folder, artifact_filter=not args.no_artifact_filter)
    n_classes = len(np.unique(subjects[0]["y"]))
    print(f"Loaded {len(subjects)} subjects | {n_classes} classes | "
          f"erp_set={args.erp_set} bp={args.bp_channel_set}")

    F, y, groups, names = extract_all(subjects, args.erp_set, args.bp_channel_set, args.bp_relative)
    F = per_group_zscore(F, groups)
    print(f"Feature matrix: {F.shape}  ({len(names)} features)")

    # (A) F-score
    rank_a, fscore = method_a_fscore(F, y, names)
    # (B) fold-stability (needs >=2 groups for LOSO)
    n_groups = len(np.unique(groups))
    if n_groups >= 2:
        rank_b, mean_imp, hit_rate, n_folds = method_b_fold_stability(F, y, groups, names, args.top_k)
    else:
        rank_b, n_folds = [], 0
        print("WARNING: <2 subjects, skipping fold-stability (LOSO needs >=2).")

    # Figures
    sig_path = os.path.join(args.output_dir, f"signature_bandpower_{n_classes}c.png")
    signature_figure(fscore, names, sig_path, n_classes)
    if rank_b:
        top_path = os.path.join(args.output_dir, f"top_features_{n_classes}c.png")
        top_features_figure(rank_b, top_path, n_classes, args.top_k)

    out = {
        "n_classes": n_classes, "n_subjects": len(subjects), "n_folds": n_folds,
        "n_features": len(names),
        "config": {"erp_set": args.erp_set, "bp_channel_set": args.bp_channel_set,
                   "bp_relative": args.bp_relative, "top_k": args.top_k},
        "method_a_fscore": rank_a,
        "method_b_fold_stability": rank_b,
    }
    jpath = os.path.join(args.output_dir, f"feature_importance_{n_classes}c.json")
    with open(jpath, "w") as f:
        json.dump(out, f, indent=2)

    # Console summary
    print(f"\nTop 10 by F-score (model-free discriminability):")
    for r in rank_a[:10]:
        print(f"  {r['feature']:>22s}  F={r['f_score']:8.2f}")
    if rank_b:
        print(f"\nTop 10 by fold-stable LDA weight ({n_folds} folds):")
        for r in rank_b[:10]:
            print(f"  {r['feature']:>22s}  |w|={r['mean_abs_weight']:.3f}  "
                  f"stable={r['topk_hit_rate']*100:.0f}% of folds")
    print(f"\nSaved -> {jpath}")
    if rank_b:
        print(f"Figures -> {sig_path}, {top_path}")
    else:
        print(f"Figure -> {sig_path}")


if __name__ == "__main__":
    main()