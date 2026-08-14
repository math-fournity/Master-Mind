# D盘、CAS、Vault、数据库与事件投影

## 一句话结论

D盘保存大对象和受限内容；Arango保存小型身份、状态、事件、索引和artifact引用；Redis只做可重建调度投影。任何一层都不能成为另一层丢失真值的借口。

## 存储分工

| 层 | 保存什么 | 不保存什么 |
|---|---|---|
| Git repo | 代码、Schema、docs、tests、非密钥示例 | run artifact、答案、日志、live配置 |
| D盘 CAS | WP-GV0复用并硬化v0.1 artifact store为最小CompletionArtifactStore，WP-VLT0复用同一核心扩展为immutable raw events、trajectory、proof、audit、bundle存储 | 可变队列状态；平行第二bundle store |
| D盘 Vault | 答案、holdout、candidate solution、solution-bearing调用 | 普通worker可读内容 |
| Arango隔离且版本化的`seven_*_vN` | ID、WorkEvent、Gate、hash、ref、ledger、outbox；v1只作bootstrap/scaffold，v2+承载经批准的原子结构 | 大型正文、密钥、答案blob；题海/`system/`集合 |
| Redis `evidence:seven:*` | lease-ready队列、优先级、心跳投影 | 历史真值、唯一结论 |

## Artifact提交

WP-GV0复用并硬化v0.1现有D盘append-once artifact-store代码为最小CompletionArtifactStore，只实现普通工作包完成包所需的content-addressed append-once提交、hash/byte校验、原子rename与路径逃逸/fallback拒绝，并用于自托管GV0自己的ImplementationCompletionBundle。它不接受模型/Solver artifact或答案。WP-VLT0必须在同一CAS代码与数据命名空间上补齐下述live/partial/seal、Vault、ACL/view和reconcile合同；若另建第二套完成包store，VLT0必须FAIL。

```text
writer live root
→ WRITERS_DRAINED
→ copy to <attempt>.partial
→ validate files/size/schema/hash
→ artifact_manifest.json
→ DB fenced transaction records durable CommitIntent
→ fsync COMMITTED marker + directory
→ atomic rename to content-addressed final bundle
→ DB fenced transaction writes ArtifactRef + COMMITTED + outbox + permit consumption
→ queue ACK
```

final bundle不可再改。marker不参与manifest hash，但必须携带manifest hash。`CommitIntent`必须在final rename前用有效fence与当前permit持久化，至少绑定job、attempt、input hashes、manifest hash、预期terminal、目标CAS URI、authorization/permit hash和expiry。若DB已经声称terminal但artifact缺失或hash不符，必须QUARANTINE，不能伪造空bundle；“CAS已seal但DB尚未提交”只允许走下述受限reconcile。

CAS存在而DB未提交时，Reconciler**只能**在以下全部成立时补DB：

1. 存在未消耗、未撤销的durable `CommitIntent`；
2. intent的fence仍是该aggregate当前有效fence；
3. job/attempt/input view/manifest/CAS URI与sealed bundle逐字段、逐hash相等；
4. 预期terminal对该WorkItem kind合法，且没有cancel/quarantine/更高fence事件；
5. `ExternalExecutionAuthorization/LiveRunPermit`在dispatch时合法且未被追溯撤销，相应consumption处于`RESERVED`/`UNKNOWN_START_HELD`而非可重用状态；
6. 补交使用单个expected-revision transaction同时完成ArtifactRef、WorkEvent、WorkItem、Outbox和AuthorizationConsumptionReceipt。

任一条不成立就产生RecoveryRecord并QUARANTINE；不得因为文件“看起来完整”就猜测业务提交意图。

## Vault与view

Vault对象至少记录：

- content hash、size、media type；
- sensitivity：public/restricted/solution_bearing/holdout_bearing；
- owner case/release/invocation；
- allowed roles、purpose、expiry/revocation；
- source artifact和derivation rule；
- access event append-only ledger。

公开view必须由纯程序从sealed source机械派生并单独hash。把答案和题面放同一JSON再删字段，不算物理隔离。

### deny-by-default访问链

