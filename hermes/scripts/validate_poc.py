#!/usr/bin/env python3
"""Validate and optionally install the Hermes job-search POC skills."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys


SKILLS = (
    "job-search-control",
    "job-discovery",
    "job-application",
    "job-search-learning",
)
REQUIRED_FRONTMATTER = (
    "name",
    "description",
    "version",
    "author",
    "license",
    "platforms",
)


def parse_frontmatter(path: Path) -> tuple[dict[str, object], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("frontmatter must start at byte zero")
    match = re.search(r"\n---\s*\n", text[4:])
    if not match:
        raise ValueError("frontmatter is not closed")
    end = match.start() + 4
    raw = text[4:end]
    body = text[match.end() + 4 :].strip()
    values: dict[str, object] = {}
    for line in raw.splitlines():
        if line.startswith((" ", "\t", "-")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    if not body:
        raise ValueError("skill body is empty")
    return values, text


def validate(repo_hermes: Path) -> dict[str, object]:
    errors: list[str] = []
    manifest: dict[str, str] = {}
    for skill in SKILLS:
        path = repo_hermes / "skills" / skill / "SKILL.md"
        if not path.is_file():
            errors.append(f"{skill}: missing SKILL.md")
            continue
        try:
            frontmatter, text = parse_frontmatter(path)
        except ValueError as exc:
            errors.append(f"{skill}: {exc}")
            continue
        missing = [key for key in REQUIRED_FRONTMATTER if not frontmatter.get(key)]
        if missing:
            errors.append(f"{skill}: missing {', '.join(missing)}")
        if frontmatter.get("name") != skill:
            errors.append(f"{skill}: frontmatter name does not match directory")
        description = str(frontmatter.get("description", ""))
        if len(description) > 60 or not description.endswith("."):
            errors.append(f"{skill}: description must be <=60 chars and end with a period")
        if len(text) > 100_000:
            errors.append(f"{skill}: SKILL.md exceeds 100,000 characters")
        manifest[skill] = hashlib.sha256(text.encode("utf-8")).hexdigest()

    model = repo_hermes / "skills" / "job-search-control" / "references" / "data-model.md"
    if not model.is_file():
        errors.append("job-search-control: missing references/data-model.md")
    return {"ok": not errors, "errors": errors, "manifest": manifest}


def install(repo_hermes: Path, hermes_home: Path, force: bool) -> list[str]:
    installed: list[str] = []
    target_root = hermes_home / "skills" / "productivity"
    target_root.mkdir(parents=True, exist_ok=True)
    for skill in SKILLS:
        source = repo_hermes / "skills" / skill
        target = target_root / skill
        if target.exists():
            if not force:
                raise FileExistsError(f"refusing to overwrite {target}; rerun with --force")
            shutil.rmtree(target)
        shutil.copytree(source, target)
        installed.append(str(target))
    return installed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-hermes", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--install", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--hermes-home", type=Path, default=Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes")))
    args = parser.parse_args()

    result = validate(args.repo_hermes)
    if result["ok"] and args.install:
        try:
            result["installed"] = install(args.repo_hermes, args.hermes_home, args.force)
        except (FileExistsError, OSError) as exc:
            result["ok"] = False
            result["errors"].append(str(exc))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
