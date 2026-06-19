"""
run_bandpower.py
================
Entry point for the band-power -> shrinkage-LDA decoder. Edit CONFIG and run:

    python run_bandpower.py

Runs the chosen validation across one or more channel sets and prints a summary
table. Auto-detects class count (3 or 4) from the data.
"""

import json
import numpy as np
from train_bandpower import (load_dataset, compare_channel_sets, summary_table)

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
CONFIG = {
    "data_folder":     "data/og-dwnsm-trimmed-3c",        # folder of .npz subjects
    "channel_sets":    ["all60", "sensorimotor", "central_fc"],
    "modes":           ["within", "loso"],  # subset of these two
    "relative":        False,               # relative (normalized) band power
    "n_splits":        5,
    "n_repeats":       5,
    "artifact_filter": True,
    "save_report":     "bandpower_results.json",
}


def main(cfg=CONFIG):
    print(f"Loading subjects from: {cfg['data_folder']}")
    subjects = load_dataset(cfg["data_folder"], artifact_filter=cfg["artifact_filter"])
    n_cls = len(np.unique(subjects[0]["y"]))
    print(f"Loaded {len(subjects)} subjects | {n_cls} classes "
          f"| chance = {100.0/n_cls:.0f}%\n")

    results = compare_channel_sets(
        subjects,
        channel_sets=tuple(cfg["channel_sets"]),
        modes=tuple(cfg["modes"]),
        relative=cfg["relative"],
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
