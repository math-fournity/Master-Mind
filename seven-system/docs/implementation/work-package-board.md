# Seven System 工作包看板

> 本看板只记录状态和下一动作；依赖边必须与[`work-package-dag.v1.json`](work-package-dag.v1.json)机器真值源完全相等，不替代`implementation-status.md`的当前能力事实。

## 状态规则

`owner_type`、`completion_contract`和当前状态分别以canonical DAG、DAG contract和本看板记录，三者不得混成自造状态。implementer-owned普通包最高只能写`READY_FOR_AUDIT`，DOC0同属implementer-owned但交付`DOC_BOOTSTRAP_RECORD`；auditor-owned包拒绝实施者状态命令，只有独立审计路径可以写`AUDITED_*`。上游`READY_FOR_AUDIT`可满足无副作用development dependency，但下游必须记录审计债；真实激活要求适用上游`AUDITED_PASS`，并为每次副作用同时验证父级`ExternalExecutionAuthorization`、不可扩权`LiveRunPermit`和原子`AuthorizationConsumptionReceipt(RESERVED)`。未审canary只能在这条完整授权链精确覆盖时运行并标记`UNAUDITED_AUTHORIZED_CANARY`，不能获得正式PASS。

| 工作包 | 当前状态 | Development依赖 | Activation依赖 | 下一动作 |
|---|---|---|---|---|
| WP-DOC0 | `READY_FOR_AUDIT` | 无 | 无 | 已生成[`DOC_BOOTSTRAP_RECORD`](evidence/wp-doc0/doc-bootstrap-completion-record-8b5e9c92fd8b.json)，等待repo外独立审计；不生成ImplementationBundle |
| WP-GV0 | `NOT_STARTED` | WP-DOC0 | WP-DOC0 | 实现两个Verifier与最小D盘CompletionArtifactStore，自托管首个普通Bundle |
| WP-VLT0 | `NOT_STARTED` | WP-GV0 | WP-GV0 | 复用GV0 CAS核心扩展完整Artifact/Vault，禁止第二store |
| WP-HG0 | `NOT_STARTED` | WP-GV0、WP-VLT0 | WP-GV0、WP-VLT0 | HumanTask/HumanGate；消费GV0验证器 |
| WP-CW0 | `NOT_STARTED` | WP-GV0、WP-VLT0 | WP-GV0、WP-VLT0 | ModelRole公共运行时与fake adapter |
| WP-CW-D1 | `NOT_STARTED` | WP-CW0 | WP-CW0、WP-VLT0、WP-HG0、WP-DB1I、WP-RT1 | Devin `glm-5-2` High认知adapter；live canary等待DB运行账本与reconcile |
| WP-CW-C1 | `NOT_STARTED` | WP-CW0 | WP-CW0、WP-VLT0、WP-HG0、WP-DB1I、WP-RT1 | Codex认知adapter；live canary等待DB运行账本与reconcile |
| WP-QA0 | `NOT_STARTED` | WP-HG0、WP-CW-D1、WP-CW-C1 | WP-VLT0、WP-HG0、WP-DB1I、WP-RT1、WP-CW-D1、WP-CW-C1 | 受控双载体出题纵切与Bakeoff-A（无Target Solver/bare） |
| WP-DB1L | `NOT_STARTED` | WP-GV0 | WP-GV0、WP-HG0 | 全部`seven_*_vN`逻辑站点只读核验 |
| WP-DB1I | `NOT_STARTED` | WP-DB1L、WP-HG0、WP-VLT0 | WP-DB1L、WP-HG0、WP-VLT0 | 受控版本化Schema；只交付SchemaState/bootstrap三对象 |
| WP-RT1 | `NOT_STARTED` | WP-DB1I、WP-VLT0 | WP-DB1I、WP-VLT0、WP-HG0 | 只交付Runtime/Reconcile能力与checkpoint |
| WP-SV1 | `NOT_STARTED` | WP-VLT0、WP-RT1 | WP-VLT0、WP-RT1、WP-HG0 | TargetSolver与NoTool Harness |
| WP-IN1 | `NOT_STARTED` | WP-GV0 | WP-GV0 | 只读CandidateManifest导入 |
| WP-TX1 | `NOT_STARTED` | WP-IN1、WP-VLT0、WP-RT1、WP-HG0 | WP-IN1、WP-VLT0、WP-RT1、WP-HG0 | Taxonomy/Tell Registry与版本谱系 |
| WP-CW1 | `NOT_STARTED` | WP-RT1、WP-CW-D1、WP-CW-C1 | WP-RT1、WP-VLT0、WP-HG0、WP-CW-D1、WP-CW-C1 | P3N/P6生产认知worker |
| WP-QA1 | `NOT_STARTED` | WP-QA0、WP-SV1、WP-RT1、WP-HG0 | WP-QA0、WP-VLT0、WP-SV1、WP-RT1、WP-HG0 | 生成题bare准入与Bakeoff-B |
| WP-CS1 | `NOT_STARTED` | WP-IN1、WP-TX1、WP-CW1、WP-HG0、WP-QA1、WP-SV1 | WP-IN1、WP-TX1、WP-CW1、WP-HG0、WP-QA1、WP-SV1 | CaseLab双入口与P3C |
| WP-ST1 | `NOT_STARTED` | WP-TX1、WP-CW1、WP-SV1 | WP-TX1、WP-CW1、WP-SV1、WP-CS1 | Selector/Renderer/Option/Injection/Critic运行时 |
| WP-EX1 | `NOT_STARTED` | WP-CS1、WP-QA1、WP-SV1、WP-ST1 | WP-CS1、WP-QA1、WP-SV1、WP-ST1、WP-HG0 | P4/P5实验 |
| WP-AU1 | `NOT_STARTED` | WP-EX1、WP-CW1 | WP-EX1、WP-CW1、WP-VLT0、WP-HG0 | P6三审 |
| WP-EV1 | `NOT_STARTED` | WP-AU1 | WP-AU1 | P7 Evidence |
| WP-RV1 | `NOT_STARTED` | WP-EV1、WP-HG0 | WP-EV1、WP-HG0 | P8 NO_CHANGE/Revision |
| WP-VR1 | `NOT_STARTED` | WP-RV1 | WP-RV1 | P9 Verdict/Replay |
| WP-GA1 | `NOT_STARTED` | WP-VR1 | WP-VR1 | owner=`AUDITOR`；等待repo外AuditAssignment，实施者不得推进 |
| WP-OP1 | `NOT_STARTED` | WP-VR1 | WP-GA1、WP-HG0、WP-RT1、WP-VLT0 | 候选代码可在VR1后开发；真实规模化须GA1审计通过 |

## 当前唯一允许的实施动作

WP-DOC0已基于subject commit `8b5e9c92fd8b05a4811b0c9e8336b3e3dcc0170c`完成机器自检和bootstrap evidence，实施者状态现为`READY_FOR_AUDIT`。这不是独立审计结论，也不解除任何activation gate。

当前只允许：

- 由repo外owner签发AuditAssignment后，对WP-DOC0执行独立审计；
- 按DAG启动WP-GV0的无外部副作用development，并显式继承WP-DOC0的审计债；
- 复验DOC0 subject commit、bootstrap record和测试收据；
- 不得借本轮文档工作实现或调用任何远程模型、DB写入、Redis或Solver。

实施AI下一步先完成WP-GV0；GV0达到`READY_FOR_AUDIT`后才可继续VLT0/DB1L/CW0/IN1的无副作用开发。在未来独立审计清除审计债之前，不得把任何候选运行或能力写成正式PASS。
