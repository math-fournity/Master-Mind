# 实现状态

## 一句话结论

Seven System v0.1.0 是一个可运行、可测试的 P0 + P1 scaffold 控制面，不是387号完整P1，更不是已完成的非特化实验平台。WP-1 是新增的工程前置工作包名称，也不是 canonical P1 的别名。

## 已实现

| 能力 | 入口 | 结果 |
|---|---|---|
| 配置读取 | `preflight` | 先执行`runtime-config.schema.json`并拒绝未知字段，再进行语义校验；不读取密钥 |
| fail-closed preflight | `preflight` | 检查 D 盘、README、数据根、DB 名、Harness、目录隔离、工具策略与能力报告 |
| RuntimeManifest | `init-epoch` | 冻结 Epoch、真实源码树哈希、卷/README指纹、路径、输入空位和实现边界；返回成功前完成双轴自验 |
| 编排文件集 | `init-epoch` | 生成 phase plan、runbook、logging contract、scenario matrix、checkpoint、evidence index、verdict、summary |
| 幂等提交 | `dry-run` | 相同内容只提交一次；重复投递返回已有提交 |
| 冲突拒绝 | `dry-run` | 相同路径出现不同内容时拒绝覆盖 |
| P1 scaffold Gate | `dry-run` | 追加GateDecision、后续checkpoint、P1 scaffold verdict；一致的PASS或FAIL都是可重放终态 |
| 完整性验证 | `validate-epoch` / `status` | 执行本版Schema子集、两级逐文件索引、交叉hash与Epoch外local receipt；完整性和当前resume兼容性分轴 |
| Strict DB 离线契约 | `wp1-db-contract-report` | 清除Arango凭据后运行固定测试，执行Schema+跨字段语义验证，将绑定当前实现/spec的报告append-once提交到批准的D盘根 |

## WP-1 站点存储与 Strict DB 状态

2026-08-14已完成D卷、OrbStack宿主数据镜像与Arango容器路径的分层只读核对，但尚未连接或核验真实逻辑数据库，也没有对共享生产数据库做任何变更：

| Gate / Advisory | 当前判定 | 含义 |
|---|---|---|
| `G-WP1-S` | `PASS` | D 卷 README 和 `/data/seven-system-data/` 已准备，真实 dry-run preflight PASS |
| `G-WP1-C` | `PASS` | Strict DB port、离线planner、7集合/13唯一索引spec、受控测试、报告CLI和semantic verifier均已落盘并由实际报告验证 |
| `G-WP1-L` | `NOT_IMPLEMENTED` | 目标是复用`xishujuzhen_math_glm52`；尚无真实站点身份/catalog报告生成器、semantic verifier或operator CLI |
| `G-WP1-I` | `NOT_IMPLEMENTED` | 尚无Seven Schema初始化的受控DDL、人工授权收据、durable ledger、fence或resume |
| `A-WP1-D` | `PASS` | OrbStack group-container data symlink指向`/data/OrbStack/data`，实时OrbStack进程打开其中的`data.img.raw`；Docker containers由该D盘镜像承载 |
| `A-WP1-BIND` | `WARNING_NOT_DEDICATED` | engine在容器`/var/lib/arangodb3`的writable overlay中，未使用已配置但为空的`/data/arangodb/data:/data`专用bind；这是生命周期/可搬运性告警 |

当前 WP-1 总状态是 `PARTIAL/READY_FOR_LOGICAL_SITE_INTEGRATION`。`A-WP1-D=PASS`只回答“宿主物理字节是否在D盘”；`A-WP1-BIND=WARNING_NOT_DEDICATED`回答“是否使用Arango专用bind”。两者都不表示真实site capability或写能力已经PASS。离线报告事实如下：

- 路径：`/data/seven-system-data/capabilities/strict-db-contract/wp1-contract-20260814-002.json`；
- `verdict=PASS`，11项canonical check全部PASS，9项required claim全部为true，blockers为空；
- subject hash：`77c6e348b4124a53080322d5cbe478b5ded3c8bea31dfc4555ac320aaa97799b`；
- implementation tree hash：`656d6e807ad2e5f1e0b237145cfef94640b5eddd6054fc47d3c51111a1cc609e`；
- 报告文件 SHA-256：`68c96aa4eec1fa8f7fc0e55222f6395c7b9096c683cae85f15888bc323c64b71`；
- 隔离runner 20项、全量测试58项，全部PASS。

