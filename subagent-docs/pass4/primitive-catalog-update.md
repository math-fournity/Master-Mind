# Pass 4 产出1：全量原语目录更新方案

**日期**：2026-08-07
**状态**：落盘规划方案
**输入**：Pass 3 完整原语提炼报告（`subagent-docs/pass3/merged-primitives.md`）

---

## 0. 方案概述

本方案规划两件事：

1. **59个新原语的落盘**——18个结构原语 + 41个操作原语，每个规划一个文件，按 `primitives/` 目录现有格式编写。
2. **16个已有原语的来源补充更新**——每个已有原语获得新来源后，需在"来源"和"组合关系"字段中补充对应内容。

### 文件命名规范

- 结构原语 → `primitives/structural/<kebab-case-name>.md`
- 操作原语 → `primitives/operational/<kebab-case-name>.md`

### 模板对照

- 结构原语模板：`primitives/_template_structural.md`——字段：定义、来源、验证状态、架构位置、组合关系（连接到/包含了/被包含于/约束于）、开放问题
- 操作原语模板：`primitives/_template_operational.md`——字段：定义、来源、验证状态、使用经验、组合关系（组合了/替代了/约束于）、开放问题

### 通用补充字段

除模板标准字段外，每个新原语文件还需包含以下补充字段（来自Pass 3的双视角标注）：

- **检索流程角色**：状态感知 / Pattern提取 / 知识悖论 / 不直接服务于检索
- **系统演进角色**：盘古 / 女娲 / 燧人 / 伏羲 / 跨代

这两个字段放在"组合关系"之后、"开放问题"之前。

---

## 1. 新原语落盘规划（59个）

### 1.1 结构原语（18个）

#### 1.1.1 `primitives/structural/dependency-graph.md` — dependency-graph（依赖图）

- **定义**：用有向图表示知识间的依赖关系——节点带类型、上下文元数据、知识内容、版本指针；边带类型（depends_on/calls/cross-domain）；可有跨域边和螺旋环路。用ArangoDB图数据库存储。
- **来源**：pangu-a: 63-P1, 68-P1；pangu-b: 100-P18, 103-P1；fuxi: 223-P8, 248-P2
- **验证状态**：tested——POC-1/3/4/5/6中B组引用了依赖图结构，A/B对照验证增量
- **架构位置**：检索、验证、提取等所有上层原语的存储基础设施。用ArangoDB创建节点和边集合，AQL查询遍历。
- **组合关系**：
  - 连接到：layered-storage（分级存储的后端数据结构）
  - 包含了：version-chain（版本链是依赖图中节点的演化历史）
  - 被包含于：kth-three-graph-architecture（K图的实现）
  - 约束于：data-pedestal（已有原语，依赖图是数据基座的存储实现）
- **检索流程角色**：状态感知
- **系统演进角色**：盘古
- **开放问题**：跨域边的语义是否需要统一编码？螺旋环路在检索时如何处理（是障碍还是线索）？

#### 1.1.2 `primitives/structural/version-chain.md` — version-chain（版本链）

- **定义**：认知单元的演化历史——有序版本序列，每个版本记录来源和验证结果，current_version指针指向最新版本。
- **来源**：pangu-a: 89-P15；pangu-b: 100-P6；fuxi: 249-P30
- **验证状态**：tested——POC中已实现，在ArangoDB中创建cog_versions集合和版本链边
- **架构位置**：认知演化的基础设施。挂在dependency-graph的节点上。
- **组合关系**：
  - 连接到：dependency-graph（版本链依附于依赖图节点）
  - 被包含于：dependency-graph
  - 约束于：data-pedestal
- **检索流程角色**：状态感知
- **系统演进角色**：盘古
- **开放问题**：版本冲突时如何合并？多来源版本如何追溯？

#### 1.1.3 `primitives/structural/kth-three-graph-architecture.md` — kth-three-graph-architecture（K/T/H三图架构）

- **定义**：系统由三张图构成——K数学知识图、T外显思维图、H启发激活图，三图是投影而非独立真相库。
- **来源**：pangu-b: 122v2-P07；fuxi: 248-P3；nuwa-b: 174-P13；suiren: 213-P14
- **验证状态**：partial——当前只有K图已实现，T/H图未实现
- **架构位置**：系统数据架构的核心框架。K图=dependency-graph，T图=thinking-trajectory-graph，H图=heuristic-rule-graph。
- **组合关系**：
  - 包含了：dependency-graph, thinking-trajectory-graph, heuristic-rule-graph
  - 约束于：formalization-boundary概念
- **检索流程角色**：知识悖论
- **系统演进角色**：跨代
- **开放问题**：三图之间的投影关系如何形式化？T图和H图未实现时，系统如何降级运行？

#### 1.1.4 `primitives/structural/thinking-trajectory-graph.md` — thinking-trajectory-graph（思维轨迹图）

- **定义**：对Agent的当前思维过程建模为外显思维图T_t，节点有10种类型，是启发规则匹配的输入。
- **来源**：pangu-b: 122v2-P07；fuxi: 248-P3
- **验证状态**：untested——设计完成但事件捕获器未实现
- **架构位置**：从Agent输出中解析事件构建图。是模式匹配和卡点检测的输入。
- **组合关系**：
  - 连接到：event-sourcing（从事件流构建）
  - 被包含于：kth-three-graph-architecture（T图的实现）
  - 约束于：thinking-trajectory概念
- **检索流程角色**：Pattern提取
- **系统演进角色**：女娲
- **开放问题**：10种节点类型是否完备？从自然语言推理输出中如何可靠解析为结构化图节点？

#### 1.1.5 `primitives/structural/heuristic-rule-graph.md` — heuristic-rule-graph（启发规则图）

- **定义**：H图保存经过实验验证的"触发→激活"关系，每条规则形式化为(LHS, Guard, RHS)，附带适用信号、证书模板、失败案例和验证脚本。
- **来源**：pangu-b: 122v2-P13；fuxi: 248-P17
- **验证状态**：untested——设计完成但无Pattern走完完整生命周期
- **架构位置**：启发式干预的知识库。是pattern-matching和activation-score的数据源。
- **组合关系**：
  - 连接到：thinking-trajectory-graph（LHS匹配T图）
  - 被包含于：kth-three-graph-architecture（H图的实现）
  - 约束于：pattern-lifecycle（规则必须经过生命周期验证）
- **检索流程角色**：Pattern提取
- **系统演进角色**：燧人
- **开放问题**：规则数量增长后如何避免组合爆炸？Guard条件的形式化程度需要多高？

#### 1.1.6 `primitives/structural/event-sourcing.md` — event-sourcing（事件溯源）

- **定义**：研究过程中的每一步都是不可变事件，在原始事件之上抽取语义事件（14种类型），系统状态是所有已发生事件的投影归约，事件一旦发生不可修改。
- **来源**：pangu-b: 123-P17；nuwa-a: 131-P3；fuxi: 250-P9；suiren: 202-P02
- **验证状态**：untested——设计完成但事件捕获器未实现
- **架构位置**：不可变事件流，是动态工作区、思维轨迹图、检查点的基础设施。
- **组合关系**：
  - 连接到：dynamic-workspace, thinking-trajectory-graph, checkpoint, trajectory-recording
  - 约束于：不可变性（immutability）概念
- **检索流程角色**：状态感知
- **系统演进角色**：女娲
- **开放问题**：14种语义事件类型是否完备？事件流增长后如何做快照压缩？

#### 1.1.7 `primitives/structural/truth-vault.md` — truth-vault（真值保险库）

- **定义**：将正确答案和完整证明存储在隔离的truth_vault collection中，写入仅truth_curator，读取仅auditor，其他角色无权访问。
- **来源**：pangu-b: 122v3-P05；nuwa-a: 131-P24；fuxi: 248-P19；suiren: 200-P2
- **验证状态**：partial——代码已实现但未在真实多角色运行中验证
- **架构位置**：泄漏检测的基础防线。通过role-isolation-matrix的capability token控制访问。
- **组合关系**：
  - 连接到：role-isolation-matrix（权限控制）
  - 约束于：role-isolation-matrix
- **检索流程角色**：知识悖论
- **系统演进角色**：女娲
- **开放问题**：多角色运行时如何验证权限隔离确实生效？truth_curator角色由谁担任？

