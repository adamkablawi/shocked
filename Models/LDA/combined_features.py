"""
combined_features.py
====================
Combined feature extractor: concatenates ERP (evoked, time-domain) features and
band-power (induced, spectral) features into one vector, then hands them to the
same shrinkage-LDA pipeline.

Rationale: the evoked response (ERP peak amplitude / latency) and the induced
response (log band power) are distinct neural phenomena, so their features carry
non-redundant information. This extractor lets you test whether combining beats
either alone, under the SAME validation as the standalone runs.

Works on both 3-class (no pre-stim baseline) and 4-class (with baseline) data:
the ERP sub-extractor auto-detects whether a baseline window exists and adapts.

sklearn-compatible (fit / transform / set_meta), leakage-safe (no label use).

Example
-------
    from combined_features import CombinedExtractor
    from erp_features import load_npz_for_features
    X, y, meta = load_npz_for_features("EMS0001.npz")
    fx = CombinedExtractor(erp_set="recommended", bp_channel_set="all60").set_meta(meta)
    F = fx.fit_transform(X)            # (n_trials, n_erp + n_bp)
    names = fx.feature_names_
"""

from __future__ import annotations
import numpy as np

try:
    from sklearn.base import BaseEstimator, TransformerMixin
except Exception:
    class BaseEstimator:
        def get_params(self, deep=True): return {}
        def set_params(self, **p): return self
    class TransformerMixin:
        def fit_transform(self, X, y=None, **kw):
            return self.fit(X, y, **kw).transform(X, **kw)

from erp_features import ERPFeatureExtractor
from bandpower_features import BandPowerExtractor


class CombinedExtractor(BaseEstimator, TransformerMixin):
    """
    Concatenate ERP and band-power features.

    Parameters
    ----------
    erp_set : str
        feature_set passed to ERPFeatureExtractor ("recommended", "peak",
        "peak_window", "full").
    bp_channel_set : str
        channel_set passed to BandPowerExtractor ("all60", "sensorimotor",
        "central_fc").
    bp_relative : bool
        relative band power (normalize by total power per channel/trial).
    use_erp, use_bp : bool
        Toggle either half off to recover a standalone extractor through the
        same interface (handy for ablations / sanity checks).

    Notes
    -----
    `meta` must be supplied via set_meta() (or fit(..., meta=...)). The two
    sub-extractors are fit on the same meta. feature_names_ are prefixed
    ("erp:" / "bp:") so the combined vector stays interpretable.
    """

    def __init__(self, erp_set="recommended", bp_channel_set="all60",
                 bp_relative=False, use_erp=True, use_bp=True):
        self.erp_set = erp_set
        self.bp_channel_set = bp_channel_set
        self.bp_relative = bp_relative
        self.use_erp = use_erp
        self.use_bp = use_bp
        self._meta = None

    def set_meta(self, meta):
        self._meta = meta
        return self

    def _get_meta(self, meta):
        m = meta if meta is not None else self._meta
        if m is None:
            raise ValueError("meta must be provided (channel_names, sfreq, times).")
        return m

    def fit(self, X, y=None, meta=None):
        m = self._get_meta(meta)
        if not (self.use_erp or self.use_bp):
            raise ValueError("At least one of use_erp / use_bp must be True.")
        self.erp_ = None
        self.bp_ = None
        names = []
        if self.use_erp:
            self.erp_ = ERPFeatureExtractor(feature_set=self.erp_set).set_meta(m)
            self.erp_.fit(X, y)
            names += [f"erp:{n}" for n in self.erp_.feature_names_]
        if self.use_bp:
            self.bp_ = BandPowerExtractor(channel_set=self.bp_channel_set,
                                          relative=self.bp_relative).set_meta(m)
            self.bp_.fit(X, y)
            names += [f"bp:{n}" for n in self.bp_.feature_names_]
        self.feature_names_ = names
        # expose which half contributed how many features (for reporting)
        self.n_erp_ = len(self.erp_.feature_names_) if self.erp_ else 0
        self.n_bp_  = len(self.bp_.feature_names_) if self.bp_ else 0
        return self

    def transform(self, X, meta=None):
        if not hasattr(self, "feature_names_"):
            raise RuntimeError("Call fit before transform.")
        parts = []
        if self.erp_ is not None:
            parts.append(self.erp_.transform(X))
        if self.bp_ is not None:
            parts.append(self.bp_.transform(X))
        return np.concatenate(parts, axis=1)
