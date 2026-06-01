"""
view_epochs.py — load and visualise EEG epochs saved by the collector.

Fixes from previous version:
  - channel_names is now ALWAYS padded/trimmed to match the real channel
    count in the data, so it can never raise "list index out of range"
    (the X.on headset sends extra channels, e.g. 7 EEG + 1 AUX).
  - Safe handling when no metadata file is present.
  - welch nperseg is clamped to the epoch length.

Run it three ways:
  python view_epochs.py                         # auto-find .npy near this script
  python view_epochs.py path\to\epochs.npy      # explicit file
  (or drag-and-drop the .npy onto this file in Explorer)
"""

import numpy as np
import json
import os
import sys
import glob
import matplotlib.pyplot as plt
from scipy.signal import welch


# ── Find the .npy file ──────────────────────────────────────
def find_npy_file():
    # 1) path passed as an argument
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if os.path.exists(path):
            return path
        print(f"File not found: {path}")
        sys.exit()

    # 2) search for .npy files near this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    matches = sorted(glob.glob(os.path.join(script_dir, '**', '*.npy'), recursive=True))

    if not matches:
        print("No .npy files found. Pass the path as an argument:")
        print("  python view_epochs.py path/to/epochs.npy")
        sys.exit()

    if len(matches) == 1:
        print(f"Found: {matches[0]}")
        return matches[0]

    # 3) multiple files — let the user pick
    print("Multiple .npy files found — pick one:\n")
    for i, m in enumerate(matches):
        print(f"  [{i + 1}] {m}")
    print()
    while True:
        try:
            choice = int(input("Enter number: ")) - 1
            if 0 <= choice < len(matches):
                return matches[choice]
        except ValueError:
            pass
        print("Invalid choice, try again")


# ── Load data ───────────────────────────────────────────────
npy_path = find_npy_file()
json_path = npy_path.replace('.npy', '_meta.json')

data = np.load(npy_path)  # expected shape: (n_epochs, n_channels, n_samples)

# guard against a single-epoch file saved as 2D (n_channels, n_samples)
if data.ndim == 2:
    data = data[np.newaxis, ...]

if data.ndim != 3:
    print(f"Unexpected data shape {data.shape} — expected 3D "
          f"(epochs, channels, samples). Aborting.")
    sys.exit()

n_epochs, n_ch, n_samples = data.shape
print(f"\nLoaded: {npy_path}")
print(f"Shape:  {data.shape}  (epochs x channels x samples)")

# ── Load metadata (with sensible fallbacks) ─────────────────
if os.path.exists(json_path):
    with open(json_path) as f:
        meta = json.load(f)
    srate = float(meta.get('srate', 250.0))
    channel_names = list(meta.get('channel_names', []))
    pre_ms = meta.get('pre_ms', 200)
    post_ms = meta.get('post_ms', 1000)
    print(f"Metadata loaded — {meta.get('n_epochs', n_epochs)} epochs @ {srate}Hz")
else:
    print("No metadata file found — using defaults")
    srate = 250.0
    pre_ms = 200
    post_ms = 1000
    channel_names = []

# ── THE FIX: make channel_names exactly n_ch long ───────────
# Pad with Ch7, Ch8, ... if the data has more channels than names,
# and trim if it somehow has fewer. This makes channel_names[ch]
# safe for every ch in range(n_ch).
if len(channel_names) < n_ch:
    channel_names = channel_names + [f'Ch{i}' for i in range(len(channel_names), n_ch)]
else:
    channel_names = channel_names[:n_ch]

print(f"Channels: {channel_names}")

# time axis in ms, from -pre_ms up to +post_ms
times = np.linspace(-pre_ms, post_ms, n_samples)


# ── Plot 1: ERP — all epochs + average per channel ──────────
def plot_erp():
    fig, axes = plt.subplots(n_ch, 1, figsize=(12, 2.5 * n_ch), sharex=True)
    if n_ch == 1:
        axes = [axes]

    fig.suptitle('ERP — Individual Epochs + Average', fontsize=14)

    for ch in range(n_ch):
        ax = axes[ch]

        # each epoch in light grey
        for ep in range(n_epochs):
            ax.plot(times, data[ep, ch, :], color='lightgrey',
                    linewidth=0.8, alpha=0.7)

        # bold average across epochs
        avg = data[:, ch, :].mean(axis=0)
        ax.plot(times, avg, color='steelblue', linewidth=2, label='Average')

        ax.axvline(x=0, color='red', linestyle='--', linewidth=1, label='Stimulus')
        ax.axvspan(-pre_ms, 0, alpha=0.05, color='green', label='Baseline')

        ax.set_ylabel(f'{channel_names[ch]}\n(µV)', fontsize=9)
        ax.set_xlim(-pre_ms, post_ms)
        ax.grid(True, alpha=0.3)
        if ch == 0:
            ax.legend(loc='upper right', fontsize=8)

    axes[-1].set_xlabel('Time (ms)', fontsize=11)
    plt.tight_layout()
    out = npy_path.replace('.npy', '_erp.png')
    plt.savefig(out, dpi=150)
    print(f"Saved ERP plot     → {out}")
    plt.show()


