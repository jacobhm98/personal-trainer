---
name: training-review
description: Read-only review of planned vs executed training — adherence, pace vs target on quality sessions, ramp rate, and load/recovery flags, read primarily from the official COROS MCP (Strava as supplement).
argument-hint: "[period, default: last 7 days]"
---

Compare what was planned against what actually happened. Read-only: this skill
never creates, edits, or deletes anything anywhere.

Arguments: `$ARGUMENTS` — optional period (e.g. `last 14 days`, `week 3`);
default last 7 days.

## Steps

1. Establish the plan for the period: `state/sync-log.md`, `plans/running.md`,
   and the strength week from the sync-log (weights are in the logged names/refs —
   don't re-read the sheet unless detail is missing).
2. Pull execution data — **COROS MCP first** (the watch's own data is the source of
   truth; do not rely on Tredict for review data, it is the push channel only):
   - Official COROS MCP: `querySportRecords`/`getActivityDetail` +
     `queryActivityLapData` for interval splits, `queryTrainingLoadAssessment`,
     `querySleepData`/`querySleepHrv`, `queryRecoveryStatus`,
     `queryFitnessAssessmentOverview`.
   - Strava MCP only for what COROS lacks (e.g. segment/stream comparisons).
3. Assess:
   - **Adherence**: each planned session done / moved / skipped.
   - **Quality execution**: interval paces vs targets. Flag threshold sessions run
     faster than 4:45/km — running threshold too fast is the failure mode called
     out in `running-training-brief.md` §5.
   - **Sub-T verification** — mandatory on every sub-threshold session, from
     `queryActivityLapData`. Report all three: (1) **within-rep HR plateau** on reps
     ≥6 min ONLY — on shorter reps it gives a false pass, and lap averages are not
     enough for any of this: pull the HR stream from Strava `get_activity_streams`
     (COROS MCP has no time series) — must level off in the second half, still climbing at every rep's end
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
   - **Long-run decoupling (Pa:HR)**: compute for **every long run** and append the
     result to the log table in `running-training-brief.md` §5. Use the fixed
     convention defined there — drop the first 2 km, split the remainder in half,
     drop the middle km if odd. **Never compute it over the whole run**; the opening
     km is HR onset kinetics and inflates the number badly. Report the value against
     the trend, not as a pass/fail on one run.
   - **Recovery**: HRV/sleep/load flags from COROS data, especially in a caloric
     deficit (the brief expects some squat stall — that's the trade, not a problem).
4. Report a concise summary: per-session table, then findings, then suggested
   adjustments. Suggestions are never auto-applied — plan changes go through the
   user editing `plans/running.md` / the sheet, then a re-sync.
