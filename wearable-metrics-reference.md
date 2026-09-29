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

**But the channel is not worthless — the day-to-day READING is.** In a 2-week deliberate overload
(Nuuttila 2024, n=24), **nocturnal HRV did separate the 8 overreached from the 12 responders
(p=0.011)**, alongside nocturnal HR and a one-item readiness question. A real multi-week signal is
detectable; a Tuesday-versus-Wednesday difference is not. See §6.

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

**[V] Experimental confirmation (added 2026-09-29).**
- **Kraft, Green & Gast 2014**, *JSCR* 28(7):2042-46 — two sessions **matched for total work
  volume and work rate**, 3x6 @ ~80% 1RM vs 2x12 @ ~60%. Session RPE **5.7 vs 4.3**, with
  **no difference in recovery heart rate.** Perception separated them; HR did not.
- **Falk Neto et al. 2020**, *Front Physiol* 11:919 — same session performed all-out vs at RPE-6.
  sRPE 91.7 vs 42.6 AU (p=0.002, **ES 1.82**); **Edwards TRIMP 93.1 vs 84.9, p=0.085 — not
  significant.** An HR-zone model could not distinguish an all-out session from a deliberately
  easy one. sRPE correlated with 30-min post lactate (rho=0.596); neither TRIMP did.
- **McLaren et al. 2018 moderator detail** — TRIMP vs external load is r=0.72 in mixed training
  but changes by **−0.58 for "neuromuscular" work → residual r ≈ 0.14**, with training mode
  explaining **100%** of between-estimate variance. On strength-type work, HR-derived load has
  **essentially zero association with the external work done.**
- **Sweet et al. 2004** — session RPE rose with %1RM *"despite a decrease in the total work
  performed."* Even sRPE understates heavy work, since it underestimates the mean of per-set
  ratings.

**Honesty point:** no peer-reviewed study validates Firstbeat EPOC/TE or hrTSS against barbell
training in either direction, and "neuromuscular" in McLaren is team-sport gym work, not pure
barbell. The under-reporting conclusion follows from the models' stated scope plus the matched
experiments above — sound reasoning, not a measured error figure for this exact case.

### 4.2b THE COST THE WATCH CANNOT SEE — and why the AM-run/PM-lift order is right

**Palmer & Sleivert 2001**, *J Sci Med Sport* 4(4):447-459 [V]. n=9 well-trained distance runners
(VO2max 66.6), 50-min resistance session, treadmill runs at rest or 1, 8, 24 h after:
- Submaximal VO2 **+2.6 ± 2.3% at 1 h** (p=0.007), **+1.6 ± 2.5% at 8 h** (p=0.032), ns at 24 h
- *"No significant differences were found in exercising **heart rate**, ventilation, respiratory
  exchange ratio, ratings of perceived exertion, or running mechanics."*

**A real 2.6% loss of running economy that exercising HR could not see.** If HR does not move when
economy degrades, **no HR-derived metric can detect concurrent-training interference.** This is the
exact mechanism operating on the stacked Tue/Fri days.

**It also argues the current order is correct.** Doma, Deakin & Bentley 2017, *Sports Med*
47(11):2187-2200: carry-over fatigue impairs subsequent endurance sessions "for several hours to
days," and **endurance-before-strength with ~6 h separation was more favourable than the reverse**
— which is the order already in the plan (run AM, lift PM, >=6 h apart). Keep it. (The 6 h figure
is a study-design artefact, not a validated threshold.)

**Neuromuscular time course [V]:** Thomas et al. 2018, *MSSE* 50(12):2526-35 — 10x5 back squat
@ 80% 1RM; fatigue took **up to 72 h** to resolve, twitch force and voluntary activation still
depressed at **48 h**, peripheral/contractile rather than CNS. Raeder et al. 2016 — after a 6-day
intensified strength block, 1RM and CMJ returned to baseline within 3 days but reactive strength
index (−7.9%) and tensiomyography (−14.7%) had not.
**Caveat [P]:** "neuromuscular fatigue persists while HRV normalises" is sound inference, not a
measured effect — neither study measured HRV, and the HRV-after-resistance literature stops at
the acute window (~30 min post). The 24-72 h head-to-head has never been run.

