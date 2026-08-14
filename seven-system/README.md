# Seven System · 非特化证据工厂

Seven System 是一个独立的实验系统：它的目标是把题海系统产生的真实 bare 失败、未来第六代系统提供的冻结 Tell/分类学资产，以及 387/388 号研究协议，组织成可重放、可归责、可恢复的非特化证据。当前 v0.1.0 实现了下文列出的 P0/P1 scaffold，以及 WP-1 的站点存储前置和离线 Strict DB contract；它还不能核验真实逻辑数据库站点、初始化Seven Schema或进行非特化科学实验。

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
- Strict DB 固定数据库身份、集合白名单、只读 planner、7集合/13唯一索引的 canonical Schema初始化spec（代码历史名为migration spec）；
- `wp1-db-contract-report` 离线受控测试、Schema+语义验证和 append-once 本地报告；
- 明确列出 P2-P9 `NOT_IMPLEMENTED`。

当前没有任何 CLI 命令能连接或修改真实数据库、写 Redis 或启动 Devin CLI。真实逻辑DB site capability、Seven Schema初始化、Solver、答案 Vault、CandidateManifest 导入、三审、EvidenceRecord，以及 387 号要求的崩溃/lease/fencing/reconcile 完整 P1 矩阵仍未实现。

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

当前示例 preflight 应当退出 `0` 且 `overall_verdict=PASS`。这只证明 dry-run 站点目录前置。Seven的目标架构是复用现有Arango服务和逻辑数据库`xishujuzhen_math_glm52`，但只使用隔离的`seven_*_v1`集合/索引；当前真实逻辑站点核验和Schema初始化仍为`NOT_IMPLEMENTED`。宿主层只读核验已确认OrbStack全部Docker数据由`/data/OrbStack/data/data.img.raw`承载，因此`A-WP1-D=PASS`；Arango仍把`/var/lib/arangodb3`放在容器writable overlay中，没有使用`/data/arangodb/data:/data`专用bind，因此`A-WP1-BIND=WARNING_NOT_DEDICATED`。不要把宿主D-backing PASS误读为数据库控制面或Schema能力PASS。

上述固定 report ID重入时会重新校验当前实现绑定的离线报告，完全匹配才返回`ALREADY_COMMITTED`。报告位于`/data/seven-system-data/capabilities/strict-db-contract/wp1-contract-20260814-002.json`；其 PASS 不证明真实 DB 连接、物理落盘或 migration。`A-WP1-D=PASS`来自独立的宿主存储链核验，不是这份离线报告的主张。

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

大对象、运行日志和 Epoch 产物不进入本目录；Seven 的批准数据根是 `/data/seven-system-data/`。ArangoDB未来只保存小型元数据、事件和artifact引用。目录存在本身不证明 CAS、Vault、WORM 或 DB 物理落盘能力；当前Arango的D-backing结论来自OrbStack symlink、实时打开的`data.img.raw`和容器overlay的分层核验。

## 关键文档

- [操作手册](docs/operations.md)
- [架构与系统边界](docs/architecture.md)
- [D 盘与数据库契约](docs/storage-and-database.md)
- [实现状态](docs/implementation-status.md)
- [测试说明](docs/testing.md)
