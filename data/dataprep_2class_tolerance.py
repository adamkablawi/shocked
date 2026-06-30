"""
Convert one (X.npy, y.npy, metadata.json) trio into a single .npz file
ready for the training pipeline (2-class TOLERANCE variant).

Purpose:
    Isolate the features most indicative of HIGH-intensity (intolerable) EMS
    stimulation. The lowest three intensities (no_stim, min, medium) are merged
    into one large "tolerable" class; the single highest intensity becomes
    "intolerable". This deliberately UNBALANCED 120 / 40 split frames the
    question as "tolerable vs intolerable".

Differences from dataprep.py:
    - Merge original classes 0,1,2 -> 0 (tolerable); class 3 -> 1 (intolerable).
    - Result is a 2-class, 120 / 40 per-subject split.
    - Same downsample (1000 -> 250 Hz) and crop ([-0.2, 1.5] s) as every other set.
Usage:
    python dataprep_2class_tolerance.py --input_dir path/to/subject_folder \
                                        --output_file EMS0001.npz
"""

import argparse
import json
import os
import numpy as np
from scipy.signal import decimate


# --- Configuration ---
DOWNSAMPLE_FACTOR = 4
TARGET_SFREQ = 250.0

# Crop window in seconds, relative to stimulus onset (t=0). Same as all sets.
CROP_TMIN = -0.2
CROP_TMAX = 1.5

# Merge the bottom three intensities into "tolerable"; the top one is "intolerable".
# Original: 0 no_stim, 1 min, 2 medium, 3 max.
LABEL_REMAP = {
    0: 0,   # no_stimulation  -> tolerable
    1: 0,   # min_intensity   -> tolerable
    2: 0,   # medium_intensity-> tolerable
    3: 1,   # max_intensity   -> intolerable
}

NEW_CLASS_NAMES = [
    'tolerable',
    'intolerable',
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


def downsample(X, factor):
    """Anti-aliased decimation along the time axis."""
    X_ds = decimate(X, q=factor, axis=2, ftype='fir', zero_phase=True)
    print(f"Downsampled: {X.shape} -> {X_ds.shape}")
    return X_ds


def crop_epoch_window(X, orig_tmin, sfreq, crop_tmin, crop_tmax):
    """Crop the time axis from [orig_tmin, ...] down to [crop_tmin, crop_tmax]."""
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
    """Apply label remap dict to a 1D label array (merges the bottom three classes)."""
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

    X, y, meta = load_subject(args.input_dir)

    assert meta['sfreq'] == 1000.0, f"Expected 1000 Hz source, got {meta['sfreq']}"
    assert X.shape[0] == y.shape[0], "X and y are misaligned"

    X = downsample(X, DOWNSAMPLE_FACTOR)
    X = crop_epoch_window(
        X, orig_tmin=float(meta['epoch_tmin']), sfreq=TARGET_SFREQ,
        crop_tmin=CROP_TMIN, crop_tmax=CROP_TMAX,
    )
    y = remap_labels(y, LABEL_REMAP)
    X = X.astype(np.float32)

    np.savez(
        args.output_file,
        X=X, y=y, sfreq=TARGET_SFREQ,
        channel_names=np.array(meta['channel_names']),
        subject_id=meta['subject_id'],
        class_names=np.array(NEW_CLASS_NAMES),
        epoch_tmin=CROP_TMIN, epoch_tmax=CROP_TMAX,
    )
    print(f"Saved -> {args.output_file}")
    print(f"  X shape: {X.shape}, dtype: {X.dtype}")
    print(f"  y shape: {y.shape}, classes: {NEW_CLASS_NAMES}")


if __name__ == '__main__':
    main()
