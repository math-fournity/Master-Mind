# SixthGenRnD.md — 第六代系统研发管理制度

> **来源**：从 AGENTS.md 第1239-1471行外移（2026-08-19瘦身工程，392号方案二期）。
> **定位**：第六代系统研发管理制度+system/docs索引+运行资产管理+审计流程+设计原则+研发文档索引。
> **加载时机**：当你要做第六代系统研发管理工作（运行vein_analysis实验、管理run_id、审计run产出、查system/docs架构文档、查研发过程文档303-343号清单）时，必须用read工具全文加载本文件。不涉及第六代研发管理时不需要读。
> **AGENTS.md索引**：AGENTS.md "外部文档索引"节有指向本文件的索引行。

---

### 研发资产管理（339号方案落实）

**运行资产**：
- 每次运行的工作目录：`palyground/absorb/vein_analysis/{run_id:04d}_{problem_id}/`
- 每次运行的归档目录：`system/tests/vein_analysis/runs/{run_id:04d}/`（vein_analysis.py自动归档）
- 每次运行必须生成`run_manifest.json`——记录所有提示词文件、AGENTS模板、step要求文件、代码的md5和git commit
- 回头审计时从run_manifest.json找文件版本，不需要md5对比git历史

**目录命名**：
- 正式运行：`{run_id:04d}_{problem_id}`（如`0011_imo2009p6`）
- 单独测试：`{run_id:04d}_{problem_id}_{test_type}`（test_type只能是`synthtest`/`v8test`等预定义值）
- 不允许无run_id的目录（早期`imo2009p6`是历史遗留，不再新增）

**数据库记录**：
- 每次运行必须写`problem_entries`集合，包含`manifest_path`/`archive_path`/`git_commit`字段
- 中断的运行必须标记为`interrupted`（不是`running`）——TODO，优先级低
- 单独测试也要写数据库——TODO，优先级低

**审计流程**（改进后）：
1. 从数据库查run_id → 直接得到`manifest_path`和`archive_path`
2. 读run_manifest.json → 直接得到所有文件版本、md5、git commit
3. `git show <commit>:<文件路径>` → 查看当时的文件内容

**第六代系统架构文档**（`system/docs/`）——system是自包含的第六代系统：

> **核心定位**：`system/`是自包含的第六代系统——从代码到文档，到运行时。`six/`目录已合并到`system/`（343号方案），不再维护。理解第六代系统只需要看`system/`。
>
> **三层结构**：
> - **代码层**：`*.py` + `.ref` + `.ai-check`——真正运行的代码
> - **文档层**：`docs/`——模块设计说明书 + 系统架构文档
> - **运行时层**：`assets/`——AGENTS模板等运行时资产

**系统架构文档**（`system/docs/architecture.md`）——四个Pipe+两个过程+设计原则+验证历史：

> 包含：四个Pipe（Solver/Parser/Telling/Guide）+两个过程（解题引导/解答吸收）+设计原则（解放思想/反射）+提示词设计认知+VMS-28到28e验证历史+4并发方案+根本认知。

**研发文档索引**（`system/docs/references.md`）——研发过程的"晾衣架"：

> 研发过程文档清单（303-343号）+代码元素到研发文档的映射+POC验证清单（VMS-11到VMS-30）+三个核心问题+系统根本认知+三阶段架构+文件拆分流程控制+脉络分析审计+超时降级+全流程日志+系统时间意识。

**数据结构设计说明书**（`system/docs/schema.md`）——25个dataclass+FCA术语映射：

> 25个dataclass分类+FCA术语映射（双轨术语330号）+核心数据结构详解（Trace/Tell/Segment/LevelView的FCA对应说明）。

**设计原则——解放思想**：

> **核心原则**：不要觉得每个函数只能一个AI、一种方式去做。时时考虑三个维度：
> 1. **多种方式**——同一个函数可以用多种方式实现，用POC验证决定哪种方式可行（如VMS-28/29/30验证三种格化方式）
> 2. **多个AI**——同一个函数可以由多个AI实例并发执行（如311号的并发Telling AI）
> 3. **多个子pipe**——一个函数可以进一步迭代，拆分为多个子函数，每个子pipe独立验证、独立实现

