# POC-VMS-35：复现入题侧 Devin 文件写入契约——去 sandbox 单因素协议

> 状态：`PREREGISTERED_NOT_EXECUTED`  
> 日期：2026-08-14  
> 类型：`SOURCE_CONTRACT_REPLICATION / REVISION_FIT`  
> 上游证据：349、351、353号  
> 保护边界：不修改入题侧代码、AGENTS、prompt或历史运行产物；不连 DB/Redis；不启动 Solver。

---

## 1. 实验问题

POC-VMS-32/33 都在 `--sandbox` 下要求 Devin 直接写角色输出。当前 CLI 明确报告：

```text
--sandbox always uses the autonomous permission mode;
ignoring --permission-mode dangerous
```

三个角色因此都没有提交规定 JSON。但 353 号对入题侧源码和历史实物的回源表明，已经成功运行过的 Devin 认知角色契约是：

```text
fresh role workdir
+ frozen AGENTS/prompt/input
+ --permission-mode dangerous
+ no --sandbox
+ model writes stage files
+ --export trajectory
```

本轮只回答：

> 在保持同一批角色资产、fixture、evaluator、模型和调度不变时，只关闭 Devin sandbox，能否恢复入题侧已证实的“模型直接写文件”可执行性？

---

## 2. 单因素对照

| 维度 | POC-VMS-33 | POC-VMS-35 |
|---|---|---|
| carrier | Devin CLI | 不变 |
| model UID | `glm-5-2` | 不变 |
| normalized effort | `high` by model UID | 不变 |
| role assets | `solve-vein-assets-0.1.0` | 不变 |
| fixtures / gold | POC-VMS-32 frozen set | 不变 |
| evaluator | 同一严格 evaluator | 不变 |
| permission mode | `dangerous` | 不变 |
| sandbox | `true` + `--sandbox` | **`false`，不传 `--sandbox`** |
| session | fresh, no resume/continue | 不变 |
| output | 模型写 JSON + hashed `DONE.md` | 不变 |
| export | required | 不变 |
| inter-role cooldown | 75 seconds | 不变 |
| attempts | one per role | 不变 |

这里“去 sandbox”是一个执行 profile 因素，它同时包括：不在 argv 中传 `--sandbox`，并在可审计环境收据中记录 `DEVIN_SANDBOX=false`。不得在本轮修改任务内容来补偿结果。

---

## 3. 调用合同

```yaml
carrier: devin_cli
requested_model_uid: glm-5-2
catalog_display_name: GLM-5.2 High
normalized_effort: high
effort_encoding: model_uid
permission_mode: dangerous
sandbox_requested: false
session_policy: fresh_only
resume_or_continue: forbidden
subagents: disabled
workspace: one_fresh_directory_per_role
input_delivery: frozen_files_before_launch
output_capture: model_writes_expected_json_and_hashed_done_marker
export: required_and_json_parseable
process_exit: required_before_bundle_seal
inter_role_cooldown_seconds: 75
scientific_attempts_per_role: 1
infrastructure_retry: forbidden_in_this_poc
```

角色仍为：

1. `reasoning_event_extractor`；
2. `mathematical_state_normalizer`；
3. `process_trace_auditor`。

三个角色使用 POC-VMS-32/33 已经看过的同一校准集，因此本轮不是 prospective holdout，也不是生产 qualification。

---

## 4. DONE 与 export 时序修正

入题侧的 tmux 历史暴露了一个不能照搬的竞态：模型创建空 `DONE.md` 后，管线立即 kill session，可能中断 `--export`。

本轮规定：

1. Devin 在输出 JSON 后创建带有输出 SHA-256 的 `DONE.md`；
2. runner 不以 DONE 作为 kill 条件；
3. runner 等待子进程正常终止或预注册 timeout；
4. 进程结束后才检查 output、DONE 和 export；
5. export 不存在、不可解析或观测到非 `glm-5-2` 生成 step，该角色不得 PASS；
6. 三类物证全部进入 append-once bundle 后才生成 receipt。

---

## 5. 功能判据

内容判据完全继承 348/350 号，不事后改阈值：

- Extractor：strict Schema，source/span hash 精确，occurrence recall 1.0，typed-edge recall 至少 0.80，正确折返 identity，真合流两父全命中，false merge=0；
- Normalizer：历史不变，3 个预注册语义修正全命中，无无关变更，无虚构事件/边；
- Auditor：真 revisit PASS，伪 single-parent merge FAIL，混合集整体 verdict=FAIL。

运行合同额外要求：

```yaml
all_exit_codes_zero: true
all_timeouts_false: true
all_exports_present_and_parseable: true
all_generation_model_uids: [glm-5-2]
all_expected_outputs_present: true
all_done_markers_present: true
all_retry_counts: 0
rate_limit_errors: 0
confirmation_rejections: 0
```

---

## 6. 安全判据与明确非主张

本轮只复现入题侧的文件写入可执行性，**不证明 no-sandbox 运行的强隔离性**。

已知安全控制：

- 每个角色是新建临时工作目录；
- 只预置校准 fixture，不放凭据、参考答案、DB 配置或生产状态；
- 专用 config 禁用 subagent，拒绝 repo/Volumes 读取与外部网络命令；
- 环境变量只保留 CLI 启动所需最小集；
- 原始 stdout/stderr/export 全量封存。

未证明项：

- config deny 是否对所有路径、命令和符号链接都 fail-closed；
- 模型是否无法读取 HOME 中的其他文件；
- 兄弟 workspace/Vault 拒读能力；
- 任意 tool escape 防护。

因此，即使三角色功能全 PASS，安全 verdict 也只能是 `NOT_TESTED_STRONG_ISOLATION`。生产化前必须另行预注册 sibling-workspace/Vault canary 与 OS 级隔离资格测试。

---

## 7. Verdict 规则

- 三个角色运行合同和内容判据全部通过：`FILE_WRITING_RUNTIME_PASS_WITHIN_SOURCE_REPLICATION_CALIBRATION`；
- 运行合同通过但内容有 PARTIAL/FAIL：保留对应科学 verdict；
- 仍无输出、发生限流、export 缺失或模型不可观测：`INCONCLUSIVE_PROTOCOL`；
- 观测到禁止路径读写或其他越界：`FAIL_SECURITY_BOUNDARY`。

本轮无论结果如何都不能声称：生产资格、强隔离、新题泛化、规模能力、Solver 集成、Tell/Hint 效果或入题侧改造完成。

---

## 8. 停止条件

1. 修订 runner 支持显式 sandbox profile；
2. 离线测试证明两种 argv/env/receipt 均可机械区分；
3. 记录正式执行前的资产、fixture、runner/evaluator 哈希；
4. 每个角色只调用一次，角色间固定冷却 75 秒；
5. 封存 report/manifest/receipt 并生成结果文档后停止。

不得因输出不理想而在同一 POC ID 中补跑。
