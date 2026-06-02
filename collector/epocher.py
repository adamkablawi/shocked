import threading
from collections import deque

import numpy as np


class Epocher:
    """Rolling-buffer epoch extractor.

    Knows nothing about what triggers it or what consumes the finished epoch.
    Call trigger() from any source; feed() with every incoming sample.
    When the post-stimulus window fills, on_epoch(array, trigger_time) fires.
    """

    def __init__(self, srate, pre_ms, post_ms, on_epoch):
        self._pre_samples = int((pre_ms / 1000) * srate)
        self._post_samples = int((post_ms / 1000) * srate)
        self._post_ms = post_ms
        self._on_epoch = on_epoch

        self._pre_buf = deque(maxlen=self._pre_samples)
        self._time_buf = deque(maxlen=self._pre_samples)
        self._post_buf = []
        self._collecting = False
        self._trigger_time = None
        self._count = 0
        self._trigger_event = threading.Event()

    @property
    def total_samples(self):
        return self._pre_samples + self._post_samples

    def trigger(self):
        """Signal that an epoch should begin on the next incoming sample."""
        self._trigger_event.set()

    def feed(self, sample, timestamp):
        """Push one sample into the epocher; call this for every incoming sample."""
        if not self._collecting:
            self._pre_buf.append(sample)
            self._time_buf.append(timestamp)

            if self._trigger_event.is_set():
                self._trigger_event.clear()
                if len(self._pre_buf) < self._pre_samples:
                    print("  Pre-buffer not full yet — hold on.")
                    return
                self._trigger_time = timestamp
                self._collecting = True
                self._post_buf = []
                self._count += 1
                print(f"  Trigger {self._count} at t={timestamp:.3f}. Collecting {self._post_ms} ms...")
        else:
            self._post_buf.append(sample)
            if len(self._post_buf) >= self._post_samples:
                epoch_samples = list(self._pre_buf) + self._post_buf
                epoch_array = np.array(epoch_samples).T  # (n_channels, n_samples)
                self._collecting = False
                self._post_buf = []
                self._on_epoch(epoch_array, self._trigger_time)
