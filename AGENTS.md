# 项目 AGENTS.md · 数学大师制造

## 项目定位

本项目是 **AI 数学大师制造项目**，不是单纯的写代码项目，也不是星学项目。

项目从星学领域的 POC 实验中继承了“用稀疏关系工程化大师知道该判断什么”的方法论线索，但数学领域的动态启发能力尚未验证。当前目标不是照搬星学静态图，而是制造一个能做数学研究、并能在动态研究状态中接受最小可验证引导的 AI 大师。

**"数学大师"的定义**：本项目语境中的"数学大师"，指能做数学研究的 AI——提出猜想、构造证明、发现新定理、在复杂数学问题面前知道该从哪个方向切入、该调用哪些数学工具、该沿什么路径思考。不是只会做题的解题机器，而是具备研究品味的数学家。

**"最通用的数学大师"**：本项目目标是制造**最通用的数学大师**，不是某个特定数学领域的专家系统。数学大师应该能覆盖代数、几何、分析、拓扑、数论、组合、逻辑、范畴论等全部数学领域，能在任意数学问题面前知道该判断什么。当前以矩条件极差题等具体场景作为POC实验场，但这是验证方法论的实验场景，不是项目的终态边界。依赖图的构建从具体领域切入（如代数拓扑），逐步扩展到全部数学领域——不预设领域边界。

**"新系统"的硬边界**：本项目语境中的"新系统"，默认且专指为数学研究而建设的知识系统与思维导航系统。星学项目中的 `qizheng/`、`study-notes/`、MOIRA Java、Swiss Ephemeris 等是**参考实现和方法论证据链**，不是新系统本体。

### 本项目与星学项目的关系

本项目从 `~/MOIRA_chinese_astrology-main/`（已复制到当前目录 `/data/master-mind/`）的星学研究中继承而来。星学POC是方法论证据来源，但不能自动证明数学研究中的动态启发有效，也不能让星学运行时支配数学架构。

本项目要做的是：**把这条方法论作为可证伪假设，在数学研究领域重新定义对象、实现闭环并独立验证。**

星学是第一个实验场，数学是第二个。如果方法论在数学领域同样成立，它的意义将不限于数学——任何复杂知识体系的"综述博士"角色都可能被工程化。

## 核心假设（从星学信念降级并在数学中重验）

星学项目63号文档提出“完美提示词可以通过经典计算产生”。123号架构已将它从硬公理降为可证伪假设：

> 在部分问题族和研究状态上，确定性结构计算、状态估计、历史因果效果与数学验证，能否共同选择一个低成本、低泄漏、能增加已验证进展的最小干预？

当前纪律：

1. **大师价值的一部分是激活方向**，但不能预设全部价值都等于提示词；
2. **提示是动态策略，不是一次性完整文本**；
3. **经典计算负责确定部分**：类型/前提过滤、遍历、模式匹配、稀疏候选、预算、权限和审计；
4. **启发是否有效必须实验验证**，不能由图中存在一条边定义性保证；
5. **稀疏矩阵是计算视图，不是真值本体**；K/T/H分别是数学语义、事件状态和启发规则的查询投影；
6. 若去掉答案等价信息后增益消失，系统必须降级为诚实的静态知识/证明编译器。

### 两种博士

| 类型 | 特征 | 对应角色 | 本项目是否工程化 |
|---|---|---|---|
| 综述博士 | 知识体系全掌握、全能灵活运用 | 知道在什么时候该看什么、该结合什么 | **是，这是本项目的目标** |
| 论文博士 | 负责创新 | 创造新知识、新方法 | 不在本次工程化范围，但不排斥 |

### 大师的"一次在场"

旧xishujuzhen只编码Master预先写入的关系；新系统允许从成功/失败事件中发现**候选**启发，但候选必须经最小干预、迁移和泄漏审计后才可发布。

这意味着：**大师的一次在场仍然重要，但不能再把一次手写路线冒充系统自主发现。**

- 候选知识/启发的质量受构建者、抽取器和证据共同限制；
- 已验证关系需要版本、适用域、反例、模型范围和退役机制；
- 图构建是认知整理，因果发布是另一项独立工作。

## 方法论核心（继承方向，数学动态能力待验证）

星学POC可证明静态关系提示在其场景中的局部价值；迁移到数学时，本体、运行状态、验证标准和答案泄漏边界都必须重做，不能只替换依赖图内容。

### 稀疏关系计算

“三维稀疏矩阵”保留为历史直觉：分析节点×思维意识×上下文。123号后的精确模型不是一张万能矩阵，而是：

- K：按`requires/uses/generalizes/analogous/verified_by`等关系拆分的稀疏视图；
- T：不可变事件、状态快照和时序投影；
- H：规则—条件—动作及效果证据的稀疏因子视图。

稀疏性仍然成立：总知识量很大，但每个具体研究状态只激活少量关系。矩阵负责候选计算，不负责数学真值。

### 两种环路

| 环路类型 | 特征 | 判别标准 | 处理方式 |
|---|---|---|---|
| 平面环路 | 不同时间事件投影回同一规范化状态 | 开放义务、证据门和冲突无改善 | 停止或换策略 |
| 螺旋上升环路 | 返回同一抽象状态类，但更细粒度状态进展 | 同一任务/schema下进展向量不恶化且至少一项严格改善 | 允许继续并保存进展证据 |

数学中的例子：
- 平面环路：反复用同一个引理证明同一个结论，没有新进展
- 螺旋环路：第一轮用范畴论视角看群同态，第二轮用范畴论视角看拓扑空间，第三轮用范畴论视角看流形——三次都"回到"范畴论，但每次在不同数学领域深化

### 依赖图作为提示，而非替代思考

系统不是自动推理引擎，而是**提示生成器**。分三层：

1. **脚本计算依赖**：给定当前研究上下文，从稀疏矩阵中提取相关依赖子图
2. **AI 在依赖图提示下完成分析**：AI 看到依赖子图后，理解依赖关系，沿依赖路径完成判断
3. **粒度拆分 → 小图分析 → 大图综合**：复杂时拆分成多个小依赖路径图，逐个分析后在上下文允许时汇总成更大综合

关键约束：**依赖图的大小必须被控制在一个合理范围内**。不是把整个三维稀疏矩阵一次性呈现给 AI，而是提取当前上下文相关的子图。

### 系统不做判断，只做依赖计算和提示生成

| 维度 | 系统做 | AI 做 |
|---|---|---|
| 依赖关系 | 计算、存储、遍历、子图提取、环检测 | 理解、沿路径思考 |
| 判断 | 不做 | 在提示下完成数学判断 |
| 创造 | 不能发现未编码的新依赖 | 可以即兴发现新连接（论文博士侧面） |

### 认识论位置

本方法论在 AI 史上的独特位置：

| 路径 | 工程化什么 | 不工程化什么 | 核心区别 |
|---|---|---|---|
| 1980s 专家系统 | 判断规则 + 推理过程 | — | 试图替代专家判断，失败了 |
| 2020s 大语言模型 | — | 判断本身 | 有判断力但无方向感 |
| 2020s RAG | 文档检索 | 思维路径 | 给资料但不给思维方向 |
| **xishujuzhen** | **"知道该判断什么"** | **判断本身** | **给思维方向但不替 AI 判断** |

与 chain-of-thought 的区别：CoT 是线性思维链（A→B→C→结论），xishujuzhen 是图结构思维网（有分叉、汇聚、螺旋上升的环路）。

## 项目目标

建设一个 **"数学知识系统 + 依赖图导航 + AI 智能研究"** 的数学大师系统。

让整套项目可以辅助 AI 完成：

1. **数学研究导航** —— 面对一个数学问题，知道该从哪个方向切入、该调用哪些数学工具、该沿什么路径思考。
2. **猜想提出与验证** —— 在依赖图提示下，提出有意义的数学猜想，并知道该用什么工具验证。
3. **证明构造** —— 沿依赖路径组织证明思路，知道哪些定理是前置、哪些是引理、哪些是工具。
4. **跨领域类比** —— 发现不同数学领域之间的结构同构（如范畴论视角下的统一），并知道这种类比的适用边界。
5. **知识持续深化** —— 把数学文献、研究经验、跨领域洞察消化进知识系统和依赖图，形成能自我演化的数学认知系统。

**总体架构与建设计划状态**：122号v1—v3完成工程断层、K/T/H和证据边界复核；123号以`系统探讨.md`全文为母本，从第一性原理将目标系统定义为类型化任务/工作区、不可变事件、表示变换、启发规则、证据状态和受约束最小干预，并给出DYN-0—7与Phase 0—7。旧七步骤正式降为legacy静态重建器。项目启动认知见80号，证据复核见122号v3，当前最高架构与建设基线见 <ref_file file="/data/master-mind/dev-docs/123-v1-2026-08-05-数学大师系统全景复盘与第一性原理重构计划.md" />。

## 四类载体的分工

| 载体 | 角色 | 不是什么 |
|---|---|---|
| `math-notes/`（待建） | **数学知识系统本体**：数学知识、研究方法、领域地图、工具索引 | 不是教材摘录堆，也不是代码文档 |
| `math-notes/数学意识/`（待建） | **弥漫性数学思维**：数学直觉、美感、类比思维、证明策略等贯穿整个研究过程的底层思维模式 | 不是某个问题的专属解法 |
| `xishujuzhen/`（待建） | **依赖图导航系统**：稀疏矩阵、依赖计算、环检测、提示生成 | 不是知识仓库，不是计算引擎 |
| 数学计算工具（待选型） | **经典计算底座**：符号计算、数值计算、定理证明辅助 | 不是知识系统本体 |
| 星学项目文件（当前目录中） | **方法论参考实现**：POC1-8 验证记录、xishujuzhen 设计文档、星学知识系统结构 | 不是数学项目的工作对象 |
| AI | 读取依赖图提示，依照知识系统做数学研究和判断 | 不能把无出处记忆悄悄当成已证定理 |

## 星学参考索引（方法论证据链，不是工作对象）

以下文档是星学项目中产生的**方法论资产**，对本项目有直接参考价值。它们不是数学项目的工作对象，但在设计数学领域的依赖图、知识系统结构、验证方案时，应作为方法论参考查阅。

**重要**：以下所有路径在星学项目中指向 `~/MOIRA_chinese_astrology-main/`，在本目录中已复制为相对路径（去掉前缀即可在本目录访问）。

### 核心方法论文档（最高参考价值）

