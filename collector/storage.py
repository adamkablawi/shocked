import os
from datetime import datetime
import numpy as np

def make_saver(session_dir, channel_names, srate, pre_ms, post_ms):
    """Return an on_epoch callback that writes each epoch to its own .npz file."""
    saved = [0]

    def save(epoch_array, trigger_time):
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        path = os.path.join(session_dir, f'epoch_{stamp}.npz')
        np.savez(
            path,
            data=epoch_array,
            srate=srate,
            channel_names=np.array(channel_names),
            pre_ms=pre_ms,
            post_ms=post_ms,
            trigger_time=trigger_time,
        )
        saved[0] += 1
        print(f"  Epoch {saved[0]} saved → {path}")
        print(f"  Shape: {epoch_array.shape}. Press Space for next, Q to quit.\n")

    return save
