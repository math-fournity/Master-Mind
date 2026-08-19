# 项目 AGENTS.md · 数学大师制造

> **未来 AI 进入本 repo 时，必须先读完本文件顶部的硬约束再做事。**

---

## Grove核心循环与辅助智能体认知（跨AI共享 · 最高认知优先级）

> **本repo与Grove repo（`/data/master-mind-glm5.2-grove/`）共享同一套核心循环认知。**
> **完整版**：`dev-docs/273-v0-2026-08-08-Grove核心循环与辅助智能体JD-跨AI认知同步.md`——辅助智能体JD展开、7个场景SOP、角色切换细节、反模式/正确模式展开都在273号文档中。本节是精炼版，保留核心认知。

### Grove核心循环

**本 repo 的一切工作都围绕这个循环展开。理解这个循环 = 理解系统是什么。**

```
引导树（给方向Q）→ 推理AI（探索）→ 解题树（记录结果）
                                    ↓
                              在终点节点检索
                                    ↓
                              引导树（新边=新方向Q）→ 启动新推理AI → ...
```

**两棵树是同一棵树的两个面**：
- **引导展开树（Guided Expansion Tree）** = "应该往哪走"的视图。每个节点是一个数学处境，每条边是一个提示Q。活的、正在生长的。
- **解题记录树（Solution Record Tree）** = "实际走了什么"的视图。引导展开树展开完成后凝固的树。包含成功路径、失败路径、分叉点、中间处境。

**循环的三个推动关系**：
1. **引导树 → 推理AI**：引导树上已有节点和边（提示Q），系统从中构造脉络（从根到当前节点的路径+方向Q），给推理AI作为输入，推动它往特定方向探索
2. **推理AI → 解题树**：推理AI的thinking/trajectory被系统采集，提取出节点（数学处境），写入解题记录树——记录"实际探索了什么"
3. **推理AI → 引导树**：推理AI的输出到达某个节点后，系统在这个节点上检索数据基座，识别出新方向Q，这些新方向成为引导树的新边——引导树继续生成

**关键约束**：
- 推理AI不需要停下接受提示——"让推理AI停下"这个需求消失了
- 系统与推理AI并行运行——AI在thinking的同时，系统就从thinking中增量提取节点写入树，两棵树在AI运行过程中实时生长
- 系统的目的不是"让AI做出来"，而是"让两棵树生长出来，在过程中与正确解答的脉络相遇"
- 停机条件：与正确解答的脉络相遇时停机，不需要所有分支都探索完

**循环没转起来的判定**：如果只有解题树在长（采集到了节点），但引导树没有生成新边（没有检索出方向Q、没有启动新AI），循环只转了半圈。完整的循环必须三个推动关系都成立。

### 引导树闭环的识别端结构（000号文档）

**引导树闭环中"识别→给方向"的操作是一个二元组：tell + hint。** tell是识别端（从推理AI的thinking中读出的分叉信号），hint是注入端（给新AI的翻译方向）。hint端已在POC-VMS-8中验证（281/282/283号），tell端已在POC-VMS-9/10中验证（288/289号）。

**000号文档位置**：`000-v0-2026-08-08-引导树闭环-识别端结构定义.md`（项目根目录）

**二元组**：**读tell，给hint。** tell取自poker术语——推理AI不会主动告诉你"我没考虑这个方向"，但它的thinking会暴露它走了哪条路、没走哪条路。系统从thinking中读出这些信息就是tell。

**核心认知（v2修正，来自285号）**：系统识别的不是"AI在哪里卡住了"，而是"AI的thinking中哪些位置可以分叉但AI没分叉"。往往不是AI卡住了需要提示，而是AI走错路了——系统在AI没走的分叉上开新边，启动新AI走新分支。分叉位置有两种：line上分叉（Point Branch）和根节点分叉（Root Branch）——有时AI从第一步就选错方向，最关键的分叉在根节点。

**tell的四个组成成分**：分叉信号（Branch Signal）、分叉类型（Branch Type）、未探索诊断（Unexplored Diagnosis）、方向匹配（Direction Matching）。

**tell端验证状态（POC-VMS-9/10已完成）**：tell可去特化（Level 0→Level 1拓扑结构）、形式化过滤（Pipe 1）可命中、小概念标记分辨（Pipe 2）可区分拓扑相同且距离极近的tell。详见287/288/289号。

### AI的双重角色与系统就是脚本

进入实验时，AI的角色是双重的：**系统开发者**（Master Agent，写代码/审计/测试/commit）和**系统检查者**（系统运行时检查健康状态，运行后审计产出质量）。

**系统就是脚本（第六代核心认知转变）**：辅助Pipe的工作由代码自动执行，Master Agent不亲手执行循环。系统运行时你是检查者——检查tmux session/产出/循环完整性/alerts，不干等。发现问题切回开发者修复代码。**切换触发条件="有没有推理AI在跑"**。

**辅助智能体JD要点**：检查系统健康、检查循环完整性、审计产出质量、处理异常、检查停机条件。关键约束：你在检查，不在执行。**7个场景SOP的完整细节见273号文档。**

### 演进路径

- **阶段1-7（✅全部完成）**：A/B对照→脉络注入→并发展开→自我增殖→hint端验证（bare 0%→tree 67%）→tell端验证→第五代技术说明书编写
- **阶段8（当前）**：第六代系统研发——非局部tell、FCA数学基础、并发Telling AI、Pipe 0简化+Pipe 2并行化

> **⚠️ FCA再分析启动铁律**（本提示在always-on可见区，确保你不会忘记）：
> 做FCA再分析时采用主agent/subagent分工——你是流程管理者，不自己做分析。从`FCA学习笔记/fca-reanalysis-checklist.md`复制checklist到todo_write，从`fca-reanalysis-subagent-prompt-template.md`复制prompt模板用run_subagent启动，subagent返回后用`fca-reanalysis-output-verification-checklist.md`验证。如果subagent发现分类学问题，你自己执行修正流程（7条铁律）。完整SOP详见`.devin/rules/tell-taxonomy-iteration-audit.md`。完整Schema在下方"Tell分类学Schema"节。

### 第六代系统文档与代码存放规则（阶段8生效）

**两个文档目录**（必须严格区分）：
- `第六代系统研发过程文档/`——探索性/讨论性/评审性，三位编号（303号起），不确定的内容放这里
- `第六代系统技术说明书/`——规范性/工程性/自包含，章节编号（01-09），只有确认值得最终记录的内容才放这里
- `dev-docs/`保留给第五代及之前（000-291号），不再新增第六代文档

**代码目录**：`system/`——第六代系统的物理实现代码，自包含（代码层`*.py`+`.ref`+`.ai-check` / 文档层`docs/` / 运行时层`assets/`）。两个入口：`enter.py`（入题）、`solve.py`（解题）。**完整规则详见`system/README.md`和`SixthGenRnD.md`。**

**ref和docs**：ref=`system/`中`.ref`文件（指向system外部文档的指针），docs=`system/docs/`（system内部完整认知文档，含系统级/跨模块级/模块级三层）。改代码时先改`.py`→检查`.ref`→同步`docs/`。详见`.devin/rules/system-ref-sync.md`。

**第六代研发过程文档清单**（303-311号，截至2026-08-10，均在`第六代系统研发过程文档/`）：303引导树分叉/304 FCA对应/305非局部tell实例/306上下文分析目标/307原语化(310号评审拒绝)/308 vms_test_1 thinking/309范式转变(310号评审:命名有价值,原主张跑偏)/310 worktree评审/311并发Telling AI。

### Seven System · 非特化证据工厂运行入口（2026-08-13起）

**系统目录**：`seven-system/`。**唯一详细操作手册**：`seven-system/docs/operations.md`——启动/preflight/dry-run/状态/故障处理都以该文件为准，不复制到AGENTS.md。

**系统定位**：独立的非特化证据工厂，不是题海Profile系统，也不是第六代`system/`的第三个入口。Seven只读提供冻结bare失败候选；不得写生产`math:*`队列；未来只通过版本化带哈希的冻结bundle接入第六代`system/`。目标职责：有限Epoch、资源公平、盲化三审、contrast EvidenceRecord、人工Gate。**当前实现尚未进入三审或科学实验阶段。**

**硬约束**：
1. Solver生产实验用全局`noninteractive-solver-run` skill；调试harness用`solver-tmux-launch` skill；批量解题用pipe系统
2. Solver必须无工具；Prompt写"不要用工具"≠能力PASS，缺独立NoTool能力报告时live运行必须BLOCK
3. 只有目标Solver作业可进入`solver_harness`；认知角色经provider-neutral `ModelRolePort`，Devin认知worker不得复用Solver port/workspace/session/AGENTS/capability/receipt
4. Devin认知角色首选`glm-5-2`，Codex的`gpt-5.6-sol`为并列候选；盲化AuthoringBakeoff只选角色默认profile
5. DB访问须先确认`ARANGO_DB=xishujuzhen_math_glm52`，禁止默认库和直接raw client
6. Evidence/Artifact/WorkEvent append-only，禁止覆盖、删除负证据、retry until solved
7. 自动化不得跨人工Gate、自动切active release或把PARTIAL升级为PASS
8. 完整实现按`seven-system/docs/implementation/README.md`双依赖推进；实施AI不得把候选系统自签为正式PASS

**当前真实实现上限**：v0.1.0实现P0只读preflight+P1 scaffold dry-run+WP-1离线Strict DB契约报告。未连接真实DB，未创建`seven_*_vN`集合。`TargetSolverPort`/`ModelRolePort`/Devin/Codex adapter/QuestionRelease/AuthoringBakeoff均未实现。以`seven-system/docs/implementation-status.md`为准。

**最新工程决策记录**：`Tell分类学研究过程文档/389号` §14-17。完整文档入口：`seven-system/docs/implementation/README.md`；独立审计者入口：`seven-system/docs/audit/README.md`。

---

## 角色说明 · 你当前是什么 AI

本 AGENTS.md 可能被多种 AI 加载，进入本 repo 时请先确认自己的角色：

| 角色 | 工作目录 | 职责 | 看到本 AGENTS.md 时该做什么 |
|---|---|---|---|
| **Master Agent** | `~/master-mind-glm5.2-worktree/` | 实现、审计、迭代数学大师系统 | 遵守本 AGENTS.md 全部约束，执行工作 |
| **Subagent** | 由 Master 通过 Devin CLI/tmux 启动 | 执行被分配的子任务 | 只执行分配的任务，不承担 Master 的全部责任；若不确定就问 Master |

**如果你是 subagent**：你看到的是 Master 的 AGENTS.md，但你不等于 Master，不需要承担 Master 的长期工作系统迭代责任。你的任务是完成 Master 交给你的具体任务，任务完成后汇报。

---

## 本 repo 基本信息

- **路径**：`~/master-mind-glm5.2-worktree/`
- **工作分支**：`glm5.2`
- **origin**：`/data/master-mind`（fetch/push 都指向它）
- **Python 环境**：独立 venv（`.venv/`，python3.14 + python-arango 8.3.3，被 gitignore）
- **数据库**：ArangoDB `localhost:8529`，本 repo 专用数据库名 `xishujuzhen_math_glm52`（通过 `.env` 文件设置 `ARANGO_DB` 环境变量）

### 硬约束 1 · 数据库连接

**本 repo 专用数据库名**：`xishujuzhen_math_glm52`（通过 `.env` 文件覆盖 `ARANGO_DB` 环境变量）。

**硬规则**：
1. **启动任何会连 ArangoDB 的脚本/服务前**，必须确认 `ARANGO_DB` 环境变量已设为 `xishujuzhen_math_glm52`。
2. **每次运行前必须确认 `echo $ARANGO_DB` 输出 `xishujuzhen_math_glm52`**。若忘了 source `.env`，脚本会 fallback 到默认值 `xishujuzhen_math`，那是错误的数据库。
3. **运行 POC、研究 runtime、事件存储、启发规则存储**等所有会写库的代码前，先核对环境变量。

**题目录入信息抓手**：`problem_entries`集合——每道题入题一条记录，是查找该题目所有录入信息的抓手。从这条记录可以找到工作目录、会话ID、4个AI实例ID、产出路径、程序验证报告路径、合并trace路径。查找方法：`db.find_problem_entries_by_problem_id(problem_id)`。`system/`及本repo原有业务代码的数据库操作统一通过`system/db.py`模块，不直接操作ArangoDB客户端。

