# EMS intensity classifier on FPGA (Spartan-7)

Synthesizable SystemVerilog implementation of the **FourConnModel** stacking
classifier (`FinalModels/FourConnModel/conn_stacking_ensemble.joblib`:
erp + bp + tf + conn, shrinkage-LDA per family, logistic meta-learner, 3 classes).

**Scope:** classifier only. The host extracts the 1,664 features with the same Python
code the model was trained with. The FPGA does the rest:

- per-subject normalisation
- 4 LDAs
- softmax
- meta-learner
- class + probabilities

```
host (Python)                               FPGA (Arty S7, 100 MHz)
epoch 60x425 ─► features (1664) ─ UART ─►  ems_uart_bridge ─► ems_classifier ─► class, p[3]
calibration block ─► mean/SD ─── UART ─►  calibration RAM          │
                                                                    └─ cycle counters
```

## Layout
| path | what |
|---|---|
| `scripts/fxp.py` | fixed-point formats + **bit-accurate model of the RTL** (single source of truth) |
| `scripts/export_model.py` | joblib → `rtl/mem/*.mem` + generated `rtl/ems_params_pkg.sv` |
| `scripts/golden_model.py` | float / fixed checks, test-vector generation |
| `rtl/ems_classifier.sv` | core: normalise → MAC → softmax → meta-learner |
| `rtl/ems_softmax3.sv` | 3-way softmax (exp LUT + exact divider) |
| `rtl/ems_uart_bridge.sv`, `uart_*.sv`, `arty_s7_top.sv` | board I/O and command protocol |
| `tb/` | Verilator testbenches (softmax unit, core bit-exact, UART end-to-end) |
| `vivado/build.tcl`, `constraints/arty_s7.xdc` | Vivado non-project build |
| `host/ems_link.py` | UART protocol + RTL-simulation backend |
| `host/ems_host.py` | calibrate + classify from a PC (also a Python API for the closed loop) |
| `host/compare_sw_fpga.py` | software vs FPGA: agreement, LOSO accuracy, speed |
| `results/` | generated comparison reports |

## Quick start
```bash
cd hw
make all                        # export model, golden checks, vectors, lint, 3 simulations
python3 host/compare_sw_fpga.py --all          # SW vs RTL-sim: agreement, LOSO, speed
```
The first run extracts features for all 29 subjects (~1 min) and caches them in `hw/cache/`.
Needs `verilator` ≥ 5 and the repo's Python environment (numpy, scipy, scikit-learn,
joblib). For the board you also need `pip install pyserial`.

### Vivado (e.g. over SSH)
Copy or clone `hw/` and run from inside it:
```bash
vivado -mode batch -source vivado/build.tcl                  # synth + impl + bitstream
vivado -mode batch -source vivado/build.tcl -tclargs synth   # synthesis only
EMS_PART=xc7s25csga324-1 vivado -mode batch -source vivado/build.tcl   # Arty S7-25
```
Reports and `ems_classifier.bit` go to `build/vivado/`. The last line prints WNS/Fmax.
Pin locations follow Digilent's Arty-S7 master XDC. Check them against your board
revision.

### On the board
```bash
python3 host/ems_host.py --port /dev/tty.usbserial-XXXX --subject EMS0001 --trials 20
python3 host/compare_sw_fpga.py --all --backend fpga --port /dev/tty.usbserial-XXXX
```

## Numerics
| signal | format | notes |
|---|---|---|
| feature x, mean μ | s32 Q13.19 | range ±4096 (largest raw feature: erp rise slope ≈ −2540) |
| 1/SD | 17-bit mantissa + 6-bit shift | per feature, any range |
| z | s18 Q4.13 | saturates at ±16 (max seen 11.4) |
| folded LDA weight | s18 Q1.16 | StandardScaler folded in at export |
| accumulators | s48 | |
| logits | s32 Q.16 | |
| probabilities | u17 Q0.16 | exp: 1024-entry 2^-f LUT; exact restoring division |
| meta coefficients | s18 Q2.15 | |

The per-subject z-score happens on-chip, from calibration the host uploads. The
model's StandardScaler (mean≈0, scale≈1, since training data was already z-scored) is
folded into the LDA weights at export time.

**Degenerate features.** The 8 `erp base_mean@*` features are exactly 0 after baseline
correction. In sklearn, the z-score (÷(σ+1e-12)) and the scaler (scale ≈ 1e-4) amplify
their float round-off into non-zero inputs. The export zeroes those weights, and this
changes the deployed sklearn model's prediction on 14/4560 trials (0.3%). Every
hardware-vs-sklearn comparison therefore tops out at ~99.7%; hardware vs the folded
float model is 100%.

## Command protocol (UART 921600 8N1, little-endian)
| cmd | payload | reply |
|---|---|---|
| `W` | addr[2] data[8] | `k` |
| `B` | addr[2] count[2] data[8]×count | `k` |
| `F` | x[4]×1664 | 72-byte result packet |
| `T` | runs[2] | result packet after `runs` back-to-back re-runs of the buffered trial |

Result packet: `R` class[1] p[4]×3 fam_p[4]×12 lat_cycles[4] total_cycles[4] runs[2].

Config address map (64-bit words):
- `0x0000+k` calibration `{shift[6], mantissa[17], mu[32]}`
- `0x0800+k` weights `{w2,w1,w0}`
- `0x1000+3f+j` family bias
- `0x1010+12j+i` meta coefficient
- `0x1040+j` meta bias

Weights, biases and meta power up with the exported model and are all writable. That
is how the LOSO comparison runs each fold's model on the hardware.