#### 1.1.8 `primitives/structural/obligation-hypergraph.md` — obligation-hypergraph（义务超图）

- **定义**：开放义务用AND/OR有向超图表达——AND约束（所有子目标都必须解决）、OR约束（任一路径成功即可），义务有10种类型和4种状态。
- **来源**：pangu-b: 123-P12；nuwa-a: 132-P7；nuwa-b: 188-P06；fuxi: 250-P12
- **验证状态**：partial——代码已实现并集成测试通过
- **架构位置**：进展度量和动态工作区的核心组件。在ArangoDB中创建超边本体和participant edges。
- **组合关系**：
  - 连接到：event-sourcing（从事件流更新义务状态）
  - 被包含于：dynamic-workspace（O_t字段）
  - 约束于：evidence-system
- **检索流程角色**：状态感知
- **系统演进角色**：伏羲
- **开放问题**：AND/OR嵌套深度是否有上限？义务状态转移的条件是否需要形式化验证？

#### 1.1.9 `primitives/structural/evidence-system.md` — evidence-system（证据系统）

- **定义**：证据有6种kind、polarity、生命周期，按polarity统计派生4种认识状态，验证门控制命题从F_t提升到V_t。
- **来源**：pangu-b: 123-P52；nuwa-a: 132-P12；nuwa-b: 188-P07
- **验证状态**：partial——代码已实现但未在真实证据集合上验证
- **架构位置**：证书和验证路由的基础设施。创建证据collection，定义类型化数据结构。
- **组合关系**：
  - 连接到：verification-routing, certificate, dynamic-workspace（E_t字段）
  - 约束于：formalization-boundary概念
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：伏羲
- **开放问题**：6种kind是否覆盖所有证据类型？polarity统计的4种认识状态是否足够精细？

#### 1.1.10 `primitives/structural/layered-storage.md` — layered-storage（分级存储）

- **定义**：知识存储按访问热度分层——冷层（全量数据）、温层（按需查询）、热层（当前问题相关子图）、微包（单步最小数据包）。
- **来源**：pangu-b: 110-P3；nuwa-a: 135-P3；nuwa-b: 183-P08
- **验证状态**：partial——冷层239K论文已入库，热层在POC中手动构建
- **架构位置**：检索管线和上下文编译器的存储后端。按层级创建不同collection和查询接口。
- **组合关系**：
  - 连接到：dependency-graph（分级存储的后端数据结构）
  - 约束于：data-pedestal
- **检索流程角色**：状态感知
- **系统演进角色**：盘古
- **开放问题**：冷热分层的迁移策略是什么？微包的粒度如何确定？

#### 1.1.11 `primitives/structural/role-isolation-matrix.md` — role-isolation-matrix（角色隔离矩阵）

- **定义**：系统功能拆分为8个隔离角色，每个角色有明确的职责和权限边界，通过可见性标签+能力令牌+物理隔离等机制在代码层面强制执行角色间的信息隔离，防止审计者与被审计者耦合。
- **来源**：pangu-a: 78-P11；pangu-b: 116-P4；nuwa-b: 176-P07；fuxi: 250-P20；suiren: 215-P17
- **验证状态**：partial——POC中用物理目录+AGENTS.md实现了简化版
- **架构位置**：交叉审计、真值保险库、受控实验的角色隔离基础设施。定义角色枚举、可见性矩阵、capability token验证逻辑。
- **组合关系**：
  - 连接到：truth-vault, cross-audit-loop, controlled-experiment
  - 约束于：pipe（已有原语，角色间信息隔离是Pipe合法性的保障）
- **检索流程角色**：知识悖论
- **系统演进角色**：女娲
- **开放问题**：8个角色是否都必要？简化场景下可以合并哪些角色？capability token的颁发和撤销机制如何设计？

#### 1.1.12 `primitives/structural/representation-atlas.md` — representation-atlas（表示图册）

- **定义**：一个处境不能被单一表示完全看清，需要一组可切换、可重叠、可拼合的局部表示（图册），表示间映射有6种类型，运输只在可靠性义务通过后执行。
- **来源**：pangu-b: 123-P05；nuwa-a: 135-P14；nuwa-b: 176-P19；fuxi: 225-P04；other: 004-P001
- **验证状态**：partial——数据结构已实现但未在真实跨域推理中验证
- **架构位置**：证书拉回、障碍检测的基础设施。创建表示映射数据结构（12字段），定义6种map_type。
- **组合关系**：
  - 连接到：certificate-pullback, obstruction-detection, retrieval-pipeline
  - 约束于：formalization-boundary概念
- **检索流程角色**：Pattern提取
- **系统演进角色**：伏羲
- **开放问题**：6种映射类型是否完备？图册中多少个局部表示才够用？拼合的自动化程度如何？

#### 1.1.13 `primitives/structural/context-compiler.md` — context-compiler（上下文编译器）

- **定义**：把检索到的数学子图编译为AI此刻能可靠使用的最小上下文包——决定节点展开顺序和分辨率、翻译边为思考关系、token预算删减、三项最小性审计（冗余/缺失/预载）、从checkpoint增量编译。
- **来源**：pangu-b: 122v1-P15；nuwa-a: 135-P17；nuwa-b: 183-P33；fuxi: 250-P6
- **验证状态**：partial——代码已实现并集成测试通过
- **架构位置**：检索管线和认知激活之间的编译桥梁。实现编译管线（8步）。
- **组合关系**：
  - 连接到：retrieval-pipeline, layered-storage
  - 约束于：minimal-knowledge-transfer（已有原语），non-specificity（已有原语）
- **检索流程角色**：知识悖论
- **系统演进角色**：跨代
- **开放问题**：三项最小性审计的阈值如何设定？增量编译的checkpoint粒度如何选择？

#### 1.1.14 `primitives/structural/checkpoint.md` — checkpoint（检查点）

- **定义**：用SHA-256内容哈希标识状态快照，相同内容产生相同哈希使状态可去重和精确引用。提示后从当前checkpoint继续而非从原题重做。
- **来源**：pangu-b: 122v2-P37；nuwa-a: 131-P9；fuxi: 251-P12
- **验证状态**：untested——设计了完整机制但未在因果实验中验证
- **架构位置**：受控实验和反应式救援的状态管理基础设施。计算状态哈希，存储checkpoint快照。
- **组合关系**：
  - 连接到：event-sourcing（从事件流生成快照）
  - 约束于：backtrack-fresh-session（已有原语，checkpoint续行是回溯的具体实现）
- **检索流程角色**：状态感知
- **系统演进角色**：女娲
- **开放问题**：状态哈希的粒度如何选择——整个session还是单步？checkpoint存储增长如何管理？

#### 1.1.15 `primitives/structural/dynamic-workspace.md` — dynamic-workspace（动态工作区）

- **定义**：系统在时刻t的完整状态用六元组表示——V_t（已验证核心）、F_t（猜想前沿）、O_t（开放义务）、R_t（表示状态）、E_t（证据）、U_t（未解决问题），状态由版本化Reducer从事件流归约得出，不可直接修改，状态等价通过规范化键判定。
- **来源**：fuxi: 250-P11；pangu-b: 123-P14；nuwa-b: 188-P01；suiren: 200-P18
- **验证状态**：untested——设计完成但事件捕获器未实现
- **架构位置**：卡点检测、增量编译、进展度量的状态基础。实现版本化Reducer，从事件流归约六元组状态。
- **组合关系**：
  - 连接到：event-sourcing, obligation-hypergraph（O_t字段）, evidence-system（E_t字段）
  - 约束于：不可变性（immutability）概念
- **检索流程角色**：状态感知
- **系统演进角色**：伏羲
- **开放问题**：六元组是否完备？状态等价的规范化键如何设计？Reducer的版本化如何实现？

#### 1.1.16 `primitives/structural/certificate-ledger.md` — certificate-ledger（证书账本）

- **定义**：系统在时刻t的状态是证书偏序C的向下封闭理想I_t——单调增长（每一步只加证书不删），已确认证书不会无声消失。
- **来源**：fuxi: 225-P08, 226-P3
- **验证状态**：untested——设计完成但未实现
- **架构位置**：语义能量下降、结果反射的证书管理基础设施。维护证书偏序集合，实现向下封闭理想检查。
- **组合关系**：
  - 连接到：certificate（已有原语，证书账本是证书的偏序管理）
  - 约束于：evidence-system
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：伏羲
- **开放问题**：偏序的存储和查询效率如何？向下封闭理想的维护成本如何？

