import os
import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split, LeaveOneGroupOut
from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

# This is the EEGNet we use, from github repo: 
# https://github.com/vlawhern/arl-eegmodels

from EEGModels import EEGNet

CLASSES = ['no_stimulation', 'min_intensity', 'medium_intensity', 'max_intensity']
N_CLASSES = 4

# EEGNet hyperparams (Lawhern et al. 2016, EEGNet-8,2 variant)

F1, D, F2 = 8, 2, 16
DROPOUT_WITHIN = 0.5
DROPOUT_CROSS  = 0.25

# Training hyperparams (Lawhern et al. 2016, EEGNet-8,2 variant)

EPOCHS = 500
BATCH_SIZE = 32
PATIENCE_EARLY_STOP = 50
PATIENCE_LR_REDUCE  = 20

# Random seed for reproducibility

SEED = 42

np.random.seed(SEED)
tf.random.set_seed(SEED)

def load_data(npz_path):
    """
    Load a preprocessed EEG dataset from a single .npz file.

    The .npz is expected to contain the arrays produced by ems_data_prep.py:
        X              : float32, shape (n_epochs, n_channels, n_samples)
        y              : int64,   shape (n_epochs,)         labels in {0, 1, 2}
        sfreq          : float scalar                       sample rate in Hz
        channel_names  : array of str,  length n_channels   electrode labels
        subject_id     : str scalar                         subject identifier
        class_names    : array of str,  length N_CLASSES    human-readable labels

    Parameters
    ----------
    npz_path : str
        Path to the .npz file to load.

    Returns
    -------
    X : np.ndarray, float32, shape (n_epochs, n_channels, n_samples)
        EEG epochs.
    y : np.ndarray, int64, shape (n_epochs,)
        Integer class labels.
    sfreq : float
        Sample rate in Hz.
    channel_names : list[str]
        Electrode labels in channel order.
    subject_id : str
        Subject identifier from the source metadata.

    Raises
    ------
    FileNotFoundError
        If npz_path does not exist.
    KeyError
        If a required array is missing from the .npz.
    ValueError
        If shapes are inconsistent, labels fall outside the expected range,
        or the dataset contains NaN/Inf values.
    """
    # --- Existence check up front, with a clear error message ---
    if not os.path.exists(npz_path):
        raise FileNotFoundError(f"Dataset not found: {npz_path}")

    # allow_pickle=True is required because channel_names and class_names are
    # stored as object arrays of Python strings. The file itself is trusted
    # (it was written by our own preprocessing script), so this is safe.
    data = np.load(npz_path, allow_pickle=True)

    # --- Verify required keys are present before touching them ---
    required_keys = {'X', 'y', 'sfreq', 'channel_names', 'subject_id'}
    missing = required_keys - set(data.files)
    if missing:
        raise KeyError(
            f"{npz_path} is missing required arrays: {sorted(missing)}. "
            f"Found: {sorted(data.files)}. "
            f"Re-run ems_data_prep.py to regenerate."
        )

    # --- Extract arrays with explicit dtype casts ---
    # Cast defensively: even though ems_data_prep.py writes float32/int64,
    # never trust the file. A mismatched dtype downstream (e.g. float64 X)
    # silently doubles memory use and breaks GPU performance.
    X = np.asarray(data['X'], dtype=np.float32)
    y = np.asarray(data['y'], dtype=np.int64)
    sfreq = float(data['sfreq'])  # numpy scalar -> Python float
    channel_names = [str(c) for c in data['channel_names']]
    subject_id = str(data['subject_id'])

    # --- Structural validation ---
    if X.ndim != 3:
        raise ValueError(
            f"X must be 3D (n_epochs, n_channels, n_samples), got shape {X.shape}"
        )
    if y.ndim != 1:
        raise ValueError(f"y must be 1D, got shape {y.shape}")
    if X.shape[0] != y.shape[0]:
        raise ValueError(
            f"X and y are misaligned: {X.shape[0]} epochs vs {y.shape[0]} labels"
        )
    if X.shape[1] != len(channel_names):
        raise ValueError(
            f"Channel count mismatch: X has {X.shape[1]} channels but "
            f"channel_names has {len(channel_names)} entries"
        )

    # --- Label range validation ---
    # Catches stale .npz files generated before the 3-class merge, or
    # subjects whose labels weren't remapped correctly.
    unique_labels = np.unique(y)
    valid_range = set(range(N_CLASSES))
    if not set(unique_labels.tolist()).issubset(valid_range):
        raise ValueError(
            f"Labels in {npz_path} fall outside [0, {N_CLASSES - 1}]: "
            f"found {unique_labels.tolist()}. "
            f"Did the label remap run correctly?"
        )

    # --- Numerical health check ---
    # NaN/Inf in EEG inputs silently destroys training (loss goes to NaN
    # on the first batch). Cheaper to catch it at load time than to
    # debug a stalled training run.
    if not np.isfinite(X).all():
        n_bad = np.sum(~np.isfinite(X))
        raise ValueError(
            f"X in {npz_path} contains {n_bad} non-finite values (NaN/Inf). "
            f"Check the preprocessing pipeline for that subject."
        )

    # --- Sampling rate sanity ---
    # The training pipeline assumes 250 Hz post-decimation. A different
    # sfreq means EEGNet's kernLength will be wrong for this file.
    if sfreq <= 0:
        raise ValueError(f"sfreq must be positive, got {sfreq}")

    # --- Informational summary (single source of truth for downstream logs) ---
    label_counts = dict(zip(*np.unique(y, return_counts=True)))
    label_counts = {int(k): int(v) for k, v in label_counts.items()}
    print(
        f"Loaded {subject_id} from {npz_path}\n"
        f"  X: shape={X.shape}, dtype={X.dtype}, "
        f"range=[{X.min():.2e}, {X.max():.2e}]\n"
        f"  y: shape={y.shape}, dtype={y.dtype}, class counts={label_counts}\n"
        f"  sfreq: {sfreq} Hz, channels: {X.shape[1]}"
    )

    return X, y, sfreq, channel_names, subject_id


