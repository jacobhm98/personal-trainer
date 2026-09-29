---
name: training-review
description: Read-only review of planned vs executed training — adherence, pace vs target on quality sessions, ramp rate, and load/recovery flags, read primarily from the official COROS MCP (Strava as supplement).
argument-hint: "[period, default: last 7 days]"
---

Compare what was planned against what actually happened. **Read-only except for two
named logs**: the decoupling table in `running-training-brief.md` §5 and
`state/srpe-log.md` (step 4). It never edits plans, the sheet, or Tredict.

**Read `wearable-metrics-reference.md` before citing ANY watch-derived recovery,
sleep, HRV or load number.** Most of them are not measurements — see step 3.

Arguments: `$ARGUMENTS` — optional period (e.g. `last 14 days`, `week 3`);
default last 7 days.

## Steps

1. Establish the plan for the period: `state/sync-log.md`, `plans/running.md`,
   and the strength week from the sync-log (weights are in the logged names/refs —
   don't re-read the sheet unless detail is missing).
2. Pull execution data — **COROS MCP first** (the watch's own data is the source of
   truth; do not rely on Tredict for review data, it is the push channel only):
   - Official COROS MCP: `querySportRecords`/`getActivityDetail` +
     `queryActivityLapData` for interval splits; **`queryRestingHeartRate`** for the
     RHR series (NOT the summary header in `queryDailyHealthData`, which is a
     different field — that mistake was made twice on 2026-09-28/29);
     `queryDailyHealthData` for sleep duration and steps; `querySleepHrv` for the
     HRV series. **`querySleepData` no longer exists** — use `querySleepOverview`.
   - **Do NOT report `queryRecoveryStatus`, `queryTrainingLoadAssessment` output, or
     Training Effect / Training Focus as findings.** Pull them only if the user asks
     what the watch says; then say what they are worth (step 3, Recovery).
   - Strength sessions: `querySportRecords` with `sportTypeCodes: [402]` returns
     duration, set count and avg HR — needed for step 4.
   - Strava MCP only for what COROS lacks (e.g. segment/stream comparisons).
3. Assess:
   - **Adherence**: each planned session done / moved / skipped.
   - **Quality execution**: interval paces vs targets. Flag sub-T reps run faster
     than the band for their rep length (current bands: `sub-threshold-reference.md` §8) — running threshold too fast is the failure mode called
     out in `running-training-brief.md` §5.
   - **Sub-T verification** — mandatory on every sub-threshold session, from
     `queryActivityLapData`. Report all three: (1) **within-rep HR plateau** on reps
     ≥6 min ONLY — on shorter reps it gives a false pass, and lap averages are not
     enough for any of this: pull the HR stream from the COROS FIT file
     (`queryActivityFitFileDownloadUrls` -> curl -> fitdecode; Strava
     `get_activity_streams` if connected) — must level off in the second half, still climbing at every rep's end
     means the pace is above threshold; (2) **late-rep plateau** — do the final reps
     still level off *within themselves*? Judge that, not the raw rise from rep 2:
     cardiac drift means spread is expected even at
     constant lactate — Bakken's figure for a 6x6 is **7-10 bpm**, so score it as
     <5 = too easy (creep faster), 7-10 = correct, >10-12 = too hot (slow 5 s/km);
     scale down to 5-8 for a ~33 min 3x10; (3) **two-more-reps** — ask him. All
     passing easily → propose creeping the pace faster; any failing → propose 5 s/km
     slower next session. Full rule and rationale in CLAUDE.md (Running).
   - **Ramp rate**: actual weekly km. Progression is **RPE-gated, not
     percentage-capped** (user's call 2026-09-07) — build off what he actually ran and
     do not re-propose a ~10%/week ceiling. The constraints that still bind are the
     long run growing ~1 km/week and the niggle rule.
   - **Decoupling (Pa:HR)**: compute for **the week's longest easy run** — Thursday from W6 (the dedicated long run was dropped 2026-09-16) — and append the
     result to the log table in `running-training-brief.md` §5. Use the fixed
     convention defined there — drop the first 2 km, split the remainder in half,
     drop the middle km if odd. **Never compute it over the whole run**; the opening
     km is HR onset kinetics and inflates the number badly. Report the value against
     the trend, not as a pass/fail on one run.
   - **Recovery — MOST OF THESE NUMBERS ARE NOT MEASUREMENTS.** Full evidence and
     citations in `wearable-metrics-reference.md`; the operative rules:
     - **Report the 7-day rolling resting HR and nothing else as the headline.** Noise
       floor ±3.2 bpm (within-person CV 6%). Act only on a **sustained ≥3-4 bpm shift**
       with no alcohol/altitude/heat/illness/travel explanation. Ignore <2 bpm.
     - **HRV: 7-day rolling mean only, never a nightly value.** Measurement error is
       **4-6x** the smallest worthwhile change, so a single night needs a ~25-30% swing
       to clear noise — i.e. alcohol or illness, not training.
     - **NEVER cite sleep stage minutes or a sleep score.** Deep-sleep ICC vs PSG is
       0.13-0.36; per-night bias −43 to +73 min. Total sleep time is usable as a
       **weekly** trend only, treated as an upper bound (~30 min inflated), needing
       ≥3 nights.
     - **Recovery %, Load Ratio, Training Effect and Training Focus are not findings.**
       COROS states in writing that Recovery excludes sleep, HRV, stress and muscular
       fatigue; Load Ratio is an ACWR ("no evidence supporting the use of ACWR",
       Impellizzeri 2020). If the user asks, say what they are; never build a
       recommendation on them.
     - **A hard session SHOULD raise overnight HR ~4-5 bpm and suppress HRV for
       24-48 h (≥48 h after high intensity). That is the intended response, not a
       flag.** A PM lift moves it more than an AM run.
     - **Confounder direction is the whole game.** Discard HR-derived conclusions when
       a confounder is present, UNLESS every confounder present pushes the *opposite*
       way from the observation (then it bounds the finding). When they all push the
       *same* way as the observation, attribution is impossible — say so rather than
       naming a cause. At 1,550 m the altitude signal lives in **exercising HR at a
       fixed workload** (+5.4% day 1, gone by day 5), **not** in resting HR or HRV,
       which have a published null at this elevation.
     - **No caloric deficit from 2026-09-16** (cut abandoned, weight held ~80 kg), so a
       squat stall no longer has that excuse — treat a missed top set as real evidence
       about the TM or about running load.
4. **ASK FOR AN RPE ON EVERY LIFTING SESSION IN THE PERIOD, THEN LOG IT.**
   User's instruction, 2026-09-29: *"in the /training-review make sure to ask me for an
   RPE on lifting sessions, that's how i'll log it."*
   - **Why this is not optional.** HR-derived load prices a heavy squat session at
     **~8% of a sub-T run** (measured on his own 2026-09-24 data) where sRPE prices it
     near 80%. Matched-volume experiments confirm it is structural: at equal total work,
     sRPE separates heavy from light while recovery HR does not, and an HR-zone model
     could not distinguish an all-out session from a deliberately easy one (p=0.085).
     **Without the RPE there is no valid record of his lifting load at all** — the
     watch's weekly load is a running-only ledger.
   - **How to ask.** One short question per lifting session, naming the session and its
     date so he can place it: *"RPE for Tue's squat session (0-10)?"* Batch them into a
     single question when the period has several. Ask **plainly, in the report** — do
     not use a question tool for this, and do not block the rest of the review on it.
   - **Then append to `state/srpe-log.md`**, one row per session:
     `| date | session | duration (min) | RPE | sRPE (AU) | notes |` where
     **sRPE = RPE x duration in minutes**. Duration and set count come from
     `querySportRecords` (`sportTypeCodes: [402]`). Leave RPE blank rather than guessing
     if he does not answer; **never invent one**, and never back-fill an RPE from HR.
   - **Once ~6-8 sessions are logged**, report weekly sRPE totals (runs + lifts) as the
     load picture instead of the watch's number, and say plainly that this is the only
     validated load measure in the system.
   - Ask the same way for **runs** only if he offers; the runs already have the
     two-more-reps question and the plateau check doing this job.
   - **Do NOT sum RPE answers with other subjective items into a composite score.**
     Consolidating subjective measures into a total *reduces* sensitivity — one in five
     studies saw a change only in a subscale, not the total (Saw et al. 2016). Keep the
     numbers separate.

5. Report a concise summary: per-session table, then findings, then suggested
   adjustments. Suggestions are never auto-applied — plan changes go through the
   user editing `plans/running.md` / the sheet, then a re-sync.
