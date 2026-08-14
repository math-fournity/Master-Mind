# ChangeLog

本文件记录项目正式编号文档及其索引的新增与修订。从 2026-08-05 开始维护；更早的变更以 Git 历史和各编号文档为准。

## 2026-08-14

### 389号Arango物理存储链路纠正：经OrbStack已落D盘

- **触发**：用户纠正“Arango数据目录在D盘”的机器现状，要求同步相关文档认知。
- **核心事实**：Arango engine directory为容器内`/var/lib/arangodb3`，位于Docker overlay；OrbStack的宿主数据入口指向`/data/OrbStack/data`，其`data.img.raw`实际承载Docker machine，因此engine字节已物理落在D卷。
- **精确边界**：`physical D-backing=YES`；`/data/arangodb/data -> /data`专用bind当前未被engine使用；数据仍处于容器writable layer，尚未形成独立host-visible Arango volume。
- **语义修正**：`A-WP1-D`改为`PASS`（evidence basis为`CONFIRMED_VIA_ORBSTACK_IMAGE`），新增`A-WP1-BIND=WARNING_NOT_DEDICATED`；不再计划为“落D盘”搬迁，未来若转专用bind只属生命周期、备份与可见性硬化。
- **不变边界**：逻辑site verifier、Schema初始化和DDL/apply仍为`NOT_IMPLEMENTED`；本次没有连接或写入DB，没有重启容器，没有搬迁数据。
- **修订文件**：389号§15、Tell目录README索引、根/Seven AGENTS、Seven README与稳定docs、Schema索引、`/data/README.md`。

### 389号Seven数据库政策纠偏：复用原逻辑数据库（后续物理事实已由上节纠正）

- **触发**：用户确认Seven不需要先迁移Arango物理数据，可以继续使用原逻辑数据库，并要求文档反映最新情况。
- **事实保留**：Arango engine data仍在容器`/var/lib/arangodb3`，D盘bind `/data`为空；本轮没有连接、写入、重启或迁移数据库。
- **政策修正**：将“逻辑数据库复用”“Seven Schema初始化”“物理数据搬迁”拆开；冻结复用`xishujuzhen_math_glm52`且只使用`seven_*_v1`命名空间的架构。本步当时将物理D-backing记为`DEFERRED_WARNING`，该不完整物理判断已由上节纠正为`PASS`。
- **当前边界**：`G-WP1-S/C=PASS`；逻辑站点能力与Schema初始化仍`NOT_IMPLEMENTED`；不把离线contract升级为site PASS，不授权当前DDL/write。
- **修订文件**：389号§14、Tell目录README索引、根/Seven AGENTS、Seven README与稳定docs、旧Site v1 Schema说明、`/data/README.md`。

## 2026-08-05

### 146号审计方法论手册150号迭代：F7系统性遗漏模式

- **触发**：用户追问"是否有新发现应该被更新到146或者147号文档中？"
- **新发现**：150号Phase 4-7预防性审计揭示了149号迭代时不知道的新规律——F7的系统性遗漏模式
- **系统性遗漏模式**：F7不是随机遗漏，而是系统性遗漏。某些跨章节依赖（checkpoint 7字段/visibility label/a_t=W^T*p_t公式）会在所有用到它们的Phase中被重复遗漏。根因是这些概念是全局性概念，定义在非Phase章节
- **146号更新**：F7详解新增"系统性遗漏模式"子节（含5个跨章节依赖的系统性/非系统性分类表+根因+检测策略+已知系统性遗漏概念清单）；领域教训新增"教训8：F7的系统性遗漏模式"；实现前自检协议第7步强化（对照系统性遗漏清单）
- **147号更新**：阶段1步骤3强化（对照146号F7详解中的系统性遗漏模式清单）
- **修正文件**：146号手册（F7详解+教训8+自检第7步）、147号SOP（阶段1步骤3）、AGENTS.md索引

### Phase 4-7 Check List F7/F8预防性审计（150号审计报告）

- **触发**：用户要求"立即根据最新的审计认知，审计剩下的Phase的Check List文件"
- **审计方法**：用146号14维度审计体系（149号迭代版）的维度13(F7)+维度14(F8)预防性审计134-137号Check List。启动subagent扫描系统探讨.md 9个章节
- **发现6项偏差**：
  1. Phase 4 checkpoint 7字段缺失(F7，123号§847)
  2. Phase 4 visibility label缺失(F7，123号§607)
  3. Phase 5 a_t=W^T*p_t公式缺失(F8，系统探讨.md§10.4)
  4. Phase 5 Retriever visibility label缺失(F7，123号§607)
  5. Phase 6 checkpoint 7字段缺失(F7，123号§847)
  6. Phase 6 visibility label引用不明确(F7，123号§607)
- **偏差分布规律**：F7的checkpoint 7字段和visibility label是系统性遗漏（凡是用到这些概念的Phase都会遗漏，因为147号SOP阶段1只读本Phase章节）
- **Phase 7**：新增"角色隔离延续"节（P7-ROLE-1 Verifier覆盖域+P7-ROLE-2 8角色visibility label延续）
- **母本扫描结论**：123号对系统探讨.md 9个章节都做了继承+严格化，无其他F8遗漏
- **修正文件**：134/135/136/137号Check List + AGENTS.md索引
- **新增文档**：150-v1-2026-08-05-Phase4-7-CheckList-F7F8预防性审计与修正报告.md
- **预防性审计价值**：Phase 4-7均未实现，实现前修正可避免实现-审计-修正循环

### 146号审计方法论手册迭代：12维度→14维度，新增F7/F8断层类型

