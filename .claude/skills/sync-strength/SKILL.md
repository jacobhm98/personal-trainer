---
name: sync-strength
description: Push a week of the 5/3/1 strength program (from the Google Sheet, read-only) to the Tredict calendar as planned entries with full set/rep/weight detail.
argument-hint: "[week 1|2|3] [start YYYY-MM-DD] [dry-run]"
disable-model-invocation: true
---

Sync one week of the 5/3/1 cycle to the Tredict calendar.

Arguments: `$ARGUMENTS` — optional `week 1|2|3` (which week of the current cycle;
if absent, infer the next un-pushed week from `state/sync-log.md`), optional
`start YYYY-MM-DD` (date of the week's first session), optional `dry-run` (stop
after the confirmation table; make no writes).

Strength entries relay from Tredict to the COROS training calendar (verified
2026-08-18). Push them as misc/strength_training with the full set table in the
notes — the notes travel with the entry to COROS. On the watch they open as
followable sessions but only as a content-free shell (verified 2026-08-19), so
they serve as scheduling + notes reference only: the user records the actual
lifting as a plain Strength activity and does not start the scheduled workout.

## Steps

1. Read `plans/config.md` and `state/sync-log.md`. If the strength day mapping in
   config is still `TBD`, stop and ask which calendar days D1–D4 land on.
2. Read the Google Sheet **read-only** via
   `mcp__claude_ai_Google_Drive__read_file_content`
   (fileId `1weU4bSEZPBC6yZgvIe89ZUfcqoV5FJ-mXb8fkMwTRSQ`). The **last tab** is the
   current cycle. Validate the layout anchors from CLAUDE.md (TM Factor 0.85 cell,
   per-lift `1RM | TM` rows, `Week 1 | Week 2 | Week 3` grid, Schedule block). On
   any mismatch, stop and ask — never guess.
3. Extract the chosen week's four sessions, taking working weights **directly from
   the cells** (never recompute from the TM; recompute only to sanity-check, and
   stop on disagreement). Remember dips/pull-ups grids show *added* weight over
   bodyweight (`BW` = bodyweight only), plus FSL 5x5 back-offs and the assistance
   list.
4. Check `planned-workout-list` for existing entries on the target dates; if the
   week was already synced, stop and discuss rather than delete-and-recreate
   (deletes don't propagate to COROS; see CLAUDE.md).
5. Present a confirmation table: day, date, session name (`531 C13 W2 D1 Squat`
   convention), and every set as sets×reps@kg including FSL and assistance. If
   `dry-run` was given, stop here.
6. On explicit confirmation, create ONE plan via `plan-creation` named for the week
   (e.g. `531 C13 W2 (2026-09-01)`), each session a day-numbered training with
   `sportType: "misc"`, `subSportType: "strength_training"`, and the full set table
   in `notes` (≤2048 chars; also per-step notes if steps are used). Day 1 = the
   week's first session day.
7. Append one row per session to `state/sync-log.md`, then tell the user to apply
   the plan in Tredict with the right start date (`show-plan-ui` opens it).
