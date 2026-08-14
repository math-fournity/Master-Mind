# Seven System 独立审计入口

> **给未来审计者**：当另一位AI完成某个工作包或声称系统已可运行时，从这里开始。
> **原则**：先冻结被审对象，再独立复跑；审计者若修改代码，就必须终止当前独立审计。

审计者不得把被审repo、数据库、CompletionBundle或运行时配置当成HumanGate信任根的唯一来源。开始前必须从站点owner控制的repo外渠道取得pinned trust-root hash并保存source/time/observation receipt，随后验证符合[`audit-assignment.v1.schema.json`](../implementation/audit-assignment.v1.schema.json)的签名`AuditAssignment`。Assignment精确绑定repo外channel、root/roster/policy、目标work-package ID、subject commit/tree、CompletionBundle、可选evidence-index commit、audit plan/spec、auditor principal/public key、scope和期限；缺任一项只能`BLOCKED`。审计自身若要调用真实DB、Redis、provider或Solver，还必须另有符合EEA/LiveRunPermit/ConsumptionReceipt三Schema的逐次授权链；AuditAssignment不是外部执行permit。

## 审计目标

回答四个不同问题：

1. 实现是否覆盖全部规定性需求？
2. 是否存在绕过端口、权限、Gate、hash或证据链的路径？
3. 在真实失败、并发和恢复场景下是否仍保持不变量？
4. 最终科学主张是否真的来自预注册contrast，而不是漂亮episode或泄漏？

## 固定阅读顺序

1. 根/Seven `AGENTS.md`；
2. [`../implementation/README.md`](../implementation/README.md)；
3. 待审工作包CompletionBundle及spec hashes；
4. AuditAssignment、repo外pinned trust-root observation及其验签物证；
5. [`01-audit-method-and-verdicts.md`](01-audit-method-and-verdicts.md)；
6. [`02-static-and-bypass-audit.md`](02-static-and-bypass-audit.md)；
7. [`03-runtime-isolation-and-recovery-audit.md`](03-runtime-isolation-and-recovery-audit.md)；
8. [`04-scientific-and-evidence-audit.md`](04-scientific-and-evidence-audit.md)；
9. [`05-overclaim-checklist.md`](05-overclaim-checklist.md)。

## 审计四表

1. **Boundary Table**：所有CLI、provider、DB、D盘、Redis、Vault、人工Gate和生产系统边界；
2. **Static Table**：代码、imports、Schema、配置、状态机和权限；
3. **Dynamic Table**：unit/component/integration/capability/fault/golden slice；
4. **Orphan Table**：无需求来源代码、无父hash artifact、无receipt调用、无Gate跃迁、无terminal WorkItem。

所有表要求`remainder=0`。

四表至少还要生成两个机器投影：

- **Operator Surface Projection**：从`OperatorCommandRegistry`枚举CLI/API/worker全部入口，对照真实parser/router/application service/Port/Gate/permit/receipt调用图，双向集合差为0；
- **Role Qualification Projection**：从RuntimeManifest枚举全部启用的`role × profile × view/ACL × tool/network/sandbox × sensitivity/sink × prompt/output/adapter × qualification level`精确cell，对照RoleQualificationMatrix和CapabilityReports，禁止wildcard或跨carrier继承。

## Verdict

- `AUDITED_PASS`：全部blocker通过、证据完整、scope明确；
- `AUDITED_PARTIAL`：核心路径成立，但有未覆盖非blocker或scope不足；
- `AUDITED_FAIL`：规定性MUST、隔离、恢复或主张被有效反驳；
- `BLOCKED`：环境、授权、物证或协议缺失，无法诚实审计；
- `NOT_TESTED`：明确没有执行，不等于PASS。

审计结论必须分`implementation/factory/scientific/production_scale`四轴，禁止一个总分掩盖某一轴FAIL。

审计者产出的`AuditRecord`必须符合[`audit-record.v1.schema.json`](../implementation/audit-record.v1.schema.json)，每条finding绑定受影响轴和evidence，四轴分别给出verdict。AI审计者只生成unsigned canonical bytes；模型不可达的`AttestationSignerPort`验证Assignment、principal/key、scope和树未变后，才用绑定key生成Ed25519 envelope，私钥永不进入模型workspace。HumanGateService验明assignment、repo外root三方一致、签名、职责分离、subject/bundle/index hashes和四轴结论后，才能发生`AUDITED_*`状态跃迁。未签记录、实施者自建assignment或只在Markdown写“独立审计通过”均不改变状态。

对`WP-GA1`还必须运行DAG-aware `CompletionContractVerifier`：canonical DAG只要声明`owner_type=AUDITOR`或`completion_contract=AUDIT_RECORD`，任何ImplementationCompletionBundle和实施者状态命令都必须返回`COMPLETION_CONTRACT_MISMATCH/ACTOR_NOT_AUTHORIZED`。单对象Schema通过不能覆盖这条机器规则。
