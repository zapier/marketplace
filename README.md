# Zapier Marketplace

Zapier's plugin marketplace for coding agents. One command to add, then install any of:

| Plugin | Type | What it does |
| --- | --- | --- |
| `agent-skills` | Skills | Zapier-authored agentskills.io skills for compatible clients |
| `algolia` | MCP + skill | Algolia search — index, search, and tune records and settings |
| `alpaca` | MCP + skill | Alpaca brokerage — trade stocks, crypto, and options |
| `clay` | MCP + skill | Clay tables — create, update, and find rows |
| `dataforseo` | MCP + skill | SEO and AI-search data — SERPs, keywords, and backlinks |
| `discord` | MCP + skill | Discord messages, threads, channels, and roles |
| `dropbox` | MCP + skill | Dropbox files and folders — upload, share, search, and organize |
| `elevenlabs` | MCP + skill | AI audio — text to speech, transcription, and voice design |
| `google-ads` | MCP + skill | Google Ads campaigns, budgets, and reporting |
| `google-analytics` | MCP + skill | GA4 reports, properties, and events |
| `google-calendar` | MCP + skill | Events, calendars, and free/busy availability |
| `google-contacts` | MCP + skill | Contacts and contact groups (labels) |
| `google-docs` | MCP + skill | Create, read, and edit Google Docs |
| `google-sheets` | MCP + skill | Read and write Google Sheets data, formatting, and structure |
| `google-tasks` | MCP + skill | Task lists and to-dos in Google Tasks |
| `gtm-cheat-codes` | Skills | Marketing / sales / CS workflow recipes |
| `heygen` | MCP + skill | AI avatar videos, translation, and voice cloning |
| `mcp` | MCP server | Hosted Zapier MCP — connect any agent to 9,000+ apps |
| `microsoft-outlook` | MCP + skill | Outlook mail, calendar, and contacts |
| `microsoft-sharepoint` | MCP + skill | SharePoint sites, files, lists, and pages |
| `microsoft-todo` | MCP + skill | Tasks and task lists in Microsoft To Do |
| `notion` | MCP + skill | Independent Notion connector — search, read, and write pages |
| `resend` | MCP + skill | Transactional email, broadcasts, and contacts |
| `runway` | MCP + skill | Generate and edit AI images, video, and audio |
| `sdk` | SDK | TypeScript helpers for building against Zapier |
| `telegram` | MCP + skill | Telegram bot — messages, media, and chats |
| `trello` | MCP + skill | Trello boards, lists, and cards |
| `wade-skills` | Skills | Wade Foster's (Zapier CEO) day-to-day agent skills |
| `youtube` | MCP + skill | YouTube videos, playlists, and comments |

## Install

### Claude Code

**CLI** (from your terminal, without opening a session):

```
# Add the marketplace once
claude plugin marketplace add zapier/marketplace

# Install whichever you want
claude plugin install notion@zapier
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
/plugin install notion@zapier
/plugin install gtm-cheat-codes@zapier
/plugin install mcp@zapier
```

Browse the full list interactively with `/plugin` → Discover.

**Try it out** — once a plugin is installed, ask Claude:

```
# Invoke the Notion plugin
claude "What do our Notion docs say about onboarding new engineers?"

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
