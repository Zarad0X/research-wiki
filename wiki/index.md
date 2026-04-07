# Wiki Index

Automatically maintained by `python3 scripts/rebuild_index.py`.

## Overview (1)

- [[overview]] - Overview. Current map of the wiki and the operating thesis for this research knowledge base.

## Papers (13)

- [[2017-resnext]] - ResNeXt. A 2017 architecture paper that shows how a clean aggregated-transformation design can scale network capacity without turning model design into ad hoc complexity.
- [[2018-world-models]] - World Models. The 2018 paper that crystallized the world-model idea by learning compact latent dynamics and training a small controller inside imagined rollouts.
- [[2020-moco]] - MoCo. A 2020 self-supervised learning paper that turned contrastive visual representation learning into a scalable, reusable recipe through a momentum encoder and dynamic dictionary.
- [[2022-convnext]] - ConvNeXt. A 2022 architecture paper that re-examines ConvNet design through the lens of modern training and transformer-era practices, making convolutional backbones strong and clean again.
- [[2022-mae]] - MAE. A 2022 vision pretraining paper that made masked autoencoding into a scalable representation-learning recipe by reconstructing missing patches from visible ones.
- [[2023-dit]] - DiT. A 2023 generative modeling paper that shows transformers can serve as a strong diffusion backbone, turning architecture choice into a major scaling lever for image generation.
- [[2023-rt-2]] - RT-2. Google DeepMind's 2023 paper that established the VLA pattern by co-fine-tuning a web-pretrained VLM on robot actions expressed as text tokens.
- [[2024-genie]] - Genie. DeepMind's 2024 paper that learns an action-controllable interactive environment from unlabeled internet videos, positioning Genie as a foundation world model.
- [[2024-openvla]] - OpenVLA. A 7B open-source VLA that made the RT-2-style recipe reproducible and practical, with strong fine-tuning results and broad community impact.
- [[2024-pi-0]] - pi_0. Physical Intelligence's 2024 VLA paper that moves from discrete action tokens toward continuous action generation with a flow-matching action expert.
- [[2024-trellis]] - TRELLIS. A 2024 paper on structured 3D latents that unifies flexible 3D decoding with strong text- and image-conditioned asset generation quality.
- [[2026-dreamzero]] - DreamZero. A 2026 world action model paper that argues predictive video-and-action modeling can serve directly as zero-shot robot policy.
- [[2026-lingbot-world]] - LingBot-World. An open-source 2026 world simulator paper emphasizing long-horizon consistency, real-time interactivity, and narrowing the gap with proprietary world models.

## Topics (6)

- [[3d-generation]] - 3D Generation. A topic page for generative 3D asset creation, focusing on representation choice, conditioning, and output flexibility.
- [[ai-and-robotics-data]] - AI and Robotics Data. A topic page about data history, scaling constraints, and recipe design for AI and robotics systems.
- [[literature-review]] - Literature Review. A recurring research activity focused on organizing papers, tracking themes, and turning reading into reusable judgment.
- [[representation-learning]] - Representation Learning. A topic page about how useful internal representations are learned, reused, and scaled across vision, multimodal systems, and embodied intelligence.
- [[vision-language-action-models]] - Vision-Language-Action Models. A topic page for the VLA line of work, focusing on how RT-2, OpenVLA, and pi_0 define three distinct stages of the research trajectory.
- [[world-models]] - World Models. A topic page tracking the evolution from latent imagined dynamics to foundation-scale interactive world simulators and world action models.

## Methods (1)

- [[llm-wiki]] - LLM Wiki. A pattern where an LLM incrementally compiles research materials into a persistent markdown wiki instead of relying only on query-time RAG.

## Benchmarks

- None yet.

## People (3)

- [[andrej-karpathy]] - Andrej Karpathy. Researcher and educator who recently described the LLM Wiki pattern for personal and research knowledge bases.
- [[saining-xie]] - Saining Xie. Researcher whose work repeatedly lands on elegant, high-leverage representation and architecture primitives, from ResNeXt and MoCo to DiT and newer world-model ambitions.
- [[sergey-levine]] - Sergey Levine. UC Berkeley professor whose work spans reinforcement learning, decision making, and robotic foundation models.

## Ideas (1)

- [[research-questions]] - Research Questions. A place to accumulate open questions, suspicious assumptions, and possible directions that emerge during reading.

## Syntheses (3)

- [[rt-2-openvla-pi-0]] - RT-2 vs OpenVLA vs pi_0. A first-pass synthesis comparing RT-2, OpenVLA, and pi_0 as three milestones in the VLA research trajectory.
- [[saining-xie-research-taste-and-representative-works]] - Saining Xie Research Taste and Representative Works. A synthesis of Saining Xie's research taste, recurring design instincts, and representative works across representation learning, architectures, and world models.
- [[world-models-genie-dreamzero-lingbot-world]] - World Models vs Genie vs DreamZero vs LingBot-World. A first-pass synthesis of how four papers mark different phases in the world-model research trajectory.

## Sources (6)

- [[a-7-hour-marathon-interview-with-saining-xie-world-models-ami-labs-yann-lecun-fei-fei-li-and-42]] - A 7-hour marathon interview with Saining Xie: World Models, AMI Labs, Yann LeCun, Fei-Fei Li, and 42. A long-form March 2026 interview where Saining Xie lays out his world-model ambitions, representation-learning instincts, and critique of the Valley's LLM fixation.
- [[karpathy-llm-wiki-gist]] - Karpathy - llm-wiki gist. Karpathy's April 4, 2026 gist that describes the LLM Wiki pattern as a persistent, interlinked markdown knowledge base maintained by an LLM.
- [[robot-foundation-models-seminar-sergey-levine-2026-03-26]] - Robot Foundation Models Seminar (Sergey Levine, 2026-03-26). A March 26, 2026 seminar summarizing the Physical Intelligence roadmap from pi_0 to pi_0.5 and pi*0.6, with emphasis on reasoning, data scaling, and RL post-training.
- [[robotic-foundation-models-sergey-levine-talk]] - Robotic Foundation Models (Sergey Levine talk). DAI 2024 keynote where Sergey Levine frames robotic foundation models around three central questions: data, objective, and post-training.
- [[saining-xie-homepage]] - Saining Xie homepage. Official homepage captured on 2026-04-07, useful for tracing Saining Xie's own framing of his research agenda, representative works, and shift toward world models.
- [[xie-chen-data-survey-history-landscape-pyramid-structure-and-recipes-for-ai-and-robotics-data]] - Xie Chen: Data Survey — History, Landscape, Pyramid Structure, and Recipes for AI and Robotics Data. A March 31, 2026 podcast episode that frames AI and robotics data through history, scaling limits, landscape structure, and practical recipe design.
