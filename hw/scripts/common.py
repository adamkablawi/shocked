"""
common.py
=========
Shared paths + data access for the FPGA flow. Imports the FourConnModel training
code directly so feature extraction / model fitting are the exact same code the
deployed model was trained with.

Raw (un-normalised) features are cached once to hw/cache/features_raw.npz, since
extraction of all 29 subjects is the slow step and every other script needs it.
"""
from __future__ import annotations
import os, sys, glob
import numpy as np

HW_DIR    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_DIR  = os.path.dirname(HW_DIR)
MODEL_DIR = os.path.join(REPO_DIR, "FinalModels", "FourConnModel")
MODEL_PATH = os.path.join(MODEL_DIR, "conn_stacking_ensemble.joblib")
DATA_DIR  = os.path.join(REPO_DIR, "data", "og-ds-t-3c")
CACHE_DIR = os.path.join(HW_DIR, "cache")
MEM_DIR   = os.path.join(HW_DIR, "rtl", "mem")
RESULTS_DIR = os.path.join(HW_DIR, "results")
FEATURE_CACHE = os.path.join(CACHE_DIR, "features_raw.npz")

if MODEL_DIR not in sys.path:
    sys.path.insert(0, MODEL_DIR)
import train_conn_model as tcm          # noqa: E402  (FourConnModel trainer)

FAMILIES = ["erp", "bp", "tf", "conn"]


def load_model():
    import joblib
    art = joblib.load(MODEL_PATH)
    assert list(art["families"]) == FAMILIES, art["families"]
    return art


def load_features(n_jobs=-1, rebuild=False):
    """Raw per-family feature matrices for every trial of every subject.

    Returns dict with keys: mats {fam: (n, d)}, X (n, 1664) in stream order,
    y (n,), groups (n,), sids [str], class_names [str].
    """
    if rebuild or not os.path.exists(FEATURE_CACHE):
        os.makedirs(CACHE_DIR, exist_ok=True)
        files = sorted(glob.glob(os.path.join(DATA_DIR, "*.npz")))
        cfg = tcm.CONFIG
        mats, y, groups, sids, class_names = tcm.extract_parallel(
            files, FAMILIES, cfg["feature_opts"], cfg["artifact_filter"], n_jobs)
        np.savez_compressed(FEATURE_CACHE, y=y, groups=groups,
                            sids=np.array(sids), class_names=np.array(class_names),
                            **{f"F_{f}": mats[f] for f in FAMILIES})
    d = np.load(FEATURE_CACHE, allow_pickle=False)
    mats = {f: d[f"F_{f}"] for f in FAMILIES}
    return {"mats": mats,
            "X": np.hstack([mats[f] for f in FAMILIES]),
            "y": d["y"], "groups": d["groups"],
            "sids": [str(s) for s in d["sids"]],
            "class_names": [str(c) for c in d["class_names"]]}


def subject_stats(X, groups):
    """Per-subject feature mean / SD -- exactly what per_subject_zscore uses.
    Returns mu, sd of shape (n_subjects, d), indexed by group id."""
    gs = np.unique(groups)
    mu = np.stack([X[groups == g].mean(0) for g in gs])
    sd = np.stack([X[groups == g].std(0) for g in gs])
    return mu, sd


def zscore(X, groups):
    """Identical arithmetic to tcm.per_subject_zscore, on the stacked matrix."""
    Z = X.copy()
    for g in np.unique(groups):
        gm = groups == g
        Z[gm] = (X[gm] - X[gm].mean(0)) / (X[gm].std(0) + 1e-12)
    return Z
