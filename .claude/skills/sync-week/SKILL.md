---
name: sync-week
description: Push one week of the running plan (plans/running.md) straight onto COROS calendar dates with the official COROS MCP. One call per session, no Tredict, no relay, no apply step.
argument-hint: "[week N] [dry-run]"
disable-model-invocation: true
---

Push one running week to the COROS calendar.

**ARCHITECTURE CHANGED 2026-11-08.** This skill used to build a Tredict plan that the
user applied by hand and that Tredict relayed to COROS over a rolling 7-day window.
It now writes **directly to COROS dates** with `createScheduledWorkout`. Read the
**COROS MCP notes** in `CLAUDE.md` before using it — the course schema, the no-delete
rule and the no-per-step-notes limitation all live there.

**STRENGTH IS NOT PUSHED.** His call, 2026-11-08. The COROS MCP cannot author strength
workouts at all, and the relayed entry was only ever a shell. Write the lifting days
into the week block in `plans/running.md` so the week is legible, and leave it there.
`/sync-strength` is retired.

Arguments: `$ARGUMENTS` — optional `week N` (the `## Week N` block of
`plans/running.md`; its `(of YYYY-MM-DD)` gives the Monday; if absent, infer the next
un-pushed week from `state/sync-log.md`) and optional `dry-run` (stop after the
confirmation table; make no writes).

## Steps

1. Read `plans/config.md`, `state/sync-log.md` and `plans/running.md`. Resolve the week
   and its concrete dates. Check the week's notes for anything that changes a target
   (altitude, travel, a venue change, a TT substitution).
2. Parse each run line against the schema at the top of `plans/running.md`. **Stop and
   ask on anything that does not parse — never guess a structure.** Confirm the sub-T
   bands against `sub-threshold-reference.md` §8; **bands move only at a TT**, so a
   review must never have changed one.
3. **Check the target dates on COROS first:** `queryTrainingSchedule` over the week's
   range. Anything already there — stop and discuss. Never push a second copy; there is
   no delete tool, and a duplicate is permanent until he clears it in the app.
4. Build each session as a course (full schema in `CLAUDE.md` → COROS MCP notes):
   - `sportType: 1`. Sections in order, `sectionType` 1 warm-up / 2 training /
     3 recovery / 4 cool-down.
   - **Quality reps**: `targetType: 2` (time, seconds) with
     `intensityType: 2` and absolute `intensityValueStart/End` in **s/km**.
   - **Easy runs and warm-ups**: `targetType: 1` (distance, metres) with
     `intensityType: 1` and absolute **bpm** bounds. Easy = 125–145 under ~75 min;
     past ~75 min, split into 129–145 then 145–155. Warm-ups take a wide floor
     (105–145) so they cannot alert while HR climbs.
   - **Floats and cool-downs carry NO target**: omit `intensityType` and every
     intensity field together. Never send 0. (2026-09-18 amendment — an HR target on a
     cool-down alerts continuously and cannot be met.)
   - Repeated blocks may use `{"intervalGroup": true, "repeats": n, "sets": [...]}`;
     write them flat instead when individual reps need different targets, as a
     gradient-split rep does.
   - **There are no per-step notes** — Tredict had them, he never read them, so nothing
     is lost. `courseDescription` records *why* the session is shaped as it is. **Anything
     that has to land while he is running goes in the workout NAME**, which is what he
     actually sees; the target itself does the rest.
5. Present ONE confirmation table — day, date, name, full structure, paces
   **human-readable** (`4:44–4:50/km`) with the raw s/km in parentheses. If `dry-run`,
   stop here. **Wait for explicit confirmation** (hard rule 3).
6. On confirmation, call `createScheduledWorkout` **once per session**, `date` as
   `yyyyMMdd`. Keep each returned `idInPlan`.
7. **Verify on COROS, not on the plan file** (hard rule 5's surviving lesson):
   `queryTrainingSchedule` over the week — check the **count** is exactly one per day —
   then `queryScheduledWorkoutDetails` on each. Confirm every rep step reads back
   `intensityType: 2` with its absolute s/km bounds, that floats and cool-downs have no
   intensity fields, and that nothing was demoted. **This path is verifiable end to end;
   there is no excuse for an unverified push.**
8. Append one row per session to `state/sync-log.md` (hard rule 4), recording that it
   was a direct COROS write and the verification result. Commit only if asked.
9. Tell him it is on the calendar and to sync the watch. **There is no apply step any
   more** — do not tell him to open Tredict.

## If a pushed session needs changing

`queryScheduledWorkoutDetails` → modify the returned course JSON →
`updateScheduledWorkout` with the same `date` and `idInPlan`. It is a **full
replacement**, not a patch. It works only while the workout is **in the future and not
started** (`editable: true`); a completed or past entry is frozen. It **cannot move a
workout to another date**, and nothing can delete one — both are COROS-app jobs.
