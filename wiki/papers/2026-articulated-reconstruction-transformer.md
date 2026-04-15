---
title: Articulated Reconstruction Transformer
kind: paper
summary: A CVPR 2026 paper on category-agnostic, feed-forward articulated object reconstruction from sparse multi-state RGB images, using transformer-decoded part slots for geometry, texture, and articulation.
status: active
source_count: 3
updated: 2026-04-15
---

# Articulated Reconstruction Transformer

## Summary

`ART` 很像 articulated object reconstruction 这条线里一个很明确的“下一阶段”信号：它不再主要依赖 test-time optimization，也不再只做特定类别，而是把问题直接改写成一个 `category-agnostic, feed-forward, part-based transformer prediction` 问题。输入只是 `sparse, multi-state RGB images`，再加上已知 camera poses；模型输出的不是一个模糊的整体 shape，而是一组具有明确语义功能的 `part slots`，每个 slot 都解码出对应 part 的 `3D geometry`、`texture` 和 `explicit articulation parameters`。这使得它不仅能重建 articulated object，还能把结果直接导出为 simulation-friendly 结构。

如果说 `Ditto` 更像把 articulated digital twin 问题通过 interaction 拉起来，`Articulation in Motion` 更像从 motion cue 里长出 mobility analysis，那么 `ART` 的味道更接近一种真正的 `feed-forward articulated reconstruction backbone`。它想证明的是：articulated object 也可以像普通 3D 对象一样，被一个统一 transformer 直接预测出来，只不过这次预测单位不是 whole-object latent，而是 part-centric structured slots。

## Story / Setting

- articulated object reconstruction 一直很难标准化，因为它比普通 3D 重建多了 `part structure + kinematics` 两层难度。
- 早期方法常常依赖：
  - 优化式 pipeline
  - fragile cross-state correspondences
  - 已知类别或更强结构先验
- 这会带来两个问题：
  - inference 慢
  - 泛化到开放类别和更复杂 articulation 时容易碎
- `ART` 的研究语境很清楚：既然普通 3D perception 已经越来越多被大模型 / transformer 接管，那 articulated reconstruction 能不能也从 optimization-heavy pipeline 迁移到更统一的 feed-forward 范式。

## Why This Exists

- 想摆脱 articulated reconstruction 对慢速优化和脆弱跨状态匹配的依赖。
- 想做一个 `category-agnostic` 的模型，而不是只会少数物体类别。
- 想让输出结构本身就是 `physically interpretable` 的，这样结果更容易直接接到 simulator / embodied AI downstream。
- 想把 articulated object 重建写成一个 part-based prediction 问题，而不是先整体拟合再事后拆 part。

## Related Work

- `Ditto` 代表现代 articulated digital twin 的重要起点，强调 interaction 驱动的 twin building。
- `CARTO` 更强调 `category and joint agnostic` 的快速 reconstruction，但路线和模型表述仍与 `ART` 不同。
- `PARIS` 更偏 part-level reconstruction + motion analysis，仍更依赖多状态几何对应和分析式过程。
- `Articulation in Motion` 则把重点进一步放到 `motion-driven prior-free mobility analysis`。
- `ART` 的 distinct point 是：把 articulated object 作为 rigid parts 的组合，直接用 transformer 对 part slots 做统一预测，目标更像一个 simulation-ready 的 feed-forward reconstruction model。

## First Principles

- articulated object 的自然表示单位不是整物体一个整体 latent，而是 `parts + articulation graph / parameters`。
- 如果 part-level representation 选对了，geometry、texture、kinematics 最好一起被预测，而不是分裂成互不通信的后处理模块。
- 对 real2sim 和 embodied AI 来说，最有价值的 reconstruction 往往不是最细表面，而是最容易解释、最容易 export 的结构化结果。
- 因此相比 whole-object fitting，`part slots` 更像这类问题的正确预测单位。

## Problem

- 如何从仅有的 `sparse, multi-state RGB images` 中，恢复完整 articulated object。
- 如何同时输出：
  - 每个 part 的 geometry
  - 每个 part 的 texture
  - articulation structure / parameters
- 如何在 `category-agnostic` 设定下保持泛化，而不是被特定物体模板绑死。
- 如何让重建结果直接可用于 simulation，而不需要大量人工清理。

## Main Idea

- 用 transformer 接收多视图、多 articulation state 的图像输入。
- 与普通 image tokens 一起引入一组 `learnable part slot tokens`。
- 主干从 sparse image evidence 中，把对象解析为若干 rigid parts。
- 再通过两个解码器联合预测每个 part 的统一表示，包括：
  - 3D geometry
  - texture
  - explicit articulation parameters
- 最终把这些 per-part predictions 组合起来，构成 articulated object，并可导出到标准 simulation format。

## Core Architecture

- **Input Representation**
  - 输入是 `sparse, multi-state RGB images`。
  - project page 明确说明这些输入带有 `known camera poses`。
  - 这点很重要：ART 目前不是从完全未知相机直接做全 pipeline，而是在已知 pose 条件下做 articulated reconstruction。

- **Tokenization**
  - 图像被 tokenized 后送入 transformer。
  - 同时加入 `learnable part slot tokens`，作为 part-level structured prediction 的查询单元。

- **Transformer Backbone**
  - backbone 负责把稀疏多状态图像证据和 part slots 结合起来。
  - 这里最关键的设计直觉是：slot 不只是 attention query，而是承载未来每个 rigid part 的统一表示。