'''Model Builder:
This function builds the EEGNet using the repo linked above. We use and
train this EEGNet to perform a 3-way classification of pain tolerance.'''

def model_builder(n_channels, n_samples, s_freq, dropout_rate):
    kernel_length = int(s_freq * 0.5)
    print(f"Building EEGNet: C={n_channels}, T={n_samples}, kernLength={kernel_length}")
    model = EEGNet(
        nb_classes = N_CLASSES,
        Chans = n_channels,
        Samples = n_samples,
        dropoutRate = dropout_rate,
        kernLength = kernel_length,
        F1 = F1, D = D, F2 = F2,
        dropoutType = 'Dropout'
    )
    model.compile(
        loss='categorical_crossentropy',
        optimizer=tf.keras.optimizers.Adam(),
        metrics=['accuracy']
    )
    return model


def fit_scaler(X_train):
    """
    Fit a per-channel z-score scaler on training epochs only.

    Treats each channel as an independent feature. Computes one mean
    and one std per channel using all time samples from all training
    epochs of that channel combined. The resulting scaler can be applied
    to val/test data via apply_scaler() without recomputing statistics.

    Parameters
    ----------
    X_train : np.ndarray, shape (n_epochs, n_channels, n_samples)
        Training EEG epochs.

    Returns
    -------
    scaler : sklearn.preprocessing.StandardScaler
        Fitted scaler with .mean_ and .scale_ of length n_channels.
    """
    n_epochs, n_channels, n_samples = X_train.shape

    # Reshape so each row is one time sample across all channels:
    #   (n_epochs, n_channels, n_samples)
    #     -> transpose to (n_epochs, n_samples, n_channels)
    #     -> flatten to (n_epochs * n_samples, n_channels)
    # StandardScaler then computes per-column (per-channel) statistics.
    flat = X_train.transpose(0, 2, 1).reshape(-1, n_channels)

    scaler = StandardScaler().fit(flat)

    print(
        f"Fitted scaler on {n_epochs} epochs, {n_channels} channels.\n"
        f"  Per-channel mean range: [{scaler.mean_.min():.2e}, {scaler.mean_.max():.2e}]\n"
        f"  Per-channel std range:  [{scaler.scale_.min():.2e}, {scaler.scale_.max():.2e}]"
    )
    return scaler

