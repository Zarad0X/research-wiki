# Research Wiki Starter

这是一个把 Karpathy 最近提出的 `LLM Wiki` 模式，改造成更适合 `computer science / robotics` 研究场景的 starter。

它的定位不是一个“笔记 app”，而是一个给 agent / LLM 持续维护的 research memory system：

- markdown-first
- agent-first
- Obsidian-friendly
- 适合论文阅读、topic map、synthesis、research ideas

## What This Repo Is

- 一个研究型 wiki 目录结构
- 一套给 agent 用的维护协议
- 一组让 LLM 更稳定读写的脚本、模板和 lint
- 一个可直接打开的 Obsidian vault

建议放置位置：

- 以后统一把项目建在 `~/workspace/<project-name>`
- 这个 starter 推荐路径：`~/workspace/research-wiki`
- 文档内部尽量使用相对路径，避免仓库搬家时还要改链接

时间线：

- 2026-04-02：Karpathy 在 X 提到他最近很常用的一种工作方式，是让 LLM 帮自己维护研究主题的个人知识库。
- 2026-04-04：他发布了 `llm-wiki.md` gist，把这套模式写成一份可以直接丢给 agent 的 idea file。

核心不是“每次提问都去原始文档里现检索现拼接”，而是先让 LLM 把知识编译成一套持续演化的 markdown wiki。对研究场景来说，这意味着你不只是存论文摘要，而是在持续维护：

- paper 页面
- topic 页面
- method 页面
- benchmark 页面
- people/lab 页面
- 自己的 ideas 和 syntheses

参考：

- [Karpathy gist: llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [Karpathy 在 gist 中提到的 qmd](https://github.com/tobi/qmd)

## 目录结构

```text
research-wiki/
├── AGENTS.md
├── README.md
├── raw/                  # 原始资料，只读
├── inbox/                # 待处理来源
├── scripts/
│   ├── rebuild_index.py  # 从 wiki 页面重建 index.md
│   ├── lint_wiki.py      # 检查链接、孤儿页、kind 和 frontmatter
│   ├── create_page.py    # 用模板快速创建新页面
│   ├── create_inbox.py   # 创建结构化 inbox 条目
│   ├── inbox_status.py   # 查看 inbox 待处理条目
│   └── query_wiki.py     # 生成给 agent 用的查询上下文包
├── templates/            # 新建页面模板
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

## 适合什么场景

这个版本更适合：

- 读很多论文，需要长期整理
- 想做 literature review，而不是只记单篇摘要
- 需要对同一 topic 下的方法做横向比较
- 需要沉淀自己的问题、判断和研究想法
- 以后要复用到组会、pre、survey、开题、proposal

## 你现在可以怎么用

1. 把网页、论文、会议记录、截图描述等先放到 `inbox/`。
2. 用 `python3 scripts/inbox_status.py` 看当前待处理条目。
3. 需要时先用模板建页：

```bash
python3 scripts/create_page.py paper "A Paper Title" --year 2026
python3 scripts/create_page.py topic "Embodied Planning"
python3 scripts/create_page.py idea "Can WAM pretraining help VLA?"
```

4. 也可以先建一个结构化 inbox 条目：

```bash
python3 scripts/create_inbox.py "A new paper to read" --source-type paper --link "https://arxiv.org/abs/xxxx.xxxxx"
```

5. 打开 Codex，直接让它按 [AGENTS.md](./AGENTS.md) 规则 ingest 一个 source。
6. 查询已有知识时，先给 agent 一份上下文包：

```bash
python3 scripts/query_wiki.py "world action model"
python3 scripts/query_wiki.py "robotics foundation model" --kind topic
```

7. 运行：

```bash
python3 scripts/inbox_status.py
python3 scripts/rebuild_index.py
python3 scripts/lint_wiki.py
```

8. 在 [wiki/index.md](./wiki/index.md) 和 [wiki/log.md](./wiki/log.md) 里看是否健康。

## 推荐的研究工作流

- 用 Obsidian 或任何 markdown 编辑器浏览 `wiki/`
- 每次只 ingest 一个 source
- 每次 ingest 后都要求 agent：
  - 先看 `python3 scripts/inbox_status.py`
  - 如果是在回答问题，先看 `python3 scripts/query_wiki.py "<query>"`
  - 更新 `papers/` 或 `sources/` 页面
  - 更新相关 `topics/`、`methods/`、`benchmarks/`、`people/`
  - 如果有启发，更新 `ideas/`
  - 更新 `overview.md`
  - 追加 `log.md`
  - 运行 lint

## 推荐的页面类型

- `papers/`：单篇论文的结构化页面
- `topics/`：研究主题，比如 `multimodal-robotics`、`world-models`
- `methods/`：方法范式，比如 `diffusion-policy`、`transformer-backbone`
- `benchmarks/`：数据集、指标、评测 protocol
- `people/`：作者、实验室、机构
- `ideas/`：你的问题、假设、研究方向、实验想法
- `syntheses/`：每周总结、专题综述、reading digest
- `sources/`：非 paper 来源，比如 blog、talk、podcast、gist

## 系统能力

目前这套 wiki 自带几项很实用的基础设施：

- `create_page.py`：按模板快速建页，避免每次手写 frontmatter 和章节骨架
- `create_inbox.py`：把待处理资料先写成结构化 inbox 条目
- `inbox_status.py`：查看 `inbox/` 里有哪些待处理资料
- `query_wiki.py`：生成一个给 agent 用的查询结果包，告诉它应该优先读哪些页面
- `rebuild_index.py`：自动重建索引，并显示每个 section 的页面数量
- `lint_wiki.py`：除了断链，还会检查重复标题、非法 `kind`、目录与 `kind` 不匹配、日期格式、`source_count` 和关键 section 是否缺失

## Obsidian 适配

这个仓库现在可以直接作为一个 Obsidian vault 打开。

- vault 起始页可以用根目录下的 [VAULT.md](./VAULT.md)
- `.obsidian/` 已经补了基础配置：
  - 模板目录指向 `templates/`
  - 新建笔记默认进入 `inbox/`
  - 附件默认进入 `raw/assets/`
  - 启用一个很轻的 CSS snippet，让阅读和扫描更舒服
- `.obsidian/workspace.json` 仍然保持忽略，这样不会把你本地窗口布局硬写进仓库

推荐打开方式：

1. 在 Obsidian 里选择 `Open folder as vault`
2. 选中 `~/workspace/research-wiki`
3. 打开 [VAULT.md](./VAULT.md)
4. 之后主要在 Obsidian 浏览、在终端和 agent 里维护

## 为什么这个 starter 还是“轻”的

Karpathy 的原始想法里明确提到：在中小规模时，`index.md` 就足够支撑查找，不必一开始就接向量数据库。这个 starter 先把最重要的“持续维护的知识编译层”搭起来，等页数和 source 数量上去，再考虑：

- 接 `qmd`
- 增加 provenance / hash 校验
- 引入自动化批处理
- 为 query 输出 slides / reports / charts

## 建议你接下来先做的主题

建议先围绕一个明确 topic 开始，不要一开始把整个 CS 都装进去。例如：

- `multimodal-robotics`
- `vision-language-models`
- `diffusion-policy`
- `embodied-agents`
- `code-agents`

主题越窄，前 20 个 source 越容易形成真正有用的 wiki。
