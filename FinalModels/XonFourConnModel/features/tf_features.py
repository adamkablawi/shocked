"""
tf_features.py
==============
Event-Related Desynchronization / Synchronization (ERD/ERS) feature extraction.

This is the time-frequency family for the modular LDA pipeline. Where
bandpower_features.py gives ONE static power value per band per trial, this
measures how band power *changes over time relative to the pre-stim baseline* --
the canonical Pfurtscheller ERD/ERS quantity:

    desynchronization (ERD) = power DROP vs baseline  (negative dB)
    synchronization   (ERS) = power RISE vs baseline  (positive dB)

Motivation for EMS intensity decoding: the stimulus response is a time-locked
modulation of ongoing rhythms (e.g. beta/mu desync, gamma sync), and its
*magnitude and timing* should scale with intensity. A whole-epoch average
(bandpower_features) washes that out; ERD/ERS keeps it.

Method (robust filter-Hilbert ERD/ERS):
  1. Band-pass each band with a 4th-order Butterworth in SECOND-ORDER-SECTIONS
     form (sosfiltfilt). SOS is numerically stable at low frequencies where the
     transfer-function (b,a) form is near-singular -- this is what made the old
     delta filter unreliable.
  2. Instantaneous power = |Hilbert envelope|^2.
  3. Express power in DECIBELS relative to the per-trial baseline mean:
         dB(t) = 10 * log10( power(t) / baseline_power )
     dB is bounded and symmetric, so it cannot explode the way the old
     percent formula (post - base)/base * 100 did when the baseline was tiny.
  4. Summarize the dB time course per channel per band into ERD/ERS features.

Features per channel per band (default):
    {band}_erd_early@{ch} : mean dB in the early window (default 0.00-0.30 s)
    {band}_erd_late@{ch}  : mean dB in the late window  (default 0.30-1.50 s)
    {band}_erd_peak@{ch}  : strongest desync = MIN smoothed dB in post window
    {band}_ers_peak@{ch}  : strongest sync   = MAX smoothed dB in post window
  Optional (include_latency=True):
    {band}_erd_lat@{ch}   : latency (s) of the ERD peak
    {band}_ers_lat@{ch}   : latency (s) of the ERS peak

sklearn-compatible (fit / transform / set_meta), leakage-safe (no labels used),
channel-set aware (all60 | sensorimotor | central_fc | custom), and band-subset
aware (e.g. bands=["delta","gamma"]).

Registered in train_combined.FEATURE_REGISTRY as "tf"; usable via run_combined,
feature_importance, feature_trends by putting "tf" in `families`.

Example
-------
    from tf_features import TFExtractor
    from erp_features import load_npz_for_features
    X, y, meta = load_npz_for_features("EMS0001.npz")
    fx = TFExtractor(channel_set="central_fc").set_meta(meta)
    F = fx.fit_transform(X)            # (n_trials, n_channels * n_summaries * n_bands)
    names = fx.feature_names_
"""

from __future__ import annotations
import warnings
import numpy as np
from scipy.signal import butter, sosfiltfilt, hilbert

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
# CONFIG  (bands match bandpower_features.py)
# ─────────────────────────────────────────────
BANDS = {"delta": (1, 4), "theta": (4, 8), "alpha": (8, 13),
         "beta": (13, 30), "gamma": (30, 45)}

SENSORIMOTOR  = ["C3", "C4", "Cz", "C1", "C2", "FC1", "FC2", "FC3", "FC4",
                "CP1", "CP2", "CP3", "CP4", "P3", "P4", "Pz"]
CENTRAL_FC    = ["C3", "Cz", "C4", "FCz", "FC1", "FC2", "FC3", "FC4"]
BEST_CHANNELS = ["FCz", "C4", "Fz", "FC4", "Cz", "C2", "FC2"]

# Time windows (s), relative to stimulus onset.
EARLY_WIN    = (0.00, 0.30)    # early transient response
LATE_WIN     = (0.30, 1.50)    # sustained response
BASELINE_WIN = (-0.20, 0.00)   # ERD/ERS reference (pre-stim)
POST_WIN     = (0.00, 1.50)    # window for peak ERD / ERS search

FILTER_ORDER = 4
SMOOTH_MS    = 100.0           # envelope smoothing for peak detection (ms)
PWR_EPS      = 1e-10           # keeps log argument strictly positive


def _design_sos(lo, hi, fs, order=FILTER_ORDER):
    """Stable band-pass as second-order sections (good down to ~1 Hz)."""
    ny = fs / 2.0
    hi = min(hi, ny - 1e-6)
    lo = max(lo, 1e-3)
    return butter(order, [lo / ny, hi / ny], btype="band", output="sos")


def _moving_average(x, k):
    """Smooth along the last axis with a length-k boxcar (odd k)."""
    if k <= 1:
        return x
    k = int(k) | 1                                   # force odd
    kernel = np.ones(k) / k
    pad = k // 2
    xp = np.pad(x, [(0, 0)] * (x.ndim - 1) + [(pad, pad)], mode="edge")
    return np.apply_along_axis(lambda m: np.convolve(m, kernel, mode="valid"),
                               -1, xp)