**Seven System例外（独立repo边界）**：`seven-system/`不得`import system.*`，其数据库访问只能通过Seven自身的`seven_system.database.StrictDatabasePort`；只有该端口唯一的Arango backend可以封装`ArangoClient`，其余Seven代码同样禁止直接使用raw client。Seven复用同一Arango服务与逻辑数据库`xishujuzhen_math_glm52`，但不得复用现有业务集合；未来仅允许隔离且显式版本化的`seven_*_vN`命名空间，`N`必须是正整数，禁止无版本Seven集合和非`seven_`前缀集合。这个架构许可不构成当前写授权：真实Schema初始化仍须通过精确数据库身份、只读catalog核验、显式计划哈希、人工确认、受控DDL入口和执行收据。Arango物理字节已经经OrbStack image由D盘承载，但未使用专用host bind；两者都不得被误写成逻辑site capability已PASS或Schema写入已授权。

### 硬约束 2 · Git 规则

1. **只在 `glm5.2` 分支上工作**。不要 commit 到本地 `main`。
2. **显式路径 add**：禁止 `git add -A`/`git add .`/`git add -u`，只 add 具体路径。
3. **改前清干净 + 改后立即 commit**：遵守全局 Git 管理协议。
4. **push 需用户明确授权**。

### 硬约束 3 · Solver 工作目录隔离

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

### 硬约束 4 · Solver启动方式（2026-08-18更新）

**生产实验运行解题AI，用全局 `noninteractive-solver-run` skill**（`devin -p --prompt-file ... --export ...`）。conversation.json的`reasoning_content`包含完整thinking，不需要mitmproxy，不需要solver-harness。

**调试solver-harness本身时，用 `solver-tmux-launch` skill**（项目级，仅调试用）。通过solver-harness启动，用tmux实时观察devin cli行为，加`--no-mitm`。

**mitmproxy已废弃**（2026-08-18）：不再用于生产trajectory采集。`--export`的conversation.json已包含`reasoning_content`（完整thinking），不需要MITM截获。mitmproxy在多AI并发时造成端口冲突，已正式废弃。

**批量解题用pipe系统**（`xishujuzhen/solver_harness/pipe/`），不走solver-harness的`launch`命令。

**具体规范见**：
- 生产实验：全局 `~/.config/devin/skills/noninteractive-solver-run/SKILL.md` + 全局AGENTS.md中的对应元组
- 调试harness：`.devin/rules/solver-tmux-launch.md` 和 `.devin/skills/solver-tmux-launch/SKILL.md`

### 硬约束 5 · Solver批次系统架构认知（已归档）

> **第一代批量系统（batch_problem_runner.py）已被管道化系统（pipe/5服务）完全替代，当前不再运行。**
>
> **完整架构说明已移到**：`dev-docs/旧模式batch_problem_runner系统说明.md`——运行模式/命令/TUI直出/`-p`vs交互模式/答案泄漏防护/选题feed/限流/并发上限/DB schema/批次状态查询脚本。
> **操作SOP已移到**：`dev-docs/旧模式batch_problem_runner操作SOP.md`——16个SOP（启动/检查健康/验证STALLED/处理dead/落盘/看thinking/扫描状态/恢复export/停止/手动feed+resume）。
>
> **何时需要读**：管理仍在运行的旧模式实例时（当前无）；需要了解`-p`模式vs交互模式的历史演变时。
>
> **跨系统共享信息**（DB schema表/数据完整性表/看Solver方法）已迁移到下方管道化系统节中。

---

### 硬约束 6 · 自动化运营系统（已归档）

> **第二代批量系统（auto_runner.py + enqueue_problem.py）是batch_problem_runner到管道化系统之间的过渡方案，已被管道化系统（pipe/5服务）完全替代，当前不再运行。**
>
> **完整架构说明已移到**：`dev-docs/旧模式auto_runner系统说明.md`——架构/三个组件/送题命令/启动runtime/监控命令/problem_queue字段/固定目录/AI工作循环/与旧模式的区别。
>
> **何时需要读**：需要了解auto_runner的problem_queue表结构时；需要了解从batch_problem_runner到管道化系统的演进过程时。

---

### 通用SOP（适用于管道化系统）

> **以下SOP是通用规范，适用于当前管道化系统（pipe/5服务）。旧系统（batch_problem_runner/auto_runner）的SOP已归档到dev-docs/。**

**SOP G1 · 编译验证（改代码后必须做）**

```bash
cd ~/master-mind-glm5.2-worktree
.venv/bin/python -m py_compile xishujuzhen/solver_harness/pipe/feeder.py && \
.venv/bin/python -m py_compile xishujuzhen/solver_harness/pipe/runner.py && \
.venv/bin/python -m py_compile xishujuzhen/solver_harness/pipe/collector.py && \
.venv/bin/python -m py_compile xishujuzhen/solver_harness/pipe/reporter.py && \
.venv/bin/python -m py_compile xishujuzhen/solver_harness/pipe/retry_infrastructure.py && \
.venv/bin/python -m py_compile xishujuzhen/solver_harness/pipe/pipe_control.py && \
.venv/bin/python -m py_compile xishujuzhen/solver_harness/solver_harness.py && \
echo "compile OK"
```

**SOP G2 · 资产追溯规范（2026-08-12）**

> **所有运行资产必须可追溯**——从DB记录能找到文件路径，从文件路径能找到DB记录。不允许放临时目录。

**运行ID唯一性保证**：

exp_id格式：`{batch_id}-{ordinal:02d}-p{progress_key}-r{run_id:07d}-{problem_id}`

- `run_id`是ArangoDB counter（`devin_counters` collection的`run_id`键）原子自增的全局运行ID
- 每次`create_batch`/`add_cases`/`create_attempt_from_queue`创建attempt时调`next_run_id(db)`获取，确保exp_id全局唯一
- 同一道题在不同batch中跑→run_id不同→exp_id不同✓
- 同batch内重跑→run_id不同→exp_id不同✓
- 两个runner并发→ArangoDB事务保证原子递增→run_id不冲突✓
- DB attempt记录中有`run_id`字段，便于从run_id反查attempt
- **目录名以exp_id开头，exp_id含run_id，所以目录永远唯一，不会错乱**

**资产存放位置**：

| 资产 | 位置 | 持久化 | 追溯方式 |
|---|---|---|---|
| **trajectory文件**（export/pipe/thinking_capture/tmux.log） | `/data/math-agent-glm5.2-tmux-agents-trajectory/<exp_id>/` | 是 | DB attempt.paths指向 |
| **solver工作目录**（problem.txt/proof.md/AGENTS.md） | `/data/math-agent-glm5.2-tmux-agents-dir/<exp_id>/` | 是 | DB attempt.paths指向 |
| **monitor日志** | `/data/math-agent-glm5.2-tmux-agents-dir/logs/batch-<label>.log` | 是 | tmux session名对应 |
| **auto_runner日志** | `/data/math-agent-glm5.2-tmux-agents-dir/logs/auto_runner.log` | 是 | 固定路径 |
| **DB记录**（attempt/event/batch/queue） | ArangoDB | 是 | batch_id → attempt → paths |
| **sessions.db** | `~/.local/share/devin/cli/sessions.db` | 是 | devin_session_id关联 |

**trajectory数据Schema文档**（项目根目录）：

| 文件 | 内容 | 何时读取 |
|---|---|---|
| `devin-cli-export-conversation.md` | `exports/conversation.json`的完整Schema（ATIF格式，含reasoning_content/tool_calls/observation） | 需要解析--export导出的conversation.json时 |
| `trajectory-schema.md` | `sessions_db/trajectory.jsonl`的完整Schema（JSONL格式，含thinking/tool_calls/tool行） | 需要解析sessions_db导出的trajectory.jsonl时 |
| `analysis-devin-failure-system/docs/solver-trajectory-schema.md` | harness采集的完整trajectory目录结构（9个文件，含session_info/mitm/tmux） | 需要了解完整目录结构时 |

**关键差异**：conversation.json的`observation`字段存tool_results（58%存在率，优先用）；trajectory.jsonl的`role="tool"`行存tool_results（82%存在率，兜底用）。

**面包屑地图方案**（不假设schema的遍历→地图→HANDOVER.md）：见 `conversation-map.md`（项目根目录）。当conversation.json结构未知或可能变化时，用 `scripts/conversation_mapper.py` 生成面包屑地图，交给编写HANDOVER.md的AI按地图逐条遍历，不依赖先验schema。

**从DB查运行时目录和文件位置**：
```bash
# 从problem_id查所有attempt及其文件路径
.venv/bin/python -c "
from arango import ArangoClient; import os
c = ArangoClient(hosts=os.environ.get('ARANGO_HOST','http://localhost:8529'))
db = c.db(os.environ['ARANGO_DB'], username=os.environ.get('ARANGO_USER','root'), password=os.environ.get('ARANGO_PASS',''))
for a in db.aql.execute('FOR a IN devin_problem_runs FILTER a.problem_id == @pid RETURN a', bind_vars={'pid': '<PID>'}):
    print(f'run_id={a.get(\"run_id\",0)} status={a[\"status\"]} batch={a[\"batch_id\"]}')
    print(f'  exp_id={a[\"exp_id\"]}')
    print(f'  export: {a[\"paths\"][\"export_path\"]}')
    print(f'  thinking_capture: {a[\"paths\"][\"tmux_pipe_path\"].replace(\"tmux_pipe.log\",\"thinking_capture.txt\")}')
    print(f'  solver_dir: {a[\"paths\"][\"solver_dir\"]}')
"
```

**禁止**：
- **禁止放`/tmp/`**——重启丢失，无法追溯
- **禁止只存DB不存文件**——DB只有paths指针，文件丢了paths指向空
- **禁止只存文件不存DB**——没有DB记录无法从batch_id查到attempt

**SOP G3 · AI失败题分类与Response truncated处理（2026-08-12）**

> **AI做不出来的题分4类**，全部记录到DB的`devin_problem_runs`中，`status`+`end_reason`字段标识失败类型。完整追溯文档见374号文档。

**AI自身问题导致的失败**：

| status | 含义 | end_reason | 是AI的问题？ |
|---|---|---|---|
| `failed_no_proof` | session结束但没输出`### PROOF COMPLETE`标记 | `tmux_session_ended` | 是——AI做了题但没按格式输出标记 |
| `failed_token_limit` | token用完没做出来 | `tmux_session_ended` / `idle_token_limited` / `response_truncated_max_token_limit` | 是——AI能力不足/效率不够 |
| `failed_tool_stall` | 工具调用卡住超时 | `stall_seconds` | 是——AI行为异常 |
| `answer_leak` | AI检测到答案泄漏主动拒绝 | `answer_leak_detected_by_solver` | 是——AI主动拒绝 |

**基础设施问题导致的失败（不算AI做不出来）**：

| status | 含义 | 归因 |
|---|---|---|
| `dead_session` | devin cli已退出(DEVIN_CLI_EXITED)但无proof | 基础设施 |
| `failed_connection` | 网络连接断开 | 网络 |
| `failed_network_stuck` | 网络不稳定卡死 | 网络 |
| `launch_error` | 启动失败 | 系统 |
| `stopped` | 手动停止 | 操作 |

**Response truncated的处理**：

> **Response truncated不是网络问题**——是模型输出达到max token limit被截断。TUI显示`⚠︎ Response truncated`，session空闲等待用户发消息继续。这属于AI做不出来的情况——AI的输出长度不够完成证明。

**处理流程**：
1. `scan-thinking`扫描发现IDLE的session
2. 看pane内容——`Response truncated`是token limit，`Connection error`是网络断开
3. **Response truncated**：可以发"继续"让AI继续输出，但如果反复truncated说明题对AI来说太长→最终标记`failed_token_limit`
4. **Connection error**：网络问题，发"继续"重试，反复失败则标记`failed_connection`

**手动落盘PROOF COMPLETE的session**（auto_runner的refresh循环会自动做，但如果需要手动做）：
- 先`capture_thinking(attempt)`保留thinking数据
- 再`stop_attempt(db, attempt, batch_dir, decode=False)`让devin cli写export
- 等3秒后kill tmux session
- 更新DB：`status=candidate_solved`, `end_reason=manual_pane_proof_complete`
- 记录event：`event_type=attempt_solved`

**查询所有AI失败的题**：
```bash
.venv/bin/python -c "
from arango import ArangoClient; import os
from collections import Counter
c = ArangoClient(hosts=os.environ.get('ARANGO_HOST','http://localhost:8529'))
db = c.db(os.environ['ARANGO_DB'], username=os.environ.get('ARANGO_USER','root'), password=os.environ.get('ARANGO_PASS',''))
for s, n in sorted(Counter(a['status'] for a in db.aql.execute('FOR a IN devin_problem_runs FILTER a.status IN [\"failed_no_proof\",\"failed_token_limit\",\"failed_tool_stall\",\"answer_leak\"] RETURN a')).items()):
    print(f'  {s}: {n}')
"
```

