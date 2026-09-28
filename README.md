# README.md — AI工作引导地图

> **强制声明**：AI必须确保本文件内容在自己的上下文中，才能回答用户的问题或进行后续操作。如果上下文中没有本文件的完整内容，必须先用read工具完整加载本文件，然后再回答问题或操作。
>
> 本文件不是知识，是引导地图。它用inline方式描述每个文档讲什么、覆盖哪些问题场景、和其他文档的关系。AI读完本文件后，判断"用户问的这个问题，我需要加载哪几个文档"，然后用read加载，再工作。

---

## 2026-08-24 当前治理接手提示

本 README 是历史导航地图，不是当前项目真值的唯一来源。当前强制宪法是 `AGENTS.md`；用户在
2026-08-24 裁定，继续第六代现状 repo 建设或目录重塑前，必须先对 `glm5.2` 全部 Git 历史做
倒序认知重建。

当前历史重建任务的可接手入口是：

- `AGENTS.md`：项目宪法、目标分支、安全边界、五方向完成门和大图先行工作法；
- `rulings.md`：用户原始裁定；
- `feature-list.md`：归一后的当前要求和验收命题；
- `MEMORY.md`：当前快照、进度和下一步；
- `dev-docs/git-history-reconstruction/README.md`：调查阶段入口、进度和注册表索引。
- `dev-docs/git-history-reconstruction/devin-execution-contract.md`：Devin E010在200k上下文中的完整
  批次、证据、压缩恢复、path-group和迁移Gate合同；
- `dev-docs/repo-group-mapping/README.md`：多代系统repo群梳理入口（核心三仓ORIGIN/GROVE/HOME+
  外围FEITEHUA/SUPERVISOR+排除与负结论登记、Git拓扑结论、2026-09-28未提交内容封存收据、
  GitHub整备Master-Mind处置提案与上传前Gate；本地路径见gitignored附录）；
- `.devin/README.md`：当前活动配置、旧项目Rules/Skills的legacy身份和harness启动边界；
- `~/devin/docs/operations/Devin-CLI超级Repo全历史重建使用说明.md`：启动命令、首条
  指令、续传和后续migration授权方法。

历史coverage现冻结为annotated tag `legacy-reconstruction-snapshot-2026-08-24`，指向
`f7dc625ced176dcc04a6151092fdb0861dc66fdc`并固定1,399 commits。之后的治理/coverage commits不会
让分母无限追涨；当前branch tip仍用于执行治理和最终tip reconciliation。

若本 README 的旧导航内容与上述当前治理入口冲突，按 `AGENTS.md`、用户裁定和 exact Git/current
evidence 裁决；旧文档只作为有日期的证据来源。

---

## 一、系统认知层

### `GroveCoreCognition.md` — Grove核心循环与辅助智能体认知

本repo最高认知优先级。本repo的一切工作都围绕Grove核心循环展开——引导树（给方向Q）→推理AI（探索）→解题树（记录结果）→在终点节点检索→引导树新边→启动新推理AI。理解这个循环=理解系统是什么。

**覆盖问题场景**：
- 你要设计/实现/迭代系统时——循环的三个推动关系、两棵树是同一棵树的两个面、停机条件
- 你要运行实验时——AI的双重角色（系统开发者+系统检查者）、"系统就是脚本"认知转变、切换触发条件
- 你要检查循环完整性时——循环没转起来的判定（只有解题树在长但引导树没生成新边=只转了半圈）
- 你要理解辅助智能体JD时——检查系统健康/循环完整性/审计产出质量/处理异常/检查停机条件，7个场景SOP
- 你要做FCA再分析时——FCA再分析启动铁律（主agent/subagent分工，7条铁律，完整SOP）
- 你要查第六代文档与代码存放规则时——两个文档目录区分、`system/`三层结构、ref和docs同步规则
- 你要运行Seven System时——系统定位、8条硬约束、当前真实实现上限

**依赖关系**：加载本文件后，如果涉及第六代系统代码，可能还需要加载`SixthGenRnD.md`；如果涉及Seven System运行，可能还需要加载`seven-system/docs/operations.md`。

