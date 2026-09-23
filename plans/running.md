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
ceiling at the time; raised 2026-09-16 with the five-run week, then again when the X session was deferred — **block goal now ~60 km/week, reached at W15**) with 2 well-executed sub-T sessions and a progressively growing long run
(→ 18 km, capped 2026-09-15), down-weeks roughly every 4th week, until the peak is reached — then
**one all-out 5k inside a normal down-week** (~Sun 2026-12-06, no taper) to feed
curiosity, re-anchor the pace bands, refine the HRmax pin, and stamp the fitness-
index running input (Riegel 5k→10k). **Superseded 2026-09-16:** the block has no endpoint
at all. 5k TTs run **every 5th week** as routine checks (09-15 → Fri 10-23 → Fri 11-27),
each replacing that week's Friday 4×10, and the Dec 6 5k is dropped. Calibration between now and then is HR-led:
after the W4 Wed pin, the %-of-max ceilings are fixed and pace floats up with
fitness; bands re-anchored from session data every ~3 weeks. **Race condition is now targeted for spring/summer 2027** (user 2026-09-16: "we're not
really on a timeline... im happy to write off autumn/winter as base building proper"), so
autumn and winter are base building with no race to serve. **Block goal: ~60 km/week.**

## Schema (parsed by /sync-running)

Each week is a `## Week N (of YYYY-MM-DD)` block (date = the Monday). Each session:

```
- <Day> | <Type> | <structure>
```

- Types: `Easy`, `Quality`, `X`, `Rest`, `Trek`, `Lift`, `Long`. **`Long` is retired from W6 (2026-09-16)** — there is no dedicated long run any more; `X` is the Sunday supra-threshold session — **dormant from 2026-09-16**, since Sunday is an easy run until volume holds ~60 km.
  `Rest`, `Trek` and `Lift` were added 2026-09-16 for the Rwanda block: `Rest` is a travel or clear day, `Trek` is a gorilla-trek day, and `Lift` is a lifting-only day with no run. `Rest` and `Trek` are not pushed to Tredict as workouts.
- Structure segments separated by `;`. `WU`/`CD` = warm-up/cool-down.
  Repeats: `5x(1km @ 4:50/km, 60s jog)`. Continuous: `20min @ 4:50/km` or `8km @ 5:15-6:15/km`.
- **Longest-run pacing cross-check (Daniels).** From W6 the week's longest run is
  **Thursday's easy run** — the dedicated long run was dropped 2026-09-16 (see the
  X-session note). He runs it at **E pace**, 59–74% VO2max ≈ **65–79% HRmax**, roughly
  **T-pace + 60–90 s/km**. That is the *citable* basis for it sitting above Bakken's 70%
  easy cap — there is no Bakken long-run figure.
  Daniels' cap of the lesser of **25–30% of weekly volume** or **150 min** is now
  comfortably met: the longest run peaks at ~12 km in a ~58 km week (**~21%**, ~80 min),
  against 31–35% when an 18 km long run was still in the plan.
