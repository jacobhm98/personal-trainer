---
name: sync-week
description: Push one full week — running (plans/running.md) AND 5/3/1 strength (Google Sheet, read-only) — to Tredict as ONE plan the user applies once with the week's Monday as start date.
argument-hint: "[week N] [dry-run]"
disable-model-invocation: true
---

Sync a complete training week (runs + lifts) in one flow. Supersedes running
/sync-running and /sync-strength separately; those remain for one-off use.

Arguments: `$ARGUMENTS` — optional `week N` (the `## Week N` block of
`plans/running.md`; its `(of YYYY-MM-DD)` Monday also dates the strength week;
if absent, infer the next un-pushed week from `state/sync-log.md`) and optional
`dry-run` (stop after the confirmation table; make no writes).

## Steps

1. Read `plans/config.md`, `state/sync-log.md`, and `plans/running.md`. Resolve
   the week, its Monday, and the strength day mapping (config `Lifting days`,
   honoring any dated one-off override there or in the week's notes).
2. **Running**: parse each session line against the schema in `plans/running.md`.
   Stop and ask on anything that doesn't parse — never guess. Apply any
   altitude/pace adjustments called out in the week's notes.
3. **Strength**: read the Google Sheet **read-only** via
   `mcp__claude_ai_Google_Drive__read_file_content`
   (fileId `1weU4bSEZPBC6yZgvIe89ZUfcqoV5FJ-mXb8fkMwTRSQ`), last tab = current
   cycle. Validate layout anchors (per-lift TM rows, `Week 1 | Week 2 | Week 3`
   3×3 grids, assistance list, Schedule block; dips/pull-ups grids are *added*
   weight over BW with `TM total` rows and FSL 5x5 markers). Take working weights
   **from the cells**; recompute from TM only as a sanity check and stop on any
   disagreement. Map D1–D4 to dates via the (possibly overridden) day mapping.
4. Check `planned-workout-list` for the week's date range. Existing entries →
   stop and discuss; date moves use `planned-workout-change-date`; **never
   delete-and-recreate** (deletes don't propagate to COROS — CLAUDE.md).
5. Present ONE confirmation table — every run (name, structure, pace targets) and
   every lift (name, all sets as sets×reps@kg incl. FSL and assistance). Show
   paces **human-readable** (`4:10-4:18/km`, `easy 5:15-6:15/km`); put the raw
   Tredict encoding (`254±4 s/km`) in parentheses after, or omit it. If
   `dry-run`, stop here. Wait for explicit confirmation.
6. On confirmation, create ONE plan via `plan-creation` named `W<N>
   (<Monday's date>)` containing all sessions as day-numbered trainings
   (day 1 = Monday):
   - Runs: `sportType: "running"`, steps per CLAUDE.md schema — pace targets via
     `targetMode: "padding"` (sec/km value + padding) on EVERY step, repeats as
     repetition blocks, per-step `note` ≤255 chars, `time` from the session's
     planned hour (minutes from midnight).
   - Lifts: `sportType: "misc"`, `subSportType: "strength_training"`, full set
     table in `notes` (≤2048 chars). Naming `531 W2 D1 Squat` / `Run W2 Mon 4x4`.
7. Append one sync-log row per session; commit plan/log changes if the user has
   asked for commits this session. Tell the user the single manual step: **apply
   the plan in Tredict with the week's Monday as start date** (`show-plan-ui`),
   after which Tredict relays the coming 7 days to COROS within ~3 h. Remind:
   strength entries are scheduling + notes only — record real lifting as a plain
   Strength activity, don't start the scheduled workout on the watch.
