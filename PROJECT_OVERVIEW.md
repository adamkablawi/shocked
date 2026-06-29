# EMS Intensity Decoding from EEG — Full Project Description

> **Purpose of this document.** This is a complete, self-contained description of
> the "Shocked" project: the scientific problem, every dataset variant, the
> preprocessing, the feature representations, the validation methodology, and a
> detailed rundown of **every model whose results live in the repo** (including
> the failed/bad runs and the current best model). It is written so that a
> separate assistant — given this file plus the result files and figures — can
> restructure or rebuild a PowerPoint without needing any other context.
>
> All accuracy numbers below are taken directly from the saved result JSONs / MD
> logs in the repo. Two metrics are reported throughout:
> - **acc** = overall accuracy.
> - **bal** = balanced accuracy (mean per-class recall; the fair metric when
>   classes are imbalanced).
> - **chance** = 1 / number-of-classes (33% for 3-class, 25% for 4-class).

---

## 1. The Problem

The project decodes **the intensity of an electrical muscle stimulation (EMS)
pulse from a subject's EEG brain response**. On each trial an EMS device delivers
a pulse at one of several pre-set intensities (or no pulse at all), and the
scalp EEG following stimulus onset is recorded. The task is a **multi-class
classification**: given a single trial's EEG epoch, predict which stimulation
intensity produced it.

**Why it matters / the longer-term goal.** The intended end-application is a
**closed-loop neurofeedback system**: deliver EMS, read the cortical response in
real time, detect a discomfort/pain threshold, and automatically stop or modulate
stimulation. Reliable *offline* decoding of intensity from EEG is the prerequisite
for that loop — this repo is the **offline decoding / modelling stage**, not the
live system. (A separate `ep_continous.py` LSL streaming scaffold exists for the
eventual real-time path, with the model hook left as a TODO.)

**Why it is hard.**
- The discriminative signal is a **stimulus-locked evoked response** — a
  somatosensory evoked potential (SEP) plus induced band-power changes — that
  scales with intensity. Neighbouring intensities produce *similar* responses, so
  errors concentrate between adjacent classes (an ordinal-confusion structure).
- **Small data per person**: ~120–160 trials per subject. This makes
  high-dimensional feature sets prone to overfitting.
- **Large inter-subject variability**: a model trained on some people generalises
  imperfectly to a new person. This shows up as a persistent gap between
  *within-subject* and *cross-subject (LOSO)* accuracy throughout the project.

---

## 2. The Data

### 2.1 Source recordings (`data/og/`)
- **29 subjects** (`EMS0001` … `EMS0031`, with a few IDs missing).
- Per subject: `X.npy` (epochs), `y.npy` (labels), `metadata.json`.
- **60-channel** EEG, standard 10–10 montage. Channels include the full set:
  `Fp1, Fz, F3, F7, FC5, FC1, C3, T7, CP5, CP1, Pz, P3, P7, O1, Oz, O2, P4, P8,
  CP6, CP2, Cz, C4, T8, FC6, FC2, F4, F8, Fp2, AF7, AF3, AFz, F1, F5, FT7, FC3,
  C1, C5, TP7, CP3, P1, P5, PO7, PO3, POz, PO4, PO8, P6, P2, CPz, CP4, TP8, C6,
  C2, FC4, FT8, F6, AF8, AF4, F2, FCz`.
- **Source sampling rate: 1000 Hz.** Source epoch window: **−2.0 s to +1.5 s**
  relative to stimulus onset.
- **4 original classes, 40 trials each (160 trials/subject)**:
  `0 = no_stimulation`, `1 = min_intensity`, `2 = medium_intensity`,
  `3 = max_intensity`.

### 2.2 Preprocessing pipeline (`data/dataprep.py` and variants)
Every modelling-ready `.npz` dataset is produced from the source trio by:
1. **Anti-aliased downsampling 1000 Hz → 250 Hz** (factor-4 FIR decimation,
   `scipy.signal.decimate`, zero-phase).
2. **Crop the epoch to −0.2 s … +1.5 s** around stimulus onset → **425 time
   samples** per epoch. (Keeps a 200 ms pre-stimulus baseline.)
