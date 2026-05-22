---
layout: default
title: "Horizon Summary: 2026-05-22 (ZH)"
date: 2026-05-22
lang: zh
---

> From 23 items, 9 important content pieces were selected

---

1. [Freenet 以基于 WebAssembly 合约的去中心化点对点应用平台重新发布。](#item-1) ⭐️ 8.0/10
2. [谷歌在搜索中测试 AI 对话式广告并扩大 Direct Offers 试点](#item-2) ⭐️ 8.0/10
3. [开发者使用 Gemma4-31B 模型和 50GB 交换空间在 2021 款 MacBook 上本地索引一年视频](#item-3) ⭐️ 7.0/10
4. [1945 年三位一体核试验的丢失影像被修复](#item-4) ⭐️ 7.0/10
5. [Flipper One 发布，作为 Flipper Zero 更强大的 Linux 系统继任者。](#item-5) ⭐️ 7.0/10
6. [西雅图警方运营与私营公司及联邦机构共享情报的网络](#item-6) ⭐️ 7.0/10
7. [Google Antigravity 更新覆盖现有安装，严重破坏开发者工作流。](#item-7) ⭐️ 7.0/10
8. [Polymarket 5.88 亿笔交易研究揭示极端利润集中，前 1%用户攫取 76.5%利润。](#item-8) ⭐️ 7.0/10
9. [Simon Willison 发布 Datasette Agent，一个用于对话式数据查询与可视化的可扩展 AI 助手。](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Freenet 以基于 WebAssembly 合约的去中心化点对点应用平台重新发布。](https://freenet.org/) ⭐️ 8.0/10

Freenet 的原始创造者发布了该项目的彻底重构版本，现在它是一个去中心化的键值存储系统，其键是用于定义和管理状态的 WebAssembly 合约。新平台自 2025 年 12 月起已上线运行，River 聊天系统和 Delta 内容管理系统等早期应用已在其上运行。 这对于一个历史上重要的点对点项目而言是一次重大演进，它引入了一种新颖的架构，可能使构建去中心化应用变得更易用和高效。通过利用 WebAssembly 实现可移植、沙盒化的合约，它的目标是为无需中心化服务器的应用提供一个抗审查的平台。 一个核心的技术创新是要求每个合约为其状态定义一个可交换的合并操作，这使得更新能像“病毒”一样传播，并在几秒内实现全局状态一致性。该平台目前提供桌面安装程序，但缺乏移动端支持，应用在网页浏览器中运行，通过 WebSocket 本地连接到 Freenet 节点。

hackernews · sanity · May 21, 14:34 · [社区讨论](https://news.ycombinator.com/item?id=48223362)

**背景**: Freenet 是一个长期存在的、专注于抗审查通信的点对点网络项目，最初于 21 世纪初推出。2023 年，原基于 Java 的项目更名为 Hyphanet，而“Freenet”这个名字被重新用于这个新的基于 Rust 的重构项目。WebAssembly (WASM) 是一种可移植的二进制指令格式，允许用多种语言编写的代码在沙盒环境中安全运行，常用于区块链系统中的智能合约。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hyphanet">Hyphanet - Wikipedia</a></li>
<li><a href="https://blog.scottlogic.com/2019/11/26/webassembly-on-the-blockchain.html">WebAssembly on the Blockchain and JavaScript Smart Contracts</a></li>
<li><a href="https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type">Conflict-free replicated data type - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 讨论显示出社区对基于 WebAssembly 的合约模型和用于一致性的新颖合并操作有很高的技术兴趣。然而，关于项目治理也出现了重大争议，有评论称原开发团队的工作未经协商就被废弃，转而由另一个团队进行了此次重写。

**标签**: `#decentralization`, `#peer-to-peer`, `#webassembly`, `#distributed-systems`

---

<a id="item-2"></a>
## [谷歌在搜索中测试 AI 对话式广告并扩大 Direct Offers 试点](https://blog.google/products/ads-commerce/google-marketing-live-search-ads/) ⭐️ 8.0/10

谷歌宣布正在搜索中测试新的 AI 驱动广告格式，包括由 Gemini 生成的对话式产品推荐，并扩大其 Direct Offers 试点项目。Direct Offers 格式允许广告主在谷歌的 AI 模式中，向看似准备购买的用户直接展示独家优惠，如折扣。 这标志着谷歌广告策略向更具说服力、代理式商务的重大转变，可能模糊有机搜索结果与促销内容之间的界限。它引发了关于 AI 驱动说服性广告、为影响力模型收集数据以及搜索工具对用户效用降低的重大伦理担忧。 对话式推荐将使用 Gemini 调取相关产品并生成定制化说明，强调产品为何可能适合用户。Direct Offers 试点利用现有 Shopping 或 Performance Max 广告活动中的优惠，并在 AI 模式中展示它们。

hackernews · sofumel · May 21, 09:49 · [社区讨论](https://news.ycombinator.com/item?id=48220105)

**背景**: 谷歌的 Gemini 是一个 AI 助手和聊天机器人，类似于 OpenAI 的 ChatGPT，能够生成文本和回答问题。AI 驱动的广告使用机器学习来个性化和优化广告投放，而'代理式商务'指的是主动协助或引导用户完成购物决策的 AI 系统。谷歌的 AI 模式是搜索中的一个功能，提供 AI 生成的查询概览和答案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.cloud.google.com/retail/docs/conversational-filtering">Conversational product filtering overview | AI Commerce ...</a></li>
<li><a href="https://www.luzern.co/direct-offers-googles-first-agentic-ad-format/">Direct Offers : Google’s First Agentic Ad Format – Luzern</a></li>
<li><a href="https://www.jasminedirectory.com/blog/the-ethics-of-ai-persuasion-boundaries-in-2026-advertising/">The Ethics of AI Persuasion: Boundaries in 2026 Advertising</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了深切担忧，用户担心谷歌搜索将因无处不在的广告而变得无用，并认为对话式 AI 广告是'AI 广告邪恶本质的集中体现'。一个关键担忧是谷歌将收集数据，研究如何在用户明知被影响的情况下仍能有效影响他们，这拉响了伦理警报。一些人建议屏蔽谷歌机器人，或创建一个像维基百科那样的公共、非商业替代方案进行网络搜索。

**标签**: `#advertising`, `#search-engines`, `#ai-ethics`, `#google`, `#user-experience`

---

<a id="item-3"></a>
## [开发者使用 Gemma4-31B 模型和 50GB 交换空间在 2021 款 MacBook 上本地索引一年视频](https://blog.simbastack.com/indexed-a-year-of-video-locally/) ⭐️ 7.0/10

一位开发者在 2021 款 MacBook 上，通过运行 Gemma4-31B 大语言模型，并利用 50GB 的交换空间来满足内存需求，成功地对一年的个人视频素材进行了本地索引。该工具已以 MIT 许可证在 GitHub 上开源，名为 'framedex'。 这表明像视频索引这样通常需要云端或高端硬件支持的复杂 AI 任务，现在可以在消费级设备上完成，降低了个人数据管理和归档的门槛。它凸显了开源权重的大语言模型在处理个人媒体库方面的实际应用，兼顾了效率与隐私。 该过程需要大量使用交换空间（50GB），由于高写入周期，可能会加速 SSD 的磨损。Gemma4-31B 模型拥有 310 亿参数，很可能以量化形式（如 4-bit）使用以减少内存占用，但报告的实际内存使用量为 28.4 GiB，高于 4-bit 量化预期的约 19 GiB，这可能与图像上下文处理有关。

hackernews · asenna · May 21, 14:01 · [社区讨论](https://news.ycombinator.com/item?id=48222733)

**背景**: Gemma4-31B 是谷歌于 2026 年 4 月发布的一个拥有 310 亿参数的开源权重大语言模型，具有 256K token 的上下文窗口和多模态能力。交换空间是操作系统在物理 RAM 不足时用作虚拟内存的一部分存储空间，它允许应用程序使用比物理内存更多的内存，但代价是速度较慢和潜在的存储磨损。视频索引涉及分析视频内容以创建场景、物体、人脸或主题的可搜索数据库，传统上需要大量的计算资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/google/gemma-4-31B">google/gemma-4-31B · Hugging Face</a></li>
<li><a href="https://getdeploying.com/llms/gemma-4-31b">Gemma 4 31B - Specs & Pricing [2026]</a></li>
<li><a href="https://www.geeksforgeeks.org/operating-systems/swap-space-in-operating-system/">Swap Space in Operating System - GeeksforGeeks</a></li>

</ul>
</details>

**社区讨论**: 社区讨论包括对内存使用和 SSD 磨损问题的技术审视，有用户质疑大量交换空间的必要性，并指出 4-bit 量化的 Gemma4-31B 模型应占用约 19 GiB。其他人分享了在旧硬件上运行模型的类似经历，并对搜索索引的细节以及与达芬奇调色等工具集成进行人脸索引感兴趣。作者的开源发布受到欢迎，并讨论了视频编辑加速等未来应用。

**标签**: `#AI`, `#Video Indexing`, `#Local LLM`, `#Personal Archiving`, `#Machine Learning`

---

<a id="item-4"></a>
## [1945 年三位一体核试验的丢失影像被修复](https://spectrum.ieee.org/trinity-nuclear-test) ⭐️ 7.0/10

利用现代图像处理技术，修复了 1945 年首次原子弹爆炸试验——三位一体核试验中先前丢失或损坏的影像。这次修复为这一历史事件提供了新的视觉记录。 此次修复意义重大，因为它为这一历史转折点提供了更清晰、更详细的视觉记录，有助于历史研究和公众理解核时代的开端。它也展示了应用当代档案科学和图像处理技术来保存和修复脆弱历史材料的价值。 修复工作可能涉及处理档案胶片中常见的结构损伤和退化技术。原始试验于 1945 年 7 月 16 日山地战争时间上午 5 点 29 分在新墨西哥州进行，使用的是内爆式钚装置。

hackernews · pseudolus · May 21, 11:02 · [社区讨论](https://news.ycombinator.com/item?id=48220639)

**背景**: 三位一体试验是美国曼哈顿计划的一部分，是首次核武器爆炸试验。它使用了内爆式钚弹，与后来投在长崎的原子弹类型相同。这次试验标志着核时代的开始，并涉及 J·罗伯特·奥本海默等许多著名科学家。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Trinity_(nuclear_test)">Trinity (nuclear test)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fallout_from_the_Trinity_nuclear_test">Fallout from the Trinity nuclear test - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论反映了高度的参与，用户分享了关于试验的不确定性和伦理影响的历史背景。讨论还涵盖了试验对当地下风向居民的持久影响，他们在没有充分警告或补偿的情况下暴露于放射性沉降物，以及参观该地点的个人轶事揭示了关于辐射安全的混杂信息。

**标签**: `#history-of-technology`, `#nuclear-history`, `#image-restoration`, `#archival-science`, `#IEEE`

---

<a id="item-5"></a>
## [Flipper One 发布，作为 Flipper Zero 更强大的 Linux 系统继任者。](https://blog.flipper.net/flipper-one-we-need-your-help/) ⭐️ 7.0/10

Flipper 团队宣布了下一代设备 Flipper One，它搭载了更强大的瑞芯微 RK3576 处理器、完整的 Linux 操作系统，并具备 Wi-Fi/蓝牙扫描和本地 AI 处理等新功能。团队详细介绍了这些特性，并积极征求社区对产品方向的反馈。 此次发布之所以重要，是因为它标志着一个流行的开源硬件平台发生了重大演变，可能将 Flipper 从一个专注的渗透测试工具转变为更通用的、可编程的 Linux 手持设备。它的成功或失败可能会影响开源、极客友好的嵌入式设备领域格局。 关键的技术细节包括转向瑞芯微 RK3576 系统级芯片，这使得运行完整的 Linux 发行版和支持 AI 工作负载成为可能。团队明确表示正在就功能优先级和产品整体范围征求社区意见，这表明设计尚未最终确定。

hackernews · sandebert · May 21, 11:03 · [社区讨论](https://news.ycombinator.com/item?id=48220647)

**背景**: Flipper Zero 是一款流行的便携式多功能工具设备，被安全研究人员和爱好者用于 RFID/NFC 读取、红外控制和无线电信号分析等任务。它作为一个开源硬件项目而闻名，这意味着其设计文件是公开的，可供修改和协作。继任者的发布意味着这个社区驱动的工具将迎来一次重大的硬件和软件平台升级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flipper_Zero">Flipper Zero - Wikipedia</a></li>
<li><a href="https://flipper.net/">Flipper Zero — Portable Multi-tool Device for Geeks</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_open-source_hardware_projects">List of open-source hardware projects - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区情绪复杂，一方面对新芯片的强大性能和 Linux 能力感到兴奋，另一方面也对功能蔓延和产品方向不明确表示严重担忧。关键观点包括批评公告中“寻求帮助”的表述模糊，对没有键盘的情况下设备端 AI 的实用性表示怀疑，并提及了“第二系统效应”——即一个简单的初代产品之后，往往会推出一个过度复杂的继任者。

**标签**: `#embedded-systems`, `#hardware`, `#iot`, `#open-source-hardware`, `#developer-tools`

---

<a id="item-6"></a>
## [西雅图警方运营与私营公司及联邦机构共享情报的网络](https://prismreports.org/2026/05/20/seattle-shield-private-companies-surveillance/) ⭐️ 7.0/10

2026 年 5 月 20 日发布的一份调查报告揭露了“西雅图之盾”的存在，这是一个由西雅图警察局运营的情报共享网络，其成员包括亚马逊、Facebook 等私营公司，以及 ICE、FBI 等联邦机构。该网络促进了成员之间可疑活动报告和其他监控数据的共享。 此事意义重大，因为它代表了公私监控合作的显著扩张，引发了关于隐私、问责制以及其使命可能从反恐扩大到监控抗议或其他合法活动的关键问题。它突显了一种全国性的趋势，即企业安全机构与执法情报深度整合，可能绕过了传统的监督机制。 该网络被描述为像一个用于监控的企业 Slack 频道，使用安全门户和邮件群发来传播信息。值得注意的是，一些前成员如山达基教会和美国海军已表示不再参与，这表明该网络的成员构成是流动的。

hackernews · root-parent · May 21, 17:55 · [社区讨论](https://news.ycombinator.com/item?id=48226588)

**背景**: 近年来，公私情报共享伙伴关系不断增长，这通常由技术整合和实时犯罪中心推动。这些网络通常被描述为通过允许执法机构与拥有自身安全资源的私营实体之间及时交换信息，来加强公共安全和反恐工作。然而，它们的运作缺乏公众透明度，引发了人们对监控和数据共享范围的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://prismreports.org/2026/05/20/seattle-shield-private-companies-surveillance/">Amazon, Facebook, ICE have access to Seattle police ...</a></li>
<li><a href="https://www.gadgetreview.com/the-secret-intelligence-network-linking-local-seattle-police-to-amazon-facebook-and-the-fbi">The Secret Intelligence Network Linking Local Seattle Police to Amazon, Facebook, and the FBI - Gadget Review</a></li>
<li><a href="https://www.police1.com/real-time-policing/how-police-and-corporate-security-are-building-a-shared-intelligence-network">Real-time intelligence sharing between police and corporate ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示出怀疑与担忧并存。一些用户质疑报告的耸人听闻以及特别提及亚马逊和 Facebook，而另一些人则对企业参与监控表示警觉。讨论还涉及该网络公开宣称的反恐使命与其可能被用于更广泛监控之间的对比，并有评论提醒参与公司的员工注意他们在此类系统中所扮演的角色。

**标签**: `#surveillance`, `#privacy`, `#law-enforcement`, `#public-private-partnership`, `#ethics`

---

<a id="item-7"></a>
## [Google Antigravity 更新覆盖现有安装，严重破坏开发者工作流。](https://www.0xsid.com/blog/antigravity-bait-n-switch) ⭐️ 7.0/10

Google 对其 Antigravity AI 工具套件进行了一次破坏性更新，该更新自动覆盖了现有安装，移除了旧的 Antigravity IDE，并用新的、独立的聊天应用、CLI 工具和新版 IDE 取而代之。这迫使现有用户重新安装组件并重新配置环境，导致了严重的混乱和工作流中断。 这一事件凸显了谷歌这一主要开发者工具在用户体验和产品管理上的重大失败，动摇了依赖稳定工具的早期采用者和专业开发者的信任。它也为快速发展的 AI 辅助开发平台领域，提供了关于激进、不向后兼容的更新所带来风险的警示案例。 此次更新似乎是重大战略转向的一部分，将 'Antigravity' 从单一的 IDE 重新定位为包含多个独立应用的更广泛的 '智能体开发平台'。社区成员已经创建了应对方案，例如一个供 Mac 用户使用的 Python 脚本来恢复设置和合并数据库，这说明了手动恢复所需的复杂性。

hackernews · ssiddharth · May 21, 13:50 · [社区讨论](https://news.ycombinator.com/item?id=48222529)

**背景**: Google Antigravity 是谷歌推出的一个以 AI 智能体为核心的开发平台。它的设计理念是让 AI 不再仅仅是聊天侧边栏，而是为 AI 智能体提供一个专用的工作空间来辅助编程。该平台包含 AI 驱动的 IDE、命令行工具，并支持多种 AI 模型。在此次更新之前，它主要作为一个集成的开发环境存在。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/">Build with Google Antigravity, our new agentic development platform - Google Developers Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_Antigravity">Google Antigravity - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区表达了强烈的不满，将此次更新描述为令人困惑的、无视现有用户的 '诱饵调包' 行为。情绪包括批评谷歌缺乏产品专注度和一致性。技术用户正在分享脚本和变通方案以减轻损害，而其他人则指出这次经历削弱了他们对谷歌开发者工具的信任。

**标签**: `#google`, `#developer-tools`, `#user-experience`, `#ai-assistants`

---

<a id="item-8"></a>
## [Polymarket 5.88 亿笔交易研究揭示极端利润集中，前 1%用户攫取 76.5%利润。](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6443103) ⭐️ 7.0/10

对预测市场 Polymarket 上 5.88 亿笔交易（670 亿美元交易额）的分析发现，利润高度集中，前 1%的用户攫取了 76.5%的总利润。研究还发现，成功的交易者主要使用限价单提供流动性，而不成功的交易者倾向于使用市价单获取流动性。 这很重要，因为它首次提供了预测市场中极端不平等的大规模实证证据，挑战了预测市场是广泛参与的有效平台这一观念。研究结果强调了市场结构和订单类型策略如何导致巨大的结果差异，这对于理解金融市场、加密货币交易以及去中心化平台的设计具有重要意义。 研究发现，顶尖交易者 81%的收益来自体育市场，并且他们经常对不同球队下注。此外，月度表现显示出微弱的持续性，作者认为这可能源于样本选择而非持续的技能。

hackernews · vcf · May 21, 12:55 · [社区讨论](https://news.ycombinator.com/item?id=48221877)

**背景**: Polymarket 是一个基于加密货币的预测市场平台，用户可以对体育、政治、经济等未来事件的结果进行投注。在交易中，限价单是指定价格或更好价格买卖的订单，通常用于提供流动性；而市价单是以当前最佳可用价格立即买卖的订单，用于获取流动性。预测市场通过聚集群体智慧来预测事件概率，但其动态和利润分布的实证研究尚不充分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Polymarket">Polymarket - Wikipedia</a></li>
<li><a href="https://www.schwab.com/learn/story/3-order-types-market-limit-and-stop-orders">3 Order Types: Market, Limit, and Stop Orders</a></li>

</ul>
</details>

**社区讨论**: 社区讨论指出，成功的体育博彩者可能转向 Polymarket，因为传统体育博彩应用会封禁或限制赢利用户，而 Polymarket 不会。用户还就一边倒市场中的利润来源进行了辩论，质疑当某一结果概率极高时，谁承担了亏损方。一些人将这种利润集中度与 OnlyFans 等其它平台及更广泛经济中的不平等现象进行了比较。

**标签**: `#prediction-markets`, `#empirical-research`, `#trading-strategies`, `#cryptocurrency`, `#economics`

---

<a id="item-9"></a>
## [Simon Willison 发布 Datasette Agent，一个用于对话式数据查询与可视化的可扩展 AI 助手。](https://simonwillison.net/2026/May/21/datasette-agent/#atom-everything) ⭐️ 7.0/10

Simon Willison 宣布了 Datasette Agent 的首个版本，这是一个新的可扩展 AI 助手，将其 LLM Python 库与 Datasette 工具集成，支持对存储在 Datasette 中的数据进行对话式查询。初始版本包含了如 datasette-agent-charts 等用于生成图表的插件，并提供了一个使用 Gemini 3.1 Flash-Lite 的实时演示实例。 此次集成通过允许用户使用自然语言与数据库交互，代表了使数据探索更易访问的重要一步，降低了非技术用户的门槛。它结合了两个成熟且备受好评的项目（Datasette 和 LLM），创建了一个新颖的 AI 驱动工具，可以简化记者、研究人员和开发人员的数据分析工作流程。 该代理能够根据自然语言问题编写并执行 SQL 查询，如一个关于鹈鹕目击记录的查询所示。它可通过插件进行扩展，目前已发布了三个插件，包括使用 Observable Plot 进行可视化的 datasette-agent-charts。实时演示运行在 Gemini 3.1 Flash-Lite 上，选择它是因其在生成 SQLite 查询方面的成本效益和速度。

rss · Simon Willison · May 21, 19:52

**背景**: Datasette 是一个用于探索和发布数据的开源工具，由 Simon Willison 创建，它将 SQLite 数据库转换为交互式网站和 JSON API。LLM Python 库同样由 Willison 开发，是一个用于从命令行或 Python 代码与各种大语言模型（如 OpenAI、Gemini）交互的 CLI 工具和库。两者结合，实现了 AI 增强的数据分析，其中自然语言可用于查询结构化数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datasette.io/">Datasette: An open source multi-tool for exploring and ...</a></li>
<li><a href="https://github.com/simonw/llm">GitHub - simonw/llm: Access large language models from the command-line · GitHub</a></li>
<li><a href="https://agent.datasette.io/">Datasette Agent</a></li>

</ul>
</details>

**标签**: `#datasette`, `#ai-assistant`, `#data-analysis`, `#python`, `#llm`

---