# Pass 3：跨组全局归并——完整原语提炼报告

## 1. 统计

| 指标 | 数量 |
|---|---|
| Pass 2 输入新候选 | 213 |
| 跨组归并吸收 | 168（归入42个归并组） |
| 归并后唯一概念 | 87（42个归并组 + 45个独立候选） |
| 降级为概念框架 | 27 |
| 补充至已有原语 | 1（direction-only-content → non-specificity） |
| **最终新原语候选** | **59**（18个结构原语 + 41个操作原语） |
| 已有原语补充 | 87（覆盖16个已有原语） |
| 概念框架候选 | 89（Pass 2）+ 27（Pass 3降级）= 116 |
| 性质标准候选 | 68（Pass 2） |

---

## 2. 归并记录

共42个归并组，吸收168个候选。以下列出所有归并组（按归并规模降序排列）：

### 归并组1：role-isolation-matrix（角色隔离矩阵）— 9个候选归并
- **包含**：pangu-a"角色分离" + pangu-b"角色隔离矩阵" + nuwa-b"角色隔离矩阵" + fuxi"role-isolation-matrix" + fuxi"meta-normal-separation" + suiren"Solver角色隔离" + pangu-b"隔离测试协议" + suiren"文件传递隔离" + nuwa-a"能力令牌"
- **归并理由**：所有候选都描述同一核心思想——meta操作与normal操作由不同AI实例完成，通过权限矩阵/令牌/物理隔离/文件传递等机制防止利益冲突。从pangu-a的角色分离理念，到nuwa-b的8角色矩阵形式化，到fuxi的8角色架构，到suiren的Solver隔离实现，是同一原语在不同代际的具体化。
- **统一名称**：role-isolation-matrix
- **统一定义**：系统功能拆分为隔离角色，每个角色有明确的职责和权限边界，通过可见性标签+能力令牌+物理隔离等机制在代码层面强制执行角色间的信息隔离，防止审计者与被审计者耦合。

### 归并组2：retrieval-pipeline（多级检索管线）— 10个候选归并
- **包含**：pangu-a"图遍历检索" + pangu-b"检索管线" + fuxi"three-stage-retrieval" + nuwa-b"五层检索优先级" + nuwa-a"五层优先检索" + pangu-b"子图预算提取" + fuxi"subgraph-extraction" + pangu-a"种子推荐表" + fuxi"seed-selection" + other"局部视图"
- **归并理由**：所有候选都描述从知识图中检索相关子图的多级管线——种子选择→结构化匹配→图遍历→语义检索→预算剪枝。种子选择和子图提取是管线的子组件。
- **统一名称**：retrieval-pipeline
- **统一定义**：多级递进检索机制——种子选择（层次索引定位+语义检索top-K）→图遍历扩展（BFS/DFS有界深度）→预算剪枝（深度/宽度/token控制）→返回结构化子图。

### 归并组3：dynamic-workspace（动态工作区）— 9个候选归并
- **包含**：fuxi"dynamic-workspace" + pangu-b"状态归约器" + nuwa-b"事件流状态重建" + suiren"状态归约" + suiren"探索地图" + nuwa-a"状态等价规范化" + other"路径等价" + nuwa-b"冻结状态强制" + fuxi"Schema冻结"
- **归并理由**：所有候选都描述同一概念——系统状态由版本化Reducer从不可变事件流中归约得出，状态用六元组表示，状态等价通过规范化键判定，核心数据用frozen dataclass保证不可变性。
- **统一名称**：dynamic-workspace
- **统一定义**：系统在时刻t的完整状态用六元组表示——V_t（已验证核心）、F_t（猜想前沿）、O_t（开放义务）、R_t（表示状态）、E_t（证据）、U_t（未解决问题），状态由版本化Reducer从事件流归约得出，不可直接修改。

### 归并组4：context-compiler（上下文编译器）— 8个候选归并
- **包含**：pangu-b"上下文编译器" + nuwa-a"上下文编译器" + nuwa-b"上下文编译" + fuxi"incremental-context-compilation" + pangu-b"内容分辨率层级" + nuwa-b"最小性审计" + nuwa-b"微包" + suiren"AI编译提示"
- **归并理由**：所有候选都描述把检索结果编译为AI可用的最小上下文包——选择分辨率、翻译边为思考关系、token预算删减、最小性审计、增量编译。微包是交付单元，AI编译提示是AI辅助环节。
- **统一名称**：context-compiler
- **统一定义**：把检索到的数学子图编译为AI此刻能可靠使用的最小上下文包——决定节点展开顺序和分辨率、翻译边为思考关系、token预算删减、三项最小性审计（冗余/缺失/预载）、从checkpoint增量编译。

### 归并组5：multi-level-knowledge-extraction（多层知识提取）— 8个候选归并
- **包含**：pangu-a"三层提取" + pangu-b"三层提取" + fuxi"multi-level-knowledge-extraction" + suiren"四层知识结构" + suiren"质量审计" + suiren"知识吸收pipeline" + suiren"过程性模式标注" + fuxi"progressive-pattern-extraction"
- **归并理由**：所有候选都描述从数学解法中按多个抽象层次提取知识——L1具体步骤→L2思维模式→L3范式思维→（可选L4），过程性标注在转折点，质量审计是门控环节。
- **统一名称**：multi-level-knowledge-extraction
- **统一定义**：多遍管道从数学解法中提取多层知识——L1具体步骤→L2思维模式（AI二次分析）→L3范式思维（AI三次分析）→可选L4哲学洞察，每层有质量审计门控。

### 归并组6：controlled-experiment（受控对照实验）— 6个候选归并
- **包含**：pangu-b"A/B对照实验协议" + suiren"三组对照实验" + fuxi"双路线对照" + nuwa-a"检查点分层因果实验" + fuxi"baseline-verification" + fuxi"causal-intervention-validation"
- **归并理由**：所有候选都是实验验证协议的不同变体——A/B基本对照、三组对照、双路线对照、检查点分层因果实验。
- **统一名称**：controlled-experiment
- **统一定义**：设置对照组和实验组在相同隔离条件下并行执行，通过组间差异量化因果效果——A/B对照、三组对照（增加去答案等价组）、双路线对照（AI路线vs闭环路线）、检查点分层因果实验。

### 归并组7：dependency-graph（依赖图）— 5个候选归并
- **包含**：pangu-a"依赖图" + pangu-b"依赖图存储" + fuxi"dependency-graph-k" + pangu-b"跨领域映射边" + pangu-a"认知单元"
- **归并理由**：所有候选都描述用图数据库存储知识依赖关系的核心结构。认知单元是节点类型，跨领域映射边是边类型。
- **统一名称**：dependency-graph
- **统一定义**：用有向图表示知识间的依赖关系——节点带类型、上下文元数据、知识内容、版本指针；边带类型（depends_on/calls/cross-domain）；可有跨域边和螺旋环路。用ArangoDB图数据库存储。

### 归并组8：representation-atlas（表示图册）— 7个候选归并
- **包含**：pangu-b"表示变换图" + nuwa-a"表示运输" + nuwa-b"表示映射" + fuxi"representation-atlas" + other"表示映射" + other"传输对象" + other"可靠性义务"
- **归并理由**：所有候选都描述数学对象在不同表示形式之间的映射与运输——图册是一组可切换的局部表示，映射有6种类型，运输只在可靠性义务通过后执行。
- **统一名称**：representation-atlas
- **统一定义**：一个处境不能被单一表示完全看清，需要一组可切换、可重叠、可拼合的局部表示（图册），表示间映射有6种类型，运输只在可靠性义务通过后执行。

### 归并组9：stall-detection（卡点检测）— 6个候选归并
- **包含**：pangu-b"停滞检测" + nuwa-a"停滞检测" + nuwa-b"卡点检测与环路判别" + suiren"卡点诊断" + fuxi"stuck-detection" + other"空洞检测"
- **归并理由**：所有候选都描述检测Solver是否卡住并分类卡点类型——7种互斥卡点类型，区分平面环路和螺旋上升环路。
- **统一名称**：stall-detection
- **统一定义**：从Solver的外显思维轨迹中检测7种卡点信号，区分平面环路（应停止）和螺旋上升环路（应继续）。

### 归并组10：event-sourcing（事件溯源）— 5个候选归并
- **包含**：pangu-b"事件溯源" + nuwa-a"不可变事件日志" + fuxi"event-sourcing" + suiren"不可篡改事件流" + nuwa-a"语义抽取"
- **归并理由**：所有候选都描述以不可变事件流记录每一步输出，语义抽取从原始事件中识别结构化语义单元。
- **统一名称**：event-sourcing
- **统一定义**：研究过程中的每一步都是不可变事件，在原始事件之上抽取语义事件（14种类型），系统状态是所有已发生事件的投影归约。

