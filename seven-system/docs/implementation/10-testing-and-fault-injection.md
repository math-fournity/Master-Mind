# 测试、能力探针与故障注入

## 一句话结论

测试必须证明“错误路径会被机械阻断”，而不只是happy path会跑。每个工作包至少同时有blocker tests、confidence tests和绑定源码树的机器收据。

## 测试层级

| 层级 | 证明什么 | 不能证明什么 |
|---|---|---|
| Schema | JSON形状和常量 | 跨对象语义、runtime能力 |
| Unit | 单函数/状态机逻辑 | 外部CLI/DB/文件系统真实行为 |
| Contract | adapter/port兼容 | 真实provider是否遵约 |
| Component | 多模块最小闭环 | 完整系统恢复/科学有效性 |
| Integration | 真实边界组合 | 生产规模和长期稳定 |
| Capability canary | 精确版本/profile/权限可用 | 所有角色、所有profile |
| Fault injection | 崩溃/重复/漂移可恢复 | 未注入故障 |
| Golden slice | P0–P9真实纵切 | 生产规模与理论普遍性 |
| Soak | 并发、背压、资源长期稳定 | 未覆盖模型/分支 |

## 测试收据

每次可作为Gate证据的测试必须记录：

```yaml
test_execution_id:
source_commit_and_tree_hash:
schema_and_spec_hashes: []
exact_command_argv:
isolated_environment_summary:
started_at / ended_at:
exit_code:
discovered / executed / skipped / failed / errored:
test_ids: []
stdout_stderr_ref_and_hash:
side_effect_summary:
artifact_refs: []
verdict:
```

必须阻断`PYTHONPATH/sitecustomize`注入、伪造“ok”文本、0 tests、未声明skip和调用者自报hash。

### DOC0两层收据为什么不能只写PASS

操作者真正需要的是“这组检查在什么源码、什么规范、什么命令和什么输出上通过”，不是一个脱离对象的布尔值。因此[`DocContractVerificationReceipt`](doc-contract-verification-receipt.v1.schema.json)必须绑定implementation subject、实际工作树关系、NormativeRequirementIndex source set、DAG/Plan/migration、完整规范与Schema hash清单、精确verification IDs、checker及依赖锁、起止时间和规范化输出hash；receipt自己的hash还必须在把`receipt_hash`置null后重算。

[`DOC0TestExecutionReceipt`](doc0-test-execution-receipt.v1.schema.json)必须再绑定精确subject、Index/Plan/source set、Schema/spec清单，以及每条命令的隔离环境、完整test IDs、argv、cwd、起止时间、stdout/stderr和artifact refs。`aggregate_verdict=PASS`时，每条命令必须`exit_code=0`、`verdict=PASS`、至少执行一个测试、`failed=errors=0`，并满足`executed=passed+failed+errors`和`discovered=executed+skipped`；命令test IDs的并集必须与Plan冻结的`test_plan_ids`完全相等。任何caller自报字段即使通过JSON Schema，只要不能由checker从冻结输入重算，也必须被semantic verifier拒绝。

所有证据时间必须采用canonical UTC RFC3339：`YYYY-MM-DDTHH:MM:SS[.1-9 digits]Z`。Schema format检查、正则和semantic parser必须同时启用；offset形式、空格分隔、无时区、非法日历日期、超过9位小数、`completed_at <= started_at`或receipt早于命令完成都必须进入负向向量并fail-closed。

AuditRecord的Schema通过也不等于审计闭包。checker必须核对assignment冻结的auditor key ID/public-key hash、外部channel、subject/bundle/index、plan/spec集合和allowed axes；每个finding必须恰好挂到所有`affected_axes`的`finding_ids`，未知、重复、漏挂或多挂都拒绝。assignment未允许的轴只能是有非空理由且无evidence的`NOT_TESTED`；任何未由audited subject解决的P0 finding都必须阻断`AUDITED_PASS`或科学`SUPPORTS`，不能用`ACCEPTED_SCOPE_LIMIT`洗成PASS。

