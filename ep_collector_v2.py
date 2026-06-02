import pylsl
import numpy as np
from collections import deque
import threading
import os
import msvcrt
from datetime import datetime

# Config all the epoch timing
PRE_MS = 200 # Time pre live epoch
POST_MS = 1000 # Time of live epoch

# Config all the files and directory jargon
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # Path Directory
SESSION_NAME = f'epochs_{datetime.now().strftime("%Y%m%d_%H%M%S")}' # Creates name for current session
SESSION_DIR = os.path.join(SCRIPT_DIR, SESSION_NAME) # Creates a path to session director
os.makedirs(SESSION_DIR, exist_ok=True) # Creates the new directory (to put each epoch file in)
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
pre_samples = int((PRE_MS / 1000) * srate)
post_samples = int((POST_MS / 1000) * srate)
total = pre_samples + post_samples

print(f"Connected: {n_ch} channels, sampled at {srate} Hz")
print(f"Channels: {channel_names}")
print(f"Epoch: {total} samples ({pre_samples} pre + {post_samples} post)")
print("\nPress 'Space' to capture epoch and 'Q' to quit\n")

# This is the queue designed to hold the 200ms of pre epoch data
pre_buf = deque(maxlen = pre_samples)
# And this one stores time samples to pair with the other queue
time_buf = deque(maxlen = pre_samples)

# This is all the state stuff
trigger_flag = threading.Event() # Flag indicating beginning of collection
stop_flag = threading.Event() # Flag indicating quitting the program
collecting = False # Collecting bool
post_buf = []
saved_count = 0 # Running tally of epochs written to disk
current_trigger_time = None # LSL timestamp of the trigger we're currently collecting

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

# This function writes a single finished epoch straight to its own .npz file
def save_epoch(epoch_array, trigger_time):
    # Timestamp the filename down to microseconds so triggers never collide
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    path = os.path.join(SESSION_DIR, f'epoch_{stamp}.npz')

    # Bundle the data and its metadata together so the file stands on its own
    np.savez(
        path,
        data = epoch_array,              # shape is (n_channels, n_samples)
        srate = srate,
        channel_names = np.array(channel_names),
        pre_ms = PRE_MS,
        post_ms = POST_MS,
        trigger_time = trigger_time,     # LSL timestamp of the trigger
    )
    return path

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
                    current_trigger_time = timestamp
                    collecting = True
                    post_buf = []
                    print(f"  Trigger {saved_count + 1} captured at t = {timestamp:.3f}. Collecting {POST_MS}ms:")

            else:
                # We're in the post-stimulus window, keep appending samples
                post_buf.append(sample)

                if len(post_buf) >= post_samples:
                    # Put the pre and post buffers into one 1200ms epoch
                    epoch_samples = list(pre_buf) + post_buf
                    # Switch so shape is (n_channels, n_samples) not (n_samples, n_channels)
                    epoch_array = np.array(epoch_samples).T

                    # Save this epoch to its own file right now, then reset for the next one
                    path = save_epoch(epoch_array, current_trigger_time)
                    saved_count += 1
                    collecting = False
                    post_buf = []

                    print(f"  Epoch {saved_count} complete. Shape: {epoch_array.shape}")
                    print(f"  Saved: {path}")
                    print(f"  Press 'Space' for next epoch, 'Q' to quit\n")

except KeyboardInterrupt:
    print("\nInterrupted.")

finally:
    # Nothing to flush, epochs are already on disk. Just stop and report.
    stop_flag.set()
    print(f"\nDone. {saved_count} epochs saved in:\n  {SESSION_DIR}")