### 归并组11-42：其余归并组（简表）

| 归并组 | 统一名称 | 包含候选数 | 包含的候选来源 |
|---|---|---|---|
| 11 | verification-routing | 5 | nuwa-a"验证路由" + nuwa-b"验证路由" + fuxi"multi-level-verification" + nuwa-a"验证器六态输出" + nuwa-b"逐步验证标注" |
| 12 | pattern-lifecycle | 5 | pangu-b"Pattern生命周期管理" + nuwa-a"规则生命周期门控" + nuwa-b"规则生命周期" + fuxi"heuristic-rule-lifecycle" + nuwa-a"迁移验证" |
| 13 | hint-gradient | 4 | pangu-b"提示梯度" + fuxi"hint-gradient" + suiren"提示分级" + fuxi"Level排序提示" |
| 14 | kth-three-graph-architecture | 4 | pangu-b"K/T/H三图分离" + fuxi"three-graph-architecture" + nuwa-b"K/T/H投影" + suiren"K/H双存储" |
| 15 | obligation-hypergraph | 4 | pangu-b"义务图" + nuwa-a"AND/OR义务超图" + nuwa-b"AND/OR义务超图" + fuxi"obligation-hypergraph" |
| 16 | evidence-system | 4 | pangu-b"证据系统" + nuwa-a"证据认识状态" + nuwa-b"证据状态模型" + nuwa-b"验证门" |
| 17 | truth-vault | 4 | pangu-b"真值库" + nuwa-a"真理保险库隔离" + fuxi"truth-vault" + suiren"答案隔离" |
| 18 | checkpoint | 4 | pangu-b"Checkpoint干预" + nuwa-a"内容寻址检查点" + fuxi"checkpoint-continuation" + nuwa-a"分叉点检测" |
| 19 | leakage-detection | 3 | nuwa-a"四门泄漏检测" + suiren"四门泄漏审计" + fuxi"four-gate-leak-audit" |
| 20 | pattern-matching | 4 | pangu-b"因子化模式匹配" + suiren"规则库匹配" + suiren"形状匹配" + fuxi"shape-matching" |
| 21 | constrained-policy | 4 | nuwa-a"受约束多目标策略" + suiren"ABSTAIN动作" + nuwa-a"帮助依赖度量" + suiren"AI按需介入与降级" |
| 22 | hypothesis-driven-validation | 3 | pangu-b"假设驱动验证" + nuwa-a"预注册门" + nuwa-b"预注册因果实验" |
| 23 | cross-audit-loop | 2 | pangu-a"交叉审计" + pangu-a"闭环审计修正" |
| 24 | gain-attribution | 3 | suiren"增益归因" + fuxi"gain-attribution" + nuwa-a"长期归因" |
| 25 | version-chain | 3 | pangu-a"版本链" + pangu-b"版本链" + fuxi"version-chain" |
| 26 | thinking-trajectory-graph | 2 | pangu-b"外显思维图" + fuxi"thinking-trajectory-graph" |
| 27 | heuristic-rule-graph | 3 | pangu-b"启发激活图" + fuxi"heuristic-rule" + fuxi"pattern-library" |
| 28 | layered-storage | 3 | pangu-b"冷热温微四级存储" + nuwa-a"四层分级存储" + nuwa-b"三层存储" |
| 29 | progress-measurement | 3 | pangu-b"进展势函数" + nuwa-a"进展偏序" + nuwa-b"偏序进展度量" |
| 30 | spiral-loop-detection | 3 | pangu-a"螺旋环路检测" + pangu-b"螺旋环路" + fuxi"spiral-loop-detection" |
| 31 | topology-coverage-verification | 2 | pangu-a"拓扑覆盖验证" + fuxi"topology-coverage-verification" |
| 32 | reactive-rescue | 2 | pangu-b"反应式救援" + nuwa-a"反应式救援模式" |
| 33 | gaming-detection | 2 | nuwa-a"博弈检测" + nuwa-b"Gaming检测" |
| 34 | blind-evaluation | 2 | pangu-b"盲评" + nuwa-b"盲评" |
| 35 | phase-gate | 3 | pangu-b"Phase门控" + nuwa-b"Phase门控" + other"阶段门控" |
| 36 | legacy-handling | 2 | pangu-b"Legacy冻结+只读适配器" + nuwa-b"Legacy标记" |
| 37 | activation-score | 2 | nuwa-a"稀疏矩阵激活" + nuwa-b"激活分数计算" |
| 38 | budget-management | 2 | nuwa-b"多类型预算硬约束" + suiren"AI预算约束" |
| 39 | trajectory-recording | 3 | nuwa-b"三层轨迹记录" + fuxi"three-layer-recording" + suiren"四路径数据捕获" |
| 40 | failure-boundary-record | 2 | fuxi"failure-boundary-record" + fuxi"dead-end-marking" |
| 41 | e-graph（降级为概念） | 2 | nuwa-a"E-图等价饱和" + other"E-图" |
| 42 | trajectory-alignment（降级为概念） | 2 | nuwa-a"轨迹对齐" + other"轨迹对齐" |

---

## 3. 最终原语清单

### 3.1 已有原语补充（16个）

| 已有原语 | 新来源补充 | 补充内容 |
|---|---|---|
| backtrack-fresh-session | suiren: file-transfer-isolation, checkpoint | 文件传递隔离是新session中状态延续的机制；checkpoint续行是回溯的具体实现 |
| base-change | nuwa-a: representation-transport; fuxi: certificate-pullback | 表示运输是换基的具体化实现；证书拉回是换表示后的证书翻译 |
| continuous-questioning | suiren: rehearsal | 预演产出供连续发问使用的候选提示序列 |
| dfs-guidance | suiren: rehearsal; nuwa-b: budget-management | 预演产出候选Q列表供DFS使用；分支预算限制DFS分支因子 |
| execution-contract | nuwa-b: phase-gate; fuxi: dual-output-closed-loop | Phase门控是执行契约的验证机制；双产出闭环是执行契约的运行实例 |
| implicit-filtering | nuwa-b: minimality-audit; pangu-b: direction-only-content | 预载检查是泄漏检测的一部分；方向性节点内容是隐含筛选的具体实现 |
| minimal-knowledge-transfer | nuwa-b: micro-package; pangu-b/fuxi: hint-gradient | 微包是最小知识传递的封装形式；提示梯度从低到高实现最小知识传递 |
| non-specificity | pangu-b: direction-only-content; leakage-detection | 方向性节点内容是非特定性的具体实现；四门泄漏检测是非特定性的验证机制 |
| safe-first-step | suiren: shape-matching; stall-detection | 形状描述来自安全第一步；solo explore后检测卡点才给hint |
| certificate | evidence-system; fuxi: certificate-ledger, certificate-pullback | 证据系统是证书的实现基础；证书账本是证书的偏序管理；证书拉回是跨表示翻译 |
| cognitive-activation | activation-score; context-compiler | 激活分数是认知激活的计算机制；编译结果是激活包的具体内容 |
| constraint-solver-engine | constrained-policy; gaming-detection, budget-management | 受约束多目标策略是多约束求解的具体化；gaming检测影响动作选择 |
| data-pedestal | dual-output-closed-loop, failure-boundary-record | 双产出闭环自动生成数据基座条目；失败边界是数据基座一等公民 |
| math-reasoning-engine | solver-role-isolation | Solver角色隔离确保推理引擎只做数学推理 |
| pattern-recognition-engine | activation-score; multi-level-knowledge-extraction | 激活分数排序候选Pattern；多层知识提取是模式识别的深层实现 |
| pipe | role-isolation-matrix, micro-package | 角色间信息隔离是Pipe合法性的保障；微包是Pipe间传递的数据单元 |

### 3.2 新原语候选（59个）

#### [结构原语] dependency-graph（依赖图）
- **定义**：用有向图表示知识间的依赖关系——节点带类型、上下文元数据、知识内容、版本指针；边带类型；可有跨域边和螺旋环路。说"用依赖图"就知道要构建节点、编码边、嵌入知识、标注上下文。
- **三判据验证**：可执行性——用ArangoDB创建节点和边集合，AQL查询遍历；可验证性——POC-1/3/4/5/6中B组引用了依赖图结构，A/B对照验证增量；构造性——是检索、验证、提取等所有上层原语的存储基础设施
- **来源**：pangu-a: 63-P1, 68-P1...; pangu-b: 100-P18, 103-P1...; fuxi: 223-P8, 248-P2...
- **验证状态**：tested
- **依赖关系**：依赖 data-pedestal；支撑 retrieval-pipeline, topology-coverage-verification, spiral-loop-detection, multi-level-knowledge-extraction, incremental-graph-expansion
- **检索流程角色**：状态感知
- **系统演进角色**：盘古

