"""
erd_ers_plot.py
===============
Illustrate ERD/ERS as condition-split time courses, in a grid:

    rows    = channels you choose (CONFIG["channels"])
    columns = frequency bands     (CONFIG["bands"])
    each cell = band power in dB vs pre-stim baseline, over time, one line per
                stimulation-intensity condition (3- or 4-class, auto-detected)

This is the canonical Pfurtscheller ERD/ERS figure: a power DROP below the
0 dB baseline is desynchronization (ERD), a RISE above it is synchronization
(ERS). Splitting by condition shows whether intensity grades the response --
the decoding rationale behind tf_features.py.

It reuses the SAME filter-Hilbert and dB definition as tf_features.py
(sosfiltfilt + Hilbert power, 10*log10(power/baseline)), so these curves are
exactly what the TFExtractor summarizes into erd_early/erd_late/erd_peak/ers_peak.

Grand average: for each subject we average the dB time course across trials
within a condition, then average those per-subject curves across subjects
(optional SEM shading). This avoids letting high-trial subjects dominate.

Edit CONFIG and run:  python erd_ers_plot.py
"""

from __future__ import annotations
import os, json, warnings
import numpy as np

warnings.filterwarnings("ignore")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.signal import sosfiltfilt, hilbert

from train_combined import load_dataset
from tf_features import BANDS, BASELINE_WIN, _design_sos, PWR_EPS

# ─────────────────────────────────────────────
# CONFIG  (in-file; no CLI)
# ─────────────────────────────────────────────
CONFIG = {
    "data_folder": "data/og-ds-t-3c",
    "output_dir":  "Results/erd_ers_3c",

    # rows of the grid: list the channels you want to see ERD/ERS for
    "channels":    ["FCz", "Cz", "C4", "C2"],

    # columns of the grid: which bands (None = all five, in canonical order)
    "bands":       ["delta", "theta", "alpha", "beta", "gamma"],

    "smooth_ms":      100.0,   # display smoothing of the dB curve
    "show_sem":       True,    # shade +/- SEM across subjects
    "shade_windows":  True,    # light shading for early (0-0.3) and late (0.3-1.5)
    "early_win":      (0.0, 0.3),
    "late_win":       (0.3, 1.5),
    "filter_order":   4,
    "artifact_filter": True,
    "save_curves_json": True,
}

COND_COLORS = ["#9EB3C2", "#1C7293", "#21295C", "#B85042"]  # up to 4 conditions
MID = "#21295C"; GREY = "#64748B"


def _smooth(x, k):
    if k <= 1:
        return x
    k = int(k) | 1
    ker = np.ones(k) / k
    pad = k // 2
    xp = np.pad(x, [(0, 0)] * (x.ndim - 1) + [(pad, pad)], mode="edge")
    return np.apply_along_axis(lambda m: np.convolve(m, ker, mode="valid"), -1, xp)


def db_timecourse(power, base_mask):
    """power:(trials,time) -> dB vs per-trial baseline mean (matches tf_features)."""
    ref = power[:, base_mask].mean(axis=1, keepdims=True)
    return 10.0 * np.log10((power + PWR_EPS) / (ref + PWR_EPS))


def compute_curves(subjects, channels, bands, fs_order, smooth_ms):
    """
    Returns:
      curves[band][ch][cond] -> (n_subjects, T) per-subject condition-mean dB
      times, classes, class_names
    """
    times = np.asarray(subjects[0]["meta"]["times"])
    sfreq = float(subjects[0]["meta"]["sfreq"])
    base_mask = (times >= BASELINE_WIN[0]) & (times <= BASELINE_WIN[1])
    ksm = int(round(smooth_ms / 1000.0 * sfreq))
    classes = np.unique(subjects[0]["y"])
    class_names = subjects[0]["meta"].get("class_names") or [str(c) for c in classes]

    sos = {b: _design_sos(*BANDS[b], sfreq, fs_order) for b in bands}
    curves = {b: {ch: {int(c): [] for c in classes} for ch in channels} for b in bands}

    for s in subjects:
        meta = s["meta"]; ch_names = list(meta["channel_names"])
        idx = {ch: ch_names.index(ch) for ch in channels if ch in ch_names}
        if len(idx) < len(channels):
            missing = [c for c in channels if c not in idx]
            raise ValueError(f"{s['subject_id']}: channels not found: {missing}")
        Xc = s["X"][:, [idx[ch] for ch in channels], :]      # (trials, nch, T)
        y = s["y"]
        for b in bands:
            filt = sosfiltfilt(sos[b], Xc, axis=-1)
            power = np.abs(hilbert(filt, axis=-1)) ** 2       # (trials, nch, T)
            for ci, ch in enumerate(channels):
                db = db_timecourse(power[:, ci, :], base_mask)   # (trials, T)
                if ksm > 1:
                    db = _smooth(db, ksm)
                for c in classes:
                    m = db[y == c].mean(axis=0)                  # (T,)
                    curves[b][ch][int(c)].append(m)
    # stack subjects
    for b in bands:
        for ch in channels:
            for c in classes:
                curves[b][ch][int(c)] = np.vstack(curves[b][ch][int(c)])
    return curves, times, classes, class_names


