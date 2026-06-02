import pylsl
import numpy as np
from collections import deque
import queue
import threading

# Config all the window timing
WINDOW_MS = 1000  # Time between windows (non-overlapping stride), in ms
OVERLAP_MS = 200  # How far back into the previous window each new window reaches, in ms
# So each window actually contains WINDOW_MS + OVERLAP_MS ms of raw EEG data

# Connectivity Script
print("Connecting to EEG stream.")
streams = pylsl.resolve_byprop('type', 'EEG', timeout=10) # Retrieved for pylsl connect
if not streams: # If stream not found quit
    print("No stream found.")
    exit()

inlet = pylsl.StreamInlet(streams[0])
# Only one device, so only stream is in streams[0]
# Opens connection to one stream of data, samples start buffering immediately
info = inlet.info()
# Metadata about the single stream
srate = float(info.nominal_srate())
# Sample rate, probably around 250 Hz depending on how we set it
n_ch = info.channel_count()
# Number of channels, depends on the device

# Try to pull the real channel labels straight out of the LSL stream's metadata
channel_names = []
ch = info.desc().child('channels').child('channel') # First channel node in the XML
for i in range(n_ch):
    label = ch.child_value('label') # Grab this channel's label, empty string if missing
    if label:
        channel_names.append(label)
    else:
        # Stream didn't bother labeling this one, fall back to a generic name
        channel_names.append(f'Ch{i + 1}')
    ch = ch.next_sibling() # Walk to the next channel node

# These are samples / channel of course
window_samples = int((WINDOW_MS  / 1000) * srate) # Samples in one stride
overlap_samples = int((OVERLAP_MS / 1000) * srate) # Samples of lookback overlap
total_samples = window_samples + overlap_samples  # Samples per emitted window

print(f"Connected: {n_ch} channels, sampled at {srate} Hz")
print(f"Channels: {channel_names}")
print(f"Window: {total_samples} samples ({overlap_samples} overlap + {window_samples} stride)")
print("\nRunning continuously. Press Ctrl+C to stop.\n")

# Rolling buffer sized to hold exactly one full window at all times
# The deque's maxlen handles the overlap automatically - oldest samples fall off
# as new ones come in, so we always have the right lookback sitting there
buf = deque(maxlen=total_samples)
samples_since_last = 0 # Counts new samples since the last window was emitted

# This queue passes finished windows to the pipeline worker thread
# Shape of each item: (n_channels, total_samples), ready for preprocessing and inference
window_queue: "queue.Queue[np.ndarray]" = queue.Queue()

# This is where the ML pipeline will live once it's built
# Right now it's a stub and just receives the window and does nothing with it
def process_window(epoch_array: np.ndarray):
    np.savez(f'window_{window_count}.npz', data=epoch_array)
    window_count += 1
    print(f"  Window {window_count} saved. Shape: {epoch_array.shape}")

# This worker drains the queue so the main acquisition loop never blocks
def pipeline_worker():
    while True:
        try:
            epoch_array = window_queue.get(timeout=0.5)
            process_window(epoch_array)
            window_queue.task_done()
        except queue.Empty:
            # Nothing in the queue right now - check if we should shut down
            if stop_flag.is_set():
                break

# This is all the state stuff
stop_flag = threading.Event() # Flag indicating the pipeline should shut down
window_count = 0 # Running tally of windows emitted

worker = threading.Thread(target=pipeline_worker, daemon=True)
worker.start()

# This is the main loop (we try unless there is a keyboard interrupt)
try:
    while True:
        # Pull whatever samples have built up since the last iteration
        samples, timestamps = inlet.pull_chunk(timeout=0.01, max_samples=32)

        # Walk through each sample and its timestamp together
        for sample, timestamp in zip(samples, timestamps):
            buf.append(sample)
            samples_since_last += 1

            # Once the buffer is full and we've accumulated a full stride of new samples,
            # the window is ready - the overlap is already sitting in the buffer for free
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
    # Signal the worker to wrap up and wait for it to finish
    stop_flag.set()
    worker.join()
    print(f"\nDone. {window_count} windows produced.")