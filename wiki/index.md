# Wiki Index

Automatically maintained by `python3 scripts/rebuild_index.py`.

## Now (1)

- [[now]] - Now. A living dashboard of the questions, theses, programs, and readings that currently matter most in this research wiki.

## Overview (1)

- [[overview]] - Overview. The stable worldview page for this research wiki, centered on current bets, tensions, and the owner's evolving research agenda.

## Questions (1)

- [[research-questions]] - Research Questions. A research decision panel for tracking current beliefs, competing evidence, and the next readings that could actually change my mind.

## Theses (1)

- [[working-theses]] - Working Theses. A page for current working theses about where the field is going, what matters, and what would change my mind.

## Programs (1)

- [[human-video-to-robot-learning]] - Human Video to Robot Learning. A live research program on what representations, data recipes, and system interfaces are needed to turn human interaction video into executable robot behavior.

## Reviews

- None yet.

## Topics (7)

- [[3d-generation]] - 3D Generation. A topic page for generative 3D asset creation, focusing on representation choice, conditioning, and output flexibility, while increasingly touching the broader question of 3D representations as reusable infrastructure.
- [[ai-and-robotics-data]] - AI and Robotics Data. A topic page about data history, scaling constraints, and recipe design for AI and robotics systems.
- [[articulated-object-reconstruction-and-hoi]] - Articulated Object Reconstruction and HOI. A topic page for articulated object reconstruction and hand-object interaction, focusing on how structure, motion, and interaction cues support real2sim and manipulation research.
- [[literature-review]] - Literature Review. A recurring research activity focused on organizing papers, tracking themes, and turning reading into reusable judgment.
- [[representation-learning]] - Representation Learning. A topic page about how useful internal representations are learned, reused, and scaled across vision, multimodal systems, and embodied intelligence.
- [[vision-language-action-models]] - Vision-Language-Action Models. A topic page for the VLA line of work, focusing on how RT-2, OpenVLA, and pi_0 define three distinct stages of the research trajectory.
- [[world-models]] - World Models. A topic page tracking the evolution from latent imagined dynamics to foundation-scale interactive world simulators and world action models.

## Papers (28)

