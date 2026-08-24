# POC-VMS-43 Trace Auditor结构审计（零模型）

**日期**：2026-08-14  
**状态**：`TRACE_AUDITOR_STRUCTURAL_ZERO_MODEL_PASS / LIVE_NOT_AUTHORIZED`  
**所属路线**：363号 `SV-S4.1`  
**前置**：346—386号已完成解题侧结构化DAG/FCA/RCA-style核心、VMS-40真值协议、VMS-41/R1抽取器失败与修订链、VMS-42 State Normalizer及DAG sidecar。

---

## 1. 本文档的身份

本文档冻结 SV-S4 的第一版 Trace Auditor 零模型合同。它不从自然语言中抽取事件，不判断数学证明正确性，也不选择Tell/Hint。它只审计已经结构化的 `ReasoningDag`：

> 给定一个DAG，机械识别其中是否存在分叉、失败分支、折返、跨分支复用、真合流和矛盾后恢复等 trace-family 证据；如果同时给出 State Normalizer sidecar，则验证 sidecar 与 DAG 的 hash、节点集合和拓扑顺序兼容。

换句话说，Trace Auditor 是“结构证据审计器”，不是“模型抽取器”。

---

## 2. 新增对象

| 对象 | 路径 | SHA-256 |
|---|---|---|
| Trace Auditor module | `system/solve_vein_analysis/trace_auditor.py` | `86ad84d87300154e19d42bc01b1094c54e43019019b84c60dbc2a03ce196f455` |
| Trace Auditor tests | `system/tests/solve_vein_analysis/test_trace_auditor.py` | `c66138ac9f8d8b7563183c3039969eef3fa938495a50b7501d7137c2c48cee2a` |

新增 `.ref` / `.ai-check`：

- `system/solve_vein_analysis/trace_auditor.ref`
- `system/solve_vein_analysis/trace_auditor.ai-check`
- `system/tests/solve_vein_analysis/test_trace_auditor.ref`
- `system/tests/solve_vein_analysis/test_trace_auditor.ai-check`

---

## 3. Trace Auditor合同

`trace_auditor.py` 输出：

```yaml
schema_version: solve-vein/trace-audit/v1
protocol_path:
protocol_exists_at_build_time:
dag_sha256:
state_annotation_bundle_sha256:
node_count:
edge_count:
branch_point_count:
revisit_event_count:
explicit_merge_event_count:
trace_family_observations:
  LINEAR_PROGRESS: {status:, evidence_event_ids: [], evidence_edge_ids: [], rule_id:}
  BRANCH_EXPLORATION: ...
  FAILED_BRANCH: ...
  REVISIT_WITH_NEW_INFORMATION: ...
  CROSS_BRANCH_REUSE: ...
  TRUE_MERGE: ...
  RECOVERY_AFTER_CONTRADICTION: ...
observed_trace_families: []
required_trace_family_verdict:
  required_trace_families: []
  missing_trace_families: []
  status: PASS | FAIL
state_sidecar_verdict:
  status: NOT_PROVIDED | PASS
  bundle_sha256:
  annotated_occurrence_count:
  missing_from_dag: []
side_effects:
  model_calls: 0
  devin_sessions: 0
  database_connections: 0
  solver_calls: 0
  files_written: 0
overall_verdict: PASS | FAIL
```

关键约束：

1. 输入DAG必须是 `solve-vein/reasoning-dag/v1`；
2. DAG必须声明 `acyclic: true`；
3. `topological_order` 的集合必须等于 `nodes[*].event_id`；
4. 每条edge的source/target必须存在，并且必须前向；
5. edge ID不可重复；
6. 缺少必需trace family时输出科学 `FAIL`，不得冒充协议异常或PASS；
7. 未知必需trace family属于合同错误，fail-closed；
8. 若提供State Normalizer sidecar，sidecar必须是PASS，且 `dag_sha256` 必须匹配当前DAG；
9. sidecar的 `topological_annotation_order` 必须等于DAG拓扑序中过滤出annotated occurrence后的序列；
10. 输出副作用必须全为0。

