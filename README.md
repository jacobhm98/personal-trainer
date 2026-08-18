# personal-trainer

Claude Code-driven training pipeline for a COROS watch. Running and strength plans
are synced to the COROS training calendar through [Tredict](https://www.tredict.com)
(official COROS Training API partner) — no reverse-engineered APIs, no credentials
in files.

- **Strength**: modified 5/3/1 (squat, deadlift, dips, pull-ups) in a Google Sheet —
  the source of truth, read-only to this project.
- **Running**: `plans/running.md`, distilled from `running-training-brief.md`.
- **Push**: `/sync-running` and `/sync-strength` skills create workouts via the
  Tredict MCP; Tredict relays the coming 7 days to COROS (~3 h cadence). Structured
  runs reach the watch with pace targets; strength sessions relay to the COROS
  calendar too (verified Aug 2026).
- **Review**: `/training-review` compares plan vs execution using the official
  COROS MCP + Strava.

## One-time setup

1. Create a Tredict account (2-month full trial; write access is $49/12 months
   after that) → Settings → Services: connect COROS and enable
   "Synchronisation of scheduled trainings with Coros".
2. `claude` in this repo → approve the project MCP server (`coros-official`,
   in `.mcp.json`) → `/mcp` → complete its OAuth login.
3. Tredict uses a **personal API token**, not OAuth (its OAuth callback fails in
   Claude Code as of Aug 2026). Create a token in Tredict → Settings →
   Personal API / MCP, save it as `TREDICT_TOKEN=...` in `.env` (gitignored),
   then register the server at local scope (per-machine, never committed):

   ```
   source .env
   claude mcp add --transport http -s local tredict \
     https://www.tredict.com/api/mcp/v2/ -H "Authorization: Bearer $TREDICT_TOKEN"
   ```

4. Smoke test: `claude mcp list` should show both servers ✔ Connected.

Conventions and hard rules live in `CLAUDE.md`; training config in
`plans/config.md`; push history in `state/sync-log.md`.