- **触发**：用户追问"为什么做了那么多次审计，这次依然发现了问题？146号应该迭代什么内容？"
- **根因分析**：146号手册和147号SOP的审计范围设计有两个结构性缺口：
  - 缺口A（F7）：147号SOP阶段1只要求读"本Phase对应章节"，不读跨章节依赖。Phase 3用了Phase 4/DYN-3定义的checkpoint（§847）、§21-28定义的动作集合（§485-497）、§23定义的依赖代理（§530）、§28定义的visibility label（§607），这些都不在§48 Phase 3章节内。
  - 缺口B（F8）：147号SOP阶段1把系统探讨.md列为"辅助文件（按需）"，不是必读文件。系统探讨.md§10.4的a_t=W^T*p_t公式被123号§25概括为"incidence/factor视图"，公式丢失。
- **新增断层类型**：
  - F7：跨章节依赖遗漏——Phase X用了Phase Y/§Z定义的概念，但只读Phase X章节，没读定义章节
  - F8：母本继承损失——123号概括了系统探讨.md母本中的实现细节，实现只读123号不读母本，细节丢失
- **新增审计维度**：
  - 维度13：跨章节依赖扫描——对Phase X用到的每个概念，回溯123号定义章节
  - 维度14：母本回溯审计——对Phase X用到的每个设计概念，回溯系统探讨.md母本
- **新增领域教训**：
  - 教训6：Check List概括不等于定义完整
  - 教训7：系统探讨.md不是辅助文件，是必读母本
- **147号SOP同步更新**：阶段1三文件并读→系统探讨.md从"辅助文件"升级为"必读母本"，123号从"本Phase对应章节"改为"全文扫描"，新增跨章节依赖扫描+母本回溯两个步骤
- **修正文件**：146号手册（标题+演进史+F7/F8详解+维度表+实现前自检+实现后审计+领域教训）、147号SOP（阶段1）、AGENTS.md索引

### Phase 3三文件审计与修正（149号审计报告）

- **触发**：用户要求用plan-dad3347dc4d8e542.md+系统探讨.md+123号文档三文件交叉审计Phase 3实现
- **审计方法**：3个并行subagent分别捋三个文件的每一行（387+2288+1210=3885行），提取所有Phase 3相关要求
- **三文件权威性裁决**：123号文档最高权威（最终严格化版本），系统探讨.md设计母本，plan历史参考
- **发现5项实现偏差**：
  1. MatcherAction动作集合5→9个（123号§485-497冻结9个完整动作）
  2. checkpoint补全Q_0/事件前缀/模型/工具/权限/预算/版本哈希7字段（123号§847）
  3. 角色可见性落实为visibility label+能力令牌运行时检查（123号§607）
  4. 稀疏计算实现a_t=W^T*p_t公式（系统探讨§10.4，7种数值组合权重）
  5. 新增AgentDependencyProxy类实现3个Agent依赖代理（123号§530，F6防线）
- **修正文件**：matcher.py/state_aligner.py/sparse_view.py/leakage_audit.py/test_phase3.py
- **新增文档**：149-v1-2026-08-05-Phase3实现三文件审计与修正报告.md
- **验证**：test_phase3.py全部通过（含5项审计修正验证）
- **AGENTS.md同步**：认知资产索引追加149号条目

### Phase 3实现：离线候选启发（148号方案+133号Check List）

- **触发**：用户说"请你遵照147号文档中的SOP，开始实现Phase 3"→"开始实现"
- **SOP执行**：147号SOP 10阶段全部执行——认知加载(CP1-CP3, 33认知单元)→三文件并读(133/127/123)→Phase 2 EXIT门实际运行验证(α=1.00)→D1-D4预检→127号逐字核对无偏差→F1-F6断层预扫(5个高风险项)→全局项核对(G0-4/R-1/R-4/R-5/R-8/R-13/CC-R-3/NO-8/NO-9)→角色隔离确认(heuristic_matcher离线模式)→方案先行(148号)→环境确认→启动声明
- **新增文档**：148-v1-2026-08-05-Phase3实现方案.md
- **新增代码**：xishujuzhen/research_runtime/heuristics/模块（11个文件）
  - models.py: HeuristicRule schema（覆盖127号§7全部字段：LHS/interface/RHS/guard/eta + 生命周期状态）
  - state_aligner.py: P3-1/P3-2 状态对齐+内容哈希checkpoint+共同状态+分叉点检测
  - rule_extractor.py: P3-3 LHS/interface/RHS/guard/eta抽取
  - activation_packet.py: P3-4 H0/H1/H2激活包（基于128号§3.2 Ramsey干预阶梯）
  - leakage_audit.py: P3-5/P3-6 答案等价性审计四门+泄漏审计（代理分数非互信息，F6防线）
  - rule_store.py: P3-7/P3-8 规则存储+生命周期管理（candidate禁止在线自动提示，R-4防线）
  - sparse_view.py: P3-9 H图incidence matrix稀疏表示（R-5防线：规则因子化）
  - matcher.py: P3-ROLE-1 HeuristicMatcher类（离线模式，不读取Truth Vault）
  - migrate.py: ArangoDB migration（heuristic_rules + activation_packets）
  - test_phase3.py: 集成测试（全部通过）
- **出口门**：P3-EXIT-1(候选可重复匹配)✅ + P3-EXIT-2(Hint不唯一确定答案)✅
- **Check List更新**：133号Phase 3状态更新为"已完成"
- **AGENTS.md同步**：认知资产索引追加133号(已实现状态)+148号条目

### Phase实现启动SOP建立（147号SOP）

