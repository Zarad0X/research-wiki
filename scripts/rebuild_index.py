#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
INDEX = WIKI / "index.md"
EXCLUDED = {"index.md", "log.md"}

SECTION_ORDER = [
    ("overview", "Overview"),
    ("papers", "Papers"),
    ("topics", "Topics"),
    ("methods", "Methods"),
    ("benchmarks", "Benchmarks"),
    ("people", "People"),
    ("ideas", "Ideas"),
    ("syntheses", "Syntheses"),
    ("sources", "Sources"),
]


@dataclass
class Page:
    slug: str
    title: str
    summary: str
    section: str
    relpath: Path


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    block = text[4:end]
    data: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def extract_title(text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return fallback.replace("-", " ").title()


def extract_summary(frontmatter: dict[str, str], text: str) -> str:
    summary = frontmatter.get("summary")
    if summary:
        return summary
    for line in text.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#") and stripped != "---":
            return stripped
    return "No summary yet."


def detect_section(relpath: Path, frontmatter: dict[str, str]) -> str:
    kind = frontmatter.get("kind", "").strip().lower()
    if kind == "overview":
        return "overview"
    if relpath.parent == Path("."):
        return "overview"
    return relpath.parts[0]


def load_pages() -> list[Page]:
    pages: list[Page] = []
    for path in sorted(WIKI.rglob("*.md")):
        if path.name in EXCLUDED:
            continue
        relpath = path.relative_to(WIKI)
        text = path.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(text)
        slug = path.stem
        title = frontmatter.get("title") or extract_title(text, slug)
        summary = extract_summary(frontmatter, text)
        section = detect_section(relpath, frontmatter)
        pages.append(Page(slug=slug, title=title, summary=summary, section=section, relpath=relpath))
    return pages


def build_index(pages: list[Page]) -> str:
    grouped: dict[str, list[Page]] = {key: [] for key, _ in SECTION_ORDER}
    for page in pages:
        grouped.setdefault(page.section, []).append(page)

    lines = ["# Wiki Index", "", "由 `python3 scripts/rebuild_index.py` 自动维护。", ""]
    for section_key, section_title in SECTION_ORDER:
        items = grouped.get(section_key, [])
        count_suffix = f" ({len(items)})" if items else ""
        lines.append(f"## {section_title}{count_suffix}")
        lines.append("")
        if not items:
            lines.append("- 暂无")
            lines.append("")
            continue
        for page in sorted(items, key=lambda item: item.slug):
            lines.append(f"- [[{page.slug}]] - {page.title}. {page.summary}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    pages = load_pages()
    INDEX.write_text(build_index(pages), encoding="utf-8")
    print(f"Rebuilt {INDEX} with {len(pages)} pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
