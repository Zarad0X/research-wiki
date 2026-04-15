---
title: ArtHOI
kind: paper
summary: A CVPR 2026 highlight paper that reconstructs 4D hand-articulated-object interactions from a single monocular RGB video by coordinating and refining multiple foundation-model priors.
status: active
source_count: 3
updated: 2026-04-15
---

# ArtHOI

## Summary

`ArtHOI` 很适合放进现在这条 `articulated object reconstruction + HOI` 线里细读，因为它抓住了一个非常具体、也非常难的 setting：**只给一段单目 RGB 视频，要同时恢复 hand 和 articulated object 的 4D interaction**。这比普通 HOI reconstruction 更难，因为 object 不是 rigid；也比普通 articulated reconstruction 更难，因为你不只是恢复物体，还要恢复手与物之间随时间变化的对齐、接触和协调运动。

这篇工作的核心风格不是“从零训练一个端到端大模型”，而是更像一篇很现实的系统整合论文：它假设 foundation models 已经能各自提供一部分有用但不可靠的先验，然后把真正的研究贡献放在 **怎样驯服这些 foundation-model priors** 上。作者明确指出两类关键 failure mode：一类是 object prior 自己不在真实尺度和真实世界坐标里，另一类是 hand 和 object 各自重建后彼此对不上。围绕这两点，`ArtHOI` 提出了 `ASR` 去恢复 metric scale / pose，又提出 `MLLM-guided hand-object alignment` 去把 contact reasoning 变成 HOI mesh composition 的物理约束。

所以我会把 `ArtHOI` 看成一个很典型的 bridge paper：它一头接 `foundation model as prior`，另一头接 `monocular 4D articulated HOI reconstruction`。它未必已经是最优雅、最统一的终局方案，但非常清楚地说明了：对于 hand-articulated-object interaction，这个问题已经不能只靠单一 rigid HOI 模型或单一 articulated reconstruction 模型来解决，而要靠多种 priors 的 coordinated refinement。

## Story / Setting

- 现有 HOI reconstruction 方法大多仍然主要处理 rigid objects。
- 而 articulated object 的 4D reconstruction 方法，通常又需要：
  - object pre-scan
  - multi-view videos
  - 或更强的外部几何条件
- 这导致一个很现实但空缺很大的问题：如果只有一段普通单目视频，里面是人手在操作一个未知 articulated object，能不能把整个 4D interaction 重建出来。
- `ArtHOI` 正是在这个 gap 上出发：它要解决的是 monocular、unknown object、articulated、hand-object coupled 这四重困难叠加的 setting。

## Why This Exists

- 想把 HOI reconstruction 从 rigid-object assumption 推进到 articulated objects。
- 想避免 articulated reconstruction 对 pre-scanned object 或 multi-view capture 的依赖。
- 想利用 foundation models 已有的通用能力，但又不盲信它们输出，而是把它们变成可被优化和纠偏的 priors。
- 想让最终结果不仅是 object 或 hand 的单独重建，而是 physically plausible 的 4D HOI reconstruction。

## Related Work

- 一类工作做 rigid-object HOI reconstruction，但无法很好处理 articulated motion。
- 一类工作做 articulated object 4D reconstruction，但通常要求 pre-scan 或 multi-view。
- `TASTE-Rob` 更偏 task-oriented HOI data / generation，为 manipulation 学习提供更对路的视频数据。
- `Articulation in Motion` 更偏从 interaction video 中做 motion-first mobility analysis 和 articulated digital replica 恢复。
- `ART` 更像 feed-forward, part-slot-based articulated reconstruction backbone。
- `ArtHOI` 的 distinct point 在于：它不是只做 object，也不是只做 hand，而是要把 **hand + articulated object + temporal interaction + contact consistency** 作为一个整体去恢复。

## First Principles

- 对 HOI 来说，单独把 hand 和 object 分开重建通常不够，因为真正困难的地方在两者之间的对齐与接触。
- 对 articulated object 来说，normalized mesh 或 canonical object prior 若不被 grounding 到真实世界尺度与位姿，就很难直接用于 4D interaction reconstruction。
- foundation models 的价值在于提供强 prior，但这些 priors 通常不物理、不一致、也不直接可组合。
- 因此真正高杠杆的问题不是“哪个 foundation model 更强”，而是“怎样把多个不完美先验拼成一个 physically plausible 4D system”。