### 4.3 Recovery % — what COROS says it excludes

Verbatim from COROS support: *"Currently, other factors such as **Sleep, HRV, Daily Stress, or
muscular fatigue (rather than cardiovascular fatigue) are not part of the Recovery calculation**,
so it's important to listen to your body."*

It is a decay curve on an HR-only load number. **"83%, moderate training recommended" means
"you have not run much lately."** Nothing more.

**[V] Systematic evaluation of the whole category.** Doherty et al. 2025, *Translational Exercise
Biomedicine* 2:128-144 — **14 composite scores across 10 manufacturers** (Garmin Body Battery and
Training Readiness, Oura Readiness, WHOOP Recovery/Strain, Polar Nightly Recharge, Fitbit Daily
Readiness, Samsung Energy Score). Inputs: HRV in 86%, RHR 79%, activity 71%, sleep 71%. Conclusion:
**no manufacturer discloses its algorithm, and most scores lack empirical validation or
peer-reviewed evidence of accuracy or clinical relevance.** (One author has Oura/HRV4Training ties
and still reaches a negative conclusion.)

**[V] And a direct negative test.** Nuuttila et al. 2025, *Sensors* 25(2):533 — n=24, deliberate
overload block. **Perceived strain and muscle soreness rose significantly (p<0.001) while every
nightly recovery metric — including the proprietary composite (HR + HRV + breathing rate) —
remained unchanged.** The score missed an overload that a subjective question caught.

**On the vendor's own flagship evidence:** Grosicki et al. 2026, *IJSPP* 21(2):180-191 — 389 pro
golfers, +10 pp WHOOP Recovery → −0.238 strokes. **All six authors are affiliated "Performance
Science, WHOOP Inc.",** and the within-athlete models compare **season averages, not day-to-day**,
so it never tests the actual use case.

PubMed record counts, independently confirmed: **zero** for "Body Battery," **zero** for Firstbeat
recovery time/training status, **zero** for Polar Nightly Recharge, **zero of any kind on COROS
Recovery.** Garmin's cited basis for Body Battery is an unpublished 2012 Firstbeat white paper.

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

### 5.1 Heat — the error is measured, and it is large

**Bröde & Kampmann 2019**, *Ind Health* 57(5):615-620 — **373 climatic-chamber experiments** [V].
Metabolic rate from measured O2 was accurate to 5%; **metabolic rate estimated from heart rate
overestimated it by 43%.** Mechanism: rising core temperature raises HR by **~30 bpm per °C**.
Correcting for the thermal component restored 10-15% accuracy. Parallel field study (41 forest
workers, thermal ΔHR 0-38 bpm): raw HR overestimated work by **30% on average, range 1-64%**, with
**74% of prediction-error variance** explained by the thermal HR component alone.

**Every HR-derived load metric inherits this in full — none contains a temperature term.**
The 2026-09-24 treadmill session logged **32 °C**.

Magnitudes (Périard, Eijsvogels & Daanen 2021, *Physiol Rev*): 40 km TT at 35 vs 20 °C, HR **+8
bpm**; 30-min TT at 32 vs 23 °C, **+4 bpm with 6.5% lower power**; 15-min self-paced at 40 vs
20 °C, **+10 bpm with 17% less work done**. Heat acclimation reverses it and shows how much was
thermal: exercising HR **−10 bpm by day 8**, **−14 bpm** on a 5-day protocol.

Subtle point worth keeping — in the heat, HR is **not** lying about relative cardiovascular strain;
it is lying about mechanical work and about the adaptive stimulus.

### 5.2 Altitude at 1,550 m — where the signal actually lives

**[V] The signal is in EXERCISING HR at a fixed workload, and it decays inside a week.**
Garvican et al. 2014, *IJSPP* 9(3):397-404 — n=20 elite athletes at **1,600 m, essentially Kigali**,
standardised 5-min run at 11 km/h daily for 10 days: mean HR **+5.4% on day 1** (ES 1.01 ± 0.35),
probably still elevated days 2-3, **back to baseline by day 5.** At easy pace that is roughly
**+8 bpm at identical pace, decaying over 4-5 days.**

