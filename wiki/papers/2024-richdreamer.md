---
title: RichDreamer
kind: paper
summary: A 2024 CVPR paper that uses a normal-depth diffusion prior to improve detail richness in text-to-3D, representing Xiaoguang Han's group at the strong 3D generation end of the spectrum.
status: active
source_count: 2
updated: 2026-04-07
---

# RichDreamer

## Summary

`RichDreamer` 很像 Xiaoguang Han 老师近年工作里“3D generation 极致一端”的代表作。它关心的不是能不能粗略生成一个 3D 形状，而是怎样把几何细节做得更稳定、更丰富。这里很能看出他组的一种倾向：即使做生成，也还是很在乎 normal / depth 这类和几何结构紧密相关的中间表示。

## Story / Setting

- text-to-3D 很热，但质量瓶颈一直在几何细节与稳定性
- 纯 2D diffusion prior 往往很难给出足够可靠的 3D 几何约束

## Why This Exists

- 想让 text-to-3D 的结果不只是“看起来像”，而是真有更细的几何结构
- 想把与几何更贴近的 normal/depth prior 引进来

## Related Work

- DreamFusion 一类 text-to-3D 开创了路线
- 但细节丰富度和几何稳定性始终是难点
- `RichDreamer` 的位置是用更结构化的 diffusion prior 去补这一层

## First Principles

- 如果中间表示更接近几何结构，生成出来的 3D 结果就更容易稳定
- 高质量 3D generation 不能只靠像素幻觉，还需要更强的结构先验

## Problem

- text-to-3D 生成细节不足
- 结果在 normal / depth 维度上不够稳定

## Main Idea

- 引入 generalizable 的 normal-depth diffusion model
- 用它提升 text-to-3D 的细节丰富度和几何一致性

## Core Architecture

- 核心不是单一 3D backbone，而是把 normal/depth prior 纳入生成流程
- 让几何结构信号在生成中更有话语权

## Method

- 使用 normal / depth diffusion prior 辅助 3D generation
- 提升几何细节和整体稳定性

## Experimental Setup

- 主要在 text-to-3D 任务上验证
- 对比其他使用 2D prior 的方法

## Results

- 论文与项目页强调 detail richness 和更可靠的几何质量
- 在 Xiaoguang Han 近年的版图里，这篇很适合作为 3D generation 代表作锚点

## Strengths

- 把生成质量问题重新表述成结构先验问题
- 很符合“做生成但仍然重视几何表示”的路线

## Limitations

- 仍然属于 3D content generation，而不是 interaction 或 robotics
- 最终效果仍依赖 text-to-3D 整体管线

## Questions

- normal/depth prior 是否会成为更多 3D generation 系统的标准配置
- 这类结构先验能不能继续长到交互式 3D world modeling

## My Take

如果你想看 Han 老师组在 2024 年把 3D 生成推到什么程度，`RichDreamer` 很值得先看。它很能代表那种“生成也要讲几何纪律”的味道。

## Connections

- [[xiaoguang-han]]
- [[3d-generation]]
- [[2024-trellis]]
- [[xiaoguang-han-recent-papers-2024-2025]]

## Sources

- Paper: https://arxiv.org/abs/2311.16918
- Faculty listing: [[xiaoguang-han-cuhksz-faculty-page]]
