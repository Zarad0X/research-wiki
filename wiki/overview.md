---
title: Overview
kind: overview
summary: Current map of the wiki and the operating thesis for this research knowledge base.
status: active
source_count: 19
updated: 2026-04-07
---

# Overview

## Summary

这个库当前围绕一个核心命题展开：相比每次 query 都重新从原始文档中检索和拼装，先让 LLM 把研究知识持续编译进一套 interlinked markdown wiki，会得到更强的复利效应。当前已经形成两个较清晰的小研究簇：一组是 VLA，另一组是 world models / WAM；另外开始长出一条新的 `3D generation` 线，目前以 `TRELLIS` 作为种子论文。最近又补进了两条很有价值的 Sergey Levine 讲座来源：一条是 DAI 2024 的 `Robotic Foundation Models` keynote，另一条是 2026-03-26 的 seminar，后者更具体地覆盖了 `pi_0` 之后的 reasoning、数据策略和 RL post-training 发展。现在又开始长出一条 `AI and robotics data` 线，用来承接模型之外的数据配方问题。同时，围绕 Saining Xie 已经形成一个更像“研究 taste cluster”的小簇：不仅有长访谈、主页 source、`representation learning` topic 和 taste synthesis，还补进了 `ResNeXt`、`MoCo`、`MAE`、`ConvNeXt`、`DiT` 这组代表作作为具体锚点。

## Working Thesis

- `raw/` 保存原始事实来源
- `wiki/` 保存经 LLM 维护的结构化研究知识
- 高价值 query 结果应该继续写回 wiki，而不是丢在聊天历史里
- 单篇论文、topic map、method comparison、benchmark notes、research ideas 都应成为长期页面
- 研究脉络应尽量从“单篇 paper 摘要”升级到“paper 之间的关系图”

## Current Pages

- 方法页：[[llm-wiki]]
- 人物页：[[andrej-karpathy]]、[[sergey-levine]]
- 新的人物页：[[saining-xie]]
- 首个来源页：[[karpathy-llm-wiki-gist]]
- 新的讲座来源页：[[robotic-foundation-models-sergey-levine-talk]]
- 新的 seminar 来源页：[[robot-foundation-models-seminar-sergey-levine-2026-03-26]]
- 新的数据播客来源页：[[xie-chen-data-survey-history-landscape-pyramid-structure-and-recipes-for-ai-and-robotics-data]]
- 新的长访谈来源页：[[a-7-hour-marathon-interview-with-saining-xie-world-models-ami-labs-yann-lecun-fei-fei-li-and-42]]
- 新的主页来源页：[[saining-xie-homepage]]
- VLA topic 页：[[vision-language-action-models]]
- 第一批论文页：[[2023-rt-2]]、[[2024-openvla]]、[[2024-pi-0]]
- 首个对比 synthesis：[[rt-2-openvla-pi-0]]
- world model topic 页：[[world-models]]
- 第二批论文页：[[2018-world-models]]、[[2024-genie]]、[[2026-dreamzero]]、[[2026-lingbot-world]]
- 第二个对比 synthesis：[[world-models-genie-dreamzero-lingbot-world]]
- 新的 3D generation topic 页：[[3d-generation]]
- 新的 data topic 页：[[ai-and-robotics-data]]
- 新的 representation topic 页：[[representation-learning]]
- 新增论文页：[[2024-trellis]]
- 新增代表作 paper 页：[[2017-resnext]]、[[2020-moco]]、[[2022-mae]]、[[2022-convnext]]、[[2023-dit]]
- 新的 taste synthesis：[[saining-xie-research-taste-and-representative-works]]
- topic 页面：[[literature-review]]
- idea 页面：[[research-questions]]

## Open Questions

- 什么时候需要从 `index.md` 升级到专用搜索工具
- 如何给 paper 页面增加更强的 provenance
- 什么时候应该把 query 结果沉淀成 `synthesis` 或 `idea`
- 如何把日常阅读节奏转成每周和每月的研究回顾
- 当 topic 刚起步时，什么时机值得从“单篇种子 paper”升级到一个真正的 cluster

## Sources

- [[karpathy-llm-wiki-gist]]
- [[2023-rt-2]]
- [[2024-openvla]]
- [[2024-pi-0]]
- [[2018-world-models]]
- [[2024-genie]]
- [[2026-dreamzero]]
- [[2026-lingbot-world]]
- [[2024-trellis]]
- [[robotic-foundation-models-sergey-levine-talk]]
- [[robot-foundation-models-seminar-sergey-levine-2026-03-26]]
- [[xie-chen-data-survey-history-landscape-pyramid-structure-and-recipes-for-ai-and-robotics-data]]
- [[a-7-hour-marathon-interview-with-saining-xie-world-models-ami-labs-yann-lecun-fei-fei-li-and-42]]
- [[saining-xie-homepage]]
- [[2017-resnext]]
- [[2020-moco]]
- [[2022-mae]]
- [[2022-convnext]]
- [[2023-dit]]
