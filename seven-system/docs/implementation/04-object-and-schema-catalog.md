# 对象、Schema与状态目录

## 一句话结论

每个跨阶段事实都必须是版本化、可哈希、可验证的对象；Markdown里的字段示例不能替代JSON Schema，Schema通过也不能替代跨对象semantic verifier。

## Schema共同规则

所有canonical对象必须：

- 有稳定`schema_id`和`schema_version`；
- `additionalProperties=false`，未知字段拒绝；
- 使用canonical JSON，拒绝NaN/Infinity和不稳定浮点；
- 内容hash规则版本化，自引用hash字段不参与自身内容hash；
- 引用父对象的ID与hash；
- 明确`sensitivity`、允许view和Vault/CAS sink；
- `N/A`使用枚举和理由，禁止空字符串；
- 有独立semantic verifier检查跨字段和跨对象不变量；
- 派生对象记录生成器/规则/代码hash；
- 旧版本保留，不能原地改外键伪装成新对象。

安全关键对象不能停留在Markdown字段示例。当前冻结的机器合同是：

| 对象 | JSON Schema | 机器边界 |
|---|---|---|
| AuditAssignment | [`audit-assignment.v1.schema.json`](audit-assignment.v1.schema.json) | owner经repo外渠道钉住root/roster/policy，绑定auditor、subject、bundle、计划、scope和attestation key |
| AuditRecord | [`audit-record.v1.schema.json`](audit-record.v1.schema.json) | 保存repo外root观察、四轴finding/verdict及auditor签名；对象本身不改变状态 |
| ExternalExecutionAuthorization | [`external-execution-authorization.v1.schema.json`](external-execution-authorization.v1.schema.json) | 人类签发的外部副作用上限，不能直接交给adapter消费 |
| LiveRunPermit | [`live-run-permit.v1.schema.json`](live-run-permit.v1.schema.json) | 将父授权收窄为逐action、逐ordinal、逐job/attempt/input/profile/sink的可预留单位 |
| AuthorizationConsumptionReceipt | [`authorization-consumption-receipt.v1.schema.json`](authorization-consumption-receipt.v1.schema.json) | append-only记录`RESERVED/CONSUMED/RELEASED_UNUSED/UNKNOWN_START_HELD/QUARANTINED` |
| OperatorCommandRegistry | [`operator-command-registry.v1.schema.json`](operator-command-registry.v1.schema.json) | `EXTERNAL_SIDE_EFFECT`在Schema层就必须声明EEA、permit、action registry、原子预留和最终Port |

Schema只检查单对象形状。WP-GV0是`SecurityContractVerifier`和`CompletionContractVerifier`公共核心的唯一代码所有者：前者检查签名、有效期、撤销、root/roster/policy一致性、Assignment scope、EEA→Permit不可扩权、ordinal唯一和额度守恒；后者加载冻结DAG，检查`owner_type + completion_contract + submitted schema + actor authority`。状态是独立维度，不能用`AUDITOR_OWNED_*`之类自造状态替代owner校验。Security verifier的原子预留Port由GV0冻结，WP-DB1I只实现D盘Schema-bootstrap backend，WP-RT1只实现canonical DB事务backend。GV0同时拥有最小D盘`CompletionArtifactStore`以自托管首个普通ImplementationCompletionBundle，VLT0必须复用并扩展同一CAS核心。只运行JSON Schema、只实现其中一个后端或复制一套局部semantic check，都不能接受任何上述对象。

## 基础设施对象

