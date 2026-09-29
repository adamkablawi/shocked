"""
compare_sw_fpga.py
==================
Software (sklearn) vs FPGA inference on the SAME feature vectors.

  python hw/host/compare_sw_fpga.py --agree            # trial-by-trial agreement
  python hw/host/compare_sw_fpga.py --loso             # held-out accuracy, SW vs FPGA
  python hw/host/compare_sw_fpga.py --bench            # speed
  python hw/host/compare_sw_fpga.py --all --backend fpga --port /dev/tty.usbserial-XXXX

Backends: rtl-sim (default; Verilator run of the exact RTL) or fpga (board over UART).
Outputs: hw/results/{comparison,loso,benchmark}.md + per-trial CSVs.

Paths compared:
  sklearn : the deployed joblib, float64 (the reference the model was validated with)
  float   : folded float model (scaler folded into weights; degenerate features = 0)
  fixed   : bit-accurate Python model of the RTL (fxp.py)
  hw      : the backend (FPGA or RTL sim)
"""
from __future__ import annotations
import os, sys, time, argparse, platform, subprocess, json
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))
import common as c                   # noqa: E402
import fxp                           # noqa: E402
import golden_model as gm            # noqa: E402
import ems_link                      # noqa: E402

from sklearn.metrics import balanced_accuracy_score, confusion_matrix   # noqa: E402

P_ONE = float(1 << fxp.P_FRAC)


def metrics(pred, y):
    cm = confusion_matrix(y, pred, labels=[0, 1, 2])
    return {"acc": float((pred == y).mean()), "bal": float(balanced_accuracy_score(y, pred)),
            "recall": (cm.diagonal() / np.maximum(cm.sum(1), 1)).tolist(), "cm": cm.tolist()}


def md_table(header, rows):
    s = "| " + " | ".join(header) + " |\n|" + "---|" * len(header) + "\n"
    return s + "".join("| " + " | ".join(str(v) for v in r) + " |\n" for r in rows)


def pct(v):
    return f"{100 * v:.2f}%"


def make_backend(a):
    if a.backend == "fpga":
        if not a.port:
            sys.exit("--backend fpga needs --port")
        return ems_link.FpgaLink(a.port, a.baud)
    return ems_link.RtlSimBackend()


def select_subjects(S, n):
    gs = np.unique(S.d["groups"])
    return gs if n is None else gs[:n]