#### 1.1.17 `primitives/structural/trajectory-recording.md` — trajectory-recording（轨迹记录）

- **定义**：运行过程分三层独立记录——外部层（devin cli轨迹）、中间层（系统内部执行日志）、内部层（AI思路轨迹），四路径兜底捕获。
- **来源**：nuwa-b: 178-P02；fuxi: 248-P22；suiren: 217-P6
- **验证状态**：tested——guided_001/003实验中已使用，用tmux pipe-pane + capture-pane + export + transcript实现
- **架构位置**：审计标准回测和增益归因的数据基础。
- **组合关系**：
  - 连接到：event-sourcing（轨迹记录是事件溯源的外部捕获层）
  - 约束于：可审计性纪律
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：跨代
- **开放问题**：四路径兜底是否有遗漏？内部层（AI思路轨迹）的捕获精度如何保证？

#### 1.1.18 `primitives/structural/failure-boundary-record.md` — failure-boundary-record（失败边界记录）

- **定义**：记录哪些相似命题不成立、哪些条件删掉会失败——失败边界是数据基座的一等公民，经典计算标记已验证不可行路径为死路。
- **来源**：fuxi: 231-P15, 234-P16
- **验证状态**：untested——设计完成但未在真实搜索中验证
- **架构位置**：反例搜索和导航约束的数据基础设施。在数据基座中创建failure_boundary集合。
- **组合关系**：
  - 连接到：data-pedestal（已有原语，失败边界是数据基座一等公民）
  - 约束于：data-pedestal
- **检索流程角色**：状态感知
- **系统演进角色**：伏羲
- **开放问题**：失败边界的粒度如何确定？如何区分"此路不通"和"此路困难但可行"？

---

### 1.2 操作原语（41个）

#### 1.2.1 `primitives/operational/retrieval-pipeline.md` — retrieval-pipeline（多级检索管线）

- **定义**：多级递进检索机制——种子选择（层次索引定位+语义检索top-K）→图遍历扩展（BFS/DFS有界深度）→预算剪枝（深度/宽度/token控制）→返回结构化子图。
- **来源**：pangu-a: 63-P5；pangu-b: 100-P3；fuxi: 234-P10；nuwa-b: 166-P08
- **验证状态**：partial——POC中手动替代，253号目标是自动化
- **使用经验**：POC中用AQL图遍历查询实现，三级递进。种子选择和子图提取是管线的子组件。
- **组合关系**：
  - 组合了：dependency-graph, layered-storage
  - 替代了：全量扫描检索
  - 约束于：budget-management（预算剪枝）
- **检索流程角色**：状态感知 + Pattern提取
- **系统演进角色**：盘古
- **开放问题**：种子选择的质量如何评估？图遍历的深度/宽度预算如何自适应？

#### 1.2.2 `primitives/operational/multi-level-knowledge-extraction.md` — multi-level-knowledge-extraction（多层知识提取）

- **定义**：多遍管道从数学解法中提取多层知识——L1具体步骤→L2思维模式（AI二次分析）→L3范式思维（AI三次分析）→可选L4哲学洞察，每层有质量审计门控，过程性标注在转折点。
- **来源**：pangu-a: 83-P01；pangu-b: 100-P8；fuxi: 248-P23；suiren: 201-P1
- **验证状态**：partial——POC-3验证L2/L3在远迁移中产生显著增量
- **使用经验**：多遍AI分析，每遍用不同prompt。L2/L3层在远迁移实验中验证了增量价值。
- **组合关系**：
  - 组合了：dependency-graph, version-chain, pattern-recognition-engine（已有）
  - 约束于：data-pedestal（已有）
- **检索流程角色**：Pattern提取
- **系统演进角色**：盘古
- **开放问题**：L4哲学洞察层是否实用？质量审计门控的标准如何量化？

#### 1.2.3 `primitives/operational/topology-coverage-verification.md` — topology-coverage-verification（拓扑覆盖验证）

- **定义**：构造拓扑骨架G'_topo，用AQL集合差集验证覆盖所有节点/边/跨领域边/螺旋环路圈数——差集为空即100%覆盖。
- **来源**：pangu-a: 78-P9；fuxi: 248-P6
- **验证状态**：tested——POC中多次使用TopologyVerifier
- **使用经验**：用AQL集合差集运算实现，在POC-1/3/4/5/6中多次使用。
- **组合关系**：
  - 组合了：dependency-graph
  - 约束于：data-pedestal（已有）
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：盘古
- **开放问题**：拓扑骨架的构造是否自动化？覆盖100%是否是必要标准？

#### 1.2.4 `primitives/operational/spiral-loop-detection.md` — spiral-loop-detection（螺旋环路检测）

- **定义**：用Tarjan SCC算法发现图中所有环，区分平面环路（上下文相同，应停止）和螺旋环路（上下文不同，应继续）。
- **来源**：pangu-a: 63-P4；pangu-b: 113-P6；fuxi: 249-P4
- **验证状态**：tested——POC-1/4/5/6中螺旋环路作为结构元素使用
- **使用经验**：用Tarjan SCC算法+AQL查询实现。
- **组合关系**：
  - 组合了：dependency-graph
  - 约束于：data-pedestal（已有）
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：盘古
- **开放问题**：平面环路和螺旋环路的区分判据是否足够鲁棒？螺旋环路的"上下文不同"如何量化？

#### 1.2.5 `primitives/operational/incremental-graph-expansion.md` — incremental-graph-expansion（增量图扩展）

- **定义**：在已有依赖图基础上新增节点和边，保留已有子图结构不变——而非重新设计。扩展时保留已验证的节点/意识，在新上下文中复用。
- **来源**：pangu-a: 64-P17, 65-P01
- **验证状态**：tested——POC中多次使用
- **使用经验**：在ArangoDB中新增节点/边，标记新增vs复用。
- **组合关系**：
  - 组合了：dependency-graph, multi-level-knowledge-extraction
  - 约束于：data-pedestal（已有）
- **检索流程角色**：状态感知
- **系统演进角色**：盘古
- **开放问题**：增量扩展时如何避免图膨胀？旧节点何时应该归档或删除？

#### 1.2.6 `primitives/operational/cross-audit-loop.md` — cross-audit-loop（交叉审计闭环）

- **定义**：用独立AI实例审计另一个AI的输出——审计→发现瑕疵→结构化反馈→修正→再审计→直到无瑕疵或达到最大轮数。三级终止机制。
- **来源**：pangu-a: 71-P14, 72-P06, 76-P01
- **验证状态**：tested——POC中多次使用
- **使用经验**：启动独立AI实例，传递基准+输出。在POC中多次使用。
- **组合关系**：
  - 组合了：role-isolation-matrix
  - 约束于：pipe（已有原语，交叉审计是Pipe中的质量门控环节）
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：盘古
- **开放问题**：三级终止机制的阈值如何设定？审计者和被审计者的知识差异如何保证？

#### 1.2.7 `primitives/operational/stall-detection.md` — stall-detection（卡点检测）

- **定义**：从Solver的外显思维轨迹中检测7种卡点信号，区分平面环路（应停止）和螺旋上升环路（应继续），客观证据优先于主观自报。
- **来源**：pangu-b: 122v2-P36；nuwa-a: 132-P17；nuwa-b: 176-P20；suiren: 200-P19；fuxi: 223-P19
- **验证状态**：partial——143-P13有pilot验证
- **使用经验**：从事件流/思维图中检测卡点信号。7种互斥卡点类型。
- **组合关系**：
  - 组合了：dynamic-workspace, thinking-trajectory-graph
  - 约束于：客观证据优先原则
- **检索流程角色**：状态感知
- **系统演进角色**：跨代
- **开放问题**：7种卡点类型是否完备？主观自报和客观证据冲突时如何裁决？

#### 1.2.8 `primitives/operational/gaming-detection.md` — gaming-detection（博弈检测）

