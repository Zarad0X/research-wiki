---
title: Vision-Language-Action Models
kind: topic
summary: A topic page for the VLA line of work, focusing on how RT-2, OpenVLA, and pi_0 define three distinct stages of the research trajectory.
status: active
source_count: 7
updated: 2026-04-08
---

# Vision-Language-Action Models

## Summary

VLA 可以先粗略看成“把视觉、语言和动作放进一个统一模型中做端到端控制”的路线。但如果按研究脉络看，RT-2、OpenVLA、`pi_0` 更像是在回答三个不同问题：VLA 能不能成立、VLA 能不能开放并实用、VLA 能不能更好地处理连续且灵巧的控制。

## Three-Step Story

- [[2023-rt-2]]：定义范式，证明 web pretraining 可以迁移到 robot control
- [[2024-openvla]]：开放范式，把 VLA 变成社区可以训练、微调、评测的对象
- [[2024-pi-0]]：推进架构，把重点转向连续动作建模和 dexterous control
- [[gen-1-scaling-embodied-foundation-models-to-mastery]]：代表一个更偏 proprietary frontier system 的分支，开始把 `VLA` 这个词往更宽的 embodied foundation model system 叙事外推

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
- 如果你想看这条线如何继续长到 reasoning、steerability 和 RL post-training，再读 [[robot-foundation-models-seminar-sergey-levine-2026-03-26]]
- 如果你想看 frontier 公司如何把这条线包装成完整系统，而不再只是模型架构，也可以补读 [[gen-1-scaling-embodied-foundation-models-to-mastery]]

## Open Questions

- 未来最强路线会继续离散 token 化，还是向连续 action 生成迁移
- community-friendly open baseline 和 frontier proprietary data/robots 之间的差距究竟有多大
- VLA 的下一阶段瓶颈会在 action modeling、world modeling、memory，还是 post-training
- 如果按 Levine 的 framing 看，VLA 真正的难点可能不只在架构，而更在数据 recipe、训练目标和 post-training
- embodied chain of thought 和 steerable VLA 这类推理增强，会不会像 LLM 里的 CoT 一样成为默认配置
- frontier robotics 的主竞争单位，未来到底还是 `VLA architecture`，还是 `embodied foundation model system`

## Connections

- [[2023-rt-2]]
- [[2024-openvla]]
- [[2024-pi-0]]
- [[rt-2-openvla-pi-0]]
- [[world-models]]
- [[sergey-levine]]
- [[generalist-ai]]
- [[gen-1-scaling-embodied-foundation-models-to-mastery]]
- [[robotic-foundation-models-sergey-levine-talk]]
- [[robot-foundation-models-seminar-sergey-levine-2026-03-26]]

## Sources

- [[2023-rt-2]]
- [[2024-openvla]]
- [[2024-pi-0]]
- [[gen-1-scaling-embodied-foundation-models-to-mastery]]
- [[robotic-foundation-models-sergey-levine-talk]]
- [[robot-foundation-models-seminar-sergey-levine-2026-03-26]]
