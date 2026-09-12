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
- **EASY RUNS ARE HR-CAPPED, NOT PACE-CAPPED** (user's call 2026-09-12, from Bakken:
  easy running capped at **70% HRmax**). Pace bands below are now descriptive, not
  prescriptive — the cap governs, and being under it is always fine.
  - **Easy / recovery runs: ≤70% HRmax.** Provisional max **200** until the Tue 09-15
    TT returns a real figure → **cap 140 bpm**.
  - **Long run: ≤75% → cap 150 bpm.** Deliberately looser: cardiac drift alone adds
    5–10 bpm over 90+ min at constant effort, so a 70% cap on a 20k would mean slowing
    down all run to chase a number moving for non-metabolic reasons.
  - **Expect this to feel absurdly slow — roughly 7:00–7:20/km.** Every easy run to date
    has sat at 78–84% of an assumed 200 (155–169 bpm). If the cap really does land there,
    that is not an error, it is the "high ceiling, small tank" profile showing up
    exactly where the brief says it should. Err slow: a cap set too high just preserves
    the status quo we are trying to change.
  - Time of day: morning runs read ~2–4 bpm lower than the same effort in the evening
    (resting HR and core temp both rise through the day; max HR is also a few bpm higher
    late). Real but smaller than the ±7 bpm uncertainty in the assumed max — **do not
    correct for it.** Run at consistent times where possible.
- Paces (min/km, now descriptive): easy 5:15–6:15, recovery 5:45–6:15, long 5:45–6:15,
  threshold 4:45–4:55, VO2max 4:00–4:05 (retired from the weekly rotation 2026-09-03).
