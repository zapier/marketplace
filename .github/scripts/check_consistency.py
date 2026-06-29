#!/usr/bin/env python3
"""Verify the same plugin entry resolves to the same source target across every manifest."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.parse import urlparse

MANIFESTS = {
    "claude-code": Path(".claude-plugin/marketplace.json"),
    "copilot-cli": Path(".github/plugin/marketplace.json"),
    "codex": Path(".agents/plugins/marketplace.json"),
}


def normalize_path(path: str | None) -> str:
    if not path:
        return ""
    return path.lstrip("./").rstrip("/")


def normalize_url(url: str) -> str:
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    repo_path = parsed.path.removesuffix(".git").strip("/")
    return f"{host}/{repo_path}"


def source_target(source) -> tuple[str, str, str] | None:
    """Return (repo, path, ref) for a plugin source, or None if local-only."""
    if isinstance(source, str):
        return None
    if not isinstance(source, dict):
        return None
    kind = source.get("source")
    ref = source.get("ref", "main")
    path = normalize_path(source.get("path"))
    if kind == "github":
        repo = source.get("repo", "")
        return (f"github.com/{repo}", path, ref)
    if kind in ("git-subdir", "url"):
        url = source.get("url", "")
        return (normalize_url(url), path, ref)
    return None


def main() -> int:
    plugins_by_manifest: dict[str, dict[str, tuple]] = {}
    errors: list[str] = []

    for manifest_name, manifest_path in MANIFESTS.items():
        if not manifest_path.exists():
            errors.append(f"missing manifest: {manifest_path}")
            continue
        data = json.loads(manifest_path.read_text())
        plugins_by_manifest[manifest_name] = {}
        for entry in data.get("plugins", []):
            name = entry.get("name")
            if not name:
                errors.append(f"{manifest_path}: plugin entry without name")
                continue
            target = source_target(entry.get("source"))
            plugins_by_manifest[manifest_name][name] = target

    plugin_names = {
        name for plugins in plugins_by_manifest.values() for name in plugins
    }

    for plugin_name in sorted(plugin_names):
        targets_by_manifest = {
            manifest: plugins.get(plugin_name)
            for manifest, plugins in plugins_by_manifest.items()
        }
        missing = [m for m, t in targets_by_manifest.items() if t is None and plugin_name not in plugins_by_manifest[m]]
        if missing:
            errors.append(f"plugin '{plugin_name}' missing from: {', '.join(missing)}")
        present_targets = {
            m: t for m, t in targets_by_manifest.items()
            if plugin_name in plugins_by_manifest.get(m, {}) and t is not None
        }
        unique_targets = set(present_targets.values())
        if len(unique_targets) > 1:
            errors.append(
                f"plugin '{plugin_name}' has inconsistent source targets across manifests: {present_targets}"
            )

    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        return 1

    print(f"ok: {len(plugin_names)} plugin(s) consistent across {len(plugins_by_manifest)} manifest(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
