# POC-VMS-42 State Normalizer预注册协议：多轴状态绑定

**日期**：2026-08-14  
**状态**：`PREREGISTERED_OFFLINE_CORE_IMPLEMENTED / LIVE_NOT_AUTHORIZED`  
**阶段**：`SV-S3.1`  
**前置**：VMS-35 gold语义反例、VMS-40多视图真值、VMS-41R1 Event Extractor零模型链  
**代码入口**：`system/solve_vein_analysis/state_normalization.py`  
**测试入口**：`system/tests/solve_vein_analysis/test_state_normalizer_vms42.py`

---

## 1. 为什么需要VMS-42

VMS-35暴露了一个关键问题：单一`canonical_math_state_id`会同时承载问题义务、策略方法、表示、知识状态和分支生命周期，导致两类错误：

1. 该合并的problem obligation没合并；
2. 不该合并的strategy/representation/knowledge被压成同一状态。

VMS-40已经证明多轴State Binding是正确方向。VMS-42把这件事从“真值Evaluator的一部分”拆成独立State Normalizer组件。

---

## 2. 第一版范围

本阶段是零模型离线核心，不资格化Devin角色。它只证明：

- raw axis claim可以通过冻结dictionary归一化到canonical value id；
- `PROBLEM_OBLIGATION`、`STRATEGY_METHOD`、`REPRESENTATION`、`KNOWLEDGE_STATE`、`BRANCH_LIFECYCLE`、`EPISTEMIC_VALIDITY`等轴彼此独立；
- `MUST_LINK`、`CANNOT_LINK`、`EXACT_VALUE`约束可机械判定；
- legacy projection可以由指定轴派生，而不是反过来吞掉多轴信息；
- unknown alias、duplicate claim、缺required axis都fail-closed。

本阶段不主张：

- State Normalizer模型角色已资格化；
- 可从任意raw reasoning自动抽出state axis；
- 已接入streaming、DB、Seven或两棵树；
- 可替代未来未见样本live资格实验。

---

## 3. 冻结夹具

夹具：`system/tests/solve_vein_analysis/state_normalizer_fixtures/vms42_cases.json`

当前包含两个case：

1. `V42-MULTIAXIS-REVISIT`：两个occurrence共享`PROBLEM_OBLIGATION`，但`STRATEGY_METHOD`、`REPRESENTATION`和`KNOWLEDGE_STATE`必须不同；
2. `V42-BRANCH-LIFECYCLE`：同一problem obligation下，tentative claim与contradicted/refuted claim必须在lifecycle和epistemic validity轴上分开。

---

## 4. 命令

```bash
.venv/bin/python \
  system/solve_vein_analysis/state_normalization.py \
  --pack system/tests/solve_vein_analysis/state_normalizer_fixtures/vms42_cases.json
```

预期：

- `schema_version = solve-vein/state-normalization-pack-evaluation/v1`；
- `case_count = 2`；
- `candidate_count = 4`；
- `mismatch_count = 0`；
- `overall_verdict = PASS`；
- 全部model/Devin/DB/Solver side effects为0。

---

## 5. 晋级规则

`SV-S3.1`只关闭离线核心合同。下一步若继续VMS-42，应做：

1. VMS-42不可变development calibration pack；
2. 全新未见State Normalizer qualification pack；
3. 角色资产与preexecution freeze；
4. LiveRunPermit与盲审/hidden join链。

未经上述链路，任何“State Normalizer PASS”只能指当前离线机械合同，不能指模型角色资格化。
