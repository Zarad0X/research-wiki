---
title: MonoArt
kind: paper
summary: A 2026 paper on monocular articulated 3D reconstruction that turns single-image input into simulation-ready part structure and kinematics through progressive structural reasoning.
status: active
source_count: 3
updated: 2026-04-15
---

# MonoArt

## Summary

`MonoArt` 是一篇我会放进 `articulated object reconstruction + HOI / real2sim` 主线里认真读的论文，因为它抓住了一个非常硬、也非常有代表性的 setting：**只给单张图像，直接恢复 articulated object 的 3D geometry、part structure 和 motion parameters**。这件事难的地方不只是信息少，而是单图里关于 articulation 的信号本来就很弱，object structure 和 motion cue 还强烈纠缠在一起，所以直接从 image feature 回归 joint 参数很不稳定。

这篇工作的核心贡献，不只是“又做了 single-image articulated reconstruction”，而是它试图把这个问题重新表述成一个 **progressive structural reasoning** 过程。作者不再主要依赖 retrieval-based assembly、video generation、VLM symbolic reasoning 或手工 motion priors，而是先借助 frozen `TRELLIS` 得到 canonical geometry，再一步步把表面几何变成 part-aware representation、motion-aware query，最后再回归 kinematic parameters 和 tree structure。也就是说，它强调的是：**先让 3D geometry 和 part structure 站稳，再做 articulation inference**。

所以我会把 `MonoArt` 看成这条线里一个很关键的信号：single-image articulated reconstruction 正在从“外部辅助很多的 pipeline”往“geometry-grounded, feed-forward, structured prediction”方向收敛。它未必已经解决了所有 hard cases，但它很清楚地说明：如果几何 prior 足够强、part reasoning 足够结构化，单图 articulated reconstruction 可以不靠太重的外部 motion hallucination 也做得不错，而且速度和可部署性都更像一个可落地 backbone。

## Story / Setting

- articulated object reconstruction 一直比 rigid object reconstruction 更难，因为除了形状，还要恢复：
  - part decomposition
  - joint type
  - joint axis / pivot
  - motion limits
  - kinematic hierarchy
- 传统更稳的方法往往依赖：
  - multi-view
  - 多个 articulation states
  - interaction video
  - 或显式的 asset retrieval / assembly
- 但如果目标是更 scalable 的 `real2sim` 或 open-world 资产生成，这些条件都太重。
- 所以 `MonoArt` 想回答的是：**在单图输入下，能不能只靠一个统一模型，把 geometry、parts 和 kinematics 一步步推出来。**

## Why This Exists

- 想摆脱对多视图、双状态 observation、video generation 的依赖。
- 想避免 retrieval-based 方法带来的 texture mismatch、几何误差和 instance mismatch。
- 想比 vision-language / symbolic reasoning 路线更“几何内生”一些，不那么依赖手工 motion templates。
- 想把 single-image articulated reconstruction 做成更接近 `simulation-ready structured prediction` 的 backbone。

## Related Work

- 一类工作依赖多视图或多 articulation states，例如 `PARIS`、`DTA`、`ArticulatedGS`，优点是更稳，缺点是输入条件重。
- 一类工作做 retrieval-based single-image articulated reconstruction，例如 `SINGAPO`，更 scalable，但容易出现几何和纹理不对齐。
- 一类更新的工作开始借助更强 generative 或 reasoning priors，例如：
  - `DreamArt` 用辅助 video generation
  - `Articulate-Anything` 用 VLM 做 symbolic articulation reasoning
  - `PhysX-Anything` 往 simulation-ready asset 更进一步
- `MonoArt` 的 distinct point 在于：
  - 不主打 retrieval
  - 不主打 VLM reasoning
  - 不主打 external motion templates
  - 而是主打 `canonical geometry -> part-aware reasoning -> motion-aware decoding -> kinematic estimation`

## First Principles

- 单图 articulation inference 难，不是因为网络不够大，而是因为 motion cue 太弱、part structure 太隐式。
- 如果先有更稳定的 canonical 3D geometry，part reasoning 就有了 anchor。
- 如果 part-aware feature 和 motion reasoning 被显式拆开，articulation regression 会更稳定、更可解释。
- articulation 不是一个纯几何问题，也不是一个纯语义问题；它需要把 `geometry + part semantics + motion anchoring` 一起建模。

## Problem

- 输入：一张 monocular RGB image。
- 输出：完整 articulated object 的：
  - canonical geometry
  - per-part mask / decomposition
  - joint type
  - joint axis
  - joint pivot / origin
  - motion limits
  - kinematic tree
- 目标不是只做看起来像的 mesh，而是做 **带可操作运动结构的 3D reconstruction**。

## Main Idea

- 先用 frozen `TRELLIS` 从单图恢复 canonical 3D shape 和 sparse voxel latent。
- 再把 geometry-aligned latent 转成 part-aware point features。
- 然后用一个 `dual-query motion decoder`，把“part semantics”和“motion anchor location”解耦成两类 query，迭代推理。
- 最后用 `kinematic estimator` 回归 articulation parameters，并预测 parent-child kinematic tree。

