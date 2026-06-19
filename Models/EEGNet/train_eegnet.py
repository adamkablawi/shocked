"""
train_eegnet.py
===============
Unified EEGNet trainer for the EMS "Shocked" project. One script for BOTH the
3-class and 4-class datasets, with all tunable hyperparameters in one place so
the two class counts can finally be compared under identical settings.

Key changes vs the original train_eegnet_3class.py / _4class.py:
  * N_CLASSES and class names are read from the .npz (class_names), not hardcoded.
  * EEGNet is defined inline (clean reimplementation of Lawhern et al. 2018),
    so there is no dependency on the arl-eegmodels repo. Nothing to clone on Kaggle.
  * kernLength is an explicit hyperparameter (was hardcoded to sfreq*0.5 = 125).
  * Named CONFIGS let you launch a sweep one config per Kaggle run.
  * LOSO summary reports overall AND balanced accuracy plus the aggregated
    confusion matrix and per-class recall, for both class counts consistently.

Run on Kaggle (GPU on):
    python train_eegnet.py --data_glob '/kaggle/input/ems-4c/*.npz' \
                           --output_dir /kaggle/working/out_4c --config baseline

    python train_eegnet.py --data_glob '/kaggle/input/ems-3c/*.npz' \
                           --output_dir /kaggle/working/out_3c --config short_kernel

Within-subject instead of LOSO:
    python train_eegnet.py --data_glob '...' --output_dir ... --mode within --config baseline
"""

import os
import json
import glob
import argparse
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import (
    Input, Conv2D, BatchNormalization, Activation, DepthwiseConv2D,
    SeparableConv2D, AveragePooling2D, Dropout, Flatten, Dense,
)
from tensorflow.keras.constraints import max_norm
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split, LeaveOneGroupOut
from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import classification_report, confusion_matrix, balanced_accuracy_score

SEED = 42
np.random.seed(SEED)
tf.random.set_seed(SEED)

# ----------------------------------------------------------------------------
# Hyperparameter configs. Each Kaggle run uses one config (--config NAME).
# To sweep, launch the same script several times with different --config.
# kernel_ms is the temporal kernel in MILLISECONDS; it is converted to samples
# using the data's own sfreq, so it is sampling-rate safe.
# ----------------------------------------------------------------------------
CONFIGS = {
    # Reproduces the prior 4-class architecture (kernLength 125 = 500 ms @ 250 Hz)
    "baseline": dict(
        F1=8, D=2, F2=16, kernel_ms=500, dropout_cross=0.25, dropout_within=0.5,
        epochs=500, batch_size=32, patience_stop=50, patience_lr=20,
        lr=1e-3, class_weight="balanced",
    ),
    # Shorter kernel: 256 ms. Band-power analysis put the signal in faster
    # gamma/SEP components, which a 500 ms kernel smears over.
    "short_kernel": dict(
        F1=8, D=2, F2=16, kernel_ms=256, dropout_cross=0.25, dropout_within=0.5,
        epochs=500, batch_size=32, patience_stop=50, patience_lr=20,
        lr=1e-3, class_weight="balanced",
    ),
    # Even shorter kernel + higher dropout to fight LOSO overfit on small data.
    "short_kernel_hi_drop": dict(
        F1=8, D=2, F2=16, kernel_ms=128, dropout_cross=0.5, dropout_within=0.5,
        epochs=500, batch_size=32, patience_stop=50, patience_lr=20,
        lr=1e-3, class_weight="balanced",
    ),
    # Bigger capacity, short kernel.
    "wide_short": dict(
        F1=16, D=2, F2=32, kernel_ms=256, dropout_cross=0.5, dropout_within=0.5,
        epochs=500, batch_size=32, patience_stop=50, patience_lr=20,
        lr=1e-3, class_weight="balanced",
    ),
    # No class weighting (lets the merged/adjacent classes compete on their own).
    "short_kernel_noweight": dict(
        F1=8, D=2, F2=16, kernel_ms=256, dropout_cross=0.25, dropout_within=0.5,
        epochs=500, batch_size=32, patience_stop=50, patience_lr=20,
        lr=1e-3, class_weight="none",
    ),
}


