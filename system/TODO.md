# system/ TODO

> 本文件记录system/目录下代码实现过程中发现的待办事项。
> 每条TODO标注来源（哪个讨论/哪个文件发现的）和优先级。

---

## 脉络分析阶段（vein_analysis）

### TODO-1: solve模式的提示词未设计 [高优先级]

**来源**：vein_analysis实现方案讨论（2026-08-10）

**问题**：V5-V9全部是absorb模式提示词——分析完整解答文本，线性脉络。solve模式（从推理AI的thinking分析脉络，可能有分叉，树/DAG结构）的提示词从未设计过。

**影响**：vein_analysis()函数签名支持`process="solve"`和`process="absorb"`两种模式，但只有absorb模式有验证过的提示词。solve模式调用时无提示词可用。

**选项**：
- a) 基于V9提示词设计solve模式变体——在V9基础上加分支处理段（如何从thinking中识别分叉位置、如何处理树/DAG结构的格化）
- b) 先只实现absorb模式，solve模式留NotImplementedError，等解题引导阶段实现时再设计
- c) solve和absorb共用V9提示词，先简化忽略分支（thinking也当线性脉络处理）

**建议**：选b——先把absorb模式（入题）跑通，因为absorb有完整的POC验证（VMS-28c/28d/28e）。solve模式的提示词设计需要新的POC验证，等absorb模式系统跑通后再做。

---

### TODO-2: V5提示词没有结构化JSON输出要求 [中优先级]

**来源**：vein_analysis实现方案讨论（2026-08-10）

**问题**：4并发方案中V5是自由直觉提示词，没有JSON schema要求（V7才加的）。V5产出的是自由文本（vms28b_v5_output.md那种），不是结构化JSON。4并发合并trace时，V5的产出需要单独解析。

**影响**：vein_analysis()的4并发合并逻辑中，V7/V8/V9的产出可以直接用JSON解析，V5不行。

**选项**：
- a) 给V5加一个轻量JSON包装要求——在V5提示词末尾加"最后把所有trace列成JSON"，不改V5的核心分析逻辑
- b) V5产出自由文本，用另一个AI解析成JSON（增加成本和复杂度）
- c) V5产出自由文本，用正则/规则解析（脆弱，不推荐）
- d) 4并发降为3并发（V7/V8/V9），放弃V5的独有发现（"归纳递降三种方式"）

**建议**：选a——给V5加轻量JSON包装。V5的独有发现（归纳递降三种方式）有价值，不应该放弃。加JSON包装不改V5的核心分析逻辑，只在末尾加一个结构化输出要求。

---

### TODO-3: schema.py的Trace缺V9产出的字段 [中优先级]

**来源**：vein_analysis实现方案讨论（2026-08-10）

**问题**：当前schema.py的Trace有：trace_id, level, trace_type, pattern_description, source_segment_ids, is_branch_position。

V9产出的trace还有以下字段：
- `generalizable`（是否可泛化）——trace匹配阶段需要，决定trace是否值得去特化后存入tell库
- `closed_element_id`（关联的闭元素）——程序验证需要，关联trace和闭元素
- `meta_reflection`（是否元反思产出）——区分系统化步骤产出的trace和元反思产出的trace
- `reason_not_covered`（元反思未覆盖原因）——元反思trace的元信息，说明为什么系统化步骤没覆盖

**影响**：vein_analysis()解析V9 JSON产出时，这些字段无处可放。如果丢弃，trace匹配阶段缺少generalizable字段做判断，程序验证缺少closed_element_id做关联。

**选项**：
- a) 在Trace中加这4个字段（generalizable: bool, closed_element_id: Optional[str], meta_reflection: bool, reason_not_covered: Optional[str]）
- b) 不改Trace，把这些字段放在LevelView的view_features里
- c) 不改Trace，新建一个TraceExtension dataclass存放这些字段

**建议**：选a——直接在Trace中加。这些字段是V9验证过的必要信息，不是可选的。generalizable影响trace匹配阶段的行为，closed_element_id影响程序验证。技术行说明说"不要修改schema.py，如果觉得需要新增字段，先和项目负责人讨论"——这里需要讨论后决定。

---

### TODO-4: vein_analysis()的执行方式——编排描述还是可执行代码 [高优先级]

**来源**：vein_analysis实现方案讨论（2026-08-10）

**问题**：vein_analysis()需要启动4个AI Agent（V5/V7/V8/V9）。按AI Agent启动规范rule，AI Agent通过tmux启动，启动前要准备AGENTS.md/prompt.md/input.md。这些"准备文件+启动tmux+等待+收集产出"的动作，是写在Python代码里自动执行，还是由Master Agent手动执行？

**和AGENTS.md核心认知的关系**：AGENTS.md说"系统就是你，不是脚本"——辅助Pipe的采集、整理、检索、启动是Master Agent亲手做的动作，不是脚本替你做的。如果vein_analysis()写成自动执行的Python代码（subprocess启动tmux），就违反了这个原则。