# ─────────────────────────────────────────────
# 1. Agreement (deployed model, in-sample)
# ─────────────────────────────────────────────
def run_agree(S, be, a):
    g, y = S.d["groups"], S.d["y"]
    subs = select_subjects(S, a.subjects)
    segs, idx_all = [], []
    for k, si in enumerate(subs):
        idx = np.where(g == si)[0]
        segs.append((S.qm if k == 0 else None, S.calib[si], S.xq[idx]))
        idx_all.append(idx)
    idx = np.concatenate(idx_all)
    ems_link.set_default_model(be, S.qm)

    t0 = time.time()
    hw = be.infer(segs)
    print(f"  backend done in {time.time() - t0:.1f}s")
    sk_all = S.sklearn()
    sk = {k: v[idx] for k, v in sk_all.items()}
    fl = fxp.infer_float(S.Z[idx], S.fm)
    fx = S.fixed(idx=idx)
    yy = y[idx]

    bitexact = ((hw["cls"] == fx["cls"]) & (hw["probs"] == fx["probs"]).all(1)
                & (hw["fam_probs"] == fx["fam_probs"]).all(1))
    hp, hfp = hw["probs"] / P_ONE, hw["fam_probs"] / P_ONE
    rows = []
    for name, ref in [("sklearn (deployed)", sk), ("folded float", fl)]:
        dp, dfp = np.abs(hp - ref["probs"]), np.abs(hfp - ref["fam_probs"])
        rows.append([f"hw vs {name}", pct((hw["cls"] == ref["cls"]).mean()),
                     int((hw["cls"] != ref["cls"]).sum()),
                     f"{dp.mean():.2e} / {dp.max():.2e}", f"{dfp.mean():.2e} / {dfp.max():.2e}"])
    rows.append(["hw vs fixed-point model", pct((hw["cls"] == fx["cls"]).mean()),
                 int((hw["cls"] != fx["cls"]).sum()), "bit-exact" if bitexact.all() else
                 f"{(~bitexact).sum()} trials differ", "-"])

    acc_rows = []
    for name, pred in [("sklearn (deployed)", sk["cls"]), ("folded float", fl["cls"]),
                       ("fixed-point model", fx["cls"]), (f"hw ({be.name})", hw["cls"])]:
        m = metrics(pred, yy)
        acc_rows.append([name, pct(m["acc"]), pct(m["bal"])] + [f"{r:.3f}" for r in m["recall"]])

    subj_rows = []
    for si, ix in zip(subs, idx_all):
        sel = np.isin(idx, ix)
        subj_rows.append([S.d["sids"][si], int(sel.sum()),
                          pct((hw["cls"][sel] == sk["cls"][sel]).mean()),
                          pct((sk["cls"][sel] == yy[sel]).mean()), pct((hw["cls"][sel] == yy[sel]).mean())])

    dis = np.where(hw["cls"] != sk["cls"])[0]
    dis_rows = [[int(idx[i]), S.d["sids"][g[idx[i]]], int(yy[i]), int(sk["cls"][i]), int(hw["cls"][i]),
                 " ".join(f"{p:.3f}" for p in sk["probs"][i]), " ".join(f"{p:.3f}" for p in hp[i])]
                for i in dis[:25]]

    md = f"""# Software vs FPGA inference: agreement

Backend: **{be.name}**. Deployed model `FourConnModel/conn_stacking_ensemble.joblib`,
{len(idx)} trials from {len(subs)} subjects, per-subject z-score from each subject's own trials
(as in training). All paths receive identical feature vectors.

## Agreement
{md_table(["comparison", "class agreement", "# differ", "final prob |err| mean / max", "family prob |err| mean / max"], rows)}
hw vs sklearn disagreements come from the 8 degenerate `erp base_mean` features: they
are exactly 0 after baseline correction, and sklearn's z-score (divide by 1e-12) plus
its scaler (scale 1e-4) turn their float round-off into non-zero inputs. No fixed-point
design can reproduce that. hw vs the folded float model isolates quantisation error.

## Accuracy against true labels (in-sample: the deployed model was trained on these subjects)
{md_table(["path", "acc", "bal acc", "recall no_stim", "recall medium", "recall max"], acc_rows)}
## Per subject
{md_table(["subject", "trials", "hw = sklearn", "sklearn acc", "hw acc"], subj_rows)}
## Disagreements with sklearn (first 25)
{md_table(["trial", "subject", "true", "sklearn", "hw", "sklearn probs", "hw probs"], dis_rows) if dis_rows else "None."}
"""
    os.makedirs(c.RESULTS_DIR, exist_ok=True)
    with open(os.path.join(c.RESULTS_DIR, "comparison.md"), "w") as f:
        f.write(md)
    hdr = "trial,subject,y,sk_cls,hw_cls,fixed_cls,sk_p0,sk_p1,sk_p2,hw_p0,hw_p1,hw_p2,lat_cycles,wall_ns"
    arr = np.column_stack([idx, g[idx], yy, sk["cls"], hw["cls"], fx["cls"], sk["probs"], hp,
                           hw["lat_cycles"], hw["wall_ns"]])
    np.savetxt(os.path.join(c.RESULTS_DIR, "comparison_per_trial.csv"), arr, delimiter=",",
               header=hdr, comments="", fmt=["%d"] * 6 + ["%.6f"] * 6 + ["%d", "%d"])
    print(md.split("## Per subject")[0])
    return hw


# ─────────────────────────────────────────────
# 2. LOSO: retrain per fold in SW, upload each fold's weights to the HW
# ─────────────────────────────────────────────
def _fit_fold(Zm, y, groups, g_out, classes):
    import train_conn_model as tcm
    from sklearn.linear_model import LogisticRegression
    tr, te = groups != g_out, groups == g_out
    base, meta_tr, meta_te = {}, [], []
    for f in fxp.FAMILIES:
        F = Zm[f]
        meta_tr.append(tcm._oof(F[tr], y[tr], groups[tr], classes, tcm.CONFIG["inner_splits"]))
        base[f] = tcm.base_model().fit(F[tr], y[tr])
        meta_te.append(tcm._aligned_proba(base[f], F[te], classes))
    meta = LogisticRegression(max_iter=1000, C=tcm.CONFIG["meta_C"]).fit(np.hstack(meta_tr), y[tr])
    P = np.hstack(meta_te)
    art = {"base_models": base, "meta_learner": meta}
    return {"g": int(g_out), "sk_cls": meta.predict(P), "sk_probs": meta.predict_proba(P),
            "qm": fxp.quantize_model(fxp.fold_model(art))}


