# Seven System 工作包看板

> 本看板只记录状态和下一动作；依赖边必须与[`work-package-dag.v1.json`](work-package-dag.v1.json)机器真值源完全相等，不替代`implementation-status.md`的当前能力事实。

## 状态规则

`owner_type`、`completion_contract`和当前状态分别以canonical DAG、DAG contract和本看板记录，三者不得混成自造状态。implementer-owned普通包最高只能写`READY_FOR_AUDIT`，DOC0同属implementer-owned但交付`DOC_BOOTSTRAP_RECORD`；auditor-owned包拒绝实施者状态命令，只有独立审计路径可以写`AUDITED_*`。上游`READY_FOR_AUDIT`可满足无副作用development dependency，但下游必须记录审计债；真实激活要求适用上游`AUDITED_PASS`，并为每次副作用同时验证父级`ExternalExecutionAuthorization`、不可扩权`LiveRunPermit`和原子`AuthorizationConsumptionReceipt(RESERVED)`。未审canary只能在这条完整授权链精确覆盖时运行并标记`UNAUDITED_AUTHORIZED_CANARY`，不能获得正式PASS。

## 当前状态（R2 亲自整改后，2026-08-14）

本节取代下方历史错误状态。当前事实以本节和[`../implementation-status.md`](../implementation-status.md)为准。

- 文档合同检查、P0-B、P0-C、DB1I、R5、全量`seven-system/tests`和`git diff --check`均已在当前工作树通过。
- 该结论只支持`side-effect-free implementer-owned development regression = PASS`，不支持`READY_FOR_AUDIT`、`AUDITED_PASS`、live副作用或科学Evidence。
- 当前缺口从“代码/单测是否闭合”转为“当前subject的WorkPackagePlan/CompletionBundle/DocBootstrapCompletionRecord物证是否整理并可被GA1独立审计”。
- 旧`8b5e...` DOC0 evidence和旧`a3ac934...` GV0 evidence仅作为历史物证；当前dirty working tree需要新的subject物证。

