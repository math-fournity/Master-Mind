# RepoInfo.md — 本repo基本信息与硬约束详细说明

> **来源**：从 AGENTS.md "本 repo 基本信息"节外移（2026-08-19瘦身工程二期，392号方案）。
> **定位**：repo的详细基本信息+硬约束1-6的完整解释+任务追踪系统。AGENTS.md中只保留铁律一行摘要，详细解释在本文件。
> **加载时机**：当你要了解repo的详细配置（Python环境/数据库连接细节/Git规则细节/Solver隔离原因/Solver启动方式细节/已归档系统详情/任务追踪文档清单）时，用read工具加载本文件。日常工作中AGENTS.md的铁律摘要足够。

---

## 本 repo 基本信息

- **路径**：`~/master-mind-glm5.2-worktree/`
- **工作分支**：`glm5.2`
- **origin**：`/data/master-mind`（fetch/push 都指向它）
- **Python 环境**：独立 venv（`.venv/`，python3.14 + python-arango 8.3.3，被 gitignore）
- **数据库**：ArangoDB `localhost:8529`，本 repo 专用数据库名 `xishujuzhen_math_glm52`（通过 `.env` 文件设置 `ARANGO_DB` 环境变量）

---

## 硬约束 1 · 数据库连接

**本 repo 专用数据库名**：`xishujuzhen_math_glm52`（通过 `.env` 文件覆盖 `ARANGO_DB` 环境变量）。

**硬规则**：
1. **启动任何会连 ArangoDB 的脚本/服务前**，必须确认 `ARANGO_DB` 环境变量已设为 `xishujuzhen_math_glm52`。
2. **每次运行前必须确认 `echo $ARANGO_DB` 输出 `xishujuzhen_math_glm52`**。若忘了 source `.env`，脚本会 fallback 到默认值 `xishujuzhen_math`，那是错误的数据库。
3. **运行 POC、研究 runtime、事件存储、启发规则存储**等所有会写库的代码前，先核对环境变量。

**题目录入信息抓手**：`problem_entries`集合——每道题入题一条记录，是查找该题目所有录入信息的抓手。从这条记录可以找到工作目录、会话ID、4个AI实例ID、产出路径、程序验证报告路径、合并trace路径。查找方法：`db.find_problem_entries_by_problem_id(problem_id)`。`system/`及本repo原有业务代码的数据库操作统一通过`system/db.py`模块，不直接操作ArangoDB客户端。

**Seven System例外（独立repo边界）**：`seven-system/`不得`import system.*`，其数据库访问只能通过Seven自身的`seven_system.database.StrictDatabasePort`；只有该端口唯一的Arango backend可以封装`ArangoClient`，其余Seven代码同样禁止直接使用raw client。Seven复用同一Arango服务与逻辑数据库`xishujuzhen_math_glm52`，但不得复用现有业务集合；未来仅允许隔离且显式版本化的`seven_*_vN`命名空间，`N`必须是正整数，禁止无版本Seven集合和非`seven_`前缀集合。这个架构许可不构成当前写授权：真实Schema初始化仍须通过精确数据库身份、只读catalog核验、显式计划哈希、人工确认、受控DDL入口和执行收据。Arango物理字节已经经OrbStack image由D盘承载，但未使用专用host bind；两者都不得被误写成逻辑site capability已PASS或Schema写入已授权。

---

## 硬约束 2 · Git 规则

1. **只在 `glm5.2` 分支上工作**。不要 commit 到本地 `main`。
2. **显式路径 add**：禁止 `git add -A`/`git add .`/`git add -u`，只 add 具体路径。
3. **改前清干净 + 改后立即 commit**：遵守全局 Git 管理协议。
4. **push 需用户明确授权**。

---

## 硬约束 3 · Solver 工作目录隔离

**数学大师 Solver 的 devin cli 实例必须在外部目录运行，不能在本 repo 内运行。**

原因：本 repo 的 AGENTS.md 包含工作系统规则（CP1-CP3、认知种子、七步骤pipeline等），如果 Solver 在本 repo 内运行 devin cli，这些规则会劫持 Solver 的行为——Solver 不做数学，而是去加载认知种子。这在 run_20260806_guided_001/002 中已验证发生。

**当前模式 · tmux-agents-dir（2026-08-07起）**：每个实验在 `/data/math-agent-glm5.2-tmux-agents-dir/` 下有独立的工作目录，运行后保留全部记录。目录命名规范：`<dev-docs编号>-<实验名>`。AGENTS.md模板：`templates/solver_agents_md.md`（bare）和`templates/solver_agents_md_guided.md`（guided）。

**旧模式 · 三固定目录（legacy，已废弃）**：`/data/math-agent-glm5.2-{1,2,3}`，目录在run之间被清理复用，运行记录不保留。

**Solver角色定义**：直接做数学，不走工作系统流程。可以搜索通用数学知识（定理/定义/公式），但禁止搜索题目答案/解答。允许exec（Python/SymPy计算验证）、read/write/edit、web_search。不知道就说"我不知道"，系统通过提示引导。**启动必须加`--permission-mode dangerous`**——否则exec被rejected，AI只做2步就停。

**Solver监控操作手册**：`.devin/skills/solver-monitoring/SKILL.md`（启动/观察/已知问题处理/判断是否做出来了）。

**元组：solver-batch-health-check**（批量集群健康检查）