| 对象 | 核心用途 |
|---|---|
| RuntimeManifest | 冻结Epoch、代码、Schema、profiles、预算、路径和停止规则 |
| CapabilityReport | 证明精确组件/profile能力，而非自报PASS |
| WorkItem / WorkEvent | 逻辑工作与append-only状态跃迁 |
| RoleInvocationAttempt / SolverExecutionAttempt | 物理执行attempt；不能混用 |
| LeaseRecord / FenceRecord | worker所有权和旧worker拒绝 |
| OutboxRecord | DB真值到队列投影的可重放事件 |
| ArtifactRef / ArtifactSeal | CAS内容、manifest和提交证明 |
| CompletionArtifactStore | WP-GV0建立的最小D盘append-once完成包store；VLT0复用同一CAS核心扩展，不能形成第二真值 |
| RecoveryRecord / AlertRecord | 恢复裁决和持久告警 |
| RuntimeCheckpoint | ledger/queue cursor、active hash、预算和holdout状态 |
| CommitIntent | 在CAS seal前持久化本次job/attempt/input/terminal/fence/授权的唯一提交意图 |
| ExternalExecutionAuthorization / LiveRunPermit | 将人类授予的外部副作用范围收窄成精确的work-package/run许可 |
| AuthorizationConsumptionReceipt | 原子记录permit额度的预留、消耗、释放或隔离，防止双重调用 |
| DatabaseSchemaStateReport | 证明真实site catalog与某个已冻结Schema spec精确一致 |
| DatabaseRuntimeCapabilityReport | 证明transaction/CAS、event sequence、lease/fence、outbox与recovery语义 |
| ArtifactCommitReconcileCapabilityReport | 证明CommitIntent、partial→seal、DB链接和单边崩溃恢复语义 |
| SchemaBootstrapLedger / SchemaBootstrapReceipt / SchemaBootstrapImportAnchor | Seven集合存在前的D盘append-only DDL真值、执行收据与后续DB导入锚 |
| [VaultAccessCapability](vault-access-capability.v1.schema.json) | 由可信issuer签发、精确绑定principal/operation/object/view/sink且可撤销的最小访问能力；没有通配授权 |
| [AccessDecision](access-decision.v1.schema.json) / [AccessEvent](access-event.v1.schema.json) / [ViewDerivation](view-derivation.v1.schema.json) | deny-by-default裁决、append-only访问账和sealed source到最小view的可复验派生链；对象中没有raw Vault路径 |

## 模型与人工角色对象

| 对象 | 核心用途 |
|---|---|
| RoleExecutionContract | 冻结角色、输入view、requested profile、权限、预算和重试 |
| RoleTypeRegistry / [RoleQualificationMatrix](role-qualification-matrix.v1.schema.json) | 冻结机器角色全集，并逐格记录`role × carrier × model × profile × view × policy × adapter × capability`资格及required/pass/not-tested/failed/extra remainder；不得通配继承 |
| CarrierProfile | 精确carrier/model/effort/mode/orchestration/tool policy |
| CognitiveWorkerCapabilityReport | 对一个角色+精确profile的端到端能力证明 |
| AIInvocationReceipt | 事后effective配置、事件、usage、成本、输出和终止物证 |
| ReviewIndependenceRecord | context/model/provider/human/formal独立性分轴 |
| HumanGatePolicy / ActorRoster | 授权actor和职责分离规则 |
| HumanTask / HumanGateDecision | 待审对象与签名决定 |
| AuditAssignment | 由站点owner签发，绑定独立审计者、被审subject、信任根和允许的审计动作；被审树不能自签 |
| AttestationSignerPort | 在模型workspace之外保存审计attestation私钥；只为Assignment绑定的auditor和精确canonical bytes生成Ed25519 envelope，不判断finding或写状态 |
| HumanGateTrustRootSnapshot / HumanGateKeyRecord | 冻结验签信任根、actor/key绑定、有效期和撤销历史 |
| TrustRootBootstrapReceipt / KeyRevocationRecord / GateTimePolicy | 锚定初始信任仪式、密钥撤销语义与过期时间边界 |
| HumanGateReadinessReport | 证明trust root、algorithm registry、roster、separation、time policy与replay store可用 |
| ProtocolRegistrySnapshot | 冻结GateType、WorkEventType、CapabilityKind、AlertAction、EvidenceStatus等动态全集 |
| [AuditInputPack](audit-input-pack.v1.schema.json) | 只读汇总候选完成物证，供未来GA1独立审计前机械预检；不创建`AuditAssignment`、不生成`AuditRecord`、不改变状态、不声明`AUDITED_*` |
| [AuditReadinessReport](audit-readiness-report.v1.schema.json) | 只读比较`AuditInputPack`与声明scope的覆盖差异，列出missing/unexpected/invalid工作包；`COMPLETE`也只表示机械交接覆盖完整，不表示GA1审计通过 |
| [DatabaseLogicalSiteCapabilityReport](database-logical-site-capability-report.v1.schema.json) | WP-DB1L只读逻辑站点报告；冻结精确数据库身份、CURRENT_DATABASE、site fingerprint、catalog snapshot、seven集合枚举、零写入收据和自哈希；不授权DDL、migration、runtime事务或outbox |

