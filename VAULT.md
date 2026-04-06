# Vault Home

这是给 Obsidian 打开的起始页。底层 source of truth 仍然是 markdown 文件本身，Obsidian 只是更舒服的人类浏览层。

## Quick Links

- [[overview]]
- [[index]]
- [[log]]
- [[literature-review]]
- [[vision-language-action-models]]
- [[world-models]]
- [[research-questions]]

## Fast Workflow

1. 把新资料先放进 `inbox/`
2. 在终端运行 `python3 scripts/inbox_status.py`
3. 如果需要，先建结构化条目：
   `python3 scripts/create_inbox.py "A new paper to read" --source-type paper`
4. 如果需要，先建 wiki 页面骨架：
   `python3 scripts/create_page.py paper "A Paper Title" --year 2026`
5. 让 agent ingest / update
6. 最后运行：
   `python3 scripts/rebuild_index.py`
   `python3 scripts/lint_wiki.py`

## Obsidian Notes

- 模板目录已经指向 `templates/`
- 新建笔记默认进 `inbox/`
- 附件默认进 `raw/assets/`
- 这个 vault 默认更适合阅读 mode + Live Preview

## Suggested Starting Points

- 想按主题读：从 [[index]] 和 [[overview]] 开始
- 想追某一条研究线：直接进 [[vision-language-action-models]] 或 [[world-models]]
- 想记录自己的想法：先看 [[research-questions]]