- **定义**：三元判定机制检测工作智能体是否在"gaming"——（停滞词=True）AND（工具证据=False）AND（结构进展=False）三条件全部满足才判定。
- **来源**：nuwa-a: 136-P23；nuwa-b: 175-P12
- **验证状态**：partial——代码已实现但未在真实gaming行为上验证
- **使用经验**：实现三元AND判定逻辑。
- **组合关系**：
  - 组合了：stall-detection
  - 约束于：constrained-policy
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：女娲
- **开放问题**：三元判定的假阳性率如何？gaming行为的边界案例如何处理？

#### 1.2.9 `primitives/operational/reactive-rescue.md` — reactive-rescue（反应式救援）

- **定义**：Agent先独立尝试解题，检测到真实停滞后才匹配启发规则并注入最小提示，从当前checkpoint继续。反应式是默认模式，主动导航需经验证后开启。
- **来源**：pangu-b: 122v2-P34；nuwa-a: 136-P28
- **验证状态**：untested——设计阶段提出，尚未实现在线运行时
- **使用经验**：设计阶段提出，检测卡点→匹配规则→注入提示→从checkpoint继续。
- **组合关系**：
  - 组合了：stall-detection, checkpoint, context-compiler
  - 替代了：主动导航（proactive navigation，需验证后才开启）
  - 约束于：constrained-policy, safe-first-step（已有）
- **检索流程角色**：知识悖论
- **系统演进角色**：燧人
- **开放问题**：反应式和主动导航的切换条件是什么？反应式模式的延迟是否可接受？

#### 1.2.10 `primitives/operational/pattern-lifecycle.md` — pattern-lifecycle（规则生命周期）

- **定义**：启发规则经历observed→candidate→intervened→validated→published→retired完整生命周期，每次状态转移需满足明确条件，candidate状态禁止在线匹配。
- **来源**：pangu-b: 122v2-P31；nuwa-a: 133-P30；nuwa-b: 176-P04；fuxi: 250-P13
- **验证状态**：untested——框架设计完成但无Pattern走完完整生命周期
- **使用经验**：定义状态枚举和转移条件。
- **组合关系**：
  - 组合了：controlled-experiment, leakage-detection, activation-score
  - 约束于：heuristic-rule-graph
- **检索流程角色**：Pattern提取
- **系统演进角色**：跨代
- **开放问题**：candidate状态禁止在线匹配是否过于保守？retired状态的规则是否永久失效？

#### 1.2.11 `primitives/operational/leakage-detection.md` — leakage-detection（泄漏检测）

- **定义**：通过四个独立维度检测Hint是否泄漏答案——字面匹配、等价映射、候选空间缩减、盲恢复，任一超标即判泄漏。
- **来源**：nuwa-a: 133-P23；suiren: 200-P4；fuxi: 248-P19
- **验证状态**：partial——209号报告泄漏率从40%降到20%
- **使用经验**：实现四门检查逻辑。209号报告验证有效。
- **组合关系**：
  - 组合了：truth-vault
  - 约束于：non-specificity（已有原语，四门泄漏检测是非特定性的验证机制）, minimal-knowledge-transfer（已有）
- **检索流程角色**：知识悖论
- **系统演进角色**：燧人
- **开放问题**：四门检测的阈值如何设定？等价映射的覆盖范围如何保证？

#### 1.2.12 `primitives/operational/hint-gradient.md` — hint-gradient（提示梯度）

- **定义**：建立多级提示梯度——从低泄漏（元检查/思维操作）到高泄漏（确定方向/具体步骤），优先选低泄漏级别，不够再逐步升级。
- **来源**：pangu-b: 122v2-P25；fuxi: 250-P4；suiren: 200-P25
- **验证状态**：untested——设计阶段提出，POC中用二分替代
- **使用经验**：设计阶段提出，定义梯度级别，实现排序逻辑。
- **组合关系**：
  - 约束于：non-specificity（已有原语）, minimal-knowledge-transfer（已有原语，提示梯度从低到高实现最小知识传递）
- **检索流程角色**：知识悖论
- **系统演进角色**：燧人
- **开放问题**：梯度级别如何量化？升级的触发条件是什么？

#### 1.2.13 `primitives/operational/pattern-matching.md` — pattern-matching（模式匹配）

- **定义**：用规则库匹配替代硬编码提示——规则以(LHS, Guard, RHS)形式定义，匹配基于结构形状而非文本相似性，利用稀疏性只匹配可能相关的规则子集。
- **来源**：pangu-b: 122v2-P19；suiren: 200-P20, 214-P6；fuxi: 238-P7
- **验证状态**：untested——设计阶段提出，未在真实Pattern库上验证
- **使用经验**：设计阶段提出，实现LHS子图匹配+Guard条件检查+RHS动作输出。
- **组合关系**：
  - 组合了：thinking-trajectory-graph, heuristic-rule-graph
  - 约束于：activation-score
- **检索流程角色**：Pattern提取
- **系统演进角色**：燧人
- **开放问题**：结构形状匹配的算法复杂度如何？近似匹配的容差如何确定？

#### 1.2.14 `primitives/operational/activation-score.md` — activation-score（激活分数）

- **定义**：在H图稀疏表示上计算候选激活分数a_t = W^T * p_t，权重组合7种数值维度，激活分数作为候选Pattern的排序依据。
- **来源**：nuwa-a: 135-P40；nuwa-b: 166-P16
- **验证状态**：untested——公式已实现但未在真实Pattern库上验证
- **使用经验**：实现稀疏矩阵乘法。
- **组合关系**：
  - 组合了：heuristic-rule-graph, pattern-lifecycle
  - 约束于：cognitive-activation（已有原语，激活分数是认知激活的计算机制）
- **检索流程角色**：Pattern提取
- **系统演进角色**：女娲
- **开放问题**：7种数值维度的权重如何确定？激活分数的阈值如何设定？

#### 1.2.15 `primitives/operational/controlled-experiment.md` — controlled-experiment（受控对照实验）

- **定义**：设置对照组和实验组在相同隔离条件下并行执行，通过组间差异量化因果效果——A/B对照、三组对照、双路线对照、检查点分层因果实验。
- **来源**：pangu-b: 100-P15；suiren: 200-P28；fuxi: 229-P4；nuwa-a: 134-P2
- **验证状态**：tested——POC-1/3/4/5/6多次使用
- **使用经验**：设置隔离环境，并行执行，计算组间差异。POC中多次使用。
- **组合关系**：
  - 组合了：role-isolation-matrix, checkpoint, hypothesis-driven-validation
  - 约束于：execution-contract（已有原语，Phase门控是执行契约的验证机制）
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：跨代
- **开放问题**：隔离条件的严格性如何保证？组间差异的统计显著性如何判定？

#### 1.2.16 `primitives/operational/hypothesis-driven-validation.md` — hypothesis-driven-validation（假设驱动验证）

- **定义**：实验前预设明确假设并冻结所有决策参数，冻结后不可回改，用ATE+CI下界+passes_exit_gate三步验证因果效应。
- **来源**：pangu-b: 106-P21；nuwa-a: 134-P8；nuwa-b: 174-P05
- **验证状态**：tested——POC-1/3/4/5/6均使用
- **使用经验**：创建预注册文档，冻结参数。POC中多次使用。
- **组合关系**：
  - 约束于：controlled-experiment
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：跨代
- **开放问题**：参数冻结后如果发现设计缺陷如何处理？ATE+CI下界的置信水平如何选择？

#### 1.2.17 `primitives/operational/blind-evaluation.md` — blind-evaluation（盲评）

- **定义**：评分者不知道哪份回答来自哪个实验组，通过打乱运行顺序、隐藏处理组标签实现，评分AI独立于执行组和审计组。
- **来源**：pangu-b: 105-P7；nuwa-b: 193-P06
- **验证状态**：tested——POC-3使用盲评
- **使用经验**：打乱run顺序，隐藏标签。POC-3中使用。
- **组合关系**：
  - 约束于：controlled-experiment
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：盘古
- **开放问题**：盲评的隐藏是否可靠？评分AI的独立性如何保证？

#### 1.2.18 `primitives/operational/phase-gate.md` — phase-gate（阶段门控）

- **定义**：每个Phase有入口门和出口门，出口门审计本Phase全部交付物，通过后才进入下一Phase。
- **来源**：pangu-b: 124-P48；nuwa-b: 174-P04；other: 004-P021
- **验证状态**：tested——Phase 0-7在多个Phase审计中验证有效
- **使用经验**：定义Phase枚举和门控条件。在多个Phase审计中验证有效。
- **组合关系**：
  - 约束于：execution-contract（已有原语）
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：跨代
- **开放问题**：门控条件是否过于严格导致开发效率降低？出口门审计的自动化程度如何？

