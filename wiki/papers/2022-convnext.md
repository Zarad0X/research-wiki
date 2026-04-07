---
title: ConvNeXt
kind: paper
summary: A 2022 architecture paper that re-examines ConvNet design through the lens of modern training and transformer-era practices, making convolutional backbones strong and clean again.
status: active
source_count: 2
updated: 2026-04-07
---

# ConvNeXt

## Summary

`ConvNeXt` 是非常能体现 Saining Xie taste 的 work，因为它没有顺着“Transformer 赢了，所以 ConvNet 过时了”这条最省事的结论走，而是重新问了一遍：如果把现代训练经验、设计选择和 scaling 逻辑认真用回 ConvNet，会发生什么。答案是，ConvNet 不仅没死，还能变得非常强。

## Story / Setting

- Vision Transformer 崛起之后，很多人默认 ConvNet 已经落后
- 但这里面混杂了 architecture、training recipe、data scale 等多种变量

## Why This Exists

- 想分清楚到底是卷积本身落后，还是旧版 ConvNet recipe 落后
- 想重新整理 ConvNet design space，让其在现代条件下竞争

## Related Work

- `ResNet`、`ResNeXt` 是传统 ConvNet 代表
- ViT 提供了新时代 baseline
- `ConvNeXt` 的位置像一次系统性的“公平重跑”

## First Principles

- 一个范式看起来被替代，不一定说明其 core primitive 不行，可能只是 recipe 落后
- 好研究不一定总是发明新范式，也可以重新证明旧范式在正确设计下仍有生命力

## Problem

- ConvNet 是否真的在现代视觉任务中不如 Transformer
- 如果要让 ConvNet 重新强起来，哪些设计元素最关键

## Main Idea

- 系统吸收 transformer-era 的训练和结构经验
- 在保持卷积主干的前提下，重新设计 block、stage、normalization 和 macro architecture
- 把 ConvNet 带回现代竞争力前线

## Core Architecture

- 仍是卷积 backbone
- 但 block 和整体设计经过全面现代化调整
- 强调简单统一的设计，而不是杂乱叠加技巧

## Method

- 对传统 ConvNet recipe 逐步现代化
- 在标准视觉任务上与 ViT 等现代模型比较

## Experimental Setup

- 主要是 ImageNet 及常见下游视觉 benchmark
- 强调 architecture comparison 的系统性

## Results

- `ConvNeXt` 证明了现代化后的 ConvNet 可以与 Transformer 直接竞争
- 它也改变了社区对“什么算落后 backbone”的判断

## Strengths

- 研究问题很干净，结论也很有解释力
- 不是追热点，而是重新清理 design space
- 很符合“优雅”与“长期高杠杆”两个标准

## Limitations

- 更偏 architecture rethinking，而不是提出全新学习范式
- 对非视觉领域的直接迁移意义没那么直接

## Questions

- `ConvNeXt` 真正改变的，是性能格局还是研究者对 design space 的信心
- 为什么这种“回头重做旧范式”的工作往往特别容易显出 research taste

## My Take

如果说 `MAE` 是把 pretraining principle 做对了，`ConvNeXt` 则是把 architecture design space 重新做对了。两者合起来很能说明 Saining Xie 为何会给人“work 很优雅”的感觉。

## Connections

- [[saining-xie]]
- [[representation-learning]]
- [[2017-resnext]]
- [[2022-mae]]
- [[2023-dit]]
- [[saining-xie-research-taste-and-representative-works]]

## Sources

- Paper: https://arxiv.org/abs/2201.03545
- Homepage listing: [[saining-xie-homepage]]
