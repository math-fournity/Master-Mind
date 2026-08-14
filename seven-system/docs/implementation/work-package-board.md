# Seven System 工作包看板

> 本看板只记录状态和下一动作；依赖边必须与[`work-package-dag.v1.json`](work-package-dag.v1.json)机器真值源完全相等，不替代`implementation-status.md`的当前能力事实。

## 状态规则

`owner_type`、`completion_contract`和当前状态分别以canonical DAG、DAG contract和本看板记录，三者不得混成自造状态。implementer-owned普通包最高只能写`READY_FOR_AUDIT`，DOC0同属implementer-owned但交付`DOC_BOOTSTRAP_RECORD`；auditor-owned包拒绝实施者状态命令，只有独立审计路径可以写`AUDITED_*`。上游`READY_FOR_AUDIT`可满足无副作用development dependency，但下游必须记录审计债；真实激活要求适用上游`AUDITED_PASS`，并为每次副作用同时验证父级`ExternalExecutionAuthorization`、不可扩权`LiveRunPermit`和原子`AuthorizationConsumptionReceipt(RESERVED)`。未审canary只能在这条完整授权链精确覆盖时运行并标记`UNAUDITED_AUTHORIZED_CANARY`，不能获得正式PASS。

| 工作包 | 当前状态 | Development依赖 | Activation依赖 | 下一动作 |
|---|---|---|---|---|
| WP-DOC0 | `READY_FOR_AUDIT` | 无 | 无 | 已生成[`DOC_BOOTSTRAP_RECORD`](evidence/wp-doc0/doc-bootstrap-completion-record-8b5e9c92fd8b.json)，等待repo外独立审计；不生成ImplementationBundle |
| WP-GV0 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-DOC0 | WP-DOC0 | 代码+测试完成（51 GV0 + 109 全量回归 PASS），但自托管 ImplementationCompletionBundle BLOCKED（需D盘写授权EEA/Permit/RESERVED）；WorkPackagePlan schema-validity BLOCKED（需NormativeRequirementReviewRecord）；状态为 IMPLEMENTED_PENDING_EVIDENCE，不是 READY_FOR_AUDIT |
| WP-VLT0 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-GV0 | WP-GV0 | 代码+测试完成（91 VLT0测试 PASS），复用GV0 CAS核心扩展Vault/view/seal/reconcile；自托管Bundle BLOCKED（同GV0阻塞） |
| WP-HG0 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-GV0、WP-VLT0 | WP-GV0、WP-VLT0 | 代码+测试完成（58 HG0测试 PASS），HumanTask/HumanGate/KeyLifecycle/ActorRoster，消费GV0验证器；自托管Bundle BLOCKED |
| WP-CW0 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-GV0、WP-VLT0 | WP-GV0、WP-VLT0 | 代码+测试完成（82 CW0测试 PASS），ModelRolePort+fake adapter+11 frozen roles+attempt/reconcile；自托管Bundle BLOCKED |
| WP-CW-D1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-CW0 | WP-CW0、WP-VLT0、WP-HG0、WP-DB1I、WP-RT1 | 代码+测试完成（Devin adapter profile+ATIF parser+bypass tests）；live canary BLOCKED（等待DB1I/RT1/VLT0/HG0激活） |
| WP-CW-C1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-CW0 | WP-CW0、WP-VLT0、WP-HG0、WP-DB1I、WP-RT1 | 代码+测试完成（Codex adapter profile+JSONL parser+bypass tests）；live canary BLOCKED（等待DB1I/RT1/VLT0/HG0激活） |
| WP-QA0 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-HG0、WP-CW-D1、WP-CW-C1 | WP-VLT0、WP-HG0、WP-DB1I、WP-RT1、WP-CW-D1、WP-CW-C1 | 代码+测试完成（96 QA0测试 PASS），P3A状态链/MechanismContract/QuestionDraft/QuestionRelease/Bakeoff-A盲评/InvalidationPropagation；自托管Bundle BLOCKED（同GV0阻塞） |
| WP-DB1L | `IMPLEMENTED_PENDING_EVIDENCE` | WP-GV0 | WP-GV0、WP-HG0 | 代码+测试完成（62 DB1L测试 PASS），逻辑站点v2只读report/verifier，零写入收据；自托管Bundle BLOCKED（同GV0阻塞） |
| WP-DB1I | `IMPLEMENTED_PENDING_EVIDENCE` | WP-DB1L、WP-HG0、WP-VLT0 | WP-DB1L、WP-HG0、WP-VLT0 | 代码+测试完成（53 DB1I测试 PASS），SchemaBootstrapPlan+fenced apply/verify/resume+DVolumeLedger backend+SchemaStateReport/Receipt/ImportAnchor；自托管Bundle BLOCKED |
| WP-RT1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-DB1I、WP-VLT0 | WP-DB1I、WP-VLT0、WP-HG0 | 代码+测试完成（113 RT1测试 PASS，commit 47bdf49），WorkEvent/LeaseFence/Outbox/CommitIntent/DBReservationBackend/RuntimeReconciler/RedisProjection/Checkpoint；自托管Bundle BLOCKED（同GV0阻塞） |
| WP-SV1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-VLT0、WP-RT1 | WP-VLT0、WP-RT1、WP-HG0 | 代码+测试完成（141 SV1测试 PASS），TargetSolverPort/HarnessAdapter/NoToolPolicy/SafeLaunchReport/AnswerIsolationReport/SolverCapabilityReport；自托管Bundle BLOCKED（同GV0阻塞） |
| WP-IN1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-GV0 | WP-GV0 | 代码+测试完成（34 IN1测试 PASS），只读CandidateManifest exporter + duplicate lineage；自托管Bundle BLOCKED（同GV0阻塞） |
| WP-TX1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-IN1、WP-VLT0、WP-RT1、WP-HG0 | WP-IN1、WP-VLT0、WP-RT1、WP-HG0 | 代码+测试完成（134 TX1测试 PASS），TaxonomySnapshot/TellCore/TellFamily/TellHintRelation/TellStrategyRelease/release lineage；自托管Bundle BLOCKED（同GV0阻塞） |
| WP-CW1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-RT1、WP-CW-D1、WP-CW-C1 | WP-RT1、WP-VLT0、WP-HG0、WP-CW-D1、WP-CW-C1 | 代码+测试完成（123 CW1测试 PASS，commit e082c00），RoleQualificationMatrix/ProductionRoleRouter/P3N+P6Workers/IndependenceEnforcer/WorkerCapabilityReport；自托管Bundle BLOCKED（同GV0阻塞） |
| WP-QA1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-QA0、WP-SV1、WP-RT1、WP-HG0 | WP-QA0、WP-VLT0、WP-SV1、WP-RT1、WP-HG0 | 代码+测试完成（98 QA1测试 PASS，commit bb1d83a），P3B bare admission/BareBaseline/BareQualificationResult/Bakeoff-B盲评/BareResultRetention；自托管Bundle BLOCKED（同GV0阻塞） |
| WP-CS1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-IN1、WP-TX1、WP-CW1、WP-HG0、WP-QA1、WP-SV1 | WP-IN1、WP-TX1、WP-CW1、WP-HG0、WP-QA1、WP-SV1 | 代码+测试完成（93 CS1测试 PASS），CasePack/AdmissionDecision/CaseRole/DualEntry/MechanismReview/RelationMapping/P3CVerifier；自托管Bundle BLOCKED（同GV0阻塞） |
| WP-ST1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-TX1、WP-CW1、WP-SV1 | WP-TX1、WP-CW1、WP-SV1、WP-CS1 | 代码+测试完成（105 ST1测试 PASS，commit d122f51），Selector/Renderer/Binder/Injector/Critic/StrategyRuntime/7-arm payload/FixturePreState；自托管Bundle BLOCKED（同GV0阻塞） |
| WP-EX1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-CS1、WP-QA1、WP-SV1、WP-ST1 | WP-CS1、WP-QA1、WP-SV1、WP-ST1、WP-HG0 | 代码+测试完成（93 EX1测试 PASS），ExperimentPlan/ResourceContract/BranchSnapshot/RandomizationPlan/7-arm/P5Runner/RunArtifactBundle；自托管Bundle BLOCKED（同GV0阻塞） |
| WP-AU1 | `NOT_STARTED` | WP-EX1、WP-CW1 | WP-EX1、WP-CW1、WP-VLT0、WP-HG0 | P6三审 |
| WP-EV1 | `NOT_STARTED` | WP-AU1 | WP-AU1 | P7 Evidence |
| WP-RV1 | `NOT_STARTED` | WP-EV1、WP-HG0 | WP-EV1、WP-HG0 | P8 NO_CHANGE/Revision |
| WP-VR1 | `NOT_STARTED` | WP-RV1 | WP-RV1 | P9 Verdict/Replay |
| WP-GA1 | `NOT_STARTED` | WP-VR1 | WP-VR1 | owner=`AUDITOR`；等待repo外AuditAssignment，实施者不得推进 |
| WP-OP1 | `NOT_STARTED` | WP-VR1 | WP-GA1、WP-HG0、WP-RT1、WP-VLT0 | 候选代码可在VR1后开发；真实规模化须GA1审计通过 |