3. **Class handling** (this is what distinguishes the dataset variants — see 2.3).
4. Cast to `float32`, save `.npz` with `X (n_trials, 60, 425)`, `y`, `sfreq=250`,
   `channel_names`, `class_names`, `epoch_tmin=-0.2`, `epoch_tmax=1.5`.

> Note: at the *modelling* stage further per-trial signal conditioning is applied
> inside the feature extractors (baseline subtraction, band-pass/Hilbert, etc. —
> see Section 3). The real-time scaffold additionally does detrend + band-pass +
> notch + common-average-reference, but the offline datasets above are the basis
> for all results in this document.

### 2.3 The dataset variants (the "splits")
All three modelling datasets are 60-channel, 250 Hz, −0.2…1.5 s, 425 samples.
They differ **only in how the four original classes are mapped**:

| Dataset folder | Classes | Per-subject split | Pooled total | How it's built |
|---|---|---|---|---|
| `data/og-ds-t-4c` | **4** — no_stim / min / medium / max | 40 / 40 / 40 / 40 | 4×1160 = 4640 | Keep all four classes (`dataprep.py`). Balanced. |
| `data/og-ds-t-3c` | **3** — no_stim / **medium** / max | **40 / 80 / 40** | 1160 / 2320 / 1160 | **`min` is merged into `medium`** → the "medium" class is min+medium combined (hence 80). **Imbalanced (25/50/25).** |
| `data/og-ds-t-3c-bal` | **3** — min / medium / max | 40 / 40 / 40 | 3×1160 = 3480 | **`no_stimulation` is dropped entirely** (`dataprep_3class_balanced.py`), remaining labels remapped to 0/1/2. **Balanced.** |

**Critical interpretation points for slides:**
- The **40/80/40 (`og-ds-t-3c`)** set is the project's *primary* 3-class dataset
  and the one most models are reported on. Because it is **imbalanced (25/50/25)**,
  raw accuracy should be read against a **50% majority-class baseline**, while
  *balanced accuracy* is the honest number against 33% chance. Its three classes
  are `no_stimulation`, a merged `medium` (= min+medium), and `max_intensity`.
- The **40/40/40 balanced (`og-ds-t-3c-bal`)** set removes the easy
  "stim vs no-stim" contrast and asks the *pure intensity* question
  (min vs medium vs max). It is the cleaner scientific question; chance is a clean
  33%.
- The **4-class** set is fully balanced and is the hardest (four graded levels,
  25% chance).

---

## 3. Feature Representations (the "feature families")

The LDA models use a **modular feature pipeline** (`ModularFeatureExtractor`): any
set of "feature families" can be concatenated, each is a self-contained,
sklearn-compatible extractor. Four families exist:

### 3.1 `erp` — ERP / SEP time-domain features (`erp_features.py`)
Per-channel, per-trial features of the stimulus-locked evoked potential, computed
on a central / fronto-central channel set (`C3, Cz, C4, FCz, FC1, FC2, FC3, FC4`
by default). The "full" set includes four families of features:
- **peak**: negative-peak amplitude & latency (search 0.10–0.20 s), positive-peak
  amplitude & latency (0.20–0.30 s), peak-to-peak. (5/channel)
- **window**: mean amplitude in fixed post-stim bins 0.10–0.18, 0.20–0.28,
  0.28–0.40 s. (3/channel)
- **baseline**: pre-stim mean, pre-stim SD, post-minus-baseline shift. (3/channel)
- **shape**: rectified area-under-curve, rising-edge slope. (2/channel)
Each trial is per-trial baseline-corrected using the −0.2…0 s window.

### 3.2 `bp` — band-power / spectral features (`bandpower_features.py`)
**Log Welch power per channel per canonical band**, over the whole epoch:
- Bands: **delta (1–4), theta (4–8), alpha (8–13), beta (13–30), gamma (30–45) Hz**.
- Channel sets: `all60` (every channel → 5×60 = 300 features), `sensorimotor`
  (~16 central/parietal), `central_fc` (the 8 ERP channels), or `custom`.
- Optionally relative (band / total power); the project uses **absolute** log
  power (relative was tested and was worse).

### 3.3 `tf` — time-frequency ERD/ERS features (`tf_features.py`)
Event-Related Desynchronization / Synchronization. Where `bp` gives one static
power value, `tf` measures **how band power changes over time vs the pre-stim
baseline** (Pfurtscheller ERD/ERS), via robust filter–Hilbert in dB:
- Per channel per band: mean dB in an early window (0–0.30 s) and a late window
  (0.30–1.50 s), plus peak-ERD (min dB) and peak-ERS (max dB) over the post
  window. → 4 summaries × 5 bands × channels (e.g. all60 → 1200 features).
