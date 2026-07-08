"""
connectivity_analysis.py
========================
Phase-based FUNCTIONAL CONNECTIVITY analysis of the 3-class EMS dataset
(data/og-ds-t-3c: no_stimulation / medium / max), between three cortical regions:

    FC (fronto-central) : FC5 FC1 FC6 FC2 FC3 FC4 FCz
    C  (central)        : C3 Cz C4 C1 C5 C6 C2
    P  (parietal)       : Pz P1..P8

Goal: test whether stimulation intensity modulates PHASE-LOCKED coupling between
these regions — a neuroscience-grounded, interpretable alternative to Riemannian
covariance. (This is analysis only; it does NOT modify any model or feature.)

Measures (per band, per condition, computed per subject then averaged):
  * PLV  — Phase-Locking Value across trials: |<exp(i·Δφ)>|. Captures phase
           consistency across trials at each post-stimulus time point → the
           canonical "phase-locked" connectivity measure.
  * iPLV — imaginary PLV: |Im<exp(i·Δφ)>|. The volume-conduction-robust version
           (removes zero-lag coupling that could be a common source / smearing).
  * A pre-stim baseline (−0.2..0 s) PLV is also computed so we report the
    stimulus-INDUCED modulation (post − baseline), not just raw coupling.

Windows: post = 0.0..0.5 s (evoked, phase-locked); baseline = −0.2..0 s.
Bands: delta(1-4) theta(4-8) alpha(8-13) beta(13-30) gamma(30-45) Hz.

Stats: per band, per inter-region pair (FC-C, FC-P, C-P), a Friedman test across
the three conditions (repeated-measures over the 29 subjects) on the induced PLV /
iPLV — i.e. does the coupling change with intensity?

Outputs -> ConnectivityAnalysis/results/
  connectivity_results.json           # region PLV/iPLV per band/condition + stats
  dose_response_PLV.png / _iPLV.png   # inter-region coupling vs condition, per band
  region_heatmaps.png                 # 3x3 region PLV: max condition + (max−no_stim)
  timecourse.png                      # PLV(t) for the most significant pair/band

Run from repo root:
    PYTHONPATH=. python ConnectivityAnalysis/connectivity_analysis.py [--jobs 4]
"""
from __future__ import annotations
import os, json, glob, argparse, time
import numpy as np
from joblib import Parallel, delayed
from scipy.signal import butter, sosfiltfilt, hilbert
from scipy.stats import friedmanchisquare

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "results")

DATA = "data/og-ds-t-3c"
REGIONS = {
    "FC": ["FC5", "FC1", "FC6", "FC2", "FC3", "FC4", "FCz"],
    "C":  ["C3", "Cz", "C4", "C1", "C5", "C6", "C2"],
    "P":  ["Pz", "P3", "P7", "P4", "P8", "P1", "P5", "P6", "P2"],
}
REG_ORDER = ["FC", "C", "P"]
BETWEEN = [("FC", "C"), ("FC", "P"), ("C", "P")]
WITHIN = [("FC", "FC"), ("C", "C"), ("P", "P")]
PAIRS = BETWEEN + WITHIN
BANDS = {"delta": (1, 4), "theta": (4, 8), "alpha": (8, 13),
         "beta": (13, 30), "gamma": (30, 45)}
POST_WIN = (0.0, 0.5)
BASE_WIN = (-0.2, 0.0)
SFREQ = 250.0
COND_COLORS = ["#9EB3C2", "#1C7293", "#B85042"]   # no_stim / medium / max
NAVY = "#21295C"


def _sos(lo, hi):
    ny = SFREQ / 2
    return butter(4, [max(lo, 0.5) / ny, min(hi, ny - 1e-6) / ny], btype="band", output="sos")


def _region_val(mat, idxA, idxB, same):
    """Mean connectivity over channel pairs between two regions (off-diag if same)."""
    sub = mat[np.ix_(idxA, idxB)]
    if same:
        m = ~np.eye(len(idxA), dtype=bool)
        return float(sub[m].mean())
    return float(sub.mean())