- **5k TT CADENCE — set 2026-09-16 (user's call).** A 5k TT runs **every ~5th week** as a
  routine progress check and sub-T re-anchor, **not** as a goal. It **replaces the week's
  most intensive sub-T session — the Friday 4×10** — so the week loses a hard session
  rather than gaining one. No taper, no sharpening, graded at face value; if a TT lands
  on a bad day, that is data too and the next one is five weeks out.
  Schedule — **strictly every 5 weeks, W5/W10/W15** (user 2026-09-16: "dec 6th is a
  completely arbitrary date, lets stick to a schedule instead"):
  **Tue 09-15 (done)** → **Fri 2026-10-23 (W10)** → **Fri 2026-11-27 (W15)** → next would
  be ~Fri 2027-01-01, which belongs to the Barcelona build rather than this block.
  **The Dec 6 5k is gone entirely** — it was the block endpoint from 2026-09-03, demoted
  to a check on 2026-09-16 and dropped the same day once the cadence made its date
  arbitrary. W16 is now an ordinary down week. Each TT returns: 5k time → VDOT → T-pace →
  all three §2 bands, plus an HRmax reading, plus a Riegel 10k-equivalent for the index.
  Run the **same route** every time and score on **grade-adjusted** time.
- **SIGNAL SPLIT (user 2026-09-12): easy + long runs run off HR; sub-T runs off pace.**
  Sub-T HR tiers become a **post-hoc review check, not something he watches mid-rep**.
  On a sub-T session: pace steers, **RPE aborts** (the two-more-reps question is the
  in-session safety valve — a fixed pace on a bad day will cook him), HR diagnoses at
  review. Sub-T wants flat consistent terrain, since a pace target cannot see a hill.
- **EASY RUNS ARE HR-CAPPED, NOT PACE-CAPPED** (user's call 2026-09-12, from Bakken:
  easy running capped at **70% HRmax**). Pace bands below are now descriptive, not
  prescriptive — the cap governs, and being under it is always fine.
  - **Easy / recovery runs: ≤70% HRmax.** Provisional max **~200**, kept after the
    09-15 TT peaked at only 193 (next check: the W10 TT) → **cap 140 bpm**.
  - **Thursday's longest run: start ≤70% (140), drift allowed toward ~150.** Corrected 2026-09-12 —
    Bakken specifies ≤70% for easy/recovery and nothing separate for long runs; the
    earlier "≤75% cap" here was **my inference wrongly attributed to him**. The drift
    reasoning stands (a fixed 70% ceiling over 90+ min means slowing progressively to
    chase a number rising for thermoregulatory reasons), and Daniels' E pace at
    **65–79% HRmax** independently supports long runs above 70% — but cap the *opening*
    rather than inventing a higher ceiling.
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
  **T-pace 4:40 (measured 2026-09-15)**, VO2max 4:00–4:05 (retired from the weekly
  rotation 2026-09-03).
- **Sub-threshold bands — MEASURED 2026-09-15** from the 5k TT (21:57 grade-adjusted →
  VDOT 44.7 → T-pace 4:40): **1–3 min reps 4:43–4:45, 4–6 min 4:50–4:52, 8–12 min
  4:57–4:59.** Record and method in `sub-threshold-reference.md` §8.1. **Next re-anchor:
  the W10 5k TT, Fri 2026-10-23.** Between tests the session checks move the bands (all
  passing easily → creep faster; any failing → slow 5 s/km). These replace the
  placeholders set 2026-09-03: 4:48–4:55 / 4:55–5:00 / 5:00–5:05.
  **PACE DERIVATION — Bakken's two rules (recorded 2026-09-12, user supplied from the
  book). These govern.**

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

  **Pipeline (first run 2026-09-15):** 5k time, **grade-adjusted** → Daniels VDOT →
  **T-pace** → apply the three offsets above. **No Riegel step** — Daniels' tables take a
  5k directly; Riegel only produces the 10k-equivalent. Do not set sub-T paces any other
  way. As a sanity check, T-pace should land roughly **10k race pace + 6-10 s/km** for a
  runner in the 40-50 min range.

  **How the placeholders compared — resolved 2026-09-15.** They assumed T 4:45–4:52; the
  measured T is 4:40, so all three placeholder bands were **3–10 s/km conservative, not
  hot** — including the 8–10 min band this note once flagged as too fast.

  **Session menu, set 2026-09-12 from Marius Bakken's book (user's call).** His
  bread-and-butter sub-T sessions are **6×6 min** and **3–4×10 min**; those are now the
  staple and everything else is the exception. Shorter/faster work (8–10×3 min) stays
  in the rotation but as the **minority** — planned for W5, W10 and W14, **now W10 and
  W14** (W5's became the 5×6 on 09-12). Bakken also prescribes *alternating* rep
  length, so the two weekly sessions never use the same one: a 6-min day pairs with a
  10-min day.
  **RESOLVED 2026-09-15 by the 5k TT: T-pace 4:40 — his read was right, and every
  placeholder band was conservative. Kept below for history.**
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
  **SUPERSEDED — paces now come from the TT pipeline above, and the drift threshold is
  Bakken's 7–10 bpm band (`sub-threshold-reference.md` §5), not ≤8. Kept for history.**
  **New control: drift, not a fixed pace** — and it is robust to the estimate being
  wrong either way, which is why it is worth keeping regardless. W5 Wed runs the band
  **as written, 4:55–5:00 for the 6min reps**, starting at the slow end. If drift across the reps is ≤8 bpm and the two-more-reps test passes,
  that is the band and it may creep faster over time. If drift exceeds 8 bpm, slow by
  5 s/km next session. This self-corrects toward his real threshold instead of
  inheriting an estimate built on an estimate. Confirm on the first clean session
  (W5), and settle it properly with a measured fitness test once healthy.
  **SUPERSEDED 2026-09-15** — the W5 5×6 experiment starting at 5:05 gave way to the
  measured TT bands; the plateau logic below lives on in `sub-threshold-reference.md` §4/§6.
  **Anchor on the LONG reps, derive the short ones** (decided 2026-09-11). Rep length
  genuinely changes sub-T pace — shorter reps accumulate less lactate per rep and get a
  better recovery ratio (8×3min/60s ≈ 1:3, 3×10min/90s ≈ 1:7), so they run faster for
  the same internal dose. But on a 3min rep HR never stabilises, so drift there is
  mostly measuring HR lag. On 6–10min reps HR approaches steady state *within* the rep:
  **plateaus mid-rep = at or under threshold; climbs throughout = over it.** So run the
  experiment on **W5 Wed's 5×6min, starting at 5:05/km**, then derive the rest from the
  settled band — 3min ≈ 6 s/km faster, 8–10min ≈ 5 s/km slower — instead of running
  three independent experiments on noisy data.
  Controls, in order: **session drift within `sub-threshold-reference.md` §5** (7–10 bpm for a 6×6); the pace band; the **HR ceiling**; finish
  every session able to do two more reps. If any says too hot, slow the rep. **HR CEILINGS — REPLACED 2026-09-12** (user supplied from Bakken; the old flat ~180
  and the ≤90/88/86% tiers are retired). Bakken: the **threshold zone for a well-trained
  amateur is 80–87% HRmax**. The old tiers were set off Daniels' T-pace anchor (88–92%),
  which is **LT2** — the top of threshold, not sub-threshold. Sub-T belongs in 80–87%.
  Tiered so the fastest reps sit at the top of the zone (provisional max **~200** — kept
  after the 09-15 TT peaked at only 193; next check the W10 TT):

  | Tier | % HRmax | bpm @ max 200 |
  |---|---|---|
  | 1–3 min  | 85–87% | 170–174 |
  | 4–6 min  | 83–85% | 166–170 |
  | 8–12 min | 80–83% | 160–166 |

  > **THESE CEILINGS DO NOT FIT THIS ATHLETE — established 2026-09-18. Do not prescribe
  > from them.** The 09-18 session ran the 4:51 band at **185–187 bpm** sustained, 15–19
  > above the 4–6 min tier, with every rep plateauing internally. The 09-15 TT averaged
  > 188, and a 5k sits 4–8 bpm above LTHR, giving **LTHR ≈ 180–184** — so 166–170 sits
  > roughly 15 bpm *below* his actual threshold and would prescribe an easy run in place
  > of a quality session. The tier split is [C] inference (`sub-threshold-reference.md`
  > §3), and §3 already ranks the §4 checks above it. **Sub-T is prescribed on PACE + RPE**
  > (user 2026-09-18), verified by within-rep plateau. Kept here as Bakken's framework and
  > as the record of why it was set aside, not as a live prescription.

  End-of-rep values; HR lags on short reps. **Corroborated by his own sessions:** the
  09-10 8×3min ran rep 2 at 167 (83.5%) and rep 8 at 182 (91%) — correctly pitched at
  the start, out of the zone by ~rep 4, which is where the two-more-reps test would also
  have failed. The 09-02 tempo averaged 181 (90.5%), exactly where a *Daniels threshold*
  session should sit. Both bands land correctly on real data.
  Full intensity map: easy ≤70% (140), long starts ≤70% and drifts to ~150, sub-T 80–87% (160–174) —
  nothing lives between 150 and 160.

  **30-MINUTE TT — the direct LTHR test (added 2026-09-12, Bakken protocol via user).**
  Run 30 min at the fastest sustainable steady-state pace; **the average HR of the final
  20 min is LTHR**; the sub-T "golden zone" is **LTHR − 4–7 bpm**. Its virtue is needing
  **no HRmax at all**, same as the plateau test.
  **It is NOT the same as the 5k TT and does not replace it.** A ~22 min 5k is run
  *above* threshold, so its average HR sits ~4–8 bpm above LTHR — never read a 5k
  average as threshold HR. The 5k gives **performance + near-max**; the 30-min gives
  **LTHR**. Two anchors, two tests.
  **NOT SCHEDULED — the 30-min TT was dropped 2026-09-12.** Calibration runs on 5k TTs
  only: Tue 09-15, plus one every ~5th week from 2026-09-16 (Fri 2026-10-23, Fri 2026-11-27). The W7 30-min TT
  was proposed and dropped, and W7 Tue reverts to its 6×6.
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
- **The "X session" — DEFERRED 2026-09-16 (user's second call the same day).** Bakken
  prescribes **two sub-T days plus one X session** for ambitious recreational runners, and
  the X session is a standing drip of **anaerobic / supra-threshold** work. It is still the
  right end state. It is **not** the right thing to add while weekly volume is the priority:
  a third hard day competes directly with mileage growth, and the block to December is
  base building proper (user 2026-09-16: "we're not really on a timeline... im happy to
  write off autumn/winter as base building proper").
  - **Until volume holds ~60 km/week, Sunday is an easy run** of 8–14 km — the week's
    second long-ish run alongside Thursday. Two quality days (Tue, Fri), not three.
  - **Hill strides stay, as the cheap hedge:** **6–8 × 10–15 s hill sprints, full
    recovery**, tacked onto the end of Sunday's easy run **every other week** (W9, W11,
    W13, W15). ~5 min of work, too short to produce meaningful lactate, and they hold on
    to turnover, leg stiffness and economy — the qualities that quietly rot over months of
    nothing faster than 5:30/km and do not come back quickly.
  - **Trigger to reinstate the X session: three consecutive weeks at ~60 km with sessions
    feeling routine** — a condition, not a date. At that point Sunday converts to
    **45/15s: 2–3 × (10 × 45 s @ ~3k effort, 15 s float), 3 min jog between blocks**, and
    the three-quality-day week designed on 2026-09-16 takes over. Realistically that is
    the spring/summer 2027 race build, not this block.
  - **Hills, when they return as full sessions:** 8–12 × 200 m uphill hard, jog down, run
    on effort rather than pace.
  - **Known consequence, accepted:** apart from the strides and a 5k TT every 5 weeks,
    this block has nothing above threshold. That is the deliberate cost of buying mileage,
    and the strides are what keep the door open.
  - **The dedicated long run stays gone** (user 2026-09-16: "we dont need a dedicated long
    run, im not in a marathon block"). **Thursday** is the week's longest run and carries
    the **decoupling measurement**; Sunday is now a close second.
- Day roles — **restructured 2026-09-16 (user's design), in force from W6.** Supersedes
  the 2026-09-12 four-run week, which this otherwise keeps intact:
  **Mon easy recovery** (no lift, follows Sunday's X); **Tue sub-T AM + D1 Squat PM**;
  **Wed D2 Dips** (no run); **Thu easy — the week's longest run** (no lift); **Fri sub-T
  AM + D3 Deadlift PM**; **Sat D4 Pull-ups** (no run); **Sun X session**.
  **Five runs, four lifts.** Hard days are **Tue, Fri and Sun**, with Monday's recovery
  run and Thursday's easy run between them.
  **Still exactly two double days** — Tue and Fri, sub-T AM with the heavy lift PM (run
  first, ≥6 h gap). The fifth run went on **Thursday** rather than Wednesday (user's call,
  same day): Thursday carries no lift at all, so the run lands on the one day that is
  completely clear, and Wednesday stays a single upper-body session.
  Constraints all still hold: squat→deadlift 72 h, deadlift→squat 96 h, never
  consecutive, abs land Wed + Sat rather than back-to-back, all four lifts in phase.
  **SUPERSEDED — the full rest day is gone.** "One full rest day per week, no run, no
  lift" was an invariant from 2026-09-12; putting the fifth run on Thursday spends it.
  **This rests on one condition** (user 2026-09-16: "its fine if i genuinely keep my
  easy's easy"): Monday, Thursday and every warm-up run **at or under 140
  bpm**, no exceptions. Easy-pace creep is this athlete's documented failure mode, and it
  is what the rest day used to absorb. If easy days start drifting, the clear day comes
  back before any other cut is made.
  **COOL-DOWNS ARE EXEMPT — amended 2026-09-18 (user's call).** An HR cap on a cool-down
  is unachievable by construction: HR *decays* from the last rep rather than settling
  into a band. Evidence from the 09-18 session — the cool-down opened at 179 straight off
  the final float, averaged 164, and never dropped below 141 across 4:53. A 120-140 target
  would have alerted continuously, which is the 2026-09-12 pace-band-on-an-HR-run error
  mirrored, and is likely part of why that cool-down was cut to 0.6 km of the prescribed 2.
  **Cool-downs are prescribed by DISTANCE only and run easy by feel** (user: "i think just
  prescribe a distance going forward, ill make sure to run it easy"). No HR target. See
  CLAUDE.md for the Tredict push shape.
  Wednesday (dips only) and Saturday (pull-ups only) are now the lightest days, both
  upper-body. If a genuinely clear day is wanted back, the cheapest move is dips or
  pull-ups onto a day that already has a session.
- Mon stays the lightest run of the week (rule set 2026-08-31): it follows Sunday's
  X session (Sunday's long run until 2026-09-16). Evidence: 2026-08-31 easy 8k ran 5:38/km at HR 169 on the same route and
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
*executed* km. The block has no endpoint at all from 2026-09-16 (TTs every 5th week);
the 55 km/wk ceiling was **raised
2026-09-16** (user: "with this many days we can build past 55km reasonably") now that the
same volume spreads over five runs instead of four.
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

## Week 5 (of 2026-09-14) — ~45 km

- Mon | Easy | 6km @ 5:45-6:15/km
- Tue | Test | **ALL-OUT 5k TIME TRIAL, OUTDOORS** (replaces Tuesday's sub-T; D1 Squat follows in the PM)
- Thu | Easy | 5km, HR <=140 — **added 2026-09-16 on the day** (user: "im kinda down to run an easy run tomorrow as well")
- Fri | Quality | WU 2km easy; 5x(6min @ 4:50-4:52/km, 60s jog); CD 2km easy
- Sun | Long | 15km @ 5:45-6:15/km

**Amended 2026-09-15 (user's call): hold W4's executed 39.7 km.** The TT day came in at
8.1 km (1.8 km warm-up), not the ~10 assumed, which left the week at ~38.4. Sun long
14 → 15 km (+1 km on W4's executed 14.01 — inside the ~1 km/week long-run cap) and
Fri CD 1.5 → 2 km. Week
lands ~39.9 km: Mon 6.0 + Tue 8.1 (done) + Fri ~10.8 + Sun 15.

**Amended again 2026-09-16: Thursday easy 5 km added**, taking the week to **~44.9 km,
+13% on W4's executed 39.7** — the largest week-on-week step of the block. Accepted under
the RPE-gated rule, and well timed: W7 loses ~10 km to the gorilla treks, so the volume is
better banked now than later. Two consequences, both accepted: it **spends W5's clear day**
(Thursday), and it sits the day before the block's first sub-T session on measured paces,
so it runs at **HR <=140 and no faster** or it costs more than it adds. Plain run, nothing
pushed to Tredict.
**Knock-on:** W6 is planned at ~42 km, now a *step down* from W5. That is fine — W6 and W7
are the travel weeks and act as the dip. W8 is no longer a down week (changed 2026-09-23).

### W5 Friday changed 8x3 -> 5x6 (2026-09-12, user's catch)

Three reasons, all of which I had missed: he **already ran an 8x3 on Thu 09-10**, so the two
sessions would sit 8 days apart — which contradicts them being the minority format; Friday
09-18 is the **first session on TT-derived paces**, the one most worth verifying; and
that verification needs **reps >=6 min**, since the plateau check gives a false pass on
short reps. 5x6 rather than 6x6 because it is 3 days after a maximal TT in a week that
also restarts C14. W6 Tue takes the 6x6 instead.

**Do not push Friday's session before the TT.** Tredict cannot edit a workout's steps,
only its title and notes — so pace targets pushed with guessed numbers are permanent.
Build it Tuesday evening once T-pace is known. W5's push covers Mon, Sun and the four
lifts only; Tuesday stays blank (he uses the GPX route + COROS race-pace screen, and a
competing structured workout is exactly the 09-10 trap).

### Tue 2026-09-15 — 5k TT (decided 2026-09-10, user's call: "fuck it"; moved Wed -> Tue 2026-09-12 with the new week structure)

**RESULT 2026-09-15: 22:07 clock, 21:57 grade-adjusted → VDOT 44.7 → T-pace 4:40/km.**
Sub-T bands: **1–3 min 4:43–4:45, 4–6 min 4:50–4:52, 8–12 min 4:57–4:59.** Peak HR 193
in ~15 °C; HRmax kept at ~200 provisional. Full record, splits and method in
`sub-threshold-reference.md` §8.1, which wins on any disagreement. The planning notes
below were written before the run.

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
number about to anchor everything; and **every later TT in the cadence is outdoors**, so a
belt baseline would not be comparable to them — and comparing them is the point of the
series.

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

## Week 6 (of 2026-09-21) — RWANDA, arrival week, ~25 km run + an MTB weekend

**Rewritten 2026-09-23**, mid-week, once the trip's real shape was known: a found
gym/coworking (so lifting is on), **all running on a treadmill**, and **mountain biking at
Lake Kivu Sat 09-26 - Sun 09-27**. Mon-Wed are recorded as executed, not as planned.
Pushed as Tredict plan `6LiGcCcCA`.

- Mon | Rest | **FLEW STOCKHOLM -> KIGALI.** Travel day — the week's clear day
- Tue | Easy | gym session (a gym/coworking was found)
- Wed | Easy | easy run — **done** + **C14 W2 D2 Dips PM**
- Thu | Quality | TREADMILL. WU 10min easy (HR 110-150); 2min belt ramp; 5x(6min @ **11.5-11.8 kph = 5:06-5:12/km**, 60s float @ ~8 kph); CD 8min easy; ~55min, ~9.5km + **C14 W2 D1 Squat PM**
- Fri | Easy | TREADMILL. 55min, HR 110-150, effort governs; ~8km
- Sat | MTB | **MOUNTAIN BIKING, LAKE KIVU — ~3 h easy** — no run, no lift
- Sun | MTB | **MOUNTAIN BIKING, LAKE KIVU — ~4 h easy** — no run, no lift

Notes: the planned ~43 km week did not survive contact — Monday was the outbound flight,
Tuesday a gym session, Wednesday an easy run, so the week was rebuilt on Wednesday around
what was left of it.
- **One sub-T, not two.** Thursday is the only slot that remains, and it is stacked with
  the squat. This is a calendar constraint, not a design choice — unlike the *original*
  W6 draft, which carried one session for no recorded reason (user's catch, 2026-09-18).
- **Easy runs move to a 110-150 HR band**, replacing the <=140 cap. Heat and altitude both
  raise HR at a given effort, so the error is one-directional: a tight cap would only make
  easy runs easier than intended. Effort governs, HR backstops.
- **~25 km running against the planned 43**, with two days of mountain biking carrying the
  weekend. That is the reduction the user asked for, not a shortfall to be made up.
### TRAVEL BLOCK — Rwanda, 2026-09-21 to 2026-10-05 (told 2026-09-16)

Flights **Mon 09-21 out** and **Mon 10-05, departing 20:00, landing Stockholm midday
Tue 10-06**; **gorilla trekking Fri 10-02 to Sun 10-04**. Based in **Kigali** apart from
the trek. Covers W6, W7 and the front of W8. User's instruction: "i'd like to rescue as
much mileage as possible."

- **No time-zone shift.** Sweden (CEST) and Rwanda (CAT) are both UTC+2 — zero jet lag,
  which is why W6 can carry a normal week's volume from Tuesday onward.
- **Altitude ~1,570 m** in Kigali (confirmed — based there apart from the trek); the Volcanoes NP trek days run ~2,300-3,000 m.
  Unacclimatised, expect sea-level pace bands to be **10-20 s/km optimistic**, and
  Rwanda's terrain is hilly on top of that, so pace is doubly invalid.
- **SUB-T RUNS ON ALTITUDE-ADJUSTED PACE, WITH RPE GOVERNING — changed 2026-09-18
  (user's call: "do a conversion of pace to altitude adjusted pace for rwanda so we
  sidestep this problem").** Supersedes the earlier "run by HR 166-170" prescription.
  **Why HR was dropped:** the 09-18 session ran the 4:51 band at **185-187 bpm** sustained,
  15-19 bpm above the 166-170 tier, and the 09-15 TT's 188 average implies **LTHR ≈ 180-184**
  — so the 83-85%-of-200 tier sits well below this athlete's actual threshold and would
  have prescribed an easy run in place of a quality session. The %HRmax tiers are [C]
  inference (§3) and do not fit him; pace is the anchor he has chosen to trust.
  **Bands for the trip**, converted off 4:50-4:52 for ~1,570 m:
  - **W6 (unacclimatised): 5:06-5:11/km** — sea-level band + 15-20 s/km.
  - **W7 (partially acclimatised): 5:01-5:06/km** — + 10-15 s/km.
  - **W7, 10-min reps: 5:07-5:13/km** — the 8-12 min band (4:57-4:59 = T+17-19),
    same altitude adjustment. Added 2026-09-23 with the rep-length rotation.
    **Longer reps run slower** — do not carry the 6-min band onto a 10-min session.
  **These are guides, not gates.** Kigali is hilly, so flat-ground pace may be
  unreachable at the right effort on the terrain available — in that case run the effort,
  not the number. **The controls remain RPE and the two-more-reps rule**, verified on
  review by the §4 within-rep plateau, which needs neither HRmax nor sea level.
  Revert to the sea-level band on **10-07**, the first quality session home (was 10-09, written when Friday was the first quality day back; corrected 2026-09-23).
- **ALL RUNNING IS ON A TREADMILL (told 2026-09-23).** That changes the prescription unit:
  the belt sets the pace, so sessions are pushed as **time-based steps with kph in the
  title**, and the watch's indoor pace estimate is noise — set the machine, ignore the
  alerts. Two consequences to keep straight: the "Kigali is hilly, so pace is doubly
  invalid" caveat above **no longer applies** — indoors, pace is a real control for the
  first time this trip — while the altitude adjustment **still does**, since the air is at
  1,570 m either way. Treadmill heat remains a listed confounder, so HR-derived
  conclusions are still discarded outright. Keep the incline constant (0 or 1%) so
  sessions stay comparable to each other.
  Belt speeds: **11.5-11.8 kph** (W6, 6-min reps), **11.8-12.0** (W7, 6-min),
  **11.5-11.7** (W7, 10-min), easy ~8.5 kph adjusted to hold HR 110-150.
- **Easy runs need no pace adjustment** — they are HR-governed on a **110-150 band**
  (widened from the <=140 cap on 2026-09-23), so altitude and heat self-correct by
  slowing the belt. ~8.5 kph at 1,570 m indoors is correct execution, not a bad day.
- **Mileage was rescued by adding days, not lengthening them — until 2026-09-23, when
  the two loaded weekends replaced it.** MTB on 09-26/27 and the treks on 10-02/04 are
  the volume now; running drops to ~25 km in W6 and ~28 km in W7 on the user's own call.
  The outbound travel day is W6's clear day, Wednesday 09-30 is W7's, and in W8 it is Tuesday.
- **The three trek days are the week's hard aerobic work, several times over** — 4-8 h
  on steep ground at altitude. Do not run quality around them, and expect the descents to
  produce real DOMS on 10-04/05. W8's Monday flight is the recovery day, and W8 was
  no longer a down week (changed 2026-09-23) — Rwanda's low weeks served that function,
  so W8 comes back at ~44 km rather than dropping again.
- **W10's TT (Fri 10-23) stays put** — 2.5 weeks after return, with W8 and W9 to rebuild.
  Two weeks at 1,570 m is not altitude training; expect no boost and grade it at face
  value like every other check.
- **Lifting continues on schedule, but C14 W2 now spans W6 and W7** — a gym/coworking was
  found 2026-09-23, so nothing slides for lack of equipment. The target is the user's own:
  "i think the goal should be to finish week2 of the block by the time i leave rwanda."
  - **C14 W2 runs Wed 09-23 -> Tue 09-29**: D2 dips Wed, D1 squat Thu, D3 deadlift Mon,
    D4 pull-ups Tue. **C14 W3 does not run in Rwanda** — it starts at home Wed 10-07.
  - **D1/D2 are swapped in W6.** The in-phase rule governs week *numbers*, not day order;
    all four lifts stay in C14 W2, so the swap costs nothing.
  - **This rescues deadlift and pull-up progression.** Under the previous plan those two
    fell on trek days, got no W3 attempt, and their TMs would have held by default into
    C15 — a hold with no evidence behind it. Now all four lifts get a real W3 top set,
    and on home equipment rather than found-gym loads.
  - **Every cycle mapping downstream slides one week.** See `plans/config.md`.
  - **Weights from a found gym are not comparable to the sheet** — different bars,
    plates and calibration. Record what was done, run the prescribed loads if the
    equipment allows, substitute freely if it does not, and **never advance a TM off an
    improvised session**.

## Week 7 (of 2026-09-28) — RWANDA, trek week, ~28 km running + 3 trek days

**Rewritten 2026-09-23** — treadmill running, hard days stacked, and C14 **W2** (not W3)
finishing here. Pushed as Tredict plan `6LiGcCcCA`.

- Mon | Optional | **OPTIONAL easy ~40min**, HR 110-150 — left to feel after ~7 h of MTB. **No calendar entry by design** (easy runs are HR-governed and need no structure). This is the week's clear day; see the note below before spending it
- Tue | Quality | TREADMILL. WU 10min easy (HR 110-150); 2min belt ramp; 6x(6min @ **11.8-12.0 kph = 5:01-5:06/km**, 60s float @ ~8 kph); CD 8min easy; ~62min, ~11km + **C14 W2 D3 Deadlift PM**
- Wed | Easy | TREADMILL. 55min, HR 110-150, effort governs; ~8km + **C14 W2 D4 Pull-ups PM** — closes C14 W2
- Thu | Quality | TREADMILL. WU 10min easy; 2min belt ramp; 3x(10min @ **11.5-11.7 kph = 5:07-5:13/km**, **90s** float @ ~8 kph); CD 8min easy; ~55min, ~9.3km. **No lift**
- Fri | Trek | **GORILLA TREK** (Volcanoes NP, ~2,300-3,000 m) — no running
- Sat | Trek | **GORILLA TREK** — no running
- Sun | Trek | **GORILLA TREK** — no running

Notes: running is front-loaded into Mon-Thu because Fri-Sun are the treks. ~28 km of
running against W7's originally planned 43.5 — but the three trek days are hours on steep
ground at altitude, so the week's *training* is not down 15 km, only its running-specific
part. The user asked for exactly this on 2026-09-23: "we can reduce the amount of easy runs
slightly due to the hiking/mountain biking weekends i got planned."
- **Two sub-T sessions, one 6-min and one 10-min** — Bakken's rep-length rotation (user,
  2026-09-23). Monday is the 6-min session, Thursday the 10-min one, and **Thursday runs
  slower**: the 8-12 min band is T+17-19 against the 4-6 min band's T+10-12. Do not run
  Thursday at Tuesday's belt speed. The two sit **48 h apart** after the shift, which is
  standard Norwegian singles spacing (Tue/Thu), not a compromise. **Float lengths are fixed by rep length** (§7 of
  `sub-threshold-reference.md`): 60 s after a 6-min rep, **90 s** after a 10-min one.
- **Hard days are stacked, not spread** (user, 2026-09-23: "we should stack hard leg days
  together... easy days easy hard days hard"). Monday pairs the sub-T with the deadlift;
  Tuesday is an easy run plus pull-ups, upper body only, so it costs the legs nothing.
  **This supersedes the old "nothing hard on Thursday" rule.** That rule was written when
  W7 also carried a squat day; with C14 W3 moved home, Thursday has room it did not have.
  Going into the treks slightly tired is an acceptable price for a second quality session
  — but err easy on the belt, and it converts to an easy 55min without ceremony if he
  wakes up flat.
- **The whole week shifted one day on 2026-09-23**, when the MTB weekend turned out to be
  **~3 h Saturday + ~4 h Sunday**. Seven hours on the bike is more time on legs than the
  entire running week, and the old layout put the hardest day of W7 — sub-T plus deadlift —
  roughly twelve hours after getting off it. Cycling damages far less than running would,
  so this is not about wrecked legs: it is that a sub-T session run flat is wasted, either
  run slow for nothing or pushed until it stops being sub-threshold. Monday became the
  clear day instead, directly after the biggest aerobic block of the trip. Nothing was
  lost — same three runs, same two lifts, same ~28 km, moved one day right. Executed with
  `planned-workout-change-date` on four entries, the one operation verified to propagate
  to COROS.
- **Monday's optional run costs the clear day, and that is stated rather than hidden**
  (user 2026-09-23: "i think we can plan an easy run on monday as well. though you can
  leave it up to feel"). Taking it makes Sat 09-26 -> Sun 10-04 **nine consecutive
  training days**. This week is what **retired the full-rest-day invariant** outright —
  see `plans/config.md`: clear days now carry an optional easy run governed by feel rather
  than a rule. The trek block made the old invariant fictional here anyway, since no
  arrangement of Fri-Sun is restful. **If it is taken, drop
  Wednesday's easy run**; Wednesday keeps pull-ups, which are upper body and cost the legs
  nothing, making it the closest thing to a clear day the week can offer. Keep it to
  ~40 min, not 55: it is a shakeout after seven hours of riding, not a training run.
- **Lifting closes C14 W2 on Wednesday.** D3 deadlift Tue, D4 pull-ups Wed — the standard
  D3->D4 pair. Squat Thu 09-24 -> deadlift Tue 09-29 is 5 days. C14 W3 starts at home
  Wed 10-07; see the travel-block note.
## Week 8 (of 2026-10-05) — RE-ENTRY, ~44 km. **NOT a down week** (changed 2026-09-23)

- Mon | Optional | easy 5km in Kigali, by feel — day after the last trek, legs likely sore; **flight leaves 20:00**
- Tue | Easy | **LAND STOCKHOLM ~midday** off an overnight flight. Easy 5km in the evening
- Wed | Quality | WU 2km easy; 6x(6min @ **4:50-4:52/km**, 60s jog); CD 1.5km easy; ~11.5km + **C14 W3 D1 Squat PM** — **FIRST SESSION BACK AT SEA LEVEL**
- Thu | Easy | 6km, HR 110-150 + **C14 W3 D2 Dips PM**
- Fri | Easy | 5km, HR 110-150
- Sat | Quality | WU 2km easy; 3x(10min @ **4:57-4:59/km**, 90s jog); CD 1.5km easy; ~10.3km + **C14 W3 D3 Deadlift PM**
- Sun | Easy | 6km, HR 110-150 + **C14 W3 D4 Pull-ups PM**

Notes: **rewritten 2026-09-23 on the user's call — "nah lets start back at 40km/week
straight away", then "an easy on tuesday after i land, then a sub-T on wednesday and we're
back on track."** W8 was a down week of ~35 km carrying C15 W1; it is now a full re-entry
week of ~44 km carrying **C14 W3**.
- **Why this is not reckless despite the +57% step off W7's ~28 km.** Rwanda *was* the
  down block — three weeks at 25-28 km — so a fourth low week would be one deload too
  many. And 40+ is not new territory: **W4 executed 39.7 km**, four weeks earlier.
  Returning to recently-held volume is a different act from climbing past it. The engine
  comes home intact or better (7 h of MTB plus three trek days), with only the
  running-specific tissue having idled. **The ramp discipline still binds above ~40**,
  which is where this block has never been.
- **~44 km, not exactly 40**, because two quality sessions are ~21 km between them. To
  hold 40 exactly, trim the easy days to 4-5 km. Monday's optional run adds ~5 on top.
- **Cross-training does NOT count toward the running ramp** (answered 2026-09-23). The
  cap exists for *mechanical* tissue adaptation, which is loading-pattern specific: seven
  hours of MTB has effectively zero impact and buys no running-specific tolerance. Count
  it in the **recovery** column instead — real fatigue, do not stack hard running on it
  (this is what moved W7). Conversion heuristics (3:1 or 4:1 bike-time to run-distance)
  estimate energy cost and are irrelevant to what the ramp protects. **Trekking is the
  exception**: three days of steep descents is heavy eccentric quad loading, the same
  family as running damage, so the treks count *against* the re-entry week.
- **Wednesday runs on RPE, not on the band.** The sea-level paces derive from the 09-15
  TT — four weeks and a trip earlier, with no post-Rwanda data behind them. First session
  home, three days off the last descent, one night's sleep after a red-eye: if 4:51 feels
  like threshold, it is threshold, and the pace comes down. **The Fri 10-23
  TT re-anchors everything properly.**
- **Lifting resumes Wednesday**, because Tuesday is the arrival day. That puts D3 deadlift
  on **Saturday** to keep squat->deadlift at 72 h, and D4 pull-ups on Sunday. Wednesday
  stacks the sub-T with the squat, which is the standard hard-day pairing.
- **The 10-07 squat is the TM-deciding top set of C14 W3, on trek legs, six hours after a
  sub-T.** A miss there is a *hold*, not a verdict — record it as confounded by the treks,
  the travel and the morning run. Move it to Thursday if Wednesday reads badly.
- **KNOWN CONSTRAINT BREAK, accepted:** Saturday's deadlift leaves **72 h to W9's Tuesday
  squat**, against the standing **96 h deadlift->squat** rule. The compressed week cannot
  satisfy both gaps, and moving the deadlift to Friday would make squat->deadlift 48 h,
  which is worse. **Re-justified 2026-09-23:** the old excuse was that C15 W1 is the
  lightest week of its cycle — but W8 now carries C14 **W3**, the heaviest (75/85/95%), so
  Saturday's deadlift is a *maximal* top set. What still makes this acceptable is the
  other side of the gap: **W9's Tuesday squat is C15 W1 at 65%**, thoroughly submaximal.
  The heavy session is the one with recovery in front of it, not behind it.

Notes W6-W8: sub-T dose runs **36 → 66 → 66 min**, alternating 6-min and 10-min reps every
session from W7 (Bakken's rotation — a two-session week never uses the same rep length
twice). W6 carries a single session because the week was rebuilt mid-flight around the
Kigali arrival and the Lake Kivu MTB weekend. **Sunday is an easy run throughout** — the X
session is deferred until volume holds ~60 km/week (see the schema), so these weeks carry
**two quality days, not three**. **Hill strides start in W9** and run every other week from
there; none during the travel block or the re-entry week.
Down-weeks every ~4th week — **now W12 and W16 only** (W8 dropped 2026-09-23: Rwanda's
three weeks at 25-28 km already served that function). The base block earns its ramp by
paying recovery on schedule. HARD RULE unchanged: any shin/achilles/knee niggle → repeat
the previous week's volume instead of progressing.


## Week 9 (of 2026-10-12) — ~47 km

- Mon | Easy | 6km @ 5:45-6:15/km
- Tue | Quality | WU 2km easy; 6x(6min @ 4:50-4:52/km, 60s jog); CD 2km easy
- Thu | Easy | 8.5km @ 5:45-6:15/km
- Fri | Quality | WU 2km easy; 3x(10min @ 4:57-4:59/km, 90s jog); CD 2km easy
- Sun | Easy | 10km @ 5:45-6:15/km, then **6x(10-15s hill sprint, full recovery)** at the end

Notes: **judge W9 against W6's 43.1 km** (43.1 → 47.2 = +9.5%) — not against W7's trek
week or W8's re-entry, both of which are travel-distorted rather than planned down weeks.
**First strides of the block:** 6 × 10-15 s hill sprints on the end of Sunday's easy run,
walking back for full recovery. About five minutes of work, too short to produce
meaningful lactate. They repeat every other week (W9, W11, W13, W15) and are, apart from
the 5k TTs, the only fast running in the block.


## Week 10 (of 2026-10-19) — ~50 km, 5k progress check

- Mon | Easy | 7km @ 5:45-6:15/km
- Tue | Quality | WU 2.5km easy; 10x(3min @ 4:43-4:45/km, 60s jog); CD 2km easy
- Thu | Easy | 10km @ 5:45-6:15/km
- Fri | Test | **ALL-OUT 5k TT, OUTDOORS, same route as 09-15** (replaces Friday's 4x10; D3 Deadlift follows in the PM)
- Sun | Easy | 11km @ 5:45-6:15/km

Notes: **second 5k of the cadence** — five weeks after 09-15, per the every-5th-week rule
in the schema. It replaces Friday's 4×10, the most intensive sub-T session of the week, so
W10 trades a hard session rather than adding one. **No taper** — it is a check, not a race.
- **Deadlift still follows that evening.** A top set missed after a maximal 5k is
  TT-confounded, same as the 09-15 squat; under the hit/miss rule the TM simply holds.
- **Thursday's 10 km stays as written.** No pre-TT easing: these are deliberately run on
  ordinary legs so the results compare to each other rather than to a tapered peak.
- **Same route** (`stockholm-tt-postlight.gpx`), scored on **grade-adjusted** time
  (`sub-threshold-reference.md` §8.1).
- **Lessons from 09-15:** km 1 is the descent — hold the planned split, don't bank time;
  keep the watch **running** through the 20 s stand-still (on 09-15 it was stopped first
  and the reading was lost); warm up ~3 km with strides before reaching the start.
- Returns T-pace and all three sub-T bands for W11 onward. **Friday's session in W11 is
  built after this**, not before — Tredict cannot edit steps after creation.

## Week 11 (of 2026-10-26) — lifting 7th Week deload, running builds, ~53.5 km

- Mon | Easy | 6km @ 5:45-6:15/km
- Tue | Quality | WU 2.5km easy; 6x(6min @ 4:50-4:52/km, 60s jog); CD 2km easy
- Thu | Easy | 9.5km @ 5:45-6:15/km
- Fri | Quality | WU 2.5km easy; 4x(10min @ 4:57-4:59/km, 90s jog); CD 2km easy
- Sun | Easy | 12km @ 5:45-6:15/km, then **8x(10-15s hill sprint, full recovery)** at the end

Notes: lifting runs the **7th Week Protocol deload** (C14 = W5-W7, C15 = W8-W10,
deload Oct 26 - Nov 1) while **running builds through it** — the same pattern as W4.
Judge W11 against W10, not against the W8 down week.
**Decoupled from the running down week 2026-09-15 (user's call: "idk why lifting and
running need to deload at the same time").** W11 had been both, which left only two
build weeks after W8's down week and four before W16's. Swapping W11 and W12 evens it
out: running down weeks now fall on **W8, W12 and W16**, three build weeks before each.


## Week 12 (of 2026-11-02) — down week, ~40 km

- Mon | Easy | 5.5km @ 5:45-6:15/km
- Tue | Quality | WU 2km easy; 6x(6min @ 4:50-4:52/km, 60s jog); CD 1.5km easy
- Thu | Easy | 5km @ 5:45-6:15/km
- Fri | Quality | WU 2km easy; 3x(10min @ 4:57-4:59/km, 90s jog); CD 1.5km easy
- Sun | Easy | 8km @ 5:45-6:15/km

Notes: running down week, swapped in from W11 on 2026-09-15 (see W11). Lifting starts
C16 here, so this is not a lifting deload.
**The TT that briefly lived here is gone** — it moved to W10 when the every-5th-week
cadence was set (2026-09-16). W12 is now an ordinary down week: sub-T dose drops to 48
min and Sunday is a plain 8 km easy run.


## Week 13 (of 2026-11-09) — ~55.5 km

- Mon | Easy | 6km @ 5:45-6:15/km
- Tue | Quality | WU 2.5km easy; 6x(6min @ 4:50-4:52/km, 60s jog); CD 2km easy
- Thu | Easy | 11km @ 5:45-6:15/km
- Fri | Quality | WU 2.5km easy; 4x(10min @ 4:57-4:59/km, 90s jog); CD 2km easy
- Sun | Easy | 12.5km @ 5:45-6:15/km, then **8x(10-15s hill sprint, full recovery)** at the end

Notes: judge W13 against W11, not against the W12 down week. Sub-T bands come from the
W10 TT (Fri 10-23), adjusted by the W11 and W12 session checks, before this week is synced.

## Week 14 (of 2026-11-16) — ~57.5 km

- Mon | Easy | 6.5km @ 5:45-6:15/km
- Tue | Quality | WU 2.5km easy; 10x(3min @ 4:43-4:45/km, 60s jog); CD 2km easy
- Thu | Easy | 12.5km @ 5:45-6:15/km
- Fri | Quality | WU 2.5km easy; 4x(10min @ 4:57-4:59/km, 90s jog); CD 2km easy
- Sun | Easy | 13km @ 5:45-6:15/km

## Week 15 (of 2026-11-23) — PEAK, ~60 km, 5k progress check

- Mon | Easy | 8km @ 5:45-6:15/km
- Tue | Quality | WU 3km easy; 6x(6min @ 4:50-4:52/km, 60s jog); CD 2.5km easy
- Thu | Easy | 14km @ 5:45-6:15/km
- Fri | Test | **ALL-OUT 5k TT, OUTDOORS, same route as 09-15** (replaces Friday's 4x10; D3 Deadlift follows in the PM)
- Sun | Easy | 14km @ 5:45-6:15/km, then **8x(10-15s hill sprint, full recovery)** at the end

Notes: **third 5k of the cadence, Fri 2026-11-27** — five weeks after W10's, same slot,
same route, replacing Friday's 4×10 again. Peak week: **~60 km — the block target**, longest run 14 km on
Thursday, 41 min of sub-T on Tuesday.
- **Sunday is an easy 14 km with strides on the end**, not an X session — the X session
  is deferred until volume holds ~60 km (see the schema).
- Pace bands here are the 09-15 values — the W10 TT and the session checks will have
  moved them well before this week is synced.


## Week 16 (of 2026-11-30) — down week, ~33 km

- Mon | Easy | 5km @ 5:45-6:15/km
- Tue | Quality | WU 2km easy; 4x(6min @ 4:50-4:52/km, 60s jog); CD 2km easy
- Thu | Easy | 6km @ 5:45-6:15/km
- Fri | Easy | 5km @ 5:45-6:15/km
- Sun | Easy | 8km @ 5:45-6:15/km

Notes: **the Dec 6 all-out 5k is gone** — dropped 2026-09-16 once TTs moved to a fixed
5-week schedule and its date turned out to be arbitrary (user's words). This is now a
plain down week following W15's TT: one sub-T session, easy hills, no test.
Falls in lifting C17 W2 — no accommodation.
**The written block ends here**, but nothing ends with it: the cadence continues (next TT
~Fri 2027-01-01) and W17 onward gets planned when the Barcelona race and date are picked.

## Open items

- Treadmill calibration (brief §7.1) — if the belt runs fast, VO2max outdoor paces
  shift slower. Recalibrate with COROS Track Run mode once the Pace 4 arrives.
- Block endpoint — **retired 2026-09-16.** The block no longer has a single endpoint;
  5k TTs run every ~5th week as progress checks (see the schema). History below.
  Block endpoint (form of 2026-09-03, after two same-day revisions): **no fall
  10k at all** — the endpoint was the **W16 all-out 5k, Sun 2026-12-06**, inside a
  down-week with no taper. Endpoint history: Oct 11 TT vs 45:00-45:30 (2026-08-27,
  after Hässelbyloppet fell through) → moved to Nov 1 vs sub-45 with an Oct 18
  gate (2026-09-03 morning, Norwegian realignment) → scrapped entirely
  (2026-09-03 evening, user: a TT is development budget spent on curiosity; a
  base block to 55 km/wk is the efficient medium-term play). Face-value grading
  and no-solo-discount rules carry over to the 5k. **Open: which race is the
  sub-44 "Barcelona" gate** — **retargeted 2026-09-16 to the spring/summer 2027 window**;
  pick the race and date when the base block is done. No timeline pressure before then. Strides dropped from
  all easy runs per user (2026-08-23). Current race shape: **45:46 10k-equivalent (4:35/km)**, from the 09-15 5k TT; re-measured at W12.
- **Tredict trial ends ~2026-10-17** — before the W10/W11 syncs, and W12 carries the second 5k TT.
  Decide before then: pay the $49/yr or swap the push layer to Intervals.icu.
