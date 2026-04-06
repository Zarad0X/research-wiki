---
title: TRELLIS
kind: paper
summary: A 2024 paper on structured 3D latents that unifies flexible 3D decoding with strong text- and image-conditioned asset generation quality.
status: active
source_count: 3
updated: 2026-04-06
---

# TRELLIS

## Summary

`TRELLIS` 的关键价值不只是“生成高质量 3D”，而是提出了一种更像中间层基础设施的表示：`Structured LATent (SLAT)`。它试图同时抓住几何结构和外观信息，并保持输出格式的灵活性，让同一个 latent 可以被解码成 radiance fields、3D gaussians 和 meshes。对研究者来说，这篇文章的重要性在于它把“representation choice”重新拉回 3D generation 的中心。

## Story / Setting

近两年的 3D generation 一直在几个目标之间拉扯：质量要高、条件控制要强、输出格式要实用、编辑能力要灵活。但很多方法往往在表示层先做了强绑定，比如更偏某一种渲染或重建格式。`TRELLIS` 想讲的故事是：如果先把 3D asset 压到一个足够强、又足够通用的 structured latent 里，再做统一生成，很多下游解码和编辑能力就能一起打开。

## Why This Exists

- 现有 3D generation 方法常常在表示层被输出格式绑死
- 文本到 3D、图像到 3D、局部编辑往往各做各的，缺少统一 substrate
- 如果 latent 表示同时保留结构和视觉信息，就更可能兼顾质量、可控性和多格式输出

## Related Work

- 接在 text-to-3D / image-to-3D / generative reconstruction 这条更大的 3D generation 主线上
- 和只围绕单一 3D 表示优化的方法相比，它更强调统一 latent 与多格式解码
- 也能和最近大量“foundation model 做强特征抽取，再把 3D 任务压到统一表示空间”这类工作放在一起看

## First Principles

如果一个 3D asset 的核心信息真的被表示好了，那么下游输出成哪种 3D 格式不应该决定生成模型本身。表示层应该先抓住“结构 + 外观”的关键因子，再把解码留给不同 renderer / decoder。

## Problem

- 如何做一个既适合生成又适合解码到多种 3D 输出格式的 latent 表示
- 如何同时支持 text-conditioned 和 image-conditioned 3D asset generation
- 如何在大规模训练下兼顾细节质量、可扩展性和编辑能力

## Main Idea

- 提出统一的 `Structured LATent (SLAT)` 作为 3D asset 的中间表示
- 用 sparse 3D grid 承载结构信息，用 dense multiview visual features 承载外观信息
- 在这个 latent 空间里训练 rectified-flow transformer 进行生成
- 再把生成出的 latent 解码到不同 3D 表示，如 radiance fields、3D gaussians 和 meshes

## Core Architecture

- `SLAT`：由稀疏 3D 结构网格和稠密多视角视觉特征共同构成
- 强视觉 foundation model 提供多视角视觉特征
- `Rectified Flow Transformer` 负责在 SLAT 空间里做条件生成
- 多种 decoder 负责把同一 latent 转成不同 3D 输出格式
- 支持 local 3D editing，而不是只做一次性生成

## Method

- 先把大规模 3D asset 编码到统一的 structured latent 空间
- 在 latent 空间中训练大参数量的生成模型，而不是直接在最终 3D 表示上做生成
- 条件可以来自文本或图像
- 通过统一 latent 保持下游输出和编辑的灵活性

## Experimental Setup

- arXiv 摘要和 Microsoft Research 页面都提到，模型训练规模达到 2B 参数
- 使用约 500K 个多样化 3D objects 组成的大规模 3D asset dataset
- 支持 text-conditioned 和 image-conditioned generation
- 重点展示生成质量、多格式输出能力以及局部 3D 编辑能力

## Results

- 论文摘要报告其在 text/image conditioned 3D generation 上显著超过既有方法，包括相近规模的近期方法
- 同一 latent 可以灵活解码到 radiance fields、3D gaussians 和 meshes
- 论文特别强调 local 3D editing，这比很多只关注一次性生成的工作更实用

## Strengths

- 把 3D generation 的重点重新放回“统一表示”这个高杠杆位置
- 既考虑质量，也考虑实际输出格式和编辑工作流
- text-to-3D 和 image-to-3D 共用同一底层表示，叙事比较完整
- 大规模训练设置让它不只是一个小实验室原型

## Limitations

- 从摘要和项目页能看出它很强调整体能力，但具体每个下游 decoder 的误差来源还需要细读全文
- 多格式灵活性很吸引人，但工程复杂度也更高
- 它主要是 asset generation 路线，不直接回答物理可交互、可执行控制或 embodied semantics 等问题

## Questions

- `SLAT` 相比更简单的 latent 表示，真正的核心增益来自哪里
- 如果只关心某一种输出格式，统一 latent 是否依然值得
- local editing 的边界在哪里，是否真的能支撑复杂资产工作流
- 这条线和 3D understanding / 3D reconstruction / embodied world modeling 未来会如何交叉

## My Take

这篇 paper 给我的第一感觉是“它想做 3D generation 的表示层标准件”。很多论文把注意力放在生成器本身，但 `TRELLIS` 更像是在说：先把 latent 设计对，生成、解码、编辑三件事才有机会一起做好。对做 research wiki 来说，它也很适合作为 `3D Generation` 这条线的起点，因为它不是单点 trick，而是一个比较完整的方法论声明。

## Connections

- [[3d-generation]]
- [[literature-review]]

## Sources

- Archived source: `raw/papers/2026-04-06-trellis.md`
- Source link: https://arxiv.org/abs/2412.01506
- Microsoft Research page: https://www.microsoft.com/en-us/research/publication/structured-3d-latents-for-scalable-and-versatile-3d-generation/
- GitHub: https://github.com/microsoft/TRELLIS
