---
name: sync-running
description: Push a week of the running plan (plans/running.md) to the COROS calendar via Tredict as structured workouts with pace targets.
argument-hint: "[week N] [dry-run]"
disable-model-invocation: true
---

Sync one week of the running plan to COROS via the Tredict MCP.

Arguments: `$ARGUMENTS` — optional `week N` (which `## Week N` block of
`plans/running.md` to push; if absent, infer the next un-pushed week from
`state/sync-log.md`, or the week containing today if nothing is logged) and
optional `dry-run` (stop after the confirmation table; make no writes).

## Steps

1. Read `plans/running.md`, `plans/config.md`, and `state/sync-log.md`. Resolve
   which week to push and the concrete dates (the week header holds the Monday;
   sessions map Mon/Wed/Fri/Sun per the schema).
2. Parse each session line (`- <Day> | <Type> | <structure>`) into a structured
   workout: warm-up, main set (repeats with pace ranges and recoveries), cool-down.
   If a line doesn't parse cleanly against the schema documented in the file, stop
   and ask — never guess a workout structure.
3. Check `planned-workout-list` for existing entries on the target dates. If the
   week was already synced (sync-log row or matching calendar entries), stop and
   discuss — never delete-and-recreate (deletes do not propagate to COROS; see
   CLAUDE.md). Date moves for already-applied workouts use
   `planned-workout-change-date`.
4. Present a confirmation table: day, date, workout name (`Run W3 Wed 5x1k @4:50`
   convention), and full structure with paces. If `dry-run` was given, stop here.
5. On explicit confirmation, create ONE plan via `plan-creation` named for the week
   (e.g. `Run W3 (2026-09-01)`), with each session as a day-numbered training
   (day 1 = the week's Monday; set `time` from config). Build steps per the schema
   notes in CLAUDE.md: pace targets in `targetMode: "padding"` (sec/km + padding)
   on EVERY step, interval repeats as repetition blocks, per-step watch notes.
6. Append one row per session to `state/sync-log.md` (pushed-at, plan ref like
   `run W3 Wed`, date, name, Tredict plan id).
7. Tell the user the one manual step: **apply the plan in Tredict with the week's
   Monday as the start date** (use `show-plan-ui` to open it). Once applied,
   Tredict relays the coming 7 days to COROS within ~3 h — verify the first
   session on the watch/app.