- **触发**：用户希望把"开启新Phase实现之前应该做的事"固化为可触发的SOP，以后用"请你遵照147号文档中的SOP，开始实现Phase X"触发
- **新增文档**：147-v1-2026-08-05-Phase实现启动SOP-从指令到第一行代码的标准作业流程.md
- **内容**：10个阶段的标准作业流程——阶段0认知加载→阶段1三文件并读→阶段2前置Phase验收核对→阶段3 Check List可实现性预检→阶段4权威性预核对→阶段5 F1-F6断层预扫→阶段6全局项核对→阶段7角色隔离确认→阶段8方案先行→阶段9环境确认→阶段10启动声明。含阻塞处理、维护规则、触发语言变体
- **与146号的关系**：147号是上层工程工作流，146号第8章是其中阶段3/4/5的子流程，不重复
- **AGENTS.md 同步**：认知资产索引追加147号条目

### 审计方法论手册化（146号手册）

- **触发**：129—145号审计链中"如何把事做好、做对"的经验散落在7份文档中，用户决定收敛为一份可独立阅读、持续维护的手册
- **新增文档**：146-v1-2026-08-05-审计方法论手册-从覆盖性到权威性的12维度审计体系.md
- **内容**：完整收录 F1-F6 断层类型学、D1-D4 实现深度等级、12个审计维度、三文件交叉审计标准流程、权威性逐字核对清单（第12维度详表）、领域教训清单（TaskType≠ObligationType/Schema是权威/角色隔离不是可选项/方法近似必须声明/枚举权威值速查）、实现前自检协议、实现后审计协议、维护规则
- **AGENTS.md 同步**：原"Check List措辞规范"节（~30行）精简为指向146号手册的指针+速查要点；认知资产索引追加146号条目
- **定位**：每个Phase实现前/后的AI和审计者都要读；发现新断层类型（F7+）时追加到本手册

### 权威性逐字核对审计完成（145号审计报告）

- **触发**：144号Phase 2审计暴露了140/142未覆盖的F4/F5/F6三种新断层类型
- **新断层类型**：
  - F4概念混淆：TaskType和ObligationType等不同概念被合并
  - F5权威定义偏差：实现与127号Schema冻结文档不一致
  - F6方法近似：要求的方法被近似方法替代且未声明
- **第12审计维度**：权威性逐字核对——实现时必须同时打开127号逐字核对，Check List是导航，127号是法律
- **133-137号预防性修正**：
  - 133号：角色命名改为127号权威格式（heuristic_matcher/state_reducer/verifier）
  - 134号：无偏差
  - 135号：127号补充6种验证等级枚举（proven/formally_verified/computationally_supported/numerically_tested/contradicted/unknown）
  - 136号：Controller澄清为orchestrator的运行时功能组件，不是独立角色
  - 137号：Representation字段数从8改为12，补充rep_id/domain/preconditions/evidence
- **127号自身修正**：map_type注释补全relaxation（6种）+ 新增验证等级小节
- **新增文档**：145-v1-2026-08-05-权威性逐字核对审计与新断层类型F4F5F6.md

### Phase 2审计修正完成（144号审计报告）

- **审计依据**：plan-dad3347dc4d8e542.md + 系统探讨.md + 123号文档 + 127号Schema冻结文档 + 132号Check List
- **发现10项问题**：
  1. ObligationType枚举混淆TaskType和ObligationType（严重）
  2. EvidenceStatus枚举值错误（严重）
  3. StallType枚举值错误（严重）
  4. Obligation缺少evidence_refs和sub_obligations字段（中等）
  5. Evidence缺少source_event/confidence/conflicts字段（中等）
  6. Verifier角色完全缺失（严重）
  7. Retriever角色完全缺失（严重）
  8. StateReducer可复现约束验证缺失（中等）
  9. Krippendorff α用Jaccard近似而非真正计算（中等）
  10. ObligationStatus用released而非discharged（中等）
- **修正**：10项全部修正，新建verifier.py和retriever.py，集成测试全部通过
- **新增文档**：144-v1-2026-08-05-Phase2实现三文件审计与修正报告.md

### Phase 2实现完成（143号方案 + 132号Check List更新）

- **目标**：完成DYN-1（状态重建一致性）和DYN-2（卡点检测校准）
- **实现**：
  1. P2-1：Q_0 Ramsey案例Task实例化 + 冻结验证（q0.py）
  2. P2-2：WorkspaceStore + Budget/ModelConfig + ArangoDB workspaces collection（workspace_store.py + workspace.py扩展）
  3. P2-3：ObligationStore + AND/OR超边 + DAG验证 + 自环检测 + SCC循环依赖不自动释放（obligation.py）
  4. P2-4：VerificationGate + F_t→V_t验证门 + V_t/F_t分离验证（verification_gate.py）
  5. P2-5：EvidenceStore + 6种kind + 4种派生认识状态 + 冲突检测不爆炸（evidence.py）
  6. P2-6：RuleBasedReducer + SemanticBasedReducer + Krippendorff α一致性测试（reducer.py）
  7. P2-7：StallDetector + 7类卡点 + 假性停滞gaming检测 + precision/recall校准（stall_detector.py）
  8. P2-8：BeliefEstimator + 9种动作 + gaming弃权 + 预算约束（controller_belief.py）
  9. P2-9：ProgressOrder + 5分量进展偏序 + 状态等价~_{α,κ} + 两种环路判别 + 跨任务比较（progress.py）
- **ArangoDB新增6个collections**：workspaces/obligations/obligation_relations/obligation_edges/evidence/stall_annotations
- **出口门验证**：
  - P2-EXIT-1: DYN-1 α≥0.80且无关键字段低于0.67 ✅（5个关键字段α=1.00）
  - P2-EXIT-2: DYN-2卡点检测有校准能力 ✅（precision/recall计算通过）
  - P2-EXIT-3: DYN-1和DYN-2验收全部通过 ✅
- **方案文档**：143号
- **Check List更新**：132号Phase 2状态更新为"已完成"