def _one_subject(path):
    d = np.load(path, allow_pickle=True)
    X = np.asarray(d["X"], dtype=float)                 # (n, 60, T)
    y = np.asarray(d["y"]).astype(int)
    ch = [str(c) for c in d["channel_names"]]
    tmin = float(d["epoch_tmin"]) if "epoch_tmin" in d else -0.2
    tmax = float(d["epoch_tmax"]) if "epoch_tmax" in d else 1.5
    times = np.linspace(tmin, tmax, X.shape[2])
    ridx = {r: [ch.index(c) for c in chs if c in ch] for r, chs in REGIONS.items()}
    conds = [0, 1, 2]
    nb, nc = len(BANDS), len(conds)

    post_m = (times >= POST_WIN[0]) & (times <= POST_WIN[1])
    base_m = (times >= BASE_WIN[0]) & (times <= BASE_WIN[1])

    chan_plv = np.zeros((nb, nc, 60, 60))          # post-window PLV (for heatmaps)
    reg_plv_post = np.zeros((nb, nc, len(PAIRS)))
    reg_iplv_post = np.zeros((nb, nc, len(PAIRS)))
    reg_plv_base = np.zeros((nb, nc, len(PAIRS)))
    reg_plv_t = np.zeros((nb, nc, len(PAIRS), X.shape[2]))

    for bi, (lo, hi) in enumerate(BANDS.values()):
        sos = _sos(lo, hi)
        analytic = hilbert(sosfiltfilt(sos, X, axis=2), axis=2)
        cp = np.exp(1j * np.angle(analytic))       # unit phasors (n, 60, T)
        for ci, cond in enumerate(conds):
            sel = y == cond
            cpc = cp[sel]                          # (nc_trials, 60, T)
            n = cpc.shape[0]
            # full-epoch cross phasor mean: M[c,d,t] = <exp(i(φc-φd))>_trials
            Mt = np.einsum("nct,ndt->cdt", cpc, np.conj(cpc)) / n   # (60,60,T) complex
            plv_t = np.abs(Mt)                     # (60,60,T)
            iplv_t = np.abs(Mt.imag)
            # window means
            plv_post = plv_t[:, :, post_m].mean(2)
            iplv_post = iplv_t[:, :, post_m].mean(2)
            plv_base = plv_t[:, :, base_m].mean(2)
            chan_plv[bi, ci] = plv_post
            for pi, (a, b) in enumerate(PAIRS):
                same = a == b
                reg_plv_post[bi, ci, pi] = _region_val(plv_post, ridx[a], ridx[b], same)
                reg_iplv_post[bi, ci, pi] = _region_val(iplv_post, ridx[a], ridx[b], same)
                reg_plv_base[bi, ci, pi] = _region_val(plv_base, ridx[a], ridx[b], same)
                # region time-course (mean of |Mt| over the region's channel pairs)
                sub = plv_t[np.ix_(ridx[a], ridx[b])]
                if same:
                    m = ~np.eye(len(ridx[a]), dtype=bool)
                    reg_plv_t[bi, ci, pi] = sub[m].mean(0)
                else:
                    reg_plv_t[bi, ci, pi] = sub.reshape(-1, sub.shape[-1]).mean(0)
    return chan_plv, reg_plv_post, reg_iplv_post, reg_plv_base, reg_plv_t, times