def apply_scaler(X, scaler):
    """
    Apply a fitted per-channel scaler to EEG epochs.

    Parameters
    ----------
    X : np.ndarray, shape (n_epochs, n_channels, n_samples)
        Epochs to normalize. Can be train, val, or test data.
    scaler : sklearn.preprocessing.StandardScaler
        Scaler previously fit via fit_scaler().

    Returns
    -------
    X_scaled : np.ndarray, same shape and dtype as X
        Normalized epochs.
    """
    n_epochs, n_channels, n_samples = X.shape

    # Apply scaler under the same reshape used for fitting,
    # then reshape back to the original (n_epochs, n_channels, n_samples).
    flat = X.transpose(0, 2, 1).reshape(-1, n_channels)
    flat = scaler.transform(flat)
    X_scaled = flat.reshape(n_epochs, n_samples, n_channels).transpose(0, 2, 1)

    # Preserve the original dtype. StandardScaler upcasts to float64
    # internally, which doubles memory if not cast back.
    return X_scaled.astype(X.dtype, copy=False)


def train_fold(X_train, y_train, X_val, y_val, sfreq, dropout_rate, checkpoint_path):
    """
    Train one EEGNet model on a single train/val split.

    This is the core training primitive, reused for both within-subject
    training (one call) and LOSO cross-validation (one call per fold).
    The split itself is the caller's responsibility; this function just
    takes whatever splits it's given and trains on them.

    Parameters
    ----------
    X_train : np.ndarray, shape (n_train, n_channels, n_samples)
        Training EEG epochs, already z-score normalized.
    y_train : np.ndarray, shape (n_train,)
        Integer class labels in {0, ..., N_CLASSES - 1}.
    X_val : np.ndarray, shape (n_val, n_channels, n_samples)
        Validation EEG epochs, normalized with the training scaler.
    y_val : np.ndarray, shape (n_val,)
        Integer validation labels.
    sfreq : float
        Sample rate, used to scale EEGNet's temporal kernel.
    dropout_rate : float
        Dropout probability. Use DROPOUT_WITHIN (0.5) for within-subject
        training, DROPOUT_CROSS (0.25) for cross-subject training.
    checkpoint_path : str
        Where to save the best model weights during training.

    Returns
    -------
    model : tf.keras.Model
        Trained EEGNet with best-validation weights restored.
    history : tf.keras.callbacks.History
        Per-epoch training metrics (loss, accuracy, val_loss, val_accuracy).
    """
    # --- Reshape inputs to EEGNet's expected 4D format ---
    # EEGNet was written for Keras's "channels_last" image convention:
    # (batch, height, width, channels). For EEG, the "image" is the
    # channels-by-time matrix and there's a single "image channel."
    X_train_4d = X_train[..., np.newaxis]    # (n, C, T) -> (n, C, T, 1)
    X_val_4d   = X_val[..., np.newaxis]

    # --- One-hot encode labels for categorical_crossentropy ---
    # to_categorical([0, 2, 1, 0]) -> [[1,0,0], [0,0,1], [0,1,0], [1,0,0]]
    # Required because EEGNet's softmax output is shape (batch, N_CLASSES)
    # and the loss expects matching one-hot targets.
    y_train_oh = to_categorical(y_train, num_classes=N_CLASSES)
    y_val_oh   = to_categorical(y_val,   num_classes=N_CLASSES)

    # --- Compute class weights for imbalance handling ---
    # After the min+medium merge, the intermediate class is 2x the size of
    # the other two (40+40 vs 40 each). Without class weights, the model
    # can score 50% accuracy by always predicting "intermediate" and the
    # loss won't push back hard enough to learn the minority classes.
    # 'balanced' sets weight = n_samples / (n_classes * n_in_class), so
    # rare classes get up-weighted proportionally.
    cw = compute_class_weight(
        class_weight='balanced',
        classes=np.arange(N_CLASSES),
        y=y_train
    )
    class_weights = {i: float(w) for i, w in enumerate(cw)}
    print(f"Class weights: {class_weights}")

    # --- Build the model ---
    model = model_builder(
        n_channels=X_train.shape[1],
        n_samples=X_train.shape[2],
        s_freq=sfreq,
        dropout_rate=dropout_rate,
    )

    # --- Callbacks ---
    callbacks = [
        # Stop training when validation loss stops improving, and restore
        # the weights from the best epoch (not the last epoch). Without
        # restore_best_weights=True the returned model is whatever you
        # had at the last epoch, which is usually overfit by 10-50 epochs.
        EarlyStopping(
            monitor='val_loss',
            patience=PATIENCE_EARLY_STOP,
            restore_best_weights=True,
            verbose=1,
        ),
        # When val_loss plateaus, halve the learning rate. This often
        # unsticks training and squeezes out a few more percentage points.
        # min_lr=1e-6 prevents reducing into territory where the optimizer
        # makes essentially no progress per step.
        ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.5,
            patience=PATIENCE_LR_REDUCE,
            min_lr=1e-6,
            verbose=1,
        ),
        # Save the best-val-loss model to disk. Redundant with
        # restore_best_weights=True for in-memory use, but persists a copy
        # so you don't lose the model if the script crashes after training.
        ModelCheckpoint(
            filepath=checkpoint_path,
            monitor='val_loss',
            save_best_only=True,
            verbose=0,
        ),
    ]

    # --- Train ---
    # verbose=2 prints one line per epoch (vs verbose=1's progress bar,
    # which spams the terminal during long runs).
    history = model.fit(
        X_train_4d, y_train_oh,
        validation_data=(X_val_4d, y_val_oh),
        epochs=EPOCHS,
        batch_size=BATCH_SIZE,
        class_weight=class_weights,
        callbacks=callbacks,
        verbose=2,
    )

    # Report final state
    best_epoch = int(np.argmin(history.history['val_loss']))
    print(
        f"Training complete. Best epoch: {best_epoch + 1} of {len(history.history['val_loss'])}. "
        f"Best val_loss: {history.history['val_loss'][best_epoch]:.4f}, "
        f"val_accuracy: {history.history['val_accuracy'][best_epoch]:.4f}"
    )

    return model, history

