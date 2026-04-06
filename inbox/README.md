# Inbox

Keep pending material here before it enters the archive.

Use this directory as a queue for new sources: links to read later, rough notes, pasted excerpts, and newly collected material. Once an item is ingested, it should leave `inbox/` and be archived under `raw/`.

Guidelines:

- Put newly collected material here before it reaches `raw/`.
- Prefer one file or one folder per source.
- Include a date or a short title in file names.
- For markdown items, prefer frontmatter with `title`, `source_type`, `status`, `priority`, and `created`.
- Use `python3 scripts/inbox_status.py` to inspect pending items.
- Use `python3 scripts/create_inbox.py "Title"` to create a structured entry quickly.
- Use `python3 scripts/ingest_inbox.py "<item>"` to archive the item into `raw/` and create its first-pass wiki scaffold.