## 基础设施blocker矩阵

- RuntimeManifest/Schema/receipt任意必需字段删除；
- 重算内部index但外部root receipt不变；
- 祖先或叶symlink逃逸；
- 当前源码漂移与历史artifact integrity分轴；
- 错误DB、默认DB、secret出现在日志；
- 非canonical/额外index；
- 仅有现存`seven_*_v1` scaffold/离线Schema却试图解锁HumanGate、外部模型、Solver、Redis写或canonical Epoch；
- read操作触发DDL；
- D盘掉线、UUID变化、容量低；
- sealed artifact篡改、partial崩溃、CAS/DB单边提交；
- duplicate delivery、stale fence、outbox ACK丢失、Redis全丢。

## WP-DOC0文档合同测试

DOC0检查器依赖[`requirements-docs.txt`](requirements-docs.txt)中冻结的`jsonschema`版本。审计者必须在隔离环境安装该文件后使用同一解释器运行`tools/verify_doc_contracts.py`；`ModuleNotFoundError`是环境`BLOCKED`，不得切换到功能更弱的临时验证器后仍报告PASS。检查收据必须记录Python与`jsonschema`精确版本。

- 解析canonical DAG JSON及Schema，拒绝未知依赖、重复节点和环；
- 从Mermaid与工作包看板提取依赖集合，与canonical DAG做精确相等比较；
- 检查全部相对Markdown链接、代码围栏和JSON语法；
- 对`docs/implementation/*.schema.json`逐份执行Draft 2020-12 metaschema校验，并递归要求每个`type=object`节点显式`additionalProperties=false`；动态map只能用受限`patternProperties + additionalProperties=false`表达；
- 重跑`tools/generate_normative_index.py`，要求每个source hash等于当前文件、clause ID唯一、`unclassified_clause_count=0`、`duplicate_clause_id_count=0`；
- 重新扫描全部非代码围栏中的规定性token，要求与生成索引双向集合相等；
- 执行内置安全Schema向量：外部副作用命令缺EEA/Permit/原子预留、live Plan缺授权链、GA1伪装ImplementationCompletionBundle、owner自任auditor、错误auditor签AuditRecord都必须被Schema或semantic verifier拒绝；
- 检查实现入口、审计入口、当前状态和每个工作包的依赖/输入/输出/blocker/物证无第二套真值源；
- 文档检查PASS只支持`WP-DOC0 READY_FOR_AUDIT`，不支持任何runtime、模型、DB、Solver或科学能力PASS。

## Vault访问机器合同测试

先对[`VaultAccessCapability`](vault-access-capability.v1.schema.json)、[`AccessDecision`](access-decision.v1.schema.json)、[`ViewDerivation`](view-derivation.v1.schema.json)和[`AccessEvent`](access-event.v1.schema.json)分别执行Schema正例与负例，再做跨对象semantic/fault测试。最低blocker集合：

- 任一层出现未知字段、缺principal/operation/object+view hash/sink/nonce/issuer/signature/revocation，或`deny_by_default`不为`true`；
- operation、ID或ref使用`*`/glob/`ANY`，或对象试图增加`raw_vault_path`、URI、filesystem locator、capability bearer字段；
- capability签名/domain separator/issuer key/time window不合法仍ALLOW；
- principal、operation、object ID/hash、view ID/hash/policy或sink ID/kind/policy任一不相等仍ALLOW；
- nonce第二次使用、revocation=`REVOKED/EXPIRED/UNKNOWN`或registry查询失败仍ALLOW；
- `ALLOW`存在任一非PASS检查，或`ACCESS_GRANTED`没有ViewDerivation、sink write receipt和ACTIVE revocation snapshot；
- derivation source/rule/generator/redaction/output hash任一漂移，模型仍收到旧view；
- raw Vault路径、源object locator、capability token或签名材料出现在prompt、argv、env、workspace、stdout/stderr、普通日志或模型工具参数；
- access ledger重复sequence、previous-event hash断链、decision/event被覆盖，或撤销与ALLOW的并发竞态无法裁决仍继续dispatch；
- restricted输出先落普通sink再搬运，或sink写失败却记录`ACCESS_GRANTED`。

