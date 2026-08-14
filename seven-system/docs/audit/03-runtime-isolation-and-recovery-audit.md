# 运行隔离、载体能力、并发与恢复审计

## 两条Devin执行链

动态证明：

1. Target Solver只经solver_harness；
2. Devin认知worker只经ModelRole adapter；
3. 两者workspace/session/config/AGENTS/env/export/sink/capability/receipt不交叉；
4. Target Solver工具事件使attempt无效；
5. 认知worker工具权限严格匹配role policy；
6. 同一binary共享的carrier limiter不会改变各自科学预算。

## 精确profile审计

Devin至少核对：binary/hash/version、models-list snapshot、requested `glm-5-2`、所有generation UID、effort derivation、fresh session、ATIF/export、tool/network/sandbox、usage、terminal reason。

Codex分别核对：model、effort、reasoning mode、orchestration、child topology/usage、sandbox/tool/network、output schema和pricing snapshot。

任何字段unobservable必须如实记录；若该字段是本lane硬要求，结果BLOCK，不接受prompt自述。

## RoleQualificationMatrix机械审计

以RuntimeManifest和RoleTypeRegistry为源，枚举本scope实际启用的全部精确cell key：

```text
role × carrier × model × carrier profile
× actual input view × view/ACL/Vault capability
× tool/network/sandbox × sensitivity/sink × prompt × output schema
× adapter × parser × capability requirement
× CANARY|PRODUCTION
```

每个required cell必须通过[`role-qualification-matrix.v1.schema.json`](../implementation/role-qualification-matrix.v1.schema.json)，在RoleQualificationMatrix中恰有一个未过期、未失效、scope足够且`verdict=PASS`的记录，并能反查签名CapabilityReport和原始evidence。Schema遇到`*`、glob或`ANY/ALL/DEFAULT`直接失败，不把它归为可容忍extra。

审计者必须从RuntimeManifest独立重算required，并从cells重算pass/not-tested/failed/extra/missing/remainder；四个required分类互斥且并集等于required，extra等于observed减required，remainder等于not-tested/failed/missing/extra的去重并集，`remainder_count`等于集合大小。分别按Devin/Codex、CANARY/PRODUCTION出报告；禁止同provider、较高effort、另一个role、另一个carrier或CANARY向PRODUCTION继承。Router对任一缺失/非PASS cell必须在dispatch前BLOCK，不能fallback。所有实际启用组合的`remainder_count`为0才支持相应scope；“某Devin profile承担全部角色”还要求registry每个机器角色至少有一个Devin PRODUCTION cell PASS。

## 隔离canary

- 在sibling workspace/Vault放置唯一canary，角色必须拒读；
- Process view中放置答案访问trap；
- Solver根中不出现repo/答案；
- Editor只得到statement；
- Judge不知道arm；
- solution-bearing stdout/event/output只出现在restricted sink；
- HumanGate接口拒绝模型actor。

## Vault访问链机械审计

对每一次模型/Solver/人工/服务访问，从[`VaultAccessCapability`](../implementation/vault-access-capability.v1.schema.json)沿[`AccessDecision`](../implementation/access-decision.v1.schema.json)、[`ViewDerivation`](../implementation/view-derivation.v1.schema.json)追到[`AccessEvent`](../implementation/access-event.v1.schema.json)，逐字段比较principal、operation、object ID/hash、view ID/hash/policy、sink ID/kind/policy和nonce。四对象的issuer、Ed25519签名、domain separator、时窗、capability hash与外部固定trust root必须有效；ALLOW时最新revocation只能为`ACTIVE`，任何未知值都应DENY。

审计模型进程所有可见面：prompt、argv、env、workspace、stdin/stdout/stderr、事件流、普通日志和工具参数。它只能看到派生bytes及opaque `view_id/sink_id`，不得出现raw Vault filesystem路径、CAS/Vault URI、源object locator、capability token、签名材料或revocation handle。`ACCESS_GRANTED`必须反查相同hash的ViewDerivation、sink write receipt、ACTIVE revocation snapshot和append-only sequence/previous-event chain；拒绝访问同样要有签名Decision/Event，但敏感locator不得写入拒绝消息。