#### [结构原语] version-chain（版本链）
- **定义**：认知单元的演化历史——有序版本序列，每个版本记录来源和验证结果，current_version指针指向最新版本。
- **三判据验证**：可执行性——在ArangoDB中创建cog_versions集合和版本链边；可验证性——POC中已实现；构造性——是认知演化的基础设施
- **来源**：pangu-a: 89-P15...; pangu-b: 100-P6...; fuxi: 249-P30...
- **验证状态**：tested
- **依赖关系**：依赖 dependency-graph；支撑 multi-level-knowledge-extraction, pattern-lifecycle
- **检索流程角色**：状态感知
- **系统演进角色**：盘古

#### [结构原语] kth-three-graph-architecture（K/T/H三图架构）
- **定义**：系统由三张图构成——K数学知识图、T外显思维图、H启发激活图，三图是投影而非独立真相库。
- **三判据验证**：可执行性——在ArangoDB中创建三个图集合；可验证性——当前只有K图已实现，T/H图未实现；构造性——是系统数据架构的核心框架
- **来源**：pangu-b: 122v2-P07...; fuxi: 248-P3...; nuwa-b: 174-P13...; suiren: 213-P14
- **验证状态**：partial
- **依赖关系**：包含 dependency-graph, thinking-trajectory-graph, heuristic-rule-graph
- **检索流程角色**：知识悖论
- **系统演进角色**：跨代

#### [结构原语] thinking-trajectory-graph（思维轨迹图）
- **定义**：对Agent的当前思维过程建模为外显思维图T_t，节点有10种类型，是启发规则匹配的输入。
- **三判据验证**：可执行性——从Agent输出中解析事件构建图；可验证性——设计完成但事件捕获器未实现；构造性——是模式匹配和卡点检测的输入
- **来源**：pangu-b: 122v2-P07...; fuxi: 248-P3...
- **验证状态**：untested
- **依赖关系**：依赖 event-sourcing；支撑 pattern-matching, stall-detection, heuristic-rule-graph
- **检索流程角色**：Pattern提取
- **系统演进角色**：女娲

#### [结构原语] heuristic-rule-graph（启发规则图）
- **定义**：H图保存经过实验验证的"触发→激活"关系，每条规则形式化为(LHS, Guard, RHS)，附带适用信号、证书模板、失败案例和验证脚本。
- **三判据验证**：可执行性——在ArangoDB中创建H图集合；可验证性——设计完成但无Pattern走完完整生命周期；构造性——是启发式干预的知识库
- **来源**：pangu-b: 122v2-P13...; fuxi: 248-P17...
- **验证状态**：untested
- **依赖关系**：依赖 thinking-trajectory-graph；约束于 pattern-lifecycle（规则需经生命周期验证才可上线，是约束条件而非前置依赖）；支撑 pattern-matching, activation-score
- **检索流程角色**：Pattern提取
- **系统演进角色**：燧人

#### [结构原语] event-sourcing（事件溯源）
- **定义**：研究过程中的每一步都是不可变事件，系统状态是所有已发生事件的投影归约，事件一旦发生不可修改。
- **三判据验证**：可执行性——创建append-only事件集合；可验证性——设计完成但事件捕获器未实现；构造性——是动态工作区、思维轨迹图、检查点的基础设施
- **来源**：pangu-b: 123-P17...; nuwa-a: 131-P3...; fuxi: 250-P9...; suiren: 202-P02...
- **验证状态**：untested
- **依赖关系**：无前置依赖；支撑 dynamic-workspace, thinking-trajectory-graph, checkpoint, trajectory-recording
- **检索流程角色**：状态感知
- **系统演进角色**：女娲

#### [结构原语] truth-vault（真值保险库）
- **定义**：将正确答案和完整证明存储在隔离的truth_vault collection中，写入仅truth_curator，读取仅auditor，其他角色无权访问。
- **三判据验证**：可执行性——创建隔离collection，用capability token控制访问；可验证性——代码已实现但未在真实多角色运行中验证；构造性——是泄漏检测的基础防线
- **来源**：pangu-b: 122v3-P05...; nuwa-a: 131-P24...; fuxi: 248-P19...; suiren: 200-P2...
- **验证状态**：partial
- **依赖关系**：依赖 role-isolation-matrix；支撑 leakage-detection
- **检索流程角色**：知识悖论
- **系统演进角色**：女娲

#### [结构原语] obligation-hypergraph（义务超图）
- **定义**：开放义务用AND/OR有向超图表达——AND约束（所有子目标都必须解决）、OR约束（任一路径成功即可），义务有10种类型和4种状态。
- **三判据验证**：可执行性——在ArangoDB中创建超边本体和participant edges；可验证性——代码已实现并集成测试通过；构造性——是进展度量和动态工作区的核心组件
- **来源**：pangu-b: 123-P12...; nuwa-a: 132-P7...; nuwa-b: 188-P06...; fuxi: 250-P12...
- **验证状态**：partial
- **依赖关系**：依赖 event-sourcing；支撑 dynamic-workspace, progress-measurement
- **检索流程角色**：状态感知
- **系统演进角色**：伏羲

#### [结构原语] evidence-system（证据系统）
- **定义**：证据有6种kind、polarity、生命周期，按polarity统计派生4种认识状态，验证门控制命题从F_t提升到V_t。
- **三判据验证**：可执行性——创建证据collection，定义类型化数据结构；可验证性——代码已实现但未在真实证据集合上验证；构造性——是证书和验证路由的基础设施
- **来源**：pangu-b: 123-P52...; nuwa-a: 132-P12...; nuwa-b: 188-P07...
- **验证状态**：partial
- **依赖关系**：支撑 certificate, verification-routing, dynamic-workspace
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：伏羲

#### [结构原语] layered-storage（分级存储）
- **定义**：知识存储按访问热度分层——冷层（全量数据）、温层（按需查询）、热层（当前问题相关子图）、微包（单步最小数据包）。
- **三判据验证**：可执行性——按层级创建不同collection和查询接口；可验证性——冷层239K论文已入库，热层在POC中手动构建；构造性——是检索管线和上下文编译器的存储后端
- **来源**：pangu-b: 110-P3...; nuwa-a: 135-P3...; nuwa-b: 183-P08...
- **验证状态**：partial
- **依赖关系**：依赖 dependency-graph；支撑 retrieval-pipeline, context-compiler
- **检索流程角色**：状态感知
- **系统演进角色**：盘古

#### [结构原语] role-isolation-matrix（角色隔离矩阵）
- **定义**：系统功能拆分为8个隔离角色，每个角色有明确的职责和权限边界，通过可见性标签+能力令牌+物理隔离等机制在代码层面强制执行。
- **三判据验证**：可执行性——定义角色枚举、可见性矩阵、capability token验证逻辑；可验证性——POC中用物理目录+AGENTS.md实现了简化版；构造性——是交叉审计、真值保险库、受控实验的角色隔离基础设施
- **来源**：pangu-a: 78-P11...; pangu-b: 116-P4...; nuwa-b: 176-P07...; fuxi: 250-P20...; suiren: 215-P17...
- **验证状态**：partial
- **依赖关系**：支撑 truth-vault, cross-audit-loop, controlled-experiment
- **检索流程角色**：知识悖论
- **系统演进角色**：女娲

#### [结构原语] representation-atlas（表示图册）
- **定义**：一个处境不能被单一表示完全看清，需要一组可切换、可重叠、可拼合的局部表示（图册），表示间映射有6种类型，运输只在可靠性义务通过后执行。
- **三判据验证**：可执行性——创建表示映射数据结构（12字段），定义6种map_type；可验证性——数据结构已实现但未在真实跨域推理中验证；构造性——是证书拉回、障碍检测的基础设施
- **来源**：pangu-b: 123-P05...; nuwa-a: 135-P14...; nuwa-b: 176-P19...; fuxi: 225-P04...; other: 004-P001...
- **验证状态**：partial
- **依赖关系**：支撑 certificate-pullback, obstruction-detection, retrieval-pipeline
- **检索流程角色**：Pattern提取
- **系统演进角色**：伏羲

#### [结构原语] context-compiler（上下文编译器）
- **定义**：把检索到的数学子图编译为AI此刻能可靠使用的最小上下文包——决定分辨率、翻译边为思考关系、token预算删减、三项最小性审计、增量编译。
- **三判据验证**：可执行性——实现编译管线（8步）；可验证性——代码已实现并集成测试通过；构造性——是检索管线和认知激活之间的编译桥梁
- **来源**：pangu-b: 122v1-P15...; nuwa-a: 135-P17...; nuwa-b: 183-P33...; fuxi: 250-P6...
- **验证状态**：partial
- **依赖关系**：依赖 retrieval-pipeline, layered-storage；支撑 cognitive-activation, reactive-rescue
- **检索流程角色**：知识悖论
- **系统演进角色**：跨代

