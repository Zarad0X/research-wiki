---
title: World Models
kind: topic
summary: A topic page tracking the evolution from latent imagined dynamics to foundation-scale interactive world simulators and world action models.
status: active
source_count: 4
updated: 2026-04-06
---

# World Models

## Summary

`world models` 这条线最核心的野心，是让系统先学会“世界如何变化”，再基于这种内部模拟去支持控制、规划、泛化与数据扩展。从 2018 年的 `World Models` 到 `Genie`、`DreamZero`、`LingBot-World`，这个方向的重心已经从小规模 latent dynamics 走向 foundation-scale 交互世界与可执行策略。

## Story Arc

- [[2018-world-models]]：定义经典想法，内部模拟可以成为控制 substrate
- [[2024-genie]]：把 world model 提升为 foundation interactive environment
- [[2026-dreamzero]]：把 world model 与 policy 合一，提出 `World Action Model`
- [[2026-lingbot-world]]：强调开源、长时域和实时交互的世界模拟基础设施

## Key Tensions

- 表征世界，还是直接控制世界
- 学 latent dynamics，还是学可交互视频与动作联合分布
- 更关注 planning substrate，还是直接作为 zero-shot policy
- 更关注 frontier demo，还是 open-source research infrastructure

## Comparison Axes

| Axis | World Models | Genie | DreamZero | LingBot-World |
| --- | --- | --- | --- | --- |
| Historical role | Defines imagined dynamics pipeline | Scales to foundation interactive environments | Recasts world models as policies | Pushes open-source long-horizon world simulation |
| Core substrate | Latent VAE + RNN | Video tokenizer + autoregressive dynamics + latent actions | Video diffusion + joint video/action modeling | Open video-generation-based world simulator |
| Main output | Compact latent rollouts | Action-controllable environments | Zero-shot robot policy via WAM | Real-time interactive simulated worlds |
| Primary value | Conceptual clarity | Unsupervised controllable world generation | Physical generalization in robotics | Open infrastructure and long-horizon interactivity |

## Relation To VLA

- VLA 更强调从 observation 到 action 的统一建模
- world model / WAM 更强调显式或隐式建模“世界如何随动作变化”
- 对 robotics 而言，这两条线现在越来越像会相互融合，而不是长期平行

## Open Questions

- world model 最终会是 planner、policy，还是训练数据引擎
- robotics foundation model 的主干会继续偏 VLA，还是逐渐转向 WAM
- 开放世界视频学习与真实可执行物理控制之间的 gap 该如何缩小

## Connections

- [[2018-world-models]]
- [[2024-genie]]
- [[2026-dreamzero]]
- [[2026-lingbot-world]]
- [[vision-language-action-models]]
- [[world-models-genie-dreamzero-lingbot-world]]

## Sources

- [[2018-world-models]]
- [[2024-genie]]
- [[2026-dreamzero]]
- [[2026-lingbot-world]]
