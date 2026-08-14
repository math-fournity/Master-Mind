# D 盘与数据库契约

## 一句话结论

Repo 只保存代码、Schema、运行资产、文档和测试；大对象、Epoch 运行产物和日志必须位于经批准的 D 盘数据根，ArangoDB 只应保存可查询元数据、事件和大对象引用。答案 Vault 仍是未来能力，目录名不能冒充隔离能力。

## 当前站点事实

2026-08-14 的站点核对结果。这里必须同时看容器路径、OrbStack虚拟磁盘和macOS宿主卷，不能只看其中一层：

- `/data` 正常挂载；
- APFS，稳定 Volume UUID 为 `C293C841-DD80-4EFF-9AE4-EA7D826FBE20`；设备节点只作为当次观测，不作为稳定身份；
- 根目录可见现有 ArangoDB、Redis、Solver workspace 和 trajectory 数据；
- `/data/README.md` 已创建并记录卷角色、边界与 Seven 数据根；
- `/data/seven-system-data/` 已创建为真实目录，未用 symlink，也没有自动创建尚未实现的 Vault/CAS/Solver 子目录；
- 真实 `dry_run` preflight 已 PASS；这只关闭站点目录前置条件，不检查 live DB 物理落盘能力；
- 容器层：Arango实际engine data directory是`/var/lib/arangodb3`，位于容器writable overlay；配置的`/data/arangodb/data -> /data`专用bind为空且未被engine使用；
- OrbStack层：其group-container data symlink指向`/data/OrbStack/data`，OrbStack说明该目录的`data.img.raw`承载全部Docker images、containers和Linux machines；
- 宿主层：实时OrbStack进程正打开`/data/OrbStack/data/data.img.raw`，该文件由D卷设备承载。因此Arango物理字节在D盘，但不是通过Arango专用bind承载。

因此，Seven的站点存储根门可以PASS，Arango宿主物理D-backing记为`A-WP1-D=PASS`；未使用专用bind记为`A-WP1-BIND=WARNING_NOT_DEDICATED`。这两个状态都不证明Seven逻辑site核验或Schema初始化能力。当前工作没有停止、重启、重建共享ArangoDB，也没有连接或写入数据库；生产题海系统没有被改动。

## 建议物理布局

未来每项能力分别实现并通过 Gate 后，建议逐步形成：

```text
/data/seven-system-data/
├── epochs/                   每个有限Epoch的人类可读导出
├── receipts/                 Epoch外local append-once index锚；当前非WORM
├── live/                     尚有writer的运行目录
├── staging/                  校验中的.partial bundle
├── cas/sha256/               sealed内容寻址对象；append-only
├── logs/                     控制面与worker结构化日志
├── quarantine/               冲突、污染和不可审物证
└── vault/                    逻辑入口；真实权限必须另做能力验证
```

其中 `staging` 和 `cas` 必须在同一个文件系统，才能在 fsync 后原子 rename。当前只批准并创建了数据根本身；空目录不证明 CAS、Vault、WORM 或权限隔离。禁止自动 fallback 到 repo、Home 或 `/tmp`。

### 当前 CLI 会创建什么

`init-epoch` 只在**已经存在且可写**的 `data_root` 下创建：

```text
epochs/<epoch_id>/
├── runtime-manifest.json
├── preflight-report.json
├── phase-plan.json
├── runbook.md
├── logging-contract.json
├── scenario-matrix.json
├── runtime-checkpoint.json
├── runtime-checkpoints/      append-only后续checkpoint
├── gate-decisions/           append-only GateDecision
├── evidence-index.json
├── verdict.json
├── integrity-index.json      初始文件seal
├── dry-run-report.json       P1完成后才出现
├── p1-verdict.json           P1 scaffold结论
├── p1-integrity-index.json   P1文件seal并链接初始index
├── summary.md
├── alerts/
├── artifacts/
├── audits/
├── evidence/
├── ledger/
├── quarantine/
└── revisions/
```

它不会创建 `data_root` 本身，不会连接数据库，也不会启动 Solver。

`wp1-db-contract-report` 还会在受控测试和语义验证全部通过后，append-once创建：

```text
capabilities/strict-db-contract/<report-id>.json
```

这是本地离线契约报告，不是DB site capability、WORM或外部信任根；报告命令不会连接ArangoDB。所谓append-once只指Seven API拒绝覆盖，拥有直接磁盘写权限的人仍可能改写文件。

初始化与P1完成时还会在`data_root/receipts/`各写一份不可由Seven API覆盖的local receipt，用来阻止只重算Epoch内部index的篡改。其`trust_scope=LOCAL_APPEND_ONCE_API_NOT_WORM`：当前没有签名、WORM或外部DB账本，拥有直接磁盘写权限的人仍可同时伪造receipt；因此它是scaffold一致性锚，不是最终确认性证据根。