**设计原则——反射**：

> **核心原则**：系统的各处不应该是完全固化的，而是随着系统运行、使用经验丰富而成长发展。流程中必须在合适的地方进行反射——系统停下来审视自己的行为，从中学习，改进自己。
>
> **反射的三层对象**：反射自己的产出 / 反射自己的流程 / 反射自己的认知
> **反射的触发时机**：每次循环结束后 / 匹配失败时 / 停机后 / 周期性反思 / 人工触发
> **和解放思想的关系**：解放思想是设计时的开放性（不要固化设计），反射是运行时的开放性（不要固化运行）。两者配套。

**设计认知——提示词是核心资产**（321号）：

> **核心认知**：六代系统势必积累很多提示词，用于启发AI完成相关的工作。提示词是系统的核心资产，和代码同等重要。
>
> **提示词管理**：提示词需要积累、管理、版本化。每个版本记录版本号/内容/改进原因/验证状态/使用效果。旧版本保留用于对比和回退。提示词和代码一起版本化管理。

**提示词积累目录**（`第六代系统提示词积累目录/`）：

> 提示词完整文本在`第六代系统提示词积累目录/`中按目录结构积累：`Pipe阶段/子pipe/set_<编号>_<简短描述>/v<版本号>.md` + `README.md`
>
> **当前积累**：
> - `pipe_1_parser/step_2_grid_vein/set_A_fca_hassee/`：套A（用FCA/Hasse图启发），V5/V7/V8/V10四个版本+综合分析提示词+4阶段step要求
> - 其他Pipe阶段的目录已建，待积累
>
> **三处对齐同步（326号，硬约束）**：提示词在三个地方有记录，必须对齐同步——
> - **A：提示词积累目录**（`第六代系统提示词积累目录/`）——提示词的完整文本
> - **B：运行时资产**（`system/assets/`）——AGENTS模板（运行时复制到工作目录）
> - **C：POC验证文档**（`第六代系统研发过程文档/3xx号`）——提示词的验证结果
>
> 新增提示词时三处同步创建；改进提示词时三处同步更新版本；POC验证完成后三处同步更新验证状态。

**Schema——晾衣架的完整地形图**：

| 代码位置 | 内容 | 对应的研发文档 | 什么时候看 |
|---|---|---|---|
| `system/schema.py` → `Problem` | 题目数据结构 | 第五代01-基础概念/04-两棵树.md | 讨论题目时 |
| `system/schema.py` → `Hint` | 提示Q数据结构 | 000号+315号§5阶段6 | 讨论hint时 |
| `system/schema.py` → `Tell` | tell数据结构（含分类学四层位置） | 000号+313号§4.1+287号+315号§4.1 | 讨论tell时 |
| `system/schema.py` → `Trace` | trace数据结构（含is_branch_position） | 309号+314号问题2+313号§4.1+315号§6.2.2 | 讨论trace时 |
| `system/schema.py` → `Vein/Segment/Branch/LevelView` | 脉络相关数据结构 | 312号+304号§8.9+318号§4+314号问题2 | 讨论脉络格化时 |
| `system/schema.py` → `Thinking/SolutionRecord` | Pipe 0输出/过程B输入 | 第五代03-引导树闭环.md+315号§6.2.1 | 讨论过程A/B输入时 |
| `system/schema.py` → `SolverInput/SolverOutput` | Pipe 0输入输出 | 319号§1+315号§6.8 | 讨论Solver AI时 |
| `system/schema.py` → `AnalysisInput/AnalysisOutput` | Pipe 1输入输出 | 333号+335号+336号 | 讨论Parser AI时 |
| `system/vein_analysis.py` → `vein_analysis_three_phase()` | 三阶段脉络分析 | 333号+336号 | 讨论脉络分析时 |
| `system/verify_lattice_completeness.py` | 闭元素枚举+三层验证 | 332号 | 讨论程序验证时 |

**第六代系统词汇表**（术语定义 + 代码Schema结合）：

> 以下每个术语给出：定义、来源文档、对应的代码Schema（dataclass/字段）。AI看到术语时，既知道定义，又知道代码中的对应。术语新增时必须追加到此表（工作系统纪律第1条）。

**基础概念**：

