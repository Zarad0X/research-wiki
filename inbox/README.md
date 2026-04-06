# Inbox

这里放还没正式 ingest 的资料。

可以把临时抓下来的网页、零散笔记、截图说明先放进来。等你准备好后，再让 agent 把它们整理进 `raw/` 或直接编译到 `wiki/`。

建议：

- 新来的资料先放这里，不要直接堆到 `raw/`
- 一份资料尽量一个文件或一个目录
- 文件名尽量包含日期或短标题
- 如果是 markdown，优先带 frontmatter：`title`、`source_type`、`status`、`priority`、`created`
- 用 `python3 scripts/inbox_status.py` 查看待处理条目
- 用 `python3 scripts/create_inbox.py "Title"` 快速创建结构化条目
- 完成 ingest 后，再决定是否移入 `raw/`
