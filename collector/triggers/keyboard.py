import msvcrt
import threading


class KeyboardTrigger:
    """Windows keyboard backend. Space fires on_trigger(); Q fires on_stop()."""

    def __init__(self, on_trigger, on_stop):
        self._on_trigger = on_trigger
        self._on_stop = on_stop
        self._stop_flag = threading.Event()
        self._thread = threading.Thread(target=self._listen, daemon=True)

    def start(self):
        self._thread.start()

    def stop(self):
        self._stop_flag.set()

    def _listen(self):
        while not self._stop_flag.is_set():
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key == b' ':
                    self._on_trigger()
                elif key in (b'q', b'Q'):
                    self._on_stop()