def main(n_jobs=4):
    os.makedirs(OUT, exist_ok=True)
    files = sorted(glob.glob(os.path.join(DATA, "*.npz")))
    print(f"Connectivity analysis | {len(files)} subjects | regions {list(REGIONS)} | n_jobs={n_jobs}")
    t0 = time.time()
    res = Parallel(n_jobs=n_jobs, verbose=5, max_nbytes=None)(
        delayed(_one_subject)(f) for f in files)
    print(f"  computed in {time.time()-t0:.1f}s")

    chan_plv = np.mean([r[0] for r in res], axis=0)                 # (nb,nc,60,60)
    reg_plv_post = np.stack([r[1] for r in res])                    # (S,nb,nc,npair)
    reg_iplv_post = np.stack([r[2] for r in res])
    reg_plv_base = np.stack([r[3] for r in res])
    reg_plv_t = np.mean([r[4] for r in res], axis=0)               # (nb,nc,npair,T)
    times = res[0][5]

    bands = list(BANDS); conds = ["no_stim", "medium", "max"]
    induced = reg_plv_post - reg_plv_base                           # (S,nb,nc,npair)
    induced_iplv = reg_iplv_post - reg_plv_base * 0                 # iPLV baseline ~0; keep raw iPLV
    # (baseline iPLV is near zero by construction; use raw iPLV post as the induced value)

    # ── stats: Friedman across conditions, per band, per BETWEEN pair ──
    stats = {}
    for measure, arr in [("PLV_induced", induced), ("iPLV_post", reg_iplv_post)]:
        stats[measure] = {}
        for bi, band in enumerate(bands):
            for pi, (a, b) in enumerate(PAIRS):
                if (a, b) not in BETWEEN:
                    continue
                vals = [arr[:, bi, ci, pi] for ci in range(3)]     # 3 x (S,)
                try:
                    chi2, p = friedmanchisquare(*vals)
                except Exception:
                    chi2, p = float("nan"), float("nan")
                means = [float(np.mean(v)) for v in vals]
                stats[measure][f"{band}:{a}-{b}"] = {
                    "chi2": float(chi2), "p": float(p),
                    "mean_per_condition": dict(zip(conds, means)),
                    "trend_max_minus_nostim": means[2] - means[0]}

    # ── figures ──
    _dose_fig(induced, bands, "PLV (induced, post − baseline)", stats["PLV_induced"],
              os.path.join(OUT, "dose_response_PLV.png"))
    _dose_fig(reg_iplv_post, bands, "iPLV (post, volume-conduction robust)", stats["iPLV_post"],
              os.path.join(OUT, "dose_response_iPLV.png"))
    _heatmaps(chan_plv, bands, os.path.join(OUT, "region_heatmaps.png"))
    _timecourse(reg_plv_t, times, bands, stats["PLV_induced"], os.path.join(OUT, "timecourse.png"))

    # ── save + report ──
    def reg_summary(arr):
        return {band: {f"{a}-{b}": {c: float(arr[:, bi, ci, pi].mean())
                                    for ci, c in enumerate(conds)}
                       for pi, (a, b) in enumerate(PAIRS)}
                for bi, band in enumerate(bands)}
    out = {"data": DATA, "regions": REGIONS, "bands": BANDS,
           "post_window": POST_WIN, "baseline_window": BASE_WIN,
           "PLV_post": reg_summary(reg_plv_post),
           "PLV_baseline": reg_summary(reg_plv_base),
           "PLV_induced": reg_summary(induced),
           "iPLV_post": reg_summary(reg_iplv_post),
           "stats_friedman": stats}
    json.dump(out, open(os.path.join(OUT, "connectivity_results.json"), "w"), indent=2)

    print("\n=== Significant inter-region condition effects (Friedman p<0.05) ===")
    hits = []
    for measure in ("PLV_induced", "iPLV_post"):
        for key, s in stats[measure].items():
            if s["p"] < 0.05:
                hits.append((measure, key, s["p"], s["trend_max_minus_nostim"]))
    for measure, key, p, tr in sorted(hits, key=lambda x: x[2]):
        arrow = "up with intensity" if tr > 0 else "DOWN with intensity"
        print(f"  {measure:>12} {key:>14}  p={p:.4f}  ({arrow}, Δ={tr:+.3f})")
    if not hits:
        print("  none reached p<0.05")
    print(f"\nSaved -> {OUT}/connectivity_results.json + 4 figures")


def _dose_fig(arr, bands, title, stat, path):
    fig, axes = plt.subplots(1, len(bands), figsize=(3.0 * len(bands), 3.3), dpi=170, sharey=True)
    x = np.arange(3); w = 0.26
    labels = ["FC-C", "FC-P", "C-P"]
    for bi, (band, ax) in enumerate(zip(bands, axes)):
        for k, lab in enumerate(labels):
            pi = PAIRS.index(BETWEEN[k])
            vals = [arr[:, bi, ci, pi].mean() for ci in range(3)]
            errs = [arr[:, bi, ci, pi].std() / np.sqrt(arr.shape[0]) for ci in range(3)]
            ax.bar(x + (k - 1) * w, vals, w, yerr=errs, capsize=2,
                   color=["#9EB3C2", "#1C7293", "#B85042"][k], label=lab, alpha=0.9)
            s = stat.get(f"{band}:{BETWEEN[k][0]}-{BETWEEN[k][1]}", {})
            if s.get("p", 1) < 0.05:
                ax.text((k - 1) * w + 1, max(vals) + max(errs), "*", ha="center", fontsize=14, color="black")
        ax.set_title(band, fontsize=10, fontweight="bold", color=NAVY)
        ax.set_xticks(x); ax.set_xticklabels(["no-stim", "med", "max"], fontsize=7.5)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel(title, fontsize=9)
    axes[-1].legend(title="region pair", fontsize=7, title_fontsize=7)
    fig.suptitle(f"Inter-region coupling vs stimulation intensity — {title}\n(* Friedman p<0.05)",
                 fontsize=11, fontweight="bold", color=NAVY, y=1.06)
    fig.tight_layout(); fig.savefig(path, bbox_inches="tight"); plt.close()


