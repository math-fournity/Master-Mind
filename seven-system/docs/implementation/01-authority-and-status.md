# 文档权威、实现状态与主张权限

## 一句话结论

Seven 同时维护“目标应该是什么”和“当前实际上有什么”两条真值轴。实施 AI 必须按目标规范写代码，但只能依据真实代码、测试和运行物证更新实现状态；两者冲突时必须停下记录偏差，不能挑对自己方便的一份。

目标规范与当前事实必须分轴记录；`DESIGN_FROZEN`不能冒充`NOT_IMPLEMENTED`能力已经实现。

## 两条真值轴

### 目标规范轴

回答“完整系统必须怎样实现”：

1. `AGENTS.md`：安全、权限、Git、数据库、Solver和人工 Gate硬约束；
2. `seven-system/docs/implementation/`：完整目标、接口、状态、工作包和验收；
3. `seven-system/docs/decisions/`：重大架构裁决及被替代关系；
4. 387/389号研究文档：设计来源、论证和历史，不单独证明功能存在。

### 当前事实轴

回答“这个commit真的实现了什么”：

1. `seven-system/docs/implementation-status.md`；
2. 受版本控制的代码、Schema和测试；
3. 绑定源码树的测试收据、CapabilityReport和运行artifact；
4. 当前操作手册中已经验证可运行的命令。

代码与文档不一致不代表代码自动胜出。审计者应当把它记为“实现偏离规范”或“文档过度主张”，而不是静默选择一边。

## 状态写权限

`owner_type`、`completion_contract`和`state`是三个正交维度：owner回答“谁有资格提交”，contract回答“必须提交哪种机器对象”，state回答“当前推进到哪里”。禁止创建`AUDITOR_OWNED_NOT_ASSIGNED`这类把owner塞进state的混合值；未指派审计者时，auditor-owned节点保持`NOT_STARTED`并在reason/next action记录等待条件。

| owner_type | 允许的completion_contract | 提交边界 |
|---|---|---|
| `IMPLEMENTER` | `IMPLEMENTATION_BUNDLE`；仅WP-DOC0为`DOC_BOOTSTRAP_RECORD` | 实施者最高写`READY_FOR_AUDIT`，不得写`AUDITED_*` |
| `AUDITOR` | `AUDIT_RECORD` | 实施者命令一律拒绝；只有外部Assignment绑定的独立审计路径可提交 |

| 状态 | 谁可以写 | 必需证据 |
|---|---|---|
| `NOT_STARTED/READY` | 维护者或实施计划 | 依赖与工作包规范 |
| `IN_PROGRESS` | 当前实施者 | 领取记录、spec hash、基线commit |
| `IMPLEMENTED_PENDING_EVIDENCE` | 当前实施者 | 代码和初步测试已存在 |
| `READY_FOR_AUDIT` | 当前实施者 | 完整CompletionBundle、所有规定测试收据 |
| `AUDITED_PASS/PARTIAL/FAIL` | 独立审计者 | AuditRecord、复跑物证、finding闭合情况 |
| `BLOCKED` | 实施者或审计者 | 明确阻塞条件、证据和解除条件 |

同一个 AI 如果实现过程中修改了被审对象，就不再是该 revision 的独立审计者。它可以做自检，但只能写 `SELF_CHECK_PASS`，不能写 `AUDITED_PASS`。

WP-GV0唯一拥有DAG-aware `CompletionContractVerifier`和`SecurityContractVerifier`公共核心。所有状态服务在写状态前必须先用冻结DAG hash检查owner、contract、submitted schema和actor；Schema-bootstrap原子预留后端由WP-DB1I实现，canonical DB事务后端由WP-RT1实现，但两者不得复制或放宽GV0语义。

## 实现依赖与激活依赖必须分开

用户希望另一位实施AI能够沿文档把整个候选系统实现出来，完成后再交给未来独立审计。因此工作包有两种依赖语义：

- **development dependency**：上游达到`READY_FOR_AUDIT`后，下游可以继续写代码、Schema、fake/in-memory集成和无外部副作用测试；下游CompletionBundle必须列出继承的`audit_debt`，不得把上游当作已审能力。
- **activation dependency**：任何真实DB写入、远程模型调用、Target Solver、正式HumanGate、canonical P0–P9运行或科学Evidence，都要求适用上游已`AUDITED_PASS`；此外，每次副作用必须由父级`ExternalExecutionAuthorization`、其不可扩权子集`LiveRunPermit`和原子`AuthorizationConsumptionReceipt(RESERVED)`共同承载。未审canary只有在这条完整授权链针对工作包、次数、profile和预算精确覆盖时才能运行，并只能记`UNAUDITED_AUTHORIZED_CANARY`；结果用于实现调试和未来审计，不能用于科学主张或active release。

这允许一个实施AI把所有候选代码和受控运行物证准备到`SYSTEM_CANDIDATE_READY_FOR_EXTERNAL_AUDIT`，但不允许它把该状态改写成`FACTORY_GOLDEN_SLICE_AUDITED`。

## 需求用词

- **MUST / 必须**：缺失即 blocker，除非工作包明确写 `NOT_APPLICABLE`及理由。
- **MUST NOT / 禁止**：违反即 FAIL 或 QUARANTINE。
- **SHOULD / 应当**：偏离必须记录 rationale、风险和替代验证。
- **MAY / 可以**：实现选择，不形成默认能力主张。

## 当前基线

本规范建立时，当前实现仍是：

- P0只读preflight；
- P1 scaffold dry-run，而非387号完整P1；
- WP-1离线Strict DB契约；
- 不连接真实DB/Redis；
- 不启动Target Solver；
- 不调用Codex或Devin认知worker；
- P2–P9、Vault、HumanGate、ModelRolePort、TargetSolverPort均未实现。

这些事实只能由后续独立工作包和审计证据逐项改变。

## 主张分层

每次提交与报告都必须同时写：

```yaml
explicit_claims: []
explicit_nonclaims: []
implementation_scope: []
evidence_scope: []
known_limitations: []
```

至少区分：

1. `DESIGN_FROZEN`：规定已经明确，代码未必存在；
2. `IMPLEMENTED`：代码路径存在，尚未证明本站或live能力；
3. `TESTED_OFFLINE`：受控测试通过，不等于真实外部能力；
4. `CAPABILITY_VERIFIED`：精确profile、版本、权限和观测链已通过能力门；
5. `RUNTIME_OBSERVED`：在受控真实运行中形成收据；
6. `SCIENTIFIC_SUPPORTS/CONTRADICTS`：只能来自预注册contrast级EvidenceRecord。

## 冲突处理

发现冲突时：

1. 停止进入下游工作包；
2. 保存冲突两侧的文件路径、行号和hash；
3. 生成 `SpecificationConflictRecord`；
4. 由维护者裁决目标规范，或由实施者修正过度主张；
5. 新版本重新计算所有受影响的spec/Schema/report hash；
6. 旧证据保留并标注适用版本，禁止改外键伪装成新版本证据。

## 读完应记住的五句话

1. 目标规范不证明实现存在。
2. 代码存在不证明它符合目标规范。
3. 实施者不能给自己签独立审计PASS。
4. 负结果和BLOCKED都是合法、必须保留的状态。
5. 任何主张都要能落到版本、hash、测试和运行证据。
