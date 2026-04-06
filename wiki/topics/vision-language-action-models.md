---
title: Vision-Language-Action Models
kind: topic
summary: A topic page for the VLA line of work, focusing on how RT-2, OpenVLA, and pi_0 define three distinct stages of the research trajectory.
status: active
source_count: 3
updated: 2026-04-06
---

# Vision-Language-Action Models

## Summary

VLA 可以先粗略看成“把视觉、语言和动作放进一个统一模型中做端到端控制”的路线。但如果按研究脉络看，RT-2、OpenVLA、`pi_0` 更像是在回答三个不同问题：VLA 能不能成立、VLA 能不能开放并实用、VLA 能不能更好地处理连续且灵巧的控制。

## Three-Step Story

- [[2023-rt-2]]：定义范式，证明 web pretraining 可以迁移到 robot control
- [[2024-openvla]]：开放范式，把 VLA 变成社区可以训练、微调、评测的对象
- [[2024-pi-0]]：推进架构，把重点转向连续动作建模和 dexterous control

## Comparison Axes

| Axis | RT-2 | OpenVLA | pi_0 |
| --- | --- | --- | --- |
| Historical role | Defines VLA | Opens VLA | Pushes VLA toward continuous dexterous control |
| Openness | Mostly closed | Strongly open | Later opened via openpi |
| Action formulation | Discrete action tokens | Discrete action tokens | Continuous action chunks via flow matching |
| Main value | Web knowledge transfer | Reproducible research baseline | Better fit for dexterous real-world control |

## What Matters For Research Use

- 如果你想理解 VLA 的原始直觉，先读 [[2023-rt-2]]
- 如果你想做实验、微调、复现，先抓 [[2024-openvla]]
- 如果你关心 dexterous manipulation、连续控制和 action modeling，重点看 [[2024-pi-0]]

## Open Questions

- 未来最强路线会继续离散 token 化，还是向连续 action 生成迁移
- community-friendly open baseline 和 frontier proprietary data/robots 之间的差距究竟有多大
- VLA 的下一阶段瓶颈会在 action modeling、world modeling、memory，还是 post-training

## Connections

- [[2023-rt-2]]
- [[2024-openvla]]
- [[2024-pi-0]]
- [[rt-2-openvla-pi-0]]
- [[world-models]]

## Sources

- [[2023-rt-2]]
- [[2024-openvla]]
- [[2024-pi-0]]
