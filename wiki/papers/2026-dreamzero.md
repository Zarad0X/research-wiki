---
title: DreamZero
kind: paper
summary: A 2026 world action model paper that argues predictive video-and-action modeling can serve directly as zero-shot robot policy.
status: active
source_count: 1
updated: 2026-04-06
---

# DreamZero

## Summary

`DreamZero` 的核心主张非常激进也非常有趣：world action model 本身就可以是 zero-shot policy。相比传统 VLA 更强调语义对齐，它把重点转向“通过联合预测未来视频和动作来真正学物理 dynamics”，然后直接把这个生成模型拿来闭环控制。

## Story / Setting

在 VLA 路线已经证明语义泛化很强之后，一个越来越明显的问题是：这些模型在陌生环境里的新物理运动泛化并不够强。DreamZero 的故事就是从这个 tension 出发的，它说我们可能不该只学“看到什么就输出什么动作”，而应该学“世界和动作如何一起演化”。

## Why This Exists

- SOTA VLA 的 semantic generalization 强，但对新物理运动和新环境的泛化不足
- 纯 action prediction 可能没有真正学到环境 dynamics
- video generation backbone 已经足够强，可能适合作为 control substrate

## Related Work

- 一边接在 `World Models` 和 `Genie` 这条世界建模主线上
- 一边又直接与 `RT-2`、`OpenVLA`、`pi_0` 这类 VLA 路线形成对照
- 它提出的 `World Action Model (WAM)` 可以看作 world model 和 policy model 更深的融合

## First Principles

如果策略真的理解物理世界，它不应只会输出下一个动作，而应该能同时预测“世界接下来会变成什么样”以及“什么动作会让它这样变化”。

## Problem

- 如何超越 VLA 对未见物理运动的泛化瓶颈
- 如何把 world modeling 直接转化为可执行 policy
- 如何让大型视频生成模型进入 real-time closed-loop control

## Main Idea

- 用预训练视频 diffusion backbone 构建 world action model
- 联合预测未来 world states 和 actions
- 把生成式世界预测能力直接作为 zero-shot policy substrate

## Core Architecture

- `Pretrained Video Diffusion Backbone`
- `Joint Video-and-Action Modeling`
- `Real-time Closed-loop Control Stack`

## Method

- 在 heterogeneous robot data 上学习视频与动作联合分布
- 通过系统优化让 14B autoregressive video diffusion model 跑到 7Hz closed-loop control
- 探索 video-only demonstrations 与 cross-embodiment transfer

## Experimental Setup

- 实机对比 state-of-the-art VLA
- 关注新任务、新环境和 cross-embodiment generalization
- 还测试了人类或其他机器人视频演示的迁移能力

## Results

- arXiv 摘要报告：相对 SOTA VLA，在真实机器人实验里对新任务和新环境的泛化提升超过 2x
- 只用 10 到 20 分钟数据，来自其他机器人或人类的视频演示可带来超过 42% 的未见任务性能相对提升
- 对新 embodiment，只用 30 分钟 play data 即可实现 few-shot adaptation，同时保留 zero-shot generalization

## Strengths

- 明确提出 `WAM`，概念上很强
- 把 world model 与 policy 之间的边界推得很近
- 对 robotics 很关键的一点是，它把“物理泛化”摆到中心位置

## Limitations

- 系统复杂，训练与部署门槛都很高
- 7Hz 已经很 impressive，但对某些高频控制场景仍然有限
- 这条路线是否稳定、是否容易复现，还要看后续社区验证

## Questions

- WAM 会不会成为 VLA 之后的新主流抽象
- DreamZero 的优势主要来自视频 backbone、联合建模，还是更大更杂的数据
- world model 直接当 policy，用起来会不会比显式 planning 更脆弱

## My Take

DreamZero 很像 robotics foundation model 叙事的一次重心转移。它不再满足于“语义上更懂”，而是强调“要在陌生物理世界里也更会动”。如果这条线成立，后续很多对比就不再是 VLA 内部小修小补，而是 VLA vs WAM。

## Connections

- [[world-models]]
- [[2018-world-models]]
- [[2024-genie]]
- [[2026-lingbot-world]]
- [[vision-language-action-models]]
- [[2024-openvla]]
- [[2024-pi-0]]
- [[world-models-genie-dreamzero-lingbot-world]]

## Sources

- Paper: https://arxiv.org/abs/2602.15922
- Project: https://dreamzero0.github.io/
