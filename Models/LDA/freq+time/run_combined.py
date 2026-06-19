"""
run_combined.py
===============
Entry point for the combined (ERP + band-power) -> shrinkage-LDA decoder.
Compares erp_only vs bp_only vs combined under identical validation, so you can
see whether combining actually beats either alone. Edit CONFIG and run:

    python run_combined.py

Auto-detects class count (3 or 4). Works on data with or without a pre-stim
baseline (the ERP half adapts).
"""

import json
import numpy as np
from train_combined import load_dataset, compare_feature_modes, summary_table

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
CONFIG = {
    "data_folder":     "data/og-dw-t-3c",   # folder of .npz subjects
    "modes":           ["erp_only", "bp_only", "combined"],
    "validation":      ["within", "loso"],        # subset of these two
    "erp_set":         "recommended",             # recommended | peak | peak_window | full
    "bp_channel_set":  "all60",                   # all60 | sensorimotor | central_fc
    "bp_relative":     False,
    "n_splits":        5,
    "n_repeats":       5,
    "artifact_filter": True,
    "save_report":     "Results/LDA_td+fd_3c.json",
}


def main(cfg=CONFIG):
    print(f"Loading subjects from: {cfg['data_folder']}")
    subjects = load_dataset(cfg["data_folder"], artifact_filter=cfg["artifact_filter"])
    n_cls = len(np.unique(subjects[0]["y"]))
    print(f"Loaded {len(subjects)} subjects | {n_cls} classes | chance = {100.0/n_cls:.0f}%")
    print(f"ERP set: {cfg['erp_set']} | band-power channels: {cfg['bp_channel_set']}\n")

    results = compare_feature_modes(
        subjects,
        modes=tuple(cfg["modes"]),
        validation=tuple(cfg["validation"]),
        erp_set=cfg["erp_set"],
        bp_channel_set=cfg["bp_channel_set"],
        bp_relative=cfg["bp_relative"],
        n_splits=cfg["n_splits"],
        n_repeats=cfg["n_repeats"],
    )

    print("\n" + "=" * 50)
    print("SUMMARY (pooled accuracy)")
    print("=" * 50)
    print(summary_table(results))

    if cfg["save_report"]:
        with open(cfg["save_report"], "w") as f:
            json.dump(results, f, indent=2)
        print(f"\nSaved results -> {cfg['save_report']}")
    return results


if __name__ == "__main__":
    main()
