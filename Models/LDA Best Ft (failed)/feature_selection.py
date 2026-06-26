"""
feature_selection.py
====================
Nested-CV cross-family feature selection for the shrinkage-LDA decoder.

Goal
----
Find a COMPACT, cross-family feature subset that decodes EMS intensity at least
as well as the full erp+bp model -- and ideally better -- on the metric that
matters: leave-one-subject-out (LOSO). This directly tests the hypothesis that
the way to beat erp+bp is FEWER, BETTER features (countering the dilution we saw
when whole families were concatenated), curated from across erp / bp / tf.

Why nested CV
-------------
Feature selection on the whole dataset and then reporting accuracy is leakage:
the test subjects influenced which features were chosen. Here, selection happens
INSIDE each outer LOSO fold, ranking features on the TRAIN subjects only; the
held-out subject is never seen during ranking or scaling. The accuracy-vs-k
curve it produces is therefore an honest estimate of how a selected-subset model
would generalize to a new person.

What it outputs (-> ./results/)
-------------------------------
  * feature_selection.json : full accuracy-vs-k curves (acc + balanced acc, mean
    and std over folds) for each selector, the chosen k, the family composition
    of the selected set, and the STABLE feature list (features selected in the
    top-k across a high fraction of folds -- the deployable shortlist).
  * accuracy_vs_k.png      : curves with the erp+bp baseline drawn as a line.

Selectors
---------
  "fscore" : univariate ANOVA F-score top-k (relevance only).
  "mrmr"   : minimum-Redundancy-Maximum-Relevance (greedy). Relevance = ANOVA
             F (normalised to [0,1]); redundancy = mean |Pearson r| to the
             already-selected features. This is the one that can actually beat
             plain ranking, because it refuses to spend the budget on the
             spatially-correlated band-power / ERP features that say the same
             thing.

Edit CONFIG and run:
    PYTHONPATH=Models/LDA-Best-Features python Models/LDA-Best-Features/feature_selection.py
(run from the repo root so the data/ paths resolve.)
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
from sklearn.metrics import balanced_accuracy_score

from train_combined import load_dataset, ModularFeatureExtractor

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
CONFIG = {
    "output_dir":  "Models/LDA-Best-Features/results",

    # 40/80/40 set the best.json model was built on. Switch to a balanced
    # 40/40/40 set here if/when one exists.
    "data_folder": "data/og-ds-t-3c",

    # Candidate POOL the selector draws from -- spans the families. riem is left
    # out by default (1830 features, shown to dilute; add "riem" to include it).
    "candidate_families": ["erp", "bp", "tf"],
    "feature_opts": {
        "erp":  {"feature_set": "full"},
        "bp":   {"channel_set": "all60"},
        "tf":   {"channel_set": "all60"},
        "riem": {"channel_set": "all60"},
    },

    # Reference model to beat (its features are pulled by name prefix from the
    # candidate pool, so it is evaluated on identical data/folds).
    "baseline_families": ["erp", "bp"],

    "selectors":       ["fscore", "mrmr"],
    "k_grid":          [10, 20, 30, 50, 75, 100, 150, 200, 300],
    "stable_threshold": 0.6,     # feature must appear in top-k in >= 60% of folds
    "artifact_filter": True,
    "per_subject_norm": True,
}


# ─────────────────────────────────────────────
# EXTRACTION  (per-subject features, pooled, per-subject z-scored)
# ─────────────────────────────────────────────
def extract_pool(subjects, families, feature_opts, per_subject_norm=True):
    Fs, ys, groups, names = [], [], [], None
    for gi, s in enumerate(subjects):
        fx = ModularFeatureExtractor(families, feature_opts).set_meta(s["meta"])
        F = fx.fit_transform(s["X"])
        if names is None:
            names = list(fx.feature_names_)
        Fs.append(F); ys.append(s["y"]); groups.append(np.full(len(s["y"]), gi))
    F = np.concatenate(Fs); y = np.concatenate(ys); groups = np.concatenate(groups)
    if per_subject_norm:
        for g in np.unique(groups):
            gm = groups == g
            mu = F[gm].mean(axis=0); sd = F[gm].std(axis=0) + 1e-12
            F[gm] = (F[gm] - mu) / sd
    return F, y, groups, np.array(names)


# ─────────────────────────────────────────────
# RANKERS  (train-only)
# ─────────────────────────────────────────────
def rank_fscore(Ftr, ytr, n_select):
    Fstat, _ = f_classif(Ftr, ytr)
    Fstat = np.nan_to_num(Fstat, nan=0.0)
    return np.argsort(Fstat)[::-1][:n_select]


def rank_mrmr(Ftr, ytr, n_select):
    """Greedy mRMR: relevance = normalised ANOVA F; redundancy = mean |corr|."""
    Fstat, _ = f_classif(Ftr, ytr)
    rel = np.nan_to_num(Fstat, nan=0.0)
    rel = rel / (rel.max() + 1e-12)                       # -> [0, 1], comparable to |corr|
    C = np.abs(np.corrcoef(Ftr, rowvar=False))
    C = np.nan_to_num(C, nan=0.0)

    p = Ftr.shape[1]
    n_select = min(n_select, p)
    selected = [int(np.argmax(rel))]
    remaining = [i for i in range(p) if i != selected[0]]
    while len(selected) < n_select and remaining:
        rem = np.array(remaining)
        redundancy = C[np.ix_(rem, selected)].mean(axis=1)   # mean |corr| to chosen
        score = rel[rem] - redundancy                        # MID criterion
        pick = rem[int(np.argmax(score))]
        selected.append(int(pick))
        remaining.remove(int(pick))
    return np.array(selected)


RANKERS = {"fscore": rank_fscore, "mrmr": rank_mrmr}


# ─────────────────────────────────────────────
# CORE: nested LOSO sweep over k
# ─────────────────────────────────────────────
def loso_sweep(F, y, groups, selector, k_grid):
    ranker = RANKERS[selector]
    kmax = min(max(k_grid), F.shape[1])
    logo = LeaveOneGroupOut()
    accs = {k: [] for k in k_grid}
    bals = {k: [] for k in k_grid}
    sel_counts = {k: np.zeros(F.shape[1], dtype=int) for k in k_grid}
    n_folds = 0

    for tr, te in logo.split(F, y, groups):
        Ftr, ytr, Fte, yte = F[tr], y[tr], F[te], y[te]
        order = ranker(Ftr, ytr, kmax)                   # train-only ranking, best first
        for k in k_grid:
            kk = min(k, F.shape[1])
            idx = order[:kk]
            sc = StandardScaler().fit(Ftr[:, idx])
            lda = LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")
            lda.fit(sc.transform(Ftr[:, idx]), ytr)
            pred = lda.predict(sc.transform(Fte[:, idx]))
            accs[k].append(float((pred == yte).mean()))
            bals[k].append(float(balanced_accuracy_score(yte, pred)))
            sel_counts[k][idx] += 1
        n_folds += 1

    curve = []
    for k in k_grid:
        a = np.array(accs[k]); b = np.array(bals[k])
        curve.append({"k": k, "acc_mean": float(a.mean()), "acc_std": float(a.std()),
                      "bal_mean": float(b.mean()), "bal_std": float(b.std())})
    return curve, sel_counts, n_folds


def plain_loso(F, y, groups, idx):
    """LOSO accuracy using a FIXED feature index set (no selection) -- for baselines."""
    logo = LeaveOneGroupOut()
    accs, bals = [], []
    for tr, te in logo.split(F, y, groups):
        sc = StandardScaler().fit(F[tr][:, idx])
        lda = LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")
        lda.fit(sc.transform(F[tr][:, idx]), y[tr])
        pred = lda.predict(sc.transform(F[te][:, idx]))
        accs.append(float((pred == y[te]).mean()))
        bals.append(float(balanced_accuracy_score(y[te], pred)))
    return {"acc_mean": float(np.mean(accs)), "acc_std": float(np.std(accs)),
            "bal_mean": float(np.mean(bals))}


def family_of(name):
    return name.split(":", 1)[0]


# ─────────────────────────────────────────────
# PLOT
# ─────────────────────────────────────────────
def plot_curves(results, baseline, cand_full, out_png, n_classes):
    fig, ax = plt.subplots(figsize=(7, 4.4), dpi=160)
    colors = {"fscore": "#1C7293", "mrmr": "#B85042"}
    for sel, r in results.items():
        ks = [c["k"] for c in r["curve"]]
        bal = [c["bal_mean"] * 100 for c in r["curve"]]
        std = [c["bal_std"] * 100 for c in r["curve"]]
        ax.errorbar(ks, bal, yerr=std, marker="o", ms=4, capsize=2, lw=1.6,
                    color=colors.get(sel, None), label=f"{sel} (best k={r['best_k']})")
    ax.axhline(baseline["bal_mean"] * 100, color="#21295C", ls="--", lw=1.4,
               label=f"erp+bp baseline ({baseline['bal_mean']*100:.1f}%)")
    ax.axhline(cand_full["bal_mean"] * 100, color="#64748B", ls=":", lw=1.2,
               label=f"full pool, no selection ({cand_full['bal_mean']*100:.1f}%)")
    ax.axhline(100.0 / n_classes, color="gray", ls="-", lw=0.8, alpha=0.5,
               label=f"chance ({100.0/n_classes:.0f}%)")
    ax.set_xlabel("number of selected features (k)")
    ax.set_ylabel("LOSO balanced accuracy (%)")
    ax.set_title("Nested-CV cross-family feature selection", fontsize=12,
                 fontweight="bold", color="#21295C")
    ax.legend(fontsize=8, frameon=True)
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout(); plt.savefig(out_png, bbox_inches="tight"); plt.close()


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
def main(cfg=CONFIG):
    os.makedirs(cfg["output_dir"], exist_ok=True)
    subjects = load_dataset(cfg["data_folder"], artifact_filter=cfg["artifact_filter"])
    n_classes = len(np.unique(subjects[0]["y"]))
    print(f"Loaded {len(subjects)} subjects | {n_classes} classes | "
          f"chance {100.0/n_classes:.0f}%")

    F, y, groups, names = extract_pool(subjects, cfg["candidate_families"],
                                       cfg["feature_opts"], cfg["per_subject_norm"])
    print(f"Candidate pool: {F.shape[1]} features "
          f"({dict(zip(*np.unique([family_of(n) for n in names], return_counts=True)))})")

    # Reference baselines, evaluated on the SAME folds/data.
    base_idx = np.array([i for i, n in enumerate(names)
                         if family_of(n) in cfg["baseline_families"]])
    baseline = plain_loso(F, y, groups, base_idx)
    cand_full = plain_loso(F, y, groups, np.arange(F.shape[1]))
    print(f"erp+bp baseline LOSO: acc={baseline['acc_mean']*100:.1f}% "
          f"bal={baseline['bal_mean']*100:.1f}%")
    print(f"full pool LOSO:       acc={cand_full['acc_mean']*100:.1f}% "
          f"bal={cand_full['bal_mean']*100:.1f}%")

    k_grid = [k for k in cfg["k_grid"] if k <= F.shape[1]] + (
        [F.shape[1]] if F.shape[1] not in cfg["k_grid"] else [])
    results = {}
    for sel in cfg["selectors"]:
        print(f"\n--- selector: {sel} ---")
        curve, sel_counts, n_folds = loso_sweep(F, y, groups, sel, k_grid)
        best = max(curve, key=lambda c: c["bal_mean"])    # peak balanced accuracy
        best_k = best["k"]
        for c in curve:
            flag = "  <- best" if c["k"] == best_k else ""
            print(f"  k={c['k']:>4}: acc={c['acc_mean']*100:5.1f}%  "
                  f"bal={c['bal_mean']*100:5.1f}% +/-{c['bal_std']*100:4.1f}{flag}")

        # Stable feature shortlist at best k.
        freq = sel_counts[best_k] / max(n_folds, 1)
        stable_idx = np.where(freq >= cfg["stable_threshold"])[0]
        stable_idx = stable_idx[np.argsort(freq[stable_idx])[::-1]]
        stable = [{"feature": names[i], "select_freq": float(freq[i])} for i in stable_idx]
        fam_comp = dict(zip(*np.unique([family_of(names[i]) for i in stable_idx],
                                       return_counts=True))) if len(stable_idx) else {}
        fam_comp = {k: int(v) for k, v in fam_comp.items()}
        print(f"  best k={best_k}: bal={best['bal_mean']*100:.1f}% "
              f"(baseline {baseline['bal_mean']*100:.1f}%, delta "
              f"{(best['bal_mean']-baseline['bal_mean'])*100:+.1f})")
        print(f"  stable features (>= {cfg['stable_threshold']*100:.0f}% of folds): "
              f"{len(stable)}  composition={fam_comp}")

        results[sel] = {"curve": curve, "best_k": best_k,
                        "best_bal": best["bal_mean"], "best_acc": best["acc_mean"],
                        "n_folds": n_folds, "family_composition": fam_comp,
                        "stable_features": stable}

    out_json = os.path.join(cfg["output_dir"], "feature_selection.json")
    with open(out_json, "w") as f:
        json.dump({"n_classes": n_classes, "n_subjects": len(subjects),
                   "data_folder": cfg["data_folder"],
                   "candidate_families": cfg["candidate_families"],
                   "n_candidate_features": int(F.shape[1]),
                   "baseline_erp_bp": baseline, "full_pool": cand_full,
                   "selectors": results}, f, indent=2)
    out_png = os.path.join(cfg["output_dir"], "accuracy_vs_k.png")
    plot_curves(results, baseline, cand_full, out_png, n_classes)

    print(f"\nSaved -> {out_json}\n         {out_png}")
    # Headline
    best_overall = max(results.values(), key=lambda r: r["best_bal"])
    print(f"\nBEST: bal={best_overall['best_bal']*100:.1f}% at k={best_overall['best_k']} "
          f"vs erp+bp {baseline['bal_mean']*100:.1f}%  "
          f"(delta {(best_overall['best_bal']-baseline['bal_mean'])*100:+.1f} pts)")


if __name__ == "__main__":
    main()
