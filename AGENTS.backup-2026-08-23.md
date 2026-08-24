# 项目 AGENTS.md · 数学大师制造

> **强制声明**：回答任何问题或进行任何操作前，必须先用read工具完整加载`README.md`（项目根目录）。README.md是AI工作引导地图，用inline方式索引了所有文档。AI必须确保README.md的内容在自己的上下文中，才能回答用户的问题。如果上下文中没有README.md的完整内容，必须重新加载，然后再回答问题或操作。
>
> 本文件（AGENTS.md）只放铁律和最小索引。README.md是引导地图，帮助你判断"当前问题需要加载哪些文档"。加载文档是正常工作流的第一步，不是例外。

---

## 角色

你是Master Agent（实现/审计/迭代数学大师系统），工作目录`~/master-mind-glm5.2-worktree/`。Subagent只执行分配的任务，不承担Master的长期责任。

---

## repo基本信息

- 分支：`glm5.2`，origin：`/data/master-mind`
- Python：`.venv/`（python3.14），DB：ArangoDB `localhost:8529`
- 详细信息（环境配置/数据库连接细节/题目录入抓手/Seven System DB边界）→ `RepoInfo.md`

---

## 铁律

1. **DB**：`ARANGO_DB=xishujuzhen_math_glm52`，运行前必须`echo $ARANGO_DB`确认。忘了source `.env`会fallback到错误数据库。详见`RepoInfo.md`
2. **Git**：只在`glm5.2`分支，显式路径add（禁`-A`/`-.`/`-u`），改前清干净改后立即commit，push需用户授权
3. **两大解题系统在独立repo**：①平凡解题系统`~/master-mind-normal-solver/`——pipe系统（5服务+Redis队列）让AI直接在TUI中解题，已大规模运行，产出大量截断题（单次输出上限导致thinking spin中途停止）和trace；②续传解题系统`~/master-mind-analysis-system/`——多轮次续传解题管线（Pipe 4，持续迭代中），用handover交接文档续传解决平凡系统未解出的题，glm-5.2已在其中解出约148道这类题（DB实况2026-08-21：10,072 run入池，151 completed）。本repo不再包含解题系统代码。进入哪个repo工作前必须先读该repo的`AGENTS.md`
4. **不做清单**（123号·硬约束）：①不先扩张再验证 ②不答案泄漏 ③不用覆盖率代正确 ④不伪造CoT ⑤不角色混用 ⑥不混淆L1/L2/L3 ⑦不未定义宣称同调洞 ⑧不在线自动写入production H。详见`WorkPrinciples.md`

---

## 文档索引

**回答问题前，先判断需要加载哪些文档：**

| 你要做什么 | 加载什么 |
|---|---|
| Grove核心循环/辅助智能体JD/7场景SOP/FCA再分析/第六代文档代码规则/Seven System | `GroveCoreCognition.md` |
| repo详细配置/硬约束详细解释/任务追踪表 | `RepoInfo.md` |
| 工作原则（星学继承+数学特有）/不做清单详细/规则文件清单/Pipe命名体系/POC系列文档 | `WorkPrinciples.md` |
| 题海梳理与数据基座建设 | `DataFoundation.md` |
| 错题分析系统运行操作 | `AnalysisSystemOps.md` |
| 第六代研发管理（run_id/审计/system/docs索引） | `SixthGenRnD.md` |
| 题目侧写Profile提取 | `ProblemProfileWork.md` |
| Pipe 3规模化选题（5题分组） | `Pipe3SelectionSOP.md` |
| 跨Session待办事项 | `TodoArchive.md` |
| 当前活跃任务（跨session接手首要入口） | `CurrentTaskAwareness.md` |
| 工作系统（CP1-CP6/Hook机制/认知图） | `WorkSystemTech.md` |
| 规则完整描述/两套Pipe命名完整论述/POC文档完整摘要 | `RulePointers.md` |
| 跨session认知（POC-VMS方法论/第五代核心设计/第一性原理基线）/交接记录 | `MemoryArchive.md` |
| 术语（xishujuzhen/tell/hint/Pipe/概念树等） | `Glossary.md` |
| 认知资产索引/原语目录/论文原语化版/五代技术说明书 | `SystemAssets.md` |
| 平凡解题系统（pipe架构/运行SOP/审计方法） | `~/master-mind-normal-solver/`的`AGENTS.md`+`README.md` |
| 续传解题系统（Pipe 4管线/SOP/src/docs） | `~/master-mind-analysis-system/`的`AGENTS.md`+`README.md` |

### 其他关键文档

| 文档 | 什么时候加载 |
|---|---|
| `000-v0-2026-08-08-引导树闭环-识别端结构定义.md` | 理解tell/hint二元组根定义时 |
| `AnalysisSystemDesign.md` | 错题分析系统设计（架构/决策） |
| `system/README.md` / `system/docs/architecture.md` | 第六代系统代码 |
| `seven-system/docs/operations.md` | Seven System运行 |
| `seven-system/docs/implementation-status.md` | Seven System实现状态 |
| `任务追踪/README.md` | 任务追踪导航 |
| `dev-docs/第五代系统交接与历史记录.md` | 第五代交接状态/数据丢失事件 |
