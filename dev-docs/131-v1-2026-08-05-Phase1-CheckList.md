# 131-Phase 1 Check List：只观察，不提示

> **文档定位**：从124号拆出的Phase 1独立Check List。Phase 1目标——完成DYN-0（事件捕获真实性）。
>
> **入口门**：Phase 0出口门全部通过。
>
> **出口门**：关键事件可重放、原始证据无丢失、DYN-0验收4条全部通过。
>
> **停止条件**：关键工具或分支无法稳定捕获，则不进入状态建模（Phase 2）。
>
> **来源追溯**：123号第四十六节、plan"DYN-0：事件捕获真实性"
>
> **粒度说明**：Phase 1已细化到可执行子项。到实际执行前还需对照plan和123号补充完整性标准。

---

## P1-1 创建运行manifest

> 来源：123号§46 + plan"新运行主链步骤1"

- [ ] **P1-1.1**：定义manifest格式（run_id, task_id, model_version, tool_versions, budget, permissions, timestamp_start, timestamp_end）
- [ ] **P1-1.2**：实现manifest创建脚本（`xishujuzhen/research_runtime/manifest.py`，Phase 1首次创建research_runtime目录）
- [ ] **P1-1.3**：manifest落盘到`xishujuzhen/research_runtime/runs/<run_id>/manifest.json`

### 完整性标准（执行前补充）

- [ ] **P1-1.COMP**：manifest格式覆盖plan"新运行主链步骤1"的全部冻结项（原题、可见性、模型/工具配置、知识/规则版本和实验manifest）

---

## P1-2 捕获公开文本和工具事件

> 来源：123号§46 + plan"新运行主链步骤3—4" + 128号G0-1事件清单

- [ ] **P1-2.1**：定义事件捕获接口（哪些API调用、哪些文本输出、哪些工具调用需要捕获）
- [ ] **P1-2.2**：实现事件捕获器（hook到Devin CLI的tool调用、subagent输出、文件写入等）
- [ ] **P1-2.3**：验证捕获不遗漏关键事件类型

### 完整性标准（执行前补充）

- [ ] **P1-2.COMP**：捕获覆盖128号§1定义的全部27种事件类型（5类：工具调用/文本段落/分支点/状态变更/语义事件）
- [ ] **P1-2.COMP2**：捕获覆盖123号§17定义的全部14种语义事件类型

---

## P1-3 建立不可变原始事件

> 来源：123号§17 + 127号Event schema（RawEvent）

- [ ] **P1-3.1**：定义原始事件collection schema（event_id, type, timestamp, raw_payload, content_hash, run_id, causal_predecessors）
- [ ] **P1-3.2**：在ArangoDB中创建`raw_events` collection（新collection，不动旧数据）
- [ ] **P1-3.3**：实现事件写入接口（append-only，不允许修改或删除）
- [ ] **P1-3.4**：验证content_hash的正确性（同内容同hash，不同内容不同hash）

### 完整性标准（执行前补充）

- [ ] **P1-3.COMP**：原始事件schema符合127号§3的RawEvent定义（含causal_predecessors的DAG边）

---

## P1-4 建立语义事件抽取版本

> 来源：123号§17 + 127号Event schema（SemanticEvent）

- [ ] **P1-4.1**：定义语义事件schema（在原始事件基础上增加workspace_ref, obligation_ref, evidence_ref, conflict_with, confidence, source）
- [ ] **P1-4.2**：在ArangoDB中创建`semantic_events` collection
- [ ] **P1-4.3**：实现语义抽取器（从原始事件中识别命题、义务、表示、证据和拒绝分支）
- [ ] **P1-4.4**：验证抽取失败不会丢失原始证据（原始事件保留，语义事件可重抽）

### 完整性标准（执行前补充）

- [ ] **P1-4.COMP**：语义事件schema符合127号§3的SemanticEvent定义（含conflict_with的#关系）
- [ ] **P1-4.COMP2**：语义事件类型覆盖127号§3的14种枚举值

---

## P1-5 建立内容寻址checkpoint

> 来源：123号§39 + plan"新运行主链步骤10"

- [ ] **P1-5.1**：定义checkpoint格式（序列化Q_0/W_t、关键事件前缀、模型/工具/权限/预算和版本哈希）
- [ ] **P1-5.2**：实现checkpoint创建和存储
- [ ] **P1-5.3**：验证checkpoint不含LLM隐藏内部状态（只含公开产物）

### 完整性标准（执行前补充）

- [ ] **P1-5.COMP**：checkpoint定义符合123号§39"checkpoint定义为序列化Q_0/W_t、关键事件前缀、模型/工具/权限/预算和版本哈希；它不包含、也不能冻结LLM隐藏内部状态"

---

## P1-6 验证重放与来源追溯

> 来源：123号§36 DYN-0验收

- [ ] **P1-6.1**：从checkpoint重放后续continuation（同一checkpoint可产生多个continuation）
- [ ] **P1-6.2**：每个语义事件可追溯到原始事件（event_id链）
- [ ] **P1-6.3**：每个原始事件可追溯到manifest和run_id

---

## P1-7 记录"不要求隐藏CoT"的协议

> 来源：123号§36 + R-1风险监控

- [ ] **P1-7.1**：在实验protocol文档中明确声明"不要求或伪造隐藏chain-of-thought"
- [ ] **P1-7.2**：在manifest中记录"hidden_cot_required: false"

---

## 出口门

- [ ] **P1-EXIT-1**：关键事件可重放（从checkpoint恢复到同一可观测状态）
- [ ] **P1-EXIT-2**：原始证据无丢失（抽取失败时原始事件仍在）
- [ ] **P1-EXIT-3**：DYN-0验收4条全部通过（原始输出/工具/提示/时间/分支可定位、事件可回放、不要求隐藏CoT、抽取失败不丢原始证据）

---

## Phase 1状态

**待开始**。入口门（Phase 0出口门）已通过。
