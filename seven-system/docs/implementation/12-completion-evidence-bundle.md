# 工作包完成物证与最终交付包

## 一句话结论

“代码写完了”不是可审计交付。每个工作包必须按canonical DAG的`completion_contract`提交一份绑定spec、源码、Schema、测试、运行收据和nonclaims的完成对象，未来审计者才能知道应该复验什么。普通实施包使用ImplementationCompletionBundle；DOC0使用DocBootstrapCompletionRecord；auditor-owned包使用AuditRecord，三者不得互换。

## ImplementationCompletionBundle

Canonical JSON必须通过[`implementation-completion-bundle.v1.schema.json`](implementation-completion-bundle.v1.schema.json)及跨对象semantic verifier；下列YAML仅是字段导读。

```yaml
schema_id: seven/implementation-completion-bundle
schema_version: 1
bundle_id:
wp_id:
implementation_attempt_id:
status: READY_FOR_AUDIT
baseline:
  commit:
  tree:
implementation_subject:
  commit:
  tree:
spec_refs_and_hashes: []
requirement_coverage:
  - requirement_id:
    normative_clause_ids: []
    code_refs: []
    schema_refs: []
    test_receipts: []
    runtime_evidence_refs: []
    status: COVERED | NOT_APPLICABLE | UNRESOLVED
modified_files: []
schema_ids_and_hashes: []
code_entrypoints: []
state_transitions_implemented: []
test_receipts: []
fault_injection_receipts: []
capability_reports: []
live_run_receipts: []
artifact_refs: []
external_side_effect_counts:
  database_connections:
  database_reads:
  database_writes:
  redis_connections:
  redis_reads:
  redis_writes:
  d_volume_writes:
  model_invocations_by_profile: {}
  solver_launches:
  human_gate_decisions:
claims: []
nonclaims: []
known_limitations: []
protocol_deviations: []
unresolved_findings: []
inherited_audit_debt: []
recovery_notes: []
audit_replay_commands: []
created_at:
creator:
bundle_hash:
```

上述字段名与v1 JSON Schema完全一致；`model_invocations_by_profile`只能使用受限profile key并保存非负整数，其余side-effect count字段固定、未知字段拒绝。实施者不能把status写成AUDITED_PASS。`WP-DOC0`的machine contract是`DOC_BOOTSTRAP_RECORD`，`WP-GA1`的machine contract是`AUDIT_RECORD`；两者都不能套用ImplementationCompletionBundle。单对象v1 Schema对已知GA1作第一层拒绝，状态服务仍必须用下述`CompletionContractVerifier`读取冻结DAG，对DOC0、未来新增节点、旧Schema和伪造对象执行通用拒绝。

## 提交协议：消除commit自引用

CompletionBundle不进入它所绑定的implementation subject tree，采用固定的两次提交/外部物证协议：

1. 在干净工作树上提交工作包代码、Schema、tests和规范，得到不可变`implementation_subject_commit_and_tree_hash`；
2. 在该精确commit上运行收据化测试；若测试需要修代码，产生新的implementation commit并重新开始；
3. 把CompletionBundle作为D盘CAS的append-only外部artifact生成，绑定第1步commit/tree及全部receipt；
4. 可再提交一个只含看板/状态/外部bundle ref+hash的`evidence-index commit`。它不是第1步subject tree的一部分，不能被bundle反向声称为已审实现；
5. AuditRecord同时记录被审implementation subject commit、CompletionBundle hash和可选index commit。

### WP-DOC0的CAS自举例外

canonical DAG对WP-DOC0固定`owner_type=IMPLEMENTER, completion_contract=DOC_BOOTSTRAP_RECORD`。WP-DOC0创建时，提供D盘CAS的WP-VLT0尚未实现且反向依赖DOC0。为避免“DOC0必须先写CAS、CAS又必须先有DOC0”的循环，只有DOC0可使用以下bootstrap协议：