def evaluate(model, X_test, y_test, label=""):
    """
    Evaluate a trained EEGNet on a held-out test set.

    Prints a confusion matrix and per-class precision/recall/F1, and
    returns a dict suitable for JSON serialization.

    Parameters
    ----------
    model : tf.keras.Model
        Trained EEGNet (typically the return value of train_fold).
    X_test : np.ndarray, shape (n_test, n_channels, n_samples)
        Test EEG epochs, normalized with the training scaler.
    y_test : np.ndarray, shape (n_test,)
        Integer test labels.
    label : str
        Identifier used in print output (e.g. "within-subject" or
        "LOSO fold 3 / subject EMS0007"). Purely cosmetic.

    Returns
    -------
    results : dict
        Contains accuracy, per-class metrics, confusion matrix,
        predicted classes, and class probabilities. JSON-safe.
    """
    # --- Reshape and predict ---
    X_test_4d = X_test[..., np.newaxis]
    y_pred_prob = model.predict(X_test_4d, verbose=0)  # shape (n_test, N_CLASSES)
    y_pred = np.argmax(y_pred_prob, axis=1)

    # --- Print human-readable summary ---
    print(f"\n========== Evaluation: {label} ==========")

    print("\nConfusion matrix (rows = true class, cols = predicted class):")
    cm = confusion_matrix(y_test, y_pred, labels=range(N_CLASSES))
    # Pretty-print with class names as headers
    header = "             " + "  ".join(f"{c[:8]:>8}" for c in CLASSES)
    print(header)
    for i, row in enumerate(cm):
        row_str = "  ".join(f"{v:>8d}" for v in row)
        print(f"  {CLASSES[i][:10]:>10}  {row_str}")

    print("\nClassification report:")
    print(classification_report(
        y_test, y_pred,
        labels=range(N_CLASSES),
        target_names=CLASSES,
        digits=3,
        zero_division=0,
    ))

    overall_acc = float((y_pred == y_test).mean())
    print(f"Overall accuracy: {overall_acc:.4f}")

    # --- Build serializable results dict ---
    # Cast everything to native Python types so json.dump doesn't choke
    # on numpy int64 / float32 / ndarray.
    return {
        'label': label,
        'accuracy': overall_acc,
        'confusion_matrix': cm.tolist(),
        'class_names': CLASSES,
        'predictions': y_pred.tolist(),
        'true_labels': y_test.tolist(),
        'probabilities': y_pred_prob.tolist(),
    }

