# 项目 AGENTS.md · 数学大师制造

## 项目定位

本项目是 **AI 数学大师制造项目**，不是单纯的写代码项目，也不是星学项目。

项目从星学领域的 POC 实验中继承了一套已验证的方法论——"用稀疏矩阵依赖图工程化大师的'知道该判断什么'"——现在要把这套方法论迁移到数学研究领域，目标是制造一个能做数学研究的 AI 大师。

**"数学大师"的定义**：本项目语境中的"数学大师"，指能做数学研究的 AI——提出猜想、构造证明、发现新定理、在复杂数学问题面前知道该从哪个方向切入、该调用哪些数学工具、该沿什么路径思考。不是只会做题的解题机器，而是具备研究品味的数学家。

**"最通用的数学大师"**：本项目目标是制造**最通用的数学大师**，不是某个特定数学领域的专家系统。数学大师应该能覆盖代数、几何、分析、拓扑、数论、组合、逻辑、范畴论等全部数学领域，能在任意数学问题面前知道该判断什么。当前以矩条件极差题等具体场景作为POC实验场，但这是验证方法论的实验场景，不是项目的终态边界。依赖图的构建从具体领域切入（如代数拓扑），逐步扩展到全部数学领域——不预设领域边界。

**"新系统"的硬边界**：本项目语境中的"新系统"，默认且专指为数学研究而建设的知识系统与思维导航系统。星学项目中的 `qizheng/`、`study-notes/`、MOIRA Java、Swiss Ephemeris 等是**参考实现和方法论证据链**，不是新系统本体。

### 本项目与星学项目的关系

本项目从 `~/MOIRA_chinese_astrology-main/`（已复制到当前目录 `/data/master-mind/`）的星学研究中继承而来。星学项目完成了从"直觉画面"到"POC1-8 验证体系"的完整方法论 POC，证明了"大师的完美提示词可以通过经典计算产生"这一核心信念在星学领域可行。

本项目要做的是：**把这套已验证的方法论，迁移到数学研究领域。**

星学是第一个实验场，数学是第二个。如果方法论在数学领域同样成立，它的意义将不限于数学——任何复杂知识体系的"综述博士"角色都可能被工程化。

## 核心信念（从星学 POC 继承）

这是整个项目的灵魂，直接继承自星学项目 63 号文档的完整对话。以下不是抽象口号，而是已经过 POC1-8 验证的可证伪信念：

### 信念陈述

> 大师（综述博士）让 AI 在某时某处完美地输出，是因为大师的提示词是完美的。而这份完美的提示词，是可以通过经典计算产生的。

拆开来看：

1. **大师的价值在于提示词**——大师让 AI 完美输出，不是因为大师替 AI 做了判断，而是因为大师给了 AI 完美的提示词。
2. **完美提示词的本质**——是在正确的时刻，把正确的知识依赖关系呈现给 AI，让 AI 看到此刻该考虑什么、它们之间什么关系。
3. **可以通过经典计算产生**——完美提示词不需要另一个 AI 来生成，不需要神秘直觉，可以通过经典计算（图遍历、稀疏矩阵依赖计算）产生。
4. **稀疏矩阵是载体**——经典计算的对象是稀疏矩阵（依赖图），计算的结果是依赖子图，子图就是提示词。

### 两种博士

| 类型 | 特征 | 对应角色 | 本项目是否工程化 |
|---|---|---|---|
| 综述博士 | 知识体系全掌握、全能灵活运用 | 知道在什么时候该看什么、该结合什么 | **是，这是本项目的目标** |
| 论文博士 | 负责创新 | 创造新知识、新方法 | 不在本次工程化范围，但不排斥 |

### 大师的"一次在场"

xishujuzhen 系统（稀疏矩阵支撑的提示系统）不发现依赖关系，只编码依赖关系。"代数拓扑依赖范畴论"——这条边是谁写进图的？是数学大师（或理解数学的人）在构建系统时写进去的。

这意味着：**我们没有消除大师，我们把大师从"每次研究都在场"变成了"构建系统时在场一次"。**

- 依赖图的质量上限 = 构建者的数学水平
- 依赖图需要持续维护，数学认知深化后新的依赖关系需要被编码进图
- 依赖图的构建本身就是数学认知整理的过程

## 方法论核心（从星学 POC 继承，已验证）

