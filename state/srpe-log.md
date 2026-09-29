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

| Date | Session | Region | Duration (min) | RPE | sRPE (AU) | Notes |
|---|---|---|---|---|---|---|
| 2026-09-23 | 531 C14 W2 D2 Dips (bench substituted — no dip bars) | upper | 34.3 | — | — | 14 sets, avg HR 97. Found gym, Kigali. **CLOSED, no RPE — do not re-ask** |
| 2026-09-24 | 531 C14 W2 D1 Squat 5/5/5 @ 115/131.4/147.8 + FSL 3x5 | **legs** | 38.3 | — | — | 13 sets, avg HR 101 (max 140). Stacked after the AM 5x6 sub-T. **COROS scored this ~10 AU against the run's ~133.** **CLOSED, no RPE — do not re-ask** |
| 2026-09-29 | 531 C14 W2 D3 Deadlift 5/5/5 @ 134.6/153.8/173.0 + FSL 3x5 | **legs** | | | | Stacked after the AM 6x6 @ 12.0 kph. **First live row** |

**Back-filling was declined 2026-09-29** ("its chill man, ill do it going forwards"), so the
two rows above stay blank permanently. **The log starts from 2026-09-29.** Do not ask for a
retrospective RPE on anything older than that date.