## 哪些数据放哪里

| 数据 | 位置 | 原因 |
|---|---|---|
| Python、JSON Schema、Prompt/AGENTS 资产 | repo 的 `seven-system/` | 需要 Git 版本化和代码审查 |
| RuntimeManifest、PhasePlan、Summary | D 盘 Epoch 导出 | 每次运行独立可重放 |
| thinking、trajectory、payload、proof、盲化 view、审计正文 | D 盘 CAS | 体积大、内容寻址、不可覆盖 |
| WorkEvent、GateDecision、EvidenceRecord 元数据 | ArangoDB | 查询、索引、CAS revision 和谱系 |
| pending/leased/backpressure 投影 | Redis `evidence:seven:*` | 高频调度，可由 ledger 重建 |
| 标准答案、完整解答、sealed holdout | 物理 Vault | 与 Solver/Selector/Process Auditor 隔离 |

DB 记录只保存 artifact 的 hash、size、media type、schema version、producer、access class 和 CAS URI，不把大块 thinking 当普通文档塞入 DB。

## 数据库边界

站点 expected database 固定为：

```text
xishujuzhen_math_glm52
```

任何未来 DB 命令前必须：

```bash
set -a; source .env; set +a
echo "$ARANGO_DB"
```

输出不精确等于 `xishujuzhen_math_glm52` 时立即停止。禁止 fallback 默认库。

Seven复用这个原逻辑数据库，但不复用它的原业务Schema：

- 题海系统、`system/`与Seven可以共用同一Arango服务和逻辑数据库；
- Seven只允许访问隔离的`seven_*_v1`集合/索引；
- Seven不得写题海或`system/`集合，不得把原集合改名成Seven集合；
- 大对象仍在D盘CAS，数据库只保存小型元数据、事件和artifact引用。

这项架构决策不构成当前写授权。真实site verifier和Schema初始化入口尚未实现。

### WP-1现行Gate与Advisory

WP-1不是387号canonical P1。它只是Seven工程化前置工作包，必须把逻辑站点能力、Schema初始化和物理运维状态分开判定：

| Gate / Advisory | 证明对象 | 当前状态 | 当前证据/阻断 |
|---|---|---|---|
| `G-WP1-S` | D 卷 README、数据根、非 symlink、同设备与可写性 | `PASS` | 真实 dry-run preflight 已 PASS |
| `G-WP1-C` | Strict DB port 的离线契约 | `PASS` | CLI生成的实际报告经Schema、语义验证和受控测试复验PASS |
| `G-WP1-L` | 原逻辑DB的精确身份、连接后current DB、principal和只读catalog | `NOT_IMPLEMENTED` | adapter/planner已有离线基础，但没有真实site report generator、semantic verifier或operator CLI |
| `G-WP1-I` | Seven Schema初始化的计划、人工授权、受控DDL、收据和恢复边界 | `NOT_IMPLEMENTED` | 生产package没有apply/DDL/authorization/receipt primitive |
| `A-WP1-D` | Arango物理字节是否由D盘承载 | `PASS` | OrbStack data symlink、实时打开的`/data/OrbStack/data/data.img.raw`与D卷设备形成完整宿主证据链 |
| `A-WP1-BIND` | Arango是否使用独立、显式的专用bind/volume | `WARNING_NOT_DEDICATED` | engine使用容器`/var/lib/arangodb3` writable overlay；`/data/arangodb/data:/data`为空且未被使用 |

这些状态不得折叠。尤其是`G-WP1-C=PASS`只说明代码在离线测试中满足接口约束，不能把`G-WP1-L/I`变绿；`A-WP1-D=PASS`只说明宿主字节在D盘，不能掩盖`A-WP1-BIND`告警，也不能被当成逻辑接入父Gate。当前WP-1总状态为`PARTIAL/READY_FOR_LOGICAL_SITE_INTEGRATION`，不是site capability PASS。

旧模型的`G-WP1-P@v1=BLOCKED`和`G-WP1-M@v1=NOT_REACHED`作为基于不完整存储层核验形成的历史记录继续保留，但不再是现行Gate。现行物理判断以完整OrbStack宿主链为准。

### 两种报告不能混用

`wp1-strict-db-contract-report.schema.json` 定义 `StrictDbContractReport`：

- subject 是 adapter 源码、冻结 migration plan、索引计划和离线测试物证的组合 hash；
- 允许在不连接数据库的 static/fake-adapter 检验后得到 `PASS`；
- `side_effects` 强制 DB connection/write、migration、容器重启、Solver 和 Redis 全为 0；
- 明确不主张本站可连接、engine 在 D 盘、migration 已应用或生产可切换。