| 术语 | 定义 | 来源 | 代码Schema |
|---|---|---|---|
| **题目（Problem）** | 一道数学题——有problem_id/problem_text/domain/answer | 第五代01-基础概念 | `types.py`→`Problem`：problem_id, problem_text, domain, answer |
| **提示Q / hint** | 引导从一个数学处境移动到另一个处境的语义移动。tell的注入端。tell+hint构成二元组。 | 000号§引导树闭环 | `types.py`→`Hint`：hint_id, hint_text, hint_level(0=最具体,N=最抽象), tell_id |
| **tell** | 从trace去特化后存入库中的可泛化思维模式。tell是trace的"泛化版"——从这道题的trace提取出可以启发其他题的思维模式。tell的四个成分：分叉信号/分叉类型/未探索诊断/方向匹配。 | 000号+285号v2修正 | `types.py`→`Tell`：tell_id, branch_signal, branch_type, unexplored_diagnosis, direction_matching, domain, trace_type, segment_pattern, specific_concept |
| **trace** | 在脉络的某个Level视图上识别出的思维模式。trace是Parser AI的产出，Telling AI的输入。过程A描述"AI在这里可以分叉但没分叉"，过程B描述"解答者在这里做了某个操作"。 | 309号+314号问题2+319号 | `types.py`→`Trace`：trace_id, level(0=最细,N=最粗), trace_type(local/non_local/global), pattern_description, source_segment_ids, is_branch_position(仅过程A) |
| **局部trace** | 在单个段上（Level 0）识别出的思维模式。 | 322号§1第二部分 | `Trace.trace_type="local"`，`Trace.source_segment_ids`长度=1 |
| **非局部trace** | 跨多个段的思维模式——只有把几个段合在一起看才能识别出的模式。中间Level视图上的trace。 | 303号+322号§1第二部分 | `Trace.trace_type="non_local"`，`Trace.source_segment_ids`长度>1 |
| **全局trace** | 整个脉络层面的策略模式——只有把所有段合在一起看（最粗Level）才能识别出的模式。 | 322号§1第二部分 | `Trace.trace_type="global"`，`Trace.source_segment_ids`包含所有段 |
| **数学处境（MathSituation）** | 引导树/解题树的节点——一个数学处境。有node_type(root/internal/leaf_success/leaf_deadend/leaf_truncated)。 | 第五代04-两棵树 | `types.py`→`MathSituation`：node_id, problem_id, node_type, situation_text, depth, path_from_root, parent_edge_key |
| **树的边（TreeEdge）** | 引导树/解题树的边——一个提示Q。连接父节点和子节点。 | 第五代04-两棵树 | `types.py`→`TreeEdge`：edge_id, from_node, to_node, hint(Hint), level |

**脉络相关概念**：

| 术语 | 定义 | 来源 | 代码Schema |
|---|---|---|---|
| **脉络（Vein）** | 从推理内容中分析出的思维脉络。过程A从Thinking分析→可能有分叉的树/DAG；过程B从SolutionRecord分析→通常线性。 | 312号+319号 | `types.py`→`Vein`：vein_id, source_id, source_type(thinking/solution_record), structure(linear/tree/dag), segments(list[Segment]), branches(list[Branch]) |
| **段（Segment）** | 脉络中的一个推理步骤或一段推理。最细的段划分是把脉络分成最小的推理步骤。段有特征（用于FCA形式上下文的属性）。 | 314号问题2+319号 | `types.py`→`Segment`：segment_id, vein_id, segment_text, segment_features(dict), order |
| **分叉（Branch）** | 脉络中AI选了A没选B的位置（仅过程A）。 | 000号+319号 | `types.py`→`Branch`：branch_id, vein_id, at_segment_id, chosen_path, unchosen_paths(list) |
| **Level视图（LevelView）** | 段的一种合并方式形成的"看法"。最细Level=每个段独立；最粗Level=所有段合并；中间Level=几个段合并。 | 322号§1第一部分+319号 | `types.py`→`LevelView`：view_id, vein_id, level(0=最细,N=最粗), merged_segments(list[list[str]]), view_features(dict) |
| **格化（grid_vein）** | 把脉络分成段后，考虑段的不同合并方式。每种合并方式形成一个Level视图。"有意义的合并"是把"在思维上属于同一层"的段合在一起。 | 314号问题2+319号§step_2_grid_vein | `pipes.py`→`pipe_1_parser()`的子pipe `step_2_grid_vein()`；产出`list[LevelView]` |
| **FCA（形式概念分析）** | 用闭包算子定义"有意义的合并"——闭元素是指属性闭包等于自身的段集合。直觉上说，闭元素就是"在思维上属于同一层"的段集合。 | 304号 | `Segment.segment_features`是FCA形式上下文的属性集 |
| **Hasse图** | 格的可视化——最下面是最细Level，最上面是最粗Level，中间是各个中间Level，节点之间的边表示"从细到粗的合并关系"。 | 322号§1第一部分 | `LevelView`的level字段定义了Hasse图的层次 |