## 题目与Case对象

| 对象 | 核心用途 |
|---|---|
| CandidateManifest | 冻结自然题/历史attempt入口 |
| HistoricalBareEvidenceAssessment | 判断旧bare物证是否足够或需P2B |
| MechanismContract | 机制、不变量、trigger、动作、进展、边界、泄漏预算 |
| CoverageCell | 数学分支、迁移距离、case关系和证据用途位置 |
| AuthoringBrief | 受控生成目标、禁止捷径和预算 |
| QuestionDraftVersion | append-only草稿、父版本、公开题面和密封解答refs |
| AdversarialReview / VerificationDossier | statement攻击与数学正确性核验 |
| QuestionRelease | 由G-Q-RELEASE签发的不可变题面 |
| AuthoringEvaluationPack | 冻结calibration/qualification用途、brief/cell集合、盲化、指标、停止和禁止流入的下游lane |
| AuthoringBootstrapInputPack | 由HumanGate批准的QA0启动包；冻结MechanismContract、CoverageCell和evaluation pack来源，不依赖尚未存在的生产CasePack |
| BareBaseline / BareQualificationResult | problem级bare分布和资格判定 |
| AdmissionDecision / CasePackVersion | P3C签名角色冻结和题包版本 |

## 分类学、Tell与策略对象

| 对象 | 核心用途 |
|---|---|
| TaxonomySnapshot / AttributeDictionaryVersion | 冻结分类坐标、枚举、定义与适用版本 |
| FCAContextSnapshot | 保存用于校准/重分类的对象—属性上下文；不是自动真理源 |
| ObservationView / TellManifestation | 同一latent机制在不同观察粒度和trace位置的表现 |
| TellRecognitionRecord | span、observer、置信度、候选分叉与taxonomy snapshot下的识别事件 |
| TellFamily / TellCore | 因果身份、invariant kernel、认知动作与家族谱系 |
| ApplicabilityBoundary | trigger、negative guards、binding roles与适用变换 |
| TellHintRelation | Tell↔Hint/Renderer显式M:N边和适用条件 |
| HintRenderer / HintInstance | 面向模型的表达策略与本次绑定后的实际payload |
| SelectorDecision / InjectionPolicy | 检索、排序、abstain、注入位置和policy版本 |
| Progress/Termination/Critic/CompositionContract | 执行、退出、纠偏与多Tell关系 |
| TellStrategyRelease | 锁定Core、boundary、selector、renderer、injection、critic、composition、taxonomy和scope的hash manifest |
| MathValidityRecord / SystemEfficacyRecord | 数学/机制有效性与特定Solver/资源下效力分开记账 |

## 实验、审计、证据和学习对象

