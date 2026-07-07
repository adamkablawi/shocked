# EMS Intensity Decoding from EEG — Full Project Description

> **Purpose of this document.** A complete, self-contained description of the
> "Shocked" project: the scientific problem, every dataset variant, the
> preprocessing, the feature representations, the validation methodology, a
> detailed rundown of **every model whose results live in the repo** (baselines,
> the failed/bad runs, the best model, the deployable final model, the reduced
> montage, and the 2-class biomarker model), and the model-explainability work.
> Written so that a separate assistant — given this file plus the result files and
> figures — can reconstruct the project (a talk, a paper section, a slide deck)
> without any other context.
>
> Metrics used throughout:
> - **acc** = overall accuracy.
> - **bal** = balanced accuracy (mean per-class recall; the fair metric under
>   class imbalance).
> - **chance** = 1 / n-classes (33% for 3-class, 25% for 4-class, 50% for 2-class).
>   For imbalanced sets the **majority-class baseline** is also given (e.g. 50% for
>   the 40/80/40 3-class set, 75% for the 2-class set).
>
> All numbers below are taken directly from the saved result JSONs / MD logs.

---

## 1. The Problem

The project decodes **the intensity of an electrical muscle stimulation (EMS)
pulse from a subject's EEG brain response**. On each trial an EMS device delivers
a pulse at one of several pre-set intensities (or no pulse at all), and the scalp
EEG following stimulus onset is recorded. The core task is **multi-class
classification**: from a single trial's EEG epoch, predict which stimulation
intensity produced it. A **2-class reframing** (tolerable vs intolerable) is used
to isolate the biomarkers of high-intensity stimulation.

**Why it matters / the longer-term goal.** The intended end-application is a
**closed-loop neurofeedback system**: deliver EMS, read the cortical response,
detect a discomfort/pain threshold, and automatically stop or modulate
stimulation. Reliable *offline* decoding of intensity is the prerequisite — this
repo is the **offline decoding / modelling stage**, not the live system. (A
separate `ep_continous.py` LSL streaming scaffold exists for the eventual
real-time path, with the model hook left as a TODO.)

**Why it is hard.**
- The discriminative signal is a **stimulus-locked evoked response** — a
  somatosensory evoked potential (SEP) plus induced band-power changes — that
  scales with intensity. Neighbouring intensities produce *similar* responses, so
  errors concentrate between adjacent classes (an ordinal-confusion structure).
- **Small data per person**: ~120–160 trials per subject → high-dimensional
  feature sets overfit easily (the recurring "dilution" failure mode).
- **Large inter-subject variability**: a model trained on some people generalises
  imperfectly to a new person — a persistent **within-subject ≫ LOSO** gap.

---

## 2. The Data

### 2.1 Source recordings (`data/og/`)
- **29 subjects** (`EMS0001` … `EMS0031`, a few IDs missing).
- Per subject: `X.npy` (epochs), `y.npy` (labels), `metadata.json`.
- **60-channel** EEG, 10–10 montage (full list: `Fp1, Fz, F3, F7, FC5, FC1, C3,
  T7, CP5, CP1, Pz, P3, P7, O1, Oz, O2, P4, P8, CP6, CP2, Cz, C4, T8, FC6, FC2,
  F4, F8, Fp2, AF7, AF3, AFz, F1, F5, FT7, FC3, C1, C5, TP7, CP3, P1, P5, PO7,
  PO3, POz, PO4, PO8, P6, P2, CPz, CP4, TP8, C6, C2, FC4, FT8, F6, AF8, AF4, F2,
  FCz`).
- **Source sampling rate 1000 Hz.** Source epoch window **−2.0 s … +1.5 s**.
- **4 original classes, 40 trials each (160 trials/subject)**:
  `0 = no_stimulation`, `1 = min_intensity`, `2 = medium_intensity`,
  `3 = max_intensity`.

### 2.2 Preprocessing pipeline (`data/dataprep.py` and variants)
Every modelling-ready `.npz` is produced from the source trio by:
1. **Anti-aliased downsampling 1000 → 250 Hz** (factor-4 FIR decimation,
   `scipy.signal.decimate`, zero-phase).
2. **Crop to −0.2 s … +1.5 s** → **425 samples** (keeps a 200 ms pre-stim baseline).
3. **Class handling** — the only thing that distinguishes the dataset variants (2.3).
4. Cast `float32`, save `.npz` with `X (n_trials, 60, 425)`, `y`, `sfreq=250`,
   `channel_names`, `class_names`, `epoch_tmin=-0.2`, `epoch_tmax=1.5`.

