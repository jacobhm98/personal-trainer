# Fitness metric — spec

_Draft v0.1, 2026-09-01. Defines the single number used to judge "as fit as possible by
30." Everything here is a decision already taken in discussion unless marked **open**._

## 1. What it measures

One score, the **impressiveness** of a two-domain performance:

- **Cardiovascular**: 10k running time (absolute speed).
- **Strength**: squat, deadlift, weighted dips, weighted pull-ups (absolute load).
- **Equal weighting** between the two domains.
- **Reference population: men aged 25–34, general population** — not race finishers,
  not lifters. Both domains are expressed as "how rare is this among men my age."
- **Output**: the rarity of the equal-weight composite, reported as `1 in N` (with the
  underlying z), plus the two domain z's so the balance is visible.

Horizon: the 30th birthday, ~March 2028 (**open**: exact date). Baseline: the
**2026-11-01 checkpoint** (§7; moved from 2026-10-11 on 2026-09-03 when the TT was
pushed back — gate Oct 18, fallback 2026-11-08).

## 2. Design decisions

| # | Decision | Why |
|---|---|---|
| 1 | **Absolute, not bodyweight-relative.** No BW term anywhere in the formula. | The goal is what the body can do, not what it can do per kg. Running already carries bodyweight; strength is scored in kg lifted. A cut is credited only through the seconds it removes from the 10k and charged for any absolute strength it costs. |
| 2 | **Population-referenced, not self-referenced.** | A percentile answers "how fit" in a way a ratio-to-baseline cannot. The self-relative index is kept only as a fallback (Appendix A). |
| 3 | **Single base population for both domains.** | Race-finisher and lifter datasets are selected with very different intensity (median powerlifting competitor ≈ 99.8th pct of men on deadlift; median 10k finisher ≈ 85–90th of men). Comparing z's across differently-selected references undervalues strength by ~1.5–2 sd and distorts the slope. Everything is chained to men 25–34 (§5 step 2). |
| 4 | **Combine in z-space, not raw percentiles.** | Raw percentiles saturate in the tail: 45:00 → 40:00 is ~12 percentile points, 60:00 → 52:00 is ~30. Averaging percentiles would say gains in a strong domain are worthless once it passes ~95. z is linear in population-sd. |
| 5 | **Equal weights = equal z contribution.** | Exchange rate between domains is `σ_run : σ_str` in the base population — 0.1 sd of running = 0.1 sd of strength. A convention, but one about how spread the world is rather than an arbitrary "1% = 1%". |
| 6 | **Lifts collapsed to one strength construct before combining.** | Squat/deadlift/dips/pull-ups correlate ~0.8; four lift z's are ~one piece of evidence, not four. Collapsing removes the need to model intra-lift correlation in the composite; a variance correction (§5 step 4) keeps the strength z on the same scale as a single variable. |
| 7 | **Report log-odds / `1 in N`, not percentile.** | Where this is going (97–99.x), percentiles hide the movement in decimals. Log-odds stay linear in z in the tail. Also: chaining errors (wrong participation rate) become an additive shift in log-odds, so the *trend* is insulated from the *level's* uncertainty. |
| 8 | **Dips and pull-ups scored as total system load (bodyweight + added).** | This is the load the muscles moved; it is a measure of absolute strength, not a normalisation. Scoring added weight only would show a bodyweight drop as a strength gain. |
| 9 | **Composite = rarity of the value-weighted sum, not a dominance or density measure.** | "Nobody beats me at both" silently becomes max-weighting (a 99.9th-pct runner with median strength scores ~1 in 2,000). Density/depth measures can't distinguish rare-because-good from rare-because-bad without reintroducing a value function. Given a value function, the composite is the principled object; the joint distribution's only job is to say how rare a composite value is. |

## 3. Inputs — measurement protocol

### Running: `T` = best 10k-equivalent time in the trailing 16 weeks

- Test: 10k race or flat solo TT. Graded at face value — no solo/altitude/heat discounts.
- Other distances convert with Riegel: `T_10k = T_d × (10 / d_km)^1.06`
  (5k × 2.09; half-marathon ÷ 2.19). Prefer a real 10k.
- Cadence: one result every 8–12 weeks. A result older than 16 weeks is stale and is
  not used.
- Watch estimates (COROS VO2max, race predictor) are **never** inputs.

### Strength: `E1RM` per lift, Epley, from the W3 top set

- The 5s PRO W3 top set (5 reps @ 95% TM) is the built-in test — same relative load,
  same rep target, every cycle. `E1RM = w × (1 + reps / 30)`.
- `w` is total load: bar weight for squat/deadlift; **bodyweight + added** for dips and
  pull-ups (bodyweight from the sheet's `Bodyweight` cell, updated from the weekly
  weigh-in — §3 Context).
- Per lift, take the **best of the last two cycles** so one condition-confounded miss
  (AM session, <48 h after heavy legs) doesn't drag the score.
- A 7th-week TM test (`3–5 @ 100% TM`) replaces the W3 top set for that lift when run.
- Reps are what was actually completed. 4 clean + a failed 5th = 4.

### Context (recorded, not scored)