#### [结构原语] checkpoint（检查点）
- **定义**：用SHA-256内容哈希标识状态快照，相同内容产生相同哈希使状态可去重和精确引用。提示后从当前checkpoint继续而非从原题重做。
- **三判据验证**：可执行性——计算状态哈希，存储checkpoint快照；可验证性——设计了完整机制但未在因果实验中验证；构造性——是受控实验和反应式救援的状态管理基础设施
- **来源**：pangu-b: 122v2-P37...; nuwa-a: 131-P9...; fuxi: 251-P12...
- **验证状态**：untested
- **依赖关系**：依赖 event-sourcing；支撑 controlled-experiment, reactive-rescue
- **检索流程角色**：状态感知
- **系统演进角色**：女娲

#### [结构原语] dynamic-workspace（动态工作区）
- **定义**：系统在时刻t的完整状态用六元组表示（V_t/F_t/O_t/R_t/E_t/U_t），由版本化Reducer从事件流归约得出，不可直接修改，状态等价通过规范化键判定。
- **三判据验证**：可执行性——实现版本化Reducer，从事件流归约六元组状态；可验证性——设计完成但事件捕获器未实现；构造性——是卡点检测、增量编译、进展度量的状态基础
- **来源**：fuxi: 250-P11...; pangu-b: 123-P14...; nuwa-b: 188-P01...; suiren: 200-P18...
- **验证状态**：untested
- **依赖关系**：依赖 event-sourcing, obligation-hypergraph, evidence-system；支撑 stall-detection, context-compiler, progress-measurement
- **检索流程角色**：状态感知
- **系统演进角色**：伏羲

#### [结构原语] certificate-ledger（证书账本）
- **定义**：系统在时刻t的状态是证书偏序C的向下封闭理想I_t——单调增长（每一步只加证书不删），已确认证书不会无声消失。
- **三判据验证**：可执行性——维护证书偏序集合，实现向下封闭理想检查；可验证性——设计完成但未实现；构造性——是语义能量下降、结果反射的证书管理基础设施
- **来源**：fuxi: 225-P08, 226-P3...
- **验证状态**：untested
- **依赖关系**：依赖 certificate；支撑 semantic-energy-descent, result-reflection, dual-output-closed-loop
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：伏羲

#### [结构原语] trajectory-recording（轨迹记录）
- **定义**：运行过程分三层独立记录——外部层（devin cli轨迹）、中间层（系统内部执行日志）、内部层（AI思路轨迹），四路径兜底捕获。
- **三判据验证**：可执行性——用tmux pipe-pane + capture-pane + export + transcript实现；可验证性——guided_001/003实验中已使用；构造性——是审计标准回测和增益归因的数据基础
- **来源**：nuwa-b: 178-P02...; fuxi: 248-P22...; suiren: 217-P6...
- **验证状态**：tested
- **依赖关系**：支撑 audit-standard-backtesting, gain-attribution
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：跨代

#### [结构原语] failure-boundary-record（失败边界记录）
- **定义**：记录哪些相似命题不成立、哪些条件删掉会失败——失败边界是数据基座的一等公民，经典计算标记已验证不可行路径为死路。
- **三判据验证**：可执行性——在数据基座中创建failure_boundary集合；可验证性——设计完成但未在真实搜索中验证；构造性——是反例搜索和导航约束的数据基础设施
- **来源**：fuxi: 231-P15, 234-P16...
- **验证状态**：untested
- **依赖关系**：依赖 data-pedestal；支撑 counterexample-search
- **检索流程角色**：状态感知
- **系统演进角色**：伏羲

---

#### [操作原语] multi-level-knowledge-extraction（多层知识提取）
- **定义**：多遍管道从数学解法中提取多层知识——L1具体步骤→L2思维模式→L3范式思维→（可选L4），每层有质量审计门控，过程性标注在转折点。
- **三判据验证**：可执行性——多遍AI分析，每遍用不同prompt；可验证性——POC-3验证L2/L3在远迁移中产生显著增量；构造性——是依赖图知识补充的核心操作
- **来源**：pangu-a: 83-P01...; pangu-b: 100-P8...; fuxi: 248-P23...; suiren: 201-P1...
- **验证状态**：partial
- **依赖关系**：依赖 dependency-graph, version-chain, pattern-recognition-engine；支撑 incremental-graph-expansion
- **检索流程角色**：Pattern提取
- **系统演进角色**：盘古

#### [操作原语] retrieval-pipeline（多级检索管线）
- **定义**：多级递进检索——种子选择（层次索引+语义检索top-K）→图遍历扩展（BFS/DFS有界深度）→预算剪枝→返回结构化子图。
- **三判据验证**：可执行性——用AQL图遍历查询实现，三级递进；可验证性——POC中手动替代，253号目标是自动化；构造性——是上下文编译器的输入管线
- **来源**：pangu-a: 63-P5...; pangu-b: 100-P3...; fuxi: 234-P10...; nuwa-b: 166-P08...
- **验证状态**：partial
- **依赖关系**：依赖 dependency-graph, layered-storage；支撑 context-compiler
- **检索流程角色**：状态感知 + Pattern提取
- **系统演进角色**：盘古

#### [操作原语] topology-coverage-verification（拓扑覆盖验证）
- **定义**：构造拓扑骨架G'_topo，用AQL集合差集验证覆盖所有节点/边/跨领域边/螺旋环路圈数——差集为空即100%覆盖。
- **三判据验证**：可执行性——用AQL集合差集运算实现；可验证性——POC中多次使用TopologyVerifier；构造性——是经典计算展开的质量门控
- **来源**：pangu-a: 78-P9...; fuxi: 248-P6...
- **验证状态**：tested
- **依赖关系**：依赖 dependency-graph
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：盘古

#### [操作原语] spiral-loop-detection（螺旋环路检测）
- **定义**：用Tarjan SCC算法发现图中所有环，区分平面环路（上下文相同，应停止）和螺旋环路（上下文不同，应继续）。
- **三判据验证**：可执行性——用Tarjan SCC算法+AQL查询实现；可验证性——POC-1/4/5/6中螺旋环路作为结构元素使用；构造性——是依赖图结构验证的组件
- **来源**：pangu-a: 63-P4...; pangu-b: 113-P6...; fuxi: 249-P4...
- **验证状态**：tested
- **依赖关系**：依赖 dependency-graph；支撑 topology-coverage-verification
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：盘古

#### [操作原语] incremental-graph-expansion（增量图扩展）
- **定义**：在已有依赖图基础上新增节点和边，保留已有子图结构不变——而非重新设计。扩展时保留已验证的节点/意识，在新上下文中复用。
- **三判据验证**：可执行性——在ArangoDB中新增节点/边，标记新增vs复用；可验证性——POC中多次使用；构造性——是认知图持续增长的机制
- **来源**：pangu-a: 64-P17, 65-P01...
- **验证状态**：tested
- **依赖关系**：依赖 dependency-graph, multi-level-knowledge-extraction
- **检索流程角色**：状态感知
- **系统演进角色**：盘古

#### [操作原语] cross-audit-loop（交叉审计闭环）
- **定义**：用独立AI实例审计另一个AI的输出——审计→发现瑕疵→结构化反馈→修正→再审计→直到无瑕疵或达到最大轮数。三级终止机制。
- **三判据验证**：可执行性——启动独立AI实例，传递基准+输出；可验证性——POC中多次使用；构造性——是Pipe中的质量门控环节
- **来源**：pangu-a: 71-P14, 72-P06...; pangu-a: 76-P01...
- **验证状态**：tested
- **依赖关系**：依赖 role-isolation-matrix；支撑 pipe
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：盘古

#### [操作原语] stall-detection（卡点检测）
- **定义**：从Solver的外显思维轨迹中检测7种卡点信号，区分平面环路（应停止）和螺旋上升环路（应继续），客观证据优先于主观自报。
- **三判据验证**：可执行性——从事件流/思维图中检测卡点信号；可验证性——143-P13有pilot验证；构造性——是反应式救援和博弈检测的触发机制
- **来源**：pangu-b: 122v2-P36...; nuwa-a: 132-P17...; nuwa-b: 176-P20...; suiren: 200-P19...; fuxi: 223-P19...
- **验证状态**：partial
- **依赖关系**：依赖 dynamic-workspace, thinking-trajectory-graph；支撑 gaming-detection, reactive-rescue
- **检索流程角色**：状态感知
- **系统演进角色**：跨代

