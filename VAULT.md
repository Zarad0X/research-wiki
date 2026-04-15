# Vault Home

This is the recommended landing page for opening the repository in Obsidian. The source of truth is still the markdown repository itself; Obsidian is simply the most convenient human-facing reading layer.

## Start Here

- [[now]]
- [[overview]]
- [[research-questions]]
- [[working-theses]]
- [[human-video-to-robot-learning]]

## Quick Links

- [[index]]
- [[log]]
- [[research-taste]]
- [[vision-language-action-models]]
- [[world-models]]
- [[ai-and-robotics-data]]
- [[articulated-object-reconstruction-and-hoi]]

## Fast Workflow

1. Put new material into `inbox/`.
2. Run `python3 scripts/inbox_status.py`.
3. If needed, create a structured inbox item:
   `python3 scripts/create_inbox.py "A new paper to read" --source-type paper`
4. If needed, create a wiki page scaffold:
   `python3 scripts/create_page.py paper "A Paper Title" --year 2026`
5. Ask your agent to ingest or update.
6. Make sure the result does not stop at `papers/` or `sources/`:
   - update a `topic` if the map changed
   - update a `question` or `thesis` if your judgment changed
   - update a `program` if the source affects an active research line
   - update a `review` if the comparison has become reusable
7. Finish with:
   `python3 scripts/rebuild_index.py`
   `python3 scripts/lint_wiki.py`

## Obsidian Notes

- The template folder already points to `templates/`.
- New notes default to `inbox/`.
- Attachments default to `raw/assets/`.
- The vault is tuned for reading mode plus Live Preview.

## Suggested Starting Points

- To see what currently matters, start with [[now]] and [[overview]].
- To see active uncertainties and bets, read [[research-questions]] and [[working-theses]].
- To follow a live research agenda, jump into [[human-video-to-robot-learning]].
- To browse the full archive, use [[index]].