---

### 旧模式SOP（batch_problem_runner直接操作 · 已归档）

> **以下SOP来自2026-08-12的调试实战，适用于batch_problem_runner.py直接操作模式。该系统已被管道化系统完全替代，当前不再运行。**
>
> **完整操作SOP已移到**：`dev-docs/旧模式batch_problem_runner操作SOP.md`——16个SOP（SOP 1启动批次/SOP 2检查批次健康/SOP 3验证STALLED/SOP 4处理dead session/SOP 5批量落盘/SOP 6看thinking内容/SOP 7停止批次/SOP 9扫描thinking状态/SOP 10恢复export=0B/SOP 13手动feed+resume）+ 数据完整性表 + 已知根因清单。
>
> **何时需要读**：管理仍在运行的旧模式实例时（当前无）。

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

---

## 题目侧写Profile提取工作（活文档 · 数据基座建设）

> **本节记录题目侧写（problem profile）提取工作的进度、方法和产出。这是系统数据基座的核心建设线。**
> **详细审计日志**：`subagents-dirs/review-log.md`（每批审计结果）
> **任务追踪文档**：`任务追踪/05-题目侧写Profiling系统.md`

### 工作方法

每道题通过subagent完成11步分析：读题目解答→QA序列分析→问题拓扑层→解答思维模式层→翻译方向层→tell拓扑层→提取(tell,hint)对→实验适用性层→输出profile JSON→入库ArangoDB→汇报。

Master Agent对每批3题做完整6-Phase审计：格式检查（situation_type/hint_level/per-pair拓扑/必填字段/QA序列结构）+数学内容审查（题目理解/解答理解/key_insight准确性/瓶颈标注合理性）+落盘audit-checklist.md。

### 数据库存储

- **ArangoDB集合**：`problem_profiles`（_key=problem_id，含完整profile JSON）
- **ArangoDB集合**：`problem_extraction_progress`（_key=数字ID，含global_sequence/extraction_status/metadata）
- **数据库**：`xishujuzhen_math_glm52`，localhost:8529

### 完成进度（截至2025-01-24）

| 层级 | 来源 | 完成数/总数 | 状态 |
|---|---|---|---|
| **Tier 1** | 高难度竞赛题（IMO/IMO SL/Putnam/China TST/FATE-X等） | **452/452** | ✅全部完成 |
| **Tier 2** | IMO Shortlist剩余+IMO剩余+Putnam剩余+IMO Longlists+China TST剩余+Balkan MO SL+China NOL+ToT+IMC+Yau+Alibaba | 3/606 | 进行中 |
| **Tier 3** | USAMO+FATE-H+HMMT系列+SMT+CMIMC+Iranian+Brazilian | 0/3127 | 待处理 |
| **Tier 4** | OlympiadBench+FATE-M+AIME 2024 | 0/860 | 待处理 |
| **Tier 5** | pascal+fermat+cayley+mathd | 0/942 | 待处理 |
| **Tier 6+** | olympiads+Hendrycks MATH+AoPS 2024等 | 0/62000+ | 暂不规划 |

**当前总进度**：455/67838（0.67%），但Tier 1高难度题已100%完成。

### Token统计

| 指标 | 数值 |
|---|---|
| profile总数 | 455 |
| 局部tell数量 | 3,192 |
| 全局tell数量 | 972 |
| tell总数 | 4,164 |
| tell字段总token | ~122K |
| 完整profile总token（含所有文本字段） | ~407K |
| 平均每profile token | ~893 |

### 质量记录

- **连续0个小问题批次**：129批（从第41批至今）
- **subagent静默失败处理**：少数题目subagent返回空结果，Master Agent手动创建profile（如omni_math_004296）
- **原解答问题处理**：部分题目原Lean解答有计算错误/不严谨/模糊/hand-wavy/事实错误，subagent在profile中重构或注明
- **空答案字段处理**：部分题目answer为空，subagent从解答中推导答案

### Tier 2后续优先级（难的先处理）

1. IMO Shortlist剩余96题（起始seq=1955）← 当前进行中
2. IMO剩余89题（起始seq=1403）
3. Putnam剩余88题（起始seq=1756）
4. IMO Longlists剩余39题（起始seq=1994）
5. China TST剩余80题（起始seq=1443）
6. Balkan MO SL剩余31题（起始seq=1862）
7. China NOL剩余35题（起始seq=1446）
8. ToT剩余54题（起始seq=1956）
9. IMC剩余67题（起始seq=1627）
10. Yau Contest剩余6题（起始seq=1630）
11. Alibaba Contest剩余21题（起始seq=1597）

### 关键文件

- `subagents-dirs/review-log.md`：完整审计日志（每批的seq范围/题目/审计结果/修复内容/数学审查结论）
- `subagents-dirs/<problem_id>/`：每题的工作目录（problem.lean/checklist.md/profile.json/audit-checklist.md）
- `subagents-dirs/audit-checklist-template.md`：审计checklist模板
- `subagents-dirs/checklist-template.md`：subagent工作checklist模板
- `scripts/prepare_subagent_dir.py`：subagent工作目录准备脚本
- `scripts/ingest_problem_extraction_progress.py`：progress记录入库脚本

---

## 认知资产索引（活文档）

认知资产索引（隔离实施状态、ArangoDB 初始化状态、认知图/依赖图/题库统计）在 `xishujuzhen/cognition_asset_index.md`，由工作系统持续维护。每次新增认知单元、新增 dev-docs、ArangoDB 状态变更后更新该文档。

---

## 系统设计原语目录（活文档）

系统设计原语分四层管理（244号重构 + 245号面相独立 + 257号全库原语找回）：
- **`primitives/`** — 原语（构造系统的积木，72个）：`operational/`（操作原语47个）+ `structural/`（结构原语25个）。验证状态四等级：tested 35 / partial 16 / untested 20 / tested_negative 1。
- **`concepts/`** — 概念框架（8个）：形式化边界、两种计算、闭环、处境等。
- **`criteria/`** — 性质标准与探索性隐喻（3个）。
- **`facets/`** — 面相（7个）：两种计算/语料双路径/Pipeline网络/树的生长 + 实践涌现/知识选取/设计过程自举。

详见 `dev-docs/257-v0-2026-08-07-全量原语目录更新方案-以253号检索问题为抓手的全库原语找回.md`。每次跑实验后更新相关原语的验证状态。

---

## 原语化AI数学工程系统设计（活文档 · 论文原语化版）

**`原语化AI数学工程系统设计/`** — 256号论文的原语化升级版（v5）。29个自包含的Markdown文件，通过前置阅读和关联原语链接形成阅读网络。README.md是导航枢纽。包含四代系统的完整设计文档。

---

## 系统技术说明书系列（活文档 · 系统演进主线）

数学大师系统经历了五代演进，每一代有中国神话命名和独立技术说明书。命名规则见 `.devin/rules/system-generation-naming.md`。

| 代际 | 神话名 | 核心理念 | 技术说明书 |
|---|---|---|---|
| 第一代 | **盘古** | 静态图前置 | `dev-docs/249-v0-2026-08-07-第一代数学大师系统-最完整技术说明书.md` |
| 中间代 | **女娲** | 动态控制+角色隔离 | `dev-docs/250-v0-2026-08-07-中间代数学大师系统-技术说明书.md` |
| 第二代 | **燧人** | 非特定元认知提问 | `dev-docs/238-v1-2026-08-07-非特定高Level启发式提问方案完整梳理.md` |
| 第三代 | **伏羲** | 形式化边界推进 | `dev-docs/239-v0-2026-08-07-AI数学工程系统-最完整技术说明书.md` |
| **第五代** | **（待命名）** | **集大成者：tell+hint二元组+三层Pipe架构+概念树** | **编写中：`第五代系统技术说明书/编写方案.md`** |

**第五代系统**是四代的集大成者——整合盘古的拓扑覆盖、女娲的T图/W_t、燧人的形状匹配/Level/DFS引导架构、伏羲的不自然识别/形式化边界/两种计算，加上tell+hint闭环和概念树。从前四代继承了29项具体内容（详见`dev-docs/290-v0-2026-08-08-第五代系统从前四代继承了什么-详细梳理.md`），另有7项独特贡献是四代都没有的。

**第五代验证状态**：POC-VMS-8（hint端，bare 0%→tree 67%）、POC-VMS-9（tell端去特化+形式化过滤）、POC-VMS-10（小概念标记分辨）全部PASS。

**第五代交接文档**：`dev-docs/291-v0-2026-08-08-第五代系统工作交接文档-含加载清单和加载顺序.md`

**代际转折点**：盘古→女娲（122-v1诊断架构断层）→燧人（200-202号危机诊断）→伏羲（218号非特定性危机+222号形式化边界）→第五代（tell+hint闭环+概念树，285-291号）

---

## 工作原则

### 从星学项目继承的工作原则

- **新系统本体纪律**：本项目中的"新系统"专指为数学研究建设的知识系统与导航系统。不得把星学代码、星学知识文件或星学运行时称为新系统。
- **有机积累纪律**：新认知应融入已有概念、步骤、专题和来源网络；不能总在文件末尾追加孤立段落，也不能重复制造平行定义。
- **结构可修订纪律**：现有知识系统结构只是当前状态。材料暴露结构问题时，先修正结构，再安放内容。
- **不确定性保留纪律**：不同证明路径、不同数学流派的差异必须保留。没有充分证据时使用"候选、待考、类比"，不能强行统一。
- **AGENTS 高价值内容保全纪律**：重构 AGENTS.md 时，不得把原有高价值规则、操作门槛、索引直接删除。确需移出时，必须已有明确承接文件、保留强约束摘要、保留索引、说明迁出原因。
- **细节推出纪律**：从 AGENTS.md 推出到 dev-docs/ 的内容，不能被视为废弃内容。未来 Session 必须能通过 AGENTS 的索引找回。

### 数学项目特有工作原则

- **渐进积累、迭代测试**：一边装入一边充分测试——每装入一批知识/依赖边/意识节点，就立即用POC验证其价值，验证通过再继续装入。
- **穷尽式知识吸收**：全能数学大师应该知道一切可得的数学知识。十三大来源详见109号方案。
- **数学计算交给工具，数学知识由知识系统承载，数学判断由 AI 执行，三者不混用。**
- **依赖图构建需要数学功力**：判断"代数拓扑依赖范畴论"是一条边——这个判断需要"综述博士"参与。
- **方法论迁移不是照搬**：星学的依赖图结构不适用于数学，数学的依赖图需要重新设计。

### 明确不做清单（123号第五十九节 · 硬约束）

以下8项是项目级硬约束，任何Phase都不得违反：

1. **不先扩张到325000知识节点再验证核心闭环**——先通过DYN-0—DYN-4，证明状态可建模且最小Hint有效
2. **不把完整答案路线改写成"意识"后继续做B组提示**——这是答案泄漏的根因
3. **不用节点覆盖率代替数学正确或研究能力**——100%拓扑覆盖只证明结构保真
4. **不要求或伪造隐藏chain-of-thought**——只处理公开研究产物与工具事件
5. **不让同一Master同时持有答案、设计Hint、运行Solver和评分**——角色隔离是硬约束
6. **不把L1/L2/L3当成同一认知单元的版本号**——L1/L2/L3是提取层次，版本链独立编号
7. **不在状态空间未定义时宣称找到了同调洞**——HoTT/同调/几何方法在对象与分布假设成熟后进入
8. **不让在线一次成功自动写入production H**——candidate规则禁止在线自动提示

### 其他规则指针

