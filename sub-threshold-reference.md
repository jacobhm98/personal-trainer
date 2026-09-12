# Sub-threshold reference

Knowledge bank for pinpointing, prescribing and verifying sub-threshold work.
Sources: **Marius Bakken, *The Norwegian Method Applied*** (2026) — relayed by the
user 2026-09-11/12 — plus session evidence from this athlete's own data. Jack
Daniels supplies the T-pace anchor only.

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
that feeds the fitness index and the race gates. Corrected 2026-09-12; an earlier
version of this file routed the pace derivation through Riegel unnecessarily.

- Also yields a **near-max HR** at the finish (a 5k finish lands within a few bpm of
  true max), which feeds §3.
- Sanity check on the output: T-pace should land roughly **10k race pace + 6–10 s/km**
  for a runner in the 40–50 min range.

### 1.3 %HRmax zones  *(fallback)*

Use only when neither test above has fresh data. See §3.

### The two TTs are NOT interchangeable

A ~22 min 5k is run **above** threshold, so its average HR sits **4–8 bpm above
LTHR**. Never read a 5k average as threshold HR. The 5k gives **performance +
near-max**; the 30-min gives **LTHR**. Two anchors, two tests, both wanted.

**Decision 2026-09-12: one TT only — the 5k.** The 30-min TT is documented here but
**not scheduled**, and that costs less than an earlier draft of this file claimed. The
5k anchors the **pace** side completely, and pace is the prescription. What is lost is
only LTHR, which would have been a second, redundant route to the same place.

**The resulting hierarchy — use it in this order:**

1. **Prescribe from pace.** VDOT → T-pace → §2 offsets. Measured, from Tue 09-15.
2. **Verify in-session.** §4's three checks. These need **no anchor of any kind** and
   are what tells you the derivation was right.
3. **HR ceilings (§3) are a soft rail, not the prescription.** They run as %-of-max off
   a max that is approximate — the 5k finish reading is a *floor*, since wrist optical
   under-reads peaks by 5–15 bpm. **If §3 disagrees with 1 and 2, §3 loses.**

Rationale for choosing the 5k over the 30-min: the block endpoint (2026-12-06) is a 5k,
so a 5k baseline makes that result directly interpretable.

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

| Tier | % HRmax |
|---|---|
| 1–3 min  | 85–87% |
| 4–6 min  | 83–85% |
| 8–12 min | 80–83% |

Read as **end-of-rep values** — HR lags, especially on short reps.

**Full intensity map:** easy **≤70%**, long run **≤75%**, sub-T **80–87%**, Daniels
threshold **88–92%**. Nothing should live between the long-run cap and the sub-T
floor — that gap is the polarisation.

**Cross-check between §1.1 and §3:** if LTHR ≈ 88–90% of max, then the golden zone
(LTHR − 4–7) ≈ **84–87%** — i.e. the **1–3 min tier**. So the golden zone is the
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

**Scale by session duration.** 7–10 is quoted for a 6×6, which runs ~42 min with
floats. A 3×10 is only ~33 min → expect **5–8**.

**Recovery length is a lever, not just pace.** If a session ratchets *but the reps
still plateau internally*, the mechanism is accumulation from short floats rather
than reps in the severe domain. Lengthen the float before slowing the pace — it
preserves more of the stimulus.

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

Weekly sub-T dose in the current block runs **60 → 76 min**.

---

## 8. Current state (update as tests land)

| Quantity | Value | Status |
|---|---|---|
| HRmax | 200 | **ASSUMED.** Observed floor 195 (2026-08-20, altitude, recovery jog). 186 reached on a non-maximal session 2026-09-10, so the true figure is likely 200–205. |
| LTHR | — | **NOT MEASURED, and will not be** — one TT only. Golden-zone method unavailable. |
| T-pace | — | **NOT MEASURED.** Derives from the 5k TT, Tue 2026-09-15. |
| 10k shape | 47:00 | **ASSUMED**, user's own estimate 2026-08-18 off a race paced blind. Strava predicts 44:00; the 09-02 tempo implies ~47–48. Four minutes of disagreement, nothing measured. |
| Easy cap | ≤140 bpm | Provisional on max 200 |
| Long-run cap | ≤150 bpm | Provisional on max 200 |
| Sub-T ceilings | 170–174 / 166–170 / 160–166 | Provisional on max 200 |

**Every running data point in this block is a floor, not a measure** —
Midnattsloppet was paced blind, the 09-02 tempo was run to a prescription, the 09-10
session stopped with reps in hand. Nothing has been run to failure since August.

---

## 9. Calibration calendar

| When | Test | Yields |
|---|---|---|
| **Tue 2026-09-15** | All-out **5k TT**, outdoors | Performance → T-pace → §2 bands; near-max HR → §3 |
| ~~Tue 2026-09-28~~ | ~~30-min TT~~ — **dropped 2026-09-12, one TT only** | — (LTHR stays unmeasured) |
| **Sun 2026-12-06** | All-out **5k**, block endpoint | Re-anchors everything; comparable to 09-15 |

With only the 5k, the **pace** side is measured and the **HR** side stays approximate
all block. That is the right way round: pace is the prescription, HR is the rail.
Treat §3 as provisional throughout and let §2 and §4 overrule it on any disagreement.
