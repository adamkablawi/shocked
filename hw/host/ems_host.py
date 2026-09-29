"""
ems_host.py
===========
Run the FPGA classifier from a host PC.

  # smoke test: upload a subject's calibration, classify its trials, check vs the
  # bit-accurate model
  python hw/host/ems_host.py --port /dev/tty.usbserial-XXXX --subject EMS0001 --trials 20

  # live use (closed loop), from Python:
  from ems_host import EmsClassifier
  clf = EmsClassifier("/dev/tty.usbserial-XXXX")
  clf.calibrate(calib_epochs, meta)      # (n, 60, 425) epochs from a calibration block
  cls, probs = clf.classify(epoch, meta) # one (60, 425) epoch -> class, 3 probabilities

Feature extraction runs on the host with the exact extractors the model was trained
with (FinalModels/FourConnModel/features). The FPGA does normalisation → 4 LDAs →
softmax → meta-learner.

Calibration note: training z-scored each subject over ALL their trials (every
intensity), so the calibration block should contain a similar mix of intensities.
"""
from __future__ import annotations
import os, sys, argparse
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))
import common as c          # noqa: E402
import fxp                  # noqa: E402
import ems_link             # noqa: E402

CLASS_NAMES = ["no_stimulation", "medium_intensity", "max_intensity"]


def extract_features(X, meta):
    """Raw epochs (n, 60, 425) µV -> (n, 1664) features in FPGA stream order."""
    from train_combined import ModularFeatureExtractor
    X = np.asarray(X, dtype=float)
    if X.ndim == 2:
        X = X[None]
    opts = c.tcm.CONFIG["feature_opts"]
    return np.hstack([ModularFeatureExtractor([f], opts).set_meta(meta).fit_transform(X)
                      for f in fxp.FAMILIES])


class EmsClassifier:
    def __init__(self, port, baud=921600, upload_model=True):
        self.link = ems_link.FpgaLink(port, baud)
        if upload_model:        # make sure the board runs the exported model
            self.link.upload_model(fxp.quantize_model(fxp.fold_model(c.load_model())))
        self.calib = None

    def calibrate_features(self, F):
        """F: (n, 1664) raw features from a calibration block."""
        self.calib = fxp.quantize_calib(F.mean(0), F.std(0))
        self.link.upload_calib(self.calib)

    def calibrate(self, epochs, meta):
        self.calibrate_features(extract_features(epochs, meta))

    def classify_features(self, f):
        r = self.link.run(fxp.quantize_x(np.asarray(f)))
        return r["cls"], np.array(r["probs"]) / (1 << fxp.P_FRAC), r

    def classify(self, epoch, meta):
        return self.classify_features(extract_features(epoch, meta)[0])

    def close(self):
        self.link.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", required=True)
    ap.add_argument("--baud", type=int, default=921600)
    ap.add_argument("--subject", default="EMS0001")
    ap.add_argument("--trials", type=int, default=20)
    a = ap.parse_args()

    d = c.load_features()
    si = d["sids"].index(a.subject)
    idx = np.where(d["groups"] == si)[0]
    F = d["X"][idx]

    clf = EmsClassifier(a.port, a.baud)
    clf.calibrate_features(F)
    qm = fxp.quantize_model(fxp.fold_model(c.load_model()))
    ref = fxp.infer_q(fxp.quantize_x(F), *(np.broadcast_to(v, F.shape) for v in clf.calib), qm)

    ok = 0
    for t in range(min(a.trials, len(idx))):
        cls, probs, r = clf.classify_features(F[t])
        match = (cls == ref["cls"][t]) and tuple(r["probs"]) == tuple(ref["probs"][t])
        ok += match
        print(f"trial {t:3d}: true {CLASS_NAMES[d['y'][idx[t]]]:<16} fpga {CLASS_NAMES[cls]:<16} "
              f"p=[{', '.join(f'{p:.3f}' for p in probs)}]  {r['lat_cycles']} cycles  "
              f"{r['wall_ns'] / 1e6:.1f} ms round-trip  {'OK' if match else 'MISMATCH vs model'}")
    n = min(a.trials, len(idx))
    print(f"\n{ok}/{n} trials bit-exact with the fixed-point model")
    r = clf.link.rerun(1000)
    print(f"on-chip: latency {r['lat_cycles']} cycles, "
          f"{r['total_cycles'] / r['runs']:.1f} cycles/trial back-to-back")
    clf.close()
    sys.exit(0 if ok == n else 1)


if __name__ == "__main__":
    main()
