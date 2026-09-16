# Sub-threshold reference

Knowledge bank for pinpointing, prescribing and verifying sub-threshold work.
Sources: **Marius Bakken, *The Norwegian Method Applied*** (2026) — relayed by the
user 2026-09-11/12 — plus session evidence from this athlete's own data. Jack
Daniels supplies the T-pace anchor only.

**PROVENANCE — read this first.** Claims are tagged so inference is never mistaken for
doctrine: **[B]** = stated by Bakken, **[D]** = Daniels, **[S]** = this athlete's own
session data, **[C]** = *my inference*, defensible but not sourced. Anything untagged is
mechanism or background, not a prescription. This convention was added 2026-09-12 after
I attributed a long-run HR cap to Bakken that I had invented myself — if you catch
another, tag it or cut it.

This is the **single source of truth for sub-T paces and HR ceilings.** `CLAUDE.md`
points here; `plans/running.md` carries the week-by-week prescriptions derived from
it. If they disagree, this file wins and the others get corrected.

**One-line summary:** sub-T is not a pace, it is a *zone defined relative to
threshold*, tiered by rep length, verified in-session by HR shape rather than by
hitting a number.

---

## 1. The three anchors

Sub-T can be located three ways. They are ranked by directness — prefer the one
highest on the list that has fresh data.

### 1.1 30-minute TT → LTHR → golden zone  *(primary HR anchor)*

> Run **30 minutes at the fastest sustainable steady-state pace**. The **average HR
> of the final 20 minutes is LTHR**. The sub-T **"golden zone" = LTHR − 4–7 bpm.**

- **Needs no HRmax at all**, which is its main virtue — the same property that makes
  the within-rep plateau test robust.
- Costs little: a 30 min steady effort *is* roughly a threshold session, so it
  substitutes for a quality day rather than adding to one.
- **Repeat every 4–6 weeks** — LTHR drifts as fitness comes, and a stale anchor
  silently makes every session too easy.

### 1.2 5k TT → T-pace → pace offsets  *(primary pace anchor)*

> All-out 5k → **Daniels VDOT** (the tables take a 5k time *directly*) → **T-pace** →
> apply the rep-length offsets in §2.

**No Riegel step is needed here** — that conversion is only for the 10k-equivalent
used for race gates and for comparing TTs across distances. Corrected 2026-09-12; an earlier
version of this file routed the pace derivation through Riegel unnecessarily.

- Also yields a **near-max HR** at the finish (a 5k finish lands within a few bpm of
  true max), which feeds §3.
- Sanity check on the output **[C]**: T-pace should land roughly **10k race pace +
  6–10 s/km** for a runner in the 40–50 min range. My rule of thumb, not Daniels'.

### 1.3 %HRmax zones  *(fallback)*

Use only when neither test above has fresh data. See §3.

### The two TTs are NOT interchangeable

A ~22 min 5k is run **above** threshold, so its average HR sits **4–8 bpm above
LTHR**. Never read a 5k average as threshold HR. The 5k gives **performance +
near-max**; the 30-min gives **LTHR**. Two anchors, two tests, both wanted.

