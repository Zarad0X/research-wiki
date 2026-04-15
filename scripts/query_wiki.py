#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
WORD_RE = re.compile(r"[a-z0-9_+-]+")
HEADER_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)


@dataclass
class Page:
    slug: str
    title: str
    kind: str
    summary: str
    path: Path
    text: str
    headings: list[str]


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
        parsed = value.strip()
        if len(parsed) >= 2 and parsed[0] == '"' and parsed[-1] == '"':
            try:
                parsed = json.loads(parsed)
            except json.JSONDecodeError:
                pass
        elif len(parsed) >= 2 and parsed[0] == "'" and parsed[-1] == "'":
            parsed = parsed[1:-1]
        data[key.strip()] = parsed
    return data


def tokenize(text: str) -> list[str]:
    return [token for token in WORD_RE.findall(text.lower()) if token]


def load_pages() -> dict[str, Page]:
    pages: dict[str, Page] = {}
    for path in sorted(WIKI.rglob("*.md")):
        if path.name == "log.md":
            continue
        text = path.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(text)
        headings = [match.group(1).strip() for match in HEADER_RE.finditer(text)]
        pages[path.stem] = Page(
            slug=path.stem,
            title=frontmatter.get("title", path.stem),
            kind=frontmatter.get("kind", "unknown"),
            summary=frontmatter.get("summary", ""),
            path=path,
            text=text,
            headings=headings,
        )
    return pages


def inbound_counts(pages: dict[str, Page]) -> dict[str, int]:
    counts = {slug: 0 for slug in pages}
    for page in pages.values():
        for target in LINK_RE.findall(page.text):
            slug = target.split("|", 1)[0].strip()
            if slug in counts:
                counts[slug] += 1
    return counts


OWNER_PRIORITY_KINDS = {"question", "thesis", "program", "review"}


def score_page(page: Page, query_tokens: list[str], inbound: int) -> int:
    haystack = page.text.lower()
    title = page.title.lower()
    summary = page.summary.lower()
    headings = "\n".join(page.headings).lower()
    score = inbound
    for token in query_tokens:
        if token in title:
            score += 20
        if token in summary:
            score += 8
        if token in headings:
            score += 6
        score += haystack.count(token)
    if page.kind in OWNER_PRIORITY_KINDS:
        score += 5
    return score


def best_snippet(page: Page, query_tokens: list[str]) -> str:
    body = page.text
    if body.startswith("---\n"):
        end = body.find("\n---\n", 4)
        if end != -1:
            body = body[end + 5 :]
    lines = [
        line.strip()
        for line in body.splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    for token in query_tokens:
        for line in lines:
            if token in line.lower():
                return line
    return page.summary or (lines[0] if lines else "")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Rank relevant wiki pages for a query and print an agent-friendly context pack.")
    parser.add_argument("query")
    parser.add_argument("--kind", choices=["paper", "source", "topic", "method", "benchmark", "person", "idea", "synthesis", "question", "thesis", "program", "review", "overview"])
    parser.add_argument("--limit", type=int, default=6)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    pages = load_pages()
    query_tokens = tokenize(args.query)
    counts = inbound_counts(pages)

    ranked = []
    for page in pages.values():
        if args.kind and page.kind != args.kind:
            continue
        score = score_page(page, query_tokens, counts.get(page.slug, 0))
        if score > 0:
            ranked.append((score, page))
    ranked.sort(key=lambda item: (-item[0], item[1].slug))

    print("Wiki Query Pack")
    print("===============")
    print(f"Query: {args.query}")
    if args.kind:
        print(f"Kind filter: {args.kind}")
    print("")

    if not ranked:
        print("No matching pages found.")
        return 0

    print("Suggested read order:")
    for index, (score, page) in enumerate(ranked[: args.limit], start=1):
        print(f"{index}. [[{page.slug}]] | kind={page.kind} | score={score}")
        print(f"   title: {page.title}")
        print(f"   path: {page.path.relative_to(ROOT)}")
        if page.headings:
            print(f"   headings: {', '.join(page.headings[:6])}")
        snippet = best_snippet(page, query_tokens)
        if snippet:
            print(f"   snippet: {snippet}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
