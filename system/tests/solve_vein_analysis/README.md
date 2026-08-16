# 解题侧脉络分析测试与POC证据总索引

**作用**：这是`system/solve_vein_analysis/`全部自动测试和POC的唯一证据索引。  
**任务追踪真值源**：`第六代系统研发过程文档/363-v0-2026-08-14-解题侧非线性脉络分析后续路线图-阶段门与任务追踪.md`  
**保护基线**：`protected_absorb_baseline.sha256`，当前digest为`9bb4fd2551d13f196610ddf8e203ad96b0855f3337f6c4e6502f6c764eafd6b3`。

本README只索引证据，不替代预注册协议、结果文档、raw artifact或final receipt。没有在这里登记的测试/POC，不得被阶段门用作晋级证据。

---

## 1. 自动测试

当前基线：

```text
2026-08-14
293 tests
PASS
```

标准命令：

```bash
.venv/bin/python -m unittest discover \
  -s system/tests/solve_vein_analysis \
  -p 'test_*.py' \
  -v
```

| 文件 | 范围 | 当前证据 |
|---|---|---|
| `test_pipeline.py` | 严格trajectory合同、typed DAG、FCA/关系尺度、Next Closure oracle、批增量等价、CLI封存、入题侧隔离 | 31 tests中的确定性核心部分；VMS-31 |
| `test_live_poc.py` | 冻结live fixture、三个角色evaluator、role runtime、asset/config/model/export/ATIF合同 | VMS-32—38；含ATIF-v1.7 13/7计数缺陷回归 |
| `test_tmux_runtime.py` | private tmux、attempt identity、观察/intervention/abort/finalize、no-sandbox合同 | VMS-36—38 |
| `test_agents_limit.py` | VMS-39确定性精确尺寸fixture、16 KiB前后sentinel、single/multi-message与prefix/suffix ATIF grader、cell attempt身份和fake-tmux封存 | 13 tests；只证明fixture/grader/runner合同，尚无live Devin结论 |
| `test_agents_limit_static.py` | VMS-39零模型静态loader、隔离HOME/XDG、完整fixture显示、收据/全树审计、篡改与旧辅助文件反例 | 7 tests；只支持静态Stage A与审计合同 |
| `test_agents_limit_aggregate.py` | VMS-39四cell跨bundle身份、停止集、全树hash、symlink拒绝与16,384-byte边界派生 | 6 tests；证明聚合器合同，live结论仍来自封存ATIF物证 |
| `test_semantic_truth.py` | VMS-40五层真值、多视图关系、多轴State、完整alternative、真合流、canonicalization与fail-closed反例 | 16 tests；6 case/26 candidate全部与预注册Verdict一致 |
| `test_event_extraction_qualification.py` | VMS-41隐藏acceptable set、UTF-8 witness/span、occurrence一一映射、required/optional/forbidden relation与真/假MERGE | 15 tests；只证明资格包与机械grader |
| `test_event_extraction_qualification_runtime.py` | VMS-41 task渲染、tool边界、四case fake-Devin one-shot→延迟gold→append-only seal及只读重算/篡改拒绝 | 5 tests；全离线，机械PASS最高仍为`PENDING_MANUAL_AUDIT` |
| `test_event_extractor_diagnostic_audit.py` | VMS-41事后非盲诊断的严格输入、历史freeze成员重放、append-only seal、source binding、篡改/symlink/partial拒绝 | 9 tests；只支持failure localization；机械强制`confirmation_eligible=false`与`NOT_QUALIFIED` |
| `test_event_extraction_projection.py` | VMS-41R1 occurrence history/coarse projection分层、typed path、双时间状态、MERGE贡献/injective frontier、资源上限与fail-closed反例 | 26 tests；只证明V2离线parser/evaluator合同，不资格化模型角色 |
| `test_file_effect_audit.py` | VMS-41R1 pre/post inventory与结构化provider file-event联合审计、瞬态create-delete、越界、symlink和可观测性分级 | 15 tests；只证明离线审计合同；真实CLI事件完备性尚未资格化 |
| `test_event_extractor_calibration.py` | VMS-41R1不可变calibration pack、受限mutation DSL、19场景逐轴重放、tamper/额外文件/symlink/expected漂移拒绝 | 12 tests；calibration永久`DEVELOPMENT_ONLY`，不进入qualification |
| `test_event_extractor_qualification_v2.py` | VMS-41R1全新未见qualification pack、hidden/public分离、真实source谱系、reference self-check与负向mutation、manifest篡改/symlink拒绝 | 9 tests；只证明qualification pack freeze/preflight合同，live仍未授权 |
| `test_event_extractor_vms41r1_prefreeze.py` | VMS-41R1零模型preexecution freeze、0.4.1角色资产绑定、append-once复验、外部输出与漂移拒绝、零副作用授权 | 5 tests；只证明prefreeze清单合同，仍不启动Devin、不资格化模型 |
| `test_event_extractor_vms41r1_runner.py` | VMS-41R1 live runner shell的零模型preflight、workspace计划、public/hidden分离、`--execute` fail-closed与零副作用收据 | 6 tests；只证明runner外壳已可审计并停在`READY_FOR_AUTHORIZATION`，不授权live |
| `test_event_extractor_vms41r1_permit_plan.py` | VMS-41R1 LiveRunPermit与blind-review plan的不可消费permit、hidden文件隔离、canonical输出和fail-closed反例 | 6 tests；只证明permit/review计划形状，`authorized_live_attempts=0`，不授权live |
| `test_event_extractor_vms41r1_manual_judgment_contract.py` | VMS-41R1 sealed manual judgment合同、case/attempt绑定、盲审attestation、六轴Verdict和CLI验证反例 | 7 tests；只证明人工判断对象Schema/语义，不导入真实review、不运行hidden grader |
| `test_event_extractor_vms41r1_hidden_join_simulator.py` | VMS-41R1 fake manual judgment + fake/reference candidate hidden join simulator、join顺序、负向mutation和零副作用CLI | 5 tests；只证明development-only join语义，不使用真实live输出 |
| `test_event_extractor_vms41r1_fake_materializer.py` | VMS-41R1 fake live bundle与blind-review package materializer、Reviewer可见文件精确集合、hidden隔离与hash局部性 | 4 tests；只证明计划manifest，不写真实bundle |
| `test_event_extractor_vms41r1_final_join_receipt.py` | VMS-41R1 final qualification join receipt、materializer/hidden-join按case/attempt/candidate hash合并、side-effect fail-closed和profile非资格化边界 | 5 tests；只证明development-only final receipt，不授权live |
| `test_event_extractor_vms41r1_fake_bundle_dry_run.py` | VMS-41R1 fake blind-review bundle append-only dry-run、临时输出根、重复写/repo根/symlink拒绝和hidden文件缺席 | 5 tests；只证明临时目录写包边界，不授权live |
| `test_state_normalizer_vms42.py` | VMS-42 State Normalizer多轴绑定、dictionary alias归一化、legacy projection、must/cannot/exact约束和fail-closed反例 | 8 tests；只证明离线机械合同，不资格化模型角色 |
| `test_state_normalizer_vms42_pack.py` | VMS-42 State Normalizer资格包public/hidden分离、reference/negative重放、expected/hash篡改拒绝和零副作用CLI | 7 tests；只证明零模型资格包形状，不资格化模型角色 |
| `test_state_normalizer_vms42_hidden_join.py` | VMS-42 State Normalizer candidate bundle hidden join、public hash/candidate hash/hidden key拒绝、negative保留和零副作用CLI | 8 tests；只证明hidden join形状，不资格化模型角色 |
| `test_state_normalizer_vms42_manual_judgment_contract.py` | VMS-42 State Normalizer sealed reviewer judgment合同、candidate bundle绑定、blinding attestation、六轴Verdict和CLI验证反例 | 10 tests；只证明reviewer judgment对象形状，不执行人工审查、不资格化模型角色 |
| `test_state_normalizer_vms42_final_join_receipt.py` | VMS-42 State Normalizer final reviewer+hidden-join receipt、manual/hidden FAIL保留、hash错配拒绝和非资格化边界 | 8 tests；只证明最终合并receipt形状，不资格化模型角色 |
| `test_state_normalizer_vms42_unseen_pack.py` | VMS-42 State Normalizer unseen qualification extension、新旧case/candidate ID不重叠、expected drift拒绝、public/hidden隔离和非资格化边界 | 8 tests；只证明未见fixture扩展包形状，不资格化模型角色 |
| `test_state_normalized_dag.py` | VMS-42 State Normalizer DAG writeback sidecar、DAG不变性、occurrence存在性、PASS evaluation/hash绑定和重复binding拒绝 | 8 tests；只证明零模型sidecar回写合同，不资格化模型角色 |
| `test_trace_auditor.py` | VMS-43 Trace Auditor结构审计、必需family缺失FAIL、sidecar hash/order绑定、未知edge端点和重复edge拒绝 | 10 tests；只证明结构审计合同，不抽取自然语言、不资格化模型角色 |

