# 383-v0-2026-08-14-POC-VMS-42-State-Normalizer-reviewer-judgment-零模型

## 0. 本文定位

本文是 VMS-42 State Normalizer 的第四个零模型步骤。

前置链条：

1. 380号：多轴 State Normalizer 确定性核心；
2. 381号：public/hidden 资格包；
3. 382号：candidate bundle hidden join；
4. 本文：sealed reviewer judgment 合同。

本文冻结的不是人工审查结果本身，而是未来 Reviewer 必须提交的 sealed judgment 对象形状。Reviewer 只允许看：

- public manifest；
- candidate bundle；
- candidate bundle 中的 `StateNormalizationInput`。

Reviewer 不允许看：

- dictionary；
- acceptable set；
- reference candidate；
- hidden join result；
- hidden mechanical evaluation。

因此本文的 reviewer judgment 合同必须先于最终 manual+hidden join 合并存在，防止未来“看过hidden评分再写人工判断”的 hindsight 污染。

## 1. 新增物证

新增文件：

- `system/tests/solve_vein_analysis/vms42_state_normalizer_manual_judgment_contract.py`
- `system/tests/solve_vein_analysis/vms42_state_normalizer_manual_judgment_contract.ref`
- `system/tests/solve_vein_analysis/vms42_state_normalizer_manual_judgment_contract.ai-check`
- `system/tests/solve_vein_analysis/test_state_normalizer_vms42_manual_judgment_contract.py`
- `system/tests/solve_vein_analysis/test_state_normalizer_vms42_manual_judgment_contract.ref`
- `system/tests/solve_vein_analysis/test_state_normalizer_vms42_manual_judgment_contract.ai-check`

依赖：

- `system/tests/solve_vein_analysis/vms42_state_normalizer_hidden_join.py`
- `system/tests/solve_vein_analysis/build_vms42_state_normalizer_pack.py`

## 2. Judgment Schema

`vms42_state_normalizer_manual_judgment_contract.py` 定义：

```text
solve-vein/vms42-state-normalizer-sealed-reviewer-judgment/v1
```

sealed judgment 必须绑定：

- `pack_id`
- `public_manifest_sha256`
- `candidate_bundle_sha256`
- `reviewed_candidates[]`
  - `case_id`
  - `candidate_id`
  - `candidate_input_sha256`

并必须包含 blinding attestation：

```json
{
  "reviewer_view_only": true,
  "dictionary_seen": false,
  "acceptable_set_seen": false,
  "reference_candidates_seen": false,
  "hidden_join_result_seen": false
}
```

## 3. Reviewer Judgment 六个轴

当前最小轴：

1. `candidate_bundle_integrity`
2. `public_manifest_alignment`
3. `occurrence_set_fidelity`
4. `required_axis_coverage_fidelity`
5. `raw_axis_claim_source_fidelity`
6. `no_hidden_gold_in_candidate`

每个轴只允许：

```text
PASS | FAIL | INCONCLUSIVE
```

最终 judgment 只允许：

```text
MANUAL_PASS | MANUAL_FAIL | MANUAL_INCONCLUSIVE
```

一致性约束：

- `MANUAL_PASS` 要求全部轴为 `PASS`；
- `MANUAL_FAIL` 至少要求一个轴为 `FAIL`；
- missing/duplicate reviewed candidate 必须 fail。

## 4. 当前零模型结果

新增专项测试：

```text
test_state_normalizer_vms42_manual_judgment_contract.py
  10 tests
```

覆盖：

- synthetic valid judgment 与 candidate bundle 精确绑定；
- contract summary 零副作用，且不运行 hidden join；
- hidden material exposure attestation 拒绝；
- candidate bundle hash drift 拒绝；
- reviewed candidate drift 拒绝；
- `MANUAL_PASS` 但某轴 `FAIL` 拒绝；
- duplicate reviewed candidate 拒绝；
- missing nonclaim 拒绝；
- CLI `--validate --candidate-bundle` 成功/失败；
- 模块无模型、Solver、数据库、网络、subprocess import。

VMS-42当前累计：

- core tests：8；
- qualification pack tests：7；
- hidden join tests：8；
- reviewer judgment contract tests：10；
- total VMS-42专项：33。

全量解题侧测试计数在本轮更新后应为 259 项。

## 5. 非主张

本文不主张：

- 不执行真实人工审查；
- 不导入真实模型输出；
- 不运行 hidden join；
- 不读取 hidden dictionary / acceptable set；
- 不资格化任何 state extractor profile；
- 不授权 live execution。

## 6. 下一步

下一步应当是：

1. final reviewer+hidden-join receipt：把 sealed reviewer judgment 与 hidden join receipt 合并，但不提升为模型资格；
2. 全新未见 qualification extension：不再复用380—383的开发fixture；
3. state-normalized bundle 回写推理事件DAG；
4. 再往后才是角色资产、preexecution freeze 和 LiveRunPermit。
