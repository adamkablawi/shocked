import pylsl
import numpy as np
from collections import deque
import threading
import json
from datetime import datetime

# ── Config ─────────────────────────────────────────────────
PRE_MS        = 200
POST_MS       = 1000
CHANNEL_NAMES = ['F3', 'F4', 'C3', 'Cz', 'C4', 'P3', 'P4']
SAVE_FILE     = f'epochs_{datetime.now().strftime("%Y%m%d_%H%M%S")}'

# ── Connect to EEG stream ───────────────────────────────────
print("Looking for EEG stream...")
streams = pylsl.resolve_stream('type', 'EEG', timeout=10)
if not streams:
    print("No EEG stream found. Is the X.on app streaming?")
    exit()

inlet = pylsl.StreamInlet(streams[0])
info  = inlet.info()
srate = float(info.nominal_srate())
n_ch  = info.channel_count()

pre_samples  = int((PRE_MS  / 1000) * srate)
post_samples = int((POST_MS / 1000) * srate)
total        = pre_samples + post_samples

print(f"Connected — {n_ch}ch @ {srate}Hz")
print(f"Epoch: {total} samples ({pre_samples} pre + {post_samples} post)")
print("\nPress SPACE to capture epoch, Q to quit and save\n")

# ── Rolling pre-stimulus buffer ─────────────────────────────
pre_buf  = deque(maxlen=pre_samples)
time_buf = deque(maxlen=pre_samples)

# ── State ───────────────────────────────────────────────────
epochs        = []
trigger_times = []
trigger_flag  = threading.Event()
stop_flag     = threading.Event()
collecting    = False
post_buf      = []
current_trigger_time = None

# ── Keyboard listener ───────────────────────────────────────
def keyboard_listener():
    import msvcrt
    while not stop_flag.is_set():
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b' ':
                trigger_flag.set()
            elif key in (b'q', b'Q'):
                stop_flag.set()

kb = threading.Thread(target=keyboard_listener, daemon=True)
kb.start()

# ── Save ────────────────────────────────────────────────────
def save():
    if not epochs:
        print("No epochs to save.")
        return

    data = np.array(epochs)  # shape: (n_epochs, n_channels, n_samples)
    np.save(f'{SAVE_FILE}.npy', data)

    meta = {
        'srate':         srate,
        'n_channels':    n_ch,
        'channel_names': CHANNEL_NAMES[:n_ch],
        'pre_ms':        PRE_MS,
        'post_ms':       POST_MS,
        'n_epochs':      len(epochs),
        'trigger_times': trigger_times,
    }
    with open(f'{SAVE_FILE}_meta.json', 'w') as f:
        json.dump(meta, f, indent=2)

    print(f"\nSaved {len(epochs)} epochs → {SAVE_FILE}.npy")
    print(f"Metadata         → {SAVE_FILE}_meta.json")

# ── Main loop ───────────────────────────────────────────────
try:
    while not stop_flag.is_set():

        # pull latest samples into rolling buffer
        samples, timestamps = inlet.pull_chunk(timeout=0.01, max_samples=32)

        for sample, ts in zip(samples, timestamps):
            
            if not collecting:
                # always keep rolling pre-stimulus buffer topped up
                pre_buf.append(sample)
                time_buf.append(ts)

                # check for spacebar trigger
                if trigger_flag.is_set():
                    trigger_flag.clear()

                    # only collect if we have a full pre-stimulus buffer
                    if len(pre_buf) < pre_samples:
                        print("  Buffer not full yet — wait a moment and try again")
                        continue

                    # lock in this trigger time
                    current_trigger_time = ts
                    trigger_times.append(ts)

                    # start collecting post-stimulus samples
                    collecting = True
                    post_buf   = []
                    n          = len(epochs) + 1
                    print(f"  Trigger {n} captured at t={ts:.3f} — collecting {POST_MS}ms...")

            else:
                # collecting post-stimulus window
                post_buf.append(sample)

                if len(post_buf) >= post_samples:
                    # we have enough — assemble the full epoch
                    epoch_samples = list(pre_buf) + post_buf  # 1200ms total
                    epoch_array   = np.array(epoch_samples).T  # (n_channels, n_samples)

                    epochs.append(epoch_array)
                    collecting = False
                    post_buf   = []

                    print(f"  Epoch {len(epochs)} complete — shape: {epoch_array.shape}")
                    print(f"  Press SPACE for next epoch, Q to quit\n")

except KeyboardInterrupt:
    print("\nInterrupted.")

finally:
    stop_flag.set()
    save()