# ----------------------------------------------------------------------------
# EEGNet (clean reimplementation of the EEGNet-8,2 architecture,
# Lawhern et al. 2018, J. Neural Eng.). Architecture only; original code not used.
# ----------------------------------------------------------------------------
def build_eegnet(nb_classes, chans, samples, dropout_rate, kern_length, F1, D, F2):
    inp = Input(shape=(chans, samples, 1))

    # Block 1: temporal conv -> depthwise spatial conv (per-channel filters)
    x = Conv2D(F1, (1, kern_length), padding='same', use_bias=False)(inp)
    x = BatchNormalization()(x)
    x = DepthwiseConv2D((chans, 1), use_bias=False, depth_multiplier=D,
                        depthwise_constraint=max_norm(1.))(x)
    x = BatchNormalization()(x)
    x = Activation('elu')(x)
    x = AveragePooling2D((1, 4))(x)
    x = Dropout(dropout_rate)(x)

    # Block 2: separable conv (temporal mixing) -> pool
    x = SeparableConv2D(F2, (1, 16), use_bias=False, padding='same')(x)
    x = BatchNormalization()(x)
    x = Activation('elu')(x)
    x = AveragePooling2D((1, 8))(x)
    x = Dropout(dropout_rate)(x)

    x = Flatten()(x)
    x = Dense(nb_classes, kernel_constraint=max_norm(0.25))(x)
    out = Activation('softmax')(x)
    return Model(inputs=inp, outputs=out)


# ----------------------------------------------------------------------------
# Data loading
# ----------------------------------------------------------------------------
def load_data(npz_path):
    if not os.path.exists(npz_path):
        raise FileNotFoundError(f"Dataset not found: {npz_path}")
    data = np.load(npz_path, allow_pickle=True)
    required = {'X', 'y', 'sfreq', 'channel_names', 'subject_id'}
    missing = required - set(data.files)
    if missing:
        raise KeyError(f"{npz_path} missing arrays: {sorted(missing)}")
    X = np.asarray(data['X'], dtype=np.float32)
    y = np.asarray(data['y'], dtype=np.int64)
    sfreq = float(data['sfreq'])
    channel_names = [str(c) for c in data['channel_names']]
    subject_id = str(data['subject_id'])
    class_names = [str(c) for c in data['class_names']] if 'class_names' in data.files else None
    if X.ndim != 3 or y.ndim != 1 or X.shape[0] != y.shape[0]:
        raise ValueError(f"Bad shapes in {npz_path}: X={X.shape}, y={y.shape}")
    if not np.isfinite(X).all():
        raise ValueError(f"{npz_path} contains NaN/Inf in X")
    return X, y, sfreq, channel_names, subject_id, class_names


def load_all_subjects(npz_glob):
    paths = sorted(glob.glob(npz_glob))
    if not paths:
        raise FileNotFoundError(f"No files matched glob: {npz_glob}")
    Xs, ys, sids = [], [], []
    ref_sfreq = ref_chans = ref_classes = None
    for path in paths:
        X, y, sfreq, chans, sid, class_names = load_data(path)
        if ref_sfreq is None:
            ref_sfreq, ref_chans, ref_classes = sfreq, chans, class_names
        else:
            if sfreq != ref_sfreq:
                raise ValueError(f"{path} sfreq={sfreq} != {ref_sfreq}")
            if chans != ref_chans:
                raise ValueError(f"{path} channel set differs from first file")
        Xs.append(X); ys.append(y); sids.append(np.array([sid] * len(y)))
    X = np.concatenate(Xs, axis=0)
    y = np.concatenate(ys, axis=0)
    subject_ids = np.concatenate(sids, axis=0)
    print(f"Loaded {len(paths)} subjects, {len(X)} epochs. "
          f"Classes {ref_classes}, dist {dict(zip(*np.unique(y, return_counts=True)))}")
    return X, y, subject_ids, ref_sfreq, ref_chans, ref_classes


# ----------------------------------------------------------------------------
# Scaler (per-channel z-score, fit on train only)
# ----------------------------------------------------------------------------
def fit_apply_scaler(X_train, *others):
    n_ch = X_train.shape[1]
    flat = X_train.transpose(0, 2, 1).reshape(-1, n_ch)
    mean = flat.mean(axis=0)
    std = flat.std(axis=0)
    std[std == 0] = 1.0

    def apply(X):
        n, c, t = X.shape
        f = X.transpose(0, 2, 1).reshape(-1, c)
        f = (f - mean) / std
        return f.reshape(n, t, c).transpose(0, 2, 1).astype(np.float32)

    return (apply(X_train),) + tuple(apply(o) for o in others) + (mean, std)


