# Contributing

Thanks for your interest in `zapier/marketplace`. This repo is small and opinionated: it's a pointer manifest that lets agents discover Zapier plugins, not a place to host plugin source. Most contributions fit one of two shapes:

1. **Add or update a Zapier-owned plugin entry** — see [adding a plugin](#adding-a-plugin) below
2. **Improve the schemas, CI, or repo scaffolding** — open a PR with a clear summary of what's changing and why

For everything else (general questions, support for a specific plugin), open the issue in the plugin's home repo, not here. See the [plugin table in the README](./README.md#plugins) for links.

## Before you start

- Read [AGENTS.md](./AGENTS.md). It's short, and it covers the manifest invariant (plugins listed in two or more platforms must resolve to the same source), the naming convention (short, kebab-case product names — no `zapier-` prefix), and the CI that enforces all of it.
- Skim [`schemas/README.md`](./schemas/README.md) so you know which JSON Schema your changes will be validated against.

## Adding a plugin

1. **Confirm the home repo is ready.** Each platform's marketplace consumes a different per-plugin manifest from the source repo — `.claude-plugin/plugin.json` for Claude Code, the equivalent for Copilot CLI, and `.codex-plugin/plugin.json` for Codex. The plugin won't install on a given platform if that platform's manifest isn't published in the home repo.
2. **Add the plugin to each manifest whose per-plugin manifest exists in the home repo.** Today that is usually just [`.claude-plugin/marketplace.json`](./.claude-plugin/marketplace.json); Copilot ([`.github/plugin/marketplace.json`](./.github/plugin/marketplace.json)) and Codex ([`.agents/plugins/marketplace.json`](./.agents/plugins/marketplace.json)) are scaffolded but empty until source repos publish their platform manifests. It is fine to land a Claude-only entry — CI only enforces cross-manifest source parity across populated manifests.
3. **Fill in the optional fields.** `displayName`, `description`, `author`, `homepage`, `repository`, `license`, `category`, and `tags` all render in the marketplace listing before install — populate them so browsing is useful. See `schemas/` for the full field list.
4. **Pick the right name.** Short, kebab-case product names — `notion`, `slack`, `mcp`, `sdk`. Do **not** prefix with `zapier-`; the `@zapier` marketplace suffix at install time already provides namespacing.
5. **Open the PR.** The `Validate marketplace manifests` workflow runs JSON syntax, schema validation, source-URL reachability, and the consistency check. Fix anything it flags; merge when green and reviewed.

## Removing or renaming a plugin

Both are user-visible breaking changes — anyone with the plugin installed will see it disappear or fail to update. Don't do either silently:

- **Remove:** open a PR explaining why, and call it out in the PR description so reviewers can flag it for users.
- **Rename:** use the marketplace-level [`renames`](https://code.claude.com/docs/en/plugin-marketplaces) map (Claude Code v2.1.193+) to migrate existing installs automatically. Add the new entry, add the old → new (or old → `null`) mapping in `renames`, and remove the old entry in the same PR.

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
4. Cross-manifest consistency — for any plugin listed in more than one populated manifest, the source target must match. Empty manifests (`plugins: []`) skip the check.

If any step fails, the PR isn't mergeable. Look at the failed step's output first — the errors are designed to point at the specific manifest and entry that's off.

## PR conventions

- One concern per PR. Adding a plugin, fixing a schema, and refactoring CI should each be their own PR.
- Branch names use the standard public-repo convention: `feat/short-description`, `fix/short-description`, `chore/short-description`.
- Commit messages follow the same convention (`feat: …`, `fix: …`, `chore: …`).
- Keep PR descriptions focused on the "why" — the diff already covers the "what".

## Reporting a security issue

Don't open a public issue for security-sensitive reports. Email **security@zapier.com** instead. See the [org-wide security policy](https://github.com/zapier/.github/blob/main/SECURITY.md) for what to include.
