---
title: Stable-SCore
kind: paper
summary: A 2025 CVPR paper on stable registration-based 3D shape correspondence, representing Xiaoguang Han's group's geometry-heavy line focused on robustness and real applications.
status: active
source_count: 2
updated: 2026-04-07
---

# Stable-SCore

## Summary

`Stable-SCore` 很能代表 Xiaoguang Han 老师组最近的一种“几何硬功夫”路线。它不是 flashy 的生成 demo，而是在 3D shape correspondence 这个基础又实用的问题上，重新把 registration-based 方法做稳。对你如果偏好扎实、能落地的 3D work，这篇会很值得看。

## Story / Setting

- 3D shape correspondence 是视觉和图形里的基础问题
- 现有 dominant 方法在真实场景下常受非等距变形、预对齐质量等影响

## Why This Exists

- 想让 correspondence 在更复杂、更真实的场景里稳定工作
- 想重新挖掘 registration-for-correspondence 这条路线的潜力

## Related Work

- functional map 类方法在受控场景表现强
- 但 registration-based 方法在真实应用里仍有价值，只是常常不够稳
- `Stable-SCore` 的思路是借助更可靠的 2D correspondence 来引导 3D registration

## First Principles

- correspondence 的价值不只在 benchmark，而在后续 re-topology、shape transfer、interpolation 等真实应用
- 稳定性往往比单次最优数字更重要

## Problem

- registration-based correspondence 容易不稳定
- 往往还依赖很好的初始对齐或高质量 3D correspondences

## Main Idea

- 重新利用 registration-for-correspondence 的思路
- 用 foundation-style 的 2D character correspondence 作为稳定引导
- 提出 `Semantic Flow Guided Registration`

## Core Architecture

- 2D correspondence 模块提供更可靠的语义匹配
- 3D mesh deformation / registration 在其引导下进行
- 整体目标是稳定 correspondence estimation

## Method

- 先获得稳定的 2D mapping
- 再把 2D 语义流引入 3D registration
- 最终提高 3D correspondence 的稳定性

## Experimental Setup

- 面向更复杂的 character / shape correspondence 场景
- 强调真实应用挑战，而不只是理想条件

## Results

- arXiv 摘要显示其在 challenging scenarios 下显著优于现有方法
- 同时展示了更多真实应用可能性

## Strengths

- 问题很基础，但很重要
- 很体现 Han 老师组“几何稳健性”这一面
- 不追表面热闹，重视稳定可用的结构能力

## Limitations

- 题目更偏 correspondence / registration，离 embodied interaction 有距离
- 对非几何方向读者来说，入口门槛可能比生成类论文更高

## Questions

- 这条 registration-based correspondence 路线会不会在 avatar / animation 等应用里继续放大影响
- 2D foundation correspondence 对 3D 几何问题的帮助还能扩到哪些地方

## My Take

如果你想看 Han 老师组最近不是只有生成方向在发力，`Stable-SCore` 很能说明问题。这类 work 往往最能体现一个组的技术底盘。

## Connections

- [[xiaoguang-han]]
- [[3d-generation]]
- [[xiaoguang-han-recent-papers-2024-2025]]

## Sources

- Paper: https://arxiv.org/abs/2503.21766
- Faculty listing: [[xiaoguang-han-cuhksz-faculty-page]]
