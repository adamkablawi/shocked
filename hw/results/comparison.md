# Software vs FPGA inference: agreement

Backend: **rtl-sim**. Deployed model `FourConnModel/conn_stacking_ensemble.joblib`,
4560 trials from 29 subjects, per-subject z-score from each subject's own trials
(as in training). All paths receive identical feature vectors.

## Agreement
| comparison | class agreement | # differ | final prob |err| mean / max | family prob |err| mean / max |
|---|---|---|---|---|
| hw vs sklearn (deployed) | 99.69% | 14 | 2.22e-03 / 2.59e-01 | 1.08e-03 / 4.48e-01 |
| hw vs folded float | 100.00% | 0 | 6.51e-05 / 3.73e-04 | 4.93e-05 / 3.30e-04 |
| hw vs fixed-point model | 100.00% | 0 | bit-exact | - |

hw vs sklearn disagreements come from the 8 degenerate `erp base_mean` features: they
are exactly 0 after baseline correction, and sklearn's z-score (divide by 1e-12) plus
its scaler (scale 1e-4) turn their float round-off into non-zero inputs. No fixed-point
design can reproduce that. hw vs the folded float model isolates quantisation error.

## Accuracy against true labels (in-sample: the deployed model was trained on these subjects)
| path | acc | bal acc | recall no_stim | recall medium | recall max |
|---|---|---|---|---|---|
| sklearn (deployed) | 76.32% | 74.05% | 0.683 | 0.832 | 0.707 |
| folded float | 76.45% | 74.17% | 0.684 | 0.833 | 0.708 |
| fixed-point model | 76.45% | 74.17% | 0.684 | 0.833 | 0.708 |
| hw (rtl-sim) | 76.45% | 74.17% | 0.684 | 0.833 | 0.708 |

## Per subject
| subject | trials | hw = sklearn | sklearn acc | hw acc |
|---|---|---|---|---|
| EMS0001 | 157 | 100.00% | 85.99% | 85.99% |
| EMS0002 | 159 | 98.74% | 71.70% | 71.70% |
| EMS0003 | 158 | 98.73% | 77.22% | 77.22% |
| EMS0004 | 158 | 100.00% | 68.99% | 68.99% |
| EMS0005 | 159 | 99.37% | 66.67% | 67.30% |
| EMS0006 | 158 | 100.00% | 62.03% | 62.03% |
| EMS0007 | 157 | 99.36% | 85.35% | 85.99% |
| EMS0008 | 157 | 100.00% | 79.62% | 79.62% |
| EMS0009 | 158 | 100.00% | 79.75% | 79.75% |
| EMS0011 | 155 | 100.00% | 64.52% | 64.52% |
| EMS0012 | 156 | 100.00% | 62.82% | 62.82% |
| EMS0013 | 157 | 98.73% | 87.26% | 87.26% |
| EMS0014 | 157 | 99.36% | 83.44% | 84.08% |
| EMS0015 | 156 | 100.00% | 79.49% | 79.49% |
| EMS0016 | 157 | 100.00% | 74.52% | 74.52% |
| EMS0017 | 158 | 100.00% | 72.78% | 72.78% |
| EMS0018 | 158 | 100.00% | 73.42% | 73.42% |
| EMS0019 | 157 | 99.36% | 64.33% | 64.97% |
| EMS0020 | 157 | 100.00% | 84.71% | 84.71% |
| EMS0021 | 157 | 98.73% | 82.17% | 83.44% |
| EMS0022 | 159 | 100.00% | 86.16% | 86.16% |
| EMS0023 | 157 | 99.36% | 81.53% | 80.89% |
| EMS0025 | 159 | 100.00% | 77.36% | 77.36% |
| EMS0026 | 156 | 100.00% | 68.59% | 68.59% |
| EMS0027 | 158 | 100.00% | 79.11% | 79.11% |
| EMS0028 | 155 | 100.00% | 84.52% | 84.52% |
| EMS0029 | 157 | 100.00% | 82.80% | 82.80% |
| EMS0030 | 157 | 100.00% | 68.79% | 68.79% |
| EMS0031 | 156 | 99.36% | 77.56% | 78.21% |

## Disagreements with sklearn (first 25)
| trial | subject | true | sklearn | hw | sklearn probs | hw probs |
|---|---|---|---|---|---|---|
| 247 | EMS0002 | 1 | 1 | 0 | 0.468 0.498 0.034 | 0.536 0.438 0.026 |
| 277 | EMS0002 | 0 | 1 | 0 | 0.449 0.515 0.036 | 0.567 0.408 0.025 |
| 351 | EMS0003 | 1 | 0 | 1 | 0.570 0.395 0.035 | 0.407 0.528 0.064 |
| 449 | EMS0003 | 0 | 0 | 1 | 0.500 0.455 0.045 | 0.396 0.539 0.065 |
| 718 | EMS0005 | 0 | 1 | 0 | 0.447 0.513 0.040 | 0.490 0.477 0.034 |
| 1105 | EMS0007 | 1 | 2 | 1 | 0.030 0.484 0.486 | 0.027 0.518 0.455 |
| 1781 | EMS0013 | 0 | 0 | 1 | 0.696 0.282 0.023 | 0.474 0.475 0.051 |
| 1842 | EMS0013 | 1 | 0 | 1 | 0.571 0.408 0.022 | 0.408 0.554 0.038 |
| 1942 | EMS0014 | 1 | 0 | 1 | 0.507 0.476 0.017 | 0.464 0.516 0.020 |
| 2771 | EMS0019 | 0 | 1 | 0 | 0.403 0.552 0.045 | 0.550 0.421 0.029 |
| 3064 | EMS0021 | 1 | 0 | 1 | 0.490 0.483 0.027 | 0.486 0.486 0.028 |
| 3104 | EMS0021 | 2 | 1 | 2 | 0.021 0.490 0.490 | 0.021 0.488 0.491 |
| 3461 | EMS0023 | 1 | 1 | 2 | 0.029 0.509 0.461 | 0.031 0.481 0.488 |
| 4440 | EMS0031 | 1 | 2 | 1 | 0.021 0.489 0.490 | 0.021 0.490 0.489 |

