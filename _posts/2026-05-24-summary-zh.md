---
layout: default
title: "Horizon Summary: 2026-05-24 (ZH)"
date: 2026-05-24
lang: zh
---

> From 7 items, 2 important content pieces were selected

---

1. [80386 微码通过黑盒逆向工程成功反汇编](#item-1) ⭐️ 8.0/10
2. [从第一性原理理解深度学习性能优化的基础指南](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [80386 微码通过黑盒逆向工程成功反汇编](https://www.reenigne.org/blog/80386-microcode-disassembled/) ⭐️ 8.0/10

一篇博客文章详细介绍了通过黑盒逆向工程技术，成功对英特尔 80386 处理器的微码进行反汇编和分析。这项工作建立在之前对 8086 微码进行反汇编的基础上，并得益于一张 80386 微码 ROM 的高分辨率图像。 这是历史计算机架构保存领域的一项重大成就，因为微码是控制 CPU 如何执行复杂指令的低层固件，通常是严格保密的。此次反汇编为了解这一基础性 32 位 x86 处理器的内部工作原理提供了宝贵资料，有助于保存工作、学术研究以及像 z386 这样旨在以微码级精度重现 CPU 的项目。 该分析采用了黑盒方法，这意味着其内部结构是从外部行为和观察中推断出来的，而非直接访问设计文档。博客文章特别提到，乘法和除法等操作的微码与已知算法高度吻合，揭示了其执行时序和可能涉及的底层硬件。

hackernews · nand2mario · May 23, 12:11 · [社区讨论](https://news.ycombinator.com/item?id=48247004)

**背景**: 微码是 CPU 内部的一层低级指令，负责将复杂的机器码指令翻译成更简单的硬件控制信号序列。英特尔 80386（i386）是一款具有历史意义的 32 位微处理器，为现代 x86 架构奠定了基础。黑盒逆向工程指在事先不了解系统内部设计的情况下分析其功能，通常通过观察其输入、输出和副作用来实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/I386">i386 - Wikipedia</a></li>
<li><a href="https://sesamedisk.com/z386-open-source-80386-microcode-recreation/">z386: Open-Source Microcode Recreation of the 80386 CPU</a></li>
<li><a href="https://capec.mitre.org/data/definitions/189.html">CAPEC - CAPEC-189: Black Box Reverse Engineering (Version 3.9)</a></li>

</ul>
</details>

**社区讨论**: 社区对这项令人印象深刻且难度极高的技术成就表示赞赏。评论还引发了相关话题的讨论，包括对如何从芯片显微图像中提取微码的好奇，以及提及了正在进行的、旨在使用原始微码重现 80386 的 z386 开源项目。

**标签**: `#reverse-engineering`, `#computer-architecture`, `#microcode`, `#x86`

---

<a id="item-2"></a>
## [从第一性原理理解深度学习性能优化的基础指南](https://horace.io/brrr_intro.html) ⭐️ 8.0/10

2022 年，一篇名为《从第一性原理让深度学习“飞”起来》的综合技术指南发布，系统性地阐述了让深度学习模型快速运行的硬件与软件原理。该指南涵盖了从 GPU 架构、CUDA 到混合精度训练、内核融合等高阶性能优化技术。 这份指南之所以重要，是因为它提供了对整个性能栈全面而基础的理解，这对于从业者高效训练和部署大模型至关重要。它揭示了支撑现代 AI 快速发展的算法、框架与硬件之间复杂的相互作用。 该指南使用了具体示例，比如对比 Python 操作与 NVIDIA A100 GPU 之间的巨大性能差距，来阐释核心概念。它还强调了性能可移植性的实际复杂性，指出模型在不同的导出格式、运行时和硬件目标上可能表现出不同的行为。

hackernews · tosh · May 23, 11:50 · [社区讨论](https://news.ycombinator.com/item?id=48246889)

**背景**: 深度学习性能严重依赖 GPU 等专用硬件和 CUDA 等软件栈，CUDA 是英伟达的并行计算平台。混合精度训练（同时使用 16 位和 32 位浮点数）和内核融合（将多个操作合并为一个高效内核）等优化技术，对于在模型训练和推理过程中实现高吞吐量和降低内存使用至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CUDA">CUDA - Wikipedia</a></li>
<li><a href="https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html">Train With Mixed Precision - NVIDIA Docs</a></li>
<li><a href="https://www.compilenrun.com/docs/library/pytorch/pytorch-performance-optimization/pytorch-fusion-optimization/">PyTorch Fusion Optimization | Compile N Run</a></li>

</ul>
</details>

**社区讨论**: 社区称赞该指南是经典之作，讨论中强调了英伟达在硬件领域的持续领导地位及其在算力、带宽等能力上的指数级增长。一个被提出的关键担忧是性能可移植性的“巨大混乱”，即模型在不同格式和运行时中表现不同。社区也提出了一些具体的技术问题，例如 PyTorch 如何优化像`x.cos().cos()`这样的连续操作。

**标签**: `#deep-learning`, `#performance`, `#systems`, `#gpu`, `#machine-learning`

---