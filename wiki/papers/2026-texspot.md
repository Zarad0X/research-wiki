---
title: TexSpot
kind: paper
summary: A 2026 paper on 3D texture enhancement using a spatially-uniform point latent representation, extending Xiaoguang Han's group's 3D generation line into higher-fidelity texture modeling.
status: active
source_count: 2
updated: 2026-04-07
---

# TexSpot

## Summary

`TexSpot` 是 Xiaoguang Han 老师最近这条 3D generation 线继续细化的一篇。它盯的不是粗几何，而是更难处理的 `3D texture enhancement`。这很重要，因为很多 3D 生成系统几何已经够像了，但纹理在跨视角一致性和高分辨率细节上仍然很脆弱。

## Story / Setting

- 当前主流 multi-view diffusion pipeline 在纹理上容易出现 view inconsistency
- UV map 有展开畸变问题
- point-based texture 表示又容易把纹理质量绑死在几何点密度上

## Why This Exists

- 想提升 3D texture fidelity 和跨视角一致性
- 想找到比 UV 或普通 point texture 更合适的中间表示

## Related Work

- 许多 3D generation 系统更重形状而轻纹理
- 现有纹理表示要么畸变，要么不利于高分辨率纹理建模
- `TexSpot` 的 distinct point 是提出 `Texlet` 这种更平衡的 latent representation

## First Principles

- 纹理表示既需要局部 patch fidelity，也需要全局 shape context
- 如果 latent representation 本身更均匀、更适配纹理任务，后续 enhancement 才可能真正稳定

## Problem

- 3D texture enhancement 在 view consistency 和高分辨率细节上困难很大
- UV-based 和 point-based 两类表示各有明显缺陷

## Main Idea

- 提出 `Texlet`，一种 spatially-uniform point latent representation
- 用 diffusion transformer 在 Texlet space 里做 texture refinement 和 enhancement

## Core Architecture

- 每个 Texlet latent 编码一个局部 texture patch
- 2D encoder 负责 patch 级表示
- 3D encoder 聚合全局 shape context
- 3D-to-2D cascaded decoder 重建高质量纹理 patch

## Method

- 学习 Texlet latent space
- 训练 diffusion transformer 条件在 Texlets 上
- 用于增强多视图 diffusion 方法生成的纹理

## Experimental Setup

- 面向 3D texture generation / enhancement 任务
- 对比现有纹理增强和 3D texture generation baselines

## Results

- arXiv 摘要显示其在 visual fidelity、geometric consistency 和 robustness 上都有优势
- 对 Han 老师组而言，这篇说明他们在 3D generation 这条线上已经开始细抠更难的 texture layer

## Strengths

- 很明确地把 texture 问题抽象成 representation 问题
- 延续了 Han 老师组对 3D 表示设计的关注

## Limitations

- 仍然聚焦在 texture enhancement，不直接触及 interaction 或 motion
- 它更像 3D asset quality work，而不是 embodied 方向

## Questions

- `Texlet` 这类表示能不能被更多 3D foundation model 吸收
- texture-level representation 是否会成为 3D generation 下一轮关键瓶颈

## My Take

`TexSpot` 让我更确定 Han 老师组并不是只在追大而泛的 3D 叙事，而是在持续往细粒度、高质量、可用的 3D 表示上深挖。

## Connections

- [[xiaoguang-han]]
- [[3d-generation]]
- [[2024-richdreamer]]
- [[2025-reconviagen]]
- [[xiaoguang-han-recent-papers-2024-2025]]

## Sources

- Paper: https://arxiv.org/abs/2602.12157
- Faculty listing: [[xiaoguang-han-cuhksz-faculty-page]]