一次读取或写入不是“拿到路径再自行打开文件”，而是下面四个机器对象组成的一次性访问链：

```text
VaultAccessCapability（issuer签发的最小能力）
→ AccessDecision（逐请求、逐nonce重新验签和查撤销）
→ ViewDerivation（sealed source → 精确view → 精确sink）
→ AccessEvent（append-only结果账）
```

- [`vault-access-capability.v1.schema.json`](vault-access-capability.v1.schema.json)精确绑定principal、单一operation、object ID/hash、view ID/hash/policy hash、sink ID/kind/policy hash、时窗、nonce、issuer和revocation handle。能力没有`READ_RAW_OBJECT`操作，也没有raw path字段；`deny_by_default`只能为`true`。
- [`access-decision.v1.schema.json`](access-decision.v1.schema.json)必须重验capability签名与issuer trust，并逐字段比较principal/operation/object/view/sink，检查时窗、nonce replay和最新revocation registry。只有全部检查`PASS`、revocation=`ACTIVE`才能`ALLOW`；撤销状态未知也必须`DENY`。
- [`view-derivation.v1.schema.json`](view-derivation.v1.schema.json)冻结source hash、规则/生成器/redaction manifest hash、derived view hash、sink write receipt和仍有效的revocation检查。模型交付模式只能是`OPAQUE_HANDLE_AND_DERIVED_BYTES`，且声明raw locator与capability token均未暴露。
- [`access-event.v1.schema.json`](access-event.v1.schema.json)保存相同principal/operation/object/view/sink/nonce绑定、decision/derivation/receipt refs、revocation snapshot、sequence和previous-event hash。`ACCESS_GRANTED`缺任何derivation或sink receipt均不合法。

模型、Target Solver和其他不可信worker从来不拿raw Vault filesystem路径、CAS/Vault URI、源object locator、签名私钥、capability bearer或revocation handle；这些只存在于Vault broker可信控制面。worker只得到派生bytes与opaque `view_id/sink_id`，且opaque ID不能被解析成路径。输出可能含solution/holdout时，也由broker把worker输出流直接写入能力指定的restricted sink，不能先落普通workspace或日志再搬运。

`VaultAccessCapability`、`AccessDecision`和`ViewDerivation`可作为小型canonical record保存；`AccessEvent`是独立安全账，不是`WorkEventTypeRegistry`的自由扩展。生产持久化必须原子保证`issuer+nonce`不重放、ledger sequence唯一、撤销在ALLOW前可线性观察、decision/event不可覆盖；若`seven_records_v1`及已批准的`seven_*_vN`高版本结构不能证明这些约束，WP-VLT0/DB1I必须发布专用索引/集合的新版MigrationSpec，live Vault保持`BLOCKED`。

## 逻辑数据库

Seven复用`xishujuzhen_math_glm52`，但只使用匹配`^seven_[a-z0-9_]+_v[1-9][0-9]*$`且经批准的集合/索引。`seven_*_v1`只允许bootstrap/scaffold；HumanGate、外部模型、Solver、canonical Epoch或active release的live状态必须使用04号规定的`seven_*_v2`或更高版本原子结构。所谓“等价结构”只允许在该版本化Seven命名空间内选择不同专用集合/索引设计，不允许复用题海/`system/`集合或无版本集合。只有`seven_system.database.StrictDatabasePort`的批准Arango backend可以封装raw client。

### WP-DB1L只读能力

先验证：

- env/config精确数据库名；
- 连接后的`CURRENT_DATABASE()`；
- endpoint/server/driver/principal fingerprint；
- 只读权限和catalog；
- canonical集合/索引冲突；
- 零写入计数和网络调用物证。

### WP-DB1I写入能力

DB1I只接受以下冻结输入：DB1L的`DatabaseLogicalSiteCapabilityReport`与零写入收据、`ObjectPersistenceMapping + IndexAdequacyReport`、版本化MigrationSpec、WP-GV0验证器能力、VLT0 D盘/CAS能力、HG0签名Gate能力，以及绑定精确site/plan/actions的EEA→Permit→`RESERVED`链。真实Schema初始化必须有：