以下方法论在星学领域经过 POC1-8 完整验证（验证记录见下方星学参考索引）。迁移到数学领域时，方法论本身不变，变化的是依赖图的内容（从星学知识节点变为数学知识节点）。

### 三维稀疏矩阵

大师的思维可以形式化为一个三维稀疏矩阵：

- **行**：分析节点（在数学中 = 研究问题、定理证明、猜想探索……）
- **列**：思维意识（在数学中 = 数学直觉、工具选择、领域类比、证明策略……）
- **第三维**：上下文层（同一个意识在不同研究上下文中被反复调用，每次产生不同结论）

稀疏性：总知识量很大，但在每个具体研究点上，只有一小部分被激活。大师的功力不在于知道多少，而在于知道在什么时候激活什么。

### 两种环路

| 环路类型 | 特征 | 判别标准 | 处理方式 |
|---|---|---|---|
| 平面环路 | A→B→C→A，回到起点，没有新东西 | 追溯一圈后是否产生了新的判断维度——如果没有，是循环论证 | 应停止追溯 |
| 螺旋上升环路 | 投影到平面上也是环路，但三维中每次到达的已不是原来的 | 上下文变了，在不同层次上产生新判断 | 应继续追溯 |

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

**终态目标与建设计划**：待制定。项目启动认知基础见 <ref_file file="/data/master-mind/dev-docs/80-数学大师项目启动认知基础.md" />。

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
| `dev-docs/64-xishujuzhen-POC1验证方案.md` ~ `dev-docs/77-xishujuzhen-POC8验证方案.md` | **POC1-8 完整验证体系**：从5节点小图到71节点大图、从静态分析到动态螺旋、从开环到闭环审计 | **必读**。数学项目的验证方案应参考这套实验设计 |
| `dev-docs/71-xishujuzhen-POC5验证结果.md` | POC-5 结果：边际增益+3.95，B组9.75 vs A组5.8 | 验证方法论的量化证据 |
| `dev-docs/73-xishujuzhen-POC6验证结果.md` | POC-6 结果：边际增益+5.92，交叉审计比AI自审更严格 | 交叉审计方法的参考 |
| `dev-docs/75-xishujuzhen-POC7验证结果.md` | POC-7 结果：边际增益+4.08，大规模依赖图可行（71节点100%覆盖） | 大规模可行性证据 |
| `dev-docs/76-xishujuzhen闭环审计纠正流程优化方案.md` | 闭环审计流程：审计→反馈→修正→再审→直到无瑕疵，最大3轮 | 质量保证流程参考 |
| `dev-docs/78-xishujuzhen下一代工作流-从文字随机到拓扑覆盖.md` | **下一代工作流数学本质分析**：依赖图G是规范化拓扑结构，展开图G'是G的覆盖，审计是覆盖验证φ:G'→G。HoTT框架 | **高价值**。数学项目可能直接用到这套拓扑视角 |
| `dev-docs/79-xishujuzhen下一代工作流技术选型.md` | 技术选型：ArangoDB（多模型：图+文档+键值）作为依赖图数据库 | **技术架构基础**。数学版在此基础上新增 Lean 4/MathLib、SageMath、arXiv 管道，见 81 号文档 |
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

### 星学知识系统结构参考

| 文档 | 内容 | 对数学项目的参考价值 |
|---|---|---|
| `AGENTS-星学版.md` | **星学项目完整 AGENTS.md**：1056行，包含项目定位、四类载体分工、8个工作流入口、吸收范式、形式化思维规则、解释框架、维度/成熟度/可计算性 | **必读**。数学项目的 AGENTS.md 结构直接参考它 |
| `dev-docs/56-新系统老系统吸收范式.md` | 新系统/老系统吸收范式第一版 | 知识系统建设范式参考 |
| `dev-docs/57-新系统方案迭代与老方案更新.md` | 对吸收范式的8问审视 | 知识系统迭代方法参考 |
| `dev-docs/58-新系统迭代执行CheckList.md` | 可执行 CheckList 设计 | Check List 设计参考 |
| `dev-docs/59-AGENTS重构纠偏与高价值规则回收.md` | AGENTS 重构时的保全纪律 | 本 AGENTS.md 重写时已遵循 |
| `dev-docs/60-外部系统收敛与暂存规划.md` | 外部系统收敛决策 | 知识边界管理参考 |
| `dev-docs/13-七政四余形式化体系.md` | 形式化体系：算子+集合+命题 | 数学形式化的直接参考 |

