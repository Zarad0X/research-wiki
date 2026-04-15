---
title: Research Questions
kind: question
summary: A research decision panel for tracking current beliefs, competing evidence, and the next readings that could actually change my mind.
status: active
source_count: 11
updated: 2026-04-15
---

# Research Questions

## Summary

这个页面不再只是堆 open questions，而是一个研究决策面板：只保留当前真正影响阅读优先级、判断更新和选题方向的少数关键问题。每个问题都要写清楚我现在更倾向于什么、证据站在哪边、什么新证据会让我改主意，以及下一步最值得补什么。

## How To Use This Page

- 只保留少数几个真的会影响后续阅读和判断的问题，不把这里变成愿望清单。
- 每个问题都尽量写出 `Current belief`，避免一直停在“我还不确定”。
- 如果一个问题已经长成了稳定的 topic comparison，就应该拆到单独的 `synthesis` 页面，而不是无限堆在这里。
- 每次新增 paper 或 source 时，优先更新已有判断；只有当它引入了新的决策岔路，才新增问题。

## Active Decision Panel

| Priority | Question | Current lean | Next step |
| --- | --- | --- | --- |
| P1 | VLA 会继续是 robotics foundation model 的主干，还是会逐渐让位给 world model / WAM？ | 近期更像融合，不像替代 | 继续补 policy-world-model interface 的代表作 |
| P1 | 从 human video 学机器人时，真正该学习的 action representation 是什么？ | 更偏 object-centric / interaction-centric 中间表示，而不是直接从原始视频到动作 | 继续补动作表示与可执行控制之间的桥接工作 |
| P2 | 下一阶段 embodied intelligence 的主要瓶颈更在 data recipe，还是 architecture innovation？ | 当前更偏 data recipe + post-training | 继续补 frontier system 和 open baseline 的对照证据 |

### Question 1

#### VLA 会继续是 robotics foundation model 的主干，还是会逐渐让位给 world model / WAM？

**Why this matters**

这是当前最影响阅读排序的问题之一。如果主干仍然是 VLA，那么阅读重点应该继续放在 action modeling、reasoning、post-training 和 deployment recipe；如果 world model / WAM 会成为更核心的 substrate，那么就应该更系统地补 representation、predictive modeling、simulation 和 planning 这条线。

**Current belief**

我当前更倾向于：短中期内不会出现“VLA 被 world model 直接替代”的简单结论，更可能的方向是两者逐渐融合。VLA 仍然是最直接的 control interface 和开放研究基线，而 world model / WAM 更像是在补 predictive structure、data efficiency、planning substrate 和 policy pretraining 的上层能力。

**Best evidence for this belief**

- [[2024-openvla]] 说明 VLA 仍然是当前最可操作、最可复现、最适合社区迭代的主干对象。
- [[2024-pi-0]] 说明 VLA 线本身也在演化，并不是停在离散 action token 阶段。
- [[2026-dreamzero]] 把 world model 直接推向 policy，说明两条线的边界正在变模糊，而不是严格分离。
- [[robot-foundation-models-seminar-sergey-levine-2026-03-26]] 也在暗示下一阶段的关键未必只是 backbone，而是 reasoning、data 和 post-training 的系统协同。

**Best evidence against this belief**

- 如果 [[2026-dreamzero]] 这种路线后续在真实机器人执行上继续成立，world model / WAM 可能不只是辅助模块，而会重新定义 policy 本体。
- [[2024-genie]] 和 [[2026-lingbot-world]] 这类工作说明，可交互世界建模正在从“辅助分析工具”往更完整的 substrate 方向推进。
- 如果未来最关键的瓶颈变成 long-horizon consistency、counterfactual planning、failure recovery，那么 VLA-only 的 framing 可能会越来越吃亏。

**What would change my mind**

- 出现一批在真实机器人上稳定证明 `world model as policy substrate` 明显优于强 VLA baseline 的工作。
- 出现一个开放、可复现、任务覆盖广的 world-model-centric 研究基线，社区可以像用 OpenVLA 一样直接迭代。
- 相反，如果未来最强结果仍然主要来自更强数据 recipe、continuous action modeling 和 post-training，而不是显式世界建模，我会继续把 VLA 视为主干。

**Next readings / experiments**

- 继续补 `policy + world model` 真正耦合而不是口号式耦合的代表作。
- 对照读 [[2024-openvla]]、[[2024-pi-0]]、[[2026-dreamzero]]，专门比较“policy interface”到底放在哪里。
- 后面如果这个问题证据开始收敛，可以单独长成一篇 `VLA vs WAM` synthesis。

### Question 2

#### 从 human video 学机器人时，真正该学习的 action representation 是什么？

**Why this matters**

这关系到你现在这几个 cluster 能不能真正接上：`AI and robotics data` 讲的是数据来源，`3D generation / geometry` 可能提供结构化中间表示，而 robotics 这边最终关心的是可执行控制。这个问题如果想清楚，后面的读法会从“看到 human video 就都算数据红利”变成“哪些表示真的能落到 robot action”。

**Current belief**

我当前更倾向于：从 human video 到 robot policy 的关键不只是多收视频，而是找到足够 task-aligned、object-centric、interaction-centric 的中间动作表示。直接把原始视频当 supervision 虽然有吸引力，但真正限制泛化和可执行性的，可能越来越是表示是否保留了对 manipulation 有用的对象关系、接触变化和可迁移运动结构。