- **Sub-threshold bands** (Norwegian singles, set 2026-09-03) — scale by rep length:
  3min reps 4:48–4:55, 6min reps 4:55–5:00, 8–10min reps 5:00–5:05.
  **PACE DERIVATION — Bakken's two rules (recorded 2026-09-12, user supplied from the
  book). These govern; the literal numbers above are placeholders until the TT.**

  1. **Headline: sub-T runs ~8-12 s/km slower than Jack Daniels T-pace.** That figure
     corresponds to the **4-6 min** tier — the bread-and-butter session — so read it as
     the mid-tier value, not a blanket offset for every rep length.
  2. **Tiered by rep length.** His worked example, verbatim: *if threshold is
     4:15-4:20, run 1-3 min reps at 4:18-4:25, 4-6 min at 4:25-4:32, 8-12 min at
     4:32-4:39.* Extracting the rule as offsets from the T-pace band:

     | Rep length | Offset from T-pace | From the example |
     |---|---|---|
     | 1-3 min  | **T + 3-5 s/km**   | 4:18-4:25 |
     | 4-6 min  | **T + 10-12 s/km** | 4:25-4:32 |
     | 8-12 min | **T + 17-19 s/km** | 4:32-4:39 |

     Each tier is **~7 s/km slower than the one above**, and each band is **~7 s wide**.
     Note rule 2's mid-tier (+10-12) sits inside rule 1's 8-12 range — they agree.

  **Pipeline once the Tue 09-15 TT lands:** 5k time → Riegel 1.06 → 10k-equivalent →
  Daniels VDOT → **T-pace** → apply the three offsets above. Do not set sub-T paces any
  other way from then on. As a sanity check, T-pace should land roughly **10k race pace
  + 6-10 s/km** for a runner in the 40-50 min range.

  **How the current placeholders compare** (assumed T 4:45-4:52): the rule would give
  1-3 min 4:48-4:57, 4-6 min 4:55-5:04, 8-12 min 5:02-5:11. The written 3-min and 6-min
  bands are close; the **8-10 min band (5:00-5:05) is ~5 s/km too fast** at both ends.
  All three get replaced after the TT anyway — flagging it so the long-rep sessions are
  not run hot in the meantime.

  **Session menu, set 2026-09-12 from Marius Bakken's book (user's call).** His
  bread-and-butter sub-T sessions are **6×6 min** and **3–4×10 min**; those are now the
  staple and everything else is the exception. Shorter/faster work (8–10×3 min) stays
  in the rotation but as the **minority** — three appearances in the whole block (W5,
  W10, W14) against ten staple sessions. Bakken also prescribes *alternating* rep
  length, so the two weekly sessions never use the same one: a 6-min day pairs with a
  10-min day.
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
  every session able to do two more reps. If any says too hot, slow the rep. **HR CEILINGS — REPLACED 2026-09-12** (user supplied from Bakken; the old flat ~180
  and the ≤90/88/86% tiers are retired). Bakken: the **threshold zone for a well-trained
  amateur is 80–87% HRmax**. The old tiers were set off Daniels' T-pace anchor (88–92%),
  which is **LT2** — the top of threshold, not sub-threshold. Sub-T belongs in 80–87%.
  Tiered so the fastest reps sit at the top of the zone (provisional max **200** until
  the Tue 09-15 TT):

  | Tier | % HRmax | bpm @ max 200 |
  |---|---|---|
  | 1–3 min  | 85–87% | 170–174 |
  | 4–6 min  | 83–85% | 166–170 |
  | 8–12 min | 80–83% | 160–166 |

  End-of-rep values; HR lags on short reps. **Corroborated by his own sessions:** the
  09-10 8×3min ran rep 2 at 167 (83.5%) and rep 8 at 182 (91%) — correctly pitched at
  the start, out of the zone by ~rep 4, which is where the two-more-reps test would also
  have failed. The 09-02 tempo averaged 181 (90.5%), exactly where a *Daniels threshold*
  session should sit. Both bands land correctly on real data.
  Full intensity map: easy ≤70% (140), long ≤75% (150), sub-T 80–87% (160–174) —
  nothing lives between 150 and 160.

  **30-MINUTE TT — the direct LTHR test (added 2026-09-12, Bakken protocol via user).**
  Run 30 min at the fastest sustainable steady-state pace; **the average HR of the final
  20 min is LTHR**; the sub-T "golden zone" is **LTHR − 4–7 bpm**. Its virtue is needing
  **no HRmax at all**, same as the plateau test.
  **It is NOT the same as the 5k TT and does not replace it.** A ~22 min 5k is run
  *above* threshold, so its average HR sits ~4–8 bpm above LTHR — never read a 5k
  average as threshold HR. The 5k gives **performance + near-max**; the 30-min gives
  **LTHR**. Two anchors, two tests.
  **NOT SCHEDULED — user is doing one TT only (2026-09-12).** The 5k on Tue 09-15 is
  it; the W7 30-min TT was proposed and dropped, and W7 Tue reverts to its 6×6.
  **This costs less than first stated.** The 5k anchors the **pace** side outright —
  Daniels' tables take a 5k time directly, so it is 5k → VDOT → T-pace → offsets, no
  Riegel step. Pace is the prescription; the in-session checks verify it; the %-of-max
  HR ceilings are a **soft rail** on an approximate max and lose any disagreement with
  the derived pace or the plateau test. LTHR would have been a second route to the same
  place, not a missing foundation. Kept here because it stays the cheapest way to
  measure LTHR if he ever wants it — a 30 min steady effort substitutes for a quality
  session rather than adding to one, unlike an all-out 5k.
  **Consistency check:** if LTHR ≈ 88–90% max, then LTHR − 4–7 ≈ 84–87% — which is the
  **1–3 min tier** above (170–174 @ max 200). So the golden zone is the short-rep end,
  and longer reps sit progressively below it — the same direction the pace offsets tier.
  Two independent systems agreeing.
  The 2026-09-02 tempo at 181 avg was over the line. These sessions are deliberately
  unheroic — accumulation is the stimulus. Do not race them.