**过程A/B和输入**：

| 术语 | 定义 | 来源 | 代码Schema |
|---|---|---|---|
| **过程A** | 分析推理AI的上下文——输入是树状的（推理AI探索后折返）。Parser AI在过程A中分析推理AI的thinking/trajectory。 | 319号§pipe_1_parser+324号附加章节A | `ParserInput.process="A"`，`ParserInput.thinking: Thinking` |
| **过程B** | 分析已有题目和解答记录——输入是线性的（已完成解答）。Parser AI在过程B中分析外部解答文本。 | 319号§pipe_1_parser+324号附加章节B | `ParserInput.process="B"`，`ParserInput.solution_record: SolutionRecord` |
| **Thinking** | 推理AI的thinking/trajectory——Pipe 0的输出，Pipe 1过程A的输入。 | 第五代03-引导树闭环+315号 | `types.py`→`Thinking`：solver_ai_id, problem_id, trajectory, rounds(list[dict]), entry_node_id, entry_hint(Hint) |
| **解答记录（SolutionRecord）** | 外部解答记录——Pipe 1过程B的输入。和Thinking的区别：解答记录是已完成的、正确的、通常线性的脉络。 | 315号§6.2.1 | `types.py`→`SolutionRecord`：record_id, problem(Problem), solution_text, is_verified |
| **孤悬trace（orphan trace）** | 没匹配到tell的trace。过程A的孤悬trace存档后用于启发过程B——"从什么Level观察外部解答记录"。 | 315号§6.2 | `TellingOutput.unmatched_traces: list[Trace]`；`Step5Output.orphan_traces`；`loops.py`→`archive_orphan_traces()`/`get_archived_orphan_traces()` |

**Pipe和AI角色**：

| 术语 | 定义 | 来源 | 代码Schema |
|---|---|---|---|
| **Pipe 0 / Solver AI** | 推理AI——做数学。输入是题目+脉络文本+方向Q，输出是thinking+最终状态+终点节点。 | 318号§2.1+315号§6.8 | `pipes.py`→`pipe_0_solver()`；`SolverInput`(problem, path_text, hint)→`SolverOutput`(thinking, final_status, final_situation) |
| **Pipe 1 / Parser AI** | 分析AI——从Thinking(过程A)或SolutionRecord(过程B)中分析脉络、格化、识别全Level Trace。三个子step：step_1_analyze_vein / step_2_grid_vein / step_3_identify_traces。 | 318号§3.1+315号§6.2.2+319号 | `pipes.py`→`pipe_1_parser()`；`ParserInput`(process, thinking, solution_record, orphan_traces)→`ParserOutput`(traces, veins, level_views, process) |
| **Pipe 2 / Telling AI** | 匹配AI——把trace匹配到tell库中的tell。311号后改为多AI并发，每个Telling AI负责一个domain分区。不需要汇总AI（315号确认）。 | 318号§2.1+311号+315号§6.3 | `pipes.py`→`pipe_2_telling()`；`TellingInput`(traces, tell_library_path)→`TellingOutput`(results(list[TellingResult]), unmatched_traces) |
| **步骤5分叉** | Pipe 2输出后的分叉——过程A：匹配到tell→取hint送入Pipe 3；没匹配到→孤悬trace存档。过程B：新建tell+hint存入AGENTS.md。 | 315号§6.2.1/6.4+319号 | `pipes.py`→`step_5_branch()`；`Step5Input`(telling_output, process)→`Step5Output`(process, hints, orphan_traces, new_tells, new_hints) |
| **Pipe 3 / Guide AI** | 引导AI——把hint变成引导树的新边，构造新SolverInput，启动新推理AI。 | 318号§2.1+315号§6.5/6.6 | `pipes.py`→`pipe_3_guide()`；`GuideInput`(hints, problem_id, tree_state)→`GuideOutput`(new_edges, new_solver_inputs, tree_state, stop) |
| **引导树（Guided Expansion Tree）** | "应该往哪走"的视图。每个节点是一个数学处境，每条边是一个提示Q。活的、正在生长的。 | AGENTS.md§Grove核心循环 | `types.py`→`TreeState`：problem_id, nodes(list[MathSituation]), edges(list[TreeEdge]), status(growing/solved/exhausted), running_solvers |
| **解题树（Solution Record Tree）** | "实际走了什么"的视图。引导展开树展开完成后凝固的树。包含成功路径、失败路径、分叉点。 | AGENTS.md§Grove核心循环 | 同`TreeState`——两棵树是同一棵树的两个面 |