- Motivation: the response magnitude/timing should scale with intensity. **In
  practice this family was the least useful on its own (see bad runs).**

### 3.4 `riem` — Riemannian covariance / tangent-space features (`riemann_features.py`)
Each trial is summarised by its **channel×channel covariance matrix** (spatial
co-activation / coupling), regularised (OAS), then projected into the **tangent
space** at the data's geometric mean → a flat vector usable by a linear model. For
60 channels this is 60×61/2 = **1830 features**, each interpretable as an electrode
pair. Captures *spatial coupling* structure the per-channel families discard.
**Individually weak here, but valuable inside the stacking ensemble (see best model).**

---

## 4. Validation Methodology (applies to all LDA models)

Two leakage-safe schemes are reported for every model:
- **Within-subject**: per subject, **Repeated Stratified K-Fold** (5 splits ×
  5 repeats). Trains and tests on the *same* person. Measures the ceiling when
  per-person calibration data is available.
- **LOSO (Leave-One-Subject-Out)**: train on 28 subjects, test on the held-out
  one, rotate. Measures **generalisation to a brand-new person** — the metric that
  matters most for deployment. Features are per-subject z-scored before pooling.

Other standard pieces:
- Classifier: **shrinkage LDA** (`solver='lsqr', shrinkage='auto'`, Ledoit-Wolf) —
  a regulariser well-suited to high-dimensional, collinear EEG features.
- **Artifact filter**: trials whose pre-stim baseline SD is a per-subject outlier
  (z > 3) are dropped (~1–2% of trials).
- Pipelines are refit inside every fold (no feature/scaler leakage).
- **Recurring finding:** within-subject ≫ LOSO by ~8–12 points across the whole
  project, reflecting inter-subject variability.

---

## 5. The Models & Results

### 5.0 Quick scoreboard (LOSO is the headline generalisation metric)

| Model | Dataset | Validation acc / bal | Notes |
|---|---|---|---|
| **Stack (4-family) — BEST** | 3c 40/80/40 | within **73.0% / 70.2%**, **LOSO 66.7% / 63.0%** | erp+bp+tf+riem fused by meta-learner |
| LDA erp+bp (primary) | 3c 40/80/40 | within 71.1% / 70.3%, LOSO 62.8% / 59.9% | the baseline everything is compared to |
| LDA erp+bp, 7-channel | 3c 40/80/40 | within 68.7% / 67.7%, LOSO 63.1% / 59.4% | deployable reduced montage |
| EEGNet | 3c 40/80/40 | within 63.4% / 64.7%, LOSO 59.8% / 60.8% | deep net, all 60 ch |
| LDA erp+bp (balanced) | 3c 40/40/40 | within 69.0% / 69.0%, LOSO 58.0% / 58.1% | pure intensity, no_stim removed |
| LDA erp+bp combined | 4c | within 61.6%, LOSO 48.7% | 4 graded levels, 25% chance |
| LDA erp+bp, 7-channel | 4c | within 57.2%, LOSO 47.3% | |
| EEGNet | 4c | within 53.0%, LOSO 49.7% | |
| *bad:* erp+bp+**tf** | 3c 40/80/40 | within 64.6%, LOSO 57.4% | tf concatenation **hurts** |
| *bad:* **riem only** | 3c 40/80/40 | within 67.9%, LOSO 57.5% | covariance alone is weaker |
| *bad:* erp+bp+riem concat | 3c 40/80/40 | within 72.0%, LOSO 59.7% | concatenation dilutes LOSO |
| *bad:* **XON channels** | 4c | within 54.8%, LOSO 46.9% | poor channel choice |
| *failed:* feature selection | 3c 40/80/40 | best LOSO bal 60.1% | could not beat erp+bp |

---

### 5.1 PRIMARY MODEL — 3-class LDA, erp+bp, 40/80/40 split
**Files:** `Results/LDA_3c/3c/LDA_td+fd_3c.json` (+ `importance_3c/`, `trends_3c/`)
**Config:** features = `erp` (full) + `bp` (all 60 channels); dataset =
`og-ds-t-3c` (no_stim / medium / max, 40/80/40).