### `000-v0-2026-08-08-引导树闭环-识别端结构定义.md` — tell/hint二元组根定义

系统架构的根定义文档。引导树闭环中"识别→给方向"的操作是一个二元组：tell（识别端，从推理AI的thinking中读出的分叉信号）+hint（注入端，给新AI的翻译方向）。

**覆盖问题场景**：你需要理解tell/hint的精确含义、tell的四个组成成分（分叉信号/分叉类型/未探索诊断/方向匹配）、核心认知（系统识别的不是"AI卡住了"而是"AI没走的分叉"）时。

**依赖关系**：是`GroveCoreCognition.md`的根定义基础，通常一起加载。

---

## 二、repo配置与硬约束层

### `RepoInfo.md` — 本repo基本信息与硬约束详细说明

repo的详细配置和所有硬约束的完整解释。AGENTS.md中只有铁律一行摘要，详细解释在本文件。

**覆盖问题场景**：
- 你要了解repo环境配置时——路径/分支/origin/Python venv/ArangoDB连接
- 你要连数据库时——硬约束1的完整规则（`ARANGO_DB=xishujuzhen_math_glm52`，echo确认，fallback错误数据库的坑）、题目录入信息抓手`problem_entries`集合、Seven System的DB边界
- 你要做Git操作时——硬约束2的完整规则（只在glm5.2分支，显式路径add，改前清干净改后立即commit）
- 你要启动Solver时——硬约束3的完整解释（为什么Solver不能在本repo内运行——AGENTS.md会劫持Solver行为）、tmux-agents-dir模式、Solver角色定义、`--permission-mode dangerous`、solver-batch-health-check元组（三条铁律+7项检查清单+并发上限经验+检查工具batch_status.py的8个命令）
- 你要了解Solver启动方式时——硬约束4的完整规则（生产用noninteractive-solver-run skill，调试用solver-tmux-launch skill，mitmproxy已废弃，批量用pipe系统）
- 你要了解已归档系统时——硬约束5（batch_problem_runner已废弃）和硬约束6（auto_runner已废弃）的完整说明
- 你要查任务追踪文档时——5个活跃任务追踪文档的清单和编写要求

**依赖关系**：如果你要运行Solver，加载本文件后可能还需要加载`SolverOpsSOP.md`（运行操作SOP）和`SolverPipeSystem.md`（管道化系统）。如果你要查任务追踪，加载本文件后按其中的清单加载`任务追踪/`目录下具体文件。

---

## 三、工作原则与规则层

### `WorkPrinciples.md` — 工作原则与规则指针

项目的工作哲学、方法论、不做清单、规则文件指针、Pipe命名体系、POC系列文档。

**覆盖问题场景**：
- 你要理解项目工作哲学时——从星学继承的6条工作原则（新系统本体纪律/有机积累/结构可修订/不确定性保留/AGENTS高价值内容保全/细节推出）+数学项目特有的5条工作原则
- 你要查"不做清单"的详细解释时——123号第五十九节的8项硬约束（每项的完整解释）
- 你要查某个rule文件的触发条件和核心约束时——9个核心rule文件清单（tell-taxonomy-iteration-audit/tell-taxonomy-schema-maintenance/tell-taxonomy-research-docs/system-ref-sync/pipeline-monitor-sop/audit-pipeline-rate-limit/solver-batch-health-check/solver-concurrency/guided-math-solving）
- 你要查关键dev-docs文档时——214号提示策略/146号审计方法论/201号K维度/202号AI角色/388号rate limit/389号题目纠错记录
- 你要区分两套Pipe命名体系时——第六代系统Pipe体系（Pipe 0-3）vs错题分析系统Pipe体系（Pipe 1-3），提到"Pipe 1"时必须明确是哪个体系
- 你要查POC系列文档时——396号非特化理论/397号POC审视/398-409号12份POC方案

**依赖关系**：如果你要查某条规则的完整描述（不只是清单），加载本文件后还需要加载`RulePointers.md`。如果你要做FCA再分析，还需要加载`.devin/rules/tell-taxonomy-iteration-audit.md`。