| 文档 | 内容 | 对数学项目的参考价值 |
|---|---|---|
| `dev-docs/63-星学意识与螺旋上升的稀疏矩阵.md` | **整个方法论的起源**：从直觉画面到核心信念的完整对话记录。三维稀疏矩阵、两种环路、依赖图作为提示、数字化的大师、核心信念 | **必读**。数学项目的整个方法论框架来自这里 |
| `dev-docs/64-xishujuzhen-POC验证方案.md` ~ `dev-docs/77-xishujuzhen-POC8验证方案.md` | **POC1-8 完整验证体系**：从5节点小图到71节点大图、从静态分析到动态螺旋、从开环到闭环审计 | **必读**。数学项目的验证方案应参考这套实验设计 |
| `dev-docs/71-xishujuzhen-POC5验证结果.md` | POC-5 结果：边际增益+3.95，B组9.75 vs A组5.8 | 验证方法论的量化证据 |
| `dev-docs/73-xishujuzhen-POC6验证结果.md` | POC-6 结果：边际增益+5.92，交叉审计比AI自审更严格 | 交叉审计方法的参考 |
| `dev-docs/75-xishujuzhen-POC7验证结果.md` | POC-7 结果：边际增益+4.08，大规模依赖图可行（71节点100%覆盖） | 大规模可行性证据 |
| `dev-docs/69-xishujuzhen-POC4验证结果.md` | POC-4 结果：双宫联动+跨宫依赖场景，19节点25边，边际增益+3.20 | 复杂场景可行性证据 |
| `dev-docs/76-xishujuzhen闭环审计纠正流程优化方案.md` | 闭环审计流程：审计→反馈→修正→再审→直到无瑕疵，最大3轮 | 质量保证流程参考 |
| `dev-docs/78-xishujuzhen下一代工作流-从文字随机到拓扑覆盖.md` | **下一代工作流数学本质分析**：依赖图G是规范化拓扑结构，展开图G'是G的覆盖，审计是覆盖验证φ:G'→G。HoTT框架 | **高价值**。数学项目可能直接用到这套拓扑视角 |
| `dev-docs/79-xishujuzhen下一代工作流技术选型.md` | 技术选型：ArangoDB（多模型：图+文档+键值）作为依赖图数据库 | **技术架构基础**。数学版在此基础上新增 Lean 4/MathLib、SageMath、arXiv 管道，见 81 号文档 |
| `dev-docs/80-数学大师项目启动认知基础.md` | **项目启动认知**：成功的数学大师能解决什么问题（从具体计算到跨领域统一）、需要积累什么知识（P0经典/P1专题/P2前沿三层）、依赖图初始结构设计。是整个数学项目的认知起点 | **必读**。项目启动的认知基础 |
| `dev-docs/81-数学大师项目基础设施技术选型.md` | **数学版技术选型更新**：ArangoDB 保留 + 新增三层验证器阶梯（SymPy→SageMath→Lean 4）+ arXiv HTML 管道 + MathLib 依赖图导入 | **必读**。数学项目基础设施方案 |
| `dev-docs/82-题库作为数学思维积累方向.md` | **题库方法论**：解法路径=依赖图实证边、一题多解=图结构实证、跨领域映射边来源、难度梯度=POC阶梯、卡点=依赖图缺口发现、结构化格式、建设路径 | **必读**。题库是数学思维积累的主要方向 |
| `dev-docs/83-解法路径的三层提取与POC验证方案.md` | **三层提取方法论+POC**：L1解题思路（具体步骤）→L2数学思维（弥漫性模式，AI二次分析）→L3新的思维方式（范式级，改变图结构，AI三次分析）。三组对照POC（A=仅L1 / B=L1+L2 / C=L1+L2+L3），测试跨题近迁移和远迁移复用增益 | **必读**。L3是数学版相比星学版的本质增量 |
| `dev-docs/84-大师-POC-1验证方案.md` | **大师-POC-1正式方案**：矩条件极差题场景（第一问证明+第二问指数纠错），8节点10边依赖图（极端检验↔数值检验意识螺旋环路），A组（教材Markdown）vs B组（依赖图提示JSON）对照，5维评分。**核心测试点**：B组依赖图含"数值检验意识"节点，能否帮助AI发现第二问指数错误（-1/3应为-3/2）。原始题面来源：`~/Documents/Playground 2/docs_for_next_time/2026-03-06-矩条件极差题-详细推导与排错记录.md` | **必读**。数学版方法论验证的起点 |
| `dev-docs/85-大师-POC-1验证结果.md` | **大师-POC-1结果**：B组显著优于A组（综合5.00 vs 3.25，边际增益+1.75/5分制≈+3.50/10分制）。**核心发现**：两组都发现了指数错误，但只有B组给出了正确指数n^(-3/2)——A组将三点构型上界O(1/n)误认为下界，B组依赖图的"数值检验意识"节点和螺旋环路提示帮助其系统检验多个候选并正确区分上界与下界。验证了核心信念在数学领域成立 | **必读**。首个数学POC成功证据 |
| `dev-docs/86-从星学项目同步下一代工作流基础设施.md` | **从星学同步基础设施**：星学项目已完成POC-9（下一代工作流），拓扑覆盖验证1次通过100%覆盖。同步资产：①HoTT化理论（78号文档）——对数学更自然，数学对象本身就是拓扑结构；②TopologyVerifier代码——与领域无关，直接复用；③七步骤工作流——meta/normal分离，审计只做1次；④ArangoDB基础设施——共用星学实例。后续POC从文字对照升级为拓扑确定性验证 | **必读**。后续POC的方法论基础 |
| `dev-docs/87-大师-POC-2验证方案.md` | **大师-POC-2方案**：矩条件极差题第二问完整证明（n^(-3/2)下界），18节点25边2螺旋环路依赖图，采用七步骤工作流（ArangoDB + G'_topo + TopologyVerifier）。三组对照：A组（教材Markdown）vs B'组（依赖图JSON）vs B组（七步骤工作流）。8维15分制评分。验证H1-H5假设在数学领域是否成立 | **必读**。七步骤工作流在数学领域的首次验证 |
| `dev-docs/88-大师-POC-2验证结果.md` | **大师-POC-2结果**：B组显著优于A组（+4.9/15分制）和B'组（+3.5/15分制）。10分制边际增益：B vs A=+3.27，B vs B'=+2.34，B' vs A=+0.93。**核心发现**：B组唯一完成了稳定性方程5D=3√5(B_r-B_s)+2C_3的完整推导——这是A组和B'组都未能完成的关键突破。H1-H5全部验证通过。TopologyVerifier从星学到数学零修改复用，1次通过100%覆盖 | **必读**。七步骤工作流在数学领域成功验证 |
| `dev-docs/89-工作系统审计与升级方案-星学对比.md` | **工作系统审计**：审计星学项目已完成的工作系统升级（5层架构：运行时协议+Devin CLI集成+核心控制脚本+运行时工具+运行时状态），对比数学项目当前状态（几乎空白）。**结论**：有必要升级，但不是简单复制——数学项目有独特资产（七步骤工作流+ArangoDB+TopologyVerifier），应借鉴星学的运行时架构，同时在状态存储（ArangoDB替代JSON）、质量门控（集成TopologyVerifier）、自我迭代（从POC结果发现新意识节点）上超越星学。**第二次审计纠正**：真正的升级是 `xishujuzhen/cognition_*.py` 系列——把"稀疏矩阵/依赖图/拓扑验证/ArangoDB"基座安装到工作系统自身上，64个认知单元100条边，CP1-CP6工作流，三 hook 集成 | **必读**。工作系统升级的决策依据 |
| `dev-docs/90-经典计算展开依赖图的愿景分析.md` | **经典计算展开愿景**：用户提出"经典计算负责依赖图展开（G'_topo），AI 再根据展开结果转译"。分层可行性分析：L0骨架展开（拓扑排序+节点/边拷贝，**经典计算完全可行，保证全覆盖**）→ L1类型推断（启发式规则，可行）→ L2 section划分（经典计算推荐+AI细化）→ L3语义标注（AI不可替代）。建议实现L0+L1作为步骤2经典计算版本，L2作为推荐，L3保留给AI | **必读**。七步骤工作流步骤2的升级方向 |
| `dev-docs/91-工作系统升级方案-cognition基座安装.md` | **工作系统升级方案**：把cognition基座安装到数学项目。~30个认知单元（core/process/support+意识节点），ArangoDB新增5个collections，CP1-CP6工作流，**Hook v2方案（git post-commit + SessionStart，不用Stop hook——吸取星学v1废弃教训）**，三层维护机制，Devin CLI集成。超越星学三点：两套图共享ArangoDB、TopologyVerifier作为质量验证、经典计算展开G'_topo。含数学形式化（G_math定义）+规模指标+3档复用指南 | **必读**。工作系统升级的执行方案 |
| `dev-docs/92-经典计算展开依赖图方案-topo_generator.md` | **经典计算展开方案**：实现topo_generator.py，从ArangoDB中的G自动生成G'_topo骨架。L0骨架展开（Kahn拓扑排序+节点/边拷贝）→ L1类型推断（static/dynamic+connection类型）→ L2 section划分推荐。用POC-2依赖图测试，TopologyVerifier必然1次通过100%覆盖。步骤2从"meta AI生成"变为"经典计算生成骨架+AI语义细化" | **必读**。七步骤工作流步骤2的执行方案 |
| `dev-docs/93-差距分析-星学88-93号vs数学89-92号.md` | **差距分析**：对比星学88-93号（6篇完整技术说明书）和数学89-92号（4篇方案文档）。**星学有而数学缺失的6项**：设计哲学/POC验证体系/Hook演进记录（含subagent防护）/诚实评估/数学形式化/复用指南。**数学有而星学缺失的3项**：经典计算展开/两套图共享ArangoDB/意识节点双重身份。**最严重发现**：91号方案的Hook设计重蹈星学已废弃的v1覆辙（Stop hook影响subagent）——因为我只读了星学的stop_hook.py代码，没有读92号文档中v1废弃的教训 | **必读**。91号方案修正的依据 |
| `dev-docs/94-POC验证体系设计-工作系统有效性验证.md` | **POC验证体系**：验证工作系统有效性的POC设计。POC-R1-Math（D1-D6评分+H1-H8假设检验+回归验证）+ POC-3-Math（经典计算展开验证）+ POC-4-Math（两套图共享验证）。8条验证体系设计原则（7条从星学继承+1条数学独有：拓扑确定性原则）。3档复用指南（最小/标准/增强） | **必读**。工作系统有效性的验证方案 |
| `dev-docs/95-设计哲学-数学项目工作系统.md` | **设计哲学**：数学项目工作系统的10个设计决策（7个从星学继承+3个数学独有：经典计算展开G'_topo/两套图共享ArangoDB/意识节点双重身份）。用户两条直觉（稀疏矩阵与螺旋环路 + 经典计算展开依赖图）。适用范围 | **必读**。工作系统的"为什么" |
| `dev-docs/96-诚实评估与未来-数学项目工作系统.md` | **诚实评估**：8条已知局限（6条继承星学+2条数学独有：经典计算section划分质量不确定/两套图共享一致性风险）。HoTT诚实定位（数学项目比星学更接近HoTT但仍然不是HoTT）。未来方向（短期5+中期4+长期4）。给其他AI的建议（可复用/需调整/需警惕） | **必读**。工作系统的诚实面对 |
| `dev-docs/97-测试方案-工作系统与经典计算展开的完备验证.md` | **测试方案**：6层16个测试用例（T1-T15 + T11b），每个含测试目标/前置条件/测试步骤/预期结果/判定标准/失败排查。Layer 1基础设施(T1-T2)→Layer 2核心功能(T3-T6)→Layer 3 Hook与纪律(T7-T9含subagent防护)→Layer 4经典计算展开(T10-T11 + T11b与meta AI版对比)→Layer 5两套图共享(T12-T13)→Layer 6有效性验证(T14 A/B对照+T15回归验证)。含测试执行计划+通过标准+测试数据准备 | **必读**。实现后按此方案逐项测试 |
| `dev-docs/98-测试报告-工作系统与经典计算展开验证结果.md` | **测试报告**：T1-T15逐项结果。**14/16通过**（T11b未执行——topo_generator已覆盖meta AI版数据无法对比；T14 A/B对照待执行——需真实任务场景）。关键发现：max_depth从5调整为7（数学项目路径更长）/ git hook shebang必须用绝对路径 / 意识节点名称映射（英文cog_id↔中文node_id）/ **topo_generator 1次通过100%覆盖** / 回归验证能检测版本链问题 | **必读**。工作系统验证结果 |
| `dev-docs/99-工作系统经验反哺大师系统升级方案.md` | **反哺方案**：工作系统升级（89-98号）的6个机制反哺数学大师系统。反哺1：经典计算展开替代七步骤步骤2（topo_generator已实现，P0立即执行）/ 反哺2：CP1-CP3加载数学意识作为做证明的前置认知（系统化POC-1的发现）/ 反哺3：版本链管理数学意识演化（POC-1发现→POC-2深化→POC-3验证）/ 反哺4：回归验证保障依赖图变更后已有功能不被破坏 / 反哺5：从POC结果中自动发现新数学意识（半自动，长期）/ 反哺6：三层提取L1/L2/L3用版本链管理（v1=具体步骤→v2=思维模式→v3=范式思维）。含实现优先级（P0-P3）+ Check List + 与POC-3的关系 | **必读**。数学大师系统的下一代升级方向 |
| `dev-docs/100-反哺方案执行计划-细化CheckList与测试方案.md` | **执行计划**：99号反哺方案的执行级文档。6个反哺点的Check List全部细化+10个测试方案。**执行结果：10/10测试通过**。反哺1（R1-1/R1-2）：seven_step_pipeline.py集成topo_generator，1次通过100%覆盖 / 反哺2（R2-1/R2-2/R2-3）：种子推荐表5种问题类型+CP1-CP3覆盖率100% / 反哺3（R3-1/R3-2）：5个意识节点v1(POC-1)→v2(POC-2)版本链 / 反哺4（R4-1/R4-2）：POC-1回归94/100+POC-2回归100/100+敏感性验证通过 / 反哺6（R6-1）：Cayley-Hamilton三层版本链v1→v2→v3 | **必读**。反哺方案执行结果 |
| `dev-docs/101-UserPromptSubmit提醒机制方案.md` | **提醒机制方案**：模仿星学97号文档的v3方案（纯提醒无硬门禁），给数学项目加UserPromptSubmit hook。每次用户提问时从`UserPromptSubmit.txt`读取提醒注入AI上下文。数学项目独有内容：数学问题额外提醒查种子推荐表+七步骤工作流。**5/5 Check List通过** | 工作系统提醒机制 |
| `dev-docs/102-AGENTS.md技术说明内联方案.md` | **内联方案**：把工作系统和数学大师系统的操作级技术说明内联到AGENTS.md中，确保跨session/压缩后AI不丢失"怎么用"的认知。每节末尾加"依赖维护"标注——当依赖的dev-docs更新时同步更新AGENTS.md对应内容。**6/6 Check List通过** | AGENTS.md维护 |
| `dev-docs/103-AGENTS.md技术说明依赖入稀疏矩阵方案.md` | **依赖入图方案**：纠正102号的纯Markdown依赖表——依赖关系应该存储在稀疏矩阵中。新增2个认知单元（agents_tech_worksystem, agents_tech_mathmaster）+ 11条depends_on边 + SDK新增find_dependents_by_doc方法（反向查询：给定dev-docs编号返回依赖它的认知单元）。AGENTS.md中Markdown依赖表改为指向稀疏矩阵。**6/6 Check List通过** | AGENTS.md维护 |
| `dev-docs/104-CP4检查清单补全-对照星学98-99号方案.md` | **CP4补全方案**：对照星学98号（CP4动态查询技术说明书）和99号（CP4补全两个稀疏矩阵更新纪律），补全数学项目CP4检查清单。新增3个纪律认知单元（doc_sync_discipline, work_matrix_update, math_master_matrix_update）+ 加3条stop_hook依赖边 + 移除3条错误依赖边（arangodb_infra, work_system_upgrade, agents_management不是纪律）。修复后CP4检查清单5项纪律，与星学项目完全对称。AGENTS.md中"检查依赖"纪律改为指向稀疏矩阵中的work_matrix_update和math_master_matrix_update。 | **必读**。CP4检查清单纪律 |
| `dev-docs/105-大师-POC-3验证方案.md` | **POC-3方案**：三层提取跨题复用验证。题1(Cayley-Hamilton)提取L1/L2/L3→题2(谱定理,近迁移)+题3(Euler公式,远迁移)。三组对照(A=仅L1/B=L1+L2/C=L1+L2+L3)。8维15分制评分。成功标准：题3远迁移C vs B L3增量≥+1.5 | POC-3验证方案 |
| `dev-docs/106-大师-POC-3验证结果.md` | **POC-3结果**：**三层提取跨题复用价值验证成立**。题2(近迁移)：C>A +4.1, C>B(L3增量) +2.1。题3(远迁移)：C>A +3.9, **C>B(L3增量) +2.6≥+1.5成功**。L2审计4/4通过，L3审计1/2通过(L3-2应降级为L2——元思维不是具体范式)。H1-H4验证通过，H5部分通过。核心发现：L3在远迁移中增量大于近迁移(+2.6>+2.1)，L3范式思维跨领域迁移价值成立。C组在题3中给出组合+拓扑两条证明路径并建立结构同构 | **必读**。L3跨领域迁移验证成功 |
| `dev-docs/107-题库Phase-A建设方案.md` | **题库Phase A方案+执行结果**：从Proofs from THE BOOK + MathLib 100 Theorems +经典教材中手工结构化标杆题。**Phase A完成**：15道题42个解法已导入ArangoDB。3批：POC-3已有3道+MathLib 100定理7道+Proofs from THE BOOK 5道。依赖图452节点393边(含69条跨领域映射边)。认知图57个认知单元(新增21个意识节点)。领域覆盖：线性代数/拓扑/组合/数论/分析/代数几何/几何 | **必读**。题库Phase A完成 |
| `dev-docs/108-数学大师全知识体系准备方案.md` | **v2穷尽式方案（已被109号v3接替）**：v1→v2转变：从标杆题库选取改为穷尽式吸收。七大来源：竞赛题全集/数学家工作/菲尔兹奖/教材/MathLib 100/THE BOOK/Wikipedia。估计~110000节点。v2的吸收Loop架构、校验策略、存档结构仍有效，但知识范围以109号v3为准 | v2方案，被109号接替 |
| `dev-docs/109-数学大师全知识宇宙-穷尽式知识地图v3.md` | **v3全知识宇宙地图（当前最新）**：从"数学痴狂爱好者"视角发掘AI内在知识，从v2七大来源扩展到**十三大来源**：①数学家全集（Euler 80卷/Ramanujan笔记+Berndt 5卷+Andrews-Berndt 5卷+所有后续）②教材与专著~200本（含全部习题）③习题集与问题集（Pólya-Szegő/Lovász/Stanley/Demidovich/Arnold Trivium）④数学思想书（Hadamard/Poincaré/Arnold/Rota/Lakatos/Thurston/Grothendieck/Manin）⑤arXiv/ar5iv（32个数学分类）⑥竞赛题全集（含Schweitzer研究级）⑦百科与数据库（OEIS 37万序列/DLMF/nLab/MathWorld/Princeton Companion）⑧形式化数学库（MathLib 100000+定理/Coq/Mizar/Metamath）⑨数学杂志问题栏（AMM 1894-/Crux/Kvant）⑩讲义与综述（Bourbaki Seminar/ICM Proceedings）⑪趣味数学（Gardner 25年专栏/Conway全部）⑫开放问题清单（千禧年/Erdős/Smale/Hilbert/Arnold）⑬历史与哲学（Kline通史/Stillwell/Neugebauer/Heath）。估计~60万条目，~325000节点。含Ramanujan专题（笔记+注解+后续链条）、知识存档结构v3、修订后分批计划 | **必读**。当前最新知识地图 |
| `dev-docs/110-大规模依赖图可操作性方案-三层访问架构.md` | **325000节点可操作性方案**：解决"325000节点 vs 20万token上下文"的核心架构问题。**三层访问架构**：①冷存储层（ArangoDB全部325000节点，永不全部装入上下文）②热工作集（当前问题相关200-800节点子图，~80K token装入上下文）③温查询层（AI推理中按需expand/query，每次返回10-50节点追加到热工作集）。**种子选择三級机制**：层次索引定位（3层主题树~20K token常驻）→语义检索（embedding top-20种子）→图遍历扩展（token预算控制剪枝到200-800节点）。**多分辨率节点存储**：R1全细节~300token/~5000节点、R2中细节~100token/~20000节点、R3轻量~30token/~200000节点、R4极简~10token/~100000节点。**渐进式展开协议**：AI可发起expand/dependencies/path/loop/search查询。**粒度拆分**：子图仍太大时拆分为小图分别分析再综合。Token预算分析：80K给依赖图子图可装270-800个全/中细节节点，远超POC所需（POC-2用18节点即显著增益）。分阶段启用：<5000节点全遍历、5000-50000层次索引+遍历、50000+完整三层架构 | **必读**。大规模可操作性架构 |
| `dev-docs/111-知识搜集优先级方案-最难最妙最新.md` | **搜集优先级方案**：核心洞察（来自用户）——数学大师系统的价值不在于装AI已经会的东西，而在于装AI不会的。越是难、妙、新，越是AI本身可能不会的，越应该优先装入。**三级优先级**：P0=AI最不可能会的（Ramanujan冷僻恒等式/最新arXiv/Schweitzer研究级竞赛/Erdős冷僻问题/Arnold Trivium/数学思想书/Conway深度工作/开放问题详细进展）；P1=AI浅层知道但深度不够的（MathLib形式化定理/THE BOOK/OEIS/关键数学家工作/Bourbaki Seminar/IMO Shortlist）；P2=AI基本会的（标准教材/Wikipedia/基础竞赛题）；P3=AI完全会的（只做索引）。"难妙新"三准则：满足越多优先级越高 | **必读**。搜集优先级逻辑 |
| `knowledge/` | **P0知识搜集成果（截至2026-08-04）**：①P0经典知识：38文件10810行680KB（Ramanujan/Arnold/思想书/竞赛题/突破/Conway/开放问题）②**arXiv全文**：1305篇972008行114MB（145个分类的HTML全文，math.* 325篇/cs.* 302篇/physics.* 182篇/quant-ph 7篇/math-ph 8篇/hep-th 9篇/stat.* 45篇/nlin.* 45篇等）③**arXiv穷尽式元数据**：**239472篇**唯一论文，323.8MB JSON，覆盖44个分类（math.* 28个+cs理论7个+quant-ph+math-ph+hep-th+stat.ML+nlin 4个），2023-2026年，按submittedDate日期范围查询穷尽获取，大分类达10000 API上限。年份分布：2023=48983/2024=69810/2025=62131/2026=58548 | **必读**。P0知识存档 |
| `scripts/arxiv_search.py` | arXiv API搜索脚本v1：28个数学分类各50篇 | 工具脚本（已被v3接替） |
| `scripts/arxiv_fetch_html.py` | arXiv HTML全文抓取脚本v1：从arxiv.org/html/<id>抓取HTML转为markdown，27个数学分类各3篇 | 工具脚本（已被v2接替） |
| `scripts/arxiv_search_v3.py` | **arXiv API穷尽式搜索脚本v3**：44个分类（math+cs理论+quant-ph+math-ph+hep-th+stat.ML+nlin），submittedDate日期范围查询（2025-2026 + 2023-2024），200条/页，3秒间隔，429重试退避。239472篇元数据 | **当前版本** |
| `scripts/arxiv_fetch_html_v2.py` | **arXiv HTML全文抓取脚本v2**：从239K篇元数据中按"难妙新"原则筛选1452篇，145个分类各10篇最新论文HTML全文。1305篇成功（含v1的69篇），972008行114MB | **当前版本** |
| `dev-docs/112-arXiv论文导入ArangoDB与节点映射规则方案.md` | **arXiv论文操作化方案**：239K篇元数据导入ArangoDB `arxiv_papers` collection。四级映射规则：L1定理级（论文中的定理→dg_nodes concept节点）/ L2方法级 / L3意识级 / L4索引级（默认，可搜索不在依赖图中）。论文不是节点，论文是节点的出处。SDK新增`search_arxiv()`/`promote_arxiv_paper()`。实现110号三层架构的冷存储层 | **必读**。arXiv知识操作化 |
| `dev-docs/113-大师-POC-4验证方案-代数拓扑领域泛化性验证.md` | **POC-4方案**：代数拓扑领域（Klein瓶同调群计算）验证方法论泛化性。12节点+15边+新增structural_thinking意识节点。A/B对照实验。与矩条件极差题的思维差异最大（结构性vs分析性） | POC-4方案 |
| `dev-docs/114-大师-POC-4验证结果.md` | **POC-4结果**：A组15/15，B组15/15，边际增益=0。**问题选择不当**——Klein瓶同调群是标准教材内容，AI已完全掌握。陷阱在AI"会"区 | POC-4结果 |
| `dev-docs/115-大师-POC-5验证方案-数论最新论文泛化性验证.md` | **POC-5方案**：从arXiv:2608.02381（2026-08-03最新论文）提取orientation-rigidity定理。10节点+12边+3意识节点+螺旋环路 | POC-5方案 |
| `dev-docs/116-POC隔离测试方案-独立目录+tmux监督.md` | **隔离测试方案**：独立目录(`/data/math-agent-{1,2}/`) + AGENTS.md软限制(禁止web_search/禁止访问master-mind) + tmux监督(master agent观察pane)。审计必须覆盖完整运行过程和最终结果，不能只检查result.md。 | **必读**。POC测试标准流程 |
| `dev-docs/117-大师-POC-5验证结果-隔离测试.md` | **POC-5结果**：隔离测试方案验证有效（无违规）。A组15/15，B组15/15，增量=0。但B组使用了反证法+螺旋交叉验证+对偶性观察——依赖图影响证明结构。**三次POC对比洞察**：POC-1增量+3.50(AI"不会"区)，POC-4/5增量0(AI"会"区)。直接验证111号"难妙新"原则 | **必读**。三次POC对比 |
| `dev-docs/118-大师-POC-6验证方案-Ramsey数发现型问题.md` | **POC-6原始方案**：发现型问题——从arXiv:2608.02537让AI猜测R_k(C_5)下界。原版依赖图后来发现有节点直接或等价写出答案，不能原样复用 | POC-6历史方案；纠偏见120-121号 |
| `dev-docs/119-大师-POC-6验证结果-Ramsey数发现型问题.md` | **POC-6原始结果，已降级为低可信历史证据**：A组猜k^{k/5}，B组猜(log k)^{k/3}，但B组依赖图存在答案泄漏，原`+4.0/10`不能支持“泛化性最终验证成立” | 不得作为最终结论；当前状态见120-121号 |
| `dev-docs/120-工作交接文档-POC6修正版重跑与下一步.md` | **POC-6修正版交接状态**：原始实验答案泄漏；修正版A组猜k^{k/6}，B组运行中断、尚无结果；记录隔离目录和恢复任务 | **必读**。当前实验事实记录 |
| `dev-docs/121-v1-2026-08-05-POC6修正版重跑纠偏与证据闭环方案.md` | **POC-6修正版正式纠偏方案**：明确测量口径，修复环声明与边集合不一致，冻结输入，保存完整运行证据，先恢复B组再做至少3对A/B配对复跑，以四档判定收口 | **必读**。后续执行的事实与流程依据 |
| `dev-docs/122-v1-2026-08-05-数学大师系统总体架构调查.md` | **数学大师系统总体架构v1调查**：把现有知识资产、数学依赖图、研究运行、工具验证、POC和工作认知图统一为三平面、八组件、三闭环；实测发现当前主链未闭合、图模式分裂、KC稀疏、全图拓扑验证失败、大规模召回和工具验证未接入 | 架构调查初版，已被v2深化 |
| `dev-docs/122-v2-2026-08-05-思维形状与启发关系架构修订.md` | **三图架构修订**：确立“思维形状可观测、可比较、可干预”；分离数学知识图K、外显思维图T、启发激活图H；定义动态题目Q_t、Agent M救援闭环和因果干预POC | 当前架构模型，证据裁决见v3 |
| `dev-docs/122-v3-2026-08-05-完整机制复核与费马极限案例.md` | **证据复核基线**：完整通读80—99号后回答五问；裁决现有静态提示、七步骤、经典展开和工作认知图各自真正证明了什么；解释Master答案泄漏的系统根因；以Frey—Ribet—Wiles链区分“调用已证模性推FLT”“重建Wiles证明”“独立发现路线” | **必读**。123号的证据前提 |
| `dev-docs/123-v1-2026-08-05-数学大师系统全景复盘与第一性原理重构计划.md` | **当前最高架构与建设基线**：以`系统探讨.md`全文为母本，保留七层能力、五类资产和K/T/H直觉；用类型化任务/工作区、事件溯源、表示变换、时序规则、证据状态和受约束最小干预严格化；建立DYN-0—7、Phase 0—7、角色权限、数据crosswalk、停止条件及Ramsey/费马案例 | **最高优先级必读**。后续schema、POC和运行时必须服从 |
| `dev-docs/124-v1-2026-08-05-Phase0-7建设计划CheckList.md` | **Phase 0—7可执行Check List**：把123号Phase 0—7、DYN-0—7、停止条件、不做清单和下一实施包全部细化为可追踪的Check List条目。每个Phase有入口门、细化的子项Check List、出口门、停止条件和失败回滚。含全局预注册门（G0-1—G0-6）、核心指标清单（G0-M1—M10）、风险登记（R-1—R-16）、贯穿案例（Ramsey CC-R-0—6 + 费马 CC-F-0/7）、角色隔离矩阵（P0-5.1—5.13）、降级路径（DEG-1—6）、进度追踪表和5个未决问题。v1修正：修正P0-7.1的DYN编号错误（DYN-4→DYN-5）、修正P4-EXIT-4的逻辑错误（冻结标准≠达到标准） | **必读**。Phase推进的执行视图，按Phase顺序逐项打勾 |
| `dev-docs/125-v1-2026-08-05-AGENTS对齐审计与Git-Hook防不同步机制.md` | **AGENTS.md对齐审计+防御机制**：审计发现7类不同步问题（DYN阶梯定义错误/Phase编号偏移/文档索引遗漏/代码文件未引用/文件名引用错误等），全部修正后新增`alignment_check.py`（6项对齐检查）+`pre-commit` hook（硬性违规阻止commit）+`post-commit` hook增强（commit后对齐提醒）。机制首次运行即自动检测到人工审计遗漏的64号文件名错误 | **必读**。理解AGENTS.md与repo对齐的防护机制 |
| `dev-docs/126-v1-2026-08-05-dg星图只读盘点报告.md` | **dg_*只读盘点报告**：Phase 0 (P0-3)冻结`dg_nodes`(1719)/`dg_edges`(1483)/`loops`(4)的type/edge_type/mapping_type/graph分布、五类初步归类、schema字段清单。重要发现：96.5%边edge_type为unknown，真实边语义在mapping_type字段；当前dg_*完全是K视图，无T/H/E节点 | **必读**。Phase 0架构冻结的数据基线 |
| `dev-docs/127-v1-2026-08-05-Schema冻结与角色隔离矩阵.md` | **Schema冻结与角色隔离矩阵**：Phase 0核心交付物。冻结8类schema（Task/Workspace/Event/Obligation/Representation/Evidence/HeuristicRule/Visibility）、8角色可见性矩阵（8×14 collection）、逐组件最小输入/输出契约、CapabilityToken强制机制、candidate/validated/published/retired生命周期状态机。123号10条架构裁决在schema中的逐项体现 | **最高优先级必读**。Phase 1起按此schema创建新collection |
| `dev-docs/128-v1-2026-08-05-全局预注册项与贯穿案例冻结.md` | **全局预注册项与贯穿案例冻结**：Phase 0全局项落盘。G0-1关键事件完整清单（5类20+种事件类型）、R-1—R-16风险监控机制（每项含监控机制/检查点/触发停止条件）、CC-R-0 Ramsey案例冻结（非泄漏干预阶梯+验证维度）、CC-F-0费马案例冻结（三层难度阶梯+推论链+大师启发维度） | **必读**。每个Phase出口门对照检查 |
| `xishujuzhen/arxiv_to_arangodb.py` | arXiv元数据→ArangoDB导入脚本：读取JSON批量导入239K篇+创建4个索引+验证 | 工具脚本 |
| `xishujuzhen/arangodb_init.py` | ArangoDB数据库初始化：创建xishujuzhen_math数据库+12 collections+3 graphs+8索引 | 基础设施脚本 |
| `xishujuzhen/topology_verifier.py` | 拓扑覆盖验证器：检查G'→G的节点/边/环路集合保真。**123号裁决：结构保真验证，不代表语义或数学正确** | legacy验证器 |
| `xishujuzhen/test_dependency_graph.py` | 依赖图回归测试。**123号裁决：legacy图回归，不作为动态研究系统验收** | legacy测试 |
| `xishujuzhen/import_math_graph_to_arangodb.py` | 数学依赖图→ArangoDB导入脚本 | 数据导入脚本 |
| `xishujuzhen/batch_extractor.py` | 批量提取器脚本 | 工具脚本 |
| `xishujuzhen/absorb_test_loop.py` | 吸收测试循环脚本 | 工具脚本 |
| `xishujuzhen/poc4_build_graph.py` | POC-4（Klein瓶同调群）依赖图构建脚本 | POC工具脚本 |
| `xishujuzhen/poc9_export_graph.py` | POC-9图导出脚本 | POC工具脚本 |
| `xishujuzhen/poc9_import_topo.py` | POC-9拓扑图导入脚本 | POC工具脚本 |
| `xishujuzhen/poc9_import_unfold_full.py` | POC-9完整展开图导入脚本 | POC工具脚本 |
| `xishujuzhen/poc9_prepare_translate_input.py` | POC-9转译输入准备脚本 | POC工具脚本 |

