---
title: Articulated Object Reconstruction for Real2Sim
kind: synthesis
summary: A reading-oriented map of papers on articulated object reconstruction and digital-twin building, focusing on what is most relevant for real-to-sim pipelines.
status: active
source_count: 12
updated: 2026-04-15
---

# Articulated Object Reconstruction for Real2Sim

## Summary

如果你关心的是 `articulated objects reconstruction`，而且目标不是只做几何重建，而是进一步服务 `real2sim`，那这条线可以粗分成三种研究味道：

- `digital twin / articulation modeling`：直接从真实观测恢复 part geometry + joint parameters，让结果可导入仿真
- `category-level feed-forward inference`：追求更快、更泛化的 articulated shape / pose / joint state 预测
- `reconstruction + downstream manipulation`：把 articulated reconstruction 和 grasp / affordance / interaction 直接绑在一起

对 `real2sim` 来说，最核心的问题通常不是“形状能不能看起来像”，而是：

- part decomposition 对不对
- joint type / axis / limits 对不对
- 不同 articulation state 之间是否一致
- 输出是否能稳定转成 simulator-friendly asset

## Best Entry Points

- `Ditto: Building Digital Twins of Articulated Objects from Interaction`
  这篇很像 modern articulated real2sim 的经典起点。核心味道很正：before/after interaction 观测，恢复 part-level geometry 和 articulation model，并明确把结果放进 simulation。

- `Real2Code: Reconstruct Articulated Objects via Code Generation`
  这篇非常适合你如果关心 `real2sim asset generation`。它不只想做 reconstruction，而是把 articulation 显式写成 code，这一点和 simulator asset export 很接近。

- `PARIS: Part-level Reconstruction and Motion Analysis for Articulated Objects`
  如果你更关心 part-level reconstruction + motion parameter estimation 的纯视觉路线，这篇很值得细看。它比较像 articulated reconstruction 里的 strong geometry baseline。

## Key Papers

- `Ditto: Building Digital Twins of Articulated Objects from Interaction` (2022)
  https://arxiv.org/abs/2202.08227
  关键词：interactive perception、digital twin、category-agnostic、simulation export。

- `CARTO: Category and Joint Agnostic Reconstruction of ARTiculated Objects` (CVPR 2023)
  https://arxiv.org/abs/2303.15782
  关键词：single stereo observation、category/joint agnostic、shape + 6D pose + joint state、sim-to-real transfer。

- `PARIS: Part-level Reconstruction and Motion Analysis for Articulated Objects` (ICCV 2023)
  https://arxiv.org/abs/2308.07391
  关键词：two articulation states、self-supervised、part-level reconstruction、motion estimation。

- `Real2Code: Reconstruct Articulated Objects via Code Generation` (2024)
  https://arxiv.org/abs/2406.08474
  关键词：LLM code generation、part boxes、joint code、real-world generalization、multi-part scalability。

- `CenterArt: Joint Shape Reconstruction and 6-DoF Grasp Estimation of Articulated Objects` (2024)
  https://arxiv.org/abs/2404.14968
  关键词：RGB-D、reconstruction + grasping、articulated manipulation。

- `ArticulatedGS: Self-supervised Digital Twin Modeling of Articulated Objects using 3D Gaussian Splatting` (2025)
  https://arxiv.org/abs/2503.08135
  关键词：3DGS、digital twin、part appearance + geometry + motion params、self-supervised。

- [[2026-articulation-in-motion]] (ICLR 2026)
  https://arxiv.org/abs/2603.02910
  关键词：dynamic-static disentanglement、dual-Gaussian、prior-free mobility analysis、unknown part count、interaction video。

- `LARM: A Large Articulated-Object Reconstruction Model` (2025)
  https://arxiv.org/abs/2511.11563
  关键词：large model、sparse views、joint geometry + texture + kinematics、feed-forward。

- [[2026-articulated-reconstruction-transformer]] (CVPR 2026)
  https://arxiv.org/abs/2512.14671
  关键词：part slots、category-agnostic、sparse multi-state RGB、simulation-ready reconstruction。

- [[2026-arthoi]] (CVPR 2026 Highlight)
  https://arxiv.org/abs/2603.25791
  关键词：monocular 4D HOI、foundation-model priors、ASR、MLLM-guided alignment、articulated interactions。

- [[2026-monoart]] (2026)
  https://arxiv.org/abs/2603.19231
  关键词：single-image articulated reconstruction、progressive structural reasoning、TRELLIS prior、dual-query motion decoder、kinematic tree。

