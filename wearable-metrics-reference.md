# Wearable metrics reference

**What the COROS numbers are worth, and which ones to ignore.** Compiled 2026-09-25/29 from
three literature reviews commissioned after the user asked "how accurate are these metrics?".
Read this before citing any watch-derived recovery, sleep, load or readiness number in a review.

Evidence tags: **[V]** measured against a gold standard in peer-reviewed work · **[P]** plausible
by mechanism or sensor-class transfer, not measured on this device · **[X]** no validation exists.

---

## 0. The one-line version

| Metric | Verdict |
|---|---|
| **Raw HR stream, pace, treadmill belt speed** | **Trustworthy.** The measurement is good; the modelling is the weak part |
| **Nightly resting / sleeping HR** | **Trustworthy as a 7-day rolling mean.** The best metric on the watch |
| Total sleep time | Usable as a weekly trend, with a known **+20-47 min** inflation |
| Nightly HRV | Error is **4-6x** the smallest worthwhile change. Multi-week trend only |
| Sleep stages (deep/REM) | **Not a measurement.** ICC 0.13-0.36 vs PSG. Do not cite |
| Recovery % | **Ignore.** Excludes sleep, HRV, stress and muscular fatigue *by COROS's own statement* |
| Load Ratio / Intensity Trend | **Ignore.** An ACWR — discredited metric, computed on a load that omits lifting |
| Training Effect / Training Focus | **Ignore.** No published validation; inherits every HRmax error |

**There is no peer-reviewed validation of ANY COROS wrist sensor for HR, HRV or sleep. [X]**
COROS appears in zero sleep-validation studies and zero nocturnal HR/HRV validations. Their
marketed "within 3 bpm of ECG 95% of the time" refers to the **arm-worn** strap, not the watch.
`COROS EvoLab` returns **0** PubMed hits. The fair proxy for the wrist sensor is a Garmin
Fenix 6, and in every head-to-head the *sport-watch* brands land at the bottom of the range.

---

## 1. Resting and sleeping heart rate — the metric that works

**[V] Accuracy.** Dial et al. 2025, *Physiological Reports* 13:e70527 — 13 adults, **536 home
nights**, vs Polar H10 ECG. Nocturnal RHR bias −0.01 to −1.41 bpm, MAPE 1.67–3.00%, CCC 0.86–0.98.
Garmin was **excluded from the analysis entirely** because it will not disclose when it samples
the value — and COROS documents its overnight HR no better.

**[V] Noise floor.** Nuuttila et al. 2024, *Sports Medicine – Open* — 24 recreational runners,
~43 nights each, wrist PPG: within-person CV **6.0 ± 2.1%**. At ~53 bpm that is **±3.2 bpm of
ordinary night-to-night scatter**; smallest worthwhile change ≈ **1.7 bpm**.

**[V] Calibration — what moves it:**

| Stimulus | Effect on nocturnal HR |
|---|---|
| Hard endurance session | **+4.5 bpm** (109% of baseline) |
| Marathon-scale effort | +15 bpm (130%) |
| Four consecutive hard days | peaks **on night 2**, not night 1 (52 → 61 bpm) |
| Alcohol | **+2.4–2.8 bpm per drink**, dose-dependent |
| Moderate altitude ~1,550 m | **[P]** order +2 to +5 bpm — at or below the noise floor |

Two consequences that matter here:
- **A hard session and two or three drinks produce indistinguishable signatures.** Log the
  confounder before reading the number.
- **PM sessions show up far more strongly than AM.** Relevant to the stacked run-AM/lift-PM days:
  the *lift* is what moves the overnight number, which is ironic given the load model ignores it.

**HOW TO USE IT:** 7-day rolling mean against a 28-day baseline. Ignore anything under ~2 bpm.
Treat a **≥3–4 bpm sustained elevation with no alcohol/altitude/illness/travel explanation** as a
real flag worth a down-day. A single night +5 bpm after a hard double is the *expected response*,
not a warning.

---

## 2. HRV — error is 4-6x the signal

| | Nightly RMSSD | Nightly resting HR |
|---|---|---|
| Measurement error (watch class) | LoA **±13 ms**, MAPE 10.5% | MAPE 1.5–3% |
| On a 47–62 ms range | **±22–33%** | ~±1–2 bpm |
| Biological day-to-day CV | 10–12% | ~4% |
| Smallest worthwhile change | ~5% | ~1 bpm |
| **Error ÷ SWC** | **4–6x** | **<1x** |

