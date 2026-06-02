import pylsl
import numpy as np
from collections import deque
import threading
import json
import os
import msvcrt
from datetime import datetime

# Config all the epoch timing and channels
PRE_MS = 200 # Time pre live epoch
POST_MS = 1000 # Time of live epoch
CHANNEL_NAMES = ['F3', 'F4', 'C3', 'Cz', 'C4', 'P3', 'P4'] # Names of all EEG Channels

# Config all the files and directory jargon
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # Path Directory
SESSION_NAME = f'epochs_{datetime.now().strftime("%Y%m%d_%H%M%S")}' # Creates name for current session
SESSION_DIR = os.path.join(SCRIPT_DIR, SESSION_NAME) # Creates a path to session director
os.makedirs(SESSION_DIR, exist_ok=True) # Creates the new directory (to put the json & EEG data)
NPY_PATH = os.path.join(SESSION_DIR, f'{SESSION_NAME}.npy') # EEG data path
JSON_PATH = os.path.join(SESSION_DIR, f'{SESSION_NAME}_meta.json') # JSON Metadata path
print(f"Session folder: {SESSION_DIR}\n") # Just to show user the folder

# Connectivity Script
print("Connecting to EEG stream.")
streams = pylsl.resolve_byprop('type', 'EEG', timeout = 10) # Retrieved for pylsl connect
if not streams: # If stream not found quit
    print("No stream found.") 
    exit()

inlet = pylsl.StreamInlet(streams[0]) 
# Only one device, so only stream is in streams[0]
# Opens connection to one stream of data, samples start buffering into the 200ms buffer
info = inlet.info() 
# Metadata about the single stream
srate = float(info.nominal_srate())
# Sample rate, probably around 250 Hz depending on how we set it
n_ch = info.channel_count()
# Number of channels, in our case 7

# These are samples / channel of course
pre_samples = int((PRE_MS / 1000) * srate)
post_samples = int((POST_MS / 1000) * srate)
total = pre_samples + post_samples

print(f"Connected: {n_ch} channels, sampled at {srate} Hz")
print(f"Epoch: {total} samples ({pre_samples} pre + {post_samples} post)")
print("\Press 'Space' to capture epoch and 'Q' to quit + save\n")

# This is the queue designed to hold the 200ms of pre epoch data
pre_buf = deque(maxlen = pre_samples)
# And this one stores time samples to pair with the other queue
time_buf = deque(maxlen = pre_samples)

# This is all the state stuff
epochs = []
trigger_times = []
trigger_flag = threading.Event() # Flag indicating beginning of collection
stop_flag = threading.Event() # Flag indicating quitting the program
collecting = False # Collecting bool
post_buf = []

# This function waits for the keyboard's space or q
def keyboard_listener():
    while not stop_flag.is_set():
        if msvcrt.kbhit():
            key = msvcrt.getch()
            # If key is space, trigger the collection
            if key == b' ':
                trigger_flag.set()
            # If key is Q, quit the program
            elif key in (b'q', b'Q'):
                stop_flag.set()

kb = threading.Thread(target=keyboard_listener, daemon=True)
kb.start()

# This function saves the epochs on quit
def save():
    if not epochs:
        print("No epochs to save.")
        return

    data = np.array(epochs)  # shape is (n_epochs, n_channels, n_samples)
    np.save(NPY_PATH, data)

    meta = {
        'srate': srate,
        'n_channels': n_ch,
        'channel_names': CHANNEL_NAMES[:n_ch],
        'pre_ms': PRE_MS,
        'post_ms': POST_MS,
        'n_epochs': len(epochs),
        'trigger_times': trigger_times,
    }

    with open(JSON_PATH, 'w') as f:
        json.dump(meta, f, indent = 2)

    print(f"\nSaved {len(epochs)} epochs to:")
    print(f"  Data: {NPY_PATH}")
    print(f"  Metadata: {JSON_PATH}")

# This is the main loop (we try unless there is a keyboard interrupt)
try:
    # Loop while the stop_flag hasn't been set yet
    while not stop_flag.is_set():

        # Pull whatever samples have built up since the last iteration
        samples, timestamps = inlet.pull_chunk(timeout=0.01, max_samples=32)

        # Walk through each sample and its timestamp together
        for sample, timestamp in zip(samples, timestamps):

            if not collecting:
                # Keep the rolling 200ms buffer topped up with fresh samples
                pre_buf.append(sample)
                time_buf.append(timestamp)

                if trigger_flag.is_set():
                    # Clear the flag so it doesn't trigger again immediately
                    trigger_flag.clear()

                    # Don't collect if we haven't filled the pre-stimulus buffer yet
                    if len(pre_buf) < pre_samples:
                        print("  Buffer not full yet. No rush!")
                        continue

                    # Lock in the trigger timestamp and start collecting post-stimulus
                    trigger_times.append(timestamp)
                    collecting = True
                    post_buf = []
                    n = len(epochs) + 1
                    print(f"  Trigger {n} captured at t = {timestamp:.3f}. Collecting {POST_MS}ms:")

            else:
                # We're in the post-stimulus window, keep appending samples
                post_buf.append(sample)

                if len(post_buf) >= post_samples:
                    # Put the pre and post buffers into one 1200ms epoch
                    epoch_samples = list(pre_buf) + post_buf
                    # Switch so shape is (n_channels, n_samples) not (n_samples, n_channels)
                    epoch_array = np.array(epoch_samples).T

                    # Store the finished epoch and reset for the next one
                    epochs.append(epoch_array)
                    collecting = False
                    post_buf = []

                    print(f"  Epoch {len(epochs)} complete. Shape: {epoch_array.shape}")
                    print(f"  Press 'Space' for next epoch, 'Q' to quit\n")

except KeyboardInterrupt:
    print("\nInterrupted.")

finally:
    # Always save on the way out, whether Q was pressed or Ctrl+C
    stop_flag.set()
    save()