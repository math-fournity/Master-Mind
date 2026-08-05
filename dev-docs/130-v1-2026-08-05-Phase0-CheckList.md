# 130-Phase 0 Check List：冻结legacy与统一语义

> **文档定位**：从124号拆出的Phase 0独立Check List。Phase 0目标——先停止概念漂移，不改生产运行时。
>
> **入口门**：123号v1已是最高架构基线。
>
> **出口门**：术语、字段、权限和版本规则通过审计；没有原地清空或迁移旧集合；123号10条架构裁决全部在schema中体现。
>
> **失败回滚**：继续把现有系统称作静态重建器，不启动新数据写入。
>
> **来源追溯**：123号第四十五节、plan"Phase crosswalk与迁移门"

---

## P0-1 将七步骤标记为`legacy-static`

> 来源：123号§45 + plan"数据与旧资产迁移原则" + 系统探讨.md§12

- [x] **P0-1.1**：在`seven_step_pipeline.py`文件头部注释中标记`legacy-static`，说明"保留静态重建价值，不再承担主运行时" —— 证据：`seven_step_pipeline.py:1-7`
- [x] **P0-1.2**：在AGENTS.md"七步骤工作流"节确认已标注legacy —— 证据：`AGENTS.md:366` "[legacy-static]"
- [x] **P0-1.3**：在`cognition_units_math.json`中确认`seven_step_workflow`的status已是`legacy` —— 证据：JSON中status="legacy"

### 完整性标准（129号审计后补充）

- [x] **P0-1.4**：给出旧七步骤→新12步运行时的迁移映射表（7行对应表） —— 证据：AGENTS.md"七步骤工作流"节迁移映射表

---

## P0-2 将TopologyVerifier定义为结构保真验证

> 来源：123号§45 + plan"TopologyVerifier保留集合保真功能，但重命名其语义边界"

- [x] **P0-2.1**：在`topology_verifier.py`文件头部注释中明确"结构保真验证=输出骨架不遗漏输入图节点/边，不代表语义或数学正确" —— 证据：`topology_verifier.py:1-4`
- [x] **P0-2.2**：在AGENTS.md"TopologyVerifier拓扑覆盖验证"节确认措辞不含"数学正确"宣称 —— 证据：`AGENTS.md:416` "[结构保真验证]"
- [x] **P0-2.3**：在`cognition_units_math.json`中`topology_coverage`和`topology_verifier`的key_cognition确认含"结构保真"限定 —— 证据：JSON已更新

---

## P0-3 冻结`dg_*`现状和模式统计

> 来源：123号§45 + plan"dg_nodes/dg_edges/loops冻结为legacy/candidate来源"

- [x] **P0-3.1**：执行只读盘点脚本，统计`dg_nodes`的type/label分布、`dg_edges`的edge_type分布、`loops`的graph分布 —— 证据：126号文档§2
- [x] **P0-3.2**：统计`dg_nodes`中按`is_knowledge/is_trace/is_heuristic/is_evidence/is_execution`五类拆分的初步归类 —— 证据：126号文档§3
- [x] **P0-3.3**：记录`dg_*`的schema字段清单 —— 证据：126号文档§4
- [x] **P0-3.4**：把统计结果落盘到126号文档 —— 证据：`126-v1-2026-08-05-dg星图只读盘点报告.md`
- [x] **P0-3.5**：在AGENTS.md Handover Section更新dg_*统计为冻结时点值 —— 证据：`AGENTS.md:751`

---

## P0-4 定义8类schema

> 来源：123号§14—§31 + plan"目标架构：五个协同平面、六个核心数学对象"

- [x] **P0-4.1**：定义Task schema —— 证据：127号§1
- [x] **P0-4.2**：定义Workspace schema —— 证据：127号§2
- [x] **P0-4.3**：定义Event schema —— 证据：127号§3
- [x] **P0-4.4**：定义Obligation schema —— 证据：127号§4
- [x] **P0-4.5**：定义Representation schema —— 证据：127号§5
- [x] **P0-4.6**：定义Evidence schema —— 证据：127号§6
- [x] **P0-4.7**：定义HeuristicRule schema —— 证据：127号§7
- [x] **P0-4.8**：定义Visibility schema —— 证据：127号§8
- [x] **P0-4.9**：把8个schema定义落盘到127号文档 —— 证据：`127-v1-2026-08-05-Schema冻结与角色隔离矩阵.md`

### 完整性标准（129号审计后补充）