Prep scripts, one per class scheme:
- `data/dataprep.py` — 4-class (keep all) and 3-class 40/80/40 (merge min→medium).
- `data/dataprep_2class_tolerance.py` — **2-class** tolerable/intolerable (new).
- (`dataprep_3class_balanced.py` — 40/40/40; a transient script, see 2.3.)

> At the *modelling* stage, further per-trial conditioning happens inside the
> feature extractors (baseline subtraction, band-pass/Hilbert, per-subject
> z-scoring). The real-time scaffold additionally does detrend + band-pass + notch
> + common-average-reference, but the offline `.npz` sets are the basis for all
> results here.

### 2.3 The dataset variants (the "splits")
All are 60-channel, 250 Hz, −0.2…1.5 s, 425 samples; they differ only in how the
four original classes are mapped:

| Dataset folder | Classes | Per-subject split | Balance | How it's built |
|---|---|---|---|---|
| `data/og-ds-t-4c` | **4** — no_stim / min / medium / max | 40 / 40 / 40 / 40 | balanced (25% chance) | keep all four (`dataprep.py`) |
| `data/og-ds-t-3c` | **3** — no_stim / **medium** / max | **40 / 80 / 40** | imbalanced 25/50/25 | **min merged into medium** (so "medium" = min+medium) |
| `data/og-ds-t-3c-bal` | **3** — min / medium / max | 40 / 40 / 40 | balanced (33% chance) | **no_stim dropped**, relabel 0/1/2 |
| `data/og-ds-t-2c-tol` | **2** — **tolerable** / **intolerable** | **120 / 40** | imbalanced 75/25 | **bottom three merged → tolerable; max → intolerable** (`dataprep_2class_tolerance.py`) |

**Interpretation notes:**
- **`og-ds-t-3c` (40/80/40)** is the project's **primary** 3-class set (most models
  reported on it). Imbalanced 25/50/25 → read raw accuracy against a **50%
  majority baseline**; **balanced accuracy** is the honest number vs 33% chance.
- **`og-ds-t-3c-bal` (40/40/40)** isolates the *pure intensity* question. **Note:
  this folder is regenerated on demand and is frequently absent from disk** — its
  result JSON (`Results/LDA_3c_bal/LDA_3c_bal.json`) persists even when the `.npz`s
  are gone. Regenerate with `dataprep_3class_balanced.py` if needed.
- **`og-ds-t-4c`** is the hardest (four graded levels, 25% chance).
- **`og-ds-t-2c-tol`** frames the *safety-relevant* question — "is this stimulation
  intolerable (high) or not?" — to surface the biomarkers of intolerable EMS.
  Imbalanced 75/25 → **majority baseline 75%**, so balanced accuracy / ROC-AUC are
  the metrics; imbalance is handled at the classifier (see 5.10).

---

## 3. Feature Representations (the "feature families")

A **modular feature pipeline** (`ModularFeatureExtractor`) concatenates any set of
sklearn-compatible extractors. Four families exist, each usable on any channel
subset (`all60`, `sensorimotor`, `central_fc`, or `custom`):

### 3.1 `erp` — ERP / SEP time-domain (`erp_features.py`)
Per-channel evoked-potential features (default central/fronto-central channels
`C3, Cz, C4, FCz, FC1, FC2, FC3, FC4`). The `"full"` set:
- **peak**: neg-peak amp & latency (0.10–0.20 s), pos-peak amp & latency
  (0.20–0.30 s), peak-to-peak (5/ch).
- **window**: mean amplitude in bins 0.10–0.18, 0.20–0.28, 0.28–0.40 s (3/ch).
- **baseline**: pre-stim mean, pre-stim SD, post-minus-baseline shift (3/ch).
- **shape**: rectified AUC, rising-edge slope (2/ch).
Per-trial baseline-corrected over −0.2…0 s. (60-ch full ≈ 104 features on the 8
default channels; on all60 it uses the 8 central by default.)

### 3.2 `bp` — band-power / spectral (`bandpower_features.py`)
**Log Welch power per channel per band**, whole epoch. Bands: delta (1–4), theta
(4–8), alpha (8–13), beta (13–30), gamma (30–45) Hz. `all60` → 5×60 = **300
features**. Project uses **absolute** log power (relative was tested, worse).

