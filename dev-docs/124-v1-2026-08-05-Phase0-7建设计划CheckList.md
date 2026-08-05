# 124-Phase 0—7建设计划Check List

> **文档定位**：123号v1架构基线的可执行Check List。把123号第十部分Phase 0—7、第九部分DYN-0—7、第十二部分停止条件与不做清单、第十三部分"下一实施包"全部细化为可追踪的Check List条目。
>
> **使用方式**：每个Phase有入口门、Check List（细化为可执行子项）、出口门、停止条件和失败回滚。按Phase顺序推进，前一Phase出口门通过后才进入下一Phase。Check List条目完成后标记`[x]`并附证据定位（文件:行或commit hash）。
>
> **与123号的关系**：本文件是123号的执行视图，不修改123号的架构定义。123号是"是什么和为什么"，本文件是"做什么和做到什么程度"。

---

## 全局预注册门（适用于所有Phase）

> 123号第四十四节：阈值不能在看完结果后补写。每个DYN protocol先用独立pilot估计方差，再冻结最小实际效应δ、样本量、排除标准和区间估计方法。

- [ ] **G0-1**：在Phase 1开始前，定义"关键事件"的完整清单（哪些工具调用、哪些文本段落、哪些分支点必须捕获）
- [ ] **G0-2**：在Phase 2开始前，冻结状态字段的Krippendorff α阈值（首版建议：关键状态字段α≥0.80，无关键字段低于0.67）
- [ ] **G0-3**：在Phase 4开始前，冻结DYN-3最小实际效应δ、样本量、排除标准和区间估计方法
- [ ] **G0-4**：在Phase 4开始前，冻结泄漏门阈值（Hint的答案信息量上限）
- [ ] **G0-5**：published通用规则至少跨3个未参与设计的问题族和2个模型版本复现——此标准在Phase 4出口门前冻结
- [ ] **G0-6**：具体阈值若调整，必须产生新protocol版本，不能回改历史

---

## Phase 0：冻结legacy与统一语义

> **目标**：先停止概念漂移，不改生产运行时。
>
> **入口门**：123号v1已成为项目最高架构基线，AGENTS.md/ChangeLog/认知图已同步。

### Check List

#### P0-1 将七步骤标记为`legacy-static`

- [ ] **P0-1.1**：在`seven_step_pipeline.py`文件头部注释中标记`legacy-static`，说明"保留静态重建价值，不再承担主运行时"
- [ ] **P0-1.2**：在AGENTS.md"数学大师系统技术说明>七步骤工作流"节确认已标注legacy
- [ ] **P0-1.3**：在`cognition_units_math.json`中确认`seven_step_workflow`的status已是`legacy`（当前已是）

#### P0-2 将TopologyVerifier定义为结构保真验证

- [ ] **P0-2.1**：在`topology_verifier.py`文件头部注释中明确"结构保真验证=输出骨架不遗漏输入图节点/边，不代表语义或数学正确"
- [ ] **P0-2.2**：在AGENTS.md"TopologyVerifier拓扑覆盖验证"节确认措辞不含"数学正确"宣称
- [ ] **P0-2.3**：在`cognition_units_math.json`中`topology_coverage`和`topology_verifier`的key_cognition确认含"结构保真"限定

#### P0-3 冻结`dg_*`现状和模式统计

- [ ] **P0-3.1**：执行只读盘点脚本，统计`dg_nodes`的type/label分布、`dg_edges`的edge_type分布、`loops`的graph分布
- [ ] **P0-3.2**：统计`dg_nodes`中按`is_knowledge/is_trace/is_heuristic/is_evidence/is_execution`五类拆分的初步归类（只读，不改数据）
- [ ] **P0-3.3**：记录`dg_*`的schema字段清单（每个collection的实际字段名和类型）
- [ ] **P0-3.4**：把统计结果落盘到`dev-docs/125-`号文档（只读盘点报告）
- [ ] **P0-3.5**：在AGENTS.md Handover Section更新dg_*统计为冻结时点值

#### P0-4 定义任务、工作区、事件、义务、表示、证据、规则和visibility schema