- [x] **P0-4.10**：给出原文数据对象到严格模式的crosswalk（10行对应表） —— 证据：127号§13
- [x] **P0-4.11**：给出12步运行时与原文11阶段的crosswalk（12行对应表） —— 证据：127号§14

---

## P0-5 建立Truth Vault与角色隔离矩阵

> 来源：123号§28 + plan"角色数据可见性与非干扰矩阵"

- [x] **P0-5.1**：定义Truth Vault的collection名和读写权限 —— 证据：127号§10.1
- [x] **P0-5.2**：定义Runner可见的collection白名单 —— 证据：127号§10.2
- [x] **P0-5.3**：在schema冻结文档中记录可见性矩阵（8×14） —— 证据：127号§10.3
- [x] **P0-5.4**：定义Solver的可见性边界 —— 证据：127号§10.4
- [x] **P0-5.5**：定义Event Capture/Trace Modeler的可见性边界 —— 证据：127号§10.5
- [x] **P0-5.6**：定义State Reducer的可见性边界 —— 证据：127号§10.6
- [x] **P0-5.7**：定义Retriever的可见性边界 —— 证据：127号§10.7
- [x] **P0-5.8**：定义Heuristic Matcher/Policy的可见性边界 —— 证据：127号§10.8
- [x] **P0-5.9**：定义Verifier的可见性边界 —— 证据：127号§10.9
- [x] **P0-5.10**：定义Auditor的可见性边界 —— 证据：127号§10.10
- [x] **P0-5.11**：定义Orchestrator的可见性边界 —— 证据：127号§10.11
- [x] **P0-5.12**：把8个角色的逐组件最小输入/输出契约写入schema冻结文档 —— 证据：127号§10.4—10.11
- [x] **P0-5.13**：定义角色隔离的运行时强制机制（CapabilityToken） —— 证据：127号§10.6

---

## P0-6 取消L1/L2/L3=v1/v2/v3的错误映射

> 来源：123号§45 + plan"L1/L2/L3保留为历史标注，但拆为5个正交字段"

- [x] **P0-6.1**：在`cognition_units_math.json`中确认L1/L2/L3不再作为版本号使用 —— 证据：JSON确认
- [x] **P0-6.2**：在AGENTS.md中确认"三层提取"节的措辞不含"L1=v1, L2=v2, L3=v3" —— 证据：`AGENTS.md:426`
- [x] **P0-6.3**：在认知图中确认`cayley_hamilton`的版本链不再标注为"L1/L2/L3" —— 证据：cayley_hamilton不在JSON中（已丢失），重建时使用正确版本语义

### 完整性标准（129号审计后补充）

- [x] **P0-6.4**：建立5正交字段设计（semantic_role/abstraction_level/reuse_scope/evidence_level/intervention_effect）替代L1/L2/L3版本映射 —— 证据：127号§12

---

## P0-7 建立candidate/validated/published/retired生命周期

> 来源：123号§21/§44 + plan"candidate/validated/published/retired生命周期"

- [x] **P0-7.1**：定义4个生命周期的进入条件和允许操作 —— 证据：127号§9
- [x] **P0-7.2**：在HeuristicRule schema中增加`lifecycle_status`字段 —— 证据：127号§7 `status`字段
- [x] **P0-7.3**：在schema冻结文档中记录生命周期状态机 —— 证据：127号§9

---

## P0-9 现有文件后续职责冻结

> 来源：123号§53(现有文件的后续职责) + plan"后续实施的代码影响图"
> 129号审计遗漏项：130号只覆盖了seven_step_pipeline.py和topology_verifier.py，缺少其余4个文件

- [x] **P0-9.1**：`seven_step_pipeline.py` → 兼容legacy-static入口，不承载新闭环 —— 证据：P0-1已完成
- [x] **P0-9.2**：`topo_generator.py` → 保留为legacy静态路线复制/排序器；不再全图展开生产知识库；纯函数经契约测试后才可被新编译器复用 —— 证据：AGENTS.md已标注legacy-static
- [x] **P0-9.3**：`topology_verifier.py` → 集合保真API，文档不得宣称数学正确 —— 证据：P0-2已完成
- [x] **P0-9.4**：`arangodb_init.py` → 不用truncate式旧导入改新schema；新模式走版本化migration —— 证据：P0-8.1已改为upsert模式
- [x] **P0-9.5**：`cognition_sdk_math.py` → 项目工作认知控制面，不混入数学运行状态 —— 证据：AGENTS.md"四类载体分工"节明确
- [x] **P0-9.6**：`test_dependency_graph.py` → 保留legacy图回归，不作为动态研究系统验收 —— 证据：AGENTS.md已标注legacy

