---
title: Articulated Object Reconstruction and HOI
kind: topic
summary: A topic page for articulated object reconstruction and hand-object interaction, focusing on how structure, motion, and interaction cues support real2sim and manipulation research.
status: active
source_count: 8
updated: 2026-04-15
---

# Articulated Object Reconstruction and HOI

## Summary

这个 topic 想承接的是一条很具体、也越来越重要的研究线：`articulated object reconstruction` 和 `HOI (hand-object interaction)` 不该再被看成两条完全分开的方向。对很多 real2sim、robot manipulation、interaction understanding 任务来说，手和物体之间的接触、驱动和相对运动，本身就是恢复 articulated structure 的关键信号；反过来，如果我们不知道 object 的 part decomposition、joint axis、mobility，很多 HOI cue 也很难被正确解释。

所以这条线最值得追的问题不是单独的“几何重建”或“视频理解”，而是：如何把 `part structure + mobility + interaction cue` 放在一个统一研究框架里看。最近这类工作大致在往三种方向长：

- `motion-first articulated analysis`：从 interaction / motion cue 中先长出 part decomposition 和 mobility
- `geometry-first articulated reconstruction`：先建立 canonical geometry 和 part structure，再做 kinematic decoding
- `task-oriented HOI data or generation`：为 manipulation 学习构造更对路的 hand-object interaction data
- `digital twin / real2sim asset building`：把 reconstruction 结果进一步变成 simulator-ready articulated asset

## Story Arc

- 早期 articulated object work 更像传统 3D vision / geometry 问题，重点放在 part segmentation、pose、joint estimation。
- HOI work 则常常更像 action / video understanding 问题，重点放在手部轨迹、接触、交互意图。
- 对 robotics 和 real2sim 来说，这两个视角天然应该汇合：
  - articulated object 的结构常常通过 interaction 才真正暴露出来
  - HOI cue 的可解释性又依赖 object structure
- 最近这条线开始越来越像一个闭环：
  - 先有更对路的 HOI data 或 interaction video
  - 再从 motion / contact 里恢复 articulated structure
  - 最后把结果编译成 digital twin 或 manipulation-friendly representation
- 同时内部也开始出现比较清楚的分支：
  - `Articulation in Motion` 更像 motion-first
  - `ArtHOI` 更像 interaction-first
  - `MonoArt` 更像 geometry-first

## Key Questions

- articulated structure 的最佳监督来源到底是静态几何，还是 interaction motion cue
- HOI 表示最该保留的是手部姿态、接触区域，还是 object-centric motion
- real2sim pipeline 里最关键的输出到底是 mesh、Gaussian representation，还是更结构化的 code / kinematic graph
- articulated reconstruction 和 HOI modeling 最终会不会被统一成一类更 general 的 interaction-centric world model

## Important Pages

- [[articulated-object-reconstruction-real2sim]]
- [[2026-articulation-in-motion]]
- [[2026-articulated-reconstruction-transformer]]
- [[2026-arthoi]]
- [[2026-monoart]]
- [[2025-taste-rob]]
- [[2025-object-centric-3d-motion-field]]
- [[2024-ipod]]
- [[2025-reconviagen]]

## Open Questions

- `motion-first` articulated analysis 能否稳定替代预设 part-count 的传统路线
- task-oriented HOI video generation 会不会成为 manipulation 学习的数据层标配
- articulated reconstruction 的中间表示最终更适合用 3DGS、point-based fields，还是 code / graph-based assets
- hand-object interaction 里的接触与力学信息，什么时候会被系统性并入当前 mostly-visual 的 reconstruction pipeline
- articulated object reconstruction and HOI 这条线未来更像 perception 模块，还是更像 world model / action model 的一部分

## Connections

- [[3d-generation]]
- [[ai-and-robotics-data]]
- [[articulated-object-reconstruction-real2sim]]
- [[2026-articulation-in-motion]]
- [[2026-articulated-reconstruction-transformer]]
- [[2026-arthoi]]
- [[2026-monoart]]
- [[2025-taste-rob]]
- [[2025-object-centric-3d-motion-field]]
- [[literature-review]]
- [[overview]]

## Sources

- [[2026-articulation-in-motion]]
- [[2026-articulated-reconstruction-transformer]]
- [[2026-arthoi]]
- [[2026-monoart]]
- [[2025-taste-rob]]
- [[2025-object-centric-3d-motion-field]]
- [[articulated-object-reconstruction-real2sim]]
