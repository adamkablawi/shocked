import pylsl
import pickle
import numpy as np
from collections import deque
from scipy.signal import welch
from scipy.signal import butter, iirnotch, filtfilt, detrend
import queue
import threading

# Each window contains WINDOW_MS + OVERLAP_MS ms of raw EEG data
WINDOW_MS = 1500  # Time between windows (non-overlapping stride), in ms
OVERLAP_MS = 2000  # How far back into the previous window each new window reaches, in ms

# Filter configuration
BANDPASS_LOW_HZ  = 0.0     # set to None to skip highpass
BANDPASS_HIGH_HZ = 100.0   # set to None to skip lowpass; must be < srate/2
NOTCH_HZ         = 50.0    # set to None to skip; 50.0 outside the Americas, 60 in
NOTCH_Q          = 25.0
FILTER_ORDER     = 4
USE_CAR          = True    # common average reference
USE_DETREND      = True

def _build_filters(fs):
    nyq = fs / 2
    bp = None
    if BANDPASS_LOW_HZ is not None and BANDPASS_HIGH_HZ is not None:
        assert (BANDPASS_HIGH_HZ < nyq, f"Lowpass {BANDPASS_HIGH_HZ} >= Nyquist {nyq}")
        bp = butter(FILTER_ORDER, [BANDPASS_LOW_HZ, BANDPASS_HIGH_HZ], btype='band', fs=fs)
    elif BANDPASS_LOW_HZ is not None:
        bp = butter(FILTER_ORDER, BANDPASS_LOW_HZ, btype='high', fs=fs)
    elif BANDPASS_HIGH_HZ is not None:
        bp = butter(FILTER_ORDER, BANDPASS_HIGH_HZ, btype='low', fs=fs)

    notch = None
    if NOTCH_HZ is not None and NOTCH_HZ < nyq:
        notch = iirnotch(w0=NOTCH_HZ, Q=NOTCH_Q, fs=fs)

    return bp, notch

# Sanity-check filter edge-effect length against the actual window size.
# filtfilt's transient is roughly 3 * max(len(a), len(b)) samples per edge.
def _check_edge_safety(total_samples, overlap_samples):
    worst = 0
    for coeffs in (_BP, _NOTCH):
        if coeffs is not None:
            b, a = coeffs
            worst = max(worst, 3 * max(len(a), len(b)))
    if worst > overlap_samples:
        print(f"  [warn] filter transient ~{worst} samples > overlap "
              f"{overlap_samples}; consider increasing OVERLAP_MS.")

def preprocess(epoch):
    x = epoch.astype(np.float64, copy=True)
    if USE_DETREND:
        x = detrend(x, axis=1, type='constant')
    if _BP is not None:
        b, a = _BP
        x = filtfilt(b, a, x, axis=1)
    if _NOTCH is not None:
        b, a = _NOTCH
        x = filtfilt(b, a, x, axis=1)
    if USE_CAR and x.shape[0] >= 2:
        x -= x.mean(axis=0, keepdims=True)
    return x

# Connectivity Script
print("Connecting to EEG stream.")
streams = pylsl.resolve_byprop('type', 'EEG', timeout=10)   # Retrieved for pylsl connect
if not streams:                                             # If stream not found quit
    print("No stream found.")
    exit()

inlet = pylsl.StreamInlet(streams[0])   # Only one device, so only stream is in streams[0]
info = inlet.info()                     # Metadata about the single stream
srate = float(info.nominal_srate())     # Sample rate, probably 250 Hz depending on how we set it
n_ch = info.channel_count()             # Number of channels, depends on the device


# Try to pull the real channel labels straight out of the LSL stream's metadata
channel_names = []
ch = info.desc().child('channels').child('channel') # First channel node in the XML
for i in range(n_ch):
    label = ch.child_value('label')                 # Grab channel's label, empty string if missing
    if label: channel_names.append(label)
    else: channel_names.append(f'Ch{i + 1}')        # Stream didn't label, fall to generic name
    ch = ch.next_sibling()                          # Walk to the next channel node

# These are samples / channel of course
window_samples = int((WINDOW_MS  / 1000) * srate)   # Samples in one stride
overlap_samples = int((OVERLAP_MS / 1000) * srate)  # Samples of lookback overlap
total_samples = window_samples + overlap_samples    # Total samples per epoch