### 星学知识系统结构参考

| 文档 | 内容 | 对数学项目的参考价值 |
|---|---|---|
| `AGENTS-星学版.md` | **星学项目完整 AGENTS.md**：1056行，包含项目定位、四类载体分工、8个工作流入口、吸收范式、形式化思维规则、解释框架、维度/成熟度/可计算性 | **必读**。数学项目的 AGENTS.md 结构直接参考它 |
| `星学项目: dev-docs/56-新系统老系统吸收范式.md` | 新系统/老系统吸收范式第一版。**文件在星学项目目录**`~/MOIRA_chinese_astrology-main/dev-docs/`，不在数学项目dev-docs/中 | 知识系统建设范式参考 |
| `星学项目: dev-docs/57-新系统方案迭代与老方案更新.md` | 对吸收范式的8问审视。**文件在星学项目目录** | 知识系统迭代方法参考 |
| `星学项目: dev-docs/58-新系统迭代执行CheckList.md` | 可执行 CheckList 设计。**文件在星学项目目录** | Check List 设计参考 |
| `星学项目: dev-docs/59-AGENTS重构纠偏与高价值规则回收.md` | AGENTS 重构时的保全纪律。**文件在星学项目目录** | 本 AGENTS.md 重写时已遵循 |
| `星学项目: dev-docs/60-外部系统收敛与暂存规划.md` | 外部系统收敛决策。**文件在星学项目目录** | 知识边界管理参考 |
| `星学项目: dev-docs/13-七政四余形式化体系.md` | 形式化体系：算子+集合+命题。**文件在星学项目目录** | 数学形式化的直接参考 |

