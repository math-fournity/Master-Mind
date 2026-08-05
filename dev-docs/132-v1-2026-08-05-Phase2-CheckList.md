# 132-Phase 2 Check List：类型化状态与研究义务

> **文档定位**：从124号拆出的Phase 2独立Check List。Phase 2目标——完成DYN-1（状态重建一致性）和DYN-2（卡点检测校准）。
>
> **入口门**：Phase 1出口门全部通过（131号P1-EXIT-1/2/3）。
>
> **出口门**：状态重建α≥0.80、卡点检测校准通过、DYN-1和DYN-2验收全部通过。
>
> **失败回滚**：保留事件日志，停止H建设，改进抽取与状态本体。
>
> **来源追溯**：123号§47 + §37(DYN-1) + §38(DYN-2) + §15-16(Workspace/Obligation schema) + §31(Evidence) + §44(预注册门G0-2)；系统探讨.md§16(Phase 2) + §6阶段3(状态审计)；plan"新Phase 2：类型化工作区、AND/OR义务和证据状态模型"

---

## P2-1 解析Q_0的任务类型、对象、前提、目标和成功条件

> 来源：123号§14 Task schema + §32步骤2(建态) + 系统探讨.md§6阶段0 + 127号§1

- [ ] **P2-1.1**：选定第一个实验用任务Q_0
  - 候选：Ramsey修正版材料（128号§3 CC-R-0冻结的实验基底）
  - 用新protocol，不是继续POC-6（NO约束：不能反向把119号结论升级）
- [ ] **P2-1.2**：用Task schema（127号§1）解析Q_0的全部7个字段：
  - `task_id` / `type`（9种枚举之一）/ `domain`
  - `objects`（数学对象和表达语言D）
  - `premises`（原始前提与约束Γ_0）
  - `goal`（目标G_0）
  - `success_conditions`（成功条件χ_success）
  - `stop_conditions` / `failure_conditions`
- [ ] **P2-1.3**：定义Q_0的success_conditions
  - 不只是"答对"，而是123号§44核心指标中"任务类型特定的已验证进展"
  - 123号§23明确：`prove/refute`看义务证据门与反例；`construct`看候选对象通过的约束比例；`compute`看已验证子计算；`conjecture`看非重复、可证伪、通过初筛且未被反例否定的候选；`classify/optimize/value`分别需要覆盖、界和决策论指标

### 完整性标准

- [ ] **P2-1.COMP**：Task schema覆盖127号§1的全部字段（task_id/type/domain/objects/premises/goal/success_conditions/stop_conditions/failure_conditions）
- [ ] **P2-1.COMP2**：success_conditions按123号§23的任务类型特定进展定义，不用粗糙计数
- [ ] **P2-1.COMP3**：Q_0在运行时保持冻结（127号§1冻结声明：Q_0在运行时保持冻结）

---

## P2-2 实现`V/F/O/R/D/E`工作区

> 来源：123号§15 Workspace schema + §32步骤5(状态归约) + 系统探讨.md§6阶段3 + 127号§2

- [ ] **P2-2.1**：定义6类工作区的collection schema，覆盖127号§2的Workspace定义：
  - `V_t`：已验证核心（verified_premises/verified_lemmas/verified_tool_results）
  - `F_t`：猜想前沿（candidates/temporary_assumptions/unverified_bridges）
  - `O_t`：开放研究义务（obligation_ids指向Obligation schema）
  - `R_t`：当前表示及其转换（active_representations/pending_transforms）
  - `D_t`：被证伪/拒绝/暂停/可恢复分支
  - `E_t`：每个命题与动作的证据（evidence_ids指向Evidence schema）
- [ ] **P2-2.2**：在ArangoDB中创建workspace collection（新collection，不动旧数据）
- [ ] **P2-2.3**：实现工作区读写接口
- [ ] **P2-2.4**：定义完整RunState（127号§2）：`S_t = (Q_0, W_t, L_≤t, b_t, B_t, M_t)`
  - `b_t`：控制器对卡点/策略/缺失信息的带不确定性信念
  - `B_t`：token/计算/工具/分支/Hint预算
  - `M_t`：模型版本/推理配置/权限/工具能力

### 完整性标准

- [ ] **P2-2.COMP**：Workspace schema符合127号§2的完整RunState定义（6类工作区 + Q_0 + L_≤t + b_t + B_t + M_t）
- [ ] **P2-2.COMP2**：W_t只能由版本化Reducer按明确字段规则派生，不能被直接修改（127号§2冻结声明）
- [ ] **P2-2.COMP3**：临时假设进入F_t，不进入V_t（127号§2冻结声明）
- [ ] **P2-2.COMP4**：被拒绝路线进入D_t，不与representation共用R（127号§2冻结声明）

---

## P2-3 建立AND/OR研究义务

> 来源：123号§16 Obligation schema + 127号§4 + 系统探讨.md§6阶段3

- [ ] **P2-3.1**：定义义务类型，覆盖127号§4的10种枚举：
  - `prove` / `refute` / `construct` / `compute` / `search` / `compare` / `evaluate` / `interface`（跨表示运输保真义务）/ `verification`（数值支持仍需证明或反例搜索）/ `value`（方向判断）
