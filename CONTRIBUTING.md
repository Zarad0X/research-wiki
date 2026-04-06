# Contributing

This repository is both a human-readable research wiki and an agent-maintained memory system. Contributions should protect both properties:

- for humans, content should be clear, readable, and traceable
- for agents, structure should stay stable, patchable, and lintable

## Principles

- prefer small, incremental changes
- keep page schemas stable; do not rename sections casually
- important claims should trace back to `wiki/papers/` or `wiki/sources/`
- update existing pages before creating overlapping topics
- treat `raw/` as source of truth

## Repository Map

- `inbox/`: pending material that has not entered the archive yet
- `raw/`: archived source material and the canonical source layer
- `wiki/`: compiled knowledge maintained by agents
- `templates/`: page templates
- `scripts/`: index, lint, query, and creation tools
- `AGENTS.md`: the operating protocol for LLMs and agents

## Common Contribution Types

- add a new paper page
- update a topic page
- add a synthesis page
- expand a benchmark / method / person page
- fix broken links, structural issues, or missing sections
- improve scripts or templates

## Human Workflow

1. Read [README.md](/Users/zhanghan/workspace/research-wiki/README.md) and [AGENTS.md](/Users/zhanghan/workspace/research-wiki/AGENTS.md)
2. Put new source material into `inbox/` first
3. Use these scripts as needed:

```bash
python3 scripts/inbox_status.py
python3 scripts/create_inbox.py "A new paper to read" --source-type paper
python3 scripts/ingest_inbox.py "2026-04-06-a-new-paper-to-read.md" --year 2026
python3 scripts/create_page.py paper "A Paper Title" --year 2026
python3 scripts/query_wiki.py "world action model"
python3 scripts/rebuild_index.py
python3 scripts/lint_wiki.py
```

4. Before finishing, at minimum run:

```bash
python3 scripts/rebuild_index.py
python3 scripts/lint_wiki.py
```

## Agent Workflow

If you use Codex / Claude Code / Openclaw or similar agents:

1. Read [AGENTS.md](/Users/zhanghan/workspace/research-wiki/AGENTS.md) first
2. If answering a question, run:

```bash
python3 scripts/query_wiki.py "<query>"
```

3. If ingesting a new source:
   - read `wiki/index.md`, `wiki/overview.md`, and `wiki/log.md`
   - prefer `ingest_inbox.py` when the source already exists as a structured inbox item
   - when using `ingest_inbox.py`, expect the source to move from `inbox/` into `raw/`
   - classify the source and affected pages
   - use `create_page.py` when creating new pages
4. After edits, always:
   - update `wiki/log.md`
   - run `rebuild_index.py`
   - run `lint_wiki.py`

## Page Conventions

- use kebab-case file names
- paper pages should usually be named `year-short-title.md`
- `kind` must match the containing directory
- keep stable section names so agents can patch incrementally

At minimum, paper pages should preserve:

- `Summary`
- `Problem`
- `Main Idea`
- `Connections`
- `Sources`

When appropriate, also add:

- `Story / Setting`
- `Why This Exists`
- `Related Work`
- `First Principles`
- `Core Architecture`
- `Method`
- `Experimental Setup`
- `Results`
- `Strengths`
- `Limitations`
- `Questions`
- `My Take`

## Writing Style

- write reusable research conclusions, not chat residue
- distinguish facts, interpretations, and speculation
- keep writing compressed without losing traceability
- when old and new conclusions conflict, surface the tension instead of silently overwriting it

## Language Policy

- repository-facing infrastructure should stay in English:
  - `README.md`
  - `AGENTS.md`
  - `CONTRIBUTING.md`
  - scripts and their user-facing output
  - Obsidian / vault configuration docs
- research-note content may stay in Chinese if that is more practical for the repository owner
- do not translate existing paper notes or syntheses into English unless explicitly requested

## Pull Request Checklist

Before submitting, check:

- did you update related topics or syntheses, not only a single paper
- did you create avoidable duplicate pages
- did you include `Sources`
- did you run `rebuild_index.py`
- did you run `lint_wiki.py`
- did you record major changes in `wiki/log.md`

## License and Attribution

- the repository's code, scripts, templates, and structure are governed by the root [LICENSE](/Users/zhanghan/workspace/research-wiki/LICENSE)
- this repository is inspired by Andrej Karpathy's `llm-wiki` gist but is an independent implementation
- when you include outside material, keep the necessary attribution and do not assume outside content is automatically covered by this repository's license
