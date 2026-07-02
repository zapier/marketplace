# Zapier Marketplace

Zapier's plugins for Claude Code. One `/plugin marketplace add`, then install any of:

| Plugin | Type | What it does |
| --- | --- | --- |
| `mcp` | MCP server | Hosted Zapier MCP — connect any agent to 9,000+ apps |
| `notion` | MCP + skill | Independent Notion connector — search, read, and write pages |
| `gtm-cheat-codes` | Skills | Marketing / sales / CS workflow recipes |
| `agent-skills` | Skills | Zapier-authored skills for Claude Code |
| `sdk` | SDK | TypeScript helpers for building against Zapier |

## Install

```
/plugin marketplace add zapier/marketplace
/plugin install notion@zapier
```

Browse the full list interactively with `/plugin` → Discover.

## Roadmap

GitHub Copilot CLI and OpenAI Codex marketplaces are scaffolded in this repo but intentionally unpopulated — installing on those platforms requires per-plugin manifests (`.codex-plugin/plugin.json`, Copilot equivalent) that most home repos don't yet ship. We'll fill them in once the source repos publish those manifests.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md). The three manifest files (Claude Code + Copilot + Codex) live under `.claude-plugin/`, `.github/plugin/`, and `.agents/plugins/` — the schemas that validate each are in [`schemas/`](./schemas/).

## Trust

Plugins run in the same environment as the agent that loads them. The plugins listed here are Zapier-maintained; their source is auditable in each linked home repo.

## License

[MIT](./LICENSE). Individual plugins carry their own license from their home repos.
