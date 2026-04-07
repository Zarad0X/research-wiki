---
title: Robotic Foundation Models (Sergey Levine talk)
kind: source
summary: "DAI 2024 keynote where Sergey Levine frames robotic foundation models around three central questions: data, objective, and post-training."
status: active
source_count: 4
updated: 2026-04-07
---

# Robotic Foundation Models (Sergey Levine talk)

## Source Metadata

- Official talk title: `Robotic Foundation Models`
- Common Chinese repost title: `机器人基础模型：从语言到物理世界的智能飞跃｜Sergey Levine 深度讲座`
- Speaker: [[sergey-levine]]
- Event: DAI 2024
- Time: 9:00-10:00, December 21, 2024, UTC+8

## Summary

这场讲座更像是一个 research framing，而不是单一模型报告。Levine 的核心论点是：机器人领域天然适合 foundation model，因为单一平台、单一任务的数据都太难收；如果能在大规模 embodied experience 上训练通用预训练模型，就不仅能提高机器人泛化能力，也会推动我们理解 situated problem solving、physical understanding 和 decision making。但真正难的问题不只是“模型做多大”，而是三件更系统的事：到底用什么数据、训练目标是什么、以及 alignment 或 post-training 应该怎么做。

## Key Takeaways

- 这场 talk 的出发点很明确：机器人比 NLP/CV 更缺单任务大数据，所以更需要通用预训练模型。
- Levine 把 robotics foundation model 的价值同时放在“工程可扩展性”和“通用 AI 研究”两层上。
- 官方摘要里最重要的三个问题可以直接压缩成一条 recipe：用什么数据训练、训练目标是什么、alignment / post-training 应该怎么做。
- 这套 framing 很适合拿来审视 [[vision-language-action-models]] 和 [[world-models]] 两条路线，因为它强调的不是单一架构，而是整条 recipe。
- 这场 talk 的原始官方题目是 `Robotic Foundation Models`，你提到的中文标题更像是后续传播时的中文转述。

## Connections

- [[sergey-levine]]
- [[vision-language-action-models]]
- [[world-models]]
- [[2024-openvla]]

## Sources

- Archived source: `raw/sources/2026-04-07-robotic-foundation-models-sergey-levine-talk.md`
- Source link: https://opendrivelab.github.io/CVPR%202024/jun_2024_robotic_foundation_models.pdf
- DAI talk detail page: https://adai.ai/dai/2024/Talk_Sergey_Levine.html
- DAI keynote schedule: https://adai.ai/dai/2024/Program-Keynotes.html
- DAI 2024 manual: https://adai.ai/dai/2024/paper/DAI2024Manual.pdf
