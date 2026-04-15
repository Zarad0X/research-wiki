---
title: 3D Generation
kind: topic
summary: A topic page for generative 3D asset creation, focusing on representation choice, conditioning, and output flexibility, while increasingly touching the broader question of 3D representations as reusable infrastructure.
status: active
source_count: 7
updated: 2026-04-08
---

# 3D Generation

## Summary

`3D generation` 这条线关心的不只是“生成一个看起来像 3D 的东西”，而是如何在表示、条件控制、渲染质量、编辑能力和输出格式之间找到可扩展的平衡。当前这条 topic 已经不再只是 `TRELLIS` 一个点，而是开始能和另一条更偏 3D 视觉的路线接起来，比如 Xiaoguang Han 老师近年的 [[2024-richdreamer]]、[[2024-ipod]]、[[2025-reconviagen]]、[[2026-texspot]] 和 [[2026-motioncrafter]]，以及更偏 `geometry foundation model` 取向的 [[2025-vggt]]。这也让这页不再只是在谈生成资产，而是开始碰到“3D 表示能否成为更广泛基础设施”的问题。

## Story Arc

- 早期 3D generation 经常围绕单一表示或单一任务组织
- 近期工作越来越强调统一 latent、跨模态条件和更实用的输出格式
- [[2024-trellis]] 可以看作是这条线里一个很典型的“先把表示做对，再谈生成和编辑”的版本
- Han 老师组的最近工作则更像从另一侧补进来：[[2024-richdreamer]] 强调 normal / depth 先验，[[2024-ipod]] 强调 generalizable reconstruction
- [[2025-vggt]] 又从多视图几何这一侧补了一块：如果真实场景 geometry 也能被大模型统一前馈预测，那么 generation / reconstruction / geometry 之间的边界会进一步变薄
- `[[articulated-object-reconstruction-real2sim]]` 则把问题继续推进到 articulated setting：对 real2sim 来说，关键不再只是形状，而是 `part structure + joint model + simulator-ready asset`
- [[2026-articulation-in-motion]] 又把 articulated 这条线往 `motion-first` 方向推了一步：先从 interaction video 里做 dynamic-static disentanglement 和 mobility analysis，再恢复 digital replica
- 现在还单独拉出 `[[articulated-object-reconstruction-and-hoi]]` 这一类 topic，用来承接 articulated structure 和 hand-object interaction 之间越来越紧的耦合
- 到 2025-2026，这条线进一步细化成：
  - generation 帮 reconstruction：[[2025-reconviagen]]
  - texture-level enhancement：[[2026-texspot]]
  - dynamic 4D geometry + motion：[[2026-motioncrafter]]

## Key Questions

- 哪种 3D 表示最适合作为大规模生成模型的中间层
- text-to-3D、image-to-3D 和 local editing 能否共用同一底层表示
- 输出 flexibility 和工程复杂度之间如何 trade off
- 这条线未来会更偏内容资产生成，还是更偏 3D understanding / embodied world modeling 的共用基础设施

## Important Papers

- [[2024-trellis]]
- [[2024-richdreamer]]
- [[2024-ipod]]
- [[2025-reconviagen]]
- [[2025-vggt]]
- [[2026-texspot]]
- [[2026-motioncrafter]]
- [[articulated-object-reconstruction-real2sim]]
- [[2026-articulation-in-motion]]
- [[articulated-object-reconstruction-and-hoi]]

## Open Questions

- `TRELLIS` 这种 unified latent 表示能否成为更广泛的 3D generation 基础模块
- `VGGT` 这种 geometry backbone 会不会和 3D generation latent 在未来合流
- 如果未来引入物理、交互和时间维度，当前的 3D asset latent 是否还够用
- 该如何把 3D generation 和 robotics / world model 社区更自然地接起来
- 从 Han 老师组最近的路线看，3D generation 和 generalizable reconstruction 会不会先在手物交互或机器人数据生成里汇合
- texture representation 和 4D dynamic representation 会不会成为下一轮更关键的中间层

## Connections

- [[2024-trellis]]
- [[2024-richdreamer]]
- [[2024-ipod]]
- [[2025-reconviagen]]
- [[2025-vggt]]
- [[2026-texspot]]
- [[2026-motioncrafter]]
- [[xiaoguang-han]]
- [[xiaoguang-han-recent-papers-2024-2025]]
- [[literature-review]]
- [[overview]]

## Sources

- [[2024-trellis]]
- [[2024-richdreamer]]
- [[2024-ipod]]
- [[2025-reconviagen]]
- [[2025-vggt]]
- [[2026-texspot]]
- [[2026-motioncrafter]]
