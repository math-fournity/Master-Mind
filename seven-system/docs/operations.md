# Seven System 操作手册

## 一句话结论

当前 Seven System 能安全运行 P0/P1 scaffold，以及 WP-1 Strict DB 的离线契约报告：这些命令都不连接真实数据库、不写 Redis、不启动 Solver，也不调用Codex或其他远程认知Worker。它不是387号完整P1；没有`start`命令是刻意的安全边界。

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
- P0/P1 scaffold、`WP1_SITE_STORAGE_PREREQUISITE`和`WP1_STRICT_DB_OFFLINE_CONTRACT_REPORT`在 `implemented`；
- `DATABASE_SITE_CAPABILITY_OR_MIGRATION_APPLY`、Redis、真实 Solver、Vault、三审和 Evidence 在 `not_implemented`。

当前`capabilities`若声称`TargetSolverPort`、`ModelRolePort`、Codex adapter、QuestionRelease或AuthoringBakeoff已经实现，立即停止并审计代码。387/389号已记录用户确认继续推进的多模型设计方向，不等于细节已最终验收，更不等于本版已有任何模型调用入口。

当前v0.1机器枚举尚未逐项列出这些新对象；遗漏不是PASS，而是`NOT_IMPLEMENTED`。不要为补显示文字直接改动绑定WP-1 Strict Contract hash的CLI代码；该同步必须在后续代码工作包中连同测试和新版离线报告一起完成。

如果输出声称真实 Solver 已实现，而代码版本仍是 `0.1.0`，停止并审计代码；不能继续运行。

## 3. P0 preflight

### 3.1 当前站点的预期结果

```bash
.venv/bin/python seven-system/scripts/seven.py preflight \
  --config seven-system/config/runtime.example.json
```

2026-08-14，D 卷 README 和数据根已由用户批准并准备完成。当前示例配置应返回退出码 `0` 和：

```json
{
  "overall_verdict": "PASS",
  "side_effects": "NONE"
}
```

这个 PASS 只表示 **dry-run P0** 的卷、路径、容量和静态配置检查通过。由于 dry-run 中 `expected_database` 和 `database_capability` 都是 `NOT_REQUIRED`，它不证明逻辑DB站点能力、ArangoDB engine在D盘，也不解锁Schema初始化或live。

如果 README、数据根或挂载漂移，仍应立即恢复为非零退出和 `BLOCKED`。Preflight 不会替你修复目录，也不会 fallback 到别处。

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
| 现有四类 capability | v0.1.0为DB、Safe Launch、No Tool、Answer Isolation预留的live依赖 | 任一报告未PASS就保持BLOCKED；它们不是387完整P0 |
| Harness资源 capability（未来） | 逐字段证明token/context/reasoning/timeout等ResourceContract是requested、enforced、observed或unavailable | 不得用Safe Launch替代；当前无完整consumer |
| 认知Worker capability（未来） | 对实际adapter/model/role配置证明requested/effective模型与权限/事件能力 | 当前无Schema或consumer；六类中缺任一适用项，P3/P6保持NOT_IMPLEMENTED/BLOCKED |
| HumanGate readiness（未来，非模型能力报告） | 冻结actor roster、职责分离policy、签名/验签和HUMAN_PENDING语义 | 当前未实现；缺失时所有人工Gate lane保持HUMAN_PENDING/BLOCKED |

`preflight` 是只读命令：不连接数据库、不写 Redis、不启动 Solver、不创建数据根。

## 4. 准备站点配置

D 盘 README 和数据根已经批准；需要保存站点本地覆盖时才复制配置：

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

## 4.1 生成或复验 Strict DB 离线报告

唯一已实现的 WP-1 DB 命令是：

```bash
.venv/bin/python seven-system/scripts/seven.py wp1-db-contract-report \
  --config seven-system/config/runtime.example.json \
  --report-id wp1-contract-20260814-002
```

它先要求dry-run P0 preflight PASS，再用`python -I -S -B`启动只输出机器JSON的受控runner；子进程环境不继承调用者的`PYTHONPATH`、sitecustomize或`ARANGO_*`凭据。机器收据绑定完整test IDs，并把allowlist和13索引语义测试列为required evidence。随后执行`wp1-strict-db-contract-report.schema.json`和跨字段semantic verifier，最后把报告通过Seven API append-once提交到批准的数据根。它的允许副作用只有本地报告文件提交；报告内以下外部副作用必须全为0：DB connection/write、migration、容器重启、Redis write、Solver launch。

当前固定报告：

```text
path=/data/seven-system-data/capabilities/strict-db-contract/wp1-contract-20260814-002.json
status=ALREADY_COMMITTED
verdict=PASS
subject_hash=77c6e348b4124a53080322d5cbe478b5ded3c8bea31dfc4555ac320aaa97799b
implementation_hash=656d6e807ad2e5f1e0b237145cfef94640b5eddd6054fc47d3c51111a1cc609e
test_execution_receipt_sha256=055ac2d9d9479663b529888295701ddc7f347830bfbbb1372ece775534e4533a
file_sha256=68c96aa4eec1fa8f7fc0e55222f6395c7b9096c683cae85f15888bc323c64b71
isolated_runner_tests=20
full_tests=58
```

重复执行同一命令会重新运行受控测试、重算当前 subject 并复验已有文件；完全匹配时返回 `ALREADY_COMMITTED`。代码、spec、绑定测试、Schema或validator漂移后，旧ID会报错且不会被覆盖。完成新一版评审后应使用新的report ID追加报告，禁止编辑、删除或覆盖旧报告。

