> 本文档从 AGENTS.md 迁出（2026-08-03），记录 Master-Worker 架构和自动化系统。工程开发恢复时查阅。

## Master-Worker架构与完整性审计（2026-07-09 新增）

**架构目标**：用Master Agent控制sub-agents在tmux中执行古籍研究任务，确保内容完整性。

**核心组件**：

| 组件 | 文件 | 功能 |
|---|---|---|
| **Master Agent** | `master.py` | 主控脚本：分配任务/记录检查点/完成任务/验证完整性 |
| **Worker Agent** | `worker.sh` | 启动脚本：在tmux中启动 opencode 或 Devin CLI 执行任务 |
| **任务队列** | `tasks.json` | 任务状态管理：queued/leased/completed |
| **Path树** | `build_path_tree.py` | 构建《星平会海》完整path树（精确到每一行） |
| **完整性验证** | `verify_integrity.py` | 全量验证/行级验证/审计日志 |

**Master命令**：
```bash
# 查看系统状态
python3 master.py status

# 分配任务
python3 master.py assign --task-id 20.4 --worker-id W1

# 记录检查点
python3 master.py checkpoint --worker-id W1 --task-id 20.4 --phase <PHASE> --cursor-line <LINE> --evidence-count <COUNT> --note '<NOTE>'

# 完成任务
python3 master.py complete --task-id 20.4 --result '<RESULT>'

# 报告行级覆盖
python3 master.py report-line-coverage --worker-id W1 --task-id 20.4 --section-id 卷一/星曜躔度歌 --start-line 1 --end-line 130 --content-hash <SHA256>

# 验证section完整性
python3 master.py verify-section --worker-id W1 --task-id 20.4 --section-id 卷一/星曜躔度歌

# 全量验证
python3 master.py verify-complete --document 星平会海

# 停止门检查
python3 master.py may-stop
```

**Worker启动**：
```bash
# 基本启动
./worker.sh --worker-id W1 --task-id 20.4

# 带行级参数启动
./worker.sh --worker-id W1 --task-id 20.4 --start-line 1 --end-line 130 --section-id 卷一/星曜躔度歌

# 使用 Devin CLI
./worker.sh --provider devin --worker-id W1 --task-id 20.4
```

**完整性审计结果**（2026-07-09 测试）：
- Path树：10卷 / 246节 / 79子节 / 307规则
- 卷覆盖：10/10 (100%)
- 节覆盖：246/246 (100%)
- 规则覆盖：307/307 (100%)
- 行级报告：1-130 (130行) 已验证

**审计日志位置**：`runtime/audit_logs/`

## Devin CLI 非线性运行时支撑（2026-07-10 新增）

本项目未来可以由 Devin CLI 支撑，但不能把这个迁移理解成简单替换命令行工具。MOIRA 的运行时是非线性的：系统会从 `S-n` 吸收经验包，发现新维度，提升成熟度，改变可计算性，再反过来生成新的任务和审计要求。

因此，Devin 进入本项目时必须先读取 runtime capsule，而不是只依赖上下文记忆。项目已新增 `.devin/config.json`、`.devin/hooks.v1.json`、`.devin/skills/`、`ai-runtime/protocol/`、`tools/moira_runtime.py` 和 `tools/agent_launcher.py`。Devin 的 `SessionStart` 与 `UserPromptSubmit` 会注入当前任务状态、Worker 状态、非线性维度覆盖、协议锚点和下一步动作。

**关于 Stop hook（2026-08-03 修订）**：本项目一般而言不需要 Stop hook。Stop hook 的设计初衷是防止 Worker 在任务没干完时就停，但装在项目级配置会对 Master session 也生效，导致 Master 在等待用户决策时被死循环拦截（详见 dev-docs/46 根因分析）。更智能的 stop hook 是让 Master agent 持续在 tmux 中监控 Worker 的运行——Master 主动观察 Worker 状态、任务账本和审计结果，在对话中判断是否该继续或停止，而不是用一个机械的 hook 强制拦截。Stop hook 已从 `.devin/hooks.v1.json` 移除，后续不要加回来。

默认 provider 仍是 opencode，以保护当前工作面。未来启动 Devin Worker 或 Auditor 时，使用 `--provider devin`，或设置 `MOIRA_AGENT_PROVIDER=devin`。无论 provider 是谁，Worker 仍必须输出维度、成熟度和可计算性，Auditor 仍必须把执行完成和语义通过分开。

## Devin Worker yolo 模式 + git worktree + 限流恢复（2026-07-10 新增）

**核心约束：最多 2 个 Devin Worker 实例**（算上 Master 共 3 个 Devin 进程）。超过会触发 API 限流，导致全部 Worker 白费工作。

**禁止用 subagent 派 Worker**。subagent 共享 Master 的 rate limit，10 个 subagent 同时跑会瞬间触发限流。Worker 必须用独立的 Devin CLI 进程，在独立 tmux 会话中运行。

**Worker 启动方式**：

```bash
# 方式一：用 launch_workers.sh 自动从 tasks.json 取任务并启动
./tools/launch_workers.sh                    # 启动 2 个 Worker
./tools/launch_workers.sh --max-workers 1    # 只启动 1 个

# 方式二：手动启动单个 Worker
./tools/worker_v2.sh --worker-id W1 --task-id auto.40 \
  --section-id 卷一/星曜照宫歌/兄弟宫 --start-line 302 --end-line 303
```