### 星学 POC 验证方案完整列表

| POC | 文档 | 验证内容 |
|---|---|---|
| POC-1 | `dev-docs/64-xishujuzhen-POC验证方案.md` | 对照实验设计、5节点7边依赖图、5维度结构化评分 |
| POC-2 | `dev-docs/65-xishujuzhen-POC2验证方案.md` | 12节点16边扩展图、知识内容嵌入提示、配对审计 |
| POC-3 | `dev-docs/66-xishujuzhen-POC3验证方案.md` | AI自解读环节、双重提示、双重对照审计 |
| POC-4 | `dev-docs/68-xishujuzhen-POC4验证方案.md` | 双宫联动、19节点25边、跨宫依赖、空宫设计 |
| POC-5 | `dev-docs/70-xishujuzhen-POC5验证方案.md` | 静态+动态分析、30节点40边8跨宫依赖、静态螺旋环路 |
| POC-6 | `dev-docs/72-xishujuzhen-POC6验证方案.md` | A组知识缺失+交叉审计、独立AI实例审计 |
| POC-7 | `dev-docs/74-xishujuzhen-POC7验证方案.md` | 12限全量、71节点106边、动态螺旋三圈修正 |
| POC-8 | `dev-docs/77-xishujuzhen-POC8验证方案.md` | 闭环审计标准流程化、开环组vs闭环组对照 |

### 星学实验执行模式参考

| 文档 | 内容 |
|---|---|
| `dev-docs/67-Subagent对照实验执行模式.md` | 双subagent并行对照、分阶段subagent、盲评、background模式、输出保存到文件 |

## 工作原则

### 从星学项目继承的工作原则

- **新系统本体纪律**：本项目中的"新系统"专指为数学研究建设的知识系统与导航系统。不得把星学代码、星学知识文件或星学运行时称为新系统。
- **有机积累纪律**：新认知应融入已有概念、步骤、专题和来源网络；不能总在文件末尾追加孤立段落，也不能重复制造平行定义。
- **结构可修订纪律**：现有知识系统结构只是当前状态。材料暴露结构问题时，先修正结构，再安放内容。
- **不确定性保留纪律**：不同证明路径、不同数学流派的差异必须保留。没有充分证据时使用"候选、待考、类比"，不能强行统一。
- **AGENTS 高价值内容保全纪律**：重构 AGENTS.md 时，不得把原有高价值规则、操作门槛、索引直接删除。确需移出时，必须已有明确承接文件、保留强约束摘要、保留索引、说明迁出原因。（本文件已遵循：旧 AGENTS.md 保留为 `AGENTS-星学版.md`，星学参考索引完整保留。）
- **细节推出纪律**：从 AGENTS.md 推出到 dev-docs/ 的内容，不能被视为废弃内容。未来 Session 必须能通过 AGENTS 的索引找回。

### 数学项目特有工作原则

- **渐进积累、迭代测试**：创造数学大师系统不是一蹴而就，而是渐进的。我们不是一把装入所有知识然后测试，而是一边装入一边充分测试——每装入一批知识/依赖边/意识节点，就立即用POC验证其价值，验证通过再继续装入。不积跬步无以至千里，全部装入完成之时，大师已成。这个理念贯穿题库建设（Phase A/B/C/D每批都验证）、依赖图构建（每扩展一批节点就跑回归验证）、三层提取（每提取一批L2/L3就验证跨题复用增益）。
- **穷尽式知识吸收（v3：十三大来源）**：全能数学大师应该知道**一切**可得的数学知识。v2的七大来源（竞赛题/数学家工作/菲尔兹奖/教材/MathLib 100/THE BOOK/Wikipedia）仍然是"课程设计师"思维。v3从"数学痴狂爱好者"视角发掘了**十三大来源**：①数学家全集（Euler 80卷/Gauss 12卷/Ramanujan笔记+Berndt 5卷注解+Andrews-Berndt 5卷注解+所有后续证明）②教材与专著（~200本，含全部习题）③习题集与问题集（Pólya-Szegő/Lovász/Stanley/Demidovich等独立习题集）④数学思想书（Hadamard发明心理学/Poincaré科学与方法/Arnold散文/Rota/Lakatos证明与反驳/Thurston论证明与进步/Grothendieck收获与播种/Manin Mathematics as Metaphor）⑤arXiv/ar5iv（32个数学分类，每日更新）⑥竞赛题全集（含Schweitzer研究级竞赛）⑦百科与数据库（OEIS 37万序列/DLMF/nLab/MathWorld/Princeton Companion）⑧形式化数学库（MathLib 100000+定理/Coq/Mizar/Metamath/Isabelle AFP）⑨数学杂志问题栏（AMM 1894-/Crux/Kvant）⑩讲义与综述（Bourbaki Seminar/ICM Proceedings/各大学公开讲义）⑪趣味数学（Gardner 25年专栏/Conway全部）⑫开放问题清单（千禧年/Erdős/Smale/Hilbert/Arnold）⑬历史与哲学（Kline通史/Stillwell/Neugebauer古代数学/Heath希腊数学）。估计~60万条目，~325000节点。详见109号方案。**AI可以自己生成知识内容**——通过维基百科+AI内在知识还原，用SymPy/SageMath/Lean4校验正确性。知识素材原文应在knowledge/目录中按十三大来源分类存档。
- **数学计算交给工具，数学知识由知识系统承载，数学判断由 AI 执行，三者不混用。**
- AI 需要数值/符号计算时，调用数学计算工具，不靠心算。
- AI 需要数学判断时，以知识系统为规范知识载体；计算工具只提供计算原料，不能代替数学判断。
- AI 在对话中发现的新数学认知，不能只留在上下文中；经审查后，应有机融入知识系统的正确位置。
- **依赖图构建需要数学功力**：判断"代数拓扑依赖范畴论"是一条边、"数论依赖调和分析"是不是一条边——这个判断需要数学水平。依赖图的构建阶段需要"综述博士"参与。
- **方法论迁移不是照搬**：星学的依赖图结构（命宫/官禄/大限/流年）不适用于数学。数学的依赖图需要重新设计——可能是按数学领域（代数/几何/分析/拓扑/数论...）、按数学工具（范畴论/同调/表示论...）、按问题类型（分类/计算/存在性/构造...）组织。