### 星学 POC 验证方案完整列表

| POC | 文档 | 验证内容 |
|---|---|---|
| POC-1 | `dev-docs/64-xishujuzhen-POC1验证方案.md` | 对照实验设计、5节点7边依赖图、5维度结构化评分 |
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

### 七步骤工作流

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
- `dg_nodes`：节点集（step/substep/意识三种类型）
- `dg_edges`：边集（depends_on/calls两种类型）
- `loops`：螺旋环路（含圈数）

### G'_topo生成（经典计算展开）

`topo_generator.py`从G自动生成G'_topo骨架：
- L0骨架展开：节点集+边集直接拷贝（拓扑同构保证全覆盖）+ Kahn拓扑排序确定traversal_order
- L1类型推断：static/dynamic + connection类型（linear/shortcut/cross_section）
- L2 section划分：按依赖链长度分段+意识节点处理
- L3语义标注（AI）：section命名、spiral_static/dynamic最终确认

### TopologyVerifier拓扑覆盖验证

`topology_verifier.py`验证G'_topo是否覆盖G：
- 节点覆盖：ut_nodes vs dg_nodes的集合差集
- 边覆盖：ut_edges vs dg_edges的集合差集
- 螺旋环路：圈数是否保持
- 结果：passed=True + 100%覆盖 = 通过

### 三层提取（L1/L2/L3）+ 版本链管理

83号文档设计的三层提取，用版本链管理演化：

| 层次 | 版本 | 内容 | 复用范围 |
|---|---|---|---|
| L1解题思路 | v1 | 具体步骤序列 | 类似题 |
| L2数学思维 | v2 | 从L1抽象出的思维模式（AI二次分析） | 跨题、跨领域 |
| L3范式思维 | v3 | 从多个L2综合出的范式（AI三次分析） | 改变图结构 |

**版本链操作**：
```bash
# 添加新版本
.venv/bin/python3 -c "from cognition_sdk_math import CognitionSDK; sdk=CognitionSDK(); sdk.add_version('<cog_id>', 'v2', '<doc>', '<summary>', version_order=2); sdk.update_current_version('<cog_id>', 'v2')"
```

**current_version反映当前提取层级**：v1=类似题复用，v2=跨题复用，v3=跨领域复用。

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

> 本节记录跨 Session 需要保持的待办事项。当前为空，待项目启动后填充。

- [ ] 制定数学大师制造项目的建设计划（Phase 划分 + Check List）——认知基础已落盘到 80 号文档
- [ ] 设计数学领域的依赖图初始结构（数学领域/工具/问题类型如何组织为节点和边）
- [ ] 选型数学计算工具（SymPy / SageMath / Lean / Coq / ...）——已落盘到 81 号文档：三层验证器阶梯 SymPy→SageMath→Lean 4
- [ ] 建立第一个数学知识系统骨架（`math-notes/` 目录结构）
- [x] 设计数学版 POC 验证方案（参考星学 POC1-8 实验设计）——大师-POC-1 正式方案已落盘到 84 号文档；题库难度梯度与 POC 阶梯的对应关系见 82 号文档第七节
- [x] 确定第一个数学研究场景作为 POC 实验场——矩条件极差题（84号文档）
- [x] **大师-POC-1 执行完成**：B组显著优于A组（边际增益+1.75/5分制），核心信念在数学领域成立。结果见 85 号文档
- [ ] 题库建设：Phase A 标杆题库（Proofs from THE BOOK + MathLib 100 Theorems，手工结构化 20-50 道）——见 82 号文档第六节
- [ ] **三层提取 POC**：验证 L1/L2/L3 三层提取的跨题复用增益（A=仅L1 / B=L1+L2 / C=L1+L2+L3 三组对照）——见 83 号文档第六节
- [x] **部署 ArangoDB 基础设施**：共用星学项目 ArangoDB 实例（端口8529），创建 `xishujuzhen_math` 数据库，运行 `arangodb_init.py`（已复制到数学项目 `xishujuzhen/`）——见 86 号文档
- [x] **大师-POC-2 采用七步骤工作流**：矩条件极差题第二问完整证明，使用 ArangoDB + G'_topo + TopologyVerifier，从文字对照升级为拓扑确定性验证。B组显著优于A组（+3.27/10分制）和B'组（+2.34/10分制），H1-H5全部验证通过。结果见 88 号文档