# ----------------------------------------------------------------------------
# Train / evaluate
# ----------------------------------------------------------------------------
def train_fold(X_train, y_train, X_val, y_val, sfreq, n_classes, cfg,
               dropout_rate, checkpoint_path):
    X_train_4d = X_train[..., np.newaxis]
    X_val_4d = X_val[..., np.newaxis]
    y_train_oh = to_categorical(y_train, num_classes=n_classes)
    y_val_oh = to_categorical(y_val, num_classes=n_classes)

    if cfg['class_weight'] == 'balanced':
        present = np.unique(y_train)
        cw = compute_class_weight('balanced', classes=present, y=y_train)
        class_weights = {int(c): float(w) for c, w in zip(present, cw)}
    else:
        class_weights = None

    kern = max(1, int(round(cfg['kernel_ms'] / 1000.0 * sfreq)))
    print(f"  Building EEGNet: C={X_train.shape[1]}, T={X_train.shape[2]}, "
          f"kernLength={kern} ({cfg['kernel_ms']} ms @ {sfreq:.0f} Hz), "
          f"F1/D/F2={cfg['F1']}/{cfg['D']}/{cfg['F2']}")
    model = build_eegnet(n_classes, X_train.shape[1], X_train.shape[2],
                         dropout_rate, kern, cfg['F1'], cfg['D'], cfg['F2'])
    model.compile(loss='categorical_crossentropy',
                  optimizer=tf.keras.optimizers.Adam(learning_rate=cfg['lr']),
                  metrics=['accuracy'])

    callbacks = [
        EarlyStopping(monitor='val_loss', patience=cfg['patience_stop'],
                      restore_best_weights=True, verbose=1),
        ReduceLROnPlateau(monitor='val_loss', factor=0.5,
                          patience=cfg['patience_lr'], min_lr=1e-6, verbose=1),
        ModelCheckpoint(checkpoint_path, monitor='val_loss',
                        save_best_only=True, verbose=0),
    ]
    history = model.fit(
        X_train_4d, y_train_oh, validation_data=(X_val_4d, y_val_oh),
        epochs=cfg['epochs'], batch_size=cfg['batch_size'],
        class_weight=class_weights, callbacks=callbacks, verbose=2,
    )
    return model, history


def evaluate(model, X_test, y_test, class_names, n_classes, label=""):
    y_pred = np.argmax(model.predict(X_test[..., np.newaxis], verbose=0), axis=1)
    cm = confusion_matrix(y_test, y_pred, labels=range(n_classes))
    acc = float((y_pred == y_test).mean())
    bal = float(balanced_accuracy_score(y_test, y_pred))

    print(f"\n========== Evaluation: {label} ==========")
    print("Confusion matrix (rows=true, cols=pred):")
    print("             " + "  ".join(f"{c[:8]:>8}" for c in class_names))
    for i, row in enumerate(cm):
        print(f"  {class_names[i][:10]:>10}  " + "  ".join(f"{v:>8d}" for v in row))
    print("\n" + classification_report(y_test, y_pred, labels=range(n_classes),
                                        target_names=class_names, digits=3,
                                        zero_division=0))
    print(f"Overall accuracy: {acc:.4f}   Balanced accuracy: {bal:.4f}")
    return {'label': label, 'accuracy': acc, 'balanced_accuracy': bal,
            'confusion_matrix': cm.tolist()}


