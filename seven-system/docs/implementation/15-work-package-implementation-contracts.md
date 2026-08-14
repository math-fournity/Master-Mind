# 工作包实施合同与逐包验收表

## 一句话结论

`03-work-package-dag.md`决定顺序，本文决定每个包必须交付什么。实施AI不得把“之后再设计”当代码TODO；未冻结的语义先修spec，再编码。

## WorkPackagePlan

每个包开工前先生成下列机器对象并绑定canonical DAG节点：

```yaml
schema_id: seven/work-package-plan
schema_version: 1
wp_id:
implementation_attempt_id:
plan_timing: PREREGISTERED
execution_mode: SIDE_EFFECT_FREE | AUTHORIZED_LIVE_CANARY
protocol_deviations: []
baseline:
  commit:
  tree:
canonical_dag:
  ref:
  sha256:
development_dependency_bundles: []
inherited_audit_debt: []
activation_dependencies: []
requirement_ids: []
normative_clause_scope:
normative_spec_refs_and_hashes: []
goals: []
non_goals: []
allowed_path_rules: []
forbidden_boundaries: []
input_object_types_and_hashes: []
output_object_types: []
interfaces_and_schema_ids: []
state_machines_and_registries: []
security_and_view_contracts: []
idempotency_fence_recovery_rules: []
test_plan_ids: []
external_execution_authorization_ref: null
live_run_permit_ref: null
authorization_consumption_reservation_ref: null
side_effect_budget:
  db_connections: 0
  db_writes: 0
  redis_connections: 0
  remote_model_calls: 0
  target_solver_launches: 0
  d_volume_writes: 0
pass_criteria: []
stop_conditions: []
explicit_nonclaims: []
plan_hash_algorithm: sha256(canonical-json-with-plan_hash-null)
plan_hash:
```

没有该对象的工作包不得进入`IN_PROGRESS`。`SIDE_EFFECT_FREE`要求三个授权ref全部为null且六项预算全为0；`AUTHORIZED_LIVE_CANARY`要求三个ref都是带hash引用，并至少有一项正预算。只有父级EEA、其不可扩权子级LiveRunPermit和原子`AuthorizationConsumptionReceipt(status=RESERVED)`全部存在且通过独立验证时，才可执行许可范围内的live canary；任意单一ref不构成授权。

`WP-DOC0`在VLT0/CAS尚不存在时使用专门的bootstrap例外：canonical DAG固定其`completion_contract=DOC_BOOTSTRAP_RECORD`；先冻结机器`wp-doc0-plan.v1.json`，实施subject commit后在第二个Git evidence-index commit中生成`DocBootstrapCompletionRecord`，不生成ImplementationCompletionBundle。该历史bootstrap plan早于`execution_mode`字段，Schema仅对`wp_id=WP-DOC0`兼容字段缺失并强制其授权refs为null、预算全零，语义上等同`SIDE_EFFECT_FREE`；任何后续工作包都必须显式写mode。VLT0完成后必须把原始record逐字节导入D盘CAS并生成`DocBootstrapImportAnchor`；该例外只适用于DOC0文档包，不能扩展到任何live/runtime工作包。

## 基础与执行面工作包

表内`GV0`即canonical `WP-GV0`，它是两个跨对象验证器公共核心的唯一实现包；DB1I/RT1只补各自reservation backend，不取得另一份验证器所有权。