| 对象 | 核心用途 |
|---|---|
| ExperimentPlan / ResourceContract | arms、contrast、随机化、预算、停止和盲化 |
| BranchSnapshot | 各arm共享的处理前状态 |
| RunArtifactBundle | 按purpose封存intake/admission/causal运行物证 |
| ProcessAudit / ProofJudgment / LeakageAudit | 三种独立真值 |
| RunAudit | 单episode观察，不直接作因果supports |
| EvidenceRecord | 预注册contrast级因果或迁移证据 |
| NoChangeDecision / RevisionProposal | 不变或受控修订分支 |
| CandidateRelease / ProspectiveEvaluation | 冻结候选与一次性前瞻确认 |
| SixGateVerdict / MachineVerdict | 科学门与系统门分轴结论 |
| EvidenceIndex | 从Verdict反查全部物证的DAG索引 |
| ProvenanceSnapshot | P8开始前对sealed P7 EvidenceRecord集合及其谱系的只读快照；不是最终EvidenceIndex |
| ImplementationCompletionBundle / AuditRecord | 分别对应DAG的`IMPLEMENTATION_BUNDLE / AUDIT_RECORD`；AuditRecord必须绑定外部AuditAssignment和四轴Verdict |
| WorkPackagePlan / NormativeRequirementIndex / NormativeRequirementReviewRecord | 冻结每个实现包的输入、边界和验收，并机械枚举规定性条款到需求族或`LOCAL_ONLY`；普通implementer-owned包可由stdout-only `build-work-package-plan`从DAG、索引和已签规范复核记录派生脆弱字段，且必须先验证真实规范复核记录 |
| DocBootstrapCompletionRecord / DocBootstrapImportAnchor | DAG的`DOC_BOOTSTRAP_RECORD`只适用于WP-DOC0：在VLT0尚未实现时，以Git侧第二提交锚定DOC0物证；VLT0完成后原样导入CAS并建立不可改写的导入锚 |
| DocContractVerificationReceipt / DOC0TestExecutionReceipt | 分别保存文档合同检查器的Schema-valid结果，以及绑定精确subject commit/tree、命令输出与零副作用计数的DOC0测试收据 |
| OperatorCommandRegistry | 冻结CLI/API/worker入口、读写级别、Port、授权、幂等/fence、receipt和退出码 |
| AuditLaneStatusRegistry / CausalEligibilityRegistry | 冻结P6 lane终态与RunAudit因果资格的总枚举和转换规则 |
| AnalysisMethodRegistry / MultiplicityRuleRegistry / StoppingRuleRegistry | 冻结P7估计器、伪随机参数、多重性和停止语义 |
| VerdictRuleRegistry | 冻结Evidence状态到P9四轴Verdict的总函数和golden vectors |
| EpochSelectionRecord / CoverageTensorSnapshot/Delta | 冻结跨Epoch选格依据、覆盖变化和主动学习决策 |
| GlobalBudgetLedger / ActiveReleasePointerSnapshot | 跨Epoch预算真值与active release指针快照 |
| EpochSealRecord / CrossEpochDuplicateAssessment / LongitudinalLearningVerdict | 封口Epoch、阻止跨Epoch重复计数并承载长期学习结论 |

## Vault访问与角色资格的机器合同

这两组Schema解决的是两个不同问题：Vault访问合同回答“这个精确principal此刻能否对这个精确对象做这个精确动作”，资格矩阵回答“这个精确模型载体组合是否已被证明确实能承担这个角色”。前者不能由矩阵PASS替代，后者也不能由一次访问ALLOW替代。

- [`vault-access-capability.v1.schema.json`](vault-access-capability.v1.schema.json)冻结签发者、principal、单一operation、object hash、view hash、sink、policy、时窗、nonce和revocation handle；`deny_by_default=true`且`raw_vault_path_disclosure=false`。
- [`access-decision.v1.schema.json`](access-decision.v1.schema.json)逐请求记录签名、issuer、时窗、principal、operation、object/view hash、sink、nonce replay和最新revocation检查。只有全部检查为`PASS`且revocation为`ACTIVE`时Schema才允许`ALLOW`；任何`UNKNOWN`走`DENY`。
- [`view-derivation.v1.schema.json`](view-derivation.v1.schema.json)把sealed source hash、派生规则/代码hash、redaction manifest、输出view hash和sink receipt连成一条链；模型可见交付固定为派生bytes加opaque handle，不能含raw Vault locator或capability token。
- [`access-event.v1.schema.json`](access-event.v1.schema.json)以sequence和previous-event hash形成append-only访问账；`ACCESS_GRANTED`必须反查ViewDerivation、sink write receipt和当时仍为`ACTIVE`的revocation检查。
- [`role-qualification-matrix.v1.schema.json`](role-qualification-matrix.v1.schema.json)拒绝`*`、`?`、glob字符及`ANY/ALL/DEFAULT`哨兵；每个cell显式绑定role、carrier、model、profile、实际input view、view/ACL/Vault capability、tool/network/sandbox、output sink、prompt、output Schema、adapter、parser和capability requirement。`completeness`保存required/pass/not-tested/failed/extra/missing/remainder集合与算法hash。