**系统级概念**：

| 术语 | 定义 | 来源 | 代码Schema |
|---|---|---|---|
| **tell分类学** | tell的四层分类位置——第一层domain(数论/代数/...)、第二层trace_type(local/non_local/global)、第三层segment_pattern(段结构模式)、第四层specific_concept(具体概念)。 | 313号§4.1 | `Tell`的四个字段：domain, trace_type, segment_pattern, specific_concept |
| **三个核心问题** | 314号定义的三个必须着力解决的问题——①非局部tell库缺失②推理脉络格化③Tell分类学。 | 314号 | `system/docs/references.md` §4 |
| **方式A/B/C** | 317号定义的三种格化方式——A：AI做全部格化+trace识别，FCA是理论指导；B：脚本运行FCA格遍历算法；C：AI做+FCA验证。 | 317号§VMS-28/29/30 | `system/docs/architecture.md` §5验证历史 |
| **多套提示词并发** | 同一Pipe阶段可以有多套不同的提示词（不是不同版本号，是完全不同的设计），并发给多个AI实例处理同一输入。 | 325号§1 | `第六代系统提示词积累目录/`中的set_A/set_B/... |
| **三处对齐同步** | 提示词在三个地方有记录——A目录(完整文本)、B运行时资产(system/assets/)、C POC验证文档——三处必须对齐同步。 | 326号§1 | 提示词积累目录+system/assets/+研发过程文档 |
| **trace→tell匹配（TraceTellMatch）** | 一个trace匹配到一个tell的结果——有trace_id/tell_id/confidence/matched。 | 319号 | `system/schema.py`→`TraceTellMatch`：trace_id, tell_id, confidence(float), matched(bool) |
| `system/process_solve.py` | 解题引导过程（Grove核心循环） | 319号§1+第五代03-引导树闭环.md+315号§6 | 讨论端到端工作流时 |
| `system/process_absorb.py` | 解答吸收过程（tell库增长循环） | 319号§1+315号§6.2.1 | 讨论Parser AI处理外部解答时 |
| `system/docs/references.md` → §1 | 研发过程文档清单（303-343号） | 全部 | 需要查文档编号时 |
| `system/docs/references.md` → §2 | 代码元素到研发文档的映射 | 全部 | 需要追溯代码元素来源时 |
| `system/docs/references.md` → §3 | POC验证清单（VMS-11到VMS-30） | 317号 | 讨论POC验证时 |
| `system/docs/references.md` → §4 | 314号三个必须着力解决的问题 | 314号 | 讨论系统核心问题时 |
| `system/docs/references.md` → §5 | 系统的根本认知 | 315号§6.8+第五代 | 讨论系统设计理念时 |