def loso_folds(S, subs, n_jobs):
    import joblib
    from joblib import Parallel, delayed
    cache = os.path.join(c.CACHE_DIR, "loso_folds.joblib")
    if os.path.exists(cache):
        folds = joblib.load(cache)
        if all(int(s) in folds for s in subs):
            return folds
    offs = np.cumsum([0] + [S.d["mats"][f].shape[1] for f in fxp.FAMILIES])
    Zm = {f: S.Z[:, offs[i]:offs[i + 1]] for i, f in enumerate(fxp.FAMILIES)}
    y, groups = S.d["y"], S.d["groups"]
    print(f"  training {len(subs)} LOSO folds in software (n_jobs={n_jobs}) ...", flush=True)
    t0 = time.time()
    res = Parallel(n_jobs=n_jobs, verbose=5)(
        delayed(_fit_fold)(Zm, y, groups, g, np.unique(y)) for g in subs)
    print(f"  folds trained in {time.time() - t0:.0f}s")
    folds = {r["g"]: r for r in res}
    joblib.dump(folds, cache)
    return folds


def run_loso(S, be, a):
    g, y = S.d["groups"], S.d["y"]
    subs = select_subjects(S, a.subjects)
    folds = loso_folds(S, subs, a.jobs)
    segs, idxs = [], []
    for si in subs:
        idx = np.where(g == si)[0]
        segs.append((folds[int(si)]["qm"], S.calib[si], S.xq[idx])); idxs.append(idx)
    hw = be.infer(segs)

    rows, k = [], 0
    sw_acc, hw_acc, sw_bal, hw_bal, agree = [], [], [], [], []
    sw_all, hw_all, y_all = [], [], []
    for si, idx in zip(subs, idxs):
        n = len(idx); h = hw["cls"][k:k + n]; s = folds[int(si)]["sk_cls"]; yy = y[idx]; k += n
        sw_acc.append((s == yy).mean()); hw_acc.append((h == yy).mean())
        sw_bal.append(balanced_accuracy_score(yy, s)); hw_bal.append(balanced_accuracy_score(yy, h))
        agree.append((h == s).mean())
        sw_all.append(s); hw_all.append(h); y_all.append(yy)
        rows.append([S.d["sids"][si], n, pct(sw_acc[-1]), pct(hw_acc[-1]), pct(agree[-1])])
    sw_all, hw_all, y_all = map(np.concatenate, (sw_all, hw_all, y_all))
    msw, mhw = metrics(sw_all, y_all), metrics(hw_all, y_all)
    summ = [["software (sklearn, per-fold retrain)", f"{pct(np.mean(sw_acc))} ± {pct(np.std(sw_acc))}",
             f"{pct(np.mean(sw_bal))} ± {pct(np.std(sw_bal))}"] + [f"{r:.3f}" for r in msw["recall"]],
            [f"hardware ({be.name}, per-fold upload)", f"{pct(np.mean(hw_acc))} ± {pct(np.std(hw_acc))}",
             f"{pct(np.mean(hw_bal))} ± {pct(np.std(hw_bal))}"] + [f"{r:.3f}" for r in mhw["recall"]]]
    md = f"""# Software vs FPGA: leave-one-subject-out accuracy

For each held-out subject, the stack is retrained in software on the other subjects
(same code path as `train_conn_model._loso_fold`). That fold's folded + quantised
weights are uploaded to the hardware, and the held-out subject's trials are streamed.
This is the generalisation comparison; the deployed model's in-sample numbers are in
comparison.md.

Model card reference (FourConnModel LOSO): acc 66.58%, bal 62.96%.

{md_table(["path", "LOSO acc (mean ± sd over folds)", "LOSO bal acc", "recall no_stim", "recall medium", "recall max"], summ)}
Class agreement hw vs sw over all held-out trials: **{pct((hw_all == sw_all).mean())}**
({int((hw_all != sw_all).sum())} of {len(sw_all)} trials differ).

## Per fold
{md_table(["held-out subject", "trials", "sw acc", "hw acc", "hw = sw"], rows)}"""
    os.makedirs(c.RESULTS_DIR, exist_ok=True)
    with open(os.path.join(c.RESULTS_DIR, "loso.md"), "w") as f:
        f.write(md)
    print(md.split("## Per fold")[0])


# ─────────────────────────────────────────────
# 3. Speed
# ─────────────────────────────────────────────
def _cpu_name():
    try:
        return subprocess.run(["sysctl", "-n", "machdep.cpu.brand_string"],
                              capture_output=True, text=True).stdout.strip() or platform.processor()
    except Exception:
        return platform.processor()


def _stats_ns(t):
    t = np.asarray(t, dtype=float)
    return {"median_us": np.median(t) / 1e3, "p99_us": np.percentile(t, 99) / 1e3, "mean_us": t.mean() / 1e3}