**worker_v2.sh 做了什么**：

1. **git worktree 隔离**：每个 Worker 在 `.worktrees/worker-<WID>/` 独立工作目录中运行，避免文件冲突。worktree 基于 main 分支创建，分支名 `worker/<WID>/<TID>`。
2. **Devin yolo 模式**：`devin --permission-mode dangerous --prompt-file <prompt> --export <transcript>`。dangerous 模式自动批准所有操作，无需人工确认。
3. **tmux 会话**：Worker 在 `tmux new-session -d -s worker-<WID>` 中运行，可 `tmux attach -t worker-<WID>` 查看。
4. **watchdog 监控**：`tools/watchdog.sh` 在后台监控 Worker tmux 会话状态。

**限流检测和自动恢复**：

watchdog 脚本（`tools/watchdog.sh`）每 30 秒检查一次 Worker tmux 会话：

| 情况 | watchdog 行为 |
|---|---|
| tmux 会话正常运行 | 继续监控 |
| tmux 会话退出 + 任务已完成 | 标记完成，watchdog 退出 |
| tmux 会话退出 + 检测到限流 | 等待 cooldown（默认 1800 秒 = 30 分钟）→ 重启 Worker 并发"继续" |
| tmux 会话退出 + 非限流错误 | re-queue 任务，watchdog 退出 |
| 超过最大重试次数（默认 5 次） | re-queue 任务，watchdog 退出 |

**限流检测方式**：检查 transcript 文件（`runtime/transcripts/*.devin.atif.json`）和 tmux pane 输出中是否包含 `rate limit` / `Reached overall message rate limit` / `limit will reset` 等关键词。

**"继续"机制**：限流恢复后，watchdog 在 worktree 目录中重新启动 devin，并发送"继续之前被限流中断的工作"提示词。Devin 会检查已有工作成果（AUDIT 文件、checkpoint），继续完成未完成的部分。

**检测间隔合理性**：

- **poll_interval = 30 秒**：tmux 会话状态检查间隔。30 秒足够及时检测到 Worker 退出，又不会过于频繁。
- **cooldown = 1800 秒（30 分钟）**：限流恢复等待时间。API 限流通常提示"28-30 分钟后重置"，30 分钟留足余量。
- **max_retries = 5 次**：最多重试 5 次限流恢复。超过则 re-queue，避免无限循环。

**关键文件**：

| 文件 | 功能 |
|---|---|
| `tools/launch_workers.sh` | 启动器：从 tasks.json 取任务，启动最多 2 个 Worker |
| `tools/worker_v2.sh` | Worker 启动脚本 v2：git worktree + Devin yolo + tmux + watchdog |
| `tools/watchdog.sh` | 监控脚本：限流检测 + cooldown + 自动重启 + "继续" |
| `.worktrees/worker-<WID>/` | Worker 独立工作目录（git worktree） |
| `runtime/prompts/` | Worker 提示词文件 |
| `runtime/transcripts/` | Devin 会话导出文件 |
| `runtime/watchdog_logs/` | watchdog 日志 |

## 系统脚本架构与调用关系（2026-07-10 补全）

**四个主控脚本的分工**：

| 脚本 | 定位 | 角色 |
|---|---|---|
| `master.py` | **手动控制接口** | 分配任务/记录检查点/完成任务/验证完整性/启动Auditor。AI（Master Agent）通过 CLI 命令直接调用 |
| `master_controller.py` | **自动化循环控制器** | 最高层。循环调用 factory.py + self_iteration.py，实现无人值守运行 |
| `factory.py` | **Worker 生命周期管理** | 从 schema.json 自动发现任务、动态创建 Worker、分配任务、检查完成 |
| `self_iteration.py` | **自我迭代引擎** | 从吸收结果中发现新任务、动态调整吸收策略、构建知识图谱 |

**调用关系图**：

```
AI Master Agent（如 Devin CLI）
    │
    │ 直接调用 master.py CLI 命令
    ↓
master.py（手动控制）
    │ 读写 tasks.json, runtime/checkpoints/, runtime/audit_logs/
    │ subprocess → auditor.py, tools/agent_launcher.py, tmux
    │
    │ 或者由自动化控制器接管
    ↓
master_controller.py（自动化循环）
    │ 读写 runtime/master_state.json, tasks.json
    │ subprocess → factory.py --action run/status
    │ subprocess → self_iteration.py --action iterate/status
    ↓
factory.py（Worker 工厂）
    │ 读写 tasks.json, runtime/factory_state.json
    │ 读 dev-docs/原典/星平会海/schema.json → 自动发现 auto.* 任务
    │ subprocess → worker.sh（旧）或 tools/worker_v2.sh（新）
    ↓
self_iteration.py（自我迭代）
    │ 读写 runtime/iteration_state.json
    │ 读写 runtime/absorption_strategy.json
    │ 读写 runtime/knowledge_graph.json（尚未创建）
    │ 读写 tasks.json → 生成 explore.*/random.* 任务
```

**非线性状态文件**：