- [ ] **P0-4.1**：定义Task schema（task_id, type, domain, objects, premises, goal, success_conditions, stop_conditions）——123号第十四节
- [ ] **P0-4.2**：定义Workspace schema（V/F/O/R/D/E六类工作区）——123号第十五节
- [ ] **P0-4.3**：定义Event schema（event_id, type, timestamp, workspace_ref, payload, causal_predecessors, content_hash）——123号第十七节
- [ ] **P0-4.4**：定义Obligation schema（AND/OR有向超图，obligation_id, type, status, sub_obligations, evidence_refs）——123号第十六节
- [ ] **P0-4.5**：定义Representation schema（rep_id, source_form, target_form, soundness_obligation, domain）——123号第十九节
- [ ] **P0-4.6**：定义Evidence schema（evidence_id, type, status, source_event, confidence, conflicts）——123号第三十一节
- [ ] **P0-4.7**：定义HeuristicRule schema（rule_id, LHS, interface, RHS, guard, status, effect_evidence,适用问题族, 模型版本, 失败案例）——123号第二十一节
- [ ] **P0-4.8**：定义Visibility schema（role, visible_collections, visible_fields, write_permissions）——123号第二十八节
- [ ] **P0-4.9**：把8个schema定义落盘到`dev-docs/126-`号文档（schema冻结文档）

#### P0-5 建立Truth Vault与Runner可见性边界

- [ ] **P0-5.1**：定义Truth Vault的collection名和读写权限（Truth Curator只写，Runner不可见）
- [ ] **P0-5.2**：定义Runner可见的collection白名单（不含Truth Vault、不含答案等价内容）
- [ ] **P0-5.3**：在schema冻结文档中记录可见性矩阵（7个角色 × N个collection）

#### P0-6 取消L1/L2/L3=v1/v2/v3的错误映射

- [ ] **P0-6.1**：在`cognition_units_math.json`中确认L1/L2/L3不再作为版本号使用（当前JSON中`three_layer_extraction`的key_cognition已不含v1/v2/v3映射）
- [ ] **P0-6.2**：在AGENTS.md中确认"三层提取"节的措辞不含"L1=v1, L2=v2, L3=v3"
- [ ] **P0-6.3**：在认知图中确认`cayley_hamilton`的版本链不再标注为"L1/L2/L3"（注意：该单元在事件2026-08-05-A中丢失，需重建时使用正确版本语义）

#### P0-7 建立candidate/validated/published/retired生命周期

- [ ] **P0-7.1**：定义4个生命周期的进入条件和允许操作
  - candidate：离线发现，禁止在线自动提示
  - validated：通过DYN-3因果实验且泄漏门通过
  - published：通过DYN-4跨题迁移，至少跨3个未参与设计的问题族和2个模型版本复现
  - retired：模型漂移、反例发现或更好规则替代
- [ ] **P0-7.2**：在HeuristicRule schema中增加`lifecycle_status`字段
- [ ] **P0-7.3**：在schema冻结文档中记录生命周期状态机

#### P0-8 数据丢失修复（事件2026-08-05-A的待修复项）

- [ ] **P0-8.1**：改`cognition_import_math.py`为merge/upsert模式，不truncate
- [ ] **P0-8.2**：新增`cognition_export_math.py`（ArangoDB→JSON双向同步）
- [ ] **P0-8.3**：在`cognition_sdk_math.py`的`add_unit()`中增加审计日志
- [ ] **P0-8.4**：配置arangodump定期备份到`/data/master-mind/backups/arango/`

**出口门**：
- [ ] **P0-EXIT-1**：术语、字段、权限和版本规则通过审计（对照schema冻结文档逐项检查）
- [ ] **P0-EXIT-2**：没有原地清空或迁移旧集合（`dg_*`数据未变，只做只读盘点）
- [ ] **P0-EXIT-3**：123号v1的10条架构裁决全部在schema中得到体现

**失败回滚**：继续把现有系统称作静态重建器，不启动新数据写入。

---

## Phase 1：只观察，不提示

> **目标**：完成DYN-0（事件捕获真实性）。
>
> **入口门**：Phase 0出口门全部通过。

### Check List

#### P1-1 创建运行manifest

