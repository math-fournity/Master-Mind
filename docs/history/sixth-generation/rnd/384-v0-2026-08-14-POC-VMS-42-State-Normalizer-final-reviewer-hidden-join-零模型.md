# 384-v0-2026-08-14-POC-VMS-42-State-Normalizer-final-reviewer-hidden-join-零模型

## 0. 本文定位

本文是 VMS-42 State Normalizer 零模型资格链的第五步。

前置链条：

1. 380号：State Normalizer deterministic core；
2. 381号：public/hidden qualification pack；
3. 382号：candidate bundle hidden join；
4. 383号：sealed reviewer judgment contract；
5. 本文：final reviewer + hidden-join receipt。

本文冻结的是“两个独立裁决面如何合并”：

```text
candidate bundle
  ├─ reviewer judgment（只看public/candidate bundle）
  └─ hidden join（看hidden dictionary/acceptable set）
        ↓
final reviewer+hidden join receipt
```

这一步依然是零模型、零人工真实审查、零DB、零Solver、零Devin。

## 1. 新增物证

新增文件：

- `system/tests/solve_vein_analysis/vms42_state_normalizer_final_join_receipt.py`
- `system/tests/solve_vein_analysis/vms42_state_normalizer_final_join_receipt.ref`
- `system/tests/solve_vein_analysis/vms42_state_normalizer_final_join_receipt.ai-check`
- `system/tests/solve_vein_analysis/test_state_normalizer_vms42_final_join_receipt.py`
- `system/tests/solve_vein_analysis/test_state_normalizer_vms42_final_join_receipt.ref`
- `system/tests/solve_vein_analysis/test_state_normalizer_vms42_final_join_receipt.ai-check`

依赖：

- `vms42_state_normalizer_hidden_join.py`
- `vms42_state_normalizer_manual_judgment_contract.py`

## 2. Final Join 合同

`vms42_state_normalizer_final_join_receipt.py` 定义：

```text
solve-vein/vms42-state-normalizer-final-reviewer-hidden-join/v1
```

final join 必须核对：

1. reviewer judgment 对同一 candidate bundle 有效；
2. hidden join receipt 的 `candidate_bundle_sha256` 与 candidate bundle一致；
3. hidden join receipt 的 `public_manifest_sha256` 与 reviewer judgment一致；
4. manual verdict 与 hidden verdict 独立保留；
5. 任一侧 FAIL 都使 final FAIL；
6. 两侧都 PASS 时也只能输出：

```text
DEVELOPMENT_SYNTHETIC_FINAL_JOIN_PASS_NOT_LIVE_QUALIFIED
```

它绝不能把 synthetic reference candidate 的成功升级为真实模型资格。

## 3. 当前零模型结果

新增专项测试：

```text
test_state_normalizer_vms42_final_join_receipt.py
  8 tests
```

覆盖：

- synthetic reference final join PASS，但不live-qualified；
- hidden FAIL 保留为 final FAIL；
- manual FAIL 即使 hidden PASS 也保留为 final FAIL；
- candidate bundle hash mismatch 拒绝；
- invalid reviewer judgment 拒绝；
- public manifest hash mismatch 拒绝；
- CLI输出positive/negative receipt；
- 模块无模型、Solver、数据库、网络、subprocess import。

VMS-42当前累计：

- core tests：8；
- qualification pack tests：7；
- hidden join tests：8；
- reviewer judgment contract tests：10；
- final join receipt tests：8；
- total VMS-42专项：41。

全量解题侧测试计数在本轮更新后应为 267 项。

## 4. 非主张

本文不主张：

- 不资格化任何 state extractor profile；
- 不使用真实模型输出；
- 不执行真实人工review；
- 不授权live run；
- 不证明raw Solver thinking能自动抽成正确axis claims；
- 不测试流式/增量normalizer；
- 不测试Trace/Tell/Hint检索或因果效果。

## 5. 下一步

VMS-42之后真正该前进的方向是：

1. 全新未见 qualification extension：不能继续复用380—384开发fixture；
2. state-normalized bundle 回写推理事件DAG；
3. 设计状态identity如何进入推理树节点；
4. 再往后才是角色资产/preexecution freeze/live permit。
