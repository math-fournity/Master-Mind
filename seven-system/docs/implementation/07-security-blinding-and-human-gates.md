# 安全、答案隔离、盲化与人工Gate

## 一句话结论

每个角色只看到完成职责所需的最小view；敏感内容进入Vault；人工Gate由可验签的人类决定。模型很聪明不是给它更多权限的理由。

## 角色最小视图

| 角色 | 可以看到 | 永久不能看到 |
|---|---|---|
| Question Architect | MechanismContract、CoverageCell、AuthoringBrief | 未来holdout结果、Devin准入结果 |
| Adversarial Editor | public statement | candidate solution、作者scratch、Tell实验结果 |
| Math Verifier | statement、candidate solution、Verification规则 | 作者scratch、Devin结果、其他review结论 |
| Target Solver | QuestionRelease、该arm允许的Hint/lineage | 答案、Tell库、其他arm、Vault |
| Process Auditor | 题面、盲化trajectory、process contract | 答案、真实arm、Hint文本、Proof结论 |
| Proof Judge | 题面、final proof、最小Verification view | Tell、arm、完整thinking、其他审计结论 |
| Leakage Auditor | Solver实际payload、访问记录、最小solution view | Process/Proof结论和实验解释 |
| Selector/Renderer | 允许的pre-state和Tell元数据 | sealed solution、post-outcome |

所有可能复述解答的request/raw event/output都按`solution_bearing`处理，不能只保护输入而把Judge输出写进普通日志。

## 三种独立性

`ReviewIndependenceRecord`分开记录：

- context relation；
- model relation；
- provider/carrier relation；
- reviewer kind（AI/human/formal组合）；
- 是否在其他review公开前seal。

同一个Devin GLM fresh session只算context-independent；同模型通过Codex/Devin不同carrier也不自动算model-independent。

## Blinding Broker

纯程序Broker：

1. 从sealed source生成view；
2. 分配masked run IDs和随机arm代号；
3. 记录source/view hash和derivation rule；
4. 不做数学或因果判断；
5. 审计报告seal后才将masked IDs映回真实arm；
6. blind breach产生协议无效，不由人事后“忽略”。

## HumanTask与HumanGate

HumanTask包含：gate type、payload ref/hash、允许view、截止时间、eligible actor roles、separation policy、required signatures。

HumanGateDecision至少包含：

```yaml
decision_id:
task_id:
gate_type:
payload_hash:
actor_id_and_role:
decision: APPROVE | REJECT | REQUEST_CHANGES | QUARANTINE
reason_codes: []
signed_at:
signature_method_and_key_id:
signature:
separation_evidence_refs: []
verification_status:
```

禁止：

- ModelRole adapter调用决定接口；
- 作者批准自己的QuestionRelease；
- proposal生成器独自批准promotion；
- 超时默认通过；
- 签名覆盖摘要而非完整payload hash；
- 修改payload后沿用旧签名；
- 通用管理员身份绕过roster和separation。

### HumanGate信任根与canonical签名

`signature`字段本身不是信任。每个Epoch必须在RuntimeManifest冻结`HumanGateTrustRootSnapshot`、`ActorRoster`、`HumanGatePolicy`、`SignatureAlgorithmRegistry`和`GateTimePolicy`的hash。

v1签名输入固定为：

```text
UTF8("seven-human-gate-decision/v1\0")
|| canonical_json(unsigned_decision_envelope)
```

`canonical_json`固定为RFC 8785 JCS的UTF-8 bytes（无BOM）；Schema拒绝JCS不能无歧义表示的值。`unsigned_decision_envelope`是完整Decision对象移除`signature`、`verification_status`和自引用hash后的对象；包含`schema_id/schema_version/decision_id/task_id/canonical gate_type/payload ref+hash/actor ID+role/key ID/signature algorithm/decision/reason codes/nonce/issued_at/expires_at/policy+roster+trust-root+algorithm-registry hashes/separation evidence`。不得签一段人类摘要、文件名、URL或可被替换的间接指针。canonicalizer profile和实际signed-bytes hash必须记入Decision，但signed-bytes hash不进入它自身的签名输入。

