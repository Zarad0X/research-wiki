#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
TEMPLATES = ROOT / "templates"

DIR_BY_KIND = {
    "paper": "papers",
    "source": "sources",
    "topic": "topics",
    "method": "methods",
    "benchmark": "benchmarks",
    "person": "people",
    "idea": "ideas",
    "synthesis": "syntheses",
}


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a new research wiki page from a template.")
    parser.add_argument("kind", choices=sorted(DIR_BY_KIND))
    parser.add_argument("title")
    parser.add_argument("--slug", help="Override the auto-generated slug.")
    parser.add_argument("--year", help="Prefix paper slugs with a publication year, e.g. 2024.")
    parser.add_argument("--summary", default="TODO: add one-line summary.")
    parser.add_argument("--status", default="active")
    parser.add_argument("--source-count", default="0")
    parser.add_argument("--force", action="store_true", help="Overwrite an existing page.")
    return parser.parse_args()


def resolve_slug(kind: str, title: str, explicit_slug: str | None, year: str | None) -> str:
    base = explicit_slug or slugify(title)
    if kind == "paper" and year:
        return f"{year}-{base}"
    return base


def load_template(kind: str) -> str:
    template_path = TEMPLATES / f"{kind}.md"
    return template_path.read_text(encoding="utf-8")


def yaml_scalar(value: str) -> str:
    if (
        not value
        or "\n" in value
        or re.search(r":\s", value)
        or value[0] in "#{}[],-?@`!&*'\""
        or value[0].isspace()
        or value[-1].isspace()
    ):
        return json.dumps(value, ensure_ascii=False)
    return value


def normalize_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    if end == -1:
        return text
    block = text[4:end]
    lines = ["---"]
    for line in block.splitlines():
        if ":" not in line:
            lines.append(line)
            continue
        key, value = line.split(":", 1)
        lines.append(f"{key.strip()}: {yaml_scalar(value.strip())}")
    lines.append("---")
    body = text[end + 5 :]
    return "\n".join(lines) + "\n" + body


def main() -> int:
    args = parse_args()
    slug = resolve_slug(args.kind, args.title, args.slug, args.year)
    target_dir = WIKI / DIR_BY_KIND[args.kind]
    target_path = target_dir / f"{slug}.md"

    if target_path.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite existing page: {target_path}")

    content = load_template(args.kind).format(
        title=args.title,
        kind=args.kind,
        slug=slug,
        summary=args.summary,
        updated=date.today().isoformat(),
        status=args.status,
        source_count=args.source_count,
    )
    content = normalize_frontmatter(content)
    target_dir.mkdir(parents=True, exist_ok=True)
    target_path.write_text(content, encoding="utf-8")
    print(target_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
