---
title: 3D Generation
kind: topic
summary: A topic page for generative 3D asset creation, focusing on representation choice, conditioning, and output flexibility.
status: active
source_count: 1
updated: 2026-04-06
---

# 3D Generation

## Summary

`3D generation` 这条线关心的不只是“生成一个看起来像 3D 的东西”，而是如何在表示、条件控制、渲染质量、编辑能力和输出格式之间找到可扩展的平衡。当前这个 topic 还只是一个起点，但 `TRELLIS` 已经很适合作为第一篇种子论文，因为它把“统一表示”这件事放到了中心位置。

## Story Arc

- 早期 3D generation 经常围绕单一表示或单一任务组织
- 近期工作越来越强调统一 latent、跨模态条件和更实用的输出格式
- [[2024-trellis]] 可以看作是这条线里一个很典型的“先把表示做对，再谈生成和编辑”的版本

## Key Questions

- 哪种 3D 表示最适合作为大规模生成模型的中间层
- text-to-3D、image-to-3D 和 local editing 能否共用同一底层表示
- 输出 flexibility 和工程复杂度之间如何 trade off
- 这条线未来会更偏内容资产生成，还是更偏 3D understanding / embodied world modeling 的共用基础设施

## Important Papers

- [[2024-trellis]]

## Open Questions

- `TRELLIS` 这种 unified latent 表示能否成为更广泛的 3D generation 基础模块
- 如果未来引入物理、交互和时间维度，当前的 3D asset latent 是否还够用
- 该如何把 3D generation 和 robotics / world model 社区更自然地接起来

## Connections

- [[2024-trellis]]
- [[literature-review]]
- [[overview]]

## Sources

- [[2024-trellis]]
