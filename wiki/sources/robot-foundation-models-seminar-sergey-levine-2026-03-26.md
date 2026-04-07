---
title: Robot Foundation Models Seminar (Sergey Levine, 2026-03-26)
kind: source
summary: A March 26, 2026 seminar summarizing the Physical Intelligence roadmap from pi_0 to pi_0.5 and pi*0.6, with emphasis on reasoning, data scaling, and RL post-training.
status: active
source_count: 2
updated: 2026-04-07
---

# Robot Foundation Models Seminar (Sergey Levine, 2026-03-26)

## Source Metadata

- Source type: seminar video plus user-supplied structured notes
- Event: `AI Agent Frontier Seminar`
- Speaker: [[sergey-levine]]
- Date: `2026-03-26`
- Video: https://www.youtube.com/watch?v=_b-FwaiETwM
- This page relies heavily on the user's supplied notes for the detailed takeaways
- Common Chinese title used in reposts: `机器人基础模型：从语言到物理世界的智能飞跃｜Sergey Levine 深度讲座`

## Summary

这场 seminar 可以看作是对 `pi_0` 路线的一次阶段性总结：从最初的 action expert + flow matching 架构，推进到 `pi_0.5` 的 reasoning / verbal supervision，再推进到 `pi*0.6` 的 RL post-training。它和前一场更偏 framing 的 `Robotic Foundation Models` talk 不同，这场更像是一个“技术路线复盘”，把 Physical Intelligence 的方法栈拆成几层：VLM backbone 负责认知，action expert 负责运动控制，thinking 负责 test-time reasoning，多源数据负责泛化，RL 负责鲁棒性与吞吐量。

## Key Takeaways

- 讲座把 `pi_0` 描述成第二代 VLA：在 VLM backbone 上增加 action expert，用 flow matching 生成约 `50Hz` 的连续动作块。
- 一个很强的叙事点是“虚拟运动皮层”比喻：VLM 像视觉和语义理解系统，action expert 像精细运动控制系统。
- `Embodied Chain of Thought` 和 `thinking VLA` 是这场 talk 的重要主题之一，核心观点是 reasoning / test-time compute 在机器人上同样有效。
- `Steerable VLA` 强调多抽象层级控制：高层语义、中层子任务、低层坐标或动作。
- 数据策略被讲得非常系统：预训练解决 coverage，后训练解决 consistency；高质量数据本身不够，因为恢复能力来自更混乱的大规模经验。
- `RTX` 数据池化、多平台迁移、`3%` 移动机器人数据继承其他平台技能、`100` 个家庭环境饱和点，都是这场讲座里很值得记住的数据点。
- `pi*0.6` 的 RL 后训练被描述为把 value function 和 advantage conditioning 引入 foundation-model policy，从而显著提升鲁棒性和任务吞吐量。
- 讲座最后的哲学点也很重要：物理世界中的交互经验不只是 engineering data，也可能成为 AI 学到新物理知识的来源。

## Connections

- [[sergey-levine]]
- [[2024-pi-0]]
- [[vision-language-action-models]]
- [[robotic-foundation-models-sergey-levine-talk]]

## Sources

- Archived source: `raw/sources/2026-04-07-robot-foundation-models-seminar-sergey-levine-2026-03-26.md`
- Source link: https://www.youtube.com/watch?v=_b-FwaiETwM
- User-provided seminar notes in this chat session