def run_within_subject(npz_path, output_dir):
    """
    Train and evaluate EEGNet on a single subject using a 70/15/15 split.

    This is the realistic closed-loop deployment scenario: each user is
    calibrated individually, training only on their own data.

    Parameters
    ----------
    npz_path : str
        Path to one subject's preprocessed .npz file.
    output_dir : str
        Directory where the trained model, scaler, and results JSON
        will be written. Created if it doesn't exist.

    Returns
    -------
    results : dict
        Test-set evaluation dict from evaluate().
    """
    os.makedirs(output_dir, exist_ok=True)

    # --- Load ---
    X, y, sfreq, channel_names, subject_id = load_data(npz_path)

    # --- 70/15/15 stratified split ---
    # Two consecutive splits: first carve 70% train, then split the
    # remaining 30% into 15% val / 15% test. Stratify on y so each class
    # is represented proportionally in every split.
    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y,
        test_size=0.30,
        stratify=y,
        random_state=SEED,
    )
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp,
        test_size=0.50,
        stratify=y_temp,
        random_state=SEED,
    )
    print(
        f"Split sizes: train={len(X_train)}, val={len(X_val)}, test={len(X_test)}"
    )

    # --- Fit scaler on train, apply to all three splits ---
    scaler = fit_scaler(X_train)
    X_train = apply_scaler(X_train, scaler)
    X_val   = apply_scaler(X_val,   scaler)
    X_test  = apply_scaler(X_test,  scaler)

    # --- Train ---
    checkpoint_path = os.path.join(output_dir, f'{subject_id}_within.keras')
    model, history = train_fold(
        X_train, y_train, X_val, y_val,
        sfreq=sfreq,
        dropout_rate=DROPOUT_WITHIN,
        checkpoint_path=checkpoint_path,
    )

    # --- Evaluate on held-out test set ---
    results = evaluate(
        model, X_test, y_test,
        label=f"within-subject test / {subject_id}",
    )
    results['subject_id'] = subject_id
    results['mode'] = 'within_subject'

    # --- Persist artifacts ---
    # Save scaler stats for inference time. The model alone isn't enough
    # to do inference correctly; you also need the per-channel mean and
    # std that were used during training.
    np.savez(
        os.path.join(output_dir, f'{subject_id}_scaler.npz'),
        mean=scaler.mean_,
        scale=scaler.scale_,
        channel_names=np.array(channel_names),
    )

    with open(os.path.join(output_dir, f'{subject_id}_results.json'), 'w') as f:
        json.dump(results, f, indent=2)

    # Also save training history for plotting later
    history_dict = {k: [float(x) for x in v] for k, v in history.history.items()}
    with open(os.path.join(output_dir, f'{subject_id}_history.json'), 'w') as f:
        json.dump(history_dict, f, indent=2)

    print(f"\nArtifacts saved to {output_dir}/")
    return results

def load_all_subjects(npz_glob):
    """
    Load and concatenate multiple subject .npz files into one big dataset.

    Parameters
    ----------
    npz_glob : str
        Glob pattern, e.g. 'EMS/EMS*.npz'.

    Returns
    -------
    X : np.ndarray, shape (total_epochs, n_channels, n_samples)
    y : np.ndarray, shape (total_epochs,)
    subject_ids : np.ndarray, shape (total_epochs,), dtype str
        Subject identifier for each epoch, used as the LOSO grouping key.
    sfreq : float
    channel_names : list[str]
    """
    import glob

    paths = sorted(glob.glob(npz_glob))
    if not paths:
        raise FileNotFoundError(f"No files matched glob: {npz_glob}")

    Xs, ys, sids = [], [], []
    reference_sfreq = None
    reference_channels = None

    for path in paths:
        X, y, sfreq, channel_names, subject_id = load_data(path)

        # Enforce consistency across subjects. Mixing sample rates or
        # channel sets in one dataset is a silent disaster.
        if reference_sfreq is None:
            reference_sfreq = sfreq
            reference_channels = channel_names
        else:
            if sfreq != reference_sfreq:
                raise ValueError(
                    f"{path} has sfreq={sfreq}, expected {reference_sfreq}"
                )
            if channel_names != reference_channels:
                raise ValueError(
                    f"{path} has different channel set than the first file."
                )

        Xs.append(X)
        ys.append(y)
        sids.append(np.array([subject_id] * len(y)))

    X = np.concatenate(Xs, axis=0)
    y = np.concatenate(ys, axis=0)
    subject_ids = np.concatenate(sids, axis=0)

    print(
        f"\nLoaded {len(paths)} subjects, {len(X)} total epochs.\n"
        f"  Unique subjects: {len(np.unique(subject_ids))}\n"
        f"  Class distribution: "
        f"{dict(zip(*np.unique(y, return_counts=True)))}"
    )
    return X, y, subject_ids, reference_sfreq, reference_channels