- **提示策略路线选择与Level连续谱**：详见 `dev-docs/214-v1-2026-08-06-提示策略路线选择与Level连续谱.md`。核心决策：走路线B（思维模式）而非路线A（堆砌知识）。
- **元组群guided-math-solving**：5个Skill详见 `.devin/rules/guided-math-solving.md`。
- **Tell分类学迭代审计铁律**：对已有profile做FCA再分析、Tell分类学修正时的SOP流程和版本化审计要求。详见 `.devin/rules/tell-taxonomy-iteration-audit.md`。**触发条件**：对已有profile做FCA再分析时；Tell分类学（`FCA学习笔记/08-先验Tell分类学.md`）需要修正时；用FCA理论审查分类学自洽性时。**核心约束**：再分析9步SOP + 版本化审计6条铁律（明面版本历史、四要素记录、覆盖性检查、版本总表、文件结构完整、关联文件同步）。
- **Tell分类学Schema维护铁律**：AGENTS.md中"Tell分类学Schema"节是跨压缩边界保真的核心，分类学修正后必须同步更新该节。详见 `.devin/rules/tell-taxonomy-schema-maintenance.md`。**触发条件**：Tell分类学版本号变化/段结构模式变化/domain变化/结构框架变化/观察Level参数变化/关键修正认知变化时。**核心约束**：08号文件和AGENTS.md Schema节必须一致，不一致即违反rule。
- **Tell分类学研究过程文档存放规则**：Tell分类学相关的研发过程文档（探索性、讨论性、评审性、方案演进性）记录到 `Tell分类学研究过程文档/`目录，不放在`第六代系统研发过程文档/`。编号从343号开始（333-340号已迁移至本目录，341-342号已被第六代研发过程文档占用）。**每次新增文档必须同步更新 `Tell分类学研究过程文档/README.md` 索引。** 详见 `.devin/rules/tell-taxonomy-research-docs.md`。
- **system/ 代码与 .ref 文件同步规则**：`system/` 中每个 `.py` 文件必须有同名 `.ref` 文件，内容是理解该模块需要参考的文档路径列表（相对 repo 根目录）。**改代码或改设计文档后都必须同步检查 .ref**——改了 `.py` 检查 `.ref` 是否还准确，改了设计文档检查引用该文档的 `.ref` 是否需要更新。详见 `.devin/rules/system-ref-sync.md`。
- **审计方法论**：F1-F15断层类型学、D1-D4深度等级、21审计维度，详见 `dev-docs/146-v4-2026-08-05-审计方法论手册-*.md`。
- **形式化思维规则**：从星学继承，适配数学。详见第一代技术说明书249号。
- **项目定位与核心假设**：数学大师制造项目，详见 `原语化AI数学工程系统设计/README.md`。核心假设从星学信念降级为可证伪假设，详见123号。
- **K维度多层知识结构（L1-L4）**：详见 `dev-docs/201号`系列。
- **AI在运行过程中的角色**：经典计算给候选，AI做最终判断。详见 `dev-docs/202号`。
- **Pipe监控SOP**：运行任何Pipe（分析/审计/选题）时，必须启动Monitor Pipe并行监控。**检查时用标准化脚本** `analysis-devin-failure-system/scripts/monitor_check.sh <batch_id>`，禁止inline编写检查命令。脚本输出4项检查：Monitor Pipe pane输出 / alerts集合 / 进程状态 / 进度。详见 `.devin/rules/pipeline-monitor-sop.md`。
- **解题系统Monitor Pipe**（2026-08-17新增）：解题系统（pipe/5服务）现在有独立的Monitor Pipe——`xishujuzhen/solver_harness/pipe/monitor_pipe.py`，13项自动检查（session_health/queue_progress/rate_limit/zombie_sessions/export_landing/solve_time_credibility/failure_rate/throughput_trend/long_running_tasks/proof_completeness/feeder_health/collector_health/db_redis_consistency）+ AI review抽样（每3轮抽样2条candidate_solved检查proof质量）。alert写入ArangoDB `pipe_monitor_alerts`集合。**检查脚本**：`bash xishujuzhen/solver_harness/pipe/scripts/monitor_check.sh`（5项检查+对AI的核心提醒：检查Monitor Pipe的系统深度审查结果）。**启动**：`pipe_start.sh`自动启动Monitor Pipe，或`pipe_control.py monitor start --interval 300 --concurrency 20`单独启动。`pipe_control.py health`输出末尾提醒AI去检查Monitor Pipe。详见 `dev-docs/391号`。
- **审计Pipeline Rate Limit防护**：运行audit_launcher前必须检查当前devin cli进程数并据此设置并发（>8个进程时并发=1）。rate limit是账户级的，跨所有CLI实例共享。选题只用status=completed的审计结果。详见 `.devin/rules/audit-pipeline-rate-limit.md`。根因分析见 `dev-docs/388号`。
- **Mid-Hint实验选题数据链**：Pipe 1（分析2050条）→ Pipe 2（审计721个PASS_SELECTABLE）→ **Pipe 3（选题708条，产出47道YES候选+69道假朋友+30道边界）** → POC-0 CasePack精筛（✅v1已冻结·2026-08-17，6正迁移+4假朋友+2边界从Pipe 3精筛）。Pipe 3规模化运行已完成（2026-08-17），产出统计见 `analysis-devin-failure-system/output/selection-full1/selection_results_summary.json`。详见 `eight-system/HANDOFF.md`和`analysis-devin-failure-system/output/analysis_summary.md`和`audit-full1/audit_summary.md`。
- **Pipe 3选题系统（已扩展·2026-08-17·规模化运行完成）**：复用错题分析系统框架（audit_launcher的tmux架构+Redis队列+rate limit防护），新增`src/selection_collector.py`/`selection_launcher.py`/`selection_result_collector.py`+`run_selection_pipeline.py`+`templates/selection_agents_md.md`+`src/monitor_selection.py`+`scripts/monitor_check_selection.sh`。**已按412号方案扩展**——提示词模板增加POC Preparation Metadata节（6项POC准备数据字段），解析器增加6个新标签的解析和DB写入，collect加跨batch去重，monitor_selection.py提供POC字段质量监控。**规模化运行完成（2026-08-17）**：708/708题全部完成，0失败，0 XML解析失败，耗时约85分钟（5并发）。产出47道suitable=YES候选题+69道假朋友候选+30道边界候选，6字段填写率100%，逻辑一致性0问题（1个初始问题已修正）。YES题batch分布均匀（batch1:15/batch2:10/batch3:10/extended:12）。分类逻辑审查见`dev-docs/387号`§九。扩展方案见`Tell分类学研究过程文档/412号`。运行SOP见下方"### Pipe 3扩展运行SOP"小节。
- **MH第一圈(00995)已完成**：交互模式运行13分钟，AI用doubling construction解决n≡2(mod 4)卡点，答案5048。**重大发现：标准答案3800有误**——穷举代码`mean_int_search.py`的`row_options`只生成排序行，漏掉非排序行解空间，n=6错误判定IMPOSSIBLE。n=6构造已程序验证正确（1-36每个出现一次，所有行/列均值整数）。正确答案5048（S={1,...,100}\{2}）。详见`eight-system/runs/midhint/realtrack/00995/experiment_report.md`和`verification/README.md`。
- **题目纠错记录**：`dev-docs/389号`——集中记录所有发现标准答案有误的题目。**选题前必须先查本文档**。当前记录：polymath_00995（标准答案3800→5048）。ArangoDB `problem_profiles`集合中已更新正确答案。
- **两套Pipe命名体系统一说明（2026-08-17厘清）**：项目中存在两套Pipe命名体系，用了相同的编号但指不同的东西，必须区分：
  - **第六代系统Pipe体系**（AGENTS.md第1014-1018行定义）：Pipe 0 / Solver AI（推理AI做数学）→ Pipe 1 / Parser AI（分析脉络格化识别trace）→ Pipe 2 / Telling AI（trace匹配到tell库）→ Pipe 3 / Guide AI（hint变成引导树新边）。这是Grove核心循环的四Pipe架构。
  - **错题分析系统Pipe体系**（387号dev-docs目录定义）：Pipe 1（分析Pipe——判定d1/d2方向错误类型）→ Pipe 2（审计Pipe——检查分析结果质量属性）→ Pipe 3（选题Pipe——按Mid-Hint标准语义选题）。这是错题分析系统的三Pipe架构，**缺少Pipe 0**——因为bare AI跑题在系统外完成，输入是已经跑完的失败trace。
  - **两套体系的关系**：错题分析系统的Pipe 1是第六代系统Pipe 1的粗粒度简化版（判定d1/d2 vs 完整脉络格化识别trace）；错题分析系统的Pipe 2/3在第六代系统中没有对应（审计和语义选题是错题分析系统特有的）。两套体系不要混淆——提到"Pipe 1"时必须明确是哪个体系。
  - **完整流程的Pipe顺序**（统一视角）：Pipe 0 Solver AI跑题产出失败trace → Pipe 1识别d1/d2（方向错误？什么类型？）→ Pipe 2审计分析结果质量 → Pipe 3语义粗筛适合Mid-Hint的题 → POC-0 CasePack精筛→22道CasePack → POC-1因果取商深度分析→TellCore → POC-2~9六门审计+端到端闭环。详见396号§7.4"Pipe 3在识别端中的角色"和399号POC-0方案§4.1"与Pipe 3的接力关系"。
- **非特化理论综合文档（396号）**：`Tell分类学研究过程文档/396-v0-2026-08-17-非特化理论综合-从钟形曲线最高点到认知Option与Pareto前沿.md`——把用户的Tell/Hint概念厘清（钟形曲线绑在Hint上不是Tell上）与GPT在371/372号看到的三层深化（Pareto前沿/认知Option/因果贡献证明）统一成一份完整认知。包含：GPT框架里两个不同的"从trace中读"（识别端从失败trace读分叉vs学习端从成功trace提取认知技能）、错题分析系统是识别端工程化实现、Pipe 3和POC-0的接力关系、GPT设计的POC系列状态（373号9个POC，POC-0/1已完成，POC-2~8未执行）。
- **POC系列审视文档（397号）**：`Tell分类学研究过程文档/397-v0-2026-08-17-GPT373号POC套装的逐个审视-完备性合理性与缺失项.md`——逐个审视373号9个POC的完备性和合理性，识别过度设计部分（POC-5首批过早/POC-7版本修订过重/CaseCard 30字段过多/评分表10维度过重）和GPT未考虑到的8项缺失（最关键：Hint非特化程度钟形曲线验证/识别端验证/基础因果效应验证）。建议修订后首批POC系列为11个POC。
- **POC自包含方案文档（398-409号）**：`Tell分类学研究过程文档/`下12份自包含POC方案文档（398号POC-2.5基础因果效应验证/399号POC-0 CasePack冻结/400号POC-0.5变形关系声明/401号POC-1因果取商增强版/402号POC-2可选择/403号POC-3.5 Hint非特化程度验证/404号POC-3可执行/405号POC-4可终止/406号POC-6可归责/407号POC-7可持续学习简化版/408号POC-8端到端闭环/409号POC-9识别端验证）。每份遵循398号样板的10节结构（§0规范/§1定位/§2理论背景/§3前置状态/§4输入/§5方法/§6输出/§7通过标准/§8被索引文档全文加载清单/§9执行约束/§10与其他POC关系），§8列出3-7份需全文加载的核心文档。**未来20万上下文的AI只加载某份POC方案+它§8清单的文档，就能完整执行这个POC，不需要用户另外指点。**

### Pipe 3扩展运行SOP（5题分组+检查标准·2026-08-17建立）

> 本小节是Pipe 3扩展后的**永久性运行SOP**。任何Session的AI运行Pipe 3规模化选题时，必须按本SOP执行。

#### 运行思想

**不直接全量并发，而是5题一组、5并发处理、每组完成后检查。** 原因：

1. **早发现质量问题**——如果6个新字段的填写率或值分布有系统性问题（如全部填unclear、全部填hard），5题就能发现，不需要跑完726题再发现
2. **早发现rate limit问题**——5并发是小规模验证，确认rate limit安全后再继续
3. **渐进式放量**——前几组用5并发验证稳定性，后续可以根据rate limit情况调整并发数

#### 操作步骤

```
# 1. collect 5题
python3 analysis-devin-failure-system/run_selection_pipeline.py \
  --batch-id selection-batchN --source-batch-id audit-full1 \
  --step collect --limit 5

# 2. launch 5题（5并发）
python3 analysis-devin-failure-system/run_selection_pipeline.py \
  --batch-id selection-batchN --step launch --concurrency 5

# 3. collect-results
python3 analysis-devin-failure-system/run_selection_pipeline.py \
  --batch-id selection-batchN --step collect-results

# 4. 检查（AI执行，见下方检查标准）
```

#### 检查标准（每组完成后AI必须执行）

**A. 基础完整性检查**

| 检查项 | 标准 | 不通过时的处理 |
|---|---|---|
| 完成率 | 5/5完成，0失败 | 失败题重跑（--step launch会自动入队未完成的） |
| XML解析率 | 0 failed_parse | 检查tmux pane输出，看XML格式是否正确 |
| 6字段填写率 | ≥95%（允许少量unclear，但不应该大量为空或MISSING） | 如果大量MISSING，检查模板是否正确注入 |

