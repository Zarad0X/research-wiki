---
title: OpenVLA
kind: paper
summary: A 7B open-source VLA that made the RT-2-style recipe reproducible and practical, with strong fine-tuning results and broad community impact.
status: active
source_count: 1
updated: 2026-04-06
---

# OpenVLA

## Summary

OpenVLA 的关键价值不是“又一个 VLA”，而是把 RT-2 式的路线真正开放出来，让研究者可以训练、微调、评测、复现，并开始系统研究 VLA 的 recipe。

## Problem

- 早期 VLA 很强，但大多 closed
- 社区缺少可以直接拿来 fine-tune 和研究的强基线
- 如何高效把 VLA 适配到新机器人、新任务，也是 adoption 的关键问题

## Main Idea

- 做一个 7B 的 open-source VLA
- 利用大规模真实机器人 demonstration 进行预训练
- 同时把 fine-tuning、LoRA、量化部署这些实际研究工作流一起开放

## Method

- OpenVLA 建立在一个视觉语言 backbone 之上，并扩展为 action prediction
- arXiv 摘要显示，它结合了 Llama 2 语言模型与融合 DINOv2 和 SigLIP 的视觉编码器
- 官方代码库和 README 显示，vanilla OpenVLA 采用离散 action 表示，后续又衍生出 FAST 和 OFT 等加速或连续化路线

## Experimental Setup

- 论文报告使用 970k 条真实机器人 demonstration 进行训练
- 评测覆盖 29 个任务和多种 robot embodiment
- 还专门研究了 LoRA 和 consumer GPU 上的 fine-tuning 可行性

## Results

- 论文报告：相对 RT-2-X (55B)，OpenVLA 在 29 个任务上的绝对 success rate 高 16.5%，同时参数量少约 7 倍
- 相对从零开始的 imitation learning 方法 Diffusion Policy，报告有 20.4% 的优势
- 展示了在消费级 GPU 上进行高效微调和量化部署的实际可行性

## Strengths

- 真正把 VLA 研究从“看论文”推进到“可以自己做实验”
- 开源代码、权重和训练脚手架的研究价值非常高
- 在性能、开放性、工程可用性之间取得了很强平衡

## Limitations

- 虽然开源，但完整训练和评测仍然有较强算力和数据门槛
- 基础路线仍偏离散 action token，自带 latency 和精细控制上的 tradeoff
- 更擅长 generalist manipulation，不代表已经覆盖长期规划或复杂机器人系统集成

## Questions

- OpenVLA 的最大增益究竟来自开放数据、多样性，还是 backbone 设计
- 对于 robotics research，下一步更重要的是更强 pretraining 还是更好的 post-training
- 如果任务更加 dexterous，是否需要离开纯 autoregressive discrete action 路线

## Initial Take

OpenVLA 是“社区研究转折点”型论文。RT-2 证明 VLA 可行，OpenVLA 则让这件事变成一个可以被社区真正迭代的研究对象。对学生来说，它的价值常常大于单篇 SOTA 数字，因为它给了你一个可进入的系统。

## Connections

- [[vision-language-action-models]]
- [[2023-rt-2]]
- [[2024-pi-0]]
- [[rt-2-openvla-pi-0]]

## Sources

- Paper: https://arxiv.org/abs/2406.09246
- Code: https://github.com/openvla/openvla
- Project: http://openvla.github.io
