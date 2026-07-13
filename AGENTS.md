# AGENTS.md

Canonical guide for AI agents (and humans) working in `zapier/marketplace`. `CLAUDE.md` is a one-line shim that points here.

## Repository purpose

This repo is the central pointer manifest that lets agents discover Zapier plugins across Claude Code, GitHub Copilot CLI, and OpenAI Codex. It does **not** host plugin source — every plugin lives in its own home repo. This repo only maintains the marketplace entries that point at those repos.

## Manifest invariant: any plugin listed in two or more platforms must resolve to the same source

There are three manifest files, one per platform:

- [`.claude-plugin/marketplace.json`](./.claude-plugin/marketplace.json) — Claude Code (populated)
- [`.github/plugin/marketplace.json`](./.github/plugin/marketplace.json) — GitHub Copilot CLI (scaffolded, empty)
- [`.agents/plugins/marketplace.json`](./.agents/plugins/marketplace.json) — OpenAI Codex (populated)

For every plugin that appears in more than one manifest, all copies must:

1. Use the same plugin name
2. Resolve to the same source target (same repo, same `path`, same `ref`)

An **empty manifest** (`plugins: []`) is intentional — a platform we've scaffolded but not yet populated because the per-plugin manifests it needs (`.codex-plugin/plugin.json`, Copilot equivalent) don't yet exist in the home repos. Empty manifests skip the consistency check entirely.

CI fails if a plugin listed in two populated manifests drifts. The consistency check lives at [`.github/scripts/check_consistency.py`](./.github/scripts/check_consistency.py).

When adding a plugin to a populated platform that isn't yet supported by the others, **it is OK to add it to only that platform**. Filling in Codex / Copilot is a follow-up when the source repos ship the platform-specific manifest.

## Naming and ordering

- Plugin names are short, lowercase, kebab-case product names: `notion`, `slack`, `mcp`, `agent-skills`, `gtm-cheat-codes`, `sdk`
- **Do not prefix with `zapier-`.** The `@zapier` marketplace suffix at install time (`/plugin install notion@zapier`) already provides provenance and namespacing — a `zapier-notion@zapier` install would be redundant and reads as Zapier-branded rather than an open connector for the vendor.
- Renaming a plugin is a breaking change for every user who has it installed — use the marketplace `renames` field (Claude Code v2.1.193+) to migrate existing installs when a rename is unavoidable.
- **Keep the plugin list sorted alphabetically by `name`.** Applies to every manifest (`.claude-plugin/marketplace.json`, `.github/plugin/marketplace.json`, `.agents/plugins/marketplace.json`) and to the plugins table in [`README.md`](./README.md). Insert new entries in place; do not append.

## Schemas and validation

Each manifest is validated against a JSON Schema in [`schemas/`](./schemas/). The schemas are self-authored (no platform vendor publishes a canonical schema yet) and derived from each vendor's official marketplace + docs — see [`schemas/README.md`](./schemas/README.md) for provenance. When a vendor adds a field a real-world marketplace uses, update the relevant schema and bump its `description` to note the new source.

## Sources, refs, and pinning

Plugin sources currently pin to `"ref": "main"`. That means every installer pulls the latest commit on the source repo's default branch. Pinning to a specific commit SHA is the safer pattern (auditable, reproducible) — switching to SHA-pinning + an automated bump workflow is on the roadmap, not yet wired up. When adding a new plugin, follow the existing `main` convention unless a PR explicitly changes the convention repo-wide.

## How to add a plugin

For the contributor walkthrough — including the CI checks, review flow, and PR conventions — follow [`CONTRIBUTING.md`](./CONTRIBUTING.md). This section stays short and lists only the invariants those steps must preserve:

1. The home repo must expose the right per-platform manifest at the right path (`.claude-plugin/plugin.json` for Claude Code, `.codex-plugin/plugin.json` for Codex, Copilot equivalent when Copilot comes online). A plugin only gets an entry here for a platform once its home repo publishes that platform's per-plugin manifest.
2. New entries respect the [naming and ordering rules](#naming-and-ordering) above — kebab-case, no `zapier-` prefix, inserted alphabetically.
3. Standard optional fields (`displayName`, `description`, `author`, `homepage`, `repository`, `license`, `category`, `tags`) are populated so the marketplace listing renders useful metadata before install.
4. The same plugin listed in more than one manifest resolves to the same source target — see [manifest invariant](#manifest-invariant-any-plugin-listed-in-two-or-more-platforms-must-resolve-to-the-same-source) above. CI enforces this.

If CI passes and the PR is reviewed, merging makes the plugin installable on the populated platforms.

## What does **not** belong in this repo

- Plugin source — it lives in the plugin's home repo
- Plugin documentation longer than the entry in the manifest — link to the home repo's README
- Platform-specific manifests for plugins that aren't on this marketplace — that's the home repo's job

## Trust model

Plugins listed here run in the same environment as the agent that loads them. The validation CI checks that source URLs resolve, but it does **not** audit plugin behavior. Adding a plugin to this marketplace is an endorsement that it's a Zapier-maintained or Zapier-vetted plugin — review accordingly.
