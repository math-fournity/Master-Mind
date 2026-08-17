# Seven System 完整实现入口

> **给谁看**：负责继续实现 Seven System 的 AI，以及未来独立审计该实现的 AI。
> **文档状态**：目标系统的规定性实现说明；它不表示对应代码已经存在。
> **当前事实**：真实实现上限始终以 [`../implementation-status.md`](../implementation-status.md) 为准。

## 一句话结论

从这里开始，按工作包依赖逐项实现；先读canonical DAG的`owner_type`与`completion_contract`，再决定谁可提交哪种完成对象。implementer-owned普通包最高到`READY_FOR_AUDIT`，DOC0是机器化`DOC_BOOTSTRAP_RECORD`例外；auditor-owned包只能由独立审计路径提交`AuditRecord`并写`AUDITED_*`。`READY_FOR_AUDIT`可以满足后续无副作用开发依赖，但必须显式继承审计债；真实DB写入、远程模型、Target Solver、正式HumanGate、canonical P0–P9或科学Evidence仍受激活依赖以及`EEA→LiveRunPermit→原子额度预留`逐次授权链约束。不得把“能 import”写成“系统已可运行”。

## 先理解两条执行面

Devin CLI 可以承担两种完全不同的职责，但两种职责不能混用物理执行面：

```text
TargetSolverPort
└── DevinSolverAdapter
    └── solver_harness
        └── no-tool Target Solver

ModelRolePort
├── DevinCliModelRoleAdapter
│   └── requested model UID = glm-5-2
│       normalized effort = high
└── CodexExecModelRoleAdapter
    └── qualified Codex profile
```

- 只有目标 Solver 作业可以进入 `solver_harness`。
- Devin CLI 并不专属于 Solver；它可以经 `ModelRolePort`执行出题、编辑、核验、Judge 和 Auditor。
- 同为 Devin，也必须使用不同 adapter、workspace、session、配置、权限、输入 view、artifact sink、能力报告和资源池。
- Codex 与 Devin 是并列候选载体。每个角色可以选择任一已经通过该角色精确 profile 能力门的 adapter。
- dispatch 后不能因为答案不好、超时或失败而悄悄切换载体；跨载体重跑是新的 attempt 和新的实验条件。

## 实施 AI 的固定阅读顺序

1. 仓库根 `AGENTS.md` 与 `seven-system/AGENTS.md`。
2. [`../implementation-status.md`](../implementation-status.md)，确认当前真实上限。
3. [`01-authority-and-status.md`](01-authority-and-status.md)，理解真值源和状态权限。
4. [`02-target-state-and-done.md`](02-target-state-and-done.md)，理解最终完成定义。
5. [`03-work-package-dag.md`](03-work-package-dag.md) 与 [`work-package-board.md`](work-package-board.md)，只领取第一个依赖满足的工作包。
6. 当前工作包涉及的专题规范：对象、端口、存储、安全、恢复、阶段管线。
7. [`10-testing-and-fault-injection.md`](10-testing-and-fault-injection.md) 与对应审计文档。
8. [`11-ai-implementation-runbook.md`](11-ai-implementation-runbook.md)，按固定循环实现、验证、落证据并交接。

## 文档地图