**Best evidence for this belief**

- [[2025-object-centric-3d-motion-field]] 直接把问题打到动作表示层，而不是把 human video 仅仅当作更多数据。
- [[2025-taste-rob]] 说明 task-oriented interaction video 可能有价值，但它的价值未必只是“视频更多”，而是“视频更 task-aligned”。
- [[gen-1-scaling-embodied-foundation-models-to-mastery]] 进一步推动了 wearable human interaction data 的想象空间，但它也反过来强化了一个问题：什么表征能把这类数据变成真正可执行控制，而不是只变成更强观察先验。

**Best evidence against this belief**

- 如果规模足够大，端到端方法也可能绕过手工设计的中间表示，直接学出有用的 action abstraction。
- [[2024-pi-0]] 这样的连续动作建模路线提醒我们，表示问题不一定非要显式 object-centric 才能奏效。
- 更结构化的中间表示通常会带来更强感知依赖和更复杂的误差传播，可能在现实系统里不如更粗暴的 end-to-end recipe 稳定。

**What would change my mind**

- 出现大规模证据表明，直接从原始 human video 预训练的模型，在跨 embodiment、跨任务迁移上已经稳定优于引入结构化中间表示的方法。
- 相反，如果越来越多工作证明 object-centric / 3D / interaction-aware 表示可以稳定提升 controllability、sample efficiency 或 transfer，这个判断会被进一步强化。

**Next readings / experiments**

- 系统补 human-video-to-robot 里关于 action abstraction、contact representation、motion-centric representation 的工作。
- 把 [[2025-object-centric-3d-motion-field]] 和 [[2025-taste-rob]] 放到同一张比较表里，区分“生成更好的训练视频”和“提纯更好的动作表示”这两类路线。
- 留意 `3D geometry foundation model` 是否会开始对这条问题提供真正可执行的中间层，而不只是 perception bonus。

### Question 3

#### 下一阶段 embodied intelligence 的主要瓶颈更在 data recipe，还是 architecture innovation？

**Why this matters**

这决定你该把阅读资源更多投到哪里：如果主要瓶颈已经转到 data recipe，那么对 frontier system、数据分层、后训练和 evaluation 的跟踪优先级会显著上升；如果 architecture 仍然是主要杠杆，就应该继续更细地拆模型设计变化。

**Current belief**

我当前更倾向于：在当前阶段，data recipe、data mixture、post-training 和 system integration 的边际回报，可能已经不低于、甚至高于单点 architecture innovation。但 architecture 依然重要，尤其当它改变了动作空间、表示方式或训练目标时。

**Best evidence for this belief**

- [[xie-chen-data-survey-history-landscape-pyramid-structure-and-recipes-for-ai-and-robotics-data]] 明确把数据问题从“规模”提升到“结构与 recipe”的层面。
- [[robot-foundation-models-seminar-sergey-levine-2026-03-26]] 持续强调 data、objective、post-training，而不是只谈 backbone。
- [[gen-1-scaling-embodied-foundation-models-to-mastery]] 这种第一方 framing 也更像在讲完整系统如何长成，而不只是某个单模型改进。

**Best evidence against this belief**

- [[2024-pi-0]] 说明 architecture change 一旦打到动作表示和控制方式本身，收益仍然可能非常大。
- [[2026-dreamzero]] 这种工作如果继续成立，说明“换主干范式”仍然可能压过 recipe 微调。
- 如果开放数据依然远远不够，某些 architecture improvement 可能会在数据稀缺 regime 下继续发挥更高杠杆。

**What would change my mind**

- 如果未来最强进展主要来自 backbone / objective 的代际替换，而不是更好的数据和 post-training，我会把 architecture 的优先级重新提高。
- 如果越来越多 frontier 系统的进步都难以被单篇架构论文解释，而更像数据引擎、后训练和系统闭环的复合产物，这个判断会继续被强化。

**Next readings / experiments**

- 更系统地对照 open baseline 和 proprietary frontier system 的叙事差别。
- 补读明确讨论 `data mixture`、`post-training`、`failure recovery`、`evaluation bottleneck` 的来源，而不是只读 model paper。
- 如果这条判断持续稳定，可以单独长一篇 `data recipe vs architecture` synthesis。

## Review Triggers

- 当一个新 paper 明显改变了我对 `policy substrate`、`action representation` 或 `data bottleneck` 的判断时，优先更新这里。
- 当某个问题已经积累出稳定的正反证据时，把它升级成独立 `synthesis` 页面。
- 当某个问题连续几轮阅读都没有新证据推动，就考虑把它降级，避免页面变成永久悬而未决的问题池。

## Connections

- [[llm-wiki]]
- [[literature-review]]
- [[overview]]
- [[vision-language-action-models]]
- [[world-models]]
- [[ai-and-robotics-data]]
- [[3d-generation]]
- [[representation-learning]]

## Sources

- [[2024-openvla]]
- [[2024-pi-0]]
- [[2018-world-models]]
- [[2024-genie]]
- [[2026-dreamzero]]
- [[2026-lingbot-world]]
- [[xie-chen-data-survey-history-landscape-pyramid-structure-and-recipes-for-ai-and-robotics-data]]
- [[robot-foundation-models-seminar-sergey-levine-2026-03-26]]
- [[gen-1-scaling-embodied-foundation-models-to-mastery]]
- [[2025-taste-rob]]
- [[2025-object-centric-3d-motion-field]]
