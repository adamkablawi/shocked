"""
fxp.py
======
Fixed-point formats, quantisation and the BIT-ACCURATE model of the RTL.
Every integer operation here is mirrored 1:1 in hw/rtl -- if you change one,
change the other (and regenerate vectors).

Datapath (per trial, features streamed in FAMILIES order):
  x    s32  Q13.19   raw feature from host
  mu   s32  Q13.19   per-subject feature mean            (calibration)
  m,s  u17 / u6      1/sd = m * 2^-(s-6)                  (calibration)
  z    s18  Q4.13    z = sat18((x - mu) * m  >>r s)       (>>r = round-half-up shift)
  w    s18  Q1.16    folded LDA weight (scaler folded in)
  acc  s48  Q.29     sum z*w over the family
  lg   s32  Q.16     logit = (acc >>r 13) + bias_q16
  softmax3: e_j = EXP_LUT[fidx] >> n,  t = ((max-lg_j) * LOG2E) >> 16
            p_j = floor(e_j * 2^16 / (e0+e1+e2))          u17 Q0.16
  meta: c s18 Q2.15, logit = (sum p*c >>r 15) + mbias_q16 -> argmax (+ softmax3)
"""
from __future__ import annotations
import numpy as np

FAMILIES = ["erp", "bp", "tf", "conn"]
N_CLASSES = 3

X_FRAC = 19;  X_BITS = 32          # raw feature / mu
Z_FRAC = 13;  Z_BITS = 18          # normalised feature
W_FRAC = 16;  W_BITS = 18          # folded LDA weights
ACC_FRAC = Z_FRAC + W_FRAC         # 29
L_FRAC = 16;  L_BITS = 32          # logits
M_BITS = 17                        # inv-sd mantissa (unsigned, [2^16, 2^17))
S_BITS = 6                         # inv-sd shift
P_FRAC = 16;  P_BITS = 17          # probabilities, unsigned (1.0 = 65536)
C_FRAC = 15;  C_BITS = 18          # meta coefficients
E_FRAC = 17;  E_BITS = 18          # exp LUT values (1.0 = 131072)
EXP_IDX_BITS = 10                  # 1024-entry 2^-f LUT
LOG2E_Q16 = int(round(np.log2(np.e) * (1 << 16)))   # 94548 (u17)
DIFF_CLAMP = 32 << L_FRAC          # max-lg >= 32 -> e = 0 (t >= 46 > 18 shifts)
SD_EPS = 1e-9                      # sd below this -> m = 0 (degenerate feature)
DEGENERATE_SCALE = 1e-2            # scaler scale below this -> weight forced 0

EXP_LUT = np.array([int(round(2.0 ** (-i / (1 << EXP_IDX_BITS)) * (1 << E_FRAC)))
                    for i in range(1 << EXP_IDX_BITS)], dtype=np.int64)


def _sat(v, bits):
    lo, hi = -(1 << (bits - 1)), (1 << (bits - 1)) - 1
    return np.clip(v, lo, hi)


def _rshift_round(v, s):
    """Arithmetic right shift with round-half-up; s may be an array, s >= 1."""
    v = np.asarray(v, dtype=np.int64); s = np.asarray(s, dtype=np.int64)
    return (v + (np.int64(1) << (s - 1))) >> s


# ─────────────────────────────────────────────
# Quantisation of model / calibration / inputs
# ─────────────────────────────────────────────
def fold_model(art):
    """Float folded model: W[f] (3, d_f), b[f] (3,), meta coef (3,12), meta bias (3,)."""
    W, b = {}, {}
    for f in FAMILIES:
        m = art["base_models"][f]
        sc = m.named_steps["standardscaler"]; lda = m.named_steps["lineardiscriminantanalysis"]
        assert list(lda.classes_) == [0, 1, 2]
        Wf = lda.coef_ / sc.scale_
        Wf[:, sc.scale_ < DEGENERATE_SCALE] = 0.0        # constant features (erp base_mean)
        W[f] = Wf
        b[f] = lda.intercept_ - Wf @ sc.mean_
    meta = art["meta_learner"]
    return {"W": W, "b": b, "mc": meta.coef_.copy(), "mb": meta.intercept_.copy()}


def quantize_model(fm):
    q = {"W": {}, "b": {}}
    for f in FAMILIES:
        q["W"][f] = _sat(np.round(fm["W"][f] * (1 << W_FRAC)).astype(np.int64), W_BITS)
        q["b"][f] = _sat(np.round(fm["b"][f] * (1 << L_FRAC)).astype(np.int64), L_BITS)
    q["mc"] = _sat(np.round(fm["mc"] * (1 << C_FRAC)).astype(np.int64), C_BITS)
    q["mb"] = _sat(np.round(fm["mb"] * (1 << L_FRAC)).astype(np.int64), L_BITS)
    return q


def quantize_x(X):
    return _sat(np.round(np.asarray(X) * (1 << X_FRAC)).astype(np.int64), X_BITS)