| 文件 | 写入者 | 读取者 | 内容 |
|---|---|---|---|
| `runtime/iteration_state.json` | `self_iteration.py` | `self_iteration.py`, `tools/moira_runtime.py` | 迭代次数、发现列表、生成的新任务 |
| `runtime/absorption_strategy.json` | `self_iteration.py` | `self_iteration.py`, `tools/moira_runtime.py` | 当前阶段(exploration)、6维度覆盖率、非线性权重 |
| `runtime/knowledge_graph.json` | `self_iteration.py` | `self_iteration.py`, `tools/moira_runtime.py` | 算子/集合/命题/关系/概念/发现（尚未创建，系统未进入知识积累阶段） |
| `runtime/master_state.json` | `master_controller.py` | `master_controller.py` | 主控状态、周期数、发现数 |
| `runtime/factory_state.json` | `factory.py` | `factory.py` | 工厂状态 |

**moira_runtime.py 如何使用这些文件**：`tools/moira_runtime.py` 的 `nonlinear_state()` 函数读取 `iteration_state.json`、`absorption_strategy.json`、`knowledge_graph.json`，生成 runtime capsule 中的 `nonlinear_phase`、`iteration_count`、`dimension_coverage`、`lowest_coverage_dimensions` 等字段。这就是 SessionStart/UserPromptSubmit hook 注入的"当前系统状态"的来源。

## 双账本架构：tasks.json vs dev-docs/todos.json（2026-07-10 补全）

**两个文件是平行的，没有映射关系**：

| 账本 | 文件 | 管理工具 | ID 格式 | 用途 |
|---|---|---|---|---|
| **执行账本** | `tasks.json` | `master.py`, `factory.py` | `auto.N`, `random.N`, `explore.N` | Worker 实际执行的任务队列（文献考据、探索等） |
| **规划账本** | `dev-docs/todos.json` | `todo.py` | `phase.N`（如 20.4, 13.1） | 项目建设的长期规划（Phase 1-25） |

**auto.* 任务的来源**：`factory.py` 的 `discover_tasks_from_schema()` 从 `dev-docs/原典/星平会海/schema.json` 自动生成 `auto.N` 考据任务，每个 subsection 生成一个。

**runtime-manifest.json 的定义**：`ai-runtime/protocol/runtime-manifest.json` 中明确标注了 `tasks.json` = execution_tasks，`dev-docs/todos.json` = todo_truth。

## Worker 执行流程与 AUDIT 文件（2026-07-10 补全）

**Worker 提示词**（`worker_prompt.py` 生成，约200行）：
- **核心思维力提示词**（~150行）：形式化五问、定量化意识、开放性意识、全息意识、时代性意识、PathListGate 硬门
- **动态任务信息**（~50行）：任务ID、标题、Section ID、行范围、执行步骤、汇报要求
- **不直接读取数据文件**：提示词要求 Worker 自己确认 `full_path_tree.json` 存在，而不是预加载内容

**Worker 产出物**：`dev-docs/AUDIT-auto.{N}-{section名}.md`，包含：
- PathListGate 验证（hash 比对）
- 原始文本内容（来源、文件、行号、歌诀、注释）
- 形式化五问（每条规则的算子/输入/输出/可求值性/一致性）
- 维度/成熟度/可计算性汇报（SOP 三要素）
- 跨文献对照、定量化/开放性/全息/时代性分析
- 审计判定（PASS + 理由）

**已知缺口**：AUDIT-auto.*.md 文件目前由 Worker 直接产出，**缺少 Auditor 的二次审查**。审计系统脚本已实现但未自动运行。

## 审计系统脚本架构（2026-07-10 补全）

**四个审计脚本的分工**：

| 脚本 | 定位 | 读写文件 | CLI 命令 |
|---|---|---|---|
| `auditor.py` | **Auditor Agent 主控** | 读 checkpoints/，写 auditor_prompts/ | `audit-section`, `audit-task`, `generate-report` |
| `audit.py` | **审计记录管理** | 读写 dev-notes/AUDIT-*.json，读 todos.json | `create`, `validate`, `report`, `list` |
| `sop_audit.py` | **SOP 汇报审计** | 读 checkpoints/，写 audit_logs/ | `audit-section`, `audit-task`, `report` |
| `quality_gate.py` | **质量门控** | 读 dev-notes/AUDIT-*.json, todos.json | `check`, `check-all`, `report` |

**审计流程**：

```
Worker 完成任务 → 汇报 SOP（维度/成熟度/可计算性）→ 保存到 checkpoint
    ↓
Master 调用 sop_audit.py 审计 SOP 汇报 → 保存到 runtime/audit_logs/
    ↓
Master 调用 master.py launch-auditor 启动 Auditor Agent
    ↓
auditor.py 生成审计提示词 → runtime/auditor_prompts/
    ↓
Auditor Agent（tmux 中）进行语义审计 → 保存到 runtime/audit_logs/
    ↓
Master 读取审计结果 → PASS 则任务完成 / FAIL 则 Worker 重新执行
```

**`master.py launch-auditor` 已实现**（第 685-798 行），支持 `--provider opencode/devin`，在 tmux 中启动 Auditor Agent。