#### [操作原语] gaming-detection（博弈检测）
- **定义**：三元判定机制检测工作智能体是否在"gaming"——（停滞词=True）AND（工具证据=False）AND（结构进展=False）三条件全部满足才判定。
- **三判据验证**：可执行性——实现三元AND判定逻辑；可验证性——代码已实现但未在真实gaming行为上验证；构造性——是规则生命周期停止条件的触发机制
- **来源**：nuwa-a: 136-P23...; nuwa-b: 175-P12...
- **验证状态**：partial
- **依赖关系**：依赖 stall-detection；支撑 pattern-lifecycle, constrained-policy
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：女娲

#### [操作原语] reactive-rescue（反应式救援）
- **定义**：Agent先独立尝试解题，检测到真实停滞后才匹配启发规则并注入最小提示，从当前checkpoint继续。反应式是默认模式，主动导航需经验证后开启。
- **三判据验证**：可执行性——检测卡点→匹配规则→注入提示→从checkpoint继续；可验证性——设计阶段提出，尚未实现在线运行时；构造性——是整个引导系统的运行模式
- **来源**：pangu-b: 122v2-P34...; nuwa-a: 136-P28...
- **验证状态**：untested
- **依赖关系**：依赖 stall-detection, checkpoint, context-compiler；支撑 constrained-policy
- **检索流程角色**：知识悖论
- **系统演进角色**：燧人

#### [操作原语] pattern-lifecycle（规则生命周期）
- **定义**：启发规则经历observed→candidate→intervened→validated→published→retired完整生命周期，每次状态转移需满足明确条件，candidate状态禁止在线匹配。
- **三判据验证**：可执行性——定义状态枚举和转移条件；可验证性——框架设计完成但无Pattern走完完整生命周期；构造性——是H图规则管理的核心机制
- **来源**：pangu-b: 122v2-P31...; nuwa-a: 133-P30...; nuwa-b: 176-P04...; fuxi: 250-P13...
- **验证状态**：untested
- **依赖关系**：依赖 controlled-experiment, leakage-detection；支撑 heuristic-rule-graph, activation-score
- **检索流程角色**：Pattern提取
- **系统演进角色**：跨代

#### [操作原语] leakage-detection（泄漏检测）
- **定义**：通过四个独立维度检测Hint是否泄漏答案——字面匹配、等价映射、候选空间缩减、盲恢复，任一超标即判泄漏。
- **三判据验证**：可执行性——实现四门检查逻辑；可验证性——209号报告泄漏率从40%降到20%；构造性——是提示发送的出口门控
- **来源**：nuwa-a: 133-P23...; suiren: 200-P4...; fuxi: 248-P19...
- **验证状态**：partial
- **依赖关系**：依赖 truth-vault；支撑 pattern-lifecycle, non-specificity
- **检索流程角色**：知识悖论
- **系统演进角色**：燧人

#### [操作原语] hint-gradient（提示梯度）
- **定义**：建立多级提示梯度——从低泄漏（元检查/思维操作）到高泄漏（确定方向/具体步骤），优先选低泄漏级别，不够再逐步升级。
- **三判据验证**：可执行性——定义梯度级别，实现排序逻辑；可验证性——设计阶段提出，POC中用二分替代；构造性——是minimal-knowledge-transfer的具体实现机制
- **来源**：pangu-b: 122v2-P25...; fuxi: 250-P4...; suiren: 200-P25...
- **验证状态**：untested
- **依赖关系**：约束于 non-specificity, minimal-knowledge-transfer；支撑 pattern-lifecycle
- **检索流程角色**：知识悖论
- **系统演进角色**：燧人

#### [操作原语] pattern-matching（模式匹配）
- **定义**：用规则库匹配替代硬编码提示——规则以(LHS, Guard, RHS)形式定义，匹配基于结构形状而非文本相似性，利用稀疏性只匹配可能相关的规则子集。
- **三判据验证**：可执行性——实现LHS子图匹配+Guard条件检查+RHS动作输出；可验证性——设计阶段提出，未在真实Pattern库上验证；构造性——是反应式救援的匹配引擎
- **来源**：pangu-b: 122v2-P19...; suiren: 200-P20...; suiren: 214-P6...; fuxi: 238-P7...
- **验证状态**：untested
- **依赖关系**：依赖 thinking-trajectory-graph, heuristic-rule-graph；支撑 reactive-rescue, activation-score
- **检索流程角色**：Pattern提取
- **系统演进角色**：燧人

#### [操作原语] activation-score（激活分数）
- **定义**：在H图稀疏表示上计算候选激活分数a_t = W^T * p_t，权重组合7种数值维度，激活分数作为候选Pattern的排序依据。
- **三判据验证**：可执行性——实现稀疏矩阵乘法；可验证性——公式已实现但未在真实Pattern库上验证；构造性——是模式匹配的排序机制
- **来源**：nuwa-a: 135-P40...; nuwa-b: 166-P16...
- **验证状态**：untested
- **依赖关系**：依赖 heuristic-rule-graph, pattern-lifecycle；支撑 pattern-matching
- **检索流程角色**：Pattern提取
- **系统演进角色**：女娲

#### [操作原语] controlled-experiment（受控对照实验）
- **定义**：设置对照组和实验组在相同隔离条件下并行执行，通过组间差异量化因果效果——A/B对照、三组对照、双路线对照、检查点分层因果实验。
- **三判据验证**：可执行性——设置隔离环境，并行执行，计算组间差异；可验证性——POC-1/3/4/5/6多次使用；构造性——是所有机制验证的实验基础设施
- **来源**：pangu-b: 100-P15...; suiren: 200-P28...; fuxi: 229-P4...; nuwa-a: 134-P2...
- **验证状态**：tested
- **依赖关系**：依赖 role-isolation-matrix, checkpoint, hypothesis-driven-validation
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：跨代

#### [操作原语] hypothesis-driven-validation（假设驱动验证）
- **定义**：实验前预设明确假设并冻结所有决策参数，冻结后不可回改，用ATE+CI下界+passes_exit_gate三步验证因果效应。
- **三判据验证**：可执行性——创建预注册文档，冻结参数；可验证性——POC-1/3/4/5/6均使用；构造性——是受控实验的验证框架
- **来源**：pangu-b: 106-P21...; nuwa-a: 134-P8...; nuwa-b: 174-P05...
- **验证状态**：tested
- **依赖关系**：支撑 controlled-experiment, pattern-lifecycle
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：跨代

#### [操作原语] blind-evaluation（盲评）
- **定义**：评分者不知道哪份回答来自哪个实验组，通过打乱运行顺序、隐藏处理组标签实现，评分AI独立于执行组和审计组。
- **三判据验证**：可执行性——打乱run顺序，隐藏标签；可验证性——POC-3使用盲评；构造性——是受控实验的评分机制
- **来源**：pangu-b: 105-P7...; nuwa-b: 193-P06...
- **验证状态**：tested
- **依赖关系**：支撑 controlled-experiment
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：盘古

#### [操作原语] phase-gate（阶段门控）
- **定义**：每个Phase有入口门和出口门，出口门审计本Phase全部交付物，通过后才进入下一Phase。
- **三判据验证**：可执行性——定义Phase枚举和门控条件；可验证性——Phase 0-7在多个Phase审计中验证有效；构造性——是系统开发流程的门控机制
- **来源**：pangu-b: 124-P48...; nuwa-b: 174-P04...; other: 004-P021
- **验证状态**：tested
- **依赖关系**：支撑 legacy-handling, execution-contract
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：跨代

#### [操作原语] legacy-handling（遗留处理）
- **定义**：旧数据和概念不原地清空或迁移，保留原貌作为只读历史数据，通过只读adapter访问，新数据写入新collection。
- **三判据验证**：可执行性——创建只读adapter，新collection用幂等可回滚migration；可验证性——Phase 0冻结旧数据后验证有效；构造性——是系统演化的数据管理机制
- **来源**：pangu-b: 121-P16...; nuwa-b: 166-P35...
- **验证状态**：tested
- **依赖关系**：依赖 phase-gate
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：跨代

#### [操作原语] progress-measurement（进展度量）
- **定义**：进展由5个可测量分量定义的偏序P_κ(S_t)，不同任务类型有不同权重，进展向量比较产生4种结果。
- **三判据验证**：可执行性——从动态工作区提取5个分量，计算偏序；可验证性——设计完成但未在真实运行中验证；构造性——是受约束策略的目标函数
- **来源**：pangu-b: 123-P21...; nuwa-a: 132-P22...; nuwa-b: 188-P03...
- **验证状态**：untested
- **依赖关系**：依赖 dynamic-workspace, obligation-hypergraph, evidence-system；支撑 constrained-policy, stall-detection
- **检索流程角色**：状态感知
- **系统演进角色**：伏羲