动态canary必须在Vault放置只有raw source含有的trap，并证明派生view和模型所有可见通道均不含该trap；同时以错误principal、错误view hash、错误sink、重放nonce和撤销后并发请求逐个攻击。任一拒绝链缺事件也不算PASS：DENY/BLOCK本身必须产生签名AccessDecision和append-only AccessEvent，但不得向模型泄漏拒绝原因中的敏感locator。

## Role注册表与资格矩阵测试

`RoleTypeRegistry`和`RoleQualificationMatrix`必须先用fake/stub完成下列blocker tests：

- `RoleExecutionContract`使用自由字符串、`...`、未知role、旧registry hash或已退役role；
- Target Solver、HumanTask/HumanGate或纯程序组件被错误注册为ModelRole；
- registry原地增删/改名而不创建新version/hash；
- 新registry自动继承旧matrix PASS，或历史receipt被重写到新registry；
- cell key漏掉role、carrier、model、profile、实际input view、view/ACL/Vault capability、tool/network/sandbox policy、sensitivity/sink policy、prompt、output schema、adapter、parser、capability requirement或qualification level任一维度；
- 通配符cell、同provider继承、“更高effort应兼容”、CANARY PASS升级PRODUCTION PASS；
- CapabilityReport为空、hash不匹配、已过期或缺证据时管理员直接写PASS；
- role/profile/view/tool policy任一漂移后旧cell仍可dispatch；
- Router在精确cell不存在、非PASS、过期或scope不足时自动fallback；
- `selector`/`hint_renderer`走确定性程序时错误要求ModelRole资格，或选择模型实现时绕过资格矩阵。

必须生成机器可读的matrix completeness报告，至少包含：

```yaml
role_type_registry_ref_and_hash:
runtime_manifest_ref_and_hash:
qualification_scope: CANARY | PRODUCTION
completeness:
  required_cell_keys: []
  pass_cell_keys: []
  not_tested_cell_keys: []
  failed_cell_keys: []
  extra_cell_keys: []
  missing_cell_keys: []
  remainder_cell_keys: []
  remainder_count:
  verdict: PASS | BLOCKED
  algorithm_ref_and_hash:
```

该对象必须通过[`role-qualification-matrix.v1.schema.json`](role-qualification-matrix.v1.schema.json)。semantic verifier还要从RuntimeManifest重算required、从cells重算其余集合，并断言：所有集合内无重复；pass/not-tested/failed/missing互斥且并集恰为required；extra恰为observed减required；remainder恰为not-tested/failed/missing/extra的去重并集；`remainder_count`等于该并集大小。Schema已经拒绝wildcard，因此任何wildcard不是“extra”，而是整个对象形状失败。

阶段断言：

- WP-CW-D1初始Devin canary集合必须**恰好**是`question_architect`、`adversarial_editor`、`math_verifier`的无敏感输入/输出cell；运行前为`NOT_TESTED`，未运行不能预填PASS；
- WP-CW-D1代表性CANARY PASS不能解锁Trace/Solution Analyst、Adjudicator、三审、Selector/Hint Renderer或任何PRODUCTION cell；
- WP-CW1验收必须覆盖RuntimeManifest实际启用的P3N/P6精确cell；
- `PRODUCTION_SCALE_AUDITED`要求每个生产启用的完整Schema cell（role/carrier/model/profile/actual view/Vault capability/全部policy/adapter/parser/capability requirement）逐格PASS且`remainder_count=0`；若声称某Devin profile承担全部当前机器角色，还要逐role至少一个Devin PRODUCTION cell PASS；
- Codex、Devin和未来adapter分别计算completeness，不能用一个carrier的PASS补另一个carrier的缺口。