1. 先提交规范、Schema、生成器和测试，形成implementation subject commit；
2. 在该commit上只读复跑DOC0检查；
3. 第二个Git evidence-index commit只增加`DocBootstrapCompletionRecord`、测试收据ref/hash和看板状态，不修改subject规范；
4. 该record明确`LOCAL_GIT_APPEND_ONLY_NOT_CAS`，不能声称WORM、D盘持久化或独立审计；
5. WP-VLT0完成后，把record原始bytes逐字节导入D盘CAS，并生成绑定原hash的`DocBootstrapImportAnchor`。导入失败或bytes变化使VLT0和所有下游activation BLOCK。

第2步的文档合同检查输出必须通过[`doc-contract-verification-receipt.v1.schema.json`](doc-contract-verification-receipt.v1.schema.json)；第3步引用的完整测试执行收据必须通过[`doc0-test-execution-receipt.v1.schema.json`](doc0-test-execution-receipt.v1.schema.json)。前者证明当前文档、DAG、Schema、需求索引和负向向量在冻结环境中一致，后者绑定精确subject commit/tree、依赖锁、完整argv、stdout/stderr hash、测试计数和零副作用计数；两者都不能替代独立审计。

该例外不能用于模型、Solver、数据库、HumanGate、科学Evidence或其他工作包。DOC0即使完成bootstrap record，也只到`READY_FOR_AUDIT`；`AUDITED_*`仍需要owner签发AuditAssignment和独立AuditRecord。

### WP-GV0的D盘自托管顺序

GV0不是第二个Git bootstrap例外。它先以`SIDE_EFFECT_FREE`在隔离fixture中实现最小D盘`CompletionArtifactStore`与两个verifier，提交implementation subject并在该精确subject上复验append-once、原子提交、hash/byte、symlink/fallback和completion-contract正负向量；随后必须取得覆盖精确D盘写入的EEA、LiveRunPermit与原子`RESERVED`，才可使用已经验证的store生成自己的ImplementationCompletionBundle。该bundle仍遵守普通两提交/外部CAS协议并记录D盘写入计数；未获授权时GV0合法停在`IMPLEMENTED_PENDING_EVIDENCE/BLOCKED`。VLT0必须复用这一CAS核心扩展完整Artifact/Vault能力；GV0的最小store不能接收模型/Solver输出、答案或holdout，也不能签CAS/Vault正式CapabilityReport。

ImplementationCompletionBundle中**不得**出现`evidence_index_commit_if_any`：bundle先生成，index commit后生成且引用bundle hash，反向填写会制造不可解的hash环。可选index commit只由后续AuditAssignment/AuditRecord记录。禁止在同一个Git commit内写入“本commit hash”，也禁止生成bundle后修改subject tree而沿用旧bundle。

若下游开发基于尚未独立审计、但已`READY_FOR_AUDIT`的上游包，必须把上游bundle/hash逐项写入`inherited_audit_debt`。审计债不会因为下游测试通过而自动消失；最终系统审计必须沿DAG逐项清零。

## 测试收据要求

每条test receipt绑定：源码树、依赖环境、完整test IDs、命令argv、exit code、stdout/stderr hash、executed/skipped/error数和side effects。复制一行`58 tests OK`不构成收据。

## CapabilityReport要求

报告必须：

- 由受控runner产生，不接受调用者任意evidence文本；
- 绑定实际binary/adapter/source/config/profile/view policy；
- 执行Schema和semantic verifier；
- 列出required checks的完整test IDs；
- 区分requested/effective/unobservable；
- 失败或PARTIAL可合法seal，不能当artifact损坏；
- 有独立verifier和篡改测试；
- 不因catalog/help存在而PASS。

## AuditRecord

独立审计完成后另生成：

`AuditAssignment`和`AuditRecord`分别执行[`audit-assignment.v1.schema.json`](audit-assignment.v1.schema.json)与[`audit-record.v1.schema.json`](audit-record.v1.schema.json)；Markdown示例不能放宽Schema。