## 工作系统技术说明

> 本节是工作系统（AI自己的工作认知管理）的操作级技术说明。跨session/压缩后AI通过本节恢复"怎么用工作系统"的认知。完整方案见依赖文档。

### CP1-CP6工作流

工作系统的核心是CP1-CP6六个检查点，通过`cognition_checkpoint_math.py`执行：

| CP | 时机 | 内容 | 命令 |
|---|---|---|---|
| CP1 | 工作开始前 | 种子选择：确定本次任务需要哪些种子认知单元 | `cognition_checkpoint_math.py start --seeds <cog_id1>,<cog_id2>` |
| CP2 | 工作开始前 | 认知加载：AQL图遍历，从种子出发沿depends_on边找到所有前置认知 | CP1命令自动执行 |
| CP3 | 工作开始前 | 缺口检查：验证已加载的认知是否覆盖任务所需 | CP1命令自动执行 |
| CP4 | 工作结束时 | 认知捕获：检查本次工作是否产生新方法论/新依赖/新版本/新术语/临场脚本 | git post-commit hook自动打印 |
| CP5 | 工作结束时 | 认知图更新：新版本/新边写入ArangoDB | `cognition_sdk_math.py`的add_version/add_edge |
| CP6 | 工作结束时 | 任务-认知映射：记录"这个任务用了哪些种子" | `cognition_sdk_math.py`的record_task |

**关键参数**：max_depth=7（数学项目路径比星学长，星学用5）

### 种子推荐表

`xishujuzhen/seed_recommendation_table.json`——数学问题类型→推荐意识种子映射：

| 问题类型 | 推荐种子 |
|---|---|
| 极值/上下界问题 | numerical_check, extreme_testing, invariant_thinking, approximation_thinking |
| 证明构造问题 | invariant_thinking, local_global_thinking, seven_step_workflow |
| 跨领域问题 | local_global_thinking, invariant_thinking, spiral_cognition, three_layer_extraction |
| 逼近/误差分析 | approximation_thinking, numerical_check, extreme_testing |
| 一般证明问题 | seven_step_workflow, math_awareness_nodes |

**用法**：AI接到数学问题后，先查此表确定种子，再执行CP1-CP3。

### 认知图查询与审计

```bash
# 查统计
.venv/bin/python3 -c "from cognition_sdk_math import CognitionSDK; sdk=CognitionSDK(); print(sdk.get_stats())"

# 图遍历（从种子出发）
.venv/bin/python3 -c "from cognition_sdk_math import CognitionSDK; sdk=CognitionSDK(); print(sdk.traverse(['seven_step_workflow'], max_depth=7))"

# 全量审计
.venv/bin/python3 xishujuzhen/cognition_audit_math.py all

# POC回归验证
.venv/bin/python3 xishujuzhen/cognition_audit_math.py poc-regression --seeds <seeds> --ground-truth <cog_ids>
```

### 回归验证

每次认知图变更（新增/修改/删除认知单元或依赖边）后，运行回归验证：
- D1覆盖率：图遍历是否覆盖ground truth
- D3版本链：current_version是否指向latest
- D4图遍历完整性：depth=7 vs depth=9是否一致
- 满分100，低于95需排查

### Hook机制

三个hook的分工（均为纯提醒，无硬门禁）：

| hook | 触发时机 | 脚本 | 作用 |
|---|---|---|---|
| SessionStart | 新session/压缩后 | `session_start_hook_math.py` | 注入认知图统计+工作纪律 |
| UserPromptSubmit | 每次用户提问 | `user_prompt_submit_hook_math.py` | 从`UserPromptSubmit.txt`读取提醒注入 |
| git post-commit | 每次commit后 | `githooks/post-commit` | 打印CP4检查清单（从稀疏矩阵动态查询） |

**改提醒内容**：直接编辑`xishujuzhen/UserPromptSubmit.txt`，不用改代码，下次提问立即生效。

**不要用Stop hook**：Stop hook会影响subagent（星学项目实测证实）。

### 依赖维护

本节的依赖关系存储在认知图稀疏矩阵中（认知单元 `agents_tech_worksystem`）：
- source_docs: [91, 94, 97, 100, 101]
- depends_on: sdk_maintenance, work_system_upgrade, math_awareness_nodes, stop_hook

**查依赖**：`cognition_sdk_math.py traverse(['agents_tech_worksystem'])`
**反向查询**（当某个dev-docs更新时，查哪些技术说明节需要同步）：
```bash
.venv/bin/python3 -c "import sys; sys.path.insert(0,'xishujuzhen'); from cognition_sdk_math import CognitionSDK; [print(u['cog_id'],u['title']) for u in CognitionSDK().find_dependents_by_doc(91)]"
```

## 数学大师系统技术说明

> 本节是数学大师系统（目标系统——数学证明的依赖结构管理）的操作级技术说明。跨session/压缩后AI通过本节恢复"怎么用数学大师系统"的认知。完整方案见依赖文档。

### 七步骤工作流 [legacy-static]

> **[legacy-static]** 123号v1已将七步骤正式降为legacy静态重建器。保留静态知识图与提示展开价值，不再承担主运行时。主运行时改为12步事件溯源循环（观测→状态归约→候选规则匹配→受约束干预→验证→归因→回写）。旧七步骤的100%拓扑覆盖只证明结构保真，不证明语义或数学真值，也不证明动态思维矫正。

数学大师系统的核心是七步骤工作流，通过`seven_step_pipeline.py`执行：

| 步骤 | 执行者 | 内容 | 命令 |
|---|---|---|---|
| 1 | 代码 | 依赖图G导入ArangoDB | `seven_step_pipeline.py --steps 1` |
| 2 | **经典计算** | **topo_generator.py生成G'_topo骨架（L0+L1+L2）** + AI语义细化（L3） | `seven_step_pipeline.py --steps 2` |
| 3 | 代码 | TopologyVerifier拓扑覆盖验证（1次通过100%覆盖） | `seven_step_pipeline.py --steps 3` |
| 4 | normal AI | 按G'_topo转译为大师提示词 | `seven_step_pipeline.py --steps 4` |
| 5 | meta AI | KC忠实审计（转译是否忠实于知识内容） | `seven_step_pipeline.py --steps 5` |
| 6 | normal AI | 在大师提示词引导下做数学证明 | `seven_step_pipeline.py --steps 6` |
| 7 | meta AI | 分析覆盖审计（分析是否覆盖G'_topo所有节点和边） | `seven_step_pipeline.py --steps 7` |

**一键执行步骤1-3**（经典计算部分）：
```bash
.venv/bin/python3 xishujuzhen/seven_step_pipeline.py --steps 1,2,3
```

**步骤2的升级**（反哺1）：从"meta AI生成G'_topo"升级为"经典计算生成骨架+AI语义细化"。经典计算保证全覆盖，AI只做L3语义标注（section命名、spiral类型确认）。

### 依赖图导入ArangoDB

依赖图G存储在ArangoDB的`xishujuzhen_math`数据库中：
- `dg_nodes`：节点集（1719个，7种type：concept/domain_concept/paradigm/problem/substep/意识/step）——详见126号只读盘点报告
- `dg_edges`：边集（1483个，edge_type以unknown为主但mapping_type有40+种映射类型）——详见126号只读盘点报告
- `loops`：螺旋环路（4个，含圈数）
- `arxiv_papers`：**arXiv论文库**（239472篇元数据，2023-2026年，44个分类）。支持按分类/日期/作者/关键词查询。每篇论文有mapping_level（L1定理级/L2方法级/L3意识级/L4索引级）和linked_nodes（关联的dg_nodes）。详见112号方案。

### arXiv论文查询

```bash
# 按分类查询
.venv/bin/python3 -c "import sys; sys.path.insert(0,'xishujuzhen'); from cognition_sdk_math import CognitionSDK; [print(p['arxiv_id'],p['title'][:50]) for p in CognitionSDK().search_arxiv(category='math.AG', limit=5)]"

# 关键词搜索
.venv/bin/python3 -c "import sys; sys.path.insert(0,'xishujuzhen'); from cognition_sdk_math import CognitionSDK; [print(p['arxiv_id'],p['title'][:50]) for p in CognitionSDK().search_arxiv(keyword='Ramanujan', limit=5)]"

# 有全文的论文
.venv/bin/python3 -c "import sys; sys.path.insert(0,'xishujuzhen'); from cognition_sdk_math import CognitionSDK; [print(p['arxiv_id'],p['title'][:50]) for p in CognitionSDK().search_arxiv(has_fulltext=True, limit=5)]"

# 提升论文映射级别（L4→L1/L2/L3）
.venv/bin/python3 -c "import sys; sys.path.insert(0,'xishujuzhen'); from cognition_sdk_math import CognitionSDK; print(CognitionSDK().promote_arxiv_paper('2607.27504','L1','Ramanujan_airy_asymptotics'))"
```

### G'_topo生成（经典计算展开）

`topo_generator.py`从G自动生成G'_topo骨架：
- L0骨架展开：节点集+边集直接拷贝（拓扑同构保证全覆盖）+ Kahn拓扑排序确定traversal_order
- L1类型推断：static/dynamic + connection类型（linear/shortcut/cross_section）
- L2 section划分：按依赖链长度分段+意识节点处理
- L3语义标注（AI）：section命名、spiral_static/dynamic最终确认

### TopologyVerifier拓扑覆盖验证（结构保真验证）

> **[结构保真验证]** TopologyVerifier验证的是输出骨架不遗漏输入图节点/边（结构保真），不代表语义或数学正确。100%拓扑覆盖只证明结构完整性，不证明语义真值、数学正确性或动态思维矫正效果。

`topology_verifier.py`验证G'_topo是否覆盖G：
- 节点覆盖：ut_nodes vs dg_nodes的集合差集
- 边覆盖：ut_edges vs dg_edges的集合差集
- 螺旋环路：圈数是否保持
- 结果：passed=True + 100%覆盖 = 结构保真通过（不代表语义或数学正确）

### 三层提取（L1/L2/L3）

83号文档设计的三层提取，L1/L2/L3是提取层次（解题思路→数学思维→范式思维），不是版本号。版本链用v1/v2/v3等独立编号，与L1/L2/L3无映射关系。

| 层次 | 内容 | 复用范围 |
|---|---|---|
| L1解题思路 | 具体步骤序列 | 类似题 |
| L2数学思维 | 从L1抽象出的思维模式（AI二次分析） | 跨题、跨领域 |
| L3范式思维 | 从多个L2综合出的范式（AI三次分析） | 改变图结构 |

**版本链操作**（版本号独立于L1/L2/L3层次）：
```bash
# 添加新版本
.venv/bin/python3 -c "from cognition_sdk_math import CognitionSDK; sdk=CognitionSDK(); sdk.add_version('<cog_id>', 'v2', '<doc>', '<summary>', version_order=2); sdk.update_current_version('<cog_id>', 'v2')"
```

**current_version反映文档版本**，与L1/L2/L3提取层次无映射关系。

### 数学意识节点（5个）

| 意识节点 | cog_id | 说明 |
|---|---|---|
| 不变量思维 | invariant_thinking | 识别什么是不变量，在扰动下保持 |
| 局部-全局思维 | local_global_thinking | 局部性质推出全局性质 |
| 逼近论思维 | approximation_thinking | 分析逼近精度和误差阶 |
| 极端检验 | extreme_testing | 在极端构型下验证命题 |
| 数值检验意识 | numerical_check | 用数值例子检验命题自洽性 |

**双重身份**：每个意识节点同时在cognition_units（工作认知）和dg_nodes（数学依赖图）中有记录。

**版本链状态**：5个意识节点都有v1(POC-1发现)→v2(POC-2深化)版本链，current_version=v2。

### 依赖维护

