---
title: Cambrian-1
kind: paper
summary: A 2024 fully open, vision-centric MLLM paper that treats multimodal systems as a way to evaluate and improve visual representations rather than as language systems with image inputs attached.
status: active
source_count: 2
updated: 2026-04-07
---

# Cambrian-1

## Summary

`Cambrian-1` 是理解 Saining Xie 近年 research taste 的关键 paper，因为它把他长期的 `representation-first` 取向明确带进了多模态系统。它的核心态度不是“拿一个更强的 LLM 再接个视觉塔就行”，而是反过来问：如果我们真正在乎 visual grounding，多模态系统应该怎样尊重视觉表示学习本身。

## Story / Setting

- 多模态 LLM 快速变热，很多系统都默认语言模型是主轴
- 视觉部分经常被当作 connector engineering 的附属品
- 这让来自视觉表示学习的许多问题被遮蔽了

## Why This Exists

- 想把 multimodal systems 重新拉回 vision-centric 视角
- 想系统比较不同视觉表示在 MLLM 场景下的作用
- 想把“更好的 visual grounding”做成开放、可复用的 cookbook

## Related Work

- 许多 MLLM 更强调更强的 language model 与 instruction tuning
- `Cambrian-1` 的 distinctive point 是重新把视觉 encoder 选择、视觉 token 聚合、视觉数据配方放回中心

## First Principles

- 多模态能力不应只被理解成“语言模型会不会答题”
- 如果视觉表示层不扎实，系统的真实视觉 grounding 就会很脆弱
- 视觉组件不是附件，而是系统智能边界的重要来源

## Problem

- 当前 MLLM 对 vision component 的研究不够系统
- benchmark 和评测也常常不足以反映视觉 grounding 的真实质量
- 高分辨率视觉特征与 LLM interface 之间仍有结构性摩擦

## Main Idea

- 做一个 fully open、vision-centric 的 MLLM family
- 系统比较 20+ 视觉 encoder
- 提出 `Spatial Vision Aggregator (SVA)`，更好地整合高分辨率视觉特征
- 同时强调 visual instruction-tuning data 的配方设计

## Core Architecture

- LLM 仍作为接口层存在
- 但设计重点放在 vision encoder、视觉 token 聚合和视觉信息保真
- `SVA` 是很关键的 connector / aggregator 设计

## Method

- 用 instruction-tuned MLLM 作为接口来评估不同视觉表示
- 建立 vision-centric benchmark 与 recipe
- 发布模型、代码、工具和数据流程

## Experimental Setup

- 对比多种视觉 encoder 和架构
- 在多种 multimodal benchmark 上评测
- 还提出 `CV-Bench` 来更明确地衡量视觉能力

## Results

- 论文报告 `Cambrian-1` 达到很强的开源多模态表现
- 但更重要的结果是：它把视觉表示学习的洞察重新带回 MLLM 设计讨论

## Strengths

- 很清楚地表达了 `vision-centric` 立场
- 不只是做模型，也像在写一份多模态 cookbook
- 非常适合拿来理解 Saining Xie 为什么会对 language-first 叙事保持距离

## Limitations

- 虽然批评语言中心主义，但系统层仍需借助 LLM interface
- 它更像是重新平衡多模态设计重心，而不是完全脱离当前 MLLM 范式

## Questions

- `Cambrian-1` 是否会成为从 language-centric MLLM 转向 more grounded multimodal systems 的重要过渡点
- 这种 vision-centric 取向，未来会如何继续延伸到 world models

## My Take

`Cambrian-1` 很像 Saining Xie 这条研究轨迹的一个公开宣言：即使在最热的 MLLM 叙事里，他依然会把 attention 拉回 representation 和 visual grounding 本身。

## Connections

- [[saining-xie]]
- [[representation-learning]]
- [[2023-dit]]
- [[world-models]]
- [[saining-xie-research-taste-and-representative-works]]

## Sources

- Paper: https://arxiv.org/abs/2406.16860
- Homepage listing: [[saining-xie-homepage]]
