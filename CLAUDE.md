# personal-trainer

Claude Code-driven training pipeline: the running plan (`plans/running.md`) is written
**directly to the COROS training calendar** by the official COROS MCP. The strength plan
(Google Sheet) is **no longer pushed to any calendar at all**.

> **ARCHITECTURE CHANGED 2026-11-08 — TREDICT IS OUT OF THE WRITE PATH, AND STRENGTH IS OFF
> THE WATCH.** His call, after the COROS MCP was found to have gained direct calendar writes:
> *"ok, its fine i think lets just drop the strength from the watch. ill still record them
> manually."* Two separate decisions in one sentence, both deliberate:
> 1. **Running is pushed straight to COROS** with `createScheduledWorkout`. No Tredict, no
>    relay, no manual apply step, no rolling 7-day window — and therefore **no duplication
>    class and no vanishing entries.** Both of those failure modes were properties of the
>    relay, and the relay is gone.
> 2. **Strength is not pushed anywhere.** The COROS MCP cannot author strength (see below),
>    and the Tredict relay only ever delivered a content-free shell. The calendar entry was
>    doing nothing the sheet and the week block do not already do. He records a plain
>    Strength activity himself, exactly as the old protocol already told him to.
>
> **Hard rule 5 and the Tredict MCP notes are kept below as LEGACY.** They are not dead
> letters — they document real incidents, they still govern anything already on the calendar
> from the old path, and they are what to re-read if the write path ever moves back.

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
5. **LEGACY FROM 2026-11-08 — THIS RULE GOVERNS THE TREDICT RELAY, WHICH IS NO LONGER THE
   WRITE PATH.** Read it for entries pushed before 2026-11-08, and before ever restoring the
   relay. For new pushes, the COROS MCP notes below govern. **The one line that still applies
   to everything, old path and new: THERE IS NO DELETE TOOL ANYWHERE. COROS app only.**
   **Deletes don't propagate to COROS, and neither does moving a workout out of the
   relay window.** Deleting a planned workout in Tredict leaves it on the COROS
   calendar (COROS API limitation; manual removal in the COROS app only). Verified
   2026-08-30: rescheduling 8 entries from the coming week to 2027-01-04 did **not**
   clear them from COROS either — the relay is effectively *additive* over its rolling
   7 days. It pushes what Tredict currently has and never removes what it already sent.
   A within-window date change does propagate (used successfully 2026-08-22/23).
   **BUT "ADDITIVE" DOES NOT MEAN "RE-SENDS" — IT SENDS EACH ITEM ONCE (2026-11-06).** The
   relay tracks what it has already delivered. The W12 Friday v2 sat in Tredict on 11-06,
   inside the window, through **six-plus ~3 h resync cycles**, and COROS stayed empty.
   **So a missing COROS entry will NEVER appear by waiting** — that was my assumption and it
   is wrong. Re-check, then fix it actively.
   **AND A DELIVERED COROS ENTRY CAN VANISH ON ITS OWN — FIRST CASE 2026-11-06.** v2 relayed
   within 2 minutes of the apply and I verified it on the calendar at 11-05 19:52Z. By
   11-06 14:55Z the day held **nothing**. He deleted exactly once and it was **v1**
   (*"well i deleted v1, but not v2"*). Mechanism unknown — a queued app-side delete that
   caught the day rather than the entry, or a relay reconciliation pass. **Do not assert a
   cause without new evidence.** What this does NOT overturn: a Tredict delete still does not
   propagate. What it DOES overturn: "COROS keeps what the relay sent" is falsified, so
   **a verified push is no longer permanently verified — re-check on the morning of a
   session that matters.**
   Always prefer *editing* an existing Tredict workout over delete-and-recreate.
   **Never re-apply a plan to fix a wrong start date** — re-applying ADDS a second copy
   rather than moving the first (learned 2026-08-30: produced 16 entries, all 8 stale
   ones stranded on COROS). Fix a wrong start date with `planned-workout-change-date`
   on each entry instead, while it is still inside the 7-day window.
   **THE RELAY DUPLICATES ENTRIES ON COROS BY ITSELF, FROM A SINGLE APPLY — TWICE NOW, AND
   A CLEAN TREDICT CALENDAR IS NOT EVIDENCE AGAINST IT.**
   - **2026-09-23:** three entries duplicated (09-23 dips, 09-24 squat, 09-24 run) from one
     application; all 9 Tredict entries shared one `updatedAt`. Logged verbatim: *"I wrongly
     suggested he had applied twice; he had not."*
   - **2026-10-26 (W11):** **eight** duplicated. Tredict held exactly 9 on a single apply
     timestamp (08:42:53.524 -> .626) with no strays from 10-19 to 12-31; COROS held **17**
     under one plan, `idInPlan` **108-116** then **117-124**. The two batches are the **same
     payload in the same non-date order**: A was [dips, Mon, Sun, Tue, pull-ups, DL, Thu, Fri,
     squat] and B is that list with its **first** item dropped. One source list, sent twice,
     the second pass off by one. **User: "i think i only applied it once, i only see the
     singular entries in tredict calendar. that leaves the tredict -> coros relay as broken."**
   - **NEVER DIAGNOSE THIS AS A DOUBLE APPLY.** I did it on 09-23 and again on 10-26 — the
     second time against a repo row that already said so, and against my own log sentence
     ("a ~100 ms spread, i.e. a single apply") written two sentences earlier.
     `grep -n duplicat state/sync-log.md` takes seconds, and the
     `verify-claims-about-own-records` memory exists for exactly this. A one-off double apply
     IS real and documented (2026-08-30, 16 entries), but **it shows up IN TREDICT**. If
     Tredict holds one copy per session, the relay did it — do not blame the user's click.
   - **SO VERIFY A PUSH ON COROS, NOT TREDICT:** end every push with `queryTrainingSchedule`
     over the pushed window and check the count. The 10-26 verification read all 9 Tredict
     steps back, passed, and never looked at the calendar that matters; **he found the
     duplication both times, not me.**
   - **HIS CALL, 2026-10-26: LEAVE THEM — cleanup is not a priority.** *"as long as at least
     one session is in coros calendar itll show up in my watch."* The copies are identical, so
     whichever he opens is the right session, and reviews read *executed* activities, not
     planned entries. Cost is doubled TL estimates (already junk — HRmax unset) and clutter.
     **Do not push cleanup.** If he ever asks for it: manual deletion in the COROS app only —
     the plan library is **empty** (checked statusList `[0,1,2]`), so the relay's plan is not
     an MCP-editable execution record, and the official COROS MCP ships **no delete tool**.
   - **THE COROS MCP WRITES DIRECTLY TO THE CALENDAR — USE IT WHEN THE RELAY FAILS
     (2026-11-06).** `createScheduledWorkout` puts **one standalone workout** on a date with
     full step structure: sections, interval groups, and per-section absolute targets
     (`intensityType` 1 = HR bpm, 2 = pace **s/km**, 4 = power W; omit all intensity fields to
     leave a step with no target, which is how floats and cool-downs stay silent). Date must be
     today..+90 d. Siblings: `updateScheduledWorkout` (full-course replacement, by date +
     idInPlan), `createSingleWorkout` (library, no date), `scheduleWorkout`. **This bypasses
     Tredict, the relay and the entire duplication class** and is the remedy when a session
     must be on the watch today. Used successfully for the W12 Friday 3x10 — 8 sections,
     per-rep pace targets, read back byte-exact.
     Costs to name before using it: it lands as a **standalone**, outside the relayed plan, and
     **there is still no delete tool**, so moving or removing it is COROS-app-only. Prefer the
     normal Tredict path when there is time for a relay cycle; this is the rescue path.
   - **`queryTrainingPlanDetails` IS NOT A WITNESS FOR WHAT IS ON THE CALENDAR.** On 2026-11-06
     it reported 11-02, 11-03, 11-04 and 11-06 all as `Rest day` while `queryTrainingSchedule`
     showed real workouts on the first three. The record it returns is flagged *"not a valid
     execution copy"*. **Decide presence/absence with `queryTrainingSchedule`.**