> **触发条件**：用户说"检查进度"/"看看有没有问题"/"检查链接问题"时；批量Solver集群运行时；新session接手批量系统时。
> **Rule**：`.devin/rules/solver-batch-health-check.md`——三条铁律（用batch_status.py不现写脚本/DB数字会骗人必须到最前线/发现问题先修检查工具再修监控逻辑）+ 并发上限经验（管道化系统实测：60并发最优，100并发触发限流）+ 已知问题清单（10个已修复问题，含2026-08-13的collector误杀/中文proof/rate_limited检测3个修复）。
> **Skill**：`.devin/skills/solver-batch-health-check/SKILL.md`——7项检查清单（批次活着/running数合理/活跃度/僵尸session/错误分类/feed/泄漏）+ 手动清理僵尸session脚本 + 并发调整命令。
> **并发约束Rule**：`.devin/rules/solver-concurrency.md`——3秒启动间隔铁律（runner.py第333行不可改）+ 并发经验表（40/50/60/80/100实测数据）+ Redis实时调整命令。
> **检查工具**：`xishujuzhen/solver_harness/batch_status.py`（8个命令：status/active/errors/solved/feed/leak/dead/all，dead支持--cleanup自动清理僵尸session）。

---

## 硬约束 4 · Solver启动方式（2026-08-18更新）

**生产实验运行解题AI，用全局 `noninteractive-solver-run` skill**（`devin -p --prompt-file ... --export ...`）。conversation.json的`reasoning_content`包含完整thinking，不需要mitmproxy，不需要solver-harness。

**调试solver-harness本身时，用 `solver-tmux-launch` skill**（项目级，仅调试用）。通过solver-harness启动，用tmux实时观察devin cli行为，加`--no-mitm`。

**mitmproxy已废弃**（2026-08-18）：不再用于生产trajectory采集。`--export`的conversation.json已包含`reasoning_content`（完整thinking），不需要MITM截获。mitmproxy在多AI并发时造成端口冲突，已正式废弃。

**批量解题用pipe系统**（`xishujuzhen/solver_harness/pipe/`），不走solver-harness的`launch`命令。

**具体规范见**：
- 生产实验：全局 `~/.config/devin/skills/noninteractive-solver-run/SKILL.md` + 全局AGENTS.md中的对应元组
- 调试harness：`.devin/rules/solver-tmux-launch.md` 和 `.devin/skills/solver-tmux-launch/SKILL.md`

---

## 硬约束 5 · Solver批次系统架构认知（已归档）

> **第一代批量系统（batch_problem_runner.py）已被管道化系统（pipe/5服务）完全替代，当前不再运行。**
>
> **完整架构说明已移到**：`dev-docs/旧模式batch_problem_runner系统说明.md`——运行模式/命令/TUI直出/`-p`vs交互模式/答案泄漏防护/选题feed/限流/并发上限/DB schema/批次状态查询脚本。
> **操作SOP已移到**：`dev-docs/旧模式batch_problem_runner操作SOP.md`——16个SOP（启动/检查健康/验证STALLED/处理dead/落盘/看thinking/扫描状态/恢复export/停止/手动feed+resume）。
>
> **何时需要读**：管理仍在运行的旧模式实例时（当前无）；需要了解`-p`模式vs交互模式的历史演变时。
>
> **跨系统共享信息**（DB schema表/数据完整性表/看Solver方法）已迁移到下方管道化系统节中。

---

## 硬约束 6 · 自动化运营系统（已归档）

> **第二代批量系统（auto_runner.py + enqueue_problem.py）是batch_problem_runner到管道化系统之间的过渡方案，已被管道化系统（pipe/5服务）完全替代，当前不再运行。**
>
> **完整架构说明已移到**：`dev-docs/旧模式auto_runner系统说明.md`——架构/三个组件/送题命令/启动runtime/监控命令/problem_queue字段/固定目录/AI工作循环/与旧模式的区别。
>
> **何时需要读**：需要了解auto_runner的problem_queue表结构时；需要了解从batch_problem_runner到管道化系统的演进过程时。

---

## 任务追踪（跨Session工作意识维持）

**任务追踪文档目录**：`任务追踪/`——每个工作线一个独立文件，顺序编号化，自包含，互不干扰。

**`任务追踪/README.md`** — 导航枢纽，记录各任务追踪文档之间的依赖关系DAG。

**当前活跃的任务追踪文档**：

| 文件 | 工作线 | 焦点 |
|---|---|---|
| `任务追踪/01-253号检索机制验证.md` | 253号检索机制验证 | P0+P1原型验证完成，泛化验证通过 |
| `任务追踪/02-trajectory采集与solver-harness.md` | Trajectory采集基础设施 | solver-harness方案v1完成 |
| `任务追踪/03-虚拟数学系统VMS-POC验证.md` | 虚拟数学系统POC验证 | POC-VMS-0到VMS-10全部完成 |
| `任务追踪/04-端到端效果验证-接真实Solver.md` | 端到端效果验证 | ✅A/B实验完成，已演进到Grove核心循环 |
| `任务追踪/05-题目侧写Profiling系统.md` | 题目侧写Profiling系统 | 设计完成 |

**任务追踪文档编写要求**：自包含、Checklist化、结构统一（§0当前焦点/§1已完成/§2待办/§3关键决策/§4 Git Commit历史/§5跨Session读取指南）、不删除历史、新建时更新README.md、记录git commit ID和全部产出资产path。详见`任务追踪/README.md`。
