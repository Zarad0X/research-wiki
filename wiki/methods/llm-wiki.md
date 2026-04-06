---
title: LLM Wiki
kind: method
summary: A pattern where an LLM incrementally compiles research materials into a persistent markdown wiki instead of relying only on query-time RAG.
status: active
source_count: 1
updated: 2026-04-06
---

# LLM Wiki

## Summary

LLM Wiki 是一种知识组织模式：把原始来源和最终问答之间，加入一层由 LLM 持续维护的 markdown wiki。对研究场景来说，它会随着 paper ingest、topic 对比和 query 回写不断变厚，而不是每次重新从零搜索、重新拼接。

## Core Difference From Plain RAG

- plain RAG：问题来了再去找 chunk
- LLM Wiki：先把知识整理成稳定页面，再围绕这些页面继续问答和输出

## Minimum Architecture

- `raw/`：原始来源
- `wiki/`：编译后的知识页
- `AGENTS.md`：维护协议

## Important Operations

- ingest：处理一个新 source，并更新多个页面
- query：优先从 wiki 回答，必要时把高价值结论写回 wiki
- lint：检查断链、孤儿页、冲突和缺页

## Why It Compounds

- cross-link 会被持续维护
- 新 source 会直接修订旧结论
- query 结果也能沉淀成新页面

## Connections

- [[andrej-karpathy]]
- [[karpathy-llm-wiki-gist]]
- [[overview]]
- [[literature-review]]
- [[research-questions]]

## Sources

- [[karpathy-llm-wiki-gist]]