**A single night's HRV on this hardware is not interpretable.** To clear the noise floor you need
a **25–30% swing**, which in practice means alcohol, illness or fever — not training.

**The user's own series proves it.** Every reading except one sits 47–62 against a baseline of 57
— that entire spread is inside one measurement error. The exception is **2026-09-24: 30 ms, a 47%
drop**, which does clear the floor. That one was real; everything else narrated from this series
has been noise. (Note the drop was ~4x larger than the population model predicts for five drinks
— **do not read population effect sizes onto this athlete**.)

**[V] HRV-guided training is essentially null.** Manresa-Rocamora et al. 2021 — 7 RCTs, 199
participants total: VO2max SMD 0.13 (p=0.30), endurance performance 0.20 (p=0.18), every primary
outcome non-significant; two HRV subgroups pointed in *opposite* directions; allocation
concealment unreported in 87.5% of trials. The one durable finding is a **responder-distribution**
effect (fewer non-responders), not a performance effect.
**And every positive trial used chest-strap morning HRV. No RCT has tested wrist-optical nightly
HRV as a decision input.**

**HOW TO USE IT:** 7-day rolling mean only, against a 28–60 day baseline, acting only on several
consecutive days outside the band. Never a nightly value. **Discard frequency-domain outputs
entirely** (LF, LF:HF, "stress") — least valid things wrist PPG produces.

**Two traps:**
- **A hard session should suppress HRV for 24–48 h, ≥48 h after high intensity.** That is the
  intended response. Do not report it as a flag.
- **High HRV is not automatically good.** Very high RMSSD with very low HR can mean parasympathetic
  saturation, and HRV can *rise* in overreaching. The proposed early warning is a **collapsing
  day-to-day variability** — the variability going unusually stable — not a low value.

---

## 3. Sleep — one number of four is worth reading

**[V] The sleep/wake asymmetry drives everything.** Wrist devices call sleep at sensitivity
**0.93–0.99** and wake at specificity **0.18–0.54**. Since sleep efficiency is 85–92%, answering
"asleep" every epoch would score ~90% accuracy — specificity is the only informative number, and
it is a coin flip. Consequence: **sport watches inflate TST by +20 to +47 min** and swallow
15–50 min of wake. Accuracy is *worst on disrupted nights*, i.e. the ones worth knowing about.

**[V] Staging is not a measurement.** Four-stage kappa vs PSG: Apple 0.53, Fitbit 0.41–0.42,
Whoop 0.37, Withings 0.22, **Garmin Vivosmart 4 = 0.21**. Two trained human scorers agree at 0.76.
For deep sleep the decisive figure is the **ICC against PSG nightly totals: 0.13–0.36** — the
device's ranking of nights is close to random. Per-night minute bias spans **−43 to +73 min**.
A Polar watch once classified **entire nights as deep sleep on 10 of 146 nights**, with no error flag.

**[P] Endurance athletes should expect systematic over-calling of deep sleep.** The algorithms use
low HR + low motion as the slow-wave signature; a runner with a sleeping HR in the 40s–50s lying
still looks like deep sleep to that model. Matches the observed sport-watch biases of +31 to +73 min.

**[V] Altitude at 1,630 m** (44 men, PSG, vs 490 m): SpO2 96% → 94%, AHI 4.6 → 7.0/h, slow-wave
sleep **−3.5 percentage points on night 1**. Real physiology, small.

**HOW TO USE IT:** TST as a **weekly** trend, treated as an upper bound with ~30 min subtracted.
Needs **3 nights minimum** for a weekly mean, 5 for a good one. **Never cite stage minutes or any
composite sleep score** — the score is a weighted sum whose heaviest inputs have ICC 0.13–0.36.

---

## 4. Training Load, Recovery % and Training Effect

**What COROS actually computes.** Load is a Banister-family TRIMP, **heart rate only** — no power,
no pace, no elevation, no temperature:

```
TRIMP = duration(min) x B x (0.2445 x e^(3.411 x B))
B = (HRworkout - HRrest) / (HRmax - HRrest)
```

Base Fitness = 42-day rolling load; Load Impact = 7-day; **Load Ratio = their ratio, i.e. an ACWR.**
(Coefficients are DC Rainmaker's reporting of a COROS disclosure, not an official publication —
but the qualitative conclusion holds for any Banister-family model.)

