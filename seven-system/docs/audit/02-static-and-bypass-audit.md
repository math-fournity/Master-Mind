# 代码、Schema与旁路审计

## 目标

证明所有有副作用或敏感权限的动作只能经过规定端口，并且报告、Schema和状态不能被调用者伪造。

## 静态搜索

审计者应当使用`rg`/AST/import检查确认：

- raw `ArangoClient`只在批准backend；
- Redis client只在投影adapter；
- `solver_harness`只由DevinSolverAdapter调用；
- Seven源码内直接`devin` binary只允许由`DevinCliModelRoleAdapter`调用；`DevinSolverAdapter`只能调用`solver_harness`，由Seven外部既有Harness内部封装binary；
- `codex`/Responses SDK只在Codex adapter；
- phase/Case/Audit模块不直接`subprocess`调用provider；
- ModelRole代码不调用HumanGate决定接口；
- application service、CLI、HTTP/worker handler和adapter都不能直接消费`ExternalExecutionAuthorization`；LiveRunPermit必须经受信任签发路径成为EEA的不可扩权子集，composition root只负责验签/验subset并原子reserve，adapter只接收已预留permit ordinal；
- `epoch resume`、Redis rebuild、Schema/reconcile apply、模型/Solver dispatch和active release变更都经OperatorCommandRegistry标为外部副作用并走permit；`pause/stop/kill-switch/quarantine`不能被permit缺失阻断；
- AuditAssignment只能由受信任owner路径创建，AuditRecord不能由实现者自签后直接改变状态；
- attestation私钥及signing agent不可被模型workspace、被审repo或实施者进程读取；AttestationSignerPort只签Assignment绑定的auditor/subject/scope/canonical bytes；
- canonical DAG中`owner_type=AUDITOR`或`completion_contract=AUDIT_RECORD`的节点拒绝ImplementationCompletionBundle和实施者状态命令；
- 没有repo/Home/`/tmp`的fallback写路径；
- 没有artifact overwrite/delete/GC生产入口；
- 没有答案正文进入DB或普通日志；
- 没有硬编码PASS、测试数、费用或model effective字段。

## Schema/semantic攻击

对每个对象至少尝试：

- 删除required字段；
- 添加unknown字段；
- 错类型、空值、非法enum、NaN/Infinity；
- 伪父hash、错Schema version、错对象类型；
- 合法JSON但跨字段矛盾；
- 重算内部hash/index但不更新信任锚；
- PASS claim与side effects/状态矛盾；
- malformed check IDs导致verifier异常；
- 重复check、缺required evidence、伪test receipt；
- 错profile report解锁另一role/effort。
- 只有现存`seven_*_v1` SchemaState或离线contract却解锁HumanGate、live调用、Solver、Redis写或canonical Epoch；
- EEA被当成可消费permit、permit扩大parent scope、重复ordinal、错action/input/profile/sink或状态跃迁绕过原子reserve/consume；
- CompletionBundle反向包含后生成的evidence-index commit，或AuditRecord没有同时绑定subject/bundle/index三者；
- 单一AuditRecord总分掩盖`implementation/factory/scientific/production_scale`任一轴FAIL/BLOCKED。
- AuditAssignment缺repo外channel/root/roster/policy/audit plan，AuditRecord缺root source/time/receipt、attestation key或finding→axis引用，却仍被Schema/semantic verifier接受；
- `EXTERNAL_SIDE_EFFECT` registry entry把EEA/permit设false、action entry设null、原子reserve设false或final Ports/receipts留空；
- EEA/Permit/Receipt只通过单对象Schema，却在parent subset、ordinal唯一、额度守恒、时间、fence或append-only revision上矛盾。

Verifier必须fail-closed并返回结构化错误，不能TypeError崩溃或跳过检查。

## HumanGate信任根与审计身份攻击

- 审计者必须保存从站点owner repo外渠道观察到的pinned root hash；被审repo/DB/bundle内的root只能作为待比较对象，不能反向成为信任来源；
- 整体替换root、roster、policy和bootstrap receipt，即使内部hash闭合，仍必须因外部pin不符而BLOCK；
- 用独立实现重算RFC 8785 JCS signed bytes和domain separator，攻击未知算法、错key、过期、撤销、rotation断链、nonce重放、换task/payload/actor、quorum/conflict/separation；
- AuditAssignment必须绑定repo外channel/root/roster/policy、精确subject commit/tree、CompletionBundle、可选index commit、audit plan/spec、auditor principal/key、四轴scope、期限和nonce；实现者自建、过期、扩大scope或替换key一律拒绝；
- AuditRecord必须由assignment中的attestation key经AttestationSignerPort签名。审计者修改被审树、签名后改finding/verdict/scope、finding没有反向进入受影响轴，或没有HumanGate验收时，不得写`AUDITED_*`；
- 对Assignment、AuditRecord、EEA、Permit分别按07号文档移除精确自引用字段，重算domain+RFC8785 JCS signed bytes；对ConsumptionReceipt重算service attestation。仅验证对象自报hash不能通过。

## OperatorCommandRegistry与入口remainder

从registry正向遍历每个entry到CLI/API/worker binding、Command Schema、application service、Gate/permit、最终Port和receipt；再从全部parser/router/handler反向遍历回registry。至少攻击：

- 帮助中存在但registry缺失、registry存在但实现不可达、同一operation在CLI与HTTP分类不同；
- `READ_ONLY`实际写DB/Redis/CAS或调provider，`SAFETY_ONLY`偷偷resume/rebuild/activate；
- `EXTERNAL_SIDE_EFFECT`的Schema conditional未把EEA、permit、action registry entry、fence和原子reserve固定为必需；
- 内部service method、测试后门、admin flag、插件或queue consumer绕过公开CLI直接执行副作用；
- 相同request ID不同input不冲突，重复请求产生第二次副作用，或退出码/receipt与registry不符。

Operator Surface Projection的未登记入口、孤儿entry、分类差、缺permit、缺receipt和不可达Port计数必须全部为0。

## 路径攻击

- leaf/ancestor symlink；
- `..`、casefold、unicode、hardlink；
- approved root是repo祖先/子目录；
- mount被同名普通目录替代；
- D卷device变化；
- existing fast-path绕过bounded read；
- partial/final marker与manifest不一致。

## 配置与环境攻击

- wrong/secret-like `ARANGO_DB`且日志不泄密；
- `PYTHONPATH/PYTHONHOME/PYTHONSTARTUP/sitecustomize`注入；
- provider user config/global rules污染；
- unknown config字段；
- env继承密钥超出allowlist；
- binary path被替换、版本/hash漂移；
- model catalog snapshot被替换。

## 输出

Static Table每行记录：requirement ID、搜索/攻击方法、实际证据、结果、finding、剩余未检查面。没有“未发现”而无命令/范围的结论。