- [[2017-resnext]] - ResNeXt. A 2017 architecture paper that shows how a clean aggregated-transformation design can scale network capacity without turning model design into ad hoc complexity.
- [[2018-world-models]] - World Models. The 2018 paper that crystallized the world-model idea by learning compact latent dynamics and training a small controller inside imagined rollouts.
- [[2020-moco]] - MoCo. A 2020 self-supervised learning paper that turned contrastive visual representation learning into a scalable, reusable recipe through a momentum encoder and dynamic dictionary.
- [[2022-convnext]] - ConvNeXt. A 2022 architecture paper that re-examines ConvNet design through the lens of modern training and transformer-era practices, making convolutional backbones strong and clean again.
- [[2022-mae]] - MAE. A 2022 vision pretraining paper that made masked autoencoding into a scalable representation-learning recipe by reconstructing missing patches from visible ones.
- [[2023-convnext-v2]] - ConvNeXt V2. A 2023 paper that co-designs ConvNet architecture and masked autoencoding, showing that modern convolutional backbones can keep improving when representation learning and architecture are optimized together.
- [[2023-dit]] - DiT. A 2023 generative modeling paper that shows transformers can serve as a strong diffusion backbone, turning architecture choice into a major scaling lever for image generation.
- [[2023-rt-2]] - RT-2. Google DeepMind's 2023 paper that established the VLA pattern by co-fine-tuning a web-pretrained VLM on robot actions expressed as text tokens.
- [[2024-cambrian-1]] - Cambrian-1. A 2024 fully open, vision-centric MLLM paper that treats multimodal systems as a way to evaluate and improve visual representations rather than as language systems with image inputs attached.
- [[2024-genie]] - Genie. DeepMind's 2024 paper that learns an action-controllable interactive environment from unlabeled internet videos, positioning Genie as a foundation world model.
- [[2024-ipod]] - IPoD. A 2024 CVPR paper on generalizable 3D object reconstruction from single RGB-D images, showing Xiaoguang Han's group's continued emphasis on robust 3D reconstruction as reusable infrastructure.
- [[2024-openvla]] - OpenVLA. A 7B open-source VLA that made the RT-2-style recipe reproducible and practical, with strong fine-tuning results and broad community impact.
- [[2024-pi-0]] - pi_0. Physical Intelligence's 2024 VLA paper that moves from discrete action tokens toward continuous action generation with a flow-matching action expert.
- [[2024-richdreamer]] - RichDreamer. A 2024 CVPR paper that uses a normal-depth diffusion prior to improve detail richness in text-to-3D, representing Xiaoguang Han's group at the strong 3D generation end of the spectrum.
- [[2024-trellis]] - TRELLIS. A 2024 paper on structured 3D latents that unifies flexible 3D decoding with strong text- and image-conditioned asset generation quality.
- [[2025-object-centric-3d-motion-field]] - Object-centric 3D Motion Field. A 2025 paper that proposes dense object-centric 3D motion fields as an action representation for robot learning from human videos, aiming to transfer manipulation knowledge without robot demonstrations.
- [[2025-reconviagen]] - ReconViaGen. A 2025 paper on accurate multi-view 3D object reconstruction via generation, showing how Xiaoguang Han's group tries to fuse reconstruction priors with generative priors instead of treating them as separate camps.
- [[2025-stable-score]] - Stable-SCore. A 2025 CVPR paper on stable registration-based 3D shape correspondence, representing Xiaoguang Han's group's geometry-heavy line focused on robustness and real applications.
- [[2025-taste-rob]] - TASTE-Rob. A 2025 CVPR paper that uses task-oriented hand-object interaction video generation to support more generalizable robotic manipulation, marking Xiaoguang Han's group's clearer move toward robotics.
- [[2025-vggt]] - VGGT. A CVPR 2025 best paper that turns multi-view geometry into a large feed-forward transformer problem, jointly predicting cameras, depth, point maps, and tracking features from one to hundreds of views.
- [[2026-arthoi]] - ArtHOI. A CVPR 2026 highlight paper that reconstructs 4D hand-articulated-object interactions from a single monocular RGB video by coordinating and refining multiple foundation-model priors.
- [[2026-articulated-reconstruction-transformer]] - Articulated Reconstruction Transformer. A CVPR 2026 paper on category-agnostic, feed-forward articulated object reconstruction from sparse multi-state RGB images, using transformer-decoded part slots for geometry, texture, and articulation.
- [[2026-articulation-in-motion]] - Articulation in Motion. An ICLR 2026 paper that reconstructs articulated objects and analyzes part mobility from a start-state scan plus an interaction video, using dual-Gaussian dynamic-static disentanglement without part-count priors.
- [[2026-dreamzero]] - DreamZero. A 2026 world action model paper that argues predictive video-and-action modeling can serve directly as zero-shot robot policy.
- [[2026-lingbot-world]] - LingBot-World. An open-source 2026 world simulator paper emphasizing long-horizon consistency, real-time interactivity, and narrowing the gap with proprietary world models.
- [[2026-monoart]] - MonoArt. A 2026 paper on monocular articulated 3D reconstruction that turns single-image input into simulation-ready part structure and kinematics through progressive structural reasoning.
- [[2026-motioncrafter]] - MotionCrafter. A 2026 paper on dense geometry and motion reconstruction from monocular video with a 4D VAE, extending Xiaoguang Han's group's recent work toward dynamic 4D reconstruction and motion understanding.
- [[2026-texspot]] - TexSpot. A 2026 paper on 3D texture enhancement using a spatially-uniform point latent representation, extending Xiaoguang Han's group's 3D generation line into higher-fidelity texture modeling.

## Sources (8)

