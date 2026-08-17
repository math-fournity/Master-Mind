# POC-VMS-40：多视图脉络真值与 Acceptable Set 确定性协议

**日期**：2026-08-14  
**阶段**：SV-S1  
**状态**：FROZEN_BEFORE_IMPLEMENTATION  
**证据用途**：DEVELOPMENT_ONLY / DETERMINISTIC_OFFLINE  
**允许执行**：文档、fixture、纯本地确定性代码与测试  
**禁止执行**：模型调用、Devin、Codex、Solver、DB、Redis、网络、入题侧代码或运行资产修改  

---

## 0. 预注册声明

本文在 VMS-40 实现和结果产生前冻结。实现不得根据测试失败反向修改本协议的验收语义；若协议本身有缺陷，封存本轮为协议失败，另开新版本和新 POC。

本轮只解决一个问题：

> 对同一非线性推理过程，如何允许多个数学上等价或互补的关系视图，同时仍能机械地拒绝漏边、错边、非法拼接、假合流和状态轴混淆？

本轮不资格化 Event Extractor、State Normalizer 或 Auditor，不证明真实模型可以完成脉络分析，也不产生 Tell 因果证据。

---

## 1. 为什么旧单一 Gold 不够

VMS-38 的候选图与旧 Gold 在同一个折返处出现了至少两种合理投影：

- 视图 A：e0→e3 是 BRANCH_FROM，同时 e2→e3 是 REVISIT；
- 视图 B：e0→e3 直接记为 REVISIT，并用其他边表达控制流来源。

这不意味着所有图都可接受。至少以下错误仍必须被拒绝：

1. 从视图 A 取一条边、从视图 B 取另一条边，拼成任何完整解释都不允许的混合图；
2. 把同一问题目标误当成同一策略、同一表示或同一知识状态；
3. 只因文本再次提到旧对象就标 REVISIT；
4. 只因两个分支都出现在结论附近就标 MERGE；
5. 漏掉必需 occurrence，或添加原证据中不存在的 occurrence/edge；
6. 用最终答案正确与否倒推中间关系标签。

所以，VMS-40 不再把真值写成唯一一张平面 Gold 图，而是冻结分层事实、关系视图、状态轴和一组受约束的可接受解释。

---

## 2. 五层真值

### L0 Raw Evidence

原始 trajectory、字节范围、tool/event 物证和内容哈希。L0 不承载语义结论。

### L1 Occurrence Facts

按时间发生的 reasoning occurrence。每个 occurrence 有独立 ID；同一数学状态被再次访问也不能覆盖旧 occurrence。

### L2 Semantic Assertions

候选分析对 occurrence 之间的关系、状态轴绑定和 legacy status 作出的可审计判断。L2 可以有多个合法投影。

### L3 Preregistered Acceptable Set

在看候选输出之前冻结的约束集合。它定义共同必需事实、互斥或可并存的合法关系方案、禁止事实、可选事实和结构约束。

### L4 Candidate Evaluation

确定性 evaluator 对 L2 相对于 L3 的裁决。总 Verdict 必须由各项检查机械派生，不能由模型或人工直接填写 PASS。

---

## 3. 状态不是一个 canonical ID

旧 canonical_math_state_id 同时承担了题目义务、策略、表示、知识状态和分支生命周期，导致“同题”被误解成“同状态”。VMS-40 冻结以下正交轴：

| 轴 | 含义 | 示例 |
|---|---|---|
| PROBLEM_OBLIGATION | 当前要证明、求解或排除的数学义务 | 证明主命题、验证边界情形 |
| STRATEGY_METHOD | 当前采用的方法或证明路线 | 归纳、极值、局部化 |
| REPRESENTATION | 对象的表示或坐标系 | 组合表示、代数表示 |
| KNOWLEDGE_STATE | 当前已经建立并可使用的事实集合 | 已知引理 L、排除分支 B |
| BRANCH_LIFECYCLE | 分支的控制状态 | ACTIVE、ABANDONED、REOPENED |
| EPISTEMIC_VALIDITY | 命题当前的认知状态 | HYPOTHESIS、SUPPORTED、CONTRADICTED |
| LEGACY_CANONICAL | 与 v1 canonical_math_state_id 的兼容投影 | 只作迁移和回归，不再作为全状态真值 |

每个轴独立绑定 value_id。候选必须提交预注册要求的轴，不能把一个相同字符串复制到所有轴。状态等价由每个轴的 must-link / cannot-link 约束判断，而不是比较任意生成的 canonical ID。

