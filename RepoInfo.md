# RepoInfo.md — 本repo基本信息与硬约束详细说明

> **来源**：从 AGENTS.md "本 repo 基本信息"节外移（2026-08-19瘦身工程二期，392号方案）。
> **定位**：repo的详细基本信息+硬约束1-2的完整解释+任务追踪系统。AGENTS.md中只保留铁律一行摘要，详细解释在本文件。
> **加载时机**：当你要了解repo的详细配置（Python环境/数据库连接细节/Git规则细节/任务追踪文档清单）时，用read工具加载本文件。日常工作中AGENTS.md的铁律摘要足够。
>
> **注意**：Solver隔离/启动/批量系统等硬约束3-6已随解题系统拆分迁移到`~/master-mind-normal-solver/`repo。详见该repo的`AGENTS.md`和`RepoInfo.md`（如有）。

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

## 任务追踪（跨Session工作意识维持）

**任务追踪文档目录**：`任务追踪/`——每个工作线一个独立文件，顺序编号化，自包含，互不干扰。

**`任务追踪/README.md`** — 导航枢纽，记录各任务追踪文档之间的依赖关系DAG。

**当前活跃的任务追踪文档**：

| 文件 | 工作线 | 焦点 |
|---|---|---|
| `任务追踪/01-253号检索机制验证.md` | 253号检索机制验证 | P0+P1原型验证完成，泛化验证通过 |
| `任务追踪/03-虚拟数学系统VMS-POC验证.md` | 虚拟数学系统POC验证 | POC-VMS-0到VMS-10全部完成 |
| `任务追踪/04-端到端效果验证-接真实Solver.md` | 端到端效果验证 | ✅A/B实验完成，已演进到Grove核心循环 |
| `任务追踪/05-题目侧写Profiling系统.md` | 题目侧写Profiling系统 | 设计完成 |

**任务追踪文档编写要求**：自包含、Checklist化、结构统一（§0当前焦点/§1已完成/§2待办/§3关键决策/§4 Git Commit历史/§5跨Session读取指南）、不删除历史、新建时更新README.md、记录git commit ID和全部产出资产path。详见`任务追踪/README.md`。
