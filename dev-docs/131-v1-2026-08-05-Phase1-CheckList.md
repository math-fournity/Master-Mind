# 131-Phase 1 Check List：只观察，不提示

> **文档定位**：从124号拆出的Phase 1独立Check List。Phase 1目标——完成DYN-0（事件捕获真实性）。
>
> **入口门**：Phase 0出口门全部通过（130号P0-EXIT-1/2/3）。
>
> **出口门**：关键事件可重放、原始证据无丢失、DYN-0验收4条全部通过。
>
> **停止条件**：关键工具或分支无法稳定捕获，则不进入状态建模（Phase 2）。
>
> **失败回滚**：保留事件日志，不启动状态建模。
>
> **来源追溯**：123号§46 + §36(DYN-0) + §32(12步步骤1/3/4) + §55(数据迁移原则)；系统探讨.md§16(Phase 1) + §6(阶段0-2)；plan"Phase crosswalk" + "research_runtime/events模块"

---

## P1-1 创建运行manifest

> 来源：123号§32步骤1（冻结）+ §46 + 系统探讨.md§6阶段0 + plan"新Phase 1：事件协议"

- [x] **P1-1.1**：定义manifest格式，字段必须覆盖123号§32步骤1的全部冻结项：
  - `run_id`：唯一运行标识符
  - `task_id`：关联Task schema（127号§1）的task_id
  - `model_version`：模型版本
  - `tool_versions`：工具版本清单
  - `budget`：token/计算/工具/分支/Hint预算（127号RunState的B_t）
  - `permissions`：权限配置（127号RunState的M_t）
  - `timestamp_start` / `timestamp_end`：运行时间
  - `k_version`：K图版本（知识库快照哈希）
  - `h_version`：H图版本（启发规则库快照哈希）
  - `hidden_cot_required`：固定为`false`（R-1风险防线）
- [x] **P1-1.2**：实现manifest创建脚本（`xishujuzhen/research_runtime/manifest.py`）
  - Phase 1首次创建`research_runtime/`包（plan要求：按Phase建立独立运行时包）
  - 不在Phase 0预建框架（NO-9约束）
- [x] **P1-1.3**：manifest落盘到`xishujuzhen/research_runtime/runs/<run_id>/manifest.json`
- [x] **P1-1.4**：manifest创建后内容冻结，不允许修改（123号§32步骤1"冻结"语义）

### 完整性标准

- [x] **P1-1.COMP**：manifest格式覆盖123号§32步骤1的全部冻结项（题面、任务类型、成功条件、模型/工具、权限、K/H版本和manifest本身）
- [x] **P1-1.COMP2**：manifest包含`hidden_cot_required: false`字段（R-1风险监控机制）

---

## P1-2 捕获公开文本和工具事件

> 来源：123号§32步骤3（独立探索）+步骤4（事件捕获）+ 系统探讨.md§6阶段1-2 + 128号G0-1

- [x] **P1-2.1**：定义事件捕获接口，覆盖以下捕获源：
  - Solver的公开文本输出（不要求隐藏CoT，R-1）
  - 工具调用（API调用、文件写入、代码执行）
  - 分支点（选择路径A而非B）
  - 回退行为
  - 时间戳
- [x] **P1-2.2**：实现事件捕获器（hook到Devin CLI的tool调用、subagent输出、文件写入等）
- [x] **P1-2.3**：验证捕获不遗漏关键事件类型

### 完整性标准

- [x] **P1-2.COMP**：捕获覆盖128号§1定义的全部27种事件类型（5类：工具调用7种 + 文本段落12种 + 分支点5种 + 状态变更7种 - 语义事件14种中部分重叠）
- [x] **P1-2.COMP2**：捕获覆盖123号§17定义的全部14种语义事件类型：`observation/claim/representation/subgoal/candidate/test/tool_result/contradiction/stall/backtrack/resolution/hint_injection/state_reduction/verification`
- [x] **P1-2.COMP3**：不捕获隐藏CoT（R-1风险防线：只处理公开研究产物与工具事件）