### 4.1 HRmax sensitivity — the one fixable problem

The exponential weighting amplifies HRmax error ~4.4x:

| Avg HR | HRmax 5 bpm low | HRmax 10 bpm low |
|---|---|---|
| 130 | +10.0% | +21.6% |
| 150 | +11.6% | +25.4% |
| 180 | **+14.1%** | **+31.2%** |

COROS's exponent is **~1.5x steeper than textbook TRIMP**, so it is more HRmax-sensitive than the
classic model. `220 − age` carries an SD of ±10–12 bpm. **While HRmax sits on a default, every
load, TE, Load Ratio and Recovery figure is inflated 15–50% — and the error scales with intensity,
so it also distorts the hard/easy ratio the system reports.** Pinning HRmax and setting it in the
profile is the single highest-value action available. See the memory `pace4-hr-calibration`.

Related: **[V]** COROS Pace 3 lactate-threshold estimation vs lab testing (Lu et al. 2025,
n=17): LT HR **MAE 8.93 bpm**, single-test success rate **47.1%** (worst of three devices),
LT *pace* MAPE **22.6%** with systematic overestimation. Since EvoLab anchors on LT HR zones,
the anchor itself carries ~9 bpm of error by construction.

### 4.2 The strength blind spot, measured on this athlete

**2026-09-24, same day, same person** (verified from COROS records):

| | Duration | Avg HR | kcal | COROS load |
|---|---|---|---|---|
| 5x6 min sub-T, treadmill | 55:11 | 163 | 690 | **~133 AU** |
| 531 C14 W2 D1 Squat, 13 sets | 38:15 | **101** (max 140) | 166 | **~10 AU** |

**The squat session scores ~8% of the run. Session-RPE would price it at ~80%.** The HR model
under-values heavy lifting by roughly **an order of magnitude**.

Why: a heavy 5RM is ~20–30 s of near-maximal mechanical output; HR lags the effort, peaks *after*
the set, and decays through the rest interval. HR-based models integrate cardiac work and are blind
to mechanical tension, motor-unit recruitment and eccentric damage — the three things that actually
cost two days of recovery. Firstbeat's EPOC model was fitted on **48 exercise settings, 158
subjects, running/cycling/arm-ergometer only — no resistance training in the fitting data at all.**

Worse, it is direction-specific: Genner & Weston 2014 found blood lactate and salivary cortisol
were **greater at 55% 1RM than at 70 or 85%**. Heavy low-rep work produces a *smaller* metabolic
signature while imposing more mechanical cost — exactly the direction that breaks HR load for
5s PRO programming. And a 10 bpm-low HRmax inflates the run +27% but the squat only +16%, so it
**widens** an already-wrong ratio.

**Consequence: the weekly Load Impact, Load Ratio and Recovery % are a running-only ledger.**
Four lifting days contribute ~40–50 AU against a weekly total in the hundreds. The system will
report him under-loaded and well-recovered in exactly the weeks when heavy lower-body work is
what is limiting his running.

### 4.3 Recovery % — what COROS says it excludes

Verbatim from COROS support: *"Currently, other factors such as **Sleep, HRV, Daily Stress, or
muscular fatigue (rather than cardiovascular fatigue) are not part of the Recovery calculation**,
so it's important to listen to your body."*

It is a decay curve on an HR-only load number. **"83%, moderate training recommended" means
"you have not run much lately."** Nothing more.

### 4.4 Load Ratio is a discredited metric

Impellizzeri et al. 2020, *IJSPP* 15(6):907-913, verbatim: *"There is no evidence supporting the
use of ACWR in training-load-management systems or for training recommendations aimed at reducing
injury risk. The statistical properties of the ratio make the ACWR an inaccurate metric and
complicate its interpretation for practical applications. In addition, it adds noise and creates
statistical artifacts."* The numerator sits inside the denominator. Optimized/Maintaining/Excessive
are bands on this ratio, computed from a load that omits half the training.

---

## 5. Altitude and heat inflate load with no change in training

Both raise HR at a fixed external workload, and every HR model maps HR → intensity → load through
an exponential. **COROS corrects for neither — the model has no temperature or elevation input.**

A second, independent mechanism at altitude: **HRmax itself falls with hypoxia** while the profile
value stays fixed, so B is computed against a maximum unreachable that day. This compounds.

