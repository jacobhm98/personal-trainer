# Running plan

Distilled from `running-training-brief.md` §4–5 (compiled 16 Aug 2026, day after the
Midnattsloppet 10k). Direction: 4 runs/week, ramp ~10%/week from ~28 to ~38 km/week,
long run is the priority variable (12 → 16–18 km), quality alternates
threshold → VO2max with threshold as the majority stimulus.

**Realigned 2026-09-03 (from W4, user decision): Norwegian-singles structure.**
Mon recovery run, **Wed + Fri sub-threshold sessions** (Fri run AM, deadlift PM),
Sun long run. VO2max sessions dropped entirely. Rationale: threshold time was
~14 min/wk on the old plan; the singles structure accumulates 50-60+ min/wk at a
tolerable intensity. Sparked by Bakken's *The Norwegian Method Applied* (2026).

**Base block (decided 2026-09-03, second decision the same day): no racing this
fall.** The Nov 1 TT (which had briefly replaced the Oct 11 TT) is **scrapped** —
user's call: a TT is ~2.5 weeks of development budget (sharpening + taper +
recovery) spent on curiosity. Instead: **build to 55 km/week** (the config
ceiling) with 2 well-executed sub-T sessions and a progressively growing long run
(→ ~20 km), down-weeks roughly every 4th week, until the peak is reached — then
**one all-out 5k inside a normal down-week** (~Sun 2026-12-06, no taper) to feed
curiosity, re-anchor the pace bands, refine the HRmax pin, and stamp the fitness-
index running input (Riegel 5k→10k). Calibration between now and then is HR-led:
after the W4 Wed pin, the %-of-max ceilings are fixed and pace floats up with
fitness; bands re-anchored from session data every ~3 weeks. Next race gate =
sub-44 Barcelona (date TBD — see open items).

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
  3min reps 4:48–4:55, 6min reps 4:55–5:00, 8–10min reps 5:00–5:05.
  **UNVALIDATED IN EITHER DIRECTION — do not assume too fast** (revised 2026-09-11
  after the user pushed back; an earlier version of this note claimed "provisionally
  too fast" and was wrong to). The bands descend from an assumed threshold of
  4:45–4:55, which descends from the **~47:00 10k estimate — a number that has never
  been measured.** The objection that sub-T was set *at* threshold rather than under it
  only holds if that estimate is right. His counter, which is sound: "i think im fitter
  than 47:00, so to me the sub-T is fine." If true threshold is nearer 4:35, then
  4:48–4:55 sits 13–20 s/km below it, which is correct sub-T placement, and every band
  in this plan is conservative rather than hot.
  The 09-10 evidence is weaker than first reported: 2 of 3 checks **passed** (every rep
  plateaued to ±2 bpm over its last 45 s; he finished able to do two more, easily). Only
  the session ratchet failed (plateau 170 → 185, float floor 165 → 178) — and that is
  the metric most contaminated by the two known confounders, treadmill heat (5–10
  bpm/hr) and illness. Mechanism looks like accumulation from 60 s floats, not reps in
  the severe domain.
  **Every running data point in this block is a floor, not a measure** — Midnattsloppet
  was paced blind, the 09-02 tempo was run to a prescription, 09-10 stopped with reps in
  hand. Nothing has been run to failure since August, so nothing can confirm or refute
  the estimate. This is the strongest argument for doing the COROS fitness test early:
  it replaces the single load-bearing guess the whole plan hangs off, in one session,
  rather than waiting for the Dec 6 5k.
  **New control: drift, not a fixed pace** — and it is robust to the estimate being
  wrong either way, which is why it is worth keeping regardless. W5 Wed runs the band
  **as written, 4:55–5:00 for the 6min reps**, starting at the slow end. If drift across the reps is ≤8 bpm and the two-more-reps test passes,
  that is the band and it may creep faster over time. If drift exceeds 8 bpm, slow by
  5 s/km next session. This self-corrects toward his real threshold instead of
  inheriting an estimate built on an estimate. Confirm on the first clean session
  (W5), and settle it properly with a measured fitness test once healthy.
  **Anchor on the LONG reps, derive the short ones** (decided 2026-09-11). Rep length
  genuinely changes sub-T pace — shorter reps accumulate less lactate per rep and get a
  better recovery ratio (8×3min/60s ≈ 1:3, 3×10min/90s ≈ 1:7), so they run faster for
  the same internal dose. But on a 3min rep HR never stabilises, so drift there is
  mostly measuring HR lag. On 6–10min reps HR approaches steady state *within* the rep:
  **plateaus mid-rep = at or under threshold; climbs throughout = over it.** So run the
  experiment on **W5 Wed's 5×6min, starting at 5:05/km**, then derive the rest from the
  settled band — 3min ≈ 6 s/km faster, 8–10min ≈ 5 s/km slower — instead of running
  three independent experiments on noisy data.
  Controls, in order: **drift ≤8 bpm**; the pace band; the **HR ceiling**; finish
  every session able to do two more reps. If any says too hot, slow the rep. HR ceilings: flat **~180**
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

## Week 4 (of 2026-09-07) — Norwegian structure begins; lifting deloads, running builds, ~39.5 km

- Mon | Easy | 7km @ 5:45-6:15/km
- Wed | Quality | WU 3km easy; 3x(2.5min uphill HARD, jog down ~2.5min) — rep 1 strong but controlled, rep 3 all-out with a sprint finish; CD 2km easy
- Fri | Quality | WU 2km easy; 8x(3min @ 4:48-4:55/km, 60s jog); CD 1.5km easy
- Sun | Long | 15km @ 5:45-6:15/km

Notes: running deload **scrapped by user 2026-09-03** ("i actually don't think i need
a deload from running next week, just lifting"), and **resolved 2026-09-06 after the
13k review: not just held — built.** His call: "let's do a lifting deload but continue
building running volume in w4." Mon 6->7 km and the long run 14->15 km take the week
from ~37 to **~39.5 km, +7.6% on W3's executed 36.8**. Deliberately under the 10%
ceiling because W4 already stacks two novel stressors — the Wed max test and the first
sub-T-before-deadlift double — and volume is the third. The added km go on the two
*easy* days; Wed and Fri structure is untouched. Rationale for building at all: the
7th Week Protocol strips FSL, assistance and 40% of the load off every lifting
session, so the systemic budget freed by the deload is spent on running instead of
banked. Lifting still runs the **7th Week Protocol deload**.
**Executed amendment 2026-09-07:** Monday's 7 km came in at **9.03 km** — got lost.
Run at 6:08/km (5:57 adjusted), HR 155, 235 W, "Very Easy" — the softest run of the
block, so it was absorbed rather than compensated for elsewhere. Week lands at
**~41.5 km, +12.9% on W3** instead of the planned +7.5%; accepted because the lifting
deload (two sessions, no FSL, no assistance) leaves systemic load well below a normal
week. **Progression is RPE-gated, not percentage-capped** — user's call 2026-09-07: "if i
can do it without it feeling rough we keep it going." So W5 builds off the **41.5 km
actually run**, not a discounted 40, and the ~10%/wk figure is a reference point
rather than a ceiling. He is not a novice (sub-41 10k history) and the 10% rule is a
weakly-evidenced heuristic; his own feel is the better governor for muscular load.
**Two guardrails survive, because feel does not cover them:** (1) the **long run grows
~1 km/week max** — per-session distance is where bone/tendon stress concentrates, and
connective-tissue injury presents *after* accumulation with no warning during the ramp;
(2) the **niggle rule stays sovereign**. Also note W4 reads easy partly because lifting
is deloaded to two sessions with no FSL or assistance — C14 restores that in W5, so
identical running volume will cost more.

**Ladder consequence:** W5 as written (~40 km) is now flat against W4, so the
W5-W16 ramp is stale. **Not being re-spaced** — user's call 2026-09-06: "lets take
each week as it comes." The written W5-W16 numbers are therefore a sketch, not a
commitment; set each week's volume at its own sync off the previous week's
*executed* km. The 55 km/wk ceiling and the Dec 6 endpoint still stand.
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
- Wed | Test | **ALL-OUT 5k TIME TRIAL, OUTDOORS** (replaces the 5x6min sub-T)
- Fri | Quality | WU 2km easy; 8x(3min @ 4:48-4:55/km, 60s jog); CD 1.5km easy
- Sun | Long | 14km @ 5:45-6:15/km

### Wed 2026-09-16 — 5k TT (decided 2026-09-10, user's call: "fuck it")

**Why it is the priority session of the block.** Every pace band, the fitness-index
baseline and the sub-44 gate descend from a **~47:00 10k estimate that has never been
measured** — his own assessment from 2026-08-18, off a race paced blind on a broken
watch. Three live estimates disagree by four minutes: **44:00** (Strava's prediction),
**47:00** (his August estimate), **~47-48** (inferred from the 09-02 tempo, 20 min at
4:42 grade-adjusted costing 181 bpm). Every running data point in the block is a
**floor, not a measure** — Midnattsloppet paced blind, 09-02 run to a prescription,
09-10 stopped with reps in hand. Nothing has been run to failure since August. One TT
replaces all three guesses, and the finish HR pins HRmax for free (a 5k finish lands
within a few bpm of true max), closing both open calibration questions at once.

**Outdoors, not the treadmill** (he proposed the belt first). Two reasons: treadmill
belts run 2-5% off with no way to detect it, which is 30-70 s of error over 5k in a
number about to anchor everything; and the **Dec 6 endpoint 5k is outdoors**, so a
belt baseline would not be comparable to it — and comparing them is the point of the
block.

**Course:** 400 m track preferred (12.5 laps, count them, ignore watch distance — GPS
over-reads on a track); else a flat **2.5 km out-and-back**, which cancels wind and net
gradient in a way a loop does not. No lights, crossings or tight turns.

**Pacing ladder** — open conservative and build; the error is asymmetric (6 s/km too
slow costs ~15 s, 6 s/km too fast costs the whole test, and a negative-split 5k is
near-optimal anyway):

| km | Target |
|---|---|
| 1 | 4:30 — will feel far too easy; check at 400 m, that is where he will be 10-15 s/km hot |
| 2 | 4:28 |
| 3 | 4:25 — if this is comfortable, Strava is right; jump early |
| 4 | 4:20 |
| 5 | empty it |

That lands ~22:00 (= 45:50 10k). Room to run 4:10s off it if he is 44:00 shape.

**Capture:** stop dead at the line, stand still, watch HR for 20 s before touching
anything — that peak is the HRmax pin, and standing still is when wrist optical is at
its best (no chest strap available; see the 09-06 cadence-lock artefact).

**Open for the W5 sync:** C14 W1 restarts Monday with squat at 65/75/85% — a real
session 48 h before a maximal effort. **Move it to after the TT** rather than
compromise the number.

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

## Week 8 (of 2026-10-05) — down week, ~36 km

- Mon | Easy | 6km @ 5:45-6:15/km
- Wed | Quality | WU 2km easy; 8x(3min @ 4:48-4:55/km, 60s jog); CD 1.5km easy
- Fri | Quality | WU 2km easy; 4x(6min @ 4:55-5:00/km, 75s jog); CD 1.5km easy
- Sun | Long | 13km @ 5:45-6:15/km

Notes W5-W8: sub-T dose builds 24 → 54 → 60 → 60, then 48 in the W8 down-week,
rotating rep lengths (3/6/10 min) like the singles standard; long runs stay clean
easy — the quality budget lives on Wed/Fri now. Down-weeks every ~4th week (W8,
W11, W16) — the base block earns its ramp by paying recovery on schedule.
HARD RULE unchanged: any shin/achilles/knee niggle → repeat the previous week's
volume instead of progressing.

## Week 9 (of 2026-10-12) — ~46 km

- Mon | Easy | 7km @ 5:45-6:15/km
- Wed | Quality | WU 2.5km easy; 4x(8min @ 4:55-5:00/km, 75s jog); CD 2km easy
- Fri | Quality | WU 2.5km easy; 8x(3min @ 4:48-4:55/km, 60s jog); CD 2km easy
- Sun | Long | 17km @ 5:45-6:15/km

Notes: judge W9 against W7 (43 → 46 = +7%), not against the W8 down-week.

## Week 10 (of 2026-10-19) — ~48 km

- Mon | Easy | 8km @ 5:45-6:15/km
- Wed | Quality | WU 2.5km easy; 3x(10min @ 5:00-5:05/km, 90s jog); CD 2km easy
- Fri | Quality | WU 2.5km easy; 5x(6min @ 4:55-5:00/km, 75s jog); CD 2km easy
- Sun | Long | 18km @ 5:45-6:15/km

## Week 11 (of 2026-10-26) — down week + lifting 7th Week deload, ~38 km

- Mon | Easy | 6km @ 5:45-6:15/km
- Wed | Quality | WU 2km easy; 8x(3min @ 4:48-4:55/km, 60s jog); CD 1.5km easy
- Fri | Quality | WU 2km easy; 4x(6min @ 4:55-5:00/km, 75s jog); CD 1.5km easy
- Sun | Long | 13km @ 5:45-6:15/km

Notes: running down-week aligned with the lifting 7th Week Protocol deload
(C14 = W5-W7, C15 = W8-W10, deload Oct 26 - Nov 1) — the whole organism recovers
in the same week.

## Week 12 (of 2026-11-02) — ~49 km

- Mon | Easy | 8km @ 5:45-6:15/km
- Wed | Quality | WU 2.5km easy; 10x(3min @ 4:48-4:55/km, 60s jog); CD 2km easy
- Fri | Quality | WU 2.5km easy; 4x(8min @ 4:55-5:00/km, 75s jog); CD 2km easy
- Sun | Long | 18km @ 5:45-6:15/km

Notes: judge W12 against W10 (48 → 49), not against the W11 down-week. Sub-T pace
bands re-anchored from W5-W11 session data before this week is synced.

## Week 13 (of 2026-11-09) — ~51 km

- Mon | Easy | 8km @ 5:45-6:15/km
- Wed | Quality | WU 2.5km easy; 5x(6min @ 4:55-5:00/km, 75s jog); CD 2.5km easy
- Fri | Quality | WU 2.5km easy; 3x(10min @ 5:00-5:05/km, 90s jog); CD 2.5km easy
- Sun | Long | 19km @ 5:45-6:15/km

## Week 14 (of 2026-11-16) — ~53 km

- Mon | Easy | 9km @ 5:45-6:15/km
- Wed | Quality | WU 2.5km easy; 4x(8min @ 4:55-5:00/km, 75s jog); CD 2.5km easy
- Fri | Quality | WU 2.5km easy; 5x(6min @ 4:55-5:00/km, 75s jog) + 2x(3min @ 4:48-4:55/km, 60s jog); CD 2km easy
- Sun | Long | 20km @ 5:45-6:15/km

## Week 15 (of 2026-11-23) — PEAK, ~55 km

- Mon | Easy | 10km @ 5:45-6:15/km
- Wed | Quality | WU 3km easy; 3x(10min @ 5:00-5:05/km, 90s jog); CD 2.5km easy
- Fri | Quality | WU 3km easy; 10x(3min @ 4:48-4:55/km, 60s jog); CD 2.5km easy
- Sun | Long | 20km @ 5:45-6:15/km

Notes: the block target — 55 km, 60 min sub-T, 20k long run, all absorbed. Pace
bands here are placeholders; they will have been re-anchored twice by now.

## Week 16 (of 2026-11-30) — down week + all-out 5k, ~31 km

- Mon | Easy | 7km @ 5:45-6:15/km
- Wed | Quality | WU 2km easy; 6x(3min @ 4:48-4:55/km, 60s jog); CD 2km easy
- Fri | Easy | 5km @ 5:45-6:15/km
- Sun | Quality | WU 3km easy; 5km all-out; CD 2km easy

Notes: **Sun Dec 6 = the all-out 5k** — inside a normal down-week, deliberately
NOT tapered for (user's design: it feeds curiosity, it is not a goal race).
Graded at face value per standing rule. It does triple duty: re-anchors every
pace band, refines/confirms the HRmax pin (an all-out 5k finish lands within a
few bpm of true max), and stamps the fitness-index running input (Riegel 1.06 →
10k-equivalent). Falls in lifting C17 W2 — no lifting accommodation. What comes
after the block (Barcelona build timing, structure) is a fresh planning
conversation informed by this result.

## Open items

- Treadmill calibration (brief §7.1) — if the belt runs fast, VO2max outdoor paces
  shift slower. Recalibrate with COROS Track Run mode once the Pace 4 arrives.
- Block endpoint (final form 2026-09-03, after two same-day revisions): **no fall
  10k at all** — the endpoint is the **W16 all-out 5k, Sun 2026-12-06**, inside a
  down-week with no taper. Endpoint history: Oct 11 TT vs 45:00-45:30 (2026-08-27,
  after Hässelbyloppet fell through) → moved to Nov 1 vs sub-45 with an Oct 18
  gate (2026-09-03 morning, Norwegian realignment) → scrapped entirely
  (2026-09-03 evening, user: a TT is development budget spent on curiosity; a
  base block to 55 km/wk is the efficient medium-term play). Face-value grading
  and no-solo-discount rules carry over to the 5k. **Open: which race is the
  sub-44 "Barcelona" gate** — pick the race + date (likely Jan-Mar 2027 window);
  that sets when the base block hands over to a race build. Strides dropped from
  all easy runs per user (2026-08-23). Current race shape ~47:00 (4:42/km).
- **Tredict trial ends ~2026-10-17** — before the W10/W11 syncs and the Nov 1 TT.
  Decide before then: pay the $49/yr or swap the push layer to Intervals.icu.