### `RulePointers.md` — 其他规则指针完整版

每条规则的完整描述（触发条件/核心约束/详细说明）、两套Pipe命名体系的完整论述、POC系列文档的完整内容摘要。`WorkPrinciples.md`中只有清单，本文件有完整描述。

**覆盖问题场景**：你需要某条规则的具体触发条件、核心约束的详细说明、两套Pipe命名体系的完整论述、POC系列文档的完整内容摘要时。

**依赖关系**：是`WorkPrinciples.md`的展开版，通常先加载`WorkPrinciples.md`看到清单，再按需加载本文件查具体规则。

---

## 四、系统运行层

### `SolverOpsSOP.md` — Solver运行通用SOP+旧模式归档

Solver运行的通用SOP（适用于管道化系统pipe/5服务）+旧模式SOP归档（batch_problem_runner/auto_runner）。

**覆盖问题场景**：你要运行/操作Solver时——启动pipe、检查健康、处理异常、批量解题。涉及旧模式batch_problem_runner时也读本文件。

**依赖关系**：通常和`RepoInfo.md`（硬约束3/4）一起加载。如果要查管道化系统的架构设计，还需要加载`SolverPipeSystem.md`。

### `SolverPipeSystem.md` — 管道化GLM-5.2能力边界Profile系统运行手册

管道化GLM-5.2能力边界Profile系统的自包含运行手册。5服务+Monitor Pipe+Redis队列。

**覆盖问题场景**：你要运行/监控/调试管道化系统时。本文件还包含"DB schema关键表/数据完整性表/看Solver的4种方法"三个跨系统共享小节——其他系统需要查这些信息时也读本文件。

**依赖关系**：通常和`SolverOpsSOP.md`一起加载。

### `AnalysisSystemOps.md` — 错题分析系统运行操作手册

错题分析系统（analysis-devin-failure-system/）的运行操作手册。判定失败题是"方向出错"还是"token不够"并分类卡点类型。包含POC-2.5/2.6/2.7续传机制详细SOP。

**覆盖问题场景**：你要运行/监控/调试错题分析系统时。涉及错题分析系统设计时另读`AnalysisSystemDesign.md`。要运行POC-2.5/2.6/2.7续传机制时也读本文件。

**依赖关系**：涉及设计时加载`AnalysisSystemDesign.md`。

### `Pipe3SelectionSOP.md` — Pipe 3扩展运行SOP

Pipe 3扩展后的永久性运行SOP。5题分组+检查标准的规模化选题操作流程。

**覆盖问题场景**：你要运行Pipe 3规模化选题时——5题分组、5并发、检查6字段填写率、渐进放量。

**依赖关系**：通常在错题分析系统运行后加载（Pipe 3是选题阶段）。

---

## 五、数据基座层

### `DataFoundation.md` — 题海梳理与数据基座建设工作线手册

题海梳理工作线的自包含任务文档。从有答案的数学题中提炼(tell,hint)对放入ArangoDB。

**覆盖问题场景**：你要做题海梳理与数据基座建设工作时。任何AI进入本repo做题海梳理工作时，读完本文件即可接手。

**依赖关系**：如果涉及题目侧写Profile提取，还需要加载`ProblemProfileWork.md`。

### `ProblemProfileWork.md` — 题目侧写Profile提取工作

题目侧写（problem profile）提取工作的进度、方法、产出记录。系统数据基座的核心建设线。

**覆盖问题场景**：你要做题目侧写Profile提取工作时——subagent提取profile、审计profile质量、管理Tier 2优先级。

**依赖关系**：通常和`DataFoundation.md`一起加载。

---

## 六、第六代研发层

### `SixthGenRnD.md` — 第六代系统研发管理制度

第六代系统研发管理制度+system/docs索引+运行资产管理+审计流程+设计原则+研发文档索引。

**覆盖问题场景**：你要做第六代系统研发管理工作时——运行vein_analysis实验、管理run_id、审计run产出、查system/docs架构文档、查研发过程文档303-343号清单。

**依赖关系**：如果涉及代码，还需要加载`system/README.md`和`system/docs/architecture.md`。如果涉及Grove核心循环认知，还需要加载`GroveCoreCognition.md`。

