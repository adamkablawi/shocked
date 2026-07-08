"""
conn_features.py
================
Phase-based FUNCTIONAL CONNECTIVITY feature family (`conn`) — the per-trial,
deployable form of the findings in ConnectivityAnalysis/. Designed as a
neuroscience-grounded, interpretable replacement for the Riemannian covariance
family (`riem`).

The ConnectivityAnalysis showed that EMS intensity modulates phase-locked
coupling between three regions:
    FC (fronto-central) : FC5 FC1 FC6 FC2 FC3 FC4 FCz
    C  (central)        : C3 Cz C4 C1 C5 C6 C2
    P  (parietal)       : Pz P1..P8
— low-frequency (delta/theta/alpha) inter-region coupling rises with intensity,
gamma coupling falls. This extractor turns that into a SINGLE-TRIAL feature.

Per trial, for each frequency band and each region pair, it computes:
  * PLV  — single-trial phase-locking over the post-stim window:
           |<exp(i·Δφ(t))>_t|  averaged over the channel pairs of the region pair.
  * iPLV — |Im<exp(i·Δφ(t))>_t|  (volume-conduction robust; the measure that was
           most strongly significant in the group analysis).

Region pairs: FC-C, FC-P, C-P (between) + FC-FC, C-C, P-P (within) = 6.
Bands: delta(1-4) theta(4-8) alpha(8-13) beta(13-30) gamma(30-45) Hz.
Features = 6 pairs × 5 bands × 2 measures = 60, each named
  `plv_<band>_<A>-<B>` / `iplv_<band>_<A>-<B>` (interpretable).

sklearn-compatible (set_meta / fit / transform / feature_names_), uses no labels.
"""
from __future__ import annotations
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

REGIONS = {
    "FC": ["FC5", "FC1", "FC6", "FC2", "FC3", "FC4", "FCz"],
    "C":  ["C3", "Cz", "C4", "C1", "C5", "C6", "C2"],
    "P":  ["Pz", "P3", "P7", "P4", "P8", "P1", "P5", "P6", "P2"],
}
PAIRS = [("FC", "C"), ("FC", "P"), ("C", "P"), ("FC", "FC"), ("C", "C"), ("P", "P")]
BANDS = {"delta": (1, 4), "theta": (4, 8), "alpha": (8, 13),
         "beta": (13, 30), "gamma": (30, 45)}
POST_WIN = (0.0, 1.0)     # single-trial window (wider than the group 0-0.5 s so
                          # low-frequency bands see enough cycles per trial)


class ConnFeatureExtractor(BaseEstimator, TransformerMixin):
    """
    Per-trial region-to-region phase connectivity features.

    Parameters
    ----------
    regions : dict[str, list[str]]   region -> channel names (default FC/C/P)
    pairs   : list[(str,str)]        region pairs (default 6: 3 between + 3 within)
    bands   : dict[str, (lo,hi)]     bands (default delta..gamma)
    window  : (float, float)         post-stim window in seconds
    measures: list[str]              subset of ["plv", "iplv"]
    """

    def __init__(self, regions=None, pairs=None, bands=None, window=POST_WIN,
                 measures=("plv", "iplv"), filter_order=4):
        self.regions = regions or REGIONS
        self.pairs = pairs or PAIRS
        self.bands = bands or BANDS
        self.window = window
        self.measures = list(measures)
        self.filter_order = filter_order
        self._meta = None

    def set_meta(self, meta):
        self._meta = meta
        return self

    def _get_meta(self, meta):
        m = meta if meta is not None else self._meta
        if m is None:
            raise ValueError("meta must be provided (channel_names, sfreq, times).")
        return m

    def _sos(self, lo, hi):
        ny = self.sfreq_ / 2.0
        return butter(self.filter_order, [max(lo, 0.5) / ny, min(hi, ny - 1e-6) / ny],
                      btype="band", output="sos")

    def fit(self, X, y=None, meta=None):
        m = self._get_meta(meta)
        ch = list(m["channel_names"])
        self.sfreq_ = float(m["sfreq"])
        self.times_ = np.asarray(m["times"])
        # resolve region -> channel indices (only channels present)
        self.ridx_ = {r: [ch.index(c) for c in chs if c in ch] for r, chs in self.regions.items()}
        missing = [r for r, idx in self.ridx_.items() if len(idx) == 0]
        if missing:
            raise ValueError(f"No channels found for regions {missing}")
        self.wmask_ = (self.times_ >= self.window[0]) & (self.times_ <= self.window[1])
        self.sos_ = {b: self._sos(lo, hi) for b, (lo, hi) in self.bands.items()}
        self.feature_names_ = [f"{meas}_{band}_{a}-{b}"
                               for band in self.bands
                               for (a, b) in self.pairs
                               for meas in self.measures]
        return self

    def transform(self, X, meta=None):
        if not hasattr(self, "ridx_"):
            raise RuntimeError("Call fit before transform.")
        X = np.asarray(X, dtype=float)
        n = X.shape[0]
        cols = []
        for band in self.bands:
            filt = sosfiltfilt(self.sos_[band], X, axis=2)
            phase = np.angle(hilbert(filt, axis=2))
            cp = np.exp(1j * phase)[:, :, self.wmask_]          # (n, 60, Tw)
            for (a, b) in self.pairs:
                ai, bi = self.ridx_[a], self.ridx_[b]
                cpa = cp[:, ai, :]                              # (n, |A|, Tw)
                cpb = cp[:, bi, :]                              # (n, |B|, Tw)
                # single-trial mean phasor product over time -> (n, |A|, |B|)
                m = np.einsum("nat,nbt->nab", cpa, np.conj(cpb)) / cp.shape[2]
                plv = np.abs(m); iplv = np.abs(m.imag)
                if a == b:                                     # within: drop self pairs
                    keep = ~np.eye(len(ai), dtype=bool)
                    plv_v = plv[:, keep].mean(1); iplv_v = iplv[:, keep].mean(1)
                else:
                    plv_v = plv.reshape(n, -1).mean(1); iplv_v = iplv.reshape(n, -1).mean(1)
                for meas in self.measures:
                    cols.append(plv_v if meas == "plv" else iplv_v)
        return np.stack(cols, axis=1)