def run_bench(S, be, a):
    import sklearn, scipy
    from scipy.special import softmax
    X, g = S.d["X"], S.d["groups"]
    mu, sd = c.subject_stats(X, g)
    MU, SD = mu[g], sd[g]
    n = min(a.bench_trials, len(X))
    rng = np.random.default_rng(0)
    pick = rng.choice(len(X), n, replace=False)
    art = S.art
    offs = np.cumsum([0] + [S.d["mats"][f].shape[1] for f in fxp.FAMILIES])
    fams = list(enumerate(fxp.FAMILIES))

    # (a) sklearn, one trial per call (production path, incl. per-subject z-score)
    def sk_one(i):
        z = ((X[i] - MU[i]) / (SD[i] + 1e-12))[None, :]
        P = np.hstack([art["base_models"][f].predict_proba(z[:, offs[k]:offs[k + 1]]) for k, f in fams])
        return art["meta_learner"].predict_proba(P)

    # (c) lean NumPy, folded weights, one trial
    W = [S.fm["W"][f] for f in fxp.FAMILIES]; B = [S.fm["b"][f] for f in fxp.FAMILIES]
    INV = 1.0 / (SD + 1e-12); MC, MB = S.fm["mc"], S.fm["mb"]

    def np_one(i):
        z = (X[i] - MU[i]) * INV[i]
        P = np.concatenate([softmax(W[k] @ z[offs[k]:offs[k + 1]] + B[k]) for k in range(4)])
        return softmax(MC @ P + MB)

    res = {}
    for name, fn in [("sw_a_sklearn_single", sk_one), ("sw_c_numpy_single", np_one)]:
        for i in pick[:50]: fn(i)                                   # warm-up
        t = []
        for _ in range(a.bench_repeats):
            for i in pick:
                t0 = time.perf_counter_ns(); fn(i); t.append(time.perf_counter_ns() - t0)
        res[name] = _stats_ns(t)
        print(f"  {name}: median {res[name]['median_us']:.1f} us")

    # (b) sklearn batched over all trials
    def sk_batch():
        Z = (X - MU) / (SD + 1e-12)
        P = np.hstack([art["base_models"][f].predict_proba(Z[:, offs[k]:offs[k + 1]]) for k, f in fams])
        return art["meta_learner"].predict_proba(P)
    sk_batch()
    t = []
    for _ in range(max(3, a.bench_repeats)):
        t0 = time.perf_counter_ns(); sk_batch(); t.append((time.perf_counter_ns() - t0) / len(X))
    res["sw_b_sklearn_batched"] = _stats_ns(t)
    print(f"  sw_b_sklearn_batched: {res['sw_b_sklearn_batched']['median_us']:.2f} us/trial")

    # hardware
    mhz = a.clock_mhz
    si = int(g[pick[0]]); idx = np.where(g == si)[0][:min(n, 200)]
    ems_link.set_default_model(be, S.qm)
    hw = be.infer([(S.qm, S.calib[si], S.xq[idx])], progress=False)
    lat = float(np.median(hw["lat_cycles"]))
    if isinstance(be, ems_link.FpgaLink):
        r = be.rerun(1000)
        period = r["total_cycles"] / r["runs"]
        e2e = _stats_ns(hw["wall_ns"])
    else:
        per = [l for l in be.summary if l.startswith("period")]
        period = float(per[0].split("mean")[1].split()[0]) if per else lat + 1
        e2e = None
    res["hw_compute"] = {"latency_cycles": lat, "latency_us": lat / mhz,
                         "period_cycles": period, "trials_per_s": mhz * 1e6 / period}

    in_b, out_b = 1 + 4 * fxp_n_feat(S), 72
    links = [("UART 921.6 kbaud", 921_600 / 10), ("UART 3 Mbaud", 3_000_000 / 10),
             ("SPI 25 MHz", 25e6 / 8), ("SPI 50 MHz, 4-bit (QSPI)", 50e6 * 4 / 8)]
    link_rows = [[nm, f"{(in_b + out_b) / bps * 1e3:.2f} ms",
                  f"{((in_b + out_b) / bps * 1e6 + lat / mhz) / 1e3:.2f} ms"] for nm, bps in links]

    a_med = res["sw_a_sklearn_single"]["median_us"]; c_med = res["sw_c_numpy_single"]["median_us"]
    hw_us = res["hw_compute"]["latency_us"]
    rows = [
        ["SW (a) sklearn, 1 trial/call", f"{a_med:.1f}", f"{res['sw_a_sklearn_single']['p99_us']:.1f}",
         f"{1e6 / a_med:,.0f}", "1.0x", f"{c_med / a_med:.2f}x"],
        ["SW (b) sklearn, batched (per trial)", f"{res['sw_b_sklearn_batched']['median_us']:.2f}", "-",
         f"{1e6 / res['sw_b_sklearn_batched']['median_us']:,.0f}",
         f"{a_med / res['sw_b_sklearn_batched']['median_us']:.1f}x",
         f"{c_med / res['sw_b_sklearn_batched']['median_us']:.1f}x"],
        ["SW (c) NumPy folded, 1 trial/call", f"{c_med:.1f}", f"{res['sw_c_numpy_single']['p99_us']:.1f}",
         f"{1e6 / c_med:,.0f}", f"{a_med / c_med:.1f}x", "1.0x"],
        [f"HW compute ({be.name}, {mhz:.0f} MHz)", f"{hw_us:.2f}", f"{hw_us:.2f} (deterministic)",
         f"{res['hw_compute']['trials_per_s']:,.0f}", f"{a_med / hw_us:.1f}x", f"{c_med / hw_us:.1f}x"],
    ]
    if e2e:
        rows.append(["HW end-to-end over UART (host wall clock)", f"{e2e['median_us']:.0f}",
                     f"{e2e['p99_us']:.0f}", f"{1e6 / e2e['median_us']:,.0f}",
                     f"{a_med / e2e['median_us']:.3f}x", f"{c_med / e2e['median_us']:.3f}x"])

    md = f"""# Software vs FPGA: inference speed

Classifier only (1,664 features in → class out, including the per-subject
normalisation). Host: {_cpu_name()}, Python {platform.python_version()},
NumPy {np.__version__}, scikit-learn {sklearn.__version__}, SciPy {scipy.__version__}.
{n} random trials × {a.bench_repeats} repeats after warm-up.

{md_table(["path", "latency median (µs)", "p99 (µs)", "throughput (trials/s)", "speed-up vs (a)", "speed-up vs (c)"], rows)}
HW compute is measured by on-chip cycle counters: latency is first feature accepted
→ result valid ({lat:.0f} cycles), and throughput is back-to-back trials
({period:.1f} cycles/trial). Features stream at 1 per cycle, so latency is ~90% feature
ingest; the arithmetic after the last feature takes ~180 cycles.
{"Backend is the RTL simulation: cycle counts are exact, µs assume the clock above (check Fmax in the Vivado timing report)." if e2e is None else ""}

## Where end-to-end time goes (link transfer per trial: {in_b} B in + {out_b} B out)
{md_table(["link", "transfer", "transfer + HW compute"], link_rows)}
Over UART the link dominates end-to-end time. The FPGA's compute advantage only shows
end-to-end with a faster link, or when features are computed on the FPGA itself.
"""
    os.makedirs(c.RESULTS_DIR, exist_ok=True)
    with open(os.path.join(c.RESULTS_DIR, "benchmark.md"), "w") as f:
        f.write(md)
    with open(os.path.join(c.RESULTS_DIR, "benchmark.json"), "w") as f:
        json.dump({k: v for k, v in res.items()} | ({"hw_end_to_end": e2e} if e2e else {}), f, indent=2)
    print(md)