该Schema已由`wp1-db-contract-report`实际执行；generator不会接受调用者注入的PASS、check evidence、测试收据或生成时间。semantic verifier还会通过`-I -S -B`机器runner重跑固定测试，绑定完整test IDs，把allowlist和索引语义纳入required evidence，并检查canonical check顺序与唯一性、9项claim、6项nonclaim、零外部副作用、时区时间格式和当前subject hash。verifier只验时间格式，不认证wall-clock。因此这里只把 **Schema+semantic+current subject全部通过** 的报告称为有效离线PASS。

`wp1-database-site-capability-report.schema.json` v1曾定义旧`DatabaseSiteCapabilityReport`前向shape：

- subject 是本站卷身份、Arango 容器配置、engine data directory、Strict contract report 和 migration 状态的组合 hash；
- 只有四个 Gate 全部 PASS 才允许总判定 PASS；
- 当前只允许只读观测，`side_effects` 中 DB write、migration、restart、生产状态变更、Solver 和 Redis 均为 0。

这个v1 shape把唯一可接受的D-backing形式写死为`/data/arangodb/data`专用bind，并编码成site PASS必需条件，已被2026-08-14后续核验取代，状态为`SUPERSEDED_NOT_EXECUTED`，禁止消费。它没有generator、semantic verifier或实际报告，不能静默改写语义。后续新增逻辑站点v2合同，以`G-WP1-L/I`作为能力门，分别记录`A-WP1-D`宿主D-backing和`A-WP1-BIND`专用bind状态。

两个现存Schema的执行状态不同：Strict report Schema已经执行并有实际PASS报告；Site v1只保留旧前向shape。**Site Schema-valid不等于site capability-valid**。现有通用`capability-report/v1`也不得接收一个离线contract PASS后冒充site capability PASS。

### 已冻结的离线报告

2026-08-14 对当前实现生成并复验：

```text
path=/data/seven-system-data/capabilities/strict-db-contract/wp1-contract-20260814-002.json
schema_version=wp1-strict-db-contract-report/v1
verdict=PASS
subject_hash=77c6e348b4124a53080322d5cbe478b5ded3c8bea31dfc4555ac320aaa97799b
implementation_hash=656d6e807ad2e5f1e0b237145cfef94640b5eddd6054fc47d3c51111a1cc609e
test_execution_receipt_sha256=055ac2d9d9479663b529888295701ddc7f347830bfbbb1372ece775534e4533a
file_sha256=68c96aa4eec1fa8f7fc0e55222f6395c7b9096c683cae85f15888bc323c64b71
isolated_runner_tests=20
full_tests=58
```

报告共11项canonical check，全部PASS；9项required claim全部为true；6项explicit nonclaim完整；blockers为空；DB connection/write、migration、container restart、Redis write、Solver launch全部为0。文件mode为`0600`，同一ID重入返回`ALREADY_COMMITTED`；这仍不是WORM或文件不可变性证明。

同目录中的001是在后续代码硬化前生成的历史物证，现为`STALE/SUPERSEDED`并继续保留；它不能替代与当前implementation subject匹配的002。

报告明确不主张：

- DB site capability已经成立；
- 物理数据库存储已经验证；
- 已连接ArangoDB或执行migration；
- 已实现durable migration ledger、fence或resume；
- 已证明runtime append-only、CAS或outbox delivery语义；
- 已认证wall-clock或本地报告文件不可变性。

### Strict DB port 离线契约

离线契约至少要证明：

1. runtime config Schema用`const`锁定expected DB和adapter contract，Python配置解析器再用canonical常量复核；环境仍必须显式提供DB连接四元组，没有默认数据库；
2. read path 不创建 database、collection 或 index；
3. 所有集合名以 `seven_` 开头，禁止访问题海系统和 `system/` 的集合；
4. Schema初始化只有显式 plan/verify 路径，普通读写不能隐式 ensure schema；
5. spec冻结`(aggregate_id, event_sequence)`唯一索引，但不把索引存在误写成runtime append-only证明；
6. spec冻结WorkItem、attempt、artifact和outbox的唯一键，但不证明runtime CAS或outbox delivery语义；
7. 不向业务层暴露可以绕过这些检查的 raw client。

离线报告的 PASS 必须同时满足：所有语义检查 PASS、所有 required claim 为 `true`、所有 side effect 为 0、blockers 为空。轻量 Schema 不能表达“若总判定 PASS，则数组内所有检查 PASS”等跨字段约束；已实现的 Strict report semantic verifier负责补足这些规则。Site report尚无对应verifier，所以任何手写Site JSON即使Schema-valid也不能成为能力证据。