**审计结果存储位置**：
- `runtime/audit_logs/` — 自动化审计日志（JSON）
- `runtime/auditor_prompts/` — 审计提示词（Markdown）
- `runtime/checkpoints/` — Worker 检查点（JSON）
- `dev-notes/AUDIT-*.json` — 结构化审计记录（由 audit.py 生成）
- `dev-docs/AUDIT-*.md` — Worker 手写的详细审计报告（Markdown）

**当前状态**：审计系统脚本已实现，runtime/audit_logs/ 中有 2026-07-09 的运行记录，但目前没有 Auditor 在运行。97 个 auto.* 任务的 AUDIT 文件缺少 Auditor 二次审查。

## 全 path 列表前置门（PathListGate · 2026-07-10 新增）

任何一本原典在正文处理前，必须先完成全 path 列表。这里的“处理”包括摘要、形式化、规则抽取、考据、审计和系统吸收。没有全 path 列表时，Master 不得派 Worker 读正文，Worker 不得自行开始正文处理，Auditor 不得给正文处理结果 PASS。

全 path 列表至少要覆盖：源文件、卷、篇、章、节、子节、规则、行号范围、稳定 path ID、原文定位和可复核 hash。对当前《星平会海》，已有入口是 `dev-docs/原典/星平会海/schema.json` 和 `dev-docs/原典/星平会海/full_path_tree.json`，构建脚本是 `build_path_tree.py`。后续处理其他书时，也必须先在该书目录下建立 `full_path_tree.json` 和 path 审计记录。

PathListGate 的判定口径是 remainder=0。也就是说，Master 要先证明这本书的 path list 覆盖完整、没有断裂、没有重复、能回到原文行号和内容 hash，再进入 Worker 分包。Worker 只能处理 Master 分配的 path ID 和行号范围；发现 path list 缺失、错位或无法定位时，必须停止正文处理并回报 Master 修 path。

## 优雅停止机制（2026-07-09 新增）

**停止命令**：

| 命令 | 功能 | 参数 |
|---|---|---|
| `shutdown` | 优雅停止系统 | `--force` 强制停止 |
| `cleanup` | 清理临时文件和会话 | 无 |
| `status-report` | 生成状态报告 | 无 |

**优雅停止流程**：

```
用户请求停止
    ↓
执行停止门检查 (may-stop)
    ↓
├── STOP_ALLOWED → 执行清理流程
└── CONTINUE_REQUIRED → 提示未完成任务
    ↓
清理流程
    ├── 终止所有Worker tmux会话
    ├── 保存检查点状态
    ├── 更新任务状态
    ├── 生成停止报告
    └── 清理临时文件
    ↓
系统停止完成
```

**停止报告内容**：

```json
{
  "shutdown_time": "2026-07-09T10:30:00",
  "shutdown_type": "graceful",
  "tasks_summary": {
    "total": 3,
    "completed": 2,
    "in_progress": 1,
    "queued": 0
  },
  "workers_summary": {
    "W1": {"status": "idle", "last_task": "20.4"},
    "W2": {"status": "idle", "last_task": "30.11"}
  },
  "checkpoints_saved": 5,
  "audit_logs_generated": 3
}
```

**资源清理清单**：

| 资源类型 | 清理方式 | 命令 |
|---|---|---|
| tmux会话 | 终止所有Worker会话 | `tmux kill-session -t worker-W1` |
| 检查点文件 | 保留在`runtime/checkpoints/` | 不清理（用于恢复） |
| 任务状态 | 更新为最终状态 | `tasks.json` |
| 审计日志 | 保留在`runtime/audit_logs/` | 不清理（用于审计） |
| 临时文件 | 清理`runtime/`下的临时文件 | `rm -rf runtime/temp/*` |

**使用示例**：

```bash
# 优雅停止（等待所有任务完成）
python3 master.py shutdown

# 强制停止（立即停止所有Worker）
python3 master.py shutdown --force

# 清理临时文件和会话
python3 master.py cleanup

# 生成状态报告
python3 master.py status-report
```

## 自动化系统设计（2026-07-09 新增）

**核心问题**：如何确保系统以非线性模式吸收目标文集，而不是沦为线性模式？

**解决方案**：三个核心脚本协同工作，实现完全自动化的非线性吸收。

### 1. 工厂脚本 (factory.py)

**功能**：管理Worker/Auditor的生命周期

**核心特性**：
- **动态Worker创建**：根据任务量自动创建Worker
- **自动任务分配**：将排队任务分配给空闲Worker
- **任务发现**：从schema.json和文本文件自动发现任务
- **完成检查**：定期检查Worker完成情况

**非线性策略**：
- **随机打乱卷顺序**：不按卷1→卷10的顺序处理
- **随机选择起始行**：在每个卷内随机选择处理区间
- **多区间处理**：每个卷处理3-5个随机区间，而不是整体处理

**使用方式**：
```bash
# 自动发现任务
python3 factory.py --action discover

# 创建Worker
python3 factory.py --action spawn-worker

# 运行工厂
python3 factory.py --action run --max-cycles 100
```

### 2. 自我迭代引擎 (self_iteration.py)

**功能**：实现系统的自我迭代机制

**核心特性**：
- **知识图谱构建**：记录已吸收的内容和发现的新概念
- **吸收策略调整**：动态调整吸收方式（探索→深化→整合）
- **新任务生成**：从吸收过程中发现新任务
- **跨体系关联**：发现七政四余与其他体系的关联