### 3.3 `tf` — time-frequency ERD/ERS (`tf_features.py`)
Event-related desync/sync (Pfurtscheller), via robust filter–Hilbert in dB. Per
channel per band: early-window mean dB (0–0.30 s), late-window mean dB (0.30–1.50
s), peak-ERD (min dB), peak-ERS (max dB). `all60` → 4×5×60 = **1200 features**.
**Least useful family on its own** (see bad runs) — but contributes in the stack.

### 3.4 `riem` — Riemannian covariance / tangent-space (`riemann_features.py`)
Each trial → channel×channel covariance (OAS-regularised) → tangent-space
projection at the geometric mean → flat vector, each dim an electrode pair. `all60`
→ 60×61/2 = **1830 features**. Captures *spatial coupling* the per-channel families
discard. **Weak as a standalone block, valuable as a stacking base model.**

---

## 4. Validation Methodology

Two leakage-safe schemes reported for (almost) every model:
- **Within-subject**: per subject, **RepeatedStratifiedKFold** (5 splits × 5
  repeats). The ceiling with per-person calibration data.
- **LOSO (Leave-One-Subject-Out)**: train on 28, test on the held-out subject,
  rotate. **The deployment metric** (generalisation to a new person). Features are
  per-subject z-scored before pooling.

Standard pieces:
- Base classifier: **shrinkage LDA** (`solver='lsqr', shrinkage='auto'`,
  Ledoit-Wolf) — a regulariser for high-dimensional, collinear EEG features.
- **Artifact filter**: trials whose pre-stim baseline SD is a per-subject outlier
  (z > 3) are dropped (~1–2%).
- Pipelines refit inside every fold (no feature/scaler leakage).
- **Recurring finding:** within-subject ≫ LOSO by ~8–12 pts everywhere →
  inter-subject variability is the dominant limit.
- **Parallelism (newer models):** the `FinalModel/` and `XonModel/` scripts run
  feature extraction and the CV folds across cores with `joblib` (path-based
  loading, so raw arrays never hit temp). At 7 channels the within-subject phase
  that took ~2 h at 60 ch runs in ~20 s.

---

## 5. The Models & Results

### 5.0 Quick scoreboard (LOSO = headline generalisation metric)

| Model | Dataset | Within acc/bal | LOSO acc/bal | Notes |
|---|---|---|---|---|
| **Stack (4-family) — BEST** | 3c 40/80/40 | **73.0 / 70.2** | **66.7 / 63.0** | erp+bp+tf+riem, meta-learner (5.8) |
| **Final deployable model** | 3c 40/80/40 | — | 66.7 / 63.0 | same stack fit on all 29 subj, saved to disk (5.9) |
| **Stack, 7-channel (XON)** | 3c 40/80/40 | 69.1 / 65.4 | 64.0 / 59.8 | 7 electrodes, ~294 features (5.11) |
| LDA erp+bp (primary baseline) | 3c 40/80/40 | 71.1 / 70.3 | 62.8 / 59.9 | reference (5.1) |
| LDA erp+bp, 7-channel (central) | 3c 40/80/40 | 68.7 / 67.7 | 63.1 / 59.4 | BEST_CHANNELS montage (5.2) |
| EEGNet | 3c 40/80/40 | 63.4 / 64.7 | 59.8 / 60.8 | deep net, all 60 ch (5.5) |
| LDA erp+bp (balanced) | 3c 40/40/40 | 69.0 / 69.0 | 58.0 / 58.1 | pure intensity (5.3) |
| **Stack — tolerable vs intolerable** | 2c 120/40 | 87.3 / 86.4 | 79.9 / 79.9 | ROC-AUC 0.94/0.88; biomarkers (5.10) |
| LDA erp+bp combined | 4c | 61.6 / 61.6 | 48.7 / 48.7 | four levels, 25% chance (5.4) |
| LDA erp+bp, 7-channel | 4c | 57.2 | 47.3 | (5.4) |
| EEGNet | 4c | 53.0 | 49.7 / 49.7 | (5.5) |
| *bad:* erp+bp+**tf** concat | 3c 40/80/40 | 64.6 | 57.4 | tf concatenation dilutes (5.6a) |
| *bad:* **riem only** | 3c 40/80/40 | 67.9 / 63.3 | 57.5 / 55.1 | covariance alone weaker (5.6b) |
| *bad:* erp+bp+riem concat | 3c 40/80/40 | 72.0 / 68.3 | 59.7 / 58.1 | concatenation dilutes LOSO (5.6b) |
| *bad:* XON channels, plain LDA | **4c** | 54.8 | 46.9 | old run; superseded by 5.11 (5.6c) |
| *failed:* nested-CV feature selection | 3c 40/80/40 | — | best bal 60.1 | could not beat erp+bp (5.7) |