- **Two Decoders**
  - project page 特别强调使用了 `two separate decoders`。
  - 它们共同预测每个 part 的 geometry、texture 和 articulation structure。
  - 从整体设计看，这等于把 “看图 -> 拆 part -> 给每 part 写几何/材质/关节” 变成了端到端前馈过程。

- **Composition and Rendering**
  - 各 part 的输出可以进一步组合，并在不同 articulation states 下渲染完整对象。
  - 这说明它不是只预测静态 canonical object，而是显式建模 part articulation。

- **Simulation Export**
  - project page 明确写到结果可以转换为 `URDF` 并导出到已有 simulator。
  - 这让 ART 很适合放在 real2sim 语境里读，而不只是 CV benchmark paper。

## Method

- 给定 sparse multi-state RGB observations 和已知 camera poses。
- 将图像 token 与 learnable part slots 一起送入 transformer。
- 让 part slots 从多视角、多状态 evidence 中聚合出各自对应的 rigid part 表示。
- 用两个解码器为每个 part 写出 unified representation：
  - 几何
  - 外观 / 纹理
  - articulation parameters
- 将各 part 组装成 articulated object，并可进一步转换成 URDF-like simulator asset。

从公开材料来看，ART 的方法论重点不在复杂后处理，而在于直接学习 `part-based structured prediction`。这也是它最像 foundation-model recipe 的地方：把繁琐 pipeline 编译进一个统一前馈网络。

## Experimental Setup

- 训练依赖一个 `large-scale, diverse dataset with per-part supervision`。
- 评测覆盖 `diverse benchmarks`，目标是验证：
  - category-agnostic articulated reconstruction
  - sparse image input 下的完整 object recovery
  - simulation-ready articulation structure
- 从 abstract 和 project page 看，ART 的比较对象主要是两类 baseline：
  - optimization-heavy articulated reconstruction methods
  - 只适用于特定类别的 feed-forward models

需要说明的是，公开页面目前给到的是高层实验设定和 qualitative demos，具体 benchmark 名称、指标拆解和 ablation 细节还需要细读正式论文全文补齐。

## Results

- arXiv abstract 明确声称：在多个 benchmark 上，ART 相比现有 baselines 有 `significant improvements`，并建立新的 SOTA。
- project page 的 qualitative demos 也强调了三类结果：
  - reconstructed articulated objects
  - interactive 3D viewer 中的 part-based object recovery
  - export into simulator 后支持 embodied AI interactions
- 这篇最值得记住的结果，不只是 “指标更高”，而是它把这几件事第一次更完整地绑在了一起：
  - sparse multi-state image input
  - category-agnostic articulated reconstruction
  - simulation export

换句话说，它更像是在证明一种新的 pipeline shape，而不只是刷一个 reconstruction 分数。

## Strengths

- `category-agnostic + feed-forward + simulation-ready` 这三个标签同时出现，很有辨识度。
- `part slots` 作为 articulated prediction 单位，非常符合这个问题的结构。
- 输出 geometry、texture、articulation 三者统一表示，结果更完整。
- 明确面向 simulator export，让它比很多“只做 analysis”的方法更贴近 real2sim。
- 从 abstract 看，它已经在 benchmark 上超过了 optimization-heavy 和 category-limited baselines，说明这条 recipe 不只是概念上好看。

## Limitations

- 当前输入仍假设 `known camera poses`，这意味着它还没有把 perception pipeline 前端完全吃掉。
- 公开材料里对 articulation hierarchy、joint limits、物理稳定性等 simulator 细节说明还不充分。
- 虽然是 category-agnostic，但它依然依赖 `per-part supervision` 的大规模训练数据，这种数据成本不低。
- 作为 feed-forward 模型，它可能在极复杂 articulation 或极端遮挡场景下仍会受到 sparse observation 限制。
- 与 `AiM` 相比，它更像 structure-first / slot-first reconstruction，而不是 motion-first articulation discovery。

## Questions

- `part slots` 会不会成为 articulated reconstruction 的默认表示单位，就像 object queries 之于检测。
- 如果把 `ART` 和 `AiM` 结合，一个负责 slot-based structural prediction，一个负责 motion-driven mobility refinement，会不会更强。
- 已知 camera poses 这个假设未来能否被 `VGGT` 一类 geometry backbone 部分替代。
- simulator export 目前离 truly robust real2sim asset 还有多远：
  - collision meshes
  - joint limits
  - contact-relevant geometry
  - physical parameter estimation

## My Take

我会把 `ART` 看成 articulated object reconstruction 这条线里一个很值得认真跟的“系统化节点”。如果 `Real2Code` 更像是把结果编译成 code asset，`AiM` 更像从 motion 中长出 mobility analysis，那 `ART` 则像是试图把 articulated reconstruction 本身先变成一个稳定、统一、可扩展的 transformer backbone。

它最吸引我的地方是：问题表述终于很像一个现代视觉大模型任务了。不是“先拟合几何、再找 correspondence、再估 joints”，而是“直接预测一组 part-centric structured slots”。这个视角如果被证明足够稳，后面很多 articulated / HOI / real2sim 工作都可能把 ART 当成基础设施，而不是一个单独 paper。

## Connections

- [[articulated-object-reconstruction-and-hoi]]
- [[articulated-object-reconstruction-real2sim]]
- [[2026-articulation-in-motion]]
- [[2025-object-centric-3d-motion-field]]
- [[2025-taste-rob]]
- [[3d-generation]]
- [[literature-review]]
- [[overview]]

## Sources

- Paper: https://arxiv.org/abs/2512.14671
- Project: https://kyleleey.github.io/ART/
- CVPR 2026 project page statement on simulator export and part-based reconstruction: https://kyleleey.github.io/ART/