---

## 七、工作系统层

### `WorkSystemTech.md` — 工作系统技术说明

工作系统（AI自己的工作认知管理）的操作级技术说明。CP1-CP6工作流、cognition_checkpoint_math.py、Hook机制、认知图更新。

**覆盖问题场景**：你要使用工作系统时——CP1-CP6检查点、cognition_checkpoint_math.py、Hook机制、认知图更新。跨session/压缩后AI通过本文件恢复"怎么用工作系统"的认知。

**依赖关系**：独立加载即可。

---

## 八、任务与记忆层

### `CurrentTaskAwareness.md` — 当前任务意识跨压缩边界保用

当前活跃任务的完整工作意识。跨session接手工作的首要入口。

**覆盖问题场景**：你要接手当前活跃任务时——错题分析系统selfrun载体接替、解题侧脉络分析新方案、非特化研究POC系列、第六代系统研发、系统时间意识与效率意识。

**依赖关系**：接手任务后，按本文件中的指引加载相关系统运行文档。

### `TodoArchive.md` — 跨Session待办事项归档

跨Session需要保持的待办事项归档。包含已完成/进行中/待启动的TODO项。

**覆盖问题场景**：你要查待办事项状态、更新TODO进度、确认某任务是否已完成时。

**依赖关系**：独立加载即可。

### `MemoryArchive.md` — 跨session认知与交接记录

跨Session需要保持的认知（虚拟数学系统方法论/第五代核心设计/第一性原理基线）+第五代交接状态指针。

**覆盖问题场景**：你要了解跨session需要保持的认知、第五代系统交接状态、2026-08-05数据丢失事件时。

**依赖关系**：如果要查第五代交接的详细记录，加载本文件后按其中指引加载`dev-docs/第五代系统交接与历史记录.md`。

---

## 九、参考层

### `Glossary.md` — 术语备忘

项目中使用的专有术语定义。

**覆盖问题场景**：你遇到不认识的术语时——xishujuzhen/综述博士/tell/hint/Pipe 0/1/2/概念树/AGENTS-星学版.md。

**依赖关系**：独立加载即可。

### `SystemAssets.md` — 系统资产索引与活文档

系统的活文档索引——认知资产/原语目录/论文原语化版/五代技术说明书。

**覆盖问题场景**：你要查认知资产索引状态、系统设计原语目录（72个原语+8个概念框架+3个性质标准+7个面相）、原语化AI数学工程系统设计文档、五代系统技术说明书（盘古/女娲/燧人/伏羲/第五代）时。

**依赖关系**：如果要查具体原语的验证状态，按本文件中的指引加载`primitives/`目录下具体文件。如果要查某代技术说明书，按本文件中的指引加载对应dev-docs。

---

## 十、其他关键文档

| 文档 | 什么时候加载 |
|---|---|
| `AnalysisSystemDesign.md` | 错题分析系统设计（架构/决策），和`AnalysisSystemOps.md`分工：Design=设计，Ops=运行 |
| `system/README.md` | 涉及第六代系统代码时（目录规范/使用方法） |
| `system/docs/architecture.md` | 理解第六代系统架构时（四Pipe+两过程+设计原则+验证历史） |
| `system/docs/references.md` | 查研发文档索引/代码映射/POC清单时 |
| `seven-system/docs/operations.md` | 运行Seven System时（启动/preflight/dry-run/状态/故障处理） |
| `seven-system/docs/implementation-status.md` | 查Seven System当前实现状态时 |
| `seven-system/docs/implementation/README.md` | Seven System完整实现入口 |
| `seven-system/docs/audit/README.md` | Seven System独立审计者入口 |
| `任务追踪/README.md` | 任务追踪导航枢纽（各任务追踪文档之间的依赖关系DAG） |
| `dev-docs/第五代系统交接与历史记录.md` | 第五代交接状态/2026-08-05数据丢失事件 |
| `dev-docs/392-v1-2026-08-19-AGENTS_md瘦身外移工程交接说明.md` | AGENTS.md瘦身工程的完整实施记录 |