# Build once using whatever srate the stream reported
_BP, _NOTCH = _build_filters(srate)
_check_edge_safety(total_samples, overlap_samples)

print(f"Connected: {n_ch} channels, sampled at {srate} Hz")
print(f"Channels: {channel_names}")
print(f"Window: {total_samples} samples ({overlap_samples} overlap + {window_samples} stride)")
print("\nRunning continuously. Press Ctrl+C to stop.\n")

# Rolling buffer sized to hold one window at all times
# Oldest samples fall off as new ones come in.
buf = deque(maxlen=total_samples)
samples_since_last = 0 # Counts new samples since the last window was emitted

# This queue passes finished windows to the pipeline worker thread
# Shape of each item: (n_channels, total_samples), ready for preprocessing and inference
window_queue: "queue.Queue[np.ndarray]" = queue.Queue()

# This is where the ML pipeline lives
def process_window(epoch_array: np.ndarray):
    clean = preprocess(epoch_array)
    # TODO: Model
    pass

# This worker drains the queue so the main acquisition loop never blocks
def pipeline_worker():
    while True:
        try:
            epoch_array = window_queue.get(timeout=0.5)
            process_window(epoch_array)
            window_queue.task_done()
        except queue.Empty:
            # Nothing in the queue, check if we should shut down
            if stop_flag.is_set():
                break

# This is all the state stuff
stop_flag = threading.Event()   # Shut down flag
window_count = 0                # Running tally of windows emitted

worker = threading.Thread(target=pipeline_worker, daemon=True)
worker.start()

# This is the main loop (we try unless there is a keyboard interrupt)
# Not to be touched in general
try:
    while True:
        # Pull whatever samples have built up since the last iteration
        samples, timestamps = inlet.pull_chunk(timeout=0.01, max_samples=50)

        # Walk through each sample and its timestamp together
        for sample, timestamp in zip(samples, timestamps):
            buf.append(sample)
            samples_since_last += 1

            # Once the buffer is full and we've accumulated a full stride of new samples,
            # the window is ready. The overlap is already in the buffer.
            if len(buf) >= total_samples and samples_since_last >= window_samples:
                # Switch so shape is (n_channels, n_samples) not (n_samples, n_channels)
                epoch_array = np.array(buf).T
                window_queue.put(epoch_array)
                window_count += 1
                samples_since_last = 0 # Reset stride counter for next window
                print(f"  Window {window_count} queued. Shape: {epoch_array.shape}")

except KeyboardInterrupt:
    print("\nInterrupted.")

finally:
    stop_flag.set()
    worker.join()
    print(f"\nDone. {window_count} windows produced.")

'''
# This comment contains code for a kmeans clustering model,
# just to demonstrate the capabilities of the pipeline.
_BANDS = {"delta": (0.5, 4), "theta": (4, 8), "alpha": (8, 13), "beta": (13, 30), "gamma": (30, 100)}

def _band_power(psd, freqs, fmin, fmax):
    mask = (freqs >= fmin) & (freqs <= fmax)
    return np.trapz(psd[mask], freqs[mask])

def _extract_features(window, fs):
    features = []
    for ch in range(window.shape[0]):
        freqs, psd = welch(window[ch], fs=fs, nperseg=min(128, window.shape[1]))
        for fmin, fmax in _BANDS.values():
            features.append(_band_power(psd, freqs, fmin, fmax))
    return np.array(features)

_model_artifact = None
try:
    with open("kmeans/eeg_kmeans_fake.pkl", "rb") as _f:
        _model_artifact = pickle.load(_f)
    print("Loaded eeg_kmeans_fake.pkl, inference enabled.")
except FileNotFoundError:
    print("eeg_kmeans_fake.pkl not found, inference disabled.")


# This is where the ML pipeline lives, as of now uses the kmeans clustering model
def process_window(epoch_array: np.ndarray):
    if _model_artifact is None:
        print(f"  Window {window_count}: no model loaded, skipping inference.")
        return
    feats = _extract_features(epoch_array, srate).reshape(1, -1)
    feats_scaled = _model_artifact["scaler"].transform(feats)
    cluster = int(_model_artifact["model"].predict(feats_scaled)[0])
    pc = _model_artifact["pca"].transform(feats_scaled)[0]
    print(f"  Window {window_count}: cluster={cluster}  PC1={pc[0]:+.2f}  PC2={pc[1]:+.2f}")
'''