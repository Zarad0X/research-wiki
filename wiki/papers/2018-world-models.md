---
title: World Models
kind: paper
summary: The 2018 paper that crystallized the world-model idea by learning compact latent dynamics and training a small controller inside imagined rollouts.
status: active
source_count: 1
updated: 2026-04-06
---

# World Models

## Summary

`World Models` 是这条线里最经典的起点之一。它把“先学环境模型，再在模型里学策略”这件事用非常清晰、几乎是教学级的方式讲通了，并且用极简 controller 展示：如果 latent world model 足够好，policy 本身可以非常小。

## Story / Setting

这篇文章出现时，强化学习里大家已经很熟悉 model-free 路线的样本效率问题。作者想讲的是：智能体不一定要直接在原始像素和真实环境里硬学动作，也可以先学会“想象世界如何变化”，再把决策建立在这种想象上。

## Why This Exists

- model-free RL 往往数据昂贵、训练慢
- 真实交互成本高，而想象 rollout 很便宜
- 如果能把世界压缩成一个可预测的 latent dynamics，控制问题可能会大幅简化

## Related Work

- 接在 model-based RL 和 latent dynamics modeling 传统之后
- 但它的表达方式更像是把 world model 变成一个完整 cognitive stack：`V + M + C`
- 对后来的 dreamer、video world model、robotics world model 影响都很深

## First Principles

先把“世界是什么”学出来，再去学“该怎么做”。如果一个系统能在内部预测未来，它就能在真正行动之前先在脑中试错。

## Problem

- 如何从高维像素 observation 中学到压缩表征
- 如何建模 latent dynamics
- 如何让 policy 在 imagined environment 里训练后仍能转移回真实环境

## Main Idea

- 用 VAE 学视觉压缩表示
- 用 RNN 混合密度模型学 latent dynamics
- 用一个很小的 controller 只基于 latent state 做决策
- 甚至可以完全在 hallucinated dream 里训练 controller

## Core Architecture

- `V`: Variational Autoencoder，负责把图像压缩成 latent code
- `M`: Mixture Density Network + RNN，负责预测 latent dynamics
- `C`: Compact Controller，负责从 latent state 输出 action

## Method

- 先分别训练 V 和 M
- 再固定世界模型，用 evolutionary strategy 优化 controller
- 在 CarRacing 和 VizDoom 场景中验证 imagined training 的可行性

## Experimental Setup

- 环境主要包括 CarRacing-v0 和 VizDoom Take Cover
- 重点不是大规模 benchmark，而是证明 world model pipeline 本身能工作
- 一个重要实验是直接在 dream environment 中训练 policy，再迁回真实环境

## Results

- 论文展示了很小的 controller 也能在 learned latent space 中解决任务
- 在 VizDoom 实验中，作者展示了 purely imagined training 也可以迁移回真实环境

## Strengths

- 思想极其清晰，结构非常可解释
- 把 world model 从抽象概念变成可运行 pipeline
- 对后来的想象式训练、latent planning、video world models 影响很大

## Limitations

- 环境相对简单，离真实机器人和开放世界很远
- latent dynamics 的建模能力有限，长时域复杂交互能力不强
- 更多是“定义思路”的 landmark paper，而不是今天直接能拿来做 robotics foundation model 的方案

## Questions

- 什么时候 world model 更像是辅助表征，什么时候它真的能承担 planning substrate
- 在复杂接触动力学和开放世界中，早期 latent-RNN world model 的瓶颈在哪里
- 后来的 video diffusion world model 与这个经典框架之间，哪些是本质延续，哪些是范式变化

## My Take

这篇 paper 最值得反复看的是它的“认知结构感”。很多后续论文模型更大、更强，但未必比它更清楚地说明：为什么 internal simulation 会帮助 decision making。

## Connections

- [[world-models]]
- [[2024-genie]]
- [[2026-dreamzero]]
- [[2026-lingbot-world]]
- [[vision-language-action-models]]
- [[world-models-genie-dreamzero-lingbot-world]]

## Sources

- Paper: https://arxiv.org/abs/1803.10122
- Project: https://worldmodels.github.io/