**B. 值分布合理性检查**

| 字段 | 合理分布 | 异常信号 |
|---|---|---|
| suitable | YES和NO都有，NO占多数（AIME题大部分不涉及局部-全局切换） | 全YES（标准过松）或全NO（标准过严） |
| false_friend_candidate | 大部分no，少量yes或unclear | 全yes（假朋友识别过松）或全no且suitable=NO题多（可能没认真识别） |
| boundary_case_candidate | 大部分no，少量yes或unclear | 全yes（边界识别过松） |
| process_signal_observability | suitable=YES题应为high/medium，suitable=NO题unclear合理 | suitable=YES题全low（过程信号不可观察，POC-3用不了） |
| leakage_risk | 大部分low/medium，少量high | 全high（泄漏风险预评过严） |
| difficulty_estimate | 应有easy/medium/hard分布，与batch对应 | 全hard（没有区分度）或全easy（过松） |
| branch_position_hint | root和line都应出现 | 全root或全line（没有区分度） |

**C. 字段间逻辑一致性检查**

- suitable=YES的题：batch不应为N/A，d2_reclassified应有具体子类型
- suitable=NO的题：batch应为N/A
- suitable=YES且process_signal_observability=low：标记为POC-0精筛时的降优先级题
- suitable=YES且leakage_risk=high：标记为POC-0精筛时的降优先级题
- false_friend_candidate=yes仅应出现在suitable=NO的题中（YES题不可能是假朋友）

**D. 跨组趋势检查（从第2组开始）**

- 累计suitable=YES的题数是否在合理范围（每5题约0-2道YES）
- 6个字段的累计分布是否稳定（不是第1组全hard、第2组全easy这种突变）
- 是否出现rate limit（如果有failed=rate_limited，降低并发数）

#### 检查不通过时的处理

| 问题 | 处理 |
|---|---|
| 6字段大量MISSING | 检查模板是否正确注入（grep 6个字段名在生成的AGENTS.md中） |
| 6字段大量unclear | 可接受——Pipe 3是二阶判断，信息不足时unclear是诚实回答。但如果suitable=YES题的process_signal_observability全是unclear，说明d2_exp质量不够 |
| suitable全NO | 检查这5题的d1是否都是TOKEN_LIMIT/CONNECTION_ERROR（如果是，说明collect读到了不该读的审计结果） |
| suitable全YES | 检查选题标准是否过松（d1是否真的都是DIRECTION_ERROR） |
| difficulty全hard | 412号模板中difficulty判定指引偏粗，AI可能对不涉及局部-全局切换的题默认标hard。这是低价值字段（410号§2说"低价值"），不影响POC-0精筛，可接受 |
| rate limit | 降低并发到1，暂停20分钟后重试（388号§4.1机制） |

#### 通过检查后继续下一组

检查通过后，collect下一组5题继续运行。累计suitable=YES的题达到30-50道时可以停止（412号§7.1的完成标准）。

---

## 工作系统技术说明

> 本节是工作系统（AI自己的工作认知管理）的操作级技术说明。跨session/压缩后AI通过本节恢复"怎么用工作系统"的认知。

### CP1-CP6工作流

工作系统的核心是CP1-CP6六个检查点，通过`cognition_checkpoint_math.py`执行：

| CP | 时机 | 内容 | 命令 |
|---|---|---|---|
| CP1 | 工作开始前 | 种子选择：确定本次任务需要哪些种子认知单元 | `cognition_checkpoint_math.py start --seeds <cog_id1>,<cog_id2>` |
| CP2 | 工作开始前 | 认知加载：AQL图遍历，从种子出发沿depends_on边找到所有前置认知 | CP1命令自动执行 |
| CP3 | 工作开始前 | 缺口检查：验证已加载的认知是否覆盖任务所需 | CP1命令自动执行 |
| CP4 | 工作结束时 | 认知捕获：检查本次工作是否产生新方法论/新依赖/新版本/新术语/临场脚本 | git post-commit hook自动打印 |
| CP5 | 工作结束时 | 认知图更新：新版本/新边写入ArangoDB | `cognition_sdk_math.py`的add_version/add_edge |
| CP6 | 工作结束时 | 任务-认知映射：记录"这个任务用了哪些种子" | `cognition_sdk_math.py`的record_task |

**关键参数**：max_depth=7（数学项目路径比星学长，星学用5）

### Hook机制

| hook | 触发时机 | 脚本 | 作用 |
|---|---|---|---|
| SessionStart | 新session/压缩后 | `session_start_hook_math.py` | 注入认知图统计+工作纪律 |
| UserPromptSubmit | 每次用户提问 | `user_prompt_submit_hook_math.py` | 从`UserPromptSubmit.txt`读取提醒注入 |
| git post-commit | 每次commit后 | `githooks/post-commit` | 打印CP4检查清单（从稀疏矩阵动态查询） |

**改提醒内容**：直接编辑`xishujuzhen/UserPromptSubmit.txt`。**不要用Stop hook**：Stop hook会影响subagent。

### 工作系统纪律

1. **新术语必须追加到词汇表**（认知单元 `glossary`）。
2. **临场脚本沉淀纪律**：现写的一次性脚本，如果操作模式可复用，结束后必须沉淀到 `cognition_sdk_math.py`。
3. **必须 commit**：commit 后 git post-commit hook 会打印 CP4 检查清单。
4. **认知图变更后跑回归验证**：运行 `cognition_audit_math.py poc-regression`。
5. **边吸收边测试**：每次往依赖图/认知图装入新内容后，必须立即跑测试验证。
6. **"检查依赖"触发词**：当用户说"检查依赖"时，AI 立即执行CP4检查清单中的第3、4项。

---

## 当前任务意识跨压缩边界保有用的一节

> 本节是**临时性**的，用于跨压缩边界保持当前活跃任务的完整工作意识。任务完成后清空，把需要长期保持的认知迁移到TODO或Memory Section。

### 当前任务：错题分析系统selfrun载体接替（2026-08-16起·活跃）

devin cli载体失效，错题分析系统（`analysis-devin-failure-system/`）的分析/审计AI由ZCode主会话+subagent顶替，现有流水线零改动。进度：1579/3180题完成，剩余polymath 1433可放量、deepmath/oda 168待修data_collector题文错位缺陷。

- **主交接文档**：`任务追踪/08-错题分析系统selfrun载体接替.md`（进度游标/坑清单/恢复命令）
- **操作手册**：`analysis-devin-failure-system/docs/selfrun-workflow.md`（机制/验证记录/交接与恢复节）
- **核心机制**：`selfrun_driver.py plan`生成任务文件→每波派3个subagent→`sweep --ingest`入库；每~100题`recheck`双盲复测（d1一致率≥80%阈值）
- **两个必须知道的坑**：①insert_result纯insert，禁止全量重跑collect（结果翻倍），增量只走collect-delta；②devin时代audit-launcher僵尸服务若仍在跑需先停（failed_stall任务可被selfrun回收）

### 当前任务：解题侧脉络分析新方案执行（2026-08-16起·活跃）

解题侧脉络分析线（`system/solve_vein_analysis/`，VMS-31~43）经390号评审后重构：363号路线图及route-lock已SUPERSEDED（不再是真相源，勿按其指针推进资格链），22个资格链脚本冻结。现行唯一方案=391号：P0清偿与冻结→P1真实数据golden slice→P2 trace→tell对接→P3 Grove闭环接入。执行载体=ZCode主会话+subagent+确定性代码（devin cli不再参与，391号§3.5）。**当前状态：P0已完成（2026-08-16，五层commit+SUPERSEDED标记+293项复跑绿，含freeze测试platform环境钉死修复）——下一对象是P1。**

- **方案入口（含§8唯一状态源看板）**：`第六代系统研发过程文档/391-v0-2026-08-16-解题侧脉络分析新工作方案-取代363号路线图.md`
- **常备参考**：392号（入题侧脉络分析31条经验全量提取与解题侧对照）、390号（过度设计评审）
- **操作状态（commit游标/坑清单/恢复命令）**：`任务追踪/09-解题侧脉络分析新方案执行.md`
- **编号注意**：393/394/395号已被391号预留（P1结果/P2协议/P2结果），解题侧新文档从396号起；第六代目录与Tell分类学目录在380-389段已冲突，跨目录查编号勿只看一个目录

### 当前任务：非特化研究（2026-08-17起·活跃·并行于大规模解题系统和错题分析系统）

**任务定位**：非特化研究是一个独立任务线，并行于"大规模解题系统运行"和"错题分析系统运行"。它的目标是验证(Tell, Hint)的有效性——从正确的答题过程中分层提取有价值的解题思维，将其中因果充分的认知动作提炼成TellCore，按相应非特化策略产生Hint，最终Hint能摸到钟形曲线最高点（或Pareto前沿）。

**与其他任务的并行关系**：

```
任务线1：大规模解题系统运行（Pipe 0 Solver AI跑题）
  → 产出：bare AI的失败trace和成功trace
  → 代码：xishujuzhen/solver_harness/

任务线2：错题分析系统运行（Pipe 1分析→Pipe 2审计→Pipe 3选题）
  → 产出：d1/d2判定 + 审计通过的结果 + **Pipe 3语义选题结果（708条，含6项POC准备数据，47道YES候选+69道假朋友+30道边界）**
  → 代码：analysis-devin-failure-system/
  → 文档：dev-docs/387号（方案）、388号（rate limit根因）、Tell分类学研究过程文档/412号（Pipe 3扩展方案）
  → 状态：Pipe 3规模化运行已完成（2026-08-17），产出已就绪供POC-0使用

任务线3：非特化研究（POC-0~9验证Tell/Hint有效性）← 本任务
  → 输入：错题分析系统的Pipe 3选题结果（**47道候选题+69道假朋友+30道边界+6项POC准备数据，已就绪**）
  → 产出：TellCore v0 + HintRenderer + HintInstance + EvidenceRecord + 钟形曲线/Pareto前沿实验证据
  → 文档：Tell分类学研究过程文档/396-410号
  → 代码：暂无独立代码（POC阶段以方案文档驱动，执行时复用solver_harness）
```

**三线接力关系**：任务线1跑题→任务线2分析审计选题→任务线3验证Tell/Hint有效性。任务线3的输入依赖任务线2的Pipe 3产出，但任务线3的理论研究和POC方案设计可以与任务线1/2并行进行。

**核心文档体系**：

| 文档 | 位置 | 内容 |
|---|---|---|
| 396号 | `Tell分类学研究过程文档/396-v0-2026-08-17-非特化理论综合-*.md` | 非特化理论综合——用户Tell/Hint厘清+GPT三层深化（Pareto前沿/认知Option/因果贡献证明）+GPT框架两个"从trace中读"+错题分析系统是识别端工程化实现+Pipe 3和POC-0接力关系+GPT设计POC系列状态 |
| 397号 | `Tell分类学研究过程文档/397-v0-2026-08-17-GPT373号POC套装的逐个审视-*.md` | 373号9个POC的逐个审视——识别过度设计（POC-5过早/POC-7过重/CaseCard过多）+8项缺失（最关键：Hint非特化程度验证/识别端验证/基础因果效应验证） |
| 398-409号 | `Tell分类学研究过程文档/39*-*.md` | 12份POC自包含方案文档（POC-0/0.5/1/2/2.5/3.5/3/4/6/7/8/9），每份10节结构+§8被索引文档全文加载清单，未来AI只加载一份POC方案+§8清单即可执行 |
| 410号 | `Tell分类学研究过程文档/410-v0-2026-08-17-Pipe3为POC系列顺带做什么-*.md` | Pipe 3顺带产出6项POC准备数据（d2子类型/假朋友候选/边界题候选/过程信号可观察性/泄漏风险/难度预估） |
| 411号 | `Tell分类学研究过程文档/411-v0-2026-08-17-POC资产准备分析-*.md` | POC资产准备分析——7项现在可准备+6项需等前置POC完成 |
| 412号 | `Tell分类学研究过程文档/412-v0-2026-08-17-Pipe3扩展自包含方案-*.md` | Pipe 3扩展自包含方案——扩展选题提示词增加6个输出字段+规模化运行+产出POC-0候选题清单。这是POC-0的前置工作 |
| poc_assets/ | `Tell分类学研究过程文档/poc_assets/` | 7项已准备好的POC资产（poc_0简化CaseCard/poc_0.5变形关系声明/poc_1候选TellCore+独立审查者指南/poc_2小型Tell库/poc_3.5的5个HintInstance/poc_9失败trace选题） |