夹具：

- `fixtures/c1_linear.*`：线性；
- `fixtures/c2_branch.*`：分叉；
- `fixtures/c3_revisit.*`：折返；
- `fixtures/c4_merge.*`：多父合流；
- `fixtures/c5_composite.*`：复合；
- `multiview_fixtures/vms40_cases.json`：VMS-40的MV1—MV6、26个正/负/边界candidate；
- `live_fixtures/poc_vms_32/`：认知角色冻结素材；
- `live_fixtures/poc_vms_35.freeze.json`—`poc_vms_38.freeze.json`：历史一次性运行冻结清单。
- `qualification_fixtures/vms41/`：VMS-41两个人工反例、两个只读真实reasoning摘录、source receipts与候选不可见acceptable-set pack。
- `qualification_fixtures/vms41r1_calibration/`：VMS-41R1不可变开发校准包；6个内容文件由`pack-manifest.json`绑定，13个candidate+6个file-effect场景由`scenario-matrix.json`冻结。
- `qualification_fixtures/vms41r1/`：VMS-41R1全新未见qualification pack；6个case、hidden acceptable set、hidden reference candidates、盲审rubric、thresholds与manifest冻结，manifest SHA=`ac270b0a6aadceae18c141200a8fd7abbbbfb4c2272b4b6e92c43350ffee020b`。
- `live_fixtures/poc_vms_41r1.freeze.json`：VMS-41R1零模型preexecution freeze；绑定0.4.1角色资产、6个attempt IDs、hidden grader物证和盲审rubric，freeze SHA=`37a9fa407be5341305fe61fe63e5a26894d98271c7d7bd3480e6413d0d7295ad`，外部副作用授权全为0。
- `run_vms41r1_event_extractor_qualification.py`：VMS-41R1 live runner shell；默认只生成零模型preflight receipt，状态为`READY_FOR_AUTHORIZATION / NOT_AUTHORIZED`，`--execute`必须fail-closed。
- `build_vms41r1_live_permit_review_plan.py`：VMS-41R1 LiveRunPermit与盲审包零模型计划；默认只输出不可消费plan，`permit_consumable=false`、`authorized_live_attempts=0`。
- `vms41r1_manual_judgment_contract.py`：VMS-41R1 sealed manual judgment合同；验证未来人工盲审结果必须绑定case/attempt、保持hidden未见证明，并按六个轴给出Verdict。
- `vms41r1_hidden_join_simulator.py`：VMS-41R1 hidden join零模型模拟器；用synthetic manual judgment与hidden reference candidate证明join顺序和final development-only verdict。
- `vms41r1_fake_live_bundle_materializer.py`：VMS-41R1 fake live bundle / blind-review package materializer；只输出计划manifest，不写文件，Reviewer可见集合不含hidden项。
- `vms41r1_final_qualification_join_receipt.py`：VMS-41R1 final qualification join receipt；把fake materializer与hidden join simulator按case/attempt/candidate hash合并，输出development-only final receipt，profile仍为`NOT_QUALIFIED_LIVE_NOT_AUTHORIZED`。
- `vms41r1_fake_bundle_append_only_dry_run.py`：VMS-41R1 fake bundle append-only dry-run；在显式临时输出根写出Reviewer可见文件和bundle manifest，拒绝覆盖、repo根和symlink根。
- `state_normalizer_fixtures/vms42_cases.json`：VMS-42 State Normalizer离线预注册包；2个case、4个candidate，覆盖多轴revisit和branch lifecycle。
- `build_vms42_state_normalizer_pack.py`：VMS-42 State Normalizer零模型资格包构建器；从冻结fixture派生public manifest、hidden manifest、reference/negative check rows和零副作用receipt，不写文件、不调用模型。
- `vms42_state_normalizer_hidden_join.py`：VMS-42 State Normalizer hidden join零模型模拟器；只接收candidate bundle，用hidden dictionary/acceptable set评分，保留negative结果且不资格化live profile。
- `vms42_state_normalizer_manual_judgment_contract.py`：VMS-42 State Normalizer sealed reviewer judgment合同；绑定public manifest、candidate bundle和reviewed candidates，强制hidden未见attestation和六轴Verdict一致性。
- `vms42_state_normalizer_final_join_receipt.py`：VMS-42 State Normalizer final reviewer+hidden-join receipt；合并reviewer judgment与hidden join receipt，任一侧FAIL即final FAIL，双PASS仍development-only不资格化。
- `state_normalizer_fixtures/vms42_unseen_cases.json` + `build_vms42_state_normalizer_unseen_pack.py`：VMS-42 unseen qualification extension；新增2个case/4个candidate，强制与原fixture的case/candidate ID不重叠，public/hidden分离，输出development-only非资格化extension receipt。
- `state_normalized_dag.py`：VMS-42 state-normalized DAG writeback sidecar；把PASS normalized bundle按DAG event_id/topological order生成不可变annotation bundle，不改写DAG本体。
- `trace_auditor.py`：VMS-43 Trace Auditor结构审计器；在已结构化ReasoningDag上观察branch/failure/revisit/reuse/merge/recovery family，并验证可选state sidecar与DAG hash/order兼容。