# ----------------------------------------------------------------------------
# LOSO
# ----------------------------------------------------------------------------
def run_loso(npz_glob, output_dir, cfg):
    os.makedirs(output_dir, exist_ok=True)
    X, y, subject_ids, sfreq, channel_names, class_names = load_all_subjects(npz_glob)
    n_classes = len(class_names) if class_names else int(y.max() + 1)
    if class_names is None:
        class_names = [f"class_{i}" for i in range(n_classes)]
    print(f"Inferred n_classes={n_classes} from data.\n")

    logo = LeaveOneGroupOut()
    n_subj = len(np.unique(subject_ids))
    fold_results, agg_cm = [], np.zeros((n_classes, n_classes), dtype=int)

    for fold_idx, (trainval_idx, test_idx) in enumerate(
            logo.split(X, y, groups=subject_ids)):
        held_out = str(np.unique(subject_ids[test_idx])[0])
        print(f"\n{'='*60}\nFold {fold_idx+1} of {n_subj}: holding out {held_out}\n{'='*60}")

        X_tv, y_tv = X[trainval_idx], y[trainval_idx]
        X_te, y_te = X[test_idx], y[test_idx]
        X_tr, X_va, y_tr, y_va = train_test_split(
            X_tv, y_tv, test_size=0.15, stratify=y_tv, random_state=SEED)

        X_tr, X_va, X_te, _, _ = fit_apply_scaler(X_tr, X_va, X_te)

        ckpt = os.path.join(output_dir, f"loso_fold{fold_idx:02d}_{held_out}.keras")
        model, _ = train_fold(X_tr, y_tr, X_va, y_va, sfreq, n_classes, cfg,
                              cfg['dropout_cross'], ckpt)
        res = evaluate(model, X_te, y_te, class_names, n_classes,
                       label=f"LOSO fold {fold_idx+1} / held-out {held_out}")
        res.update({'fold_idx': fold_idx, 'held_out_subject': held_out})
        fold_results.append(res)
        agg_cm += np.array(res['confusion_matrix'])
        tf.keras.backend.clear_session()

    accs = np.array([r['accuracy'] for r in fold_results])
    bals = np.array([r['balanced_accuracy'] for r in fold_results])
    recall = (agg_cm.diagonal() / agg_cm.sum(axis=1)).tolist()
    summary = {
        'mode': 'loso', 'n_folds': len(fold_results), 'n_classes': n_classes,
        'class_names': class_names, 'config': cfg,
        'mean_accuracy': float(accs.mean()), 'std_accuracy': float(accs.std()),
        'mean_balanced_accuracy': float(bals.mean()), 'std_balanced_accuracy': float(bals.std()),
        'min_accuracy': float(accs.min()), 'max_accuracy': float(accs.max()),
        'aggregate_confusion': agg_cm.tolist(),
        'per_class_recall': recall,
        'per_fold': fold_results,
    }
    print(f"\n{'='*60}\nLOSO Summary ({n_classes}-class)\n{'='*60}")
    print(f"Mean accuracy:          {accs.mean():.4f} ± {accs.std():.4f}")
    print(f"Mean balanced accuracy: {bals.mean():.4f} ± {bals.std():.4f}")
    print(f"Range: [{accs.min():.4f}, {accs.max():.4f}]")
    print(f"Per-class recall: {dict(zip(class_names, np.round(recall, 3)))}")
    print(f"Aggregate confusion:\n{agg_cm}")
    with open(os.path.join(output_dir, 'loso_summary.json'), 'w') as f:
        json.dump(summary, f, indent=2)
    return summary


def run_within(npz_glob, output_dir, cfg):
    os.makedirs(output_dir, exist_ok=True)
    paths = sorted(glob.glob(npz_glob))
    results = []
    for path in paths:
        X, y, sfreq, channel_names, sid, class_names = load_data(path)
        n_classes = len(class_names) if class_names else int(y.max() + 1)
        if class_names is None:
            class_names = [f"class_{i}" for i in range(n_classes)]
        print(f"\n{'='*60}\nWithin-subject: {sid}\n{'='*60}")
        X_tr, X_tmp, y_tr, y_tmp = train_test_split(
            X, y, test_size=0.30, stratify=y, random_state=SEED)
        X_va, X_te, y_va, y_te = train_test_split(
            X_tmp, y_tmp, test_size=0.50, stratify=y_tmp, random_state=SEED)
        X_tr, X_va, X_te, _, _ = fit_apply_scaler(X_tr, X_va, X_te)
        ckpt = os.path.join(output_dir, f"{sid}_within.keras")
        model, _ = train_fold(X_tr, y_tr, X_va, y_va, sfreq, n_classes, cfg,
                              cfg['dropout_within'], ckpt)
        res = evaluate(model, X_te, y_te, class_names, n_classes,
                       label=f"within-subject / {sid}")
        res['subject_id'] = sid
        results.append(res)
        tf.keras.backend.clear_session()
    accs = np.array([r['accuracy'] for r in results])
    print(f"\nWithin-subject mean accuracy: {accs.mean():.4f} ± {accs.std():.4f}")
    with open(os.path.join(output_dir, 'within_summary.json'), 'w') as f:
        json.dump({'mode': 'within', 'mean_accuracy': float(accs.mean()),
                   'per_subject': results, 'config': cfg}, f, indent=2)
    return results


def main():
    p = argparse.ArgumentParser(description="Unified EEGNet trainer (3- and 4-class).")
    p.add_argument('--data_glob', required=True, help="Glob for subject .npz files.")
    p.add_argument('--output_dir', required=True)
    p.add_argument('--mode', choices=['loso', 'within'], default='loso')
    p.add_argument('--config', choices=list(CONFIGS.keys()), default='baseline')
    args = p.parse_args()

    cfg = CONFIGS[args.config]
    gpus = tf.config.list_physical_devices('GPU')
    print(f"=== train_eegnet | mode={args.mode} | config={args.config} | "
          f"GPUs={len(gpus)} ===")
    print(f"Config: {cfg}\n")

    if args.mode == 'loso':
        run_loso(args.data_glob, args.output_dir, cfg)
    else:
        run_within(args.data_glob, args.output_dir, cfg)


if __name__ == '__main__':
    main()