| 文档 | 回答的问题 |
|---|---|
| [01-authority-and-status.md](01-authority-and-status.md) | 哪份文档管目标，哪份文件管当前事实，谁有权改变状态 |
| [02-target-state-and-done.md](02-target-state-and-done.md) | 什么才叫系统真的运行起来，什么仍只是局部完成 |
| [03-work-package-dag.md](03-work-package-dag.md) | 从当前 v0.1.0 到完整系统按什么依赖顺序实现 |
| [04-object-and-schema-catalog.md](04-object-and-schema-catalog.md) | 必须有哪些对象、Schema、父哈希、状态和失效规则 |
| [05-execution-ports-and-carriers.md](05-execution-ports-and-carriers.md) | Solver、Devin认知角色、Codex认知角色和人工任务如何隔离 |
| [06-storage-database-and-eventing.md](06-storage-database-and-eventing.md) | D盘、CAS、Vault、Arango、Redis、outbox和提交如何实现 |
| [07-security-blinding-and-human-gates.md](07-security-blinding-and-human-gates.md) | 答案隔离、最小视图、盲化和人工签名 Gate 如何执行 |
| [08-orchestration-concurrency-and-recovery.md](08-orchestration-concurrency-and-recovery.md) | WorkItem、attempt、lease/fence、并发、停止和恢复如何实现 |
| [09-phase-pipeline-p0-p9.md](09-phase-pipeline-p0-p9.md) | 自然题/生成题如何进入实验，P0–P9如何逐门推进 |
| [10-testing-and-fault-injection.md](10-testing-and-fault-injection.md) | 每层要测什么、哪些攻击必须被拒绝、如何形成测试收据 |
| [11-ai-implementation-runbook.md](11-ai-implementation-runbook.md) | 另一位AI每次开工、改代码、验收、提交和交接的固定动作 |
| [12-completion-evidence-bundle.md](12-completion-evidence-bundle.md) | 每个工作包完成时必须交付哪些可复验物证 |
| [13-operator-cli-and-api.md](13-operator-cli-and-api.md) | 完整系统的目标CLI/API、退出码、幂等和授权语义 |
| [14-evidence-analysis-and-multi-epoch.md](14-evidence-analysis-and-multi-epoch.md) | P6–P9的分歧、估计、缺失、Evidence规则与多Epoch调度 |
| [15-work-package-implementation-contracts.md](15-work-package-implementation-contracts.md) | 每个工作包的输入、对象、blocker、物证和停止条件 |
| [requirements-traceability.md](requirements-traceability.md) | 需求ID如何反查设计、Schema、代码、测试、运行证据和审计项 |
| [normative-requirement-index.v1.json](normative-requirement-index.v1.json) / [Schema](normative-requirement-index.v1.schema.json) / [Review Schema](normative-requirement-review-record.v1.schema.json) | 当前规定性Markdown中的局部MUST逐条枚举、source hash、需求族分类和未来独立语义复核 |
| [work-package-board.md](work-package-board.md) | 当前只允许做哪个工作包，哪些仍被依赖阻塞 |
| [work-package-dag.v1.json](work-package-dag.v1.json) / [Schema](work-package-dag.v1.schema.json) | 工作包依赖边的唯一机器真值源及其形状合同 |
| [wp-doc0-plan.v1.json](wp-doc0-plan.v1.json) / [Plan Schema](work-package-plan.v1.schema.json) | 本文档工作包的冻结范围、零副作用预算和bootstrap偏差记录 |
| [analysis-golden-vectors.v1.json](analysis-golden-vectors.v1.json) | P6–P9估计、缺失、duplicate和Holm的可执行参考向量 |
| [RoleQualificationMatrix Schema](role-qualification-matrix.v1.schema.json) | 精确冻结role/carrier/model/profile/view/policy/adapter/capability cell及required/pass/not-tested/failed/extra remainder |
| [VaultAccessCapability Schema](vault-access-capability.v1.schema.json) / [AccessDecision Schema](access-decision.v1.schema.json) / [ViewDerivation Schema](view-derivation.v1.schema.json) / [AccessEvent Schema](access-event.v1.schema.json) | deny-by-default、可撤销、带签名的Vault访问与最小view派生链；模型不得得到raw Vault路径 |
| [ExternalExecutionAuthorization Schema](external-execution-authorization.v1.schema.json) / [LiveRunPermit Schema](live-run-permit.v1.schema.json) / [AuthorizationConsumptionReceipt Schema](authorization-consumption-receipt.v1.schema.json) | 外部副作用的父级上限、不可扩权单次许可和原子额度状态链 |
| [AuditAssignment Schema](audit-assignment.v1.schema.json) / [AuditRecord Schema](audit-record.v1.schema.json) | repo外owner指派、独立审计者attestation、四轴结论和HumanGate验收前零状态效力 |
| [AuditInputPack Schema](audit-input-pack.v1.schema.json) / [AuditReadinessReport Schema](audit-readiness-report.v1.schema.json) | 实施者可准备的只读审计输入候选包与覆盖报告；只机械检查候选完成物证和缺口，不签发assignment、不生成record、不改变状态 |
| [DatabaseLogicalSiteCapabilityReport Schema](database-logical-site-capability-report.v1.schema.json) | WP-DB1L只读逻辑站点报告对象；fixture/验证器可零DB测试，真实`environment-readonly`路径仍须显式调用和只读DB确认 |
| [ImplementationCompletionBundle Schema](implementation-completion-bundle.v1.schema.json) / [OperatorCommandRegistry Schema](operator-command-registry.v1.schema.json) | 实施物证完成包与CLI/API/worker入口的副作用、授权、幂等和receipt总登记 |
| [DocBootstrapCompletionRecord Schema](doc-bootstrap-completion-record.v1.schema.json) / [DocBootstrapImportAnchor Schema](doc-bootstrap-import-anchor.v1.schema.json) | `WP-DOC0 → DOC_BOOTSTRAP_RECORD`的唯一机器完成对象，以及VLT0后的逐字节CAS导入锚 |
| [DocContractVerificationReceipt Schema](doc-contract-verification-receipt.v1.schema.json) / [DOC0TestExecutionReceipt Schema](doc0-test-execution-receipt.v1.schema.json) | 文档合同检查器的自验证输出，以及绑定精确subject commit/tree与完整命令输出的DOC0测试执行收据 |
| [requirements-docs.txt](requirements-docs.txt) | DOC0机器检查器的冻结Python依赖；先安装到隔离审计环境，再运行检查器 |
| [tools/verify_doc_contracts.py](tools/verify_doc_contracts.py) | DAG、看板、Mermaid、Schema、计划hash、需求索引、链接和围栏的fail-closed检查 |
| [tools/sync_doc0_plan.py](tools/sync_doc0_plan.py) | 在NormativeRequirementIndex或DAG更新后，确定性同步DOC0 Plan的精确clause集合、source hashes和自哈希；`--check`只读核对 |

