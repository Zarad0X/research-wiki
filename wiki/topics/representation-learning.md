---
title: Representation Learning
kind: topic
summary: A topic page about how useful internal representations are learned, reused, and scaled across vision, multimodal systems, and embodied intelligence.
status: active
source_count: 5
updated: 2026-04-08
---

# Representation Learning

## Summary

`representation learning` 这条线关心的核心，不是模型最后会不会输出对的答案，而是系统内部到底学到了什么样的状态、结构和可迁移知识。对这个库来说，它特别重要，因为很多看起来彼此分散的方向，其实都能被 representation 视角重新串起来：自监督视觉、multimodal systems、world models、robotics foundation models，甚至生成模型里的 latent design。最近补进来的 Saining Xie 相关材料尤其适合当这一页的支点，因为他的很多代表作都在反复回答同一个问题：怎样的内部表示既简洁、又可扩展、还能在范式切换后继续保持价值。

## Story Arc

- 早期视觉研究更常把 representation 当作 task-specific feature。
- 自监督学习阶段，问题变成：能不能先学出通用的视觉内部表示，再迁移到下游任务。
- `MoCo`、`MAE` 这一类工作把 representation learning 从附属技巧推成了基础 recipe。
- 再往后，representation 不再只属于判别式视觉；它开始影响 architecture 设计、multimodal alignment、diffusion backbone，甚至 world models。
- 最近像 [[2025-vggt]] 这样的工作还说明，representation learning 的战场已经进一步扩展到 `scene geometry`：好的 backbone 不一定只学语义，也可以学 camera、depth、point map 这类结构化 3D 表示。
- 以 Saining Xie 这条线为例，会看到一种连续性：从视觉结构与自监督表示，到 `ConvNeXt` / `ConvNeXt V2` / `DiT` 这种基础 backbone，再到 `Cambrian` 与更明确的 world-model ambition。

## Key Questions

- 好的 representation 应该追求 invariance，还是尽量保留可恢复世界结构的信息。
- 表征学习的价值主要体现在 sample efficiency、transfer，还是后续推理与控制能力。
- 语言会不会在某些场景里“污染”视觉表征，而不是帮助它。
- world models 的本质究竟是 rollout / simulation，还是更强的 structured representation。

## Important Papers

- [[2020-moco]]
- [[2022-mae]]
- [[2022-convnext]]
- [[2023-convnext-v2]]
- `ConvNeXt V2`
- [[2023-dit]]
- [[2024-cambrian-1]]
- [[2025-vggt]]
- [[2017-resnext]]
- `Cambrian`
- [[saining-xie-homepage]]

## Open Questions

- 表征学习在今天是不是被“LLM as interface” 的叙事压住了真实价值。
- vision-centric representation 与 language-centric multimodality 最终会融合，还是会形成持续张力。
- 在 robotics 里，真正可迁移的东西到底是 action policy，还是对世界的内部表示。
- 如果按 Saining Xie 的 taste 去看，下一波最值得押注的，也许不是更大的 instruction layer，而是更好的 world-grounded representation。
- `vision-centric` 的 multimodal 路线会不会重新把 representation learning 拉回主舞台，而不只是做 LLM 的附属塔。
- `geometry-centric` backbone 会不会成为视觉表示学习的另一条主线，而不只是 SfM / MVS 社区的专用工具。

## Connections

- [[saining-xie]]
- [[2017-resnext]]
- [[2020-moco]]
- [[2022-mae]]
- [[2022-convnext]]
- [[2023-convnext-v2]]
- [[2023-dit]]
- [[2024-cambrian-1]]
- [[ami-labs]]
- [[saining-xie-homepage]]
- [[saining-xie-research-taste-and-representative-works]]
- [[world-models]]
- [[vision-language-action-models]]
- [[ai-and-robotics-data]]
- [[3d-generation]]

## Sources

- [[saining-xie-homepage]]
- [[a-7-hour-marathon-interview-with-saining-xie-world-models-ami-labs-yann-lecun-fei-fei-li-and-42]]
- [[ami-labs]]