它的关键词不是 end-to-end regression，而是 **progressive structural reasoning**。

## Core Architecture

- **TRELLIS-based 3D Generator**
  - 输入单图。
  - 用 frozen `TRELLIS` 预测 sparse voxel latent `Z` 和 canonical mesh `O`。
  - 这一步提供几何基础，不在这里直接预测 articulation。

- **Part-aware Semantic Reasoner**
  - 从 `TRELLIS` 的 voxel latent 上做 tri-linear interpolation，得到 surface-aligned point features。
  - 再把这些点特征投影到三个正交平面，形成 tri-plane representation。
  - 经过 `Part Contrast Transformer` 建模全局关系后，得到 part-aware point embeddings `H`。
  - 作者用 triplet loss 做 3D 结构监督，让 feature 更 part-discriminative。

- **Dual-Query Motion Decoder**
  - 用两类 query：
    - `content query` 编码 part semantics
    - `position query` 编码 spatial motion anchors
  - query 从全局 object context 初始化。
  - 经过多层 refinement block，用 self-attention + cross-attention 逐步细化。
  - 中间还预测 per-query part logits，并用 frozen `CLIP` text embeddings 做 prototype retrieval，增强 semantic consistency。
  - 同时预测 query confidence，在 inference 时自动筛掉无效 part hypothesis。

- **Kinematic Estimator**
  - 通过 query-point affinity 得到 part mask。
  - 回归 joint type、axis、pivot、limits。
  - 再基于 part logits 和 learnable compatibility matrix 推 parent-child affinity，构建 cycle-free kinematic tree。

## Method

整个 pipeline 可以按四步理解：

1. **几何初始化**
   - 从单图用 `TRELLIS` 得到 canonical mesh 和 sparse structured latent。

2. **part-aware feature construction**
   - 从 voxel latent 采样 surface-aligned features。
   - 通过 tri-plane projection + transformer refinement，把局部几何点特征变成带全局上下文的 part-aware embedding。

3. **motion-aware query reasoning**
   - 用 dual-query 机制把 “这是什么 part” 和 “它的运动锚点在哪” 分开表示。
   - 通过多层 residual refinement，让 position/content queries 一起收敛。
   - 用 confidence estimation 决定哪些 queries 真对应有效 articulated parts。

4. **kinematic regression**
   - 用 refined queries 回归关节参数和 part masks。
   - 预测 part 之间的 attachment probability，并构成 tree-structured articulated object。

我觉得这篇方法最值得记的是两个设计：
- 它没有试图直接从 image token 一步回 joint parameters，而是显式走 `geometry -> part -> motion -> kinematics`
- 它把 motion reasoning 的 query 分成 content / position 两支，这个解耦很符合问题本质

## Experimental Setup

- 数据集：`PartNet-Mobility`
- 两个 setting：
  - `7-category` split，沿用 `SINGAPO`
  - `46-category` split，沿用 `PhysX-Anything`
- 几何指标：
  - `CD`
  - `F-Score`
  - `PSNR`
  - `CLIP similarity`
- articulation / kinematics 指标：
  - `Type Accuracy`
  - `Axis Direction Error`
  - `Pivot Distance Error`
- 评估方式比较认真：
  - 对每个 shape 沿预测 motion range 采样 6 个 articulation states
  - 每个 state 从 10 个随机视角渲染
  - 再对 geometry 和 appearance 一起评测
- baseline 包括：
  - `URDFormer`
  - `SINGAPO`
  - `Articulate-Anything`
  - `PhysXGen`
  - `PhysX-Anything`

实现细节里几个值得记的数字：
- surface points `M = 100,000`
- voxel resolution `Nz = 64`
- tri-plane resolution `Nt = 128`
- lifted point embedding dim `d2 = 448`
- dual queries `Nq = 100`
- refinement blocks `L = 6`

作者采用四阶段训练：
- 先 warm up part-aware reasoner
- 再训练 dual-query initialization
- 再 joint train reasoner + decoder + articulation regressor
- 最后单独训练 kinematic tree predictor

## Results

### PartNet-Mobility 7 classes

- `MonoArt`:
  - `CD 0.77`
  - `F-Score 0.728`
  - `PSNR 17.55`
  - `CLIP 0.926`
  - `Type Acc. 88.26`
  - `Axis Err. 0.209`
  - `Pivot Err. 0.085`

对比 `SINGAPO`：
- `CD 1.26 -> 0.77`
- `F-Score 0.572 -> 0.728`
- `Type Acc. 77.12 -> 88.26`
- `Axis Err. 0.493 -> 0.209`
- `Pivot Err. 0.201 -> 0.085`

这不是小幅领先，而是 geometry 和 kinematics 两边都拉开了比较明确的差距。

### PartNet-Mobility 46 classes

- `MonoArt`:
  - `CD 1.25`
  - `F-Score 0.670`
  - `PSNR 18.55`
  - `CLIP 0.907`
  - `Type Acc. 67.47`
  - `Axis Err. 0.423`
  - `Pivot Err. 0.108`