## 当前唯一允许的实施动作

WP-DOC0已基于subject commit `8b5e9c92fd8b05a4811b0c9e8336b3e3dcc0170c`完成机器自检和bootstrap evidence，实施者状态现为`READY_FOR_AUDIT`。这不是独立审计结论，也不解除任何activation gate。

WP-GV0已完成代码和测试开发，实施者状态现为`IMPLEMENTED_PENDING_EVIDENCE`。已实现CompletionContractVerifier、SecurityContractVerifier、ReservationBackendPort、最小D盘CompletionArtifactStore和51项正负向量测试（109项全量回归全PASS）。但自托管ImplementationCompletionBundle被BLOCKED（需D盘写授权EEA/Permit/RESERVED），WorkPackagePlan schema-validity被BLOCKED（需NormativeRequirementReviewRecord）。状态不是`READY_FOR_AUDIT`，因为12号文档明确："未获授权时GV0合法停在IMPLEMENTED_PENDING_EVIDENCE/BLOCKED"。

当前只允许：

- 由repo外owner签发AuditAssignment后，对WP-DOC0执行独立审计；
- 由repo外owner签发AuditAssignment后，独立审查者生成NormativeRequirementReviewRecord，解除GV0 WorkPackagePlan schema-validity阻塞；
- 由repo外owner签发EEA/LiveRunPermit/AuthorizationConsumptionReceipt(RESERVED)后，GV0可生成D盘自托管ImplementationCompletionBundle；
- 按DAG启动WP-VLT0/WP-DB1L/WP-CW0/WP-IN1的无外部副作用development，并显式继承WP-DOC0和WP-GV0的审计债；
- 复验DOC0 subject commit、bootstrap record和测试收据；
- 复验GV0 verifier测试、CompletionArtifactStore和测试执行收据；
- 不得借本轮文档工作实现或调用任何远程模型、DB写入、Redis或Solver。

实施AI下一步可并行启动WP-VLT0/DB1L/CW0/IN1的无副作用开发。在未来独立审计清除审计债之前，不得把任何候选运行或能力写成正式PASS。
