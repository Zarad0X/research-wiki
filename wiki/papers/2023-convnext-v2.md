---
title: ConvNeXt V2
kind: paper
summary: A 2023 paper that co-designs ConvNet architecture and masked autoencoding, showing that modern convolutional backbones can keep improving when representation learning and architecture are optimized together.
status: active
source_count: 2
updated: 2026-04-07
---

# ConvNeXt V2

## Summary

`ConvNeXt V2` 很适合放在 Saining Xie 的代表作序列里，因为它不是简单给 `ConvNeXt` 打一个续集，而是把 `architecture` 和 `representation learning` 真正绑在一起重新做。它的味道很典型：不是为了叠更多系统复杂度，而是把“现代 ConvNet 怎么和 masked modeling 更自然地配合”这个问题做干净。

## Story / Setting

- `ConvNeXt` 已经证明现代化后的 ConvNet 仍然很强
- `MAE` 证明 masked autoencoding 是视觉预训练的重要 recipe
- 但直接把这两者拼起来，效果并不理想

## Why This Exists

- 想解决“强 architecture + 强 pretraining objective”并不自动兼容的问题
- 想让 ConvNet 也能真正吃到 masked autoencoding 的红利
- 想继续证明卷积 backbone 不是只能活在旧监督学习范式里

## Related Work

- [[2022-convnext]] 重新梳理了现代 ConvNet design space
- [[2022-mae]] 把 masked autoencoding 做成了视觉预训练主线
- `ConvNeXt V2` 的位置是把这两条路真正 co-design 到一起

## First Principles

- architecture 和 pretraining objective 不应被视为两个独立模块
- 如果表征学习目标和 backbone inductive bias 不匹配，再强的方法也会打折
- 真正高杠杆的改进，常常来自 jointly designing the recipe

## Problem

- 为什么 `ConvNeXt + MAE` 的直接组合效果不够理想
- 如何让 ConvNet 在 masked modeling 框架里获得更强、更稳定的收益

## Main Idea

- 共同调整 masked autoencoder recipe 和 ConvNeXt 架构
- 引入 fully convolutional masked autoencoder
- 加入 `Global Response Normalization (GRN)`，增强通道间竞争

## Core Architecture

- backbone 仍以 ConvNeXt 系列为核心
- masked autoencoding 被改写得更贴合 convolutional structure
- `GRN` 成为很关键的架构小部件，用来改善特征交互

## Method

- 论文核心不是单个 trick，而是 `co-design`
- 一方面改 pretraining framework，让其适配 ConvNet
- 一方面改 backbone，让其更适配 masked representation learning

## Experimental Setup

- 主要验证分类、检测、分割等标准视觉 benchmark
- 比较对象包括原始 ConvNeXt 和其他现代 backbone

## Results

- 论文报告 `ConvNeXt V2` 在 ImageNet、COCO、ADE20K 等任务上带来明显提升
- 更重要的是，它证明了 ConvNet 与 masked modeling 的组合不是死路，而是需要正确的 recipe

## Strengths

- 很典型的 “clean follow-up” work：不是硬加东西，而是把上一代工作里没完全打通的地方真正打通
- 同时强化了 `ConvNeXt` 和 `MAE` 两条主线
- 很符合 Saining Xie 一贯的 taste：让基础件再变得更稳、更自然

## Limitations

- 它仍然主要是视觉 backbone work
- 不是那种直接定义 multimodal 或 world-model 系统边界的论文

## Questions

- `ConvNeXt V2` 的长期价值会不会更多来自 co-design 这个思路，而不是 `GRN` 这样的具体部件
- 在今天的 world-model / multimodal 系统里，还有哪些地方需要这种 architecture-objective co-design

## My Take

如果说 `ConvNeXt` 像是在说“ConvNet 还没过时”，那 `ConvNeXt V2` 更像是在说“而且它还能继续长”。这种 work 很能体现一种研究上的克制和耐心。

## Connections

- [[saining-xie]]
- [[representation-learning]]
- [[2022-convnext]]
- [[2022-mae]]
- [[saining-xie-research-taste-and-representative-works]]

## Sources

- Paper: https://arxiv.org/abs/2301.00808
- Homepage listing: [[saining-xie-homepage]]