**Decision 2026-09-12: one TT only — the 5k.** *(Amended 2026-09-16: 5k TTs now run every ~5th week as routine checks — 09-15, Fri 10-23 (W10), Fri 11-27 (W15) — each replacing that week's Friday 4×10. Still no 30-min TT.)* The 30-min TT is documented here but
**not scheduled**, and that costs less than an earlier draft of this file claimed. The
5k anchors the **pace** side completely, and pace is the prescription. What is lost is
only LTHR, which would have been a second, redundant route to the same place.

**WHICH SIGNAL GOVERNS WHICH SESSION** (user's call 2026-09-12: "lets aim to run long
and easy runs roughly off hr and the sub-T work off pace goals"):

| Session | Governed by | Why |
|---|---|---|
| Easy / recovery / long | **HR** | Long enough for HR to settle; no precision needed, just a ceiling; pace varies hugely with terrain and fatigue while the physiological target does not |
| Sub-T reps | **Pace** | 3–10 min is exactly where HR lag bites worst, and HR is confounded by heat, sleep and illness; pace is instantaneous and anchored to a measured T-pace |

Three-way division of labour on a sub-T session:
- **Pace steers**, in real time.
- **RPE aborts** — the two-more-reps question is the in-session safety valve. Running a
  fixed pace on a bad day will otherwise cook him. If reps 4–5 say there aren't two more
  left, end the session regardless of the watch.
- **HR diagnoses afterwards** — plateau shape (§4) and drift spread (§5), read at review.
  The §3 tiers are therefore a **post-hoc check, not a ceiling he watches while running**.

Operational: pace targets don't know about hills or wind, and a fixed 5:00/km over-cooks
every climb. Run sub-T on flat consistent terrain, or score it on grade-adjusted pace at
review rather than raw.

**The resulting hierarchy — use it in this order:**

1. **Prescribe from pace.** VDOT → T-pace → §2 offsets. Measured, from Tue 09-15.
2. **Verify in-session.** §4's three checks. These need **no anchor of any kind** and
   are what tells you the derivation was right.
3. **HR ceilings (§3) are a soft rail, not the prescription.** They run as %-of-max off
   a max that is approximate — the 5k finish reading is a *floor*, since wrist optical
   under-reads peaks by 5–15 bpm. **If §3 disagrees with 1 and 2, §3 loses.**

Rationale for choosing the 5k over the 30-min: the block's recurring progress check is a
5k (every ~5th week from 2026-09-16), so a 5k baseline makes each result directly
comparable to the last.

---

## 2. Pace by rep length

Bakken tiers sub-T pace by interval duration: **shorter reps run closer to
threshold, longer reps further below it.**

**Headline rule:** sub-T runs **~8–12 s/km slower than Daniels T-pace**. That figure
is the **4–6 min tier** — the bread-and-butter session — not a blanket offset.

| Rep length | Offset from T-pace |
|---|---|
| 1–3 min  | **T + 3–5 s/km**   |
| 4–6 min  | **T + 10–12 s/km** |
| 8–12 min | **T + 17–19 s/km** |

Each tier is **~7 s/km slower than the one above**; each band is **~7 s/km wide**.

**Worked example, verbatim from the book** — use it to check any derivation:

> If threshold is **4:15–4:20**: run **1–3 min** reps at **4:18–4:25**, **4–6 min**
> at **4:25–4:32**, **8–12 min** at **4:32–4:39**.

**Why the tiering exists** (mechanism, in case it needs defending):
1. Lactate needs time to accumulate — end-of-rep lactate is lower after 3 min than
   after 10 at the same pace, so the short rep must run faster to reach the same dose.
2. Recovery ratio — 8×3min/60s ≈ 1:3 clearance, 3×10min/90s ≈ 1:7. More frequent
   clearance lets each rep sit slightly higher.
3. Oxygen kinetics — every rep opens with a deficit partly repaid in the float; more
   reps means more of the work rides that repeated transient.

---

## 3. HR by rep length

**Bakken: the threshold zone for a well-trained amateur is 80–87% HRmax.**

Do **not** confuse this with **Daniels T-pace at 88–92% HRmax**, which is **LT2** —
the top of threshold, not sub-threshold. Setting sub-T ceilings off the 88–92% anchor
makes every session too hot; this project did exactly that until 2026-09-12.

**The zone is 80–87% [B]. The split across rep lengths below is [C]** — my construction
by analogy with his pace tiers in §2, not something he states. Treat the boundaries as
soft; the §4 checks outrank them.

| Tier | % HRmax |
|---|---|
| 1–3 min  | 85–87% **[C]** |
| 4–6 min  | 83–85% **[C]** |
| 8–12 min | 80–83% **[C]** |

Read as **end-of-rep values** — HR lags, especially on short reps.

**Full intensity map:** easy/recovery **≤70%** **[B]**, long run **starts ≤70%, drift
allowed** (see below), sub-T **80–87%** **[B]**, Daniels threshold **88–92%** **[D]**.

**Long run — corrected 2026-09-12.** Bakken specifies **≤70% for easy/recovery runs
[B]** and nothing separate for long runs; an earlier version of this file carried a
"≤75% long-run cap" **attributed to him that I invented [C]**. The honest position:
**cap the opening at 70% and let it drift**, rather than setting a higher ceiling. The
drift reasoning is sound **[C]** — a fixed 70% ceiling over 90+ min forces progressive
slowing to chase a number rising for thermoregulatory reasons — and there is real
support for long runs sitting above 70%, but it comes from **Daniels' E pace, 59–74%
VO2max ≈ 65–79% HRmax [D]**, not from Bakken.

**Cross-check between §1.1 and §3 [C]** (the LTHR ≈ 88–90% of max step is general
physiology, not from either source): the golden zone (LTHR − 4–7) ≈ **84–87%** — i.e.
the **1–3 min tier**. So the golden zone is the
short-rep end of the ladder, and longer reps sit progressively below it. That is the
same direction the pace offsets tier, from two independent systems.

---

## 4. In-session verification

Run all three on **every** sub-T session. Needs **lap data plus the HR stream** —
lap averages alone actively mislead (see §6).

1. **Within-rep plateau** — on reps **≥6 min**, HR must level off in the second half
   and hold. Still climbing at the end of every rep → the pace is above threshold.
   A plateau at a fixed work rate *is* the sustainable-steady-state boundary measured
   on the day, so this needs no pinned HRmax and should be preferred to a % ceiling.
   It should plateau **early and comfortably**, not barely by the end.
2. **Session spread** — see §5.
3. **Two more reps** — he must finish able to do two more. Ask; his RPE is reliable.

**All three passing easily → creep the pace faster. Any failing → slow 5 s/km next
session.**

---

## 5. Expected HR drift

**Bakken: expect 7–10 bpm of spread across a 6×6 session at identical lactate.**
That is what *correct execution* looks like, not a failure — HR rises while lactate
holds flat because plasma volume falls with sweating, stroke volume drops, and HR
rises to maintain cardiac output. Core temperature does the rest.

| Spread across session | Read |
|---|---|
| **< 5 bpm**   | Probably too easy — propose creeping the pace faster |
| **7–10 bpm**  | Correctly pitched — leave it alone |
| **> 10–12 bpm** | Lactate is rising — slow 5 s/km next session |

**Scale by session duration [C].** 7–10 is quoted for a 6×6 **[B]**, which with 60 s
floats runs ~41 min. Scaling that to the other staples — my figures, not his:

| Session | Duration with floats | Expected spread |
|---|---|---|
| 3×10 | ~33 min | **5–8** **[C]** |
| 6×6  | ~41 min | **7–10** **[B]** |
| 4×10 | ~44.5 min | **7–10** **[C]** |

A 4×10 is the *longest* staple session, so do not read its spread against the 3×10
figure.

**Recovery length is a lever — but only on short-rep sessions.** If a session ratchets
*but the reps still plateau internally*, the mechanism is accumulation from short floats
rather than reps in the severe domain. On **3-min sessions**, lengthen the float before
slowing the pace — it preserves more of the stimulus. On **6- and 10-min sessions the
floats are specified (60 s / 90 s) [B]**, so pace is the only lever there.

---

## 6. Confounders and failure modes

- **On reps <6 min the plateau test gives a FALSE PASS.** Short reps do plateau — but
  a 3 min rep settles at *baseline + the rep's demand*, so when the baseline creeps
  the plateau creeps with it and the check still reads as a pass. Only 6–12 min reps
  reach the true steady state for that pace. **Anchor bands on long-rep sessions and
  derive short-rep paces from them.**
- **Lap averages hide float recovery.** HR keeps *rising* for 15–20 s into a float, so
  the float's average reads high and recovery looks absent when it isn't. Always use
  the HR stream.
- **Data source:** the COROS MCP exposes **no HR time series** and
  `analyzeActivityDetail` only re-summarises. Pull the stream from Strava
  `get_activity_streams`.
- **Treadmill:** no airflow → thermal drift well above the 5–10 bpm/hr baseline.
  Belts also run 2–5% off with no way to detect it, so never set paces from one.
- **Illness / alcohol / poor sleep:** raise HR at any given intensity. When a
  confounder is present, **discard HR-derived conclusions outright** rather than
  asterisking them, and fall back on running power, stride length, cadence, ground
  contact time, grade-adjusted pace and RPE.
- **Wrist optical:** under-reads 5–15 bpm at maximal effort and lags 10–30 s on rapid
  changes. Cadence-lock is a live risk here — his cadence (163–172) overlaps his easy
  HR (155–170), so a locked reading looks plausible. If HR sits pinned near cadence and
  barely moves, break stride and see if it responds.

---

## 7. Session menu

**Bakken's bread-and-butter sub-T sessions are 6×6 min and 3–4×10 min.** Those are the
staple. Shorter/faster work (8–10×3 min) stays in the rotation as the **minority** —
three appearances across the whole Sep–Dec block against sixteen staple sessions.

**Alternate rep length**: the two weekly sessions never use the same one. A 6-min day
pairs with a 10-min day.

**Recovery lengths are specified, not free parameters [B]** (user 2026-09-12):

| Rep length | Float |
|---|---|
| 3 min  | 60 s |
| 6 min  | **60 s** |
| 10 min | **90 s** |

**The 10-min intervals are the toughest session [B]** (user 2026-09-12). Mechanism:
they have the **tightest relative recovery** (600 s work : 90 s float = 6.7:1, against
6:1 for a 6-min rep), and they spend the **most time at true steady state** — a 3-min
rep gives much of itself up to HR onset kinetics, while a 10-min rep sits at target
intensity for 8+ minutes. Same nominal zone, far more time actually in it. That is
precisely what the pace tiering in §2 compensates for: T + 17–19 s/km for the 10s
against T + 10–12 for the 6s.

**Two consequences:**
- **The 4×10 belongs on Friday**, which follows Thursday's full rest day and therefore
  has the freshest legs of the week (Tuesday sits two days off Sunday's X session). The cost
  lands on that evening's deadlift, which is the accepted trade under running-priority.
- **The 10-min sessions are the best diagnostic in the week.** §4's plateau check needs
  reps ≥6 min and works best on the longest ones, since a 10-min rep has time to reach
  and hold a genuine steady state. So the hardest session also carries the most
  information about whether the §2 pace derivation is right — weight it accordingly at
  review.

Note the 6 min rep runs a **1:6 work:recovery ratio** — tight. That has a consequence
for §5: **"lengthen the float before slowing the pace" no longer applies to 6- and
10-min sessions**, since the float is now doctrine. On those, **pace is the only
adjustment lever**. The float remains negotiable only on the short-rep sessions, which
is where the 09-10 accumulation problem actually occurred.

Weekly sub-T dose in the current block runs **60 → 76 min**.

---

## 8. Current state (update as tests land)

| Quantity | Value | Status |
|---|---|---|
| HRmax | ~200 | **PROVISIONAL — kept 2026-09-15 (user's call).** The 5k TT recorded a peak of only **193**, run outdoors in ~15 °C — cool, so no heat pushing HR up — on wrist optical, which under-reads maximal peaks by 5–15 bpm (§6). That is below the 195 floor observed 2026-08-20 (altitude, recovery jog), so it neither lowers nor pins the max. Next chance: the W10 5k TT, Fri 2026-10-23. |
| LTHR | — | **NOT MEASURED, and will not be** — 5k TTs only; the 30-min TT is not scheduled. Golden-zone method unavailable. |
| VDOT | **44.7** | **MEASURED 2026-09-15**, from the grade-adjusted 5k (21:57). Raw clock gives 44.3. See §8.1. |
| T-pace | **4:40/km** | **MEASURED 2026-09-15**, from VDOT 44.7. Raw clock gives 4:42. See §8.1. |
| 10k shape | **45:46** | **DERIVED 2026-09-15** — Riegel from the grade-adjusted 5k (raw clock: 46:07). Replaces the unmeasured 47:00 (his August estimate); lands between that and Strava's 44:00. |
| Easy cap | ≤140 bpm | Provisional on max 200 |
| Long-run cap | ≤150 bpm | Provisional on max 200 |
| Sub-T paces | **4:43–4:45 / 4:50–4:52 / 4:57–4:59** | **MEASURED 2026-09-15** — T-pace 4:40 plus the §2 offsets, for 1–3 / 4–6 / 8–12 min reps |
| Sub-T ceilings | 170–174 / 166–170 / 160–166 | Provisional on max 200 |

**Until 2026-09-15 every running data point in this block was a floor, not a
measure** — Midnattsloppet was paced blind, the 09-02 tempo was run to a prescription,
the 09-10 session stopped with reps in hand. The 5k TT is the first all-out effort
since August and the first measured anchor.

### 8.1 5k TT record — Tue 2026-09-15 [S]

**Conditions.** Outdoors in Stockholm, **~15 °C**, TT start 11:51. Resting HR 53, sleep
HRV 61 ms (normal; baseline 56), 8h15 sleep. He reported slightly heavy legs beforehand,
48 h after the 14k long run. Warm-up 1.81 km, cool-down 1.23 km.

**Result.**

| | km 1 | km 2 | km 3 | km 4 | km 5 | 5k |
|---|---|---|---|---|---|---|
| Clock | 4:01 | 4:23 | 4:21 | 4:37 | 4:44 | **22:07** |
| Grade-adjusted (COROS) | 4:06 | 4:19 | 4:22 | 4:31 | 4:39 | **21:57** |
| Avg HR | 180 | 188 | 189 | 191 | 191 | 188 |

- **Shoelace stop:** watch paused for 17 s at 2.35 km, so it is already excluded from
  22:07. Slowing down and restarting cost a few seconds more; not adjusted.
- **Course:** +31 / −32 m. Net flat, but climbs cost more than descents give back —
  COROS grade-adjusted pace puts the terrain at ~10 s.
- **Pacing:** planned 21:41 on 4:13 / 4:28 / 4:19 / 4:28 / 4:13. Km 1 went 12 s fast on
  the descent, and the fade from km 4 is real rather than terrain: grade-adjusted pace
  4:06 → 4:39, power 346 → 304 W, stride 1.44 → 1.22 m. Graded at face value — nothing
  added back for the pacing, the legs or the stop.

**HR.** Average 188, ~190 over the final 15 min. **Peak 193**, reached in km 3 rather
than at the finish; 190–191 across the line and 188 when the watch was stopped. The
planned 20 s stand-still happened but **is not in the file** — the watch was stopped
before it. **Decision: HRmax stays ~200, provisional** (reasoning in the §8 table).

**Conversion.** Decision 2026-09-15: **anchor on the grade-adjusted time.** Sub-T is run
on flat terrain, so the anchor should describe flat running. This corrects the
measurement only; pacing, legs and the stop stay in the result.

| | 5k | VDOT | T-pace | 10k equivalent (Riegel) |
|---|---|---|---|---|
| **Grade-adjusted — use this** | **21:57** | **44.7** | **4:40/km** | **45:46** |
| Raw clock | 22:07 | 44.3 | 4:42/km | 46:07 |

Method **[D]**: Daniels–Gilbert equations.
VO2 = −4.60 + 0.182258·v + 0.000104·v² (v in m/min);
%max = 0.8 + 0.1894393·e^(−0.012778·t) + 0.2989558·e^(−0.1932605·t) (t in min);
VDOT = VO2 / %max. **T-pace = the velocity at 88% of VDOT.** Checked against the
published table: VDOT 50 → T 4:15/km.

**Sub-T bands** — T-pace 4:40 plus the §2 offsets:

| Rep length | Offset | Band | Watch target |
|---|---|---|---|
| 1–3 min | T + 3–5 s/km | **4:43–4:45** | 4:44 ±3 |
| 4–6 min | T + 10–12 s/km | **4:50–4:52** | 4:51 ±3 |
| 8–12 min | T + 17–19 s/km | **4:57–4:59** | 4:58 ±3 |

The watch target widens each band to ±3 s/km, because GPS pace noise is larger than a
2 s band **[C]**.

**Consequences.**
- **Overturns the 09-10 read.** 4:53/km was called "probably at threshold" after the
  8×3. It is 8–10 s slower than the 3-min band that session belonged in. His "could have
  done two more reps" was right.
- **HR side unchanged:** easy ≤140, long ≤150 and the §3 tiers stay provisional on ~200.
- **Every later TT:** same route, grade-adjusted time, so the series compares to itself.

---

## 9. Calibration calendar

| When | Test | Yields |
|---|---|---|
| ~~Tue 2026-09-15~~ **DONE** | All-out **5k TT**, outdoors | **21:57 grade-adjusted (22:07 clock) → VDOT 44.7 → T-pace 4:40.** Peak HR 193; HRmax kept ~200 provisional. Full record in §8.1 |
| **Fri 2026-10-23** (W10) | All-out **5k TT**, outdoors, **same route**, grade-adjusted | Re-anchors T-pace and all §2 bands after W6–W9; another HRmax read. Replaces that week's Friday 4×10 |
| ~~Tue 2026-09-28~~ | ~~30-min TT~~ — **dropped 2026-09-12** | — (LTHR stays unmeasured) |
| **Fri 2026-11-27** (W15) | All-out **5k TT**, outdoors, **same route**, grade-adjusted | Re-anchors T-pace and all §2 bands after W11–W14; another HRmax read. Replaces that week's Friday 4×10 |

**Cadence (2026-09-16):** a 5k TT **every 5th week** — W5/W10/W15, then ~Fri 2027-01-01 — replacing that week's **Friday 4×10**,
the most intensive sub-T session, so a TT week trades a hard session rather than adding
one. No taper; graded at face value; same route every time. **The Dec 6 5k that used to
end the block was dropped** the same day — the schedule replaced it.

With only the 5k, the **pace** side is measured and the **HR** side stays approximate
all block. That is the right way round: pace is the prescription, HR is the rail.
Treat §3 as provisional throughout and let §2 and §4 overrule it on any disagreement.
