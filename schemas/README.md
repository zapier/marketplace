# schemas/

JSON Schema files used by CI to validate the marketplace manifests in this repo.

> **These schemas are self-authored, not officially published.** No platform vendor currently publishes a canonical JSON Schema for their plugin marketplace format. Anthropic's canonical `marketplace.json` references `https://anthropic.com/claude-code/marketplace.schema.json`, but that URL returns 404. The schemas here are derived from canonical reference marketplaces published by each vendor and from their public docs.

| Schema | Validates | Derived from |
|---|---|---|
| [`claude-code.schema.json`](./claude-code.schema.json) | [`../.claude-plugin/marketplace.json`](../.claude-plugin/marketplace.json) | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official/blob/main/.claude-plugin/marketplace.json) + [Claude Code plugin marketplace docs](https://code.claude.com/docs/en/plugin-marketplaces) |
| [`copilot-cli.schema.json`](./copilot-cli.schema.json) | [`../.github/plugin/marketplace.json`](../.github/plugin/marketplace.json) | [github/copilot-plugins](https://github.com/github/copilot-plugins/blob/main/.github/plugin/marketplace.json) + [github/awesome-copilot](https://github.com/github/awesome-copilot/blob/main/.github/plugin/marketplace.json) + [GitHub Copilot CLI plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference) |
| [`codex.schema.json`](./codex.schema.json) | [`../.agents/plugins/marketplace.json`](../.agents/plugins/marketplace.json) | [openai/plugins](https://github.com/openai/plugins/blob/main/.agents/plugins/marketplace.json) + [Codex plugin build docs](https://developers.openai.com/codex/plugins/build) |

## How to update a schema

When a vendor publishes an official schema, or when our derived schema misses a field a real-world example uses, update the relevant file here and bump the `description` to note the source.

## How CI uses these

See [`../.github/workflows/validate-marketplace.yml`](../.github/workflows/validate-marketplace.yml). Each PR runs:

1. JSON syntax check on every `marketplace.json`
2. JSON Schema validation against the matching schema in this directory
3. Reachability check on the `git-subdir` source URLs
4. Cross-manifest consistency: same plugin name and same source target across all three files
