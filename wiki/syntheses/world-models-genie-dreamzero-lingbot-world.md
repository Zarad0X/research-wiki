---
title: World Models vs Genie vs DreamZero vs LingBot-World
kind: synthesis
summary: A first-pass synthesis of how four papers mark different phases in the world-model research trajectory.
status: active
source_count: 4
updated: 2026-04-06
---

# World Models vs Genie vs DreamZero vs LingBot-World

## Summary

这四篇 paper 最好不要只按“性能更强”来理解。更有用的读法是：它们分别代表了 world model 研究里四种不同 ambition。

## The Four Moves

- [[2018-world-models]]：证明 internal simulation 可以帮助决策
- [[2024-genie]]：把 world model 提升成可交互环境生成基础模型
- [[2026-dreamzero]]：把 world model 直接推进成 zero-shot policy
- [[2026-lingbot-world]]：把高能力 world simulator 往开源基础设施推进

## A Useful Reading Lens

- `World Models` 关注的是 cognitive structure
- `Genie` 关注的是 unsupervised controllable world generation
- `DreamZero` 关注的是 world model 对 robot policy 的直接替代性
- `LingBot-World` 关注的是 capability + openness + long-horizon serving

## What Changed Over Time

- 世界建模从 latent dynamics 走向 foundation video generation
- 目标从“辅助 agent”走向“直接就是 control substrate”
- 评价标准从小环境任务成功率，逐渐走向可交互性、长时域一致性、cross-embodiment transfer 和实时闭环控制

## Why This Matters For Your Reading

- 如果你想看思想起点，先读 [[2018-world-models]]
- 如果你想看“世界模型为什么忽然又变热”，重点看 [[2024-genie]]
- 如果你关心 robotics 和 policy learning，重点读 [[2026-dreamzero]]
- 如果你关心开源平台和下一代实验环境，补 [[2026-lingbot-world]]

## Cross-Cluster Insight

和前面的 VLA 簇放在一起看，会出现一个很明显的问题：下一代 robotics foundation model，到底会更像 `OpenVLA/pi_0`，还是更像 `DreamZero` 这种 WAM？这很可能是接下来一两年里最值得追的主线之一。

## Connections

- [[world-models]]
- [[vision-language-action-models]]
- [[2018-world-models]]
- [[2024-genie]]
- [[2026-dreamzero]]
- [[2026-lingbot-world]]
- [[research-questions]]

## Sources

- [[2018-world-models]]
- [[2024-genie]]
- [[2026-dreamzero]]
- [[2026-lingbot-world]]