### 新增

- `dev-docs/121-v1-2026-08-05-POC6修正版重跑纠偏与证据闭环方案.md`
  - 把 120 号交接复查发现转化为正式执行方案。
  - 明确 POC-6 修正版的测量口径、答案泄漏边界、依赖图拓扑修复、完整过程审计、项目内证据归档、重复 A/B 配对验证和四档判定标准。
- `dev-docs/122-v1-2026-08-05-数学大师系统总体架构调查.md`
  - 从文档、代码、ArangoDB和本机工具四个维度调查数学大师系统全貌。
  - 建立三平面、八组件、三闭环的总体架构v1，区分知识资产、规范知识、数学图、研究运行和控制面。
  - 记录主链未闭合、图模式分裂、KC稀疏、拓扑验证失败、召回与数学工具未接入等结构性问题，并给出后续分层调查顺序。

### 修订

- `dev-docs/122-v2-2026-08-05-思维形状与启发关系架构修订.md`
  - 把“思维的形状可观测、可比较、可干预”确立为总体架构基础公理。
  - 将单一数学依赖图修正为数学知识图K、外显思维图T、启发激活图H三图模型。
  - 将稀疏矩阵深化为带上下文、时序、失败状态和干预证据的“模式→激活包”关系，定义动态题目Q_t、Agent M救援闭环和最小因果干预POC。
- `dev-docs/122-v3-2026-08-05-完整机制复核与费马极限案例.md`
  - 在同一轮中完整通读80—99号，逐篇对账原始愿景、POC、工作系统、经典展开、测试与反哺机制。
  - 分别裁决当前启发/矫正机制、有效性证据、改进架构和Master答案泄漏的系统根因。
  - 用Frey曲线、Ribet降层和Wiles半稳定模性链分析“谷山—志村能否赋予AI证明FLT能力”，并列出大型证明所需知识接口和思维启发。
- `dev-docs/123-v1-2026-08-05-数学大师系统全景复盘与第一性原理重构计划.md`
  - 以`系统探讨.md`全文（1—2289行，SHA-256 `a2ac4dc1…4924b`）为母本，建立12段连续映射，`unmapped_ranges=[]`。
  - 从第一性原理将目标系统严格化为：类型化任务/工作区、不可变事件、表示变换、时序启发规则、证据状态和受约束最小干预；保留七层能力、五类资产和K/T/H直觉作为投影。
  - 给出DYN-0—DYN-7动态能力阶梯、Phase 0—7建设计划（含入口门、验收、停止条件和回滚边界）、角色权限矩阵、`dg_*`→新schema字段级crosswalk、Ramsey R(3,3)/R(3,3,3)与费马案例的动态化样例。
  - 把“完美提示词可通过经典计算产生”从硬公理降为可证伪假设；旧七步骤正式降为legacy静态重建器；明确高级数学（类型论、超图、可实现事件结构、因果实验、操作化泄漏指标）先行，严格信息论、范畴、层、TDA、HoTT在对象与分布假设成熟后进入。
  - 列出8类基本风险、6阶段迁移顺序和5项原文变化的严格化结论。

### 同步

- `AGENTS.md`
  - 将 119 号原始 POC-6 结果降级为存在答案泄漏的低可信历史证据。
  - 加入 120、121、122 v1/v2/v3 索引，并把122 v3设为当前总体架构与证据裁决基线。
  - 把 POC-6 恢复为待完成状态，并明确 POC-7 依赖修正版证据闭环。
  - 修正 Memory Section 中把原始 `+4.0/10` 当作最终泛化证据的旧结论。
  - 新增数学大师总体架构基线和架构调查A/B/C待办。
  - 123号落盘后：把“总体架构与建设计划状态”改为指向123号；把122 v3从“最高优先级基线”降为“证据复核基线 / 123号的证据前提”；新增123号文档索引并标为“最高优先级必读”；将“两种环路”严格化为基于开放义务、证据门和冲突进展向量的判别，不再使用“是否产生新判断维度”的直觉表述。
- `xishujuzhen/poc/cognition_units_math.json` 与 ArangoDB 认知图
  - 新增 `poc_methodology v3`，把答案泄漏审计、重复 A/B 运行和完整过程证据闭环纳入 POC 方法论。
  - 新增 `glossary v2`，定义“答案泄漏审计”“恢复性重跑”“验证性复跑”。
  - 将 `math_master_system` 更新到 v3，来源指向122号总体架构调查。
  - 将词汇表更新到 v3，定义知识平面、研究运行平面、控制平面、上下文编译器和研究运行记录。
  - 122 v2落盘后，将 `math_master_system` 更新到 v4、`dependency_graph_prompt` 更新到 v2、`glossary` 更新到 v4。
  - 新增 `thought_trace_graph` 和 `heuristic_activation_model` 两个核心认知单元及其依赖边。
  - 122 v3落盘后，将 `math_master_system`、`heuristic_activation_model`、`poc_methodology` 和 `glossary` 分别更新到证据复核版本。
  - CP6 任务认知覆盖率 100%，认知图 POC 回归综合评分 100/100。
  - 123号同步时运行`cognition_import_math.py`导致**事件2026-08-05-A**：ArangoDB `cognition_units`中130个awareness单元被truncate清空（165→35），不可恢复。详见AGENTS.md"数据丢失事件记录"节。`cognition_units_math.json`已更新为35个单元（29原有+6新增），ArangoDB已同步导入。

### 数据丢失事件

