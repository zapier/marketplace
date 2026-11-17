# Zapier Marketplace

Zapier's plugin marketplace for coding agents. One command to add, then install any of:

| Plugin | Type | What it does |
| --- | --- | --- |
| `agent-skills` | Skills | Zapier-authored agentskills.io skills for compatible clients |
| `gtm-cheat-codes` | Skills | Marketing / sales / CS workflow recipes |
| `mcp` | MCP server | Hosted Zapier MCP — connect any agent to 9,000+ apps |
| `sdk` | SDK | TypeScript helpers for building against Zapier |
| `wade-skills` | Skills | Wade Foster's (Zapier CEO) day-to-day agent skills |

## Install

### Claude Code

**CLI** (from your terminal, without opening a session):

```
# Add the marketplace once
claude plugin marketplace add zapier/marketplace

# Install whichever you want
claude plugin install sdk@zapier
claude plugin install gtm-cheat-codes@zapier
claude plugin install mcp@zapier

# See what you've got
claude plugin list
```

**In-session** (slash commands inside an active Claude Code session):

```
# Add the marketplace once
/plugin marketplace add zapier/marketplace

# Install whichever you want
/plugin install sdk@zapier
/plugin install gtm-cheat-codes@zapier
/plugin install mcp@zapier
```

Browse the full list interactively with `/plugin` → Discover.

**Try it out** — once a plugin is installed, ask Claude:

```
# Invoke a GTM cheat code
claude "Draft a cold outreach email for our new pricing tier"
```

**Docs:** [Discover and install plugins](https://code.claude.com/docs/en/discover-plugins.md) · [Plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces.md)

### GitHub Copilot CLI

```
copilot plugin marketplace add zapier/marketplace
copilot plugin install mcp@zapier
copilot plugin install sdk@zapier
copilot plugin install wade-skills@zapier
```

`mcp` (Zapier MCP), `sdk`, and `wade-skills` are currently installable via Copilot CLI. Other plugins will be added as their home repos ship `.github/plugin/plugin.json`.

**Docs:** [Finding and installing plugins](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing)

### OpenAI Codex

```
codex plugin marketplace add zapier/marketplace
codex plugin add zapier@zapier
codex plugin add sdk@zapier
codex plugin add wade-skills@zapier
```

Or open the in-CLI picker with `/plugins` and toggle plugins on.

`zapier` (Zapier MCP), `sdk`, and `wade-skills` are currently installable via Codex. Other plugins will be added as their home repos ship `.codex-plugin/plugin.json`.

**Docs:** [Building plugins](https://developers.openai.com/codex/plugins/build) · [CLI slash commands](https://developers.openai.com/codex/cli/slash-commands)

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md). The three manifest files (Claude Code + Copilot + Codex) live under `.claude-plugin/`, `.github/plugin/`, and `.agents/plugins/` — the schemas that validate each are in [`schemas/`](./schemas/).

## Trust

Plugins run in the same environment as the agent that loads them. The plugins listed here are Zapier-maintained; their source is auditable in each linked home repo.

## License

[MIT](./LICENSE). Individual plugins carry their own license from their home repos.
