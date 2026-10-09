# Session-RPE log

**The only validated load measure in this system.** Started 2026-09-29 on the user's
instruction: *"in the /training-review make sure to ask me for an RPE on lifting sessions,
that's how i'll log it."*

**sRPE = RPE (0-10) x session duration in minutes.** Populated by `/training-review`, which
asks for an RPE on every lifting session in the period. Duration and set count come from
COROS (`querySportRecords`, `sportTypeCodes: [402]`).

**Why it exists.** HR-derived load prices a heavy squat session at **~8% of a sub-T run**
(measured on 2026-09-24: run ~133 AU, squat ~10 AU) where sRPE prices it near **80%**. The
watch's weekly load is a running-only ledger. Evidence and citations in
`wearable-metrics-reference.md` §4.2.

## STRENGTH RPE IS LOCAL, NOT SYSTEMIC — never sum it with running

**User's correction, 2026-09-29:** *"rpe for strength sessions are localized not systemic in
the same way as running."* He is right, and the first version of this file was wrong to plan
on reporting combined weekly sRPE totals.

An RPE 8 squat session means **quads and hips near failure**. An RPE 8 run means **whole-body
cardiorespiratory and metabolic strain**. They are different constructs and adding them
produces a number that measures nothing.

**Mechanistic support.** Thomas et al. 2018 (*MSSE*, 10x5 back squat @ 80% 1RM): fatigue took
up to 72 h to clear and was **peripheral/contractile, not CNS** — twitch force and voluntary
activation depressed at 48 h while systemic function was intact. Palmer & Sleivert 2001 is the
same story from the other side: lifting cost **2.6% running economy at 1 h with no change in
exercising HR, ventilation or RPE** — a local cost invisible to systemic channels.
The established refinement is **differential RPE** (RPE-breathlessness vs RPE-legs); we use a
lightweight version of it — one number per session, tagged by region.

**So: TWO LEDGERS, NEVER ONE TOTAL.**
- **Local / regional** — the strength sessions below, tagged `legs` (D1 Squat, D3 Deadlift) or
  `upper` (D2 Dips, D4 Pull-ups).
- **Systemic** — running, already covered by the two-more-reps question and the within-rep
  plateau. Not logged here unless he offers a number.

**The axis that actually matters is `legs`.** Squat days, deadlift days and hard running all
draw on it, and that is where concurrent-training interference lives. Report the **legs series
against the running quality days**, not a grand total.

**Rules.**
- **Never invent an RPE**, and never derive one from heart rate. A blank is correct and
  useful; a guess is corruption.
- **Never sum across modalities**, and do not combine these with other subjective items into a
  composite readiness score — consolidation reduces sensitivity (Saw et al. 2016).
- Runs are logged only if he offers one.
- Once ~6-8 strength sessions are logged, report the **legs series** and the **upper series**
  separately, alongside weekly running volume — three numbers, not one.

**First calibration point (2026-09-29).** RPE 6 x 27.2 min = **163 AU legs** for a session COROS would
price in the low tens: avg HR 82, and overnight resting HR flat at 59 across a day that also carried a
6x6 sub-T. The 8%-vs-80% gap documented in `wearable-metrics-reference.md` §4.2 is now visible in this
log's own numbers, not just in the literature.