| 工作包 | 当前状态 | Development依赖 | Activation依赖 | 下一动作 |
|---|---|---|---|---|
| WP-DOC0 | `IN_PROGRESS` | 无 | 无 | 文档合同与全量测试在当前工作树PASS；旧8b5e证据仅覆盖历史subject。下一步生成当前subject的DocBootstrapCompletionRecord/测试收据或等干净commit后重签；完成前不是READY_FOR_AUDIT。 |
| WP-GV0 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-DOC0 | WP-DOC0 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |
| WP-VLT0 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-GV0 | WP-GV0 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |
| WP-HG0 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-GV0、WP-VLT0 | WP-GV0、WP-VLT0 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |
| WP-CW0 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-GV0、WP-VLT0 | WP-GV0、WP-VLT0 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |
| WP-CW-D1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-CW0 | WP-CW0、WP-VLT0、WP-HG0、WP-DB1I、WP-RT1 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |
| WP-CW-C1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-CW0 | WP-CW0、WP-VLT0、WP-HG0、WP-DB1I、WP-RT1 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |
| WP-QA0 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-HG0、WP-CW-D1、WP-CW-C1 | WP-VLT0、WP-HG0、WP-DB1I、WP-RT1、WP-CW-D1、WP-CW-C1 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |
| WP-DB1L | `IMPLEMENTED_PENDING_EVIDENCE` | WP-GV0 | WP-GV0、WP-HG0 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |
| WP-DB1I | `IMPLEMENTED_PENDING_EVIDENCE` | WP-DB1L、WP-HG0、WP-VLT0 | WP-DB1L、WP-HG0、WP-VLT0 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |
| WP-RT1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-DB1I、WP-VLT0 | WP-DB1I、WP-VLT0、WP-HG0 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |
| WP-SV1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-VLT0、WP-RT1 | WP-VLT0、WP-RT1、WP-HG0 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |
| WP-IN1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-GV0 | WP-GV0 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |
| WP-TX1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-IN1、WP-VLT0、WP-RT1、WP-HG0 | WP-IN1、WP-VLT0、WP-RT1、WP-HG0 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |
| WP-CW1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-RT1、WP-CW-D1、WP-CW-C1 | WP-RT1、WP-VLT0、WP-HG0、WP-CW-D1、WP-CW-C1 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |
| WP-QA1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-QA0、WP-SV1、WP-RT1、WP-HG0 | WP-QA0、WP-VLT0、WP-SV1、WP-RT1、WP-HG0 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |
| WP-CS1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-IN1、WP-TX1、WP-CW1、WP-HG0、WP-QA1、WP-SV1 | WP-IN1、WP-TX1、WP-CW1、WP-HG0、WP-QA1、WP-SV1 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |
| WP-ST1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-TX1、WP-CW1、WP-SV1 | WP-TX1、WP-CW1、WP-SV1、WP-CS1 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |
| WP-EX1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-CS1、WP-QA1、WP-SV1、WP-ST1 | WP-CS1、WP-QA1、WP-SV1、WP-ST1、WP-HG0 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |
| WP-AU1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-EX1、WP-CW1 | WP-EX1、WP-CW1、WP-VLT0、WP-HG0 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |
| WP-EV1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-AU1 | WP-AU1 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |
| WP-RV1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-EV1、WP-HG0 | WP-EV1、WP-HG0 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |
| WP-VR1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-RV1 | WP-RV1 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |
| WP-GA1 | `NOT_STARTED` | WP-VR1 | WP-VR1 | owner=`AUDITOR`；等待repo外AuditAssignment与独立审计。实施者路径保持停止，等待审计者路径。 |
| WP-OP1 | `IMPLEMENTED_PENDING_EVIDENCE` | WP-VR1 | WP-GA1、WP-HG0、WP-RT1、WP-VLT0 | side-effect-free代码/测试存在（包相关测试存在，且当前全量2385 tests OK）；WorkPackagePlan/ImplementationCompletionBundle builders与NormativeReviewRecord verifier已能组装或验证普通implementer-owned包审计前候选Plan/Bundle链路，且Plan→Bundle连接测试已通过；但仍缺真实NormativeRequirementReviewRecord，尚未为当前subject落出正式候选Plan/CompletionBundle物证；未独立审计，未获live授权。下一步整理候选Plan/CompletionBundle并继承审计债。 |

## 历史错误状态记录（append-only，不删除）

### R0 / R1 历史快照

早期看板曾把DOC0写成`READY_FOR_AUDIT`、把GV0写成`IMPLEMENTED_PENDING_EVIDENCE`但列出P0-A/B/C旁路，且把下游22个包退回`NOT_STARTED`。这些记录对应当时的审计阶段，不再是当前状态。

R2修正后：

- P0-A/B/C与DB1I/R5相关旁路已由测试覆盖并通过；
- 下游包的side-effect-free代码/测试已在当前工作树闭合；
- 但所有implementer-owned包仍缺当前subject的正式完成物证，状态保持在`IMPLEMENTED_PENDING_EVIDENCE`或DOC0的`IN_PROGRESS`；
- GA1仍是唯一auditor-owned包，保持`NOT_STARTED`。

### 曾经的越级状态

审计基线commit `783d4be` / tree `36148d1f` 时，多个工作包曾被上一位实施AI标为`IMPLEMENTED_PENDING_EVIDENCE`，但当时development dependency未满足，属于越级启动。既有代码保留；R2后这些代码作为当前side-effect-free候选实现的一部分接受全量回归，后续经当前subject的Plan/CompletionBundle/GA1链路重新取得可审计状态。

### 当前唯一允许的下一步

1. 为当前subject整理或生成DOC0 bootstrap物证与普通implementer-owned包的候选ImplementationCompletionBundle；
2. 每个候选Bundle显式写明fake/stub、未运行live、未产生科学Evidence、未取得AUDITED_PASS；
3. 准备GA1独立审计输入；AuditAssignment/AuditRecord留给审计者路径；
4. GA1或相应activation gate之前，真实DB写入、D盘CAS/Vault写入、模型调用、Target Solver或P2-P9科学实验保持未启动。
