# Contributing

Thanks for your interest in `zapier/marketplace`. This repo is small and opinionated: it's a pointer manifest that lets agents discover Zapier plugins, not a place to host plugin source. Most contributions fit one of two shapes:

1. **Add or update a Zapier-owned plugin entry** — see [adding a plugin](#adding-a-plugin) below
2. **Improve the schemas, CI, or repo scaffolding** — open a PR with a clear summary of what's changing and why

For everything else (general questions, support for a specific plugin), open the issue in the plugin's home repo, not here. See the [plugin table in the README](./README.md#plugins) for links.

## Before you start

- Read [AGENTS.md](./AGENTS.md). It's short, and it covers the hard invariant (three manifests must stay in sync), the naming convention (`zapier-<product>` for third-party connectors, short names for first-party), and the CI that enforces all of it.
- Skim [`schemas/README.md`](./schemas/README.md) so you know which JSON Schema your changes will be validated against.

## Adding a plugin

1. **Confirm the home repo is ready.** Each platform's marketplace consumes a different per-plugin manifest from the source repo — `.claude-plugin/plugin.json` for Claude Code, the equivalent for Copilot CLI, and `.codex-plugin/plugin.json` for Codex. The plugin won't install if those aren't published in the home repo.
2. **Edit all three manifests** in the same PR:
   - [`.claude-plugin/marketplace.json`](./.claude-plugin/marketplace.json)
   - [`.github/plugin/marketplace.json`](./.github/plugin/marketplace.json)
   - [`.agents/plugins/marketplace.json`](./.agents/plugins/marketplace.json)

   Same `name`, same source target (repo, path, ref). CI's cross-manifest consistency check fails if any of those drift.
3. **Pick the right name.** Third-party connectors use `zapier-<product>` (e.g. `zapier-notion`). First-party Zapier products use a short name (`mcp`, `agent-skills`).
4. **Open the PR.** The `Validate marketplace manifests` workflow runs JSON syntax, schema validation, source-URL reachability, and the consistency check. Fix anything it flags; merge when green and reviewed.

## Removing or renaming a plugin

Both are user-visible breaking changes — anyone with the plugin installed will see it disappear or fail to update. Don't do either silently:

- **Remove:** open a PR explaining why, and call it out in the PR description so reviewers can flag it for users.
- **Rename:** prefer adding the new entry first, leaving the old one in place for a grace period, then removing the old one in a follow-up PR.

## Updating a schema

The schemas in [`schemas/`](./schemas/) are self-authored, derived from each platform's canonical reference marketplace and public docs. Update one when:

- A platform publishes an official schema we should adopt (replace ours and link the source)
- A real-world marketplace from that platform uses a field our schema doesn't allow (extend ours)

When you update a schema, bump its top-level `description` to note the new source so future readers can audit provenance.

## CI

Every PR runs [`.github/workflows/validate-marketplace.yml`](./.github/workflows/validate-marketplace.yml):

1. JSON syntax (`jq empty`) on each manifest
2. Schema validation (`ajv`) against the matching file in `schemas/`
3. Source-URL reachability — every linked source repo must 200
4. Cross-manifest consistency — same plugin name, same source target across all three files

If any step fails, the PR isn't mergeable. Look at the failed step's output first — the errors are designed to point at the specific manifest and entry that's off.

## PR conventions

- One concern per PR. Adding a plugin, fixing a schema, and refactoring CI should each be their own PR.
- Branch names use the standard public-repo convention: `feat/short-description`, `fix/short-description`, `chore/short-description`.
- Commit messages follow the same convention (`feat: …`, `fix: …`, `chore: …`).
- Keep PR descriptions focused on the "why" — the diff already covers the "what".

## Reporting a security issue

Don't open a public issue for security-sensitive reports. Email **security@zapier.com** instead. See the [org-wide security policy](https://github.com/zapier/.github/blob/main/SECURITY.md) for what to include.
