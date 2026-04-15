---
title: Working Theses
kind: thesis
summary: A page for current working theses about where the field is going, what matters, and what would change my mind.
status: active
source_count: 12
updated: 2026-04-15
---

# Working Theses

## Summary

这个页面用来放那些已经不只是 open question、但又还没有稳定到能写成最终结论的判断。它和 `research-questions` 的区别是：那边强调 decision panel，这边强调 **我现在到底已经更相信什么**。如果一个 thesis 连续被新论文强化，它就应该逐渐成为这个 wiki 的主视角之一。

## Thesis 1

### 下一阶段 embodied intelligence 的高杠杆更可能来自更好的中间表示和系统 recipe，而不只是更大的端到端模型

**Current lean**

我当前更倾向于：`representation + recipe + post-training + system integration` 的复合杠杆，会比单点模型改进更重要。这里的 `representation` 尤其重要，因为它决定了哪些数据和控制结构真正能被编译进模型。

**Why I think this**

- [[2025-vggt]] 把 geometry backbone 这件事重新拉回主舞台。
- [[2025-object-centric-3d-motion-field]] 说明 action representation 本身可能就是 robotics 泛化的瓶颈。
- [[gen-1-scaling-embodied-foundation-models-to-mastery]] 和 [[robot-foundation-models-seminar-sergey-levine-2026-03-26]] 都更像在讲完整 recipe，而不是单一 backbone。

**What would change my mind**

- 如果未来最强进展仍主要来自单一 backbone 替换，而不是更好的 representation / recipe / post-training 组合。
- 如果结构化中间表示在大规模真实系统里持续输给更粗暴的 end-to-end models。

## Thesis 2

### human-video-to-robot 这条线最后赢的关键，很可能不是视频更多，而是更好的 interaction-centric / object-centric action abstraction

**Current lean**

我现在更相信：对机器人来说，真正重要的不是把所有 human video 都吞进去，而是找到能保留对象关系、接触变化、可迁移运动结构的中间表示。

**Why I think this**

- [[2025-taste-rob]] 和 [[2025-object-centric-3d-motion-field]] 正好代表这条线的两侧：
  - 一个在造更 task-aligned 的交互视频
  - 一个在提纯更适合控制的动作表示
- `ArtHOI`、`AiM` 这类工作也在强化一个直觉：interaction cue 自身就是结构监督。

**What would change my mind**

- 出现强证据表明，大规模 raw human video 预训练本身已经足以稳定学出跨 embodiment 的动作抽象，而不需要额外结构中间层。

## Thesis 3

### articulated object reconstruction 不应该再被当成单独几何问题，而应该被放进 HOI / real2sim / manipulation 的闭环里看

**Current lean**

我现在更倾向于把 articulated reconstruction 看成一个 interaction problem，而不是静态 3D problem。真正高价值的输出是 simulator-ready articulated structure，而不是单次漂亮重建。

**Why I think this**

- [[2026-articulation-in-motion]] 说明 motion cue 本身可以长出 part decomposition。
- [[2026-articulated-reconstruction-transformer]] 说明 part slots + simulation-ready export 是一条很清楚的结构化路线。
- [[2026-arthoi]] 则说明只恢复 object 本身已经不够，hand-object coordination 也必须进系统。

**What would change my mind**

- 如果未来最强 real2sim pipeline 证明不需要明确 articulation structure，也能稳定做 manipulation 和 simulation transfer。

## Thesis 4

### VLA 和 world model / WAM 更像会融合，而不是简单替代

**Current lean**

我目前仍然更相信二者融合，而不是谁把谁吃掉。VLA 更像 control interface，world model 更像 predictive structure / planning substrate。

**Why I think this**

- [[2024-openvla]]、[[2024-pi-0]] 说明 VLA 仍是最清晰的 control interface。
- [[2026-dreamzero]]、[[2024-genie]]、[[2026-lingbot-world]] 则说明 predictive world modeling 正在向 policy substrate 靠拢。

**What would change my mind**

- 出现开放、稳定、可复现的 world-model-centric 主干，真实机器人上显著压过强 VLA baseline。

## How To Use This Page

- 这里只放已经有明确 `current lean` 的判断，不放纯 open questions。
- 每条 thesis 都要写什么会让我改主意，否则它就容易变成口号。
- 当某条 thesis 已经足够稳定且证据丰富，可以升级成单独 synthesis。

## Connections

- [[research-taste]]
- [[research-questions]]
- [[vision-language-action-models]]
- [[world-models]]
- [[ai-and-robotics-data]]
- [[articulated-object-reconstruction-and-hoi]]
- [[overview]]

## Sources

- [[2024-openvla]]
- [[2024-pi-0]]
- [[2024-genie]]
- [[2026-dreamzero]]
- [[2026-lingbot-world]]
- [[2025-vggt]]
- [[2025-object-centric-3d-motion-field]]
- [[2025-taste-rob]]
- [[2026-articulation-in-motion]]
- [[2026-articulated-reconstruction-transformer]]
- [[2026-arthoi]]
- [[gen-1-scaling-embodied-foundation-models-to-mastery]]
