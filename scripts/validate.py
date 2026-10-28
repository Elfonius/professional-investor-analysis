#!/usr/bin/env python3
"""Validate the Professional Investor Analysis skill package.

This is a structural check, not an investment check. It verifies that the
package is loadable, internally consistent and within the token budget. It
does not prove that any analysis produced with it is correct.

Usage:
    python scripts/validate.py .
    python scripts/validate.py . --strict
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

TOKEN_CEILING = 5000
LINE_CEILING = 500
DESC_MAX = 1024
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+([+-][0-9A-Za-z.-]+)?$")
POINTER_RE = re.compile(r"(?:references|templates)/[A-Za-z0-9._-]+\.md")
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$")
STEP_RE = re.compile(r"^\d+\. \*\*", re.MULTILINE)
LENS_RE = re.compile(r"^\| \d+ \|", re.MULTILINE)
PRIVACY_PATTERNS = [
    (re.compile(r"C:[\\/]Users[\\/]", re.IGNORECASE), "absolute Windows user path"),
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        raise ValueError("file does not start with YAML frontmatter")
    end = text.find("\n---", 3)
    if end == -1:
        raise ValueError("frontmatter is not closed")
    block = text[3:end].strip("\n")
    body = text[end + 4 :].lstrip("\n")
    data: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip() or line.startswith((" ", "\t", "#")):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1]
        data[key] = value
    return data, body


def count_tokens(text: str) -> tuple[int, str]:
    try:
        import tiktoken  # type: ignore

        enc = tiktoken.get_encoding("o200k_base")
        return len(enc.encode(text)), "measured (tiktoken o200k_base)"
    except Exception:
        return max(1, len(text) // 4), "estimated (len/4; install tiktoken for exact count)"


def check_tables(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    block: list[tuple[int, str]] = []
    start = 0

    def flush() -> None:
        nonlocal block, start
        if len(block) > 1:
            counts = {len(line.replace(r"\|", "").split("|")) for _, line in block}
            if len(counts) > 1:
                errors.append(f"{path}: table starting at line {start} has inconsistent column counts")
        block = []

    for number, line in enumerate(text.splitlines(), 1):
        if TABLE_ROW_RE.match(line):
            if not block:
                start = number
            block.append((number, line))
        else:
            flush()
    flush()
    return errors


def check_links(path: Path, text: str, root: Path) -> list[str]:
    errors: list[str] = []
    for target in LINK_RE.findall(text):
        target = target.strip()
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0].strip()
        if not target:
            continue
        candidate = (root / target.lstrip("/")) if target.startswith("/") else (path.parent / target)
        if not candidate.resolve().exists():
            errors.append(f"{path}: broken relative link '{target}'")
    return errors


def validate(root: Path, strict: bool) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    skill_root = root
    if not (root / "SKILL.md").exists() and (root / "skill" / "SKILL.md").exists():
        skill_root = root / "skill"
    skill_path = skill_root / "SKILL.md"
    if not skill_path.exists():
        print(f"FAIL: {skill_path} not found")
        return 1

    text = read(skill_path)
    try:
        meta, body = parse_frontmatter(text)
    except ValueError as exc:
        print(f"FAIL: {exc}")
        return 1

    for key in ("name", "description", "version", "license", "platforms"):
        if not meta.get(key):
            errors.append(f"SKILL.md: missing frontmatter field '{key}'")

    name = meta.get("name", "")
    if not NAME_RE.match(name):
        errors.append(f"SKILL.md: invalid name '{name}'")
    if len(meta.get("description", "")) > DESC_MAX:
        errors.append(f"SKILL.md: description exceeds {DESC_MAX} characters")
    if not meta.get("description", "").lower().startswith("use when"):
        warnings.append("SKILL.md: description does not start with 'Use when'")
    if not SEMVER_RE.match(meta.get("version", "")):
        errors.append(f"SKILL.md: version '{meta.get('version')}' is not semver")
    if meta.get("license") != "MIT":
        warnings.append("SKILL.md: license is not MIT (expected for this repository)")
    if "windows" not in meta.get("platforms", "") or "linux" not in meta.get("platforms", ""):
        warnings.append("SKILL.md: platforms should include linux, macos and windows")

    lines = body.count("\n") + 1
    tokens, token_source = count_tokens(body)
    if lines > LINE_CEILING:
        errors.append(f"SKILL.md: {lines} lines exceeds {LINE_CEILING}")
    if tokens > TOKEN_CEILING:
        errors.append(f"SKILL.md: {tokens} tokens exceeds {TOKEN_CEILING}")
    if token_source.startswith("estimated"):
        warnings.append(f"SKILL.md: token count is {token_source}")

    for section in ("## When to Use", "## Procedure", "## Gates and standards", "## Verification"):
        if section not in body:
            errors.append(f"SKILL.md: missing required section '{section}'")
    steps = len(STEP_RE.findall(body))
    lenses = len(LENS_RE.findall(body))
    if steps < 10:
        errors.append(f"SKILL.md: only {steps} numbered procedure steps")
    if lenses < 10:
        errors.append(f"SKILL.md: only {lenses} lens rows")

    md_files = sorted((skill_root / "references").glob("*.md"))
    templates = sorted((skill_root / "templates").glob("*.md"))
    if len(md_files) < 10:
        errors.append(f"references/: only {len(md_files)} reference files")
    if len(templates) < 4:
        errors.append(f"templates/: only {len(templates)} template files")

    for required in (
        "templates/investment-screen-en.md",
        "templates/investment-memo-en.md",
        "templates/investment-report-en.md",
        "templates/investment-committee-en.md",
    ):
        if not (skill_root / required).exists():
            errors.append(f"missing English template: {required}")

    scanned = [skill_path] + md_files + templates
    all_md = sorted({*scanned, *(root.glob("*.md")), *(root.glob("docs/*.md")), *(root.glob("examples/*.md"))})
    pointers: set[str] = set()
    for path in all_md:
        content = read(path)
        pointers.update(POINTER_RE.findall(content))
        if path == skill_path or path.parent.name == "references":
            if "{{" in content:
                errors.append(f"{path}: placeholder '{{{{' leaked into method/reference content")
        errors.extend(check_tables(path, content))
        errors.extend(check_links(path, content, root))

    for pointer in sorted(pointers):
        if not (skill_root / pointer).exists():
            errors.append(f"dangling pointer: {pointer} (referenced in the package)")

    for path in all_md:
        content = read(path)
        for pattern, label in PRIVACY_PATTERNS:
            if pattern.search(content):
                errors.append(f"{path}: contains {label}")

    print("Professional Investor Analysis — validation")
    print(f"Repository: {root}")
    print(f"Skill package: {skill_root}")
    print(f"Name: {name}")
    print(f"Version: {meta.get('version')}")
    print(f"SKILL.md: {lines} lines, {tokens:,} tokens — {token_source}")
    print(f"References: {len(md_files)} · Templates: {len(templates)} · Pointers: {len(pointers)}")
    print(f"Procedure steps: {steps} · Lens rows: {lenses}")
    print()

    for warning in warnings:
        print(f"WARN: {warning}")
    for error in errors:
        print(f"FAIL: {error}")

    if errors:
        print(f"\nFAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    if strict and warnings:
        print(f"\nFAILED (strict): {len(warnings)} warning(s)")
        return 1
    print(f"\nPASS: 0 errors, {len(warnings)} warning(s)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="repository root (default: .)")
    parser.add_argument("--strict", action="store_true", help="treat warnings as failures")
    args = parser.parse_args()
    return validate(Path(args.root).resolve(), args.strict)


if __name__ == "__main__":
    sys.exit(main())
