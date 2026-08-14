# Seven System 操作手册

## 一句话结论

当前 Seven System 只能安全运行 P0与P1 scaffold：先做只读 preflight，再初始化有限Epoch，最后执行不会连接数据库或启动Solver的dry-run。它不是387号完整P1；没有`start`命令是刻意的安全边界。

## 0. 操作者先确认自己在做什么

你运行的是非特化证据工厂控制面，不是：

- 正在运行的 Devin 题海管道；
- 第六代 `system/enter.py` 或 `system/solve.py`；
- 数学 Solver 本身。

Seven v0.1.0 的成功含义只是：配置边界、manifest、目录、幂等提交和冲突拒绝可运行。它不产生 Tell 科学证据。

## 1. 固定入口

当前monorepo中，先用Git确定workspace根，不要把某台机器的绝对路径写进自动化：

```bash
SEVEN_WORKSPACE_ROOT="$(git rev-parse --show-toplevel)"
cd "$SEVEN_WORKSPACE_ROOT"
```

统一入口是：

```bash
.venv/bin/python seven-system/scripts/seven.py <command>
```

Seven源码仅使用Python标准库。若`seven-system/`未来迁为独立repo，则从其repo根使用`python3 scripts/seven.py <command>`；不应保留对父repo或父repo `.venv`的依赖。

不要临时写脚本、不要直接操作 Redis、不要直接连接 ArangoDB，也不要手工 tmux 启动 Solver。

## 2. 先看实现边界

```bash
.venv/bin/python seven-system/scripts/seven.py capabilities
```

你应看到：

- `implementation_ceiling = P1_DRY_RUN`；
- P0与P1 scaffold能力在 `implemented`；
- DB、Redis、真实 Solver、Vault、三审和 Evidence 在 `not_implemented`。

如果输出声称真实 Solver 已实现，而代码版本仍是 `0.1.0`，停止并审计代码；不能继续运行。

## 3. P0 preflight

### 3.1 当前站点的预期结果

```bash
.venv/bin/python seven-system/scripts/seven.py preflight \
  --config seven-system/config/runtime.example.json
```

当前应返回非零退出码和：

```json
{
  "overall_verdict": "BLOCKED",
  "side_effects": "NONE"
}
```

至少会有两个 blocker：

- `volume_readme`：`/data/README.md` 不存在；
- `data_root_ready`：`/data/seven-system-data/` 不存在。

这是正确的 fail-closed。Preflight 不会替你创建目录，也不会 fallback 到别处。

### 3.2 每项检查的含义

| Check | PASS 意义 | BLOCK 时怎么办 |
|---|---|---|
| `system_identity` | 配置确实属于 seven-system | 修正配置，不要绕过 |
| `repository_root` | 配置代码根精确等于实际Seven代码根 | 使用真实绝对路径，不得指向替身目录 |
| `volume_mounted` | D盘是实际mount point且非symlink | 停止；不得用同名本地目录替代 |
| `volume_readme` | 卷用途和目录规则可审计 | 先批准并补卷 README |
| `data_root_boundary` | 数据根是 D 盘严格子目录且不在 repo | 修正路径 |
| `data_root_ready` | 数据根已由操作者批准创建且可写 | 人工准备后重跑 |
| `data_root_device` | 数据根与批准卷是同一设备，README hash可冻结 | 修复挂载/路径；缺根时先处理上一项 |
| `disk_capacity` | 空间高于配置阈值 | 清理方案另行审批，不自动删证据 |
| `expected_database` | live 模式精确命中专用 DB | `source .env` 后核对；不允许默认值 |
| `queue_namespace` | 不碰生产 `math:*` | 使用 `evidence:seven:` |
| `solver_harness_present` | live时唯一合法Harness入口存在；dry-run为NOT_REQUIRED | 修复代码/路径，不旁路 |
| `solver_root_isolation` | 两个Solver根互异，均在Seven数据根内且repo外 | 修正路径，禁止复用题海生产根 |
| `no_tool_policy` | 所有实验臂同为 `forbid_all` | 禁止降级 |
| `launch_interval_floor` | 不低于历史 3 秒站点下限 | 修正配置 |
| `solver_asset_contract` | canonical AGENTS 有必要终止和禁工具规则 | 修复资产并重测 |
| `answer_vault_boundary` | Vault 不在 Solver 工作根 | 修正物理边界 |
| 四类 capability | live 依赖已由独立报告证明 | 报告未 PASS 就保持 BLOCKED |