---

### 5.1 PRIMARY BASELINE — 3-class LDA, erp+bp, 40/80/40
**Files:** `Results/LDA_3c/3c/LDA_td+fd_3c.json` (+ `importance_3c/`, `trends_3c/`).
**Config:** erp (full) + bp (all60), dataset `og-ds-t-3c`.

| Validation | acc | bal | chance |
|---|---|---|---|
| within | 71.1% | 70.3% | 33% |
| LOSO | 62.8% | 59.9% | 33% |

The reference "time-domain + frequency-domain" decoder (~2× chance). erp+bp beats
either family alone (4-class ablation, 5.4). This is the baseline every other
approach is measured against.

**Feature importance** (`importance_3c/`, 404 features over 29 LOSO folds):
- ANOVA F-score top: `erp:peak_to_peak@Cz`, `@FCz`, `@FC2`, `erp:rise_slope@FC2`,
  `erp:auc_rect@Cz` — **central/fronto-central ERP amplitude & latency**.
- Fold-stable LDA weight top: `erp:post_minus_base@C4`, `erp:mean_020_028@C4`,
  **`bp:gamma@Fz`**, `erp:peak_to_peak@Cz`, **`bp:gamma@C2`** — central ERP
  amplitude **plus gamma-band power**.
- Figures: `signature_bandpower_3c.png` (gamma stands out), `top_features_3c.png`.

**Feature trends** (`trends_3c/`): the top fold-stable features (`post_minus_base@C4`,
`mean_020_028@C4`, `bp:gamma@Fz`, `peak_to_peak@Cz`, …) scale monotonically across
no_stim → medium → max (real dose-response). Figure `feature_trends_3c.png`.

---

### 5.2 REDUCED 7-CHANNEL BASELINE — 3-class LDA, erp+bp
**File:** `Results/LDA_3c/3c/LDA_7ch_3c.json`. **Config:** 5.1 restricted to
`BEST_CHANNELS = [FCz, C4, Fz, FC4, Cz, C2, FC2]` (top central/fronto-central
electrodes from the importance analysis).

| Validation | acc | bal |
|---|---|---|
| within | 68.7% | 67.7% |
| LOSO | 63.1% | 59.4% |

Dropping 60→7 channels costs ~2.4 pts within and **LOSO is essentially unchanged**
(63.1 vs 62.8) — the deployable-montage argument. (Superseded as best 7-channel
model by the XON *stack*, 5.11.)

---

### 5.3 BALANCED 3-class LDA — 40/40/40 (no_stim removed)
**File:** `Results/LDA_3c_bal/LDA_3c_bal.json`. **Config:** erp+bp (all60),
dataset `og-ds-t-3c-bal`.

| Validation | acc | bal |
|---|---|---|
| within | 69.0% | 69.0% |
| LOSO | 58.0% | 58.1% |

Removing `no_stimulation` isolates the **pure graded-intensity** question. Only a
modest drop vs the 40/80/40 set even without the easy class → the decoder genuinely
separates intensity *levels*, not just stim-vs-no-stim. Balanced, so raw accuracy
is directly interpretable vs 33% chance.

---

### 5.4 4-class LDA — all four intensities
**Files:** `Results/LDA_4c/LDA_td+fd_4c.json`, `LDA_7ch_4c.json` (+ `importance_4c/`,
`trends_4c/`). **Dataset:** `og-ds-t-4c` (balanced, 25% chance).

Family ablation (all60):

| Feature set | within | LOSO |
|---|---|---|
| erp only | 50.8% | 44.8% |
| bp only | 58.0% | 44.2% |
| **erp + bp** | **61.6%** | **48.7%** |

7-channel: within 57.2%, LOSO 47.3%. The hardest task; erp+bp still ~2× chance
within. 4-class importance leans more on **gamma band-power** (`bp:gamma@Fz`,
`bp:gamma@C2`, `bp:delta@C6` top the fold-stable weights).

---

### 5.5 EEGNet (deep-learning baseline) — 3-class & 4-class
**Files:** `Results/EEGNet_3c.md`, `EEGNet_4c.md`. **Model:** EEGNet-8,2 (Lawhern
2018), inline in `Models/EEGNet/train_eegnet.py`. Raw 60-ch epochs, kernel 500 ms,
F1/D/F2 = 8/2/16, per-channel z-score, balanced loss, early stopping.