`wp1-strict-db-contract-report.schema.json` 已由报告生成器和验证器实际执行。`wp1-database-site-capability-report.schema.json` v1仍只是未执行的旧前向shape；它把唯一可接受的D-backing写死为`/data/arangodb/data`专用bind，并把这个物理条件错误编码成site PASS必需条件，现已标记`SUPERSEDED_NOT_EXECUTED`，不得生成、接受或实现本站PASS。后续必须新增逻辑站点v2合同，把`G-WP1-L/I`、宿主D-backing观测与专用bind告警分开。

离线报告明确不主张：真实DB site capability、物理DB存储、Arango连接或migration已经发生、durable migration ledger/fence/resume、runtime append-only/CAS/outbox delivery语义或可信wall-clock/文件不可变性已经实现。9项true claim中的ledger/outbox项只冻结对应unique-index spec，不是runtime语义证明。它不能替未来`DatabaseLogicalSiteCapabilityReport v2`解锁live。

## 明确未实现

以下能力不存在，也没有隐藏入口：

- 逻辑站点v2 capability report CLI、真实站点Schema plan/verify CLI、Schema apply、事务、CAS、durable outbox、lease/fencing；
- Redis 队列或分布式 worker；
- 387号完整P1的lease/fencing/outbox、崩溃恢复、重复投递和Redis重建矩阵；
- 真实 Devin Solver dispatch；
- `TargetSolverPort/DevinSolverAdapter`及其LaunchReceipt；
- provider-neutral `ModelRolePort`（Cognitive Worker子系统）、`HumanTaskPort/HumanGateService`、`DevinCliModelRoleAdapter`、Codex或其他模型adapter；
- WP-GV0 `SecurityContractVerifier/CompletionContractVerifier`公共核心及其DB/bootstrap reservation backends；
- `RoleExecutionContract`、`CognitiveWorkerCapabilityReport`、`AIInvocationReceipt`和`ReviewIndependenceRecord`；
- provider/工具表面层面的无工具强制；
- 对现有 `trajectory.jsonl` 的 fail-closed 工具审计；
- CandidateManifest/BareBaseline/CasePack/ExperimentPlan、QuestionDraftVersion/QuestionRelease 导入；
- D 盘 CAS 的 live→partial→seal；
- 答案/holdout Vault；
- Process/Proof/Leakage 三种盲化视图和 Judge；
- RunAudit、contrast、EvidenceRecord；
- RevisionProposal、prospective holdout、Promotion；
- 自动出题、Selector、分类学迁移、Active Learning；
- AuthoringBakeoff、WP-QA0 Controlled Authoring Lab与WP-QA1 Question Admission；
- 多 Tell 组合和跨 Epoch 持续学习；
- Artifact GC、删除、清空队列或生产 pipe 回写。
- 签名、WORM或外部DB anchoring；当前local receipt只保证Seven API下append-once。

当前preflight只保留历史四类live capability槽位（DB、Safe Launch、No Tool、Answer Isolation），且live仍无条件BLOCK。387号完整P0另要求独立`HarnessCapabilityReport`（资源强制）与`CognitiveWorkerCapabilityReport`，合计至少六类；后两类当前均无完整Schema、生成器、semantic verifier或consumer。不能把Safe Launch当作Harness资源能力，也不能因旧四类报告存在就声称P3/P6可运行。

凡经过人工Gate的lane还必须冻结HumanGate policy、授权actor roster、职责分离与签名验签readiness；这是六类机器/基础设施报告之外的人类治理前置，当前同样`NOT_IMPLEMENTED`。

当前`seven.py capabilities`仍是v0.1 legacy枚举，尚未逐项列出TargetSolverPort、ModelRolePort、Devin/Codex认知adapter、Human Gate、QuestionRelease、WP-QA0/QA1和Bakeoff；**机器列表中的沉默一律解释为NOT_IMPLEMENTED，绝不能解释为可用**。未来同步该代码会改变WP-1 Strict Contract绑定的实现树hash，必须在独立代码工作包中补测试并重发新报告，不能在本轮文档修订中偷改002物证。

## 为什么 live 模式必然 BLOCKED