`preflight` 是只读命令：不连接数据库、不写 Redis、不启动 Solver、不创建数据根。

## 4. 准备站点配置

只有用户批准 D 盘 README 和数据根后，才复制站点配置：

```bash
cp seven-system/config/runtime.example.json \
  seven-system/config/runtime.local.json
```

`runtime.local.json` 已被本目录 `.gitignore` 忽略。它不应包含密钥；密钥仍只来自受控环境。

检查这些字段：

- `mode` 当前只能是 `dry_run`；
- `repository_root` 是当前 worktree 的 `seven-system`；
- `volume_root` 与 `data_root` 是批准后的绝对路径；
- `allow_writes=false`；
- `allow_live_dispatch=false`；
- `redis_namespace` 以独立的 `evidence:seven:` 开头；
- capability reports 在 dry-run 可为 `null`。

配置会在转换为运行时对象前执行`runtime-config.schema.json`；未知字段、类型错误和非法常量都会直接拒绝，不会静默忽略。

不要为了让 preflight 变绿而把 `require_volume_readme` 改成 `false`；站点正式配置应保留这个保护。

## 5. 初始化一个 Epoch

Preflight PASS 后执行：

```bash
.venv/bin/python seven-system/scripts/seven.py init-epoch \
  --config seven-system/config/runtime.local.json \
  --epoch-id dryrun-001
```

成功后输出 `epoch_root` 和 `manifest_hash`。相同 Epoch、相同配置重复执行只返回 `ALREADY_INITIALIZED`；不同配置试图复用同一 Epoch ID 会拒绝。

每次重入都会重新执行P0；卷README、挂载、源码树或目录边界漂移时不会因为Epoch已存在而绕过检查。

Epoch 目录里的文件一旦提交就不要手改。需要改配置时创建新 Epoch。

## 6. 执行 P1 dry-run

```bash
.venv/bin/python seven-system/scripts/seven.py dry-run \
  --config seven-system/config/runtime.local.json \
  --epoch-id dryrun-001
```

PASS 需要同时满足：

1. 首次探针提交成功；
2. 同内容重复提交返回 `ALREADY_COMMITTED`；
3. 异内容写到同一路径被拒绝；
4. 初始文件seal、源码树、卷/README指纹与manifest完整；
5. 追加P1 GateDecision、后续checkpoint、P1 scaffold verdict；
6. P1文件seal链接初始integrity index，并由Epoch外local receipt分别锚定两级index；
7. 当前命令范围没有DB、Solver或Redis adapter入口（报告中的0是静态命令范围声明，不是外部计数器）。

查看持久报告：

```bash
python3 -m json.tool \
  /data/seven-system-data/epochs/dryrun-001/dry-run-report.json
```

这一PASS只证明P1 scaffold原语和最小append-only Gate闭合；不证明387号完整P1、P2-P9或任何Tell效果。

## 7. 查看状态与验证

```bash
.venv/bin/python seven-system/scripts/seven.py status \
  --epoch-root /data/seven-system-data/epochs/dryrun-001

.venv/bin/python seven-system/scripts/seven.py validate-epoch \
  --epoch-root /data/seven-system-data/epochs/dryrun-001
```

`status` 给出：

- Epoch/manifest 身份；
- 当前 mode；
- 文件完整性；
- dry-run verdict；
- 最新runtime state与P1 scaffold verdict；
- `scientific_claim=NOT_TESTED`。

