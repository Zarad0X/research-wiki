#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "inbox"
IGNORED = {"README.md", ".DS_Store"}
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def describe(path: Path) -> str:
    stat = path.stat()
    modified = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M")
    size_kb = max(1, stat.st_size // 1024)
    kind = "dir" if path.is_dir() else path.suffix.lstrip(".") or "file"
    if path.is_file() and path.suffix == ".md":
        frontmatter = parse_frontmatter(path.read_text(encoding="utf-8"))
        title = frontmatter.get("title", path.stem)
        source_type = frontmatter.get("source_type", kind)
        status = frontmatter.get("status", "pending")
        priority = frontmatter.get("priority", "normal")
        return (
            f"- {path.name} | {title} | {source_type} | status={status} | "
            f"priority={priority} | {size_kb} KB | modified {modified}"
        )
    return f"- {path.name} | {kind} | {size_kb} KB | modified {modified}"


def main() -> int:
    items = sorted(path for path in INBOX.iterdir() if path.name not in IGNORED)
    print("Inbox Status")
    print("============")
    print(f"Path: {INBOX}")
    print("")
    if not items:
        print("Inbox is empty.")
        return 0

    print(f"Pending items: {len(items)}")
    print("")
    for item in items:
        print(describe(item))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