| Validation | acc | bal | chance |
|---|---|---|---|
| within-subject | 71.1% | 70.3% | 33% |
| LOSO | 62.8% | 59.9% | 33% |

This is the project's reference decoder — "time-domain + frequency-domain"
(td+fd = ERP + band-power). Performance is ~2× chance. The combination of the two
families beats either alone (see the 4-class ablation in 5.4, where erp-only 50.8%
< bp-only 58.0% < combined 61.6% within).

#### Feature importance (`Results/LDA_3c/3c/importance_3c/`)
Two readings, both over 29 LOSO folds (404 total features):
- **Univariate ANOVA F-score top features** (most individually discriminative):
  `erp:peak_to_peak@Cz`, `erp:peak_to_peak@FCz`, `erp:peak_to_peak@FC2`,
  `erp:rise_slope@FC2`, `erp:auc_rect@Cz`, `erp:neg_latency@FC2/@FCz` … —
  dominated by **central/fronto-central ERP amplitude & latency**.
- **Fold-stable LDA weights top features** (what the model relies on, stable
  across folds): `erp:post_minus_base@C4`, `erp:mean_020_028@C4`, **`bp:gamma@Fz`**,
  `erp:peak_to_peak@Cz`, **`bp:gamma@C2`**, `erp:post_minus_base@FC3`, … —
  central ERP amplitude **plus gamma-band power**.
- Figures: `signature_bandpower_3c.png` (per-band discriminability — gamma stands
  out), `top_features_3c.png` (top features coloured by family).

#### Feature trends (`Results/LDA_3c/3c/trends_3c/`)
Dose-response of the top fold-stable features across the 3 conditions
(no_stim → medium → max). Top features:
`erp:post_minus_base@C4`, `erp:mean_020_028@C4`, `bp:gamma@Fz`,
`erp:peak_to_peak@Cz`, `bp:gamma@C2`, `erp:post_minus_base@FC3`,
`erp:mean_020_028@FCz`, `erp:neg_amp@FCz`. Figure `feature_trends_3c.png` shows
these features scale monotonically with intensity (real dose-response), with faint
per-subject lines behind the condition means.

---

### 5.2 REDUCED 7-CHANNEL MODEL — 3-class LDA, erp+bp, 40/80/40
**File:** `Results/LDA_3c/3c/LDA_7ch_3c.json`
**Config:** identical to 5.1 but **erp + bp restricted to 7 channels**:
`BEST_CHANNELS = [FCz, C4, Fz, FC4, Cz, C2, FC2]` (the most informative
central/fronto-central electrodes, chosen from the importance analysis).

| Validation | acc | bal | chance |
|---|---|---|---|
| within-subject | 68.7% | 67.7% | 33% |
| LOSO | 63.1% | 59.4% | 33% |

**Key message:** dropping from 60 channels to 7 costs only ~2.4 pts within-subject
and **LOSO is essentially unchanged** (63.1% vs 62.8%). This is the
**deployable montage** — a real EMS+EEG headset needs few electrodes, and the
7-channel model holds cross-subject performance while being far cheaper to acquire.

---

### 5.3 BALANCED 3-class LDA — 40/40/40 split (no_stim removed)
**File:** `Results/LDA_3c_bal/LDA_3c_bal.json`
**Config:** features = erp (full) + bp (all60); dataset = `og-ds-t-3c-bal`
(min / medium / max, balanced 40/40/40, the `no_stimulation` class removed).

| Validation | acc | bal | chance |
|---|---|---|---|
| within-subject | 69.0% | 69.0% | 33% |
| LOSO | 58.0% | 58.1% | 33% |

**Why this dataset exists / its message:** the 40/80/40 set includes
`no_stimulation`, which is partly an easy "was there a pulse at all?" detection.
Removing it isolates the **pure graded-intensity** question (min vs medium vs max).
Performance drops only modestly vs the 40/80/40 set even though the easy class is
gone — confirming the decoder genuinely separates **intensity levels**, not just
stim-vs-no-stim. Because it's balanced, raw accuracy is directly interpretable
against 33% chance (no majority-baseline caveat).

---

