# Seven System · 非特化证据工厂

Seven System 是一个独立的实验系统：它的目标是把题海系统产生的真实 bare 失败、未来第六代系统提供的冻结 Tell/分类学资产，以及 387/388 号研究协议，组织成可重放、可归责、可恢复的非特化证据。当前 v0.1.0 仅实现下文列出的 P0/P1 scaffold。

它不是第三套解题模型，也不接管正在运行的题海系统。

## 三套系统的边界

| 系统 | 当前职责 | Seven System 如何使用 |
|---|---|---|
| Devin 大规模高并发题目测试系统 | 设计上要求Solver无工具地批量做题，发现能力边界和bare失败；现有物理无工具证明仍有缺口 | 只读消费冻结的题目、attempt和物证；不写回`math:*`队列 |
| `system/` 第六代 AI 数学系统 | 未来的入题/解题系统；当前只有脉络分析子阶段有历史 POC | 未来只接收带 Schema 与哈希的冻结 bundle；禁止直接 import 或共享内部状态 |
| `seven-system/` | 非特化 Case、因果实验、三审、EvidenceRecord 与版本学习的证据工厂 | 独立控制面、独立命名空间、独立大对象根和人工门 |

## 当前真实实现状态

版本 `0.1.0` 只实现 P0 与 P1 scaffold（不是 387 号完整 P1）：

- 只读 preflight；
- RuntimeManifest 和单 Epoch 文件集；
- 确定性对象哈希；
- 同内容幂等提交、异内容冲突拒绝；
- append-only P1 GateDecision、后续 checkpoint 与 scaffold verdict；
- 初始/P1两级完整性索引与 Epoch 完整性检查；
- 明确列出 P2-P9 `NOT_IMPLEMENTED`。

当前没有任何命令能连接数据库、写 Redis 或启动 Devin CLI。真实 Solver、答案 Vault、CandidateManifest 导入、三审、EvidenceRecord，以及 387 号要求的崩溃/lease/fencing/reconcile 完整 P1 矩阵仍未实现。

## 第一次使用

先读 [操作手册](docs/operations.md)，再从当前workspace根执行：

```bash
SEVEN_WORKSPACE_ROOT="$(git rev-parse --show-toplevel)"
cd "$SEVEN_WORKSPACE_ROOT"
.venv/bin/python seven-system/scripts/seven.py capabilities
.venv/bin/python seven-system/scripts/seven.py preflight \
  --config seven-system/config/runtime.example.json
```

`seven-system/`本身只使用Python标准库；若未来独立迁出，可从其新repo根用`python3 scripts/seven.py ...`运行，无需依赖当前父repo路径。

当前示例 preflight 应当 `BLOCKED`：`/data/README.md` 与 `/data/seven-system-data/` 尚不存在。这是预期的 fail-closed 结果，不是脚本故障。

## 目录

```text
seven-system/
├── scripts/                 统一 CLI
├── src/seven_system/        P0/P1 控制面代码
├── assets/                  Solver 等运行时资产
├── config/                  非密钥站点配置示例
├── schemas/                 当前 wire contract
├── docs/                    架构、操作、存储与状态说明
└── tests/                   隔离单元与 dry-run 测试
```

大对象、数据库数据、运行日志和 Epoch 产物不进入本目录；它们未来位于经批准的 D 盘数据根。

## 关键文档

- [操作手册](docs/operations.md)
- [架构与系统边界](docs/architecture.md)
- [D 盘与数据库契约](docs/storage-and-database.md)
- [实现状态](docs/implementation-status.md)
- [测试说明](docs/testing.md)