现有高并发系统的无工具规则主要靠 Prompt 和事后检查，但当前检查链存在 fail-open 风险：Harness 产出的是 `trajectory.jsonl`，历史 Collector 却查找不存在时会被当成“没有工具”的 `*.db`。此外，Harness 会二次包装 AGENTS，且 CLI 仍运行在 dangerous permission 模式。

Arango engine data directory没有使用专用D盘bind，但承载OrbStack overlay的宿主数据镜像确实位于D盘；因此前者是`A-WP1-BIND=WARNING_NOT_DEDICATED`，后者是`A-WP1-D=PASS`。本版 live preflight仍无条件增加`live_execution_implementation=BLOCK`，原因是NoTool能力、逻辑site verifier、Schema初始化、Vault和P2-P9均未完成。这不是否定现有题海数据价值，而是拒绝把“没有观测到工具”误写成“工具能力已被物理关闭”，也拒绝用存储位置或离线DB contract PASS冒充本站DB可运行。

## 下一批工作包

1. ~~DOC0完成bootstrap record后先实现`WP-GV0`~~ → **WP-GV0 代码+测试完成，状态 `IMPLEMENTED_PENDING_EVIDENCE`**（两个硬阻塞阻止升至 READY_FOR_AUDIT，见下节"WP-GV0 实现状态"）。GV0用该store自托管自己的ImplementationCompletionBundle，在GV0前不接受任何普通工作包完成对象。
2. 版本化定义逻辑站点v2 report与semantic verifier，再对原逻辑数据库执行只读identity/current DB/catalog核验；catalog冲突检查覆盖全部隔离的`seven_*_vN`，不得复用题海/`system/`或无版本集合。
3. 只读生成`seven_*_v1` scaffold及`seven_*_v2+`原子结构的版本化Schema初始化计划，检查与现有catalog的冲突；不创建集合。
4. 在单独授权的未来写工作包中设计真实DDL入口、人工收据、durable ledger、fence、resume/reconcile和故障注入；当前生产包只有只读planner。DB1I只交付SchemaState/bootstrap三对象，RT1才交付Runtime/Reconcile两份能力报告。
5. 若要把Arango从容器writable overlay改成专用bind/volume，另列独立运维硬化事项，按容器生命周期、备份、停机和回滚需要决定；这不是“迁到D盘”，也不阻塞前述只读核验。
6. Harness adapter：单次 canonical prompt、结构化 argv、`trajectory.jsonl` fail-closed 审计、能力报告。
7. WP-VLT0复用GV0同一CAS核心，扩展物理答案 Vault、三类最小权限 view及完整artifact reconcile；禁止另造第二套bundle store。
8. 只读 CandidateManifest exporter；不写生产 pipe。
9. 自然题走`P2A → 按需P2B → P3N → P3C`；生成题走`P3A → P3B admission-only bare → P3C`。P2B/P3B都只做problem-only准入；P2-P4冻结对象完成后，才进入第一个正式guided/control因果实验P5。
10. 先实现`WP-CW0 Offline Cognitive Worker Runtime`公共合同、fake adapter、author/review角色、D盘file-backed Vault/receipt和低并发恢复；随后分别实现`WP-CW-D1 DevinCliModelRoleAdapter`与`WP-CW-C1 CodexExecModelRoleAdapter`。Devin认知候选精确请求`glm-5-2`（GLM-5.2 High，effort由UID编码），不得使用solver_harness或Solver workspace。
11. 单独实现`WP-HG0 Offline Human Task & Gate Runtime`：file-backed人工任务、actor身份、职责分离、签名GateDecision和HUMAN_PENDING；禁止ModelRole自批。这里的offline只证明组件合同，不是canonical Gate激活。
12. `WP-QA0` development只用fake/stub和签名fixtures证明不可变P3A状态链，不调用真实Devin/Codex、不提交正式HumanGate。真实双载体纵切与`AuthoringBakeoff-A`必须等待DB1I的`DatabaseSchemaStateReport`、RT1的`DatabaseRuntimeCapabilityReport + ArtifactCommitReconcileCapabilityReport`、VLT0/HG0能力与逐次授权全部有效；模型调用、HumanGate、WorkEvent和artifact只走canonical DB/CAS运行链，不连Redis、不启动Target Solver、不产生bare/Tell结论，禁止file-only live旁路。
13. `WP-QA1 Question Admission`只有在QuestionRelease、Vault、D盘存储/空间、预算、`P3A/G-Q-RELEASE`及Database logical site/schema state/runtime、TargetSolverPort/Devin adapter、Harness资源、NoTool、SafeLaunch、AnswerIsolation、artifact commit/reconcile能力全部PASS后，才可执行canonical P3B problem-level bare并经P3C人工Gate冻结Case角色；它不等待完整P2/P3先PASS，file-only lab也不能冒充P3B。
14. QA0通过后再做`WP-CW1 Production Cognitive Worker Expansion`，增加P3N/P6角色、judge pool、DB-backed lease/fence和reconcile；solver pool仍只归`WP-SV1` TargetSolver。