def fxp_n_feat(S):
    return S.xq.shape[1]


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--backend", choices=["rtl-sim", "fpga"], default="rtl-sim")
    ap.add_argument("--port"); ap.add_argument("--baud", type=int, default=921600)
    ap.add_argument("--agree", action="store_true"); ap.add_argument("--loso", action="store_true")
    ap.add_argument("--bench", action="store_true"); ap.add_argument("--all", action="store_true")
    ap.add_argument("--subjects", type=int, default=None, help="limit to the first N subjects")
    ap.add_argument("--jobs", type=int, default=-1, help="parallel LOSO training jobs")
    ap.add_argument("--bench-trials", type=int, default=500)
    ap.add_argument("--bench-repeats", type=int, default=3)
    ap.add_argument("--clock-mhz", type=float, default=100.0)
    a = ap.parse_args()
    if not (a.agree or a.loso or a.bench or a.all):
        ap.error("pick --agree, --loso, --bench or --all")
    S = gm.Setup()
    be = make_backend(a)
    try:
        if a.agree or a.all: print("\n=== agreement ==="); run_agree(S, be, a)
        if a.loso or a.all:  print("\n=== LOSO ===");      run_loso(S, be, a)
        if a.bench or a.all: print("\n=== speed ===");     run_bench(S, be, a)
    finally:
        if isinstance(be, ems_link.FpgaLink): be.close()
