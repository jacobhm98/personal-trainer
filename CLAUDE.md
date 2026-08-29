# personal-trainer

Claude Code-driven training pipeline: strength plan (Google Sheet) and running plan
(`plans/running.md`) are synced to the COROS training calendar via Tredict.

## Hard rules

1. **Don't write to the Google Sheet unless explicitly told to.** It is the source of
   truth for strength. Read it with `mcp__claude_ai_Google_Drive__read_file_content`,
   fileId `1weU4bSEZPBC6yZgvIe89ZUfcqoV5FJ-mXb8fkMwTRSQ`. Writes are allowed only on a
   direct instruction naming the change (amended 2026-08-29, when the Schedule block was
   edited on request): use the `gws` CLI
   (`gws sheets spreadsheets values update`; strip the leading `Using keyring backend:`
   line before parsing JSON). Always dump the tab to the scratchpad as a backup first,
   and never touch TM/1RM/percentage cells without being asked.
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
- **5s PRO**: main-lift work sets are straight 5s (5/5/5 at the week's percentages),
  no AMRAP/plus sets — write set tables as `5@weight`, never `3+@`/`5+@`
  (documented 2026-08-27; user clarified 2026-08-29 he has been running 5s PRO **the
  entire time** — it was just never written down). Do NOT read the sheet's
  65/75/85 - 70/80/90 - 75/85/95 grid as classic 5/3/1 with AMRAP top sets.
- **Progression rule (user's own, confirmed 2026-08-29).** The target is **5 reps on
  the top set every week**, and it should feel like roughly a **5RM**. Then:
  - **Hit it → TM +2.5 kg.**
  - **Miss it → re-run the week at the same TM.**

  So a missed top set is a *re-run trigger*, not a stall and not a reset signal. The
  rule self-calibrates the TM to ~92% of true 1RM (if 95% TM is to equal a 5RM, and a
  5RM ≈ 87% of 1RM, then TM ≈ 0.916 × 1RM). **Never propose a TM reset off a missed
  top set — the rule already handles it.** Occasional larger resets are acceptable to
  him but are his call, not a default (sheet history shows one: deadlift TM 182.25 →
  177.25 mid-history). Corroboration: deadlift TM sits at 192.25 in *both* of the last
  two tabs — that held TM is the record of a miss-and-re-run, not a stable ceiling.
- **FSL** back-off sets on **all four main lifts**, at that week's first-set weight:
  - **Dips and pull-ups → 5×5.** Encoded in the sheet as an explicit `FSL 5x5` row.
  - **Squat and deadlift → 3×5.** Reduced from 5×5 on **2026-08-29** to hold lower-body
    volume down while running volume ramps. **Temporary** — revisit once weekly km
    plateaus (~W7–W8 of the running block) or if strength stalls.

  Squat/deadlift FSL is **not in the sheet at all** (user confirmed 2026-08-28) — derive
  it from that week's first-set cell. All weights kg.
- Day split (from the sheet's Schedule block, restructured 2026-08-29) — **exactly
  3 exercises per day**:
  D1 Squat + Row + Seated DB press; D2 Dips + Chin-ups + Abs;
  D3 Deadlift + Curl + Lateral raises; D4 Pull-ups + Dips + Abs.
  The standalone Assistance day (Lunges, Row, Lateral raises) was **removed** — Row and
  Lateral raises folded into D1/D3; Lunges is now unused (its 80 kg reference is still in
  the assistance weight list at the top of the tab). **Abs is 2x/week (D2, D4), not
  daily** — user doesn't want it every session, and not on back-to-back lifting days.

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
