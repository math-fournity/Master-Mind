# 解题侧非线性脉络分析运行手册

本手册只适用于 `system/solve_vein_analysis/`。确定性核心仍是 `0.1.0`；其外另有隔离的 Devin 认知角色实验运行时和 tmux 交互调试档。普通 `version`、`validate-assets`、`analyze` 与单元测试不会启动 Devin、Codex 或 Solver，也不连接 ArangoDB/Redis。只有本手册明确标为 **live** 的命令才允许调用 Devin。

任何命令都不得触碰入题侧代码、`system/assets/vein_analysis/`、历史运行目录或其 `AGENTS.md`。交互调试产物只能进入 `DEVELOPMENT_ONLY` 证据 lane。

---

## 1. 从哪里运行

进入 repo 根目录：

```bash
cd ~/master-mind-glm5.2-worktree
```

使用 repo 自带虚拟环境：

```bash
.venv/bin/python -m system.solve_vein_analysis.cli version
```

预期输出：

```text
0.1.0
```

---

## 2. 先验证运行资产

```bash
.venv/bin/python -m system.solve_vein_analysis.cli validate-assets
```

必须看到：

- `verdict: PASS`；
- `asset_count: 4`；
- `live_execution: NOT_TESTED`（当前资产集`0.3.0` manifest 的发布时声明）。

不得手工覆写这个不可变历史字段。当前命令只验证文件哈希；VMS-35的文件写入证据和VMS-38的debug执行合同证据都另行封存，二者都不是角色能力PASS。

---

## 3. 运行完整测试

```bash
.venv/bin/python -m unittest discover \
  -s system/tests/solve_vein_analysis \
  -p 'test_*.py' \
  -v
```

当前基线是 **295 个测试全部通过（2026-08-24实跑）**。测试包含：

- 五个正例 fixture；
- Next Closure 与独立 oracle 对账；
- 批处理与逐事件重放；
- tree/flattened comparison；
- 输入破坏与单父合流拒绝；
- 运行资产篡改/软链拒绝；
- CLI 原子封存与拒绝覆盖；
- 解题侧包不导入入题侧模块。
- 开工时冻结的 161 个入题侧文件逐项哈希不变。
- sandbox/no-sandbox 单因素启动合同、exact model/export/DONE 检查；
- ATIF-v1.7顶层step与实际tool call不重复计数；
- 使用 fake Devin 的真实 tmux 可观测、干预、正常退出、abort 与原子封存合同。
- VMS-39静态rules loader的隔离HOME/XDG、精确fixture显示、辅助副作用索引和独立全树审计合同。
- VMS-41R1 occurrence/projection、typed path、双时间状态、MERGE贡献、资源上限与联合file-effect审计。
- VMS-41R1不可变calibration pack的19场景逐轴重放、mutation DSL与tamper/symlink/expected漂移反例。
- VMS-41R1全新未见qualification pack的append-once复验、public/hidden split、真实source span receipt、负向mutation与tamper/symlink拒绝。
- VMS-41R1零模型preexecution freeze的0.4.1角色资产绑定、append-once复验、外部输出与漂移拒绝、零副作用授权。
- VMS-41R1 live runner shell的workspace计划、public/hidden split、零模型preflight receipt与`--execute` fail-closed。
- VMS-41R1 LiveRunPermit/盲审包计划的不可消费permit、Reviewer可见文件集、hidden join顺序与fail-closed反例。
- VMS-41R1 sealed manual judgment合同的case/attempt绑定、盲审attestation、六轴Verdict和CLI验证反例。
- VMS-41R1 hidden join simulator的synthetic manual judgment、fake/reference candidate、join顺序、negative mutation和development-only final verdict。
- VMS-41R1 fake live bundle与blind-review package materializer的Reviewer可见文件hash manifest、hidden隔离和非live输出声明。
- VMS-41R1 final qualification join receipt的case/attempt/candidate hash合并、fail-closed反例和非资格化边界。
- VMS-41R1 fake bundle append-only dry-run的临时输出根真实写包、重复写/repo根/symlink拒绝和hidden文件缺席。
- VMS-42 State Normalizer的多轴状态绑定、dictionary alias归一化、legacy projection、must/cannot/exact约束、fail-closed反例、零模型资格包public/hidden分离、hidden join、reviewer judgment合同、final receipt、unseen qualification extension和DAG writeback sidecar。
- VMS-43 Trace Auditor结构审计的branch/failure/revisit/merge/recovery family观测、必需family缺失FAIL、state sidecar hash/order兼容和DAG端点/edge ID反例。

如果测试数发生变化，应解释新增/删除了哪些测试，不能只更新数字。

---

## 4. 分析一条冻结轨迹