**Observed in this athlete and consistent with it:** 9.0 kph treadmill runs on **day 3** (09-23,
last 3 km HR 150/149/151) and **day 5** (09-25, 145/147/146). ~4 bpm lower at identical belt speed,
on Garvican's exact timeline.

**[V] Resting HR and HRV have a published NULL at this elevation.** Karlsson, Laaksonen & McGawley
2022, *Front Sports Act Living* 4:852108 — n=32 elite endurance athletes, **17-21 days at 1,800 m**:
resting SpO2, **resting HR** and urine specific gravity **did not change systematically** (p>0.05;
within-subject CV for resting HR **7.2 ± 5.1%**). They declined to measure HRV because "HRV
responses are highly variable."
**So "HRV drops for days at altitude" is well supported above ~2,300 m and poorly supported at
Kigali's elevation. Do not read a recovery score for an altitude effect here** — that channel has
a demonstrated null and ~7% day-to-day CV.

**[V] Why the HR→VO2 calibration breaks anyway.** HRmax declines detectably from **600-700 m** at
~**1.7 bpm per 1,000 m** (Mourot 2018, pooled 86 studies, 322 groups), more in higher-VO2max
individuals — so at 1,550 m expect HRmax ~2.5-3 bpm below sea level and every %HRmax zone computed
against a ceiling that moved. VO2max falls **6.3% per 1,000 m** (Wehrlin & Hallén 2006), so at
1,550 m it is **~8-9% lower.**

**Stated precisely:** because VO2max is ~8-9% lower, a given pace at 1,550 m genuinely **is** a
higher %VO2max — the elevated HR is **right about relative cardiovascular strain and wrong about
mechanical work**. What breaks is the inverse mapping: hypoxia left-shifts the HR/ventilation/
lactate curves against work rate, so any EPOC or hrTSS model converting HR→VO2 on a sea-level
VO2max assigns more aerobic work than was performed. **[P]** — no study validates a Firstbeat-style
model at altitude. The heat case (43%) is the measured one.

**Altitude is not a fixed offset.** In *acclimatised* mountain guides, HR and lactate at a fixed
100 W were "unchanged or even slightly reduced" at 2,000 m. **Do NOT introduce a blanket
"subtract X bpm for altitude" correction — the literature does not support a constant.** The
existing rule (discard HR-derived conclusions under a confounder unless every confounder pushes
the opposite way) is exactly right and should not be replaced by a bpm offset.

**Vendor note:** Garmin/Firstbeat document Heat Acclimation (>22 °C, ~4 days to full) and Altitude
Acclimation (>800 m, weighted by *sleeping* altitude). **COROS has neither.** Garmin's has no
published validation — a claim, not a finding.

---

## 6. What to use instead

Ranked by evidence behind them, best first:

1. **The two-more-reps question and the within-rep plateau.** Already doctrine. Needs no HRmax,
   works unchanged at altitude and in heat. Strictly better than any HR-derived readiness number.
2. **Top-set performance on the four main lifts.** The per-lift hit/miss rule already *is* a
   readiness test with a real criterion, and it self-calibrates.
3. **Session-RPE (RPE x minutes), logged for every session including lifts.** 36 validation
   studies across sports, sexes, ages and levels. The only measure here that prices a heavy squat
   day correctly, and the only one that separated matched-volume heavy from light work (§4.2).
4. **7-day rolling resting HR.** The one genuinely physiological channel on the watch — and the
   Recovery score ignores it.
5. **A single-item readiness/fatigue question — least-bad and free, NOT validated.**
   See the correction below.

**[V] The strongest direct support for this list.** Nuuttila et al. 2024, *Eur J Sport Sci*
24(7):857-869 — 24 recreational runners through a 2-week overload; 8 overreached vs 12 responders.
Nocturnal HR (p=0.002), nocturnal HRV (p=0.011), **the single item "readiness to train" (p=0.009)**
and leg soreness (p=0.04) all separated the groups. **Nocturnal HR, "readiness to train" and an
HR-running-power index each reached ≥85% positive AND negative predictive value.**
Note what this implies about HRV: **over a two-week overload with a real signal, nocturnal HRV
worked.** The failure documented in §2 is *day-to-day* reading, not the channel itself.