**非线性策略**：
- **探索新维度**：优先探索覆盖率低的维度
- **深化未完成内容**：研究未完成的算子和未知概念
- **随机探索**：随机选择新内容进行探索
- **跨体系关联**：发现不同体系之间的关联

**使用方式**：
```bash
# 运行迭代
python3 self_iteration.py --action iterate

# 查看状态
python3 self_iteration.py --action status

# 发现新任务
python3 self_iteration.py --action discover --count 5
```

### 3. 主控脚本 (master_controller.py)

**功能**：实现系统的完全自动化运行

**核心特性**：
- **周期运行**：定期运行迭代和工厂
- **优雅停止**：支持SIGINT/SIGTERM信号处理
- **状态监控**：实时监控系统状态
- **统计更新**：更新系统统计信息

**使用方式**：
```bash
# 运行主控
python3 master_controller.py --action run --max-cycles 100

# 查看状态
python3 master_controller.py --action status

# 优雅停止
python3 master_controller.py --action shutdown
```

## 非线性吸收策略

**核心思想**：不按线性顺序处理，而是根据多维度优先级和随机性动态选择处理内容。

**策略实现**：

1. **维度优先级**：
   - 算子维度（优先级1）
   - 集合维度（优先级2）
   - 命题维度（优先级3）
   - 状态维度（优先级4）
   - 时间维度（优先级5）
   - 体系维度（优先级6）

2. **吸收阶段**：
   - **探索阶段**：优先发现新维度和新概念
   - **深化阶段**：深化已发现但未完成的内容
   - **整合阶段**：整合各维度内容，构建完整体系

3. **非线性权重**：
   - **随机性**（0.3）：引入随机因素，避免线性处理
   - **优先级**（0.4）：根据维度优先级选择内容
   - **覆盖率**（0.3）：优先选择覆盖率低的维度

**自检机制**：

每次迭代后，系统必须自检：
1. **是否发现了新维度？**（新算子/新集合/新命题）
2. **各维度覆盖率是否提升？**（不是简单的数量增加）
3. **是否构建了新的可计算模型？**（形式/定量/推演）
4. **是否发现了跨体系关联？**（七政四余与八字/紫微/周易）
5. **是否发现了新问题？**（开放性，不预设终点）

## 使用流程

**1. 启动系统**：
```bash
# 方式1：使用主控脚本（推荐）
python3 master_controller.py --action run --max-cycles 100

# 方式2：手动启动各组件
python3 factory.py --action run --max-cycles 100 &
python3 self_iteration.py --action iterate
```

**2. 监控系统**：
```bash
# 查看主控状态
python3 master_controller.py --action status

# 查看工厂状态
python3 factory.py --action status

# 查看迭代状态
python3 self_iteration.py --action status
```

**3. 停止系统**：
```bash
# 优雅停止
python3 master_controller.py --action shutdown

# 或使用Ctrl+C
```

## SOP汇报审计（2026-07-09 新增）

**审计目标**：确保Worker按照SOP要求汇报了维度/成熟度/可计算性三要素。

**SOP汇报要求**：

Worker在检查点中必须包含`sop_report`字段：

```json
{
  "dimensions": ["算子维度", "集合维度", "命题维度", "状态维度", "时间维度", "体系维度"],
  "maturity": {
    "coverage": "已提升",
    "consistency": "已验证",
    "evaluability": "已实现",
    "explanatory": "待建设",
    "quantitative": "待建设",
    "cross_system": "待建设",
    "verifiability": "已验证"
  },
  "computability": {
    "formal": "已实现",
    "quantitative": "待建设",
    "deductive": "待建设"
  }
}
```

**审计命令**：

```bash
# 审计单个section的SOP汇报
python3 master.py sop-audit --worker-id W1 --task-id 20.4 --section-id 卷一/星曜躔度歌

# 审计整个任务的SOP汇报
python3 master.py sop-audit --worker-id W1 --task-id 20.4
```

**审计维度**：

| 维度类型 | 说明 | 例子 |
|---|---|---|
| 算子维度 | 新发现的算子 | 躔/照/会/守/冲/合/拱/夹/刑 |
| 集合维度 | 新发现的集合 | Star/Mansion/Palace/Dignity |
| 命题维度 | 新发现的命题类型 | 躔度命题/照宫命题/交会命题 |
| 状态维度 | 新发现的状态 | 吉凶/强弱/旺衰/多少 |
| 时间维度 | 新发现的时间切片 | 原盘/大限/流年/小限 |
| 体系维度 | 新发现的体系 | 七政四余/八字/紫微/周易 |

**审计成熟度指标**：

| 指标 | 说明 |
|---|---|
| 覆盖率 | 系统能描述的现象范围 |
| 一致性 | 规则之间是否矛盾 |
| 可求值性 | 规则能否判定真假 |
| 解释力 | 能否说"为什么" |
| 定量化 | 能否给出数值结果 |
| 跨体系 | 能否与其他体系对接 |
| 可验证性 | 能否用命例验证 |

**审计可计算性层次**：

| 层次 | 问题 |
|---|---|
| 形式可计算 | 给定输入，能否算法化地得到输出？ |
| 定量可计算 | 能否给出数值结果？ |
| 推演可计算 | 能否从已知推出未知？ |

