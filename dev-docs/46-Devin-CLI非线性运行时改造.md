# 46 · Devin CLI 非线性运行时改造

> 记录时间：2026-07-10
> 来源：将 MOIRA 从当前 opencode 支撑扩展为未来可由 Devin CLI 支撑的工作系统
> 关键词：Devin CLI，非线性运行时，Master-Worker，runtime capsule，hooks，skills

## 为什么记录

MOIRA 不是普通软件项目。它的运行时不是线性任务队列，而是一个会随着古籍吸收、形式化发现和命例验证不断演化的研究系统。

当前 opencode 体系已经有 Master、Worker、Auditor、tasks.json、checkpoint、audit log 和自我迭代引擎。问题在于，这些机制仍然依赖 AI 在长上下文中记住“为什么要这样做”。如果未来换成 Devin CLI，不能只把 `opencode run` 替换成 `devin`。真正需要迁移的是运行时约束：每次 Agent 启动、接收 prompt 或尝试停止时，都要重新获得当前系统状态、非线性演化状态、协议锚点和 stop gate。

## 运行时设计

本轮改造采用五层结构。

第一层是项目宪法。`AGENTS.md` 继续保存 MOIRA 的哲学、形式化规则、系统自我成长 SOP、TODO 纪律和 Master-Worker 入口。

第二层是 Devin 项目层。`.devin/config.json` 关闭从 Cursor、Windsurf、Claude 自动导入配置，防止别的工具规则污染 Devin。`.devin/hooks.v1.json` 在 `SessionStart`、`UserPromptSubmit` 和 `Stop` 阶段调用 MOIRA runtime capsule。

第三层是协议层。`ai-runtime/protocol/agent-anchors.json` 保存必须持续激活的规则锚点；`command-briefs.json` 保存 Master、Worker、Auditor 和 Stop 的角色 brief；`runtime-manifest.json` 保存 ledgers、provider 和 stop gate。

第四层是 capsule 层。`tools/moira_runtime.py` 从 `tasks.json`、`runtime/iteration_state.json`、`runtime/absorption_strategy.json`、`runtime/knowledge_graph.json` 和协议文件生成当前 runtime capsule。capsule 会报告任务状态、Worker 状态、最低覆盖维度、协议 verdict、stop policy 和下一步动作。

第五层是 provider adapter。`tools/agent_launcher.py` 把 Worker 或 Auditor prompt 交给 opencode 或 Devin。当前默认仍是 opencode；未来设置 `MOIRA_AGENT_PROVIDER=devin` 或传 `--provider devin` 即可切换。

## PathListGate

Devin Master 不能直接派 Worker 处理一本书的正文。每一本书在处理前，必须先建立全 path 列表，并通过审计。

全 path 列表至少包含源文件、卷、篇、章、节、子节、规则、行号范围、稳定 path ID、原文定位和内容 hash 或等价可复核定位。对当前《星平会海》，已有入口是 `dev-docs/原典/星平会海/schema.json`、`dev-docs/原典/星平会海/full_path_tree.json` 和 `build_path_tree.py`。对其他书，也应该在对应目录建立 `full_path_tree.json` 和 path audit report。

PathListGate 没过时，Worker 只能执行 path list 构建或 path list 审计，不能进入正文处理。Worker 处理正文时只能处理 Master 分配的 path ID 和行号范围。Auditor 必须把 path 覆盖作为语义审计的一部分。

## Devin 支撑方式

Devin CLI 的项目级配置落在 `.devin/config.json`，hooks 落在 `.devin/hooks.v1.json`，项目级 skills 落在 `.devin/skills/<name>/SKILL.md`。本轮按这个结构新增了四个 skills。

`moira-runtime` 用于读取 capsule 和协议审计。

`moira-worker` 用于执行一个有边界的经验包，并要求输出维度、成熟度和可计算性。

`moira-auditor` 用于审计 Worker 输出，把执行完成和语义 PASS 分开。

`moira-orchestrator` 用于 Master 视角调度 Worker、Auditor 和 stop gate。

Worker 启动方式现在兼容两种 provider。

```bash
# 保持当前 opencode 行为
./worker.sh --worker-id W1 --task-id 20.4

# 使用 Devin CLI
./worker.sh --provider devin --worker-id W1 --task-id 20.4

# 或全局切换
MOIRA_AGENT_PROVIDER=devin ./worker.sh --worker-id W1 --task-id 20.4
```