## Devin认知adapter测试

- ModelRole Devin从不调用solver_harness；
- TargetSolver从不调用ModelRole adapter；
- DevinSolverAdapter直接调用devin binary的AST、import或monkeypatch路径必须BLOCK；Seven内只有DevinCliModelRoleAdapter可以直接调用binary；
- argv结构化，prompt只通过受限file；
- exact UID不是`glm-5-2`即BLOCK；
- catalog snapshot缺失/漂移；
- export缺失、ATIF损坏、parser未知；
- 某generation-bearing assistant/model step缺失或generation model不一致；user/tool/telemetry step不要求该字段；
- global config/rules污染；
- sibling workspace/Vault拒读；
- tool/network/sandbox越权；
- stdout/export含解答却落普通日志；
- accepted/started未知后重复调用；
- receipt缺精确argv、binary、permission/sandbox flags、accepted/started物证、stdout/stderr/export或tool definitions/events任一required ref；
- timeout、cancel、rate limit、token truncation；
- 同模型fresh reviewer只记context-independent；
- carrier-global限流不让Solver或Judge互相饿死。

Devin的架构合同测试还必须遍历当前`RoleTypeRegistry`，证明adapter不会把非首轮canary角色硬编码拒绝；遍历成功只记`PORT_COMPATIBLE`，不创建CapabilityReport PASS。

## Codex adapter测试

Codex CLI与OpenAI Responses API必须使用不同adapter、prepared-request Schema和receipt backend；下面矩阵对`CodexExecModelRoleAdapter`逐层执行，不能用stub或当前交互式Codex会话冒充live能力：

| 层级 | 外部调用 | 必测内容 | 可产生的最高结论 |
|---|---|---|---|
| Fake | 无 | 公共port、状态机、fence、Vault sink、RoleQualificationMatrix | `PORT_COMPATIBLE` |
| Protocol stub | 无真实provider | 精确argv mapping、JSONL fixtures、accepted/started、parser、cancel/reattach/reconcile | `PROTOCOL_COMPATIBLE` |
| Live canary | 仅逐次授权 | 精确本机binary+账号+model/profile+policy cell | 该cell的`CANARY PASS` |
| Fault/soak | 按独立授权和预算 | 真实断连、partial、背压、usage/cost与恢复 | 对应scope的能力证据 |

fake与protocol stub必须覆盖：

- `CodexExecPreparedRequest`缺registry/cell、binary hash、argument mapping、精确argv、input、project doc、workdir、config home、env allowlist、credential policy、event/export sink或fence contract任一必需字段；
- exact argv不是token数组、出现shell、调用者extra args、占位符、prompt/secret暴露在argv，或requested字段没有一对一mapping；
- Codex CLI adapter代发Responses API请求、把CLI session ID冒充response ID，或用非规范`Ultra-like`作为profile/effective枚举；
- requested/effective model、effort、reasoning mode和orchestration没有分别核对，字段不支持时静默删除或降级；
- single profile PASS解锁multi-agent、standard/pro、另一effort/model/role/view/tool policy；
- repo/Solver/sibling role workspace运行，复用session/thread/config home/project doc，继承用户AGENTS、历史context或未声明memory；
- env不在allowlist，长期凭据进入workspace、prompt、argv、普通receipt/stdout，或credential handle跨pool误用；
- input view可越权读取sibling workspace/Solver root/Vault；
- sandbox、tool definitions/events、network requested与observed不一致；
- process fork/PID/exit 0被错误写成`REQUEST_ACCEPTED`，或没有generation事件/usage正证据却写`GENERATION_STARTED`；
- accepted/started未知后重复Codex、自动转Devin或在同一attempt改profile；
- JSONL/event序号缺口、未知event type、截断、无terminal、parser版本不匹配或只保留final文本仍被接受；
- solution/holdout-bearing request、raw events、stdout/stderr或output先落普通sink；
- output schema失败、partial artifact未隔离或raw event无法重放仍被seal；
- reattach无稳定provider ID/能力报告却重跑，cancel未带fence或超时后假定未生成，reconcile遗漏孤儿/重复terminal；
- child invocations、topology或usage不可见却声称multi-agent可观察；parent-child usage/cost双计；
- provider billed amount不可观察却填推导值，usage不完整却计算正式cost；
- timeout、rate limit、credential失效、token truncation、disk full、event sink中断和进程崩溃；
- 失败后自动转Devin，或fallback结果并入原attempt。