```yaml
schema_id: seven/audit-record
schema_version: 1
audit_id:
wp_id:
audit_assignment_ref_and_hash:
assignment_verification_receipt_ref_and_hash:
audited_bundle_ref_and_hash:
audited_subject:
  commit:
  tree:
evidence_index_commit_if_any:
externally_observed_pinned_trust_root:
  trust_root_hash:
  source_channel_id:
  observed_at:
  observation_receipt_ref_and_hash:
runtime_manifest_trust_root_hash:
audit_plan_and_spec_refs_and_hashes: []
auditor_principal_id:
auditor_attestation_key_id:
auditor_attestation_public_key_hash:
auditor_session_attestation_ref_and_hash:
independence_evidence: []
findings:
  - finding_id:
    finding_kind: STATIC | DYNAMIC | FAULT_INJECTION | TRACEABILITY | SECURITY | SCIENTIFIC | SCALE
    severity: P0 | P1 | P2 | P3
    status: OPEN | RESOLVED_BY_AUDITED_SUBJECT | ACCEPTED_SCOPE_LIMIT
    affected_axes: []
    requirement_ids: []
    summary:
    evidence_refs: []
replayed_test_receipts: []
external_execution_receipts: []
traceability_remainder:
orphan_remainder:
claims_confirmed: []
claims_rejected: []
nonclaims_checked: []
axis_verdicts:
  implementation:
    verdict: AUDITED_PASS | AUDITED_PARTIAL | AUDITED_FAIL | BLOCKED | NOT_TESTED
    finding_ids: []
    evidence_refs: []
    scope_reason_if_not_tested:
  factory:
    verdict: AUDITED_PASS | AUDITED_PARTIAL | AUDITED_FAIL | BLOCKED | NOT_TESTED
    finding_ids: []
    evidence_refs: []
    scope_reason_if_not_tested:
  scientific:
    verdict: SUPPORTS | CONTRADICTS | DOES_NOT_SUPPORT | INCONCLUSIVE | NOT_TESTED
    finding_ids: []
    evidence_refs: []
    scope_reason_if_not_tested:
  production_scale:
    verdict: AUDITED_PASS | AUDITED_PARTIAL | AUDITED_FAIL | BLOCKED | NOT_TESTED
    finding_ids: []
    evidence_refs: []
    scope_reason_if_not_tested:
scope_limits: []
followups: []
state_transition_effect: NONE_UNTIL_HUMAN_GATE_SERVICE_ACCEPTS
created_at:
canonicalizer_profile: RFC8785_JCS_UTF8
signature_domain: "seven-audit-record/v1\0"
signed_bytes_hash:
signature_envelope:
  algorithm: Ed25519
  key_id:
  signer_principal_id:
  signature_encoding: base64
  signature_b64:
  signed_bytes_hash:
audit_record_hash_algorithm: sha256(RFC8785-JCS-object-with-audit_record_hash-null)
audit_record_hash:
```

`AuditRecord`必须引用站点owner预先签发的`AuditAssignment`。该assignment绑定repo外channel/root、subject commit/tree、CompletionBundle、可选index commit、审计plan/spec/scope、auditor principal与attestation public key；审计者不能自行创建或扩大assignment。每条finding显式列出受影响轴，四个axis verdict再反向引用finding IDs和evidence refs，禁止一个总分掩盖P0或未测试轴。签名输入、AttestationSignerPort和外部pinned trust-root要求见07号文档。验签通过前只能保存为审计草稿，不能改变工作包状态。

四轴分别计算，不能由一个总分覆盖另一轴的FAIL/BLOCKED。工作包级审计不适用的轴显式写`NOT_TESTED`并给非空scope理由，其他verdict的scope reason必须为null并至少引用一条evidence或finding。每个axis的`finding_ids`必须恰好等于`findings[].affected_axes`包含该轴的相关finding集合；未知、孤儿或漏挂finding使AuditRecord不能验收。`scientific`轴只消费科学Evidence，不从实现测试推导；`production_scale`不能由golden slice自动继承。

审计者若修改代码、Schema、测试、规范或任何subject tree内容，必须终止当前audit，生成新implementation attempt，之后由另一独立审计执行。最终`AUDITED_*`状态跃迁还必须由HumanGateService验证assignment、AuditRecord签名、职责分离和所有绑定hash；实现者或审计AI不能直接写状态。