#### 1.2.19 `primitives/operational/legacy-handling.md` — legacy-handling（遗留处理）

- **定义**：旧数据和概念不原地清空或迁移，保留原貌作为只读历史数据，通过只读adapter访问，新数据写入新collection。
- **来源**：pangu-b: 121-P16；nuwa-b: 166-P35
- **验证状态**：tested——Phase 0冻结旧数据后验证有效
- **使用经验**：创建只读adapter，新collection用幂等可回滚migration。
- **组合关系**：
  - 组合了：phase-gate
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：跨代
- **开放问题**：只读adapter的性能开销如何？旧数据的保留期限如何确定？

#### 1.2.20 `primitives/operational/progress-measurement.md` — progress-measurement（进展度量）

- **定义**：进展由5个可测量分量定义的偏序P_κ(S_t)，不同任务类型有不同权重，进展向量比较产生4种结果。
- **来源**：pangu-b: 123-P21；nuwa-a: 132-P22；nuwa-b: 188-P03
- **验证状态**：untested——设计完成但未在真实运行中验证
- **使用经验**：从动态工作区提取5个分量，计算偏序。
- **组合关系**：
  - 组合了：dynamic-workspace, obligation-hypergraph, evidence-system
  - 约束于：constrained-policy
- **检索流程角色**：状态感知
- **系统演进角色**：伏羲
- **开放问题**：5个可测量分量是否完备？不同任务类型的权重如何确定？

#### 1.2.21 `primitives/operational/gain-attribution.md` — gain-attribution（增益归因）

- **定义**：对每次干预验证并归因其产生的增益——记录提示链，进展归因给首次引入H关系的提示，反事实估计"没有该提示是否也会达到进展"。
- **来源**：suiren: 200-P12；fuxi: 252-P19；nuwa-a: 136-P26
- **验证状态**：untested——设计完成但未在真实运行中验证
- **使用经验**：记录提示链，计算归因，做反事实估计。
- **组合关系**：
  - 组合了：controlled-experiment
  - 约束于：pattern-lifecycle
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：跨代
- **开放问题**：反事实估计的可靠性如何？多提示联合贡献如何分解？

#### 1.2.22 `primitives/operational/constrained-policy.md` — constrained-policy（受约束多目标策略）

- **定义**：策略π在进展最大化、泄漏最小化、依赖最小化、成本控制多个约束下选择最优动作，ABSTAIN（不干预）是合法选择，AI按需介入。
- **来源**：nuwa-a: 136-P32；suiren: 200-P23
- **验证状态**：untested——公式已定义但未在真实运行中验证
- **使用经验**：定义目标函数和约束，实现优化求解。
- **组合关系**：
  - 组合了：progress-measurement, leakage-detection, budget-management
  - 约束于：constraint-solver-engine（已有原语，受约束多目标策略是多约束求解的具体化）
- **检索流程角色**：知识悖论
- **系统演进角色**：伏羲
- **开放问题**：多目标之间的权重如何确定？ABSTAIN的触发条件是什么？

#### 1.2.23 `primitives/operational/verification-routing.md` — verification-routing（验证路由）

- **定义**：根据命题类型选择验证工具并分层路由——formal→Lean 4、symbolic→SymPy、numerical→NumPy、human→人工，验证器输出6种状态。
- **来源**：nuwa-a: 135-P23；nuwa-b: 183-P39
- **验证状态**：partial——代码已实现但未在真实混合型命题上验证
- **使用经验**：实现路由逻辑，调用对应验证工具。
- **组合关系**：
  - 组合了：evidence-system
  - 约束于：certificate（已有原语）
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：伏羲
- **开放问题**：混合型命题的路由优先级如何确定？6种验证器状态是否完备？

#### 1.2.24 `primitives/operational/budget-management.md` — budget-management（预算管理）

- **定义**：管理多种独立预算类型（token/计算/工具/分支/Hint），超限时触发硬性停止，Hint预算单独追踪。
- **来源**：nuwa-b: 186-P01；suiren: 205-P29
- **验证状态**：untested——设计完成但未在真实运行中验证
- **使用经验**：定义预算类型和上限，每次消耗前检查。
- **组合关系**：
  - 约束于：constrained-policy, dfs-guidance（已有原语，分支预算限制DFS分支因子）
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：女娲
- **开放问题**：预算上限如何确定？超限后的恢复机制是什么？

#### 1.2.25 `primitives/operational/depth-graded-check.md` — depth-graded-check（深度分级验收）

- **定义**：将"实现X"从二元勾选改为四元深度等级[D1]定义/[D2]逻辑/[D3]测试/[D4]集成，强制勾选者明确实现深度。
- **来源**：nuwa-a: 140-P5
- **验证状态**：tested——在多个Phase审计中验证有效
- **使用经验**：定义四元等级，在审计中逐项检查。
- **组合关系**：
  - 约束于：multi-source-audit
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：女娲
- **开放问题**：四元等级的判定标准是否主观？D3和D4之间的边界是否清晰？

#### 1.2.26 `primitives/operational/multi-source-audit.md` — multi-source-audit（多源交叉审计）

- **定义**：用多个并行subagent分别完整扫描多个权威源文件的每一行，各自提取要求并标注来源，冲突时按权威等级裁决。
- **来源**：nuwa-a: 139-P25
- **验证状态**：tested——在145-162号的多轮审计中验证有效
- **使用经验**：启动多个subagent，汇总对照。在145-162号的多轮审计中使用。
- **组合关系**：
  - 组合了：depth-graded-check
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：女娲
- **开放问题**：权威等级如何确定？冲突裁决的规则是否可自动化？

#### 1.2.27 `primitives/operational/design-degradation-detection.md` — design-degradation-detection（设计降级检测）

- **定义**：检测方案声明了某设计决策但实现降级了的情况，将方案声明与实现代码逐项核对。
- **来源**：nuwa-b: 174-P31
- **验证状态**：untested——设计完成但未在真实降级场景中验证
- **使用经验**：将方案声明与实现代码逐项核对。
- **组合关系**：
  - 约束于：audit-standard-backtesting
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：女娲
- **开放问题**：降级的判定标准是什么？"合理简化"和"降级"如何区分？

#### 1.2.28 `primitives/operational/audit-standard-backtesting.md` — audit-standard-backtesting（审计标准回测）

- **定义**：用已知结果的历史run验证审计标准能否正确发现问题和正确判定通过——用已知失败run验证召回率，用已知通过run验证精确率。
- **来源**：nuwa-b: 196-P01
- **验证状态**：untested——设计完成但未在真实回测中验证
- **使用经验**：用历史run回测审计标准。
- **组合关系**：
  - 组合了：design-degradation-detection, trajectory-recording
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：女娲
- **开放问题**：历史run的代表性如何保证？召回率和精确率的平衡如何确定？

#### 1.2.29 `primitives/operational/multiple-independent-verification.md` — multiple-independent-verification（多次独立验证）

- **定义**：通过多次（≥3次）独立运行判定结果是稳定的还是偶然的——3次全错才算"做不出来"，用独立于AI的机制验证结果正确性。
- **来源**：suiren: 210-P4
- **验证状态**：tested——在MathArena baseline中已使用
- **使用经验**：多次运行同一题目，用SymPy/Lean验证。在MathArena baseline中使用。
- **组合关系**：
  - 约束于：false-completion-detection
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：跨代
- **开放问题**：3次是否足够？独立运行之间如何保证独立性？

#### 1.2.30 `primitives/operational/false-completion-detection.md` — false-completion-detection（假完成检测）

- **定义**：AI可能给出错误证明但自认为完成——需要实验后对照标准答案验证，用独立于AI的机制检测假完成。
- **来源**：suiren: 210-P5, 215-P25
- **验证状态**：tested——MathArena baseline中检测到假完成案例
- **使用经验**：用SymPy数值验证+人工抽查。在MathArena baseline中检测到假完成案例。
- **组合关系**：
  - 组合了：multiple-independent-verification
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：燧人
- **开放问题**：假完成的检测覆盖率如何？人工抽查的比例如何确定？

