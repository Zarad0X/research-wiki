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

## [2026-04-07] ingest | source from inbox

- Archived the source into `raw/sources/2026-04-07-robotic-foundation-models-sergey-levine-talk.md`.
- Created `[[robotic-foundation-models-sergey-levine-talk]]` from the archived source.
- Added `[[sergey-levine]]` and connected the talk back into VLA, world models, and overview.
- Rebuilt `wiki/index.md` and ran lint after the ingest scaffold.

## [2026-04-07] ingest | source from inbox

- Archived the source into `raw/sources/2026-04-07-robot-foundation-models-seminar-sergey-levine-2026-03-26.md`.
- Created `[[robot-foundation-models-seminar-sergey-levine-2026-03-26]]` from the archived source.
- Connected the seminar back into `[[2024-pi-0]]`, `[[vision-language-action-models]]`, `[[sergey-levine]]`, and `[[overview]]`.
- Rebuilt `wiki/index.md` and ran lint after the ingest scaffold.

## [2026-04-07] ingest | source from inbox

- Archived the source into `raw/sources/2026-04-07-xie-chen-data-survey-history-landscape-pyramid-structure-and-recipes-for-ai-and-robotics-data.md`.
- Created `[[xie-chen-data-survey-history-landscape-pyramid-structure-and-recipes-for-ai-and-robotics-data]]` from the archived source.
- Added `[[ai-and-robotics-data]]` as a topic page for the data pillar and connected it back into overview.
- Rebuilt `wiki/index.md` and ran lint after the ingest scaffold.

## [2026-04-07] ingest | source from inbox

- Archived the source into `raw/sources/2026-04-07-a-7-hour-marathon-interview-with-saining-xie-world-models-ami-labs-yann-lecun-fei-fei-li-and-42.md`.
- Created `[[a-7-hour-marathon-interview-with-saining-xie-world-models-ami-labs-yann-lecun-fei-fei-li-and-42]]` from the archived source.
- Added `[[saining-xie]]` and connected the interview into `[[world-models]]`, `[[ai-and-robotics-data]]`, and `[[overview]]`.
- Rebuilt `wiki/index.md` and ran lint after the ingest scaffold.

## [2026-04-07] expand | Saining Xie taste cluster

- Archived `Saining Xie homepage` into `raw/sources/2026-04-07-saining-xie-homepage.md`.
- Added `[[saining-xie-homepage]]` as a first-party source for Saining Xie's self-framing, representative works, and world-model ambition.
- Expanded `[[saining-xie]]` from a thin person page into a page about recurring research taste and representative works.
- Filled in `[[representation-learning]]` and `[[saining-xie-research-taste-and-representative-works]]` to capture the representation-learning throughline and why his work often feels elegant.
- Rebuilt `wiki/index.md` and ran lint after the expansion.

## [2026-04-07] expand | Saining Xie representative papers

- Added `[[2017-resnext]]`, `[[2020-moco]]`, `[[2022-mae]]`, `[[2022-convnext]]`, and `[[2023-dit]]` as concrete anchor papers for the Saining Xie cluster.
- Updated `[[saining-xie]]`, `[[representation-learning]]`, `[[saining-xie-research-taste-and-representative-works]]`, and `[[overview]]` so the taste discussion now points to specific works instead of only high-level commentary.
- Rebuilt `wiki/index.md` and ran lint after the paper expansion.

## [2026-04-07] ingest | source from inbox

- Archived the source into `raw/sources/2026-04-07-saining-xie-homepage.md`.
- Created `[[saining-xie-homepage]]` from the archived source.
- Rebuilt `wiki/index.md` and ran lint after the ingest scaffold.