**如何使用system/docs/**：

1. **用户提到某个概念时**→查`system/docs/references.md` §2，找到对应的代码元素和来源文档
2. **需要查POC验证时**→查`system/docs/references.md` §3
3. **需要查研发文档编号时**→查`system/docs/references.md` §1
4. **需要看某个数据结构的定义时**→看`system/schema.py`中对应的dataclass + `system/docs/schema.md`中的FCA对应说明
5. **需要看系统架构时**→看`system/docs/architecture.md`（四个Pipe+设计原则+验证历史）
6. **需要看脉络分析模块时**→看`system/docs/vein_analysis.md`（三阶段架构+文件拆分）

**如何维护system/docs/**：

1. **新增研发文档时**→在`system/docs/references.md` §1中添加条目
2. **新增或修改数据结构时**→在`system/schema.py`中修改，同时在`system/docs/schema.md`中更新FCA对应说明
3. **新增POC时**→在`system/docs/references.md` §3中添加条目
4. **POC验证完成后**→在`system/docs/references.md` §3中更新状态，在`system/docs/architecture.md`中更新验证历史
5. **修改Pipe接口时**→同步修改`system/schema.py`（输入输出数据结构）+对应模块代码+`system/docs/`中的模块文档
6. **新增核心问题或认知时**→在`system/docs/references.md` §4或§5中添加

**维护规则**：
- 代码元素（dataclass/函数/参数）和`system/docs/references.md`中的映射必须同步——改了一个必须改另一个
- 模块代码变更时同步更新对应的`system/docs/`模块文档
- `system/docs/references.md`是只读索引——不包含实现逻辑，只包含映射关系
- `.ref`文件引用`system/docs/`中的模块文档路径

**设计原则rule绑定**（rule文件在`.devin/rules/`中，AGENTS.md只保留索引）：

| rule | 文件 | 触发条件 | 来源 |
|---|---|---|---|
| **代码为中心铁律** | `.devin/rules/six-codebase-first.md` + `.devin/skills/codebase-first/SKILL.md` | **always-on——任何时候回答或响应用户提问时** | 用户原话 |
| 解放思想原则 | `.devin/rules/six-liberation-principle.md` | 设计或修改任何函数时 | 318号/`principles.py` |
| 反射原则 | `.devin/rules/six-reflection-principle.md` | 设计或修改任何Pipe函数时 | `reflection.py` |
| 提示词原则+三处对齐同步 | `.devin/rules/six-prompt-principle.md` | 设计或修改任何Pipe函数时；新增/改进/验证提示词时 | 321/325/326号/`prompts.py` |
| 文档自包含与可审计 | `.devin/rules/six-doc-selfcontained.md` | 编写或修改任何研发过程文档时 | 328号 |
| 三个核心问题 | `.devin/rules/six-core-problems.md` | 设计或修改任何Pipe时 | 314号/`references.py` |
| POC三层组织 | `.devin/rules/six-poc-organization.md` | 设计新POC时 | 317号/`references.py` |
| 形式化定义同步 | `.devin/rules/six-formal-def-sync.md` | 修改任何dataclass或Pipe函数签名时 | 319号/`types.py`/`pipes.py` |
| 完整工作流对照 | `.devin/rules/six-workflow-alignment.md` | 设计或修改任何Pipe衔接关系时 | 315号/`loops.py` |
| 双轨术语原则 | `.devin/rules/six-dual-terminology.md` | 编写或修订提示词、技术文档、代码注释时涉及术语选择 | 330号§4 |
| 提示词自包含 | `.devin/rules/six-prompt-selfcontained.md` | 创建或修订提示词文件时 | 328号/330号§4建议D |
| **机械化过程描述+程序验证** | `.devin/rules/six-mechanization-reference.md` + `.devin/skills/mechanization-reference/SKILL.md` | 设计提示词时，当认知任务有对应机械化算法且AI用直觉做但产出需完备性保证时 | 332号/用户原话（系统创新） |
| **运行痕迹全程保留** | `.devin/rules/six-trace-preservation.md` | **always-on——设计或实现系统任何运行阶段、阶段间数据传递、AI实例启动、数据库写入时** | 用户原话（系统设计必须既要考虑运行逻辑，也要考虑痕迹保留） |
| **AI Agent启动规范** | `.devin/rules/six-ai-agent-launch.md` | **always-on——启动系统中任何AI Agent实例时** | 用户原话（全部使用tmux，先到指定目录，准备好AGENTS.md和提示词文件，短启动提示词+提示词文件加载） |
| **双重检查机制** | `.devin/rules/six-dual-check-mechanism.md` | **always-on——设计或实现系统任何运行阶段后；系统运行中检查健康状态时；系统运行后审计产出质量时** | 用户原话（代码能保证的用代码检查，无法用代码完成的用流程审计AI检查，.ai-check文件记录checklist） |
| **"更新文档"动作定义** | `.devin/rules/six-update-docs-action.md` | **用户在system系统研发中说"更新文档"时** | 用户原话（"更新文档"代表很多动作，需要思考哪些文档需要更新，以后只说一句更新文档就全面检查） |
| **系统资产分级与上下文预算** | `.devin/rules/six-asset-grading.md` | **always-on——设计或修改AI Agent的AGENTS.md内容时；设计或修改提示词文件时；向AI Agent发送直接提示词时；向system/添加新的资产文件时** | 用户原话（AGENTS.md和可复用提示词是system资产，题目解答放文件中，大块要求放文件中，直接提示词不大块，分类学资产从AGENTS.md拆分到单独文件，单文件300行限制，超长检测+警报） |
| **系统测试规矩** | `.devin/rules/six-test-discipline.md` | **always-on——为系统模块编写测试、POC验证、回归验证时；在`system/tests/`下创建测试资产时；架构改动后需要验证不退化时** | 用户原话（测试不是用完就扔的临时文件，方案先行、按模块组织、内容全留存） |
| **文件拆分流程控制** | `.devin/rules/six-file-staged-flow.md` | **always-on——设计提示词时，当一个AI session的工作流程有多个阶段且thinking可能过大时** | 用户原话（335号V8改进为例） |
| **运行数字ID命名规范** | `.devin/rules/six-run-id-naming.md` | **always-on——任何系统运行、测试、实验、审计存档时** | 用户原话（数字ID是可查可审计的保证，应该在任何它应该出现的地方出现） |
| **数据库-文件双向可追溯性** | `.devin/rules/db-file-traceability.md` + `~/.config/devin/skills/db-file-traceability/SKILL.md` | **always-on——任何向数据库写入记录且同时产出物理文件时；声称"数据已入库"或"文件已落盘"前** | 用户原话（数据库和数据任何时候都可以被"顺藤摸瓜"，要做成AI的工作意识。362号验证发现3个gap后修复） |
| **研发资产管理** | `.devin/rules/six-asset-management.md` | **always-on——运行vein_analysis_three_phase()时；审计历史运行时；从数据库run_id查找运行资产时** | 339号方案（run_manifest.json+自动归档+目录命名规范+数据库字段，回头审计从5步缩减到3步且确定性） |
| **代码修改后同步更新文档** | `.devin/rules/code-doc-sync.md` | **always-on——修改了错题分析系统或解题系统的代码逻辑后** | 用户原话（代码修改和文档更新必须在同一个commit中完成。不允许"先提交代码，文档以后再补"——以后永远不会补） |

**第六代研发的核心方向**（截至2026-08-10）：
1. 非局部tell（303/305号）——tell不只在卡点，可以在脉络上任意点或跨多节点范围
2. FCA数学基础（304号）——形式概念分析为三层Pipe架构提供完备性证明和系统化格遍历算法
3. 并发Telling AI（311号）——Pipe 2从单AI串行变为多AI并行，每个Telling AI负责一个tell分区
4. Pipe 0简化（311号）——从精确拓扑化（8种组合+手工信号词）降级为粗domain分类
5. trace/tell/hint命名（309号）——trace=辅助AI识别产物，tell=库中标准化描述，hint=方向提示
6. Parser AI统一（315/318号）——分析AI和Parser AI统一为Parser AI，在过程A和过程B中都用同一套核心能力（提取格化全Level Trace）
7. 脉络分析管线（315/316号）——过程A和过程B共用步骤1-4，只在步骤5分叉
8. 四个Pipe命名（318/319号）——Solver AI/Parser AI/Telling AI/Guide AI

**已识别的跑偏方向**（310号评审结论）：
- 307号原语化——破坏推理AI独立性，拒绝"必须原语化"，保留"可选优化"定位
- 309号"范式转变"原主张——Pipe 0/1/2融合成一次分析在大规模下不成立；但用户后续提出的"分区后并发Telling AI"是Pipe 2并行化，不跑偏

---

