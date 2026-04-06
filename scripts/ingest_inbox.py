#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import subprocess
import re


ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "inbox"
RAW = ROOT / "raw"
WIKI = ROOT / "wiki"
LOG = WIKI / "log.md"
TEMPLATES = ROOT / "templates"

DIR_BY_KIND = {
    "paper": "papers",
    "source": "sources",
}
RAW_DIR_BY_KIND = {
    "paper": "papers",
    "source": "sources",
}


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Turn a structured inbox item into a first-pass wiki page skeleton."
    )
    parser.add_argument("item", help="Inbox item path, file name, or slug fragment.")
    parser.add_argument(
        "--kind",
        choices=sorted(DIR_BY_KIND),
        help="Override the inferred page kind. Defaults to paper for paper-like inbox items, otherwise source.",
    )
    parser.add_argument(
        "--year",
        help="Optional publication year prefix for paper pages, e.g. 2024.",
    )
    parser.add_argument(
        "--source-count",
        default="1",
        help="Initial source_count value for the created page.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the planned actions without writing files.",
    )
    return parser.parse_args()


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    block = text[4:end]
    data: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    body = text[end + 5 :]
    return data, body


def dump_frontmatter(frontmatter: dict[str, str], body: str) -> str:
    lines = ["---"]
    for key, value in frontmatter.items():
        lines.append(f"{key}: {value}")
    lines.append("---")
    lines.append("")
    lines.append(body.lstrip("\n"))
    return "\n".join(lines).rstrip() + "\n"


def resolve_inbox_path(raw: str) -> Path:
    candidate = Path(raw).expanduser()
    if candidate.exists():
        return candidate.resolve()

    direct = INBOX / raw
    if direct.exists():
        return direct.resolve()

    if not raw.endswith(".md") and (INBOX / f"{raw}.md").exists():
        return (INBOX / f"{raw}.md").resolve()

    matches = sorted(INBOX.glob(f"*{raw}*.md"))
    if len(matches) == 1:
        return matches[0].resolve()
    if len(matches) > 1:
        names = ", ".join(path.name for path in matches)
        raise SystemExit(f"Ambiguous inbox item '{raw}'. Matches: {names}")
    raise SystemExit(f"Could not find inbox item: {raw}")


def infer_kind(frontmatter: dict[str, str], explicit_kind: str | None) -> str:
    if explicit_kind:
        return explicit_kind
    source_type = frontmatter.get("source_type", "").strip().lower()
    if source_type in {"paper", "preprint"}:
        return "paper"
    return "source"


def resolve_page_slug(kind: str, title: str, explicit_year: str | None) -> str:
    base = slugify(title)
    if kind == "paper" and explicit_year:
        return f"{explicit_year}-{base}"
    return base


def load_template(kind: str) -> str:
    return (TEMPLATES / f"{kind}.md").read_text(encoding="utf-8")


def extract_source_link(body: str) -> str:
    marker = "## Source Link"
    if marker not in body:
        return "TODO"
    section = body.split(marker, 1)[1]
    lines = [line.strip() for line in section.splitlines()[1:]]
    collected: list[str] = []
    for line in lines:
        if not line:
            if collected:
                break
            continue
        if line.startswith("## "):
            break
        collected.append(line)
    return "\n".join(collected).strip() or "TODO"


def extract_notes(body: str) -> str:
    marker = "## Notes"
    if marker not in body:
        return "TODO"
    section = body.split(marker, 1)[1]
    lines = [line.rstrip() for line in section.splitlines()[1:]]
    collected: list[str] = []
    for line in lines:
        if line.startswith("## "):
            break
        collected.append(line)
    text = "\n".join(collected).strip()
    return text or "TODO"


def build_page_content(
    kind: str,
    title: str,
    slug: str,
    source_count: str,
    source_link: str,
    raw_relpath: Path,
    notes: str,
) -> str:
    content = load_template(kind).format(
        title=title,
        kind=kind,
        slug=slug,
        summary=f"TODO: ingest from archived source {raw_relpath.as_posix()}.",
        updated=date.today().isoformat(),
        status="active",
        source_count=source_count,
    )
    if kind == "paper":
        replacement = (
            "## Sources\n\n"
            f"- Archived source: `{raw_relpath.as_posix()}`\n"
            f"- Source link: {source_link}\n"
        )
    else:
        replacement = (
            "## Source Metadata\n\n"
            f"- Archived source: `{raw_relpath.as_posix()}`\n"
            f"- Source link: {source_link}\n\n"
            "## Summary\n\nTODO\n\n"
            "## Key Takeaways\n\n"
            f"{notes}\n\n"
            "## Connections\n\nTODO\n\n"
            "## Sources\n\n"
            f"- Archived source: `{raw_relpath.as_posix()}`\n"
            f"- Source link: {source_link}\n"
        )
    return content.replace("## Sources\n\nTODO\n", replacement)


