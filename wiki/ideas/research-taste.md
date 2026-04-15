---
title: Research Taste
kind: idea
summary: A first-class page for recurring research taste, filters, and what kinds of work feel high-leverage or suspicious.
status: active
source_count: 12
updated: 2026-04-15
---

# Research Taste

## Summary

这个页面不是记录“我最近看了什么”，而是记录“我反复被什么打动、反复对什么起疑、以及我到底在用什么标准筛论文”。如果 `research-questions` 更像决策面板，这页更像是这些决策背后的长期 taste 层。它的目的，是让这个 wiki 不只是 paper archive，而能逐渐长出更清楚的 **我的研究滤镜**。

## What I Keep Rewarding

- 我明显偏好那些把问题 **重新表述对** 的工作，而不是只做局部数值提升。
- 我会反复被“先把中间表示做对，再谈 downstream”的论文吸引：
  - [[2024-trellis]]
  - [[2025-vggt]]
  - [[2025-object-centric-3d-motion-field]]
  - [[2026-articulated-reconstruction-transformer]]
- 我对 `bridge papers` 的兴趣很高，尤其是能把两个本来分裂的社区接起来的工作：
  - geometry 和 generation
  - HOI 和 articulated reconstruction
  - VLA 和 world models
  - data recipe 和 controllable action
- 我更容易信服那些明确暴露 failure mode、把关键假设讲清楚的工作，而不是端到端 magic pipeline 叙事。

## What Feels High-Leverage

- `representation / substrate` 往往比表面任务定义更重要。
- `action representation` 是 human-video-to-robot 这条线里的真正瓶颈之一。
- `data recipe`、`post-training`、`system integration` 现在的边际价值很可能已经不低于单点 architecture innovation。
- articulated / HOI / real2sim 这类问题里，真正有价值的输出不是“看起来像”，而是：
  - part structure
  - mobility / articulation
  - contact-consistent interaction
  - simulator-ready structure
- 对 3D 来说，我现在越来越把它看成一种 **基础设施问题**，而不是单独的内容生成问题。

## What Feels Suspicious

- 只讲 benchmark gain，却不解释 gain 到底来自哪里。
- 把 `more data` 和 `better representation` 混为一谈。
- 把 `foundation model prior` 当终点，而不是当原材料。
- articulated / HOI 论文只重建表面，却不认真处理：
  - part count
  - joint axis / limits
  - contact consistency
  - simulator export
- 过度依赖 closed demo，但没有给出足够清楚的中间结构解释。

## What I Am Probably Biased Toward

- 我明显偏向 `structure-first` 和 `representation-first` 的论文。
- 我可能会低估那些看起来更“脏”、但工程上真正强大的 end-to-end systems。
- 我容易高估带有 geometry / object-centric flavor 的方法，低估语言或 policy-only 路线的长期潜力。
- 我倾向于相信“中间层会留下来”，这可能会让我对直接大模型吃掉全部 pipeline 的可能性反应不够快。

## Reading Implications

- 当一篇论文让我觉得“这方向很对”，以后要追问到底是：
  - 它真的揭示了高杠杆结构
  - 还是只是正好踩中了当前 benchmark
- 当一条线越读越像“系统拼装”，要主动把我的判断单独写回 `ideas/` 或 `syntheses/`，而不是只留在 paper 页的 `My Take` 段落里。
- 以后补论文时，优先标记它是在强化还是削弱这里的某条 taste。
- 如果某个 taste 连续被很多相互独立的来源强化，就该升级成更明确的 thesis，而不是继续停留在“个人偏好”。

## Connections

- [[working-theses]]
- [[research-questions]]
- [[3d-generation]]
- [[representation-learning]]
- [[ai-and-robotics-data]]
- [[articulated-object-reconstruction-and-hoi]]
- [[vision-language-action-models]]
- [[world-models]]
- [[overview]]

## Sources

- [[2024-trellis]]
- [[2025-vggt]]
- [[2025-object-centric-3d-motion-field]]
- [[2025-taste-rob]]
- [[2026-articulation-in-motion]]
- [[2026-articulated-reconstruction-transformer]]
- [[2026-arthoi]]
- [[2024-openvla]]
- [[2024-pi-0]]
- [[2026-dreamzero]]
- [[gen-1-scaling-embodied-foundation-models-to-mastery]]
- [[robot-foundation-models-seminar-sergey-levine-2026-03-26]]