class TFExtractor(BaseEstimator, TransformerMixin):
    """
    ERD/ERS features via robust filter-Hilbert.

    Parameters
    ----------
    channel_set : str
        "all60" | "sensorimotor" | "central_fc" | "custom"
    channels : list[str] or None
        Explicit channels when channel_set == "custom".
    bands : list[str] or None
        Subset of BANDS to use, e.g. ["delta", "gamma"]. None = all five.
    early_win, late_win : tuple(float, float)
        Windows (s) for the early / late mean-dB ERD features.
    include_peaks : bool
        Add peak-ERD (min dB) and peak-ERS (max dB) over the post window.
    include_latency : bool
        Also add the latency (s) of the ERD and ERS peaks.
    reference : str
        "baseline" (default) uses the pre-stim window as the dB reference.
        "epoch_mean" uses each trial's whole-epoch mean power instead -- a
        fallback for data with no pre-stim samples.
    smooth_ms : float
        Envelope smoothing (ms) applied before peak detection.
    filter_order : int
        Butterworth order for the band-pass.
    """

    def __init__(self, channel_set="all60", channels=None, bands=None,
                 early_win=EARLY_WIN, late_win=LATE_WIN,
                 include_peaks=True, include_latency=False,
                 reference="baseline", smooth_ms=SMOOTH_MS,
                 filter_order=FILTER_ORDER):
        self.channel_set = channel_set
        self.channels = channels
        self.bands = bands
        self.early_win = early_win
        self.late_win = late_win
        self.include_peaks = include_peaks
        self.include_latency = include_latency
        self.reference = reference
        self.smooth_ms = smooth_ms
        self.filter_order = filter_order
        self._meta = None

    # ---- meta ----
    def set_meta(self, meta):
        self._meta = meta
        return self

    def _get_meta(self, meta):
        m = meta if meta is not None else self._meta
        if m is None:
            raise ValueError("meta must be provided (channel_names, sfreq, times).")
        return m

    # ---- channel / band resolution ----
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
        if not idx:
            raise ValueError(f"None of the requested channels found for set "
                             f"'{self.channel_set}'.")
        return idx, [ch_names[i] for i in idx]

    def _resolve_bands(self):
        if self.bands is None:
            return dict(BANDS)
        bad = [b for b in self.bands if b not in BANDS]
        if bad:
            raise ValueError(f"Unknown band(s) {bad}. Options: {list(BANDS)}")
        return {b: BANDS[b] for b in self.bands}

    # ---- fit ----
    def fit(self, X, y=None, meta=None):
        m = self._get_meta(meta)
        ch_names = list(m["channel_names"])
        self.ch_indices_, self.ch_used_ = self._resolve_channels(ch_names)
        self.sfreq_ = float(m["sfreq"])
        self.times_ = np.asarray(m["times"])
        self.bands_ = self._resolve_bands()

        self.has_baseline_ = self.times_[0] <= BASELINE_WIN[0] + 1e-9
        self.reference_ = self.reference
        if self.reference == "baseline" and not self.has_baseline_:
            warnings.warn("No pre-stim baseline in epoch; ERD/ERS reference "
                          "falls back to 'epoch_mean'.")
            self.reference_ = "epoch_mean"

        # summaries, in the exact order transform() appends them
        summaries = ["erd_early", "erd_late"]
        if self.include_peaks:
            summaries += ["erd_peak", "ers_peak"]
            if self.include_latency:
                summaries += ["erd_lat", "ers_lat"]
        self.summaries_ = summaries

        self.feature_names_ = [f"{band}_{summ}@{ch}"
                               for band in self.bands_
                               for summ in summaries
                               for ch in self.ch_used_]
        # precompute SOS per band
        self.sos_ = {b: _design_sos(lo, hi, self.sfreq_, self.filter_order)
                     for b, (lo, hi) in self.bands_.items()}
        return self

    # ---- helpers ----
    def _win_mask(self, lo, hi):
        return (self.times_ >= lo) & (self.times_ <= hi)

    def _db_timecourse(self, power):
        """power:(trials,ch,time) -> dB relative to the chosen reference."""
        if self.reference_ == "baseline":
            ref = power[:, :, self._win_mask(*BASELINE_WIN)].mean(axis=2, keepdims=True)
        else:  # epoch_mean
            ref = power.mean(axis=2, keepdims=True)
        return 10.0 * np.log10((power + PWR_EPS) / (ref + PWR_EPS))

    # ---- transform ----
    def transform(self, X, meta=None):
        if not hasattr(self, "ch_indices_"):
            raise RuntimeError("Call fit before transform.")
        X = np.asarray(X, dtype=float)
        sub = X[:, self.ch_indices_, :]                  # (trials, ch, time)

        early_m = self._win_mask(*self.early_win)
        late_m = self._win_mask(*self.late_win)
        post_m = self._win_mask(*POST_WIN)
        post_t = self.times_[post_m]
        ksmooth = int(round(self.smooth_ms / 1000.0 * self.sfreq_))

        feats = []
        for band, sos in self.sos_.items():
            filt = sosfiltfilt(sos, sub, axis=-1)
            power = np.abs(hilbert(filt, axis=-1)) ** 2  # (trials, ch, time)
            db = self._db_timecourse(power)

            feats.append(db[:, :, early_m].mean(axis=2))      # erd_early
            feats.append(db[:, :, late_m].mean(axis=2))       # erd_late

            if self.include_peaks:
                db_post = db[:, :, post_m]
                db_post_s = _moving_average(db_post, ksmooth) if ksmooth > 1 else db_post
                erd_idx = np.argmin(db_post_s, axis=2)        # most negative (desync)
                ers_idx = np.argmax(db_post_s, axis=2)        # most positive (sync)
                erd_peak = np.take_along_axis(db_post_s, erd_idx[:, :, None], axis=2)[:, :, 0]
                ers_peak = np.take_along_axis(db_post_s, ers_idx[:, :, None], axis=2)[:, :, 0]
                feats.append(erd_peak)                        # erd_peak
                feats.append(ers_peak)                        # ers_peak
                if self.include_latency:
                    feats.append(post_t[erd_idx])             # erd_lat
                    feats.append(post_t[ers_idx])             # ers_lat

        return np.concatenate(feats, axis=1)


# Clear alias; the registry imports TFExtractor, this name is for readability.
ERDERSExtractor = TFExtractor