## How I Would Read This Line

- 如果你刚入门这条线，先读 `Ditto`。
  因为它最清楚地把“视觉观测 -> articulated digital twin -> simulation”这个故事讲完整了。

- 然后读 `PARIS` 和 `CARTO`。
  `PARIS` 更像 part-level reconstruction / motion analysis 代表；
  `CARTO` 更像 category-level fast inference 代表。

- 接着读 `Real2Code`。
  它很适合你如果脑子里已经在想 simulator asset、URDF-like structure、code-based abstraction。

- 如果你关心最新趋势，再看 `ArticulatedGS`、[[2026-articulation-in-motion]]、`LARM`、[[2026-articulated-reconstruction-transformer]]。
  这几篇代表 articulated reconstruction 正在从 implicit / optimization-heavy 方法，往 `3DGS`、`motion-driven mobility analysis` 和 `large feed-forward model` 三个方向长。

- 如果你特别关心 hand 和 articulated object 一起重建，而不是只看 object 本身，再补 [[2026-arthoi]]。
  它代表的是另一条很重要的分支：把 articulated object reconstruction 与 4D HOI alignment 放进同一个 monocular system。

- 如果你更关心单图 articulated reconstruction 本身，而不是 interaction video 或 hand-object coupling，再读 [[2026-monoart]]。
  它很代表一条越来越清晰的路线：把问题改写成 `geometry-first structured prediction`，先从 canonical 3D geometry 站稳，再往 part reasoning 和 kinematics 推。

## Patterns

- 早期强方法通常需要 `two states`、`before/after interaction` 或多视图观测。
- 越新的方法越想把问题改写成：
  - sparse-view
  - category-agnostic
  - feed-forward
  - simulation-ready
- 另一个新趋势是：与其先假设 parts，再估 motion；不如反过来从 motion cue 里长出 part decomposition，`[[2026-articulation-in-motion]]` 很代表这一点。
- 一个明显趋势是：方法不再只输出 mesh，而更强调 `part structure + kinematics + appearance` 一起恢复。
- 另一条明显趋势是：`real2sim` 已经不只是 perception 问题，而开始越来越像 `asset compilation` 问题。
- 同时也开始出现一种更鲜明的分化：有些方法是 `motion-first`，有些是 `interaction-first`，而 `[[2026-monoart]]` 代表的是更 orthodox 的 `geometry-first` articulated reconstruction。

## What Matters Most For Real2Sim

- 如果你最后要进 simulator，最重要的 often 不是 surface Chamfer，而是：
  - joint axis 是否稳定
  - part hierarchy 是否合理
  - articulation range 是否物理可用
  - reconstructed state 在 simulator 中是否能 replay / actuate
- 所以对 real2sim 来说，我会优先看那些明确强调：
  - `digital twin`
  - `joint parameter estimation`
  - `simulation deployment`
  - `code / structured asset output`

## Open Questions

- articulated real2sim 最终更需要的是更强几何，还是更强结构先验。
- `code generation` 会不会比直接 mesh / implicit fitting 更适合作为 simulator asset 中间层。
- sparse-view large model 会不会吃掉大部分 category-level articulated reconstruction。
- articulated object reconstruction 会不会和 affordance / manipulation policy 学习进一步绑定，而不再是独立视觉模块。
- `motion-first` 的 articulated analysis 会不会成为 real2sim 的标准前处理，尤其在 part count 未知时。

## Connections

- [[3d-generation]]
- [[2024-ipod]]
- [[2025-reconviagen]]
- [[2025-vggt]]
- [[2025-object-centric-3d-motion-field]]
- [[2026-articulation-in-motion]]
- [[2026-articulated-reconstruction-transformer]]
- [[2026-arthoi]]
- [[2026-monoart]]
- [[articulated-object-reconstruction-and-hoi]]
- [[ai-and-robotics-data]]
- [[literature-review]]
- [[overview]]

## Sources

- Ditto: https://arxiv.org/abs/2202.08227
- CARTO: https://arxiv.org/abs/2303.15782
- PARIS: https://arxiv.org/abs/2308.07391
- Real2Code: https://arxiv.org/abs/2406.08474
- CenterArt: https://arxiv.org/abs/2404.14968
- ArticulatedGS: https://arxiv.org/abs/2503.08135
- [[2026-articulation-in-motion]]
- [[2026-articulated-reconstruction-transformer]]
- [[2026-arthoi]]
- [[2026-monoart]]
- LARM: https://arxiv.org/abs/2511.11563
- ART: https://arxiv.org/abs/2512.14671