## Memory Section

> 本节记录跨 Session 需要保持的认知。

### 工作系统纪律（三层维护机制）

以下纪律由三层维护机制保障（CP4提示 + AGENTS.md约束 + 认知图依赖）：

1. **新术语必须追加到词汇表**：工作中产生的新术语，必须追加到工作系统词汇表（认知单元 `glossary`）。
2. **临场脚本沉淀纪律**：工作中现写的一次性脚本，如果操作模式可复用，结束后必须沉淀到 `cognition_sdk_math.py` 或对应模块（认知单元 `sdk_maintenance`）。
3. **必须 commit**：工作结束后必须 commit。commit 后 git post-commit hook 会打印 CP4 检查清单（从认知图稀疏矩阵动态查询）。
4. **不要用 Stop hook**：Stop hook 会影响 subagent（星学项目实测证实）。用 git post-commit hook 代替。
5. **认知图变更后跑回归验证**：认知图每次变更（新增/修改/删除认知单元或依赖边）后，运行 `cognition_audit_math.py poc-regression`。
6. **"检查依赖"触发词**：当用户说"检查依赖"时，AI 必须检查刚刚发生的对话中：
   - **是否有依赖应该被加入工作系统的稀疏矩阵中？**——对话中是否产生了新的工作认知、新的工作认知之间的依赖关系、新的dev-docs与认知单元的source_docs关系。如果有，用`cognition_sdk_math.py`的`add_unit`/`add_edge`写入认知图。
   - **是否有依赖应该被加入目标系统的稀疏矩阵中？**——对话中是否产生了新的数学知识依赖（定理→引理、方法→工具、意识→问题类型）、新的数学意识节点、新的版本链。如果有，写入`dg_nodes`/`dg_edges`。
   - 检查方法：回顾本轮对话，对照两个稀疏矩阵的现有内容，找出"对话中提到但尚未入图"的依赖关系。

### Subagent 写文件能力与 /yolo 模式

- **现象**：大师-POC-1 执行时，background subagent 无法写入 `/Volumes/` 路径下的文件；但前台 subagent 可以写入。
- **原因排查**：用户开启了 `/yolo` 模式（自动批准工具调用），这可能是影响 subagent 写文件能力的一个因素。后续测试确认前台 subagent 在当前配置下可以写入 `/Volumes/` 路径。
- **建议**：后续 POC 实验中，如果需要 subagent 写文件，优先使用前台 subagent；如果遇到写文件失败，提醒用户检查 `/yolo` 模式状态。

## Handover Section

> 本节在压缩前更新，确保压缩后不丢认知。

### 工作系统实现状态（2026-08-04）

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
- `xishujuzhen/githooks/post-commit`：git post-commit hook（CP4检查清单）
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
- 认知图：30个认知单元（含cayley_hamilton + agents_tech_worksystem + agents_tech_mathmaster），42条边
- 5个意识节点版本链：v1(POC-1发现)→v2(POC-2深化)，current_version=v2
- cayley_hamilton三层版本链：v1(L1)→v2(L2)→v3(L3)，current_version=v3
- AGENTS.md技术说明依赖已入稀疏矩阵：agents_tech_worksystem(source_docs=[91,94,97,100,101]) + agents_tech_mathmaster(source_docs=[83,85,86,88,90,92,99,100])
- 数学依赖图：18节点，25边，2环路（POC-2）
- G'_topo（经典计算生成）：18节点，25边，2环路，TopologyVerifier 1次通过100%覆盖
- POC回归验证基线：POC-1=94/100，POC-2=100/100

## 术语备忘

- **xishujuzhen**：稀疏矩阵的拼音。星学项目中建立的依赖图导航系统的代号。数学项目中沿用此名，指代同一套方法论下的数学版导航系统。
- **综述博士 / 论文博士**：用户对两种大师的区分。综述博士 = 知识体系全掌握、全能灵活运用；论文博士 = 负责创新。本项目工程化综述博士。
- **AGENTS-星学版.md**：本目录中保留的星学项目完整 AGENTS.md，是方法论参考资产，不是工作对象。
