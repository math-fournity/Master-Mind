# Seven System 工作包看板

> 本看板只记录状态和下一动作；依赖边必须与[`work-package-dag.v1.json`](work-package-dag.v1.json)机器真值源完全相等，不替代`implementation-status.md`的当前能力事实。

## 状态规则

`owner_type`、`completion_contract`和当前状态分别以canonical DAG、DAG contract和本看板记录，三者不得混成自造状态。implementer-owned普通包最高只能写`READY_FOR_AUDIT`，DOC0同属implementer-owned但交付`DOC_BOOTSTRAP_RECORD`；auditor-owned包拒绝实施者状态命令，只有独立审计路径可以写`AUDITED_*`。上游`READY_FOR_AUDIT`可满足无副作用development dependency，但下游必须记录审计债；真实激活要求适用上游`AUDITED_PASS`，并为每次副作用同时验证父级`ExternalExecutionAuthorization`、不可扩权`LiveRunPermit`和原子`AuthorizationConsumptionReceipt(RESERVED)`。未审canary只能在这条完整授权链精确覆盖时运行并标记`UNAUDITED_AUTHORIZED_CANARY`，不能获得正式PASS。

## 当前状态（R0 整改后，2026-08-14）

| 工作包 | 当前状态 | Development依赖 | Activation依赖 | 下一动作 |
|---|---|---|---|---|
| WP-DOC0 | `IN_PROGRESS` | 无 | 无 | 已生成[`DOC_BOOTSTRAP_RECORD`](evidence/wp-doc0/doc-bootstrap-completion-record-8b5e9c92fd8b.json)，等待repo外独立审计；不生成ImplementationBundle。R1 整改中：DOC0 checker source hash/document hashes/clauses/remainder 漂移已修复，待干净 subject 上重新验证 |
| WP-GV0 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-DOC0 | WP-DOC0 | 代码+测试存在（51 GV0测试），但 CompletionContractVerifier 未执行完整 Schema（P0-A）、HumanGate 无真实 Ed25519 验签（P0-B）、DB1I 授权链可绕过（P0-C）；自托管 Bundle BLOCKED（需D盘写授权EEA/Permit/RESERVED）；WorkPackagePlan schema-validity BLOCKED（需NormativeRequirementReviewRecord）；Plan draft 中 GV0-001/002/003 非法 requirement IDs。状态不是 READY_FOR_AUDIT |
| WP-VLT0 | `NOT_STARTED` | WP-GV0 | WP-GV0 | 既有代码存在（91测试）但越级——GV0 未到 READY_FOR_AUDIT。须新 remediation attempt 重新资格化 |
| WP-HG0 | `NOT_STARTED` | WP-GV0、WP-VLT0 | WP-GV0、WP-VLT0 | 既有代码存在（58测试）但越级。须新 remediation attempt |
| WP-CW0 | `NOT_STARTED` | WP-GV0、WP-VLT0 | WP-GV0、WP-VLT0 | 既有代码存在（82测试）但越级。须新 remediation attempt |
| WP-CW-D1 | `NOT_STARTED` | WP-CW0 | WP-CW0、WP-VLT0、WP-HG0、WP-DB1I、WP-RT1 | 既有代码存在但越级。须新 remediation attempt |
| WP-CW-C1 | `NOT_STARTED` | WP-CW0 | WP-CW0、WP-VLT0、WP-HG0、WP-DB1I、WP-RT1 | 既有代码存在但越级。须新 remediation attempt |
| WP-QA0 | `NOT_STARTED` | WP-HG0、WP-CW-D1、WP-CW-C1 | WP-VLT0、WP-HG0、WP-DB1I、WP-RT1、WP-CW-D1、WP-CW-C1 | 既有代码存在（96测试）但越级。须新 remediation attempt |
| WP-DB1L | `NOT_STARTED` | WP-GV0 | WP-GV0、WP-HG0 | 既有代码存在（62测试）但越级。须新 remediation attempt |
| WP-DB1I | `NOT_STARTED` | WP-DB1L、WP-HG0、WP-VLT0 | WP-DB1L、WP-HG0、WP-VLT0 | 既有代码存在（53测试）但越级，且 P0-C 发现授权链可绕过。须新 remediation attempt |
| WP-RT1 | `NOT_STARTED` | WP-DB1I、WP-VLT0 | WP-DB1I、WP-VLT0、WP-HG0 | 既有代码存在（113测试）但越级。须新 remediation attempt |
| WP-SV1 | `NOT_STARTED` | WP-VLT0、WP-RT1 | WP-VLT0、WP-RT1、WP-HG0 | 既有代码存在（141测试）但越级，DevinSolverAdapter 不存在（只有 FakeHarnessAdapter）。须新 remediation attempt |
| WP-IN1 | `NOT_STARTED` | WP-GV0 | WP-GV0 | 既有代码存在（34测试）但越级。须新 remediation attempt |
| WP-TX1 | `NOT_STARTED` | WP-IN1、WP-VLT0、WP-RT1、WP-HG0 | WP-IN1、WP-VLT0、WP-RT1、WP-HG0 | 既有代码存在（134测试）但越级。须新 remediation attempt |
| WP-CW1 | `NOT_STARTED` | WP-RT1、WP-CW-D1、WP-CW-C1 | WP-RT1、WP-VLT0、WP-HG0、WP-CW-D1、WP-CW-C1 | 既有代码存在（123测试）但越级。须新 remediation attempt |
| WP-QA1 | `NOT_STARTED` | WP-QA0、WP-SV1、WP-RT1、WP-HG0 | WP-QA0、WP-VLT0、WP-SV1、WP-RT1、WP-HG0 | 既有代码存在（98测试）但越级。须新 remediation attempt |
| WP-CS1 | `NOT_STARTED` | WP-IN1、WP-TX1、WP-CW1、WP-HG0、WP-QA1、WP-SV1 | WP-IN1、WP-TX1、WP-CW1、WP-HG0、WP-QA1、WP-SV1 | 既有代码存在（93测试）但越级。须新 remediation attempt |
| WP-ST1 | `NOT_STARTED` | WP-TX1、WP-CW1、WP-SV1 | WP-TX1、WP-CW1、WP-SV1、WP-CS1 | 既有代码存在（105测试）但越级。须新 remediation attempt |
| WP-EX1 | `NOT_STARTED` | WP-CS1、WP-QA1、WP-SV1、WP-ST1 | WP-CS1、WP-QA1、WP-SV1、WP-ST1、WP-HG0 | 既有代码存在（93测试）但越级。须新 remediation attempt |
| WP-AU1 | `NOT_STARTED` | WP-EX1、WP-CW1 | WP-EX1、WP-CW1、WP-VLT0、WP-HG0 | 既有代码存在（114测试）但越级。须新 remediation attempt |
| WP-EV1 | `NOT_STARTED` | WP-AU1 | WP-AU1 | 既有代码存在（98测试）但越级。须新 remediation attempt |
| WP-RV1 | `NOT_STARTED` | WP-EV1、WP-HG0 | WP-EV1、WP-HG0 | 既有代码存在（113测试）但越级。须新 remediation attempt |
| WP-VR1 | `NOT_STARTED` | WP-RV1 | WP-RV1 | 既有代码存在（122测试）但越级。须新 remediation attempt |
| WP-GA1 | `NOT_STARTED` | WP-VR1 | WP-VR1 | owner=`AUDITOR`；等待repo外AuditAssignment，实施者不得推进 |
| WP-OP1 | `NOT_STARTED` | WP-VR1 | WP-GA1、WP-HG0、WP-RT1、WP-VLT0 | 既有代码存在（94测试）但越级。须新 remediation attempt |