- Bodyweight: 7-day morning average in each test week. Needed to read whether a cut paid
  for itself; **not** in the formula.
- Session conditions on strength tests: time of day, hours since last leg session, sleep
  score. Explains outliers; never adjusts them.

## 4. Reference data — pin once, freeze for the whole horizon

All tables live under `reference/`, each with: source, URL, retrieval date, exact
bucket used (sex, age band, equipment/raw, bodyweight handling), and any transformation.
**Reference tables are frozen for the 18 months.** If one must change, the whole history
is recomputed against the new table — never mixed.

| Role | Variable | Source (to retrieve — verify each) | Notes |
|---|---|---|---|
| Marginal | 10k time | RunRepeat / IAAF "State of Running" result tables (~108M race results, 1986–2018, by sex × age band); or a national results database | Reference = male race finishers 25–34 |
| Marginal | Squat, deadlift, weighted dip, weighted pull-up | strengthlevel.com standards (self-reported; sex × age × bodyweight) | Reference = male gym-goers who log lifts, 25–34. Use the all-bodyweights distribution (absolute kg), not the per-BW-class one |
| Shape check | Squat, deadlift | OpenPowerlifting (competition-verified, raw, sex/age/BW) | **Not** a reference population (too selected). Used only to sanity-check the tail shape of strengthlevel's squat/DL |
| Anchor | Deadlift | US Army ACFT hex-bar 3RM deadlift (MDL), distributions by sex × age (Army / RAND evaluations) | Young men screened for health, not for strength interest — the closest thing to a general-population strength dataset. Hex-bar 3RM ≈ conventional 1RM, note the conversion used |
| Anchor | Cardiorespiratory fitness | FRIEND registry or Cooper Center norms — VO2max percentiles by sex × age | Convert 10k time → VO2max-equivalent (Daniels VDOT) for the overlay. Note the registry's own selection (clinical / preventive-medicine patients) |
| Correlation `ρ_L` | Lift–lift | OpenPowerlifting: corr(squat, deadlift) among raw male competitors 25–34 | Expect ~0.8. Used for the strength-construct variance correction |
| Correlation `ρ` | Running vs strength | ACFT: corr(2-mile run time, MDL) by sex/age, from published analyses | Expect near zero or slightly negative. If unavailable, use 0 and report the ±0.3 sensitivity |
| Participation `r_run`, `r_str` | Chaining rates | Fitted from the anchors (§6); fallback = national participation statistics (share of men 25–34 with a race result in a year; share who train barbell lifts) | Placeholders until fitted: ~0.08 running, ~0.10 strength |

## 5. Computation

Inputs: `T` (s), `E1RM_squat`, `E1RM_DL`, `E1RM_dips`, `E1RM_pullups` (kg).
`Φ` = standard normal CDF, `Φ⁻¹` its inverse.

```
1. Marginal percentile within its reference, male 25–34
      p_ref,run   = P(finisher time > T)                   faster = higher
      p_ref,lift  = P(logged E1RM < E1RM_lift)             one per lift

2. Chain to the general population of men 25–34
      p_gen = (1 − r) + r · p_ref                          r = participation rate for that domain
      (assumes non-participants would rank below you — an upper bound; §6 fits r so the
       anchor absorbs the error)

3. z per variable
      z_run   = Φ⁻¹(p_gen,run)
      z_lift  = Φ⁻¹(p_gen,lift)                            four of these

4. Collapse lifts to one strength z (variance-corrected mean)
      z_str = mean(z_squat, z_DL, z_dips, z_pullups) / sqrt( (1 + 3·ρ_L) / 4 )
      (with ρ_L = 0.8 the divisor is 0.92)

5. Equal-weight composite
      z̄ = (z_run + z_str) / 2

6. Rarity of the composite in the population
      Z = z̄ / sqrt( (1 + ρ) / 2 )                          ρ = corr(run, strength); ρ = 0 → divisor 0.707
      p = Φ(Z)
      N = 1 / (1 − p)                                       report "1 in N"
      L = ln( p / (1 − p) )                                 log-odds, the tracking series
```

Report every checkpoint as: `T`, four E1RMs, `z_run`, `z_str`, `z̄`, `Z`, `p`, `1 in N`,
`L`, bodyweight (context).

Sensitivity (state in every report):
- `ρ ∈ [−0.3, +0.3]` moves `p` by only ~0.3 percentile points at current levels but
  moves `N` by a factor of ~6 either way (§8) — `ρ` is the largest single lever on the
  *level*. Negative `ρ` makes the combination rarer. Pin it from data, and report `N`
  at ρ = 0 with the ±0.3 bracket until then.
- A factor-of-2 error in `r` shifts `L` by ≈ `ln 2 ≈ 0.7` — an offset, not a slope.
  Treat `N` as order-of-magnitude until §6 is done; treat changes in `L` as real.

## 6. Fitting the participation rates from anchors

The chaining step is where the "strength references are more selected than running
references" problem is solved, so `r` should be fitted, not guessed.