- **3-class:** within acc 63.4% / bal 64.7%; LOSO acc 59.8% / bal 60.8% (range
  41.9–72.5%). Per-class recall (LOSO): no_stim 0.71, medium 0.57, max 0.55.
- **4-class:** within 53.0%; LOSO 49.7% / 49.7% (range 28.1–70.6%). Recall: no_stim
  0.68, min 0.41, medium 0.34, max 0.55 (classic ordinal pattern).

**Message:** EEGNet does **not** beat the hand-crafted LDA features. On 3-class it
ties on LOSO (60.8 bal vs 59.9) but is lower within; on 4-class it's similar. With
~120–160 trials/subject the deep net has no data advantage.

---

### 5.6 BAD RUNS — tested and rejected
**Folder:** `Results/LDA_3c/bad_runs/`.

**(a) tf concatenation — `LDA_w_tf.json`.** erp+bp+tf: within 64.6%, LOSO 57.4% —
*worse* than erp+bp. The 1200 tf features **dilute** the model.
(`importance_w_tf/`, `trends_w_tf/` confirm tf rarely ranks near the top.) Lesson:
the time-frequency domain is less discriminative than time or frequency alone
*when concatenated*.

**(b) Riemannian alone & concatenated — `riemann_3c/riemann_comparison_3c.json`.**

| Feature set | within | LOSO |
|---|---|---|
| baseline erp+bp | 71.1 / 70.3 | 62.8 / 59.9 |
| riem only | 67.9 / 63.3 | 57.5 / 55.1 |
| erp+bp+riem concat | 72.0 / 68.3 | 59.7 / 58.1 |

Riem alone is weaker, and concatenating hurts LOSO (dilution). Conclusion *at this
stage*: "Riemann doesn't help." **Overturned by stacking (5.8)** — riem is a poor
feature block but a useful, complementary ensemble member.

**(c) XON channel set (plain LDA) — `LDA_XONCh_3c.json`.** A **4-class** plain
erp+bp LDA on `XON_CHANNELS = [F3, F4, C3, Cz, C4, P3, P4]`: within 54.8%, LOSO
46.9% (chance 25%). Filed as "poor channel choice" at the time. **Important
correction:** this was a *single LDA on the hardest (4-class) task*. With the
**stacking** architecture on the 3-class task, the *same* XON montage performs
near the full 60-channel model (see **5.11**) — so XON is a viable reduced montage;
the old number reflected the model+task, not the electrodes.

---

### 5.7 FAILED — nested-CV cross-family feature selection
**Folder:** `Results/LDA_3c_Best_FT/` (`feature_selection.json`, `accuracy_vs_k.png`).
*(Previously under `Models/LDA Best Ft (failed)/`; the results now live here.)*

**Idea:** curate the best features across erp+bp+tf (1604-feature pool) inside
nested LOSO (rank on train fold only). Selectors:
- **fscore**: best LOSO bal **60.1%** at k=300.
- **mrmr** (relevance − redundancy): best **59.3%** at k=300.
- full 1604-pool: 56.7% (confirms dilution). erp+bp baseline: **59.9%**.

**Result: could NOT beat erp+bp** (60.1 vs 59.9 = a tie in ±11% fold noise). The
"best" sets are large and tf-heavy — selection just rediscovers erp+bp-like
features. Lesson: the answer is not a cleverer subset of one concatenated vector —
it's a different *architecture* (stacking).

---

### 5.8 BEST MODEL — Per-family LDA Stacking
**Folder:** `Models/LDA-Stacking/` (`results/stacking.json`, `confusion.png`).

**Architecture.** One shrinkage-LDA **per family** (erp, bp, tf, riem); fuse their
class-probability outputs with a multinomial-logistic **meta-learner**. Each base
model stays low-dimensional relative to its family; the meta-learner *learns how
much to trust each*, so weak-but-complementary views (tf, riem) add signal instead
of diluting. Leakage-safe: out-of-fold base probabilities (inner GroupKFold over
train subjects for LOSO; inner StratifiedKFold over trials for within) train the
meta-learner; the held-out subject/rows never enter a base or meta fit.

**Dataset:** `og-ds-t-3c` (40/80/40).

| Validation | acc | bal | chance |
|---|---|---|---|
| within | **73.0%** | **70.2%** | 33% |
| LOSO | **66.7%** | **63.0%** | 33% |

