# Software vs FPGA: inference speed

Classifier only (1,664 features in → class out, including the per-subject
normalisation). Host: Apple M1, Python 3.12.13,
NumPy 2.4.6, scikit-learn 1.9.0, SciPy 1.17.1.
500 random trials × 3 repeats after warm-up.

| path | latency median (µs) | p99 (µs) | throughput (trials/s) | speed-up vs (a) | speed-up vs (c) |
|---|---|---|---|---|---|
| SW (a) sklearn, 1 trial/call | 527.1 | 590.2 | 1,897 | 1.0x | 0.07x |
| SW (b) sklearn, batched (per trial) | 6.52 | - | 153,412 | 80.9x | 5.7x |
| SW (c) NumPy folded, 1 trial/call | 37.5 | 47.1 | 26,697 | 14.1x | 1.0x |
| HW compute (rtl-sim, 100 MHz) | 18.45 | 18.45 (deterministic) | 54,171 | 28.6x | 2.0x |

HW compute is measured by on-chip cycle counters: latency is first feature accepted
→ result valid (1845 cycles), and throughput is back-to-back trials
(1846.0 cycles/trial). Features stream at 1 per cycle, so latency is ~90% feature
ingest; the arithmetic after the last feature takes ~180 cycles.
Backend is the RTL simulation: cycle counts are exact, µs assume the clock above (check Fmax in the Vivado timing report).

## Where end-to-end time goes (link transfer per trial: 6657 B in + 72 B out)
| link | transfer | transfer + HW compute |
|---|---|---|
| UART 921.6 kbaud | 73.01 ms | 73.03 ms |
| UART 3 Mbaud | 22.43 ms | 22.45 ms |
| SPI 25 MHz | 2.15 ms | 2.17 ms |
| SPI 50 MHz, 4-bit (QSPI) | 0.27 ms | 0.29 ms |

Over UART the link dominates end-to-end time. The FPGA's compute advantage only shows
end-to-end with a faster link, or when features are computed on the FPGA itself.
