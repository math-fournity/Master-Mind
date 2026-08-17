# POC-VMS-42 State Normalizer DAG writeback sidecar（零模型）

**日期**：2026-08-14  
**状态**：`DAG_WRITEBACK_SIDECAR_ZERO_MODEL_PASS / LIVE_NOT_AUTHORIZED`  
**所属路线**：363号 `SV-S3.7`  
**前置**：380—385号已完成 State Normalizer core、qualification pack、hidden join、reviewer judgment、final receipt 和 unseen extension。

---

## 1. 本文档的身份

本文档冻结 VMS-42 的“状态归一化结果写回解题侧DAG”的第一版零模型合同。这里的“写回”不是改写 `ReasoningDag`，而是生成一个**不可变 sidecar annotation bundle**：

> `ReasoningDag` 仍是轨迹图的 source-of-fact；State Normalizer 只把已通过评价的 multi-axis state binding 按 DAG event_id 附着成 sidecar。

这一步回答的问题很窄：

1. PASS 的 normalized bundle 是否能机械绑定到 DAG 中真实存在的 event；
2. sidecar 是否能保持 DAG topological order；
3. 非 PASS、hash漂移、DAG缺节点、重复axis binding 是否 fail-closed；
4. 整个过程是否保持零模型、零Devin、零Solver、零DB、零文件写入。

它不授权 live 模型，不运行 Devin/Codex/Solver，不写 DB/Redis，不触碰入题侧代码或运行资产。

---

## 2. 新增对象

| 对象 | 路径 | SHA-256 |
|---|---|---|
| DAG sidecar builder/module | `system/solve_vein_analysis/state_normalized_dag.py` | `da2faaa66928d72c75209633a5e1c59e2591a1cd29c6b4f7bd19d3d8bd7ae19f` |
| DAG sidecar tests | `system/tests/solve_vein_analysis/test_state_normalized_dag.py` | `cf1d1962f797bf6025f66890e1e849eb953d3c9dd578ac2e1796c78d02f0b3a0` |
| module ref | `system/solve_vein_analysis/state_normalized_dag.ref` | `a3af151da0233d6190b0334e43d9f4a364cf6fb5a51a03bec44b3c82a980d6e7` |
| test ref | `system/tests/solve_vein_analysis/test_state_normalized_dag.ref` | `ad34e97191ed1561aef3bf9d9caf7dc9a5537baeaf56bc52237f7a76a997e43a` |

新增 `.ai-check`：

- `system/solve_vein_analysis/state_normalized_dag.ai-check`
- `system/tests/solve_vein_analysis/test_state_normalized_dag.ai-check`

---

## 3. Sidecar对象合同

`state_normalized_dag.py` 输出：

```yaml
schema_version: solve-vein/state-normalized-dag-annotation-bundle/v1
case_id:
candidate_id:
dag_sha256:
normalized_bundle_sha256:
evaluation_sha256:
protocol_path:
protocol_exists_at_build_time:
annotated_occurrence_ids: []
topological_annotation_order: []
annotation_count:
annotations:
  - event_id:
    sequence_index:
    canonical_math_state_id:
    event_status:
    axis_bindings:
      - axis:
        value_id:
        raw_value:
    axis_binding_count:
    legacy_projection:
    annotation_sha256:
side_effects:
  model_calls: 0
  devin_sessions: 0
  database_connections: 0
  solver_calls: 0
  files_written: 0
overall_verdict: PASS
```

关键约束：

1. `ReasoningDag.schema_version` 必须是 `solve-vein/reasoning-dag/v1`；
2. DAG 必须声明 `acyclic: true`；
3. DAG `topological_order` 的集合必须等于 `nodes[*].event_id`；
4. `normalized_bundle` 必须是 `state_normalization.py` 的 normalized bundle schema；
5. `evaluation` 必须是 State Normalizer 的 PASS evaluation；
6. `evaluation.canonical_input_hashes.normalized_bundle_sha256` 必须等于当前 normalized bundle 的 canonical hash；
7. 每个 `normalized_bundle.occurrence_ids` 必须存在于 DAG event index；
8. 每个 `(occurrence_id, axis)` 最多只能出现一条 binding；
9. 输出 sidecar annotation 的顺序必须来自 DAG `topological_order`，不能来自 fixture、字典序或模型输出顺序；
10. 输出不得修改 DAG 本体。