def plot_grid(curves, times, classes, class_names, cfg, n_classes, out_png):
    channels = cfg["channels"]; bands = cfg["bands"]
    nrow, ncol = len(channels), len(bands)
    fig, axes = plt.subplots(nrow, ncol, figsize=(3.0 * ncol, 2.2 * nrow),
                             dpi=160, squeeze=False)

    # per-band (column) shared y-limits for fair comparison across channels
    col_ylim = []
    for b in bands:
        lo, hi = np.inf, -np.inf
        for ch in channels:
            for c in classes:
                arr = curves[b][ch][int(c)].mean(axis=0)
                lo = min(lo, arr.min()); hi = max(hi, arr.max())
        pad = 0.08 * (hi - lo + 1e-9)
        col_ylim.append((lo - pad, hi + pad))

    for r, ch in enumerate(channels):
        for cidx, b in enumerate(bands):
            ax = axes[r][cidx]
            if cfg["shade_windows"]:
                ax.axvspan(*cfg["early_win"], color="#F0997B", alpha=0.10, lw=0)
                ax.axvspan(*cfg["late_win"], color="#F0997B", alpha=0.05, lw=0)
            ax.axhline(0, color=GREY, lw=0.8, ls="--", alpha=0.7)
            ax.axvline(0, color=MID, lw=1.0, alpha=0.7)
            for k, c in enumerate(classes):
                stack = curves[b][ch][int(c)]            # (n_subj, T)
                gm = stack.mean(axis=0)
                col = COND_COLORS[k % 4]
                ax.plot(times, gm, color=col, lw=1.6,
                        label=class_names[int(c)] if (r == 0 and cidx == 0) else None)
                if cfg["show_sem"] and stack.shape[0] > 1:
                    sem = stack.std(axis=0) / np.sqrt(stack.shape[0])
                    ax.fill_between(times, gm - sem, gm + sem, color=col, alpha=0.15, lw=0)
            ax.set_ylim(*col_ylim[cidx])
            ax.set_xlim(times[0], times[-1])
            ax.spines[["top", "right"]].set_visible(False)
            ax.tick_params(labelsize=7)
            if r == 0:
                ax.set_title(b, fontsize=12, fontweight="bold", color=MID)
            if cidx == 0:
                ax.set_ylabel(f"{ch}\ndB", fontsize=9, fontweight="bold", color=MID)
            if r == nrow - 1:
                ax.set_xlabel("time (s)", fontsize=8, color=GREY)

    handles, labels = axes[0][0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=len(classes),
               fontsize=9, frameon=False, bbox_to_anchor=(0.5, 1.005))
    fig.suptitle(f"ERD/ERS time courses ({n_classes}-class)  "
                 f"\u2014  below 0 dB = desync (ERD), above = sync (ERS)",
                 fontsize=12.5, fontweight="bold", color=MID, y=1.04)
    fig.tight_layout(rect=[0, 0, 1, 0.99])
    fig.savefig(out_png, bbox_inches="tight"); plt.close()


def main(cfg=CONFIG):
    os.makedirs(cfg["output_dir"], exist_ok=True)
    bands = cfg["bands"] or list(BANDS)
    cfg = {**cfg, "bands": bands}
    subjects = load_dataset(cfg["data_folder"], artifact_filter=cfg["artifact_filter"])
    n_classes = len(np.unique(subjects[0]["y"]))
    print(f"Loaded {len(subjects)} subjects | {n_classes} classes")
    print(f"Grid: {len(cfg['channels'])} channels x {len(bands)} bands "
          f"= {len(cfg['channels'])*len(bands)} cells")

    curves, times, classes, class_names = compute_curves(
        subjects, cfg["channels"], bands, cfg["filter_order"], cfg["smooth_ms"])

    out_png = os.path.join(cfg["output_dir"], f"erd_ers_{n_classes}c.png")
    plot_grid(curves, times, classes, class_names, cfg, n_classes, out_png)
    print(f"Saved -> {out_png}")

    if cfg["save_curves_json"]:
        grand = {b: {ch: {class_names[int(c)]: curves[b][ch][int(c)].mean(axis=0).tolist()
                          for c in classes}
                     for ch in cfg["channels"]} for b in bands}
        jpath = os.path.join(cfg["output_dir"], f"erd_ers_{n_classes}c.json")
        with open(jpath, "w") as f:
            json.dump({"times": times.tolist(), "conditions": list(class_names),
                       "channels": cfg["channels"], "bands": bands,
                       "grand_mean_db": grand}, f)
        print(f"Saved -> {jpath}")


if __name__ == "__main__":
    main()