def run_loso(npz_glob, output_dir):
    """
    Leave-One-Subject-Out cross-validation across all matched subject files.

    For each fold:
      1. Hold out one subject as the test set.
      2. From the remaining N-1 subjects, carve a 15% stratified val set.
      3. Fit scaler on train only, apply to val and test.
      4. Train EEGNet with cross-subject dropout (0.25).
      5. Evaluate on the held-out subject.

    Parameters
    ----------
    npz_glob : str
        Glob pattern matching subject .npz files.
    output_dir : str
        Where per-fold artifacts and the LOSO summary are written.

    Returns
    -------
    summary : dict
        Aggregated metrics across all folds.
    """
    os.makedirs(output_dir, exist_ok=True)

    X, y, subject_ids, sfreq, channel_names = load_all_subjects(npz_glob)

    logo = LeaveOneGroupOut()
    fold_results = []

    for fold_idx, (trainval_idx, test_idx) in enumerate(
        logo.split(X, y, groups=subject_ids)
    ):
        held_out = str(np.unique(subject_ids[test_idx])[0])
        print(f"\n{'=' * 60}")
        print(f"Fold {fold_idx + 1} of {len(np.unique(subject_ids))}: "
              f"holding out {held_out}")
        print('=' * 60)

        X_trainval = X[trainval_idx]
        y_trainval = y[trainval_idx]
        X_test = X[test_idx]
        y_test = y[test_idx]

        # Carve val out of trainval. Stratify keeps class balance.
        X_train, X_val, y_train, y_val = train_test_split(
            X_trainval, y_trainval,
            test_size=0.15,
            stratify=y_trainval,
            random_state=SEED,
        )

        # Scaler fit on train only
        scaler = fit_scaler(X_train)
        X_train = apply_scaler(X_train, scaler)
        X_val   = apply_scaler(X_val,   scaler)
        X_test  = apply_scaler(X_test,  scaler)

        checkpoint_path = os.path.join(
            output_dir, f'loso_fold{fold_idx:02d}_{held_out}.keras'
        )

        model, history = train_fold(
            X_train, y_train, X_val, y_val,
            sfreq=sfreq,
            dropout_rate=DROPOUT_CROSS,
            checkpoint_path=checkpoint_path,
        )

        results = evaluate(
            model, X_test, y_test,
            label=f"LOSO fold {fold_idx + 1} / held-out {held_out}",
        )
        results['fold_idx'] = fold_idx
        results['held_out_subject'] = held_out
        fold_results.append(results)

        # Free memory before next fold. EEGNet is small, but stacked
        # across 30 folds + intermediate tensors, the leak adds up.
        tf.keras.backend.clear_session()

    # --- Aggregate ---
    accs = np.array([r['accuracy'] for r in fold_results])
    summary = {
        'mode': 'loso',
        'n_folds': len(fold_results),
        'mean_accuracy': float(accs.mean()),
        'std_accuracy': float(accs.std()),
        'min_accuracy': float(accs.min()),
        'max_accuracy': float(accs.max()),
        'per_fold': fold_results,
    }

    print(f"\n{'=' * 60}")
    print(f"LOSO Summary")
    print('=' * 60)
    print(f"Mean accuracy: {summary['mean_accuracy']:.4f} ± "
          f"{summary['std_accuracy']:.4f}")
    print(f"Range: [{summary['min_accuracy']:.4f}, {summary['max_accuracy']:.4f}]")
    print(f"Per-fold accuracies: "
          f"{[f'{a:.3f}' for a in accs]}")

    with open(os.path.join(output_dir, 'loso_summary.json'), 'w') as f:
        json.dump(summary, f, indent=2)

    return summary