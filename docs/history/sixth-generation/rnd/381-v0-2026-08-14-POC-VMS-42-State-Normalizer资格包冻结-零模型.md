# 381-v0-2026-08-14-POC-VMS-42-State-Normalizer资格包冻结-零模型

## 0. 本文定位

本文是 380 号 VMS-42 State Normalizer 离线核心之后的资格包冻结文档。

380 号已经证明：在给定 `StateNormalizationInput + Dictionary + AcceptableSet` 的情况下，确定性 normalizer 能把 raw axis claim 映射到多轴 state binding，并机械判定 `MUST_LINK / CANNOT_LINK / EXACT_VALUE`、occurrence coverage 与 axis coverage。

本文只补下一层：

```text
冻结核心fixture
  → 派生 public case manifest（未来候选/Reviewer 可见）
  → 派生 hidden manifest（dictionary / acceptable set / reference / negative checks）
  → 机械自检 reference PASS 与 negative FAIL/INVALID
  → receipt 证明 public/hidden 分离和零副作用
```

它不调用模型、不启动 Devin、不连接 DB/Redis、不启动 Solver，不资格化任何 state extractor profile。

## 1. 设计原因

VMS-42 的目标不是让模型“看起来会归一化状态”，而是先把未来模型资格化所需的包形状钉死。

如果没有这层包合同，后续很容易出现三种假阳性：

1. 候选模型看见了 hidden `acceptable_set` 或 `expected_verdict`；
2. qualification pack 自称有 negative checks，但没有机械重放；
3. public manifest 暗中携带 raw gold candidates 或 state constraints，导致抽取器只是复述答案。

因此 VMS-42 资格包必须显式分离：

- public manifest：只包含 case id、occurrence id、要求输出的 schema、required axes 和 legacy projection axes；
- hidden manifest：包含 dictionary hash、acceptable set hash、reference candidate hash、negative candidate hash；
- check rows：由 deterministic evaluator 重放得出，不能信任 fixture 标签；
- receipt：记录 source fixture、protocol、public/hidden hashes、非主张和零副作用。

## 2. 物证

新增文件：

- `system/tests/solve_vein_analysis/build_vms42_state_normalizer_pack.py`
- `system/tests/solve_vein_analysis/build_vms42_state_normalizer_pack.ref`
- `system/tests/solve_vein_analysis/build_vms42_state_normalizer_pack.ai-check`
- `system/tests/solve_vein_analysis/test_state_normalizer_vms42_pack.py`
- `system/tests/solve_vein_analysis/test_state_normalizer_vms42_pack.ref`
- `system/tests/solve_vein_analysis/test_state_normalizer_vms42_pack.ai-check`

复用冻结输入：

- `system/tests/solve_vein_analysis/state_normalizer_fixtures/vms42_cases.json`
- `system/solve_vein_analysis/state_normalization.py`

## 3. Pack Builder 合同

`build_vms42_state_normalizer_pack.py` 的合同：

1. 输入必须是 `solve-vein/state-normalization-pack/v1`；
2. 先调用 `evaluate_state_normalization_pack()` 重放 source fixture，若整体不是 PASS 则 fail closed；
3. 每个 case 必须至少有一个 reference PASS candidate 和一个 negative candidate；
4. public manifest 不得含以下 key：
   - `dictionary`
   - `dictionary_sha256`
   - `acceptable_set`
   - `acceptable_set_sha256`
   - `state_constraints`
   - `candidates`
   - `reference_candidates`
   - `raw_axis_claims`
   - `expected_verdict`
   - `hidden`
5. hidden manifest 才记录 dictionary / acceptable set / reference / negative 的 hash；
6. receipt 显式写入：
   - `model_calls_authorized=0`
   - `devin_sessions_authorized=0`
   - `database_calls_authorized=0`
   - `solver_calls_authorized=0`
   - side effects 全 0；
7. builder 不写文件，不导入 `arango / requests / socket / subprocess / urllib`。

## 4. 当前零模型结果

当前 fixture：

- case count：2
- candidate count：4
- reference PASS candidates：2
- negative candidates：2
- source pack mismatch：0

专项测试：

```text
test_state_normalizer_vms42_pack.py
  7 tests
```

与 380 号 core tests 合计，VMS-42 当前新增 15 项专项测试。

全量解题侧测试计数在本轮更新后应为 241 项。

## 5. 通过标准

本 POC PASS 只表示：

```text
VMS42_STATE_NORMALIZER_QUALIFICATION_PACK_ZERO_MODEL_PASS
```

具体含义：

- public/hidden 分离机械成立；
- reference 与 negative rows 被 deterministic evaluator 重放；
- expected verdict drift 会被拒绝；
- public manifest hash drift 会被拒绝；
- pack builder 无模型、Devin、DB、Solver和网络执行面。

## 6. 非主张

本 POC 不主张：

- 不资格化任何 state extractor / Devin / Codex / Solver profile；
- 不授权 live run；
- 不测试 streaming 或增量 normalizer；
- 不证明 raw Solver thinking 能被自动抽成 axis claims；
- 不证明 Trace/Tell/Hint 检索或因果效果；
- 不修改入题侧代码、入题侧运行资产或历史物证。

## 7. 下一步

下一步不是直接 live，而是继续在零模型层补：

1. VMS-42 qualification pack 的盲审/hidden join 形状；
2. 将 state-normalized bundle 接回推理事件DAG节点；
3. 为后续推理树节点 identity 设计 `occurrence_id × state-axis-binding × branch lifecycle` 的组合键；
4. 只有在 qualification pack、manual/hidden join 和 explicit LiveRunPermit 都冻结后，才考虑模型抽取器资格化。
