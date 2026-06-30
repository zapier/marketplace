# Zapier Marketplace

The single entry point agents use to discover and install Zapier plugins — across [Claude Code](https://code.claude.com/docs/en/plugin-marketplaces), [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-marketplace), and [OpenAI Codex](https://developers.openai.com/codex/plugins).

This repo is a **pointer manifest** — plugins themselves live in their home repos. One central place to add Zapier, one set of source repos for the plugin authors who maintain them.

## Plugins

| Plugin | What it does | Home repo |
| --- | --- | --- |
| `mcp` | The hosted Zapier MCP server — connect any agent to 9,000+ apps | [zapier/zapier-mcp](https://github.com/zapier/zapier-mcp) |
| `zapier-notion` | Independent connector for Notion (search, read, create pages) | [zapier/connectors](https://github.com/zapier/connectors) (`apps/notion`) |
| `gtm-cheat-codes` | Go-to-market skills for marketing, sales, and CS workflows | [zapier/gtm-cheat-codes](https://github.com/zapier/gtm-cheat-codes) |
| `agent-skills` | Zapier-authored skills for Claude Code and compatible agents | [zapier/agent-skills](https://github.com/zapier/agent-skills) |

## Install

### Claude Code

```bash
/plugin marketplace add zapier/marketplace
/plugin install mcp@zapier
/plugin install zapier-notion@zapier
/plugin install gtm-cheat-codes@zapier
/plugin install agent-skills@zapier
```

Browse interactively with `/plugin` → Discover.

### GitHub Copilot CLI

```bash
copilot plugin marketplace add zapier/marketplace
copilot plugin install mcp@zapier
```

### OpenAI Codex

Add `zapier/marketplace` from the Codex plugin marketplace UI, then install the plugins you want.

## Repository layout

```
.claude-plugin/marketplace.json   # Claude Code manifest
.github/plugin/marketplace.json   # GitHub Copilot CLI manifest
.agents/plugins/marketplace.json  # OpenAI Codex manifest
schemas/                          # JSON Schemas + CI validates each manifest against the right one
.github/workflows/                # Syntax, schema, reachability, and cross-manifest consistency checks
```

The three manifests describe the same set of plugins in three different formats. CI enforces that adding a plugin to one without updating the others is a build failure.

## Naming convention

Plugins that wrap a third-party product use `zapier-<product>` (e.g. `zapier-notion`), not the bare product name. This:

- Makes provenance explicit — the connector is built by Zapier, not the upstream vendor
- Avoids claiming a namespace the upstream vendor would own if they ever shipped their own plugin
- Matches the precedent set by other marketplaces (e.g. Anthropic's `42crunch-api-security-testing`, `adobe-for-creativity`)

First-party Zapier products keep short names (`mcp`, `agent-skills`).

## Adding a new plugin

1. Make sure the home repo exposes the manifest the relevant platform expects (`.claude-plugin/plugin.json` for Claude Code; equivalents for Copilot CLI and Codex)
2. Add the plugin entry to **all three** manifests in this repo. CI fails if the set drifts.
3. Open a PR. The validation workflow runs JSON syntax, schema, source-URL reachability, and cross-manifest consistency checks.

See [`schemas/README.md`](./schemas/README.md) for the schema each manifest is validated against.

## Trust

Plugins run in the same environment as the agent that loads them. Only install plugins from publishers you trust. The plugins listed in this marketplace are maintained by Zapier; their source is auditable in the linked home repos.

## License

[MIT](./LICENSE). Individual plugins are licensed by their home repos.