## Architecture

```
plans/running.md
        → /sync-week
        → official COROS MCP: createScheduledWorkout, ONE call per session
        → COROS calendar → app → watch
          [no relay · no apply step · no 7-day window · writable today..+90 d]

Google Sheet (strength)
        → the week block in plans/running.md  (reference only — pushed NOWHERE)
        → he records a plain Strength activity on the watch himself

Reads/analysis: official COROS MCP (EU) + Strava MCP + Tredict MCP (READS ONLY now)
```

**LEGACY, until ~2026-11-15:** entries relayed by Tredict before 2026-11-08 are still on the
calendar and still cannot be deleted over the API. Hard rule 5 governs those. Anything pushed
from 2026-11-09 onward is a COROS standalone and obeys the COROS MCP notes instead.

- Structured **running** workouts reach the watch with pace targets. Targets (pace/HR)
  must be explicitly set on each workout section in Tredict, or they won't show on
  the watch.
- **STRENGTH IS OFF THE WATCH FROM 2026-11-08 — DO NOT PUSH IT ANYWHERE.** His call. The
  COROS MCP **cannot author strength**: `sportType` accepts 1 running / 2 cycling / 5 trail
  running (4 = rest, plans only), and every create tool carries a `strengthBodypart` field
  documented *"Strength training is not supported; must stay null."* The one path that exists
  is `scheduleWorkout`, which can place a strength workout that **already exists in the COROS
  workout library** — and the library is empty, so authoring it would be an app job. Declined:
  the relayed entry was never more than a shell, so nothing is lost. **The lifting week still
  gets WRITTEN into the plans/running.md week block** as days + session names so the week is
  legible; it simply is not pushed. Weights stay in the Google Sheet. He records a plain
  Strength activity after the session, which is what the protocol below already required.
  **Historical, and the reason the entry was worth so little:**
