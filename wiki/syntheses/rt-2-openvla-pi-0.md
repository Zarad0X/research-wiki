---
title: RT-2 vs OpenVLA vs pi_0
kind: synthesis
summary: A first-pass synthesis comparing RT-2, OpenVLA, and pi_0 as three milestones in the VLA research trajectory.
status: active
source_count: 3
updated: 2026-04-06
---

# RT-2 vs OpenVLA vs pi_0

## Summary

这三篇 paper 不太适合只按“谁更强”来排。更合适的理解是：它们分别代表了 VLA 研究里的三次关键转移。

## The Three Transitions

- RT-2：从“robot policy”转向“VLA”
- OpenVLA：从“closed demo”转向“open research object”
- `pi_0`：从“离散 action token”为主，转向“连续 action generation 更重要”

## A Useful Mental Model

- RT-2 回答的是：`这种统一建模思路是否成立`
- OpenVLA 回答的是：`社区能不能真正把它拿来做研究`
- `pi_0` 回答的是：`如果我们更认真面对真实控制需求，架构应该怎么变`

## Practical Reading Order

- 第一篇读 [[2023-rt-2]]，理解 VLA 为什么出现
- 第二篇读 [[2024-openvla]]，理解现在社区为什么能大规模跟进
- 第三篇读 [[2024-pi-0]]，理解 action modeling 在 robotics 中为什么重新变成核心问题

## Research Takeaways

- 只看 RT-2，容易高估“统一 token space”本身的充分性
- 只看 OpenVLA，容易把问题理解成“更好的开源工程和数据配方”
- 加上 `pi_0` 之后，会更明显看到：动作表示本身可能就是下一个核心研究变量

## What To Watch Next

- 离散 action 与连续 action 的边界会怎么演化
- 更强的 open-source VLA 是否会结合 `pi_0` 式连续动作建模
- long-horizon planning、memory、world model 会怎样和 VLA 主干结合

## Connections

- [[vision-language-action-models]]
- [[2023-rt-2]]
- [[2024-openvla]]
- [[2024-pi-0]]
- [[research-questions]]

## Sources

- [[2023-rt-2]]
- [[2024-openvla]]
- [[2024-pi-0]]