**Strength.** Overlay the strengthlevel deadlift distribution (male 25–34, all
bodyweights) on the ACFT MDL distribution (male 25–34). Choose `r_str` so that
`(1 − r_str) + r_str · F_sl(x)` matches `F_acft(x)` at 3–4 quantiles (e.g. the ACFT
50th/75th/90th/95th). Record the residuals. Apply the same `r_str` to squat, dips and
pull-ups. If the fitted `r_str` is far from the naive gym-participation rate, that gap is
the size of the "strong men who never log a lift" population — record it, don't hide it.

**Running.** Convert the race-finisher time distribution to VO2max-equivalents (Daniels)
and overlay on the CRF registry's male 25–34 percentiles; fit `r_run` the same way. Note
the registry's own selection in the residuals.

Both anchors are imperfect general-population proxies. The point is that they include the
people who would never enter a race or log a lift, which the marginal references cannot.

## 7. Baseline, cadence, logging

- **Baseline = 2026-11-01 checkpoint** (moved 2026-09-03, TT pushed back; fallback
  2026-11-08 if the Oct 18 gate misses): the flat 10k solo TT that day, plus the W3
  top sets of cycle C15 ending 2026-10-25 (best of the last two cycles per lift).
  Both domains measured within a week of each other.
- **Strength** updates every cycle (W3 week, every 3 weeks; 7th-week protocol weeks
  carry no strength update unless a TM test is run).
- **Running** updates on every race/TT, targeted every 8–12 weeks.
- The score is recomputed whenever either domain updates. One row per checkpoint in
  `state/fitness-index.md`:

  `| date | T | squat | DL | dips | pull-ups | z_run | z_str | Z | 1 in N | L | BW | notes |`

- The computation is a script (`scripts/fitness_index.py`, **open**) that takes a
  checkpoint row and the frozen tables and emits the report line — no hand arithmetic.

## 8. Illustrative numbers — not results

Marginals from memory of the tables, rates as placeholders. Replace once §4/§6 are done.

| | Within reference | r | Chained (men 25–34) | z |
|---|---|---|---|---|
| 10k ≈ 45:00 | ~85th of finishers | 0.08 | ~98.8th | ~2.25 |
| Strength ≈ 625 kg total (~80th on each lift) | ~80th of loggers | 0.10 | ~98th | ~2.05 per lift → **2.23** after the §5 step-4 correction |

Composite (ρ = 0): `z̄ ≈ 2.24`, `Z ≈ 3.17`, `p ≈ 0.9992` → **~1 in 1,300** today
(ρ = −0.3 → ~1 in 13,000; ρ = +0.3 → ~1 in 370; both `r` doubled → ~1 in 330).

Birthday targets — 10k **40:00** and total **~680 kg** (squat ~190, DL ~220, dips ~145
total, pull-ups ~128 total), taken as ~97th of finishers and ~90th of loggers per lift:
`z_run ≈ 2.8`, `z_str ≈ 2.5`, `Z ≈ 3.8` → **~1 in 13,000**.

Today's provisional strength inputs: squat 4 @ 156.04 → 176.8; deadlift 4 @ 182.64 (last
cycle) → 207.0; dips 5 @ 109.25 total → 127.5 if 5 reps (**open**); pull-ups 5 @ 97.38
total → 113.6 if 5 reps (Thu).

## 9. Open items

1. Birthday date (sets the horizon).
2. Dips W3 top-set reps, 2026-08-31 (lap ran 49.8 s vs ~19 s for the earlier sets — the
   watch counted 4, its rep counter is unreliable).
3. Weekly weigh-ins from now on (context column; also feeds the dips/pull-up totals).
4. Retrieve and freeze the reference tables (§4); fit `r_run`, `r_str` (§6); pick `ρ`,
   `ρ_L`.
5. Write `scripts/fitness_index.py` and seed `state/fitness-index.md`.
6. Decide whether the self-relative index (Appendix A) is logged alongside as a check.

## Appendix A — self-relative fallback

If the reference tables can't be built to an acceptable standard, the fallback is the
ratio index: `C = 10000 / T` (m/s), `S = Σ E1RM` (kg), `FI = 100 · sqrt((C/C₀)(S/S₀))`
with the 2026-11-01 checkpoint as `C₀, S₀`. Equal-weighted average of log-changes;
+2% in either domain = +1 point; no external data; no standing information.

## Appendix B — worked arithmetic (check the script against this)

Inputs: `p_ref,run = 0.85`, `r_run = 0.08`; four lifts at `p_ref = 0.80`, `r_str = 0.10`;
`ρ_L = 0.8`, `ρ = 0`.

```
p_gen,run  = 0.92 + 0.08·0.85 = 0.988      z_run  = Φ⁻¹(0.988) = 2.26
p_gen,lift = 0.90 + 0.10·0.80 = 0.980      z_lift = Φ⁻¹(0.980) = 2.05  (×4)
z_str = 2.05 / sqrt((1 + 3·0.8)/4) = 2.05 / 0.922 = 2.23
z̄    = (2.26 + 2.23) / 2 = 2.24
Z     = 2.24 / 0.707 = 3.17
p     = Φ(3.17) = 0.99924      N = 1 / 0.00076 ≈ 1,300      L = ln(0.99924/0.00076) = 7.18
```