- **Strength DID relay to the COROS calendar** (verified 2026-08-18, contradicting
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
  **SCOPE OF THE IN-PHASE RULE — clarified 2026-10-12 after I read it too broadly.** It
  constrains the **week number each lift is on**, not the calendar date a session lands.
  **A late session is fine.** On 2026-10-12 I told him C14 W2's deadlift and pull-ups were
  "unrecoverable" because squat and dips had already done W2 — wrong. He corrected it:
  *"we can do deadlifts and pullups today then begin w3 on tuesday with squat and dips
  switched around to increase gap between deadlifts and squat."* Finishing W2 for **all
  four** lifts before **any** of them starts W3 is perfectly in phase; every lift still
  runs W1 → W2 → W3 in order. What the rule actually forbids is one lift being *at* W2
  while the others are *at* W3. **So a broken week is caught up by compressing the missing
  sessions, not by writing them off** — check whether catch-up is possible before ever
  calling a session lost.
  **And the DAY ORDER inside a week is free to reshuffle.** D1→D2→D3→D4 is his design
  preference, not a constraint: **swapping D1 Squat and D2 Dips is nearly free, because
  dips are `upper` and draw nothing from the legs**, which makes it the cheapest lever for
  buying deadlift→squat gap in a compressed week. He proposed it; I had not considered it.

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
- **Assistance is 3 sets per movement** (user, 2026-10-05 — asked because **nothing in the
  repo or the sheet recorded it**; the sheet carries assistance *weights* only). Reps are
  **not prescribed** — he takes assistance sets to near-failure, which is why they are valid
  E1RM input. Write them as `3x@weight`, never with an invented rep count. Expected set
  counts per session, useful as a cross-check against `querySportRecords`' set counter:
  **D1 15, D2 14, D3 12, D4 14** (3 main + FSL + 2 x 3 assistance, where FSL is 3x5 on
  squat/deadlift and 5x5 on dips/pull-ups). **D1 IS 15, NOT 12 — THE ROW IS ONE SET PER ARM AND
  THEREFORE LOGS TWICE (his correction, 2026-11-24:** *"yea but fuckin rows are one per arm"***).**
  Verified on the 11-24 D1: 15 logged = Legs/Hips 6 + Back 6 + Shoulders 3, an exact match on all
  three movements, with the Back lap reps falling in pairs (11/7, 8/7, 5/5). **This INVERTS the
  historical reading rather than refining it:** D1 had logged **13/13/14** against the old expected
  12 and the surplus was written up as a counted warm-up, so a "+1/+2 warm-up bias" entered
  `state/srpe-log.md` as a recurring explanation. Against 15 those sessions were **1-2 sets SHORT**
  — dropped assistance, most likely — and the warm-up-bias reading has no support from D1.
  **D3 IS UNVERIFIED AND MAY BE 15 TOO:** its assistance is Curl + Lateral raises, and an
  alternating or single-arm curl would log per arm on the same logic. Do not assume either way —
  check the lap count on the next D3 before using 12 as a cross-check. Corroborated elsewhere:
  COROS logged **14 sets** for the 09-23 D2 session.

## Running

`running-training-brief.md` is the coaching reference (history, race data, pace
zones, caveats — read it before changing the plan). **`sub-threshold-reference.md`**
is the sub-T knowledge bank (calibration protocols, pace/HR tiers, drift numbers,
confounders) — read it before touching any sub-threshold session.
**`wearable-metrics-reference.md`** is the validity bank for every watch-derived
number — read it before citing any recovery, sleep, HRV or load figure in a review.
Minimum you must not get wrong: **no COROS wrist sensor has ever been validated for
HR, HRV or sleep [X]**; nightly **HRV error is 4-6x the smallest worthwhile change**
(7-day rolling mean only, never a single night); **sleep stage minutes are not a
measurement** (deep-sleep ICC 0.13-0.36 vs PSG — never cite them); **Recovery %
excludes sleep, HRV, stress and muscular fatigue by COROS's own written statement**,
so it means "you have not run much lately"; **Load Ratio is an ACWR**, a metric with
"no evidence supporting [its] use" (Impellizzeri 2020); and the HR-only load model
prices a heavy squat session at **~8% of a sub-T run** against sRPE's ~80%. The one
metric that earns a conclusion is the **7-day rolling resting HR** (noise floor
±3.2 bpm; act on a sustained ≥3-4 bpm shift). A hard session **should** suppress HRV
and raise overnight HR for 24-48 h — that is the intended response, not a flag.
Two more that bear directly on the plan: **lifting costs ~2.6% running economy at 1 h
and ~1.6% at 8 h with NO change in exercising HR** (Palmer & Sleivert 2001), which is
why run-AM/lift-PM is the right order and why no watch metric can see the interference;
and at 1,550 m the altitude signal lives in **exercising HR at a fixed workload**
(+5.4% day 1, gone by day 5 at 1,600 m), **not** in resting HR or HRV, which have a
published null at this elevation. In heat, HR-estimated work overstates by **43%**. `plans/running.md` is the
executable weekly schedule the sync skill parses; its schema is defined at the top
of that file. Key paces: easy runs are **HR-governed at 70% of max [B]** — with max **~207** that is **≤145** (raised from ≤140 on **2026-10-08** with the HRmax assumption; the cap is a fraction of max, so it rescales with it). **THE DRIFT ALLOWANCE IS GATED ON DURATION, NOT ON WHICH DAY IT IS:** under ~75 min, one band, **≤145**; past ~75 min, open **≤145** and let it drift to **~155** (75%, **[C]** — that ceiling is mine, not Bakken's, see `sub-threshold-reference.md` §2). The old "Thursday's longest run starts ≤140 and drifts toward ~150" was a **text substitution made by `395fb71` (2026-09-16)**, the commit that *dropped* the dedicated 12–18 km long run — "long" became "Thursday's longest" and was never re-derived. It failed inspection on 2026-10-08 against a 7 km / 52 min Thursday: 20 bpm of drift in 52 minutes is not cardiac drift, it is running too hard. **T-pace 4:40/km** (5k TT 2026-09-15); **sub-T 4:43–4:45
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
Fri 2026-11-27 → ~Fri 2027-01-01), each replacing that week's Friday 3×10. The Dec 6 5k
is dropped: an arbitrary date once a schedule exists. No taper, graded at face value. HR-led calibration
(post-pin %-of-max ceilings; pace bands re-anchored ~every 3 weeks). **No race
until spring/summer 2027** (retargeted 2026-09-16) — autumn/winter is base building proper,
block goal ~60 km/wk.
**Week restructured 2026-09-16 (user's call, from Bakken — two sub-T days plus an X
session for ambitious recreational runners).** Five runs, in force from W6: **Mon** easy
recovery, **Tue** sub-T + D1 Squat, **Wed** D2 Dips (no run), **Thu** easy, no lift
— ~~the week's longest run~~ **NO LENGTH CLAIM: "the week's longest run" was STRUCK 2026-10-26**
as a *second* `395fb71` text substitution (the HR half of the same clause was struck 2026-10-08;
see Key paces above). In his 09-16 design **Sunday was the X session**, so Thursday was trivially
the longest *easy* run; once the X session was deferred and Sunday became an 8-14 km easy run,
that stopped being true and was never re-derived. **Sunday's 8-14 km is the only sourced number
in the pair**, and the decoupling slot follows **the week's longest easy run wherever it lands**,
not a named day — **Fri** sub-T + D3 Deadlift, **Sat** D4 Pull-ups, **Sun easy run** (8-14 km). The
**X session is deferred** (2026-09-16) until volume holds ~60 km/wk — two quality days,
not three, while mileage is the priority. **THE HILL STRIDES THAT STOOD IN FOR IT ARE ALSO
RETIRED (user 2026-10-26:** *"remove the strides and just go with a regular prescribed long
run. we arent at the mileage target yet where we can start adding in more intensity"***) and
are deferred to the SAME ~60 km/week gate.** **AND THAT GATE IS NOW CLOSED BY SOMETHING ELSE (2026-11-24): the third hard slot is SPENT ON STRENGTH.** His call — *"we should take some time to stabilize and re-introduce strength training into the routine now. we can stop pushing the mileage up next few weeks."* Volume holds near 60 while the four-day 5/3/1 week is re-established, so **a volume plateau from here is NOT the gate opening** — it exists for the opposite reason. Do not read ~60 km held as permission to add the X session or the strides. Full reasoning: `plans/running.md`, the CONSOLIDATION block above the step table. So **the only thing above threshold in this block
is the 5k TT every 5 weeks** — a deliberate, dated deferral, not an oversight. **Do not
re-pitch the strides.** Superseded: *"6-8 × 10-15 s hill strides on the end of Sunday's run
every other week keep turnover alive in the meantime."* The **dedicated long run is gone** ("we dont need a dedicated long run, im
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

- **SUB-T PACE MOVES ONLY AT A TT (user's call 2026-10-09).** *"why dont we just keep the
  sub-T paces and then readjust based on the regularly scheduled TT's. i think the hr checks
  should just be a vibe check."* The bands are **derived from a measured 5k** (T-pace + the
  §2 rep-length offsets) and are **re-anchored only by the next TT** — every 5th week, same
  route, grade-adjusted. **Do not hand-move a band off a review.** This reverts an accretion,
  not the architecture: the 2026-09-12 signal split already said "HR *diagnoses* at review",
  and the retired verdict rule ("all three passing easily → creep faster; any failing → slow
  5 s/km") had quietly turned a diagnosis into a prescription.
- **The three checks are still RUN and REPORTED — as a vibe check, with no pace consequence.**
  (1) within-rep plateau (≥6 min reps only — shorter reps give a false pass), (2) session-wide
  HR spread against the expected drift band, (3) the **reserve question**. Report all three
  every time. **Only the reserve check still carries a decision**, and it is an *abort*
  decision inside the session, never a pace edit afterwards. If an HR check comes back
  grossly off — no plateau anywhere, spread far outside the band, reps sitting at the LTHR
  estimate — **say so and ask him**; look for illness, heat or sleep. Do not move the band.
- **Why this is the right call.** The HR machinery produced "unscoreable" far more often than
  a decision: spread was unscored on 10-01 and unattributable on 10-07 (both heat), treadmill
  execution cannot be audited from pace at all, and every HR anchor it leans on is flagged in
  the files as **not a measurement** — LTHR 180–184 is derived, HRmax ~207 is an assumption.
  Pace rests on a measured TT. Prescribing off the measured quantity and merely *checking*
  with the unmeasured ones is the correct ordering. It also closes the error class that
  produced two Bakken misattributions, the circular treadmill finding and the withdrawn
  "4:50–52 runs hot" argument — all of them attempts to extract a pace decision from HR.
- **The cost, named: the TTs are now load-bearing.** With no between-TT correction, a
  mis-executed TT propagates for five weeks. Protect TT day and run the same route.
- **The reserve question SCALES with rep length — it is not "two more reps" flat.** He
  finishes with ~**a third of the session's work** left: **two more reps on a 6×6, three
  on a 10×3, ONE more on a 3×10.** Two more 10-min reps is **+67%** of a 3×10 — a
  different question, and it was asked wrongly on 2026-10-01. **It is my inference,
  tagged [C] in `sub-threshold-reference.md` §4.3 — NOT Bakken**, which it predates by
  nine days. Do not attribute it.
- **Expected spread is 7–10 bpm for a 6×6** (5–8 for a 3×10). That is *correct
  execution*, not failure. Under 5 = too easy; over 10–12 = too hot.
- **Sub-T lives at 80–87% HRmax**, tiered by rep length. 88–92% is Daniels T-pace at
  LT2 — a different thing. Do not set sub-T ceilings off the 88–92% anchor.
  **BUT those tiers do not fit this athlete (2026-09-18) — do not prescribe from them.**
  His LTHR is ≈**180–184** (09-15 TT averaged 188; a 5k sits 4–8 bpm above LTHR), so
  83–85% of ~207 = **172–176**, still ~8 bpm *below* his threshold — the 2026-10-08 rescale from max 200 (where 83–85% = 166–170, ~15 bpm below) **narrows the gap without closing it**, so the rule stands. The 09-18 session held
  the 4:51 band at 185–187 with every rep plateauing. **Sub-T is prescribed on PACE +
  RPE**, verified by the within-rep plateau — which needs no HRmax and works at altitude.
- **Pace is derived, never guessed**: T-pace + 3–5 s/km (1–3 min), +10–12 (4–6 min),
  +17–19 (8–12 min).
- **THE WEEK IS A FIXED 6×6 PLUS A 2:1 ROTATION (his call 2026-10-28); floats are fixed.**
  **Tuesday is always the 6×6**; **Friday rotates 3×10 → 3×10 → 10×3**, repeating, anchored at
  **W12 (of 11-02)**: W12 3×10 · W13 3×10 · W14 **10×3** · **W15 TT** · W16 3×10 · W17 3×10 ·
  W18 **10×3** · W19 3×10 · **W20 TT** · W21 3×10 · W22 **10×3**. **A TT week does not consume
  a rotation slot** — it takes that Friday and the rotation resumes at the same position, so
  the 2:1 ratio holds over the sessions actually run. Tuesday holds the anchor precisely
  because the TT already displaces Friday, so the constant survives every TT. **W11 is the
  exception and is NOT retro-fitted** (*"its fine this isnt the case this week"*). Superseded
  generator: ~~"in a two-session week the sessions never use the same rep length — one 6-min
  and one 10-min, with a 3-min session as the occasional minority"~~ — **but it is not
  violated, only demoted**: 6+10 and 6+3 both still avoid repeating a rep length inside a week,
  so alternation is now a consequence rather than the rule that builds the week. **The 10×3 is
  no longer the "minority"** — every third rotation week, which makes the missing 10×3 spread
  anchor a recurring gap (§4.2: do not invent one) and puts the 45 s float on a regular test
  cadence. The one thing traded away is 10-minute-rep exposure, from weekly to two weeks in
  three; work minutes are unchanged, since a 3×10 and a 10×3 are **both 30 min of work**. Full
  layout and reasoning: `sub-threshold-reference.md` §7. Floats are doctrine, not free parameters — **but only on the
  long reps: 60 s** after 6-min reps and **90 s** after 10-min reps, both **[B]**.
  **THE 3-MIN FLOAT IS NOT DOCTRINE AND IS NOT SOURCED** (corrected 2026-10-26, on his
  question *"is it really 60s float for the 3 min intervals?"*). `sub-threshold-reference.md`
  says the opposite twice — *"on 6- and 10-min sessions the floats are specified (60 s /
  90 s) [B]"*, naming **two** values, and *"the float remains negotiable only on the
  short-rep sessions"* — and §5 makes the 3-min float the **primary adjustment lever**:
  *"on 3-min sessions, lengthen the float before slowing the pace."* This file had hardened
  a table entry into a third sourced rule. **AND THE NUMBER IS NOW 45 s — his call
  2026-10-27** (*"45seconds is a more suitable rest for this interval length, 1min is what we
  do for 6min reps, which is literally double the length. lets note this down and do it going
  forwards"*). **Push 3-min sessions with 45 s floats (work:rest 4 : 1).** His argument is
  proportionality and it holds: at 60 s a 3-min rep took **3:1** while a 6-min rep takes 6:1
  and a 10-min 6.7:1, so the shortest rep was getting twice the relative recovery of the
  staple — and even at 4:1 it stays the most generous of the three. It is also **descriptive,
  not an escalation**: the 10×3 pushed with 60 s floats was *executed* at 31.5/44.6/44.4/46.7/
  43.7/44.4/45.7/44.7 s (mean 44.9 s for floats 2–8), so the prescription now matches what he
  runs. 45 s sits inside documented practice (45–90 s, one published plan at 45 s) and the §7
  research had already concluded the 3-min float was the loose one of the three. It remains a
  choice to defend per session, not a constraint, and on a short-rep session it is the **only**
  lever, since pace moves only at a TT — with the lever now running **upward from 45 s**. Both rules have been in §7 since 2026-09-12 and
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
  easy band (**that band is RETIRED — see Running; it was a Kigali heat/altitude measure left unreverted until 2026-10-08**), not a licence to reinstate asterisked conclusions.

## Naming conventions

- Runs: `Run W3 Wed 5x1k @4:50`
- Strength: `531 C13 W2 D1 Squat` — full set×rep@kg table in the workout description.

## COROS MCP notes — THE WRITE PATH from 2026-11-08

**Tool surface, as verified 2026-11-06 and 2026-11-08.** Everything here was read off the live
schemas or exercised; where something is contract-only and untested, it says so.

- **`createScheduledWorkout`** — puts ONE workout on ONE date, **today .. +90 days**. Saves to
  that date only; **nothing enters the workout library**. Returns `idInPlan`, which is the
  handle for any later read or edit. **VERIFIED END TO END 2026-11-06** — 8 sections with
  per-rep pace targets, read back byte-exact. This is the tool we use.
- **`updateScheduledWorkout`** — edits one standalone scheduled workout by `date` + `idInPlan`.
  **FULL REPLACEMENT, not a patch:** always `queryScheduledWorkoutDetails` first and modify the
  course JSON it returns. **VERIFIED WORKING 2026-11-08** — a one-string description fix on the
  11-10 entry came back with the **same `idInPlan`, all sections intact and no second entry
  created.** Full replacement behaves as documented.
  - **THE `editable` GATE IS REAL AND IT IS VERIFIED (2026-11-08):** the 11-06 entry reads back
    `Editable via MCP: no`, reasons *"already completed"* and *"in the past"*. **Updates reach
    future, un-started workouts only. Nothing retroactive.**
  - **It CANNOT move a workout to another date.** App only.
- **Library layer** — `createSingleWorkout`, `queryWorkoutLibrary`, `queryWorkoutDetails`,
  `updateWorkoutDetails`, `scheduleWorkout`. Reusable templates, any sport. **His library is
  EMPTY (verified 2026-11-08) and we do not use it.** Know one thing about it: a scheduled copy
  is **independent** of its template, so editing the template changes nothing already on a date.
  `scheduleWorkout` is the ONLY route by which a strength workout could reach the calendar, and
  it needs the workout authored in the COROS app first.
- **Plan layer** — `createTrainingPlan` / `updateTrainingPlan`. 4–16 natural weeks, start within
  **today .. +14 days**, day-granular incremental edits, completed days protected and reported.
  **NOT USED, deliberately:** one week of standalone workouts is simpler, and a plan object is
  one more undeletable thing. Reconsider only if we ever want months on the calendar at once.

**THERE IS STILL NO DELETE TOOL. ANYWHERE.** Not scheduled workouts, not library workouts, not
plans. COROS app only. Combined with "cannot move a date", **the cost of a wrong push is
unchanged from the Tredict era — get it right at push time.**

**Course schema — the parts we actually use.**

- `sportType` **1 = running** · 2 cycling · 5 trail running · 4 rest (training plans only).
- `sectionType` **1 warm-up · 2 training · 3 recovery · 4 cool-down.** Inside an interval
  group's `sets`, only 2 and 3 are allowed.
- `targetType` **1 distance (m) · 2 time (s)** · 3 climb (m, trail only) · 4 free mode.
  **Running allows 1/2/4 only.** Integer meters / integer seconds.
- `intensityType` **1 = HR bpm · 2 = pace s/km · 4 = power W**, set **per section**, never on
  the course. Pace is **total seconds per kilometre** — 4:47/km = 287.
- Exactly ONE intensity format per section: `sectionIntensity` (zone 1–6),
  `intensityPercentStart/End` (% of COROS thresholds), or `intensityValueStart/End` (absolute).
  **WE USE ABSOLUTE AND ONLY ABSOLUTE** — his COROS thresholds are derived from an HRmax that is
  still unset, so zones and percentages would be built on the junk documented in
  `wearable-metrics-reference.md`. Bounds: HR 30–240, pace 120–1499 s/km, power 10–2000 W.
- **TO LEAVE A STEP WITH NO TARGET, OMIT `intensityType` AND EVERY INTENSITY FIELD TOGETHER.**
  Never send 0 — a 0 is "provided and invalid". This is how **floats and cool-downs stay
  silent**, which the 2026-09-18 cool-down amendment requires.
- Interval groups: `{"intervalGroup": true, "repeats": 1-20, "sets": [...]}`. **No nesting.**
  The container omits `intensityType`, `targetType`, `targetValue` and all intensity fields —
  those go on the member sections.

**MOVING OFF TREDICT COST US NOTHING IN PRACTICE.** There are no per-step notes in the COROS
schema — `Section` has no note field, and the only text anywhere is course-level `courseName`
and `courseDescription`. Tredict did carry a ≤255-char note on every step, **and he never read
them** (*"i literally never used the notes"*, 2026-11-08). So this is a difference, not a
regression, and **it must not be written up as a limitation again.**

**WHAT ACTUALLY REACHES HIM MID-SESSION IS THE TARGET AND THE NAME — THAT IS THE WHOLE LIST.**
`courseDescription` is read in the app beforehand if at all; treat it as the record of *why* the
session is shaped the way it is, not as a delivery mechanism for an in-session cue. **If a cue
has to land while he is running, it goes in the workout NAME** — the same conclusion the
repurposed-workout rule and the treadmill belt-speed rule reached independently.
**BUT A PACE CUE IS NOT SUCH A CUE — HIS CALL 2026-11-15:** *"you dont need to add pacing cues
into the workout names lol."* **The name carries WARNINGS, not targets.** The pace band is
already delivered by the step structure and shows on the watch screen, so repeating it in the
name is pure duplication; a `@5:01-5:08` in a title tells him nothing the workout itself is not
already telling him. **What still belongs there is anything the structure CANNOT express** — a
repurposed or moved session, a treadmill belt speed, "RUN BY HR, IGNORE THE PACE BAND", a venue
warning. Those are the cases the rule was written for, and they stand. **Keep names short and
descriptive — `Run W13 Sun 3x10 sub-T` — and do not re-pitch pace-in-the-title.**
**THE GENERAL LESSON, WHICH IS THE EXPENSIVE PART: I RECORDED A CAPABILITY AS LOAD-BEARING
WITHOUT CHECKING WHETHER IT WAS USED.** A feature that exists is not a feature that matters.
Ask before building a rule around one — see the `dont-record-predictions-as-constraints` memory,
of which this is the mirror image.

**THE SCHEDULE-LEVEL DISTANCE ESTIMATE UNDERSTATES ANY SESSION WITH UNTARGETED FLOATS — DO NOT
READ IT AS THE SESSION DISTANCE (2026-11-08).** COROS computes it from the targeted sections
only, because a step with no pace target yields no derivable distance. The 11-10 6x6 displays
**11.21 km** (= 2000 + 6x1286 + 1500) against a real **~12.3**; the 11-13 3x10 displays
**10.10** against **~11.0**. The floats are real running and simply are not counted. **Never
"fix" this by putting a target on a float** — silent floats are required by the 2026-09-18
amendment and the estimate is a display field, not the prescription. The same artifact afflicted
relayed Tredict entries, where it was logged as a staleness bug; it is neither stale nor a bug.

**PACE TARGETS READ BACK, SO A PUSH IS VERIFIABLE END TO END.**
`queryScheduledWorkoutDetails` returns `intensityType: 2` with absolute `intensityValueStart/End`
in s/km, no `Degradation:` line, nothing demoted to OPEN. **This is the thing a relayed Tredict
entry could never do** — see the scope correction in the legacy notes below. **Verify every push
this way**, and still count the day with `queryTrainingSchedule`.

**GRADE-ADJUSTED EFFORT PACE EXISTS AND WE CANNOT USE IT YET — BUT IT IS THE RIGHT ANSWER TO
ROLLING-TERRAIN SUB-T.** `intensityType: 3` is COROS Effort Pace: grade-adjusted to the slope
underfoot, which is exactly what the 2026-11-03 session needed (32 s/km of grade-adjusted spread
from a single flat pace target) and what the 11-06 out-and-back solved by hand-splitting a rep.
**Two blockers, both real:** it is **trail running only** (`sportType: 5`), and it accepts
**only zones or percent ranges of his COROS lactate threshold pace — never an absolute**, which
puts it back on the unset-threshold problem. **Revisit the moment the COROS profile has a real
HRmax and threshold pace.** Until then, hand-split reps by gradient.

**Dates resolve in his COROS profile timezone** (UTC if it cannot be determined, and the result
says so). The 11-06 push landed on the correct date, so it is working — but **re-check after any
travel**, since this replaces the old Tredict-profile-timezone trap rather than removing it.

**Arg traps that still apply:** dates are **`yyyyMMdd`**, never ISO. On the read tools every
optional filter is listed `required` — **pass `null`, never `0`.** Both are documented at length
in the training-review skill and both have cost real time.

## Tredict MCP notes — LEGACY from 2026-11-08 (learned 2026-08-17)

**This is no longer the write path.** Kept because it governs every entry pushed before
2026-11-08, because the Tredict MCP is still used for reads, and because it is what to re-read
before ever restoring the relay. **Do not build a new push on anything in this section.**


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
  three times for a 30-second float. The retitle protocol remains the fallback for anything
  the UI cannot reach.
  **IN-WINDOW UI EDITS DO PROPAGATE TO COROS — verified 2026-09-25.** This was the open
  question left by the 09-23 entry. Two proofs on the 09-29 entry, edited while inside the
  relay window: the **title** changed on COROS from "Run W7 Mon" to "Run W7 Tue" within
  minutes, and **step durations** carried (10-01 estimates 54:30 = 600+120+3x(600+**90**)+480,
  the edited floats). **Pace targets are strongly indicated but not proven**: after the
  edit both quality sessions return `Degradation: Absolute pace values cannot be represented
  as whole seconds per kilometer` with the work rep *omitted* from the structure and an
  explicit warning not to read that absence as "no target" — and absolute pace values exist
  on those steps only because they were just added, since an OPEN step has nothing to
  degrade. **The COROS read API cannot render a pace target back on a RELAYED PLAN workout**,
  so the step-level state of anything pushed through Tredict is not directly inspectable; the
  watch screen is the only definitive check for those. **Scope corrected 2026-11-06 — this is
  a property of relayed plan entries, NOT of the COROS API.** An MCP-created *standalone*
  workout reads back fully: `queryScheduledWorkoutDetails` returned `intensityType: 2` with
  absolute `intensityValueStart/End` in s/km on every rep, no `Degradation:` line, nothing
  demoted. So a push made with `createScheduledWorkout` can be verified end to end — the only
  path that currently can be. Note also that
  the schedule-level **distance estimate goes stale** after an edit (09-29 still read 8.57 km
  against ~10.95 km implied by a 12.0 kph target) — it is a display field, not the
  prescription, so do not read it as evidence either way.
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
  Easy run ≈ value **135** padding 10 (**125–145**) — rescaled 2026-10-08 with max 200 → 207 (was 130±10 = 120–140). **Only a run past ~75 min** gets the two-step treatment — first half **137±8 (129–145)**, second half **150±5 (145–155)** — since "open ≤145 and let it drift" cannot be expressed as one band. A shorter easy run takes the single band; the duration gate is the rule, not the day of the week.
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
  tell a real target from a hint. **A pace target reads back as `targetType: "SPEED"` with
  `targetValueLow/High` in METRES PER SECOND, not as `"PACE"` in sec/km** (verified
  2026-10-13): 4:48–4:54/km came back as 3.4014–3.4722 m/s. Invert with 1000/value before
  judging it, and do not read `SPEED` as the wrong zone type. (This also means the long-standing cool-down recipe —
  loose pace, no zone type — has always produced an OPEN step. That matches its intent,
  "run easy by feel", so leave it; but the claim that every step needs *some* target or
  nothing shows on the watch is unproven.)
- **Treadmill sessions (learned 2026-09-23, corrected 2026-09-25).** The belt is still the
  prescription, and **pace targets DO belong on treadmill rep steps — but not because the
  watch measures indoor pace.** Corrected again 2026-10-01, by the user: *"pace logs exactly
  when i specify it in the watch, i only take care to do this for the live intervals or when
  im doing steady state runs."* **He enters the belt speed on the watch for rep and
  steady-state segments, and does not bother for floats.** So the 09-24 match — reps 2–5 at
  **305.1 s/km against a belt at 305.08** — is **his own typed-in number read back, not an
  independent measurement.** The "accurate to hundredths" claim was circular and is
  withdrawn; so is the 09-25 reading of his floats as "~9.9 kph against a prescribed 8",
  which was just an unentered accelerometer estimate (same artifact on 10-01: floats logged
  382–424 s/km). **What survives is stronger for rep steps and now mandatory for the rest:**
  an entered segment logs the prescription faithfully, so a pace target has something real
  to check against — while **floats and cool-downs MUST stay OPEN**, because he does not
  enter those and an estimate would alert against a correctly-run session. **So set
  `targetZoneType: "pace"` on treadmill rep steps** with padding wide enough to cover the prescribed fallback speed (±5 s/km ≈
  ±0.2 kph). The user asked for this explicitly, twice — 2026-09-23 ("why no target zone?
  they've had one before when i do it on treadmill") and 2026-09-25 ("id like for it to
  contain the actual pace bands in the workout, thats more important than the title").
  **Caveat — and it is the important one.** Because the logged pace on an entered segment
  is his own input, **watch pace can never corroborate the belt**: the two agree by
  construction, and a miscalibrated belt would log its wrong speed just as cleanly. There
  is no mismatch to detect, so **treadmill execution cannot be audited from pace at all** —
  only cadence, HR and duration are independently measured. Judge these sessions on those,
  and on what he tells you (same conclusion `sub-threshold-reference.md` §7 reached from the
  09-24 ramp/pause errors: ask rather than reconstruct). Keep floats and
  cool-downs OPEN; they should never alert.
  ~~Push treadmill runs as **time-based steps**
  (`durationType: "time"`; never `distance`, which ends at the wrong moment on a drifting
  indoor estimate)~~ — **THE TIME-BASED RULE IS DEAD, KILLED 2026-11-23 BY EVIDENCE AND BY HIM**
  (*"wtf where did this rule come from. definitely push the kms"*). **Two things were wrong with
  applying it.** (1) **It lives in this LEGACY section, whose own header says "Do not build a new
  push on anything in this section"** — I took a Tredict-era rule and applied it to a COROS push,
  which is exactly what that header forbids. (2) **The premise is empirically false on COROS:** the
  2026-11-19 treadmill run was pushed as two 6300 m DISTANCE steps and came back at **12.61 km
  against 12.60 prescribed.** No drift. **PUSH TREADMILL RUNS IN KILOMETRES like any other run.**
  **What DOES survive from this paragraph, because it rests on his own behaviour rather than on a
  guess about the device:** the **belt speed in kph in the TITLE** (the one sanctioned exception to
  the no-pace-cues-in-names rule, since the belt is a warning the step structure cannot express),
  **pace targets on rep steps**, **floats and cool-downs left OPEN** because he does not enter those,
  and **execution cannot be audited from pace at all** — judge treadmill sessions on cadence, HR and
  duration. Original text, for the record: with **`subSportType: "treadmill"`** and the **belt speed in kph in
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