**[V] Heat:** cardiovascular drift is amplified by heat and accompanied by a genuine *fall* in
VO2max. Subtle point worth keeping — in the heat, HR is **not** lying about relative cardiovascular
strain; it is lying about mechanical work and about the adaptive stimulus.

**[V] Altitude is not a fixed offset.** In *acclimatised* mountain guides, HR and lactate at a
fixed 100 W were "unchanged or even slightly reduced" at 2,000 m. The penalty is largest in the
first days and shrinks with exposure. **Do NOT introduce a blanket "subtract X bpm for altitude"
correction — the literature does not support a constant.**

**[V] And moderate altitude may do less to RHR than assumed:** elite skiers and biathletes over
**17–21 days at 1,800 m showed no systematic change in resting HR** (p=0.114, within-subject CV
7.2%). The 10–20 bpm figures in circulation are for 2,500 m+ and acute exposure.

---

## 6. What to use instead

Ranked by evidence behind them, best first:

1. **The two-more-reps question and the within-rep plateau.** Already doctrine. Needs no HRmax,
   works unchanged at altitude and in heat. Strictly better than any HR-derived readiness number.
2. **Top-set performance on the four main lifts.** The per-lift hit/miss rule already *is* a
   readiness test with a real criterion, and it self-calibrates.
3. **Session-RPE (RPE x minutes), logged for every session including lifts.** 36 validation
   studies across sports, sexes, ages and levels. The only measure here that prices a heavy squat
   day correctly.
4. **A single-item fatigue question.** Construct validity r ≈ .63–.66, reliability kappa ≈ .77–.78.
5. **7-day rolling resting HR.** The one genuinely physiological channel on the watch — and the
   Recovery score ignores it.

**Saw, Main & Gastin 2016** (56 studies, concurrent subjective and objective measures), verbatim:
*"Subjective and objective measures of athlete well-being generally did not correlate. Subjective
measures reflected acute and chronic training loads with superior sensitivity and consistency than
objective measures."* The objective measures reviewed **included resting and exercise heart rate**.

**Documented behavioural risk:** users of readiness scores report "more of an emotional response
rather than a rational one" and adjust behaviour specifically to *improve the score*. Optimising
the metric instead of the training is a real failure mode, not a hypothetical one.

---

## 7. Key sources

- Dial et al. 2025, *Physiological Reports* 13:e70527 — nocturnal RHR/HRV vs ECG, 536 nights
- Nuuttila et al. 2024, *Sports Medicine – Open* — morning vs nocturnal HR/HRV, CV values
- Nuuttila et al. 2022, *IJSPP* 17:1296 — reliability/sensitivity of nocturnal HR and HRV
- Manresa-Rocamora et al. 2021, *IJERPH* 18:10299 — HRV-guided training meta-analysis
- Chinoy et al. 2021, *SLEEP* 44(5):zsaa291 — 7 devices vs PSG
- Wang et al. 2025, *SLEEP Advances* 6(2):zpaf021 — 6 devices, n=62, staging kappa
- Nazari et al. 2024, *Sensors* 24(20):6532 — per-stage ICCs
- Latshang / Stadelmann 2013, *SLEEP* / *PLOS ONE* — sleep at 1,630 m
- Saw, Main & Gastin 2016, *BJSM* 50(5):281-91 — subjective vs objective, PMID 26423706
- Impellizzeri et al. 2020, *IJSPP* 15(6):907-913 — ACWR critique, PMID 32502973
- Borresen & Lambert 2009, *Sports Med* 39(9):779-95 — training load review, PMID 19691366
- McLaren et al. 2018, *Sports Med* 48(3):641-658 — sRPE vs TRIMP meta-analysis, PMID 29288436
- Genner & Weston 2014, *JSCR* 28(9):2621-7 — resistance-exercise internal load, PMID 24552797
- Foster et al. 2001, *JSCR* 15(1):109-15 — the original sRPE paper, PMID 11708692
- Haddad et al. 2017, *Front Neurosci* 11:612 — sRPE validity review, PMID 29163016
- Lu et al. 2025, *Front Physiol* 16:1621996 — COROS Pace 3 LT estimation, PMC12309276
- Grosicki et al. 2026, *PLOS Digital Health* 5(3):e0001284 — alcohol, 5.1M person-days
- Pühringer et al. 2022, *High Alt Med Biol* 23(1):37-42 — acclimatised HR at 2,000 m
- Firstbeat EPOC and Training Effect white papers; COROS support pages; DC Rainmaker EvoLab teardown