输出目录必须不存在：

```bash
OUT=/tmp/solve-vein-c5-result
test ! -e "$OUT"

.venv/bin/python -m system.solve_vein_analysis.cli analyze \
  --input system/tests/solve_vein_analysis/fixtures/c5_composite.trajectory.json \
  --output "$OUT"
```

成功时命令输出 `run-manifest.json` 的内容，退出码为 0。检查：

```bash
find "$OUT" -maxdepth 1 -type f -print | sort
.venv/bin/python -m json.tool "$OUT/audit-report.json"
.venv/bin/python -m json.tool "$OUT/run-manifest.json"
```

预期关键值：

```text
pipeline_integrity = PASS
graph_fidelity = PASS
fca_closure_correctness = PASS
relational_scaling = PASS
live_extraction = NOT_TESTED
incremental_equivalence = true
live_model_calls = 0
database_connections = 0
solver_launches = 0
```

不要把 `/tmp` 用作未来正式数据根；这里仅用于本地离线演示。正式 Seven/System 接入必须服从各自 D 盘资产合同。

---

## 5. 重跑 POC-VMS-31

POC 输出目录同样必须不存在。建议使用新 run ID，而不是覆盖既有结果：

```bash
POC_OUT=system/tests/solve_vein_analysis/poc_results/poc-vms-31-manual-001
test ! -e "$POC_OUT"

.venv/bin/python system/tests/solve_vein_analysis/run_poc.py \
  --output "$POC_OUT"
```

查看：

```bash
.venv/bin/python -m json.tool "$POC_OUT/poc-report.json"
sed -n '1,200p' "$POC_OUT/poc-report.md"
shasum -a 256 "$POC_OUT"/*
```

正式基线结果在：

```text
system/tests/solve_vein_analysis/poc_results/poc-vms-31-20260814/
```

POC PASS 的含义仅是结构化 fixture 范围内的算法结果通过。若 `raw_thinking_extraction`、`live_solver_integration` 或 `large_scale_performance` 被写成 PASS，应视为协议违规。

---

## 6. 已封存的 live POC：只读查看，不得原地重跑

POC-VMS-32/33/35 都是 append-once 历史证据。尤其 VMS-35 已按预注册协议执行一次、没有科学重试；不得为了得到 PASS 再使用同一 ID 或覆盖原目录。

```bash
POC35=system/tests/solve_vein_analysis/poc_results/poc-vms-35-20260814
python3 -m json.tool "$POC35/poc-report.json"
sed -n '1,240p' "$POC35/poc-report.md"
python3 -m json.tool "$POC35/preexecution-freeze-manifest.json"
```

当前 VMS-35 的正确解释：

- 三个角色的 Devin 进程均为 exit 0；
- exact effective model 均为 `glm-5-2`，即本机 catalog 的 GLM-5.2 High；
- 三个角色都写出严格 JSON，三个 export 都存在且可解析；
- extractor 为科学 `PARTIAL`；normalizer 为科学 `FAIL` 且 DONE 语法不精确；auditor 为科学 `PARTIAL`；
- 总体为 `INCONCLUSIVE_PROTOCOL`，角色资格均未通过；
- no-sandbox 只复现来源侧运行合同，不证明强 filesystem isolation。

POC-VMS-36同样已经封存，不得再次执行上述`start`命令：

```bash
POC36=system/tests/solve_vein_analysis/poc_results/poc-vms-36-tmux-canary-20260814
python3 -m json.tool "$POC36/tmux-debug-launch-receipt.json"
python3 -m json.tool "$POC36/tmux-debug-abort-receipt.json"
tail -80 "$POC36/pane-captures/000004.txt"
```

VMS-36证明tmux实时可观测和exact model/export物证可工作，但workspace位于repo内、被自身repo deny规则拒绝，因此没有输出/DONE并以`ABORTED / INCONCLUSIVE_PROTOCOL`封存。修复必须使用新版本和POC-VMS-37；不得以VMS-36原ID重跑。

POC-VMS-37也已经执行和封存，不得重跑。它的D盘preflight、tmux和exact model/export均通过，但冻结config中的`Read(/Volumes/**)`又拒绝了自身workspace；同时runner的历史默认值导致receipt误用VMS-36 attempt ID。结果为`ABORTED / INCONCLUSIVE_PROTOCOL`，详见360号。

下面只是VMS-37的**历史首次启动命令投影**，不得再执行：

```bash
python3 system/tests/solve_vein_analysis/run_tmux_canary.py start \
  --poc-id POC-VMS-37 \
  --attempt-id poc-vms-37-extractor-tmux-a1 \
  --freeze system/tests/solve_vein_analysis/live_fixtures/poc_vms_37.freeze.json \
  --output /data/master-mind-solve-vein-data/poc-results/poc-vms-37-d-volume-tmux-20260814
```