- deterministic plan与hash；
- target site fingerprint；
- HumanGateDecision；
- expiry、fence和maintenance window；
- durable action ledger；
- 每个DDL前/后状态；
- resume/reconcile；
- post-verify receipt。

DB1I的完成输出严格限定为`DatabaseSchemaStateReport + SchemaBootstrapReceipt + SchemaBootstrapImportAnchor`及逐action收据；它只拥有SecurityContractVerifier的`SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER`原子预留后端。它不得输出`DatabaseRuntimeCapabilityReport`、`ArtifactCommitReconcileCapabilityReport`或以Schema一致性替代事务/outbox/reconcile能力。配置`allow_writes=true`不是授权；直接调用内部函数也不能绕过permit。

### Schema bootstrap：Seven集合尚不存在时

`seven_schema_migrations_v1`不能记录它自己被创建之前的事件。首次Schema apply因此必须使用D盘外部bootstrap真值，禁止使用repo文件、`/tmp`、内存flag或“集合已出现”的事后推断代替：

```text
/data/seven-system-data/bootstrap-ledger/<site-fingerprint>/<plan-hash>/
├── bootstrap-plan.json
├── live-permit.json
├── fences/<ordinal>-<fence-id>.json
├── events/<monotonic-sequence>-<event-id>.json
├── receipts/<action-id>.json
└── root-seal.json
```

bootstrap协议：

1. 只读catalog生成deterministic plan，冻结site/DB/principal/spec/catalog/plan hash和精确DDL actions；
2. `G-DB-SCHEMA-APPLY`产生针对该plan hash的`LiveRunPermit`，内含maintenance window、最大actions、expiry和nonce；
3. 在D盘用atomic create建立唯一`SchemaBootstrapFence`；竞争者必须BLOCK，过期fence也必须先人工授权并reconcile所有旧事件才能接管；
4. 每个DDL前先append并fsync `ACTION_INTENT`，执行后append并fsync catalog observation与`ACTION_VERIFIED/ACTION_FAILED/UNKNOWN_OUTCOME`；每个entry包含previous-entry hash；
5. 继续前重读整条ledger与实site catalog；`UNKNOWN_OUTCOME`不得盲重放DDL，必须按catalog事实reconcile；
6. 全部actions验证后生成`SchemaBootstrapReceipt`和外部`root-seal`，二者绑定ledger root hash、permit consumption、post-catalog hash与fence；
7. `seven_schema_migrations_v1`可用后，将plan/events/receipts按原hash导入，生成`SchemaBootstrapImportAnchor`；anchor同时记录D盘root seal和DB导入record IDs/hash列表；
8. 正反向校验集合完全相等后才可完成bootstrap。D盘ledger仍永久保留，不得因已导入DB而删除。

该文件fence只支持经能力门验证的单站点bootstrap，不宣称通用分布式锁。多主机apply必须先增加具有一致性保证的外部lock/fence provider及新CapabilityReport。

### 三个不可合并的运行能力报告

| Report | 必须真实证明 | 不能代替 |
|---|---|---|
| `DatabaseSchemaStateReport` | site fingerprint、DB identity、spec/plan hash、全部collection/index实际snapshot、额外/缺失/语义冲突为0、bootstrap/import anchor可达 | DB transaction/outbox/recovery能力 |
| `DatabaseRuntimeCapabilityReport` | 受限principal只写`seven_*`、expected-revision transaction/CAS、WorkEvent sequence、lease/fence、outbox、duplicate delivery、Redis rebuild和关键崩溃恢复 | Schema已正确apply、CAS/Vault已安全 |
| `ArtifactCommitReconcileCapabilityReport` | CommitIntent、permit reserve/consume、partial→seal、fsync/rename、CAS/DB双向对账、stale fence/cancel/revocation拒绝和单边崩溃的真实恢复 | DB identity、Solver/ModelRole或答案隔离 |