### 5.4 4-class LDA — all four intensities
**Files:** `Results/LDA_4c/LDA_td+fd_4c.json`, `Results/LDA_4c/LDA_7ch_4c.json`
(+ `importance_4c/`, `trends_4c/`)
**Dataset:** `og-ds-t-4c` (no_stim / min / medium / max, balanced 40/40/40/40,
25% chance).

Family ablation (all 60-ch, `LDA_td+fd_4c.json`):

| Feature set | within acc/bal | LOSO acc/bal |
|---|---|---|
| erp only | 50.8% / 50.8% | 44.8% / 44.7% |
| bp only | 58.0% / 58.0% | 44.2% / 44.2% |
| **erp + bp combined** | **61.6% / 61.6%** | **48.7% / 48.7%** |

7-channel version (`LDA_7ch_4c.json`): within 57.2%, LOSO 47.3%.

**Message:** the 4-class problem is the hardest (four graded levels). erp+bp
combined still roughly doubles chance within-subject (61.6% vs 25%), but LOSO
(48.7%) shows the cross-subject difficulty of separating four adjacent levels.
The importance/trends for 4-class lean more on **gamma band-power**
(`bp:gamma@Fz`, `bp:gamma@C2`, `bp:delta@C6` top the fold-stable LDA weights).

---

### 5.5 EEGNet (deep learning baseline) — 3-class and 4-class
**Files:** `Results/EEGNet_3c.md`, `Results/EEGNet_4c.md`
**Model:** EEGNet-8,2 (Lawhern et al. 2018) reimplemented inline
(`Models/EEGNet/train_eegnet.py`). Raw 60-channel epochs (no hand features),
temporal kernel 500 ms, F1/D/F2 = 8/2/16, per-channel z-score, class-balanced
loss, early stopping. Same within / LOSO protocol.

**EEGNet 3-class** (`og-ds-t-3c`, no_stim/medium/max, 40/80/40):
- within-subject: acc **63.4%**, bal **64.7%** (chance 33%).
- LOSO: acc **59.8%**, bal **60.8%** (range 41.9–72.5%).
- Per-class recall (LOSO): no_stim 0.71, medium 0.57, max 0.55.

**EEGNet 4-class** (`og-ds-t-4c`, balanced 40/40/40/40):
- within-subject: acc **53.0%** (chance 25%).
- LOSO: acc **49.7%**, bal **49.7%** (range 28.1–70.6%).
- Per-class recall (LOSO): no_stim 0.68, min 0.41, medium 0.34, max 0.55 — the
  classic ordinal pattern (extremes recalled best, middle levels confused).

**Message:** EEGNet, learning directly from raw EEG, **does not beat the
hand-crafted LDA features**. On 3-class it is comparable on LOSO (60.8% bal vs LDA
59.9%) but lower within-subject; on 4-class it is similar to LDA. With only
~120–160 trials/subject, the deep net has no data advantage over a well-regularised
linear model on good features.

---

### 5.6 BAD RUNS — tested and rejected approaches
**Folder:** `Results/LDA_3c/bad_runs/`. These are documented dead-ends; each is
scientifically informative (what does *not* work and why).

**(a) Time-frequency (tf) concatenation — `LDA_w_tf.json`.**
erp + bp + **tf** on the 40/80/40 set: within **64.6%**, LOSO **57.4%** — *worse*
than erp+bp (71.1% / 62.8%). Adding the 1200 tf (ERD/ERS) features **dilutes** the
model. Importance/trends with tf (`importance_w_tf/`, `trends_w_tf/`) confirm tf
features rarely rank near the top. **Lesson: the time-frequency domain is less
discriminative than the time or frequency domains alone for this signal.**

**(b) Riemannian alone & concatenated — `riemann_3c/riemann_comparison_3c.json`.**
A 3-way comparison on the 40/80/40 set:

| Feature set | within acc/bal | LOSO acc/bal |
|---|---|---|
| baseline erp+bp | 71.1% / 70.3% | 62.8% / 59.9% |
| **riem only** | 67.9% / 63.3% | 57.5% / 55.1% |
| erp+bp+riem concat | 72.0% / 68.3% | 59.7% / 58.1% |

Riemannian covariance **alone is weaker** than erp+bp, and **concatenating** it
hurts LOSO (dilution again). Conclusion *at this stage*: "Riemann doesn't help."
**This was later overturned by stacking** — see 5.8: riem is weak as a feature
block but *complementary* as a base model in an ensemble.