---

## 4. CLI demo

命令：

```bash
.venv/bin/python system/solve_vein_analysis/state_normalized_dag.py --demo-unseen
```

当前开发 stdout SHA-256：

```text
42175e2d1ad47bbe6bfd0fba0641d287eeccb80ccb38ed4d52db1ef750297a47
```

当前 demo 使用 `vms42_unseen_cases.json` 的首个 PASS candidate：

```yaml
case_id: V42-UNSEEN-REPRESENTATION-REUSE
candidate_id: v42-unseen-representation-reuse-pass
annotation_count: 3
topological_annotation_order: [s0, s1, s2]
overall_verdict: PASS
```

stdout hash 只用于本地复验 CLI 输出形状；它不是 D盘 append-only receipt，也不是 live运行物证。

---

## 5. 测试矩阵

新增 8 项测试：

| 测试 | 目的 |
|---|---|
| `test_demo_unseen_annotation_passes_in_topological_order` | 正向demo PASS，保持DAG拓扑顺序与零副作用 |
| `test_annotation_sidecar_does_not_mutate_reasoning_dag` | 证明sidecar生成不改写DAG本体 |
| `test_normalized_occurrence_missing_from_dag_is_rejected` | normalized occurrence 不在DAG时拒绝 |
| `test_non_pass_state_normalization_evaluation_is_rejected` | State Normalizer非PASS时拒绝 |
| `test_normalized_bundle_tampering_is_rejected_by_hash` | bundle被篡改但evaluation未同步时拒绝 |
| `test_duplicate_axis_binding_is_rejected_after_hash_bound_evaluation` | 同occurrence/axis重复binding拒绝 |
| `test_cli_outputs_demo_unseen_pass_receipt` | CLI输出PASS JSON receipt |
| `test_state_normalized_dag_module_has_no_model_solver_database_network_or_subprocess_import` | 禁止模型/DB/网络/子进程导入面 |

专项命令：

```bash
.venv/bin/python -m unittest system.tests.solve_vein_analysis.test_state_normalized_dag -v
```

结果：

```text
Ran 8 tests in 0.081s
OK
```

---

## 6. 非主张

本POC不主张：

- 不证明真实模型能抽取 normalized state；
- 不证明 reviewer 或 hidden grader 已接入；
- 不授权 live execution；
- 不写DB、不写D盘CAS、不创建正式 EvidenceRecord；
- 不把 sidecar annotation 作为 Tell/Hint 选择证据；
- 不证明 streaming DAG 增量写回；
- 不触碰入题侧代码、资产或历史运行物证。

---

## 7. 下一步

VMS-42 当前已经把 deterministic State Normalizer 推进到：

1. 多轴状态绑定核心；
2. public/hidden pack；
3. hidden join；
4. reviewer judgment contract；
5. final reviewer+hidden join receipt；
6. unseen qualification extension；
7. DAG sidecar annotation。

下一步建议二选一：

1. **角色资产/preexecution freeze**：冻结未来模型 extractor 的 candidate-visible输入、hidden grader、manual review pack、能力报告和不可消费LiveRunPermit草案；
2. **SV-S4 Trace Auditor设计**：在 DAG+state sidecar 的基础上，定义如何审计真实AI探索中的折返、融合、重复状态、失败分支和与引导树的相遇。

在任一方向之前，仍不得启动真实模型，不得把 `DAG_WRITEBACK_SIDECAR_ZERO_MODEL_PASS` 升格为 live qualification。