# ── Plot 2: PSD per channel (averaged across epochs) ────────
def plot_fft():
    fig, axes = plt.subplots(n_ch, 1, figsize=(12, 2.5 * n_ch), sharex=True)
    if n_ch == 1:
        axes = [axes]

    fig.suptitle('Power Spectral Density (averaged across epochs)', fontsize=14)

    band_colours = {
        'Delta (0.5–4Hz)': (0.5, 4, 'blue'),
        'Theta (4–8Hz)':   (4, 8, 'green'),
        'Alpha (8–13Hz)':  (8, 13, 'gold'),
        'Beta (13–30Hz)':  (13, 30, 'orange'),
        'Gamma (30–50Hz)': (30, 50, 'red'),
    }

    nperseg = min(int(srate * 2), n_samples)

    for ch in range(n_ch):
        ax = axes[ch]
        psds = []
        for ep in range(n_epochs):
            freqs, psd = welch(data[ep, ch, :], fs=srate, nperseg=nperseg)
            psds.append(psd)

        avg_psd = np.mean(psds, axis=0)
        mask = freqs <= 50
        ax.semilogy(freqs[mask], avg_psd[mask], color='steelblue', linewidth=1.5)

        for label, (flo, fhi, colour) in band_colours.items():
            ax.axvspan(flo, fhi, alpha=0.1, color=colour,
                       label=label if ch == 0 else '')

        ax.set_ylabel(channel_names[ch], fontsize=9)
        ax.grid(True, alpha=0.3)
        if ch == 0:
            ax.legend(loc='upper right', fontsize=7, ncol=2)

    axes[-1].set_xlabel('Frequency (Hz)', fontsize=11)
    plt.tight_layout()
    out = npy_path.replace('.npy', '_fft.png')
    plt.savefig(out, dpi=150)
    print(f"Saved FFT plot     → {out}")
    plt.show()


# ── Plot 3: Heatmap — all epochs side by side per channel ───
def plot_heatmap():
    fig, axes = plt.subplots(1, n_ch, figsize=(3 * n_ch, 6), sharey=True)
    if n_ch == 1:
        axes = [axes]

    fig.suptitle('Epoch Heatmap (time × epoch per channel)', fontsize=14)

    for ch in range(n_ch):
        ax = axes[ch]
        img = data[:, ch, :].T  # (n_samples, n_epochs)
        vmax = np.percentile(np.abs(img), 95)
        vmax = vmax if vmax > 0 else 1.0  # avoid all-zero colour scale

        ax.imshow(img, aspect='auto', origin='lower', cmap='RdBu_r',
                  vmin=-vmax, vmax=vmax,
                  extent=[0, n_epochs, -pre_ms, post_ms])
        ax.axhline(y=0, color='black', linestyle='--', linewidth=1)
        ax.set_title(channel_names[ch], fontsize=9)
        ax.set_xlabel('Epoch #', fontsize=8)

    axes[0].set_ylabel('Time (ms)', fontsize=10)
    plt.tight_layout()
    out = npy_path.replace('.npy', '_heatmap.png')
    plt.savefig(out, dpi=150)
    print(f"Saved heatmap plot → {out}")
    plt.show()


# ── Optional: view each epoch on its own (all channels overlaid) ─
def plot_each_epoch():
    cols = min(4, n_epochs)
    rows = int(np.ceil(n_epochs / cols))
    fig, axes = plt.subplots(rows, cols, figsize=(4 * cols, 3 * rows),
                             squeeze=False, sharex=True)

    fig.suptitle('Each Epoch (all channels overlaid)', fontsize=14)

    for ep in range(n_epochs):
        ax = axes[ep // cols][ep % cols]
        for ch in range(n_ch):
            ax.plot(times, data[ep, ch, :], linewidth=0.8,
                    label=channel_names[ch])
        ax.axvline(x=0, color='red', linestyle='--', linewidth=1)
        ax.set_title(f'Epoch {ep + 1}', fontsize=10)
        ax.set_xlim(-pre_ms, post_ms)
        ax.grid(True, alpha=0.3)

    # hide any unused subplots
    for k in range(n_epochs, rows * cols):
        axes[k // cols][k % cols].axis('off')

    axes[0][0].legend(loc='upper right', fontsize=6, ncol=2)
    plt.tight_layout()
    out = npy_path.replace('.npy', '_each_epoch.png')
    plt.savefig(out, dpi=150)
    print(f"Saved per-epoch    → {out}")
    plt.show()


# ── Summary ─────────────────────────────────────────────────
def print_summary():
    print(f"\n{'─' * 50}")
    print(f"  File:       {os.path.basename(npy_path)}")
    print(f"  Epochs:     {n_epochs}")
    print(f"  Channels:   {n_ch} {channel_names}")
    print(f"  Samples:    {n_samples} per epoch")
    print(f"  Duration:   -{pre_ms}ms to +{post_ms}ms")
    print(f"  Srate:      {srate}Hz")
    print(f"  Data range: {data.min():.1f} to {data.max():.1f} µV")
    print(f"{'─' * 50}\n")


# ── Run everything ──────────────────────────────────────────
if __name__ == '__main__':
    print_summary()
    plot_erp()
    plot_fft()
    plot_heatmap()
    plot_each_epoch()   # remove this line if you don't want the per-epoch grid