注意：历史实跑当时未显式传`--attempt-id`，所以实际receipt保留了错误的VMS-36 ID。上面补出正确值只用于说明新合同，不改写历史物证。现行runner已将`--attempt-id`改为必填，且必须精确等于`<poc-id-lower>-extractor-tmux-a1`。

runner会在模型调用前验证D卷mount、卷README与专属根README哈希、非symlink、同一device和output范围。任何一项失败均在启动前BLOCK，禁止fallback。

POC-VMS-38已于`2026-08-14T14:50:02Z`消费唯一start权利，当时freeze manifest校验、48项回归和入题侧保护基线均PASS。它使用新资产`0.3.0`，以dangerous/bypass模式启动，并用workspace `AGENTS.md`规定可读/可写/禁止动作。下面是已执行的历史start命令，不得再次执行：

```bash
python3 system/tests/solve_vein_analysis/run_tmux_canary.py start \
  --poc-id POC-VMS-38 \
  --attempt-id poc-vms-38-extractor-tmux-a1 \
  --freeze system/tests/solve_vein_analysis/live_fixtures/poc_vms_38.freeze.json \
  --output /data/master-mind-solve-vein-data/poc-results/poc-vms-38-dangerous-agents-tmux-20260814
```

本次live bundle由start receipt冻结为：

```text
/data/master-mind-solve-vein-data/poc-results/.poc-vms-38-dangerous-agents-tmux-20260814.tmux-live-bda8d0d1205449ddb4a13ef0cbfb2e19
```

无论最终PASS、INCONCLUSIVE还是FAIL，都不得原ID重试。

VMS-38随后在同一次attempt中完成并封存，最终目录为：

```text
/data/master-mind-solve-vein-data/poc-results/poc-vms-38-dangerous-agents-tmux-20260814/
```

最终结果是`SUPPORTED_WITHIN_DEBUG_CANARY / DEVELOPMENT_ONLY`：输出通过严格解析和source-span hash复核，DONE有效，effective model为`glm-5-2`，原始ATIF中的7次tool call全部局限于本次workspace，唯一一次有记录的`/exit`后进程exit 0。封存后旧evaluator的探索性投影为`PARTIAL`（occurrence 10/10、typed edge 9/13、真合流2/2、误合流0），因此更不能把执行成功升级为角色资格，详见362号。

注意：VMS-38历史final receipt中的`step_count=0/tool_event_count=15`是旧解析器缺陷；原始ATIF实际为13 step/7 call。final bundle不得修改。现行解析器与单测已经修正，未来run使用新逻辑。

### 6.1 POC-VMS-39：静态与live均已封存

静态Stage A已经执行，原输出目录不可覆盖：

```text
/data/master-mind-solve-vein-data/poc-results/poc-vms-39-static-loader-20260814/
/data/master-mind-solve-vein-data/poc-results/poc-vms-39-static-loader-audit-20260814/
```

历史执行命令投影如下；不得用相同output重跑：

```bash
.venv/bin/python system/tests/solve_vein_analysis/run_agents_limit_static.py \
  --poc-id POC-VMS-39 \
  --devin-binary ~/.local/bin/devin \
  --protocol '第六代系统研发过程文档/364-v0-2026-08-14-POC-VMS-39-Devin-AGENTS装载物理边界-官方回源与隔离实测协议.md' \
  --freeze system/tests/solve_vein_analysis/live_fixtures/poc_vms_39.freeze.json \
  --output /data/master-mind-solve-vein-data/poc-results/poc-vms-39-static-loader-20260814
```

七个静态cell均`STATIC_SHOW_FULL_EXACT`，最大262,144 bytes；它只说明`rules show`没有16 KiB截断。首版receipt的主fixture/stdout完整性PASS，但rename前绝对路径失效且49个CLI辅助文件未进入首版索引，所以整体保持`PARTIAL_UNINDEXED_AUXILIARY`；独立audit bundle已对原目录101个文件全量哈希，原bundle没有被修改。详情见365号。

live Stage B已经按固定顺序执行A16、A16P1、A32；观察到截断后，按conditional expansion只补跑A16M1。四个attempt均写出output/DONE/export、只接受一次记账`/exit`、exit 0并封存。A16M1与A16 full exact；A16P1和A32均在ATIF中出现`Rule content truncated to 16384 bytes`，A32严格前缀恰为16,384 bytes。A64/A128/A256按停止规则未运行。

四个原attempt ID永久不可重跑。只读复验入口：

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/aggregate_agents_limit_live.py verify \
  --bundle /data/master-mind-solve-vein-data/poc-results/poc-vms-39-live-aggregate-20260814