Devin CLI的`glm-5-2`（本机catalog显示GLM-5.2 High）与Codex/Responses中的`gpt-5.6-sol`高推理配置是WP-QA0的并列候选，不是已实现能力或已胜出的生产配置。Devin的High由精确model UID编码；Codex的model/effort/mode/orchestration分别冻结。两者都必须经过角色级能力探针；WP-QA0的Bakeoff-A不含bare，WP-QA1对不可变calibration releases执行Bakeoff-B，之后还需未见brief qualification。评价只决定角色默认profile，不取消其他已合格adapter。

## 完整实现文档状态

2026-08-14已建立`docs/implementation/`、`docs/audit/`和`docs/decisions/`规定性文档体系，覆盖双认知载体、P0–P9、工作包DAG、对象/Schema、存储、安全、恢复、测试与未来审计。`WP-DOC0`的subject commit固定为`8b5e9c92fd8b05a4811b0c9e8336b3e3dcc0170c`，干净提交上的文档合同检查和bootstrap evidence已落在[`evidence/wp-doc0/`](implementation/evidence/wp-doc0/)；其machine completion contract为`DOC_BOOTSTRAP_RECORD`。R1整改后 WP-DOC0 IN_PROGRESS（doc checker source hash/clauses/remainder漂移已修复，待干净subject上重新验证生成新receipt）；此前曾标为`READY_FOR_AUDIT`，但审计确认doc checker FAIL时不应保持该状态。不是`AUDITED_PASS`，也没有生成ImplementationCompletionBundle。文档存在和机器自检通过都不提升任何运行能力。

**R0 整改后状态（2026-08-14）**：审计确认 WP-GV0 状态为 `IMPLEMENTED_PENDING_EVIDENCE`（不是 `READY_FOR_AUDIT`），且发现三个 P0 Gate 旁路（CompletionContractVerifier 未执行完整 Schema、HumanGate 无真实 Ed25519 验签、DB1I 授权链可绕过）。WP-VLT0 到 WP-OP1 共 22 个包曾被越级标为 `IMPLEMENTED_PENDING_EVIDENCE`，但 development dependency 未满足（GV0 未到 READY_FOR_AUDIT），现已纠正回 `NOT_STARTED`；既有代码视为 `existing unqualified implementation input`，须新 remediation attempt 重新资格化。其他工作包仍 `NOT_STARTED/NOT_IMPLEMENTED`。

## WP-GV0 实现状态：IMPLEMENTED_PENDING_EVIDENCE

2026-08-14 完成 WP-GV0 代码和测试开发，状态为 `IMPLEMENTED_PENDING_EVIDENCE`（不是 `READY_FOR_AUDIT`）。两个硬阻塞阻止升至 `READY_FOR_AUDIT`：

### 已实现

| 能力 | 模块 | 说明 |
|---|---|---|
| CompletionContractVerifier | `src/seven_system/contracts/completion_contract.py` | DAG-aware owner/contract/schema/actor 验证，固定错误码，fail-closed |
| SecurityContractVerifier | `src/seven_system/contracts/security_contract.py` | EEA→Permit→Receipt 链验证，签名结构、扩权拒绝、ordinal 唯一、额度守恒 |
| ReservationBackendPort | `src/seven_system/contracts/reservation.py` | GV0 冻结的原子预留接口 + side-effect-free 参考后端 |
| CompletionArtifactStore | `src/seven_system/storage/artifact_store.py` | 最小 D 盘 content-addressed append-once store，symlink/fallback/hash-conflict 拒绝 |
| VerifierCapabilityReport | `src/seven_system/contracts/capability_report.py` | GV0 能力报告生成器 |
| 固定错误码 | `src/seven_system/contracts/errors.py` | 30+ 错误码枚举，下游按码匹配 |
| CLI 命令 | `src/seven_system/cli.py` | `gv0-verify-completion-contract` 和 `gv0-store-put`，fail-closed 默认 |

