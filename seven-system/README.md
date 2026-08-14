# Seven System · 非特化证据工厂

Seven System 是一个独立的实验系统：它的目标是把题海系统产生的真实 bare 失败、未来第六代系统提供的冻结 Tell/分类学资产，以及 387/388 号研究协议，组织成可重放、可归责、可恢复的非特化证据。当前 v0.1.0 实现了下文列出的 P0/P1 scaffold，以及 WP-1 的站点存储前置和离线 Strict DB contract；它还不能进行真实数据库 migration 或非特化科学实验。

它不是第三套解题模型，也不接管正在运行的题海系统。

## 三套系统的边界

| 系统 | 当前职责 | Seven System 如何使用 |
|---|---|---|
| Devin 大规模高并发题目测试系统 | 设计上要求Solver无工具地批量做题，发现能力边界和bare失败；现有物理无工具证明仍有缺口 | 只读消费冻结的题目、attempt和物证；不写回`math:*`队列 |
| `system/` 第六代 AI 数学系统 | 未来的入题/解题系统；当前只有脉络分析子阶段有历史 POC | 未来只接收带 Schema 与哈希的冻结 bundle；禁止直接 import 或共享内部状态 |
| `seven-system/` | 非特化 Case、因果实验、三审、EvidenceRecord 与版本学习的证据工厂 | 独立控制面、独立命名空间、独立大对象根和人工门 |

## 当前真实实现状态

版本 `0.1.0` 的真实实现上限仍是 `P1_DRY_RUN`（不是 387 号完整 P1）：

- 只读 preflight；
- RuntimeManifest 和单 Epoch 文件集；
- 确定性对象哈希；
- 同内容幂等提交、异内容冲突拒绝；
- append-only P1 GateDecision、后续 checkpoint 与 scaffold verdict；
- 初始/P1两级完整性索引与 Epoch 完整性检查；
- D 盘 README、Seven 数据根与真实 dry-run preflight；
- Strict DB 固定数据库身份、集合白名单、只读 planner、7集合/13唯一索引的 canonical migration spec；
- `wp1-db-contract-report` 离线受控测试、Schema+语义验证和 append-once 本地报告；
- 明确列出 P2-P9 `NOT_IMPLEMENTED`。

当前没有任何 CLI 命令能连接或修改真实数据库、写 Redis 或启动 Devin CLI。真实 DB site capability/migration、Solver、答案 Vault、CandidateManifest 导入、三审、EvidenceRecord，以及 387 号要求的崩溃/lease/fencing/reconcile 完整 P1 矩阵仍未实现。

## 第一次使用

先读 [操作手册](docs/operations.md)，再从当前workspace根执行：

```bash
SEVEN_WORKSPACE_ROOT="$(git rev-parse --show-toplevel)"
cd "$SEVEN_WORKSPACE_ROOT"
.venv/bin/python seven-system/scripts/seven.py capabilities
.venv/bin/python seven-system/scripts/seven.py preflight \
  --config seven-system/config/runtime.example.json
.venv/bin/python seven-system/scripts/seven.py wp1-db-contract-report \
  --config seven-system/config/runtime.example.json \
  --report-id wp1-contract-20260814-002
```

`seven-system/`本身只使用Python标准库；若未来独立迁出，可从其新repo根用`python3 scripts/seven.py ...`运行，无需依赖当前父repo路径。

当前示例 preflight 应当退出 `0` 且 `overall_verdict=PASS`。这只证明 dry-run 站点目录前置；当前 Arango engine data directory 没有落在批准的 D 盘 bind 上，所以 DB site capability 仍为 `BLOCKED`，migration 为 `NOT_REACHED`。

上述固定 report ID重入时会重新校验当前实现绑定的离线报告，完全匹配才返回`ALREADY_COMMITTED`。报告位于`/data/seven-system-data/capabilities/strict-db-contract/wp1-contract-20260814-002.json`；其 PASS 不证明真实 DB 连接、物理落盘或 migration。

## 目录

```text
seven-system/
├── scripts/                 统一 CLI
├── src/seven_system/        P0/P1 控制面与离线Strict DB契约代码
├── assets/                  Solver 等运行时资产
├── config/                  非密钥站点配置示例
├── schemas/                 当前 wire contract
├── docs/                    架构、操作、存储与状态说明
└── tests/                   隔离单元与 dry-run 测试
```

大对象、数据库数据、运行日志和 Epoch 产物不进入本目录；Seven 的批准数据根是 `/data/seven-system-data/`。目录存在不证明 CAS、Vault、WORM 或 DB 物理落盘能力。

## 关键文档

- [操作手册](docs/operations.md)
- [架构与系统边界](docs/architecture.md)
- [D 盘与数据库契约](docs/storage-and-database.md)
- [实现状态](docs/implementation-status.md)
- [测试说明](docs/testing.md)