def build_raw_content(
    frontmatter: dict[str, str],
    body: str,
    raw_relpath: Path,
    page_slug: str,
    source_link: str,
) -> str:
    archived_frontmatter = dict(frontmatter)
    archived_frontmatter["status"] = "archived"
    archived_frontmatter["archived_on"] = date.today().isoformat()
    archived_frontmatter["linked_page"] = page_slug
    archived_frontmatter["raw_path"] = raw_relpath.as_posix()
    if source_link != "TODO":
        archived_frontmatter["source_link"] = source_link
    archived_body = body
    if "## Linked Page" in archived_body:
        archived_body = re.sub(
            r"## Linked Page\s+.*?(?=\n## |\Z)",
            f"## Linked Page\n\n[[{page_slug}]]\n",
            archived_body,
            flags=re.DOTALL,
        )
    elif "## Notes" in archived_body:
        archived_body = archived_body.replace(
            "## Notes",
            f"## Linked Page\n\n[[{page_slug}]]\n\n## Notes",
            1,
        )
    else:
        archived_body = archived_body.rstrip() + f"\n\n## Linked Page\n\n[[{page_slug}]]\n"
    return dump_frontmatter(archived_frontmatter, archived_body)


def append_log_entry(page_slug: str, page_kind: str, raw_relpath: Path) -> None:
    existing = LOG.read_text(encoding="utf-8").rstrip()
    entry = "\n".join(
        [
            f"## [{date.today().isoformat()}] ingest | {page_kind} from inbox",
            "",
            f"- Archived the source into `{raw_relpath.as_posix()}`.",
            f"- Created `[[{page_slug}]]` from the archived source.",
            "- Rebuilt `wiki/index.md` and ran lint after the ingest scaffold.",
        ]
    )
    LOG.write_text(existing + "\n\n" + entry + "\n", encoding="utf-8")


def run_script(script_name: str) -> None:
    subprocess.run(
        ["python3", str(ROOT / "scripts" / script_name)],
        check=True,
        cwd=ROOT,
    )


def main() -> int:
    args = parse_args()
    inbox_path = resolve_inbox_path(args.item)
    text = inbox_path.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)
    title = frontmatter.get("title")
    if not title:
        raise SystemExit(f"Inbox item is missing a title: {inbox_path}")

    page_kind = infer_kind(frontmatter, args.kind)
    page_slug = resolve_page_slug(page_kind, title, args.year)
    target_dir = WIKI / DIR_BY_KIND[page_kind]
    target_path = target_dir / f"{page_slug}.md"
    raw_dir = RAW / RAW_DIR_BY_KIND[page_kind]
    raw_path = raw_dir / inbox_path.name
    raw_relpath = raw_path.relative_to(ROOT)
    if target_path.exists():
        raise SystemExit(f"Refusing to overwrite existing page: {target_path}")
    if raw_path.exists():
        raise SystemExit(f"Refusing to overwrite existing archived source: {raw_path}")

    source_link = extract_source_link(body)
    notes = extract_notes(body)
    content = build_page_content(
        kind=page_kind,
        title=title,
        slug=page_slug,
        source_count=args.source_count,
        source_link=source_link,
        raw_relpath=raw_relpath,
        notes=notes,
    )
    raw_content = build_raw_content(frontmatter, body, raw_relpath, page_slug, source_link)

    if args.dry_run:
        print(f"Would archive: {raw_path}")
        print(f"Would create: {target_path}")
        print(f"Would remove from inbox: {inbox_path}")
        print(f"Would append log entry for [[{page_slug}]] and {raw_relpath.as_posix()}")
        return 0

    raw_dir.mkdir(parents=True, exist_ok=True)
    target_dir.mkdir(parents=True, exist_ok=True)
    raw_path.write_text(raw_content, encoding="utf-8")
    target_path.write_text(content, encoding="utf-8")
    inbox_path.unlink()
    append_log_entry(page_slug, page_kind, raw_relpath)
    run_script("rebuild_index.py")
    run_script("lint_wiki.py")
    print(target_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