## Problem

- 如何从 **单目 RGB 视频** 重建 hand-articulated-object interactions 的 4D过程。
- 如何在没有 pre-defined object templates、没有 multi-view setup、没有 object pre-scan 的条件下恢复 articulated object。
- 如何解决 foundation-model priors 的两大问题：
  - object mesh 的 metric scale / pose 不对
  - independently reconstructed hands and objects 彼此 misaligned
- 如何让最后的 hand-object composition 在接触和时序上都更可信。

## Main Idea

- 先调用多个 foundation models，各自提供手、物体、深度、相机、跟踪等先验。
- 再用一个 optimization-based framework 对这些先验做 coordinated refinement。
- 关键设计包括两块：
  - `ASR (Adaptive Sampling Refinement)`：把 normalized object mesh grounding 到真实世界尺度和位姿
  - `MLLM-guided hand-object alignment`：让 contact reasoning 成为 mesh composition optimization 的约束
- 中间再通过 `PartField + CoTracker3 + depth lifting` 做 part-wise motion reconstruction，从而把 articulated object 的动态恢复出来。

## Core Architecture

- **Foundation Model Preprocessing**
  - `SAM2` 分割 object 和 hand。
  - `Video-Depth-Anything` 与 `UniDepthV2` 估计 metric depth 和 camera intrinsics。
  - `DiffuEraser` 去掉 human region，得到更干净的 object observation。
  - `HunYuan3D` 从 clean canonical frame 重建 object mesh。
  - `WiLoR` 独立重建 hands。

- **ASR: Metric Scale & Pose Estimation**
  - foundation image-to-3D 模型给出的 object mesh 常常是 normalized 的，不在真实尺度里。
  - `ASR` 通过迭代采样 candidate scales，再调用 `FoundationPose` 对每个尺度求 pose，并用 silhouette matching against object mask 评分，最终恢复 object 的 metric-scale pose。
  - 这是全文里最关键的 grounding 模块之一。

- **Part-wise Motion Reconstruction**
  - `PartField` 把 canonical mesh 分成 parts。
  - `CoTracker3` 在 inpainted video 里跟踪这些部分。
  - 再借助估计的深度把 2D tracks 提升到 3D。
  - 最后用 visibility-aware tracking loss 优化 per-part `SE(3)` motions，处理 part-part 和 hand-part occlusion。

- **MLLM-Guided Hand-Object Alignment**
  - hand 与 object 如果各自独立重建，scale 和 position 往往对不上。
  - `Qwen-VL-Max` 被提示 camera-perspective cues、邻近帧和 colorized depth，来推断每帧 contact states 与 contacting fingers。
  - 这些 contact labels 驱动一个两阶段优化：
    - 先把 object scale 对齐 hand
    - 再 refine hand pose
  - 目标是让最终 HOI composition 更 coordinated、更 physically plausible。

## Method

- 从 monocular RGB video 开始。
- 用 segmentation、depth、camera、image-to-3D、hand reconstruction 这些 foundation models 提供初始 priors。
- 对 object side：
  - 先用 inpainting 后的 canonical frame 得到 mesh
  - 再通过 `ASR` 恢复真实尺度和位姿
  - 再通过 `PartField + CoTracker3 + depth lifting` 恢复各 articulated parts 的 3D motion
- 对 hand-object coupling：
  - 用 `WiLoR` 得到 hand reconstruction
  - 再让 `Qwen-VL-Max` 推断 contact states / contacting fingers
  - 用 contact reasoning 去约束 hand-object alignment optimization
- 最终输出的是 coordinated 4D hand-articulated-object reconstruction。

## Experimental Setup

- 论文新建了两个数据集：
  - `ArtHOI-RGBD`
  - `ArtHOI-Wild`
- 另外还在 `RSRD` 和 `ARCTIC` 上做了评测和泛化验证。
- 定量评估聚焦三块：
  - articulated object reconstruction accuracy
  - hand-object alignment quality
  - MLLM contact reasoning accuracy
- 比较对象包括：
  - `EasyHOI`
  - `RSRD`
  - 以及若干未对齐或弱对齐的 baseline 组合

从 project page 看，这篇很强调 challenging cases，尤其是 heavy hand-part occlusions 和 wild monocular videos。

## Results