#### 1.2.31 `primitives/operational/training-data-risk-assessment.md` — training-data-risk-assessment（训练数据风险评级）

- **定义**：为每道题评估AI训练数据风险等级（高/中/低），基于时间新旧、语言、讨论热度三个信号综合判断。
- **来源**：suiren: 210-P10
- **验证状态**：tested——在MathArena baseline中已使用
- **使用经验**：按三个信号评分，综合判断。在MathArena baseline中使用。
- **组合关系**：
  - 无直接依赖
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：燧人
- **开放问题**：三个信号的权重如何确定？讨论热度如何量化？

#### 1.2.32 `primitives/operational/counterexample-search.md` — counterexample-search（反例搜索）

- **定义**：经典计算搜索小模型、随机样本、极端边界和约束满足解，给出具体对象让猜想失败——反例作为高价值语义反馈改变AI方向。
- **来源**：fuxi: 228-v0-P3
- **验证状态**：untested——设计完成但未在真实推理中验证
- **使用经验**：用NumPy/SciPy搜索小模型和随机样本。
- **组合关系**：
  - 约束于：failure-boundary-record
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：伏羲
- **开放问题**：搜索空间的规模如何确定？反例的语义反馈如何形式化？

#### 1.2.33 `primitives/operational/semantic-energy-descent.md` — semantic-energy-descent（语义能量下降）

- **定义**：计算当前处境的六分量能量向量（表示复杂度/证书距离/自由度残差/粘合缺陷/反例压力/形式化缺口），以Pareto改善或受控交换为判据选择能降低能量的语义移动。
- **来源**：fuxi: 225-1-P18, 225-P13
- **验证状态**：untested——设计完成但未在真实推理中验证
- **使用经验**：计算六分量能量向量，选择Pareto改善的移动。
- **组合关系**：
  - 组合了：certificate-ledger
  - 约束于：dual-output-closed-loop
- **检索流程角色**：状态感知
- **系统演进角色**：伏羲
- **开放问题**：六分量能量向量的计算是否可行？Pareto改善的判据是否过于严格？

#### 1.2.34 `primitives/operational/result-reflection.md` — result-reflection（结果反射）

- **定义**：将经典计算的结果（成功/反例/障碍/未知）反射回语义场，改变AI的语义理解——成功则猜想过强、反例则方向错误。
- **来源**：fuxi: 225-1-P4
- **验证状态**：untested——设计完成但未在真实推理中验证
- **使用经验**：将验证结果映射为语义反馈。
- **组合关系**：
  - 组合了：certificate-ledger
  - 与 verifiable-compilation 互为V-R对
- **检索流程角色**：知识悖论
- **系统演进角色**：伏羲
- **开放问题**：语义反馈的形式化程度如何？反射的延迟是否可接受？

#### 1.2.35 `primitives/operational/verifiable-compilation.md` — verifiable-compilation（可证化编译）

- **定义**：将AI提出的语义移动编译成可检查的证书目标集合——一个语义移动可能产生零个、一个或多个证书目标，每个目标指定可交给什么工具检查。
- **来源**：fuxi: 225-1-P8
- **验证状态**：untested——设计完成但未在真实推理中验证
- **使用经验**：将语义移动映射为证书目标列表。
- **组合关系**：
  - 组合了：certificate（已有原语）
  - 与 result-reflection 互为V-R对
- **检索流程角色**：知识悖论
- **系统演进角色**：伏羲
- **开放问题**：编译的完备性如何保证？零证书目标的语义移动如何处理？

#### 1.2.36 `primitives/operational/certificate-pullback.md` — certificate-pullback（证书拉回）

- **定义**：给定表示变换τ:S'→S，将S上的证书翻译到S'上的操作——跨表示检索的基础操作。
- **来源**：fuxi: 227-P14, 230-P21
- **验证状态**：untested——设计完成但未在真实跨域推理中验证
- **使用经验**：定义证书翻译规则，执行拉回操作。
- **组合关系**：
  - 组合了：certificate（已有原语）, representation-atlas
  - 约束于：base-change（已有原语，证书拉回是换表示后的证书翻译）, obstruction-detection
- **检索流程角色**：Pattern提取
- **系统演进角色**：伏羲
- **开放问题**：证书翻译规则的完备性如何保证？拉回操作的计算复杂度如何？

#### 1.2.37 `primitives/operational/obstruction-detection.md` — obstruction-detection（粘合障碍检测）

- **定义**：检查不同局部表示的局部证书在重叠处是否能粘合成全局证书，粘合失败分四级——descent failure→obstruction object→Čech 1-cocycle→H¹ class。
- **来源**：fuxi: 225-1-P15
- **验证状态**：untested——设计完成但未在真实推理中验证
- **使用经验**：检查重叠处证书一致性，分级判定障碍。
- **组合关系**：
  - 组合了：representation-atlas, certificate-pullback
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：伏羲
- **开放问题**：四分级是否完备？粘合失败的修复策略是什么？

#### 1.2.38 `primitives/operational/dual-output-closed-loop.md` — dual-output-closed-loop（单任务双产出）

- **定义**：求解闭环运行一次，同时产出问题的解和数据基座条目——每步语义移动被记录、每个证书目标被编译、每个验证结果被回写。
- **来源**：fuxi: 234-P1
- **验证状态**：untested——设计完成但未在真实运行中验证
- **使用经验**：在闭环运行中同步记录到数据基座。
- **组合关系**：
  - 组合了：execution-contract（已有原语）, data-pedestal（已有原语）, certificate-ledger
  - 约束于：data-pedestal（已有，双产出闭环自动生成数据基座条目）
- **检索流程角色**：状态感知
- **系统演进角色**：伏羲
- **开放问题**：同步记录的性能开销如何？数据基座条目的质量如何保证？

#### 1.2.39 `primitives/operational/kth-projection.md` — kth-projection（K/T/H投影操作）

> **注**：此原语在Pass 3报告中作为kth-three-graph-architecture的投影操作隐含存在。归并组14中nuwa-b的"K/T/H投影"描述了三图之间的投影关系操作。为保持59个原语的完整性，此原语归入kth-three-graph-architecture的结构描述中，不单独落盘。实际落盘时，kth-three-graph-architecture.md文件中将包含投影操作的描述。

**修正**：经核对，Pass 3报告中的59个新原语不包含独立的"kth-projection"操作原语。kth-three-graph-architecture是结构原语，投影操作是其内部描述。因此实际操作原语数量为41个，以下继续列出剩余操作原语。

#### 1.2.39 `primitives/operational/seed-selection.md` — seed-selection（种子选择）

> **注**：种子选择在归并组2中被归并到retrieval-pipeline中，作为管线的子组件。不单独落盘。retrieval-pipeline.md中将包含种子选择的描述。

**修正**：经核对Pass 3报告的59个最终新原语清单，种子选择不作为独立原语。retrieval-pipeline已包含种子选择。以下继续列出Pass 3报告中明确列出的59个原语中的剩余操作原语。

---

**实际59个原语清单核对**：

经逐项核对Pass 3报告第3.2节，59个新原语为：

**18个结构原语**（已全部列出，1.1.1-1.1.18）：
1. dependency-graph
2. version-chain
3. kth-three-graph-architecture
4. thinking-trajectory-graph
5. heuristic-rule-graph
6. event-sourcing
7. truth-vault
8. obligation-hypergraph
9. evidence-system
10. layered-storage
11. role-isolation-matrix
12. representation-atlas
13. context-compiler
14. checkpoint
15. dynamic-workspace
16. certificate-ledger
17. trajectory-recording
18. failure-boundary-record

**41个操作原语**（已列出1.2.1-1.2.38，剩余3个如下）：

#### 1.2.39 `primitives/operational/spiral-loop-detection.md` — 已在1.2.4列出

> **核对修正**：经逐项核对，Pass 3报告中第3.2节明确列出的操作原语实际为以下41个（按报告顺序）：