#### [操作原语] gain-attribution（增益归因）
- **定义**：对每次干预验证并归因其产生的增益——记录提示链，进展归因给首次引入H关系的提示，反事实估计"没有该提示是否也会达到进展"。
- **三判据验证**：可执行性——记录提示链，计算归因，做反事实估计；可验证性——设计完成但未在真实运行中验证；构造性——是规则生命周期升级的证据来源
- **来源**：suiren: 200-P12...; fuxi: 252-P19...; nuwa-a: 136-P26...
- **验证状态**：untested
- **依赖关系**：依赖 controlled-experiment；支撑 pattern-lifecycle
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：跨代

#### [操作原语] constrained-policy（受约束多目标策略）
- **定义**：策略π在进展最大化、泄漏最小化、依赖最小化、成本控制多个约束下选择最优动作，ABSTAIN（不干预）是合法选择，AI按需介入。
- **三判据验证**：可执行性——定义目标函数和约束，实现优化求解；可验证性——公式已定义但未在真实运行中验证；构造性——是整个引导系统的决策引擎
- **来源**：nuwa-a: 136-P32...; suiren: 200-P23...
- **验证状态**：untested
- **依赖关系**：依赖 progress-measurement, leakage-detection, budget-management；协同 reactive-rescue（reactive-rescue是运行模式，constrained-policy是决策引擎，两者协同工作而非单向支撑）
- **检索流程角色**：知识悖论
- **系统演进角色**：伏羲

#### [操作原语] verification-routing（验证路由）
- **定义**：根据命题类型选择验证工具并分层路由——formal→Lean 4、symbolic→SymPy、numerical→NumPy、human→人工，验证器输出6种状态。
- **三判据验证**：可执行性——实现路由逻辑，调用对应验证工具；可验证性——代码已实现但未在真实混合型命题上验证；构造性——是证据系统的验证执行机制
- **来源**：nuwa-a: 135-P23...; nuwa-b: 183-P39...
- **验证状态**：partial
- **依赖关系**：依赖 evidence-system；支撑 certificate
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：伏羲

#### [操作原语] budget-management（预算管理）
- **定义**：管理多种独立预算类型（token/计算/工具/分支/Hint），超限时触发硬性停止，Hint预算单独追踪。
- **三判据验证**：可执行性——定义预算类型和上限，每次消耗前检查；可验证性——设计完成但未在真实运行中验证；构造性——是受约束策略和DFS引导的约束条件
- **来源**：nuwa-b: 186-P01...; suiren: 205-P29...
- **验证状态**：untested
- **依赖关系**：支撑 constrained-policy, dfs-guidance
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：女娲

#### [操作原语] depth-graded-check（深度分级验收）
- **定义**：将"实现X"从二元勾选改为四元深度等级[D1]定义/[D2]逻辑/[D3]测试/[D4]集成，强制勾选者明确实现深度。
- **三判据验证**：可执行性——定义四元等级，在审计中逐项检查；可验证性——在多个Phase审计中验证有效；构造性——是多源交叉审计的一个维度
- **来源**：nuwa-a: 140-P5...
- **验证状态**：tested
- **依赖关系**：支撑 multi-source-audit
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：女娲

#### [操作原语] multi-source-audit（多源交叉审计）
- **定义**：用多个并行subagent分别完整扫描多个权威源文件的每一行，各自提取要求并标注来源，冲突时按权威等级裁决。
- **三判据验证**：可执行性——启动多个subagent，汇总对照；可验证性——在145-162号的多轮审计中验证有效；构造性——是系统开发的质量保障机制
- **来源**：nuwa-a: 139-P25...
- **验证状态**：tested
- **依赖关系**：依赖 depth-graded-check
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：女娲

#### [操作原语] design-degradation-detection（设计降级检测）
- **定义**：检测方案声明了某设计决策但实现降级了的情况，将方案声明与实现代码逐项核对。
- **三判据验证**：可执行性——将方案声明与实现代码逐项核对；可验证性——设计完成但未在真实降级场景中验证；构造性——是审计标准回测的检测维度之一
- **来源**：nuwa-b: 174-P31...
- **验证状态**：untested
- **依赖关系**：支撑 audit-standard-backtesting
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：女娲

#### [操作原语] audit-standard-backtesting（审计标准回测）
- **定义**：用已知结果的历史run验证审计标准能否正确发现问题和正确判定通过——用已知失败run验证召回率，用已知通过run验证精确率。
- **三判据验证**：可执行性——用历史run回测审计标准；可验证性——设计完成但未在真实回测中验证；构造性——是审计标准持续改进的机制
- **来源**：nuwa-b: 196-P01...
- **验证状态**：untested
- **依赖关系**：依赖 design-degradation-detection, trajectory-recording
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：女娲

#### [操作原语] multiple-independent-verification（多次独立验证）
- **定义**：通过多次（≥3次）独立运行判定结果是稳定的还是偶然的——3次全错才算"做不出来"，用独立于AI的机制验证结果正确性。
- **三判据验证**：可执行性——多次运行同一题目，用SymPy/Lean验证；可验证性——在MathArena baseline中已使用；构造性——是假完成检测的基础
- **来源**：suiren: 210-P4...
- **验证状态**：tested
- **依赖关系**：支撑 false-completion-detection
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：跨代

#### [操作原语] false-completion-detection（假完成检测）
- **定义**：AI可能给出错误证明但自认为完成——需要实验后对照标准答案验证，用独立于AI的机制检测假完成。
- **三判据验证**：可执行性——用SymPy数值验证+人工抽查；可验证性——MathArena baseline中检测到假完成案例；构造性——是验证系统的质量保障机制
- **来源**：suiren: 210-P5, 215-P25
- **验证状态**：tested
- **依赖关系**：依赖 multiple-independent-verification
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：燧人

#### [操作原语] training-data-risk-assessment（训练数据风险评级）
- **定义**：为每道题评估AI训练数据风险等级（高/中/低），基于时间新旧、语言、讨论热度三个信号综合判断。
- **三判据验证**：可执行性——按三个信号评分，综合判断；可验证性——在MathArena baseline中已使用；构造性——是数据集选择和实验设计的辅助机制
- **来源**：suiren: 210-P10...
- **验证状态**：tested
- **依赖关系**：无直接依赖
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：燧人

#### [操作原语] counterexample-search（反例搜索）
- **定义**：经典计算搜索小模型、随机样本、极端边界和约束满足解，给出具体对象让猜想失败——反例作为高价值语义反馈改变AI方向。
- **三判据验证**：可执行性——用NumPy/SciPy搜索小模型和随机样本；可验证性——设计完成但未在真实推理中验证；构造性——是死路标记和结果反射的输入
- **来源**：fuxi: 228-v0-P3...
- **验证状态**：untested
- **依赖关系**：支撑 failure-boundary-record, result-reflection
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：伏羲

#### [操作原语] semantic-energy-descent（语义能量下降）
- **定义**：计算当前处境的六分量能量向量（表示复杂度/证书距离/自由度残差/粘合缺陷/反例压力/形式化缺口），以Pareto改善或受控交换为判据选择能降低能量的语义移动。
- **三判据验证**：可执行性——计算六分量能量向量，选择Pareto改善的移动；可验证性——设计完成但未在真实推理中验证；构造性——是闭环推进的核心决策机制
- **来源**：fuxi: 225-1-P18, 225-P13...
- **验证状态**：untested
- **依赖关系**：依赖 certificate-ledger；支撑 dual-output-closed-loop
- **检索流程角色**：状态感知
- **系统演进角色**：伏羲

#### [操作原语] result-reflection（结果反射）
- **定义**：将经典计算的结果（成功/反例/障碍/未知）反射回语义场，改变AI的语义理解——成功则猜想过强、反例则方向错误。
- **三判据验证**：可执行性——将验证结果映射为语义反馈；可验证性——设计完成但未在真实推理中验证；构造性——是闭环中经典计算→AI理解的反馈机制
- **来源**：fuxi: 225-1-P4...
- **验证状态**：untested
- **依赖关系**：依赖 certificate-ledger；与 verifiable-compilation 互为V-R对
- **检索流程角色**：知识悖论
- **系统演进角色**：伏羲

#### [操作原语] verifiable-compilation（可证化编译）
- **定义**：将AI提出的语义移动编译成可检查的证书目标集合——一个语义移动可能产生零个、一个或多个证书目标，每个目标指定可交给什么工具检查。
- **三判据验证**：可执行性——将语义移动映射为证书目标列表；可验证性——设计完成但未在真实推理中验证；构造性——是闭环中AI→经典计算的编译机制
- **来源**：fuxi: 225-1-P8...
- **验证状态**：untested
- **依赖关系**：依赖 certificate；与 result-reflection 互为V-R对
- **检索流程角色**：知识悖论
- **系统演进角色**：伏羲