**POC系列执行顺序**：

```
[前置] Pipe 3扩展（412号方案）——扩展选题提示词+6项POC准备数据+规模化运行
  → 产出：30-50道候选题 + 6项POC准备数据（d2子类型/假朋友候选/边界题候选/过程信号可观察性/泄漏风险/难度预估）
  → 这是POC-0的前置依赖——没有Pipe 3产出，POC-0只能退回人工筛选1071条DIRECTION_ERROR题

Phase A：策略对象成形
  POC-0 CasePack冻结（✅v1已冻结·2026-08-17）——从Pipe 3产出精筛6正迁移+4假朋友+2边界，保留v0的source_trace/变形/组合→22道CasePack v1（`poc_assets/poc_0/casepack_v1.md`）
  POC-0.5 变形关系声明（✅已完成·2026-08-18·400号方案，变换→题目映射审查完成，7个gap标注留待未来题包扩展）
  POC-1 因果取商增强版（✅已完成·2026-08-18·401号方案，提取完备性检查+Pareto前沿分析+遗漏项裁决完成，标准8✅通过（有条件）——3条遗漏全部补入（思维C→binding_rules扩展/思维D→internal_policy step4扩展/思维F→internal_policy新增step4.5），3个候选噪声全部保留但有标记，修订候选TellCore v0.1已记录，Pareto前沿={候选B,C}不变。有条件通过的条件：POC-3验证3个补入可执行+POC-2.5验证3个候选噪声部分可删除）

Phase B：基础验证
  POC-2 可选择（402号方案）
  POC-2.5 基础因果效应验证（新增·398号方案·快速失败门·⚠️执行中——2026-08-18批量续传运行中，15个run串行，CC-101_bare已完成(POC-2.6)，CC-101_vein执行中。详见下方"POC-2.5批量续传实例"定位方法）
  POC-2.6 续传机制验证（新增·399号方案·✅已完成·2026-08-18·单题测试CC-101_bare通过——Round 1被截断(rc=54K,msg=0)，Round 2续传后AI在Round 1 thinking基础上继续，19个agent step多轮工具调用，写出proof.md(答案boxed{4})，completed=True。续传脚本：`Tell分类学研究过程文档/poc_assets/poc_2.6/continue_solver.py`，支持find/kill命令基于cwd精确管理devin进程）
  POC-2.7 截断vs思维错误（新增·415号方案·▶️**运行中**——919道DIRECTION_ERROR题全量续传，验证续传能否大规模解决截断问题。通过标准COMPLETED≥50%。**系统已实现为Pipe 4+Monitor Pipe**——2026-08-18 12:47启动，3个服务（launcher+monitor+watchdog）全部运行中，concurrency=5, max_rounds=5, method=v2。详见下方"POC-2.7系统运行与检查"节）
  POC-3.5 Hint非特化程度验证（新增·403号方案·396号核心论断的验证·最关键）
  POC-3 可执行（404号方案·用POC-3.5确定的峰值HintInstance）
  POC-4 可终止（405号方案）

Phase C：归责与学习
  POC-6 可归责（406号方案·干预矩阵·检测Mid-Hint"所有提示都有效"问题）
  POC-7 可持续学习简化版（407号方案·只做反例识别+修订候选记录）

Phase D：端到端
  POC-8 端到端闭环（408号方案·+跨模型验证）
  POC-9 识别端验证（新增·409号方案·可并行于POC-8）
```

POC-5可组合推迟到第二个Tell家族验证后。

#### POC续传机制详细SOP（已外移）

> **POC-2.6续传机制经验沉淀 + POC-2.5批量续传实例 + POC-2.7系统运行与检查的完整内容已外移到** `AnalysisSystemOps.md`（项目根目录，§POC续传机制详细SOP节）。
> **加载时机**：当你要运行/调试POC-2.5/2.6/2.7续传机制，或需要查续传脚本用法、批量续传进程管理、Pipe 4运行检查命令时，必须用read工具全文加载 `AnalysisSystemOps.md`。只看当前状态摘要时不需要读。

### 当前任务：第六代系统研发

**任务背景**：第五代系统技术说明书50个文件已全部完成。当前进入第六代系统研发阶段——围绕非局部tell、FCA数学基础、并发Telling AI、Pipe 0简化+Pipe 2并行化等方向展开。

**文档存放**：第六代有两个文档目录，性质不同——
- `第六代系统研发过程文档/`：探索性、讨论性、评审性文档，三位编号（303号起），和 grove repo 同步。研发过程中不确定的内容放这里。
- `第六代系统技术说明书/`：规范性、工程性技术规格，章节编号（01-09）。只有经过讨论、评审、确认真正值得最终记录的内容才放这里。
- 详见上方"第六代系统文档存放规则"小节。

**第五代系统技术说明书**：`第五代系统技术说明书/` 目录下50个文件已全部完成，作为第六代研发的参照系。加载顺序见 `第五代系统技术说明书/README.md`。

**第六代研发已完成的关键文档**（均在 `第六代系统研发过程文档/`）：
- 303-309号：从 grove repo 复制的7份探索文档（非局部tell、FCA、原语化、trace-tell-hint命名等）
- 310号：worktree侧对grove侧303-309号文档的评审——判断哪些方向有闪光点、哪些跑偏
- 311号：并发Telling AI方案——Pipe 0简化（粗domain分类）+ Pipe 2并行化（多Telling AI并行trace识别+汇总AI精筛）
- 312号：第六代系统的两个核心问题——Trace识别与Trace→Tell匹配
- 313号：Tell分类学研究——建立第六代Tell的分类体系
- 314号：第六代系统必须着力解决的三个问题——非局部tell库缺失/推理脉络格化/Tell分类学
- 315号：第六代系统的完整工作流——从推理AI探索到引导树填充+完备性检查（6个缺失全部不是问题）+Parser AI定义+脉络分析管线
- 316号：第六代系统理想化工作过程——规范化完整描述（9个章节）
- 317号：第六代系统POC验证方案——20个POC三层组织（基础能力/管线验证/系统验证）
- 318号：第六代系统流程Pipe图——Pipe命名与AI命名（Solver/Parser/Telling/Guide）
- 319号：第六代系统流程Pipe图——形式化定义（Python代码+dataclass）
- 320号：POC-VMS-28执行方案——AI一眼做格化+trace识别（IMO 2009 P6蚱蜢问题）
- 321号：第六代系统设计认知——提示词是核心资产
- 322号：POC-VMS-28提示词V2——用FCA和Hasse图启发AI，列8种复杂情况
- 323号：POC-VMS-28提示词V3——加上为什么、影响例子、反模式三个章节
- 324号：POC-VMS-28提示词V4——一份基础+两个附加章节（树状输入过程A/线性输入过程B）
- 325号：第六代系统设计认知——多套提示词并发
- 326号：第六代系统设计认知——三处对齐同步（目录/代码清单/POC验证）
- 327号：POC-VMS-28执行方案v1——用V4提示词做第一次POC（一次一套set_A）
- 328号：第六代系统设计认知——文档自包含与可审计标准（通用，适用于所有研发过程文档）
- 329号：POC-VMS-28执行方案v2——自包含版（按328号标准重写）
- 333号：脉络分析Pipe内细化方案——格化与trace识别分离（三阶段架构：格化→程序枚举→综合分析）
- 334号：脉络分析新管线审计结果与改进方案——nonlocal trace退化修复（审计维度+历史运行对比+迭代终止条件）
- 335号：V8格化session的thinking过大问题分析——保守方案（不拆分，简化提示词+超时降级；v1修订：方案D 2步文件拆分，验证不退化）
- 336号：综合分析阶段文件拆分流程控制方案——不会退化的4阶段拆分（验证大幅提升：trace 43→88）
- 337号：全管线验证计划——格化+综合分析双文件拆分（6个验证维度+通过标准）
- 338号：全管线非退化审计方案——各V各阶段历史对比（3层审计+7个历史轮次+文件版本追踪）
- 339号：研发资产管理改进方案——从文件版本追踪的痛苦中提炼（run_manifest.json+4层保证）
- 340号：子管线超时降级方案——不卡住整个系统（独立超时+至少1个通过即可+数据库记录+入口返回值）
- 341号：全流程日志方案——滚动日志到system/logs/（单文件1MB+目录500MB+循环滚动）
- 342号：系统时间意识方案——全管线全子管线运行时间记录（3层时间记录+数据库timing字段+耗时摘要）
- 343号：six/合并到system/方案——system成为自包含的第六代系统（代码层+文档层+运行时层，终止six/维护）

### 系统时间意识与效率意识（342号方案落实）

**这是系统的功能，不是可选的附加**——整个系统必须有时间意识、效率意识。

**3层时间记录**：

1. **日志时间戳**（341号方案）：每条日志带`[YYYY-MM-DD HH:MM:SS]`时间戳，关键位置记录耗时（"格化版本V8完成，耗时200秒"）

2. **数据库结构化时间记录**：`problem_entries`集合的`timing`字段记录全管线全子管线运行时间：
   - `total_duration_sec`：总耗时
   - `phase1_grading.duration_sec` + `versions.{V5/V7/V8/V10}.duration_sec`：格化阶段总耗时+各版本耗时
   - `phase1_5_enumerate.duration_sec` + `versions.{V7/V8/V10}.closed_elements_count`：枚举阶段耗时+各版本闭元素数
   - `phase2_synthesis.duration_sec` + `steps.{step1-4}.duration_sec`：综合分析总耗时+4阶段拆分各步耗时

3. **运行结束耗时摘要**：运行结束时打印耗时摘要表：
   ```
   === 耗时摘要 ===
   阶段1 格化: 300秒（V5:180s V7:超时 V8:200s V10:280s）
   阶段1.5 枚举: 5秒（V7:闭元素27 V8:闭元素46 V10:闭元素26）
   阶段2 综合分析: 720秒（step1:120s step2:240s step3:150s step4:210s）
   总耗时: 1025秒（17分钟）
   ```

**时间数据用途**：
- 效率分析——定位瓶颈（格化慢还是综合分析慢？哪个版本最慢？综合分析哪个step最耗时？）
- 超时阈值调优——340号方案的超时时间需要历史耗时数据支撑
- 运行对比——不同run_id的耗时对比，发现性能退化

### 研发资产管理（已外移）

> **完整内容已外移到** `SixthGenRnD.md`（项目根目录）——第六代系统研发管理制度+system/docs索引+运行资产管理+目录命名规范+数据库记录+审计流程+设计原则+研发文档索引。
> **加载时机**：当你要做第六代系统研发管理工作（运行vein_analysis实验、管理run_id、审计run产出、查system/docs架构文档、查研发过程文档303-343号清单）时，必须用read工具全文加载 `SixthGenRnD.md`。不涉及第六代研发管理时不需要读。

## TODO

> 本节记录跨 Session 需要保持的待办事项。

### 第五代系统技术说明书（✅全部完成）

- [x] 编写01-基础概念（6文件）——tell+hint二元组/引导树闭环/两棵树/Level/概念树
- [x] 编写06-四代继承（6文件）——盘古/女娲/燧人/伏羲的遗产+第五代独特贡献+核心洞察继承
- [x] 编写02-tell端（7文件）——四个成分/去特化/Pipe 0/1/2/标准化语言描述/schema
- [x] 编写03-hint端（5文件）——字典结构/Level梯度/脉络继承/方向注入/schema
- [x] 编写04-概念树（5文件）——大概念小概念/概念文件格式/按需加载/概念膨胀应对/schema
- [x] 编写05-引导树闭环（5文件）——三个推动关系/并发DFS/回溯铁律/停机条件/辅助智能体JD
- [x] 编写07-工程规格（9文件）——系统架构总图/Pipe接口定义/ArangoDB schema/AQL查询模板等
- [x] 编写08-验证状态（5文件）——POC-VMS-8/9/10+验证总结+POC系列方案
- [x] 编写09-附录（3文件）——术语表/文档索引/参考文献

### 第六代系统必须着力解决的问题（314号）

> **文档**：`第六代系统研发过程文档/314-v0-2026-08-10-第六代系统必须着力解决的问题.md`
> **问题1（库侧）**：现有4164个tell全部是第五代局部分析方法的产物，没有经过非局部分析。tell库中看不到"反证法"、"同构之桥"、"构造-分析-排除"等高Level/非局部tell。用当前分析方法分析费马大定理证明，AI绝对不会分析出"同构之桥"。
> **问题2（识别侧）**：推理脉络的"格"化——如何找出所有Level的脉络视图。非局部tell存在于中间Level，但要找到中间Level的tell，必须先把推理脉络格化。n个节点的脉络有2^(n-1)种看法，不能全枚举，需要用FCA格遍历算法系统化地找出有意义的Level视图。问题2是问题1的前置。
> **问题3（分类侧）**：Tell的分类学——建立同时覆盖局部tell和非局部tell的分类体系。313号已启动研究任务线。依赖问题1和问题2，但局部tell的分类部分可以独立先行。