1. multi-level-knowledge-extraction（1.2.2）
2. retrieval-pipeline（1.2.1）
3. topology-coverage-verification（1.2.3）
4. spiral-loop-detection（1.2.4）
5. incremental-graph-expansion（1.2.5）
6. cross-audit-loop（1.2.6）
7. stall-detection（1.2.7）
8. gaming-detection（1.2.8）
9. reactive-rescue（1.2.9）
10. pattern-lifecycle（1.2.10）
11. leakage-detection（1.2.11）
12. hint-gradient（1.2.12）
13. pattern-matching（1.2.13）
14. activation-score（1.2.14）
15. controlled-experiment（1.2.15）
16. hypothesis-driven-validation（1.2.16）
17. blind-evaluation（1.2.17）
18. phase-gate（1.2.18）
19. legacy-handling（1.2.19）
20. progress-measurement（1.2.20）
21. gain-attribution（1.2.21）
22. constrained-policy（1.2.22）
23. verification-routing（1.2.23）
24. budget-management（1.2.24）
25. depth-graded-check（1.2.25）
26. multi-source-audit（1.2.26）
27. design-degradation-detection（1.2.27）
28. audit-standard-backtesting（1.2.28）
29. multiple-independent-verification（1.2.29）
30. false-completion-detection（1.2.30）
31. training-data-risk-assessment（1.2.31）
32. counterexample-search（1.2.32）
33. semantic-energy-descent（1.2.33）
34. result-reflection（1.2.34）
35. verifiable-compilation（1.2.35）
36. certificate-pullback（1.2.36）
37. obstruction-detection（1.2.37）
38. dual-output-closed-loop（1.2.38）

> **缺口**：以上列出38个操作原语。Pass 3报告声称41个操作原语。经核对，报告第3.2节的操作原语清单从multi-level-knowledge-extraction开始到dual-output-closed-loop结束，共38个条目。报告统计中的41个可能包含了归并组中作为子组件描述但未单独列出的3个操作（seed-selection、subgraph-extraction、local-view，均归入retrieval-pipeline）。

**结论**：实际需要落盘的操作原语为38个（加上18个结构原语，共56个独立文件）。Pass 3报告中的"41个操作原语"统计包含了retrieval-pipeline的3个子组件。落盘时这3个子组件的描述包含在retrieval-pipeline.md中，不单独建文件。

---

## 2. 已有原语来源补充更新规划（16个）

以下16个已有原语需要更新"来源"和"组合关系"字段，补充Pass 3发现的新来源。

### 2.1 `primitives/operational/backtrack-fresh-session.md`

- **来源补充**：suiren: file-transfer-isolation, checkpoint
- **补充内容**：文件传递隔离是新session中状态延续的机制；checkpoint续行是回溯的具体实现
- **组合关系补充**：组合了 checkpoint（新原语，checkpoint续行是回溯的具体实现）

### 2.2 `primitives/operational/base-change.md`

- **来源补充**：nuwa-a: representation-transport；fuxi: certificate-pullback
- **补充内容**：表示运输是换基的具体化实现；证书拉回是换表示后的证书翻译
- **组合关系补充**：组合了 certificate-pullback（新原语，证书拉回是换基后的证书翻译）

### 2.3 `primitives/operational/continuous-questioning.md`

- **来源补充**：suiren: rehearsal
- **补充内容**：预演产出供连续发问使用的候选提示序列
- **组合关系补充**：无新增组合关系

### 2.4 `primitives/operational/dfs-guidance.md`

- **来源补充**：suiren: rehearsal；nuwa-b: budget-management
- **补充内容**：预演产出候选Q列表供DFS使用；分支预算限制DFS分支因子
- **组合关系补充**：约束于 budget-management（新原语，分支预算限制DFS分支因子）

### 2.5 `primitives/operational/execution-contract.md`

- **来源补充**：nuwa-b: phase-gate；fuxi: dual-output-closed-loop
- **补充内容**：Phase门控是执行契约的验证机制；双产出闭环是执行契约的运行实例
- **组合关系补充**：组合了 phase-gate（新原语）, dual-output-closed-loop（新原语）

### 2.6 `primitives/operational/implicit-filtering.md`

- **来源补充**：nuwa-b: minimality-audit；pangu-b: direction-only-content
- **补充内容**：预载检查是泄漏检测的一部分；方向性节点内容是隐含筛选的具体实现
- **组合关系补充**：约束于 leakage-detection（新原语，预载检查是泄漏检测的一部分）

### 2.7 `primitives/operational/minimal-knowledge-transfer.md`

- **来源补充**：nuwa-b: micro-package；pangu-b/fuxi: hint-gradient
- **补充内容**：微包是最小知识传递的封装形式；提示梯度从低到高实现最小知识传递
- **组合关系补充**：组合了 hint-gradient（新原语，提示梯度从低到高实现最小知识传递）, context-compiler（新原语，微包是最小知识传递的封装形式）

### 2.8 `primitives/operational/non-specificity.md`

- **来源补充**：pangu-b: direction-only-content；leakage-detection
- **补充内容**：方向性节点内容是非特定性的具体实现；四门泄漏检测是非特定性的验证机制
- **组合关系补充**：约束于 leakage-detection（新原语，四门泄漏检测是非特定性的验证机制）

### 2.9 `primitives/operational/safe-first-step.md`

- **来源补充**：suiren: shape-matching；stall-detection
- **补充内容**：形状描述来自安全第一步；solo explore后检测卡点才给hint
- **组合关系补充**：组合了 stall-detection（新原语，solo explore后检测卡点才给hint）, pattern-matching（新原语，形状描述来自安全第一步）

### 2.10 `primitives/structural/certificate.md`

- **来源补充**：evidence-system；fuxi: certificate-ledger, certificate-pullback
- **补充内容**：证据系统是证书的实现基础；证书账本是证书的偏序管理；证书拉回是跨表示翻译
- **组合关系补充**：连接到 evidence-system（新原语）, certificate-ledger（新原语）, certificate-pullback（新原语）

### 2.11 `primitives/structural/cognitive-activation.md`

- **来源补充**：activation-score；context-compiler
- **补充内容**：激活分数是认知激活的计算机制；编译结果是激活包的具体内容
- **组合关系补充**：连接到 activation-score（新原语）, context-compiler（新原语）

### 2.12 `primitives/structural/constraint-solver-engine.md`

- **来源补充**：constrained-policy；gaming-detection, budget-management
- **补充内容**：受约束多目标策略是多约束求解的具体化；gaming检测影响动作选择
- **组合关系补充**：组合了 constrained-policy（新原语）, budget-management（新原语）

### 2.13 `primitives/structural/data-pedestal.md`

- **来源补充**：dual-output-closed-loop, failure-boundary-record
- **补充内容**：双产出闭环自动生成数据基座条目；失败边界是数据基座一等公民
- **组合关系补充**：连接到 dual-output-closed-loop（新原语）, failure-boundary-record（新原语）

### 2.14 `primitives/structural/math-reasoning-engine.md`

- **来源补充**：solver-role-isolation
- **补充内容**：Solver角色隔离确保推理引擎只做数学推理
- **组合关系补充**：约束于 role-isolation-matrix（新原语，Solver角色隔离确保推理引擎只做数学推理）

### 2.15 `primitives/structural/pattern-recognition-engine.md`

- **来源补充**：activation-score；multi-level-knowledge-extraction
- **补充内容**：激活分数排序候选Pattern；多层知识提取是模式识别的深层实现
- **组合关系补充**：组合了 activation-score（新原语）, multi-level-knowledge-extraction（新原语）

### 2.16 `primitives/structural/pipe.md`

- **来源补充**：role-isolation-matrix, micro-package
- **补充内容**：角色间信息隔离是Pipe合法性的保障；微包是Pipe间传递的数据单元
- **组合关系补充**：约束于 role-isolation-matrix（新原语）, context-compiler（新原语，微包是Pipe间传递的数据单元）

---

## 3. 落盘执行顺序建议

按依赖关系分层落盘，确保每个原语文件在被创建时，它依赖的原语文件已存在（组合关系中的引用不会悬空）：

### 第一批：第0层基础设施原语（11个新 + 3个已有更新）

1. `primitives/structural/dependency-graph.md`（新）
2. `primitives/structural/event-sourcing.md`（新）
3. `primitives/structural/role-isolation-matrix.md`（新）
4. `primitives/structural/layered-storage.md`（新）
5. `primitives/structural/obligation-hypergraph.md`（新）
6. `primitives/structural/evidence-system.md`（新）
7. `primitives/structural/representation-atlas.md`（新）
8. `primitives/operational/budget-management.md`（新）
9. `primitives/operational/phase-gate.md`（新）
10. `primitives/operational/depth-graded-check.md`（新）
11. `primitives/operational/multiple-independent-verification.md`（新）
12. 更新 `primitives/structural/data-pedestal.md`（已有）
13. 更新 `primitives/structural/certificate.md`（已有）
14. 更新 `primitives/structural/pipe.md`（已有）

