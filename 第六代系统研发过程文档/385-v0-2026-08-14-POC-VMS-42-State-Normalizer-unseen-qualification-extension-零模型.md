# POC-VMS-42 State Normalizer unseen qualification extension（零模型）

**日期**：2026-08-14  
**状态**：`ZERO_MODEL_EXTENSION_PASS / LIVE_NOT_AUTHORIZED`  
**所属路线**：363号 `SV-S3.6`  
**前置**：380—384号已完成 State Normalizer core、public/hidden pack、hidden join、reviewer judgment contract 和 final reviewer+hidden join receipt。

---

## 1. 本文档的身份

本文档冻结 VMS-42 的“全新未见 qualification extension”零模型层。它回答一个很窄但关键的问题：

> 在不改写原 380 号 fixture、不中断 381—384 号物证链的前提下，State Normalizer 能否接收一组新的 case/candidate，并机械证明新旧 case/candidate ID 不重叠、public/hidden 隔离仍成立、expected verdict 漂移会 fail-closed？

它不是 live 模型资格实验，不导入真实 reviewer 判断，不运行 Devin/Codex/Solver，不写 DB/Redis，不触碰入题侧代码或运行资产。

---

## 2. 新增对象

| 对象 | 路径 | SHA-256 |
|---|---|---|
| unseen fixture | `system/tests/solve_vein_analysis/state_normalizer_fixtures/vms42_unseen_cases.json` | `9090467cce096806835ddf61381139f26a5596b4e4abdb49750e3382996f0890` |
| unseen extension builder | `system/tests/solve_vein_analysis/build_vms42_state_normalizer_unseen_pack.py` | `2ba94d7fc1898d19bb410f6fe8a2ea50ea2dd70de71377ba6c581d71fd0d44db` |
| unseen extension tests | `system/tests/solve_vein_analysis/test_state_normalizer_vms42_unseen_pack.py` | `ed5d6575521d44270245256eb8fff5261c102047943d8e7f116ede5bbb661f2f` |

新增 `.ref` / `.ai-check`：

- `build_vms42_state_normalizer_unseen_pack.ref`
- `build_vms42_state_normalizer_unseen_pack.ai-check`
- `test_state_normalizer_vms42_unseen_pack.ref`
- `test_state_normalizer_vms42_unseen_pack.ai-check`

---

## 3. 新增未见case

### 3.1 `V42-UNSEEN-REPRESENTATION-REUSE`

覆盖“同一问题义务下发生表示切换，但后续知识证书被复用”的处境。

轴：

- `PROBLEM_OBLIGATION`
- `STRATEGY_METHOD`
- `REPRESENTATION`
- `KNOWLEDGE_STATE`

核心约束：

- `s0/s1/s2` 必须在 `PROBLEM_OBLIGATION` 上 link；
- `s0/s1` 必须在 `REPRESENTATION` 上不能 link；
- `s1/s2` 必须在 `KNOWLEDGE_STATE` 上 link；
- `s2` 的 `STRATEGY_METHOD` 必须是 `parity-lift`。

候选：

- `v42-unseen-representation-reuse-pass`：PASS；
- `v42-unseen-representation-collapsed-fail`：FAIL，表示轴被错误压平。

### 3.2 `V42-UNSEEN-BRANCH-REVISION`

覆盖“同一分类义务下，分支从猜测、反证到修正验证”的生命周期变化。

轴：

- `PROBLEM_OBLIGATION`
- `STRATEGY_METHOD`
- `BRANCH_LIFECYCLE`
- `EPISTEMIC_VALIDITY`

核心约束：

- `h0/h1/h2` 必须在 `PROBLEM_OBLIGATION` 上 link；
- `h0/h1` 必须在 `BRANCH_LIFECYCLE` 上不能 link；
- `h2` 的 `BRANCH_LIFECYCLE` 必须是 `repaired`；
- `h2` 的 `EPISTEMIC_VALIDITY` 必须是 `validated`。

候选：

- `v42-unseen-branch-revision-pass`：PASS；
- `v42-unseen-branch-revision-invalid`：INVALID，含未登记 alias `obsolete branch`。

---

## 4. Builder合同

`build_vms42_state_normalizer_unseen_pack.py` 的职责：

