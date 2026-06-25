"""
Convert one (X.npy, y.npy, metadata.json) trio into a single .npz file
ready for the training pipeline (balanced 3-class variant).

Differences from dataprep.py:
    - DROPS the lowest class, 'no_stimulation' (original label 0), entirely.
    - Remaps the remaining three stimulation classes to a contiguous 0..2,
      yielding a balanced 40/40/40 split (min / medium / max intensity).
    - Same downsample (1000 -> 250 Hz) and crop ([-0.2, 1.5] s) as dataprep.py.
Usage:
    python dataprep_3class_balanced.py --input_dir path/to/subject_folder \
                                       --output_file subj01.npz
"""

import argparse
import json
import os
import numpy as np
from scipy.signal import decimate


# --- Configuration ---
DOWNSAMPLE_FACTOR = 4
TARGET_SFREQ = 250.0

# Crop window in seconds, relative to stimulus onset (t=0).
CROP_TMIN = -0.2
CROP_TMAX = 1.5

# Original labels to discard before remapping (no_stimulation).
DROP_LABELS = {0}

# Remap of the SURVIVING original labels -> contiguous 0..2.
# Original: 0 no_stim (dropped), 1 min, 2 medium, 3 max.
LABEL_REMAP = {
    1: 0,
    2: 1,
    3: 2,
}

NEW_CLASS_NAMES = [
    'min_intensity',
    'medium_intensity',
    'max_intensity',
]


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

    print(f"Loaded {meta['subject_id']}: X={X.shape}, y={y.shape}, "
          f"sfreq={meta['sfreq']} Hz, tmin={meta['epoch_tmin']}, "
          f"tmax={meta['epoch_tmax']}")
    return X, y, meta


def drop_classes(X, y, drop_labels):
    """Remove all epochs whose label is in drop_labels (operates on original labels)."""
    keep = ~np.isin(y, list(drop_labels))
    X_kept, y_kept = X[keep], y[keep]
    print(f"Dropped classes {sorted(drop_labels)}: "
          f"{X.shape[0]} -> {X_kept.shape[0]} epochs")
    return X_kept, y_kept


def downsample(X, factor):
    """Anti-aliased decimation along the time axis."""
    # scipy.signal.decimate applies a lowpass FIR filter before subsampling,
    # which avoids aliasing. For raw slicing (no anti-alias) use: X[:, :, ::factor]
    X_ds = decimate(X, q=factor, axis=2, ftype='fir', zero_phase=True)
    print(f"Downsampled: {X.shape} -> {X_ds.shape}")
    return X_ds


def crop_epoch_window(X, orig_tmin, sfreq, crop_tmin, crop_tmax):
    """
    Crop the time axis from [orig_tmin, ...] down to [crop_tmin, crop_tmax].

    Parameters
    ----------
    X : np.ndarray, shape (n_epochs, n_channels, n_samples)
        Downsampled EEG epochs.
    orig_tmin : float
        Start time (s) of the existing epoch window, from metadata.
    sfreq : float
        Sample rate of X (post-downsampling).
    crop_tmin, crop_tmax : float
        Desired start and end times (s) relative to stimulus onset.

    Returns
    -------
    X_cropped : np.ndarray
        Same shape on the first two axes, cropped on the third.
    """
    # Convert times to sample indices into the existing array.
    start_idx = int(round((crop_tmin - orig_tmin) * sfreq))
    end_idx   = int(round((crop_tmax - orig_tmin) * sfreq))

    if start_idx < 0 or end_idx > X.shape[2]:
        raise ValueError(
            f"Crop window [{crop_tmin}, {crop_tmax}] s requires samples "
            f"[{start_idx}, {end_idx}] but X only has {X.shape[2]} samples "
            f"(orig_tmin={orig_tmin}, sfreq={sfreq})."
        )

    X_cropped = X[:, :, start_idx:end_idx]
    print(f"Cropped to [{crop_tmin}, {crop_tmax}] s "
          f"(samples [{start_idx}, {end_idx}]): {X.shape} -> {X_cropped.shape}")
    return X_cropped


def remap_labels(y, mapping):
    """Apply label remap dict to a 1D label array."""
    y_new = np.array([mapping[int(v)] for v in y], dtype=np.int64)
    unique, counts = np.unique(y_new, return_counts=True)
    print(f"Label distribution: "
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

    # 3. Drop the no_stimulation class (operates on the ORIGINAL labels).
    X, y = drop_classes(X, y, DROP_LABELS)

    # 4. Downsample (1000 Hz -> 250 Hz)
    X = downsample(X, DOWNSAMPLE_FACTOR)

    # 5. Crop time window. Uses the post-downsample sfreq, since X is now at 250 Hz.
    X = crop_epoch_window(
        X,
        orig_tmin=float(meta['epoch_tmin']),
        sfreq=TARGET_SFREQ,
        crop_tmin=CROP_TMIN,
        crop_tmax=CROP_TMAX,
    )

    # 6. Remap the surviving labels to a contiguous 0..2.
    y = remap_labels(y, LABEL_REMAP)

    # 7. Cast to training-friendly dtype
    X = X.astype(np.float32)

    # 8. Save
    np.savez(
        args.output_file,
        X=X,
        y=y,
        sfreq=TARGET_SFREQ,
        channel_names=np.array(meta['channel_names']),
        subject_id=meta['subject_id'],
        class_names=np.array(NEW_CLASS_NAMES),
        epoch_tmin=CROP_TMIN,
        epoch_tmax=CROP_TMAX,
    )
    print(f"Saved -> {args.output_file}")
    print(f"  X shape: {X.shape}, dtype: {X.dtype}")
    print(f"  y shape: {y.shape}, classes: {NEW_CLASS_NAMES}")


if __name__ == '__main__':
    main()