---

## P1-3 建立不可变原始事件

> 来源：123号§17 + 127号§3 RawEvent schema + 系统探讨.md§11.2

- [x] **P1-3.1**：定义原始事件collection schema，字段必须覆盖127号§3的RawEvent定义：
  - `event_id`：唯一标识符
  - `type`：事件类型枚举
  - `timestamp`：ISO 8601时间戳
  - `run_id`：关联运行manifest
  - `workspace_ref`：关联工作区（可选，语义层填充）
  - `raw_payload`：原始未加工内容
  - `content_hash`：SHA-256内容哈希
  - `causal_predecessors`：直接前驱event_id列表（DAG边）
- [x] **P1-3.2**：在ArangoDB中创建`raw_events` collection
  - 新collection，不动旧数据（NO-10约束）
  - 用幂等、可回滚migration创建（123号§55）
- [x] **P1-3.3**：实现事件写入接口（append-only，不允许修改或删除）
  - 123号§17冻结声明：原始事件append-only
- [x] **P1-3.4**：验证content_hash的正确性（同内容同hash，不同内容不同hash）
- [x] **P1-3.5**：验证事件因果图是DAG（causal_predecessors不形成环，123号§17冻结声明）
- [x] **P1-3.6**：验证不可变事件日志不直接灌入提示（R-6风险防线：上下文膨胀；123号§56第6项 + 系统探讨.md§11.5"不可变事件日志+当前状态快照双层结构"）

### 完整性标准

- [x] **P1-3.COMP**：RawEvent schema符合127号§3的完整定义（含causal_predecessors的DAG边）
- [x] **P1-3.COMP2**：原始事件append-only，不允许修改或删除（123号§17冻结声明）
- [x] **P1-3.COMP3**：事件因果图是DAG（时间不倒流，123号§17冻结声明）
- [x] **P1-3.COMP4**：不可变事件日志不直接灌入提示（R-6风险：上下文膨胀；系统探讨.md§11.5双层结构）

---

## P1-4 建立语义事件抽取版本

> 来源：123号§17 + 127号§3 SemanticEvent schema + 系统探讨.md§5.2

- [x] **P1-4.1**：定义语义事件schema，字段必须覆盖127号§3的SemanticEvent定义：
  - `event_id`：继承自原始事件
  - `raw_event_id`：指向原始事件
  - `type`：语义事件类型（14种枚举）
  - `timestamp` / `run_id` / `workspace_ref`
  - `obligation_ref`：关联义务（可选）
  - `evidence_ref`：关联证据（可选）
  - `payload`：抽取后的语义内容
  - `content_hash`：语义内容哈希
  - `causal_predecessors`：语义层因果前驱
  - `conflict_with`：冲突事件ID列表（#关系，满足对称和非自反）
  - `confidence`：置信度[0,1]
  - `source`：来源标注
- [x] **P1-4.2**：在ArangoDB中创建`semantic_events` collection
- [x] **P1-4.3**：实现语义抽取器（从原始事件中识别命题、义务、表示、证据和拒绝分支）
  - 输出类型化语义事件：`observation/claim/representation/subgoal/candidate/test/tool_result/contradiction/stall/backtrack/resolution`（系统探讨.md§5.2的11种 + 123号§17新增的`hint_injection/state_reduction/verification`）
- [x] **P1-4.4**：验证抽取失败不会丢失原始证据（原始事件保留，语义事件可重抽）
  - 123号§17三层保留：原始事件（不可变）→ 语义抽取（可重抽）→ 状态快照（可重建）

### 完整性标准