#### [操作原语] certificate-pullback（证书拉回）
- **定义**：给定表示变换τ:S'→S，将S上的证书翻译到S'上的操作——跨表示检索的基础操作。
- **三判据验证**：可执行性——定义证书翻译规则，执行拉回操作；可验证性——设计完成但未在真实跨域推理中验证；构造性——是障碍检测的基础操作
- **来源**：fuxi: 227-P14, 230-P21...
- **验证状态**：untested
- **依赖关系**：依赖 certificate, representation-atlas；支撑 obstruction-detection
- **检索流程角色**：Pattern提取
- **系统演进角色**：伏羲

#### [操作原语] obstruction-detection（粘合障碍检测）
- **定义**：检查不同局部表示的局部证书在重叠处是否能粘合成全局证书，粘合失败分四级——descent failure→obstruction object→Čech 1-cocycle→H¹ class。
- **三判据验证**：可执行性——检查重叠处证书一致性，分级判定障碍；可验证性——设计完成但未在真实推理中验证；构造性——是表示图册的粘合验证机制
- **来源**：fuxi: 225-1-P15...
- **验证状态**：untested
- **依赖关系**：依赖 representation-atlas, certificate-pullback
- **检索流程角色**：不直接服务于检索
- **系统演进角色**：伏羲

#### [操作原语] dual-output-closed-loop（单任务双产出）
- **定义**：求解闭环运行一次，同时产出问题的解和数据基座条目——每步语义移动被记录、每个证书目标被编译、每个验证结果被回写。
- **三判据验证**：可执行性——在闭环运行中同步记录到数据基座；可验证性——设计完成但未在真实运行中验证；构造性——是数据基座自动增长的核心机制
- **来源**：fuxi: 234-P1...
- **验证状态**：untested
- **依赖关系**：依赖 execution-contract, data-pedestal, certificate-ledger
- **检索流程角色**：状态感知
- **系统演进角色**：伏羲

---

## 4. 依赖关系网络

### 完整支撑/被支撑图

```
data-pedestal [已有]
├── dependency-graph
│   ├── version-chain
│   ├── retrieval-pipeline
│   │   └── context-compiler
│   │       └── cognitive-activation [已有]
│   ├── topology-coverage-verification
│   ├── spiral-loop-detection
│   ├── multi-level-knowledge-extraction
│   │   └── incremental-graph-expansion
│   └── failure-boundary-record
│       └── counterexample-search
│
event-sourcing
├── dynamic-workspace
│   ├── stall-detection
│   │   ├── gaming-detection
│   │   │   └── pattern-lifecycle
│   │   └── reactive-rescue
│   ├── progress-measurement
│   │   └── constrained-policy
│   │       └── reactive-rescue (双向)
│   └── context-compiler (增量编译)
├── thinking-trajectory-graph
│   ├── pattern-matching
│   │   └── reactive-rescue
│   └── heuristic-rule-graph
│       └── activation-score
│           └── pattern-matching
├── checkpoint
│   └── controlled-experiment
└── trajectory-recording
    └── audit-standard-backtesting
│
role-isolation-matrix
├── truth-vault
│   └── leakage-detection
│       ├── pattern-lifecycle
│       └── non-specificity [已有]
├── cross-audit-loop
│   └── pipe [已有]
└── controlled-experiment
│
obligation-hypergraph
├── dynamic-workspace (O_t字段)
└── progress-measurement
│
evidence-system
├── verification-routing
│   └── certificate [已有]
├── dynamic-workspace (E_t字段)
└── certificate-ledger
    ├── semantic-energy-descent
    │   └── dual-output-closed-loop
    ├── result-reflection ←→ verifiable-compilation
    └── dual-output-closed-loop
│
representation-atlas
├── certificate-pullback
│   └── obstruction-detection
└── retrieval-pipeline (第2层检索)
│
layered-storage
├── retrieval-pipeline
└── context-compiler
│
controlled-experiment
├── hypothesis-driven-validation
├── blind-evaluation
└── gain-attribution
    └── pattern-lifecycle
│
phase-gate
└── legacy-handling
│
depth-graded-check
└── multi-source-audit
│
design-degradation-detection
└── audit-standard-backtesting
│
multiple-independent-verification
└── false-completion-detection
│
budget-management
├── constrained-policy
└── dfs-guidance [已有]
│
hint-gradient
└── pattern-lifecycle
```

---

## 5. 分层结构

### 第0层（基础设施层）

被依赖最多、不依赖其他新原语的原语：

| 原语 | 类型 | 被依赖数 | 说明 |
|---|---|---|---|
| dependency-graph | 结构 | 6 | 知识图的存储基础设施 |
| event-sourcing | 结构 | 4 | 不可变事件流，状态重建的数据源 |
| role-isolation-matrix | 结构 | 3 | 角色隔离，审计和实验的基础 |
| layered-storage | 结构 | 2 | 分级存储，检索和编译的后端 |
| obligation-hypergraph | 结构 | 2 | 义务超图，状态和进展的组件 |
| evidence-system | 结构 | 3 | 证据管理，验证和证书的基础 |
| representation-atlas | 结构 | 3 | 表示图册，跨表示操作的基础 |
| budget-management | 操作 | 2 | 预算管理，策略和DFS的约束 |
| phase-gate | 操作 | 1 | 阶段门控，开发流程的基础 |
| depth-graded-check | 操作 | 1 | 深度分级，审计的基础维度 |
| multiple-independent-verification | 操作 | 1 | 多次验证，假完成检测的基础 |

已有原语在此层：data-pedestal, certificate, pipe

### 第1层（核心机制层）

依赖基础设施、被上层依赖的原语：

| 原语 | 类型 | 依赖 | 被依赖数 |
|---|---|---|---|
| version-chain | 结构 | dependency-graph | 2 |
| kth-three-graph-architecture | 结构 | (包含三图) | 0 |
| thinking-trajectory-graph | 结构 | event-sourcing | 3 |
| heuristic-rule-graph | 结构 | thinking-trajectory-graph | 1 |
| truth-vault | 结构 | role-isolation-matrix | 1 |
| dynamic-workspace | 结构 | event-sourcing, obligation-hypergraph, evidence-system | 3 |
| checkpoint | 结构 | event-sourcing | 1 |
| context-compiler | 结构 | retrieval-pipeline, layered-storage | 2 |
| certificate-ledger | 结构 | evidence-system | 3 |
| trajectory-recording | 结构 | event-sourcing | 1 |
| failure-boundary-record | 结构 | dependency-graph | 1 |
| retrieval-pipeline | 操作 | dependency-graph, layered-storage | 1 |
| verification-routing | 操作 | evidence-system | 1 |
| stall-detection | 操作 | dynamic-workspace, thinking-trajectory-graph | 2 |
| pattern-matching | 操作 | thinking-trajectory-graph, heuristic-rule-graph | 1 |
| multi-level-knowledge-extraction | 操作 | dependency-graph, version-chain | 1 |
| controlled-experiment | 操作 | role-isolation-matrix, checkpoint, hypothesis-driven-validation | 2 |
| leakage-detection | 操作 | truth-vault | 2 |
| hypothesis-driven-validation | 操作 | (无前置依赖) | 1 |

已有原语在此层：math-reasoning-engine, pattern-recognition-engine, constraint-solver-engine, cognitive-activation

### 第2层（应用层）

依赖核心机制、不被其他新原语依赖的原语：

| 原语 | 类型 | 主要依赖 |
|---|---|---|
| topology-coverage-verification | 操作 | dependency-graph |
| spiral-loop-detection | 操作 | dependency-graph |
| incremental-graph-expansion | 操作 | dependency-graph, multi-level-knowledge-extraction |
| cross-audit-loop | 操作 | role-isolation-matrix |
| gaming-detection | 操作 | stall-detection |
| reactive-rescue | 操作 | stall-detection, checkpoint, context-compiler |
| pattern-lifecycle | 操作 | controlled-experiment, leakage-detection |
| hint-gradient | 操作 | (约束于 non-specificity) |
| activation-score | 操作 | heuristic-rule-graph, pattern-lifecycle |
| progress-measurement | 操作 | dynamic-workspace, obligation-hypergraph |
| gain-attribution | 操作 | controlled-experiment |
| constrained-policy | 操作 | progress-measurement, leakage-detection, budget-management |
| blind-evaluation | 操作 | (支撑 controlled-experiment) |
| legacy-handling | 操作 | phase-gate |
| multi-source-audit | 操作 | depth-graded-check |
| design-degradation-detection | 操作 | (支撑 audit-standard-backtesting) |
| audit-standard-backtesting | 操作 | design-degradation-detection, trajectory-recording |
| false-completion-detection | 操作 | multiple-independent-verification |
| training-data-risk-assessment | 操作 | (无) |
| counterexample-search | 操作 | (支撑 failure-boundary-record) |
| semantic-energy-descent | 操作 | certificate-ledger |
| result-reflection | 操作 | certificate-ledger |
| verifiable-compilation | 操作 | certificate |
| certificate-pullback | 操作 | certificate, representation-atlas |
| obstruction-detection | 操作 | representation-atlas, certificate-pullback |
| dual-output-closed-loop | 操作 | execution-contract, data-pedestal, certificate-ledger |

