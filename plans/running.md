# Running plan

Distilled from `running-training-brief.md` §4–5 (compiled 16 Aug 2026, day after the
Midnattsloppet 10k). Direction: 4 runs/week, ramp ~10%/week from ~28 to ~38 km/week,
long run is the priority variable (12 → 16–18 km), quality alternates
threshold → VO2max with threshold as the majority stimulus.

**Realigned 2026-09-03 (from W4, user decision): Norwegian-singles structure.**
Mon recovery run, **Wed + Fri sub-threshold sessions** (Fri run AM, deadlift PM),
Sun long run. VO2max sessions dropped entirely; fast running returns only as
10k-race-pace sharpening in the final 3 weeks. **TT moved: Sun 2026-11-01**, target
**sub-45** (was Oct 11 / 45:00-45:30) — gated by a 5k tune-up TT on Oct 18 (see W9).
Rationale: threshold time was ~14 min/wk on the old plan; the singles structure
accumulates 50-60 min/wk at a tolerable intensity. Sparked by Bakken's
*The Norwegian Method Applied* (2026).

## Schema (parsed by /sync-running)

Each week is a `## Week N (of YYYY-MM-DD)` block (date = the Monday). Each session:

```
- <Day> | <Type> | <structure>
```

- Types: `Easy`, `Quality`, `Long`.
- Structure segments separated by `;`. `WU`/`CD` = warm-up/cool-down.
  Repeats: `5x(1km @ 4:50/km, 60s jog)`. Continuous: `20min @ 4:50/km` or `8km @ 5:15-6:15/km`.
- Paces (min/km): easy 5:15–6:15, recovery 5:45–6:15, long 5:45–6:15,
  threshold 4:45–4:55, VO2max 4:00–4:05 (retired from the weekly rotation 2026-09-03).
- **Sub-threshold bands** (Norwegian singles, set 2026-09-03) — scale by rep length:
  3min reps 4:48–4:55, 6min reps 4:55–5:00, 8–10min reps 5:00–5:05. Controls, in
  order: the pace band; the **HR ceiling**; finish every session able to do two more
  reps. If any of the three says too hot, slow the rep. HR ceilings: flat **~180**
  until the W4 Wed HRmax pin test (2026-09-09); after the pin, **≤90% of max for 3min reps,
  ≤88% for 6min, ≤86% for 8–10min** (end-of-rep values — HR lags on short reps).
  The 2026-09-02 tempo at 181 avg was over the line. These sessions are deliberately
  unheroic — accumulation is the stimulus. Do not race them.
- Day roles (from W4): **Mon recovery run AM, squat PM** (user set 2026-09-03: in
  any week with a proper Sat rest day, squats are on Monday — the W3 Mon-dips/
  Tue-squat swap is the fallback for broken weeks only), **Wed sub-T** (48 h after
  the squat), **Fri sub-T in the morning, deadlift in the evening** (≥6 h gap,
  always run first), **Sun long** (48 h after deadlift).
- Mon stays the lightest run of the week (rule set 2026-08-31): it follows Sunday's
  long run. Evidence: 2026-08-31 easy 8k ran 5:38/km at HR 169 on the same route and
  profile as 2026-08-27's 5:37/km at HR 164 — **+5 bpm for the same pace**, the only
  difference being ~20 h after a 13 km long run.
- **A Friday deadlift top-set miss is now confounded** with the same-morning sub-T
  run — attribute it honestly at review time; the per-lift hit/miss rule absorbs it
  either way (a miss just holds that TM).

## Week 1 (of 2026-08-17) — post-race recovery + ramp start, travel week, ~24 km

- Tue | Easy | 5km @ 5:30-6:15/km
- Thu | Quality | WU 2km easy; 4x(1km @ 4:50/km, 60s jog); CD 1.5km easy
- Sun | Long | 11km @ 5:45-6:15/km

Notes: work travel in Denver. Originally built around a Fri-evening flight (Sat rest
in transit, Sun double); flight later moved to Tue 25th, so as executed: Mon squat,
Tue easy, Wed dips, Thu 4x1k, Fri deadlift, Sat long run (moved from Sun), Sun
pull-ups only. Three runs instead of four; the dropped easy 5k is the cheapest cut
in a post-race week. Threshold cruise intervals open the block gently.

## Week 2 (of 2026-08-24) — travel week, reshuffled, ~35 km

- Mon | Quality | WU 2km easy; 4x(4min @ 4:10-4:18/km, 3min jog); CD 1.5km easy
- Tue | Easy | 8km @ 5:15-6:15/km
- Thu | Easy | 8km @ 5:15-6:15/km
- Sun | Long | 13km @ 5:45-6:15/km

