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
each replacing that week's Friday 3×10, and the Dec 6 5k is dropped. Calibration between now and then is HR-led:
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
  most intensive sub-T session — the Friday 3×10** (corrected from "4×10" on 2026-10-09:
  every written week schedules a **3×10**, so the TT displaces ~33 min of sub-T, not
  ~44.5 — which makes an all-out 5k a closer swap than the old wording implied) — so the
  week loses a hard session
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
  **And the pace itself moves ONLY at a TT (user 2026-10-09)** — *"i think the hr checks
  should just be a vibe check."* The review reports the three checks and changes nothing;
  the bands wait for the next scheduled 5k. This is the 09-12 split enforced rather than
  altered — "HR diagnoses" had drifted into "HR prescribes".
  On a sub-T session: pace steers, **RPE aborts** (the reserve question is the
  in-session safety valve — a fixed pace on a bad day will cook him; ~a third of the work
  left, so **ONE** more rep on a 3×10, not two), HR diagnoses at review. Sub-T wants flat consistent terrain, since a pace target cannot see a hill.
- **EASY RUNS ARE HR-CAPPED, NOT PACE-CAPPED** (user's call 2026-09-12, from Bakken:
  easy running capped at **70% HRmax**). Pace bands below are now descriptive, not
  prescriptive — the cap governs, and being under it is always fine.
  - **Easy / recovery runs: ≤70% HRmax.** Provisional max **~207** — raised from ~200 on
    **2026-10-08 (user's call)** because two independent routes converge on 205–211
    (`plans/config.md`) → **cap 145 bpm**. The cap is a *fraction of max*, so it moves
    whenever the max assumption does; next check is the **W10 TT (Fri 2026-10-23)**.
  - **THE DRIFT ALLOWANCE IS GATED ON DURATION, NOT ON THE DAY (fixed 2026-10-08).**
    Under ~75 min: one band, **≤145**, full stop. Past ~75 min: open **≤145** and let it
    drift toward **~155** (75%, **[C]**). The previous wording — "Thursday's longest run
    starts ≤140, drift toward ~150" — was a text substitution made by `395fb71`
    (2026-09-16), the commit that *dropped* the dedicated 12–18 km long run: "long"
    became "Thursday's longest" and was never re-derived against Thursday's actual
    duration. **It failed on 2026-10-08** against a 7 km / 52 min Thursday — 20 bpm of
    drift in 52 minutes is not cardiac drift, it is running too hard. User caught it:
    *"why is this run allowed to go hotter with hr? i thought this was a mistake left
    over from the kigali 150 ceiling."*
  - **Long-run drift rationale (unchanged, only rescaled):** Corrected 2026-09-12 —
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
  the W10 5k TT, Fri 2026-10-23.** **Between tests the bands DO NOT MOVE** (user
  2026-10-09) — the review reports the three checks as a vibe check and changes nothing.
  The previous wording here ("the session checks move the bands: all passing easily →
  creep faster; any failing → slow 5 s/km") was retired that date and was missed in the
  first pass of that edit. These replace the
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
  every session with ~a third of its work still in reserve (two more reps on a 6×6, ONE
  more on a 3×10 — `sub-threshold-reference.md` §4.3 **[C]**). If any says too hot, slow the rep. **HR CEILINGS — REPLACED 2026-09-12** (user supplied from Bakken; the old flat ~180
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
  Full intensity map **at max ~207 (rescaled 2026-10-08; the 200-based figures it replaced
  are in brackets)**: easy ≤70% = **145** [140], runs past ~75 min open ≤70% and drift to
  **~155** [150], sub-T 80–87% = **166–180** [160–174] — nothing lives between **155 and 166**.

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
  easy's easy"): Monday, Thursday and every warm-up run **at or under 145
  bpm** (140 when he said it; the number moved with the HRmax rescale on 2026-10-08, the
  condition did not), no exceptions. Easy-pace creep is this athlete's documented failure mode, and it
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
- **Easy runs move to a 110-150 HR band**, replacing the <=140 cap. **[SUPERSEDED
  2026-10-08 — THIS IS THE LINE THAT CAUSED THE BUG. It was a Rwanda-only measure and it
  was never reverted when he flew home, so the 150 ceiling survived into W8's sea-level
  easy runs while the sea-level *pace* bands were consciously restored. Easy runs are back
  on a single cap, now ≤145. Do not read this bullet as live doctrine.]** Heat and altitude both
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
  not the number. **The controls remain RPE and the reserve rule** (§4.3 — a third of the
  work left; ONE more rep on a 3×10), verified on
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
  **[Rwanda-only; SUPERSEDED 2026-10-08 — single cap ≤145 at max ~207. See the schema.]**
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
- Tue | Quality | TREADMILL. WU 10min easy (HR 110-150); 2min belt ramp; 6x(6min @ **12.0 kph = 5:00/km** — top of the W7 band, set 2026-09-25, 60s float @ ~8 kph); CD 8min easy; ~62min, ~11km + **C14 W2 D3 Deadlift PM**
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
- **PACE TARGET ZONES GO ON THE REP STEPS (user, 2026-09-25: "id like for it to contain
  the actual pace bands in the workout, thats more important than the title").** Justified
  by 09-24: the watch's indoor pace matched the belt to **0.02 s/km**, so the 09-23 worry
  that a pace target would alert against a correctly-run treadmill session was unfounded —
  see `CLAUDE.md`. Bands to set, padded to cover the prescribed fallback speed so a
  deliberate drop does not trigger an alert:
  **BOTH SET AND VERIFIED 2026-09-25** (read back via `planned-workout`; stored as
  `targetType: "SPEED"` in m/s even though entered as pace, which suits a belt — the watch
  can render kph, the unit on the dial):
  **Tue 6x6 → 5:00 +/-5 = 4:55-5:05** (11.80-12.20 kph, target **12.0**);
  **Thu 3x10 → 5:10 +/-5 = 5:05-5:15** (11.43-11.80 kph, target **11.6**).
  **The two bands came out exactly adjacent** — they share the boundary 11.80 kph and do
  not overlap, so "the 10-min session runs slower than the 6-min one" is structurally
  impossible to violate while inside either band. Better than the lopsided band first
  proposed for Thursday, which was withdrawn on the evidence that **the UI takes
  value +/- padding, not independent low/high**.
  **Thursday's midpoint is 11.6, NOT the 11.7 top of its band**: Tuesday is already taking
  the step, and moving both sessions in one week changes two variables at once three days
  before the treks.
  **Fallback coverage, stated precisely because "+/-5 covers the fallback" was too loose a
  claim:** Tuesday's 11.8 kph fallback is 305.08 s/km against a floor of 305.0, so it sits
  *on* the edge, not inside — practically irrelevant (the watch read 305.1 for that belt
  speed on 09-24 and alerts on sustained deviation, not tenths), but it is an edge, not a
  margin. Thursday's 11.3 kph fallback (5:18.6) is genuinely outside its 5:15 floor and
  will alert — accepted as the cheaper error, since the alternative band would reach
  Tuesday's speed.
  **Floats and cool-downs stay OPEN** — they exist to be run by feel and should never
  alert. Warm-ups keep their HR target.
  Tredict stores these as `targetType: "SPEED"` in m/s even when entered as pace, which
  suits a treadmill: the watch can render kph, the same unit as the belt dial.
- **TUESDAY RUNS AT 12.0 kph, THE TOP OF THE BAND — set 2026-09-25** after comparing the
  09-24 Kigali 5x6 against the matched 09-18 Stockholm 5x6 (full record in
  `sub-threshold-reference.md` §8.3). Kigali came in **7-10 bpm lower at every matched rep**
  (174/176/178 against 184/185/185) and the two-more-reps answer was yes. Altitude and
  treadmill heat can only push HR *up*, so they bound the finding rather than explaining it
  — the W6 adjustment over-corrected. The competing reading is that **Stockholm was the
  session at fault**, sitting above the 180-184 LTHR estimate; either way Tuesday moves up
  one notch, not two. **RPE still aborts:** Tuesday follows ~7 h of MTB and stacks with the
  deadlift, so if two more reps is not obviously available by rep 4, drop to 11.8 kph.
  **The sea-level bands were deliberately left alone** — the Fri 10-23 TT re-anchors those.
- **Two sub-T sessions, one 6-min and one 10-min** — Bakken's rep-length rotation (user,
  2026-09-23). Tuesday is the 6-min session, Thursday the 10-min one, and **Thursday runs
  slower**: the 8-12 min band is T+17-19 against the 4-6 min band's T+10-12. Do not run
  Thursday at Tuesday's belt speed. The two sit **48 h apart** after the shift, which is
  standard Norwegian singles spacing (Tue/Thu), not a compromise. **Float lengths are fixed by rep length** (§7 of
  `sub-threshold-reference.md`): 60 s after a 6-min rep, **90 s** after a 10-min one.
- **Hard days are stacked, not spread** (user, 2026-09-23: "we should stack hard leg days
  together... easy days easy hard days hard"). **Tuesday** pairs the sub-T with the deadlift;
  **Wednesday** is an easy run plus pull-ups, upper body only, so it costs the legs nothing.
  (Day names corrected 2026-09-25 — this bullet still described the pre-shift week.)
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
- Wed | Quality | WU 2km easy; 6x(6min @ **4:50-4:52/km**, 60s jog); CD 1.5km easy; ~11.5km + **C14 W2 D1 Squat PM** (5@114.98 / 5@131.4 / 5@147.83, FSL 3x5@114.98) — **FIRST SESSION BACK AT SEA LEVEL**
- Thu | Easy | 6km, HR 110-150 + **C14 W2 D2 Dips PM** (5@+2.25 / 5@+14.0 / 5@+25.75, FSL 5x5@+2.25)
- Fri | Easy | 5km, HR 125-145
- Sat | Quality | WU 2km easy; 3x(10min @ **4:57-4:59/km**, 90s jog); CD 1.5km easy; ~10.3km + **C14 W2 D3 Deadlift PM** (5@134.58 / 5@153.8 / 5@173.03, FSL 3x5@134.58)
- Sun | Easy | 6km, HR 125-145 + **C14 W2 D4 Pull-ups PM** (5@BW / 5@+4.0 / 5@+14.5, FSL 5x5@BW)

Notes: **rewritten 2026-09-23 on the user's call — "nah lets start back at 40km/week
straight away", then "an easy on tuesday after i land, then a sub-T on wednesday and we're
back on track."** W8 was a down week of ~35 km carrying C15 W1; it is now a full re-entry
week of ~44 km carrying a **re-run of C14 W2** (changed again 2026-09-24 — see below).
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
- **W8 RE-RUNS C14 W2; it does not carry W3** (user 2026-09-24: "my time here in rwanda will
  just be a best effort maintenance of form for the gym. ill prolly just re-run w2 when im
  back in sweden"). Rwanda's lifting counts for nothing — improvised gym, **no dip bars so
  D2 became a bench session**, unknown bar and plate calibration. W2 exists to set up W3,
  the TM-deciding week, so a W2 run on unreadable equipment would make W3 meaningless.
  Weights above are C14 W2, already read from Sheet 17, so no re-read is needed.
  **C14 W3 moves to running W9** and every later cycle slides with it — see `plans/config.md`.
  Two things this fixes: dips no longer jumps W1 -> W3 with a ~12 kg top-set step, and the
  W15 TT moves into C16 W2 so its Friday deadlift is 80% rather than 95%.
  **A miss on the 10-07 squat is a hold, not a verdict** — confounded by the treks, the
  travel and the morning run. Move it to Thursday if Wednesday reads badly.
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


## STEP LOADING — the progression model from W8 (user's call, 2026-09-24)

**Replaces the linear ramp with fixed down weeks.** User: "instead of doing deload weeks,
i think lets do like a stepwise increase and then maintain a bit with the mileage... then
we can bump it to 45 and maintain, etc."

**Steps are aligned to the 5/3/1 cycle (user 2026-09-24):** "it would be nice to line them
up, so the easiest 5/3/1 week is the same week i add volume." Every step-up therefore lands
on a lifting **W1** (65/75/85%) rather than a W3 (75/85/95%) — which matters most exactly
where it should, since the step week is the riskiest running week of each block.

**Plateaus alternate 4 and 3 weeks to make that hold.** Lifting is not on a 3-week cycle
but a **7-week supercycle** (3 + 3 + 7th Week deload); that extra week inserts a one-week
offset every six lifting weeks, so fixed 3-week plateaus would drift until step-ups landed
on 95% weeks. The **4-week plateaus absorb the deload in their final week**.

| Wk | of | Running | Lifting |
|---|---|---|---|
| W8 | 10-05 | 40 — re-entry | C14 W2 |
| W9 | 10-12 | 40 | C14 W3 |
| **W10** | 10-19 | **45 — step** | **C15 W1** · 5k TT Fri 10-23 |
| W11 | 10-26 | 45 | C15 W2 |
| W12 | 11-02 | 45 | C15 W3 |
| W13 | 11-09 | 45 | *7th Week deload* |
| **W14** | 11-16 | **50 — step** | **C16 W1** |
| W15 | 11-23 | 50 | C16 W2 · 5k TT Fri 11-27 |
| W16 | 11-30 | 50 | C16 W3 |
| **W17** | 12-07 | **55 — step** | **C17 W1** |
| W18 | 12-14 | 55 | C17 W2 |
| W19 | 12-21 | 55 | C17 W3 |
| W20 | 12-28 | 55 | *7th Week deload* · 5k TT ~Fri 01-01 |
| **W21** | 01-04 | **60 — step** | **C18 W1** |

**The first step is deliberately unaligned** — W8 is C14 W2, not a W1 — and that is the
safe one to have out of position, since 40 km is ground already held.

**Bonus the alignment produces: the 4-week plateaus carry a hidden systemic deload.**
Running holds flat while lifting drops to 40/50/60%, so total leg load falls without
giving up a kilometre. A better deal than the scheduled running down weeks this model
deleted.

**Subtlety it creates: judge those promotions on week THREE, not week four.** The
promotion check asks whether the block's last week felt easier than its first — on a
4-week plateau the last week is the lifting deload, so of course it felt easier. Comparing
a light-lifting week against a normal-lifting week would promote on a confound.

Why this over a linear ramp, in the order the reasons actually matter:
1. **It self-heals when weeks break, and his weeks break.** A linear ramp assumes an
   unbroken chain — miss a rung and the next week is a double step, which is how W5 fell
   apart and how Rwanda scrambled W6-W7. Under step loading a broken week is just a
   repeated week: re-run the step, nothing downstream moves. With a volatile calendar
   this beats a plan that is faster on paper.
2. **Tissue adapts on a slower clock than the engine.** Tendon, bone and fascia take weeks
   to months; a linear ramp never lets him *sit* at a volume long enough to consolidate.
   Week three of a block is the first time the legs run that distance with that distance
   already in them.
3. **The niggle rule was already step logic** — "any niggle → repeat the previous week's
   volume" has been in this file from the start. This makes it the default, not the
   exception.

**Cost, stated honestly:** ~60 km/week arrives the week of **2027-01-04** rather than end
of November — later still than the mid-December figure quoted before the 5/3/1 alignment,
which costs two more weeks.
With no race until spring/summer 2027 that is free — and it leaves a full spring for
race-specific work on top of a properly consolidated base.

**Four rules that make it work rather than stagnate:**
- **Plateau length tracks familiarity AND the lifting cycle.** Two weeks for ground already
  held (40), then alternating 4 and 3 so every step-up lands on a lifting W1 — see the
  table above.
- **Promote on feel, not on the calendar.** Step up when a block's LAST week felt *easier*
  than its first. If it did not, repeat the block. Same RPE gate that replaced percentage
  caps on 2026-09-07. **The failure mode here is sitting at a level after it has stopped
  asking anything** — that is what this check exists to catch.
- **Deloads are triggered, not scheduled.** The fixed W12/W16 down weeks are **removed**.
  A down week fires when a block's final week feels harder than its first, on any niggle,
  or after a real disruption. Keep **one genuine deload every ~10-12 weeks** regardless,
  as a backstop — slow fatigue accumulation is exactly what people fail to notice in
  themselves.
- **Growth goes on the easy days, not onto one run.** Per-session load is the injury lever,
  so six runs growing under a kilometre each beats +5 km on a single day. **Quality
  sessions stay structurally stable** across a block; the easy days carry the step.

## Week 9 (of 2026-10-12) — ~43.0 km, **a block high**. C14 W2 catch-up **+ the 5k TT pulled forward from W10** (rewritten 2026-10-13)

- Mon 10-12 | — | **nothing.** Lost to study; no calendar entry
- Tue 10-13 | Lift | **C14 W2 D3 Deadlift — DONE.** RPE 8, top set 5 @ 173.03 hit. No run
- Wed 10-14 | Quality | WU 14min; 6x(6min @ **4:48-4:54/km**, 60s float); CD 10min; ~11.6km. No lift
- Thu 10-15 | Easy | **8km**, HR 125-145 — the week's longest easy run, carries the decoupling measurement + **C14 W2 D4 Pull-ups PM**
- Fri 10-16 | Quality | WU 14min; 3x(10min @ **4:55-5:01/km**, 90s float); CD 10min; ~10.0km. No lift
  **EXECUTED 2026-10-16, and the reserve check FAILED. Reviewed 2026-10-17.** 10.29 km / 58:34,
  belt segments at exactly **3.36 m/s = 4:57.6/km** against the prescribed 4:58 +/-3 — pace dead
  centre (and it confirms only that he entered 12.1; treadmill pace cannot corroborate the belt).
  **Rep HR means 176.6 -> 185.7 -> 191.9**, max **197**, session spread **+15.3 bpm** against an
  expected 5-8 for a 3x10. **13.2 min at or above 190 bpm, 4.2 min at or above 195.** A 44 s walk
  logged immediately after rep 3.
  **THE SPREAD IS DISCARDED, NOT ASTERISKED — FIVE confounders, all pushing HR the same direction
  as the observation:** **NICOTINE** (see the W9 window note below), **no pre-run fuel** (user 2026-10-17: *"i didnt fuel before the run"* — low
  muscle glycogen raises HR and RPE at fixed workload, and threshold work is where it bites because
  lactate steady-state is substrate-dependent), **disrupted sleep two nights prior**, indoor thermal
  load with no confirmed airflow, and a third consecutive running day. Attribution is impossible.
  **I briefly wrote that "the prescription itself may now be wrong" and WITHDREW it** — it cannot be
  sustained against a session in this state.
  **THE BAND IS NOT INDICTED, and that is the user's own read** (2026-10-17: *"in general i think the
  bands are ok though, just given that i recover properly"*). The clean datapoint behind it is the
  **10-07 6x6, rep mean 175.0 = 84.5% of 207**, dead centre of the tier. 10-14 (humidity) and 10-16
  (four confounders) are both discarded; **two confounded sessions do not overturn one clean one.**
  What the conditional does carry: the bands have little headroom for a session that is neither
  rested nor fuelled.
  **RESERVE: FAILED** — user 2026-10-17: *"i dont think one more rep was there tbh, at least not a
  quality rep."* This is the one check that still decides anything, and it is a **non-HR** signal, so
  unlike the spread it survives the confounder discard. It confirms the session was genuinely
  overcooked **for the state he was in** — not that the band is wrong. Doctrine says the decision
  point is during rep 2 and the session should have ended there; rep 3 was run anyway, 48 h before a
  TT that sets five weeks of bands. **Second time running that the session designated "the one that
  gives if anything has to" gave nothing.**

**NICOTINE WINDOW: 2026-10-14 to 2026-10-17, POUCHES, DOSED BEFORE SESSIONS *AND* EVENINGS.**
Disclosed by the user 2026-10-17 (*"i just realized i started taking nicotine pouches on wednesday
for the first time in a long while"*; first use in a long while, bought to mark passing his driving
test, **quit 2026-10-17**). Nicotine is a **sympathomimetic** — catecholamine release, HR up roughly
**10-15 bpm at rest** for a meaningful dose, submaximal exercising HR elevated, peripheral and
coronary vasoconstriction. Dose per pouch varies widely and was not recorded.

**THIS CONTAMINATES THREE SESSIONS AND TWO METRIC SERIES. Annotate, do not re-derive:**
- **10-14 6x6** — the 18.6 bpm spread was already discarded for humidity + the 352 AU deadlift at
  24 h. Nicotine is a **third** same-direction confounder and **it started that day**. It also
  explains the one observation nothing else did: *"my hr came up super quick when i was warming
  up."* Humidity raises HR **progressively** as thermal load builds; it does not produce fast
  warm-up kinetics. Nicotine does. The *"full of energy"* and *"speed was almost too low"* reports
  from the same session are stimulant effects too.
- **10-15 easy 8k** — 7:57/km at HR 141 against 10-08's first half of 7:52 @ 139.9. If nicotine
  inflated submaximal HR, the <=145 cap bit at a lower true effort. **A third candidate for "why is
  my easy pace sad," alongside steady-vs-negative-split compliance and 48 h post-deadlift fatigue.**
  All three push the same way, so attribution is impossible. Cheap test: one easy run, no pouch, and
  compare pace at 141.
- **10-16 3x10** — fifth confounder, as above. The discard was already correct; now overdetermined.
- **Overnight RHR and HRV, 10-14 onward** — pharmacologically elevated. The 7-day rolling RHR is the
  one metric `wearable-metrics-reference.md` says earns a conclusion, and it will drift up for
  reasons unrelated to load. **Do not read it as accumulated fatigue.**

**WHAT SURVIVES, AND IT IS THE USER'S POINT (2026-10-17):** *"it doesnt raise max hr thought right?
so hitting 197 still supports a higher max."* **He is right, and I had been sloppy** — I wrote that
nicotine "can raise the peak number you observe," which is wrong in a way that matters. **HRmax is a
ceiling; nicotine does not lift it**, it only lets you reach a higher *fraction* of it at a given
workload. So **any validly-observed HR is a floor, and 197 is a floor** — conservatively, since
wrist optical **under-reads** peaks (the stated reason HRmax was held at ~200 after 09-15 peaked at
"only" 193). **HRmax = 200 is now close to ruled out:** it would make Friday's rep-3 mean of 191.9
**96.0% of max sustained for ten minutes** on a completed sub-T session, and the 09-15 TT's average
of 188 would be **94% of max as a 5k average**. Both implausible. Against 207 they are 92.7% and
90.8% — textbook. **207 stands as the working assumption and the easy cap does not move; the
December revisit is untouched.** What nicotine *does* undercut is only the secondary inference
*"I touched 197 without trying, so max must be well above it"* — that gap is no longer estimable.

**SAT 10-17 EASY 5K WAS RECORDED AS TWO FILES, AND IT IS NOT A DOUBLE COUNT.** `oa8U8kS8ydviyjDVGBsHaT`
(10:08) then `jjBEPLANAQ6UNCNdMuWLEZ` (10:16). **I told him to delete the stray one; there is no stray
one** — user, 2026-10-17: *"no it wasnt a double count, i was getting frustrated at the clock beeping
because of hr, so i ended the activity early and did a regular run for the last 4k."* So ~1 km on the
structured workout, ~4 km as a plain run. **Both files are real, together they are the one 5 km
session, and NEITHER should be deleted.**
**THE FINDING IS THE BEEPING, AND IT IS A REPEAT.** The easy band is 125-145 (value 135, padding 10).
With HR pharmacologically elevated this week, he sat against the 145 ceiling and the watch alerted
continuously — **so an HR target drove him off a correctly-executed easy run.** This is the third
instance of the same class: W5's easy 6k and long 14k were pushed with *pace* bands that would have
alerted him for running correctly at 140 (2026-09-12), and the 09-18 cool-down carried an HR target
that could not be met because HR decays from the last rep rather than settling (2026-09-18, fixed by
dropping the zone type on cool-downs). **A target that cannot be met does not discipline the session,
it gets the session abandoned.** Worth considering whether the easy band needs wider padding or no
HR target at all on short shakeouts — not actioned, and NOT a reason to touch the <=145 cap itself,
which is parked until ~2026-12-15 by his own call.

**ONE CARRY-FORWARD FOR THE TT:** his reference frame for perceived effort was set on nicotine, and
nicotine blunts RPE. A clean session will feel harder at equal fitness. **Do not let him bail down
from the belt speed on RPE calibrated against the 10-14 and 10-16 sessions** — judge form and HR
runaway instead.
- Sat 10-17 | Easy | **5km**, HR 125-145 — shakeout, cuttable
- Sun 10-18 | Test | **ALL-OUT 5k TT, OUTDOORS, same route** — WU 2km, open TT step, CD 1.5km; ~8.5km

**THE TT WAS DEFERRED TO MON 2026-10-19, AND SUNDAY BECAME AN EASY 7 KM — his call, 2026-10-18.**
*"ok yo its late on sunday the gym is closed i wasnt feeling 100% lets move the TT til tomorrow and
do a 7k easy today to hit the mileage target."* The binding reason is **venue, not feel**: the TT had
already moved to a treadmill, so a closed gym removes the option outright. Feel is the secondary
input and it points the same way.

**VENUE CHANGE — THE LINE ABOVE IS NOW WRONG AND THIS IS THE CORRECTION.** The TT runs on a
**TREADMILL**, not the 09-15 outdoor route (user 2026-10-17: winter is coming, more of the block will
be indoors, and a belt removes pacing skill, which should not be prescribing training paces).
**DO NOT COMPARE THE RESULT STRAIGHT TO 09-15.** The treadmill/outdoor offset is a **venue-pair
property** — airflow, air resistance, terrain, belt calibration — and it has never been measured for
this pair, so the 09-15 -> TT2 delta is **not** a fitness delta. What *is* valid: **belt calibration
error is common-mode and cancels** when the TT and the sub-T sessions share a machine, so a
treadmill-derived T-pace is sound for treadmill prescription. This supersedes the repo's older "belt
error swamps the signal" note, which holds only for *absolute* measurement. **RECORD WHICH MACHINE** —
it is load-bearing for both the cancellation argument and comparability to TT3 on 11-27.

**WHAT THE DEFERRAL COSTS AND DOES NOT COST:**
- **Volume: W9 lands ~41.9 km, not 43.0** (Wed 11.6 + Thu 8.0 + Fri 10.29 + Sat 5.02 + Sun 7.0).
  Still a **block high** (+2.2 km on W4's 39.72) and still clears the step table's 40 km outright.
  The block high survives; only the 43.0 figure does not.
- **Cadence: 10-19 is 34 days off 09-15 against a nominal 35 — dead on**, and better than Sunday's
  33 or the abandoned 10-23's 38. TT2 -> TT3 becomes 39 days. Leave 11-27 alone.
- **Six consecutive running days, ending on the maximal test.** That is a block first; the previous
  high was five. Stated as information, not a veto — Saturday's 5 km was the designated slack and it
  was already spent.

**THE TT TAKES THE 6x6's SLOT AND STACKS WITH MONDAY'S SQUAT — user 2026-10-18:** *"no, lets do the
TT in place of the 6x6's so stacked with the monday squat sesh."* So **Mon 10-19 = 5k TT + C14 W3 D1
Squat**, Tuesday's 6x6 is gone rather than displaced, and W10 keeps **two quality days, not three**.

**I HAD PROPOSED THE OPPOSITE AND IT WAS THE WRONG SHAPE.** I recommended swapping D1/D2 to push the
squat off the TT — i.e. spreading the two hard sessions apart to protect a day. CLAUDE.md says in
terms: *"Do not spread hard sessions across the week to be protective — propose the stacked version
and name the cost,"* and *"stacking OUTRANKS protecting a light day"* (his rule, 2026-09-23, from
muscle tone). **The collision I flagged is not a problem to engineer around; it is the intended
design.** Concentrating the load leaves Tue/Wed genuinely recovered, which spreading does not.
It also fixes the thing I *should* have led with: a TT **replaces** a quality session rather than
being added to one, which is the doctrine he declined for W9 (*"noo, add the TT not replace the
3x10"*) and is applying here.

**THE PRICE, NAMED: the squat's W3 top set becomes unreadable.** C14 W3 is the TM-deciding week — all
four lifts run 75/85/95% and the 95% result decides each TM's +2.5 kg. A squat top set attempted
hours after a maximal 5k is **TT-confounded**, so a miss tells us nothing about the TM and, under the
hit/miss rule, **the squat TM simply holds for the cycle.** That is the cost: one potential +2.5 kg
squat progression, with no reset risk and no spill onto the other three lifts, which keep their own
results. **Precedent exists** — the 09-15 TT was followed by a squat PM on the same reasoning.
**Never propose a TM reset off it.**

**ORDER IS NOT FREE: TT FIRST, SQUAT AFTER.** Lifting costs ~2.6% running economy at 1 h and ~1.6% at
8 h with **no change in exercising HR** (Palmer & Sleivert 2001) — so a squat-first day would quietly
tax the test and no watch metric would show it. Running is the standing tiebreak and this TT anchors
five weeks of sub-T bands, so it gets the fresh legs and the squat eats the interference. If both
happen in one gym visit, the sequence still holds; the gap matters far less than the order.

**VOLUME FALLS OUT AT ~41.5 km, NOT 45** (TT ~8.5 + Tue easy 6 + Thu 10 + Fri 10 + Sun 7), because the
TT's 8.5 km replaces the 6x6's 11.6. That is close to a **repeat of 40** rather than the written step
to 45 — which is also the right answer on its own terms, since the step is conditional on W9 having
felt easier than W8 and three quality sessions, a failed reserve check and "wasn't feeling 100%" is
not that signal. **Repeating 40 is the system working, not a setback.** Grow Thursday/Sunday only if
the TT and Monday's squat both come back clean.

**EXECUTED 2026-10-18: 7.17 km / 46:58 / 6:33/km, avg HR 149, max 164 — THIS WAS NOT AN EASY RUN.**
Per km: **6:53 @ 141 / 6:34 @ 147 / 6:39 @ 145 / 6:28 @ 150 / 6:47 @ 148 / 6:27 @ 156 / 6:19 @ 154**,
then a closing **169 m at 5:08/km @ 161**. **Five of seven kilometres sat above the 145 ceiling** and
the shape is a progression run with a kick, not a flat easy run. Elevation +25 / −28, so terrain
does not explain it. Volume target met and then some — **W9 closes at 42.16 km**, a block high.
**The cost is tomorrow's TT**, which this was supposed to protect; it is the same role Saturday's
5 km was given and the second time in three days that a protective easy slot ran hot.

**IT ALSO MEANS THE NICOTINE TEST WAS NOT RUN.** The designated test, written into the W9 window note
above, was *"one easy run, no pouch, and compare pace at 141."* He ran at **149**, so pace and HR both
moved and the comparison the test was built on is unavailable. **See the review of 2026-10-18 for the
full read; the short version is that the hypothesis is supported but not settled, and it can no longer
be settled** — he has quit, so there is no nicotine condition left to compare against. What survives
is one retrospective triple, outdoor-only and same route: **10-08 clean 7:21/km @ 139**, **10-15 on
nicotine 7:57/km @ 141**, **10-18 clean 6:33/km @ 149**. The two clean runs agree once HR-normalised;
the nicotine run is 36 s/km slower than the slowest of six clean easy runs at 139–144 bpm. But that
spread is itself **41 s/km**, so 10-15 is barely one scatter-width out, and its own confounders
(48 h post-deadlift, the 8:26/km first half, 19 °C) all push the same direction. **Discard stands.**
**Resting HR gives a null:** the 7-day rolling mean went **56.6 → 54.2 bpm** across the nicotine
window — *down* 2.4, inside the ±3.2 noise floor and the opposite direction from the hypothesis.
Weak instrument, though: COROS RHR is a nightly minimum and an evening pouch is largely cleared by
then, so the null constrains resting HR only and says nothing about exercising HR.

**TODAY'S 7 KM SHOULD BE RUN AS A PLAIN RUN WITH NO HR TARGET.** The only calendar entry for 10-18 is
the TT (`dVW8s3zqPNMZkXwVvLVV2A`), which must not be started, and the 10-17 beeping finding above is
the direct precedent: a 125-145 band alerts through the whole first kilometre as HR climbs from rest,
and that is what ended Saturday's structured file early. No entry, no target, by feel.

Pushed as Tredict plan **`uLQvRH4cB`**, 6 entries (5 runs + 1 strength), applied with
**Wed 2026-10-14 as day 1 — NOT Monday.** **~43.0 km over five runs.**
**`sHw2gD5Yj` and `JFWZxaZb8` are dead builds of the same week** — neither was ever applied;
both need binning by hand, since the MCP has no plan-delete tool.

Notes: **the 5k TT moved from Fri 10-23 to Sun 10-18 — his call, and it is a good one.**
*"i also think we can potentially do the 5k TT on sunday since it's turned out to be a
relatively light week lifting wise. lets take advantage rather than stack it on to the top
week of 531."* W10 carries **C14 W3 at 75/85/95%**, the TM-deciding week, and the TT would
have landed beside a 95% deadlift — the exact collision the files avoided for the *W15* TT by
placing it in C16 W2 at 80%. W10 had no such protection. Moving the test **dissolves that open
item rather than sequencing around it.**
- **The cadence is not broken by this; it is improved.** 09-15 -> **10-18 is 33 days**, against
  **38** for 10-23, where the nominal gap is 35. Sunday is *closer* to the five-week cadence
  than the date it replaced — "W10" was always an artifact of TT 1 having fallen on a Tuesday.
  The TT now sits on the **last day of W9**. Cost: TT 2 -> TT 3 stretches to **40 days**
  (10-18 -> Fri 11-27). Leave 11-27 alone — its date is protected by lifting (C16 W2, Friday
  deadlift at 80%), which is worth more than five days of cadence.
- **THREE quality sessions plus the TT — one more than the week budgets, and his decision.**
  I recommended the TT *replace* the Friday 3x10, which is what the doctrine says a TT does,
  on the grounds that the 09-15 TT faded badly from km 4 after 48 h off a 14k long run
  (grade-adjusted 4:06 -> 4:39, power 346 -> 304 W) and that a mis-anchored TT now propagates
  for five weeks. **He declined, twice:** *"noo, add the TT not replace the 3x10"*, and *"i
  still want to go for a top volume week this week if possible."* His reasoning stands on its
  own — the lifting half of the week is the lightest of the block, one legs session and it is
  already done, so the capacity is genuinely there. **Recorded as his call with the cost named,
  not as a doctrine change:** a TT still replaces the Friday 3x10 in a normal week.
- **The 3x10 is on Friday, not Thursday — also his correction.** I had put it Thursday to stack
  it with the pull-ups and buy the TT 72 h instead of 48. *"no, put the 3x10 friday so it's not
  right after tomorrows quality."* Right: back-to-back sub-T days ~22 h apart would have been a
  new pattern, against 48 h as the block's previous tightest. **So the TT gets 48 h and Friday
  is the session that gives if anything has to** — run at the slow end of the band.
- **The TT step is open, no pacing plan — his request.** *"can you just add the TT as an open
  session and ill run it in the same route, i dont think i need help pacing actually."* Which is
  also exactly how 09-15 was pushed ("calendar marker only, no targets, by design"). The notes
  carry only the two measurement instructions: **lap at 5.00 km** (the route climbs 14 m after)
  and **stand still 25 s before moving on** — the 09-15 stand-still happened but the watch was
  stopped first, so the HRmax read was lost, and HRmax ~207 is still an assumption.
- **WU 2 km and CD 1.5 km were added around it on his follow-up** (*"still add the warmup and
  cooldown to the 5k tt"*), matching 09-15's 1.81 and 1.23 km. **Neither carries a target, and
  that is deliberate:** a TT warm-up wants strides in it, which an HR ceiling would alert
  against, and §CLAUDE.md's 2026-09-18 amendment already bars HR targets on cool-downs because
  HR decays from the effort instead of settling into a band. **This forced the third build of
  the week** — `activity-update` reaches title and notes only, so steps are immutable via the
  MCP, and the plan was unapplied so there was no calendar entry for the UI to edit either.
  Rebuilding was free *because* nothing had been applied; after an apply this would have been
  UI surgery.
- **~43.0 km is a block high by 3.3 km** (previous best W4, 39.72) and **+13.3%** on W8's
  executed 37.98. Five runs in five consecutive days, three of them quality, ending in a maximal test.
  Stated as information: the ~10%/week ceiling was retired 2026-09-07 and progression is
  RPE-gated. **Saturday's 5 km is the slack** — cutting it costs the block high, nothing else.
- **No strides this week.** W9 was a strides week, but they only work on an easy Sunday and
  Sunday is now the TT, which does the turnover job far better. They could not move to Thursday
  without corrupting the decoupling run. Back in W11.
- **Decoupling sits on Thursday**, the longest easy run, at ~57 min — still under the ~75 min a
  durability test needs, so continuity rather than evidence. 8 km does give clean 3 km halves
  after the first 2 km are dropped, which the 10-08 run could not manage (a 56 s standing stop
  made four defensible methods span 8 percentage points).
- **Gym days are Tue and Thu — his constraint, and the week is built around it.** Thursday is
  the week's only double, and the cheap kind: easy run AM, `upper` lift PM.
- **Thursday's pull-ups close C14 W2 across all four lifts** (squat 10-07, dips 10-08, deadlift
  10-13, pull-ups 10-15), so **W3 opens in W10 with every lift in phase.** That was the whole
  point of the catch-up. The session has now been missed twice — 10-01 in Kigali and 10-11.
- **The previous W9 plan `JFWZxaZb8` WAS NEVER APPLIED.** Discovered 2026-10-13:
  `planned-workout-list` returned nothing for 10-12..10-20 while every W8 entry was present, so
  the calendar simply stopped at 10-11 and nothing from this week ever reached the watch. That is
  why this rebuild is a clean new plan rather than UI step-surgery — no applied entries to edit,
  no COROS ghosts. **The Tredict MCP has no plan-delete tool**, so `JFWZxaZb8` has to be binned
  by hand in My Own Training Plans.
- **OPEN ITEM FOR W10, sharpened not solved:** a maximal 5k on Sunday leaves **48 h** to W10's
  first quality session as written (Tue). Open W10 with easy Monday *and* Tuesday and push the
  first quality to Wednesday.
- **ALSO FOR W10: its written section is stale.** It still says C15 W1 at 65% and carries the
  Fri 10-23 TT. W10 now runs **C14 W3 at 75/85/95%** with **no TT**. Rewrite before pushing.

## Week 10 (of 2026-10-19) — ~41.5 km, **repeat 40 rather than step to 45**. C14 W3 (75/85/95%, the TM-deciding cycle) **opening with the 5k TT** (rewritten 2026-10-18)

- Mon 10-19 | **Test + Lift** | **ALL-OUT 5k TT, TREADMILL** — WU 2km, open TT step, CD 1.5km; ~8.5km
  **+ C14 W3 D1 Squat (95% top set), TT FIRST** — the week's first quality day, stacked
  **EXECUTED 2026-10-19: 5 km in 21:04.6, belt 14.2 kph for 4 km then 14.4.** Session 8.00 km /
  43:44, avg HR 162. Splits **4:13.8 / 4:13.8 / 4:13.5 / 4:13.5 / 4:10.0**, HR means
  **152 / 186 / 189 / 191 / 194**, peak **196**. Five splits inside 3.8 s then a deliberate kick —
  the belt did exactly the job he moved the test indoors for, and it is the inverse of 09-15's
  4:06 → 4:39 blow-up. **Full record and derivation in `sub-threshold-reference.md` §8.2.**
  **BANDS RE-ANCHORED: VDOT 46.8 → T-pace 4:29 → 4:32-4:34 / 4:39-4:41 / 4:46-4:48, belt
  13.2 / 12.9 / 12.5 kph.** ~11 s/km faster across the board. **These apply at BOTH venues** — his call
  (*"these are the new sub-T paces period"*); the 09-15 bands are superseded, not held in reserve.
  Reasoning in §8.2. **No fitness claim is made from this**: three of the four things that
  shortened the time (no air resistance, the pacing fix, 34 days of training) push the same
  direction, so attribution is impossible under the §6 rule. **HRmax unchanged** — peak 196 is
  below the 197 floor from 10-16, so ~207 and the ≤145 cap are untouched, and the stand-still
  returned no post-finish overshoot.
  **Squat was still to come at the time of review** (TT finished 14:05); its RPE is outstanding.

- Tue 10-20 | Easy | 6km, HR 125-145
- Wed 10-21 | Lift | **C14 W3 D2 Dips** — no run
- Thu 10-22 | Easy | 10km, HR 125-145 — the week's longest, carries the decoupling measurement
- Fri 10-23 | Quality | WU 2km; 3x(10min @ **4:55-5:01/km**, 90s float); CD 1.5km + **C14 W3 D3 Deadlift PM**
- Sat 10-24 | Lift | **C14 W3 D4 Pull-ups** — no run
- Sun 10-25 | Easy | 7km, HR 125-145

Notes: **this section was stale and is a full rewrite.** It previously read "45 km, C15 W1 at 65%,
5k TT outdoors Fri 10-23" — all four of those are wrong now. The TT moved to Mon 10-19 (deferred
from Sun 10-18, see W9), the lifting is **C14 W3 at 75/85/95%** because W9's catch-up closed W2
across all four lifts, and the volume repeats 40.
- **MONDAY IS THE QUALITY DAY AND IT CARRIES BOTH SESSIONS — his call** (*"lets do the TT in place
  of the 6x6's so stacked with the monday squat sesh"*). **Tuesday's 6x6 is deleted, not moved**, so
  the week runs the budgeted **two quality days** (Mon TT, Fri 3x10) with the test *replacing* a
  session rather than adding one. Rationale and the cost I had got backwards are in W9's deferral
  block; the short version is that **stacking outranks protecting a light day**, and spreading the
  two apart would have left Tue/Wed only half-recovered instead of fully.
- **TT first, squat second, and the order is load-bearing.** Lifting costs ~2.6% running economy at
  1 h with no change in exercising HR (Palmer & Sleivert 2001) — squat-first would tax the test
  invisibly. **The squat's 95% top set is therefore TT-confounded: a miss holds the squat TM and
  says nothing about it.** That is the accepted price of the stack. Precedent: the 09-15 TT was
  followed by a squat PM. Never propose a TM reset off it, and the other three lifts are unaffected.
- **Second 5k of the cadence** — 09-15 → 10-19 is **34 days** against a nominal 35, so the deferral
  landed the test *on* cadence rather than off it. **No taper** — it is a check, not a race, and
  Thursday's 10 km stays as written so tests compare to each other rather than to a tapered peak.
- **TREADMILL, NOT THE 09-15 ROUTE — do not compute a fitness delta against 09-15.** The
  treadmill/outdoor offset for this venue pair is unmeasured. Record which machine. Full reasoning
  in W9's venue-change note. Returns are still **5k → VDOT → T-pace → all three sub-T bands**, and
  they are valid for *treadmill* prescription because belt error cancels common-mode across the TT
  and the sessions that share the machine.
- **This is the first honest read on what Rwanda cost or didn't** — two weeks at 1,570 m is not
  altitude training, so expect no boost and grade it at face value.
- **The ~41.5 km is arithmetic, not a cut:** the TT's 8.5 km replaces the 6x6's 11.6. The written
  step to 45 is conditional on W9 having felt easier than W8, and it did not — three quality
  sessions, a failed reserve check and "wasn't feeling 100%" on the Sunday. Repeating 40 is the
  system working. Grow Thursday and Sunday toward 45 only if Monday comes back clean.
- **Strides stay out.** They want an easy Sunday and W11 is the next strides week anyway.
- **Not yet pushed to Tredict.** Needs a plan build before Monday, or Monday runs off the W9 TT
  entry (`dVW8s3zqPNMZkXwVvLVV2A`, still dated Sun 10-18 — in-window, so
  `planned-workout-change-date` would move it rather than needing a rebuild).

## Weeks 11-13 (of 2026-10-26, 11-02, 11-09) — 45 km, the step

- **W11** | Mon Easy 6k · **Tue QUALITY = 10x3min @ 4:32-4:34, 60s float** + **D1 Squat** · Wed **Dips** · Thu Easy 10k · Fri Quality 3x10min @ 4:46-4:48 + **Deadlift** · Sat **Pull-ups** · Sun Easy 7k + strides
- **W12/W13** | Mon Easy 6k · Tue Quality 6x6min @ 4:39-4:41 + **D1 Squat** · Wed **Dips** · Thu Easy 10k · Fri Quality 3x10min + **Deadlift** · Sat **Pull-ups** · Sun Easy 7k

**THE 8x3 LANDS IN W11 — user 2026-10-19:** *"when are we doing the 8x3min sub-T sessions?
didnt i specify i wanted them to be mixed in sometimes?"* **He was right and the miss was
structural, not a one-week slip.** §7 and the note at ~line 152 schedule the 8-10x3 for **W5,
W10 and W14**; W5's became a 5x6 on 09-12, and **W10's was never written into the week at all** —
the W10 section as drafted carried a 6x6 and the TT, so by the time the TT displaced the 6x6
there was nothing short left to displace. **Three planned appearances across the block had
become one.** W10 is applied and is not being reopened (his call); W11 carries it.

- **It replaces TUESDAY's 6x6, not Friday's 3x10** — §7's alternation rule means the week's two
  sessions never share a rep length, so pairing 3-min with 10-min is the only legal placement
  once it goes in. Tuesday also follows only an easy Monday, where Friday follows the week's
  longest run, and the fastest session of the three wants the freshest legs.
- **Band 4:32-4:34** (T-pace 4:29 + the §2 1-3 min offset of 3-5 s/km), watch target **4:33 ±3**,
  **belt 13.2 kph** = 4:32.7/km, inside the band. Float **60 s**, specified not free (§7).
- **THIS SESSION LOSES THE PLATEAU CHECK.** §6: on reps under 6 min the within-rep plateau gives
  a **false pass** — a 3-min rep settles at baseline + the rep's demand, so when the baseline
  creeps the plateau creeps with it. Report it as not applicable rather than as a pass. The
  **reserve question** still works and is the one that decides anything: a third of the work on
  an 8x3 is **three more reps**.
- **There is no expected-spread figure for an 8x3** — the §4.2 table covers 3x10, 6x6 and 4x10
  only. Do not borrow the 3x10's 5-8. Report the raw spread and say the reference is missing.
- **If it ratchets but the reps still plateau internally, lengthen the float before slowing the
  pace** (§4.2) — recovery length is a lever on short-rep sessions specifically, and the 60 s
  float is the one specified value that short reps are allowed to move.
- **TEN REPS, NOT EIGHT — settled 2026-10-19** (user: *"maybe we should be doing 10x3's? or
  9x3's"*). I had written 8 as the cautious end of §7's 8–10 range; **10 is the right call and
  three arguments converge on it.**
  1. **§7's own mechanism says a rep-count-light 3-min session under-delivers.** *"A 3-min rep
     gives much of itself up to HR onset kinetics, while a 10-min rep sits at target intensity for
     8+ minutes."* The §2 pace tiering compensates per rep, but not for the share of each short
     rep spent arriving at intensity. So matching work minutes is the floor, not the target.
  2. **It is a near-exact swap for the 6x6 it replaces.** 10x3 = **30 min work / 64:00 / ~11.0 km**
     against the 6x6's 36 min / 66:00 / ~11.4 km (the 10-14 session ran 66:00 / 11.67 km). 8x3
     would have been 24 min / 56:00 / ~9.5 km — a 33% cut in work for no stated reason. 10x3 also
     matches the week's other session, the 3x10, at 30 min exactly.
  3. **The 3-min session is the SAFEST one to be ambitious on, because the abort granularity is
     fine.** Each decision point commits **4 minutes** (rep + float) against ten on a 3x10. The
     reserve question's answer is *three more reps* on a 10x3 — the figure §4.3 already states —
     so the decision point is around rep 6–7, and being wrong costs four minutes rather than ten.
     This is the same asymmetry that made the 10-16 3x10's failed reserve check expensive.
  **Volume consequence: none.** At ~11.0 km W11 lands ~44 km on the originally written easy days,
  so **Thursday stays 10k and Sunday 7k** — the earlier plan to grow them to 11k/8k was only
  needed to cover the 8x3's shortfall and is withdrawn.
- **LIFTING MAPPING CORRECTED HERE TOO:** this section said C15 **W2** in W11. After W9's catch-up
  slid C14 W3 into W10, **W11 is C15 W1** (65/75/85%), W12 is C15 W2, W13 is C15 W3, and the
  **7th Week deload moves to W14** — which is also where the block's next 8-10x3 is scheduled, so
  that one lands in the lightest lifting week of the cycle. It also said "D2 Squat"; squat is
  **D1**. Strides on Sunday in W11 and W13, unchanged.
**Promotion check runs on W12, not W13** — W13 is the lifting deload, so it will feel
easier for reasons that have nothing to do with running fitness. If W12 felt easier than
W10, step to 50 at W14. If not, hold 45 and let W13's light lifting help — repeating is
the system working, not a setback.

## Weeks 13-21 — the remaining steps

See the step-loading table above for the week-by-week volume and lifting mapping. The 5k
TTs land in **W15** (C16 W2, so its Friday deadlift is at 80%, not 95%) and **W20** (a
7th Week deload — the lightest lifting week of all, and a good place for a test).

**Deliberately not written out day by day.** The block endpoint moved twice on 2026-09-23
and the volume model changed on 09-24; specifying twelve weeks of sessions six months out
is how that churn happens. Each block gets written when the previous one's promotion check
passes, which is also when the sub-T bands will have been re-anchored by the intervening
TT. The shape is fixed — five runs, two quality, strides every other Sunday, growth on the
easy days — only the numbers wait.


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