- 在 `ArtHOI-RGBD` 上，project page 报告 `CD`、`MSSD`、`F-scores` 都显著优于 `EasyHOI` 和 `RSRD` baselines，尤其在 hand-part occlusion 重的时候优势更明显。
- 在 `RSRD` 上，它在不需要 pre-scanned object 的情况下，取得了与 baseline competitive 甚至更优的 reconstruction quality。
- 在 `ArtHOI-Wild` 上，`RSRD` 因为需要 object scan 无法适用，而 `ArtHOI` 仍能工作，这一点很关键。
- 在 `ARCTIC` 上，project page 明确写到：
  - `RSRD` fails to reconstruct articulated objects
  - `EasyHOI` 在 `>10%` 帧上失败
  - `ArtHOI` 在 `CD`、`MSSD`、`F10`、`contact accuracy`、`finger accuracy` 上都最好
- 在 HOI alignment 上，使用 `Co² score` 评测时，`ArtHOI` 的 `MLLM-guided alignment` 在 `ArtHOI-RGBD`、`RSRD`、`ArtHOI-Wild` 三个来源上都取得最低分，说明 hand-object composition 更合理。

这篇最重要的结果，不只是“又赢了一些指标”，而是它证明了：
- 单目 setting 是可做的
- articulated HOI 是可做的
- foundation-model priors 虽然不准，但经过有针对性的 refinement 后可以真正撑起 4D reconstruction

## Strengths

- 问题设定非常强：monocular、unknown articulated object、hand-object coupled、4D reconstruction，这几个难点一起上。
- 不是生硬堆 foundation models，而是明确研究它们的 failure modes，并提出针对性 refinement。
- `ASR` 和 `MLLM-guided alignment` 都很有问题导向，而不是 generic optimization tricks。
- 新建 `ArtHOI-RGBD` 和 `ArtHOI-Wild`，说明作者在 evaluation 上也补了真实空缺。
- 结果覆盖实验室数据、已有数据集、wild 视频，叙事比较完整。

## Limitations

- 这是一个 optimization-based framework，不是纯 feed-forward pipeline，推理成本和系统复杂度都不低。
- 严重依赖多个 foundation models 的串联质量，整个系统可能有较多 error propagation。
- contact reasoning 依赖 MLLM，意味着某些复杂 interaction 可能仍会受 prompt / inference stability 影响。
- 虽然不需要 object pre-scan，但仍然需要相当多外部模块和 carefully engineered optimization。
- 它更像 monocular 4D HOI reconstruction system，而不是一个简洁统一的 representation model。

## Questions

- `ArtHOI` 这种 multi-prior refinement 路线，未来会不会被更统一的视频 foundation model 吃掉。
- `ASR` 这种 metric grounding 方法，能否泛化成更普适的 articulated object scale recovery 模块。
- `MLLM-guided contact reasoning` 究竟是一个过渡方案，还是未来 HOI reconstruction 里的长期组成部分。
- 如果把 `ArtHOI` 和 `AiM` / `ART` 结合，能不能把 object side 的 articulated structure建得更稳，再把 hand-object alignment 接上。

## My Take

`ArtHOI` 给我的感觉是：这不是那种“一个优雅的新 backbone 解决一切”的论文，而是一篇很典型、也很有现实意义的 **systems paper for hard vision problems**。它承认 monocular articulated HOI reconstruction 太病态，单一模型很难直接吃掉，于是选择把多个 foundation-model priors 都调进来，再把研究重点放在“这些先验最容易错在哪里、怎样把它们拉回物理现实”。

我觉得这篇最值得记住的，不只是它做了单目 4D articulated HOI，而是它很好地展示了一种今天越来越常见的 research pattern：**foundation model 不是终点，而是原材料；真正的研究创新在于怎样把它们驯服成一个可信系统。** 放在 articulated object reconstruction + HOI 这条线上，它很像一个很自然的桥梁节点。

## Connections

- [[articulated-object-reconstruction-and-hoi]]
- [[articulated-object-reconstruction-real2sim]]
- [[2026-articulation-in-motion]]
- [[2026-articulated-reconstruction-transformer]]
- [[2025-taste-rob]]
- [[2025-object-centric-3d-motion-field]]
- [[ai-and-robotics-data]]
- [[literature-review]]
- [[overview]]

## Sources

- Paper: https://arxiv.org/abs/2603.25791
- Project: https://arthoi-reconstruction.github.io/
- Code/Data page: https://arthoi-reconstruction.github.io/
