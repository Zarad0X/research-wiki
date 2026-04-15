---
title: AI and Robotics Data
kind: topic
summary: A topic page about data history, scaling constraints, and recipe design for AI and robotics systems.
status: active
source_count: 5
updated: 2026-04-08
---

# AI and Robotics Data

## Summary

`AI and robotics data` 这个 topic 关心的不只是“数据量够不够大”，而是数据的历史来源、行业结构、金字塔分层、瓶颈位置，以及最后怎样被组织成真正有用的训练 recipe。对机器人基础模型来说，这条线尤其关键，因为 robotics 往往比 NLP/CV 更缺大规模、稳定、可复用的数据配方。

## Story Arc

- 在传统 ML 阶段，数据更像任务特定资产
- foundation model 阶段，数据开始变成能力边界的主要决定因素之一
- 对 LLM 来说，公开互联网文本已经越来越接近高质量数据瓶颈
- 对 robotics 来说，数据机会仍然很大，但关键不只是数量，而是采集、分层、融合与后训练 recipe
- 最近像 [[2025-taste-rob]] 这样的工作又补了一层：有些关键数据不是直接收集 policy demonstration，而是先生成更 task-aligned 的 hand-object interaction video
- 像 [[2025-object-centric-3d-motion-field]] 这样的工作则从另一侧补上：即使有 human video，关键也在于怎样从视频里提纯出真正可用于控制的动作表示
- `GEN-1` 这条线又把问题推进了一步：如果 Generalist 的 claim 成立，那么大规模 wearable human interaction data 不只是 cheap pretraining substitute，而可能本身就是 robotics scaling 的主燃料之一

## Key Questions

- AI data 与 robotics data 的主要差别到底是什么
- 哪些数据是真正稀缺的：通用 coverage、专家 demonstrations、失败恢复数据，还是 post-training 数据
- “pyramid structure” 应该怎样理解：是按规模、质量、成本，还是按监督信号层级来分
- 当模型变强后，数据 recipe 的价值会不会超过单一 architecture 改进

## Important Papers

- [[2024-openvla]]
- [[2024-pi-0]]
- [[xie-chen-data-survey-history-landscape-pyramid-structure-and-recipes-for-ai-and-robotics-data]]
- [[2025-taste-rob]]
- [[2025-object-centric-3d-motion-field]]
- [[gen-1-scaling-embodied-foundation-models-to-mastery]]

## Open Questions

- LLM data 墙和 robotics data 红利之间的差距还能持续多久
- robotics data 的真正瓶颈在采集成本、标注方式、 embodiment 多样性，还是 evaluation
- 未来最重要的是更多 raw data，还是更好的 data mixture 和 post-training recipe
- 任务导向的视频生成数据会不会变成 imitation learning 的中间层，而不是只是可视化 demo
- 从 human video 学机器人时，真正的瓶颈会不会越来越落在 action representation，而不是数据量本身
- wearable human interaction data 是否真的能在更广任务上系统性替代大规模 robot teleoperation pretraining

## Connections

- [[xie-chen-data-survey-history-landscape-pyramid-structure-and-recipes-for-ai-and-robotics-data]]
- [[representation-learning]]
- [[vision-language-action-models]]
- [[world-models]]
- [[2025-taste-rob]]
- [[2025-object-centric-3d-motion-field]]
- [[gen-1-scaling-embodied-foundation-models-to-mastery]]
- [[generalist-ai]]
- [[xiaoguang-han]]
- [[robot-foundation-models-seminar-sergey-levine-2026-03-26]]
- [[literature-review]]
- [[a-7-hour-marathon-interview-with-saining-xie-world-models-ami-labs-yann-lecun-fei-fei-li-and-42]]

## Sources

- [[xie-chen-data-survey-history-landscape-pyramid-structure-and-recipes-for-ai-and-robotics-data]]
- [[a-7-hour-marathon-interview-with-saining-xie-world-models-ami-labs-yann-lecun-fei-fei-li-and-42]]
- [[2025-taste-rob]]
- [[2025-object-centric-3d-motion-field]]
- [[gen-1-scaling-embodied-foundation-models-to-mastery]]