### CompletionContractVerifier：三合同、owner与状态正交规则

单对象Schema不可能持续知道未来每个`wp_id`在canonical DAG中的owner和completion contract。WP-GV0是`CompletionContractVerifier`公共核心、固定错误码和测试向量的唯一代码所有者；状态服务、HumanGateService和P9/GA1只消费该实现，不得各写局部放宽版。在接受任何完成对象或状态命令前，必须加载并验证`work-package-dag.v1.json`的冻结hash，然后执行：

```text
node = canonical_dag[wp_id]

expected_schema = {
    "DOC_BOOTSTRAP_RECORD": "seven/docs/doc-bootstrap-completion-record",
    "IMPLEMENTATION_BUNDLE": "seven/implementation-completion-bundle",
    "AUDIT_RECORD": "seven/audit-record"
}[node.completion_contract]
require submitted_object.schema_id == expected_schema

if node.owner_type == "IMPLEMENTER":
    require node.completion_contract in {"DOC_BOOTSTRAP_RECORD", "IMPLEMENTATION_BUNDLE"}
    reject every AUDITED_* state command from the implementer

if node.owner_type == "AUDITOR":
    require node.completion_contract == "AUDIT_RECORD"
    reject every ImplementationCompletionBundle and every implementer state command
    require valid AuditAssignment + signed AuditRecord + HumanGateService acceptance
```

`owner_type`、`completion_contract`和工作包`state`是三个正交字段：`NOT_STARTED`可用于implementer-owned或auditor-owned节点；“尚未指派审计者”写在reason/next action，不创造`AUDITOR_OWNED_NOT_ASSIGNED`状态。implementer-owned是通则，不等于一律使用ImplementationBundle——DOC0由machine contract明确使用bootstrap record；auditor-owned也不等于已经审计，只有有效AuditRecord被HumanGateService接受后才能写`AUDITED_*`。

因此DAG Schema必须拒绝owner/contract错配，当前ImplementationCompletionBundle v1 Schema必须直接拒绝已知`WP-GA1`；即便恶意或旧producer绕过单对象校验，DAG-aware verifier仍必须对`WP-DOC0 + ImplementationCompletionBundle`、任一auditor-owned + ImplementationCompletionBundle、implementer命令写auditor节点返回`COMPLETION_CONTRACT_MISMATCH/ACTOR_NOT_AUTHORIZED`，且不得写任何状态。修改DAG hash后，旧CompletionContractVerifier receipt全部失效。

## GoldenSliceCompletionBundle

首条系统纵切还要聚合：

- 全部工作包AuditRecords；
- P0 CapabilityReports与Human readiness；
- RuntimeManifest/ExperimentPlan；
- 自然/生成两条Case lineage；
- Devin/Codex认知调用收据；
- Target Solver arms；
- 三审、RunAudit、EvidenceRecord；
- recovery/fault receipts；
- HumanGate decisions；
- EvidenceIndex、replay report、cost report；
- factory/scientific分轴Verdict；
- explicit validated scope和nonclaims。

系统级聚合包同样存入D盘CAS，并绑定一组精确的工作包subject commits、外部CompletionBundle hashes和AuditRecords；它不要求把自身hash写回任何被绑定commit。

## 物证完整性检查

完成包必须能回答：

1. 每个claim由哪条需求、代码、Schema、测试和运行物证支持？
2. 每次外部调用有没有attempt、accepted/started边界和receipt？
3. 每个artifact是否有source、hash、sink、seal和DB ref？
4. 每个Gate是否有payload hash、actor、签名和职责分离？
5. 每个retry是否属于同一科学sample lineage？
6. 每个planned job是否有terminal归宿？
7. 每个敏感对象是否只有允许view？
8. 每个负结果、BLOCKED和quarantine是否保留？
9. 有没有没有需求来源的代码、没有测试的MUST或没有消费方的Schema？
10. `remainder=0`是否由机器检查而非口头声明？