- **事件2026-08-05-A**：运行`cognition_import_math.py`时truncate清空ArangoDB `cognition_units`/`cog_edges`/`cog_versions`，丢失130个仅存在于ArangoDB中、未回写JSON的awareness单元。根因：import脚本设计为truncate-reload模式，但`add_unit()`只写ArangoDB不回写JSON，导致ArangoDB积累了JSON没有的单元。不可恢复（无备份、无WAL、git历史中JSON最多29个单元）。待修复：改import为merge模式、新增export脚本、配置arangodump备份。详见AGENTS.md"数据丢失事件记录"节。

### 124号Phase 0—7建设计划Check List

- 落盘`dev-docs/124-v1-2026-08-05-Phase0-7建设计划CheckList.md`：把123号Phase 0—7、DYN-0—7、停止条件、不做清单和下一实施包全部细化为可追踪的Check List条目。
- 每个Phase有入口门、细化的子项Check List（Phase 0细化到8大类30+子项）、出口门、停止条件和失败回滚。
- 含全局预注册门6项（G0-1—G0-6）、核心指标清单10项（G0-M1—M10）、风险登记16项（R-1—R-16）、贯穿案例（Ramsey CC-R-0—6 + 费马 CC-F-0/7）、角色隔离矩阵13项（P0-5.1—5.13）、项目级停止条件7项（STOP-1—STOP-7）、降级路径6项（DEG-1—6）、明确不做清单10项（NO-1—NO-10）、下一实施包5项（NI-1—NI-5）、未决问题5项（UQ-1—UQ-5）和进度追踪表。
- AGENTS.md认知资产表已补充124号索引条目。

### 124号v1审计修正

- **修正P0-7.1 DYN编号错误**：published条件中"DYN-4跨题迁移"修正为"DYN-5跨题与跨模型迁移"。DYN-4是帮助量响应曲线，DYN-5才是跨题与跨模型迁移（123号第四十一节）。
- **修正P4-EXIT-4逻辑错误**：删除P4-EXIT-4"published通用规则至少跨3个问题族和2个模型版本复现"。G0-5要求在Phase 4出口门前**冻结**published标准，不是在Phase 4出口门**达到**published标准。Phase 4是DYN-3/4/5的首轮，出口门只验证到validated级别。
- **补充风险登记**：新增R-1—R-16（123号第五十六节八项风险+第五十七节新增八项风险），每项风险标注核心防线所在Phase。
- **补充核心指标清单**：新增G0-M1—M10（123号第四十四节10个核心指标），作为DYN验收的量化基础。
- **补充贯穿案例Check List**：新增Ramsey CC-R-0—6和费马CC-F-0/7，作为贯穿所有Phase的验证材料。
- **扩充P0-5角色隔离Check List**：从3条扩充到13条，覆盖123号第二十八节8个角色的可见性矩阵和逐组件I/O契约。
- **补充降级路径**：新增DEG-1—6，明确停止条件触发后"做什么"（123号第五十八节诚实终态的操作化）。
- **标注P0-8为项目治理补充**：明确P0-8数据丢失修复不是123号架构要求，而是项目治理层面的修复项。
- **标注Phase 1—7粒度说明**：明确Phase 1—7保持123号原粒度，到实际执行前再细化。

### AGENTS.md对齐修正（与repo最新内容全面对齐）

- **修正DYN阶梯定义**：Memory Section第548行DYN-4—7全部错误（旧：DYN-4跨题迁移/DYN-5在线Agent M/DYN-6多问题并发/DYN-7自演化 → 新：DYN-4帮助量响应曲线/DYN-5跨题与跨模型迁移/DYN-6在线闭环控制器/DYN-7跨领域与长证明编排）。与123号第三十六—四十三节对齐。
- **修正Phase编号偏移**：TODO第483—485行和Memory第549行的Phase描述与123号/124号不一致。旧：Phase 0=schema冻结/Phase 1=只读盘点dg_*/Phase 2=DYN-0 → 新：Phase 0=冻结legacy与统一语义（含只读盘点dg_*）/Phase 1=只观察不提示（DYN-0）/Phase 2=类型化状态与研究义务（DYN-1/DYN-2）。
- **修正TODO中DYN编号引用**：第489行"对应DYN-3—DYN-4"修正为"对应DYN-3—DYN-5"（跨题迁移是DYN-5）。
- **修正Memory第545行DYN编号**："必须通过DYN-0—DYN-4验证"修正为"必须通过DYN-0—DYN-5验证"。
- **修正文档索引**：13/56—60号文档标注为"星学项目目录"文件（不在数学项目dev-docs/中）；补充69号文档（POC-4验证结果，原遗漏）。
- **补充代码文件索引**：补充11个未引用的py文件（arangodb_init.py、topology_verifier.py、test_dependency_graph.py、import_math_graph_to_arangodb.py、batch_extractor.py、absorb_test_loop.py、poc4_build_graph.py、poc9_*.py 4个）。
- **修正Handover日期标注**：工作系统实现状态标题从2026-08-04更新为2026-08-05。
- **修正64号文件名引用**：AGENTS.md引用`64-xishujuzhen-POC1验证方案.md`，实际文件名为`64-xishujuzhen-POC验证方案.md`（无"1"）。

### Git Hook对齐检查机制（防止AGENTS.md与repo内容不同步）