- [[a-7-hour-marathon-interview-with-saining-xie-world-models-ami-labs-yann-lecun-fei-fei-li-and-42]] - A 7-hour marathon interview with Saining Xie: World Models, AMI Labs, Yann LeCun, Fei-Fei Li, and 42. A long-form March 2026 interview where Saining Xie lays out his world-model ambitions, representation-learning instincts, and critique of the Valley's LLM fixation.
- [[gen-1-scaling-embodied-foundation-models-to-mastery]] - GEN-1: Scaling Embodied Foundation Models to Mastery. Generalist's April 2, 2026 blog post framing GEN-1 as a frontier embodied foundation model system that reaches a first notion of mastery through reliability, speed, and improvisation.
- [[karpathy-llm-wiki-gist]] - Karpathy - llm-wiki gist. Karpathy's April 4, 2026 gist that describes the LLM Wiki pattern as a persistent, interlinked markdown knowledge base maintained by an LLM.
- [[robot-foundation-models-seminar-sergey-levine-2026-03-26]] - Robot Foundation Models Seminar (Sergey Levine, 2026-03-26). A March 26, 2026 seminar summarizing the Physical Intelligence roadmap from pi_0 to pi_0.5 and pi*0.6, with emphasis on reasoning, data scaling, and RL post-training.
- [[robotic-foundation-models-sergey-levine-talk]] - Robotic Foundation Models (Sergey Levine talk). DAI 2024 keynote where Sergey Levine frames robotic foundation models around three central questions: data, objective, and post-training.
- [[saining-xie-homepage]] - Saining Xie homepage. Official homepage captured on 2026-04-07, useful for tracing Saining Xie's own framing of his research agenda, representative works, and shift toward world models.
- [[xiaoguang-han-cuhksz-faculty-page]] - Xiaoguang Han CUHK-Shenzhen faculty page. First-party source for Xiaoguang Han's recent publication clusters, especially across 3D generation, avatar/human modeling, and interaction-oriented robotics work.
- [[xie-chen-data-survey-history-landscape-pyramid-structure-and-recipes-for-ai-and-robotics-data]] - Xie Chen: Data Survey — History, Landscape, Pyramid Structure, and Recipes for AI and Robotics Data. A March 31, 2026 podcast episode that frames AI and robotics data through history, scaling limits, landscape structure, and practical recipe design.

## People (6)

- [[ami-labs]] - AMI Labs. Research lab and company centered on world models, abstract real-world representations, and controllable agentic systems, closely aligned with Saining Xie's recent direction.
- [[andrej-karpathy]] - Andrej Karpathy. Researcher and educator who recently described the LLM Wiki pattern for personal and research knowledge bases.
- [[generalist-ai]] - Generalist AI. Frontier embodied AI company framing robot learning as a scaling, data-engine, and full-system problem rather than just a narrow policy architecture problem.
- [[saining-xie]] - Saining Xie. Researcher whose work repeatedly lands on elegant, high-leverage representation and architecture primitives, from ResNeXt and MoCo to DiT and newer world-model ambitions.
- [[sergey-levine]] - Sergey Levine. UC Berkeley professor whose work spans reinforcement learning, decision making, and robotic foundation models.
- [[xiaoguang-han]] - Xiaoguang Han. Researcher whose recent work spans 3D generation, reconstruction, avatar/human modeling, and a newer bridge from hand-object interaction into robotics-oriented video generation.

## Methods (1)

- [[llm-wiki]] - LLM Wiki. A pattern where an LLM incrementally compiles research materials into a persistent markdown wiki instead of relying only on query-time RAG.

## Benchmarks

- None yet.

## Ideas (1)

- [[research-taste]] - Research Taste. A first-class page for recurring research taste, filters, and what kinds of work feel high-leverage or suspicious.

## Syntheses (5)

- [[articulated-object-reconstruction-real2sim]] - Articulated Object Reconstruction for Real2Sim. A reading-oriented map of papers on articulated object reconstruction and digital-twin building, focusing on what is most relevant for real-to-sim pipelines.
- [[rt-2-openvla-pi-0]] - RT-2 vs OpenVLA vs pi_0. A first-pass synthesis comparing RT-2, OpenVLA, and pi_0 as three milestones in the VLA research trajectory.
- [[saining-xie-research-taste-and-representative-works]] - Saining Xie Research Taste and Representative Works. A synthesis of Saining Xie's research taste, recurring design instincts, and representative works across representation learning, architectures, and world models.
- [[world-models-genie-dreamzero-lingbot-world]] - World Models vs Genie vs DreamZero vs LingBot-World. A first-pass synthesis of how four papers mark different phases in the world-model research trajectory.
- [[xiaoguang-han-recent-papers-2024-2025]] - Xiaoguang Han Recent Papers (2024-2025). A reading-oriented synthesis of Xiaoguang Han's recent paper clusters across 3D generation, reconstruction, human modeling, and an emerging bridge toward robotics-oriented interaction work.
