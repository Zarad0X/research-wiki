#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
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
    path.write_text(content, encoding="utf-8")
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