- [ ] **P2-3.2**：实现义务图构建（从语义事件中提取义务关系）
- [ ] **P2-3.3**：验证义务图是DAG（无环，环路在状态商空间处理）
- [ ] **P2-3.4**：实现义务超边存储（AND/OR超图）
  - 超边本体存relation document
  - `role=source/target`的participant edges连接义务
  - 不用普通`depends_on`边伪装超边（127号§4冻结声明）

### 完整性标准

- [ ] **P2-3.COMP**：义务超边用relation document + participant edges存储，不用普通depends_on边伪装超边（127号§4冻结声明）
- [ ] **P2-3.COMP2**：循环依赖不自动释放义务，产生待审计的SCC（127号§4冻结声明）
- [ ] **P2-3.COMP3**：Obligation schema覆盖127号§4的全部字段（obligation_id/type/status/task_id/parent_obligation/description/evidence_refs/evidence_gate/sub_obligations）

---

## P2-4 区分验证核心和猜想前沿

> 来源：123号§15 V_t/F_t分离 + R-3风险监控 + 127号§2

- [ ] **P2-4.1**：在Workspace schema中区分V_t（已验证核心）和F_t（猜想前沿）
- [ ] **P2-4.2**：对Q_0标注哪些义务是验证核心、哪些是猜想前沿
- [ ] **P2-4.3**：定义F_t进入V_t的验证门（123号§31：只有满足该命题类型预先指定的验证门，命题才进入V_t）

### 完整性标准

- [ ] **P2-4.COMP**：F_t内容进入V_t必须带证据引用（R-3触发停止条件：F_t进入V_t无证据）
- [ ] **P2-4.COMP2**：动态状态累积错误风险(R-3)有监控机制（128号§2 R-3：V/F分离实现检查）

---

## P2-5 建立证据状态模型和冲突状态

> 来源：123号§31 Evidence schema + 127号§6 + 系统探讨.md§11.4

- [ ] **P2-5.1**：用Evidence schema（127号§6）定义证据，字段覆盖：
  - `evidence_id` / `claim_id` / `kind`（6种枚举：literature/numerical/symbolic/formal_proof/counterexample/human_audit）/ `polarity`（support/refute）
  - `status`（pending/active/superseded/retracted）/ `scope` / `assumptions`
  - `artifact_hash` / `source_event` / `verifier` / `verifier_version`
  - `confidence` / `conflicts`
- [ ] **P2-5.2**：定义派生认识状态（127号§6）：`no_decisive` / `support_only` / `refute_only` / `mixed`
- [ ] **P2-5.3**：定义冲突状态（两个证据指向矛盾结论时的状态标记）
- [ ] **P2-5.4**：实现证据状态更新接口

### 完整性标准

- [ ] **P2-5.COMP**：证据集合不把数值支持与形式证明排成伪造的总序（127号§6冻结声明）
- [ ] **P2-5.COMP2**：`proved/formally_verified`是另一个验证等级字段，不是证据本身（127号§6冻结声明）
- [ ] **P2-5.COMP3**：冲突不自动爆炸到整个知识库，生成范围/前提澄清义务（127号§6冻结声明）
- [ ] **P2-5.COMP4**：只有满足该命题类型预先指定的验证门，命题才进入V_t（127号§6冻结声明）
- [ ] **P2-5.COMP5**：首版不宣称已有数学意义上的"证据格"——升级需定义偏序、join、meet并验证封闭性（127号§6冻结声明）

---

## P2-6 多观察者重建一致性测试

> 来源：123号§37 DYN-1 + G0-2预注册门 + R-9风险监控 + 123号§44

- [ ] **P2-6.1**：用2个以上独立抽取器对同一事件流做状态重建
- [ ] **P2-6.2**：计算字段级Krippendorff α（对照G0-2的阈值）
  - G0-2阈值：关键状态字段α≥0.80，无关键字段低于0.67
- [ ] **P2-6.3**：记录分歧案例和仲裁结果
- [ ] **P2-6.4**：不只是比节点数，而是预先定义字段级一致率、分歧仲裁和人工抽样（123号§37 DYN-1验收）

### 完整性标准

- [ ] **P2-6.COMP**：α值达到G0-2阈值，否则触发R-9停止条件（关键状态字段α < 0.80）
- [ ] **P2-6.COMP2**：DYN-1验收"预先定义字段级一致率、分歧仲裁和人工抽样；不是只比节点数"通过
- [ ] **P2-6.COMP3**：DYN-1停止条件"关键义务和证据的观察者一致性不足，则不建设H"（123号§37）

---

## P2-7 卡点类型和校准集

> 来源：123号§38 DYN-2 + 系统探讨.md§6阶段3

- [ ] **P2-7.1**：定义7类卡点，覆盖123号§38的全部类型：
  1. 必要探索
  2. 语义重复
  3. 矛盾未处理
  4. 工具阻塞
  5. 表示不合适
  6. 策略耗尽
  7. 预算耗尽