- [ ] **P1-1.1**：定义manifest格式（run_id, task_id, model_version, tool_versions, budget, permissions, timestamp_start, timestamp_end）
- [ ] **P1-1.2**：实现manifest创建脚本（`xishujuzhen/research_runtime/manifest.py`，Phase 0不预创建目录，此处为Phase 1首次创建）
- [ ] **P1-1.3**：manifest落盘到`xishujuzhen/research_runtime/runs/<run_id>/manifest.json`

#### P1-2 捕获公开文本和工具事件

- [ ] **P1-2.1**：定义事件捕获接口（哪些API调用、哪些文本输出、哪些工具调用需要捕获）
- [ ] **P1-2.2**：实现事件捕获器（hook到Devin CLI的tool调用、subagent输出、文件写入等）
- [ ] **P1-2.3**：验证捕获不遗漏关键事件类型（对照G0-1的"关键事件"清单）

#### P1-3 建立不可变原始事件

- [ ] **P1-3.1**：定义原始事件collection schema（event_id, type, timestamp, raw_payload, content_hash, run_id）
- [ ] **P1-3.2**：在ArangoDB中创建`raw_events` collection（新collection，不动旧数据）
- [ ] **P1-3.3**：实现事件写入接口（append-only，不允许修改或删除）
- [ ] **P1-3.4**：验证content_hash的正确性（同内容同hash，不同内容不同hash）

#### P1-4 建立语义事件抽取版本

- [ ] **P1-4.1**：定义语义事件schema（在原始事件基础上增加抽取的字段：workspace_ref, obligation_ref, evidence_ref等）
- [ ] **P1-4.2**：在ArangoDB中创建`semantic_events` collection
- [ ] **P1-4.3**：实现语义抽取器（从原始事件中识别命题、义务、表示、证据和拒绝分支）
- [ ] **P1-4.4**：验证抽取失败不会丢失原始证据（原始事件保留，语义事件可重抽）

#### P1-5 建立内容寻址checkpoint

- [ ] **P1-5.1**：定义checkpoint格式（序列化Q_0/W_t、关键事件前缀、模型/工具/权限/预算和版本哈希）
- [ ] **P1-5.2**：实现checkpoint创建和存储
- [ ] **P1-5.3**：验证checkpoint不含LLM隐藏内部状态（只含公开产物）

#### P1-6 验证重放与来源追溯

- [ ] **P1-6.1**：从checkpoint重放后续continuation（同一checkpoint可产生多个continuation）
- [ ] **P1-6.2**：每个语义事件可追溯到原始事件（event_id链）
- [ ] **P1-6.3**：每个原始事件可追溯到manifest和run_id

#### P1-7 记录"不要求隐藏CoT"的协议

- [ ] **P1-7.1**：在实验protocol文档中明确声明"不要求或伪造隐藏chain-of-thought"
- [ ] **P1-7.2**：在manifest中记录"hidden_cot_required: false"

**出口门**：
- [ ] **P1-EXIT-1**：关键事件可重放（从checkpoint恢复到同一可观测状态）
- [ ] **P1-EXIT-2**：原始证据无丢失（抽取失败时原始事件仍在）
- [ ] **P1-EXIT-3**：DYN-0验收4条全部通过（原始输出/工具/提示/时间/分支可定位、事件可回放、不要求隐藏CoT、抽取失败不丢原始证据）

**停止条件**：关键工具或分支无法稳定捕获，则不进入状态建模（Phase 2）。

---

## Phase 2：类型化状态与研究义务

> **目标**：完成DYN-1（状态重建一致性）和DYN-2（卡点检测校准）。
>
> **入口门**：Phase 1出口门全部通过。

### Check List

#### P2-1 解析Q_0的任务类型、对象、前提、目标和成功条件

- [ ] **P2-1.1**：选定第一个实验用任务Q_0（候选：Ramsey修正版材料，但用新protocol不是继续POC-6）
- [ ] **P2-1.2**：用Task schema（P0-4.1）解析Q_0的7个字段
- [ ] **P2-1.3**：定义Q_0的success_conditions（不只是"答对"，而是"已验证进展"的分级标准）

#### P2-2 实现`V/F/O/R/D/E`工作区

- [ ] **P2-2.1**：定义6类工作区的collection schema（V=可见上下文, F=形式化目标, O=开放义务, R=表示, D=数据/工具, E=证据）
- [ ] **P2-2.2**：在ArangoDB中创建6个workspace collection
- [ ] **P2-2.3**：实现工作区读写接口

