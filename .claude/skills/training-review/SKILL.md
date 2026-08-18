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
   - **Ramp rate**: actual weekly km vs the ~10%/week rule; flag jumps.
   - **Recovery**: HRV/sleep/load flags from COROS data, especially in a caloric
     deficit (the brief expects some squat stall — that's the trade, not a problem).
4. Report a concise summary: per-session table, then findings, then suggested
   adjustments. Suggestions are never auto-applied — plan changes go through the
   user editing `plans/running.md` / the sheet, then a re-sync.