自动测试PASS只证明代码合同和冻结fixture成立，不证明远程模型能力、真实streaming、Tell效果、两棵树闭环或Seven接入。

---

## 2. 已完成/封存POC

| POC | 协议 | 结果 | 物证 | Verdict | 是否可重跑 | 证据边界 |
|---|---|---|---|---|---|---|
| VMS-31 | 346号 | 347号 | `poc_results/poc-vms-31-20260814/` | `PASS_WITHIN_FROZEN_STRUCTURED_CASES` | 确定性代码可用新ID重放；历史目录不可覆盖 | 支持DAG/FCA/RCA-style结构；不支持raw抽取/live/规模 |
| VMS-32 | 348号 | 349号 | `poc_results/poc-vms-32-20260814/`及`-infra-r1/` | `INCONCLUSIVE_PROTOCOL` | 原ID不可重跑 | 暴露sandbox/权限/载体限流；不证明角色无效 |
| VMS-33 | 350号 | 351号 | `poc_results/poc-vms-33-20260814/` | `INCONCLUSIVE_PROTOCOL` | 原ID不可重跑 | 独立启动器仍未恢复写入；不证明sandbox为唯一原因 |
| VMS-34 | 352号 | 同文暂停记录 | 无live物证 | `PAUSED_BEFORE_LIVE_CALLS` | 未消费live，但不得冒充已测 | 只形成response-only候选协议 |
| VMS-35 | 354号 | 356号 | `poc_results/poc-vms-35-20260814/` | 文件写入合同SUPPORTED；总体`INCONCLUSIVE_PROTOCOL` | 原ID不可重跑 | 三角色写出JSON/export；不资格化角色，形成gold语义反例 |
| VMS-36 | 357号 | 358号 | `poc_results/poc-vms-36-tmux-canary-20260814/` | `INCONCLUSIVE_PROTOCOL / ABORTED` | 原ID不可重跑 | tmux/Thinking/exact model/export可见；repo workspace自拒绝 |
| VMS-37 | 359号 | 360号 | `/data/master-mind-solve-vein-data/poc-results/poc-vms-37-d-volume-tmux-20260814/` | `INCONCLUSIVE_PROTOCOL / ABORTED` | 原ID不可重跑 | D盘workspace/tmux/dangerous可用；配置拒绝自身读取，旧attempt ID漂移 |
| VMS-38 | 361号 | 362号 | `/data/master-mind-solve-vein-data/poc-results/poc-vms-38-dangerous-agents-tmux-20260814/` | `SUPPORTED_WITHIN_DEBUG_CANARY / DEVELOPMENT_ONLY`；科学投影`PARTIAL` | 原ID已消费，绝对不可重跑 | 严格输出/DONE/exact model/tool boundary/唯一退出/exit 0；不资格化角色 |
| VMS-39 | 364号 | 365号 | D盘四个live cell bundle + `poc-vms-39-live-aggregate-20260814/` | `SUPPORTS_EXACT_16384_BYTE_EFFECTIVE_RULE_LIMIT_WITHIN_FROZEN_PROFILE / DEVELOPMENT_ONLY` | 四个原ID已消费，绝对不可重跑；A64/A128/A256按停止规则不运行 | 静态show至256 KiB；live 16,384 full、16,385 truncated；只支持冻结CLI/profile，不支持用AGENTS作知识库 |
| VMS-40 | 366号 | 367号 | `/data/master-mind-solve-vein-data/poc-results/poc-vms-40-20260814/` | `PASS_WITHIN_DETERMINISTIC_OFFLINE_SCOPE / DEVELOPMENT_ONLY` | 原目录已消费且append-only；相同ID重启被exit 2拒绝 | 6 case/26 candidate全匹配；支持多视图/多轴/acceptable-set机械合同，不资格化任何模型角色 |
| VMS-41 | 368号 | 369号 | `/data/master-mind-solve-vein-data/poc-results/poc-vms-41-event-extractor-qualification-20260814/` + `poc-vms-41-event-extractor-diagnostic-audit-20260814/` | artifact/replay `PASS`；frozen case 0/4；`INCONCLUSIVE_PROTOCOL / NOT_QUALIFIED`；事后审计`FAILURE_LOCALIZATION_ONLY` | 四个原attempt已消费，绝对不可重跑 | 27/27 coarse anchors有映射，但粒度/typed path/status/MERGE与tool合同需修订；人工盲性已破坏，不能作确认性PASS |