live canary只有在精确`ExternalExecutionAuthorization`覆盖调用次数、model/profile、role、输入敏感性、预算、sink和停止条件，并且存在其不可扩权子集`LiveRunPermit`、本次action ordinal已原子`RESERVED`时才能运行。adapter只能消费permit ordinal，不能直接消费EEA。每次只资格化一个精确cell，并验证：

1. binary路径/SHA/version与argument mapping；
2. 本账号实际接受requested model、effort、reasoning mode和orchestration；
3. accepted/started、provider ID、raw JSONL、terminal和output Schema均有物证；
4. workspace/project doc/env/credential/ACL隔离与tool/network/sandbox实际观察；
5. cancel/reattach能力按profile声明为PASS或`UNSUPPORTED`，未知状态fail-closed；
6. usage scope、child refs、parent-child reconciliation、provider billing和derived cost来源分开；
7. 全部可能solution-bearing的数据从产生时进入Vault。
8. 成功后同一transaction把ordinal转`CONSUMED`并记录真实usage/cost；可证明pre-accept失败才可`RELEASED_UNUSED`；accepted/started不明时只能`UNKNOWN_START_HELD`，不能释放后重调。

在这些live canary真正执行并封存前，本机CLI、账号、模型、effort/mode/orchestration、工具/网络/沙箱、恢复和成本能力均必须保持`NOT_TESTED`。

## HumanGate与安全测试

- 独立审计只从被审repo/DB/CompletionBundle读取root，未从站点owner的repo外渠道取得pinned root hash却写readiness PASS；
- 同时替换trust root、roster和bootstrap receipt后内部仍自洽，但外部pin不匹配；
- RFC 8785 JCS bytes、domain separator或自引用字段排除规则发生一字节变化仍验签通过；
- 签名对象自报非allowlist算法、错误Ed25519 key、root rotation断链或已撤销key仍被接受；
- ModelRole试图签Gate；
- 作者审批自己；
- unauthorized actor/role；
- payload hash变化；
- expired/replayed signature；
- separation policy冲突；
- timeout默认PASS；
- Process Auditor读取答案；
- Solver/Selector/Renderer读取Vault；
- Judge看到arm或其他Judge结论；
- solution-bearing request/output落普通sink；
- blind ID在seal前暴露treated/control。

`AuditAssignment/AuditRecord`还必须覆盖：无owner签发assignment、assignment过期/重放、subject/bundle/index hash变化、实现者给自己分配审计角色、审计者修改被审树后继续签、attestation key不匹配、AuditRecord签名或四轴verdict被改写，以及没有最终HumanGate验收却直接跃迁`AUDITED_*`。任一项必须BLOCK或QUARANTINE。

### 安全Schema静态负例验收

安全Schema的测试不能只检查“合法JSON能通过”。runner必须同时启用Draft 2020-12和实际可用的RFC 3339 parser；开工探针必须断言`not-a-date`、不允许的offset形式和不存在的日历日期确实被拒绝，不能把库对未知`format`的静默忽略当成已启用checker。每个负例保存`input hash + schema hash + semantic verifier hash + expected/actual error code`：

