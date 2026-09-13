#!/usr/bin/env python3
"""Validate the repository's skill and plugin packaging contract."""
from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
errors: list[str] = []


def require(path: str) -> pathlib.Path:
    target = ROOT / path
    if not target.exists():
        errors.append(f"missing: {path}")
    return target


skill = require("SKILL.md")
install = require("INSTALL.md")
agents = require("AGENTS.md")
for path in [".claude-plugin/plugin.json", ".claude-plugin/marketplace.json", ".codex-plugin/plugin.json", ".agents/plugins/marketplace.json"]:
    target = require(path)
    if target.exists():
        try:
            json.loads(target.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSON: {path}: {exc}")

if skill.exists():
    text = skill.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "name: ai-film-studio" not in text:
        errors.append("SKILL.md lacks the expected frontmatter")
    if "workflows/intent-router.md" not in text:
        errors.append("SKILL.md does not point to workflows/intent-router.md")

for path, expected in [
    ("skills/ai-film-studio/SKILL.md", "../../SKILL.md"),
    (".cursor/skills/ai-film-studio/SKILL.md", "../../../SKILL.md"),
]:
    target = ROOT / path
    if not target.is_symlink():
        errors.append(f"compatibility entry point is not a symlink: {path}")
    elif target.readlink().as_posix() != expected:
        errors.append(f"wrong symlink target: {path} -> {target.readlink()}")

if install.exists():
    text = install.read_text(encoding="utf-8")
    for required in [
        "https://github.com/zoih6/ai-film-studio",
        "SKILL.md",
        "workflows/intent-router.md",
    ]:
        if required not in text:
            errors.append(f"INSTALL.md missing: {required}")

if agents.exists() and "SKILL.md" not in agents.read_text(encoding="utf-8"):
    errors.append("AGENTS.md does not identify the skill source of truth")

if errors:
    print("PACKAGE VALIDATION FAILED")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

print("PACKAGE VALIDATION PASSED")
print("- canonical skill: SKILL.md")
print("- plugin manifests: Claude Code + Codex")
print("- compatibility links: standard + Cursor")
print("- installation guide: INSTALL.md")
