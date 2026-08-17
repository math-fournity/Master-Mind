# 382-v0-2026-08-14-POC-VMS-42-State-Normalizer-hidden-join-零模型

## 0. 本文定位

本文是 VMS-42 State Normalizer 的第三个零模型步骤：

1. 380 号：确定性多轴 normalizer 核心；
2. 381 号：public/hidden 资格包冻结；
3. 本文：hidden join 形状。

hidden join 的目标是提前冻结未来 live 资格化时最容易出错的一段边界：

```text
候选模型/Reviewer 可见：public manifest + candidate bundle
hidden join 可见：dictionary + acceptable set + candidate bundle
输出：join receipt
```

candidate bundle 里允许出现模型产出的 `StateNormalizationInput`，因此可以含 `raw_axis_claims`；但绝不能含 dictionary、acceptable set、expected verdict、state constraints 或 hidden reference。

本步骤仍然是零模型：它不运行 Devin，不运行 Codex，不启动 Solver，不连接 DB/Redis，也不写文件。

## 1. 新增物证

新增文件：

- `system/tests/solve_vein_analysis/vms42_state_normalizer_hidden_join.py`
- `system/tests/solve_vein_analysis/vms42_state_normalizer_hidden_join.ref`
- `system/tests/solve_vein_analysis/vms42_state_normalizer_hidden_join.ai-check`
- `system/tests/solve_vein_analysis/test_state_normalizer_vms42_hidden_join.py`
- `system/tests/solve_vein_analysis/test_state_normalizer_vms42_hidden_join.ref`
- `system/tests/solve_vein_analysis/test_state_normalizer_vms42_hidden_join.ai-check`

依赖的冻结物证：

- `system/tests/solve_vein_analysis/state_normalizer_fixtures/vms42_cases.json`
- `system/tests/solve_vein_analysis/build_vms42_state_normalizer_pack.py`
- `system/solve_vein_analysis/state_normalization.py`

## 2. Hidden Join 合同

`vms42_state_normalizer_hidden_join.py` 定义：

- `CANDIDATE_BUNDLE_SCHEMA_VERSION = solve-vein/vms42-state-normalizer-candidate-bundle/v1`
- `HIDDEN_JOIN_SCHEMA_VERSION = solve-vein/vms42-state-normalizer-hidden-join/v1`

candidate bundle 必须包含：

- `pack_id`
- `public_manifest_sha256`
- `candidate_source`
- `candidates[]`
  - `case_id`
  - `candidate_id`
  - `candidate_input`
  - `candidate_input_sha256`
- `explicit_nonclaims`

hidden join 必须：

1. 先重建381号pack并核对 `public_manifest_sha256`；
2. 拒绝candidate bundle中的hidden key泄漏；
3. 对每个candidate重算 `candidate_input_sha256`；
4. 用hidden dictionary/acceptable set调用 deterministic evaluator；
5. 保留negative结果，不得删除失败candidate；
6. 输出零副作用receipt；
7. 即使reference candidate全部PASS，也只能给出 `DEVELOPMENT_REFERENCE_JOIN_PASS_NOT_LIVE_QUALIFIED`。

## 3. 当前零模型结果

新增专项测试：

```text
test_state_normalizer_vms42_hidden_join.py
  8 tests
```

覆盖：

- reference candidate bundle hidden join PASS；
- negative candidate bundle hidden join FAIL，但不抛弃失败；
- public manifest hash mismatch拒绝；
- candidate input hash mismatch拒绝；
- candidate bundle顶层hidden key泄漏拒绝；
- candidate input嵌套expected verdict泄漏拒绝；
- CLI输出零副作用receipt；
- hidden join模块无模型、Solver、数据库、网络或subprocess import。

VMS-42当前累计：

- core tests：8；
- pack tests：7；
- hidden join tests：8；
- total VMS-42专项：23。

全量解题侧测试计数在本轮更新后应为 249 项。

## 4. 非主张

本 POC 不主张：

- 不资格化任何模型抽取器；
- 不证明真实Solver thinking可以自动变成正确axis claims；
- 不授权live run；
- 不产生人工盲审结果；
- 不测试流式/增量normalizer；
- 不测试Trace/Tell/Hint检索或因果效果。

## 5. 下一步

VMS-42下一步应当是：

1. 将hidden join receipt接到未来manual/reviewer judgment合同；
2. 设计全新未见qualification extension，而不是继续复用380/381/382的开发fixture；
3. 定义state-normalized bundle如何回写推理事件DAG节点；
4. 再往后才是角色资产与preexecution freeze。

在没有明确 LiveRunPermit 前，仍禁止启动 Devin/Codex/Solver 或连接DB。
