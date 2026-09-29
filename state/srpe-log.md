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

**Rules.**
- **Never invent an RPE**, and never derive one from heart rate. A blank is correct and
  useful; a guess is corruption.
- Runs are logged only if he offers one — the two-more-reps question and the within-rep
  plateau already do that job.
- **Do not sum these with other subjective items into a composite readiness score.**
  Consolidating subjective measures reduces sensitivity (Saw et al. 2016).
- Once ~6-8 sessions are logged, report **weekly sRPE totals** as the load picture.

| Date | Session | Duration (min) | RPE | sRPE (AU) | Notes |
|---|---|---|---|---|---|
| 2026-09-23 | 531 C14 W2 D2 Dips (bench substituted — no dip bars) | 34.3 | — | — | 14 sets, avg HR 97. Found gym, Kigali. **CLOSED, no RPE — do not re-ask** |
| 2026-09-24 | 531 C14 W2 D1 Squat 5/5/5 @ 115/131.4/147.8 + FSL 3x5 | 38.3 | — | — | 13 sets, avg HR 101 (max 140). Stacked after the AM 5x6 sub-T. **COROS scored this ~10 AU against the run's ~133.** **CLOSED, no RPE — do not re-ask** |
| 2026-09-29 | 531 C14 W2 D3 Deadlift 5/5/5 @ 134.6/153.8/173.0 + FSL 3x5 | | | | Stacked after the AM 6x6 @ 12.0 kph. **First live row** |

**Back-filling was declined 2026-09-29** ("its chill man, ill do it going forwards"), so the
two rows above stay blank permanently. **The log starts from 2026-09-29.** Do not ask for a
retrospective RPE on anything older than that date.
