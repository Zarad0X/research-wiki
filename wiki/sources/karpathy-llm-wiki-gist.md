---
title: Karpathy - llm-wiki gist
kind: source
summary: Karpathy's April 4, 2026 gist that describes the LLM Wiki pattern as a persistent, interlinked markdown knowledge base maintained by an LLM.
status: active
source_count: 1
updated: 2026-04-06
---

# Karpathy - llm-wiki gist

## Source Metadata

- Author: Andrej Karpathy
- Date: 2026-04-04
- URL: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## Summary

这份 gist 给出的核心主张是：不要只把 LLM 用成 query-time RAG，而要让它持续维护一套持久化的 wiki。新 source 到来时，LLM 应该阅读它、写摘要、更新相关页面、处理冲突，并把结果整合进现有知识结构。

## Key Takeaways

- wiki 是一个持续累积的 artifact
- `index.md` 在中等规模下可以代替更复杂的检索基础设施
- `log.md` 可以作为 append-only 时间线
- 高价值 query 结果也应该回写成页面
- 当规模变大时，可以增加 CLI 搜索工具，比如 `qmd`

## Implications

- 这更像“knowledge compilation”而不是临时问答
- wiki 文件夹本身可以作为 git 仓库进行版本管理
- 维护协议很重要，因此需要 `AGENTS.md`
- 研究场景可以把它扩展成 paper/topic/method/idea/synthesis 的知识结构

## Connections

- [[llm-wiki]]
- [[andrej-karpathy]]
- [[overview]]
- [[literature-review]]

## Sources

- External source: Karpathy gist URL above