**vs erp+bp baseline (62.8 / 59.9 LOSO): +3.9 acc / +3.1 bal — the only approach
that beats erp+bp.**

**Meta-weights:** within erp 0.29 / bp 0.31 / riem 0.24 / tf 0.16; LOSO erp 0.37 /
bp 0.32 / riem 0.20 / tf 0.11. **Per-class recall (LOSO):** no_stim 0.53, medium
0.78, max 0.58.

**Why it works (the key story):** families that **dilute** when concatenated help
when **fused at the decision level**, because their errors are **decorrelated** —
riem = spatial coupling, tf = ERD/ERS timing, different *views* of the same
response. Ensembling rewards complementary (not individually-better) base models.
This **rehabilitates Riemannian features** (weight 0.20–0.24). The gain concentrates
in **LOSO**, doing no harm within-subject.

> Honesty caveat: the +3 pt LOSO gain is smaller than the between-fold SD (±11–13%)
> — a consistent *directional* improvement, not a proven-significant one on 29
> subjects. A paired per-fold test is the next step.

---

### 5.9 FINAL DEPLOYABLE MODEL — trained on all subjects, saved to disk
**Folder:** `FinalModel/` — `train_final_model.py`, plus self-contained
`features/` + `train_combined.py`. **Saved artifacts (in the same folder):**
- `final_stacking_ensemble.joblib` (~39 MB) — the fitted model + all weights: the
  four base pipelines (StandardScaler + shrinkage-LDA) **and** the trained logistic
  meta-learner, self-describing (families, feature config, class names, an
  inference note).
- `model_card.json` — config + LOSO metrics.

**What it is.** The **same 4-family stack as 5.8**, but fit on **all 29 subjects**
to produce a deployable model (the LOSO run is only for the performance estimate).
Config: `og-ds-t-3c`, erp+bp+tf+riem, default priors, meta LR C=1.0.

- **LOSO estimate:** acc 66.7% / bal 63.0% (reproduces 5.8 exactly). Recall no_stim
  0.53 / medium 0.78 / max 0.58. Meta-weights erp 0.37 / bp 0.32 / riem 0.20 / tf 0.11.
- **Runtime (parallel, 4 cores):** ~31 s extraction + ~6.4 min LOSO.
- **Inference recipe** (stored in the artifact): extract the same 4 families per
  epoch → per-subject z-score → each base model's `predict_proba` → hstack in
  family order → `meta_learner.predict`.

---

### 5.10 2-CLASS BIOMARKER MODEL — tolerable vs intolerable
**Folder:** `Models/LDA-Stacking-2c/` (`stacking.py`, `feature_analysis_2c.py`).
**Results:** `Results/LDA_2c/` (`stacking_2c.json`, `feature_analysis_2c.json`,
`confusion_2c.png`, `signature_bandpower_2c.png`, `top_features_2c.png`).
**Dataset:** `og-ds-t-2c-tol` (tolerable 120 / intolerable 40, imbalanced 75/25).

