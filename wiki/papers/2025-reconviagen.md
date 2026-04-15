---
title: ReconViaGen
kind: paper
summary: A 2025 paper on accurate multi-view 3D object reconstruction via generation, showing how Xiaoguang Han's group tries to fuse reconstruction priors with generative priors instead of treating them as separate camps.
status: active
source_count: 2
updated: 2026-04-07
---

# ReconViaGen

## Summary

`ReconViaGen` 很值得放进 Xiaoguang Han 老师最近这条线里，因为它非常清楚地体现了一个趋势：`reconstruction` 和 `generation` 不再是两派各做各的，而是开始被认真地融合。对 Han 老师组来说，这篇不像单纯“做一个更强生成模型”，而更像是在问：生成先验到底能不能真正服务准确的 3D reconstruction。

## Story / Setting

- 多视图 3D 重建在真实场景里常常面临视角重叠不足、遮挡和 coverage 稀疏
- diffusion-based 3D generation 似乎提供了补全不可见部分的希望
- 但 generative prior 天生又带来 stochastic inconsistency 问题

## Why This Exists

- 想把 reconstruction 和 generation 真正接起来
- 想让 generative prior 帮助补全 3D 结构，而不是只产生“看起来合理”的 hallucination

## Related Work

- 传统 multi-view reconstruction 更依赖几何和视图一致性
- 3D generative methods 则更擅长补全 unseen structure
- `ReconViaGen` 的位置是把两者系统化整合

## First Principles

- generative prior 的价值不应只是补出 plausible shape，而应受输入视图约束
- 生成如果不可控，就很难真正进入 reconstruction pipeline

## Problem

- 多视图重建在 sparse coverage 下容易不完整
- diffusion generation 虽然会补全，但经常和输入不一致

## Main Idea

- 把 reconstruction priors 融入 generative framework
- 分析并解决 cross-view connection 不足和 denoising controllability 差的问题

## Core Architecture

- 多视图条件特征提取
- generative reconstruction framework
- 多种策略共同增强全局结构与局部细节的一致性

## Method

- 从多视图输入中提取条件
- 把 3D generative prior 用于补全不可见部分
- 再通过更强的 cross-view constraints 和 controllability design 保证结果与输入一致

## Experimental Setup

- 主要针对 accurate multi-view 3D object reconstruction
- 比较对象包括传统 reconstruction 与 generative-based reconstruction baselines

## Results

- arXiv 摘要显示其在 global structure 和 local details 上都更一致、更准确
- 这篇的真正意义在于：它把“生成帮助重建”做成了更可信的 research direction

## Strengths

- 很好地连接了 Han 老师组的两条主线：3D reconstruction 和 generative prior
- 不是在 generation 与 reconstruction 二选一，而是在做融合

## Limitations

- 仍然聚焦 object reconstruction，不是完整世界或交互场景
- 生成与可控重建之间的 tension 依旧存在

## Questions

- 这条 reconstruction-via-generation 的路线，会不会成为后续 3D foundation models 的重要形态
- 它是否会进一步长到 robotics / embodied world modeling

## My Take

`ReconViaGen` 是一篇很适合当“中间桥梁”的论文。它不像 `RichDreamer` 那么偏生成，也不像 `IPoD` 那么偏重建，而是非常明确地站在两者中间。

## Connections

- [[xiaoguang-han]]
- [[3d-generation]]
- [[2024-richdreamer]]
- [[2024-ipod]]
- [[xiaoguang-han-recent-papers-2024-2025]]

## Sources

- Paper: https://arxiv.org/abs/2510.23306
- Project: https://jiahao620.github.io/reconviagen
- Faculty listing: [[xiaoguang-han-cuhksz-faculty-page]]
