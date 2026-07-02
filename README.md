# Zapier Marketplace

Zapier's plugin marketplace for coding agents. One command to add, then install any of:

| Plugin | Type | What it does |
| --- | --- | --- |
| `mcp` | MCP server | Hosted Zapier MCP — connect any agent to 9,000+ apps |
| `notion` | MCP + skill | Independent Notion connector — search, read, and write pages |
| `gtm-cheat-codes` | Skills | Marketing / sales / CS workflow recipes |
| `agent-skills` | Skills | Zapier-authored agentskills.io skills for compatible clients |
| `sdk` | SDK | TypeScript helpers for building against Zapier |

## Install

### Claude Code

**In-session** (slash commands inside an active Claude Code session):

```
/plugin marketplace add zapier/marketplace
/plugin install notion@zapier
```

Browse the full list interactively with `/plugin` → Discover.

**CLI** (from your terminal, without opening a session):

```
claude plugin marketplace add zapier/marketplace
claude plugin install notion@zapier
claude plugin list
```

**Invoke the Notion plugin** (example — same pattern works for any installed plugin):

```
claude "What do our Notion docs say about onboarding new engineers?"
```

### GitHub Copilot CLI

Coming soon.

### OpenAI Codex

Coming soon.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md). The three manifest files (Claude Code + Copilot + Codex) live under `.claude-plugin/`, `.github/plugin/`, and `.agents/plugins/` — the schemas that validate each are in [`schemas/`](./schemas/).

## Trust

Plugins run in the same environment as the agent that loads them. The plugins listed here are Zapier-maintained; their source is auditable in each linked home repo.

## License

[MIT](./LICENSE). Individual plugins carry their own license from their home repos.