| Date | Session | Region | Duration (min) | RPE | sRPE (AU) | Notes |
|---|---|---|---|---|---|---|
| 2026-09-23 | 531 C14 W2 D2 Dips (bench substituted — no dip bars) | upper | 34.3 | — | — | 14 sets, avg HR 97. Found gym, Kigali. **CLOSED, no RPE — do not re-ask** |
| 2026-09-24 | 531 C14 W2 D1 Squat 5/5/5 @ 115/131.4/147.8 + FSL 3x5 | **legs** | 38.3 | — | — | 13 sets, avg HR 101 (max 140). Stacked after the AM 5x6 sub-T. **COROS scored this ~10 AU against the run's ~133.** **CLOSED, no RPE — do not re-ask** |
| 2026-09-29 | 531 C14 W2 D3 — **SLDL substituted, no straps**: 5x7-10 @ 70 kg + curls, lateral raises | **legs** | 27.2 | **6** | **163** | 11 sets, avg HR **82** — lowest of the three logged sessions, and overnight RHR did not move (59 -> 59). **Systemically negligible, locally a 6** — exactly the gap this ledger exists to fill. Planned was 5/5/5 @ 134.6/153.8/173.0 + FSL 3x5; no top set attempted, so no TM evidence and no cost (C14 W2 re-runs in running W8). Stacked after the AM 6x6 @ 12.0 kph where he cut rep 6 on leg fatigue. 19:04-19:31 CAT. **User's words:** *"about a 6, i defo feel it in my hammies but i think because im used to dl's its not that bad."* Reported ~14-16 h post-session, i.e. before the 24-48 h DOMS peak. **FIRST LOGGED RPE.** Note the contrast this row establishes: RPE 6 x 27.2 min = **163 AU on the legs axis** from a session every systemic channel (avg HR 82, flat overnight RHR) read as negligible |

| 2026-10-07 | 531 C14 W2 D1 Squat 5/5/5 @ 114.98/131.4/147.83 + FSL 3x5@114.98, Row, Seated DB press | **legs** | 37.7 | **ASKED, awaiting** | — | 19:18-19:55 CEST. **13 sets logged: 6 Legs/Hips + 4 Back + 3 Shoulders** against an expected 12 (3 main + 3 FSL + 3 + 3) — the extra is a *Back* set, i.e. 4 rows not 3, and the exercise categories match D1 exactly, so the set-count cross-check works. Avg HR **108**, max 135 — highest of the four sessions in this log, and still systemically trivial. **8 h 18 min after the AM 6x6** (run ended 11:00, lift started 19:18), inside the >6 h window Doma 2017 favours in this order. **TOP SET HIT — 5 @ 147.83 (90% of TM 164.25), confirmed by the user 2026-10-08:** *"the squats were hit successfully, felt pretty good tbh."* Had to be asked, because the wrist rep counter returned 4, 5, 0, 0, 0, 0 across the six leg sets with a session summary of 9 reps for 6 sets — junk, as expected from accelerometer rep detection. **This is the first clean squat top set since before the altitude block:** the 09-24 Kigali attempt at the same weights has no recorded outcome and would not have counted anyway (found gym, unknown bar/plate calibration — config rules found-gym work out of TM decisions entirely). And it went **run-fatigued**, 8 h 18 min after the AM 6x6. **Not a TM signal.** Under 5s PRO, 90% x 5 feeling "pretty good" is the *designed* sensation, not evidence the TM is under-set — the rule self-calibrates TM to ~92% of true 1RM so that 95% equals a 5RM, and the decision lands on **C14 W3 in running W9**. Do not propose a bump. |
| 2026-10-08 | 531 C14 W2 D2 Dips 5/5/5 @ +2.25/+14.0/+25.75 + FSL 5x5@+2.25, Chin-ups, Abs | upper | 28.25 | **ASKED, awaiting** | — | 19:12-19:40 CEST. **14 sets, exactly as predicted, and the internal split matches D2 perfectly: Chest 8 / Back 3 / Core 3** (= 3 main + 5 FSL dips, 3 chin-ups, 3 abs). **This is the cleanest corroboration yet of the 3-sets-per-movement doctrine** (user, 2026-10-05) *and* of the sheet's explicit `FSL 5x5` row for dips — the set counter has now matched the model on D1 (13 vs 12, one extra row set) and D2 (14 vs 14, exact). Avg HR **103**, max 125. **24 h 54 min after the D1 squat** and ~6 h after the AM 7 km road run. **Rep counter logged 34 across the 8 dip sets against 40 expected (5x8), but it is not evidence** — the same counter read *9 reps for 6 sets* on the 10-07 squat. The first three sets (the main work) each logged 5. **Top set 5 @ +25.75 unverified — asked.** |

**Back-filling was declined 2026-09-29** ("its chill man, ill do it going forwards"), so the
**2026-09-23 and 2026-09-24** rows stay blank permanently (they are the two oldest in the
table, not the two immediately above this line). **The log starts from 2026-09-29.** Do not ask for a
retrospective RPE on anything older than that date.