**(c) XON channel set — `LDA_XONCh_3c.json`.**
A 4-class run using a 7-channel set `XON_CHANNELS = [F3, F4, C3, Cz, C4, P3, P4]`
(a more frontal/parietal montage) instead of the central `BEST_CHANNELS`: within
**54.8%**, LOSO **46.9%** (chance 25%). Clearly worse than the central 7-channel
set — **channel choice matters; the signal is central/fronto-central, not
frontal-parietal.** (Filed under bad runs for that reason.)

---

### 5.7 FAILED EXPERIMENT — nested-CV cross-family feature selection
**Folder:** `Models/LDA Best Ft (failed)/` (results in its `results/` subfolder:
`feature_selection.json`, `accuracy_vs_k.png`). **Belongs with the bad/rejected
runs.**

**Idea:** if concatenating whole families dilutes, maybe a *curated subset* of the
best features across erp + bp + tf (1604-feature candidate pool) could beat erp+bp.
Selection done **inside** nested LOSO (rank on train fold only — leakage-safe),
sweeping the number of selected features k, with two selectors:
- **fscore** (univariate relevance): best LOSO bal **60.1%** at k=300.
- **mrmr** (relevance minus redundancy): best LOSO bal **59.3%** at k=300.
- full 1604-feature pool (no selection): 56.7% (confirms dilution).
- erp+bp baseline on identical folds: **59.9%**.

**Result: feature selection could NOT beat erp+bp** (60.1% vs 59.9% = a tie within
the ±11% fold noise; mrmr was slightly worse). Accuracy only rises back *toward*
the baseline as k grows, and the "best" sets are large and tf-heavy — i.e. selection
just rediscovers "use erp+bp-like features." **Lesson: the answer is not a cleverer
subset of a single concatenated vector.** This is why the folder is marked
`(failed)`.

---

### 5.8 BEST MODEL — Per-family LDA Stacking (ensemble)
**Folder:** `Models/LDA-Stacking/` (results: `results/stacking.json`,
`results/confusion.png`). **This is the current best decoder.**

**Architecture.** Instead of concatenating families into one (diluting) vector,
train **one shrinkage-LDA per family** (erp, bp, tf, riem), then fuse their
**class-probability outputs** with a small multinomial-logistic **meta-learner**.
Each base model stays low-dimensional relative to its own family; the meta-learner
*learns how much to trust each family*, so individually-weak-but-complementary
views (tf, riem) add signal instead of diluting the strong ones. Stacking is
leakage-safe: out-of-fold base probabilities (inner GroupKFold over training
subjects for LOSO; inner StratifiedKFold over trials for within) train the
meta-learner; the held-out subject/rows never enter a base or meta fit.

**Dataset:** `og-ds-t-3c` (40/80/40, no_stim/medium/max — same as the primary model).

| Validation | acc | bal | chance |
|---|---|---|---|
| within-subject | **73.0%** | **70.2%** | 33% |
| LOSO | **66.7%** | **63.0%** | 33% |

**vs the erp+bp baseline (62.8% / 59.9% LOSO): +3.9 acc / +3.1 bal — the only
approach in the whole project that beats erp+bp.**

**Meta-learner family weights** (how much each family is trusted):
- within: erp 0.29, bp 0.31, riem 0.24, tf 0.16
- LOSO: erp 0.37, bp 0.32, riem 0.20, tf 0.11

**Per-class recall (LOSO):** no_stim 0.53, medium 0.78, max 0.58 — the expected
adjacent-intensity confusion (middle class strongest; extremes leak into it).
Confusion matrix saved as `results/confusion.png`.

**Why it works (the key scientific story of the project):**
- The *same* families that **dilute** when concatenated (tf, riem) **help** when
  fused at the decision level — because their errors are **decorrelated** from
  erp/bp. riem captures spatial coupling; tf captures ERD/ERS timing — different
  *views* of the response. Ensembling pays off when base models are
  **complementary, not individually better**.
- This **overturns the earlier "Riemann doesn't help" conclusion (5.6b)**: riem is
  a poor feature *block* but a useful ensemble *member* (it earns weight 0.20–0.24).
