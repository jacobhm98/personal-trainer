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
5. **Deletes don't propagate to COROS, and neither does moving a workout out of the
   relay window.** Deleting a planned workout in Tredict leaves it on the COROS
   calendar (COROS API limitation; manual removal in the COROS app only). Verified
   2026-08-30: rescheduling 8 entries from the coming week to 2027-01-04 did **not**
   clear them from COROS either — the relay is effectively *additive* over its rolling
   7 days. It pushes what Tredict currently has and never removes what it already sent.
   A within-window date change does propagate (used successfully 2026-08-22/23).
   Always prefer *editing* an existing Tredict workout over delete-and-recreate.
   **Never re-apply a plan to fix a wrong start date** — re-applying ADDS a second copy
   rather than moving the first (learned 2026-08-30: produced 16 entries, all 8 stale
   ones stranded on COROS). Fix a wrong start date with `planned-workout-change-date`
   on each entry instead, while it is still inside the 7-day window.

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
  - **Hit it → that lift's TM +2.5 kg.**
  - **Miss it → that lift's TM holds, so it re-runs the same weights next cycle.**

  **This is per-lift, not program-wide** (user corrected 2026-08-30): a missed squat
  top set does not re-run anything for deadlift, dips or pull-ups — they progress on
  their own results. What stays synchronised is the **week number**: all four lifts
  advance W1 → W2 → W3 together, and a single lift is never re-run out of phase with
  the others (see the in-phase rule he stated 2026-08-29). Only the TM progression is
  independent.

  A missed top set is therefore a *hold* on one lift, not a stall, not a reset signal,
  and not a program-wide event. The rule self-calibrates each TM to ~92% of that lift's
  true 1RM (if 95% TM is to equal a 5RM, and a 5RM ≈ 87% of 1RM, then TM ≈ 0.916 × 1RM).
  **Never propose a TM reset off a missed top set — the rule already handles it.**
  Occasional larger resets are acceptable to him but are his call, not a default (sheet
  history shows one: deadlift TM 182.25 → 177.25 mid-history). Corroboration: deadlift
  TM sits at 192.25 in *both* of the last two tabs — that held TM is the record of a
  miss, while squat bumped 161.75 → 164.25 over the same turnover.
- **FSL** back-off sets on **all four main lifts**, at that week's first-set weight:
  - **Dips and pull-ups → 5×5.** Encoded in the sheet as an explicit `FSL 5x5` row.
  - **Squat and deadlift → 3×5.** Reduced from 5×5 on **2026-08-29** to hold lower-body
    volume down while running volume ramps. **Temporary** — revisit once weekly km
    plateaus (~W7–W8 of the running block) or if strength stalls.

  Squat/deadlift FSL is **not in the sheet at all** (user confirmed 2026-08-28) — derive
  it from that week's first-set cell. All weights kg.
- **7th Week Protocol** (Wendler, *5/3/1 Forever*). After **two completed 3-week
  cycles (= 6 weeks)**, week 7 is a dedicated week rather than the start of a new
  cycle. First one scheduled for the week of **2026-09-07** (running W4), which is
  also the running deload — user had not run a purposeful 5/3/1 deload in a long
  time. Two variants:
  - **Deload** (the one chosen for 2026-09-07): `5 @ 40% TM`, `5 @ 50% TM`,
    `5 @ 60% TM`. **No FSL, no PR sets**, assistance minimal or skipped.
  - **TM Test**: `5 @ 70%`, `5 @ 80%`, `5 @ 90%`, then `3-5 @ 100% TM`. Five reps =
    TM is correct and can rise; 3-4 = hold; under 3 = drop it. Don't propose this
    unasked — his hit/miss rule already tests the TM continuously.

  **Loaded-bodyweight caveat:** 40-60% of the dips (115) and pull-up (102.5) TM totals
  all fall *below* bodyweight 80 kg, so those two are simply **3x5 bodyweight** on a
  deload.

  The sheet has **no deload column**, so these are derived from the TM rather than read
  from cells — a sanctioned exception to hard rule 2, alongside squat/deadlift FSL.
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
zones, caveats — read it before changing the plan). **`sub-threshold-reference.md`**
is the sub-T knowledge bank (calibration protocols, pace/HR tiers, drift numbers,
confounders) — read it before touching any sub-threshold session. `plans/running.md` is the
executable weekly schedule the sync skill parses; its schema is defined at the top
of that file. Key paces: easy runs are **HR-governed** (≤140; Thursday's
longest run starts ≤140 and drifts toward ~150). **T-pace 4:40/km** (5k TT 2026-09-15); **sub-T 4:43–4:45
(1–3 min reps) / 4:50–4:52 (4–6 min) / 4:57–4:59 (8–12 min)** — current values live in
`sub-threshold-reference.md` §8, and the next re-anchor is the **W10 5k TT, Fri
2026-10-23**. VO2max work is retired. Sub-T must feel comfortably hard — do not let
sessions drift faster.