`wp1-contract-20260814-001.json`是在后续源码硬化前生成的历史报告，现为`STALE/SUPERSEDED`，必须保留且不得覆盖；只有002与当前subject匹配，是本轮当前物证。

这个PASS只关闭`G-WP1-C`。报告自身明确写出六项非主张：不证明DB site capability；不验证物理DB存储；不连接Arango或apply migration；不提供durable migration ledger/fence/resume；不证明runtime append-only/CAS/outbox delivery语义；不认证wall-clock或文件不可变性。`generated_at`由builder生成且调用者不能注入，但verifier只核对时区化ISO-8601格式，不提供可信时间证明。本地文件也不是WORM。

### 4.2 仍不存在或禁止的 DB 操作

当前CLI只有离线`wp1-db-contract-report`，不要把文档里的能力名称猜成子命令：

- 生产database package只有确定性只读`plan_migration`，没有operator site-plan/site-verify命令；
- Site v1 Schema只是未被消费且已被新决策取代的前向shape，没有site report generator或semantic verifier；Schema-valid不等于capability-valid，禁止消费v1；
- 生产package和真实Arango adapter中都不存在apply、DDL、authorization或receipt primitive；
- Seven Schema初始化的任何DDL仍被禁止，直到逻辑站点v2核验、计划哈希、受控入口和人工授权全部完成；若要把Arango从容器writable overlay改成专用bind/volume，这是另一个独立维护事项，也必须另有方案与授权。

不得用ad hoc raw client、私有导入或临时脚本补出不存在的站点/写入入口。

目标架构已经确认复用原Arango服务和逻辑数据库`xishujuzhen_math_glm52`，但只使用`seven_*_v1`命名空间。当前`G-WP1-L/I=NOT_IMPLEMENTED`，所以仍不能声称真实site capability或执行Schema初始化。宿主物理字节经OrbStack `data.img.raw`落在D盘，记为`A-WP1-D=PASS`；未使用Arango专用bind、仍在容器writable overlay，记为`A-WP1-BIND=WARNING_NOT_DEDICATED`。这两个存储状态都不能解锁逻辑接入。

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
| `2` | 配置错误、preflight BLOCKED、身份/报告冲突、Strict DB受控测试失败或 I/O 错误 |
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

### WP-1 DB逻辑复用、D-backing与专用bind告警

当前共享ArangoDB的host bind `/data/arangodb/data -> /data`没有承载实际engine data directory `/var/lib/arangodb3`。与此同时，OrbStack的group-container data symlink指向`/data/OrbStack/data`，实时OrbStack进程打开其中的`data.img.raw`，所以容器writable overlay的宿主物理字节确实由D盘承载。处理时必须拆成三层：

1. 保持服务原状，不停止、不重启、不复制 engine 数据；
2. 宿主D-backing记录为`A-WP1-D=PASS`；它只说明物理承载位置；
3. 专用bind状态记录为`A-WP1-BIND=WARNING_NOT_DEDICATED`；它说明容器删除/重建、备份和搬运边界仍需运维硬化；
4. `G-WP1-L/I=NOT_IMPLEMENTED`，离线contract或物理存储PASS都不能冒充真实站点或Schema初始化PASS；
5. 任何Seven DDL都必须等v2 site verifier、计划哈希、人工授权和受控入口，不能用临时raw client补齐；
6. 若未来确需改成专用bind/volume，另写维护、备份、回滚与生产影响方案并单独授权；不要把这个动作称为“迁到D盘”。

### 发现真实 Solver、认知Worker或 Redis 被调用/修改

v0.1.0 不应产生这些副作用。任何Devin启动、Codex/API调用、远程model event或Redis变化都必须立即停止，把本次运行判为protocol invalid，并审计入口脚本；不能继续把结果当dry-run PASS。

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

未来worker必须分池观察：`author_pool`看草稿/费用/泄漏与最大修订数，`review_pool`看独立性和审稿backlog，`judge_pool`看盲化与分歧，`solver_pool`看无工具、launch interval和等资源arm。不得用solver总并发代表所有pool健康，也不得在某个pool阻塞时手工调用当前Codex会话补结果。

这些原则继承题海系统的有效经验，但 Seven 不复用其 fail-open 工具审计、全局 `math:*` 队列或 `clear` 操作。

## 12. 结束本轮前的核对

- [ ] `capabilities` 仍明确 P1 上限；
- [ ] preflight report 与实际卷/路径一致；
- [ ] Strict DB报告重新验证PASS，subject/file hash与记录一致；
- [ ] `G-WP1-L/I`仍为NOT_IMPLEMENTED，没有用离线PASS替代site PASS，也没有消费已废止的Site v1合同；
- [ ] `A-WP1-D`仍按宿主存储链证据记录为PASS，没有被误写成site或Schema能力PASS；
- [ ] `A-WP1-BIND`仍记录为WARNING_NOT_DEDICATED，没有把D-backing PASS误写成已使用专用bind；
- [ ] Epoch manifest hash 验证 PASS；
- [ ] dry-run 三类副作用均为 0；
- [ ] 未手改已提交文件；
- [ ] 未启动 Solver、未写 DB/Redis；
- [ ] 未调用Codex或其他远程认知Worker；`ModelRolePort`、QuestionRelease、P3A/P3B/P3C与AuthoringBakeoff仍为NOT_IMPLEMENTED/NOT_RUN；
- [ ] `verdict.json` 仍写科学结论 `NOT_TESTED`；
- [ ] 下一步 blocker 已记录，而不是被静默忽略。