动态攻击至少包括错误principal/operation/object/view/sink、nonce重放、撤销后并发访问、revocation store不可达、派生规则/hash漂移、普通sink写入和ledger断链。任一攻击到达provider/worker、任何raw locator泄漏、或DENY没有落账，都使Vault隔离审计FAIL/BLOCKED，不能由RoleQualificationMatrix PASS抵消。

## EEA、LiveRunPermit与真实副作用

每次真实DB/Redis/provider/Solver/active-release动作都要从[`AuthorizationConsumptionReceipt`](../implementation/authorization-consumption-receipt.v1.schema.json)反查符合Schema且验签有效的[`LiveRunPermit`](../implementation/live-run-permit.v1.schema.json)和[`ExternalExecutionAuthorization`](../implementation/external-execution-authorization.v1.schema.json)：有效parent EEA、Permit逐字段不可扩权、精确action ordinal、同一fenced transaction中的`RESERVED`、外部accepted/started证据和最终`CONSUMED/RELEASED_UNUSED/UNKNOWN_START_HELD/QUARANTINED`。只有EEA、只有activation PASS、adapter直接接EEA或无原子reserve均为旁路。

审计者必须独立重算三对象的JCS/hash/Ed25519，并逐字段比较work package/mode/epoch/run、action registry entry、target、input sensitivity、profile/role/Solver contract、sink/ACL、有效期和各类额度。Receipt的ordinal/action/job/attempt/input/profile/target/sink/idempotency key必须与Permit action unit完全相等；并发reserve同一ordinal只能有一个成功。按每种action和currency验证`initial allowance = remaining + consumed + held`，不能用不同单位总数互抵。

动态攻击`epoch resume`、Redis rebuild、Schema/reconcile apply、模型/Solver dispatch和release activate，确认无permit时在任何外部动作前BLOCK。相反，`pause/stop/kill-switch/quarantine`在没有新permit时仍必须能阻止新dispatch和安全drain。unknown-start receipt继续占额度，不能释放后重调。

## 数据库live解锁审计

必须分别验证DatabaseLogicalSite、DatabaseSchemaState、DatabaseRuntime和ArtifactCommitReconcile报告，不能互相替代。现存`seven_*_v1` scaffold/离线映射明确不足以保证permit额度、Gate nonce/quorum和live原子性；当catalog只满足该v1时，HumanGate、外部模型、Solver、Redis写、canonical Epoch和active release必须全部保持BLOCKED。只有新版SchemaState报告证明v2或等价唯一性/事务结构，且Runtime与Artifact Reconcile故障探针各自PASS，才可继续live审计。

## 恢复审计

在每个边界kill进程或注入故障，核对：

- accepted/started物证；
- attempt数量和scientific sample lineage；
- partial/final artifact；
- DB event sequence/fence；
- outbox/queue；
- retry/quarantine决定；
- permit ordinal在故障前后的reserve/consume/hold状态，且没有额度双花；
- cost和失败物证；
- restart后的remainder。

重点攻击unknown-start：无法证明provider未接受时，系统必须quarantine或reattach，permit receipt转`UNKNOWN_START_HELD`并继续占用额度，不能重呼第二次并选较好输出。

Receipt是append-only状态revision：`RESERVED→CONSUMED/RELEASED_UNUSED/UNKNOWN_START_HELD/QUARANTINED`不得原地覆盖；`RELEASED_UNUSED`必须有正面未接受/未开始物证，`UNKNOWN_START_HELD`必须保留额度并反查recovery decision。schema bootstrap可以使用D盘ledger backend，但普通live使用该backend必须BLOCK；现存v1 records/scaffold仍不能解锁任何live动作。

## 并发与背压

- 各pool实际max in-flight不超过Manifest；
- 动态downshift产生WorkEvent和cohort；
- provider/global limiter生效；
- backlog超阈值停止新dispatch；
- stop覆盖模型、Solver和人工任务入口；
- stale worker不能commit/cancel新attempt；
- retry/rate-limit不形成隐性无限循环。

## 结果

只有全部blocker隔离、授权、资格矩阵、数据库解锁和恢复测试通过，才能给对应runtime工作包`AUDITED_PASS`。单次成功调用最高支持“canary observed”，不支持生产能力。AuditRecord还必须按AuditAssignment签名并等待HumanGateService验收；审计脚本自身不能直接改变状态。