### Canonical Schema初始化spec（代码历史名为migration spec；真实DB尚未创建）

```text
seven_records_v1
seven_artifact_refs_v1
seven_work_events_v1
seven_work_items_v1
seven_outbox_v1
seven_alerts_v1
seven_schema_migrations_v1
```

canonical spec hash是`9488414a4d76103dd1c3bbc8f470d464c453aef6224c56320743d570f2d05489`，固定7个集合和13个persistent unique index：

| 集合 | 唯一索引 |
|---|---|
| `seven_records_v1` | `ux_records_type_content_hash(record_type, content_hash)`；`ux_records_type_logical_revision(record_type, logical_id, revision)` |
| `seven_artifact_refs_v1` | `ux_artifact_refs_content_hash(content_hash)`；`ux_artifact_refs_cas_uri(cas_uri)` |
| `seven_work_events_v1` | `ux_work_events_event_id(event_id)`；`ux_work_events_aggregate_sequence(aggregate_id, event_sequence)` |
| `seven_work_items_v1` | `ux_work_items_stage_idempotency(stage, idempotency_key)`；`ux_work_items_execution_attempt(execution_attempt_id)`，sparse |
| `seven_outbox_v1` | `ux_outbox_unique_key(outbox_unique_key)`；`ux_outbox_aggregate_revision(aggregate_id, aggregate_revision, event_type)` |
| `seven_alerts_v1` | `ux_alerts_dedupe_key(dedupe_key)`，sparse |
| `seven_schema_migrations_v1` | `ux_schema_migrations_migration_id(migration_id)`；`ux_schema_migrations_plan_hash(plan_hash)` |

这些只是代码中已冻结并由fake adapter验证的spec，不表示真实集合/索引已经创建。planner会确定性读取catalog并拒绝非canonical spec、冲突语义以及额外persistent user index；目前没有真实站点plan/verify CLI。

读取不得自动创建数据库、集合或索引。生产database package只有只读planner，完全没有apply/DDL/authorization/receipt primitive；真实Arango adapter同样没有DDL方法。当前不得在原逻辑DB执行apply。未来若要新增写入路径，必须作为独立工作包先完成逻辑站点v2核验、确认Seven namespace无冲突、获得用户明确授权，并实现受控DDL、执行收据、durable ledger/fence/resume。把writable overlay改为专用bind/volume另属独立运维硬化事项，不是该写工作包的前置。

## 为什么不直接复用 `system/db.py`

当前 `system/db.py` 允许默认 DB，且部分 read path 会自动 ensure collection；它也没有 Seven 需要的 ledger、outbox、CAS revision 和唯一索引能力。Seven 可以借鉴它的连接封装，但不能把它当成合格 adapter，也不能让它替代离线`StrictDbContractReport`与未来`DatabaseLogicalSiteCapabilityReport v2`的分层判定。

同样，Seven 不写第六代系统的 `problem_entries/sessions/ai_instances`，也不修改题海系统的 `devin_problem_runs` 或题目状态。

## Vault 边界

把文件放进名为 `vault/` 的目录并不等于完成答案隔离。真正 PASS 必须证明：

- Solver 环境没有 Vault 路径或凭据；
- Process Auditor 不可读取解答；
- Proof Judge 与 Leakage Auditor 只得到各自最小 view；
- 每次访问都有 append-only audit log；
- holdout 在一次性解封前对 proposal 生成器不可见。

v0.1.0 没有 Vault 实现，所以 live preflight 必须 BLOCKED。

## 删除与回收

首版没有 GC、delete、clear 或覆盖命令。任何已提交 artifact、负证据、冲突记录和被拒候选都必须保留。未来若增加回收，必须先定义引用追踪、保留期、legal hold、dry-run 和人工确认；不得用磁盘压力作为静默删除理由。

## 当前安全停止点

站点目录前置条件已关闭；数据库政策已允许下一步做“逻辑站点接入”，但当前实现仍必须停在真实连接与DDL之前：

1. 保留 `/data/README.md` 和 `/data/seven-system-data/`，继续让普通 preflight fail-closed 检查它们；
2. 保留并复验已PASS的 Strict DB port、canonical spec和离线 contract report；
3. 下一个实现工作包可以设计并验证逻辑站点v2 report，之后才可经受控命令只读核对原逻辑DB identity/current DB/catalog；
4. 当前不得停止/重启共享ArangoDB，不得复制现有engine数据，不得创建`seven_*_v1`集合；
5. 不得因为复用架构已批准、目录名、离线测试PASS或计划文件存在，就声称DB site capability、Schema初始化、CAS、Vault、WORM或科学证据已经成立。