“346号”等均位于`第六代系统研发过程文档/`。D盘目录中的`preexecution-freeze-manifest.json`、control、launch/final/abort receipt、health snapshot、pane capture、workspace输入、output和Devin export共同构成证据，不能只引用最终Markdown。

### VMS-38不可变性特别说明

历史`tmux-debug-final-receipt.json`中的`step_count=0/tool_event_count=15`来自旧解析器缺陷；raw ATIF实际为13 step/7 call。历史receipt不得修改，现行代码与测试只保证未来解析正确。

---

## 3. 当前规划POC

以下状态与363号同步。“预留”不等于预注册，“协议准备中”也不等于可发起live调用。

| POC | 目标 | 追踪阶段 | 当前状态 | 计划证据根 |
|---|---|---|---|---|
| VMS-41R1 | Event Extractor修订合同后的全新未见资格化 | SV-S2 | `FAKE_BUNDLE_APPEND_ONLY_DRY_RUN_PASS / LIVE_NOT_AUTHORIZED`；371/372/373/374/375/376/377/378/379号；6个未见case、6个hidden reference candidates、4个负向mutation自检PASS；0.4.1角色资产、`poc_vms_41r1.freeze.json`、live runner shell、不可消费LiveRunPermit/盲审包计划、sealed manual judgment合同、hidden join simulator、fake materializer、final qualification join receipt和临时append-only写包dry-run均已冻结；105项V2专项、226项全量回归PASS；旧四case与calibration均不得进入qualification | 下一步只允许显式人签LiveRunPermit后的真实资格实验，或转入VMS-42预注册；不得复用VMS-41 ID或数据，不得启动模型 |
| VMS-42 | State Normalizer资格化 | SV-S3 | `DAG_WRITEBACK_SIDECAR_ZERO_MODEL_PASS / LIVE_NOT_AUTHORIZED`；380/381/382/383/384/385/386号；State Normalizer离线核心8项、资格包7项、hidden join 8项、reviewer judgment合同10项、final join 8项、unseen extension 8项、DAG sidecar 8项PASS；尚不执行真实review、不资格化模型角色 | 下一步是角色资产/preexecution freeze或SV-S4 Trace Auditor设计；不得启动模型 |
| VMS-43 | Trace Auditor资格化 | SV-S4 | `TRACE_AUDITOR_STRUCTURAL_ZERO_MODEL_PASS / LIVE_NOT_AUTHORIZED`；387号；synthetic complex DAG覆盖branch/failure/revisit/merge/recovery，10项结构审计测试PASS；不抽取自然语言、不资格化模型角色 | 下一步是qualification pack或角色资产/preexecution freeze；不得启动模型 |
| VMS-44 | 三角色batch端到端 | SV-S5 | `RESERVED_NOT_PREREGISTERED` | E2E manifest/failure matrix |
| VMS-45 | stream可见性、batch等价与恢复 | SV-S6 | `RESERVED_NOT_PREREGISTERED` | event journal/reconcile receipts |
| VMS-46 | 动态FCA/RCA遍历与性能 | SV-S7 | `RESERVED_NOT_PREREGISTERED` | scale registry/oracle/performance report |
| VMS-47 | Trace/Tell/Hint registry、内容寻址文件分片、逐项遍历、cursor恢复与coverage remainder=0 | SV-K1/K2 | `RESERVED_NOT_PREREGISTERED`；363号追踪、370号技术方案；尚无执行授权 | registry snapshot/shard manifest/per-item records/coverage+completion receipts |
| VMS-48 | 推理树增量、折返、合流与重放 | SV-T1 | `RESERVED_NOT_PREREGISTERED` | tree bundle/replay verdict |
| VMS-49 | 引导树与Grove三推动闭环 | SV-T2/T3 | `RESERVED_NOT_PREREGISTERED` | guided/reasoning trees + launch simulator ledger |
| VMS-50 | Seven冻结接口模拟/故障矩阵 | SV-X1 | `RESERVED_NOT_PREREGISTERED` | interface fixtures/import-export receipts |
| VMS-51 | DB Schema/adapter dry-run/回放 | SV-X2 | `RESERVED_NOT_PREREGISTERED` | schema plan/catalog fake/rollback report |
| VMS-52 | Seven前全链路golden slice | SV-G1 | `RESERVED_NOT_PREREGISTERED` | end-to-end final bundle + dual verdict |

---

## 4. 新测试或POC的登记规则

在任何执行前，先向本README添加计划行，并满足：

1. POC ID唯一；
2. 预注册文档路径存在；
3. attempt数、模型/profile、资源、重试、停止、工作目录和证据根冻结；
4. 科学失败、协议失败和基础设施失败分轴；
5. raw与final目录append-only，禁止覆盖；
6. 结果文档落盘后把状态、Verdict、支持/不支持主张写回本README；
7. 新自动测试在本节或第1节登记文件和覆盖主张；
8. 更新363 checkpoint、稳定模块文档、runbook（若有命令）和`ChangeLog.md`；
9. 复跑全量测试和入题侧保护基线；
10. 未登记、缺manifest或缺raw evidence的结果不得用于PASS。

## 5. 审计入口

复核任一结论时按顺序读取：

1. 本README；
2. 对应预注册协议；
3. frozen manifest；
4. raw evidence/export/tool events；
5. final receipt；
6. 结果文档；
7. 363号阶段门与checkpoint；
8. 当前代码和回归测试。