**Norwegian realignment (2026-09-03, from running W4):** Mon recovery run, Wed +
Fri **sub-threshold** sessions (bands by rep length, HR ceilings — flat ~180 until
the W4 Wed HRmax pin test 2026-09-09, then %-of-max — and the "two more reps"
rule; see the plan schema), Fri run AM before the deadlift PM, Sun long.
VO2max retired. **No fall 10k (TT scrapped 2026-09-03): base block to 55 km/wk** (ceiling raised 2026-09-16 with the five-run week; peak ~58),
long run → 18k (capped 2026-09-15, then dropped entirely 2026-09-16 — see below), down-weeks ~every 4th week. **Endpoint retired 2026-09-16** — instead a **5k TT every
5th week** as a routine progress check and sub-T re-anchor (09-15 → Fri 2026-10-23 →
Fri 2026-11-27 → ~Fri 2027-01-01), each replacing that week's Friday 4×10. The Dec 6 5k
is dropped: an arbitrary date once a schedule exists. No taper, graded at face value. HR-led calibration
(post-pin %-of-max ceilings; pace bands re-anchored ~every 3 weeks). **No race
until spring/summer 2027** (retargeted 2026-09-16) — autumn/winter is base building proper,
block goal ~60 km/wk.
**Week restructured 2026-09-16 (user's call, from Bakken — two sub-T days plus an X
session for ambitious recreational runners).** Five runs, in force from W6: **Mon** easy
recovery, **Tue** sub-T + D1 Squat, **Wed** D2 Dips (no run), **Thu** easy — the week's
longest run, no lift — **Fri** sub-T + D3 Deadlift, **Sat** D4 Pull-ups, **Sun easy run** (8-14 km). The
**X session is deferred** (2026-09-16) until volume holds ~60 km/wk — two quality days,
not three, while mileage is the priority; **6-8 × 10-15 s hill strides** on the end of
Sunday's run every other week keep turnover alive in the meantime. The **dedicated long run is gone** ("we dont need a dedicated long run, im
not in a marathon block"); Thursday's run carries the decoupling measurement instead, and the full rest day is
spent to buy it (invariant superseded 2026-09-16).
**Hard days hard, easy days easy — stacking OUTRANKS protecting a light day
(user, 2026-09-23).** The concentration principle behind the Tue/Fri doubles is the
*general* scheduling rule, not a quirk of those two days: pair the hard run with the hard
lift so the remaining days are genuinely recovered, and keep easy days actually easy.
His reasoning is the same one behind Norwegian double-threshold days — muscle tone.
**Where this collides with a rule that keeps some particular day light, stacking wins**
and the light-day rule is the one that gives (it superseded "nothing hard on Thursday" in
the Rwanda block). Do not spread hard sessions across the week to be protective — propose
the stacked version and name the cost.

**The full-rest-day invariant is RETIRED (user 2026-09-23)**, replaced by an **optional
easy run on what would have been the clear day** — short, genuinely easy, taken or skipped
by feel. The week is still built with that day in it; it is simply no longer protected by
rule, which matches RPE-gated progression everywhere else. Keep the run short (a shakeout,
not a normal easy run), give it **no calendar entry**, and **state the consecutive-day
streak it creates** when proposing it — removing the structural guarantee is exactly what
lets such a streak grow unnoticed. See `plans/config.md` (Doubles) for the full rule and
the superseded version.

This closes the "nothing above threshold for 13 weeks" hole flagged 2026-09-03.
Sub-T sessions are deliberately unheroic — do not let them drift to threshold.

