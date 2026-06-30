"""
riemann_features.py
===================
Riemannian (covariance / tangent-space) feature extraction, drop-in compatible
with the same Pipeline / cross-validation machinery as erp_features.py and
bandpower_features.py.

Each trial is summarised by its channel x channel covariance matrix (the spatial
co-activation / coupling structure of the response). Covariance matrices live on
a curved manifold of symmetric positive-definite (SPD) matrices, so they are
projected into the tangent space at the data's geometric mean -- a flat vector
that a linear model (shrinkage-LDA) can use correctly while preserving the
manifold geometry.

Interpretability: each tangent feature maps to an electrode PAIR (i, j). The
diagonal terms are per-channel (log) power; the off-diagonal terms are pairwise
coupling -- the information the per-channel erp/bp families discard. Feature
names are "<chi>*<chj>" so the existing importance tooling can rank pairs.

Statefulness: unlike the erp/bp extractors, the tangent reference is LEARNED in
fit (the geometric mean of the training covariances). It is unsupervised (no
labels) and is refit per CV fold by the surrounding Pipeline, so it is
leakage-safe exactly like the StandardScaler step.

Features per trial: n_ch * (n_ch + 1) / 2   (upper triangle incl. diagonal).
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

from pyriemann.estimation import Covariances
from pyriemann.tangentspace import TangentSpace

# ─────────────────────────────────────────────
# CONFIG  (channel sets mirror bandpower_features.py)
# ─────────────────────────────────────────────
SENSORIMOTOR = ["C3", "C4", "Cz", "C1", "C2", "FC1", "FC2", "FC3", "FC4",
                "CP1", "CP2", "CP3", "CP4", "P3", "P4", "Pz"]
CENTRAL_FC   = ["C3", "Cz", "C4", "FCz", "FC1", "FC2", "FC3", "FC4"]

# Analysis window (s) over which the covariance is computed. None = full epoch.
COV_WIN = None     # e.g. (0.0, 1.5) to use post-stim only, or None for whole epoch


class RiemannTangentExtractor(BaseEstimator, TransformerMixin):
    """
    Covariance -> tangent-space features.

    Parameters
    ----------
    channel_set : str
        "all60" | "sensorimotor" | "central_fc" | "custom"
    channels : list[str] or None
        Explicit channel list when channel_set == "custom".
    estimator : str
        Covariance estimator passed to pyriemann.Covariances
        ("oas" = Oracle Approximating Shrinkage, well-conditioned; "scm" = raw).
    metric : str
        Tangent-space metric ("riemann" recommended).
    """

    def __init__(self, channel_set="all60", channels=None,
                 estimator="oas", metric="riemann"):
        self.channel_set = channel_set
        self.channels = channels
        self.estimator = estimator
        self.metric = metric
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
        if not idx:
            raise ValueError(f"None of the requested channels found for set "
                             f"'{self.channel_set}'.")
        return idx, [ch_names[i] for i in idx]

    def _slice(self, X):
        X = np.asarray(X, dtype=float)
        sub = X[:, self.ch_indices_, :]
        if COV_WIN is not None:
            t = self.times_
            wmask = (t >= COV_WIN[0]) & (t <= COV_WIN[1])
            sub = sub[:, :, wmask]
        return sub

    def fit(self, X, y=None, meta=None):
        m = self._get_meta(meta)
        ch_names = list(m["channel_names"])
        self.ch_indices_, self.ch_used_ = self._resolve_channels(ch_names)
        self.times_ = np.asarray(m["times"])

        self.cov_ = Covariances(estimator=self.estimator)
        self.ts_ = TangentSpace(metric=self.metric)
        covs = self.cov_.fit_transform(self._slice(X))
        self.ts_.fit(covs)

        # Feature names: upper triangle (incl. diagonal), row-major, matching
        # pyriemann's tangent-space vectorisation order.
        names = []
        n = len(self.ch_used_)
        for i in range(n):
            for j in range(i, n):
                ci, cj = self.ch_used_[i], self.ch_used_[j]
                names.append(f"{ci}*{ci}" if i == j else f"{ci}*{cj}")
        self.feature_names_ = names
        return self

    def transform(self, X, meta=None):
        if not hasattr(self, "ts_"):
            raise RuntimeError("Call fit before transform.")
        covs = self.cov_.transform(self._slice(X))
        return self.ts_.transform(covs)