**审计结果示例**：

```json
{
  "status": "incomplete",
  "worker_id": "W1",
  "task_id": "20.4",
  "section_id": "卷一/星曜躔度歌",
  "dimension_audit": {
    "reported": false,
    "count": 0,
    "types": [],
    "missing": ["operator", "set", "proposition", "state", "time", "system"]
  },
  "maturity_audit": {
    "reported": false,
    "metrics": {},
    "missing": ["coverage", "consistency", "evaluability", "explanatory", "quantitative", "cross_system", "verifiability"]
  },
  "computability_audit": {
    "reported": false,
    "levels": {},
    "missing": ["formal", "quantitative", "deductive"]
  },
  "all_reported": false
}
```

## Auditor Agent（语义审计）

**架构目标**：实现职责分离，Master负责调度，Auditor负责语义审计。

**核心组件**：

| 组件 | 文件 | 功能 |
|---|---|---|
| **Auditor Agent** | `auditor.py` | 语义审计脚本：生成审计提示词/启动审计 |
| **审计提示词** | `runtime/auditor_prompts/` | 审计任务的详细提示词 |
| **审计结果** | `runtime/audit_logs/` | 审计结果和报告 |

**Auditor命令**：

```bash
# 审计单个section
python3 auditor.py audit-section --worker-id W1 --task-id 20.4 --section-id 卷一/星曜躔度歌

# 审计整个任务
python3 auditor.py audit-task --worker-id W1 --task-id 20.4

# 生成审计报告
python3 auditor.py generate-report
```

**Master启动Auditor**：

```bash
# 启动Auditor Agent进行语义审计
python3 master.py launch-auditor --worker-id W1 --task-id 20.4 --section-id 卷一/星曜躔度歌
```

**语义审计标准**：

| 审计维度 | 审计标准 | 评分标准 |
|---|---|---|
| **维度审计** | 维度类型是否正确分类？每个维度是否有具体例子？ | 0-10分 |
| **成熟度审计** | 每个指标是否有具体说明？指标之间是否有逻辑关系？ | 0-10分 |
| **可计算性审计** | 每个层次是否有具体说明？是否有可执行的算法？ | 0-10分 |

**审计流程**：

```
Worker完成任务
    ↓
Worker汇报SOP（维度/成熟度/可计算性）
    ↓
Master生成审计提示词
    ↓
Master启动Auditor Agent
    ↓
Auditor Agent进行语义审计
    ↓
Auditor生成审计结果
    ↓
Master读取审计结果
    ↓
审计通过 → 任务完成
审计不通过 → Worker重新执行
```

**使用示例**：

```bash
# 1. Worker完成任务并汇报SOP
python3 master.py checkpoint --worker-id W1 --task-id 20.4 --phase "考据完成" --cursor-line 130 --evidence-count 10 --note "已完成角宿11条规则的考据"

# 2. Master启动Auditor进行语义审计
python3 master.py launch-auditor --worker-id W1 --task-id 20.4 --section-id 卷一/星曜躔度歌

# 3. 查看审计结果
tmux attach -t auditor-W1-20.4

# 4. 审计通过后，完成任务
python3 master.py complete --task-id 20.4 --result "PASS"
```

## Worker提示词设计（思维力内化）

**核心问题**：如何确保Worker真正具备了AGENTS.md中的思维力要求？

**解决方案**：将思维力要求内化到Worker提示词中，而不仅仅是告诉Worker执行步骤。

**提示词生成器**：`worker_prompt.py`

```bash
# 生成Worker提示词
python3 worker_prompt.py --task-id 20.4 --task-title "审计A4：天干神煞" --section-id 卷一/星曜躔度歌/角 --start-line 1 --end-line 130
```

**思维力内化要求**：

| 思维力 | 内化方式 | 质量标准 |
|---|---|---|
| **形式化思维** | 每遇到命理规则，自动进行形式化五问 | 每条规则必须有明确的算子/输入/输出，必须可求值，必须与已有规则一致 |
| **定量化意识** | 每遇到程度描述，自动思考量化可能性 | 每个程度描述必须思考量化可能性，能量化必须给出公式，不能能量化必须说明原因 |
| **开放性意识** | 每遇到新概念，自动记录为"待发现" | 每个新概念必须记录为"待发现"，每个新算子/新工具必须保持敏感 |
| **全息意识** | 每遇到跨体系描述，自动思考同构关系 | 每个跨体系描述必须思考同构关系，每个同构关系必须记录并验证 |
| **时代性意识** | 每遇到具体事件，自动思考时代背景 | 每个具体事件结论必须思考时代背景，每个能量单位必须思考兑现方式 |

**汇报要求**：

Worker汇报SOP时，不仅仅是字段填充，而是**思维过程的外化**：

```json
{
  "dimensions": [
    {
      "type": "operator",
      "found": "拱",
      "input": "两颗星",
      "output": "拱格",
      "semantic": "两颗星形成特定角度关系"
    }
  ],
  "maturity": {
    "coverage": "从只能描述躔/照/会，到能描述躔/照/会/拱",
    "consistency": "验证了拱与躔/照/会不矛盾",
    "evaluability": "拱格现在可以判定真假"
  },
  "computability": {
    "formal": "给定两颗星的黄经，可以算法化判定是否形成拱格",
    "quantitative": "拱的紧密程度可以用角度差量化",
    "deductive": "从原盘可以推演出大限/流年是否激活拱格"
  }
}
```

