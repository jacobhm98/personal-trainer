# personal-trainer

Claude Code-driven training pipeline: strength plan (Google Sheet) and running plan
(`plans/running.md`) are synced to the COROS training calendar via Tredict.

## Hard rules

1. **Never write to the Google Sheet.** It is the source of truth for strength.
   Read it with `mcp__claude_ai_Google_Drive__read_file_content`,
   fileId `1weU4bSEZPBC6yZgvIe89ZUfcqoV5FJ-mXb8fkMwTRSQ`.
2. **Read weights from the sheet cells — never recompute them from the TM.**
   Recompute only as a sanity check; on any mismatch, stop and ask instead of guessing.
3. **Confirm before pushing.** Every sync shows a full summary table (day, date,
   session, sets×reps@kg or paces) and waits for explicit user confirmation before
   creating anything in Tredict.
4. **Log every push** by appending to `state/sync-log.md`.
5. **Deletes don't propagate to COROS.** Deleting a planned workout in Tredict leaves
   it on the COROS calendar (COROS API limitation; manual removal in the COROS app
   only). Always prefer *editing* an existing Tredict workout over delete-and-recreate.

## Architecture

```
Google Sheet (strength) + plans/running.md
        → skills (/sync-week; /sync-strength + /sync-running for one-offs)
        → Tredict MCP (create/schedule workouts)
        → official COROS Training API (rolling 7 days, resync ~3h; runs AND strength relay)
        → COROS calendar → app → watch
Reads/analysis: official COROS MCP (EU) + Strava MCP + Tredict MCP
```

- Structured **running** workouts reach the watch with pace targets. Targets (pace/HR)
  must be explicitly set on each workout section in Tredict, or they won't show on
  the watch.
- **Strength DOES relay to the COROS calendar** (verified 2026-08-18, contradicting
  Tredict's older run/bike/swim-only docs): misc/strength_training entries pushed
  from Tredict appear on the COROS training schedule with full notes. They open on
  the watch as *followable* sessions, but only as a shell (~4 generic sections, no
  rep/load content — verified 2026-08-19: taps through in ~5 min). **Protocol:
  strength entries are scheduling + notes reference only. Don't start the scheduled
  workout on the watch; record a plain Strength activity for the actual training.**

## The strength program (modified 5/3/1)

- Main lifts: **Squat, Deadlift, Dips, Pull-ups** (dips/pull-ups replace bench/OHP).
- Sheet layout: one tab per cycle, **the last tab is the current cycle**. Layout
  anchors to validate before trusting a parse: a `TM Factor` cell (0.85), per-lift
  blocks with `1RM | TM` rows, a `Week 1 | Week 2 | Week 3` header over a 3×3 grid of
  working weights (rows = sets within the session, columns = week), an assistance
  list at the top, and a `Schedule` block. If anchors don't match, stop and ask.
- Dips and pull-ups TMs are **totals including bodyweight**; the week grid shows
  *added* weight (`BW` = bodyweight only).
- FSL 5x5 back-off sets on dips/pull-ups. All weights kg.
- Day split (from the sheet's Schedule block):
  D1 Squat + Seated DB press + Abs; D2 Dips + Chin-ups + Abs;
  D3 Deadlift + Curl + Abs; D4 Pull-ups + Dips + Abs.
  Assistance: Lunges, Row, Lateral raises.

## Running

`running-training-brief.md` is the coaching reference (history, race data, pace
zones, caveats — read it before changing the plan). `plans/running.md` is the
executable weekly schedule the sync skill parses; its schema is defined at the top
of that file. Key paces: easy 5:15–6:15/km, long 5:45–6:15/km, threshold
4:45–4:55/km, VO2max ~4:00–4:05/km (treadmill 4×4 @ 15.3 kph). Threshold must feel
comfortably hard — do not let sessions drift faster.

## Naming conventions

- Runs: `Run W3 Wed 5x1k @4:50`
- Strength: `531 C13 W2 D1 Squat` — full set×rep@kg table in the workout description.

## Tredict MCP notes (learned 2026-08-17)

- **Scheduling model**: there is no "create workout on calendar date" tool. The flow
  is `plan-creation` (a reusable plan in "My Own Training Plans", workouts keyed by
  `day` number, day 1 = plan start) → **the user applies the plan to a start date in
  the Tredict UI** (one click; `show-plan-ui` opens it) → applied workouts land on
  the calendar and transfer to the watch. So each synced week = one plan named e.g.
  `Run W1 (2026-08-18)`, days numbered from that Monday, and the user applies it
  with that Monday as the start date.
- Prefer `plan-creation` with inline `planTrainings` (Claude has the token budget);
  `add-plan-training` is the one-at-a-time fallback.
- **Step schema**: `durationType` distance|time|open (meters/seconds); `intensityType`
  warmup|active|recover|rest|cooldown; interval repeats via
  `{repetitions, steps[...]}`. For our fixed pace prescriptions use
  `targetMode: "padding"` with `targets.pace.value` in **sec/km** + `padding`
  (e.g. easy 5:15–6:15 → value 345, padding 30; threshold 4:45–4:55 → value 290,
  padding 5; VO2max 4:00–4:05 → value 243, padding 3). The default `targetMode`
  "range" is %-of-capacity (ftpa/hrMax) — don't use it unless capacities are set.
  Always set a pace target on every step or nothing shows on the watch. Per-step
  `note` (≤255 chars) displays on the watch.
- `time` on a plan training = minutes from midnight (default 1020 = 17:00).
- **Strength**: `sportType: "misc"` + `subSportType: "strength_training"` works as a
  structured Tredict entry (set table in `notes`, ≤2048 chars). Rest days:
  `trainingType: "note"` + `subSportType: "rest_day"`.
- Reads: `planned-workout-list` (CSV, calendar), `planned-workout` (structure),
  `planned-workout-change-date` (move a scheduled entry), `activity`/`activity-list`
  (executed), `capacity`, `zones`, `bodyvalues`, `hrv-list`, `sleep-list`,
  `training-effort-list`.
- Workout URL for the user: `https://www.tredict.com/app/training/activity/:id`;
  calendar: `https://www.tredict.com/app/training`.

## Config

Training days, timezone, bodyweight, and the current sheet tab name live in
`plans/config.md`. Sync history lives in `state/sync-log.md`.