所有签名对象均使用独立domain separator；`signature_envelope`和issuer key必须按外部固定trust root验证。Schema只拒绝形状错误，nonce唯一、签名有效、时窗顺序、集合差分和跨对象hash相等仍由semantic verifier与持久化唯一约束负责。上述合同当前只是目标Schema，不表示Vault broker、revocation registry、matrix projector或Router enforcement已经实现。

## 版本化动态Registry

任何能改变路由、状态、Gate、告警动作或科学结论语义的枚举都不得在代码中使用`...`、自由字符串或provider返回值动态扩张。`ProtocolRegistrySnapshot`是Epoch必须冻结的canonical全集，至少包含：

| Registry | v1必须覆盖的语义 |
|---|---|
| `WorkItemKindRegistry` | `MODEL_ROLE / TARGET_SOLVER / HUMAN_GATE / DB_SCHEMA_APPLY / ARTIFACT_RECONCILE / AUDIT_ASSEMBLY / EVIDENCE_AGGREGATION / QUEUE_PROJECTION` |
| `WorkItemStateRegistry` | 等待、执行、恢复和终态，并引用每种kind的合法迁移表 |
| `WorkEventTypeRegistry` | create/lease/prepare/dispatch/accepted/started/human/retry/reconcile/artifact/commit/complete/quarantine/block/cancel系列事件 |
| `GateTypeRegistry` | `DB_SCHEMA_APPLY / EXTERNAL_LIVE_RUN / Q_RELEASE / CASE_ROLE / EXPERIMENT_START / REVISION_PRE / REVISION_POST / RELEASE_ACTIVATE / RESTRICT / RETIRE` |
| `CapabilityKindRegistry` | `DATABASE_LOGICAL_SITE / DATABASE_SCHEMA_STATE / DATABASE_RUNTIME / ARTIFACT_COMMIT_RECONCILE / CAS / VAULT / TARGET_SOLVER_HARNESS / TARGET_SOLVER_NO_TOOL / TARGET_SOLVER_SAFE_LAUNCH / TARGET_SOLVER_ANSWER_ISOLATION / COGNITIVE_WORKER / HUMAN_GATE_READINESS` |
| `AlertActionRegistry` | `NOTIFY / PAUSE_LANE / PAUSE_ALL / QUARANTINE_SCOPE / ABORT_EPOCH / REQUIRE_HUMAN` |
| `EvidenceStatusRegistry` | `SUPPORTS / CONTRADICTS / DOES_NOT_SUPPORT / INCONCLUSIVE_DUE_TO_PROTOCOL / NOT_TESTED`；机器条件以14号分析规范为准 |
| `AuditLaneStatusRegistry` | `VALID / INVALID_PROTOCOL / INCONCLUSIVE / MISSING / JUDGE_DISAGREEMENT / CONTAMINATED`及每个状态的升级/终结规则 |
| `CausalEligibilityRegistry` | `ELIGIBLE / PROCESS_ONLY / RESULT_ONLY / CONTAMINATED / INVALID / INCONCLUSIVE`，只能由P6三lane输入机械派生 |
| `AnalysisMethodRegistry` | P7估计器的参数、输入shape、伪随机算法/seed、tie rule和golden test vectors |
| `MultiplicityRuleRegistry` | primary/hierarchical/Holm/exploratory的精确算法和适用条件 |
| `StoppingRuleRegistry` | 样本、资源、安全tripwire和允许的序贯停止；禁止“跑到显著” |
| `VerdictRuleRegistry` | EvidenceStatus与P9四轴状态之间的完整、确定性映射；未知组合fail-closed |
| `OperatorCommandRegistry` | 所有CLI/API/worker入口和最终Port；未登记入口不得执行 |
| `AuthorizationActionRegistry` | DB DDL、remote model canary/invocation、Target Solver launch、live Epoch、Redis write、active release变更 |
| `AuthorizationConsumptionStatusRegistry` | `RESERVED / CONSUMED / RELEASED_UNUSED / UNKNOWN_START_HELD / QUARANTINED` |
| `HumanDecisionRegistry` | `APPROVE / REJECT / REQUEST_CHANGES / QUARANTINE`及gate-type quorum/conflict policy |
| `SignatureAlgorithmRegistry` | v1只允许`Ed25519`；其他算法必须新版本、ADR和测试向量 |

