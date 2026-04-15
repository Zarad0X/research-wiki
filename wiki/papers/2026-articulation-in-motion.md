---
title: Articulation in Motion
kind: paper
summary: An ICLR 2026 paper that reconstructs articulated objects and analyzes part mobility from a start-state scan plus an interaction video, using dual-Gaussian dynamic-static disentanglement without part-count priors.
status: active
source_count: 3
updated: 2026-04-08
---

# Articulation in Motion

## Summary

`Articulation in Motion (AiM)` 很适合放进 articulated object reconstruction / `real2sim` 这条线里认真读，因为它抓住了一个非常关键、但常被低估的痛点：很多方法默认你已经知道 part 数量，或者至少能看到对象在两个 articulation state 下都很清楚，再靠跨状态对应去估计每个 part 的 articulation。这个前提在真实世界里其实很脆弱。AiM 想做的是把这套前提尽量拿掉：只给一个 `start-state scan` 和一段 `user-object interaction video`，不提供 part-level structural prior，不预设 part 数量，直接恢复 part-level decomposition、articulation kinematics，以及一个可交互的 3D digital replica。

对 `real2sim` 而言，这篇最有意思的不是“又用了 3D Gaussian Splatting”，而是它把 articulated reconstruction 更明确地写成了 `dynamic-static disentanglement + mobility analysis` 问题。也就是说，关键不只是把对象几何拟合好，而是先回答：哪些 primitive 是静态底座，哪些是被带动的 rigid parts，它们是围绕什么 joint 在动，以及这些结构能否自然导出一个 simulator-friendly articulation model。

## Story / Setting

- articulated object reconstruction 一直比刚体对象难很多，因为你需要同时恢复：
  - part geometry
  - part segmentation
  - joint type / axis / kinematics
  - 各 part 在不同状态下的对应关系
- 很多较早方法默认存在两个清晰 articulation states，或者直接假设 part 数目已知。
- 一旦真实视频里某些 parts 没有在两个状态里都清晰可见，或 part 数量本身未知，这类方法就会明显变脆。
- AiM 的故事是：不如直接利用 interaction video 中真实出现的 motion cues，把“静态部分”和“动态部分”先分开，再在动态 primitive 上做 prior-free mobility analysis。

## Why This Exists

- 想减少 articulated reconstruction 对人工先验的依赖，尤其是：
  - 预先给定的 part count
  - 需要清晰跨状态 correspondence 的假设
- 想让 articulated object digital twin 更贴近真实使用场景：用户录一段 interaction video，再配合起始状态的扫描，就能恢复可交互模型。
- 想把 articulated object analysis 从 per-point optimization，推进到更结构化、也更适合高质量 rendering 的表示。

## Related Work

- `Ditto` 代表的是现代 digital twin 路线的关键起点：interaction before/after 观测 + articulated digital twin。
- `PARIS` 更偏 part-level reconstruction + motion analysis，通过多状态之间的对应关系推 articulation。
- `CARTO` 更强调 category/joint agnostic 的快速 feed-forward inference。
- `ArticulatedGS` 则把 articulated digital twin 更明确地搬到 `3DGS` 上。
- AiM 处在这些工作之间的一个很有意思的位置：它既是 digital twin work，又更强调整个 mobility analysis 过程应当 `prior-free`，尤其不要依赖预设 part 数量。

## First Principles

- articulated object 的关键结构并不只存在于静态几何里，更存在于“物体是怎么动的”。
- 如果 motion cue 足够好，part decomposition 和 articulation analysis 应该能从动态里长出来，而不是先由模板或类别先验规定好。
- 对 `real2sim` 来说，最有价值的 reconstruction 往往不是最细表面，而是最可靠的：
  - rigid part clustering
  - joint estimation
  - kinematic structure
- 如果一个表示既能支持 part-aware analysis，又能高质量 render，那它就更像 digital twin substrate，而不只是分析中间结果。

## Problem

- 如何在不知道 part 数量的情况下，从 interaction video 中恢复 articulated object 的 part-level decomposition。
- 如何在没有 part-level structural priors 的前提下，稳定估计 articulation kinematics。
- 如何让输出结果同时满足：
  - 可解释的 mobility analysis
  - 高质量视觉重建
  - 可交互的 digital replica

## Main Idea

- 输入是两部分：
  - 一个对象起始状态的 `3DGS scan`
  - 一段展示独立 parts 运动的 `user-object interaction video`
- 用一个 `dual-Gaussian scene representation` 去做 dynamic-static disentanglement。
- 再对动态高斯 primitive 做 `sequential RANSAC`：
  - 聚类成 rigid parts
  - 自动确定 part 数量
  - 估计每个 part 的 articulation parameters
- 最终每个 part 都被表示成一个独立的 3D Gaussian set，因此既能做 mobility analysis，也能支持高质量 rendering。

## Core Architecture

- **Dual-Gaussian Representation**
  - 这是论文最核心的表示设计。
  - 它不是只拟合一个统一 3DGS，而是显式把场景拆成更适合做 `dynamic-static disentanglement` 的双分支或双角色表示。
  - 直觉上，它让系统先分清哪些高斯更像静态支撑结构，哪些更像随 articulation 运动的部分。