def quantize_calib(mu, sd):
    """mu, sd: (d,) float -> mu_q s32, m u17, s u6 such that z ~= (x-mu)/sd."""
    mu_q = quantize_x(mu)
    inv = 1.0 / (np.asarray(sd, dtype=float) + 1e-12)
    m = np.zeros(len(inv), dtype=np.int64); s = np.zeros(len(inv), dtype=np.int64)
    ok = np.asarray(sd) >= SD_EPS
    # z_raw = diff_raw * inv * 2^(Z_FRAC - X_FRAC) = diff_raw * m >> s
    k = (M_BITS - 1) - np.floor(np.log2(inv[ok])).astype(np.int64)
    mm = np.round(inv[ok] * np.exp2(k)).astype(np.int64)
    over = mm >= (1 << M_BITS)
    k[over] -= 1; mm[over] = np.round(inv[ok][over] * np.exp2(k[over])).astype(np.int64)
    ss = k + (X_FRAC - Z_FRAC)
    if ss.min() < 1 or ss.max() >= (1 << S_BITS):
        raise ValueError(f"inv-sd shift out of range [{ss.min()}, {ss.max()}]")
    m[ok], s[ok] = mm, ss
    s[~ok] = 1
    return mu_q, m, s


# ─────────────────────────────────────────────
# Bit-accurate model (vectorised over trials)
# ─────────────────────────────────────────────
def softmax3_q(lg):
    """lg: (n, 3) int64 Q.16 logits -> (n, 3) int64 Q0.16 probabilities."""
    mx = lg.max(axis=1, keepdims=True)
    diff = np.minimum(mx - lg, DIFF_CLAMP)                  # >= 0
    t = (diff * LOG2E_Q16) >> L_FRAC                        # Q.16
    n = t >> 16
    fidx = (t >> (16 - EXP_IDX_BITS)) & ((1 << EXP_IDX_BITS) - 1)
    e = np.where(n >= E_BITS, 0, EXP_LUT[fidx] >> np.minimum(n, 63))
    S = e.sum(axis=1, keepdims=True)                        # >= 2^17 (max term)
    return (e << P_FRAC) // S


def normalize_q(xq, mu_q, m, s):
    diff = xq - mu_q                                        # s33
    return _sat(_rshift_round(diff * m, s), Z_BITS)


def infer_q(xq, mu_q, m, s, qm):
    """xq, mu_q, m, s: (n, 1664) int64 (calib may be per-row). Returns dict."""
    z = normalize_q(xq, mu_q, m, s)
    off, fam_lg, fam_p = 0, [], []
    for f in FAMILIES:
        W = qm["W"][f]; d = W.shape[1]
        acc = z[:, off:off + d] @ W.T                       # Q.29, fits int64
        lg = _sat(_rshift_round(acc, ACC_FRAC - L_FRAC) + qm["b"][f], L_BITS)
        fam_lg.append(lg); fam_p.append(softmax3_q(lg)); off += d
    P = np.hstack(fam_p)                                    # (n, 12) Q0.16
    macc = P @ qm["mc"].T                                   # Q.31
    mlg = _sat(_rshift_round(macc, P_FRAC + C_FRAC - L_FRAC) + qm["mb"], L_BITS)
    return {"z": z, "fam_logits": np.hstack(fam_lg), "fam_probs": P,
            "meta_logits": mlg, "probs": softmax3_q(mlg),
            "cls": mlg.argmax(axis=1)}                      # ties -> lowest index


# ─────────────────────────────────────────────
# Float reference (folded) -- equals sklearn
# ─────────────────────────────────────────────
def infer_float(Z, fm):
    from scipy.special import softmax
    off, P, L = 0, [], []
    for f in FAMILIES:
        W = fm["W"][f]; d = W.shape[1]
        lg = Z[:, off:off + d] @ W.T + fm["b"][f]
        L.append(lg); P.append(softmax(lg, axis=1)); off += d
    P = np.hstack(P)
    ml = P @ fm["mc"].T + fm["mb"]
    return {"fam_logits": np.hstack(L), "fam_probs": P, "meta_logits": ml,
            "probs": softmax(ml, axis=1), "cls": ml.argmax(axis=1)}


# ─────────────────────────────────────────────
# Config-memory image (what the host writes over the cfg port)
# ─────────────────────────────────────────────
ADDR_CALIB = 0x0000   # + k : {s[5:0], m[16:0], mu[31:0]}  (55 bits)
ADDR_W     = 0x0800   # + k : {w2, w1, w0} s18 each        (54 bits)
ADDR_BIAS  = 0x1000   # + fam*3 + j : s32
ADDR_MC    = 0x1010   # + j*12 + i  : s18
ADDR_MB    = 0x1040   # + j         : s32


def _u(v, bits):
    return int(v) & ((1 << bits) - 1)


def calib_words(mu_q, m, s):
    return [(_u(s[k], S_BITS) << 49) | (_u(m[k], M_BITS) << 32) | _u(mu_q[k], X_BITS)
            for k in range(len(mu_q))]


def weight_words(qm):
    W = np.hstack([qm["W"][f] for f in FAMILIES])            # (3, 1664)
    return [(_u(W[2, k], W_BITS) << 36) | (_u(W[1, k], W_BITS) << 18) | _u(W[0, k], W_BITS)
            for k in range(W.shape[1])]


def model_writes(qm):
    """List of (addr, data) for a complete model upload (weights + biases + meta)."""
    wr = [(ADDR_W + k, w) for k, w in enumerate(weight_words(qm))]
    for fi, f in enumerate(FAMILIES):
        for j in range(N_CLASSES):
            wr.append((ADDR_BIAS + fi * 3 + j, _u(qm["b"][f][j], L_BITS)))
    for j in range(N_CLASSES):
        for i in range(4 * N_CLASSES):
            wr.append((ADDR_MC + j * 12 + i, _u(qm["mc"][j, i], C_BITS)))
        wr.append((ADDR_MB + j, _u(qm["mb"][j], L_BITS)))
    return wr