```

预期`artifact_integrity=PASS`。aggregate receipt文件SHA为`b77b97e1cfb273f5d905ea1c5e3f218d7db1a488fd56a63b5e04b10a3f92dc1b`。最终Verdict只限定Devin CLI `3000.4.25 (7e8e528a)`、`glm-5-2`和本次profile；实现中的短`AGENTS.md`必须显著低于该上限，Tell/Trace权威内容改由显式分片文件承载。

### 6.2 POC-VMS-41：已封存，只允许只读复核

VMS-41的四个exact attempt已经全部消费并封存，原ID绝对不得重跑。artifact/replay链PASS，但冻结机械结果为0/4，协议为`INCONCLUSIVE_PROTOCOL`，当前profile为`NOT_QUALIFIED`。事后人工诊断在看到机械结果后才进行，故只能是`FAILURE_LOCALIZATION_ONLY`，不能升级确认性结论。VMS-41R1的V2 parser/evaluator、联合file-effect auditor和不可变calibration pack已离线实现；全新未见qualification pack、阈值、盲审rubric、attempt IDs、0.4.1角色资产、零模型preexecution freeze、live runner shell、不可消费LiveRunPermit/盲审包计划、sealed manual judgment合同、hidden join simulator、fake materializer、final qualification join receipt和fake bundle append-only dry-run也已冻结。VMS-42 State Normalizer离线核心、零模型资格包、hidden join、reviewer judgment合同、final receipt、unseen qualification extension与DAG writeback sidecar已冻结。VMS-43 Trace Auditor结构审计已冻结。当前295项测试PASS（2026-08-24实跑），live仍未授权。

校准包可只读重放：

```bash
.venv/bin/python -m \
  system.tests.solve_vein_analysis.run_event_extractor_calibration \
  > /tmp/vms41r1-calibration-result.json

.venv/bin/python -m json.tool /tmp/vms41r1-calibration-result.json
```

预期`verdict=PASS`、`candidate_scenario_count=13`、`file_effect_scenario_count=6`、`mismatches=[]`且`evidence_lane=DEVELOPMENT_ONLY`。该命令不调用模型、Solver、DB、Redis或网络；PASS只证明校准合同，不得写成Event Extractor profile资格PASS。

未见qualification pack可只读复验：

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/build_vms41r1_qualification_pack.py \
  > /tmp/vms41r1-qualification-pack-load.json

.venv/bin/python -m json.tool /tmp/vms41r1-qualification-pack-load.json
```

预期`pack_id=vms41r1-event-extractor-v2-qualification-20260814`、`case_count=6`、`reference_candidate_count=6`、`negative_check_count=4`、`summary.verdict=PASS`、`manifest_sha256=ac270b0a6aadceae18c141200a8fd7abbbbfb4c2272b4b6e92c43350ffee020b`。该命令只加载/核对既有fixture和隐藏参考集，不调用模型、Solver、DB、Redis或网络；其机械上限仍是`PENDING_BLIND_MANUAL_AUDIT`。

零模型preexecution freeze可只读复验：

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/freeze_vms41r1_event_extractor_preexecution.py
```

预期`operation=ALREADY_FROZEN`、`planned_live_attempts=6`、`freeze_sha256=37a9fa407be5341305fe61fe63e5a26894d98271c7d7bd3480e6413d0d7295ad`，并且`model_calls_authorized=devin_sessions_authorized=database_connections_authorized=solver_calls_authorized=0`。该命令只复验repo内冻结文件，不启动Devin session。

VMS-41R1 live runner shell 的默认入口只生成零模型preflight receipt：

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/run_vms41r1_event_extractor_qualification.py
```

预期`overall_status=READY_FOR_AUTHORIZATION`、`live_authorization_status=NOT_AUTHORIZED`、`case_count=attempt_count=6`、`workspace_plan_verdict=hidden_public_split_verdict=PASS`，并且全部`side_effects`为0。该命令只规划工作区、检查public/hidden分离与freeze绑定，不启动Devin session、不调用模型、不连接DB/Redis/Solver。

未获新授权前，下面的负向检查必须fail-closed：

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/run_vms41r1_event_extractor_qualification.py \
  --execute
```

预期退出码为2，stderr含`LIVE_NOT_AUTHORIZED`。如果它实际启动Devin或创建live attempt，属于协议P0事故。

LiveRunPermit与盲审包计划可零模型复验：

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/build_vms41r1_live_permit_review_plan.py
```

