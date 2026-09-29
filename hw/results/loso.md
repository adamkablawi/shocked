# Software vs FPGA: leave-one-subject-out accuracy

For each held-out subject, the stack is retrained in software on the other subjects
(same code path as `train_conn_model._loso_fold`). That fold's folded + quantised
weights are uploaded to the hardware, and the held-out subject's trials are streamed.
This is the generalisation comparison; the deployed model's in-sample numbers are in
comparison.md.

Model card reference (FourConnModel LOSO): acc 66.58%, bal 62.96%.

| path | LOSO acc (mean ± sd over folds) | LOSO bal acc | recall no_stim | recall medium | recall max |
|---|---|---|---|---|---|
| software (sklearn, per-fold retrain) | 66.58% ± 8.49% | 62.96% ± 13.23% | 0.546 | 0.776 | 0.567 |
| hardware (rtl-sim, per-fold upload) | 66.56% ± 8.52% | 62.92% ± 13.21% | 0.545 | 0.776 | 0.567 |

Class agreement hw vs sw over all held-out trials: **99.45%**
(25 of 4560 trials differ).

## Per fold
| held-out subject | trials | sw acc | hw acc | hw = sw |
|---|---|---|---|---|
| EMS0001 | 157 | 80.89% | 80.89% | 98.73% |
| EMS0002 | 159 | 61.01% | 61.01% | 98.74% |
| EMS0003 | 158 | 58.86% | 58.86% | 99.37% |
| EMS0004 | 158 | 60.76% | 60.76% | 100.00% |
| EMS0005 | 159 | 55.97% | 55.97% | 100.00% |
| EMS0006 | 158 | 54.43% | 54.43% | 100.00% |
| EMS0007 | 157 | 66.88% | 66.88% | 100.00% |
| EMS0008 | 157 | 65.61% | 65.61% | 100.00% |
| EMS0009 | 158 | 71.52% | 71.52% | 100.00% |
| EMS0011 | 155 | 56.77% | 56.13% | 99.35% |
| EMS0012 | 156 | 58.97% | 58.97% | 99.36% |
| EMS0013 | 157 | 82.17% | 82.17% | 97.45% |
| EMS0014 | 157 | 73.25% | 73.25% | 98.73% |
| EMS0015 | 156 | 67.95% | 67.95% | 98.72% |
| EMS0016 | 157 | 61.15% | 61.15% | 100.00% |
| EMS0017 | 158 | 61.39% | 61.39% | 100.00% |
| EMS0018 | 158 | 60.13% | 59.49% | 99.37% |
| EMS0019 | 157 | 57.32% | 57.96% | 99.36% |
| EMS0020 | 157 | 77.71% | 77.71% | 100.00% |
| EMS0021 | 157 | 67.52% | 68.79% | 98.73% |
| EMS0022 | 159 | 81.76% | 82.39% | 99.37% |
| EMS0023 | 157 | 71.97% | 71.34% | 99.36% |
| EMS0025 | 159 | 68.55% | 67.30% | 98.74% |
| EMS0026 | 156 | 55.77% | 55.77% | 100.00% |
| EMS0027 | 158 | 68.35% | 68.99% | 99.37% |
| EMS0028 | 155 | 77.42% | 77.42% | 100.00% |
| EMS0029 | 157 | 76.43% | 75.80% | 99.36% |
| EMS0030 | 157 | 57.32% | 57.32% | 100.00% |
| EMS0031 | 156 | 73.08% | 73.08% | 100.00% |