## 历史错误状态记录（append-only，不删除）

**审计基线 commit `783d4be` / tree `36148d1f` 时的错误状态**：

以下 22 个工作包曾被上一位实施 AI 标为 `IMPLEMENTED_PENDING_EVIDENCE`，但审计确认其 development dependency 未满足（GV0 仍为 `IMPLEMENTED_PENDING_EVIDENCE`，不是 `READY_FOR_AUDIT`），属于越级启动：

WP-VLT0, WP-HG0, WP-CW0, WP-CW-D1, WP-CW-C1, WP-QA0, WP-DB1L, WP-DB1I, WP-RT1, WP-SV1, WP-IN1, WP-TX1, WP-CW1, WP-QA1, WP-CS1, WP-ST1, WP-EX1, WP-AU1, WP-EV1, WP-RV1, WP-VR1, WP-OP1

既有代码不删除，但视为 `existing unqualified implementation input`。每个包须创建新的 remediation attempt，Plan 中显式记录"既有代码先于有效 Plan 和依赖满足"这一 protocol deviation。不得倒填伪 PREREGISTERED Plan。

审计同时发现三个 P0 Gate 旁路：
- P0-A: CompletionContractVerifier 未执行完整 Schema（空壳 `{"schema_id": "..."}` 可 PASS）
- P0-B: HumanGate 无真实 Ed25519 验签（全A伪签名可 PASS）
- P0-C: DB1I 可绕过 HumanGate 和完整授权链（`human_gate_service=None` 可执行 fake DDL）

## 当前唯一允许的实施动作

WP-DOC0 已基于 subject commit `8b5e9c92fd8b05a4811b0c9e8336b3e3dcc0170c`完成机器自检和 bootstrap evidence，实施者状态现为 `READY_FOR_AUDIT`。这不是独立审计结论，也不解除任何 activation gate。DOC0 checker 当前 FAIL，须 R1 修复 source hash/document hashes/clauses/remainder 漂移。

WP-GV0 既有代码和测试存在，实施者状态现为 `IMPLEMENTED_PENDING_EVIDENCE`。但 P0-A/B/C 三个 Gate 旁路必须先修复，且 WorkPackagePlan schema-validity BLOCKED（需 NormativeRequirementReviewRecord），自托管 Bundle BLOCKED（需 D 盘写授权）。状态不是 `READY_FOR_AUDIT`。

当前只允许：

- R0：冻结基线、纠正过度状态声明（本节已完成）；
- R1：修复 DOC0 checker 的 source hash/document hashes/clauses/remainder 漂移，使 doc checker 在干净 subject 上 PASS；
- 修复 P0-A/B/C 三个 Gate 旁路（先写负向测试复现旁路，再修代码）；
- 由 repo外 owner 签发 AuditAssignment 后，对 WP-DOC0 执行独立审计；
- 由 repo外 owner 签发 AuditAssignment 后，独立审查者生成 NormativeRequirementReviewRecord，解除 GV0 WorkPackagePlan schema-validity 阻塞；
- 由 repo外 owner 签发 EEA/LiveRunPermit/AuthorizationConsumptionReceipt(RESERVED) 后，GV0 可生成 D 盘自托管 ImplementationCompletionBundle；
- **不得**在 GV0 达到 READY_FOR_AUDIT 前启动任何下游包的 development；
- 复验 DOC0 subject commit、bootstrap record 和测试收据；
- 复验 GV0 verifier 测试、CompletionArtifactStore 和测试执行收据；
- 不得借本轮文档工作实现或调用任何远程模型、DB写入、Redis或Solver。

在未来独立审计清除审计债之前，不得把任何候选运行或能力写成正式 PASS。
