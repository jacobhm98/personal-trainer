---
name: sync-running
description: Superseded 2026-11-08 by /sync-week, which is now running-only and writes directly to COROS. Use /sync-week.
argument-hint: "(use /sync-week)"
disable-model-invocation: true
---

# Superseded 2026-11-08 — use `/sync-week`

This skill existed to push running separately from strength. With **strength no longer
pushed to any calendar** (his call 2026-11-08), `/sync-week` *is* the running push, so
keeping two skills for one job only creates a chance of using the stale one.

`/sync-week` writes each run straight onto a COROS date with `createScheduledWorkout` —
no Tredict, no relay, no apply step. The course schema, the no-delete rule and the
no-per-step-notes limitation are in `CLAUDE.md` → **COROS MCP notes**.

**Everything this file used to say about `plan-creation`, `targetMode: "padding"`,
`targetZoneType` and applying a plan in the Tredict UI describes the OLD write path and
must not be used for a new push.** It is preserved in git history and summarised under
**Tredict MCP notes — LEGACY** in `CLAUDE.md`.
