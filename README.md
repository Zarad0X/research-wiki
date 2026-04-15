# Research Wiki

This repository is an independent implementation inspired by Andrej Karpathy's `llm-wiki` gist.

It is not meant to be a generic notes app. It is a research memory system maintained incrementally by agents and LLMs, with increasing emphasis on the repository owner's own questions, theses, programs, and judgments:

- markdown-first
- agent-first
- Obsidian-friendly
- built for evidence pages, map pages, judgment pages, and agenda pages

## Branch Model

This repo is designed to support a clean public framework branch and a local personal content branch:

- `main`: framework only, safe to push
- `personal`: your private research content, kept local by default

By default, `.gitignore` keeps new content under `wiki/`, `inbox/`, and archived `raw/` material out of `main`. If you want to version your private notes, do that on a local-only `personal` branch or in a separate private remote.

## What This Repo Is

- a research-oriented wiki structure
- an operating protocol for agents
- scripts, templates, and lint that make LLM maintenance more reliable
- an Obsidian vault that can be opened directly

The core idea is not query-time retrieval alone. The system asks an LLM to compile research material into an evolving markdown wiki. In practice, that means maintaining four layers:

- **Evidence layer**: archived source material, paper pages, source pages, people pages
- **Map layer**: topic, method, and benchmark pages that organize a field
- **Judgment layer**: active questions, working theses, review pages, and owner-facing syntheses
- **Agenda layer**: research programs and living dashboards that say what matters now

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
    ├── now.md            # current dashboard; usually local / personal
    ├── overview.md       # stable worldview page; usually local / personal
    ├── index.md          # generated index; usually local / personal
    ├── log.md            # ingest log; usually local / personal
    ├── questions/        # active research questions / decision panels
    ├── theses/           # current working beliefs and bets
    ├── programs/         # live research programs / agendas
    ├── reviews/          # evaluative owner-facing review pages
    ├── papers/
    ├── sources/
    ├── topics/
    ├── methods/
    ├── benchmarks/
    ├── people/
    ├── ideas/            # meta or uncategorized owner pages during transition
    └── syntheses/        # descriptive or mixed review-style syntheses during transition
```

Files such as `wiki/now.md`, `wiki/index.md`, `wiki/log.md`, and `wiki/overview.md` are expected to exist in a real working wiki, but they are not tracked on the clean framework branch by default.

## What It Is Good For

This version is especially useful if you:

- read many papers and need durable organization
- want literature review support instead of isolated paper summaries
- want your own current judgments to stay visible, not buried inside paper notes
- compare methods and research directions over time
- want to preserve questions, theses, program directions, and review-style conclusions
- expect to reuse notes for meetings, presentations, surveys, and proposals

## Basic Usage

1. Put new material into `inbox/` first: papers, blog posts, meeting notes, screenshots with descriptions, and similar sources.
2. Check pending items with `python3 scripts/inbox_status.py`.
3. Create pages directly from templates when needed:

```bash
python3 scripts/create_page.py paper "A Paper Title" --year 2026
python3 scripts/create_page.py question "Will VLA and WAM converge?"
python3 scripts/create_page.py thesis "Action representation is the real bottleneck"
python3 scripts/create_page.py program "Human Video to Robot Learning"
```

4. Or create a structured inbox item first:

```bash
python3 scripts/create_inbox.py "A new paper to read" --source-type paper --link "https://arxiv.org/abs/xxxx.xxxxx"
```

5. Turn a structured inbox item into an archived source plus a first-pass page scaffold:

```bash
python3 scripts/ingest_inbox.py "2026-04-06-a-new-paper-to-read.md" --year 2026
```

6. Open Claude Code / Codex / Openclaw and ask it to ingest or update pages following [AGENTS.md](./AGENTS.md).
7. Before answering a question or editing related pages, generate a context pack for the agent:

```bash
python3 scripts/query_wiki.py "world action model"
python3 scripts/query_wiki.py "human video robot" --kind program
```

8. After ingest, the item should no longer live in `inbox/`; it should now exist under `raw/`.
9. Keep the wiki healthy:

```bash
python3 scripts/inbox_status.py
python3 scripts/rebuild_index.py
python3 scripts/lint_wiki.py
```

10. Review the locally generated `wiki/now.md`, `wiki/overview.md`, and `wiki/index.md` if you are working on your personal branch.

## Recommended Research Workflow

- Start from `wiki/now.md` and `wiki/overview.md` to orient yourself before diving into the archive.
- Treat `inbox/` as the queue and `raw/` as the archive.
- Keep `papers/` and `sources/` as the evidence substrate, not the final output.
- After each important ingest, ask the agent to:
  - check `python3 scripts/inbox_status.py`
  - use `python3 scripts/ingest_inbox.py` if the source already exists as a structured inbox item
  - make sure the source lands in `raw/` and leaves `inbox/`
  - use `python3 scripts/query_wiki.py "<query>"` before question-answering work
  - update `papers/` or `sources/`
  - update related `topics/`, `methods/`, `benchmarks/`, and `people/`
  - update `questions/`, `theses/`, `programs/`, or `reviews/` if the source changes your live agenda
  - only use `ideas/` for meta pages or uncategorized owner notes during transition
  - update `now.md` and `overview.md` when priorities or worldview change
  - append to `log.md` when appropriate
  - run lint

## Page Types

- `questions/`: active research questions and decision panels
- `theses/`: current working beliefs, bets, and change-my-mind criteria
- `programs/`: live research lines that connect questions, evidence, and next reading priorities
- `reviews/`: evaluative review pages with owner-facing judgment
- `topics/`: research topics such as `multimodal-robotics` or `world-models`
- `methods/`: method families such as `diffusion-policy` or `transformer-backbone`
- `benchmarks/`: datasets, metrics, and evaluation protocols
- `papers/`: structured pages for individual papers
- `sources/`: non-paper material such as blogs, talks, podcasts, and gists
- `people/`: authors, labs, and organizations
- `ideas/`: meta owner pages or uncategorized judgment pages during the transition
- `syntheses/`: descriptive literature maps, reading digests, or mixed comparison pages during the transition

## Obsidian

This repository can be opened directly as an Obsidian vault.

- The recommended landing page is [VAULT.md](./VAULT.md).
- Within a populated personal branch, the human-facing starting points are usually `wiki/now.md` and `wiki/overview.md`.
- `.obsidian/` includes a lightweight baseline configuration:
  - the template folder points to `templates/`
  - new notes default to `inbox/`
  - attachments default to `raw/assets/`
  - a small CSS snippet improves readability and scanning
- `.obsidian/workspace.json` stays ignored so local window layout does not leak into the repository

## Personal Content Policy

- The public/framework branch should not track your personal wiki content.
- `wiki/`, `inbox/`, and archived `raw/` content are meant to live locally by default.
- If you want a versioned knowledge base, keep it on your local `personal` branch instead of pushing it to `origin/main`.
