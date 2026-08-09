---
description: >
  subagent产出审计铁律：必须严格按照audit-checklist-template.md逐项审计subagent的工作成果。
  WHEN to use: 每批subagent完成后、逐个审计profile时。
  WHEN NOT to use: 系统模块代码审计（用audit-trigger.md）、非profile审计任务。
trigger: model_decision
---

# subagent产出审计铁律

## 核心规则

**审计subagent产出的profile时，必须严格按照`subagents-dirs/audit-checklist-template.md`文件给出的要求，逐项审计、检查，不允许跳过任何一项。**

## 审计流程

### 1. 加载审计模板

每次审计从一张干净的`audit-checklist-template.md`模板开始，填充占位符，生成`subagents-dirs/{problem_id}/audit-checklist.md`。

### 2. 逐项执行（不允许跳过）

**Phase 0: 加载审计材料**（4项）
- 0a. 从ArangoDB读取完整profile
- 0b. 用read工具读取题目Lean文件，亲自理解题目和解答
- 0c. 读取subagent的checklist.md
- 0d. 读取subagent的profile.json，与数据库中的profile对比

**Phase 1: 格式检查**（5项）
- 1a. situation_type值规范
- 1b. hint_level格式
- 1c. per-pair拓扑字段存在性
- 1d. 必填字段完整性（对照Schema v3字段清单逐项检查）
- 1e. QA序列结构

**Phase 2: 数学内容审查**（16项，核心审计）
- 2a. 题目理解准确性——对比subagent的problem_text和自己读Lean文件的理解
- 2b. 解答理解准确性——对比solution_text/solution_summary和自己读Lean文件的理解
- 2c. solution_method_type vs problem_type区分
- 2d. key_insight准确性——自己判断"啊哈时刻"在哪里，对比subagent的key_insight
- 2e. QA序列合理性——**逐轮审查**，对每一轮单独填写situation_type/question/level/遗漏的判断
- 2f. 局部(tell,hint)对质量——**逐对审查**tell和hint是否具体、是否对应QA序列
- 2g. 全局(tell,hint)对质量——**逐对审查**path_feature型和implicit型
- 2h. 拓扑标注准确性——对比自己的判断
- 2i. bare_ai_error_prediction具体性
- 2j. thinking_patterns和knowledge_required
- 2k. translation分析
- 2l. structure_features和key_objects
- 2m. expected_ai_method和correct_method
- 2n. bare_ai_expected和实验适用性
- 2o. answer和answer_type
- 2p. analysis_metadata

**Phase 3: 拓扑分类体系审查**（3项）
- 3a. 拓扑值粒度一致性
- 3b. 是否需要新增拓扑值
- 3c. 拓扑进化建议评估

**Phase 4: 超大规模前瞻审查**（3项）
- 4a. (tell,hint)对的检索有效性
- 4b. Schema扩展性
- 4c. AI数学系统有效性

**Phase 5: 审计结论**（4项）
- 5a. 总体判断（合格/小问题/大问题）
- 5b. 大问题处理（如适用）
- 5c. 流程改进（如适用）
- 5d. 审计记录到review-log.md

**Phase 6: 元审查**（7项）
- 6a. 本审计checklist自身的完备性
- 6b. 本审计checklist自身的合理性
- 6c. 数据库表设计是否需要改进
- 6d. subagent用的checklist.md是否需要改进
- 6e. AGENTS.md中的SOP是否需要改进
- 6f. subagent的每一个工作项目是否需要反思
- 6g. 改进落实

### 3. 审计产出落盘

每个审计过的profile必须有`subagents-dirs/{problem_id}/audit-checklist.md`，记录逐项检查结果。

### 4. 审计员签字

审计checklist末尾有"审计员签字"确认区，必须确认所有Phase的所有项目都已check完才能提交审计结论。

## 禁止的行为

1. **禁止跳过任何Phase或任何项**——Phase 0到Phase 6的每一项都要实际执行
2. **禁止用批量脚本替代逐项审查**——批量脚本只能做Phase 1格式检查，Phase 2-6必须逐项人工审查
3. **禁止只读key_insight就判"合格"**——必须完成Phase 2的16项，特别是2e（QA序列逐轮审查）和2f/2g（逐对审查tell/hint质量）
4. **禁止粗审冒充审计**——只检查格式+高层读key_insight是粗审，不是审计
5. **禁止不落盘**——审计产出必须写入`subagents-dirs/{problem_id}/audit-checklist.md`

## 与AGENTS.md的关系

本规则是AGENTS.md中"检查点1：每批5道subagent全部完成后——逐个完整审计"的具体执行规范。AGENTS.md定义了"什么时候审计"，本规则定义了"怎么审计"。