### 完整性标准

- [x] **P0-9.COMP**：123号§53的6个文件后续职责全部冻结（plan要求）
- [x] **P0-9.COMP2**：不立即把topo_generator改造成动态编译器（123号§33："新Context Compiler先定义独立契约；稳定后才能复用旧模块中的纯结构函数"）

---

## P0-10 数据迁移原则冻结

> 来源：123号§55(数据迁移原则) + plan"旧dg_*不原地迁移"
> 129号审计遗漏项：130号只覆盖了dg_*只读盘点，缺少数据迁移原则的完整冻结

- [x] **P0-10.1**：旧`dg_nodes/dg_edges/loops`不原地清空 —— 证据：P0-3只读盘点，未修改数据
- [x] **P0-10.2**：先用只读adapter生成candidate K投影（Phase 5实现P5-8，Phase 0只冻结原则） —— 证据：124号总览NO-10
- [x] **P0-10.3**：新collection用幂等、可回滚migration创建（Phase 1起执行） —— 证据：131号P1-3.2
- [x] **P0-10.4**：relation document承载高阶规则，participant edges保留内部结构（Phase 3起执行） —— 证据：132号P2-3.4
- [x] **P0-10.5**：生产图、候选图、实验快照分开（Phase 1起执行） —— 证据：127号§10可见性矩阵
- [x] **P0-10.6**：历史POC材料保留原貌和可信度标签 —— 证据：126号§6冻结声明"盘点后dg_*数据冻结为只读"

### 完整性标准

- [x] **P0-10.COMP**：123号§55的6条数据迁移原则全部冻结
- [x] **P0-10.COMP2**：不原地清空或迁移旧dg_*集合（NO-10约束）

---

## P0-11 不在Phase 0一次性搭空框架

> 来源：123号§54(按Phase建立独立运行时包) + NO-9约束
> 129号审计遗漏项：130号没有显式验证NO-9约束

- [x] **P0-11.1**：Phase 0不创建`xishujuzhen/research_runtime/`包（Phase 1首次创建） —— 证据：research_runtime/不存在
- [x] **P0-11.2**：Phase 0不创建新ArangoDB collection（Phase 1起创建raw_events/semantic_events等） —— 证据：ArangoDB中无新collection
- [x] **P0-11.3**：Phase 0只冻结schema定义，不实现运行时 —— 证据：127号只定义schema，无运行时代码

### 完整性标准

- [x] **P0-11.COMP**：不在Phase 0一次性搭空框架（NO-9约束："每个模块只有在前一入口门通过后创建"）

---

## P0-8 数据丢失修复（项目治理补充）

> 来源：事件2026-08-05-A数据丢失事故，非123号架构要求

- [x] **P0-8.1**：改`cognition_import_math.py`为merge/upsert模式，不truncate —— 证据：`cognition_import_math.py`已改为upsert+orphan检测
- [x] **P0-8.2**：新增`cognition_export_math.py`（ArangoDB→JSON双向同步） —— 证据：`cognition_export_math.py`已创建
- [x] **P0-8.3**：在`cognition_sdk_math.py`的`add_unit()`中增加审计日志 —— 证据：`cognition_sdk_math.py:373` `_audit_log()`方法
- [x] **P0-8.4**：配置arangodump定期备份到`/data/master-mind/backups/arango/` —— 证据：`arango_backup.sh`已创建

---

## 出口门

- [x] **P0-EXIT-1**：术语、字段、权限和版本规则通过审计 —— 证据：129号审计报告
- [x] **P0-EXIT-2**：没有原地清空或迁移旧集合（dg_nodes=1719, dg_edges=1483, loops=4） —— 证据：129号审计报告§2.3
- [x] **P0-EXIT-3**：123号v1的10条架构裁决全部在schema中得到体现 —— 证据：127号§11

---

## 完整性标准（129号审计后补充的跨Phase项）

- [x] **P0-COMP-1**：验证`系统探讨.md` SHA-256与123号§1记录一致 —— 证据：129号§1.3（SHA-256=`a2ac4dc1...`）
- [x] **P0-COMP-2**：G0-1事件清单覆盖123号§17定义的全部14种语义事件类型 —— 证据：128号§1.5

---

## Phase 0状态

**已完成**。出口门全部通过（commit `af0276f` + `89a5c36`）。129号审计报告记录了7项遗漏并全部修正。
