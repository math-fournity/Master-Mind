# JSON Schema 索引

本目录冻结 Seven System P0/P1 当前能生成或读取的 wire contract。

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

Schema 的存在不表示对应运行阶段已经实现；实际边界以 `docs/implementation-status.md` 为准。
