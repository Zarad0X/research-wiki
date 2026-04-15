---
title: Human Video to Robot Learning
kind: program
summary: A live research program on what representations, data recipes, and system interfaces are needed to turn human interaction video into executable robot behavior.
status: active
source_count: 6
updated: 2026-04-15
---

# Human Video to Robot Learning

## Summary

这个 program 页不是在问“human video 对机器人有没有用”这种泛问题，而是在追一个更具体的研究程序：如果 human interaction video 真会成为 robotics scaling 的关键燃料，那么中间到底需要哪些表示、数据 recipe 和 system interface，才能把它稳定编译成可执行 robot behavior，而不是只学到更强 observation prior。

## Program Thesis

我当前更倾向于：`human-video-to-robot` 这条线最后能不能成立，关键不只在数据规模，而在于能否找到足够 task-aligned 的 action abstraction 和 training recipe，把 human interaction video 变成对 control 真正有用的中间层。

## Why This Line Matters

- 如果这条线成立，它会显著改变 embodied data scaling 的成本结构。
- 它正好把当前几个 cluster 接起来：`AI and robotics data`、`action representation`、`HOI / articulated interaction`、`VLA / world model`。
- 这条线也逼着人回答一个更底层的问题：robotics foundation model 最需要的到底是更多演示，还是更好的中间结构。

## Key Subquestions

- 从 human video 到 robot action，最合适的中间表示到底是什么。
- task-oriented interaction video generation 在这条线里是数据扩增手段，还是更深的 recipe 组件。
- wearable human interaction data 到底是 cheap pretraining substitute，还是独立的高价值数据源。
- VLA / world model / action representation 这几层里，真正承接 human video 的接口应该放在哪。

## Required Evidence

- 更直接比较 raw human video pretraining 与 structure-aware representation 方法的工作。
- 比较 `task-aligned synthetic / generated interaction data` 与 `real collected interaction data` 的研究。
- 明确讨论 transfer、embodiment gap、action abstraction 的 paper 或 source。
- 更系统的 frontier system 证据，而不只是单点 demo。

## Near-Term Reading Priorities

- 继续补 human-video-to-robot 里的 action abstraction / contact representation / motion-centric representation 代表作。
- 对照读 [[2025-taste-rob]] 与 [[2025-object-centric-3d-motion-field]]，区分“生成更对路的数据”和“提纯更对路的动作表示”。
- 继续跟 [[gen-1-scaling-embodied-foundation-models-to-mastery]] 这类第一方系统 framing，看看数据和 action interface 到底怎么被讲清楚。

## Connections

- [[research-questions]]
- [[working-theses]]
- [[ai-and-robotics-data]]
- [[vision-language-action-models]]
- [[articulated-object-reconstruction-and-hoi]]
- [[2025-object-centric-3d-motion-field]]
- [[2025-taste-rob]]
- [[gen-1-scaling-embodied-foundation-models-to-mastery]]
- [[overview]]

## Sources

- [[2025-object-centric-3d-motion-field]]
- [[2025-taste-rob]]
- [[gen-1-scaling-embodied-foundation-models-to-mastery]]
- [[xie-chen-data-survey-history-landscape-pyramid-structure-and-recipes-for-ai-and-robotics-data]]
- [[robot-foundation-models-seminar-sergey-levine-2026-03-26]]
- [[2024-pi-0]]