**Purpose.** Reframe the task as "is the stimulation intolerable (high) or not?"
to surface the biomarkers of intolerable EMS — supports the closed-loop
discomfort-detection goal (and a collaborator's analysis).

**Imbalance handling** (the two treatments requested):
- **Option 1 — measure honestly:** balanced accuracy, per-class recall, confusion,
  **ROC-AUC + PR-AUC** for the positive (intolerable) class; raw accuracy shown
  against the 75% majority baseline.
- **Option 2 — de-bias:** base LDAs use **uniform priors [0.5, 0.5]**; meta-learner
  uses **`class_weight='balanced'`**.

**Results (4-family stack):**

| Validation | acc | bal | ROC-AUC | PR-AUC | intolerable recall |
|---|---|---|---|---|---|
| within | 87.3% | 86.4% | 0.943 | 0.874 | 0.845 |
| LOSO | 79.9% | 79.9% | 0.875 | 0.733 | 0.799 |

Majority baseline 75%. **The minority class is genuinely detected** (intolerable
recall ~0.80 LOSO, ~equal to tolerable) — the de-biasing worked; Option 3
(threshold/resampling) was not needed. Meta-weights (LOSO): erp 0.38 / bp 0.30 /
riem 0.20 / tf 0.12.

**Biomarkers of intolerable stimulation** (`feature_analysis_2c.json`, direction =
standardized diff, **+ = elevated in intolerable**):
- Most discriminable: **`erp:peak_to_peak@Cz` (+0.86)** — a larger central evoked
  potential; also `erp:peak_to_peak@FC2/@FCz`, `erp:auc_rect@Cz` (+0.70).
- What the model relies on: **`bp:gamma@C2` (+0.53)`, `bp:gamma@Fz` (+0.62)** —
  **elevated fronto-central gamma-band power.**
- Trace coefficient on the "intolerable" vote: erp 1.38 > bp 1.20 > riem 0.78 > tf
  0.45 — the SEP and gamma experts drive the intolerable decision.
- **Conclusion:** intolerable EMS is marked by a **larger central SEP** and
  **elevated fronto-central gamma power** — both known to scale with stimulus
  intensity. Figures: `top_features_2c.png` (red = elevated in intolerable),
  `signature_bandpower_2c.png`.

---

### 5.11 REDUCED 7-CHANNEL STACK — XON montage (rehabilitates 5.6c)
**Folder:** `XonModel/` — `stacking_xon.py` (standard within+LOSO),
`run_xon_loso.py` (LOSO-only), `xon_stacking.json`. **Montage:** the 7 XON
channels `F3, F4, C3, Cz, C4, P3, P4`. **Dataset:** `og-ds-t-3c`. Stats only — no
model weights saved.

**What changed vs 5.6c.** Same architecture as the best model (4-family stack), but
every family restricted to the 7 XON channels → tiny feature sets (erp 91, bp 35,
tf 140, riem 28 = **294 features**, vs 3434 at 60 ch).

| Validation | acc | bal | recall (no_stim/med/max) |
|---|---|---|---|
| within | 69.1% | 65.4% | 0.50 / 0.80 / 0.66 |
| LOSO | 64.0% | 59.8% | 0.47 / 0.77 / 0.55 |

**Key result:** a **12× channel reduction** costs only ~2.7 acc / ~3.2 bal vs the
full-montage stack (66.7 / 63.0) — you keep **~91% of cross-subject balanced
accuracy on 7 electrodes.** The meta-learner re-balances for the reduced montage:
riem rises to ~0.26 (its 28-feature covariance is now clean/low-dim), tf/bp drop
(within erp 0.31 / bp 0.28 / riem 0.27 / tf 0.15; LOSO erp 0.38 / riem 0.26 / bp
0.19 / tf 0.18). This is why keeping the full 4-family stack (not hand-picking one
family) preserves fidelity — and it **corrects the "XON is a poor montage"
conclusion** from 5.6c (which was a plain LDA on the harder 4-class task).

---

### 5.12 EXPLAINABILITY — analytic trace of the stack
**Doc:** `STACKING_TRACE.md` (neuroscience-rooted write-up of the 3-class best
model's decision process).

Because the stack is **two linear layers** (per-family LDA → logistic meta-learner),
a prediction decomposes **exactly** — no SHAP/sampling needed. The trace shows:
- **Layer 2 (trust):** meta-weights erp 0.37 / bp 0.32 / riem 0.20 / tf 0.11, and
  a **class-specific** "self-vote" structure — `no_stim` decided by erp (+1.73) &
  bp (+1.41); `max` by bp/gamma (+1.48); `medium` gets only weak votes from every
  family (why the middle class is hardest — the trace makes the difficulty visible).
- **Layer 1 (evidence):** each base LDA keys to distinct, physiologically-grounded
  generators — erp → central SEP amplitude (C4/Cz/FCz), bp → fronto-central gamma,
  tf → sensorimotor ERD, riem → spatial covariance. Barely-overlapping → complementary.
- **Backtrack audit:** any prediction back-substitutes to specific channels/bands/
  latencies → the neural generator behind each vote. A worked trial shows a weak
  expert (tf) confidently wrong being overruled by the reliable, decorrelated
  experts — the stacking thesis in one example.

**Takeaway:** the ensemble is a **glass box** (linear weighting of named neural
markers), the weighting choices map to known intensity-coding physiology, and every
decision is auditable to neural generators — the same scientific footing that
justifies the erp/bp features, extended to the whole stack.

---

## 6. Overarching Narrative

1. **Problem:** decode graded EMS intensity from single-trial EEG; end goal is a
   closed-loop discomfort-aware stimulator.
2. **Data:** 29 subjects, 60-ch, 250 Hz, −0.2…1.5 s; four class framings (4-class;
   3-class 40/80/40 with no_stim; 3-class 40/40/40 balanced; 2-class
   tolerable/intolerable).
3. **Representations:** ERP/SEP + band-power are the workhorse; ERD/ERS and
   Riemannian covariance are complementary views.
4. **Baseline:** shrinkage-LDA on erp+bp decodes ~2× chance (3-class LOSO ~60%
   bal), with 7-channel versions nearly as good.
5. **What didn't work:** tf concatenation, riem alone/concatenated, and nested-CV
   feature selection all fail to beat erp+bp — **dilution** (too many features for
   ~120 trials/subject) is the recurring failure mode of single-vector approaches.
6. **What did work — the answer is architecture, not more features:**
   **decision-level stacking** of per-family LDAs fuses the complementary views
   without dilution → **best model (LOSO 66.7 / 63.0 bal, +3 over baseline)**, and
   it rehabilitates Riemannian features. Packaged as a **deployable saved model**.
7. **Deployment angles:** a **7-channel XON stack** keeps ~91% of the accuracy for
   a realistic headset; a **2-class tolerable/intolerable** model (imbalance-handled)
   hits **LOSO ROC-AUC 0.88** and surfaces the **biomarkers of intolerable EMS**
   (larger central SEP + elevated fronto-central gamma).
8. **Explainability:** the stack is a linear glass box — its weights map to known
   intensity-coding physiology and every decision traces to neural generators.
9. **The persistent limit:** within-subject ≫ LOSO everywhere → the real frontier
   is **inter-subject variability** (cross-subject domain alignment), not more
   features.

---

## 7. File Map

```
PROJECT_OVERVIEW.md                      # this document
STACKING_TRACE.md                        # explainability / analytic trace (5.12)

Results/
  EEGNet_3c.md / EEGNet_4c.md            # EEGNet within + LOSO logs (5.5)
  LDA_3c/3c/
    LDA_td+fd_3c.json                    # PRIMARY erp+bp baseline (5.1)
    LDA_7ch_3c.json                      # 7-channel central baseline (5.2)
    importance_3c/  trends_3c/           # feature importance + dose-response
  LDA_3c/bad_runs/
    LDA_w_tf.json                        # erp+bp+tf, diluted (5.6a)
    riemann_3c/riemann_comparison_3c.json# riem alone / concat (5.6b)
    LDA_XONCh_3c.json                    # XON plain LDA, 4-class (5.6c)
    importance_w_tf/  trends_w_tf/  erd_ers_plot.py
  LDA_3c_bal/LDA_3c_bal.json             # balanced 40/40/40 (5.3)
  LDA_3c_Best_FT/                        # FAILED feature selection (5.7)
    feature_selection.json  accuracy_vs_k.png
  LDA_4c/
    LDA_td+fd_4c.json  LDA_7ch_4c.json   # 4-class ablation + 7ch (5.4)
    importance_4c/  trends_4c/
  LDA_2c/                                # 2-class tolerable/intolerable (5.10)
    stacking_2c.json  feature_analysis_2c.json
    confusion_2c.png  signature_bandpower_2c.png  top_features_2c.png

Models/
  LDA/                                   # modular LDA pipeline + 4 feature extractors
  EEGNet/                                # EEGNet trainer (5.5)
  LDA-Stacking/                          # BEST 3-class stack (5.8)
    results/stacking.json  confusion.png
  LDA-Stacking-2c/                       # 2-class biomarker stack (5.10)
    stacking.py  feature_analysis_2c.py

FinalModel/                              # DEPLOYABLE final model (5.9)
  train_final_model.py  features/  train_combined.py
  final_stacking_ensemble.joblib         # <-- saved model + weights
  model_card.json

XonModel/                                # 7-channel XON stack (5.11)
  stacking_xon.py  run_xon_loso.py  xon_stacking.json

data/
  og/                                    # raw 1000 Hz source trios (29 subjects)
  og-ds-t-4c/                            # 4-class balanced
  og-ds-t-3c/                            # 3-class 40/80/40 (PRIMARY)
  og-ds-t-3c-bal/                        # 3-class 40/40/40 (transient; often empty)
  og-ds-t-2c-tol/                        # 2-class tolerable/intolerable
  dataprep.py                            # 4-class + 3-class 40/80/40
  dataprep_2class_tolerance.py           # 2-class prep
```

> Notes: (1) `og-ds-t-3c-bal` is regenerated on demand and is frequently absent
> from disk — its result JSON persists regardless. (2) The best model exists in two
> places: `Models/LDA-Stacking/` (validation) and `FinalModel/` (the fitted,
> saved-to-disk deployable version). (3) The XON stack (5.11) supersedes the "bad"
> XON run (5.6c) — same electrodes, better model and task.
