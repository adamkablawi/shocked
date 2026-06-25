"""
run_combined.py
===============
Entry point for the modular feature -> shrinkage-LDA decoder. Pick ANY set of
feature families per run and compare them under identical leakage-safe
validation (within-subject repeated k-fold + LOSO). Edit CONFIG and run:

    python run_combined.py

Feature families available: see train_combined.FEATURE_REGISTRY
("erp", "bp", and "tf" if tf_features.py is present). Add more by registering
an extractor there.
"""

import json
import numpy as np
from train_combined import (load_dataset, compare_feature_modes, summary_table,
                            FEATURE_REGISTRY)

BEST_CHANNELS = ["FCz", "C4", "Fz", "FC4", "Cz", "C2", "FC2"]  # the best 7
XON_CHANNELS = ["F3", "F4", "C3", "Cz", "C4", "P3", "P4"]

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
CONFIG = {
    "feature_sets": {
        "combined":   ["erp", "bp"],
    },
    
    "feature_opts": {
        "erp": {"feature_set": "full"},
        "bp":  {"channel_set": "all60"},
    },
    
    "data_folder": "data/og-ds-t-3c",

    "validation":      ["within", "loso"],
    "n_splits":        5,
    "n_repeats":       5,
    "per_subject_norm": True,
    "artifact_filter": True,
    "save_report":     "Results/LDA_3c/best.json",
}


def main(cfg=CONFIG):
    print(f"Loading subjects from: {cfg['data_folder']}")
    subjects = load_dataset(cfg["data_folder"], artifact_filter=cfg["artifact_filter"])
    n_cls = len(np.unique(subjects[0]["y"]))
    print(f"Loaded {len(subjects)} subjects | {n_cls} classes | chance {100.0/n_cls:.0f}%")
    print(f"Registered families: {list(FEATURE_REGISTRY)}\n")

    results = compare_feature_modes(
        subjects,
        feature_sets=cfg["feature_sets"],
        feature_opts=cfg["feature_opts"],
        validation=tuple(cfg["validation"]),
        n_splits=cfg["n_splits"],
        n_repeats=cfg["n_repeats"],
        per_subject_norm=cfg["per_subject_norm"],
    )

    print("\n" + "=" * 50 + "\nSUMMARY (pooled accuracy)\n" + "=" * 50)
    print(summary_table(results))

    if cfg["save_report"]:
        import os
        os.makedirs(os.path.dirname(cfg["save_report"]) or ".", exist_ok=True)
        with open(cfg["save_report"], "w") as f:
            json.dump(results, f, indent=2)
        print(f"\nSaved -> {cfg['save_report']}")
    return results


if __name__ == "__main__":
    main()