# Wiki Log

## [2026-04-06] bootstrap | initialize starter

- Created the base `raw/`, `inbox/`, and `wiki/` structure.
- Added `AGENTS.md`, `rebuild_index.py`, and `lint_wiki.py`.
- Seeded the wiki with the Karpathy gist as the first source and a concept page for `llm-wiki`.

## [2026-04-06] refactor | reshape into research wiki

- Reframed the starter around `computer science / robotics` research workflows.
- Replaced `concepts/` and `entities/` with more research-native sections such as `papers/`, `topics/`, `methods/`, `benchmarks/`, `people/`, `ideas/`, and `syntheses/`.
- Updated the maintainer protocol so future ingest can produce paper pages, topic maps, benchmark notes, and personal research ideas.

## [2026-04-06] ingest | RT-2, OpenVLA, pi_0

- Added three first-pass paper pages for `RT-2`, `OpenVLA`, and `pi_0`.
- Added a topic page for `Vision-Language-Action Models`.
- Added a synthesis page comparing the three papers as milestones in the VLA trajectory.
- Updated `overview.md` to reflect the first real research cluster in the wiki.

## [2026-04-06] ingest | World Models, Genie, DreamZero, LingBot-World

- Expanded the paper template in `AGENTS.md` to include `Story / Setting`, `Why This Exists`, `Related Work`, `First Principles`, and `Core Architecture`.
- Added four first-pass paper pages for `World Models`, `Genie`, `DreamZero`, and `LingBot-World`.
- Added a topic page for `World Models` and a synthesis page comparing the four papers as distinct phases of the research trajectory.
- Updated `overview.md` so the wiki now tracks both a VLA cluster and a world-model cluster.

## [2026-04-06] system | improve wiki tooling

- Added `templates/` plus `scripts/create_page.py` so new pages can be created from consistent scaffolds.
- Added `scripts/inbox_status.py` for a lightweight `inbox/` workflow.
- Upgraded `rebuild_index.py` to show section counts and page titles in the index.
- Upgraded `lint_wiki.py` to validate `kind`, detect directory-kind mismatches, validate dates and `source_count`, and catch duplicate slugs.

## [2026-04-06] system | strengthen agent harness

- Added `scripts/query_wiki.py` so agents can produce a ranked context pack before answering or editing.
- Added `scripts/create_inbox.py` plus `templates/inbox-item.md` so inbox entries can be structured instead of ad hoc.
- Extended `inbox_status.py` to read markdown frontmatter for status and priority.
- Extended `lint_wiki.py` to check required sections so pages stay patch-friendly for LLM maintenance.

## [2026-04-06] ingest | paper from inbox

- Archived the source into `raw/papers/2026-04-06-trellis.md`.
- Created `[[2024-trellis]]` from the archived source.
- Added `[[3d-generation]]` as the seed topic page for this new line.
- Rebuilt `wiki/index.md` and ran lint after the ingest scaffold.
