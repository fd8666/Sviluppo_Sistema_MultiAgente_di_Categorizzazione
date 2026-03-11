import time


class Throttler:
    """
    Semplice throttler sincrono:
    garantisce almeno min_interval_sec tra due chiamate .wait()
    """

    def __init__(self, min_interval_sec: float = 1.0):
        self.min_interval = min_interval_sec
        self._last_call = 0.0

    def wait(self):
        if self.min_interval <= 0:
            return

        now = time.monotonic()
        elapsed = now - self._last_call

        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)

        self._last_call = time.monotonic()