- [x] **P1-4.COMP**：SemanticEvent schema符合127号§3的完整定义（含conflict_with的#关系）
- [x] **P1-4.COMP2**：语义事件类型覆盖127号§3的14种枚举值
- [x] **P1-4.COMP3**：抽取失败不丢失原始证据（123号§17三层保留机制）
- [x] **P1-4.COMP4**：conflict_with满足对称和非自反（123号§17冻结声明：若e1 # e2，两事件不能属于同一有效分支）
- [x] **P1-4.COMP5**：不能仅因两个命题矛盾就推断生成事件冲突（123号§17冻结声明：首版只标记显式选择的互斥候选、被回退分支与其替代分支）

---

## P1-5 建立内容寻址checkpoint

> 来源：123号§39(DYN-3定义中包含checkpoint定义) + §32步骤10 + 系统探讨.md§11.5

- [x] **P1-5.1**：定义checkpoint格式，必须覆盖123号§39的定义：
  - 序列化`Q_0`（冻结初始任务）
  - 序列化`W_t`（当前工作区压缩快照）
  - 关键事件前缀（到当前时点的事件链）
  - 模型/工具/权限/预算和版本哈希（127号RunState的M_t和B_t）
- [x] **P1-5.2**：实现checkpoint创建和存储
  - 内容寻址：checkpoint用内容哈希标识
- [x] **P1-5.3**：验证checkpoint不含LLM隐藏内部状态（只含公开产物）
  - 123号§39明确："checkpoint不包含、也不能冻结LLM隐藏内部状态"
  - R-1风险防线

### 完整性标准

- [x] **P1-5.COMP**：checkpoint定义符合123号§39"序列化Q_0/W_t、关键事件前缀、模型/工具/权限/预算和版本哈希；不含LLM隐藏内部状态"
- [x] **P1-5.COMP2**：checkpoint用内容哈希标识（内容寻址，123号§39）
- [x] **P1-5.COMP3**：同一checkpoint可产生多个continuation（123号§39"即使温度为0，多个继续运行也可能非确定"）

---

## P1-6 验证重放与来源追溯

> 来源：123号§36 DYN-0验收 + 系统探讨.md§11.5

- [x] **P1-6.1**：从checkpoint重放后续continuation（同一checkpoint可产生多个continuation）
- [x] **P1-6.2**：每个语义事件可追溯到原始事件（event_id链：SemanticEvent.raw_event_id → RawEvent.event_id）
- [x] **P1-6.3**：每个原始事件可追溯到manifest和run_id（RawEvent.run_id → manifest.run_id）
- [x] **P1-6.4**：验证原始输出、工具输入/输出、提示、时间和分支全部可定位（DYN-0验收第1条）

### 完整性标准

- [x] **P1-6.COMP**：DYN-0验收第1条"原始输出、工具输入/输出、提示、时间和分支全部可定位"通过
- [x] **P1-6.COMP2**：DYN-0验收第2条"事件可回放"通过

---

## P1-7 记录"不要求隐藏CoT"的协议

> 来源：123号§36 DYN-0验收第3条 + R-1风险监控 + NO-4约束

- [x] **P1-7.1**：在实验protocol文档中明确声明"不要求或伪造隐藏chain-of-thought"
- [x] **P1-7.2**：在manifest中记录`hidden_cot_required: false`（P1-1.1已包含）
- [x] **P1-7.3**：验证事件捕获器不捕获隐藏CoT（只捕获公开研究产物与工具事件）

### 完整性标准

- [x] **P1-7.COMP**：DYN-0验收第3条"不要求隐藏CoT"通过
- [x] **P1-7.COMP2**：R-1风险监控机制在Phase 1落地（128号§2 R-1：每个Phase的Event Capture文档必须明确声明"只处理公开研究产物与工具事件"）

---

## P1-8 验证抽取失败不丢原始证据

> 来源：123号§36 DYN-0验收第4条

- [x] **P1-8.1**：故意制造语义抽取失败（如输入格式异常、抽取器无法识别的事件类型）
- [x] **P1-8.2**：验证原始事件仍在`raw_events` collection中
- [x] **P1-8.3**：验证语义事件可重新抽取（不影响原始事件）

### 完整性标准

