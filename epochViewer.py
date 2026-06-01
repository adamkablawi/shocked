import numpy as np
import json
import os
import sys
import glob
import matplotlib.pyplot as plt
from scipy.signal import welch

# ── Find the .npy file ──────────────────────────────────────
# Option 1: drag and drop the .npy onto this script
# Option 2: pass the path as an argument: python view_epochs.py path/to/file.npy
# Option 3: script will show a list of available files to pick from

def find_npy_file():
    # check if a path was passed as argument
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if os.path.exists(path):
            return path
        else:
            print(f"File not found: {path}")
            exit()

    # otherwise search for .npy files near this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    matches    = glob.glob(os.path.join(script_dir, '**', '*.npy'), recursive=True)

    if not matches:
        print("No .npy files found. Pass the path as an argument:")
        print("  python view_epochs.py path/to/epochs.npy")
        exit()

    if len(matches) == 1:
        print(f"Found: {matches[0]}")
        return matches[0]

    # multiple files — let user pick
    print("Multiple .npy files found — pick one:\n")
    for i, m in enumerate(matches):
        print(f"  [{i+1}] {m}")
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
npy_path  = find_npy_file()
json_path = npy_path.replace('.npy', '_meta.json')

data = np.load(npy_path)  # shape: (n_epochs, n_channels, n_samples)
print(f"\nLoaded: {npy_path}")
print(f"Shape:  {data.shape}  (epochs × channels × samples)")

# load metadata if available
if os.path.exists(json_path):
    with open(json_path) as f:
        meta = json.load(f)
    srate         = meta['srate']
    channel_names = meta['channel_names']
    pre_ms        = meta['pre_ms']
    post_ms       = meta['post_ms']
    n_epochs      = meta['n_epochs']
    print(f"Metadata loaded — {n_epochs} epochs @ {srate}Hz")
else:
    print("No metadata file found — using defaults")
    srate         = 250.0
    pre_ms        = 200
    post_ms       = 1000
    channel_names = [f'Ch{i}' for i in range(data.shape[1])]

n_epochs, n_ch, n_samples = data.shape
times = np.linspace(-pre_ms, post_ms, n_samples)  # time axis in ms

# ── Plot 1: ERP — all epochs + average per channel ──────────
def plot_erp():
    fig, axes = plt.subplots(n_ch, 1, figsize=(12, 2.5 * n_ch), sharex=True)
    if n_ch == 1:
        axes = [axes]

    fig.suptitle('ERP — Individual Epochs + Average', fontsize=14)

    for ch in range(n_ch):
        ax = axes[ch]

        # plot each individual epoch in light grey
        for ep in range(n_epochs):
            ax.plot(times, data[ep, ch, :], color='lightgrey', linewidth=0.8, alpha=0.7)

        # plot the average in bold
        avg = data[:, ch, :].mean(axis=0)
        ax.plot(times, avg, color='steelblue', linewidth=2, label='Average')

        # mark the stimulus onset
        ax.axvline(x=0, color='red', linestyle='--', linewidth=1, label='Stimulus')

        # shade the baseline window
        ax.axvspan(-pre_ms, 0, alpha=0.05, color='green', label='Baseline')

        ax.set_ylabel(f'{channel_names[ch]}\n(µV)', fontsize=9)
        ax.set_xlim(-pre_ms, post_ms)
        ax.grid(True, alpha=0.3)

        if ch == 0:
            ax.legend(loc='upper right', fontsize=8)

    axes[-1].set_xlabel('Time (ms)', fontsize=11)
    plt.tight_layout()
    plt.savefig(npy_path.replace('.npy', '_erp.png'), dpi=150)
    print("Saved ERP plot")
    plt.show()

# ── Plot 2: FFT / PSD per channel ───────────────────────────
def plot_fft():
    fig, axes = plt.subplots(n_ch, 1, figsize=(12, 2.5 * n_ch), sharex=True)
    if n_ch == 1:
        axes = [axes]

    fig.suptitle('Power Spectral Density (averaged across epochs)', fontsize=14)

    band_colours = {
        'Delta (0.5–4Hz)':  (0.5, 4,  'blue'),
        'Theta (4–8Hz)':    (4,   8,  'green'),
        'Alpha (8–13Hz)':   (8,   13, 'yellow'),
        'Beta (13–30Hz)':   (13,  30, 'orange'),
        'Gamma (30–50Hz)':  (30,  50, 'red'),
    }

    for ch in range(n_ch):
        ax = axes[ch]
        psds = []

        for ep in range(n_epochs):
            freqs, psd = welch(
                data[ep, ch, :],
                fs=srate,
                nperseg=min(int(srate * 2), n_samples)
            )
            psds.append(psd)

        avg_psd = np.mean(psds, axis=0)
        mask    = freqs <= 50

        ax.semilogy(freqs[mask], avg_psd[mask], color='steelblue', linewidth=1.5)

        # shade EEG bands
        for label, (flo, fhi, colour) in band_colours.items():
            ax.axvspan(flo, fhi, alpha=0.1, color=colour,
                       label=label if ch == 0 else '')

        ax.set_ylabel(channel_names[ch], fontsize=9)
        ax.grid(True, alpha=0.3)

        if ch == 0:
            ax.legend(loc='upper right', fontsize=7, ncol=2)

    axes[-1].set_xlabel('Frequency (Hz)', fontsize=11)
    plt.tight_layout()
    plt.savefig(npy_path.replace('.npy', '_fft.png'), dpi=150)
    print("Saved FFT plot")
    plt.show()

# ── Plot 3: Heatmap — all epochs side by side ───────────────
def plot_heatmap():
    fig, axes = plt.subplots(1, n_ch, figsize=(3 * n_ch, 6), sharey=True)
    if n_ch == 1:
        axes = [axes]

    fig.suptitle('Epoch Heatmap (time × epoch per channel)', fontsize=14)

    for ch in range(n_ch):
        ax    = axes[ch]
        img   = data[:, ch, :].T   # (n_samples, n_epochs)
        vmax  = np.percentile(np.abs(img), 95)

        ax.imshow(
            img,
            aspect='auto',
            origin='lower',
            cmap='RdBu_r',
            vmin=-vmax,
            vmax=vmax,
            extent=[0, n_epochs, -pre_ms, post_ms]
        )
        ax.axhline(y=0, color='black', linestyle='--', linewidth=1)
        ax.set_title(channel_names[ch], fontsize=9)
        ax.set_xlabel('Epoch #', fontsize=8)

    axes[0].set_ylabel('Time (ms)', fontsize=10)
    plt.tight_layout()
    plt.savefig(npy_path.replace('.npy', '_heatmap.png'), dpi=150)
    print("Saved heatmap plot")
    plt.show()

# ── Summary stats ────────────────────────────────────────────
def print_summary():
    print(f"\n{'─'*50}")
    print(f"  File:      {os.path.basename(npy_path)}")
    print(f"  Epochs:    {n_epochs}")
    print(f"  Channels:  {n_ch} {channel_names}")
    print(f"  Samples:   {n_samples} per epoch")
    print(f"  Duration:  -{pre_ms}ms to +{post_ms}ms")
    print(f"  Srate:     {srate}Hz")
    print(f"  Data range: {data.min():.1f} to {data.max():.1f} µV")
    print(f"{'─'*50}\n")

# ── Run everything ───────────────────────────────────────────
print_summary()
plot_erp()
plot_fft()
plot_heatmap()