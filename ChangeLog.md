# ChangeLog

本文件记录项目正式编号文档及其索引的新增与修订。从 2026-08-05 开始维护；更早的变更以 Git 历史和各编号文档为准。

## 2026-08-05

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
