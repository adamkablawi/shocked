"""
golden_model.py
===============
Reference models + test vectors for the FPGA classifier.

    python hw/scripts/golden_model.py --check-float   # folded float model vs sklearn
    python hw/scripts/golden_model.py --check-fixed   # bit-accurate model vs float
    python hw/scripts/golden_model.py --gen-vectors   # hw/tb/vectors/core.txt
    python hw/scripts/golden_model.py --gen-softmax   # hw/tb/vectors/softmax.txt

Vector file format (one command per line, hex fields):
    C <addr> <data64>                  cfg write
    X <x32>                            one feature (Q13.19)
    E <cls> <p0> <p1> <p2> <fp0..fp11> expected result of the preceding trial
"""
from __future__ import annotations
import os, sys, argparse
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as c
import fxp


class Setup:
    """Features, model, and per-subject calibration, all in one place."""
    def __init__(self):
        self.d = c.load_features()
        self.art = c.load_model()
        self.fm = fxp.fold_model(self.art)
        self.qm = fxp.quantize_model(self.fm)
        X, g = self.d["X"], self.d["groups"]
        self.Z = c.zscore(X, g)
        self.xq = fxp.quantize_x(X)
        mu, sd = c.subject_stats(X, g)
        self.calib = [fxp.quantize_calib(mu[i], sd[i]) for i in range(len(mu))]

    def calib_rows(self, idx=None):
        g = self.d["groups"] if idx is None else self.d["groups"][idx]
        return tuple(np.stack([cc[k] for cc in self.calib])[g] for k in range(3))

    def sklearn(self, Z=None):
        Z = self.Z if Z is None else Z
        off, P = 0, []
        for f in c.FAMILIES:
            n = self.d["mats"][f].shape[1]
            P.append(self.art["base_models"][f].predict_proba(Z[:, off:off + n])); off += n
        P = np.hstack(P); meta = self.art["meta_learner"]
        return {"fam_probs": P, "probs": meta.predict_proba(P), "cls": meta.predict(P)}

    def fixed(self, qm=None, idx=slice(None)):
        idx = np.arange(len(self.d["y"]))[idx]
        return fxp.infer_q(self.xq[idx], *self.calib_rows(idx), self.qm if qm is None else qm)


def check_float(S):
    sk = S.sklearn(); fl = fxp.infer_float(S.Z, S.fm)
    agree = (sk["cls"] == fl["cls"]).mean()
    print(f"folded float vs sklearn: class agreement {agree*100:.2f}% "
          f"({(sk['cls'] != fl['cls']).sum()} trials differ; caused only by the "
          f"degenerate erp base_mean features, whose sklearn value is float noise)")
    return sk, fl


def check_fixed(S):
    fl = fxp.infer_float(S.Z, S.fm); q = S.fixed()
    y = S.d["y"]
    print(f"fixed vs float: class agreement {(q['cls'] == fl['cls']).mean()*100:.3f}%  "
          f"max|dp| final {np.abs(q['probs']/65536 - fl['probs']).max():.2e}  "
          f"family {np.abs(q['fam_probs']/65536 - fl['fam_probs']).max():.2e}")
    print(f"in-sample acc: float {(fl['cls'] == y).mean()*100:.2f}%  fixed {(q['cls'] == y).mean()*100:.2f}%")
    return q


# ─────────────────────────────────────────────
# Vectors
# ─────────────────────────────────────────────
def _h(v, bits):
    return f"{int(v) & ((1 << bits) - 1):0{(bits + 3) // 4}x}"


def write_segment(fh, xq, calib, res, model_writes=None):
    """Append one segment: optional model upload, calibration upload, trials."""
    for a, w in (model_writes or []):
        fh.write(f"C {a:04x} {w:016x}\n")
    for k, w in enumerate(fxp.calib_words(*calib)):
        fh.write(f"C {fxp.ADDR_CALIB + k:04x} {w:016x}\n")
    for t in range(xq.shape[0]):
        fh.write("".join(f"X {_h(v, 32)}\n" for v in xq[t]))
        fh.write("E " + " ".join([f"{res['cls'][t]:x}"] +
                                 [_h(p, 17) for p in res["probs"][t]] +
                                 [_h(p, 17) for p in res["fam_probs"][t]]) + "\n")


def alt_model(qm):
    """A different (but valid-range) model to prove the weight/bias/meta upload path."""
    alt = {"W": {f: np.roll(qm["W"][f], 1, axis=1) for f in fxp.FAMILIES},
           "b": {f: qm["b"][f][::-1].copy() for f in fxp.FAMILIES},
           "mc": qm["mc"][::-1].copy(), "mb": qm["mb"][::-1].copy()}
    return alt


def gen_vectors(S, path, subjects=(0, 1), alt_subject=2, max_trials=None):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    g = S.d["groups"]; n = 0
    with open(path, "w") as fh:
        for si in subjects:                                  # power-on model
            idx = np.where(g == si)[0][:max_trials]
            write_segment(fh, S.xq[idx], S.calib[si], S.fixed(idx=idx)); n += len(idx)
        if alt_subject is not None:                          # uploaded model
            am = alt_model(S.qm)
            idx = np.where(g == alt_subject)[0][:max_trials]
            write_segment(fh, S.xq[idx], S.calib[alt_subject], S.fixed(am, idx=idx),
                          model_writes=fxp.model_writes(am)); n += len(idx)
    print(f"wrote {n} trials -> {path}")


def gen_softmax_vectors(path, n=20000, seed=0):
    """Adversarial softmax3 vectors: random, ties, huge spreads, saturated logits."""
    rng = np.random.default_rng(seed)
    lg = [rng.integers(-(20 << 16), 20 << 16, size=(n // 2, 3)),          # typical
          rng.integers(-(1 << 31), (1 << 31) - 1, size=(n // 4, 3)),      # full range
          np.repeat(rng.integers(-(8 << 16), 8 << 16, size=(n // 8, 1)), 3, axis=1)]  # 3-way ties
    near = rng.integers(-(4 << 16), 4 << 16, size=(n // 8, 3))
    near[:, 1] = near[:, 0] + rng.integers(-2, 3, size=n // 8)            # near ties
    near[:, 2] = near[:, 0] + (rng.integers(28, 36, size=n // 8) << 16)   # around the clamp
    lg = np.vstack(lg + [near,
                         np.array([[(1 << 31) - 1, -(1 << 31), 0], [-(1 << 31)] * 3,
                                   [(1 << 31) - 1] * 3, [0, 0, 0]])]).astype(np.int64)
    p = fxp.softmax3_q(lg)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as fh:
        for a, b in zip(lg, p):
            fh.write(" ".join([_h(v, 32) for v in a] + [_h(v, 17) for v in b]) + "\n")
    print(f"wrote {len(lg)} softmax vectors -> {path}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-float", action="store_true")
    ap.add_argument("--check-fixed", action="store_true")
    ap.add_argument("--gen-vectors", action="store_true")
    ap.add_argument("--gen-softmax", action="store_true")
    ap.add_argument("--max-trials", type=int, default=None, help="per subject")
    ap.add_argument("--out", default=os.path.join(c.HW_DIR, "tb", "vectors", "core.txt"))
    a = ap.parse_args()
    S = Setup() if (a.check_float or a.check_fixed or a.gen_vectors) else None
    if a.check_float: check_float(S)
    if a.check_fixed: check_fixed(S)
    if a.gen_vectors: gen_vectors(S, a.out, max_trials=a.max_trials)
    if a.gen_softmax: gen_softmax_vectors(os.path.join(c.HW_DIR, "tb", "vectors", "softmax.txt"))