---

## 4. 五种关系视图

| view | 回答的问题 | 典型关系 |
|---|---|---|
| TEMPORAL_OCCURRENCE | 先发生什么、后发生什么 | NEXT、LATER_THAN |
| CONTROL_FLOW | Solver 从哪个分支/节点转向哪里 | CONTINUE、BRANCH_FROM、RETURN_TO |
| EPISTEMIC_DEPENDENCY | 新判断依赖、推翻或复用哪些知识 | DEPENDS_ON、CONTRADICTS、REUSES |
| SYNTHESIS | 多条脉络是否真正合成新进展 | MERGES、CONCLUDES_FROM |
| STATE_IDENTITY | 两个 occurrence 在哪些状态轴上同一或不同 | SAME_ON_AXIS、DIFFERENT_ON_AXIS |

同一 occurrence 对可以在不同 view 下同时有边；同一 view 内是否允许多关系，由 Acceptable Set 明示。关系标签必须带 view，禁止只写一个无视图的 REVISIT 或 MERGE。

---

## 5. 冻结机器对象

### 5.1 SemanticCandidate/v1

~~~yaml
schema_version: solve-vein/semantic-candidate/v1
candidate_id:
case_id:
occurrence_ids: []
relations:
  - source_occurrence_id:
    target_occurrence_id:
    view:
    relation:
state_bindings:
  - occurrence_id:
    axis:
    value_id:
legacy_statuses:
  - occurrence_id:
    status:
~~~

数组输入可任意排序；canonicalization 后语义哈希必须相同。重复 relation、state binding 或 legacy status 一律拒绝。

### 5.2 SemanticAcceptableSet/v1

~~~yaml
schema_version: solve-vein/semantic-acceptable-set/v1
acceptable_set_id:
case_id:
expected_occurrence_ids: []
required_relations: []
relation_clauses:
  - clause_id:
    selection: EXACTLY_ONE | AT_LEAST_ONE
    alternatives:
      - alternative_id:
        complete_relation_set: []
optional_relations: []
forbidden_relations: []
required_state_axes: []
state_constraints:
  - constraint_id:
    kind: MUST_LINK | CANNOT_LINK | EXACT_VALUE
    axis:
    occurrence_ids: []
    value_id:
legacy_status_constraints:
  - occurrence_id:
    allowed_statuses: []
structural_constraints:
  - constraint_id:
    kind: MIN_DISTINCT_PARENTS
    target_occurrence_id:
    view:
    relation:
    minimum:
~~~

relation clause 的 alternative 是不可拆分的完整边集。候选只有完整命中某个 alternative 才算命中；跨 alternative 拼边不能算 PASS。

### 5.3 SemanticEvaluation/v1

~~~yaml
schema_version: solve-vein/semantic-evaluation/v1
candidate_id:
acceptable_set_id:
canonical_input_hashes: {}
occurrence_verdict:
required_relation_verdict:
relation_clause_verdicts: []
optional_relation_observations: []
forbidden_relation_verdict:
unmatched_relation_verdict:
state_constraint_verdicts: []
legacy_status_verdicts: []
structural_constraint_verdicts: []
per_view_coverage: {}
errors: []
overall_verdict: PASS | FAIL | INVALID
~~~

overall_verdict 只能按第 6 节规则派生。

---

## 6. 确定性 evaluator 语义

按以下顺序 fail-closed：

1. 严格解析 candidate 与 acceptable set；未知字段、未知 enum、bool 冒充 integer、非有限数、重复实体均 INVALID；
2. case_id 必须相同；
3. candidate occurrence 集必须与 expected occurrence 集完全相等；
4. 每条 required relation 必须出现；
5. 每个 relation clause 按 complete_relation_set 判断完整 alternative，满足 selection 规则；
6. forbidden relation 任一出现即 FAIL；
7. candidate 中除 required、已选 alternative、optional 之外的关系均为 unmatched，任一存在即 FAIL；
8. required state axis 对每个适用 occurrence 必须恰有一个 binding；
9. MUST_LINK、CANNOT_LINK、EXACT_VALUE 分别机械判断；
10. legacy status 必须落在 allowed_statuses；
11. MIN_DISTINCT_PARENTS 以不同 source occurrence ID 计数，重复同一 parent 不能凑数；
12. 每个 view 分别报告 expected、matched、missing、forbidden、unmatched；
13. 只有所有必需检查 PASS 且 errors 为空时 overall=PASS；严格解析失败为 INVALID；其余为 FAIL。

