#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
SPECIAL = {"index", "log", "overview"}
LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
VALID_KINDS = {
    "paper",
    "source",
    "topic",
    "method",
    "benchmark",
    "person",
    "idea",
    "synthesis",
    "overview",
}
DIR_TO_KIND = {
    "papers": "paper",
    "sources": "source",
    "topics": "topic",
    "methods": "method",
    "benchmarks": "benchmark",
    "people": "person",
    "ideas": "idea",
    "syntheses": "synthesis",
}
REQUIRED_SECTIONS = {
    "paper": {"Summary", "Problem", "Main Idea", "Connections", "Sources"},
    "source": {"Summary", "Connections", "Sources"},
    "topic": {"Summary", "Connections", "Sources"},
    "method": {"Summary", "Connections", "Sources"},
    "benchmark": {"Summary", "Connections", "Sources"},
    "person": {"Summary", "Connections", "Sources"},
    "idea": {"Summary", "Connections", "Sources"},
    "synthesis": {"Summary", "Connections", "Sources"},
    "overview": {"Summary", "Sources"},
}
HEADER_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)


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


def load_pages() -> tuple[dict[str, Path], list[str]]:
    pages: dict[str, Path] = {}
    slug_issues: list[str] = []
    for path in WIKI.rglob("*.md"):
        if path.name == "log.md":
            continue
        slug = path.stem
        if slug in pages:
            slug_issues.append(
                f"duplicate slug '{slug}' used by: {pages[slug].relative_to(ROOT)}, {path.relative_to(ROOT)}"
            )
        pages[slug] = path
    return pages, slug_issues


def extract_sections(text: str) -> set[str]:
    return {match.group(1).strip() for match in HEADER_RE.finditer(text)}


def main() -> int:
    pages, slug_issues = load_pages()
    broken_links: list[tuple[str, str]] = []
    inbound_counts: Counter[str] = Counter()
    frontmatter_issues: list[str] = []
    structure_issues: list[str] = []
    title_issues: list[str] = []
    section_issues: list[str] = []
    outgoing: dict[str, set[str]] = defaultdict(set)
    titles: defaultdict[tuple[str, str], list[str]] = defaultdict(list)

    for slug, path in sorted(pages.items()):
        text = path.read_text(encoding="utf-8")
        if slug not in SPECIAL:
            frontmatter = parse_frontmatter(text)
            for key in ("title", "kind", "summary", "updated"):
                if key not in frontmatter:
                    frontmatter_issues.append(f"{path.relative_to(ROOT)} missing frontmatter key: {key}")
            title = frontmatter.get("title", "").strip()
            kind = frontmatter.get("kind", "").strip().lower()
            updated = frontmatter.get("updated", "").strip()
            source_count = frontmatter.get("source_count", "").strip()
            if title:
                titles[(title.casefold(), kind or "unknown")].append(str(path.relative_to(ROOT)))
            if kind and kind not in VALID_KINDS:
                structure_issues.append(f"{path.relative_to(ROOT)} has invalid kind: {kind}")
            if updated and not DATE_RE.match(updated):
                structure_issues.append(f"{path.relative_to(ROOT)} has invalid updated date: {updated}")
            if source_count and not source_count.isdigit():
                structure_issues.append(f"{path.relative_to(ROOT)} has non-numeric source_count: {source_count}")

            expected_kind = DIR_TO_KIND.get(path.parent.name)
            if expected_kind and kind and expected_kind != kind:
                structure_issues.append(
                    f"{path.relative_to(ROOT)} is in {path.parent.name}/ but kind is {kind} (expected {expected_kind})"
                )

            sections = extract_sections(text)
            for required_section in sorted(REQUIRED_SECTIONS.get(kind, set())):
                if required_section not in sections:
                    section_issues.append(
                        f"{path.relative_to(ROOT)} missing required section: {required_section}"
                    )

        for target in LINK_RE.findall(text):
            target_slug = target.split("|", 1)[0].strip()
            outgoing[slug].add(target_slug)
            if target_slug not in pages:
                broken_links.append((slug, target_slug))
            else:
                inbound_counts[target_slug] += 1

    for title_key, paths in sorted(titles.items()):
        if len(paths) > 1:
            lowered_title, kind = title_key
            title_issues.append(f"duplicate title '{lowered_title}' within kind '{kind}' used by: {', '.join(paths)}")

    orphan_pages = []
    for slug, path in sorted(pages.items()):
        if slug in SPECIAL:
            continue
        if inbound_counts[slug] == 0:
            orphan_pages.append(str(path.relative_to(ROOT)))

    print("LLM Wiki Lint")
    print("=============")
    print(f"Pages checked: {len(pages)}")
    print("")

    if frontmatter_issues:
        print("Frontmatter issues:")
        for issue in frontmatter_issues:
            print(f"- {issue}")
        print("")

    if structure_issues:
        print("Structure issues:")
        for issue in structure_issues:
            print(f"- {issue}")
        print("")

    if slug_issues:
        print("Slug issues:")
        for issue in slug_issues:
            print(f"- {issue}")
        print("")

    if title_issues:
        print("Duplicate title issues:")
        for issue in title_issues:
            print(f"- {issue}")
        print("")

    if section_issues:
        print("Section issues:")
        for issue in section_issues:
            print(f"- {issue}")
        print("")

    if broken_links:
        print("Broken links:")
        for source_slug, target_slug in broken_links:
            print(f"- {source_slug} -> [[{target_slug}]]")
        print("")

    if orphan_pages:
        print("Orphan pages:")
        for page in orphan_pages:
            print(f"- {page}")
        print("")

    if not frontmatter_issues and not structure_issues and not slug_issues and not title_issues and not section_issues and not broken_links and not orphan_pages:
        print("No obvious issues found.")

    return 1 if frontmatter_issues or structure_issues or slug_issues or title_issues or section_issues or broken_links else 0


if __name__ == "__main__":
    raise SystemExit(main())