Auditor 也同理。

```bash
python3 master.py launch-auditor --provider devin --worker-id W1 --task-id 20.4 --section-id 卷一/星曜躔度歌
```

## Stop gate

Devin 的 `Stop` hook 会调用 capsule。如果 `tasks.json` 仍有 queued、leased 或 busy Worker，或者协议锚点漂移，hook 会阻止停止。

这不是为了让系统永远运行，而是为了防止 AI 把“当前终端安静了”误判成“系统完成了”。MOIRA 的完成必须同时满足任务账本、Worker 状态、协议锚点和项目级研究门。

## Stop gate 根因分析（2026-08-03 补录）

> 触发事件：2026-08-03，Master session 因 tasks.json 中 179 个 queued 古籍研究任务持续触发 stop gate 死循环，无法停下来等待用户决策。已临时移除 `.devin/hooks.v1.json` 中的 Stop hook（备份在 `.devin/hooks.v1.json.bak`）。

### 核心问题：stop hook 到底是给谁用的

stop hook 的设计初衷是给 **Worker** 用的——防止 Worker 在分配给它的任务没干完时就停。但实际被装在了项目级 `.devin/hooks.v1.json`，对 **Master session 也生效**。Master 是和用户对话的角色，它本来就应该在用户没给新指令时停下来等，结果被 stop gate 拦住，形成死循环。

### 证据链

1. **dev-docs/46 第 45 行（设计意图）**：`moira-orchestrator` 用于 Master 视角调度 Worker、Auditor 和 stop gate。stop gate 是 Master **使用的工具**，不是用来管 Master 自己的。

2. **`tools/moira_runtime.py` 第 291 行（hook 命令行参数）**：脚本支持 `--role master/worker/auditor`，本身能区分角色。

3. **`.devin/hooks.v1.json`（原配置）**：`python3 tools/moira_runtime.py hook Stop` 没传 `--role`，默认走 `master`，且项目级配置对 Master 和 Worker session 都生效。

4. **`derive_stop_policy()` 第 148-152 行（核心逻辑）**：看的是全局 tasks.json 的 queued/leased/busy 数量，不分 role。无论谁调进来，只要全局有 queued 就 block。

### 两个层面的缺陷

**缺陷一：角色错配。** stop hook 应该只对 Worker session 生效，对 Master session 应该直接放行。Master 的停止时机由用户对话节奏决定，不由任务账本决定。

**缺陷二：作用域错配。** 即使对 Worker，`derive_stop_policy()` 看的是全局 tasks.json 的 queued 数量，不是"分配给当前 Worker 的任务"是否完成。Worker 干完自己的 1 个任务想停，也会被全局的 179 个 queued 拦住。

### 修复方向

1. **Stop hook 只对 Worker session 生效**：Worker 启动时通过环境变量或 `--role worker` 参数区分；Master session 不装 stop hook，或 stop hook 对 master role 直接返回 `STOP_ALLOWED`。
2. **`derive_stop_policy()` 对 worker role 只看分配给该 Worker 的任务**是否完成，不看全局 queued。
3. **Master 的完成判定走另一条路径**：由用户在对话中显式确认，或由 `moira-orchestrator` skill 引导 Master 主动检查任务账本后给出建议，而不是用 hook 强制拦截。

### 当前临时措施

已移除 `.devin/hooks.v1.json` 中的 Stop hook，保留 SessionStart 和 UserPromptSubmit 两个 hook（备份在 `.devin/hooks.v1.json.bak`）。在上述修复落地前，不要把 Stop hook 加回来。

## 本轮边界

本轮没有改动 `tasks.json`，也没有迁移现有 runtime 状态。当前运行态仍属于已经存在的 opencode 工作面。

本轮完成的是支撑层：未来可以让 Devin CLI 接管新的 Worker 或 Auditor；也可以先让 Devin 作为 Master 读取 capsule、审计协议并逐步修正现有运行时。

下一步如果继续深化，应把 `master_controller.py` 和 `factory.py` 的非线性调度结果写入更严格的 event ledger，并让 Worker completion 必须经过 Auditor barrier 才能把 task 标为 completed。