Notes (reshuffled 2026-08-21): flight home moved to Tue 16:00 from Denver; Mon–Tue in a
Lone Tree hotel (~1,800 m), working days, landing Wed. Running front-loaded, lifting
pushed to the back of the week. Mon 4×4 is the VO2max session (normally 4:00-4:05/km)
with **altitude-adjusted targets** — ~4:10-4:18/km outdoors, ≈14.3-14.6 kph on a
treadmill instead of 15.3 — run it by effort, last rep at the limit; it is the HRmax
pin session (max HR is not suppressed at this altitude). Tue AM easy 8k is a
shakeout before 17 h of sitting; cut it first if the morning gets eaten. Wed:
land 14:30, then the carried-over **W1 D4 Pull-ups** in the evening (skipped Sun
23 for a hike; lightest session of the cycle, jetlag-tolerable). Thu easy run
by feel (jetlag day 1). Strength override this week (no lifting Mon–Tue —
hotel + work): Wed W1-D4 Pull-ups PM, Thu D1 Squat PM (double with the easy run),
Fri D2 Dips, Sat D3 Deadlift (Sat rest waived once), Sun D4 Pull-ups PM after the
long run. Contingency if Mon's 4×4 dies (workshop + AW): 4×4 moves to Fri at sea
level with standard 4:00-4:05 targets, dips stay Fri PM (one-off rule bend), Mon
becomes easy-or-nothing. Normal Mon/Wed/Fri/Sun rhythm and Sat rest resume Week 3.
Amended 2026-08-25: Tue shakeout came in short (4.85 of 8 km, pre-flight); volume
recovered by bumping Thu 6→8 km and Sun long 12→13 km. Pushed Tredict entries left
at 6/12 by choice — he runs past the workout-complete prompt on the watch.

## Week 3 (of 2026-08-31) — ~36 km

- Mon | Easy | 8km @ 5:15-6:15/km
- Wed | Quality | WU 2km easy; 20min @ 4:50/km; CD 2km easy
- Fri | Easy | 7km @ 5:15-6:15/km
- Sun | Long | 13km @ 5:45-6:15/km

Notes: first continuous tempo — unbroken pace-holding, the most 10k-specific stimulus in the block.

## Week 4 (of 2026-09-07) — Norwegian structure begins; lifting deloads, running does not, ~37 km

- Mon | Easy | 6km @ 5:45-6:15/km
- Wed | Quality | WU 3km easy; 3x(2.5min uphill HARD, jog down ~2.5min) — rep 1 strong but controlled, rep 3 all-out with a sprint finish; CD 2km easy
- Fri | Quality | WU 2km easy; 8x(3min @ 4:48-4:55/km, 60s jog); CD 1.5km easy
- Sun | Long | 14km @ 5:45-6:15/km

