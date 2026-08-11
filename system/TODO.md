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

### TODO-4: vein_analysis()的执行方式——编排描述还是可执行代码 [高优先级] ✅已解决

**来源**：vein_analysis实现方案讨论（2026-08-10）

**问题**：vein_analysis()需要启动4个AI Agent（V5/V7/V8/V9）。按AI Agent启动规范rule，AI Agent通过tmux启动，启动前要准备AGENTS.md/prompt.md/input.md。这些"准备文件+启动tmux+等待+收集产出"的动作，是写在Python代码里自动执行，还是由Master Agent手动执行？

**解决**：选b——可执行代码。vein_analysis()函数自动执行全部流程：准备工作目录→subprocess启动4个tmux session→轮询等待4个AI完成→收集产出→合并trace→返回AnalysisOutput。这和2026-08-11认知转变"系统就是脚本，你是检查者和开发者"一致。

**认知转变**：2026-08-11，从"系统就是你，不是脚本"（选a）变为"系统就是脚本"（选b）。理由：第六代系统把判断力编码进了提示词和程序验证，脚本可以执行；4并发手动执行效率太低；Master Agent的时间应该花在开发代码和审计运行上。

**实现**：system/vein_analysis.py已实现，2026-08-11。

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

---

## 资产分级与上下文预算相关

### TODO-13: file_size_monitor.py未实现——资产文件超长检测 [中优先级]

**来源**：six-asset-grading.md rule + 用户要求（2026-08-11）

**问题**：系统资产分级rule要求单个资产文件限制在300行左右。超长文件需要脚本检测并发出警报。file_size_monitor.py尚未实现。

**需要实现**：
- `check_file_size(file_path)`——检查单个文件是否超长（行数>300或字符数>9000）
- `scan_asset_files(asset_dirs)`——扫描所有资产文件，返回超长文件列表
- 把超长文件警报写入数据库alerts表（TODO-14）
- 受检测的文件类型：.md/.txt（资产文件）；不受限制：input.md（题目解答文本）、.py（代码文件）

**资产目录**：
- `第六代系统提示词积累目录/`——提示词文件
- `taxonomy/`——分类学识别资产文件（TODO-15拆分后）
- AI Agent工作目录中的AGENTS.md——实例运行版AGENTS.md

---

### TODO-14: alerts表未定义 [中优先级]

**来源**：six-asset-grading.md rule + 用户要求（2026-08-11）

**问题**：db_schema.py中alerts表未定义。文件超长检测（TODO-13）和其他系统警报需要写入alerts表，后续检查的AI可以看到。

**需要定义的字段**：alert_id, alert_type("file_overlong"/"runtime_error"/"trace_anomaly"等), file_path（如适用）, lines, chars, severity("warning"/"error"), detected_at, resolved_at, resolved_by, detail

**和其他表的关系**：alerts表和ai_instances表（TODO-6）一样，是系统运行健康监控的数据库层面保障。alerts表是"代码检查"的一部分——脚本自动检测并写入警报，AI后续检查时读取。

---

### TODO-15: Tell分类学Schema从AGENTS.md拆分到单独文件 [中优先级]

**来源**：six-asset-grading.md rule + 用户要求（2026-08-11）

**问题**：AGENTS.md中的"Tell分类学Schema"节（第913-993行，约80行）放在项目AGENTS.md中。随着分类学增长，这个节会越来越长，污染AGENTS.md。按资产分级rule，分类学识别资产应该从AGENTS.md拆分到单独文件中。

**需要做**：
1. 创建`taxonomy/`目录
2. 把AGENTS.md中"Tell分类学Schema"节的内容拆分到`taxonomy/schema.md`（分类学结构定义）和按domain拆分的文件（如`taxonomy/domain_algebra.md`等）
3. 每个文件限制在300行左右
4. AGENTS.md中只保留"必须加载的分类学文件清单"——不保留分类学内容本身
5. 更新`.devin/rules/tell-taxonomy-schema-maintenance.md`——维护规则改为维护taxonomy/目录下的文件，而不是AGENTS.md中的Schema节

**注意**：这个TODO涉及修改AGENTS.md的核心内容，需要谨慎执行——确保拆分后AI仍然能通过"必须加载的文件清单"找到分类学知识。