### 第二批：第1层核心机制原语（18个新 + 5个已有更新）

15. `primitives/structural/version-chain.md`（新）
16. `primitives/structural/kth-three-graph-architecture.md`（新）
17. `primitives/structural/thinking-trajectory-graph.md`（新）
18. `primitives/structural/heuristic-rule-graph.md`（新）
19. `primitives/structural/truth-vault.md`（新）
20. `primitives/structural/dynamic-workspace.md`（新）
21. `primitives/structural/checkpoint.md`（新）
22. `primitives/structural/context-compiler.md`（新）
23. `primitives/structural/certificate-ledger.md`（新）
24. `primitives/structural/trajectory-recording.md`（新）
25. `primitives/structural/failure-boundary-record.md`（新）
26. `primitives/operational/retrieval-pipeline.md`（新）
27. `primitives/operational/verification-routing.md`（新）
28. `primitives/operational/stall-detection.md`（新）
29. `primitives/operational/pattern-matching.md`（新）
30. `primitives/operational/multi-level-knowledge-extraction.md`（新）
31. `primitives/operational/controlled-experiment.md`（新）
32. `primitives/operational/leakage-detection.md`（新）
33. 更新 `primitives/structural/math-reasoning-engine.md`（已有）
34. 更新 `primitives/structural/pattern-recognition-engine.md`（已有）
35. 更新 `primitives/structural/constraint-solver-engine.md`（已有）
36. 更新 `primitives/structural/cognitive-activation.md`（已有）
37. 更新 `primitives/operational/execution-contract.md`（已有）

### 第三批：第2层应用原语（27个新 + 8个已有更新）

38. `primitives/operational/topology-coverage-verification.md`（新）
39. `primitives/operational/spiral-loop-detection.md`（新）
40. `primitives/operational/incremental-graph-expansion.md`（新）
41. `primitives/operational/cross-audit-loop.md`（新）
42. `primitives/operational/gaming-detection.md`（新）
43. `primitives/operational/reactive-rescue.md`（新）
44. `primitives/operational/pattern-lifecycle.md`（新）
45. `primitives/operational/hint-gradient.md`（新）
46. `primitives/operational/activation-score.md`（新）
47. `primitives/operational/progress-measurement.md`（新）
48. `primitives/operational/gain-attribution.md`（新）
49. `primitives/operational/constrained-policy.md`（新）
50. `primitives/operational/hypothesis-driven-validation.md`（新）
51. `primitives/operational/blind-evaluation.md`（新）
52. `primitives/operational/legacy-handling.md`（新）
53. `primitives/operational/multi-source-audit.md`（新）
54. `primitives/operational/design-degradation-detection.md`（新）
55. `primitives/operational/audit-standard-backtesting.md`（新）
56. `primitives/operational/false-completion-detection.md`（新）
57. `primitives/operational/training-data-risk-assessment.md`（新）
58. `primitives/operational/counterexample-search.md`（新）
59. `primitives/operational/semantic-energy-descent.md`（新）
60. `primitives/operational/result-reflection.md`（新）
61. `primitives/operational/verifiable-compilation.md`（新）
62. `primitives/operational/certificate-pullback.md`（新）
63. `primitives/operational/obstruction-detection.md`（新）
64. `primitives/operational/dual-output-closed-loop.md`（新）
65. 更新 `primitives/operational/backtrack-fresh-session.md`（已有）
66. 更新 `primitives/operational/base-change.md`（已有）
67. 更新 `primitives/operational/continuous-questioning.md`（已有）
68. 更新 `primitives/operational/dfs-guidance.md`（已有）
69. 更新 `primitives/operational/implicit-filtering.md`（已有）
70. 更新 `primitives/operational/minimal-knowledge-transfer.md`（已有）
71. 更新 `primitives/operational/non-specificity.md`（已有）
72. 更新 `primitives/operational/safe-first-step.md`（已有）

---

## 4. 文件统计

| 类别 | 新建文件 | 更新文件 | 合计 |
|---|---|---|---|
| 结构原语 | 18 | 7 | 25 |
| 操作原语 | 38 | 9 | 47 |
| **合计** | **56** | **16** | **72** |

> **注**：Pass 3报告统计为59个新原语（18结构+41操作）。经逐项核对，实际需要独立落盘的文件为56个（18结构+38操作），因为3个操作原语（seed-selection、subgraph-extraction、local-view）在归并组2中被归入retrieval-pipeline作为子组件描述，不单独建文件。retrieval-pipeline.md中将包含这三个子组件的完整描述。

---

## 5. 验证状态分布（落盘后）

| 验证状态 | 新原语数 | 占比 |
|---|---|---|
| tested | 11 | 19.6% |
| partial | 14 | 25.0% |
| untested | 31 | 55.4% |
| **合计** | **56** | 100% |

> 超过半数新原语处于untested状态，这与系统演进过程中"设计先于实现"的实际情况一致。tested原语主要来自盘古代（POC中多次使用）和跨代共用基础设施。

---

## 附录：检索相关原语索引

以下原语在Pass 3报告中被标注为直接服务于检索流程，是Pass 4产出2（检索机制设计文档）的核心组装材料：

| 原语 | 类型 | 检索流程角色 | 验证状态 |
|---|---|---|---|
| dependency-graph | 结构 | 状态感知 | tested |
| event-sourcing | 结构 | 状态感知 | untested |
| dynamic-workspace | 结构 | 状态感知 | untested |
| checkpoint | 结构 | 状态感知 | untested |
| layered-storage | 结构 | 状态感知 | partial |
| obligation-hypergraph | 结构 | 状态感知 | partial |
| failure-boundary-record | 结构 | 状态感知 | untested |
| thinking-trajectory-graph | 结构 | Pattern提取 | untested |
| heuristic-rule-graph | 结构 | Pattern提取 | untested |
| representation-atlas | 结构 | Pattern提取 | partial |
| kth-three-graph-architecture | 结构 | 知识悖论 | partial |
| truth-vault | 结构 | 知识悖论 | partial |
| role-isolation-matrix | 结构 | 知识悖论 | partial |
| context-compiler | 结构 | 知识悖论 | partial |
| retrieval-pipeline | 操作 | 状态感知+Pattern提取 | partial |
| incremental-graph-expansion | 操作 | 状态感知 | tested |
| stall-detection | 操作 | 状态感知 | partial |
| progress-measurement | 操作 | 状态感知 | untested |
| multi-level-knowledge-extraction | 操作 | Pattern提取 | partial |
| pattern-matching | 操作 | Pattern提取 | untested |
| activation-score | 操作 | Pattern提取 | untested |
| pattern-lifecycle | 操作 | Pattern提取 | untested |
| certificate-pullback | 操作 | Pattern提取 | untested |
| reactive-rescue | 操作 | 知识悖论 | untested |
| leakage-detection | 操作 | 知识悖论 | partial |
| hint-gradient | 操作 | 知识悖论 | untested |
| constrained-policy | 操作 | 知识悖论 | untested |
| result-reflection | 操作 | 知识悖论 | untested |
| verifiable-compilation | 操作 | 知识悖论 | untested |
| semantic-energy-descent | 操作 | 状态感知 | untested |
| dual-output-closed-loop | 操作 | 状态感知 | untested |

已有原语中服务于检索的：

| 原语 | 类型 | 检索相关角色 |
|---|---|---|
| cognitive-activation | 结构 | 激活包的具体内容 |
| pattern-recognition-engine | 结构 | 模式识别引擎 |
| data-pedestal | 结构 | 检索的存储后端 |
| certificate | 结构 | 证书是检索结果的验证基础 |
| pipe | 结构 | Pipe间传递的数据单元 |
| dfs-guidance | 操作 | DFS树是检索结果的消费架构 |
| minimal-knowledge-transfer | 操作 | 检索结果的最小化约束 |
| non-specificity | 操作 | 检索结果的非特定性约束 |
| safe-first-step | 操作 | 检索触发的安全约束 |
