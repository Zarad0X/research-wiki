#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "inbox"
TEMPLATE = ROOT / "templates" / "inbox-item.md"


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a structured inbox item for the research wiki.")
    parser.add_argument("title")
    parser.add_argument("--source-type", default="paper")
    parser.add_argument("--priority", default="normal")
    parser.add_argument("--status", default="pending")
    parser.add_argument("--slug", help="Override the auto-generated file slug.")
    parser.add_argument("--link", default="TODO")
    parser.add_argument("--notes", default="TODO")
    return parser.parse_args()


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
    slug = args.slug or slugify(args.title)
    path = INBOX / f"{date.today().isoformat()}-{slug}.md"
    if path.exists():
        raise SystemExit(f"Refusing to overwrite existing inbox item: {path}")
    content = TEMPLATE.read_text(encoding="utf-8").format(
        title=args.title,
        source_type=args.source_type,
        priority=args.priority,
        status=args.status,
        created=date.today().isoformat(),
        link=args.link,
        notes=args.notes,
    )
    content = normalize_frontmatter(content)
    path.write_text(content, encoding="utf-8")
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
