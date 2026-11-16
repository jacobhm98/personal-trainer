# personal-trainer

Claude Code-driven training pipeline for a COROS watch. The running plan is written
**directly to the COROS training calendar** through the official COROS MCP — no
reverse-engineered APIs, no credentials in files.

> **Changed 2026-11-08.** This used to go through [Tredict](https://www.tredict.com)
> as a relay. The COROS MCP gained direct calendar writes, so the relay — and with it
> a duplication bug and a vanishing-entry failure, both documented in `CLAUDE.md` — is
> out of the write path. Tredict remains connected for reads only.

- **Strength**: modified 5/3/1 (squat, deadlift, dips, pull-ups) in a Google Sheet —
  the source of truth, read-only to this project.
- **Running**: `plans/running.md`, distilled from `running-training-brief.md`.
- **Push**: the `/sync-week` skill writes each run straight onto a COROS calendar
  date with `createScheduledWorkout`. One call per session, no apply step, no relay
  window — COROS accepts today through +90 days. Structured runs reach the watch with
  per-step pace and HR targets, and the push reads back verifiably.
- **Strength is not pushed anywhere** (decided 2026-11-08). The COROS MCP cannot
  author strength workouts, and the old relayed entry was a content-free shell. The
  sheet and the week block carry the sessions; the actual lifting is recorded by hand
  as a plain Strength activity.
- **Review**: `/training-review` compares plan vs execution using the official
  COROS MCP + Strava.

## One-time setup

1. `claude` in this repo → approve the project MCP server (`coros-official`,
   in `.mcp.json`) → `/mcp` → complete its OAuth login. **This is the only server
   the push path needs.**
2. *(Optional, reads only.)* Tredict uses a **personal API token**, not OAuth (its
   OAuth callback fails in Claude Code as of Aug 2026). Create a token in Tredict →
   Settings → Personal API / MCP, save it as `TREDICT_TOKEN=...` in `.env`
   (gitignored), then register the server at local scope (per-machine, never
   committed):

   ```
   source .env
   claude mcp add --transport http -s local tredict \
     https://www.tredict.com/api/mcp/v2/ -H "Authorization: Bearer $TREDICT_TOKEN"
   ```

3. Smoke test: `claude mcp list` should show `coros-official` ✔ Connected.

Conventions and hard rules live in `CLAUDE.md`; training config in
`plans/config.md`; push history in `state/sync-log.md`.