**CORRECTION (2026-09-29) — single-item measures are not validated as a class.** Jeffries et al.
2020, *IJSPP* 15(9):1203-1215, a COSMIN review screening 9,446 records: **46.1% of athlete-reported
measures used in sport science are single items, and apart from two reliability studies no validity
studies exist for them at all.** Verbatim: *"The single-item AROMs most frequently used in sport
science have not been validated... all conclusions based on these AROMs are questionable."*
So frame a one-item check as **cheap, responsive and least-bad** — not as validated. Saw et al.'s
support is for *published* instruments (POMS, RESTQ-Sport, DALDA), since inclusion required
published validity; it does not transfer to ad-hoc wellness sliders.

**Saw, Main & Gastin 2016** (56 studies, concurrent subjective and objective measures), verbatim:
*"Subjective and objective measures of athlete well-being generally did not correlate. Subjective
measures reflected acute and chronic training loads with superior sensitivity and consistency than
objective measures."* The objective measures reviewed **included resting and exercise heart rate**.
Precise head-to-head: sensitivity/consistency/timing differed in **46% of studies, 85% of those
favouring subjective** (22 of 54).

**And a warning against building composites — including any of ours.** Saw et al., verbatim:
*"Consolidation of subjective measures into a total score typically resulted in **reduced
sensitivity**, with **one in five** studies reporting both subscale and total scores noting a
change in only the subscale score(s)."* Keep the individual questions separate; do not sum them
into a single readiness number.

**Documented behavioural risk:** users of readiness scores report "more of an emotional response
rather than a rational one" and adjust behaviour specifically to *improve the score*. Optimising
the metric instead of the training is a real failure mode, not a hypothetical one.

**⚠️ Research hygiene:** searches on this topic surface AI-generated content-farm pages citing
studies **that do not exist** (e.g. a "2024 *Front Physiol* study, WHOOP 5.0 Recovery r=0.58 with
morning cortisol" — WHOOP 5.0 launched in 2025). Every citation in this file came from PubMed,
Europe PMC or Crossref primary records. Verify before adding anything here.

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
- Doherty et al. 2025, *Transl Exerc Biomed* 2:128-144 — 14 composite scores, 10 manufacturers
- Nuuttila et al. 2025, *Sensors* 25(2):533 — recovery metrics flat through a deliberate overload
- Nuuttila et al. 2024, *Eur J Sport Sci* 24(7):857-869 — overreaching markers, >=85% PPV/NPV
- Jeffries et al. 2020, *IJSPP* 15(9):1203-1215 — COSMIN review, single-item measures unvalidated
- Palmer & Sleivert 2001, *J Sci Med Sport* 4(4):447-459 — running economy after lifting
- Doma, Deakin & Bentley 2017, *Sports Med* 47(11):2187-2200 — concurrent-training carry-over
- Thomas et al. 2018, *MSSE* 50(12):2526-35 — neuromuscular fatigue to 72 h after 10x5 squats
- Raeder et al. 2016, *JSCR* 30(12):3412-27 — intensified strength block, recovery markers
- Kraft, Green & Gast 2014, *JSCR* 28(7):2042-46 — matched-volume heavy vs light, sRPE vs HR
- Falk Neto et al. 2020, *Front Physiol* 11:919 — all-out vs RPE-6, TRIMP cannot separate
- Sweet et al. 2004, *JSCR* 18(4):796-802 — sRPE rises with %1RM despite less total work
- Bröde & Kampmann 2019, *Ind Health* 57(5):615-620 — HR overestimates metabolic rate by 43% in heat
- Périard, Eijsvogels & Daanen 2021, *Physiol Rev* 101(4):1873-1979 — heat, performance, HR
- Garvican et al. 2014, *IJSPP* 9(3):397-404 — exercising HR at 1,600 m, days 1-10
- Karlsson, Laaksonen & McGawley 2022, *Front Sports Act Living* 4:852108 — resting HR null at 1,800 m
- Mourot 2018, *Front Physiol* 9:972 — HRmax decline with altitude, 86 studies
- Wehrlin & Hallén 2006, *Eur J Appl Physiol* 96(4):404-412 — VO2max 6.3% per 1,000 m
- Rothschild et al. 2024, *Eur J Appl Physiol* 124(11):3279-90 — ML readiness, individual RMSE 5.5-23.6
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