#### P2-3 建立AND/OR研究义务

- [ ] **P2-3.1**：定义义务类型（验证核心 vs 猜想前沿，AND义务 vs OR义务）
- [ ] **P2-3.2**：实现义务图构建（从语义事件中提取义务关系）
- [ ] **P2-3.3**：验证义务图是DAG（无环，环路在状态商空间处理）

#### P2-4 区分验证核心和猜想前沿

- [ ] **P2-4.1**：在Task schema中增加`verification_core`和`conjecture_frontier`字段
- [ ] **P2-4.2**：对Q_0标注哪些义务是验证核心、哪些是猜想前沿

#### P2-5 建立证据状态模型和冲突状态

- [ ] **P2-5.1**：用Evidence schema（P0-4.6）定义证据状态（confirmed/partial/contradicted/insufficient）
- [ ] **P2-5.2**：定义冲突状态（两个证据指向矛盾结论时的状态标记）
- [ ] **P2-5.3**：实现证据状态更新接口

#### P2-6 多观察者重建一致性测试

- [ ] **P2-6.1**：用2个以上独立抽取器对同一事件流做状态重建
- [ ] **P2-6.2**：计算字段级Krippendorff α（对照G0-2的阈值）
- [ ] **P2-6.3**：记录分歧案例和仲裁结果

#### P2-7 卡点类型和校准集

- [ ] **P2-7.1**：定义7类卡点（必要探索/语义重复/矛盾未处理/工具阻塞/表示不合适/策略耗尽/预算耗尽）
- [ ] **P2-7.2**：对Q_0的多个运行标注卡点类型（人工标注校准集）
- [ ] **P2-7.3**：实现卡点检测器
- [ ] **P2-7.4**：测precision、recall、误触发时间和"把正常探索误判为停滞"的比例

**出口门**：
- [ ] **P2-EXIT-1**：状态重建Krippendorff α≥0.80且无关键字段低于0.67
- [ ] **P2-EXIT-2**：卡点检测不把正常探索大量误判为停滞（误判率低于预注册阈值）
- [ ] **P2-EXIT-3**：DYN-1和DYN-2验收全部通过

**失败回滚**：保留事件日志，停止H建设，改进抽取与状态本体。

---

## Phase 3：离线候选启发

> **目标**：发现候选规则，但绝不在线自动提示。
>
> **入口门**：Phase 2出口门全部通过。

### Check List

- [ ] **P3-1**：对齐多个成功/失败状态，而非只对齐最终答案（用Phase 2的状态重建结果）
- [ ] **P3-2**：找稳定共同状态和首个关键分叉（成功运行和失败运行在哪个checkpoint开始分叉）
- [ ] **P3-3**：抽取LHS/interface/RHS/guard（用HeuristicRule schema P0-4.7）
- [ ] **P3-4**：设计H0—H2激活包（H0=元检查, H1=思维操作, H2=概念/工具候选）
- [ ] **P3-5**：独立答案等价性审计（Hint不唯一确定答案）
- [ ] **P3-6**：泄漏审计（Hint的答案信息量低于预注册阈值G0-4）
- [ ] **P3-7**：记录适用问题族、模型和失败案例
- [ ] **P3-8**：candidate规则禁止自动发布（lifecycle_status=candidate，不进入在线运行时）

**出口门**：
- [ ] **P3-EXIT-1**：至少一个候选在多个运行中可重复匹配
- [ ] **P3-EXIT-2**：Hint不唯一确定答案（泄漏门通过）

---

## Phase 4：最小Hint因果实验

> **目标**：完成DYN-3（最小干预）、DYN-4（帮助量响应曲线）和DYN-5（跨题迁移）的首轮。
>
> **入口门**：Phase 3出口门全部通过。预注册门G0-3/G0-4/G0-5已冻结。

### Check List

- [ ] **P4-1**：同内容哈希checkpoint分层并随机分配多个非确定continuation
- [ ] **P4-2**：无提示/H0/H1/H2四组处理
- [ ] **P4-3**：冻结模型、工具、题面和预算（实验期间不变）
- [ ] **P4-4**：完整日志、哈希、盲评和Truth Vault隔离
- [ ] **P4-5**：测局部效应（同一checkpoint的treatment vs control）
- [ ] **P4-6**：测帮助量曲线（success/verified_progress = f(assistance budget)）
- [ ] **P4-7**：新题迁移（未参与设计的迁移题上复现）
- [ ] **P4-8**：记录负效应和无效规则
- [ ] **P4-9**：通过后才升为validated/transferred

