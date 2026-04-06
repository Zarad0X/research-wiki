# Research Wiki

This repository is an independent implementation inspired by Andrej Karpathy's `llm-wiki` gist.

It is not meant to be a generic notes app. It is a research memory system maintained incrementally by agents and LLMs:

- markdown-first
- agent-first
- Obsidian-friendly
- built for paper reading, topic maps, syntheses, and research ideas

## What This Repo Is

- a research-oriented wiki structure
- an operating protocol for agents
- scripts, templates, and lint that make LLM maintenance more reliable
- an Obsidian vault that can be opened directly

The core idea is not query-time retrieval alone. The system asks an LLM to compile research material into an evolving markdown wiki. In practice, that means maintaining:

- paper pages
- topic pages
- method pages
- benchmark pages
- people and lab pages
- your own ideas and syntheses

References:

- [Karpathy gist: llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [qmd, referenced by Karpathy in the gist](https://github.com/tobi/qmd)

## Repository Layout

```text
research-wiki/
├── AGENTS.md
├── README.md
├── raw/                  # archived source material; the canonical source layer
│   ├── papers/           # archived paper-like sources after ingest
│   └── sources/          # archived non-paper sources after ingest
├── inbox/                # pending material waiting for ingest
├── scripts/
│   ├── rebuild_index.py  # rebuilds wiki/index.md from wiki pages
│   ├── lint_wiki.py      # checks links, orphans, kinds, and frontmatter
│   ├── create_page.py    # creates a new wiki page from a template
│   ├── create_inbox.py   # creates a structured inbox item
│   ├── ingest_inbox.py   # turns an inbox item into a first-pass wiki page scaffold
│   ├── inbox_status.py   # shows pending inbox items
│   └── query_wiki.py     # generates an agent-facing context pack
├── templates/            # templates for new pages
└── wiki/
    ├── index.md
    ├── log.md
    ├── overview.md
    ├── sources/
    ├── papers/
    ├── topics/
    ├── methods/
    ├── benchmarks/
    ├── people/
    ├── ideas/
    └── syntheses/
```

## What It Is Good For

This version is especially useful if you:

- read many papers and need durable organization
- want literature review support instead of isolated paper summaries
- compare methods within a topic over time
- want to preserve your own questions, judgments, and research ideas
- expect to reuse notes for meetings, presentations, surveys, and proposals

## Basic Usage

1. Put new material into `inbox/` first: papers, blog posts, meeting notes, screenshots with descriptions, and similar sources.
2. Check pending items with `python3 scripts/inbox_status.py`.
3. Create pages directly from templates when needed:

```bash
python3 scripts/create_page.py paper "A Paper Title" --year 2026
python3 scripts/create_page.py topic "Embodied Planning"
python3 scripts/create_page.py idea "Can WAM pretraining help VLA?"
```

4. Or create a structured inbox item first:

```bash
python3 scripts/create_inbox.py "A new paper to read" --source-type paper --link "https://arxiv.org/abs/xxxx.xxxxx"
```

5. Turn a structured inbox item into an archived source plus a first-pass page scaffold:

```bash
python3 scripts/ingest_inbox.py "2026-04-06-a-new-paper-to-read.md" --year 2026
```

6. Open Codex / Claude Code / Openclaw and ask it to ingest or update pages following [AGENTS.md](./AGENTS.md).
7. Before answering a question or editing related pages, generate a context pack for the agent:

```bash
python3 scripts/query_wiki.py "world action model"
python3 scripts/query_wiki.py "robotics foundation model" --kind topic
```

8. After ingest, the item should no longer live in `inbox/`; it should now exist under `raw/`.
9. Keep the wiki healthy:

```bash
python3 scripts/inbox_status.py
python3 scripts/rebuild_index.py
python3 scripts/lint_wiki.py
```

10. Review [wiki/index.md](./wiki/index.md) and [wiki/log.md](./wiki/log.md).

## Recommended Research Workflow

- Browse `wiki/` in Obsidian or any markdown editor.
- Ingest one source at a time.
- Treat `inbox/` as the queue and `raw/` as the archive.
- After each ingest, ask the agent to:
  - check `python3 scripts/inbox_status.py`
  - use `python3 scripts/ingest_inbox.py` if the source already exists as a structured inbox item
  - make sure the source lands in `raw/` and leaves `inbox/`
  - use `python3 scripts/query_wiki.py "<query>"` before question-answering work
  - update `papers/` or `sources/`
  - update related `topics/`, `methods/`, `benchmarks/`, and `people/`
  - update `ideas/` if the source produces a reusable question or direction
  - update `overview.md`
  - append to `log.md`
  - run lint

## Page Types

- `papers/`: structured pages for individual papers
- `topics/`: research topics such as `multimodal-robotics` or `world-models`
- `methods/`: method families such as `diffusion-policy` or `transformer-backbone`
- `benchmarks/`: datasets, metrics, and evaluation protocols
- `people/`: authors, labs, and organizations
- `ideas/`: your questions, hypotheses, directions, and experiment ideas
- `syntheses/`: weekly summaries, review notes, and reading digests
- `sources/`: non-paper material such as blogs, talks, podcasts, and gists

## Obsidian

This repository can be opened directly as an Obsidian vault.

- The recommended landing page is [VAULT.md](./VAULT.md).
- `.obsidian/` includes a lightweight baseline configuration:
  - the template folder points to `templates/`
  - new notes default to `inbox/`
  - attachments default to `raw/assets/`
  - a small CSS snippet improves readability and scanning
- `.obsidian/workspace.json` stays ignored so local window layout does not leak into the repository