每个registry entry必须有`code`、人类语义、producer/consumer、允许的前置/后续状态、安全等级、`introduced_in`、可选`deprecated_in/replacement`。Snapshot记录registry version、前一版hash、entries排序规则和内容hash。新code必须经Schema/semantic verifier、ADR和兼容性评估进入新snapshot；运行时遇到未知code一律fail-closed。

文档中的`G-DB-SCHEMA-APPLY / G-Q-RELEASE / G-CASE-ROLE`只是供人阅读的显示标签，分别解析为canonical `DB_SCHEMA_APPLY / Q_RELEASE / CASE_ROLE`；签名envelope和数据库只能保存canonical code，不能把显示标签当成第二套枚举。

`WorkEventTypeRegistry v1`的最小精确code集是：`WORK_CREATED / LEASE_GRANTED / WORK_PREPARED / DISPATCH_REQUESTED / REQUEST_ACCEPTED / PROCESS_STARTED / GENERATION_STARTED / SIDE_EFFECT_STARTED / HUMAN_TASK_CREATED / HUMAN_DECISION_RECORDED / AUTHORIZATION_RESERVED / AUTHORIZATION_CONSUMED / AUTHORIZATION_RELEASED_UNUSED / AUTHORIZATION_UNKNOWN_START_HELD / RETRY_SCHEDULED / RETRY_EXHAUSTED / RECONCILE_STARTED / WRITERS_DRAINED / ARTIFACT_PREPARED / COMMIT_INTENT_RECORDED / ARTIFACT_SEALED / COMMIT_STARTED / COMMITTED / COMPLETED / SCIENTIFIC_COMPLETED / SCIENTIFIC_NEGATIVE / PROTOCOL_INVALID / QUARANTINED / BLOCKED / CANCEL_REQUESTED / CANCELLED / FAILED_PERMANENT`。某kind不适用的event必须由它的transition table拒绝；不得因为provider又返回了一种status就动态建立新事件语义。

event和state是不同命名空间：例如`RECONCILE_STARTED`投影为`RECONCILING`、`COMMIT_STARTED`投影为`COMMITTING`、`SCIENTIFIC_COMPLETED`投影为`SCIENTIFIC_COMPLETE`。实现者必须在registry里保存显式`event_code -> resulting_state`映射，不能依赖字符串变形猜测。

## Seven版本化命名空间与现有7集合/13唯一索引

Seven在共享逻辑数据库中的集合必须匹配`^seven_[a-z0-9_]+_v[1-9][0-9]*$`：`seven_`前缀提供系统隔离，末尾`_vN`提供物理Schema版本。v2及更高版本仍是Seven隔离命名空间的一部分，不是复用其他业务集合；禁止无版本Seven集合、禁止把既有题海/`system/`集合“视作等价结构”，也禁止原地改写旧版本语义。每个MigrationSpec必须冻结新增/保留/退役集合与索引的精确名称、版本、hash和兼容窗口。

以`seven-system/src/seven_system/database/spec.py`中`seven-database-migration-spec/v1`为当前唯一物理基线。下表是实施者必须使用的首版映射，不是“所有对象随便塞进records”的许可：

