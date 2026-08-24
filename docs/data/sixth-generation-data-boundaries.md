# 第六代系统数据边界

**状态**：current
**运行观察**：本次重建未连接或写入 ArangoDB；live schema 和数据状态未知。

## 数据权威分层

| 数据 | 当前权威 | 说明 |
|---|---|---|
| legacy 领域对象 | `system/schema.py` | Python dataclass 语义，不是 DB schema |
| DB 适配器行为 | `system/db.py` | 当前代码实际连接和读写方式 |
| DB 设计草案 | `system/db_schema.py` | 部分字段和待建集合；不能证明 live schema |
| solve-side structured trajectory | `system/solve_vein_analysis/models.py` | strict in-memory/JSON contract |
| solve-side run output | CLI sealed directory和`run-manifest.json` | 本地离线 artifact；不连接 DB |
| 测试 fixtures | `system/tests/solve_vein_analysis/` | 冻结验证输入，不是生产数据 |
| curated knowledge | `knowledge/` tracked notes | 当前 repo 可保留的小型参考资料 |
| 大语料/题库 | D 盘 offload root | Git 只保留指针和校验 manifest |
| 大 solve-side run evidence | `/data/master-mind-solve-vein-data/` | 历史/开发证据，按 receipt 和 attempt 识别 |

## ArangoDB 当前事实

`system/db.py` 通过 `ARANGO_HOST`、`ARANGO_DB`、`ARANGO_USER`、`ARANGO_PASS` 读取连接配置，并可
自动创建集合和执行写入。代码实现 `problem_entries`、`sessions`、AI instance 等操作，但当前 live
环境身份、集合 schema、索引、计数和数据质量未在本分支核验。

`system/db_schema.py` 是不完整设计层：orphan traces、Tell library changes、tree nodes/edges 和 alerts
仍为 TODO。其 `problem_entries` 示例仍写 V9，而当前 `vein_analysis.py` 使用 V10；它还混用
table/collection 术语。因此当前 DB 设计不能作为可执行迁移规范。

任何 DB 读写或 schema 迁移前必须重新核验目标环境、live catalog、消费者、备份和授权。本次只
记录差异，不修改 DB 或设计迁移。

## 文件和运行资产

legacy absorb 侧默认写 `palyground/{process}/vein_analysis/...`、ArangoDB 记录和
`system/tests/vein_analysis/runs/` 归档。`palyground/` 和 runtime logs 是运行现场，不是稳定当前真值。

solve-side 离线 CLI 对一个全新输出目录执行 exclusive create、fsync 和 atomic rename，并把 input、
asset、implementation tree 和 output hash 写入 manifest。资格/调试 bundle 使用 append-only 规则；
已消费 attempt ID 和 sealed artifact 不得覆盖。

## 大数据策略

- 当前大数据根：`/data/master-mind-glm5.2-worktree-external-data/2026-08-24/knowledge/`。
- 12,284 个 offloaded 文件已做 SHA-256 对账，0 missing、0 mismatch。
- `knowledge/arxiv/README.md` 和 `knowledge/problem_banks/README.md` 是指针，不是 corpus body。
- 新的大问题数据和大 run body 继续落 D 盘，Git 只提交 pointer、manifest、hash 和必要小 fixture。

## Secret 和 local state

`.env`、本地配置、venv、cache、bytecode、临时文件和 DB 文件不入 Git。`.env.example` 是不含真实
secret 的 tracked 模板，属于 `keep-current`。416 文档按用户裁定原文保留，但任何报告和 canonical
doc 都不得显示其 credential-like 值。

## 迁移完成条件

文件迁移必须有 old path、target 或 history pointer、commit、理由和恢复证据。DB/data 迁移另需
live identity、可恢复备份、dry-run、幂等/续跑、消费者兼容和前后不变量对账；当前均未授权执行。