| 对象 | 最小负例 | 必须得到的错误族 |
|---|---|---|
| AuditAssignment | 缺repo外channel/root/roster/policy/audit plan；任意对象冒充signature envelope；非Ed25519；owner/auditor违反separation；非法或倒序时间 | `ASSIGNMENT_SCHEMA_INVALID / SIGNATURE_INVALID / EXTERNAL_ROOT_UNPROVEN / SEPARATION_VIOLATION / TIME_INVALID` |
| AuditRecord | root只有hash而无source/time/receipt；assignment key与record signer不同；subject/bundle/index变化；finding未绑定轴；NOT_TESTED无scope reason；单字符签名 | `AUDIT_RECORD_SCHEMA_INVALID / ASSIGNMENT_BINDING_MISMATCH / FINDING_AXIS_MISMATCH / SIGNATURE_INVALID` |
| OperatorCommandRegistry | `EXTERNAL_SIDE_EFFECT`却将EEA/permit设false、action entry设null、reserve设false或final Ports/receipts为空；`SAFETY_ONLY`允许resume/activate | `COMMAND_AUTHORIZATION_CONTRACT_INVALID / SAFETY_ACTION_ESCALATES / OPERATOR_SURFACE_REMAINDER` |
| ExternalExecutionAuthorization | unaudited canary不绑定bundle；audited activation无AuditRecord；全部额度为0；未知action entry；错误root/key/时间 | `EEA_MODE_BINDING_INVALID / EEA_ZERO_BUDGET / ACTION_REGISTRY_MISMATCH / SIGNATURE_INVALID` |
| LiveRunPermit | scope、时间、action、target、input、profile、sink或任一额度超过parent；重复ordinal；bootstrap backend用于普通live | `PERMIT_ESCALATES_PARENT / DUPLICATE_ORDINAL / RESERVATION_BACKEND_INVALID` |
| AuthorizationConsumptionReceipt | 无事务收据的RESERVED；无正面未开始物证却RELEASED；UNKNOWN_START释放额度；旧fence；remaining allowance不守恒；覆盖旧revision | `RESERVATION_NOT_ATOMIC / RELEASE_WITHOUT_PROOF / UNKNOWN_START_MUST_HOLD / STALE_FENCE / ALLOWANCE_NOT_CONSERVED / APPEND_ONLY_VIOLATION` |
| Completion contract | `wp_id=WP-GA1`的ImplementationCompletionBundle或实施者状态命令 | `COMPLETION_CONTRACT_MISMATCH / ACTOR_NOT_AUTHORIZED` |

每个负例先证明单对象Schema应拒绝的部分确实拒绝，再证明跨对象semantic verifier拒绝Schema无法表达的关系。不得因为其中一层已拒绝就跳过另一层的独立fixture。合法正例也必须覆盖四种边界：无外部动作的Assignment、一次DB bootstrap、一次已审live action、一次unknown-start hold→reconcile终局。

## EEA、LiveRunPermit与操作者入口测试

对每一种外部副作用至少执行下列blocker tests：

- 只有activation dependency PASS但无EEA/permit；
- 只有EEA、直接把EEA交给adapter，或permit不是parent的不可扩权子集；
- wrong action/site/DB/profile/role/input/sink、过期/撤销、超额、重复ordinal、stale fence；
- reserve与dispatch不原子、消费后重放、unknown-start额度被错误释放；
- 首次DB bootstrap没有在D盘ledger中以同等语义reserve/consume；
- `epoch resume`、Redis `queue rebuild`、reconcile apply、Schema apply、模型/Solver dispatch或active release变更不带permit；
- 安全优先的`pause/stop/kill-switch/quarantine`被错误要求新permit而无法止损。

`OperatorCommandRegistry`必须逐条驱动CLI/API/worker入口合同测试：command ID、read-only/side-effect分类、required EEA/permit/Gate、应用服务、最终Port、幂等键、fence、receipt和退出码都与实际调用图一致。命令帮助、Schema、operations、CLI parser、HTTP/worker API和registry做双向集合比较；未登记入口、登记但不可达命令、直调provider/DB/Redis/HumanGate或任一remainder非0都不得通过。