### 测试覆盖

- 51 项 GV0 专项测试（golden/negative/fault injection），全部 PASS
- 109 项全量回归测试（含 25 subtests），全部 PASS
- blocker tests 覆盖：owner/contract/schema/actor 错配、伪签名、EEA 扩权、重复 ordinal、额度不守恒、store symlink/fallback/hash-conflict

### 显式不主张（nonclaims）

- 不主张真实 Ed25519 签名验证能力（GV0 只做结构检查，密钥验证归 HumanGateService）
- 不主张 DB_V2 或 SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER 后端实现（归 WP-DB1I / WP-RT1）
- 不主张 Vault、HumanGate、模型或 Solver live capability
- 不主张独立审计或 AUDITED_PASS
- side-effect-free 参考后端仅用于隔离 fixture 测试，不是真实 DB 或 D 盘 ledger
- 自托管 ImplementationCompletionBundle 需要 D 盘写授权（EEA/Permit/RESERVED），当前未获得

### 硬阻塞（阻止升至 READY_FOR_AUDIT）

1. **WorkPackagePlan schema-validity BLOCKED**：`normative_review_record_ref_and_hash` 必须是非 null ref_hash（Schema 对非 DOC0 包强制），但 `NormativeRequirementReviewRecord` 尚未生成——640 条条款全部 pending semantic review，`consumer_policy.requires_independent_review_record_before_non_doc0_plan=true`。已生成 plan draft（`evidence/wp-gv0/wp-gv0-plan-draft.v1.json`）显式记录此阻塞。
2. **D-volume self-hosted ImplementationCompletionBundle BLOCKED**：12号文档明确"GV0先以SIDE_EFFECT_FREE在隔离fixture中实现...随后必须取得覆盖精确D盘写入的EEA、LiveRunPermit与原子RESERVED，才可使用已经验证的store生成自己的ImplementationCompletionBundle"。当前未获 D 盘写授权，bundle 未生成。

### 已生成物证

| 物证 | 路径 | 说明 |
|---|---|---|
| 测试执行收据 | `evidence/wp-gv0/gv0-test-execution-receipt-a3ac934.json` | 绑定 subject commit a3ac934，51 GV0 + 109 全量回归 PASS，零副作用 |
| VerifierCapabilityReport | `evidence/wp-gv0/gv0-verifier-capability-report-a3ac934.json` | 绑定 DAG hash 和 implementation tree hash，列出全部 test IDs 和 golden/negative vectors |
| WorkPackagePlan draft | `evidence/wp-gv0/wp-gv0-plan-draft.v1.json` | 显式记录两个阻塞和 inherited audit debt，不是 schema-valid plan |
| 实现状态记录 | `evidence/wp-gv0/gv0-implementation-status-record-a3ac934.json` | 状态=IMPLEMENTED_PENDING_EVIDENCE，记录 blockers、claims、nonclaims |
| GV0 测试 stdout | `evidence/wp-gv0/gv0-test-stdout-a3ac934.txt` | 51 项测试详细输出 |
| 全量回归 stdout | `evidence/wp-gv0/full-regression-stdout-a3ac934.txt` | 109 项 + 25 subtests 摘要 |

### 继承的审计债

- WP-DOC0 的 `IN_PROGRESS` 审计债由 GV0 development 继承（DOC0 曾标为 READY_FOR_AUDIT，R1 整改后回到 IN_PROGRESS）
- 规范审查记录（`normative_requirement_review_record`）尚未生成——640 条条款全部 pending semantic review，`consumer_policy.requires_independent_review_record_before_non_doc0_plan=true`。这是 GV0 WorkPackagePlan schema-valid 的硬阻塞
- GV0 的 `IMPLEMENTED_PENDING_EVIDENCE` 不等于 `READY_FOR_AUDIT`，更不等于 `AUDITED_PASS`——需独立审计者按四轴 verdict 审计
- D-volume self-hosted bundle 未生成——需 repo 外 owner 签发 EEA/LiveRunPermit/AuthorizationConsumptionReceipt(RESERVED)