预期`schema_version=solve-vein/vms41r1-live-permit-review-plan/v1`、`live_run_permit.permit_consumable=false`、`live_run_permit.authorized_live_attempts=0`、`blind_review_plan.case_count=6`，并且全部`side_effects`为0。该命令只冻结未来permit和blind-review package的形状，不生成可消费permit，不创建live workspace，也不让Reviewer看到hidden acceptable set/reference/threshold/rubric。

sealed manual judgment 合同可零模型复验：

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/vms41r1_manual_judgment_contract.py
```

预期`judgment_schema_version=solve-vein/vms41r1-sealed-manual-judgment/v1`、`case_count=6`且全部`side_effects`为0。这个命令只输出未来人工判断对象的合同摘要；它不执行人工审稿、不导入真实review、不运行hidden grader，也不资格化模型。

hidden join simulator可零模型复验：

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/vms41r1_hidden_join_simulator.py
```

预期`schema_version=solve-vein/vms41r1-hidden-join-simulator/v1`、`simulator_status=DEVELOPMENT_ONLY`、`case_count=6`、`overall_join_verdict=PASS_DEVELOPMENT_SIMULATION_ONLY`且全部`side_effects`为0。它只用synthetic manual judgment和hidden reference candidate证明join顺序；不使用真实live输出。

fake live bundle与blind-review package materializer可零模型复验：

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/vms41r1_fake_live_bundle_materializer.py
```

预期`schema_version=solve-vein/vms41r1-fake-live-bundle-materializer/v1`、`materializer_status=PLAN_ONLY_NO_FILES_WRITTEN`、`case_count=6`、`hidden_public_split_verdict=PASS`且全部`side_effects`为0。它只输出未来Reviewer可见包的hash计划；不写真实bundle。

final qualification join receipt可零模型复验：

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/vms41r1_final_qualification_join_receipt.py
```

预期`schema_version=solve-vein/vms41r1-final-qualification-join-receipt/v1`、`receipt_status=FINAL_JOIN_RECEIPT_DEVELOPMENT_ONLY`、`case_count=6`、`final_join_verdict=PASS_DEVELOPMENT_SIMULATION_ONLY`、`profile_qualification_verdict=NOT_QUALIFIED_LIVE_NOT_AUTHORIZED`且全部`side_effects`为0。它只证明fake materializer与hidden join simulator可以按case/attempt/candidate hash合并；不资格化profile。

fake bundle append-only dry-run可在临时目录复验：

```bash
tmp_dir="$(mktemp -d)"
.venv/bin/python \
  system/tests/solve_vein_analysis/vms41r1_fake_bundle_append_only_dry_run.py \
  --output-root "$tmp_dir/vms41r1-fake-bundle"
```

预期`schema_version=solve-vein/vms41r1-fake-bundle-append-only-dry-run/v1`、`dry_run_status=APPEND_ONLY_FAKE_BUNDLE_WRITTEN`、`case_count=6`、`side_effects.local_files_written=31`、`side_effects.hidden_files_written=0`、`profile_qualification_verdict=NOT_QUALIFIED_LIVE_NOT_AUTHORIZED`。该命令只写显式临时输出根；不得把repo目录、已有目录或symlink作为输出根。

VMS-42 State Normalizer离线核心可复验：

```bash
.venv/bin/python \
  system/solve_vein_analysis/state_normalization.py \
  --pack system/tests/solve_vein_analysis/state_normalizer_fixtures/vms42_cases.json
```

预期`schema_version=solve-vein/state-normalization-pack-evaluation/v1`、`case_count=2`、`candidate_count=4`、`mismatch_count=0`、`overall_verdict=PASS`，并且全部model/Devin/DB/Solver side effects为0。它只证明多轴归一化机械合同，不资格化State Normalizer模型角色。

VMS-42 State Normalizer零模型资格包可复验：

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/build_vms42_state_normalizer_pack.py
```

预期`schema_version=solve-vein/vms42-state-normalizer-qualification-pack/v1`、`case_count=2`、`reference_candidate_count=2`、`negative_candidate_count=2`、`overall_verdict=PASS`、`public_manifest_sha256`和`hidden_manifest_sha256`均可重算，并且全部model/Devin/DB/Solver/file-write side effects为0。它只证明public/hidden资格包形状，不资格化模型角色。

VMS-42 State Normalizer hidden join可复验：

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/vms42_state_normalizer_hidden_join.py
```

预期`schema_version=solve-vein/vms42-state-normalizer-hidden-join/v1`、`candidate_count=2`、`pass_count=2`、`fail_count=0`、`overall_verdict=PASS`，但`profile_qualification_verdict=DEVELOPMENT_REFERENCE_JOIN_PASS_NOT_LIVE_QUALIFIED`。这只证明hidden join形状，不能把reference candidate bundle当成模型能力证据。

