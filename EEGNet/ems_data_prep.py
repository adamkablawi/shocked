"""
Convert one (X.npy, y.npy, metadata.json) trio into a single .npz file
ready for the EEGNet training pipeline.

Steps:
    1. Load X, y, and metadata from a single subject's directory.
    2. Downsample EEG from 1000 Hz to 250 Hz (anti-aliased decimation by 4).
    3. Merge labels: min_intensity (1) and medium_intensity (2) -> intermediate (1).
       Final label scheme: 0 = no_stim, 1 = intermediate, 2 = max_intensity.
    4. Save to .npz with X, y, sfreq, channel_names, subject_id.

Usage:
    python convert_to_npz.py --input_dir path/to/subject_folder --output_file subj01.npz
"""

import argparse
import json
import os
import numpy as np
from scipy.signal import decimate

# --- Configuration ---
DOWNSAMPLE_FACTOR = 4                    # 1000 Hz -> 250 Hz
TARGET_SFREQ = 250.0

# Label remapping after merging min + medium intensities.
# Original: 0 = no_stim, 1 = min, 2 = medium, 3 = max
# New:      0 = no_stim, 1 = intermediate (min OR medium), 2 = max_intensity
LABEL_REMAP = {
    0: 0,    # no_stim          -> no_stim
    1: 1,    # min_intensity    -> intermediate
    2: 1,    # medium_intensity -> intermediate
    3: 2,    # max_intensity    -> max_intensity
}

NEW_CLASS_NAMES = ['no_stimulation', 'intermediate_intensity', 'max_intensity']


def load_subject(input_dir):
    """Load X.npy, y.npy, and metadata.json from a single subject directory."""
    X_path = os.path.join(input_dir, 'X.npy')
    y_path = os.path.join(input_dir, 'y.npy')
    meta_path = os.path.join(input_dir, 'metadata.json')

    for p in (X_path, y_path, meta_path):
        if not os.path.exists(p):
            raise FileNotFoundError(f"Missing file: {p}")

    X = np.load(X_path)
    y = np.load(y_path)
    with open(meta_path) as f:
        meta = json.load(f)

    print(f"Loaded {meta['subject_id']}: X={X.shape}, y={y.shape}, sfreq={meta['sfreq']} Hz")
    return X, y, meta


def downsample(X, factor):
    """Anti-aliased decimation along the time axis."""
    # scipy.signal.decimate applies a lowpass FIR filter before subsampling,
    # which avoids aliasing. For raw slicing (no anti-alias) use: X[:, :, ::factor]
    X_ds = decimate(X, q=factor, axis=2, ftype='fir', zero_phase=True)
    print(f"Downsampled: {X.shape} -> {X_ds.shape}")
    return X_ds


def remap_labels(y, mapping):
    """Apply label remap dict to a 1D label array."""
    y_new = np.array([mapping[int(v)] for v in y], dtype=np.int64)
    unique, counts = np.unique(y_new, return_counts=True)
    print(f"Label remap done. New distribution: "
          f"{dict(zip(unique.tolist(), counts.tolist()))}")
    return y_new


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', required=True,
                        help='Directory containing X.npy, y.npy, metadata.json')
    parser.add_argument('--output_file', required=True,
                        help='Output .npz path (e.g., EMS0001.npz)')
    args = parser.parse_args()

    # 1. Load
    X, y, meta = load_subject(args.input_dir)

    # 2. Sanity checks
    assert meta['sfreq'] == 1000.0, f"Expected 1000 Hz source, got {meta['sfreq']}"
    assert X.shape[0] == y.shape[0], "X and y are misaligned"

    # 3. Downsample (1000 Hz -> 250 Hz)
    X = downsample(X, DOWNSAMPLE_FACTOR)

    # 4. Merge labels
    y = remap_labels(y, LABEL_REMAP)

    # 5. Cast to training-friendly dtypes
    X = X.astype(np.float32)

    # 6. Save
    np.savez(
        args.output_file,
        X=X,
        y=y,
        sfreq=TARGET_SFREQ,
        channel_names=np.array(meta['channel_names']),
        subject_id=meta['subject_id'],
        class_names=np.array(NEW_CLASS_NAMES),
    )
    print(f"Saved -> {args.output_file}")
    print(f"  X shape: {X.shape}, dtype: {X.dtype}")
    print(f"  y shape: {y.shape}, classes: {NEW_CLASS_NAMES}")


if __name__ == '__main__':
    main()