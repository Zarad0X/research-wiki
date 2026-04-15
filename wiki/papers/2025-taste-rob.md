---
title: TASTE-Rob
kind: paper
summary: A 2025 CVPR paper that uses task-oriented hand-object interaction video generation to support more generalizable robotic manipulation, marking Xiaoguang Han's group's clearer move toward robotics.
status: active
source_count: 2
updated: 2026-04-07
---

# TASTE-Rob

## Summary

`TASTE-Rob` 是我看 Xiaoguang Han 老师最近论文时最先会标出来的一篇，因为它清楚地标志了这条线往 robotics 走。它不再只是做 3D 物体或人类建模，而是把 `task-oriented hand-object interaction video generation` 和 `generalizable robotic manipulation` 直接挂到一起。

## Story / Setting

- 机器人 imitation learning 很需要高质量 demonstration
- hand-object interaction video generation 看起来是个很自然的桥梁
- 但现有数据如 `Ego4D` 之类往往视角不一致、交互不够对齐，不利于精细 imitation

## Why This Exists

- 想解决 task-oriented HOI video 质量与对齐问题
- 想让生成出来的视频更能服务机器人操作，而不是只当视觉 demo

## Related Work

- 现有 HOI 数据和模型更常服务视觉理解或通用视频生成
- `TASTE-Rob` 的 distinct point 是把数据与生成流程明确服务于 robotics manipulation

## First Principles

- 如果 demonstration 质量和 viewpoint consistency 不够好，机器人很难真正学到可执行技能
- robotics-friendly data generation 需要比普通视频生成更强的交互清晰度和姿态合理性

## Problem

- 现有 task-oriented HOI video data 不够稳定
- 视角和交互对齐不足，影响 imitation learning 价值

## Main Idea

- 构建大规模 `TASTE-Rob` 数据集
- 其视频与语言指令对齐，且保持一致相机视角
- 在 video diffusion model 基础上，再加三阶段 pose refinement 提升手部姿态真实性

## Core Architecture

- 数据集是核心一环
- 视频生成主干使用 video diffusion model
- 额外 pose-refinement pipeline 专门修正手部抓取姿态

## Method

- 构建 100,856 个第一视角 hand-object interaction 视频数据
- fine-tune VDM
- 再做 pose refinement，提升生成交互的可用性

## Experimental Setup

- 重点比较生成质量、交互真实性、以及服务 generalizable robotic manipulation 的效果
- 数据与模型都围绕 task-oriented setting 设计

## Results

- arXiv 摘要显示该数据与 refinement framework 带来显著提升
- 这篇的真正意义在于：它把视频生成、手物交互和机器人操作放进了同一条 pipeline

## Strengths

- 很明确地把 3D/视觉积累往 robotics 外推
- 数据和模型都不是为普通视频生成而设计，而是为 manipulation 服务
- 说明 Han 老师组开始更认真地碰 embodied / robotics

## Limitations

- 仍然主要是在“生成 demonstrations”这一层发力
- 离真正 closed-loop robot policy learning 还有距离

## Questions

- task-oriented HOI video generation 会不会成为 imitation learning 的重要数据补充层
- 这条线后面会不会继续长成 world model 或 policy pretraining

## My Take

如果你问我 Xiaoguang Han 老师最近哪篇最值得先看，我会把 `TASTE-Rob` 放在最前面。因为它最清楚地说明了这位老师的研究开始往哪里继续长。

## Connections

- [[xiaoguang-han]]
- [[ai-and-robotics-data]]
- [[2025-object-centric-3d-motion-field]]
- [[vision-language-action-models]]
- [[xiaoguang-han-recent-papers-2024-2025]]

## Sources

- Paper: https://arxiv.org/abs/2503.11423
- Faculty listing: [[xiaoguang-han-cuhksz-faculty-page]]