VMS-42 State Normalizer reviewer judgment合同可复验：

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/vms42_state_normalizer_manual_judgment_contract.py
```

预期`schema_version=solve-vein/vms42-state-normalizer-reviewer-judgment-contract/v1`，side effects全部为0，并且明确`does_not_run_hidden_join`、`does_not_perform_reviewer_judgment`。真实`--validate`需要外部sealed reviewer judgment JSON和对应candidate bundle；当前仓库只提供synthetic测试，不导入真实人工审查。

VMS-42 State Normalizer final reviewer+hidden join receipt可复验：

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/vms42_state_normalizer_final_join_receipt.py
```

预期`schema_version=solve-vein/vms42-state-normalizer-final-reviewer-hidden-join/v1`、`overall_verdict=PASS`，但`profile_qualification_verdict=DEVELOPMENT_SYNTHETIC_FINAL_JOIN_PASS_NOT_LIVE_QUALIFIED`。如加`--negative`，预期`overall_verdict=FAIL`且失败被保留。该命令只证明final receipt形状，不能资格化模型。

VMS-42 State Normalizer unseen qualification extension可复验：

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/build_vms42_state_normalizer_unseen_pack.py
```

预期`schema_version=solve-vein/vms42-state-normalizer-unseen-extension/v1`、`overall_verdict=PASS`、`case_count=2`、`reference_candidate_count=2`、`negative_candidate_count=2`，但`profile_qualification_verdict=DEVELOPMENT_UNSEEN_EXTENSION_PACK_PASS_NOT_LIVE_QUALIFIED`。该命令证明新旧case/candidate ID不重叠、expected drift拒绝、public/hidden隔离和extension receipt形状，不资格化模型。

VMS-42 State Normalizer DAG writeback sidecar可复验：

```bash
.venv/bin/python \
  system/solve_vein_analysis/state_normalized_dag.py \
  --demo-unseen
```

预期`schema_version=solve-vein/state-normalized-dag-annotation-bundle/v1`、`overall_verdict=PASS`、`annotation_count=3`、`topological_annotation_order=[s0,s1,s2]`，且全部model/Devin/DB/Solver/file-write side effects为0。该命令证明PASS normalized bundle可以按DAG event_id/topological order生成不可变annotation sidecar，不改写DAG本体，也不资格化模型。

VMS-43 Trace Auditor结构审计可复验：

```bash
.venv/bin/python \
  system/solve_vein_analysis/trace_auditor.py \
  --demo-complex
```

预期`schema_version=solve-vein/trace-audit/v1`、`overall_verdict=PASS`，并观察到`BRANCH_EXPLORATION`、`FAILED_BRANCH`、`REVISIT_WITH_NEW_INFORMATION`、`TRUE_MERGE`、`RECOVERY_AFTER_CONTRADICTION`五类family。该命令只审计已经结构化的DAG，不从自然语言抽取event，不判断证明正确性，不资格化模型角色。

冻结清单已经生成；下面命令现在只能得到字节完全相同的append-once复验结果，任何差异都必须fail-closed。它只执行本地测试以及`devin --version`、`devin models list`身份探针，不启动Devin session、不调用模型、不连接DB/Redis/Solver：

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/freeze_event_extractor_qualification.py
```

下面命令在final bundle存在时只做零模型只读复核；不得附加`--execute`：

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/run_event_extractor_qualification.py
```

历史live入口带有`--execute`参数，但四个attempt配额已经永久耗尽；本手册不再给出可复制的live命令。任何再次附加该参数的行为都违反route lock。

机械只读重算仍可执行：

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/verify_event_extractor_qualification.py
```

当前重算应复现`INCONCLUSIVE_PROTOCOL`。事后诊断bundle的唯一只读入口是：

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/seal_event_extractor_diagnostic_audit.py \
  --verify
```

预期`artifact_integrity=PASS`、`confirmation_eligible=false`、`component_qualification=NOT_QUALIFIED`。不得回写live/audit bundle，也不得让同一模型重试到符合acceptable set。用户级`~/.config/devin/AGENTS.md`属于真实可见控制面，其路径、大小和SHA已被历史freeze与每个attempt收据绑定。

---

## 7. tmux 交互调试档

### 7.1 它解决什么问题

`INTERACTIVE_TMUX_DEBUG` 用于 POC 和调试时实时观察 Devin 的 TUI、thinking spin、当前命令和输出文件是否出现。它不替代 `SEALED_NONINTERACTIVE`，也不允许进入确认性样本。

当前批准的live数据根是：

```text
/data/master-mind-solve-vein-data/
```

根目录README和`/data/README.md`必须先与实际挂载核对。repo内路径只保留代码、小型freeze与人读结论文档；不得再用作tmux模型workspace。

实现入口：

```text
system/solve_vein_analysis/tmux_runtime.py
system/tests/solve_vein_analysis/run_tmux_canary.py
```

下面是 POC-VMS-36 的**历史首次启动命令**。该ID已经消费，只用于审计重放，不得再次执行：

```bash
python3 system/tests/solve_vein_analysis/run_tmux_canary.py start \
  --poc-id POC-VMS-36 \
  --attempt-id poc-vms-36-extractor-tmux-a1 \
  --freeze system/tests/solve_vein_analysis/live_fixtures/poc_vms_36.freeze.json \
  --output system/tests/solve_vein_analysis/poc_results/poc-vms-36-tmux-canary-20260814