三种报告共享的canonical envelope至少包含`report_id / capability_kind / subject_profile_hash / site_fingerprint / database_identity_hash / source_code_and_schema_hashes / probe_plan_hash / started_at / completed_at / valid_until / probe_results / positive_and_negative_evidence_refs / residual_risks / verdict / verifier_identity`。`verdict`只能由版本化判定器从逐项probe派生；手填`PASS`、省略失败case或复用不同site/profile的报告均无效。

P0必须按本Epoch实际使用的Schema/runtime/artifact profile精确引用三份报告。任一份缺失、过期、subject hash不匹配或只有离线spec test时，live lane保持`BLOCKED`。

### DB1I → RT1闭合交接

RT1只能消费DB1I输出且仍有效的`DatabaseSchemaStateReport + SchemaBootstrapReceipt + SchemaBootstrapImportAnchor`，并同时冻结VLT0 CAS/Vault能力、WP-GV0 verifier接口与site/spec/plan/DAG hashes；不得接受模糊的“Schema/runtime capability”合并输入。RT1拥有SecurityContractVerifier唯一的canonical Arango expected-revision transaction reservation backend，并实现WorkEvent、lease/fence、outbox、CommitIntent、artifact/DB reconcile与Redis可重建投影。

RT1的完成输出严格限定为`DatabaseRuntimeCapabilityReport + ArtifactCommitReconcileCapabilityReport + RuntimeCheckpoint/recovery receipts`；它不得重发、推断或替代DB1I的`DatabaseSchemaStateReport`。任一输入hash漂移、bootstrap/import集合不相等、原子预留backend未通过重复ordinal/额度守恒故障测试，RT1必须`BLOCKED`，所有模型、Solver、正式HumanGate与QA0真实纵切继续禁止激活。

## WorkEvent与outbox

Work状态只由append-only event推导。至少包含：

```yaml
event_id:
aggregate_id:
expected_previous_sequence:
sequence:
event_type:
payload_hash:
fence_token:
created_at:
actor_or_rule:
```

outbox与状态事件同一DB事务提交，unique key绑定aggregate revision。published/ACK失败只影响投影，不影响真值；Redis可从event/outbox重建。

## 数据库与CAS对账

Reconciler必须识别：

- live writer仍活；
- partial且writer已死；
- sealed artifact、DB未commit；
- DB已commit、artifact缺失或hash不符；
- 多个attempt声称同一科学样本成功；
- outbox未投影或重复投影；
- stale fence晚提交；
- sealed对象被外部改写。
- CommitIntent缺失/过期/撤销，或与job/attempt/input/manifest不符；
- permit consumption超额、重放、`RESERVED`占用与unknown-start无法对账；
- bootstrap D盘ledger与DB import anchor的正反向集合差异。

每种状态产生RecoveryRecord，不得自动任选“看起来最好”的输出。

## D盘与Arango当前事实

- 批准的大对象根：`/data/seven-system-data/`；
- Arango物理字节经OrbStack `data.img.raw`由D盘承载；
- engine仍在容器writable overlay，未使用专用`/data/arangodb/data:/data` bind；
- 这不等于逻辑site、Seven Schema或写能力已经PASS。

## 必须测试的攻击

- volume/data_root/epoch/leaf祖先symlink逃逸；
- 路径fallback到repo/Home/`/tmp`；
- D盘掉线、UUID变化、磁盘满；
- manifest、index、receipt协调重写；
- wrong DB、默认DB、读时DDL；
- extra/非persistent索引漂移；
- apply前后崩溃、重复apply和旧fence；
- CAS/DB单边提交；
- Redis全丢与重复delivery；
- Vault越权、view derivation hash不一致；
- capability/decision/event的principal、operation、object hash、view hash、sink或nonce任一不一致；
- 已撤销/过期capability、revocation lookup未知、nonce重放或AccessEvent sequence冲突仍被ALLOW；
- 模型输入、argv、env、workspace、stdout/stderr或工具参数出现raw Vault路径、源object locator或capability token；
- 无CommitIntent的sealed CAS、stale fence或已撤销permit试图补DB；
- bootstrap每个DDL前/后崩溃、unknown outcome、fence接管、ledger断链和import anchor差异；
- SchemaState PASS试图解锁Runtime，或Runtime PASS试图解锁Artifact Reconcile。
