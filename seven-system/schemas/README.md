# JSON Schema 索引

本目录冻结 Seven System P0/P1 当前 wire contract、已执行的WP-1 Strict DB离线报告contract，以及尚未实现site verifier的数据库站点前向shape。

| 文件 | 对象 |
|---|---|
| `runtime-config.schema.json` | 站点配置 |
| `runtime-manifest.schema.json` | 单 Epoch 冻结清单 |
| `preflight-report.schema.json` | P0 只读检查结果 |
| `capability-report.schema.json` | live 前置能力的独立证明 |
| `phase-plan.schema.json` | P0-P9 阶段计划与实现状态 |
| `logging-contract.schema.json` | 结构化日志上下文与脱敏契约 |
| `scenario-matrix.schema.json` | 本地scaffold场景与未来canonical GS目录 |
| `runtime-checkpoint.schema.json` | 初始与后续append-only checkpoint |
| `evidence-index.schema.json` | 当前必须为空的Evidence占位索引 |
| `dry-run-report.schema.json` | P1 scaffold dry-run报告 |
| `gate-decision.schema.json` | append-only Phase Gate决定 |
| `idempotency-probe.schema.json` | P1单文件幂等探针 |
| `epoch-integrity-index.schema.json` | 初始/P1 append-only文件seal与hash链 |
| `local-root-receipt.schema.json` | Epoch外local append-once索引锚；明确非WORM |
| `scaffold-verdict.schema.json` | P0/P1 scaffold结论；强制科学主张NOT_TESTED |
| `verdict.schema.json` | 多维最终 Verdict 的首版保留结构 |
| `wp1-strict-db-contract-report.schema.json` | `StrictDbContractReport`离线契约报告；CLI已执行Schema+semantic verifier并产出PASS报告 |
| `wp1-database-site-capability-report.schema.json` | `DatabaseSiteCapabilityReport`本站物理能力前向shape；当前没有generator/verifier，四个WP-1子门不得折叠 |

Schema 的存在不表示对应运行阶段已经实现；实际边界以 `docs/implementation-status.md` 为准。

两个 `wp1-*` Schema 使用当前自制 validator 已支持的结构关键字：`type`、`const`、`enum`、`minLength`、`pattern`、`minimum`、`minItems`、`maxItems`、`items`、`required`、`properties` 和 `additionalProperties`。`$schema`、`$id`、`title` 只是元数据。

两者的执行状态不同：

- Strict report Schema已由`wp1-db-contract-report`加载；semantic verifier还会用隔离的机器JSON runner重跑固定测试，绑定完整test IDs，并验证check集合/顺序/evidence、9项claims、6项nonclaims、零外部副作用、时间格式和当前subject。builder不接收时间参数，但verifier只验格式，不认证wall-clock；实际报告位于`/data/seven-system-data/capabilities/strict-db-contract/wp1-contract-20260814-002.json`，subject hash为`77c6e348b4124a53080322d5cbe478b5ded3c8bea31dfc4555ac320aaa97799b`，文件SHA-256为`68c96aa4eec1fa8f7fc0e55222f6395c7b9096c683cae85f15888bc323c64b71`；
- Site report Schema仍是 **validator-compatible but NOT_EXECUTED** 的前向shape。当前没有site generator或semantic verifier，也没有有效site report。

轻量Schema不能独自表达全部跨字段规则，因此 **Schema-valid != capability-valid**：

- `StrictDbContractReport.verdict=PASS` 时，所有checks必须PASS、所有required claim必须为true、blockers必须为空；当前semantic verifier已执行这条规则；
- `DatabaseSiteCapabilityReport.gates` 必须恰好各含一次 `G-WP1-S/C/P/M`；只有四门全 PASS，总判定才允许 PASS；
- 离线 Strict contract PASS 不能替代 Site capability PASS；
- 本站当前应为 `G-WP1-P=BLOCKED`、`G-WP1-M=NOT_REACHED`，且 migration apply 不在本工作包授权范围内。