---

## 4. 当前demo

命令：

```bash
.venv/bin/python system/solve_vein_analysis/trace_auditor.py --demo-complex
```

当前开发 stdout SHA-256：

```text
b631720d72e217419abcddfde29dacfa4c7de50cd88c39679d3a915f6cc3aaf0
```

demo DAG：

```text
a0
├─BRANCH_FROM→ b1
└─BRANCH_FROM→ c1(CONTRADICTED/FAILURE)
                  └─REVISIT→ d2
b1 ─MERGE──────────────┐
d2 ─MERGE──────────────┴→ e3
```

必需family：

- `BRANCH_EXPLORATION`
- `FAILED_BRANCH`
- `REVISIT_WITH_NEW_INFORMATION`
- `TRUE_MERGE`
- `RECOVERY_AFTER_CONTRADICTION`

当前demo输出 `overall_verdict=PASS`。`CROSS_BRANCH_REUSE` 和 `LINEAR_PROGRESS` 在此demo中为 `ABSENT`，因为它们不是本demo的必需family。

---

## 5. 测试矩阵

新增 10 项测试：

| 测试 | 目的 |
|---|---|
| `test_demo_complex_trace_audit_passes_required_families` | 分叉、失败、折返、真合流和恢复family均被观察到 |
| `test_missing_required_trace_family_is_scientific_fail_not_protocol_exception` | 缺少必需family时输出科学FAIL |
| `test_unknown_required_trace_family_is_rejected` | 未知family合同错误fail-closed |
| `test_state_sidecar_matching_dag_hash_and_order_passes` | sidecar与DAG hash/order兼容时PASS |
| `test_state_sidecar_dag_hash_mismatch_is_rejected` | sidecar绑定旧/错DAG时拒绝 |
| `test_state_sidecar_order_mismatch_is_rejected` | sidecar拓扑顺序不一致时拒绝 |
| `test_unknown_edge_endpoint_is_rejected` | edge端点不存在时拒绝 |
| `test_duplicate_edge_id_is_rejected` | edge ID重复时拒绝 |
| `test_cli_outputs_demo_complex_trace_audit_receipt` | CLI输出PASS JSON receipt |
| `test_trace_auditor_module_has_no_model_solver_database_network_or_subprocess_import` | 禁止模型/DB/网络/子进程导入面 |

专项命令：

```bash
.venv/bin/python -m unittest system.tests.solve_vein_analysis.test_trace_auditor -v
```

结果：

```text
Ran 10 tests in 0.081s
OK
```

---

## 6. 非主张

本POC不主张：

- 不证明真实AI thinking已经能被正确抽取为DAG；
- 不证明数学证明正确；
- 不证明Trace→Tell/Hint选择；
- 不证明streaming增量审计；
- 不证明State Normalizer模型角色已资格化；
- 不写DB、不写D盘CAS、不创建EvidenceRecord；
- 不启动Devin/Codex/Solver；
- 不触碰入题侧代码、资产或历史运行物证。

---

## 7. 下一步

SV-S4 的下一步可以继续沿两条线推进：

1. **Trace Auditor qualification pack**：冻结更多结构化DAG case，覆盖 cross-branch reuse、linear progress、伪merge、伪revisit、sidecar partial coverage 和 required family missing 等负例；
2. **角色资产/preexecution freeze**：为未来真实 Trace Auditor / Event Extractor / State Normalizer 模型角色准备 candidate-visible bundle、hidden rubric、sealed reviewer judgment和不可消费LiveRunPermit草案。

在上述任一路线前，不得启动真实模型，不得把 `TRACE_AUDITOR_STRUCTURAL_ZERO_MODEL_PASS` 升格为 live qualification。