本节的依赖关系存储在认知图稀疏矩阵中（认知单元 `agents_tech_mathmaster`）：
- source_docs: [83, 85, 86, 88, 90, 92, 99, 100]
- depends_on: seven_step_workflow, classic_expansion, topology_verifier, topology_coverage, three_layer_extraction, math_awareness_nodes, spiral_cognition

**查依赖**：`cognition_sdk_math.py traverse(['agents_tech_mathmaster'])`
**反向查询**（当某个dev-docs更新时，查哪些技术说明节需要同步）：
```bash
.venv/bin/python3 -c "import sys; sys.path.insert(0,'xishujuzhen'); from cognition_sdk_math import CognitionSDK; [print(u['cog_id'],u['title']) for u in CognitionSDK().find_dependents_by_doc(88)]"
```

## 形式化思维规则（从星学继承，适配数学）

**核心命题**：数学本身就是一个形式系统——它有集合、算子、命题、推理规则。知识系统是数学知识在项目中的规范载体：它既保存自然语言语义、证明思路、适用条件，也显式表达集合、算子、命题和关系。

**形式化的工作方式**：

- **每条定理/引理必须可定位**：用精确的引用定位到具体文献、章节、页码，不接受"大概在某本书里"。
- **每个数学构造必须有形式定义**：群、环、域、流形、层、范畴等，必须定义输入类型、输出类型、语义。不接受"就是那种感觉"这种解释。
- **命题必须可求值**：给定一个数学实例，每条命题必须能判定为真/假/不确定。不可求值的命题是未完成的形式化。
- **知识库必须可审计**：新增数学知识必须检查与已有知识的一致性（是否矛盾？是否重复？是否归并？）。
- **形式化是一个开放过程**：不预设"形式系统长什么样"，而是让数学实践告诉我们它长什么样。

**AI 执行此规则的方式**：

当处理任何数学命题时，AI 必须问自己：
1. 这个命题的**数学对象**是什么？（群/流形/层/...）
2. 这个命题的**前提**是什么？
3. 这个命题的**结论**是什么？
4. 这个命题是否**可验证**？（给定实例能否判定真假）
5. 这个命题与已有知识库是否**一致**？

## TODO

> 本节记录跨 Session 需要保持的待办事项。

- [ ] 制定数学大师制造项目的建设计划（Phase 划分 + Check List）——80号提供启动认知，122号v1/v2/v3建立总体架构与证据复核，**123号v1已给出Phase 0—7建设计划基线**；后续按123号DYN阶梯和Phase入口门推进，不再单独冻结Phase计划
- [x] **数学大师系统总体架构v1调查**：确认三平面（知识/研究运行/控制）、八组件、三闭环；实测当前主链未闭合、全图拓扑验证失败、规范知识与上下文编译器缺失
- [x] **数学大师系统总体架构v2修订**：确立思维形状公理、动态题目Q_t、K/T/H三图模型、Agent M闭环和“模式→激活包”的高阶时序启发关系
- [x] **数学大师系统总体架构v3完整复核**：同轮通读80—99号，回答当前机制、有效性、改进、Master答案泄漏、费马大定理五问；确认旧POC只对静态完整路线有局部信号，动态P→X矫正完全未验证。见122号v3
- [x] **第一性原理重构计划v1**：以`系统探讨.md`全文为母本，严格化目标系统为类型化任务/工作区、事件溯源、表示变换、时序规则、证据状态和受约束最小干预；给出DYN-0—7、Phase 0—7、角色权限、数据crosswalk、停止条件及Ramsey/费马案例。见123号v1
- [x] **Phase 0：冻结legacy与统一语义**——按123号第十部分和124号Check List：标记七步骤为legacy-static、冻结dg_*现状和模式统计、定义8类schema、建立Truth Vault与角色隔离矩阵、取消L1/L2/L3=v1/v2/v3映射、建立candidate/validated/published/retired生命周期。**Phase 0出口门全部通过**（P0-EXIT-1/2/3），证据见126/127/128号文档
- [ ] **Phase 1：只观察，不提示**——按123号第四十六节和124号：完成DYN-0（事件捕获真实性），创建运行manifest、捕获公开文本和工具事件、建立不可变原始事件和语义事件抽取
- [ ] **Phase 2：类型化状态与研究义务**——按123号第四十七节和124号：完成DYN-1（状态重建一致性）和DYN-2（卡点检测校准），实现V/F/O/R/D/E工作区、AND/OR研究义务、多观察者一致性测试
- [ ] **架构调查A：统一词汇与系统边界**——消除多套L1/L2/L3、“三层”“七步骤”和图概念碰撞；纳入数学知识图K、外显思维图T、启发激活图H。**由Phase 0接管**
- [ ] **架构调查B：规范数学知识与三图模式**——分别统一K/T/H的节点、边、tag、证据、版本和端点规则；制定POC旧模式与题库模式的非破坏性迁移方案。**由Phase 1接管**
- [ ] **架构调查C：最小端到端研究主链**——用一个小问题闭合"独立尝试→T图建模→停滞检测→H图匹配→最小启发→工具验证→审计→候选关系回写"。**由Phase 1—2/DYN-0—DYN-2接管**
- [ ] **最小启发因果POC**——从多次失败A/成功B轨迹差分提取候选P→X，用Hint-0至Hint-2提示做有对照的重复干预和跨题迁移；未通过前不建设大规模启发库。**对应DYN-3—DYN-5**
- [ ] 设计数学领域的依赖图初始结构（数学领域/工具/问题类型如何组织为节点和边）——由架构调查B接管
- [ ] 选型数学计算工具（SymPy / SageMath / Lean / Coq / ...）——81号已提出SymPy→SageMath→Lean 4；122号确认工具已部分安装但尚未接入研究运行主链
- [ ] 建立第一个数学知识系统骨架（`math-notes/` 目录结构）——122号确认目录当前不存在，需先决定其与规范知识层及ArangoDB的权威关系
- [x] 设计数学版 POC 验证方案（参考星学 POC1-8 实验设计）——大师-POC-1 正式方案已落盘到 84 号文档；题库难度梯度与 POC 阶梯的对应关系见 82 号文档第七节
- [x] 确定第一个数学研究场景作为 POC 实验场——矩条件极差题（84号文档）
- [x] **大师-POC-1 执行完成**：B组显著优于A组（边际增益+1.75/5分制），核心信念在数学领域成立。结果见 85 号文档
- [x] 题库建设：Phase A 标杆题库（Proofs from THE BOOK + MathLib 100 Theorems，手工结构化 20-50 道）——见 82 号文档第六节。**Phase A完成**：15道题42个解法已导入ArangoDB，依赖图452节点393边(含69条跨领域映射边)，认知图57个认知单元。见 107 号文档
- [x] **三层提取 POC**：验证 L1/L2/L3 三层提取的跨题复用增益（A=仅L1 / B=L1+L2 / C=L1+L2+L3 三组对照）——见 83 号文档第六节。**POC-3完成**：题3远迁移C vs B L3增量+2.6≥+1.5成功。结果见 106 号文档
- [x] **部署 ArangoDB 基础设施**：共用星学项目 ArangoDB 实例（端口8529），创建 `xishujuzhen_math` 数据库，运行 `arangodb_init.py`（已复制到数学项目 `xishujuzhen/`）——见 86 号文档
- [x] **大师-POC-2 采用七步骤工作流**：矩条件极差题第二问完整证明，使用 ArangoDB + G'_topo + TopologyVerifier，从文字对照升级为拓扑确定性验证。B组显著优于A组（+3.27/10分制）和B'组（+2.34/10分制），H1-H5全部验证通过。结果见 88 号文档
- [x] **P0知识搜集——arXiv穷尽式**（109号方案第⑤来源）：239472篇元数据（44分类，2023-2026，323.8MB JSON）+ 1305篇HTML全文（145分类，972008行114MB）。技术路线：arXiv API submittedDate日期范围查询 + 200条/页 + 3秒间隔 + 429重试退避。大分类达10000 API上限。见`knowledge/arxiv/`
- [ ] **P1知识搜集**（109号方案十三大来源中剩余来源）：①MathLib 100000+定理导入 ②OEIS 37万序列 ③THE BOOK完整版 ④关键数学家全集（Euler 80卷/Ramanujan笔记+Berndt注解）⑤教材与专著~200本 ⑥竞赛题全集（含Schweitzer研究级）⑦形式化数学库（Coq/Mizar/Metamath）⑧数学杂志问题栏（AMM 1894-/Crux/Kvant）⑨Bourbaki Seminar/ICM Proceedings ⑩Gardner 25年专栏/Conway全部 ⑪历史与哲学（Kline通史/Stillwell/Neugebauer/Heath）。按111号"难妙新"优先级排序
- [x] **arXiv元数据导入ArangoDB**：239K篇元数据导入ArangoDB建立论文索引，支持按分类/日期/作者/关键词查询，为依赖图节点提供论文出处定位——**已完成**：239472篇导入`arxiv_papers` collection，4个persistent索引，SDK新增`search_arxiv()`/`get_arxiv_paper()`/`promote_arxiv_paper()`/`get_arxiv_stats()`方法。四级映射规则（L1定理级/L2方法级/L3意识级/L4索引级）。详见112号方案
- [x] **POC-4代数拓扑泛化性验证**：Klein瓶同调群计算。A/B两组满分15/15，增量0。问题选择不当（标准教材内容在AI"会"区）。详见113-114号文档
- [x] **POC-5数论最新论文验证+隔离测试方案**：arXiv:2608.02381 orientation-rigidity定理。独立目录+AGENTS.md软限制+tmux监督隔离测试方案验证有效。A/B两组满分15/15，增量0。B组使用了反证法+螺旋交叉验证（依赖图影响结构不影响正确性）。详见115-117号文档
- [ ] **POC-6修正版证据闭环**：原始B组依赖图存在答案泄漏，119号原`+4.0/10`已降级为低可信历史结果。修正版A组猜k^{k/6}(错误)，B组运行中断。按121号方案先完成B组恢复性重跑，再做至少3对同配置A/B配对复跑、完整过程审计和盲评，之后才能给正式判定
- [ ] **POC-7方向**：依赖POC-6修正版证据闭环。在更多领域验证"发现型"问题的增量（如分析/几何/逻辑领域），或扩展到"构造型"问题（让AI构造反例/构造证明）
- [ ] **运行6个诊断测试**（97号测试方案）：T14 A/B对照待执行（需真实任务场景），T11b未执行（topo_generator已覆盖meta AI版）

### 数据丢失修复（事件2026-08-05-A）

> 详见"数据丢失事件记录"节。ArangoDB cognition_units中130个awareness单元被truncate清空，不可恢复。

- [ ] **改`cognition_import_math.py`为merge/upsert模式**——不truncate，对每条JSON记录upsert；对ArangoDB有但JSON没有的记录保留不动或标记orphan待人工确认
- [ ] **新增`cognition_export_math.py`**——ArangoDB→JSON双向同步，定期把ArangoDB当前状态回写到`cognition_units_math.json`
- [ ] **在`cognition_sdk_math.py`的`add_unit()`中增加JSON回写或审计日志**——每次add_unit时至少写一条审计记录到单独collection，记录cog_id/title/category/key_cognition/source_docs，防止再次出现"ArangoDB有但JSON没有且无记录"的情况
- [ ] **配置arangodump定期备份**——`arangodump` + cron定时任务，备份到`/data/master-mind/backups/arango/$(date +%Y%m%d)`，保留最近N天

## Memory Section

> 本节记录跨 Session 需要保持的认知。

### 数学大师系统总体架构基线（122号v2，已被123号严格化）

> 以下13条仍是有效的工程直觉，但123号已把它们严格化为类型化对象、事件溯源、表示变换、时序规则、证据状态和受约束最小干预。当本节与123号冲突时，以123号为准。

