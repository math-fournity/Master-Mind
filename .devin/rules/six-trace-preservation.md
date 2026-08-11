# 运行痕迹全程保留规则

**触发条件**：设计或实现系统的任何运行阶段、阶段间数据传递、AI实例启动、数据库写入时。always-on——任何涉及系统运行逻辑的设计和实现都必须同时考虑痕迹保留。

## 核心约束

**系统的运行过程要全程保留所有"痕迹"用于未来的审计和调试。系统设计必须既要考虑运行逻辑，也要考虑痕迹保留。**

"痕迹"指系统运行过程中产生的所有中间产物和元数据，包括但不限于：
- 每个AI实例的完整输入（提示词、脉络文本、方向提示）
- 每个AI实例的完整输出（thinking、trajectory、结构化JSON、自由文本）
- 阶段间传递的数据包（AnalysisInput/AnalysisOutput/MatchInput/MatchOutput等）
- 程序验证的输入和报告（verify_lattice_completeness.py的审计报告）
- AI实例的启动参数（用了哪个提示词版本、工作目录、启动时间、结束时间）
- 循环每轮的状态快照（引导树的节点和边、tell库的变更）

## 痕迹保留的两个维度

### 1. 不可丢弃——所有中间产物必须落盘

系统运行中的每个中间产物都必须落盘到文件或数据库，不可只在内存中传递后丢弃。

**反模式**：vein_analysis()产出的AnalysisOutput只在内存中传给trace_match()，没有落盘。如果后续发现trace匹配有问题，无法回溯脉络分析阶段AI到底产出了什么。

**正确模式**：vein_analysis()产出的AnalysisOutput同时落盘到`palyground/{process}/vein_analysis/{problem_id}/output.json`，内存中传递的只是落盘文件的引用或副本。

### 2. 可追溯——每个产物都能追溯到产生它的上下文

每个落盘的产物必须能追溯到：
- 哪个AI实例产出的（ai_id）
- 用哪个提示词版本跑的（V5/V7/V8/V9）
- 在哪个会话中（session_id）
- 输入是什么（输入文件的路径或内容hash）
- 什么时候产出的（时间戳）

**反模式**：output.json只存了AI的产出，没存AI的启动参数。审计时无法知道这个产出是V9还是V5跑出来的。

**正确模式**：output.json包含元数据节——`{"_meta": {"ai_id": "...", "prompt_version": "V9", "session_id": "...", "started_at": "...", "completed_at": "..."}, "payload": {...}}`。

## 在系统设计中的落实

### 阶段函数的痕迹保留要求

每个阶段函数（vein_analysis/trace_match/direction_extract/guide_expand/knowledge_deposit等）在实现时必须：

1. **输入落盘**——把传给AI的完整提示词落盘到工作目录的`input.md`或`input.json`
2. **输出落盘**——把AI的完整产出落盘到工作目录的`output.md`或`output.json`
3. **元数据记录**——在输出文件中记录AI实例ID、提示词版本、时间戳
4. **程序验证报告落盘**——如果有程序验证（如verify_lattice_completeness.py），验证报告也落盘

### 4并发方案的痕迹保留

4并发（V5/V7/V8/V9）中每个版本的产出必须分别落盘到各自的工作目录：
- `palyground/{process}/vein_analysis/{problem_id}/V5/output.json`
- `palyground/{process}/vein_analysis/{problem_id}/V7/output.json`
- `palyground/{process}/vein_analysis/{problem_id}/V8/output.json`
- `palyground/{process}/vein_analysis/{problem_id}/V9/output.json`

合并后的trace并集也要落盘：
- `palyground/{process}/vein_analysis/{problem_id}/merged_traces.json`

程序验证报告落盘到：
- `palyground/{process}/vein_analysis/{problem_id}/audit_report.json`

### 数据库记录

sessions表记录每次会话。后续应增加的表（db_schema.py的TODO中已列出）：
- ai_instances表——每个AI实例的启动参数和产出路径
- orphan_traces表——孤悬trace存档
- tell_library_changes表——tell库变更日志

这些表不是可选的——它们是痕迹保留的数据库层面保障。

## 为什么痕迹保留和运行逻辑同等重要

1. **审计**——系统产出了某个结果（新tell/引导树某条路径成功），需要回溯是哪个AI在什么条件下产出的。没有痕迹就无法审计。
2. **调试**——系统某个阶段出了问题（trace匹配失败/引导树没生长），需要看每个阶段的输入输出。没有痕迹就只能重跑。
3. **迭代**——改进某个阶段的提示词或逻辑时，需要对比改进前后的产出。没有痕迹就没有对比基准。
4. **研究**——系统的运行数据本身是研究材料（哪些trace被频繁识别/哪些tell被频繁匹配/哪些方向经常失败）。没有痕迹就没有研究素材。

## 和其他规则的关系

- 和`system-ref-sync.md`的关系：.ref文件是文档层面的痕迹保留——记录"理解这个模块需要参考哪些文档"。本规则是运行层面的痕迹保留——记录"系统运行时产生了什么"。
- 和`six-mechanization-reference.md`的关系：程序验证（verify_lattice_completeness.py）的审计报告是痕迹的一种。本规则要求审计报告也落盘。
- 和`grove-core-loop.md`的关系：AGENTS.md中的"可审计性纪律"（重大分析必须留下file:line定位+理解性产物）是本规则在Master Agent行为层面的体现。本规则是系统代码层面的体现。
