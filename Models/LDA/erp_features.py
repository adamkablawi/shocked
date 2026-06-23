"""
erp_features.py
===============
Production-grade ERP / SEP feature extraction for the central / fronto-central
channels, implementing the ERP Feature Extraction Spec.

The extractor is sklearn-compatible (fit / transform) so it can live inside a
Pipeline and be cross-validated without leakage. It is deliberately defensive:
it adapts to the available time window (baseline present or not), validates its
inputs, and exposes named features for interpretability.

Feature families (per channel, per trial):
    peak       : neg/pos peak amplitude + latency, peak-to-peak        (5/ch)
    window     : mean amplitude in fixed post-stim bins                (3/ch)
    baseline   : pre-stim mean, pre-stim SD, post-minus-baseline shift (3/ch)
    shape      : rectified AUC, rising-edge slope                      (2/ch)

Use FEATURE_SETS to pick which families to include. The default "recommended"
set matches section 7 of the spec.

Example
-------
    from erp_features import ERPFeatureExtractor, load_npz_for_features
    X, y, meta = load_npz_for_features("EMS0001.npz")
    fx = ERPFeatureExtractor(feature_set="recommended")
    F = fx.fit_transform(X, meta=meta)        # (n_trials, n_features)
    names = fx.feature_names_
"""

from __future__ import annotations
import numpy as np
from pathlib import Path

try:
    from sklearn.base import BaseEstimator, TransformerMixin
except Exception:  # sklearn optional for pure extraction use
    class BaseEstimator:  # minimal shims
        def get_params(self, deep=True): return {}
        def set_params(self, **p): return self
    class TransformerMixin:
        def fit_transform(self, X, y=None, **kw):
            return self.fit(X, y, **kw).transform(X, **kw)


# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
DEFAULT_CHANNELS = ["C3", "Cz", "C4", "FCz", "FC1", "FC2", "FC3", "FC4"]

# Time windows (seconds). All relative to stimulus onset (t = 0).
NEG_PEAK_WIN  = (0.10, 0.20)   # search window for the negative peak
POS_PEAK_WIN  = (0.20, 0.30)   # search window for the positive peak
MEAN_WINS     = [(0.10, 0.18), (0.20, 0.28), (0.28, 0.40)]
BASELINE_WIN  = (-0.20, 0.0)   # used if pre-stim samples exist
ANALYSIS_WIN  = (0.0, 0.40)    # for AUC / shape features

# Which feature families each named set includes.
FEATURE_SETS = {
    "recommended": ["peak_to_peak", "neg_latency", "mean_010_018", "mean_020_028"],
    "peak":        ["peak"],
    "peak_window": ["peak", "window"],
    "full":        ["peak", "window", "baseline", "shape"],
}


# ─────────────────────────────────────────────
# LOADING (feature-oriented; keeps per-subject grouping intact)
# ─────────────────────────────────────────────
def load_npz_for_features(path):
    """
    Load ONE .npz subject for feature extraction.

    Returns
    -------
    X    : (n_trials, n_channels, n_times)  microvolts
    y    : (n_trials,)
    meta : dict (sfreq, channel_names, class_names, subject_id, tmin, tmax, times)
    """
    d = np.load(path, allow_pickle=True)
    X = np.asarray(d["X"], dtype=float)
    y = np.asarray(d["y"]).astype(int)
    if X.std() < 1e-3:                      # volts -> microvolts
        X = X * 1e6
    tmin = float(d["epoch_tmin"]) if "epoch_tmin" in d else 0.0
    tmax = float(d["epoch_tmax"]) if "epoch_tmax" in d else (X.shape[2] - 1)
    meta = {
        "sfreq":         float(d["sfreq"]) if "sfreq" in d else 250.0,
        "channel_names": [str(c) for c in d["channel_names"]],
        "class_names":   [str(c) for c in d["class_names"]] if "class_names" in d else None,
        "subject_id":    str(d["subject_id"]) if "subject_id" in d else Path(path).stem,
        "tmin":          tmin,
        "tmax":          tmax,
        "times":         np.linspace(tmin, tmax, X.shape[2]),
    }
    return X, y, meta