**`sub-threshold-reference.md` is the single source of truth for sub-T paces, HR
ceilings and session verification.** Read it before prescribing or reviewing any
sub-threshold session. It holds the Bakken material the user relayed 2026-09-11/12:
the two calibration protocols (30-min TT → LTHR → golden zone; 5k TT → Daniels T-pace),
the rep-length pace offsets, the %HRmax tiers, expected HR drift, and the confounders.
If that file and this one ever disagree, **that file wins** — correct this one.

Minimum you must not get wrong without opening it:

- **Verify every sub-T session on three checks**: within-rep plateau (≥6 min reps
  only — shorter reps give a false pass), session-wide HR spread against the expected
  drift band, and the two-more-reps question. All passing easily → creep the pace
  faster; any failing → slow 5 s/km.
- **Expected spread is 7–10 bpm for a 6×6** (5–8 for a 3×10). That is *correct
  execution*, not failure. Under 5 = too easy; over 10–12 = too hot.
- **Sub-T lives at 80–87% HRmax**, tiered by rep length. 88–92% is Daniels T-pace at
  LT2 — a different thing. Do not set sub-T ceilings off the 88–92% anchor.
  **BUT those tiers do not fit this athlete (2026-09-18) — do not prescribe from them.**
  His LTHR is ≈**180–184** (09-15 TT averaged 188; a 5k sits 4–8 bpm above LTHR), so
  83–85% of ~200 = 166–170 lands ~15 bpm *below* his threshold. The 09-18 session held
  the 4:51 band at 185–187 with every rep plateauing. **Sub-T is prescribed on PACE +
  RPE**, verified by the within-rep plateau — which needs no HRmax and works at altitude.
- **Pace is derived, never guessed**: T-pace + 3–5 s/km (1–3 min), +10–12 (4–6 min),
  +17–19 (8–12 min).
- **Rep length alternates; floats are fixed.** In a two-session week the sessions never
  use the same rep length — one 6-min and one 10-min, with a 3-min session as the
  occasional minority. Floats are doctrine, not free parameters: **60 s** after 3- and
  6-min reps, **90 s** after 10-min reps. Both rules have been in §7 since 2026-09-12 and
  both were broken in one session on 2026-09-23 (a second 6-min session proposed against
  an existing one, then a 3×10 built with 60 s floats). **Steps are immutable after
  creation, so getting this right is a push-time obligation, not a review-time one.**
- **This needs the HR stream, not lap averages** — lap data hides float recovery. Get it
  from the **COROS FIT file** (`queryActivityFitFileDownloadUrls` → curl → parse with
  **fitdecode**, not fitparse; see `sub-threshold-reference.md` §6). Strava
  `get_activity_streams` also works when that MCP is connected.
- **When a confounder is present** (illness, alcohol, treadmill heat, bad sleep),
  discard HR-derived conclusions outright rather than asterisking them.
  **One exception, and it is narrow (added 2026-09-25):** if *every* confounder present
  pushes HR the **opposite** way from the observation, it bounds the finding instead of
  explaining it, and the reading stands. Heat and altitude only raise HR at a given effort,
  so they cannot manufacture the 7-10 bpm *drop* the 09-24 Kigali 5x6 showed against the
  matched 09-18 Stockholm one (`sub-threshold-reference.md` §8.3). **Before invoking this,
  name each confounder and its direction** — if even one could have caused what you are
  looking at, discard as normal. This is the same one-directional logic behind the 110-150
  easy band, not a licence to reinstate asterisked conclusions.

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
- **STEPS *CAN* BE EDITED — IN THE WEB UI (corrected 2026-09-23).** This file previously
  said flatly that steps are immutable after creation. That is true only of the **MCP/API**:
  `activity-update` reaches title and notes, nothing else. **The Tredict web UI edits the
  steps of an already-applied calendar workout in place** — verified 2026-09-23, when the
  user changed the 10-01 3x10 floats from 60 s to 90 s: same workout id, `updatedAt` moved,
  duration 3180 -> 3270 s, no duplicate created. So a wrong session is **fixed in the UI**,
  not rebuilt. Do not create a replacement plan, and do not fall back to the
  retitle-as-warning protocol, until the UI edit has been tried. Costly lesson: three plans
  were built for one week on the false assumption, and the user was sent to delete things
  three times for a 30-second float. **Still unverified:** whether a UI step edit inside
  the 7-day relay window propagates to COROS (this one was edited while 10-01 was still
  outside it). The retitle protocol remains the fallback for anything the UI cannot reach.