| Collection（现有唯一索引） | 允许的对象/语义 | Owner | 敏感度与retention |
|---|---|---|---|
| `seven_records_v1` (`ux_records_type_content_hash`: `record_type+content_hash`; `ux_records_type_logical_revision`: `record_type+logical_id+revision`) | 小型append-only canonical records：Manifest、Capability/Schema/Runtime reports、contracts、registry snapshots、HumanTask/Decision、authorization/consumption receipt、VaultAccessCapability/AccessDecision/AccessEvent/ViewDerivation、RoleQualificationMatrix、Question/Case/Plan/Audit/Evidence/Revision/Verdict、CommitIntent与recovery裁决 | 各domain service经`RecordRepositoryPort` | 只存public/restricted metadata与opaque ref/hash；不存答案blob或raw Vault路径；证据、Gate、permit、access ledger、registry永久保留 |
| `seven_artifact_refs_v1` (`ux_artifact_refs_content_hash`: `content_hash`; `ux_artifact_refs_cas_uri`: `cas_uri`) | CAS/Vault的`ArtifactRef/ArtifactSeal`与不含正文的access metadata | Artifact/Vault service | restricted metadata；实体生命周期内保留，Evidence可达对象不得GC |
| `seven_work_events_v1` (`ux_work_events_event_id`: `event_id`; `ux_work_events_aggregate_sequence`: `aggregate_id+event_sequence`) | 所有canonical `WorkEvent`，包含permit reserve/consume、Gate、reconcile与commit事件 | Runtime EventStore | restricted metadata；append-only永久保留 |
| `seven_work_items_v1` (`ux_work_items_stage_idempotency`: `stage+idempotency_key`; sparse `ux_work_items_execution_attempt`: `execution_attempt_id`) | WorkItem的可CAS更新当前投影，不是历史真值 | Runtime Scheduler | operational metadata；Epoch存续期+审计保留期，历史仍由events重建 |
| `seven_outbox_v1` (`ux_outbox_unique_key`: `outbox_unique_key`; `ux_outbox_aggregate_revision`: `aggregate_id+aggregate_revision+event_type`) | 与业务event同事务生成的投影消息 | Runtime Outbox | operational metadata；ACK后仍保留至Epoch/audit收口 |
| `seven_alerts_v1` (sparse `ux_alerts_dedupe_key`: `dedupe_key`) | 持久AlertRecord和当前处置引用 | Operations/Policy Engine | 可含restricted refs；至少保留到关联Epoch审计完成 |
| `seven_schema_migrations_v1` (`ux_schema_migrations_migration_id`: `migration_id`; `ux_schema_migrations_plan_hash`: `plan_hash`) | bootstrap import anchor、后续Schema plan/action/verify receipts | Database Migration Service | 不含secret；永久保留 |

canonical事务边界只允许：

1. `WorkEvent + WorkItem expected-revision update + OutboxRecord`；
2. CAS final rename前，`CommitIntent + permit reservation + WorkEvent + WorkItem expected-revision update + OutboxRecord`；
3. 在CAS已seal且CommitIntent合法时，`ArtifactRef + terminal/commit WorkEvent + WorkItem update + OutboxRecord + permit consumption`；
4. `HumanGateDecision/Authorization record + WorkEvent + WorkItem update + OutboxRecord`；
5. `AlertRecord + 关联pause/quarantine WorkEvent + OutboxRecord`；
6. Schema migration action/verify receipt的独立fenced transaction。

每个`seven_records_v1`文档必须使用同一物理envelope：`record_type / logical_id / revision / schema_id / schema_version / content_hash / sensitivity / owner_ref / created_at / payload或payload_ref`。`record_type+logical_id+revision`是逻辑身份，`content_hash`是canonical内容身份；`_key`只能是存储层生成的opaque locator，不能承载第二套唯一性协议。其他六个集合也必须由各自JSON Schema规定完整物理字段，不能让repository凭对象类型临时拼字段。

### v1索引充足性裁决与版本化扩展