Notes: running deload **scrapped by user 2026-09-03** ("i actually don't think i need
a deload from running next week, just lifting") — **provisional until the Sun 09-06
13k is reviewed**; if decoupling or legs say otherwise, trim toward the old ~28 km
deload before syncing. Lifting still runs the **7th Week Protocol deload**.
**Wed = HRmax pin test** (user request 2026-09-03: no lactate meter, so the HR
ceilings are the control system and need a real max; moved Fri → Wed on his call
the same day). Replaces the 5×3 sub-T intro (W4 sub-T = Fri's 24 min only —
gentler intro anyway). Upside of Wed: Friday's first real sub-T-before-deadlift
session runs on **pinned** ceilings from day one, against the light deload pull.
With Monday squats restored (2026-09-03) the test sits 48 h after a *deload*
squat — legs effectively fresh; if the result still barely clears the 195 floor,
treat it as provisional and let the Oct 18 5k arbitrate. Protocol: take the
**highest HR observed** (usually seconds after the final sprint ends), no
formulas. Wear the chest/arm strap if available — wrist optical under-reads
peaks. Afterwards **set the result in the COROS profile** (its load/focus labels
are junk until then) and switch the sub-T ceilings from the flat ~180 placeholder
to %-of-max (see schema). Refine at the Oct 18 5k and the Nov 1 TT — an all-out
5k finish typically lands within a few bpm of true max.

## Week 5 (of 2026-09-14) — ~40 km

- Mon | Easy | 6km @ 5:45-6:15/km
- Wed | Quality | WU 2km easy; 5x(6min @ 4:55-5:00/km, 75s jog); CD 1.5km easy
- Fri | Quality | WU 2km easy; 8x(3min @ 4:48-4:55/km, 60s jog); CD 1.5km easy
- Sun | Long | 14km @ 5:45-6:15/km

## Week 6 (of 2026-09-21) — ~41.5 km

- Mon | Easy | 6km @ 5:45-6:15/km
- Wed | Quality | WU 2km easy; 3x(10min @ 5:00-5:05/km, 90s jog); CD 1.5km easy
- Fri | Quality | WU 2km easy; 5x(6min @ 4:55-5:00/km, 75s jog); CD 1.5km easy
- Sun | Long | 15km @ 5:45-6:15/km

## Week 7 (of 2026-09-28) — ~43 km

- Mon | Easy | 6km @ 5:45-6:15/km
- Wed | Quality | WU 2km easy; 10x(3min @ 4:46-4:52/km, 60s jog); CD 1.5km easy
- Fri | Quality | WU 2km easy; 3x(10min @ 5:00-5:05/km, 90s jog); CD 1.5km easy
- Sun | Long | 16km @ 5:45-6:15/km

## Week 8 (of 2026-10-05) — consolidation, ~43 km

- Mon | Easy | 6km @ 5:45-6:15/km
- Wed | Quality | WU 2km easy; 4x(8min @ 4:55-5:00/km, 75s jog); CD 1.5km easy
- Fri | Quality | WU 2km easy; 8x(3min @ 4:48-4:55/km, 60s jog); CD 1.5km easy
- Sun | Long | 16km @ 5:45-6:15/km

Notes W5-W8: sub-T dose builds 39 → 54 → 60 → 60 → 56 min/wk, rotating rep lengths
(3/6/10 min) like the singles standard; long runs stay clean easy — the quality
budget lives on Wed/Fri now. W8 holds volume flat to absorb before the gate week.
HARD RULE unchanged: any shin/achilles/knee niggle → repeat the previous week's
volume instead of progressing.

## Week 9 (of 2026-10-12) — gate week, ~34 km

- Mon | Easy | 6km @ 5:45-6:15/km
- Wed | Quality | WU 2km easy; 3x(8min @ 4:55-5:00/km, 75s jog); CD 1.5km easy
- Fri | Quality | WU 2km easy; 4x(3min @ 4:48-4:55/km, 60s jog); CD 1.5km easy
- Sun | Quality | WU 3km easy; 5km TT all-out; CD 2km easy

Notes: Sun Oct 18 = **5k tune-up TT, the readiness gate**: **≤21:40 (Riegel →
sub-45 10k) confirms the Nov 1 TT**; slower → TT slides to Sun Nov 8, W10 repeats as
a build week (Wed 4×8, Fri 8×3, Sun 14k long) and W11-shape taper shifts one week.
Graded at face value per standing rule. 48 h after Friday's C15-W2 deadlift — same
spacing as every long run, no discount. Replaces the long run this week (fine, 3
weeks out). Doubles as the HRmax pin candidate.

## Week 10 (of 2026-10-19) — race-specific, ~37 km

- Mon | Easy | 6km @ 5:45-6:15/km
- Wed | Quality | WU 2km easy; 3x(2km @ 4:30-4:33/km, 2min jog); CD 1.5km easy
- Fri | Quality | WU 2km easy; 6x(3min @ 4:48-4:55/km, 60s jog); CD 1.5km easy
- Sun | Long | 13km @ 5:45-6:15/km, last 2km @ 4:30/km

Notes: sharpening — Wed goes to goal race pace (the only above-threshold work in the
plan), Fri drops to sub-T maintenance, long run gets its race-pace finish.

## Week 11 (of 2026-10-26) — taper, ~29 km incl. TT

- Mon | Easy | 5km @ 5:45-6:15/km
- Wed | Quality | WU 2km easy; 4x(1km @ 4:30/km, 90s jog); CD 1km easy
- Fri | Easy | 4km @ 5:45-6:15/km
- Sun | Quality | WU 2km easy; 10km TT all-out; CD 1km easy

Notes: **Sun Nov 1 = flat 10k solo TT, target sub-45 (4:28-4:30/km)**, graded at
face value. Lifting runs its next 7th Week Protocol deload this same week (C14
Sep 14-Oct 4, C15 Oct 5-25, deload Oct 26-Nov 1) — lifting deload, running taper,
and the TT align with no rule-bending. Wed 4×1k is a primer, not a workout. Fri
sub-T dropped; shakeout only.

## Open items

- Treadmill calibration (brief §7.1) — if the belt runs fast, VO2max outdoor paces
  shift slower. Recalibrate with COROS Track Run mode once the Pace 4 arrives.
- Block endpoint (superseded 2026-09-03; history below): **TT is now Sun Nov 1**,
  flat 10k solo, target **sub-45**, gated by the W9 5k tune-up (Oct 18, ≤21:40;
  miss → slide to Nov 8). Original endpoint was W8 Sun Oct 11 vs 45:00-45:30
  (decided 2026-08-27 after Hässelbyloppet fell through — user likely not in
  Sweden); user chose 2026-09-03 to push it back until sub-45 is realistic, in
  exchange for the Norwegian realignment. Still graded at face value — no solo-TT
  discount, per user ("i can push myself without a group"). Doubles as the HRmax
  pin. If a flat, properly-seeded real 10k appears ~Nov 1, it can replace the TT.
  Strides dropped from all easy runs per user (2026-08-23). Current race pace
  ~4:42/km (47:00); goal race pace 4:28-4:30/km.
- **Tredict trial ends ~2026-10-17** — before the W10/W11 syncs and the Nov 1 TT.
  Decide before then: pay the $49/yr or swap the push layer to Intervals.icu.
