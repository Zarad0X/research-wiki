# Vault Home

This is the recommended landing page for opening the repository in Obsidian. The source of truth is still the markdown repository itself; Obsidian is simply the most convenient human-facing reading layer.

## Quick Links

- [[overview]]
- [[index]]
- [[log]]
- [[literature-review]]
- [[vision-language-action-models]]
- [[world-models]]
- [[research-questions]]

## Fast Workflow

1. Put new material into `inbox/`.
2. Run `python3 scripts/inbox_status.py`.
3. If needed, create a structured inbox item:
   `python3 scripts/create_inbox.py "A new paper to read" --source-type paper`
4. If needed, create a wiki page scaffold:
   `python3 scripts/create_page.py paper "A Paper Title" --year 2026`
5. Ask your agent to ingest or update.
6. Finish with:
   `python3 scripts/rebuild_index.py`
   `python3 scripts/lint_wiki.py`

## Obsidian Notes

- The template folder already points to `templates/`.
- New notes default to `inbox/`.
- Attachments default to `raw/assets/`.
- The vault is tuned for reading mode plus Live Preview.

## Suggested Starting Points

- To read by topic, start with [[index]] and [[overview]].
- To follow a research line, jump into [[vision-language-action-models]] or [[world-models]].
- To capture your own ideas, start with [[research-questions]].