- **Step schema**: `durationType` distance|time|open (meters/seconds); `intensityType`
  warmup|active|recover|rest|cooldown; interval repeats via
  `{repetitions, steps[...]}`. For our fixed pace prescriptions use
  `targetMode: "padding"` with `targets.pace.value` in **sec/km** + `padding`
  (e.g. 6-min sub-T 4:51 ±3 → value 291, padding 3; 10-min sub-T 4:58 ±3 → value 298,
  padding 3). The default `targetMode`
  "range" is %-of-capacity (ftpa/hrMax) — don't use it unless capacities are set.
  Always set a target on every step or nothing shows on the watch. Per-step
  `note` (≤255 chars) displays on the watch.
  **Easy and long runs are HR-governed (2026-09-12) — push `targetZoneType:
  "heartrate"` with `targets.heartrate {value, padding}`, NOT a pace target.** Also set
  a `targets.pace` value alongside it so Tredict can still compute distance/duration;
  the schema supports both, and the zone type decides which one the watch enforces.
  Easy run ≈ value 130 padding 10 (120–140). Long run is better as **two steps** —
  first half 132±8 (124–140), second half 145±5 (140–150) — since "start ≤140 and let
  it drift" cannot be expressed as one band.
  **Cool-downs are NOT HR-governed (amended 2026-09-18, user's call).** HR decays from
  the last rep instead of settling into a band, so an HR target on a cool-down alerts
  continuously and cannot be met: the 09-18 cool-down opened at 179, averaged 164 and
  never fell below 141 in 4:53. Push cool-downs as **distance only** —
  `durationType: "distance"`, `intensityType: "cooldown"`, **no `targetZoneType`**.
  Every step still needs *some* target or nothing shows on the watch, so set a
  deliberately loose informational pace (**value 450, padding 90 = 6:00-9:00/km**) and
  put "run easy by feel, no HR target" in the step note.
  **Learned the hard way 2026-09-12:** W5's easy 6k and long 14k were pushed with pace
  bands of 5:45–6:15 and the HR cap only in the notes. At 140 bpm he runs ~7:00/km, so
  the watch would have alerted him for being too slow while he was executing correctly.
  The plan was already applied and **steps cannot be edited after creation**, so the
  only remedy was retitling both to "RUN BY HR, IGNORE THE PACE BAND" and telling him to
  start a plain run. Get the zone type right at push time — there is no fix afterwards.
- **`targetMode: "padding"` still needs `targetZoneType` (learned 2026-09-23).** The
  schema only *requires* it for `"range"`, so it is easy to drop — but a padding step
  without it lands as **`targetType: "OPEN"`**, with the value stored as a hint
  (`extraValueSpeed`) rather than a target. Verified on the 10-01 3x10: warm-up carried
  `targetZoneType: "heartrate"` and came through as `HEART_RATE 110-150`, while every
  pace step came through OPEN. **Read the pushed workout back with `planned-workout`
  after any push** — the step JSON shows `targetType` per step, and it is the only way to
  tell a real target from a hint. (This also means the long-standing cool-down recipe —
  loose pace, no zone type — has always produced an OPEN step. That matches its intent,
  "run easy by feel", so leave it; but the claim that every step needs *some* target or
  nothing shows on the watch is unproven.)
- **Treadmill sessions (learned 2026-09-23).** Indoors the watch cannot measure pace —
  the reading is accelerometer-derived and will alert against a correctly-run session —
  so **the belt is the prescription**. Push treadmill runs as **time-based steps**
  (`durationType: "time"`; never `distance`, which ends at the wrong moment on a drifting
  indoor estimate), with **`subSportType: "treadmill"`** and the **belt speed in kph in
  the TITLE** — the title is the only reliable warning surface, same lesson as the
  repurposed-workout rule. Keep a pace target on each step so Tredict can still compute
  effort, and put "set the machine, ignore watch pace" in the notes.
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