- Day roles — **restructured 2026-09-12 (user's design), in force from W6.** The
  5/3/1 sequence D1→D2→D3→D4 runs in order with the lifting week starting Tuesday:
  **Mon easy recovery run** (no lift); **Tue sub-T AM + D1 Squat PM**; **Wed D2 Dips**
  (no run); **Thu REST**; **Fri sub-T AM + D3 Deadlift PM**; **Sat D4 Pull-ups**
  (no run); **Sun long run**. Rationale is Bakken's concentration principle applied to
  the week: stack the hard stimuli so the remaining days are genuinely recovered.
  Legs are loaded on **two days only** (Tue, Fri), each pairing the hardest run with
  the hardest lift, run first with a ≥6 h gap. Upper body sits on a separate recovery
  budget, so dips and pull-ups scatter onto otherwise-empty days where they cost
  nothing. Exactly **two double days**, both deliberate.
  Constraints all still hold: squat→deadlift 72 h, deadlift→squat 96 h, never
  consecutive, abs land Wed + Sat rather than back-to-back, all four lifts in phase.
  **One full rest day per week — no run, no lift — remains an invariant**; only the day
  moved, Sat → Thu, so it now sits *between* the two hard days rather than after the
  second one. Saturday is upper-body only. What this structure *does* supersede is
  "Mon squat is the default in any normal week" (set 2026-09-03).
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
- Tue | Test | **ALL-OUT 5k TIME TRIAL, OUTDOORS** (replaces Tuesday's sub-T; D1 Squat follows in the PM)
- Fri | Quality | WU 2km easy; 8x(3min @ 4:48-4:55/km, 60s jog); CD 1.5km easy
- Sun | Long | 14km @ 5:45-6:15/km

### Tue 2026-09-15 — 5k TT (decided 2026-09-10, user's call: "fuck it"; moved Wed -> Tue 2026-09-12 with the new week structure)

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

**Squat placement — resolved 2026-09-12.** No conflict once the new structure is in:
the TT is the Tuesday AM session and **D1 Squat is that evening**, so the TT runs on
fresh legs and the squat absorbs the cost — identical logic to sub-T AM before the
lift, and consistent with running being the priority. Expect the squat top set to be
rough six hours after a maximal 5k; **a miss there is confounded by the TT** and must
be recorded as such, exactly like the Friday deadlift confound. Under the hit/miss
rule it simply holds the TM. C14 W1 is the lightest week of the cycle, so a miss is
unlikely anyway.

## Week 6 (of 2026-09-21) — ~42 km

- Mon | Easy | 6km @ 5:45-6:15/km
- Tue | Quality | WU 2km easy; 5x(6min @ 4:55-5:00/km, 75s jog); CD 1.5km easy
- Fri | Quality | WU 2km easy; 3x(10min @ 5:00-5:05/km, 90s jog); CD 1.5km easy
- Sun | Long | 15km @ 5:45-6:15/km

## Week 7 (of 2026-09-28) — ~45 km

- Mon | Easy | 6km @ 5:45-6:15/km
- Tue | Quality | WU 2km easy; 6x(6min @ 4:55-5:00/km, 75s jog); CD 1.5km easy
- Fri | Quality | WU 2km easy; 3x(10min @ 5:00-5:05/km, 90s jog); CD 1.5km easy
- Sun | Long | 16km @ 5:45-6:15/km

## Week 8 (of 2026-10-05) — down week, ~38.5 km

- Mon | Easy | 6km @ 5:45-6:15/km
- Tue | Quality | WU 2km easy; 4x(6min @ 4:55-5:00/km, 75s jog); CD 1.5km easy
- Fri | Quality | WU 2km easy; 3x(10min @ 5:00-5:05/km, 90s jog); CD 1.5km easy
- Sun | Long | 13km @ 5:45-6:15/km

Notes W5-W8 (rewritten 2026-09-12 for the Bakken session menu): sub-T dose runs
24 (W5, TT week) → 60 → 66 → 54 in the W8 down-week, alternating 6-min and 10-min
reps every session; long runs stay clean
easy — the quality budget lives on Wed/Fri now. Down-weeks every ~4th week (W8,
W11, W16) — the base block earns its ramp by paying recovery on schedule.
HARD RULE unchanged: any shin/achilles/knee niggle → repeat the previous week's
volume instead of progressing.


## Week 9 (of 2026-10-12) — ~47 km

- Mon | Easy | 7km @ 5:45-6:15/km
- Tue | Quality | WU 2km easy; 6x(6min @ 4:55-5:00/km, 75s jog); CD 2km easy
- Fri | Quality | WU 2km easy; 3x(10min @ 5:00-5:05/km, 90s jog); CD 2km easy
- Sun | Long | 17km @ 5:45-6:15/km

Notes: judge W9 against W7 (43 → 46 = +7%), not against the W8 down-week.


## Week 10 (of 2026-10-19) — ~51 km

- Mon | Easy | 8km @ 5:45-6:15/km
- Tue | Quality | WU 2.5km easy; 10x(3min @ 4:48-4:55/km, 60s jog); CD 2km easy
- Fri | Quality | WU 2.5km easy; 4x(10min @ 5:00-5:05/km, 90s jog); CD 2km easy
- Sun | Long | 18km @ 5:45-6:15/km

## Week 11 (of 2026-10-26) — down week + lifting 7th Week deload, ~40 km

- Mon | Easy | 6km @ 5:45-6:15/km
- Tue | Quality | WU 2km easy; 5x(6min @ 4:55-5:00/km, 75s jog); CD 1.5km easy
- Fri | Quality | WU 2km easy; 3x(10min @ 5:00-5:05/km, 90s jog); CD 1.5km easy
- Sun | Long | 13km @ 5:45-6:15/km

Notes: running down-week aligned with the lifting 7th Week Protocol deload
(C14 = W5-W7, C15 = W8-W10, deload Oct 26 - Nov 1) — the whole organism recovers
in the same week.


## Week 12 (of 2026-11-02) — ~51.5 km

- Mon | Easy | 8km @ 5:45-6:15/km
- Tue | Quality | WU 2.5km easy; 6x(6min @ 4:55-5:00/km, 75s jog); CD 2km easy
- Fri | Quality | WU 2.5km easy; 4x(10min @ 5:00-5:05/km, 90s jog); CD 2km easy
- Sun | Long | 18km @ 5:45-6:15/km

Notes: judge W12 against W10 (48 → 49), not against the W11 down-week. Sub-T pace
bands re-anchored from W5-W11 session data before this week is synced.


## Week 13 (of 2026-11-09) — ~52.5 km

- Mon | Easy | 8km @ 5:45-6:15/km
- Tue | Quality | WU 2.5km easy; 6x(6min @ 4:55-5:00/km, 75s jog); CD 2km easy
- Fri | Quality | WU 2.5km easy; 4x(10min @ 5:00-5:05/km, 90s jog); CD 2km easy
- Sun | Long | 19km @ 5:45-6:15/km

## Week 14 (of 2026-11-16) — ~54 km

- Mon | Easy | 9km @ 5:45-6:15/km
- Tue | Quality | WU 2.5km easy; 10x(3min @ 4:48-4:55/km, 60s jog); CD 2km easy
- Fri | Quality | WU 2.5km easy; 4x(10min @ 5:00-5:05/km, 90s jog); CD 2km easy
- Sun | Long | 20km @ 5:45-6:15/km

## Week 15 (of 2026-11-23) — PEAK, ~55.5 km

- Mon | Easy | 10km @ 5:45-6:15/km
- Tue | Quality | WU 3km easy; 6x(6min @ 4:55-5:00/km, 75s jog); CD 2.5km easy
- Fri | Quality | WU 3km easy; 4x(10min @ 5:00-5:05/km, 90s jog); CD 2.5km easy
- Sun | Long | 20km @ 5:45-6:15/km

Notes: the block target — 55 km, 60 min sub-T, 20k long run, all absorbed. Pace
bands here are placeholders; they will have been re-anchored twice by now.


## Week 16 (of 2026-11-30) — down week + all-out 5k, ~31 km

- Mon | Easy | 7km @ 5:45-6:15/km
- Tue | Quality | WU 2km easy; 4x(6min @ 4:55-5:00/km, 75s jog); CD 2km easy
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