- **Motion-Cue-Based Segmentation**
  - interaction video 提供了最重要的 supervision source：真实运动。
  - 系统不靠类别模板，而是靠 motion cue 把 primitives 分到不同部件，并为这些部件分配 articulation joints。

- **Sequential RANSAC for Mobility Analysis**
  - 这是 AiM 最强的“prior-free”味道来源。
  - 不先给 part count，而是顺序式地从动态高斯里聚类 rigid parts，并同时估 kinematics。
  - 也就是说，part discovery 和 articulation estimation 是一起被做出来的。

- **Per-Part Gaussian Sets**
  - 最终输出不是抽象标签而已，而是每个 part 各自的一组 3D Gaussians。
  - 这让结果不仅适合分析，也适合后续渲染和 digital replica 构建。

## Method

- 从起始状态扫描初始化对象的 3DGS 表示。
- 用 interaction video 中的 motion cues 学出 dual-Gaussian representation。
- 通过 dynamic-static disentanglement，把运动相关 primitive 从静态支撑部分中剥离出来。
- 在动态 primitive 上运行 sequential RANSAC：
  - 挖出一个个 rigid moving part
  - 估计各 part 的 articulation parameters
  - 自动判断 part 数量
- 最终得到 part-aware articulated object representation，可用于渲染和交互分析。

## Experimental Setup

- 论文同时评估 `simple objects` 和 `complex objects`。
- 比较重点不是单纯几何误差，而是：
  - part segmentation quality
  - articulation / mobility analysis quality
  - generalization to more complex articulated objects
- project page 也单独展示了：
  - visual segmentation results
  - two-part objects rendering
  - three-part / complex objects rendering
  - real data results
- 从公开材料看，这篇很强调真实 interaction data，而不是只在完全受控 synthetic setup 中演示。

## Results

- arXiv abstract 和 project page 都强调：
  - 在 **无先验 part 数量** 的设定下，part segmentation quality 超过先前方法。
  - 在 simple 和 complex articulated objects 上都有较强 generalization。
  - 最终可以输出质量较高的 articulated digital replica，而不只是参数表。
- 这篇的结果价值主要不在于“单一 benchmark 刷了多少点”，而在于它明显扩大了适用场景：
  - 不需要预设 part 数目
  - 不需要非常干净的双状态对应
  - 更能适应真实 interaction video

## Strengths

- 它把 articulated reconstruction 的问题重心，从“多状态对应 + 已知 part 数”转向 `motion-driven prior-free analysis`，这个 framing 很对 real-world。
- `dual-Gaussian + sequential RANSAC` 的组合很有辨识度，不是把 3DGS 生硬套在 articulated object 上。
- 输出既保留结构信息，也保留高质量 rendering 能力，更接近 digital twin。
- 强调 complex objects 和真实数据，而不只是 toy articulated examples。

## Limitations

- 它仍然依赖 interaction video；如果对象几乎没有被有效驱动，motion cue 可能不足。
- “prior-free” 并不等于完全没有建模假设，系统仍然在找 rigid-part clustering 和可解释 articulation。
- 从公开材料看，它更擅长 `mobility analysis + digital replica`，不一定直接等于 simulator-ready URDF 资产导出。
- 如果 articulation 极其复杂、存在强非刚体行为，基于 rigid part clustering 的路线可能还是会吃力。

## Questions

- AiM 这种 `motion-first` articulated analysis，会不会比 `code-first` 的 `Real2Code` 更适合作为真实视频输入端。
- `dual-Gaussian` 是否会成为 articulated 3DGS 的一个常见设计模式，而不只是这篇的特定实现。
- 它输出的 articulation representation 离 simulator asset 还差哪一步：
  - joint limits
  - hierarchy cleanup
  - collision geometry
  - export format
- 如果把 AiM 和 `VGGT` 式 geometry backbone 接起来，能否减少对起始状态高质量扫描的依赖。

## My Take

如果说 `Ditto` 更像“articulated digital twin from interaction” 的经典起点，`Real2Code` 更像“把 articulated reconstruction 编译成代码资产”，那 `AiM` 给我的感觉是把中间这一层做得更扎实了：先别急着输出代码，也别先假设 part 数量，而是老老实实从真实运动里把 `哪些部分在动、怎么动、围绕什么在动` 这件事做对。

所以我会把它看成 articulated real2sim 线上一个很值得关注的新节点。它未必已经是终局方案，但它非常清楚地说明：对于 articulated objects，`motion cue` 本身也许就是最重要的结构监督来源。这个判断如果成立，后面很多 real2sim pipeline 都可能把“interaction video + mobility disentanglement”当成标准前处理。

## Connections

- [[articulated-object-reconstruction-real2sim]]
- [[2025-object-centric-3d-motion-field]]
- [[2025-vggt]]
- [[3d-generation]]
- [[literature-review]]
- [[overview]]

## Sources

- Paper: https://arxiv.org/abs/2603.02910
- Project: https://haoai-1997.github.io/AiM/
- Code: https://github.com/haoai-1997/AiM
