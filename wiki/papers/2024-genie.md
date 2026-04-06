---
title: Genie
kind: paper
summary: DeepMind's 2024 paper that learns an action-controllable interactive environment from unlabeled internet videos, positioning Genie as a foundation world model.
status: active
source_count: 1
updated: 2026-04-06
---

# Genie

## Summary

`Genie` 把 world model 从“学 latent dynamics 辅助 agent”往前推了一大步，变成了可以直接生成可交互环境的 foundation world model。它最强的叙事点是：不需要真实动作标签，只用无标注互联网视频，也能学出可交互的 latent action space。

## Story / Setting

早期 world model 更多在较封闭环境里建模 dynamics，而 Genie 想回答的是：能不能直接从互联网视频中学出“可玩”的、可交互的世界生成器，从而为 agent 训练创造几乎无限的环境来源。

## Why This Exists

- 真实交互和环境构造成本高
- world model 如果只能在小环境里工作，扩展性有限
- 如果能从大规模无标注视频学习 controllable environments，agent training 的数据瓶颈会被重新定义

## Related Work

- 继承了 `World Models` 这条“学环境再学 agent”的主线
- 但从 latent-RNN world model 走向了 foundation-scale 视频建模
- 也为后续 Genie 2、Genie 3，以及 robotics world model 提供了生成式世界模拟的参考框架

## First Principles

如果模型真的理解了世界如何随动作变化，那它应该能在没有动作标签的情况下，从视频中反推出“潜在可控因素”，并允许用户在这个空间里交互。

## Problem

- 如何从无标注互联网视频里学出可交互环境
- 如何在没有 ground-truth actions 的情况下获得 action-controllable generation
- 如何让 world model 兼具多样性、可控性和可扩展性

## Main Idea

- 从无标注视频中学习一个生成式交互环境
- 用 latent action model 建立“用户交互”与未来帧演化之间的关系
- 通过 foundation-scale 视频建模获得丰富环境多样性

## Core Architecture

- `Spatiotemporal Video Tokenizer`
- `Autoregressive Dynamics Model`
- `Latent Action Model`

## Method

- 在无标注互联网视频上无监督训练
- 学习视频 token 序列的动力学
- 通过 latent action space 让用户可以逐帧与生成环境交互

## Experimental Setup

- Genie 规模为 11B 参数
- 输入可以是文本、合成图像、照片、草图等
- 重点评估其交互环境生成与 latent action controllability

## Results

- DeepMind 官方摘要将其描述为首个从无标注互联网视频训练得到的 generative interactive environment
- 模型可以生成大量可交互虚拟世界，并允许逐帧控制
- 学到的 latent action space 还能用于从未见过的视频中模仿行为

## Strengths

- 叙事非常强，把 world model 扩展成“环境生成基础设施”
- 无动作标签训练这一点很有启发性
- 为开放式 agent training 和 video-driven robotics imagination 提供了新想象空间

## Limitations

- 论文关注点更偏生成环境和 latent controllability，不直接等于机器人策略学习系统
- latent actions 的可解释性和稳定性仍有限
- 和真实物理世界、接触动力学之间还有很大鸿沟

## Questions

- 从视频反推出 latent actions，和真实可执行 actions 之间的 gap 如何弥合
- Genie 这种 foundation world model 如何真正接到 robotics policy learning
- 交互世界的 realism、多样性与可控性之间是否存在硬 tradeoff

## My Take

`Genie` 的重要性不只在性能，而在于它把 world model 的 ambition 提高了：不只是模拟一个小环境，而是把“可交互世界生成”当成基础模型问题。

## Connections

- [[world-models]]
- [[2018-world-models]]
- [[2026-dreamzero]]
- [[2026-lingbot-world]]
- [[world-models-genie-dreamzero-lingbot-world]]

## Sources

- Paper: https://arxiv.org/abs/2402.15391
- DeepMind publication: https://deepmind.google/research/publications/genie-generative-interactive-environments/