- [ ] **P2-7.2**：对Q_0的多个运行标注卡点类型（人工标注校准集）
- [ ] **P2-7.3**：实现卡点检测器
- [ ] **P2-7.4**：测precision、recall、误触发时间和"把正常探索误判为停滞"的比例

### 完整性标准

- [ ] **P2-7.COMP**：7类卡点全部定义（123号§38）
- [ ] **P2-7.COMP2**：DYN-2验收"测precision、recall、误触发时间和'把正常探索误判为停滞'的比例"通过
- [ ] **P2-7.COMP3**：DYN-2停止条件"卡点检测误报使正常探索被频繁打断"（123号§38 + STOP-2）

---

## P2-8 控制器信念建模

> 来源：123号§22(控制器面对部分可观测问题) + 127号§2 RunState的b_t

- [ ] **P2-8.1**：实现控制器对"当前策略、卡点类型、是否真的停滞"的不确定估计（b_t）
  - 123号§22明确："控制器维护的是对'当前策略、卡点类型、是否真的停滞'的不确定估计，而不是假装读心"
- [ ] **P2-8.2**：定义动作集合（123号§22的8种动作）：
  - `continue_observing` / `ask_diagnostic_question` / `request_tool_check` / `retrieve_minimal_interface` / `inject_hint_0` / `inject_hint_1` / `inject_hint_2` / `abstain` / `stop_or_escalate`

### 完整性标准

- [ ] **P2-8.COMP**：控制器不假装读心（123号§22 + R-1风险：只看到公开产物和工具事件）
- [ ] **P2-8.COMP2**：动作集合覆盖123号§22的全部9种动作（含abstain）

---

## P2-9 进展偏序定义

> 来源：123号§18(两种环路判别) + §23(任务类型特定进展) + 系统探讨.md§7(动态题目的拓扑结构)

- [ ] **P2-9.1**：定义进展偏序——同一任务/schema下进展向量不恶化且至少一项严格改善
- [ ] **P2-9.2**：区分两种环路（AGENTS.md方法论核心）：
  - 平面环路：不同时间事件投影回同一规范化状态，开放义务、证据门和冲突无改善 → 停止或换策略
  - 螺旋上升环路：返回同一抽象状态类，但更细粒度状态进展 → 允许继续并保存进展证据
- [ ] **P2-9.3**：定义跨任务比较规则（123号§23：跨任务只比较归一化实验结果，不直接比较|V_t|）

### 完整性标准

- [ ] **P2-9.COMP**：进展偏序定义符合123号§18"同一任务/schema下进展向量不恶化且至少一项严格改善"
- [ ] **P2-9.COMP2**：两种环路判别标准明确（AGENTS.md方法论核心）
- [ ] **P2-9.COMP3**：跨任务比较用归一化实验结果，不直接比较|V_t|（123号§23）

---

## 出口门

- [ ] **P2-EXIT-1**：状态重建Krippendorff α≥0.80且无关键字段低于0.67（G0-2阈值）
- [ ] **P2-EXIT-2**：卡点检测不把正常探索大量误判为停滞（误判率低于预注册阈值）
- [ ] **P2-EXIT-3**：DYN-1和DYN-2验收全部通过

---

## 角色隔离落地

> 来源：127号§10 + 123号§28

Phase 2新增启用的角色：

- [ ] **P2-ROLE-1**：State Reducer角色启用
  - 可见：类型化事件、旧快照、验证结果
  - 不能做：自行补写未发生的数学推理
  - 可复现约束：相同事件+相同reducer版本必须得到可复现结果
- [ ] **P2-ROLE-2**：Verifier角色启用
  - 可见：明确命题、前提、证明片段、工具输入、期望证据等级
  - 不能做：决定下一研究路线
  - 输出：认识状态、证据类型、范围、可重放产物和失败原因（不是单一布尔值）
- [ ] **P2-ROLE-3**：Retriever角色启用
  - 可见：当前义务、表示、权限和检索约束
  - 不能做：返回整图或答案专属材料

### 完整性标准

- [ ] **P2-ROLE.COMP**：State Reducer可复现约束落地（123号§28：相同事件+相同reducer版本必须得到可复现结果）
- [ ] **P2-ROLE.COMP2**：Verifier输出不是单一布尔值（123号§28 + 系统探讨.md§5.5：输出proven/formally_verified/computationally_supported/numerically_tested/contradicted/unknown）
- [ ] **P2-ROLE.COMP3**：Retriever不返回整图或答案专属材料（123号§28 + 系统探讨.md§5.4）

---

## 代码模块创建

> 来源：plan"research_runtime/state_reducer模块" + 123号§54

- [ ] **P2-CODE-1**：创建`xishujuzhen/research_runtime/state_reducer/`模块（事件→状态）
- [ ] **P2-CODE-2**：创建`xishujuzhen/research_runtime/verification/`模块（工具路由与证据状态模型）

### 完整性标准

- [ ] **P2-CODE.COMP**：不预建全套框架（NO-9约束）

---

## Phase 2状态

**待开始**。入口门（Phase 1出口门）未通过。
