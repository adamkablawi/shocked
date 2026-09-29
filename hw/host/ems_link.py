"""
ems_link.py
===========
Host-side access to the classifier, with two interchangeable backends:

  FpgaLink       the real board over UART (protocol in rtl/ems_uart_bridge.sv)
  RtlSimBackend  the same RTL run in Verilator (hw/Makefile `sim-core`), so every
                 comparison can be run without hardware

Both expose  infer(segments) -> dict of arrays, where a segment is
  (qm or None, (mu_q, m, s), xq_rows)
  qm      : quantised model to upload first (None = keep what is loaded)
  mu_q..s : per-subject calibration (fxp.quantize_calib)
  xq_rows : (n, 1664) int64 features, Q13.19
"""
from __future__ import annotations
import os, sys, struct, subprocess, time, tempfile
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))
import common as c          # noqa: E402
import fxp                  # noqa: E402

PKT_LEN = 72


def _empty(n):
    return {"cls": np.zeros(n, int), "probs": np.zeros((n, 3), np.int64),
            "fam_probs": np.zeros((n, 12), np.int64), "lat_cycles": np.zeros(n, np.int64),
            "wall_ns": np.zeros(n, np.int64)}


def _group_writes(writes):
    """[(addr, data)] -> [(start_addr, [data...])] contiguous runs, for burst upload."""
    runs = []
    for a, d in sorted(writes):
        if runs and a == runs[-1][0] + len(runs[-1][1]):
            runs[-1][1].append(d)
        else:
            runs.append((a, [d]))
    return runs


# ─────────────────────────────────────────────
# Real hardware
# ─────────────────────────────────────────────
class FpgaLink:
    name = "fpga"

    def __init__(self, port, baud=921600, timeout=5.0):
        import serial                                   # pip install pyserial
        self.ser = serial.Serial(port, baud, timeout=timeout)
        self.ser.reset_input_buffer()

    def close(self):
        self.ser.close()

    def _read(self, n):
        b = self.ser.read(n)
        if len(b) != n:
            raise TimeoutError(f"expected {n} bytes from FPGA, got {len(b)}")
        return b

    def _ack(self):
        b = self._read(1)
        if b != b"k":
            raise RuntimeError(f"expected ack 'k', got {b!r}")

    def write(self, addr, data):
        self.ser.write(b"W" + struct.pack("<HQ", addr, data)); self._ack()

    def burst(self, addr, words):
        for i in range(0, len(words), 4096):
            chunk = words[i:i + 4096]
            self.ser.write(b"B" + struct.pack("<HH", addr + i, len(chunk)) +
                           b"".join(struct.pack("<Q", w) for w in chunk))
            self._ack()

    def upload(self, writes):
        for a, words in _group_writes(writes):
            self.burst(a, words)

    def upload_model(self, qm):
        self.upload(fxp.model_writes(qm))

    def upload_calib(self, calib):
        self.burst(fxp.ADDR_CALIB, fxp.calib_words(*calib))

    def _packet(self):
        p = self._read(PKT_LEN)
        if p[0] != ord("R"):
            raise RuntimeError(f"bad result packet header {p[0]:#x}")
        v = struct.unpack("<B3I12IIIH", p[1:])
        return {"cls": v[0], "probs": v[1:4], "fam_probs": v[4:16],
                "lat_cycles": v[16], "total_cycles": v[17], "runs": v[18]}

    def run(self, xq_row):
        """Send one trial's features, return the result packet (+ host wall time)."""
        payload = b"F" + np.asarray(xq_row, dtype=np.int64).astype("<u4", casting="unsafe").tobytes()
        t0 = time.perf_counter_ns()
        self.ser.write(payload)
        r = self._packet()
        r["wall_ns"] = time.perf_counter_ns() - t0
        return r

    def rerun(self, n):
        """Re-run the buffered trial n times back-to-back (on-chip throughput)."""
        self.ser.write(b"T" + struct.pack("<H", n))
        return self._packet()

    def infer(self, segments, progress=True):
        n = sum(len(x) for _, _, x in segments)
        out, k = _empty(n), 0
        for si, (qm, calib, xq) in enumerate(segments):
            if qm is not None:
                self.upload_model(qm)
            self.upload_calib(calib)
            for row in xq:
                r = self.run(row)
                out["cls"][k] = r["cls"]; out["probs"][k] = r["probs"]
                out["fam_probs"][k] = r["fam_probs"]; out["lat_cycles"][k] = r["lat_cycles"]
                out["wall_ns"][k] = r["wall_ns"]; k += 1
            if progress:
                print(f"  fpga: segment {si + 1}/{len(segments)} done ({k}/{n} trials)", flush=True)
        return out


# ─────────────────────────────────────────────
# RTL simulation (Verilator)
# ─────────────────────────────────────────────
class RtlSimBackend:
    name = "rtl-sim"

    def __init__(self, hw_dir=c.HW_DIR):
        self.hw = hw_dir

    def infer(self, segments, progress=True):
        import golden_model as gm
        with tempfile.TemporaryDirectory() as td:
            vec, res = os.path.join(td, "vec.txt"), os.path.join(td, "res.txt")
            with open(vec, "w") as fh:
                for qm_seg, calib, xq in segments:
                    # expectations come from the bit-accurate model; the TB checks them
                    qm_eff = qm_seg if qm_seg is not None else self._last_qm
                    exp = fxp.infer_q(xq, *(np.broadcast_to(v, xq.shape) for v in calib), qm_eff)
                    gm.write_segment(fh, xq, calib, exp,
                                     model_writes=fxp.model_writes(qm_seg) if qm_seg is not None else None)
                    self._last_qm = qm_eff
            if progress:
                print(f"  rtl-sim: running Verilator on {sum(len(x) for *_, x in segments)} trials ...",
                      flush=True)
            p = subprocess.run(["make", "-s", "sim-core", f"VEC={vec}", f"OUT={res}"],
                               cwd=self.hw, capture_output=True, text=True)
            summary = [l for l in p.stdout.splitlines() if l.startswith(("trials", "latency", "period"))]
            if p.returncode != 0:
                raise RuntimeError("RTL simulation failed:\n" + p.stdout[-3000:] + p.stderr[-3000:])
            a = np.loadtxt(res, dtype=np.int64, ndmin=2)
        self.summary = summary
        return {"cls": a[:, 0].astype(int), "probs": a[:, 1:4], "fam_probs": a[:, 4:16],
                "lat_cycles": a[:, 16], "wall_ns": np.zeros(len(a), np.int64)}

    _last_qm = None


def set_default_model(backend, qm):
    """The RTL sim starts from the power-on (exported) model."""
    if isinstance(backend, RtlSimBackend):
        backend._last_qm = qm