关键机器Schema还包括`implementation-completion-bundle`、`audit-assignment`、`audit-record`、`operator-command-registry`、`authoring-bootstrap-input-pack`、`provenance-snapshot`以及DOC0 bootstrap record/import anchor。Vault访问四对象与RoleQualificationMatrix当前也只是目标机器合同，不是已实现能力或PASS报告。Markdown字段示例与这些Schema冲突时，先停机修规范，不能任取其一。

canonical completion contract只有三种：`WP-DOC0 → DOC_BOOTSTRAP_RECORD`，普通implementer-owned包→`IMPLEMENTATION_BUNDLE`，auditor-owned包→`AUDIT_RECORD`。`owner_type`、`completion_contract`和`state`必须分别读取；例如GA1当前可以是`NOT_STARTED`且owner为`AUDITOR`，不得把二者拼成自造状态。DOC0之后第一个实施包是WP-GV0，它唯一拥有`SecurityContractVerifier/CompletionContractVerifier`公共核心，并复用、硬化v0.1 artifact store为最小CompletionArtifactStore以自托管首个普通Bundle；未完成GV0前不得接受任何普通工作包完成对象。

未来独立审计从 [`../audit/README.md`](../audit/README.md) 开始。架构裁决见 [`../decisions/`](../decisions/)。

## 实施状态机

```text
NOT_STARTED
→ READY
→ IN_PROGRESS
→ IMPLEMENTED_PENDING_EVIDENCE
→ READY_FOR_AUDIT
→ AUDITED_PASS | AUDITED_PARTIAL | AUDITED_FAIL | BLOCKED
```

权限规则：

- 实施者可以写到 `READY_FOR_AUDIT`，不能给自己的工作包写 `AUDITED_PASS`。
- 审计者不得顺手修代码后继续签 PASS；发现问题应形成 Finding，退回新的修订 attempt。
- 人工批准、真实数据库写入、付费模型调用、生产 Solver 和 active release 切换仍需对应授权，不能由“实现全部系统”的泛化目标替代。
- `BLOCKED`、负结果和失败物证必须保留；不能为了推进看板而改写历史状态。

## 另一位 AI 的执行算法

```text
读取硬约束与当前状态
→ 选择第一个 READY 工作包
→ 冻结 requirement/spec/input hashes
→ 先写 blocker/negative tests
→ 实现最小闭环
→ 运行 unit/component/integration/fault tests
→ 用build-work-package-plan绑定已签NormativeRequirementReviewRecord并机械派生普通WorkPackagePlan（DOC0/GA1除外）
→ 按DAG生成DocBootstrapCompletionRecord、ImplementationCompletionBundle或AuditRecord
→ 更新 implementation-status 与看板为 READY_FOR_AUDIT
→ 显式路径提交
→ 在development dependency满足时继续无副作用实现
→ 在activation dependency、授权或阻塞Gate处停止
```

不能用以下替代品跳步：

- 设计文档替代代码；
- Schema 文件替代 semantic verifier；
- 单元测试替代真实能力报告；
- requested model 替代 effective/observed profile；
- 一次成功输出替代幂等、恢复和负向测试；
- 实施者自写的总结替代独立审计。

## 最终停止条件

实施AI在明确的外部副作用授权下完成一条真实candidate run、封存全部物证但尚未接受独立审计时，只能写`SYSTEM_CANDIDATE_READY_FOR_EXTERNAL_AUDIT`。只有同时满足以下条件，独立审计者才能把首个正式目标状态写为`FACTORY_GOLDEN_SLICE_AUDITED`：

1. D盘 CAS/Vault、逻辑DB Schema、事件账和人工 Gate 实际可用；
2. Devin `glm-5-2` High 与 Codex 两个 `ModelRolePort` adapter 均有精确 profile 能力报告；
3. Devin Target Solver 只能经 Harness 且 NoTool 能力真实 PASS；
4. 至少一条自然题路径和一条受控生成题路径完成；
5. 至少一个冻结 Case 从 P4 实验走到 P9 Verdict；
6. Process/Proof/Leakage 三审物理隔离并分别 seal；
7. 发生一次受控崩溃后可以 reconcile/resume，且没有重复科学样本；
8. EvidenceIndex 可以从结论反查全部输入、调用、artifact、Gate和contrast，`remainder=0`；
9. 独立审计输出 PASS。

生产规模并发、长期 soak、Redis重建、backpressure和多Epoch持续学习属于更高的 `PRODUCTION_SCALE_AUDITED`，不能由首条 golden slice 自动推出。
