---
description: >
  批次todo list铁律：每批次处理FATE-X问题时，Master Agent必须用todo_write工具
  精确构建7步todo list，步骤名称和顺序固定不变。
  WHEN to use: 题海梳理工作线中每批次subagent派发+审计时。
  WHEN NOT to use: 非批次处理、单题分析、非题海梳理任务。
trigger: model_decision
---

# 批次todo list铁律

## 核心规则

**每批次（3个subagent一组）处理FATE-X问题时，Master Agent必须用`todo_write`工具精确构建以下7步todo list，步骤名称和顺序固定不变。**

## 7步todo list模板

每批次启动时，立即用`todo_write`写入以下7项（`{N}`替换为批次号，如`33b`）：

```
1. [x] 第{N-1}批3个完整审计落盘（seq {prev_seq_range}）  [completed]
2. [ ] 第{N}批·步骤1：领取seq {seq_range}并准备problem.lean+checklist  [in_progress]
3. [ ] 第{N}批·步骤2：并发启动3个subagent（{pid1}/{pid2}/{pid3}）  [pending]
4. [ ] 第{N}批·步骤3：等待3个subagent完成+逐个格式检查  [pending]
5. [ ] 第{N}批·步骤4：读题目+profile关键内容做数学内容审查  [pending]
6. [ ] 第{N}批·步骤5：写3个audit-checklist.md  [pending]
7. [ ] 第{N}批·步骤6：更新review-log.md  [pending]
8. [ ] 第{N}批·步骤7：git commit  [pending]
9. [ ] 持续批次运行直到Tier 1处理完（并发3个一组）  [pending]
```

**注意**：第1项是上一批的收尾（标记completed），第9项是持续运行的总目标（始终pending）。第2-8项是当前批次的7步。

## 7步详细说明

### 步骤1：领取题目+准备文件
- 从ArangoDB `problem_extraction_progress`查`extraction_status="pending"`且`difficulty_tier==1`的题，按`global_sequence`排序，LIMIT 3
- 为每道题写`problem.lean`文件（从FATE-X batch JSON提取informal_statement+formal_statement）
- 用`scripts/prepare_subagent_dir.py`生成`checklist.md`
- 完成后标记步骤1为completed，步骤2为in_progress

### 步骤2：并发启动3个subagent
- 用`run_subagent`（is_background=true, profile=subagent_general）同时启动3个subagent
- 每个subagent的task中包含：题目文件路径、checklist.md路径、ArangoDB连接信息、progress记录_key、profile的_key
- 3个subagent必须在一个message中并行启动（不是顺序启动）
- 完成后标记步骤2为completed，步骤3为in_progress

### 步骤3：等待3个subagent完成+逐个格式检查
- 每收到一个`<subagent_completion_notification>`，立即对该profile做格式检查：
  - situation_type是否全规范（6个值之一）
  - hint_level是否全0-1浮点数
  - per-pair拓扑字段（tell_topology + tell_small_concepts）是否全存在
  - global pair的why_not_visible_locally是否非None
  - answer是否非None
  - stats中knowledge_bottleneck和thinking_bottleneck是否字符串类型
- 3个全部完成后标记步骤3为completed，步骤4为in_progress

### 步骤4：读题目+profile关键内容做数学内容审查
- 用read工具读3个`problem.lean`文件
- 用exec执行Python脚本从ArangoDB读3个profile的关键内容（answer/problem_type/solution_method_type/key_insight/逐轮QA/stats）
- Master Agent亲自理解每道题的数学内容和解答核心思路
- 完成后标记步骤4为completed，步骤5为in_progress

### 步骤5：写3个audit-checklist.md
- 为每个profile写完整的`subagents-dirs/{problem_id}/audit-checklist.md`
- 按audit-checklist-template.md的6-Phase结构（Phase 0-6）逐项填写
- 3个文件用write工具在一个message中并行写入
- 完成后标记步骤5为completed，步骤6为in_progress

### 步骤6：更新review-log.md
- 在`subagents-dirs/review-log.md`末尾追加本批次记录
- 包含：批次范围、累计完成数、审计方式、并发数、备注、审计结果表格、审计结果摘要、本批特点、数学内容审查结论
- 用edit工具追加（old_string匹配末尾内容，new_string在末尾追加新批次块）
- 完成后标记步骤6为completed，步骤7为in_progress

### 步骤7：git commit
- `git add`本批的6个文件（3个problem.lean + 3个audit-checklist.md）+ review-log.md
- `git commit`用heredoc格式，commit message包含批次号、seq范围、主题、审计结果、累计完成数
- commit message末尾包含Devin Co-Authored-By标记
- 完成后标记步骤7为completed，步骤1（下一批）为in_progress

## 禁止的行为

1. **禁止跳过任何步骤**——7步必须全部执行，不允许合并、不允许跳过
2. **禁止改变步骤顺序**——步骤1→2→3→4→5→6→7的顺序固定不变
3. **禁止改变步骤名称**——步骤名称是固定的，不允许自创名称
4. **禁止不更新todo list**——每完成一步立即用`todo_write`更新对应项的状态
5. **禁止用粗粒度todo list**——如"发起批次"和"审计批次"两个大项是不允许的，必须用7步细粒度

## 为什么

- **7步是完整流程的最小拆分**——每步是一个独立的、可验证的工作单元
- **细粒度todo list给用户可见性**——用户随时知道当前在7步中的哪一步
- **固定步骤名称确保跨批次一致性**——每批次的todo list结构完全相同，便于追踪和审计
- **todo list是Master Agent的自我约束**——防止跳步、防止粗审、防止忘记commit

## 适用于

- 题海梳理与数据基座建设工作线（AGENTS.md §当前工作线：题海梳理与数据基座建设）
- 所有FATE-X问题的批次处理（3个subagent一组）
- Pass 1（探索性·发现维度）和 Pass 2（穷举性·完整标注）都适用

## 与其他规则的关系

- `extraction-subagent-pipeline.md`：定义并发约束（最多5个subagent）——本规则定义todo list结构
- `subagent-output-audit.md`：定义审计checklist的6-Phase内容——本规则定义审计在7步中的位置（步骤3-5）
- AGENTS.md §Master Agent审查SOP：定义审计深度要求——本规则定义审计流程的todo list落地