1. 读取原始 `vms42_cases.json` 与新增 `vms42_unseen_cases.json`；
2. 对两者分别运行确定性 State Normalizer 自检；
3. 强制新旧 `case_id` 不相交；
4. 强制新旧 `candidate_id` 不相交；
5. 从 unseen fixture 生成新的 public manifest / hidden manifest；
6. 将 manifest 的 `pack_id` 重写为 `vms42-state-normalizer-unseen-qualification-extension-20260814`；
7. 重算 public/hidden manifest hash；
8. 保留 reference/negative check rows；
9. 记录零副作用与非主张；
10. 若 expected verdict 漂移、ID重叠、manifest hash不一致或side effect非零，fail-closed。

生成的 receipt 摘要：

```yaml
schema_version: solve-vein/vms42-state-normalizer-unseen-extension/v1
extension_id: vms42-state-normalizer-unseen-qualification-extension-20260814
overall_verdict: PASS
profile_qualification_verdict: DEVELOPMENT_UNSEEN_EXTENSION_PACK_PASS_NOT_LIVE_QUALIFIED
case_count: 2
reference_candidate_count: 2
negative_candidate_count: 2
public_manifest_sha256: 1025b27c649806910407d64ba8eb318dbb19792c1da1c3e7711489e4ce9648ed
hidden_manifest_sha256: b20bcbdcd875c05cdc8afc46c6899783dfcbd70c06446aa2a33b5673038ae120
receipt_stdout_sha256: 5f238ec8df5ace4e095f61fd63d93d206fed40b4a483e30c0d3e93c5c023b531
```

`receipt_stdout_sha256` 是当前开发命令 stdout 的内容哈希，用于复验命令输出形状；它不是 append-only D盘物证，也不构成 live receipt。

---

## 5. 测试矩阵

新增 8 项测试：

| 测试 | 目的 |
|---|---|
| `test_unseen_extension_pack_passes_but_does_not_qualify_profile` | 正向构造 PASS，但 profile 仍不资格化 |
| `test_same_fixture_as_base_is_rejected_as_case_overlap` | 同fixture冒充unseen时拒绝 |
| `test_candidate_id_overlap_with_base_is_rejected` | 与旧candidate ID重叠时拒绝 |
| `test_expected_verdict_drift_is_rejected_before_extension_pass` | expected verdict 漂移时拒绝 |
| `test_public_manifest_keeps_hidden_dictionary_and_acceptables_out` | public manifest key层不泄漏hidden对象 |
| `test_public_and_hidden_manifest_hashes_are_bound_to_unseen_pack_id` | pack_id/hash绑定不可漂移 |
| `test_cli_outputs_pass_receipt` | CLI stdout为PASS receipt |
| `test_unseen_pack_builder_has_no_model_solver_database_network_or_subprocess_import` | 禁止模型/DB/网络/子进程导入面 |

专项命令：

```bash
.venv/bin/python -m unittest system.tests.solve_vein_analysis.test_state_normalizer_vms42_unseen_pack -v
```

结果：

```text
Ran 8 tests in 0.100s
OK
```

---

## 6. 非主张

本POC不主张：

- 不证明任何 Devin/Codex/模型 extractor profile 已资格化；
- 不证明真实 reviewer 判断可通过；
- 不授权 live execution；
- 不证明 streaming 或增量 normalizer；
- 不把 normalized bundle 写入 DAG；
- 不证明 Trace→Tell/Hint选择；
- 不触碰入题侧代码、资产或历史运行物证。

---

## 7. 下一步

VMS-42 的下一步有两条安全路线：

1. **state-normalized bundle 回写DAG设计与零模型实现**：把 normalized bindings 从纯评分对象推进为可被 Reasoning Event DAG 消费的 bundle，并定义 occurrence/state/axis provenance；
2. **角色资产/preexecution freeze**：为未来真实 State Normalizer extractor 准备 candidate-visible资产、hidden grader、manual review package和不可消费LiveRunPermit计划。

在此之前不得启动真实模型，不得把 `DEVELOPMENT_UNSEEN_EXTENSION_PACK_PASS_NOT_LIVE_QUALIFIED` 升格为 live qualification。