evaluator 不读取最终答案、不读取 candidate 的自评 Verdict，也不根据输出好坏改 acceptable set。

---

## 7. VMS-40 冻结案例矩阵

| Case | 要验证的主张 | 必须有的正例 | 必须有的反例 |
|---|---|---|---|
| MV1 | legacy status 可是受约束集合而非单值 | ABANDONED 与 CONTRADICTED 各自可接受 | ACTIVE 被拒绝 |
| MV2 | 问题、策略、表示、知识状态必须分轴 | problem must-link 且 strategy/representation cannot-link | 单 canonical ID 把全部轴合并被拒绝 |
| MV3 | 折返/分叉允许两套完整合法投影 | alternative A、alternative B 各 PASS | A/B 混搭、两套同时命中、缺半套均 FAIL |
| MV4 | 真合流必须有不同父 occurrence | 两个不同父分支共同 MERGES 到目标 | 单父、重复父、只有文本 mention 均 FAIL |
| MV5 | 每个 view 独立覆盖且额外边不静默放过 | required+optional 的完整候选 | missing、forbidden、unknown extra 分别 FAIL |
| MV6 | Schema、身份和 canonicalization fail-closed | 数组重排 hash 不变 | 未知字段、重复、case错配、occurrence缺失/增加均 INVALID/FAIL |

至少再增加两个组合反例：

- EXACTLY_ONE clause 同时完整命中两个 alternative，必须 FAIL；
- required_state_axes 缺任一轴，必须 FAIL。

---

## 8. 实现文件与不可变边界

计划新增：

~~~text
system/solve_vein_analysis/semantic_truth.py
system/solve_vein_analysis/semantic_truth.ref
system/solve_vein_analysis/semantic_truth.ai-check
system/tests/solve_vein_analysis/multiview_fixtures/
system/tests/solve_vein_analysis/test_semantic_truth.py
system/tests/solve_vein_analysis/test_semantic_truth.ref
system/tests/solve_vein_analysis/test_semantic_truth.ai-check
system/tests/solve_vein_analysis/run_multiview_poc.py
system/tests/solve_vein_analysis/run_multiview_poc.ref
system/tests/solve_vein_analysis/run_multiview_poc.ai-check
~~~

确定性 POC 结果使用新 append-once 目录：

~~~text
/data/master-mind-solve-vein-data/poc-results/poc-vms-40-20260814/
~~~

实现不得修改：

- system/vein_analysis.py；
- system/process_absorb.py；
- system/assets/vein_analysis/；
- palyground/absorb/vein_analysis/；
- VMS-31—39 已封存物证；
- 任何入题侧运行目录或 AGENTS.md。

---

## 9. G-S1 验收门

VMS-40 只有同时满足以下条件才可判 PASS：

1. 本协议在代码和 fixture 前冻结并记录 SHA-256；
2. MV1—MV6 全部正例与反例通过；
3. evaluator 的 overall verdict 可从逐项结果重新机械推导；
4. array order 不影响 canonical hash；
5. 旧 v1 单 Gold 的合法案例能迁移到 acceptable set，且 VMS-38 已知歧义能表达为两个完整 alternative；
6. 全量 solve-side tests PASS；
7. 入题侧保护基线不变；
8. repo diff-check、Python compile、artifact integrity 均 PASS；
9. README、363 checkpoint、稳定模块文档和 ChangeLog 同步；
10. 结果目录 append-once，包含协议 hash、代码 receipt、fixture hashes、测试命令/输出摘要和最终机械 Verdict。

如果实现只能接受一个投影，判科学 FAIL；如果通过放宽为“任意边都可接受”，判科学 FAIL；如果结果后才修改 acceptable set，判协议 INVALID。

---

## 10. 明确非主张

本轮 PASS 也不证明：

- 真实 Solver trajectory 已被正确抽取；
- Devin 或 Codex 已具备 Extractor/Normalizer/Auditor 能力；
- 多视图集合覆盖所有数学推理关系；
- FCA/RCA 已经在规模数据上有效；
- Tell 可选择、可执行、可归责；
- Trace/Tell 分片遍历已实现；
- 推理树、引导树、Grove 或 Seven 已接通。

这些分别属于 VMS-41—52，必须沿 363 号阶段门推进。