对比 `PhysX-Anything`：
- `CD 1.88 -> 1.25`
- `F-Score 0.531 -> 0.670`
- `PSNR 17.07 -> 18.55`
- `CLIP 0.880 -> 0.907`
- `Type Acc. 63.35 -> 67.47`
- `Pivot Err. 0.173 -> 0.108`

轴向误差上 `PhysX-Anything` 更低（`0.289` vs `0.423`），所以它不是所有 articulation 指标都绝对最强；但从 overall geometry + type + pivot 的综合表现看，`MonoArt` 的结果更平衡，也更像一个实例级 reconstruction backbone。

### Real-world generalization

- 作者收集了约 `100` 张 wild images。
- 做了 `20` 人用户研究，分别评几何质量和 articulation 质量。
- `MonoArt` 得分最高：
  - geometry `4.63`
  - kinematics `4.37`
- 明显高于：
  - `PhysX-Anything` `3.34 / 3.12`
  - `SINGAPO` `2.55 / 2.87`
  - `Articulate-Anything` `2.72 / 2.60`

### Runtime

- 单张图 average runtime：`20.5s / instance`
- 其中 `18.2s` 用在 `TRELLIS` 3D reconstruction
- articulation reasoning 本身只增加很少额外开销
- 对比文中数字：
  - `Articulate-Anything` `229.9s`
  - `PhysX-Anything` `256.8s`
  - `PhysXGen` `31.6s`
  - `URDFormer` `34.1s`
  - `SINGAPO` `19.6s`

所以它在速度上非常接近 `SINGAPO`，但重建质量和 articulation 质量更强。

## Strengths

- 问题设定很硬，而且很实用：single-image articulated reconstruction。
- 方法叙事清楚，`geometry -> parts -> motion -> kinematics` 很符合直觉，也比很多 pipeline 更干净。
- 不依赖 retrieval library、video generation 或强 VLM 先验，系统味道更统一。
- 结果不是只在 geometry 上赢，而是在 part / kinematics 上也明显有竞争力。
- inference time 很有说服力，说明 structured reasoning 不一定比复杂 external-prior pipeline 慢。
- 下游展示很对路：直接导入 `IsaacSim` 做 robot manipulation，以及 articulated scene reconstruction。

## Limitations

- 它强依赖 `TRELLIS` 给出的 canonical geometry 质量，所以 geometry prior 仍然是上游瓶颈。
- 对 very small parts attached to large objects 仍然吃力，作者明确提到 uniform point sampling 会让 tiny parts coverage 不足。
- 对 novel topology 或 uncommon articulation pattern，learned structural priors 可能泛化不足。
- 虽然比很多方法简洁，但仍然不是轻量级系统；真正的推理时间主要卡在 3D generation。
- 它目前只看 object，不涉及 hand-object coupling，所以如果你关心 HOI / manipulation demonstration，它不是完整终局。

## Questions

- 如果把 `MonoArt` 和 `ArtHOI` 结合，能不能把 monocular HOI 里的 object side 做得更稳。
- `TRELLIS` 这种 3D generator 在这里是 backbone 还是暂时性垫脚石；未来会不会换成更强的 geometry foundation model。
- dual-query motion decoder 这种解耦，能否迁移到 interaction video setting，而不只用于 single image。
- 这类方法最终的中间表示更适合停在 mesh + joint params，还是进一步编译成 `URDF` / code-level asset。
- 如果 part count 更复杂、更长尾，query confidence + tree prediction 还能否稳定工作。

## My Take

`MonoArt` 很像这条线里一个我会偏喜欢的 paper，因为它体现了一种很明确的 research taste：**先把结构问题写对，再让模型学。** 它没有把希望寄托在“多喂一点外部线索”上，而是把 articulation reconstruction 拆成几个更自然的中间层次，再用一个比较统一的架构串起来。

我觉得它最重要的意义有三层：

- 第一，它说明 single-image articulated reconstruction 不一定非要靠 retrieval 或外部 motion hallucination 才能做得像样。
- 第二，它强化了一个我现在越来越相信的判断：在 articulated real2sim 这条线里，真正高杠杆的往往是 `geometry prior + explicit part structure + structured kinematic decoding`。
- 第三，它比很多“看起来更聪明”的 VLM-heavy 方法更像一个可复用 backbone。你可以想象它继续往两个方向延伸：
  - 接到 `HOI / interaction video`
  - 接到 `simulation-ready asset compilation`

所以如果 `Articulation in Motion` 更像 motion-first、`ArtHOI` 更像 interaction-first、`Real2Code` 更像 simulator-asset-first，那 `MonoArt` 更像这条线上一个很“正”的 **geometry-first structured reconstruction** 节点。

## Connections

- [[articulated-object-reconstruction-and-hoi]]
- [[articulated-object-reconstruction-real2sim]]
- [[2026-articulation-in-motion]]
- [[2026-articulated-reconstruction-transformer]]
- [[2026-arthoi]]
- [[2024-trellis]]
- [[2025-vggt]]
- [[3d-generation]]
- [[overview]]

## Sources

- Paper: https://arxiv.org/abs/2603.19231
- PDF: https://arxiv.org/pdf/2603.19231
- Project: https://lihaitian.com/MonoArt/
