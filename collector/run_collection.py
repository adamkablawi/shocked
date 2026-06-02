import os
import threading
from datetime import datetime

import config
import lsl_source
from epocher import Epocher
from storage import make_saver
from triggers.keyboard import KeyboardTrigger


def main():
    session_name = f'epochs_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
    session_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), session_name)
    os.makedirs(session_dir, exist_ok=True)
    print(f"Session folder: {session_dir}\n")

    inlet, srate, n_ch, channel_names = lsl_source.connect()
    pre_samples = int((config.PRE_MS / 1000) * srate)
    post_samples = int((config.POST_MS / 1000) * srate)
    print(f"Connected: {n_ch} channels at {srate} Hz")
    print(f"Channels: {channel_names}")
    print(f"Epoch: {pre_samples + post_samples} samples ({config.PRE_MS} ms pre + {config.POST_MS} ms post)")
    print("Press Space to capture, Q to quit\n")

    saver = make_saver(session_dir, channel_names, srate, config.PRE_MS, config.POST_MS)
    epocher = Epocher(srate, config.PRE_MS, config.POST_MS, on_epoch=saver)

    stop_flag = threading.Event()
    trigger = KeyboardTrigger(on_trigger=epocher.trigger, on_stop=stop_flag.set)
    trigger.start()

    try:
        while not stop_flag.is_set():
            samples, timestamps = inlet.pull_chunk(timeout=0.01, max_samples=32)
            for sample, timestamp in zip(samples, timestamps):
                epocher.feed(sample, timestamp)
    except KeyboardInterrupt:
        print("\nInterrupted.")
    finally:
        stop_flag.set()
        trigger.stop()
        print(f"\nDone. Session saved in:\n  {session_dir}")


if __name__ == '__main__':
    main()