**使用流程**：

```bash
# 1. 启动Worker（使用新的提示词）
./worker.sh --worker-id W1 --task-id 20.4 --start-line 1 --end-line 130 --section-id 卷一/星曜躔度歌/角

# 2. Worker执行任务时会自动进行思维力内化
#    - 形式化思维：每遇到命理规则，自动进行形式化五问
#    - 定量化意识：每遇到程度描述，自动思考量化可能性
#    - 开放性意识：每遇到新概念，自动记录为"待发现"
#    - 全息意识：每遇到跨体系描述，自动思考同构关系
#    - 时代性意识：每遇到具体事件，自动思考时代背景

# 3. Worker汇报SOP时会外化思维过程
#    - 不是简单列出"算子维度"，而是具体说明发现了什么新算子
#    - 不是简单说"已提升"，而是具体说明提升了什么
#    - 不是简单说"已实现"，而是具体说明实现了什么
```

## Layer A 考据审计日志

Phase 20 Layer A 审计逐项对照原文核对数据表和算法。已完成的审计项：

| 审计项 | 日期 | 结果 | commit | 考据记录 |
|---|---|---|---|---|
| **A3 十干化曜** | 2026-07-16 | ❌→✅ 发现庚辛壬癸四干化曜错位（天嗣被误当作独立化曜）。已修复。 | `ae1d865` | <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/AUDIT-LAYER-A-03.md" /> |
| **A2 四余定义** | 2026-07-16 | ❌→✅ 发现两个严重错误：(1) 紫炁错误使用 MEAN_APOG，改为28年线性运动；(2) 月孛错误使用 OSCU_APOG，改为 MEAN_APOG。另添加 true_as_north 开关。 | `3da1f20` | <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/AUDIT-LAYER-A-02.md" /> |
| **A27-A29 拦驾经/倒限详论/一寸金总诀** | 2026-07-08 | ✅ PASS（搜索+对照+决策完成；不直接实现代码，作为AI判读参考） | 待本次commit | <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/AUDIT-LAYER-A-27-29.md" /> |
| **A30 星曜入宫/躔宿/照宫/交会吉凶表** | 2026-07-08 | ✅ PASS（搜索+对照+决策完成；部分覆盖，不完整提取三辰通载表） | 待本次commit | <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/AUDIT-LAYER-A-30.md" /> |

### Phase 21 天文验证 + Phase 24 端到端验证（2026-07-08）

| 验证项 | 结果 | 说明 |
|---|---|---|
| **B7 节气UT** | ✅ PASS | 调整UTC→CST 8小时偏移后，误差<分钟级 |
| **B8 农历转换** | ✅ PASS | 11/11测试用例全部通过 |
| **B9 朔日** | ✅ PASS | 2024年14个朔日全部正确 |
| **B4-B5 ASC/MC** | ✅ PASS | 修复calc_houses恒星黄道bug后，与Java MOIRA差异<0.0001° |
| **B19 四柱干支** | ✅ PASS | 修复calc_four_poles 4个bug后，郑氏星案40/40全部匹配 |
| **Phase 24 端到端** | ✅ PASS | 郑氏星案40例四柱→公历→排盘，40/40全部匹配（100%） |

**calc_four_poles 修复的4个bug**（Phase 24验证期间发现）：
1. **节气分年月模式**：新增`use_solar_terms=True`，用回归黄道太阳位置判断节气月（节气基于回归黄道，不是恒星黄道，ayanamsa≈23.7°）
2. **年柱基准**：用1984=甲子作为基准（原代码用公元4年，错误）
3. **时柱hour_index**：`((adj_hour+1)//2)%12`（原缺少%12，23时算成12而非0）
4. **早子时规则**：23时后不跨日（果老星宗用早子时，23-0时属于当日子时）

**审计教训**：A3 和 A2 都暴露了 Phase 1-4 翻译的方法理缺陷——"只对比输出，不审计计算机制"。A2 尤为严重：紫炁在 Java 中是自定义线性轨道（`sign_computation_type=1`），翻译时直接套用了 `swe.MEAN_APOG`，导致所有涉及紫炁的排盘结果错误。Phase 24 进一步证明：四柱计算需要区分节气分年月（果老星宗/传统八字）和农历分年月（琴堂派），节气必须用回归黄道。

## TODO 管理（JSON 化 + 脚本化）

**禁止用 grep 查 TODO 状态。** TODO 的唯一真理源是 `dev-docs/todos.json`，用 `todo.py` 脚本管理。

### 文件

| 文件 | 用途 |
|---|---|
| `dev-docs/todos.json` | TODO 数据库（唯一真理源，115 个 TODO） |
| `todo.py` | 管理脚本：查询/更新/统计/添加 |
| `dev-docs/generate_todos.py` | 初始化脚本：从 dev-docs/06 和 07 的 Markdown 表格生成 todos.json（只需运行一次） |

### 常用命令

