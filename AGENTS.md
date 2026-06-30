# AGENTS.md

Canonical guide for AI agents (and humans) working in `zapier/marketplace`. `CLAUDE.md` is a one-line shim that points here.

## Repository purpose

This repo is the central pointer manifest that lets agents discover Zapier plugins across Claude Code, GitHub Copilot CLI, and OpenAI Codex. It does **not** host plugin source — every plugin lives in its own home repo. This repo only maintains the marketplace entries that point at those repos.

## Hard invariant: keep the three manifests in lockstep

There are three manifest files, one per platform:

- [`.claude-plugin/marketplace.json`](./.claude-plugin/marketplace.json) — Claude Code
- [`.github/plugin/marketplace.json`](./.github/plugin/marketplace.json) — GitHub Copilot CLI
- [`.agents/plugins/marketplace.json`](./.agents/plugins/marketplace.json) — OpenAI Codex

For every plugin, all three manifests must:

1. List the same plugin name
2. Resolve to the same source target (same repo, same `path`, same `ref`)

CI fails if these drift. The consistency check lives at [`.github/scripts/check_consistency.py`](./.github/scripts/check_consistency.py).

When adding, removing, or moving a plugin, **edit all three files in the same PR**. There is no "Claude-only" or "Codex-only" plugin in this repo.

## Naming rules

- First-party Zapier products use short names: `mcp`, `agent-skills`, `gtm-cheat-codes`
- Connectors that wrap a third-party product use `zapier-<product>`: `zapier-notion`, not `notion`. This makes provenance explicit and avoids claiming a namespace the upstream vendor would own
- Plugin names are lowercase, kebab-case, and stable — renaming a plugin is a breaking change for every user who has it installed

## Schemas and validation

Each manifest is validated against a JSON Schema in [`schemas/`](./schemas/). The schemas are self-authored (no platform vendor publishes a canonical schema yet) and derived from each vendor's official marketplace + docs — see [`schemas/README.md`](./schemas/README.md) for provenance. When a vendor adds a field a real-world marketplace uses, update the relevant schema and bump its `description` to note the new source.

## Sources, refs, and pinning

Plugin sources currently pin to `"ref": "main"`. That means every installer pulls the latest commit on the source repo's default branch. Pinning to a specific commit SHA is the safer pattern (auditable, reproducible) — switching to SHA-pinning + an automated bump workflow is on the roadmap, not yet wired up. When adding a new plugin, follow the existing `main` convention unless a PR explicitly changes the convention repo-wide.

## How to add a plugin

1. Confirm the home repo exposes the right per-platform manifest at the right path (`.claude-plugin/plugin.json` for Claude Code, equivalents for Copilot CLI and Codex)
2. Add one entry per plugin to **all three** marketplace manifests in this repo
3. Open a PR. The `Validate marketplace manifests` workflow runs:
   - JSON syntax check
   - Schema validation against the matching file in `schemas/`
   - Source-URL reachability (the source repo must 200)
   - Cross-manifest consistency

If CI passes and the PR is reviewed, merging makes the plugin installable everywhere at once.

## What does **not** belong in this repo

- Plugin source — it lives in the plugin's home repo
- Plugin documentation longer than the entry in the manifest — link to the home repo's README
- Platform-specific manifests for plugins that aren't on this marketplace — that's the home repo's job

## Trust model

Plugins listed here run in the same environment as the agent that loads them. The validation CI checks that source URLs resolve, but it does **not** audit plugin behavior. Adding a plugin to this marketplace is an endorsement that it's a Zapier-maintained or Zapier-vetted plugin — review accordingly.