# ─────────────────────────────────────────────
# EXTRACTOR
# ─────────────────────────────────────────────
class ERPFeatureExtractor(BaseEstimator, TransformerMixin):
    """
    Extract ERP/SEP features from epoched EEG.

    Parameters
    ----------
    feature_set : str
        Key into FEATURE_SETS, or "custom" (then pass `families`).
    families : list[str] or None
        Explicit family list when feature_set == "custom". Each entry is either
        a family name ("peak", "window", "baseline", "shape") or an individual
        feature token ("peak_to_peak", "neg_latency", "mean_010_018", ...).
    channels : list[str]
        Channel names to extract from. Missing channels raise at fit time.
    baseline_correct : bool
        Subtract per-trial pre-stim baseline before extraction (if baseline
        samples are available in the epoch window).

    Notes
    -----
    `meta` (with channel_names, sfreq, times) must be supplied to fit/transform,
    either as a keyword or set once via `set_meta`. This keeps the transformer
    stateless w.r.t. the data array while still sklearn-compatible.
    """

    def __init__(self, feature_set="recommended", families=None,
                 channels=None, baseline_correct=True):
        self.feature_set = feature_set
        self.families = families
        self.channels = channels or DEFAULT_CHANNELS
        self.baseline_correct = baseline_correct
        self._meta = None

    # ---- meta handling ----
    def set_meta(self, meta):
        self._meta = meta
        return self

    def _get_meta(self, meta):
        m = meta if meta is not None else self._meta
        if m is None:
            raise ValueError("meta must be provided to fit/transform (channel_names, sfreq, times).")
        return m

    # ---- resolve which tokens to compute ----
    def _resolve_tokens(self):
        if self.feature_set == "custom":
            req = list(self.families or [])
        else:
            if self.feature_set not in FEATURE_SETS:
                raise ValueError(f"Unknown feature_set '{self.feature_set}'. "
                                 f"Options: {list(FEATURE_SETS)} or 'custom'.")
            req = list(FEATURE_SETS[self.feature_set])
        # Expand family names into their tokens
        expanded = []
        for r in req:
            if r == "peak":
                expanded += ["neg_amp", "neg_latency", "pos_amp", "pos_latency", "peak_to_peak"]
            elif r == "window":
                expanded += ["mean_010_018", "mean_020_028", "mean_028_040"]
            elif r == "baseline":
                expanded += ["base_mean", "base_sd", "post_minus_base"]
            elif r == "shape":
                expanded += ["auc_rect", "rise_slope"]
            else:
                expanded.append(r)
        # de-dup, keep order
        seen, out = set(), []
        for t in expanded:
            if t not in seen:
                seen.add(t); out.append(t)
        return out

    # ---- fit just validates + records channel indices and feature names ----
    def fit(self, X, y=None, meta=None):
        m = self._get_meta(meta)
        ch_names = list(m["channel_names"])
        missing = [c for c in self.channels if c not in ch_names]
        if missing:
            raise ValueError(f"Channels not found in data: {missing}")
        self.ch_indices_ = [ch_names.index(c) for c in self.channels]
        self.tokens_ = self._resolve_tokens()
        self.times_ = np.asarray(m["times"])
        self.has_baseline_ = self.times_[0] <= BASELINE_WIN[0] + 1e-9
        # Build feature names: token x channel
        self.feature_names_ = [f"{tok}@{ch}"
                               for tok in self.tokens_
                               for ch in self.channels]
        return self

    # ---- helpers ----
    def _win_mask(self, lo, hi):
        return (self.times_ >= lo) & (self.times_ <= hi)

    def _baseline_correct(self, sub):
        """sub: (n_trials, n_ch, n_times) -> baseline-subtracted copy."""
        if not (self.baseline_correct and self.has_baseline_):
            return sub
        bmask = self._win_mask(*BASELINE_WIN)
        if bmask.sum() == 0:
            return sub
        base = sub[:, :, bmask].mean(axis=2, keepdims=True)
        return sub - base

    # ---- transform ----
    def transform(self, X, meta=None):
        if not hasattr(self, "ch_indices_"):
            raise RuntimeError("Call fit before transform.")
        X = np.asarray(X, dtype=float)
        sub = X[:, self.ch_indices_, :]                 # (trials, ch, times)
        sub = self._baseline_correct(sub)
        n_trials, n_ch, _ = sub.shape
        t = self.times_

        # Precompute window masks
        neg_mask = self._win_mask(*NEG_PEAK_WIN)
        pos_mask = self._win_mask(*POS_PEAK_WIN)
        ana_mask = self._win_mask(*ANALYSIS_WIN)
        base_mask = self._win_mask(*BASELINE_WIN) if self.has_baseline_ else None

        # Negative peak: value + latency
        neg_seg = sub[:, :, neg_mask]                   # (trials, ch, k)
        neg_t   = t[neg_mask]
        neg_idx = np.argmin(neg_seg, axis=2)            # (trials, ch)
        neg_amp = np.take_along_axis(neg_seg, neg_idx[:, :, None], axis=2)[:, :, 0]
        neg_lat = neg_t[neg_idx]

        # Positive peak: value + latency
        pos_seg = sub[:, :, pos_mask]
        pos_t   = t[pos_mask]
        pos_idx = np.argmax(pos_seg, axis=2)
        pos_amp = np.take_along_axis(pos_seg, pos_idx[:, :, None], axis=2)[:, :, 0]
        pos_lat = pos_t[pos_idx]

        p2p = pos_amp - neg_amp

        # Mean-window features
        def mean_in(lo, hi):
            mk = self._win_mask(lo, hi)
            if mk.sum() == 0:
                return np.zeros((n_trials, n_ch))
            return sub[:, :, mk].mean(axis=2)
        mean_010_018 = mean_in(0.10, 0.18)
        mean_020_028 = mean_in(0.20, 0.28)
        mean_028_040 = mean_in(0.28, 0.40)

        # Baseline-derived
        if base_mask is not None and base_mask.sum() > 0:
            base_mean = sub[:, :, base_mask].mean(axis=2)
            base_sd   = sub[:, :, base_mask].std(axis=2)
        else:
            base_mean = np.zeros((n_trials, n_ch))
            base_sd   = np.zeros((n_trials, n_ch))
        post_mean = sub[:, :, ana_mask].mean(axis=2) if ana_mask.sum() else np.zeros((n_trials, n_ch))
        post_minus_base = post_mean - base_mean

        # Shape
        if ana_mask.sum() > 1:
            seg = sub[:, :, ana_mask]
            dt = np.median(np.diff(t[ana_mask]))
            auc_rect = np.abs(seg).sum(axis=2) * dt
            # rising-edge slope: from window start to the negative peak
            t0 = t[ana_mask][0]
            denom = (neg_lat - t0)
            denom[denom == 0] = np.nan
            rise_slope = (neg_amp - seg[:, :, 0]) / denom
            rise_slope = np.nan_to_num(rise_slope)
        else:
            auc_rect = np.zeros((n_trials, n_ch))
            rise_slope = np.zeros((n_trials, n_ch))

        token_map = {
            "neg_amp": neg_amp, "neg_latency": neg_lat,
            "pos_amp": pos_amp, "pos_latency": pos_lat,
            "peak_to_peak": p2p,
            "mean_010_018": mean_010_018, "mean_020_028": mean_020_028,
            "mean_028_040": mean_028_040,
            "base_mean": base_mean, "base_sd": base_sd,
            "post_minus_base": post_minus_base,
            "auc_rect": auc_rect, "rise_slope": rise_slope,
        }

        cols = [token_map[tok] for tok in self.tokens_]   # each (trials, ch)
        F = np.concatenate(cols, axis=1)                  # (trials, tokens*ch)
        return F


# ─────────────────────────────────────────────
# Trial-quality mask (optional artifact filter from spec section 3)
# ─────────────────────────────────────────────
def baseline_sd_outlier_mask(X, meta, channels=None, z_thresh=3.0):
    """
    Return a boolean mask of GOOD trials based on pre-stim baseline SD.
    Trials whose mean baseline SD exceeds z_thresh (per-subject z-score) are
    flagged as bad. If no baseline window exists, all trials are kept.
    """
    times = np.asarray(meta["times"])
    if times[0] > BASELINE_WIN[0] + 1e-9:
        return np.ones(X.shape[0], dtype=bool)
    ch_names = list(meta["channel_names"])
    chans = channels or DEFAULT_CHANNELS
    idx = [ch_names.index(c) for c in chans if c in ch_names]
    bmask = (times >= BASELINE_WIN[0]) & (times <= BASELINE_WIN[1])
    sd = X[:, idx, :][:, :, bmask].std(axis=2).mean(axis=1)   # per-trial
    z = (sd - sd.mean()) / (sd.std() + 1e-12)
    return z <= z_thresh