- [ ] **定义"有意义的合并"**——什么样的段合并产生有段特征的段？（304号§8.15的三个例子给出线索：构造+分析+排除合并后有"构造的目的"这个段特征）
- [ ] **把推理脉络转化为FCA形式上下文**——对象=脉络的段，属性=段特征，用闭包算子计算概念格，概念格就是所有有意义的Level视图（304号§7的gap+§8.9的对接）
- [ ] **用FCA格遍历算法系统化枚举Level视图**——不暴力枚举2^(n-1)种看法，用Next Closure/In-Close算法枚举闭元素（304号§8.7）
- [ ] **建立非局部trace的识别方法**——在每个Level视图上做trace识别，不只看一个Level（问题1的识别侧）
- [ ] **用非局部分析方法重新分析现有题目**——对现有455个profile的thinking做非局部分析，补充非局部tell到库中（问题1的库侧）
- [ ] **在非局部tell的基础上建立分类学**——分类学要同时覆盖局部tell和非局部tell，不能只覆盖局部tell

### 第六代系统研发（当前）

- [ ] 设计Telling AI提示词模板（311号§6.2）——提示词必须包含非局部分析的指导
- [ ] 定义汇总AI的判断标准——去重/排序/冲突解决（311号§6.3）——315号已确认不需要汇总，此项可能需要修订

### 第六代系统POC验证（317号启动）

> **方案文档**：`第六代系统研发过程文档/317-v0-2026-08-10-第六代系统POC验证方案-大量POC的设计.md`
> **审计后20个POC按三层组织**：基础能力(VMS-11/12/13/20/24/27/28/29/30)→管线验证(VMS-14/15/16/21/22/23/25)→系统验证(VMS-17/18/19/26)

**第一层：基础能力验证（9个可并行）**
- [ ] **POC-VMS-11**：非局部trace识别——用费马大定理证明作为脉络，验证能否识别"同构之桥"等非局部trace
- [ ] **POC-VMS-12**：推理脉络格化——用FCA格遍历算法找出有意义的Level视图
- [ ] **POC-VMS-13**：Tell分类学基础——查数据库了解现有4164个tell的分类现状
- [ ] **POC-VMS-20**：Pipe 0简化版——粗domain分类实现方式验证（311号§3.2）
- [ ] **POC-VMS-24**：当前分析方法局限性验证——费马大定理证明作为基线（314号§1.2）
- [ ] **POC-VMS-27**：已有产物二次分析——提取格化的全Level Trace（3-5个不同domain的profile，依赖VMS-12，314/312号）
- [ ] **POC-VMS-28**：方式A——AI做全部格化+trace识别，FCA是理论指导（316号§5+用户提问）
- [ ] **POC-VMS-29**：方式B——脚本做FCA格化，AI做trace识别（316号§5+用户提问）
- [ ] **POC-VMS-30**：方式C——AI做全部，FCA验证补漏（316号§5+用户提问）

**第二层：管线验证（7个）**
- [ ] **POC-VMS-14**：脉络分析管线——步骤1-4完整管线端到端运行（依赖VMS-11+VMS-12）
- [ ] **POC-VMS-15（历史载体方案）**：并发Telling AI——311号原案使用多个Devin CLI实例做trace→tell匹配（依赖VMS-13）+分区粒度验证；现行实现若进入Seven/第六代系统，Telling角色必须由provider-neutral `ModelRolePort`选择载体，Devin可作为`DevinCliModelRoleAdapter`但不再等同于角色本体
- [ ] **POC-VMS-16**：Parser AI——从外部解答记录识别新(tell,hint)（依赖VMS-14）+两个输入机制验证
- [ ] **POC-VMS-21**：分类维度结构验证——四层层次结构vs正交维度（依赖VMS-13，313号§4.1）
- [ ] **POC-VMS-22**：FCA角色验证——用FCA定义分类体系vs用FCA验证完备性（依赖VMS-13+21，313号§4.3）
- [ ] **POC-VMS-23**：非局部tell库补充——重新分析现有455个profile（依赖VMS-11，314号§2.1）
- [ ] **POC-VMS-25（历史载体方案）**：Tell存储方案——目录AGENTS.md+可审计遍历（315号原案以Devin CLI启动，依赖VMS-13+21）；现行认知角色启动必须改由`ModelRolePort`路由，其中Devin和Codex都只是可资格化adapter

**第三层：系统验证（4个）**
- [ ] **POC-VMS-17**：端到端工作流——完整7阶段循环（依赖VMS-14+VMS-15）
- [ ] **POC-VMS-18**：引导树妖娆生长——多Level多方向分叉（依赖VMS-17）
- [ ] **POC-VMS-19**：tell库持续增长闭环——过程A→过程B→过程A（依赖VMS-16+VMS-17）+管线统一性验证
- [ ] **POC-VMS-26**：两棵树Level问题——非局部trace的树级位置（依赖VMS-17，315/316号）

### Tell分类学Schema（跨压缩边界保真 · 对抗遗忘）

> **本节是Tell分类学的核心Schema——跨压缩边界也不能忘的东西。** 完整分类学在`FCA学习笔记/08-先验Tell分类学.md`（v3），本节只记录最紧要的结构。如果session压缩后你只记得本节内容，你仍然能知道分类学的结构、当前版本、关键修正历史。**本节的维护规则见`.devin/rules/tell-taxonomy-schema-maintenance.md`。**

#### 分类学结构（v3当前版本）

```
tell的固有属性（形式背景的属性维度——tell本身的特点，不随题目位置变化）：
  第一层：domain（6个：数论/代数/组合/几何/分析/跨域）
  第二层：段结构模式（5大类：构造-分析-排除/探索-诊断-修复/跨域桥接/归约策略/累积-收敛）
  第三层：具体概念（domain×段结构模式的交叉；子模式在此层体现，如"无尽追逐"是"探索-诊断-修复"的子模式）

观察trace的Level选择（不是tell的属性，是检索时的参数——取决于trace结构，不取决于tell本身）：
  局部Level / 非局部Level / 全局Level
```

#### 5大类段结构模式（必须记住的名字和一句话定义）

| 模式 | 一句话定义 |
|---|---|
| 构造-分析-排除 | 构造对象→分析性质→排除不可能 |
| 探索-诊断-修复 | 探索方向→发现gap→诊断→修复（"无尽追逐"是此模式的子模式——诊断环节断裂） |
| 跨域桥接 | 把问题从一个领域翻译到另一个领域 |
| 归约策略 | 把大问题归约到小问题 |
| 累积-收敛 | 逐步累积信息→最终收敛到结论 |

#### 版本历史摘要（全历史在08号文件顶部）

| 版本 | 触发 | 核心修正 | 关键认知 |
|---|---|---|---|
| v1 | 初始建立 | 四层结构：domain→trace类型→段结构模式→具体概念 | 初始构想 |
| v2 | FLT例子 | "局部/非局部/全局"从属性维度移到观察Level参数 | **FLT例子**：同一个tell在"题目就是证明FLT"中表现为全局，在"中间需要FLT"中表现为局部——所以"局部/非局部/全局"不是tell的固有属性，是观察方式 |
| v3 | FCA理论审查 | "无尽追逐"从第二层降级到第三层（"探索-诊断-修复"的子模式） | **FCA属性测试**：tell"应该转向X"在AI追逐时和不追逐但同样需要转向时都出现——tell相同，但"无尽追逐"只在前者中出现——所以"无尽追逐"不是tell的固有属性 |

#### 两个关键修正认知（必须记住的洞察）

**洞察1（v2）**：tell的固有属性和观察trace的方式是正交的两个轴。"局部/非局部/全局"是观察方式（你看trace的粒度），不是tell的属性（tell本身的特点）。同一个tell在不同题目位置（整体目标vs中间步骤）有不同的Level显现，但tell本身不变。

**洞察2（v3）**：FCA要求形式背景的属性必须是对象的固有特征。测试方法：如果同一个对象在不同观察方式下属性值变化，那这个属性不是固有属性。"无尽追逐"是trace特征（AI在trace中的行为模式），不是tell属性——它随AI是否追逐而变化，不随tell本身变化。

#### 高Level概念作为分类学坐标轴（336号·必须记住的洞察）

**洞察3（336号）**：高Level概念（如同构之桥）不是分类学中的"点"（被分类的对象），而是分类学的"坐标轴"（分类的维度本身）。"跨域桥接"是段结构模式这个分类维度上的一个值——它是坐标轴上的一个刻度，不是被分类到一个类别中的对象。降低Level后的具体形式（如"构造Frey曲线"）才是分类学中的"点"。

**结构知识与内容知识分离**：
- **结构知识**（在分类学Schema/解释库中）：domain定义、段结构模式定义、子模式定义（如"同构之桥"是"跨域桥接"的子模式）、高Level概念的三种解释文本——这些是分类学的"坐标轴"
- **内容知识**（在tell库/hint库中）：具体tell条目、具体hint条目，每个条目有{domain, 段结构模式}属性——这些是分类学中的"点"

**高Level概念的存储和使用方式（338号，载体口径已更新）**：高Level部分和低Level部分一样放入可审计分类目录，由专门的认知角色从中读取并识别。338号原案写作“专门的devin cli”；现行物理载体必须由provider-neutral `ModelRolePort`选择，Devin CLI仍可作为经过角色级能力门的正式adapter，与Codex并列。区别在描述方式——高Level部分要"说清楚"+带例子，不能只是一句抽象的话。详见技术说明书`04-概念树/07-高Level概念解释库.md`。

**高Level概念的两种类型（340号）**：
- **第一种（可展开的）**——如构造-分析-排除、累积-收敛、探索-诊断-修复、归约策略：概念本身定义了展开维度（过程的阶段），可以预先降低Level为具体形式列表。组合爆炸可控，覆盖缺口有限。
- **第二种（无法指定展开方向的）**——如同构之桥：概念本身不定义展开维度，目标领域开放，无法预先降低Level。主要靠充分解释+启发式触发+案例积累。组合爆炸风险高，覆盖缺口永远存在。
- 两种类型的Telling AI识别逻辑不同：第一种遍历展开后的具体形式列表，第二种理解概念+格化脉络+判断适用条件（无列表可遍历）。

#### tell和hint的多对多关系（333号·必须记住的洞察）

**洞察4（333号）**：tell和hint是多对多关系——一个tell可以对应多个hint（同一个trace识别结果可以触发多个不同的方向提示），一个hint也可能被多个tell指到（同一个方向提示可能被不同的识别结果触发）。数据库schema中tell_hint_match集合需要支持多对多。

#### 关键文件

| 文件 | 内容 |
|---|---|
| `FCA学习笔记/08-先验Tell分类学.md` | 完整分类学（v3）+版本历史+形式背景+概念格 |
| `FCA学习笔记/09-用FCA重做已完成题目Tell分类-IMO2024P5对比.md` | IMO 2024 P5的FCA再分析对比 |
| `FCA学习笔记/fca-reanalysis-full-plan.md` | **全量处理方案（455题）——分批策略、进度跟踪、恢复机制** |
| `FCA学习笔记/fca-reanalysis-checklist.md` | **执行check list模板——主agent建立TODO List用（铁律0）** |
| `FCA学习笔记/fca-reanalysis-subagent-prompt-template.md` | **subagent prompt模板——主agent构造subagent的prompt用（铁律-1分工架构）** |
| `FCA学习笔记/fca-reanalysis-output-verification-checklist.md` | **产出验证check list——主agent验证subagent产出用（铁律0.5）** |
| `第六代系统提示词积累目录/pipe_1_parser/step_2_grid_vein/set_A_fca_hassee/v6.md` | **V6提示词——格化+全Level Trace识别的完整操作指南（679行）。subagent在步骤0加载** |
| `.devin/rules/tell-taxonomy-iteration-audit.md` | 铁律-1（主agent/subagent分工）+ 铁律0（TODO List）+ 铁律0.5（产出验证）+ 再分析10步SOP + 版本化审计7条铁律 |
| `.devin/rules/tell-taxonomy-schema-maintenance.md` | 本Schema节的维护规则 |

---

### Tell分类学研究（当前任务线，313号启动）