| WP | 冻结输入 | 必需实现/对象 | blocker与故障验收 | `READY_FOR_AUDIT`最低产物 |
|---|---|---|---|---|
| DOC0 | 当前commit、387/389裁决、完整目录 | 规范树、canonical DAG、RequirementMatrix、NormativeRequirementIndex生成器/Schema/快照、审计入口 | 断链、DAG环/投影漂移、source hash漂移、无分类MUST、状态过度主张 | 文档链接/DAG/traceability收据、`DocBootstrapCompletionRecord`；不是ImplementationCompletionBundle |
| GV0 | DOC0 bootstrap record、canonical DAG/Schema hashes、签名与授权合同、D卷/root policy；self-host另需精确D写授权链 | `SecurityContractVerifier`、`CompletionContractVerifier`、原子ReservationBackendPort、最小CompletionArtifactStore、固定错误码/向量 | owner/contract/schema/actor错配、DOC0伪Bundle、实施者写auditor节点、伪签名、扩权、重复ordinal、额度不守恒、store symlink/fallback/hash冲突/半写、无D写permit | VerifierCapabilityReport、三completion-contract向量、reference backend收据；获授权后才生成D盘自托管GV0 ImplementationCompletionBundle，未授权则BLOCKED |
| VLT0 | GV0验证器与最小store、D卷指纹、root policy、sensitivity registry | 复用同一CAS核心扩展Vault/view derivation/seal/access ledger/reconcile | 平行bundle store、symlink/fallback/hash冲突/越权/掉盘/半提交 | CAS/Vault CapabilityReports、同一store lineage、故障与越权收据 |
| HG0 | GV0验证器、ActorRoster、GateTypeRegistry、信任根 | HumanTaskPort、HumanGateService、验签/撤销/replay；消费GV0验证器而不复制 | 自批、过期、重放、payload改写、职责冲突、局部semantic旁路 | GateReadinessReport、签名向量、key-lifecycle演练 |
| CW0 | Role/Capability registries、Vault port | ModelRolePort、fake adapter、attempt/receipt/reconcile | unknown-start、stale fence、敏感sink、非法状态 | fake全状态contract/fault收据 |
| CW-D1 | Devin profile、role policies、CW0；live另需DB1I SchemaState、RT1 Runtime/Reconcile、VLT0/HG0 | Devin认知adapter、ATIF parser、profile capability | UID/export/tool/view/配置漂移、旁路harness、无原子permit ledger即dispatch | 初始三角色canary；每个未测格为NOT_TESTED，禁止写入NOT_QUALIFIED |
| CW-C1 | Codex profile、role policies、CW0；live另需DB1I SchemaState、RT1 Runtime/Reconcile、VLT0/HG0 | Codex adapter、JSONL parser、profile capability | context污染、model/mode漂移、child usage缺失、fallback、无原子permit ledger即dispatch | 精确profile canary、receipt、逐格资格状态 |
| DB1L | GV0验证器、站点配置、Strict spec | 逻辑site v2只读adapter/report/verifier；枚举全部`seven_*_vN`冲突 | wrong/default DB、read-time DDL、凭据泄漏、catalog漂移、复用非Seven集合 | `DatabaseLogicalSiteCapabilityReport`与零写入receipt |
| DB1I | DB1L site report/零写收据、GV0/VLT0/HG0能力、ObjectPersistenceMapping、IndexAdequacyReport、版本化MigrationSpec、精确授权链 | fenced `seven_*_vN` apply/verify/resume、GV0 `SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER` backend、`DatabaseSchemaStateReport + SchemaBootstrapReceipt + SchemaBootstrapImportAnchor` | 每DDL前后崩溃、旧fence、计划漂移、重复apply、owner/permit错配、bootstrap/import差异 | SchemaState与bootstrap action/import收据；不得产Runtime/Reconcile capability |
| RT1 | DB1I三输出、VLT0 CAS/Vault能力、GV0 verifier接口、冻结site/spec/plan/DAG hashes | WorkEvent、lease/fence、outbox、CommitIntent、reconcile、GV0 canonical DB reservation backend | 100次重投、重复ordinal、额度不守恒、stale commit、CAS/DB单边、Redis丢失、输入hash漂移 | `DatabaseRuntimeCapabilityReport + ArtifactCommitReconcileCapabilityReport + RuntimeCheckpoint/recovery receipts`；不得重发SchemaState |
| SV1 | Vault/RT1、Harness profile | TargetSolverPort、Harness adapter、NoTool、LaunchReceipt | direct-devin旁路、tool event、缺trajectory、repo workspace | Harness/NoTool/SafeLaunch/AnswerIsolation reports |

## 输入、Tell、Case与实验工作包

