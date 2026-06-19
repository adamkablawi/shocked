"""
erp_channel_grid_4class.py
==========================
Display ERP plots for a fixed set of channels, one plot per channel per subject,
across a directory of 4-class .npz subject files (no_stim / min / medium / max).

Built for the baseline-included, downsampled dataset:
    sfreq 250 Hz, window -0.2 to 1.5 s, 4 stimulation classes.

Layout: ONE ROW PER SUBJECT, ONE COLUMN PER CHANNEL. Each cell is the
trial-averaged ERP with one line per stimulation condition. Scan down a column
to see whether the dose-dependent trend holds across subjects.

Usage:
    python erp_channel_grid_4class.py /path/to/npz_folder
    python erp_channel_grid_4class.py /path/to/npz_folder --save grid.png
    python erp_channel_grid_4class.py /path/to/npz_folder --window -0.2 0.5
"""

import argparse, glob, os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
CHANNELS = ["C3", "Cz", "C4", "FCz", "FC1", "FC2", "FC3", "FC4"]

# Default display window (s). Includes the pre-stim baseline now that it's back.
WIN_START = -0.2
WIN_END   = 0.5

# Baseline-correction window (s). Each epoch has its pre-stim mean subtracted
# over this range before plotting. Set BASELINE_CORRECT = False to disable.
BASELINE_CORRECT = True
BASELINE_START = -0.2
BASELINE_END   = 0.0

# Per-cell size in inches.
CELL_W = 1.7
CELL_H = 1.15

# Autosave (no --save needed).
AUTOSAVE = True
AUTOSAVE_DPI = 150
AUTOSAVE_EXT = "pdf"

# One color per condition, in class_names order (4 classes here).
CONDITION_COLORS = ["#888888", "#4daf4a", "#377eb8", "#e41a1c", "#984ea3"]


# ─────────────────────────────────────────────
# LOADING
# ─────────────────────────────────────────────
def load_subject(path):
    d = np.load(path, allow_pickle=True)
    X = np.asarray(d["X"], dtype=float)
    if X.std() < 1e-3:              # volts -> microvolts
        X = X * 1e6
    y = np.asarray(d["y"]).astype(int)
    meta = {
        "sfreq":         float(d["sfreq"]) if "sfreq" in d else 250.0,
        "channel_names": [str(c) for c in d["channel_names"]],
        "class_names":   [str(c) for c in d["class_names"]] if "class_names" in d else None,
        "subject_id":    str(d["subject_id"]) if "subject_id" in d else Path(path).stem,
        "tmin":          float(d["epoch_tmin"]) if "epoch_tmin" in d else -0.2,
        "tmax":          float(d["epoch_tmax"]) if "epoch_tmax" in d else 1.5,
    }
    return X, y, meta


def baseline_correct(X, times):
    """Subtract per-epoch, per-channel mean over the baseline window."""
    bmask = (times >= BASELINE_START) & (times <= BASELINE_END)
    if bmask.sum() == 0:           # no pre-stim samples available; skip safely
        return X
    base = X[:, :, bmask].mean(axis=2, keepdims=True)
    return X - base


