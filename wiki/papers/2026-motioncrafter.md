---
title: MotionCrafter
kind: paper
summary: A 2026 paper on dense geometry and motion reconstruction from monocular video with a 4D VAE, extending Xiaoguang Han's group's recent work toward dynamic 4D reconstruction and motion understanding.
status: active
source_count: 2
updated: 2026-04-07
---

# MotionCrafter

## Summary

`MotionCrafter` 是 Xiaoguang Han 老师最近这条线里很值得注意的一篇，因为它把问题从静态 3D 直接推到了 `4D geometry + dense motion`。如果说前面的 `RichDreamer / IPoD / Stable-SCore` 还更多在做静态结构，那么 `MotionCrafter` 已经开始处理动态世界里的几何和运动联合重建。

## Story / Setting

- monocular video 下的动态几何和运动重建一直很难
- 过去常常要依赖 post-optimization，或者把 geometry latent 硬对齐到 RGB VAE latent

## Why This Exists

- 想从 monocular video 直接联合恢复 4D geometry 和 dense motion
- 想避免 RGB latent 和 3D latent 强行对齐带来的次优效果

## Related Work

- 动态场景重建、scene flow estimation、4D reconstruction 各自都有积累
- `MotionCrafter` 的贡献在于用一个 shared representation 和 `4D VAE` 把 dense geometry 与 motion 统一起来

## First Principles

- 几何和运动本来就是耦合的，不应完全分开建模
- 3D/4D latent 的统计分布不一定应该强行与 RGB latent 对齐

## Problem

- monocular video 下同时重建 geometry 和 motion 难度很高
- 现有 latent alignment 设计并不总是合理

## Main Idea

- 提出 shared coordinate system 下的 joint representation
- 用 `4D VAE` 学习 dense 3D point maps 与 3D scene flows
- 用新的 normalization 与 VAE training strategy 更好迁移 diffusion prior

## Core Architecture

- 共享坐标系中的 geometry + scene flow representation
- `4D VAE` 作为核心表示学习模块
- diffusion-based reconstruction framework

## Method

- 从 monocular video 学习联合表示
- 通过新的 normalization / training strategy 改善 4D latent 学习
- 最终同时输出 geometry reconstruction 和 dense motion estimation

## Experimental Setup

- 覆盖多种数据集
- 评测 geometry reconstruction 与 dense scene flow estimation

## Results

- arXiv 摘要报告 geometry 与 motion reconstruction 分别提升 `38.64%` 和 `25.0%`
- 且无需 post-optimization

## Strengths

- 明显把 Han 老师组的路线从静态 3D 推向动态 4D
- 问题设定本身就更接近 interaction、motion、甚至 embodied scenes

## Limitations

- 仍然主要是 reconstruction / estimation，而不是 control 或 robotics policy
- 4D 任务本身门槛更高

## Questions

- `4D VAE` 这类表示会不会成为后续动态世界建模的重要中间层
- Han 老师组会不会把这条 4D motion 线继续接到 interaction 或 robotics 上

## My Take

`MotionCrafter` 很值得看，因为它透露出一个很重要的方向变化：Han 老师组已经不满足于高质量静态 3D，而是开始认真碰“动态世界怎么表示”。

## Connections

- [[xiaoguang-han]]
- [[3d-generation]]
- [[2025-taste-rob]]
- [[xiaoguang-han-recent-papers-2024-2025]]

## Sources

- Paper: https://arxiv.org/abs/2602.08961
- Project: https://ruijiezhu94.github.io/MotionCrafter_Page
- Faculty listing: [[xiaoguang-han-cuhksz-faculty-page]]
