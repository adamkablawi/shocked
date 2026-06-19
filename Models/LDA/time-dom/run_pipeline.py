"""
run_pipeline.py
===============
Entry point for the ERP -> shrinkage-LDA decoder. Edit the CONFIG block and run:

    python run_pipeline.py

It loads a folder of .npz subjects, runs the chosen validation, prints a report,
and optionally fits + saves a final deployable model.
"""

import json
import numpy as np
from train_lda import (load_dataset, run_within_subject, run_loso,
                       fit_final_model, lda_weight_report)

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
CONFIG = {
    "data_folder":     "data/og-dwnsm-trimmed-3c",        # folder of .npz subjects
    "feature_set":     "recommended",       # recommended | peak | peak_window | full
    "mode":            "both",              # within | loso | both
    "n_splits":        5,
    "n_repeats":       5,
    "artifact_filter": True,                # drop high baseline-SD trials
    "per_subject_norm": True,               # for LOSO
    "fit_final":       True,                # fit + report a deployable model
    "save_model":      None,                # path to joblib dump, or None
    "save_report":     "Results/lda_results.json",  # path to JSON results, or None
}


def main(cfg=CONFIG):
    print(f"Loading subjects from: {cfg['data_folder']}")
    subjects = load_dataset(cfg["data_folder"], artifact_filter=cfg["artifact_filter"])
    n_cls = len(np.unique(subjects[0]["y"]))
    print(f"Loaded {len(subjects)} subjects | {n_cls} classes | "
          f"feature_set={cfg['feature_set']}\n")

    results = {}

    if cfg["mode"] in ("within", "both"):
        print("=" * 60)
        print("WITHIN-SUBJECT VALIDATION")
        print("=" * 60)
        res_w = run_within_subject(
            subjects, feature_set=cfg["feature_set"],
            n_splits=cfg["n_splits"], n_repeats=cfg["n_repeats"])
        print(f"\nPOOLED within-subject: acc={res_w['acc_mean']*100:.1f}% "
              f"+/-{res_w['acc_std']*100:.1f} | balanced={res_w['bal_mean']*100:.1f}% "
              f"| chance={res_w['chance']*100:.0f}%\n")
        results["within"] = res_w

    if cfg["mode"] in ("loso", "both"):
        print("=" * 60)
        print("LEAVE-ONE-SUBJECT-OUT VALIDATION")
        print("=" * 60)
        try:
            res_l = run_loso(subjects, feature_set=cfg["feature_set"],
                             per_subject_norm=cfg["per_subject_norm"])
            print(f"\nPOOLED LOSO: acc={res_l['acc_mean']*100:.1f}% "
                  f"+/-{res_l['acc_std']*100:.1f} | balanced={res_l['bal_mean']*100:.1f}% "
                  f"| chance={res_l['chance']*100:.0f}%\n")
            results["loso"] = res_l
        except ValueError as e:
            print(f"[LOSO skipped] {e}\n")

    if cfg["fit_final"]:
        print("=" * 60)
        print("FINAL MODEL (fit on all subjects) + INTERPRETABILITY")
        print("=" * 60)
        try:
            pipe, names = fit_final_model(subjects, feature_set=cfg["feature_set"])
            print(lda_weight_report(pipe, names, top_k=6))
            if cfg["save_model"]:
                import joblib
                joblib.dump({"pipeline": pipe, "feature_names": names}, cfg["save_model"])
                print(f"\nSaved model -> {cfg['save_model']}")
        except ValueError as e:
            print(f"[final model skipped] {e}")

    if cfg["save_report"]:
        with open(cfg["save_report"], "w") as f:
            json.dump(results, f, indent=2)
        print(f"\nSaved results -> {cfg['save_report']}")

    return results


if __name__ == "__main__":
    main()