- [x] **P1-8.COMP**：DYN-0验收第4条"抽取失败不会丢失原始证据"通过

---

## 出口门

- [x] **P1-EXIT-1**：关键事件可重放（从checkpoint恢复到同一可观测状态）
- [x] **P1-EXIT-2**：原始证据无丢失（抽取失败时原始事件仍在）
- [x] **P1-EXIT-3**：DYN-0验收4条全部通过：
  1. 原始输出/工具/提示/时间/分支可定位
  2. 事件可回放
  3. 不要求隐藏CoT
  4. 抽取失败不丢原始证据

---

## 角色隔离落地（Phase 1首次启用）

> 来源：127号§10角色可见性矩阵 + R-13风险监控

Phase 1首次启用角色隔离机制。需要落地的角色：

- [x] **P1-ROLE-1**：Event Capture / Trace Modeler角色启用
  - 可见：Solver公开产物、工具事件、分支、回退、提示差异
  - 不可见：隐藏CoT
  - 不能做：选Hint或裁决成功
- [x] **P1-ROLE-2**：Orchestrator角色启用
  - 可见：内容哈希、随机化、权限、运行状态和归档
  - 不能做：修改冻结输入，补写任何组结果
- [x] **P1-ROLE-3**：Solver角色启用（只观察模式，不接收Hint）
  - 可见：Q_0、当前工作区压缩、开放义务、最小证据
  - 不可见：H全库、未来Hint、ground truth、Truth Vault

### 完整性标准

- [x] **P1-ROLE.COMP**：3个角色的CapabilityToken签发和验证逻辑实现（127号§10.6）
- [x] **P1-ROLE.COMP2**：Truth Vault对Solver不可见（R-13风险防线）

---

## 代码模块创建

> 来源：plan"research_runtime/events模块" + 123号§54

- [x] **P1-CODE-1**：创建`xishujuzhen/research_runtime/`包
- [x] **P1-CODE-2**：创建`xishujuzhen/research_runtime/events/`模块（原始/语义事件与checkpoint）
- [x] **P1-CODE-3**：创建`xishujuzhen/research_runtime/models/`模块（任务/工作区/义务类型定义）

### 完整性标准

- [x] **P1-CODE.COMP**：不预建全套框架（NO-9约束：只在入口门通过后创建对应模块）
- [x] **P1-CODE.COMP2**：不膨胀现有文件（plan要求：不继续膨胀cognition_sdk_math.py等现有文件）

---

## Phase 1状态

**已完成**。DYN-0验收4条全部通过（集成测试test_phase1.py验证）。

### 实现清单

| Check List项 | 实现文件 | 状态 |
|---|---|---|
| P1-1 manifest | `research_runtime/manifest.py` | ✅ |
| P1-2 事件捕获接口 | `research_runtime/models/event.py` (EventFactory) | ✅ |
| P1-3 RawEvent存储 | `research_runtime/events/store.py` (EventStore) + ArangoDB `raw_events` collection | ✅ |
| P1-4 SemanticEvent存储 | `research_runtime/events/store.py` (EventStore) + ArangoDB `semantic_events` collection | ✅ |
| P1-5 checkpoint | `research_runtime/events/store.py` (CheckpointStore) + ArangoDB `checkpoints` collection | ✅ |
| P1-6 重放与追溯 | `EventStore.verify_traceability()` | ✅ |
| P1-7 不要求隐藏CoT | manifest `hidden_cot_required: false` | ✅ |
| P1-8 抽取失败不丢证据 | 三层保留机制（原始事件append-only） | ✅ |
| P1-CODE 包结构 | `research_runtime/` (models + events) | ✅ |
| 集成测试 | `research_runtime/test_phase1.py` | ✅ |

### ArangoDB新增collections

- `raw_events`：原始事件（append-only）
- `semantic_events`：语义事件（可重抽）
- `checkpoints`：内容寻址checkpoint
- `run_manifests`：运行manifest