现有两个`seven_records_v1`索引只能保证内容去重和逻辑版本唯一，不自动保证“permit额度不超支”、“同一permit/action幂等键只消费一次”、“每个gate/task/actor只能作一个有效决定”、“nonce不重放”、“每gate/task唯一封口”或生产查询性能。因此当前7集合/13索引足以承载scaffold、事件/outbox和离线对象，但**不足以解锁生产HumanGate或外部live执行**。

WP-DB1I前必须生成`ObjectPersistenceMapping`与`IndexAdequacyReport`。最低可实施修复是发布`seven-database-migration-spec/v2`，经只读plan、人门和迁移收据增加专用结构：

- `seven_authorization_ledgers_v2`：唯一`permit_id+consumption_ordinal`、唯一`permit_id+action_kind+idempotency_key`、唯一`permit_id+aggregate_revision`，使额度序列化、重放拒绝和expected-revision CAS可由同一事务保证；
- `seven_human_gate_decisions_v2`：唯一`decision_id`、唯一`trust_root_hash+nonce`、唯一`task_id+payload_hash+actor_id`；gate封口仍与对应WorkItem expected-revision update、WorkEvent和Outbox同事务完成。

上述是v2的最低语义要求；最终collection/index名称、sparse属性和迁移hash必须由新版`MigrationSpec`冻结并由`DatabaseSchemaStateReport`核验。若实现者选择等价结构，该结构仍必须使用合法的`seven_*_vN`版本名，并用故障注入证明同样的不变量。禁止用字符串拼接`_key`、先扫描再写、进程内锁、无版本集合或把不同语义硬塞进通用字段伪装原子约束。

## 关键失效规则

下列变化必须使依赖对象失效并生成新版本：

- 题面任意字符变化 → 旧解答、审稿、Verification、QuestionRelease、bare结果、Case角色失效；
- Role prompt/view/tool policy/profile变化 → 旧CapabilityReport不能直接解锁新profile；
- Vault principal/operation/object hash/view hash/sink/policy、issuer key、时窗或revocation状态任一变化 → 旧AccessDecision不能用于新请求，必须以新nonce重裁决；
- Renderer/Selector/TargetSolver版本变化 → 对应efficacy与成本证据需重测；
- MechanismContract核心或boundary变化 → Coverage/Case适用性重新裁决；
- ExperimentPlan任一arm/contrast/停止规则变化 → 旧随机化计划不可继续；
- Schema semantic版本变化 → 旧对象保留，需迁移评估而非静默重写；
- 模型/provider/catalog变化 → 历史收据仍是真实历史，但新运行需revalidation。

## RunArtifactBundle按purpose的条件字段

```yaml
purpose: intake_bare | generated_bare_admission | causal_experiment | cognitive_role
```

- `intake_bare/generated_bare_admission`禁止Tell、Renderer和arm干预字段；
- `causal_experiment`必须引用arm、ExperimentPlan、BranchSnapshot和ResourceContract；
- `cognitive_role`必须引用RoleExecutionContract、RoleInvocationAttempt和AIInvocationReceipt；
- 所有purpose都必须有raw artifact、parser、termination、hash和observability状态。

## Semantic verifier最低职责

1. Schema版本与对象类型匹配；
2. 父ID/hash存在且类型正确；
3. 状态跃迁合法；
4. 时间/sequence/attempt/fence关系一致；
5. 敏感对象只引用允许的sink；
6. required CapabilityReport精确绑定本job profile；
7. Gate签名覆盖真实payload hash；
8. 题面/计划/模型变更触发失效；
9. PASS/claims与实际物证不矛盾；
10. duplicate lineage不会被双计为独立样本；
11. Vault capability、decision、derivation和event的principal/operation/object/view/sink/nonce逐字段相等，签名/issuer/time/revocation均有效，且模型交付中没有raw Vault locator；
12. RoleQualificationMatrix的cell key由Schema规定的全部精确维度重算，集合互斥且`required = pass ∪ not_tested ∪ failed ∪ missing`、`extra = observed - required`、`remainder = not_tested ∪ failed ∪ missing ∪ extra`，计数与verdict一致。