```

命令返回 JSON，其中 `live_bundle` 和 `attach_argv` 是后续唯一可信定位信息。把返回的 `live_bundle` 原样代入：

```bash
python3 system/tests/solve_vein_analysis/run_tmux_canary.py snapshot \
  --live-bundle '<live_bundle>'
```

若要亲眼观察，执行返回的 `attach_argv`。attach 只观察，不得直接输入；退出观察界面使用 tmux 自己的 detach 键，不终止 Devin。

当 snapshot 为 `DONE_WAITING_EXIT` 时，协议只允许一次：

```bash
python3 system/tests/solve_vein_analysis/run_tmux_canary.py exit \
  --live-bundle '<live_bundle>' \
  --actor 'master-agent' \
  --reason 'POC-VMS-36 preregistered graceful exit after DONE'
```

pane dead 后封存：

```bash
python3 system/tests/solve_vein_analysis/run_tmux_canary.py finalize \
  --live-bundle '<live_bundle>'
```

如果唯一退出动作后仍不退出，不能换另一种按键继续试；使用：

```bash
python3 system/tests/solve_vein_analysis/run_tmux_canary.py abort \
  --live-bundle '<live_bundle>' \
  --actor 'master-agent' \
  --reason 'POC-VMS-36 graceful-exit deadline exceeded'
```

核心 API：

```python
start_tmux_debug_role(spec)
snapshot_tmux_debug_role(handle)
send_tmux_debug_keys(handle, keys, actor=..., reason=...)
finalize_tmux_debug_role(handle)
abort_tmux_debug_role(handle, actor=..., reason=...)
```

`start` 返回的 launch receipt 包含可复制的 `attach_argv`：

```text
tmux -L <private-socket> attach-session -t <private-session>
```

不要自行猜 socket/session，也不要使用默认 tmux server。每次 snapshot 都会追加两份物证：

- `health-snapshots/NNNNNN.json`；
- `pane-captures/NNNNNN.txt`。

### 7.2 调试时的状态机

```text
STARTING → RUNNING → DONE_WAITING_EXIT → PROCESS_EXITED → FINALIZED
                      └──────────────→ ABORTED（显式、归因、保留物证）