`SignatureAlgorithmRegistry v1`只允许`Ed25519`。增加算法必须发布新registry版本、ADR、测试向量和HumanGateReadinessReport；禁止根据签名对象自报的algorithm动态选择verifier。

### 安全对象的统一签名字节

用户看到的“签过名”必须能还原成唯一一串bytes。AuditAssignment、AuditRecord、ExternalExecutionAuthorization和LiveRunPermit都使用`RFC8785_JCS_UTF8`；Ed25519 public key固定为32-byte raw key的标准Base64，signature固定为64-byte signature的标准Base64。Schema中的`signature_domain`含实际NUL byte，不是两个字符`\`和`0`。

| 对象 | domain separator | 生成unsigned对象时置为`null`的字段 |
|---|---|---|
| AuditAssignment | `seven-audit-assignment/v1\0` | `signature_envelope.signature_b64`、envelope及顶层`signed_bytes_hash`、`assignment_hash` |
| AuditRecord | `seven-audit-record/v1\0` | `signature_envelope.signature_b64`、envelope及顶层`signed_bytes_hash`、`audit_record_hash` |
| ExternalExecutionAuthorization | `seven-external-execution-authorization/v1\0` | `signature_envelope.signature_b64`、envelope及顶层`signed_bytes_hash`、`authorization_hash` |
| LiveRunPermit | `seven-live-run-permit/v1\0` | `signature_envelope.signature_b64`、envelope及顶层`signed_bytes_hash`、`permit_hash` |
| AuthorizationConsumptionReceipt service attestation | `seven-authorization-consumption-receipt/v1\0` | `service_attestation.signature_b64`、envelope及顶层`attested_bytes_hash`、`receipt_hash` |
| VaultAccessCapability | `seven-vault-access-capability/v1\0` | `signature_envelope.signature_b64`、envelope及顶层`signed_bytes_hash`、`capability_hash` |
| AccessDecision | `seven-access-decision/v1\0` | `signature_envelope.signature_b64`、envelope及顶层`signed_bytes_hash`、`decision_hash` |
| ViewDerivation | `seven-view-derivation/v1\0` | `signature_envelope.signature_b64`、envelope及顶层`signed_bytes_hash`、`derivation_hash` |
| AccessEvent | `seven-access-event/v1\0` | `signature_envelope.signature_b64`、envelope及顶层`signed_bytes_hash`、`event_hash` |
| RoleQualificationMatrix | `seven-role-qualification-matrix/v1\0` | `signature_envelope.signature_b64`、envelope及顶层`signed_bytes_hash`、`matrix_hash` |

统一算法是`UTF8(domain) || JCS(unsigned_object)`；只把表中值置null，不移除整个envelope，因此algorithm、key、signer以及该对象适用的root/roster/policy/key-registry仍被签名覆盖。Schema中的`signed_bytes_hash/attested_bytes_hash`是这串bytes的SHA-256。签名写入后，再将对象自身hash字段视为`null`计算最终对象hash；对象Schema中的`*_hash_algorithm`常量是唯一允许的最终hash算法。Schema先用pattern固定UTC `Z`形式；semantic verifier还必须使用`requirements-docs.txt`固定的RFC 3339 validator或独立严格parser，并额外验证`issued_at <= not_before < expires_at`、真实日历日期、当前可信时间、clock skew、nonce/replay、key有效期/撤销以及envelope内外hash完全相等。某些JSON Schema库会在checker未安装时静默忽略`format`，所以能力测试必须先用`not-a-date`和不存在的日历日期负向探针证明时间检查实际生效。只验证字符串长度不算验签。

Vault四对象与RoleQualificationMatrix不得再签调用者自报的摘要。它们必须携带repo外钉住的trust-root、issuer key registry ref/hash、固定canonicalizer/domain、顶层signed-bytes hash和上述完整envelope；verifier从外部root解析允许key，比较对象issuer、envelope signer/key、registry hash与RuntimeManifest，再重建唯一payload。任一对象只验证`signed_payload_sha256`式自报字段、允许调用者替换key registry，或无法逐字节重建payload时立即BLOCK。

Vault principal机器形状对两条Devin执行面作硬区分：`MODEL_ROLE`必须绑定role、carrier profile和execution attempt，并把TargetSolver contract置null；`TARGET_SOLVER`必须绑定精确TargetSolver contract和execution attempt，并把role/carrier字段置null。TargetSolver对`READ_DERIVED_VIEW/DERIVE_VIEW`只能读取`PUBLIC/RESTRICTED`对象，永远不能读取`SOLUTION_BEARING/HOLDOUT_BEARING`；其写入/封存只能进入restricted Vault/CAS sink。`ViewDerivation.model_delivery`不再重复保存可被替换的view ID/hash，只声明`TOP_LEVEL_DERIVED_VIEW`，实际交付必须直接使用顶层`derived_view`。AccessDecision还必须保存独立的`access_policy=PASS|FAIL|UNKNOWN`检查，UNKNOWN不得ALLOW。

RoleQualificationMatrix中没有CapabilityReport的精确cell统一写`NOT_TESTED`；`NOT_QUALIFIED`不是v1机器状态，不能出现在matrix、completeness或路由结果中。只有带外部信任根、可重建签名且semantic completeness为0的`PASS` cell才可路由。

`HumanGateKeyRecord`至少包含`key_id`、public-key bytes/hash、actor ID、eligible roles、valid-from/to、status、provisioning decision/ref、rotation predecessor和revocation refs。私钥不得进Git、Arango、Redis、普通D盘artifact或模型workspace，只能由经批准的用户持有keystore/signing agent保管。模型或实施者能写入一个看似Base64的字符串，不等于拥有有效签名。

初始信任根不能由Seven“自己签自己”创建。首个`HumanGateTrustRootSnapshot`必须由用户/站点owner在模型不可达的out-of-band ceremony中明确钉住public keys、actor IDs、roles和root hash，生成`TrustRootBootstrapReceipt`，并将该hash写入当次RuntimeManifest。无该收据、收据与root hash不符或owner未确认时，HumanGate readiness为`BLOCKED`。后续root更新必须由旧root下已授权的独立actor签发，或走预先冻结的disaster-recovery ceremony。

被审repo、数据库、CompletionBundle和运行时配置都不是信任根的独立来源。站点owner在签发`AuditAssignment`时写入预先钉住的root hash和repo外渠道标识；独立审计者再从该owner渠道自行观察root，把观察来源、时间和hash写入`AuditRecord`并与assignment及RuntimeManifest三方比较。只在被审对象内部看到彼此自洽的root、roster和bootstrap receipt不能通过验签readiness。外部pin缺失、三方不一致或无法确认来源时，审计只能`BLOCKED`。

密钥生命周期：

1. **Provision**：独立provisioning actor将public key与actor/role绑定，产生append-only KeyRecord和信任根更新决定；不得由待审对象的作者自我授权。
2. **Rotate**：新key建立新Record并引用predecessor；旧key保留以验证历史签名，不原地改public key。
3. **Revoke**：`KeyRevocationRecord`记录effective time、reason、scope和是否因compromise追溯作废。effective time后的签名必须拒绝；需追溯作废时，所有受影响Gate转`QUARANTINED`并重评下游证据。
4. **Expire**：签名接受时同时检查key、task、payload和permit的有效期。`HumanGateReadinessReport`必须冻结time source、最大clock skew与检查收据；时间不可信时Gate保持`HUMAN_PENDING/BLOCKED`。

每个HumanTask payload version使用唯一、不可预测`nonce`。`decision_id + task_id + gate_type + payload_hash + actor_id + nonce`必须在replay store中去重；任一签名换task/gate/payload/actor重放都拒绝。同一actor对同一task version只能有一个有效decision。

冲突处理不由“最后写入者”决定：

- 单签Gate以第一个通过CAS接受的有效Decision封口，后续Decision作为conflict evidence拒绝；
- 多签Gate按冻结policy累积不同actor的APPROVE；达到quorum前仍是`HUMAN_PENDING`；
- `REJECT/QUARANTINE`的优先级与是否立即封口必须由gate-type policy预先冻结，不能在冲突后人工挑有利结果；
- `REQUEST_CHANGES`关闭当前payload version，修改后必须创建新task/nonce；
- 两个都自称terminal且无法由冻结policy唯一裁决时，Gate转`QUARANTINED`。

### ExternalExecutionAuthorization与LiveRunPermit

科学Gate批准题目或Case，不自动授权真实外部副作用。`ExternalExecutionAuthorization`是人类签发的上限；`LiveRunPermit`是针对某个work package/run/epoch的不可扩权子集。二者都使用上述HumanGate信任链，且不得由ModelRole、builder或配置flag自行产生。

机器合同分别是[`external-execution-authorization.v1.schema.json`](external-execution-authorization.v1.schema.json)、[`live-run-permit.v1.schema.json`](live-run-permit.v1.schema.json)和[`authorization-consumption-receipt.v1.schema.json`](authorization-consumption-receipt.v1.schema.json)。三者都`additionalProperties=false`；调用方不能用自定义字段、字符串scope或布尔`--yes`替代规定对象。

```yaml
authorization_or_permit_id:
parent_authorization_ref_and_hash:  # ExternalExecutionAuthorization时可N/A
wp_id / epoch_id / run_id:
authorization_action_registry_ref_and_hash:
action_scopes_or_units: []         # 每项绑定canonical action registry entry
scope_id / scope_hash:             # EEA每个scope唯一；Permit逐unit精确反指
target_site_and_database_hash:
allowed_carrier_profile_hashes: []
allowed_role_or_solver_contract_hashes: []
allowed_input_hashes_and_sensitivity: []
required_output_sink_and_acl_hash:
database_plan_hash_and_max_writes:
redis_namespace_and_max_writes:
max_invocations_by_profile: {}
max_solver_launches:
max_tokens / max_cost / currency:
valid_from / expires_at:
nonce:
revocation_policy_and_refs: []
externally_pinned_trust_root / roster / policy / algorithm_registry:
issuer / key_id / canonicalizer / signature_domain / signed_bytes_hash / signature_envelope:
```

ExternalExecutionAuthorization的每个action scope必须有唯一`scope_id`及按`scope_hash=null`重算的JCS scope hash。LiveRunPermit的每个action unit必须携带`parent_action_scope_id + parent_action_scope_hash`，且对父EEA恰好匹配一个scope；零匹配、多匹配、重复scope ID/hash或ordinal都BLOCK。Permit的任一scope/budget/time/action必须等于或严于该精确parent scope。composition root在建立provider request、Solver launch、DDL、Redis write或active release变更前，必须在同一fenced transaction中预留一份未消耗额度；阶段代码和adapter不能绕过预留直接调用外部系统。

唯一例外是Seven集合尚不存在的首次Schema bootstrap：该时预留/消耗必须作为D盘`SchemaBootstrapLedger`的hash-chained、fsync后entry写入，并在`seven_schema_migrations_v1`可用后按原hash导入和锚定。它不允许放宽scope、超额或绕过HumanGate信任链。

首次bootstrap时数据库replay store也尚不存在；对应HumanTask/Decision nonce、ExternalExecutionAuthorization nonce、permit ordinal和consumption idempotency key必须在同一个D盘bootstrap fence下用atomic-create + hash-chain + fsync去重。任何已有相同nonce/key但payload不同的条目立即QUARANTINE；数据库可用后连同原始bytes/hash导入并由`SchemaBootstrapImportAnchor`证明集合相等。内存set或“本进程没见过”不能算防重放。

`AuthorizationConsumptionReceipt`按对应Schema至少包含authorization/permit ref+hash、精确parent scope ID/hash、consumption ordinal、canonical action registry entry、idempotency key、job/attempt/input/profile/target/sink、expected revision/fence、reservation backend、`RESERVED / CONSUMED / RELEASED_UNUSED / UNKNOWN_START_HELD / QUARANTINED`、reserved unit budget、实际副作用、held/released/remaining allowance、timestamps、前一revision、事务收据、外部root、service attestation key registry、service attestation和receipt hash。

额度语义：

1. 只有能证明provider/副作用未接受、未开始时才可`RELEASED_UNUSED`；
2. accepted/started未知时转`UNKNOWN_START_HELD`，继续占用额度直到reattach/reconcile或人工裁决；
3. retry是新consumption ordinal，必须有剩余额度和合法retry contract；
4. permit过期/撤销后不能新预留；in-flight按冻结revocation policy停止、drain或quarantine；
5. 任何超额、重复ordinal、错profile/input/sink或不匹配fence的调用在进程启动前必须BLOCK。
6. 每个revision都必须逐currency、逐计量维度满足`reserved_unit_budget = actual_side_effects + held_allowance + released_allowance`；`remaining_allowance`是父scope账本在该原子revision后的余额，不能用另一scope或另一currency补平。

状态形状固定为：`RESERVED`和`UNKNOWN_START_HELD`的actual/released全0且held非0；`CONSUMED`的actual非0且held全0；`RELEASED_UNUSED`的actual/held全0且released非0；`QUARANTINED`仍必须满足守恒并按recovery policy决定额度继续held还是进入可证明终局。Schema负责零/非零形状，SecurityContractVerifier负责逐字段加法、currency相等、reserved budget与Permit unit budget完全相等，以及跨revision/父scope总账守恒。

因此任何外部副作用的完整授权谓词都是：

```text
(activation dependencies 已 AUDITED_PASS
 或 parent ExternalExecutionAuthorization 明确允许该次 UNAUDITED_AUTHORIZED_CANARY)
