# Vault Home

This is the recommended landing page for opening the repository in Obsidian. The source of truth is still the markdown repository itself; Obsidian is simply the most convenient human-facing reading layer.

## Start Here

- In a populated personal branch, start from `wiki/now.md` and `wiki/overview.md`.
- In the clean framework branch, use this page plus `README.md` and `AGENTS.md` to understand the intended workflow.

## Quick Links

- [README.md](./README.md)
- [AGENTS.md](./AGENTS.md)
- `wiki/index.md`
- `wiki/log.md`
- `wiki/overview.md`
- `wiki/now.md`

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

- To see what currently matters in a populated personal wiki, start with `wiki/now.md` and `wiki/overview.md`.
- To browse the full archive, use `wiki/index.md`.
- To understand the framework itself, start with `README.md` and `AGENTS.md`.