def _heatmaps(chan_plv, bands, path):
    # region 3x3 matrices for max condition and (max − no_stim)
    def reg_mat(cp):
        idx = {r: [i for i in range(60)] for r in REG_ORDER}  # placeholder; recompute below
        return cp
    # rebuild region indices from a fresh load
    import glob as _g
    d = np.load(sorted(_g.glob(os.path.join(DATA, "*.npz")))[0], allow_pickle=True)
    ch = [str(c) for c in d["channel_names"]]
    ridx = {r: [ch.index(c) for c in chs if c in ch] for r, chs in REGIONS.items()}
    def to_region(mat):
        R = np.zeros((3, 3))
        for a in range(3):
            for b in range(3):
                R[a, b] = _region_val(mat, ridx[REG_ORDER[a]], ridx[REG_ORDER[b]], a == b)
        return R
    fig, axes = plt.subplots(len(bands), 2, figsize=(6.2, 2.5 * len(bands)), dpi=150)
    for bi, band in enumerate(bands):
        mx = to_region(chan_plv[bi, 2]); ns = to_region(chan_plv[bi, 0])
        for j, (M, ttl, cmap, vc) in enumerate([(mx, "max PLV", "Blues", None),
                                                (mx - ns, "max − no-stim", "RdBu_r", None)]):
            ax = axes[bi, j]
            vmax = np.abs(M).max() if vc is None else vc
            vmin = -vmax if cmap == "RdBu_r" else 0
            im = ax.imshow(M, cmap=cmap, vmin=vmin, vmax=vmax)
            for a in range(3):
                for b in range(3):
                    ax.text(b, a, f"{M[a,b]:.2f}", ha="center", va="center", fontsize=8,
                            color="black")
            ax.set_xticks(range(3)); ax.set_yticks(range(3))
            ax.set_xticklabels(REG_ORDER, fontsize=8); ax.set_yticklabels(REG_ORDER, fontsize=8)
            if j == 0:
                ax.set_ylabel(band, fontsize=10, fontweight="bold", color=NAVY)
            if bi == 0:
                ax.set_title(ttl, fontsize=9, fontweight="bold", color=NAVY)
    fig.suptitle("Region×region PLV (post-stim)", fontsize=11, fontweight="bold", color=NAVY, y=1.0)
    fig.tight_layout(); fig.savefig(path, bbox_inches="tight"); plt.close()


def _timecourse(reg_plv_t, times, bands, stat, path):
    # pick the most significant band/between-pair
    best = min(stat.items(), key=lambda kv: (kv[1]["p"] if not np.isnan(kv[1]["p"]) else 1))
    band, pair = best[0].split(":")
    bi = bands.index(band); pi = PAIRS.index(tuple(pair.split("-")))
    fig, ax = plt.subplots(figsize=(6, 3.4), dpi=170)
    for ci, (c, col) in enumerate(zip(["no-stim", "medium", "max"], COND_COLORS)):
        ax.plot(times * 1000, reg_plv_t[bi, ci, pi], color=col, lw=1.8, label=c)
    ax.axvline(0, color="black", lw=0.6, ls=":")
    ax.set_xlabel("time (ms)"); ax.set_ylabel(f"{pair} PLV ({band})")
    ax.set_title(f"Phase-locked coupling over time — {pair}, {band} band (most modulated)\n"
                 f"Friedman p={best[1]['p']:.4f}", fontsize=10.5, fontweight="bold", color=NAVY)
    ax.legend(fontsize=8); ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(path, bbox_inches="tight"); plt.close()


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--jobs", type=int, default=4)
    main(n_jobs=ap.parse_args().jobs)