EEA/Permit/Receipt还必须执行序列属性测试：生成任意合法parent EEA后，Permit缩小任一维度仍可通过，扩大任一维度必失败；并发reserve同一ordinal时恰有一个成功；任意crash point重放后`initial allowance = remaining + consumed + held`始终成立。该等式按action、currency和计量单位分别成立，不能用总数互相抵消。

## 科学协议测试

- taxonomy snapshot漂移后旧recognition/selector仍被错误接受；
- TellManifestation/观察措辞被当成TellCore因果身份；
- Tell↔Hint M:N关系被压成一对一或旧Evidence改外键；
- oracle Tell有效被错误写成automatic selector PASS；
- renderer/selector升级被错误归因给TellCore；
- HintInstance泄漏binding/lemma/证明骨架；
- 原截断bare被错误当主baseline；
- guided多一次调用或更多token；
- lineage/direction/distractor文本长度混杂；
- injection位置没有位置内neutral；
- selector abstain/错选被过滤；
- single episode直接生成因果Evidence；
- same source变体当独立样本；
- token-limit与认知失败混合；
- calibration题进入确认性Evidence；
- holdout重复使用；
- off-mechanism proof冒充Tell证据；
- positive only、无false-friend/boundary拒绝。

## 恢复场景

每个边界至少注入一次：

1. attempt记录前/后；
2. provider accepted前/后；
3. generation started前/后；
4. raw event写入中；
5. writers drained前/后；
6. partial验证中；
7. marker/fsync/rename前后；
8. DB事务前后；
9. outbox publish/ACK前后；
10. HumanGate提交前后；
11. checkpoint与shutdown中。

每个场景必须断言：科学样本数、attempt lineage、artifact数量、DB状态、queue状态、允许恢复动作和禁止动作。

对每个真实ModelRole adapter还要分别注入：accepted物证丢失、generation-start物证丢失、provider ID已落盘但worker崩溃、event stream半条JSON、cancel ACK丢失、reattach返回旧attempt、credential撤销、Vault写满和carrier-global limiter耗尽。预期动作必须在测试前冻结为`reattach/reconcile/quarantine/known-pre-accept retry`之一；任何场景都不得隐式fallback。

## Golden Slice验收场景

- 自然题完整路径；
- 生成题使用Devin Question Architect；
- 生成题使用Codex Question Architect；
- statement-only审稿和独立核验；
- RoleTypeRegistry与两个adapter各自的资格矩阵/completeness receipt；
- problem-only bare准入成功题与失败题都保留；
- P4/P5等资源矩阵；
- Process/Proof/Leakage三审；
- correct Tell vs distractor；
- false-friend/boundary拒绝；
- NO_CHANGE或一次真实revision分支；
- 中途kill/restart；
- Evidence replay/remainder=0。

## PASS规则

- Blocker test失败 → 工作包FAIL，不可用confidence test平均抵消；
- 协议损坏 → `INCONCLUSIVE_DUE_TO_PROTOCOL`，不能硬写科学FAIL；
- 功能负结果但协议有效 → 合法科学负证据；
- skip只有在spec允许且写明scope时成立；
- 架构`PORT_COMPATIBLE`、协议`PROTOCOL_COMPATIBLE`、CANARY PASS和PRODUCTION PASS不得互相升级；
- RoleQualificationMatrix存在缺口、通配符或失效cell时，相关阶段最多`PARTIAL/BLOCKED`，不得以adapter import或代表性调用补足；
- usage scope不完整、provider billed amount不可观察或pricing snapshot缺失时，正式成本结论fail-closed；原始usage仍按观察值保留；
- 实施者运行的测试只能支持`READY_FOR_AUDIT`，独立复跑后才支持`AUDITED_PASS`。