**出口门**：
- [ ] **P4-EXIT-1**：非泄漏Hint的预注册主要效应区间下界高于0且超过最小实际效应δ
- [ ] **P4-EXIT-2**：该结果在未参与设计的迁移题上复现
- [ ] **P4-EXIT-3**：副作用低于预注册阈值
- [ ] **P4-EXIT-4**：published通用规则至少跨3个未参与设计的问题族和2个模型版本复现

**停止条件**：去掉答案等价内容后增益消失，则不建设大规模H库。

---

## Phase 5：检索、Context Compiler与验证路由

> **目标**：让系统只给当前一步真正需要的数据。
>
> **入口门**：Phase 4出口门全部通过。

### Check List

- [ ] **P5-1**：冷/温/热/微包访问（123号第二十九节）
- [ ] **P5-2**：类型与前提优先检索
- [ ] **P5-3**：表示映射和按需展开
- [ ] **P5-4**：每段上下文来源/证据/权限/token记录
- [ ] **P5-5**：SymPy/Sage/Lean能力注册
- [ ] **P5-6**：命题级验证路由
- [ ] **P5-7**：裁剪清单和最小性审计
- [ ] **P5-8**：legacy图只读adapter（`dg_*`通过adapter提供K投影，不原地迁移）

**出口门**：
- [ ] **P5-EXIT-1**：每个激活包可追溯、可验证、可裁剪
- [ ] **P5-EXIT-2**：不预载未来答案路线

---

## Phase 6：在线受约束Agent M

> **目标**：完成DYN-6（在线闭环控制器）。
>
> **入口门**：Phase 5出口门全部通过。

### Check List

- [ ] **P6-1**：只加载published规则（candidate/validated不进入在线运行时）
- [ ] **P6-2**：支持继续观察、诊断、工具、提示、停止5类动作
- [ ] **P6-3**：预算和帮助依赖控制
- [ ] **P6-4**：错误状态恢复
- [ ] **P6-5**：模型版本分层和规则衰减
- [ ] **P6-6**：gaming检测（Agent是否迎合触发器以获取帮助）
- [ ] **P6-7**：长期归因（不把长程信用错误归给最近一次提示）
- [ ] **P6-8**：回滚到反应式模式（闭环失败时退回先观察再干预）

**出口门**：
- [ ] **P6-EXIT-1**：闭环长期收益为正
- [ ] **P6-EXIT-2**：且不靠更高泄漏或无限帮助获得

---

## Phase 7：表示运输、长证明和高级数学分析

> **目标**：完成DYN-7（跨领域与长证明编排）并打开远期数学研究线。
>
> **入口门**：Phase 6出口门全部通过。

### Check List

- [ ] **P7-1**：类型化`representation_maps`和soundness义务
- [ ] **P7-2**：费马型跨域模块编排（先"给定半稳定模性推出FLT"，再逐层隐去Frey和Ribet桥梁，最后才研究Wiles级模块接口）
- [ ] **P7-3**：证明路径等价和交换图
- [ ] **P7-4**：局部视图一致性与层式粘合实验
- [ ] **P7-5**：e-graph等价表达式管理
- [ ] **P7-6**：几何/最优运输轨迹对齐
- [ ] **P7-7**：数据充分后做TDA（不在状态空间未定义时宣称找到同调洞）
- [ ] **P7-8**：只有形式对象充分时研究HoTT实现

**出口门**：
- [ ] **P7-EXIT-1**：高级数学方法对明确指标有增益
- [ ] **P7-EXIT-2**：不只是更漂亮的术语

---

## 项目级停止条件（适用于所有Phase）

> 123号第五十八节。出现下列任一情况，应停止扩大H和知识规模：