```

看到 `DONE_WAITING_EXIT` 时不能 kill。先观察 pane；若协议预注册允许，可发送一次 `/exit` + `Enter`。这会写入 intervention record，并永久保持 `DEVELOPMENT_ONLY`。只有 pane 已 dead 才允许 `finalize`。

若 normal exit 失败，应执行显式 `abort`，把私有 tmux server kill、原因和最终 snapshot 一并封存；不得删除 live bundle 后伪装成“未运行”。

### 7.3 安全边界

- tmux 只负责可观测与进程承载，不提供 sandbox；
- 当前来源兼容档明确 `sandbox_requested=false`；
- `dangerous`/bypass用于取消每个动作的人工确认，不是隔离证明；
- 可读输入、可写输出和禁止动作由每个冻结workspace的`AGENTS.md`/`TASK.md`规定；
- 配置不得再禁止整个workspace所在卷；运行后必须用tool events审计模型是否越界；
- task/prompt 不进入 shell 字符串，tmux 使用多参数直接启动；
- 所有人工按键都必须走 allowlist API，禁止在未记账的 attach pane 中编辑任务或输出；
- live canary 必须另有预注册文档、唯一 run ID 和最多一次退出动作。

---

## 8. 输入制作规则

手工或未来 extractor 制作输入时：

1. occurrence 按发生先后使用连续 `sequence_index=0..n-1`；
2. 折返必须产生新 occurrence；
3. 旧/新 occurrence 可共享 `canonical_math_state_id`；
4. 所有非根 occurrence 必须有证据化入边；
5. `MERGE` 目标必须有至少两个不同语义父输入；
6. 属性必须使用 `namespace:value`；
7. 每个事件必须绑定 raw source span 与 SHA-256；
8. 不得看参考答案后再把缺失边补进 Solver 轨迹；
9. 不确定关系应保留为待审问题，不能静默猜成 `CONTINUE`；
10. JSON 不允许未知字段、NaN 或 Infinity。

---

## 9. 失败处理

| 现象 | 含义 | 处理 |
|---|---|---|
| 退出码 2，`OBJECT_KEY_*` | 输入合同破坏 | 修输入生成器，不放宽 parser |
| `NON_FORWARD_EDGE` | occurrence 顺序或边方向错误 | 新建折返 occurrence，禁止成环 |
| `MERGE_PARENT_INSUFFICIENT` | 把单父推进误标成合流 | 补真实第二证据父边或改正确 relation |
| `FCA_*_MISMATCH` | Next Closure 与 oracle 不一致 | 隔离该运行并修算法，禁止产出 PASS |
| `fixed_point_reached=false` | 最大关系尺度轮数内未稳定 | 结果只能 PARTIAL，检查尺度设计 |
| asset hash mismatch | 运行资产漂移 | 审查变更并发布新 manifest，禁止改 hash 糊过去 |
| output already exists | append-once 保护 | 使用新 run ID，不覆盖旧结果 |
| batch/incremental mismatch | 流式语义与批语义不同 | 隔离结果，定位第一个分叉前缀 |
| tmux `DONE_WAITING_EXIT` | 候选文件已出现但 Devin 尚未退出 | 继续观察；只按预注册动作正常退出，禁止立即 kill |
| tmux session/pane missing | 交互载体状态不可确认 | snapshot 后显式 abort 并保留物证 |
| tmux model mismatch/export missing | 运行事实不可确认 | 不得 finalize 成 PASS；封存为失败/abort |
| tmux读取自身workspace被deny | 配置与物理落点自相矛盾 | 封存当前POC；发布新资产/新POC，禁止原ID重试 |
| attempt ID与poc ID不一致 | 身份链污染 | 启动前fail-closed，不允许默认历史ID |

历史VMS-31离线CLI的局部失败处理与live角色运行不可混为一谈。VMS-41等live角色一旦进入`REQUEST_ACCEPTED`、`GENERATION_STARTED`或启动状态不可知，partial必须保留并进入reattach/reconcile/quarantine；不得删除后盲重试。只有具备正证据表明provider未接受请求、且协议明确允许的纯基础设施故障，才可使用新attempt lineage执行预注册重试；VMS-41当前重试数冻结为0。

---

## 10. 当前禁止事项

本版本不得：

- 修改或复制覆盖 `system/assets/vein_analysis/`；
- 调用 `system.vein_analysis`、`process_absorb` 或 `enter.py`；
- 把 fixture 成功说成 live extraction 成功；
- 连接数据库或把结果写进现有集合；
- 在未预注册的情况下启动 Devin/Codex/Solver；
- 把 tmux pane 观察、人工 `/exit` 或一次写文件成功计为确认性科学证据；
- 看到 DONE 就 kill session，导致 export 丢失；
- 为得到 PASS 反复改同一个 expected fixture；
- 覆盖既有 POC 结果；
- 把 RCA-style 存在量词尺度称为完整 RCA/Multi-FCA。

---

## 11. 下一阶段的正确顺序

1. VMS-38 tmux debug Canary、VMS-39控制面边界和VMS-40多视图/AcceptableSet合同都已封存；VMS-40只读复核使用：

   ```bash
   .venv/bin/python system/tests/solve_vein_analysis/verify_multiview_poc.py
   ```

2. VMS-41已经封存为`NOT_QUALIFIED`；旧case只进入development/regression，旧attempt不得重跑；
3. VMS-41R1的occurrence/projection、typed path、发生时status、MERGE贡献、结构化file-effect修订合同、全新未见qualification pack、0.4.1角色资产、零模型preexecution freeze、live runner shell、不可消费LiveRunPermit/盲审包计划、sealed manual judgment合同、hidden join simulator、fake materializer、final qualification join receipt和fake bundle append-only dry-run已经冻结；VMS-42 State Normalizer离线核心、零模型资格包、hidden join、reviewer judgment合同、final receipt、unseen qualification extension和DAG writeback sidecar已经实现；VMS-43 Trace Auditor结构审计已经实现；下一步只能等待显式人签LiveRunPermit，或继续Trace Auditor qualification pack，或做VMS-42/43角色资产preexecution freeze；
4. 只有获得新授权并且修订后的 extraction gate 通过，才接 streaming partial；
5. 只有恢复/隔离通过，才接真实 Solver；
6. 只有真实轨迹结构质量通过，才把 trace 接入 Tell/Hint 选择实验。

每一步都必须保留上一层的 NOT_TESTED 边界，不能用下游成功倒推上游正确。