已有原语在此层：backtrack-fresh-session, base-change, continuous-questioning, dfs-guidance, execution-contract, implicit-filtering, minimal-knowledge-transfer, non-specificity, safe-first-step

---

## 6. 概念框架候选（116个）

### Pass 2 直接产出（89个）
来自Pass 2的7组提炼结果，不满足原语三判据但有助于理解系统。

### Pass 3 从新候选降级（27个）

| 降级候选 | 原始组 | 降级理由 |
|---|---|---|
| topology-skeleton | pangu-a | 是依赖图的纯拓扑投影，不是独立原语——归入dependency-graph的属性 |
| cognitive-checkpoint | pangu-a | 是CP1-CP6的复合工作流，由其他原语组合而成 |
| classical-unfolding | pangu-a | 是生成topology-skeleton的具体算法，topology-skeleton已降级 |
| arxiv-mapping-promotion | pangu-b | 是特定数据源（arXiv）的处理流程，不是通用原语 |
| direction-only-content | pangu-b | 是non-specificity已有原语的具体实现，归入已有原语补充 |
| master-heuristics-library | nuwa-a | 是6条具体大师策略的集合，不是可执行机制 |
| e-graph | nuwa-a/other | 是等式饱和数据结构，属于实现细节而非系统构造积木 |
| trajectory-alignment | nuwa-a/other | 是轨迹匹配算法，属于实现细节 |
| gate-controlled-workflow | suiren | 是"有入口门/出口门"的通用模式，已被phase-gate覆盖 |
| cross-case-semantic-search | suiren | 明确提出"积累100+个case后才需要"，是未来功能 |
| ultimate-hint-set | suiren | 是10个具体提示的列表，不是可执行机制 |
| decision-chain | suiren | 是诊断→匹配→选择→编译的复合流程，由其他原语组合而成 |
| dataset-metadata-management | suiren | 是数据集管理工具，不是系统设计原语 |
| knowledge-absorption-pipeline | suiren | 是multi-level-knowledge-extraction+quality-audit的复合pipeline |
| rehearsal | suiren | 是"已知答案倒推提示序列"的策略，属于应用模式 |
| naturality-test | fuxi | 是数学验证方法，属于概念框架 |
| honest-downgrade | fuxi | 是"验证状态随证据动态降级"的元原则，不是可执行操作 |
| level-perception | fuxi | 是"AI通过比较感知Level"的认知能力，不是可执行操作 |
| topology-feature-vector | fuxi | 是特征表示方法，属于实现细节 |
| structured-document-index | fuxi | 是Pass 1的文档索引实现，不是系统设计原语 |
| physical-isolation | other | 是项目基础设施，不是系统设计原语 |
| name-isolation | other | 是项目基础设施，不是系统设计原语 |
| fermat-chain | other | 是特定案例的推理链模板，不是通用原语 |
| groupoid-check | other | 基于广群的代数一致性检查，理论化程度过高 |
| commutative-diagram | other | 是数学记号工具，不是系统构造积木 |
| geometry-guard | other | "推理结构的几何性质"定义不明确，可执行性不足 |
| tda-gate / persistent-homology / hott-gate | other | 基于TDA/HoTT的门控机制，前沿理论，实现可能不完整 |
| math-label | other | 是简单的标签标注，过于简单不足以独立为原语 |

---

## 7. 性质标准候选（68个）

来自Pass 2的7组提炼结果，描述原语应满足的性质和判断标准（如自然性、生死条件、语义场等），不直接用于构造系统。

---

## 8. 降级/拒绝记录

### 从213个新候选中的处理

| 处理 | 数量 | 说明 |
|---|---|---|
| 跨组归并吸收 | 168 | 归入42个归并组，每组吸收2-10个候选 |
| 归并后保留为新原语 | 40 | 42个归并组中40个通过三判据审查 |
| 归并后降级为概念 | 2 | e-graph(2候选)、trajectory-alignment(2候选) |
| 独立候选保留为新原语 | 19 | 45个独立候选中19个通过三判据审查 |
| 独立候选降级为概念 | 25 | 见第6节降级表 |
| 独立候选补充至已有原语 | 1 | direction-only-content → non-specificity |
| **最终新原语** | **59** | 40(归并) + 19(独立) |

### 降级判断标准

1. **可执行性不足**：无法说"用这个"然后知道下一步做什么——如level-perception、honest-downgrade、gate-controlled-workflow
2. **构造性不足**：是理解系统的视角而非构造系统的积木——如naturality-test、commutative-diagram、topology-feature-vector
3. **复合而非原语**：由其他原语组合而成，不是独立积木——如cognitive-checkpoint、decision-chain、knowledge-absorption-pipeline
4. **特定而非通用**：是特定案例/数据源的处理，不是通用机制——如fermat-chain、arxiv-mapping-promotion、ultimate-hint-set
5. **理论化过度**：前沿理论实现可能不完整——如groupoid-check、geometry-guard、tda-gate、persistent-homology、hott-gate
6. **项目基础设施**：是项目运维工具而非系统设计原语——如physical-isolation、name-isolation、dataset-metadata-management
7. **已被覆盖**：功能已被其他原语覆盖——如topology-skeleton（dependency-graph的投影）、gate-controlled-workflow（phase-gate覆盖）

---

## 附录：双视角标注汇总

### 检索流程角色分布

| 角色 | 新原语数 | 代表原语 |
|---|---|---|
| 状态感知 | 14 | dependency-graph, event-sourcing, dynamic-workspace, checkpoint, retrieval-pipeline, stall-detection, progress-measurement等 |
| Pattern提取 | 10 | thinking-trajectory-graph, heuristic-rule-graph, multi-level-knowledge-extraction, pattern-matching, activation-score, certificate-pullback等 |
| 知识悖论 | 10 | kth-three-graph-architecture, truth-vault, role-isolation-matrix, context-compiler, reactive-rescue, leakage-detection, hint-gradient, constrained-policy, result-reflection, verifiable-compilation |
| 不直接服务于检索 | 25 | evidence-system, certificate-ledger, verification-routing, controlled-experiment, audit类原语等 |

### 系统演进角色分布

| 角色 | 新原语数 | 代表原语 |
|---|---|---|
| 盘古（静态图前置） | 10 | dependency-graph, version-chain, layered-storage, retrieval-pipeline, topology-coverage-verification, spiral-loop-detection, incremental-graph-expansion, multi-level-knowledge-extraction, cross-audit-loop, blind-evaluation |
| 女娲（角色隔离） | 13 | kth-three-graph-architecture, thinking-trajectory-graph, event-sourcing, truth-vault, role-isolation-matrix, checkpoint, trajectory-recording, gaming-detection, budget-management, depth-graded-check, multi-source-audit, design-degradation-detection, audit-standard-backtesting |
| 燧人（非特定提问） | 7 | heuristic-rule-graph, reactive-rescue, leakage-detection, hint-gradient, pattern-matching, false-completion-detection, training-data-risk-assessment |
| 伏羲（形式化边界） | 16 | obligation-hypergraph, evidence-system, representation-atlas, dynamic-workspace, certificate-ledger, progress-measurement, constrained-policy, verification-routing, counterexample-search, semantic-energy-descent, result-reflection, verifiable-compilation, certificate-pullback, obstruction-detection, dual-output-closed-loop, failure-boundary-record |
| 跨代 | 9 | context-compiler, pattern-lifecycle, controlled-experiment, hypothesis-driven-validation, phase-gate, legacy-handling, gain-attribution, stall-detection, multiple-independent-verification |

### 验证状态分布

| 验证状态 | 新原语数 | 占比 |
|---|---|---|
| tested | 15 | 25% |
| partial | 16 | 27% |
| untested | 28 | 48% |
| **总计** | **59** | 100% |

tested的15个：dependency-graph, version-chain, trajectory-recording, topology-coverage-verification, spiral-loop-detection, incremental-graph-expansion, cross-audit-loop, controlled-experiment, hypothesis-driven-validation, blind-evaluation, phase-gate, legacy-handling, depth-graded-check, multi-source-audit, multiple-independent-verification, false-completion-detection, training-data-risk-assessment