```bash
# 查询
python3 todo.py list                          # 列出所有 TODO
python3 todo.py list --phase 13               # 按 Phase 过滤
python3 todo.py list --status pending         # 按状态过滤
python3 todo.py list --search-preset 先搜索     # 按搜索预置过滤
python3 todo.py show 13.1                     # 查看单个 TODO

# 更新状态（开始做某个 TODO 时）
python3 todo.py update 13.1 --status in_progress
python3 todo.py update 20.4 --status completed --result "PASS" --commit abc123

# 统计
python3 todo.py stats                         # 总览
python3 todo.py stats --by-phase              # 按 Phase 统计
python3 todo.py stats --by-search-preset      # 按搜索预置统计

# 找下一个可做的事
python3 todo.py next                          # pending + 依赖满足的 TODO

# 搜索预置
python3 todo.py search-preset                 # 列出所有需要搜索的 TODO
python3 todo.py search-preset --only 先搜索     # 只看"先搜索"级

# 添加新 TODO
python3 todo.py add --phase 99 --id 99.1 --title "新任务" --search-preset 先搜索
```

### 搜索预置三级

每个 TODO 都有 `search_preset` 字段，决定动手前是否需要搜索：

| 级别 | 含义 | 数量 |
|---|---|---|
| 🔍 **先搜索** | 必须先搜索外部信息源（原文/参考数据/API文档）才能动手。不搜索 = 必然幻觉或用错数据 | 57 项 |
| 🔄 **边做边搜索** | 主体是工程任务，过程中有特定细节需要核对 | 8 项 |
| ⚙️ **不需要** | 纯工程任务，不需要搜索 | 47 项 |

**执行 🔍 先搜索 的 TODO 前，必须完成：web_search → webfetch → 记录考据 → 确认充分 → 才能动手。**

详见 <ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/07-文献考据总体规划.md" /> §9。

### 执行纪律：同步更新 TODO + keep git clean

执行任何计划的过程中，必须遵守以下纪律：

1. **同步更新 TODO List**：
   - 开始做某个 TODO 时：`python3 todo.py update <id> --status in_progress`
   - 完成时：`python3 todo.py update <id> --status completed --result "..." --commit <hash>`
   - 被阻塞时：`python3 todo.py update <id> --status blocked --note "阻塞原因"`
   - **禁止只做不更新**——TODO 状态必须实时反映真实进度

2. **keep git clean**：
   - 完成一个逻辑工作单元后，立即 commit
   - commit 后确认 `git status` 回到 clean 状态
   - 禁止积压多个未提交的改动
   - 禁止在 dirty 状态下开始下一个 TODO

## 术语备忘

- **"紫气" = 紫炁**：四余之一（紫炁 qì，木之余）。用户输入法打不出"炁"字，日常用"紫气"指代。代码中统一用"炁"（如 `mean_apog_ziqi`、`shen_sha_complete.json` 中的 `qi_stars`），AI 读到用户说"紫气"时应理解为"紫炁"。同理"气"在七政四余语境下通常也指"炁"。

---

## TODO List 工作协议（正式项目纪律）

**目的**：确保所有后续工作（尤其是进入实战后的持续演进）不只活在聊天记录或个人记忆中，而是**必须先落实到一份集中式、可读的 TODO List**，并形成可传承的工作意识。

**核心文件**：
- `dev-docs/26-后续TODO-List.md`：高层次、面向人的**主 TODO List**（活文档）。
- `dev-docs/todos.json` + `todo.py`：颗粒度执行层（已有的 JSON 化管理）。

**协议内容**：

1. **落盘纪律**（强制）
   - 任何新发现的 TODO（包括实战中踩到的坑、用户反馈、新需求），必须在 24 小时内补充到 `dev-docs/26-后续TODO-List.md`。
   - 重大或跨阶段的 TODO，必须同步更新 AGENTS.md 中的"已知缺口"或本协议相关段落。
   - 禁止只在聊天中讨论而不落盘。

2. **更新时机**（必须执行）
   - 每完成一个大阶段（Phase 或一批实战命例）后，立即 review 并更新主 TODO List。
   - 进入新阶段（例如从审计进入实战）前，必须把该阶段所有准备工作写入主 TODO List。
   - 每季度进行一次全面审查（优先级调整、依赖清理、已完成归档）。

3. **主列表与执行层的关系**
   - `dev-docs/26-后续TODO-List.md` 记录"为什么要做""影响哪个入口""优先级与依赖"。
   - `todos.json` 记录"具体怎么做""当前状态""搜索预置"。
   - 所有待执行的 TODO 最终都要通过 `todo.py` 管理执行，但高层次可见性必须保留在主列表。

4. **实战特别要求**
   - 在开始任何真实命例前，必须确认 `dev-docs/26-后续TODO-List.md` 中的"实战前必须完成的准备工作"已全部完成或有明确计划。
   - 实战过程中发现的新缺口，必须立即补充到主列表，并标记"实战中发现"。

5. **审查与传承**
   - 本协议本身是项目级工作纪律，任何新加入的开发者或 AI session 都必须先阅读本节。
   - 维护主 TODO List 的意识，是本项目"从给人看 → 给 AI 看"之后，进一步"给未来自己看"的核心文化。

**最后更新**：2026-07-08（本协议正式确立）。
