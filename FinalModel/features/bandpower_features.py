"""
bandpower_features.py
=====================
Band-power (induced spectral) feature extraction, mirroring the design of
erp_features.py. This reconstructs the spectral pipeline that achieved the
higher multi-class accuracy: log Welch PSD per channel per canonical band.

sklearn-compatible (fit / transform) so it drops into the same Pipeline and
cross-validation machinery as the ERP extractor, with no leakage (extraction
uses no labels).

Features (per channel, per trial): log power in delta, theta, alpha, beta, gamma.
    n_features = n_channels * 5

Channel sets are named so the runner can compare them:
    "all60"        : every channel in the file
    "sensorimotor" : ~14 central/parietal channels
    "central_fc"   : the 8 central / fronto-central channels used for ERP

Example
-------
    from bandpower_features import BandPowerExtractor
    from erp_features import load_npz_for_features
    X, y, meta = load_npz_for_features("EMS0001.npz")
    fx = BandPowerExtractor(channel_set="all60").set_meta(meta)
    F = fx.fit_transform(X)            # (n_trials, n_channels*5)
    names = fx.feature_names_
"""

from __future__ import annotations
import numpy as np
from scipy.signal import welch

try:
    from sklearn.base import BaseEstimator, TransformerMixin
except Exception:
    class BaseEstimator:
        def get_params(self, deep=True): return {}
        def set_params(self, **p): return self
    class TransformerMixin:
        def fit_transform(self, X, y=None, **kw):
            return self.fit(X, y, **kw).transform(X, **kw)


# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
BANDS = {"delta": (1, 4), "theta": (4, 8), "alpha": (8, 13),
         "beta": (13, 30), "gamma": (30, 45)}

SENSORIMOTOR = ["C3", "C4", "Cz", "C1", "C2", "FC1", "FC2", "FC3", "FC4",
                "CP1", "CP2", "CP3", "CP4", "P3", "P4", "Pz"]
CENTRAL_FC   = ["C3", "Cz", "C4", "FCz", "FC1", "FC2", "FC3", "FC4"]

# Analysis window (s) over which the spectrum is computed. None = full epoch.
# The original spectral run used the whole post-stim window.
SPECTRAL_WIN = None     # e.g. (0.0, 1.5) or None for the whole epoch

LOG_OFFSET = 1e-12      # avoids log(0)


class BandPowerExtractor(BaseEstimator, TransformerMixin):
    """
    Log band-power features via Welch PSD.

    Parameters
    ----------
    channel_set : str
        "all60" | "sensorimotor" | "central_fc" | "custom"
    channels : list[str] or None
        Explicit channel list when channel_set == "custom".
    relative : bool
        If True, normalize each band by total (1-45 Hz) power per channel/trial,
        which reduces inter-subject amplitude differences (helps cross-subject).
    nperseg : int
        Welch segment length (samples); capped at the window length.
    """

    def __init__(self, channel_set="all60", channels=None,
                 relative=False, nperseg=128):
        self.channel_set = channel_set
        self.channels = channels
        self.relative = relative
        self.nperseg = nperseg
        self._meta = None

    def set_meta(self, meta):
        self._meta = meta
        return self

    def _get_meta(self, meta):
        m = meta if meta is not None else self._meta
        if m is None:
            raise ValueError("meta must be provided (channel_names, sfreq, times).")
        return m

    def _resolve_channels(self, ch_names):
        if self.channel_set == "all60":
            return list(range(len(ch_names))), list(ch_names)
        if self.channel_set == "sensorimotor":
            want = SENSORIMOTOR
        elif self.channel_set == "central_fc":
            want = CENTRAL_FC
        elif self.channel_set == "custom":
            want = self.channels or []
        else:
            raise ValueError(f"Unknown channel_set '{self.channel_set}'")
        idx = [ch_names.index(c) for c in want if c in ch_names]
        names = [ch_names[i] for i in idx]
        if not idx:
            raise ValueError(f"None of the requested channels found for set "
                             f"'{self.channel_set}'.")
        return idx, names

    def fit(self, X, y=None, meta=None):
        m = self._get_meta(meta)
        ch_names = list(m["channel_names"])
        self.ch_indices_, self.ch_used_ = self._resolve_channels(ch_names)
        self.sfreq_ = float(m["sfreq"])
        self.times_ = np.asarray(m["times"])
        self.feature_names_ = [f"{band}@{ch}"
                               for band in BANDS
                               for ch in self.ch_used_]
        return self

    def transform(self, X, meta=None):
        if not hasattr(self, "ch_indices_"):
            raise RuntimeError("Call fit before transform.")
        X = np.asarray(X, dtype=float)
        sub = X[:, self.ch_indices_, :]              # (trials, ch, times)

        # Optional spectral analysis window
        if SPECTRAL_WIN is not None:
            t = self.times_
            wmask = (t >= SPECTRAL_WIN[0]) & (t <= SPECTRAL_WIN[1])
            sub = sub[:, :, wmask]

        nperseg = min(self.nperseg, sub.shape[-1])
        freqs, psd = welch(sub, fs=self.sfreq_, nperseg=nperseg, axis=-1)
        # psd: (trials, ch, freqs)

        band_feats = []
        if self.relative:
            tot_mask = (freqs >= 1) & (freqs <= 45)
            total = psd[:, :, tot_mask].sum(axis=-1, keepdims=True) + LOG_OFFSET
        for lo, hi in BANDS.values():
            bm = (freqs >= lo) & (freqs <= hi)
            bp = psd[:, :, bm].mean(axis=-1)         # (trials, ch)
            if self.relative:
                bp = bp / total[:, :, 0]
            band_feats.append(np.log(bp + LOG_OFFSET))
        F = np.concatenate(band_feats, axis=1)       # (trials, ch*5)
        return F