# ─────────────────────────────────────────────
# PLOT
# ─────────────────────────────────────────────
def build_grid(folder, channels=CHANNELS, win=(WIN_START, WIN_END)):
    files = sorted(glob.glob(os.path.join(folder, "*.npz")))
    if not files:
        raise FileNotFoundError(f"No .npz files found in {folder}")

    n_sub, n_ch = len(files), len(channels)
    fig, axes = plt.subplots(
        n_sub, n_ch,
        figsize=(n_ch * CELL_W, n_sub * CELL_H),
        sharex=True, squeeze=False,
    )

    ymins = [np.inf] * n_ch
    ymaxs = [-np.inf] * n_ch
    cond_labels = None

    for r, f in enumerate(files):
        X, y, meta = load_subject(f)
        ch_names = meta["channel_names"]
        times = np.linspace(meta["tmin"], meta["tmax"], X.shape[2])
        if BASELINE_CORRECT:
            X = baseline_correct(X, times)
        wmask = (times >= win[0]) & (times <= win[1])
        tw = times[wmask]
        conds = sorted(np.unique(y))
        if cond_labels is None:
            cn = meta["class_names"]
            cond_labels = [cn[c] if cn else str(c) for c in conds]

        for col, chname in enumerate(channels):
            ax = axes[r][col]
            if chname not in ch_names:
                ax.text(0.5, 0.5, f"{chname}\nN/A", ha="center", va="center",
                        fontsize=6, color="red", transform=ax.transAxes)
                ax.set_xticks([]); ax.set_yticks([])
                continue
            ci = ch_names.index(chname)
            for k, c in enumerate(conds):
                erp = X[y == c][:, ci, :][:, wmask].mean(axis=0)
                ax.plot(tw * 1000, erp,
                        color=CONDITION_COLORS[k % len(CONDITION_COLORS)], lw=0.9)
                ymins[col] = min(ymins[col], erp.min())
                ymaxs[col] = max(ymaxs[col], erp.max())
            ax.axvline(0, color="black", lw=0.5, ls=":")   # stimulus onset
            ax.axhline(0, color="gray", lw=0.4, ls="--")
            ax.tick_params(labelsize=4, length=2)
            if r == 0:
                ax.set_title(chname, fontsize=8, fontweight="bold")
            if col == 0:
                ax.set_ylabel(meta["subject_id"], fontsize=5, rotation=0,
                              ha="right", va="center", labelpad=14)

    for col in range(n_ch):
        if np.isfinite(ymins[col]):
            pad = 0.08 * (ymaxs[col] - ymins[col] + 1e-9)
            for r in range(n_sub):
                axes[r][col].set_ylim(ymins[col] - pad, ymaxs[col] + pad)

    handles = [plt.Line2D([0], [0], color=CONDITION_COLORS[k % len(CONDITION_COLORS)], lw=2)
               for k in range(len(cond_labels))]
    fig.legend(handles, cond_labels, loc="upper center", ncol=len(cond_labels),
               fontsize=8, frameon=True, bbox_to_anchor=(0.5, 1.005))
    bc = " (baseline-corrected)" if BASELINE_CORRECT else ""
    fig.supxlabel("Time (ms)  \u2014  vertical line = stimulus onset", fontsize=9)
    fig.suptitle(f"Evoked response by channel \u00D7 subject  "
                 f"({n_sub} subjects, {win[0]*1000:.0f}\u2013{win[1]*1000:.0f} ms){bc}",
                 fontsize=11, y=1.015)
    fig.tight_layout(rect=[0.02, 0.0, 1, 0.99])
    return fig


def main():
    p = argparse.ArgumentParser(description="Per-channel per-subject ERP grid (4-class)")
    p.add_argument("folder", help="Directory containing 4-class .npz subject files")
    p.add_argument("--save", default=None, help="Explicit output path (overrides autosave)")
    p.add_argument("--no-autosave", action="store_true", help="Disable autosave; just show")
    p.add_argument("--show", action="store_true", help="Also open the window after autosaving")
    p.add_argument("--no-baseline", action="store_true", help="Disable baseline correction")
    p.add_argument("--window", nargs=2, type=float, default=[WIN_START, WIN_END],
                   metavar=("START", "END"), help="Time window in seconds (default -0.2 0.5)")
    p.add_argument("--channels", nargs="+", default=CHANNELS, help="Override channel list")
    args = p.parse_args()

    global BASELINE_CORRECT
    if args.no_baseline:
        BASELINE_CORRECT = False

    fig = build_grid(args.folder, channels=args.channels, win=tuple(args.window))

    out = args.save
    if out is None and AUTOSAVE and not args.no_autosave:
        folder_name = os.path.basename(os.path.normpath(args.folder)) or "erp_grid"
        out = f"{folder_name}_erp_grid_4class.{AUTOSAVE_EXT}"

    if out:
        fig.savefig(out, dpi=AUTOSAVE_DPI, bbox_inches="tight")
        print(f"Saved to {os.path.abspath(out)}")
        if args.show:
            plt.show()
    else:
        plt.show()


if __name__ == "__main__":
    main()