- [ ] **STOP-1**：公开产物不能稳定重建状态
- [ ] **STOP-2**：卡点检测误报使正常探索被频繁打断
- [ ] **STOP-3**：去除答案等价信息后，Hint增益消失
- [ ] **STOP-4**：效果只在原题或单一模型上存在
- [ ] **STOP-5**：正确率提升以更高泄漏或依赖为代价
- [ ] **STOP-6**：Verifier无法判断关键进展，系统只能靠语言评分
- [ ] **STOP-7**：高级数学表示没有带来可测量收益

**诚实终态**：若核心假设不成立，诚实终态可以是"一个高质量数学知识、证明路线和静态上下文编译器，而不是动态思维矫正器"。

---

## 明确不做清单（适用于所有Phase）

> 123号第五十九节。

- **NO-1**：不先扩张到325000知识节点再验证核心闭环
- **NO-2**：不把完整答案路线改写成"意识"后继续做B组提示
- **NO-3**：不用节点覆盖率代替数学正确或研究能力
- **NO-4**：不要求或伪造隐藏chain-of-thought
- **NO-5**：不让同一Master同时持有答案、设计Hint、运行Solver和评分
- **NO-6**：不把L1/L2/L3当成同一认知单元的版本号
- **NO-7**：不在状态空间未定义时宣称找到了同调洞
- **NO-8**：不让在线一次成功自动写入production H
- **NO-9**：不在Phase 0一次性搭空框架（每个模块只有在前一入口门通过后创建）
- **NO-10**：不原地清空或迁移旧`dg_*`集合（用只读adapter生成candidate K投影）

---

## 下一实施包（Phase 0首批可执行项）

> 123号第十三部分"下一实施包"。这些是Phase 0中可以立即开始的条目。

- [ ] **NI-1**：单独形成Phase 0 schema与术语执行文档 → 对应P0-4.9（`dev-docs/126-`号文档）
- [ ] **NI-2**：只读盘点现有`dg_*`模式和数据可信度 → 对应P0-3.1—P0-3.5（`dev-docs/125-`号文档）
- [ ] **NI-3**：设计DYN-0事件协议和最小观察型实验 → 对应Phase 1的P1-1—P1-7
- [ ] **NI-4**：决定第一个可重复卡点问题族 → 对应P2-1.1
- [ ] **NI-5**：以Ramsey修正版材料为候选题族，另建DYN-3同可观测checkpoint分层、分级Hint实验 → 这是新protocol，不是继续或补写尚未完成的POC-6修正版B组，也不能反向把119号结论升级

### 未决问题（需要在Phase 0—1中回答）

> 123号第十三部分"未决问题"。

- [ ] **UQ-1**：哪些公开研究产物足以形成可重建状态，而不依赖隐藏CoT？
- [ ] **UQ-2**：怎样为不同任务类型定义可比较的"已验证进展"？
- [ ] **UQ-3**：如何估计Hint的答案信息量和Agent依赖？
- [ ] **UQ-4**：哪些表示转换可在Lean或其他工具中证明soundness？
- [ ] **UQ-5**：何时高级几何/拓扑分析的数据量足够，而不是过早数学包装？

---

## 进度追踪

| Phase | 状态 | 入口门 | 出口门 | 备注 |
|---|---|---|---|---|
| Phase 0 | 待开始 | 123号v1已是最高基线 | 术语/字段/权限/版本规则审计通过 | 首批实施包：NI-1—NI-5 |
| Phase 1 | 待开始 | Phase 0出口门 | 关键事件可重放、原始证据无丢失 | 完成DYN-0 |
| Phase 2 | 待开始 | Phase 1出口门 | 状态重建α≥0.80、卡点检测校准通过 | 完成DYN-1、DYN-2 |
| Phase 3 | 待开始 | Phase 2出口门 | 候选规则可重复匹配且不泄漏 | 离线候选，禁止在线自动提示 |
| Phase 4 | 待开始 | Phase 3出口门 + 预注册门冻结 | 非泄漏Hint效应区间下界>0且迁移复现 | 完成DYN-3、DYN-4、DYN-5首轮 |
| Phase 5 | 待开始 | Phase 4出口门 | 激活包可追溯、可验证、可裁剪 | Context Compiler |
| Phase 6 | 待开始 | Phase 5出口门 | 闭环长期收益为正且不靠更高泄漏 | 完成DYN-6 |
| Phase 7 | 待开始 | Phase 6出口门 | 高级数学方法对明确指标有增益 | 完成DYN-7 |