> **启动文档**：`第六代系统研发过程文档/313-v0-2026-08-10-Tell分类学研究-建立第六代Tell的分类体系.md`
> **目标**：建立第六代Tell的分类体系，使得每个tell在分类体系中有明确位置、Telling AI可按分类体系分区、trace→tell匹配有匹配key、分类体系可扩展且有FCA数学基础。
> **⚠️ 迭代审计铁律**：Tell分类学不是一次性建成的——它在不断看新题的过程中被修正。修正的全历史审计在`FCA学习笔记/08-先验Tell分类学.md`顶部明面记录。每次修正必须做覆盖性检查。详见`.devin/rules/tell-taxonomy-iteration-audit.md`。
> **⚠️ Schema维护铁律**：上面的"Tell分类学Schema"节是跨压缩边界保真的核心——分类学修正后必须同步更新该节。详见`.devin/rules/tell-taxonomy-schema-maintenance.md`。

**已完成**：
- [x] **先验Tell分类学建立**（`FCA学习笔记/08-先验Tell分类学.md`）——v3版本，三层属性维度（domain→段结构模式→具体概念）+观察Level参数（局部/非局部/全局）。版本历史：v1初始四层→v2 FLT例子修正（"局部/非局部/全局"从属性移到观察参数）→v3 FCA理论审查修正（"无尽追逐"降级为"探索-诊断-修复"子模式）
- [x] **IMO 2024 P5对比分析**（`FCA学习笔记/09-用FCA重做已完成题目Tell分类-IMO2024P5对比.md`）——用FCA先验分类学重做一道已完成题目的Tell分类，发现原始profile遗漏6个非局部/全局tell显现

**待完成**：
- [ ] **第零步：确认现有tell库的局限性**——确认现有4164个tell全是局部tell，没有非局部tell（314号问题）
- [ ] **第一步：现状调查**——查数据库了解当前4164个tell的分类现状（有没有domain标签/大概念拓扑标签/972个"全局tell"是什么含义/来源分布是否暗示domain分类）
- [ ] **全量FCA再分析**——对67837道题做FCA再分析，按6层难度从高到低进行（Tier 1的452题可立即启动，Tier 2-5待profile提取完成）。方案见`FCA学习笔记/fca-reanalysis-full-plan.md`，与`任务追踪/06-题目侧写Profile提取完整方案.md`对齐
- [ ] **分类学迭代修正**——在抽样验证中发现的分类学问题，按版本化审计铁律修正08号文件
- [ ] **第二步：分类维度设计**——确定层次结构还是正交维度，确定每层/每维度的具体取值，确定和FCA形式上下文的对接方式
- [ ] **第三步：非局部trace段结构模式收集**——从304号§8.15的三个例子出发，用费马大定理证明过程和真实thinking收集更多段结构模式，确定有多少种（依赖314号问题的解决）
- [ ] **第四步：FCA形式上下文构建**——把分类维度转化为FCA形式上下文（对象=tell，属性=分类维度取值），用闭包算子计算概念格，验证完备性
- [ ] **第五步：Telling AI分区验证**——用分类体系验证311号的分区方案（按domain分/按domain×trace_type分/按更细层次分），验证每区tell数和并发数
- [ ] **第六步：POC验证**——验证trace→tell匹配准确率/Telling AI分区效率/非局部trace段结构模式分类覆盖率

### POC验证已完成项

- [x] **POC-VMS-0到VMS-6v2全部完成**：核心循环、可扩展性、Pattern闭环、跨域迁移、动态引导胜率验证
- [x] **POC-VMS-7g泛化POC完成**：验证了"翻译语言"hint在群论和数论两道题上都被AI采纳
- [x] **POC-VMS-7g-v3奥赛难题版完成**：高Level静态hint没有胜出（bare 0% vs knowledge 25% vs highlevel 12%）
- [x] **POC-VMS-8完成**：引导树闭环验证成功（bare 0% → tree 67%）
- [x] **POC-VMS-9完成**：tell端去特化+形式化过滤验证（全部PASS）
- [x] **POC-VMS-10完成**：拓扑相同且距离极近的tell的小概念标记分辨验证（全部PASS）

### 其他待办

- [ ] 补充1709+T05正确hint实验——验证1709题在正确hint下能成功（POC-VMS-10局限）
- [ ] 扩大同一拓扑下的tell数量——从2个tell扩展到5-10个，验证小概念标记分辨的精度
- [ ] 自动化小概念提取——用NLP方法从tell的标准化语言描述中自动提取小概念信号词
- [ ] 验证概念树管理——当小概念数量膨胀时，验证概念文件的层次结构和按需加载机制

---

## Memory Section

> 本节记录跨 Session 需要保持的认知。

### 虚拟数学系统方法论（POC-VMS）

构造HoTT同构虚拟数学系统，用于POC验证检索系统技术方案。核心原理：虚拟系统和真实数学结构相同（HoTT同构），AI在虚拟系统中做真实推理。像虚拟世界测试自动驾驶——物理引擎虚拟，AI决策过程真实。

**5个技术缺口**（四代合并后仍存在）：状态提取/模式匹配/recall检索/Pattern生成闭环/覆盖度。第五代的三层Pipe架构+概念树解决了前两个缺口。

详见：`原语化AI数学工程系统设计/07-验证/03-虚拟数学系统POC方案.md`

### 第五代系统的核心设计

- **tell+hint二元组**：读tell（从thinking读出分叉信号），给hint（给新AI翻译方向）。详见000号。
- **三层Pipe架构**：Pipe 0拓扑化→Pipe 1大概念过滤→Pipe 2小概念标记分辨。详见287号。
- **概念树**：大概念→小概念→概念树的层次化管理。无论tell数量如何增长、概念树如何膨胀，有限上下文的辅助AI都能系统化应对。详见287号用户第六次原文。
- **tell和hint是多对多关系**：一个tell可以对应多个hint，一个hint可以被多个tell触发。
- **tell可以穷举**：穷举是降低tell识别难度的手段。
- **Pipe 1是硬约束不是优化选项**：不能跳过形式化过滤直接让辅助AI暴力遍历全部tell。

### 第一性原理重构基线（123号v1）

123号以`系统探讨.md`全文为母本，把122号v2的工程直觉严格化为可证伪、可审计的对象。本节是后续schema、POC和运行时必须服从的最高基线。详见123号。

---

## Handover Section

> **第五代系统交接状态和数据丢失事件记录已移到**：`dev-docs/第五代系统交接与历史记录.md`
>
> **何时需要读**：需要了解第五代系统交接状态时；需要排查2026-08-05数据丢失事件时。

---

## 术语备忘

- **xishujuzhen**：稀疏矩阵的拼音。星学项目中建立的依赖图导航系统的代号。数学项目中沿用此名，指代同一套方法论下的数学版导航系统。
- **综述博士 / 论文博士**：用户对两种大师的区分。综述博士 = 知识体系全掌握、全能灵活运用；论文博士 = 负责创新。本项目工程化综述博士。
- **tell / hint**：引导树闭环的二元组。tell取自poker术语——观察对手揭示出的信息。hint是给新AI的翻译方向。
- **Pipe 0/1/2**：tell识别的三层架构。Pipe 0拓扑化，Pipe 1大概念过滤，Pipe 2小概念标记分辨。
- **概念树**：大概念→小概念→概念树的层次化管理，应对tell数量增长和概念膨胀。
- **AGENTS-星学版.md**：本目录中保留的星学项目完整 AGENTS.md，是方法论参考资产，不是工作对象。

---

## 题海梳理与数据基座建设（已外移）

> **完整内容已外移到** `DataFoundation.md`（项目根目录）。
> **加载时机**：当你要做题海梳理与数据基座建设工作（从有答案的数学题中提炼(tell,hint)对放入ArangoDB）时，必须用read工具全文加载 `DataFoundation.md`。不涉及题海梳理工作时不需要读。
---

## 管道化GLM-5.2能力边界Profile系统（已外移）

> **完整内容已外移到** `SolverPipeSystem.md`（项目根目录）。
> **加载时机**：当你要运行/监控/调试管道化GLM-5.2能力边界Profile系统（xishujuzhen/solver_harness/pipe/，5服务+Monitor Pipe+Redis队列）时，必须用read工具全文加载 `SolverPipeSystem.md`。本文件还包含"DB schema关键表/数据完整性表/看Solver的4种方法"三个跨系统共享小节，其他系统需要查这些信息时也读本文件。不涉及管道化解题系统时不需要读。
---

## 错题分析系统（已外移）

> **完整内容已外移到** `AnalysisSystemOps.md`（项目根目录，运行操作手册）。设计总索引见 `AnalysisSystemDesign.md`。
> **加载时机**：当你要运行/监控/调试错题分析系统（analysis-devin-failure-system/，判定失败题是"方向出错"还是"token不够"并分类卡点类型）时，必须用read工具全文加载 `AnalysisSystemOps.md`。涉及错题分析系统设计时另读 `AnalysisSystemDesign.md`。不涉及错题分析系统时不需要读。

---

## ★ 外部文档索引（从AGENTS.md外移的文档+关键外部文档）

> **本节是AGENTS.md的总目录。以下文档从AGENTS.md外移或在项目根目录独立维护，按"什么时候必须全文加载"组织。AI进入本repo时先看本索引，按当前工作类型加载对应文档。**

### 从AGENTS.md外移的文档（瘦身工程2026-08-19）

| 文档 | 位置 | 什么时候必须全文加载 |
|---|---|---|
| `DataFoundation.md` | 项目根目录 | 做题海梳理与数据基座建设工作时（从有答案的数学题中提炼(tell,hint)对放入ArangoDB） |
| `SolverPipeSystem.md` | 项目根目录 | 运行/监控/调试管道化GLM-5.2能力边界Profile系统时（xishujuzhen/solver_harness/pipe/）；查跨系统共享信息（DB schema/数据完整性/看Solver方法）时 |
| `AnalysisSystemOps.md` | 项目根目录 | 运行/监控/调试错题分析系统时（analysis-devin-failure-system/）；运行POC-2.5/2.6/2.7续传机制时 |
| `SixthGenRnD.md` | 项目根目录 | 做第六代系统研发管理工作时（运行vein_analysis实验、管理run_id、审计run产出、查system/docs架构文档） |

### 项目根目录独立维护的文档（非瘦身工程产生）

| 文档 | 位置 | 什么时候必须全文加载 |
|---|---|---|
| `AnalysisSystemDesign.md` | 项目根目录 | 涉及错题分析系统设计时（设计总索引/架构/决策） |
| `AnalysisSystem.md` | 项目根目录 | 新Session接手AI的完整加载指南（项目基本信息/当前状态/必读文档/代码结构） |
| `MonitorPipe.md` | 项目根目录 | 设计/实现Monitor Pipe时（连续工作系统的AI智能检查架构设计范式） |
| `续传规范文档.md` | 项目根目录 | 涉及多轮续传工作时（HANDOFF.md结构/截断判定/prompt模板） |
| `000-v0-2026-08-08-引导树闭环-识别端结构定义.md` | 项目根目录 | 需要理解tell/hint二元组时（系统架构的根定义文档） |
| `POC.md` | 项目根目录 | 需要了解所有POC测试的状态时 |

### 关键dev-docs文档（按需加载）

| 文档 | 位置 | 什么时候必须全文加载 |
|---|---|---|
| 273号 | `dev-docs/273-v0-2026-08-08-Grove核心循环与辅助智能体JD-跨AI认知同步.md` | 需要Grove核心循环的完整版时（辅助智能体JD展开/7个场景SOP/角色切换细节） |
| 392号 | `dev-docs/392-v0-2026-08-19-AGENTS_md瘦身外移改造方案.md` | 需要了解AGENTS.md瘦身工程的完整方案时 |

### system/内部文档

| 文档 | 位置 | 什么时候必须全文加载 |
|---|---|---|
| `system/README.md` | `system/` | 涉及第六代系统代码时（目录规范/使用方法） |
| `system/docs/architecture.md` | `system/docs/` | 理解第六代系统架构时（四Pipe+两过程+设计原则+验证历史） |
| `system/docs/references.md` | `system/docs/` | 查研发文档索引/代码映射/POC清单时 |

### seven-system/内部文档

| 文档 | 位置 | 什么时候必须全文加载 |
|---|---|---|
| `seven-system/docs/operations.md` | `seven-system/docs/` | 运行Seven System时（启动/preflight/dry-run/状态/故障处理） |
| `seven-system/docs/implementation-status.md` | `seven-system/docs/` | 查Seven System当前实现状态时 |