AND ExternalExecutionAuthorization 验签、未撤销、未过期
AND LiveRunPermit 验签且是 parent 的不可扩权子集
AND 对精确 action/job/attempt/input/profile/sink 的额度已原子 RESERVED
```

`ExternalExecutionAuthorization`本身不能被adapter或CLI直接消费。真正执行只消费`LiveRunPermit`的一个ordinal；成功转`CONSUMED`，可证明未开始才可`RELEASED_UNUSED`，启动边界未知则必须`UNKNOWN_START_HELD`。缺任一环即在建立provider request、启动进程或写DB/Redis前BLOCK。

`SecurityContractVerifier`必须按以下固定顺序运行，任一步失败都不能把对象降级成“仅告警”：

1. 对EEA、Permit和Receipt执行各自JSON Schema及format checker；未知字段、未知action code和未知状态直接拒绝；
2. 按本节domain/JCS规则独立重算hash并验证Ed25519、root、roster、policy、key lifecycle、nonce和可信时间；
3. 从EEA逐字段验证Permit是不可扩权子集：每个unit的parent scope ID/hash在EEA中唯一匹配，work package/mode/epoch/run、action registry entry、target、input sensitivity、profile/role/Solver contract、sink/ACL、每类额度、有效期、stop/revocation policy均不得放宽；
4. 验证EEA内scope ID/hash与Permit内`consumption_ordinal`分别唯一，Receipt的parent scope、ordinal/action/job/attempt/input/profile/target/sink/idempotency key与对应action unit完全相等；
5. 在单个expected-revision fenced transaction中创建首个`RESERVED` revision并扣减额度；`state_revision=0`当且仅当previous ref为null，之后每个revision必须`+1`并引用前一receipt hash；只允许`RESERVED→CONSUMED/RELEASED_UNUSED/UNKNOWN_START_HELD/QUARANTINED`以及held后的reconcile终局，禁止覆盖或分叉旧Receipt；
6. `RELEASED_UNUSED`必须有正面“未接受、未开始”物证且actual side effects全为0；`UNKNOWN_START_HELD`继续占用完整未裁决额度；逐revision验证reserved/actual/held/released等式和父scope remaining allowance，任何currency、scope归属或额度不守恒都QUARANTINE；
7. 只有验证通过的`RESERVED` action unit才能交给composition root；adapter只能收到该unit和reservation receipt，不能收到EEA签名对象或未受约束的permit全集。

首次Schema bootstrap只把第5步的事务后端替换为Schema规定的`SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER`；其余六步不变。`seven_*_v1` records/scaffold不能冒充DB v2或等价transactional ledger。

### AuditAssignment与签名AuditRecord

实现者自述“另一个上下文做过审计”不能产生`AUDITED_*`。每次独立审计开始前，站点owner必须在上述信任根下签发不可变`AuditAssignment`，至少绑定：

```yaml
schema_id: seven/audit-assignment
schema_version: 1
assignment_id:
owner_actor_id:
owner_repo_external_channel:
externally_pinned_trust_root:
actor_roster_ref_and_hash:
human_gate_policy_ref_and_hash:
signature_algorithm_registry_ref_and_hash:
subject_commit_and_tree:
completion_bundle_ref_and_hash:
evidence_index_commit_if_any:
auditor_principal_id:
auditor_attestation_public_key:
target_work_package_id:
independence_and_separation_policy_ref_and_hash:
allowed_audit_scope:
required_audit_plan_and_spec_refs_and_hashes:
issued_at / not_before / expires_at / nonce:
canonicalizer_profile / signature_domain / signed_bytes_hash:
signature_envelope:
assignment_hash_algorithm / assignment_hash:
```

`AuditAssignment`执行[`audit-assignment.v1.schema.json`](audit-assignment.v1.schema.json)。它必须把repo外channel、pinned root、roster、policy、algorithm registry、auditor key、subject/bundle/index、separation policy、audit plan/spec、四轴scope和允许的外部动作上限全部放入签名bytes。Assignment即使允许某类外部动作，也仍显式写`requires_separate_external_execution_authorization=true`；它永远不是Permit。

审计者在隔离环境中生成最终`AuditRecord`的unsigned canonical bytes，但模型workspace永远拿不到attestation私钥。`AttestationSignerPort`位于模型和被审repo之外，只接受`assignment_ref + unsigned_record + authenticated_auditor_session_receipt`；它先验证assignment、auditor principal/key、scope、subject tree未变和canonical bytes hash，再调用owner批准的signing agent。返回的只是Schema规定的Ed25519 envelope。Signer不判断finding、不修改verdict，也不能写`AUDITED_*`状态；AI审计者只能请求签署被指派的精确bytes，不能创建assignment、换key或访问私钥。

AuditRecord验签只证明“被指派的审计主体经批准的Signer签过这份记录”。最终把工作包状态切换为`AUDITED_*`还必须由HumanGateService验证：assignment有效、AuditRecord `wp_id`等于assignment的`target_work_package_id`、repo外root observation与assignment/RuntimeManifest三方相等、subject/bundle/index hashes完全相等、审计者未修改被审树、AuditRecord签名有效、四轴finding引用闭合、职责分离成立。`state_transition_effect`固定为`NONE_UNTIL_HUMAN_GATE_SERVICE_ACCEPTS`。

## 两次Revision Gate

1. Pre-evaluation：批准因果诊断、单组件修改、证据分区、candidate hash、acceptance、rollback和一次性holdout token；
2. Post-evaluation：另一独立actor只读sealed evidence，决定PROMOTE/RESTRICT/REJECT/QUARANTINE。

修订前的NO_CHANGE是独立终态；candidate评估后不晋级叫REJECT，不能复用NO_CHANGE混淆holdout是否已消耗。

## 自动化安全边界

自动化可以：验证、去重、运行已批准plan、seal artifact、生成审计草稿、告警、暂停、quarantine、生成恢复计划。

自动化不可以：修改Case角色/endpoint、解封holdout、自批revision、切active pointer、永久收窄/退休、删除负证据、把PARTIAL升级PASS。

紧急动作只能设置可逆runtime kill-switch/quarantine overlay；正式scope或release变化仍需人门。

## 高优先级安全失败

以下任一项立即停止新dispatch：

- 错误数据库或身份不明；
- Vault/答案/holdout泄漏；
- blind breach；
- artifact/hash冲突；
- 重复Solver或重复科学样本；
- 未授权Gate；
- tool/network/view越权；
- D盘丢失或容量tripwire；
- 模型/effort/profile漂移；
- 成本预算不可执行且该成本是Gate/endpoint。
- 无有效LiveRunPermit、permit超额/重放、信任根漂移或签名key已撤销。