`validate-epoch`真正执行本版Schema子集，重算两级文件hash并核对Gate/report/checkpoint/verdict交叉引用与Epoch外local receipt。它把`artifact_integrity`和`current_runtime_compatibility`分开：旧Epoch可保持物证PASS，同时因当前源码/卷漂移而禁止resume。local receipt不是签名/WORM，因此这仍只是“scaffold物证是否一致”的检查，不是最终确认性证据根或“科学主张正确”检查。

## 8. 退出码

| 退出码 | 含义 |
|---|---|
| `0` | 命令完成；对 preflight 表示没有 blocker |
| `2` | 配置错误、preflight BLOCKED、身份冲突或 I/O 错误 |
| `3` | dry-run FAIL，或 Epoch 完整性/`current_runtime_compatibility` 未 PASS |

自动脚本必须检查退出码，不能只 grep 输出中的 `PASS`。

## 9. 故障处理

### Preflight BLOCKED

按 `blockers` 修复物理前置条件，再完整重跑。禁止编辑 preflight report 来“通过”。

### `ContentConflictError`

这表示同一路径已经存在不同内容。不要覆盖、删除或换 hash；把 Epoch 放入人工审查，确认是错误复用 ID、并发提交还是物证污染。修复后使用新 Epoch ID。

### manifest hash mismatch

说明冻结文件被修改或损坏。该 Epoch 不再可信。保留现场，记录原因，不要直接重写 manifest。

### D 盘掉线或路径变化

停止。不得创建同名本地目录伪装挂载点。重新挂载并核对卷 README、设备和数据根后，再运行 preflight/status。

### DB 名错误

未来 live 命令前：

```bash
set -a; source .env; set +a
echo "$ARANGO_DB"
```

不是 `xishujuzhen_math_glm52` 就停止。当前 v0.1.0 不会连接 DB。

### 发现真实 Solver 或 Redis 被修改

v0.1.0 不应产生这些副作用。立即停止，把本次运行判为 protocol invalid，并审计入口脚本；不能继续把结果当 dry-run PASS。

## 10. 当前没有 start/stop/recover 命令

Seven v0.1.0 没有常驻服务，所以：

- 没有 `start`；
- 没有 `stop`；
- 没有 `pause/resume/drain`；
- 没有 `recover --apply`；
- 没有 `clear` 或删除命令。

不要拿题海系统的 `pipe_control.py start` 冒充 Seven 的运行入口。未来实现常驻控制面后，手册将明确区分：

- `pause`：停止新 claim，保留安全 in-flight；
- `drain`：停止新 dispatch，等待并 seal 现有任务；
- `stop`：checkpoint + reconcile，不默认 kill Solver；
- `recover`：永远先只读计划，再由显式 apply 执行。

## 11. 运行中检查者原则（未来 live 预留）

当真实 worker 存在后，Master Agent 是检查者，不是旁观者：

- 看控制面 status、队列流动、worker heartbeat 与真实 attempt activity；
- 看 D 盘空间、artifact backlog、审计 backlog、Judge 分歧和 holdout 访问；
- 不用长 sleep 干等；
- 发现新故障，先把检测写进统一 health 命令，再修服务；
- DB 数字不能代替进程、文件和事件物证。

这些原则继承题海系统的有效经验，但 Seven 不复用其 fail-open 工具审计、全局 `math:*` 队列或 `clear` 操作。

## 12. 结束本轮前的核对

- [ ] `capabilities` 仍明确 P1 上限；
- [ ] preflight report 与实际卷/路径一致；
- [ ] Epoch manifest hash 验证 PASS；
- [ ] dry-run 三类副作用均为 0；
- [ ] 未手改已提交文件；
- [ ] 未启动 Solver、未写 DB/Redis；
- [ ] `verdict.json` 仍写科学结论 `NOT_TESTED`；
- [ ] 下一步 blocker 已记录，而不是被静默忽略。
