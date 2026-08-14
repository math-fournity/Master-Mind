# D 盘与数据库契约

## 一句话结论

Repo 只保存代码、Schema、运行资产、文档和测试；所有大对象、Epoch 运行产物、日志和答案 Vault 都必须位于经批准的 D 盘数据根，ArangoDB 只保存可查询元数据、事件和大对象引用。

## 当前站点事实

2026-08-13 的只读核对结果：

- `/data` 正常挂载；
- APFS，约 1TB，总可用约 782GiB（`df` 口径）；
- 根目录可见现有 ArangoDB、Redis、Solver workspace 和 trajectory 数据；
- **缺少 `/data/README.md`**；
- `/data/seven-system-data/` 尚未创建。

由于卷级 README 缺失，本轮没有在 D 盘创建或修改任何目录。示例配置会因此 fail-closed。

## 建议物理布局

在用户批准卷级 README 和数据根之后，建议使用：

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

其中 `staging` 和 `cas` 必须在同一个文件系统，才能在 fsync 后原子 rename。禁止自动 fallback 到 repo、Home 或 `/tmp`。

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

### 首版建议集合（尚未创建）

```text
seven_records_v1
seven_artifact_refs_v1
seven_work_events_v1
seven_work_items_v1
seven_outbox_v1
seven_alerts_v1
```

这些是后续 DB migration 工作包的规格，不表示本轮已建表。

至少需要的唯一索引：

- record content hash；
- `(aggregate_id, event_sequence)`；
- WorkItem idempotency key；
- execution attempt ID；
- artifact content hash；
- outbox unique key；
- active pointer revision。

读取不得自动创建数据库、集合或索引；初始化必须是显式管理命令，并产生 capability report。

## 为什么不直接复用 `system/db.py`

当前 `system/db.py` 允许默认 DB，且部分 read path 会自动 ensure collection；它也没有 Seven 需要的 ledger、outbox、CAS revision 和唯一索引能力。Seven 可以借鉴它的连接封装，但在 `DatabaseCapabilityReport=PASS` 前不能把它当成合格 adapter。

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

## D 盘前置修复方案

在实际创建数据根前，需要用户批准：

1. 新建 `/data/README.md`，记录卷角色、APFS/挂载点、主要目录、容量口径、禁止操作和 Seven 数据根；
2. 再创建 `/data/seven-system-data/`；
3. 重新运行 `preflight`，确认 README、空间和数据根三项 PASS；
4. 只有之后才进入真实 DB/Vault 能力工作包。