1. **基础公理**：思维的形状可以通过外显研究轨迹被观察、比较和干预；这里建模的是可观测投影，不声称读取LLM全部内部思维。
2. **系统定义**：数学大师系统不是知识库或单张依赖图，而是围绕AI研究者建立的数学研究认知操作系统。
3. **三平面**：知识平面负责证据、规范知识、数学知识图K和启发激活图H；研究运行平面负责动态题目Q_t、外显思维图T、召回、上下文编译、AI研究、工具验证和结果；控制平面负责版本、POC、干预证据、审计和回归。
4. **三图模型**：K记录数学上什么关系成立；T记录某次Agent实际上怎么想；H记录“当前T出现什么局部模式，在什么上下文/时序/失败状态下，应激活K中的什么方向”。三者不得混入同一边集合。
5. **稀疏矩阵新定义**：核心格子不是普通知识依赖，而是条件化启发关系`模式→激活包`；多元关系用超边/guard保留内部结构，不为每个元组组合物化节点。
6. **动态题目**：`Q_t = 原题Q_0 + 当前思维轨迹 + 工具证据 + 未解决目标`。任何中间状态都可成为下一轮继续研究的新题目。
7. **Agent M闭环**：独立尝试→形成T图→检测停滞→匹配H图→注入最低有效Hint级别提示→从checkpoint继续→工具/审计验证→更新启发效果证据。第一阶段推荐反应式救援，不做过早主动提示。
8. **十组件**：Evidence Registry、Math Knowledge Core、Math Knowledge Graph、Thought Trace Modeler、Heuristic Activation Engine、Retrieval & Subgraph Engine、Context Compiler、Research Runtime、Verification & Audit、Governance & Evolution。
9. **因果纪律**：成功B比失败A多想到X，只能产生候选P→X；必须通过多次最小提示干预、无提示对照和跨题迁移，才能发布到生产H图。
10. **当前最大缺口**：没有闭合“独立尝试→T图→停滞→H匹配→最小启发→验证→认知回写”的产品主链；当前`dg_edges`混合知识关系、轨迹边和意识调用，需由架构调查B拆分。
11. **2026-08-05实测状态**：`dg_nodes=1719`、`dg_edges=1483`、`kcs=18`、`arxiv_papers=239472`且全部仍为L4；`prompts/analyses/audits/uf_nodes/uf_edges`均为0；全图拓扑覆盖为节点99.4%、边79.0%，未通过。
12. **当前优先级**：先统一K/T/H词汇与模式，再做一个最小可证伪的启发干预POC；通过前不以扩大节点或启发数量作为主成功指标。
13. **架构边界风险**：旧MOIRA运行胶囊仍以七政四余为硬锚点，不是数学大师控制面；不得让其错误指令支配数学架构工作。

### 第一性原理重构基线（123号v1，当前最高架构与建设基线）

> 123号以`系统探讨.md`全文为母本，把122号v2的工程直觉严格化为可证伪、可审计的对象。本节是后续schema、POC和运行时必须服从的最高基线；与122号v2冲突时以本节为准。

1. **目标系统严格化**：类型化任务/工作区、不可变事件、表示变换、时序启发规则、证据状态和受约束最小干预。K/T/H保留为底层语义、事件和规则在不同投影面上的视图，不再是三张独立混入边集合的图。
2. **核心信念降级**：“完美提示词可通过经典计算产生”从硬公理降为可证伪假设；目标改为“最小信息、低泄漏、有因果增益的策略”，必须通过DYN-0—DYN-5验证（DYN-3因果干预+DYN-4帮助量曲线+DYN-5跨题迁移）。
3. **动态对象定义**：原题固定；动态的是工作区、事件流、信念状态和预算。状态商`S_t`由开放义务、证据门和冲突进展向量构成，不再依赖“是否产生新判断维度”的直觉判别。
4. **七步骤降为legacy**：保留静态重建价值，不再承担主运行时；主运行时是12步事件溯源循环（观测→状态归约→候选规则匹配→受约束干预→验证→归因→回写）。
5. **DYN阶梯**：DYN-0事件捕获真实性 → DYN-1状态重建一致性 → DYN-2卡点检测校准 → DYN-3同可观测checkpoint分层最小干预 → DYN-4帮助量响应曲线 → DYN-5跨题与跨模型迁移 → DYN-6在线闭环控制器 → DYN-7跨领域与长证明编排。未通过DYN-3前不建设大规模启发库。
6. **Phase 0—7建设计划**：每个Phase有入口门、验收标准、停止条件和回滚边界；Phase 0是冻结legacy与统一语义（含只读盘点dg_*），Phase 1是只观察不提示（DYN-0），Phase 2是类型化状态与研究义务（DYN-1/DYN-2），依次推进。详见124号Check List。
7. **角色隔离**：Truth Curator、Runner、Trace Modeler、Hint Designer、Verifier、Auditor、Orchestrator职责分开；同一人/Agent不得同时持有答案、构图、写提示、代写输出和评分。
8. **高级数学分阶段**：类型论、超图、可实现事件结构、因果实验和操作化泄漏指标先行；严格信息论、范畴、层、TDA、HoTT在对象与分布假设成熟后进入，不在状态空间未定义时宣称找到同调洞。
9. **数据crosswalk**：`dg_*`→新schema有字段级映射；旧节点按`is_knowledge/is_trace/is_heuristic/is_evidence/is_execution`五类拆分，不允许新系统直接继承混合边。
10. **允许核心假设失败**：停止条件和降级终态（退回静态重建器或人工辅助研究）是系统科学性的一部分；不通过DYN-3即不进入DYN-5。

### 80—99号完整复核后的证据裁决（122号v3）

1. **当前真实机制**：Master预先把“应该考虑什么”写入静态图G；经典计算复制为G'_topo并检查不漏；AI按图转译和证明。它矫正的是相对预建图的覆盖，不是在线识别Agent当前思维缺口。
2. **POC-1证据边界**：B组包含具体$q(x)$、`n=500`和完整analysis guidance，且B输出由Master生成；结果只支持“给具体路线可能改善输出”，未隔离证明最小意识提示的因果增益。
3. **POC-2证据边界**：给定包含稳定性方程、BA、柯西和最终结论的完整图，七步骤可较完整展开；A/B'由Master生成、单次运行、评分混入B独占基础设施维度，不能证明未知思路发现能力。
4. **经典计算边界**：topo_generator的100%来自原样复制输入图；不发现P→X、不判断X正确、不防答案泄漏。TopologyVerifier证明结构保真，不证明语义或数学真值。
5. **工作系统边界**：98号14/16通过主要是组件自洽测试；真正A/B有效性T14未执行。工作认知回归100分不等于数学大师能力100分。
6. **答案泄漏根因**：84号把“提示有用”而非“公平/最小”定义为目标；Master同时持有答案、构图、写提示、代写输出并解释结果；图模型未区分知识、成功路线和启发，100%覆盖又鼓励完整答案图。
7. **费马案例裁决**：谷山—志村猜想陈述单独不足以证明FLT。调用已证半稳定模性定理还需要Frey曲线、半稳定性、mod p Galois表示、Ribet降层和低level模形式不存在；重建Wiles证明还需模性提升、变形理论、Hecke代数、$R=T$、Taylor—Wiles素数和patching等巨大子图。
8. **核心愿景的精确条件**：当K图知识模块充分、H图在T图卡点上触发正确、模型有局部推理能力、验证闭环可用时，系统可以把“不会组织证明的AI”提升为“能分步重建并验证证明的Agent”。
9. **下一核心实验**：不再比较“完整图B组”与无提示组；先做轨迹可观测性POC，再做限制Hint-0至Hint-2的重复、对照、盲评、跨题迁移因果POC。

### 工作系统纪律（三层维护机制）

以下纪律由三层维护机制保障（CP4提示 + AGENTS.md约束 + 认知图依赖）：

1. **新术语必须追加到词汇表**：工作中产生的新术语，必须追加到工作系统词汇表（认知单元 `glossary`）。
2. **临场脚本沉淀纪律**：工作中现写的一次性脚本，如果操作模式可复用，结束后必须沉淀到 `cognition_sdk_math.py` 或对应模块（认知单元 `sdk_maintenance`）。
3. **必须 commit**：工作结束后必须 commit。commit 后 git post-commit hook 会打印 CP4 检查清单（从认知图稀疏矩阵动态查询）。
4. **不要用 Stop hook**：Stop hook 会影响 subagent（星学项目实测证实）。用 git post-commit hook 代替。
5. **认知图变更后跑回归验证**：认知图每次变更（新增/修改/删除认知单元或依赖边）后，运行 `cognition_audit_math.py poc-regression`。
6. **边吸收边测试**（认知单元 `iterative_testing`）：每次往依赖图/认知图装入新内容后（新增题目、新增节点/边、新增意识节点、新增版本链等），必须立即跑测试验证：依赖图完整性（节点/边/领域覆盖）+ topo_generator能否生成G'_topo + TopologyVerifier拓扑覆盖验证。不测不知道有问题——从星学复用的代码遗留3个bug只有跑真实测试才发现。
7. **"检查依赖"触发词**：当用户说"检查依赖"时，AI 立即执行CP4检查清单中的第3、4项（`work_matrix_update` + `math_master_matrix_update`）——这是CP4的按需触发版本，不等到git commit：
   - **工作系统稀疏矩阵更新纪律**（`work_matrix_update`）：回顾本轮对话，是否产生了新的工作认知、新的工作认知之间的依赖关系、新的dev-docs与认知单元的source_docs关系？如果有，用`cognition_sdk_math.py`的`add_unit`/`add_edge`写入认知图。
   - **数学大师系统稀疏矩阵更新纪律**（`math_master_matrix_update`）：回顾本轮对话，是否产生了新的数学知识依赖（定理→引理、方法→工具、意识→问题类型）、新的数学意识节点、新的版本链？如果有，写入`dg_nodes`/`dg_edges`。
   - 这两项纪律也是CP4检查清单的一部分（stop_hook的depends_on边），每次git commit后post-commit hook会自动提醒。

### Subagent 写文件能力与 /yolo 模式

- **现象**：大师-POC-1 执行时，background subagent 无法写入 `/Volumes/` 路径下的文件；但前台 subagent 可以写入。
- **原因排查**：用户开启了 `/yolo` 模式（自动批准工具调用），这可能是影响 subagent 写文件能力的一个因素。后续测试确认前台 subagent 在当前配置下可以写入 `/Volumes/` 路径。
- **建议**：后续 POC 实验中，如果需要 subagent 写文件，优先使用前台 subagent；如果遇到写文件失败，提醒用户检查 `/yolo` 模式状态。

### POC隔离测试标准流程（116号方案，已验证有效）

POC对照实验必须隔离测试环境，防止subagent看到项目AGENTS.md或用网络搜索作弊：

1. **创建独立目录**：`/data/math-agent-{1,2}/`，每组一个
2. **写AGENTS.md软限制**：禁止web_search/webfetch、禁止访问/data/master-mind
3. **写problem.md**：数学问题描述（A/B组相同）
4. **B组加dependency_graph.json**：依赖图提示（A组无此文件）
5. **tmux启动devin**：`tmux send-keys -t <session> "cd /data/math-agent-X && devin --respect-workspace-trust false" Enter`
6. **发送prompt**：让agent读problem.md解题写入result.md
7. **选accept edits mode**：当agent请求文件写入审批时，按Down+Enter选option 2
8. **tmux capture-pane审计**：检查agent是否违规（web_search/访问master-mind）
9. **读取result.md评分**：按8维15分制评分

### 四次POC核心洞察（POC-6待重新验证）

| POC | 领域 | 问题类型 | A组 | B组增量 | 证据状态 | 结论 |
|---|---|---|---|---|---|---|
| POC-1 | 分析/不等式 | 证明型+计算陷阱 | 犯错(3.25/5) | **+3.50/10** | 高可信 | 依赖图显著增量 |
| POC-4 | 代数拓扑 | 证明型+标准教材 | 满分(15/15) | 0 | 高可信 | 零增量 |
| POC-5 | 数论/mod 3 | 证明型+基本功 | 满分(15/15) | 0 | 高可信 | 零增量，但影响证明结构 |
| **POC-6原始版** | **组合/Ramsey** | **发现型** | **犯错(9/15)** | **表面+4.0/10** | **低可信：依赖图泄漏答案** | **不得据此宣告泛化成立** |
| **POC-6修正版** | **组合/Ramsey** | **发现型** | **猜k^{k/6}，错误** | **B组待完成** | **实验进行中** | **按121号方案重跑和审计** |

**当前可成立的核心结论**：
1. POC-1证明依赖图在一个AI"不会"区问题上可以产生显著增量；POC-4/5说明AI"会"区可能出现零分数增量但推理结构变化
2. "发现型"问题是有价值的POC方向，但提示更容易越过“给方向”和“给答案”的边界，必须做逐节点答案泄漏审计
3. POC-6原始版不能支持跨领域泛化结论；修正版必须经过重复A/B运行、完整过程审计和盲评后再判断
4. 111号"难妙新"原则仍是知识搜集和选题假设，但不能用原始POC-6的`+4.0/10`作为有效证据

## 数据丢失事件记录

> 本节记录已发生的数据丢失事件，供后续排查、恢复和预防参考。

### 事件2026-08-05-A：ArangoDB cognition_units awareness单元清空

**发生时间**：2026-08-05，123号同步工作期间

**直接操作**：运行 `xishujuzhen/cognition_import_math.py`，该脚本先 `truncate` 清空 `cognition_units`/`cog_edges`/`cog_versions` 三个collection，再从 `xishujuzhen/poc/cognition_units_math.json` 重新导入。

**丢失数据**：