- **新增`xishujuzhen/alignment_check.py`**：AGENTS.md与repo内容对齐检查脚本。6项检查：①引用的dev-docs/*.md文件是否存在 ②dev-docs/编号文档是否都在索引中 ③引用的.py文件是否存在 ④DYN阶梯定义与123号是否一致 ⑤Phase定义与124号是否一致 ⑥认知图规模与JSON是否一致。返回(hard_violations, soft_warnings)。
- **新增`xishujuzhen/githooks/pre-commit`**：pre-commit hook，只检查硬性违规（引用的文件不存在），阻止违规commit。
- **增强`xishujuzhen/githooks/post-commit`**：在原有CP4检查清单基础上，新增AGENTS.md对齐检查（硬性+软性），commit后提醒但不阻塞。
- **修正64号文件名引用**：由alignment_check.py自动检测发现。

### 125号文档创建（2026-08-05）

- **新建`dev-docs/125-v1-2026-08-05-AGENTS对齐审计与Git-Hook防不同步机制.md`**：完整记录本轮对齐审计工作——7类不同步问题的发现与修正、alignment_check.py的6项检查设计、pre-commit/post-commit hook机制、测试验证结果和3个未决问题。

### Phase 0执行（2026-08-05）

- **新建`dev-docs/126-v1-2026-08-05-dg星图只读盘点报告.md`**：P0-3只读盘点。冻结dg_nodes(1719)/dg_edges(1483)/loops(4)的type/edge_type/mapping_type/graph分布、五类初步归类、schema字段清单。重要发现：96.5%边edge_type为unknown，真实边语义在mapping_type字段。
- **新建`dev-docs/127-v1-2026-08-05-Schema冻结与角色隔离矩阵.md`**：Phase 0核心交付物。冻结8类schema（Task/Workspace/Event/Obligation/Representation/Evidence/HeuristicRule/Visibility）、8角色×14collection可见性矩阵、逐组件最小输入/输出契约、CapabilityToken强制机制、candidate/validated/published/retired生命周期状态机。123号10条架构裁决逐项体现。
- **新建`dev-docs/128-v1-2026-08-05-全局预注册项与贯穿案例冻结.md`**：G0-1关键事件完整清单（5类20+种事件类型）、R-1—R-16风险监控机制（每项含监控机制/检查点/触发停止条件）、CC-R-0 Ramsey案例冻结（非泄漏干预阶梯+验证维度）、CC-F-0费马案例冻结（三层难度阶梯+推论链+大师启发维度）。
- **P0-1完成**：`seven_step_pipeline.py`头部标记[legacy-static]；AGENTS.md"七步骤工作流"节标注[legacy-static]。
- **P0-2完成**：`topology_verifier.py`头部标注"结构保真验证"；AGENTS.md"TopologyVerifier"节标注[结构保真验证]；cognition_units_math.json中topology_coverage/topology_verifier的key_cognition加入"结构保真"限定。
- **P0-6完成**：AGENTS.md"三层提取"节消除L1=v1/L2=v2/L3=v3映射，明确"L1/L2/L3是提取层次，不是版本号"。
- **P0-8完成**：`cognition_import_math.py`改为merge/upsert模式（不truncate）；新增`cognition_export_math.py`（ArangoDB→JSON双向同步）；`cognition_sdk_math.py`的`add_unit()`增加审计日志（`_audit_log()`方法写入cognition_audit_log collection）；新增`arango_backup.sh`备份脚本+`backups/arango/`目录。
- **124号Check List更新**：Phase 0全部条目（P0-1—P0-8 + P0-EXIT-1/2/3 + G0-1 + R-1—R-16 + CC-R-0 + CC-F-0）标记为[x]并附证据定位。
- **AGENTS.md更新**：dg_nodes/dg_edges描述更新为实际统计值；Handover Section更新冻结时点值；TODO中Phase 0标记为[x]；新增126/127/128号文档索引。

### Phase 0三文件审计与修正（2026-08-05）

- **新建`dev-docs/129-v1-2026-08-05-Phase0三文件审计与修正报告.md`**：以plan/系统探讨.md/123号v1三个文件为基准，对Phase 0全部实现做逐项审计。识别7项遗漏并全部修正。含三文件冲突裁决（Phase数量/角色数量/DYN编号/运行时步骤/风险数量）和实现优秀性评估。
- **127号文档修正**：§12补充L1/L2/L3五正交字段设计（semantic_role/abstraction_level/reuse_scope/evidence_level/intervention_effect）；§13补充原文数据对象到严格模式crosswalk（10行对应表）；§14补充12步运行时与原文11阶段crosswalk（12行对应表+4项关键变化）。
- **128号文档修正**：§1.2补充subgoal/test/contradiction/resolution/observation 5种事件类型；新增§1.5与123号Event schema的对齐说明，确保覆盖全部14种语义事件类型。
- **AGENTS.md修正**：七步骤工作流节补充旧七步骤→新12步运行时迁移映射表（7行对应表）；补充"明确不做"清单（8项硬约束，来自123号§59）；更新127/128号文档索引描述；新增129号文档索引。
- **SHA-256验证**：系统探讨.md SHA-256=`a2ac4dc1c5ea0b944f1ced587fc9623023d5dd3c9792def9311997d122e4924b`，与123号§1记录一致，文件未被修改。

### 124号Check List拆分（2026-08-05）

- **124号v2修订**：从497行单文件拆分为总览（174行）+ 130—137号各Phase独立文件。总览保留全局预注册门、核心指标、风险登记、贯穿案例、停止条件、不做清单、未决问题和进度追踪。各Phase的详细Check List在对应编号文件中。拆分原因：单文件过长难以维护，各Phase应独立演进。
- **新建130—137号**：8个Phase各自独立Check List文件。Phase 0（130号）含129号审计后补充的完整性标准；Phase 1/2（131/132号）含执行前补充的完整性标准占位符；Phase 3—7（133—137号）保持123号原粒度，到执行前再细化。
- **Check List编写规范改进**：各Phase文件中每个条目增加"来源追溯"（标注plan/123号的哪一节）和"完整性标准"（做完后应该达到什么状态）。这是129号审计发现的5个系统性不足的改进措施。

### Phase 1—7 Check List细化 + Phase 0审计（2026-08-05）

- **131—137号细化**：Phase 1—7的Check List全部从123号原粒度细化到可执行子项级别。每个Phase细化后立即用三个文件（plan/系统探讨.md/123号）自审，确认无遗漏。
- **细化新增条目**：
  - Phase 1：P1-8抽取失败验证、P1-ROLE角色隔离落地、P1-CODE代码模块创建
  - Phase 2：P2-8控制器信念建模（123号§22）、P2-9进展偏序定义（123号§18两种环路）
  - Phase 3：P3-9 H图稀疏表示（123号§25计算视图）
  - Phase 4：P4-10 Ramsey案例5个验证维度（128号§3.3）
  - Phase 5：P5-9 K/T/H投影实现（123号§24）、P5-10旧七步骤复用决策（123号§33）
  - Phase 6：P6-9受约束最小干预策略（123号§23受约束多目标选择）
  - Phase 7：P7-MATH数学主张三级别标注（R-8风险防线）
- **130号Phase 0审计**：用三文件重新审计Phase 0，发现3项遗漏并补充：P0-9现有文件后续职责冻结（123号§53的6个文件）、P0-10数据迁移原则冻结（123号§55的6条原则）、P0-11不在Phase 0一次性搭空框架（NO-9约束）。
- **完整性标准审计方法**：每个Phase细化后，逐项对照三个文件的相关章节，确认：(1) 123号Check List原条目全部覆盖；(2) plan的细化要求全部覆盖；(3) 系统探讨.md的相关内容全部覆盖；(4) 127号schema定义全部引用；(5) 128号风险/案例全部引用；(6) NO约束全部落地。

### Phase 0-7细化结果三文件交叉审计（2026-08-05）

- **138号审计报告落盘**：以plan/系统探讨.md/123号v1三个文件为基准，对Phase 0-7全部细化结果（130—137号）做跨Phase横向一致性审计和对三份文档最终理念的全面一致性审计。用3个并行subagent分别完整捋过三个文件的每一行（系统探讨.md 2289行 + 123号 1210行 + plan 387行）。
- **横向一致性**：10个审计维度（DYN阶梯/12步运行时/角色隔离/8类schema/入口门出口门链条/代码模块创建顺序/预注册门/贯穿案例/数据迁移原则/五项变化）全部通过。
- **发现8项遗漏并修正**：
  - A-1：R-5（多元时序组合爆炸）→ 133号P3-9.4 + 136号P6-2.4
  - A-2：R-6（上下文膨胀）→ 131号P1-3.6 + 135号P5-4.3
  - A-3：R-15（来源许可证/版本漂移）→ 135号P5-1.5 + 137号P7-1.4
  - A-4：NO-1（不先扩张到325000知识节点）→ 130号P0-10.7
  - A-5：NO-3（不用节点覆盖率代替数学正确）→ 134号P4-5.4
  - A-6：132号P2-9.1补充5个可测量分量（v_t/o_t/c_t/u_t/k_t）
  - A-7：135号P5-5补充NumPy/SciPy注册（系统探讨.md§4.4）
  - A-8：132号P2-1.3标注explain任务类型进展定义缺失（123号§23本身遗漏）
- **三文件冲突裁决**：5项冲突全部按演进关系裁决（势函数→偏序/topo_generator定位/洞的定义/Phase 5拆分/数学主张标注级别术语），Check List正确使用了123号的严格化版本。

### Phase 1实施：DYN-0事件捕获真实性（2026-08-05）

- **research_runtime/包创建**：按123号§54和plan要求创建`xishujuzhen/research_runtime/`包（Phase 1首次创建，NO-9约束不在Phase 0预建框架）。含models/（Task/Workspace/RunState/RawEvent/SemanticEvent类型定义）和events/（EventStore/CheckpointStore/migration）。
- **manifest实现**（P1-1）：`research_runtime/manifest.py`——运行manifest创建/落盘/冻结验证。含hidden_cot_required=false（R-1风险防线）和manifest_hash内容冻结验证。
- **RawEvent存储**（P1-3）：ArangoDB `raw_events` collection——append-only原始事件存储。含DAG验证（causal_predecessors不形成环）和content_hash验证。
- **SemanticEvent存储**（P1-4）：ArangoDB `semantic_events` collection——可重抽语义事件存储。含conflict_with对称性验证和三层保留机制（原始事件不可变→语义可重抽→快照可重建）。
- **checkpoint实现**（P1-5）：ArangoDB `checkpoints` collection——内容寻址checkpoint。不含LLM隐藏内部状态（123号§39），同内容同hash（幂等）。
- **ArangoDB新增4个collection**：raw_events/semantic_events/checkpoints/run_manifests。用幂等migration创建（123号§55），不动旧数据（NO-10约束）。
- **集成测试**（test_phase1.py）：DYN-0验收4条全部通过——(1)原始输出/工具/提示/时间/分支可定位；(2)事件可回放；(3)不要求隐藏CoT；(4)抽取失败不丢原始证据。
- **Phase 1状态**：已完成。DYN-0验收通过。

### Phase 1实现三文件审计与修正（139号，2026-08-05）

- **审计方法**：以plan/系统探讨.md/123号v1三个文件为基准，用3个并行subagent分别完整捋过三个文件的每一行，提取与Phase 1相关的所有要求。逐项对照实现代码，识别遗漏。
- **发现6项遗漏**：
  - A1. 自环检查缺失（123号§17"不存自环"）
  - A2. 事件图单调增长模式未实现（系统探讨.md§7.1"撤回不删除，新增contradicted/rejected事件"）
  - A3. 基础语义抽取器未实现（123号§46 Check List"建立语义事件抽取版本"）
  - A4. 基础事件捕获器未实现（123号§46 Check List"捕获公开文本和工具事件"）
  - A5. 事件捕获完整度度量缺失（123号§44核心指标）
  - A6. checkpoint多continuation验证缺失（123号§39实验设计要求）
- **修正实施**：
  - `events/store.py`：自环检查 + 单调增长方法（record_contradiction/record_rejection/verify_monotonic_growth） + 完整度度量（measure_capture_completeness，5维度）
  - `events/extractor.py`（新增）：SemanticExtractor，规则-based首版，20种RawEventType→SemanticEventType映射，置信度估计
  - `events/capture.py`（新增）：EventCapture，10种捕获方法，自动causal_predecessors链接，R-1风险防线
  - `models/event.py`：新增CLAIM_CONTRADICTED/CLAIM_REJECTED事件类型
  - `test_phase1.py`：新增6项审计修正测试
- **测试结果**：DYN-0验收4条 + 审计修正6项全部通过
- **审计报告**：139号文档

### Check List到实现断层元问题诊断（140号，2026-08-05）

- **触发事件**：Phase 1实现经139号审计后发现6项遗漏，用户提出元问题"为什么一审再审实现还是出问题"
- **调查方法**：完整读取131—137号全部Check List + 138号审计报告 + 139号实现审计报告，逐项对照Check List与实现，识别断层模式
- **发现三种系统性断层模式**：
  - F1"定义了=实现了"：Check List说"实现X"，但只定义了X的类型/schema/枚举就勾选（131号P1-2.2/P1-4.3）
  - F2"验证了=完整了"：写了验证函数但不覆盖边界情况就勾选（131号P1-3.5/P1-5.COMP3）
  - F3"Check List覆盖盲区"：Check List本身遗漏来源文档要求（131号遗漏123号§17自环/§44完整度/§39多continuation）
- **138号审计的盲区**：138号是"覆盖性审计"（检查Check List是否提到X），不是"可实现性审计"（不检查措辞是否能区分"定义"和"实现"）
- **其他Phase风险评估**：Phase 2/4/5/6/7的F1风险均为高（6—7项/Phase），普遍存在同样范型问题
- **根本修正方案**：
  1. 引入实现深度等级D1（定义）/D2（逻辑）/D3（测试）/D4（集成）
  2. 新增"可实现性审计"维度（第11个审计维度）
  3. 勾选从二元[x]/[ ]改为四元[D1]/[D2]/[D3]/[D4]/[ ]
- **诊断报告**：140号文档

### CheckList预防性修正与可实现性审计（142号，2026-08-05）

- **修正目标**：从源头消除140号诊断发现的三种系统性断层模式（F1/F2/F3）
- **修正方法**：
  1. AGENTS.md新增"Check List措辞规范"一节——定义D1-D4深度等级+3条措辞规则+四元勾选格式
  2. 亲自精修132号Phase 2 Check List作为模板——逐项标注D1-D4+边界情况清单+覆盖标准
  3. 对132号做F3检查——发现§18的3项遗漏（状态等价参数化`~_{α,κ}`/规范化键定义/规范化键一致性判定），补充为P2-9.3+P2-9.COMP3
  4. 亲自逐个修133—137号（不用subagent）——用132号模板逐个修正
- **修正统计**：132—137号共386项D1-D4标注、346处边界情况、38处覆盖标准
- **审计结果**：132号可实现性审计（第11维度）全部通过——11.1每项标注D1-D4 ✅ / 11.2每项附边界情况 ✅ / 11.3每项明确覆盖标准 ✅ / 11.4 F3检查通过 ✅
- **修正效果**：F1通过D1-D4深度等级消除 / F2通过边界情况清单消除 / F3通过F3检查发现并补充遗漏项消除 / 审计方法从覆盖性升级为覆盖性+可实现性
- **审计报告**：142号文档

### AI数学工程数据基座转向（231号，2026-08-07）

- **新增文档**：`dev-docs/231-v0-2026-08-07-AI数学工程的数据基座转向-从语料喂养到双重知识生产.md`
- **核心结论**：在230号综合闭环之外，补上数学知识素材的“材料论基础”。同一批习题、解答、教材和证明材料应发生两次转化：一条进入模型训练，形成AI的黑盒模式识别能力；另一条进入系统抽取，形成白盒、规范化、可执行、可证书化的数据基座。
- **对230号的补充**：下一步矩条件极差题样例不应只验证闭环求解，还应同时验证数据基座抽取，沉淀处境对象、语义移动、局部证书目标、经典计算任务、失败边界和可迁移模式模板。

### 对238与239的分析及系统设计原语目录方案（240-241号，2026-08-07）

- **新增文档**：
  - `dev-docs/240-v0-2026-08-07-对238与239的分析.md`（对238引导式提问框架与239形式化边界推进系统的对比分析）
  - `dev-docs/241-v1-2026-08-07-系统设计原语目录方案.md`（系统设计原语目录方案）
- **240号核心结论**：238有empirical core（guided_001验证的提问激活效应）但非特定性危机（218）未修复；239有深层结构（形式化边界、经典计算作为生产者、证书系统）但未测试且丢了提问激活效应。建议先跑guided_003（纯非特定Q序列）再建239闭环基础设施。
- **241号核心产出**：
  - 理念层三面相：面相1（两种计算）、面相2（语料双路径）、面相3（Pipeline网络中的Pipe——本次新增，同时修正238和239的盲区）
  - 系统设计过程两面相：面相A（实践涌现的原语）、面相B（从人类知识海洋选取的原语）
  - 提出建立 `primitives/` 目录：每个原语一个markdown文件，带验证状态（tested/untested/borrowed_unoperationalized），防止原语目录变成另一个"有道理但没测试的漂亮概念集合"
  - 第一批写5个核心原语：non-specificity / continuous-questioning / formalization-boundary / pipe / cognitive-activation
- **AGENTS.md索引同步**：新增240、241号文档索引条目