**选项**：
- a) vein_analysis()是"编排描述+产出解析"——函数定义清楚要准备什么文件、启动几个tmux、怎么合并产出，但实际启动动作由Master Agent执行。函数被调用时返回一个"执行计划"，Master Agent按计划执行后把产出喂回函数做解析
- b) vein_analysis()是可执行代码——用subprocess自动启动tmux、自动等待、自动收集产出。违反"系统就是你"原则但效率高
- c) vein_analysis()是混合模式——文件准备和产出解析在代码中，tmux启动由Master Agent手动执行

**建议**：选a——和AGENTS.md核心认知一致。vein_analysis()定义编排逻辑和产出解析逻辑，Master Agent按编排执行启动动作。这也和痕迹保留rule一致——每一步都有人检查，不是脚本黑箱。

---

### TODO-5: 4并发trace并集的去重逻辑 [中优先级]

**来源**：4并发方案设计（技术说明书06-五代继承/02-第六代的独特贡献.md）

**问题**：4并发中V5/V7/V8/V9各自产出trace，合并时需要去重。技术说明书中定义的去重规则是"段集合Jaccard≥0.8且描述思维模式相同→去重，保留更完整的描述"。但"描述思维模式相同"是语义判断，需要AI来做，不能用代码规则做。

**影响**：vein_analysis()的合并逻辑中，trace去重这一步需要调用AI做语义判断。

**选项**：
- a) 用一个专门的"去重AI"做语义判断——输入4版本的trace列表，输出去重后的trace列表
- b) 用embedding相似度做初筛，相似度高的再人工判断
- c) 不做自动去重，4版本trace全部保留，让trace_match阶段处理重复（trace_match匹配tell时自然去重——同一个tell被多个trace匹配只取一次）

**建议**：选c——不在脉络分析阶段做去重，让trace_match阶段自然去重。理由：去重本身需要语义判断（成本高且可能出错），而trace_match阶段匹配tell时自然会处理重复（多个trace匹配同一个tell只取一次匹配结果）。脉络分析阶段的职责是"发现trace"，不是"去重trace"。

---

## 数据库相关

### TODO-6: ai_instances表未定义 [中优先级]

**来源**：db_schema.py的TODO区 + 痕迹保留rule

**问题**：db_schema.py中ai_instances表只有TODO注释，没有实际定义。痕迹保留rule要求"每个AI实例的启动参数和产出路径"必须记录。

**需要定义的字段**：ai_id, session_id, ai_role(solver/parser/telling/guide), prompt_version(V5/V7/V8/V9等), working_directory, started_at, completed_at, input_path, output_path

---

### TODO-7: orphan_traces表未定义 [中优先级]

**来源**：db_schema.py的TODO区 + 痕迹保留rule

**问题**：db_schema.py中orphan_traces表只有TODO注释。孤悬trace存档是解题引导→解答吸收闭环的关键环节。

**需要定义的字段**：trace_id, problem_id, session_id, trace_type, level, pattern_description, source_segment_ids, archived_at, consumed_by_session_id

---

### TODO-8: tell_library_changes表未定义 [低优先级]

**来源**：db_schema.py的TODO区 + 痕迹保留rule

**问题**：db_schema.py中tell_library_changes表只有TODO注释。tell库变更日志用于审计tell库的增长历史。

**需要定义的字段**：change_id, change_type(add/modify), tell_id, session_id, changed_at, change_detail

---

## 入口相关

### TODO-9: load_solution_records()未实现 [高优先级]

**来源**：system/enter.py

**问题**：enter.py中的load_solution_records()是占位（raise NotImplementedError）。入题入口需要从文件/目录加载解答记录。

**需要定义**：解答记录的JSON格式（problem_id, problem_text, solution_text, is_verified等字段对应SolutionRecord dataclass）

---

### TODO-10: load_problem()未实现 [高优先级]

**来源**：system/solve.py

**问题**：solve.py中的load_problem()是占位（raise NotImplementedError）。解题入口需要从文件加载题目。

**需要定义**：题目的JSON格式（problem_id, problem_text, domain, answer等字段对应Problem dataclass）

---

## 阶段函数占位

### TODO-11: process_solve.py中的阶段函数全部是占位 [待定优先级]

**来源**：system/process_solve.py

**问题**：inference_explore/trace_match/direction_extract/guide_expand/archive_orphan_traces全部是raise NotImplementedError。这些是解题引导循环的5个阶段。

**注意**：vein_analysis占位函数将被替换为从vein_analysis.py导入（TODO-4解决后）。其他4个阶段函数待各自阶段实现时再做。

---

### TODO-12: process_absorb.py中的阶段函数全部是占位 [待定优先级]

**来源**：system/process_absorb.py

**问题**：trace_match/knowledge_deposit/get_archived_orphan_traces/save_tell_to_library全部是raise NotImplementedError。这些是解答吸收的4个阶段。

**注意**：vein_analysis占位函数将被替换为从vein_analysis.py导入（TODO-4解决后）。其他3个阶段函数待各自阶段实现时再做。trace_match和process_solve.py的trace_match是同一个函数（两个过程共享）。