| 项目 | 丢失前 | 丢失后 | 丢失量 |
|---|---|---|---|
| `cognition_units`（总） | 165 | 29（JSON原有）→ 35（本轮新增6个） | **130个认知单元** |
| `cognition_units`（awareness类） | 134 | 5（JSON原有） | **129个awareness单元** |
| `cog_edges` | ~50 | 36（JSON原有）→ 51（本轮新增15条） | 约14条边 |
| `cog_versions` | 178 | 17（JSON原有）→ 51（本轮新增34条） | 约127条版本记录 |

**丢失单元的已知特征**（从排查中拼凑）：

1. **数量演化轨迹**：
   - 91号方案设计时：~30个认知单元（12 core + 4 process + 6 support + 5 awareness）
   - 98号测试报告：27个认知单元（12 core + 4 process + 6 support + 5 awareness），31条边，30条版本记录
   - 114号（POC-4后）：162→163（+structural_thinking）
   - 117/119/120/122号：稳定在163
   - 123号SessionStart显示：165（+2，来源不明）
   - 丢失后：35（29 JSON原有 + 6本轮新增）

2. **来源推断**（无直接证据，以下为合理推测）：
   - **题库Phase A的意识节点**：91号方案第2.3节和99号反哺5提到"从POC结果中自动发现新意识节点，在cognition_units中创建对应认知单元"。107号提到题库Phase A完成时认知图有57个认知单元。题库15道题42个解法的L2/L3提取可能产生了大量awareness单元。
   - **absorb_test_loop.py的批量提取**：该脚本设计为分批吸收数学知识，每批15题做L1/L2/L3三层提取。如果执行过，L2/L3提取结果可能通过`sdk.add_unit()`写入ArangoDB。
   - **POC-4的structural_thinking**：114号记录POC-4新增了`structural_thinking`到cognition_units（162→163），这个单元在JSON中不存在，已丢失。
   - **CP4/CP5工作流中AI临场创建的单元**：AGENTS.md第567行提到"用cognition_sdk_math.py的add_unit/add_edge写入认知图"。历次session的AI可能在工作过程中通过add_unit创建了awareness单元但未回写JSON。

3. **从未被使用过的证据**：
   - `cognition_tasks`中5条任务记录共引用36个cog_id，其中7个不在当前units中（agents_tech_mathmaster/agents_tech_worksystem/doc_sync_discipline/iterative_testing/math_master_matrix_update/poc3_execution/work_matrix_update）——这些是core/process类，不是awareness。
   - 没有任何checkpoint任务加载过那134个awareness单元。
   - `seed_recommendation_table.json`只引用5个awareness种子（numerical_check/extreme_testing/invariant_thinking/approximation_thinking/local_global_thinking），都在JSON中。
   - 没有任何脚本、文档或git提交记录了那134个awareness单元的cog_id、title或key_cognition。

4. **可能包含的内容**（基于99号反哺方案设计）：
   - 题库Phase A的15道题的L2思维模式（如"矩阵=模等价""组合=拓扑不变量"等paradigm类节点，对应dg_nodes中165个paradigm节点）
   - L3范式思维节点
   - POC-3/4/5中发现的候选新意识
   - 历次session中AI临场创建的工作认知

**根因**：

1. `cognition_import_math.py`设计为`truncate → reload`模式，假设JSON是唯一source of truth
2. `cognition_sdk_math.py`的`add_unit()`只写ArangoDB不回写JSON，假设ArangoDB是运行时权威
3. 两个假设矛盾，导致ArangoDB积累了JSON没有的单元
4. 没有export脚本（ArangoDB→JSON双向同步）
5. 没有配置arangodump定期备份
6. ArangoDB无企业版hot backup，社区版无WAL回放

**不可恢复性确认**：
- ArangoDB无备份（`_admin/backup/list`返回404）
- WAL API在ArangoDB v4.0+已移除
- git历史中JSON最多29个单元
- 无其他数据源可恢复那130个单元的内容

**影响评估**：
- 那134个awareness单元从未被任何POC任务加载或使用
- 不影响123号重构计划（123号已把七步骤降为legacy，认知图控制面角色重新定义）
- 不影响现有5个数学意识种子（都在JSON中保留）
- **但**：如果未来需要重建题库Phase A的L2/L3提取结果，需要重新跑三层提取

**待修复**（见TODO节"数据丢失修复"）：
- [ ] 改`cognition_import_math.py`为merge/upsert模式，不truncate
- [ ] 新增`cognition_export_math.py`（ArangoDB→JSON双向同步）
- [ ] 配置arangodump定期备份到`/data/master-mind/backups/arango/`
- [ ] 在`add_unit()`中增加JSON回写或至少审计日志

## Handover Section

> 本节在压缩前更新，确保压缩后不丢认知。

### 工作系统实现状态（2026-08-05）

**已实现并测试通过**：
- `xishujuzhen/cognition_init_math.py`：ArangoDB初始化（5个新collections + 索引 + graph）
- `xishujuzhen/cognition_import_math.py`：认知单元导入
- `xishujuzhen/cognition_verifier_math.py`：认知图遍历引擎（AQL图遍历 + 集合差集覆盖验证）
- `xishujuzhen/cognition_sdk_math.py`：认知图SDK（CRUD + 审计 + 拓扑覆盖验证 + 交叉引用）
- `xishujuzhen/cognition_checkpoint_math.py`：CP1-CP6工作流入口
- `xishujuzhen/cognition_audit_math.py`：审计CLI（全量审计 + POC回归评分 + 拓扑覆盖验证）
- `xishujuzhen/topo_generator.py`：经典计算展开G'_topo（L0+L1+L2，1次通过100%覆盖）
- `xishujuzhen/seven_step_pipeline.py`：七步骤工作流集成脚本（步骤2调用topo_generator）
- `xishujuzhen/seed_recommendation_table.json`：种子推荐表（5种问题类型→推荐意识种子）
- `xishujuzhen/session_start_hook_math.py`：SessionStart + PostCompaction hook
- `xishujuzhen/user_prompt_submit_hook_math.py`：UserPromptSubmit hook（从txt读取提醒注入）
- `xishujuzhen/UserPromptSubmit.txt`：提醒内容文件（可随时编辑定制）
- `xishujuzhen/githooks/post-commit`：git post-commit hook（CP4检查清单 + AGENTS.md对齐检查）
- `xishujuzhen/githooks/pre-commit`：git pre-commit hook（AGENTS.md对齐硬性检查，阻止引用不存在文件的commit）
- `xishujuzhen/alignment_check.py`：AGENTS.md与repo内容对齐检查脚本（文件存在性+编号覆盖+DYN/Phase定义一致性+认知图规模一致性）
- `xishujuzhen/poc/cognition_units_math.json`：认知单元定义
- `.devin/hooks.v1.json`：Devin hooks配置（SessionStart + PostCompaction + UserPromptSubmit，不含Stop）

**测试结果**：
- 工作系统测试：14/16通过（98号报告）。T11b未执行，T14待真实任务场景。
- 反哺方案测试：10/10通过（100号报告）。R1-1~R6-1全部通过。

**关键参数**：
- max_depth默认值：7（数学项目路径比星学长，星学用5）
- git hook shebang：`#!/data/master-mind/.venv/bin/python3`（绝对路径）
- 意识节点名称映射：英文cog_id ↔ 中文node_id（cross_reference_dg方法中）

**ArangoDB状态**：
- 数据库：xishujuzhen_math
- 认知图：35个认知单元（事件2026-08-05-A后；原165个中130个awareness单元已丢失，详见"数据丢失事件记录"节），51条边
- CP4检查清单6项纪律：iterative_testing(边吸收边测试), math_master_matrix_update, work_matrix_update, doc_sync_discipline, sdk_maintenance, glossary
- 5个意识节点版本链：v1(POC-1发现)→v2(POC-2深化)，current_version=v2
- cayley_hamilton三层版本链：v1(L1)→v2(L2)→v3(L3)，current_version=v3（**注意：cayley_hamilton单元在事件中丢失，需从题库重建**）
- three_layer_extraction版本链：v1(83号方案)→v2(POC-3验证L3跨领域迁移价值成立)，current_version=v2（**注意：该单元在事件中丢失，需重建**）
- AGENTS.md技术说明依赖已入稀疏矩阵：agents_tech_worksystem(source_docs=[91,94,97,100,101]) + agents_tech_mathmaster(source_docs=[83,85,86,88,90,92,99,100])（**注意：这两个单元在事件中丢失，需重建**）
- 数学依赖图（Phase 0冻结时点值，详见126号只读盘点报告）：dg_nodes=1719（concept:867, domain_concept:599, paradigm:165, problem:53, substep:27, 意识:5, step:3），dg_edges=1483（edge_type: unknown:1431/depends_on:38/calls:13/invokes:1; mapping_type: solution_path:837/invokes:259/structural_analogy:136/equivalence:87/其他:264），loops=4（dependency_graph:2, unfold_topo:2）
- 题库：60道题，159个解法（problems + solutions集合，未受事件影响）
- arxiv_papers：239472篇（未受事件影响）
- G'_topo（经典计算生成）：18节点，25边，2环路，TopologyVerifier 1次通过100%覆盖（POC-2场景）
- POC回归验证基线：POC-1=94/100，POC-2=100/100（**注意：回归基线可能因单元丢失而变化，需重新验证**）

**知识搜集状态（2026-08-04）**：
- **P0经典知识**：38文件10810行680KB（Ramanujan/Arnold/思想书/竞赛题/突破/Conway/开放问题）——`knowledge/`根目录
- **arXiv穷尽式元数据**：239472篇唯一论文，323.8MB JSON——`knowledge/arxiv/metadata_all_2023plus.json` + `knowledge/arxiv/metadata/meta_*.json`
  - 44个分类：math.* 28个 + cs.CC/LO/FL/DS/CG/GT/SC 7个 + quant-ph + math-ph + hep-th + stat.ML + nlin.CD/SI/AO/PS 4个
  - 年份分布：2023=48983 / 2024=69810 / 2025=62131 / 2026=58548
  - 大分类达10000 API上限（math.CO/AP/OC/PR/NA, quant-ph, hep-th, stat.ML）
  - math.MP和stat.TH返回0（分类名可能需要交叉列表查询）
- **arXiv全文**：1305篇972008行114MB——`knowledge/arxiv/fulltext/*.md`
  - 145个分类各10篇最新论文HTML全文
  - math.* 325篇 / cs.* 302篇 / physics.* 182篇 / quant-ph 7篇 / math-ph 8篇 / hep-th 9篇 / stat.* 45篇 / nlin.* 45篇
  - 216篇失败（主要是旧论文无HTML版本）
- **arXiv技术路线**（全部免费匿名无key）：
  - 元数据：arXiv API `export.arxiv.org/api/query` + submittedDate日期范围查询（2025-2026 + 2023-2024两批） + 200条/页（API最大值） + 3秒间隔 + 429重试退避（60s/120s/180s...）
  - 全文：`arxiv.org/html/<id>`抓取HTML转Markdown + 3秒间隔 + 429重试退避
  - 脚本：`scripts/arxiv_search_v3.py`（元数据）+ `scripts/arxiv_fetch_html_v2.py`（全文）
- **P1待搜集**（109号方案十三大来源中剩余来源）：MathLib 100000+定理 / OEIS 37万序列 / THE BOOK / 数学家全集 / 教材~200本 / 竞赛题全集 / Coq/Mizar/Metamath / AMM问题栏 / Bourbaki Seminar / Gardner/Conway / Kline通史等

**arXiv论文ArangoDB操作化状态（2026-08-04）**：
- `arxiv_papers` collection：239472篇论文元数据已导入ArangoDB（22.9秒，10466篇/秒）
- 4个persistent索引：primary_category / published / mapping_level / has_fulltext
- 四级映射规则（112号方案）：L1定理级（论文中的定理成为dg_nodes concept节点）/ L2方法级 / L3意识级 / L4索引级（默认，仅在arxiv_papers中可搜索）
- SDK新增4个方法：`search_arxiv()`（按分类/关键词/作者/日期/全文/映射级别查询）/ `get_arxiv_paper()`（单篇获取）/ `promote_arxiv_paper()`（提升映射级别+关联dg_nodes）/ `get_arxiv_stats()`（统计）
- 所有239472篇初始为L4索引级，可按需提升为L1/L2/L3并关联到dg_nodes——这是"大师的一次在场"的体现
- 查询性能：按分类+日期排序查询~毫秒级（persistent索引生效）
- 脚本：`xishujuzhen/arxiv_to_arangodb.py`（导入+索引创建+验证）

## 术语备忘

- **xishujuzhen**：稀疏矩阵的拼音。星学项目中建立的依赖图导航系统的代号。数学项目中沿用此名，指代同一套方法论下的数学版导航系统。
- **综述博士 / 论文博士**：用户对两种大师的区分。综述博士 = 知识体系全掌握、全能灵活运用；论文博士 = 负责创新。本项目工程化综述博士。
- **AGENTS-星学版.md**：本目录中保留的星学项目完整 AGENTS.md，是方法论参考资产，不是工作对象。