- The gain is concentrated in **LOSO** (cross-subject generalisation) — exactly the
  weak spot — while doing no harm within-subject. The progression
  baseline → 3-way stack (+1.6) → 4-way stack (+3.2) is consistent, suggesting a
  real effect (though the ±11–13% fold spread means it is directional, not yet a
  statistically nailed-down significance).

> Caveat for honesty in any write-up: the +3 pt LOSO gain is smaller than the
> between-fold standard deviation, so it is a consistent *directional*
> improvement, not a proven significant one on 29 subjects. A paired per-fold test
> would be the next step to quantify confidence.

---

## 6. Overarching Narrative (for structuring the talk)

1. **Problem:** decode graded EMS stimulation intensity from single-trial EEG;
   end goal is a closed-loop discomfort-aware stimulator.
2. **Data:** 29 subjects, 60-ch, 250 Hz, −0.2…1.5 s epochs; three class framings
   (4-class balanced; 3-class 40/80/40 with no_stim; 3-class 40/40/40 balanced).
3. **Representations:** time-domain ERP/SEP + spectral band-power are the workhorse;
   time-frequency (ERD/ERS) and Riemannian covariance are alternative views.
4. **Baseline result:** shrinkage-LDA on **erp + bp** decodes at ~2× chance
   (3-class LOSO ~60% balanced), with a **7-channel** version essentially as good —
   important for a deployable headset.
5. **What didn't work:** tf concatenation, Riemann alone/concatenated, the XON
   montage, and nested-CV feature selection all **failed to beat erp+bp** — a strong
   message that erp+bp is near the ceiling of *single-vector linear feature
   engineering*, and that **dilution** (too many features for ~120 trials/subject)
   is the recurring failure mode.
6. **What did work:** **decision-level stacking** of per-family LDAs — fusing the
   complementary views without dilution — is the **best model (LOSO 66.7% / 63.0%
   balanced, +3 over baseline)**, and it rehabilitates the Riemannian features that
   failed by concatenation.
7. **Deep learning:** EEGNet on raw EEG does **not** beat the engineered linear
   features at this data scale.
8. **The persistent limit:** within-subject ≫ LOSO everywhere → the real frontier
   is **inter-subject variability** (cross-subject domain alignment), not more
   features.

---

## 7. File Map (where each result lives)

```
Results/
  EEGNet_3c.md                         # EEGNet 3-class within + LOSO (big log)
  EEGNet_4c.md                         # EEGNet 4-class within + LOSO (big log)
  LDA_3c/
    3c/
      LDA_td+fd_3c.json                # PRIMARY erp+bp 3-class model (5.1)
      LDA_7ch_3c.json                  # 7-channel reduced (5.2)
      importance_3c/                   # feature importance json + 2 figures
      trends_3c/                       # feature dose-response json + figure
    bad_runs/
      LDA_w_tf.json                    # erp+bp+tf (diluted) (5.6a)
      LDA_XONCh_3c.json                # XON channel set, 4-class (5.6c)
      riemann_3c/riemann_comparison_3c.json   # riem alone / concat (5.6b)
      importance_w_tf/, trends_w_tf/   # importance & trends incl. tf
      erd_ers_plot.py                  # plotting helper
  LDA_3c_bal/
    LDA_3c_bal.json                    # balanced 40/40/40 erp+bp (5.3)
  LDA_4c/
    LDA_td+fd_4c.json                  # 4-class family ablation (5.4)
    LDA_7ch_4c.json                    # 4-class 7-channel
    importance_4c/, trends_4c/         # 4-class importance & trends

Models/
  LDA/                                 # main modular LDA pipeline + feature extractors
  LDA Best Ft (failed)/                # FAILED nested-CV feature selection (5.7)
    results/feature_selection.json, accuracy_vs_k.png
  LDA-Stacking/                        # BEST model — per-family stacking (5.8)
    results/stacking.json, confusion.png
  EEGNet/                              # EEGNet trainer

data/
  og/                                  # raw 1000 Hz source trios (29 subjects)
  og-ds-t-4c/                          # 4-class balanced
  og-ds-t-3c/                          # 3-class 40/80/40 (no_stim/medium/max)
  og-ds-t-3c-bal/                      # 3-class 40/40/40 (no_stim removed)
  dataprep.py                          # 1000->250 Hz, crop -0.2..1.5, class mapping
```