| WP | 冻结输入 | 必需实现/对象 | blocker与故障验收 | `READY_FOR_AUDIT`最低产物 |
|---|---|---|---|---|
| IN1 | 冻结producer bundle（producer schema/version、export manifest、root hash、attempt refs、只读许可） | 只读CandidateManifest/exporter、duplicate lineage | 生产写回、可变引用、缺artifact/contract、source root漂移 | 源端绑定fixture与零写入收据 |
| TX1 | 冻结system bundle、Candidate refs | taxonomy/Tell registry、M:N、release lineage | manifestation=Core、旧Evidence换外键、无Gate改pointer | registry release、迁移/失效/继承测试 |
| QA0 | development用签名合同fixtures；真实激活另需HumanGate签发的AuthoringBootstrapInputPack、DB1I SchemaState、RT1 Runtime/Reconcile、VLT0/HG0能力与逐次授权 | fake/stub先证明P3A状态链；真实Devin/Codex纵切、QuestionRelease、Bakeoff-A的模型/HumanGate/WorkEvent/artifact只走canonical DB/CAS运行链 | 未签bootstrap输入、file-only live旁路、缺任一canonical report、修题不失效、作者泄漏、bare指标偷入、retry-until-desired | fake/fault收据；获授权后才有Devin/Codex单adapter真实纵切、盲评、人门收据；无Solver、无Redis投影 |
| CW1 | 已审profiles、RT1 | P3N/P6 workers、DB lease/reconcile、RoleQualificationMatrix | 未合格格路由、同会话审稿、judge读越权view | 所有生产启用role×profile×policy格有结论 |
| QA1 | 不可变QuestionRelease、SV1、Bakeoff-B plan | P3B problem-only bare、BareQualificationResult | Tell/Hint偷入、改题、过滤成功、retry-until-fail | 全结果收据、盲化Bakeoff-B；无P5 claim |
| CS1 | 自然P2/P3N或生成P3A/P3B物证 | CasePack、AdmissionDecision、Mechanism/Relation审查 | 自然题伪造draft、模型自签角色、process-only进result | 双入口fixture、P3C验签、角色冻结 |
| ST1 | TX1 release；development使用显式fixture_pre_state，activation使用CS1 Case/BranchSnapshot | selector/abstain、renderer、binding、injection、critic | fixture冒充live Case、答案绑定、Core/文本混淆、distractor不对等、组件漂移 | TellStrategyRelease和各arm payload纯程序重放 |
| EX1 | CasePack、StrategyRelease、P4 plan | 随机化、等资源P5、Solver artifacts | 多调用/token、原截断bare baseline、运行后改plan | 全部arms/negative/invalid保留、randomization replay |

## 审计、证据、修订与规模工作包

| WP | 冻结输入 | 必需实现/对象 | blocker与故障验收 | `READY_FOR_AUDIT`最低产物 |
|---|---|---|---|---|
| AU1 | sealed P5 runs、AuditPlan/views | Broker、三审、RunAudit | 真arm泄漏、Judge结论互看、复述当action、分歧自选 | 三审分别seal、分歧/缺失合法terminal |
| EV1 | ExperimentPlan、RunAudits | contrast aggregator、EvidenceRecord、分析registry | episode supports、cluster双计、invalid填0、换估计器 | 随机对照重放、missing/multiplicity/cost完整 |
| RV1 | sealed P7 EvidenceRecord集合、ProvenanceSnapshot、Revision policy | failure localization、NO_CHANGE/revision、holdout消费 | 读取尚未生成的最终EvidenceIndex、fit=confirmation、反复偷看、单例split、candidate自批 | NO_CHANGE或受控revision纵切，旧证据不改 |
| VR1 | P0–P8 sealed DAG、GV0 CompletionContractVerifier | Verdict Builder、checkpoint、replay/remainder、全完成对象合同回验 | PASS平均FAIL、NOT_TESTED=PASS、orphan、不可反查、owner/contract错配 | factory/scientific/scale分轴Verdict、completion-contract remainder=0、全链remainder=0 |
| GA1（auditor-owned） | owner签发AuditAssignment、VR1 subject/CompletionBundles、repo外pinned trust-root hash | 独立重放、四轴AuditRecord、审计债裁决 | 实施者自签、审计时改树、信任根来自被审bundle、缺assignment | 受信任actor签名的`AUDITED_*`或明确PARTIAL/FAIL；不使用实施CompletionBundle合同 |
| OP1 | VR1候选系统、资源policy；activation另需GA1 AUDITED_PASS | multi-worker、Redis投影、多Epoch/active learning/soak | 未审即live、饥饿、队列丢失、中途换版本、holdout重用 | soak、Redis重建、create→seal→next Epoch、跨Epoch remainder=0 |

## 逐包状态与停止

1. 文档、Schema、fake和无副作用测试可按development dependencies连续实现；
2. 首次读真实DB、调真实模型、启动Solver、写DB/Redis、恢复dispatch、切active release或提交真实人门前，必须满足activation dependencies，并同时持有有效父级`ExternalExecutionAuthorization`、不可扩权`LiveRunPermit`和原子额度预留收据；
3. 任一blocker test失败、规范冲突、敏感泄漏、未知启动、hash/fence冲突立即停止并保留物证；
4. 功能或科学结果可以是FAIL/negative，只要协议完整就是合法产物；
5. `owner_type`与`state`正交：任何owner的节点都从canonical状态集开始，未指派审计者写reason而不创造`AUDITOR_OWNED_*`状态；
6. implementer-owned普通包由实施者最高推进到`READY_FOR_AUDIT`，DOC0同属implementer-owned但按DAG交付`DOC_BOOTSTRAP_RECORD`；auditor-owned包拒绝所有实施者完成对象和状态命令，只能由外部Assignment绑定的审计路径产生AuditRecord；
7. 未解决审计债随最终SystemCompletionBundle交给独立审计者。
