---
title: Overview
kind: overview
summary: The stable worldview page for this research wiki, centered on current bets, tensions, and the owner's evolving research agenda.
status: active
source_count: 39
updated: 2026-04-15
---

# Overview

## Summary

这个页面不再只是 repo map，而是这个 wiki 的稳定 worldview 页面。它的作用不是覆盖所有页面，而是回答：这个库当前围绕哪些核心研究命题组织、我现在更相信什么、我对什么保持怀疑、以及不同 cluster 之间正在如何连起来。更动态的“这周我在追什么”放到 [[now]]；这里保留相对稳定的研究视角。

## Working Thesis

- `raw/` 保存原始事实来源，`wiki/` 保存结构化研究知识，但真正高价值的输出应该逐渐长成 owner-facing 的 `questions / theses / programs / reviews`。
- 证据层的目标不是堆 paper，而是不断把外部材料编译进自己的研究判断。
- 现在最值得跟的，不是单篇 benchmark 增益，而是哪些中间表示、数据 recipe、system interface 会在 embodied intelligence 里变成长期基础设施。
- 这个库的方向，正在从“paper archive with topic maps”转向“research judgment system with evidence backing”。

## My Current Bets

- `representation + recipe + post-training + system integration` 的组合杠杆，当前比单点 architecture innovation 更值得追。
- `human-video-to-robot` 这条线的真正瓶颈，很可能在 action abstraction / interaction-centric representation，而不只是数据规模。
- `VLA` 和 `world model / WAM` 更像会融合，而不是简单替代。
- `articulated reconstruction` 不该再被只看作几何问题，而应该放进 `HOI / real2sim / manipulation` 的闭环里理解。
- 对 3D 来说，越来越多工作值得被当作基础设施问题看，而不只是内容生成问题。

## What I’m Skeptical Of

- 只讲 benchmark gain，却不说明 gain 到底来自哪里。
- 把 `more data` 和 `better representation` 混成一个故事。
- 把 closed-system frontier demo 直接等同于稳定研究结论。
- 只恢复表面形状，却不认真处理 articulated structure、contact consistency 或 simulator-ready output 的 real2sim 叙事。
- 把 embodied progress 主要解释为单一 backbone 的代际替换，而忽略 recipe / post-training / system interface。

## What Might Change My Mind

- 开放、稳定、可复现的 world-model-centric 主干，在真实机器人上显著压过强 VLA baseline。
- 强证据表明，大规模 raw human video 预训练本身已经足以稳定学出跨 embodiment 的动作抽象，而不需要更结构化的中间表示。
- 清楚证明单一 architecture shift 比 data recipe、post-training、system integration 的组合杠杆更关键的新一代结果。
- articulated / HOI / real2sim pipeline 里，明确结构输出并不是长期必要条件的系统性证据。

## What I’m Tracking

- [[vision-language-action-models]]
- [[world-models]]
- [[ai-and-robotics-data]]
- [[3d-generation]]
- [[articulated-object-reconstruction-and-hoi]]
- [[human-video-to-robot-learning]]
- [[research-questions]]
- [[working-theses]]
- [[research-taste]]

## Current Research Layers

- `papers/`, `sources/`, `people/`: evidence layer
- `topics/`, `methods/`, `benchmarks/`: map layer
- `questions/`, `theses/`, `reviews/`: judgment layer
- `programs/`, `now.md`: agenda layer
- `ideas/` and `syntheses/` remain as transitional / mixed layers while the architecture shifts upward

## Where The Main Clusters Are Heading

- `VLA` 这条线已经不只是 action token 或 continuous action modeling 本身，而是在逼近更大的 question：control interface 应该怎样和 reasoning、post-training、predictive structure 接起来。
- `world models / WAM` 这条线正在从 simulator / predictive substrate 走向 policy substrate，因此和 VLA 的边界越来越值得显式比较。
- `AI and robotics data` 正在从“数据够不够”升级为“什么数据、什么 mixture、什么后训练 recipe 真正决定边界”。
- `3D generation` 这条线越来越不像单独的 asset generation，而越来越像 geometry / representation infrastructure。
- `articulated object reconstruction + HOI` 这条线开始变成一个更像 interaction-centric real2sim pipeline 的入口，而不只是静态重建问题。

## Key Entry Points

- 当前最动态的入口：[[now]]
- 当前决策面板：[[research-questions]]
- 当前 working beliefs：[[working-theses]]
- 当前长期滤镜：[[research-taste]]
- 当前最明确的 program：[[human-video-to-robot-learning]]

## Sources

- [[research-questions]]
- [[working-theses]]
- [[research-taste]]
- [[human-video-to-robot-learning]]
- [[vision-language-action-models]]
- [[world-models]]
- [[ai-and-robotics-data]]
- [[3d-generation]]
- [[articulated-object-reconstruction-and-hoi]]
- [[2024-openvla]]
- [[2024-pi-0]]
- [[2024-genie]]
- [[2026-dreamzero]]
- [[2026-lingbot-world]]
- [[2025-vggt]]
- [[2025-object-centric-3d-motion-field]]
- [[2025-taste-rob]]
- [[2026-articulation-in-motion]]
- [[2026-articulated-reconstruction-transformer]]
- [[2026-arthoi]]
