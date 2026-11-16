---
name: sync-strength
description: RETIRED 2026-11-08 — strength is no longer pushed to any calendar. Kept as a stub so the name does not silently resolve to nothing.
argument-hint: "(retired)"
disable-model-invocation: true
---

# RETIRED 2026-11-08 — DO NOT PUSH STRENGTH ANYWHERE

His call: *"ok, its fine i think lets just drop the strength from the watch. ill still
record them manually."*

**Two independent reasons, both verified:**

1. **The COROS MCP cannot author strength workouts.** `sportType` accepts 1 running,
   2 cycling, 5 trail running (4 = rest, training plans only). Every create tool carries
   a `strengthBodypart` field documented *"Strength training is not supported; must stay
   null."* The only route to a strength entry is `scheduleWorkout` on a workout that
   already exists in the COROS workout library — and the library is empty, so it would
   have to be authored in the COROS app by hand.
2. **The entry was never worth much.** Relayed strength opened on the watch as a
   content-free shell — ~4 generic sections, no reps or loads, taps through in ~5 min
   (verified 2026-08-19). The standing protocol already said not to start it and to
   record a plain Strength activity instead, so the calendar entry was doing nothing the
   sheet and the week block do not already do.

**What happens now.** The Google Sheet stays the source of truth for weights (hard rules
1 and 2 unchanged — read the cells, never recompute, never write unless told). The
lifting days and session names go into the week block in `plans/running.md` so the week
reads correctly. He records the session himself. `/training-review` still asks for an RPE
per lifting session and still logs it to `state/srpe-log.md` — **that is now the only
record of lifting load, so it matters more, not less.**

Use `/sync-week` for running.
