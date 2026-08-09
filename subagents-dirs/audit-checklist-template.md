# Master Agent 审计 Checklist

> **这是你的审计工作清单。每次审计一个subagent的产出时，从这张干净的模板开始。全文加载，逐项检查，每完成一项把 `[ ]` 改为 `[x]` 并填写审计结论。所有项目必须全部check完，不允许跳过任何一项。**

## 审计对象

- **problem_id**: {{PROBLEM_ID}}
- **subagent ID**: {{SUBAGENT_ID}}
- **审计时间**: {{AUDIT_TIME}}
- **profile_doc_id**: problem_profiles/{{PROBLEM_ID}}

---

## Phase 0: 加载审计材料 [ ]

**操作**：加载以下材料，全部读完后再开始逐项审计

- [ ] 0a. 从ArangoDB读取完整profile（`problem_profiles/{{PROBLEM_ID}}`）
- [ ] 0b. 用read工具读取题目Lean文件（`{{FILE_PATH}}`），亲自理解题目和解答
- [ ] 0c. 读取subagent的checklist.md（`subagents-dirs/{{PROBLEM_ID}}/checklist.md`），看subagent每步的完成情况
- [ ] 0d. 读取subagent的profile.json（`subagents-dirs/{{PROBLEM_ID}}/profile.json`），与数据库中的profile对比是否一致

**审计前提确认**：
- 我已经读完题目和解答，理解了这道题在数学上是什么：
- 我已经自己思考过"如果我是AI会怎么解、会在哪里走错"：
- 我现在可以开始对比subagent的分析了：

---

## Phase 1: 格式检查（最低线，必须全部通过） [ ]

### 1a. situation_type值规范 [ ]
- [ ] 检查所有tell_hint_pairs的situation_type值是否都是6个规范值之一（纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导）
- [ ] 如果有非规范值，列出：
- **结论**：✅ 全部规范 / ❌ 有N个非规范值

### 1b. hint_level格式 [ ]
- [ ] 检查所有tell_hint_pairs和global_tell_hint_pairs的hint_level是否是0-1浮点数
- [ ] 如果有非0-1值，列出：
- **结论**：✅ 全部规范 / ❌ 有N个非规范值

### 1c. per-pair拓扑字段存在性 [ ]
- [ ] 检查所有tell_hint_pairs是否包含tell_topology字段
- [ ] 检查所有tell_hint_pairs是否包含tell_small_concepts字段
- [ ] 检查所有global_tell_hint_pairs是否包含tell_topology字段
- [ ] 检查所有global_tell_hint_pairs是否包含tell_small_concepts字段
- **结论**：✅ 全部存在 / ❌ 缺失N个字段

### 1d. 必填字段完整性 [ ]
- [ ] 逐项检查profile是否包含所有必填字段（对照Schema v3的字段清单）：
  - _key, source_id, source_dataset, schema_version
  - problem_text, solution_text, solution_summary
  - domain, subfield, answer_type, answer
  - problem_type, solution_method_type, structure_features, key_objects
  - thinking_patterns, primary_pattern, knowledge_required, key_insight
  - translation_from, translation_to, translation_type
  - tell_topology, tell_small_concepts, expected_ai_method, correct_method
  - tell_hint_pairs, global_tell_hint_pairs
  - bare_ai_expected, bare_ai_error_prediction, suitable_for_poc, discriminates_levels
  - qa_sequence (含rounds和stats)
  - analysis_metadata
- [ ] 列出缺失的字段（如有）：
- **结论**：✅ 全部完整 / ❌ 缺失N个字段

### 1e. QA序列结构 [ ]
- [ ] qa_sequence.rounds是数组，每个元素含round/question/expected_answer/situation_type/level
- [ ] qa_sequence.stats含total_rounds/metacognitive_rounds/knowledge_rounds/level_sum/knowledge_bottleneck/thinking_bottleneck
- [ ] QA轮数在5-8之间
- **结论**：✅ 结构正确 / ❌ 问题描述

---

## Phase 2: 数学内容审查（核心审计，不惜代价） [ ]

### 2a. 题目理解准确性 [ ]
**操作**：对比subagent的problem_text和你自己读Lean文件的理解
- [ ] subagent的problem_text是否准确概括了题目（没有遗漏关键条件、没有添加题目没有的条件）？
- [ ] 如果不准确，具体问题是什么：
- **结论**：✅ 准确 / ❌ 问题描述

### 2b. 解答理解准确性 [ ]
**操作**：对比subagent的solution_text/solution_summary和你自己读Lean文件的理解
- [ ] subagent的solution_text是否准确概括了解答的核心步骤？
- [ ] subagent的solution_summary是否是1-2句话的准确概括？
- [ ] 如果不准确，具体问题是什么：
- **结论**：✅ 准确 / ❌ 问题描述

### 2c. solution_method_type vs problem_type区分 [ ]
- [ ] problem_type描述的是题目结构类型（不是解法）
- [ ] solution_method_type描述的是解答方法类型（不是题目结构）
- [ ] 两者是否明确区分？如果相同或混淆，具体问题是什么：
- **结论**：✅ 区分清晰 / ❌ 混淆

### 2d. key_insight准确性 [ ]
**操作**：你自己判断这道题的"啊哈时刻"在哪里，对比subagent的key_insight
- [ ] subagent的key_insight是否真的是解答中最关键的转折点？
- [ ] 还是只是随便找了一句话填上去？
- [ ] 如果不准确，你认为真正的key_insight是什么：
- **结论**：✅ 准确 / ❌ 不准确（真正的key_insight是：...）

### 2e. QA序列合理性 [ ]
**操作**：逐轮审查QA序列，判断是否真的能引导AI从题目走到解答

**逐轮审查**（对每一轮填写）：

**Round 1**:
- situation_type是否合理（第1轮通常应是纯元认知观察）：
- question(Q)是否真的对应了AI在这个位置需要的提示：
- expected_answer(A)是否是合理的预期回复：
- level值是否合理：
- 这轮是否遗漏了什么、或多余了什么：

**Round 2**:
- situation_type是否合理（第2轮通常应是自由列举）：
- question(Q)是否真的对应了AI在这个位置需要的提示：
- expected_answer(A)是否是合理的预期回复：
- level值是否合理：
- 这轮是否遗漏了什么、或多余了什么：

**Round 3**:
- situation_type是否合理（第3轮通常应是小尝试）：
- question(Q)是否真的对应了AI在这个位置需要的提示：
- expected_answer(A)是否是合理的预期回复：
- level值是否合理：
- 这轮是否遗漏了什么、或多余了什么：

**Round 4+**:
- （对剩余每轮重复上述审查）

**QA序列整体判断**：
- [ ] 整个QA序列真的能引导AI从题目走到解答吗？
- [ ] 有没有遗漏的关键步骤（从题目到解答之间的某个必要跳跃没有被任何一轮覆盖）？
- [ ] 有没有不必要的轮次（对引导没有贡献的轮次）？
- [ ] QA序列是机械走形式还是真实反映了引导过程？
- **结论**：✅ QA序列合理 / ❌ 问题描述

### 2f. 局部(tell, hint)对质量 [ ]
**操作**：逐对审查tell_hint_pairs

- [ ] 每个tell是否描述了AI在这个位置的具体状态/分叉信号？（不是泛泛而谈）
- [ ] 每个hint是否是具体的提示方向？（不是"继续努力"之类的废话）
- [ ] tell和hint是否真的对应了QA序列中那一轮的(状态, Q)？
- [ ] is_knowledge_bottleneck=True的pair，这轮是否真的是纯知识瓶颈（必须给知识性提示）？
- [ ] 列出有问题的pair（如有）：
- **结论**：✅ 质量合格 / ❌ N个pair有问题

### 2g. 全局(tell, hint)对质量 [ ]
**操作**：逐对审查global_tell_hint_pairs

- [ ] path_feature型的全局(tell,hint)是否真的总结了整条路径的特征？
- [ ] implicit型的全局(tell,hint)是否真的在某个Q位置看前后读出了AI的认知盲区？
- [ ] implicit型的why_not_visible_locally是否真的解释了为什么在局部不可见？（不是编了一个理由）
- [ ] generalizability的评估是否合理？
- [ ] 列出有问题的全局pair（如有）：
- **结论**：✅ 质量合格 / ❌ N个pair有问题

### 2h. 拓扑标注准确性 [ ]
**操作**：对比subagent的拓扑标注和你自己的判断

- [ ] profile级tell_topology的problem_type是否准确反映了题目的结构类型？
- [ ] profile级tell_topology的ai_method_type是否准确预测了bare AI会用的方法？
- [ ] profile级tell_topology的gap_type是否准确抓住了方法-问题不匹配的核心？
- [ ] per-pair tell_topology是否逐pair不同？（如果所有pair用同一个拓扑→分析太粗糙）
- [ ] per-pair tell_topology的值是否合理（不同轮次AI的状态确实对应不同的拓扑）？
- [ ] is_knowledge_bottleneck=True的pair，gap_type是否是knowledge_gap？
- [ ] tell_small_concepts是否是从题目和解答中实际出现的关键概念词？（不是随便编的）
- [ ] 列出有问题的拓扑标注（如有）：
- **结论**：✅ 拓扑标注准确 / ❌ 问题描述

### 2i. bare_ai_error_prediction具体性 [ ]
- [ ] bare_ai_error_prediction是否具体描述了bare AI会犯什么错？（不是只说"会失败"）
- [ ] 这个预测是否合理（你自己判断bare AI在这道题上会犯什么错）？
- [ ] 如果不合理，你认为bare AI会犯什么错：
- **结论**：✅ 具体且合理 / ❌ 太笼统或不准确

### 2j. thinking_patterns和knowledge_required [ ]
- [ ] thinking_patterns是否准确列出了解答中使用的思维模式？
- [ ] primary_pattern是否真的是主导思维模式？
- [ ] knowledge_required是否准确列出了解答所需的前置知识？
- [ ] 有没有遗漏的重要思维模式或知识？
- **结论**：✅ 准确 / ❌ 问题描述

### 2k. translation分析 [ ]
- [ ] translation_from是否准确描述了解答中"从什么方法翻译"？
- [ ] translation_to是否准确描述了"翻译到什么方法"？
- [ ] translation_type是否合理？
- [ ] 这个翻译是否真的是解答中的关键操作？
- **结论**：✅ 准确 / ❌ 问题描述

---

## Phase 3: 拓扑分类体系审查 [ ]

### 3a. 拓扑值粒度一致性 [ ]
- [ ] 这道题的problem_type值和已有值的粒度是否一致？（参考AGENTS.md拓扑分类体系节中标注✅的值作为粒度基准）
- [ ] ai_method_type值粒度是否一致？
- [ ] gap_type值粒度是否一致？
- [ ] 如果有粒度问题，具体是什么：
- **结论**：✅ 粒度一致 / ❌ 问题描述

### 3b. 是否需要新增拓扑值 [ ]
- [ ] 这道题是否使用了新建的拓扑值（不在已有值列表中）？
- [ ] 如果是，这个新值是否合理？是否应该归入已有的更抽象的类？
- **结论**：✅ 无新建值或新建值合理 / ❌ 新建值不合理，应归入...

### 3c. 拓扑进化建议评估 [ ]
- [ ] subagent是否提出了拓扑进化建议？
- [ ] 如果提出了，建议是否合理？
- [ ] 如果没提出，你自己是否发现了需要进化的地方？
- **结论**：（记录评估结果）

---

## Phase 4: 超大规模前瞻审查 [ ]

### 4a. (tell,hint)对的检索有效性 [ ]
- [ ] 这道题的(tell,hint)对在10万级数据基座中，能被Pipe 1通过拓扑匹配检索到吗？
- [ ] 如果拓扑太特殊（只有这道题有这个拓扑），Pipe 1会匹配不到→这个(tell,hint)对是孤岛
- [ ] 如果拓扑太通用（很多题都有这个拓扑），Pipe 1会匹配太多→需要Pipe 2用小概念分辨，小概念够用吗？
- **结论**：（记录评估结果）

### 4b. Schema扩展性 [ ]
- [ ] 这道题是否暴露了Schema中缺失的字段或类别？
- [ ] 如果要修改Schema，回补成本是否可控？
- **结论**：（记录评估结果）

### 4c. AI数学系统有效性 [ ]
- [ ] 这道题的(tell,hint)对在AI数学系统运行时真的会被检索到吗？
- [ ] 检索到后真的能帮AI找到正确方向吗？
- [ ] 如果答案是"不确定"或"不会"，原因是什么：
- **结论**：（记录评估结果）

---

## Phase 5: 审计结论 [ ]

### 5a. 总体判断 [ ]
- [ ] **合格**：分析质量合格，可以入库（或已入库无需修改）
- [ ] **小问题**：格式问题，用脚本批量修正即可
- [ ] **大问题——需立即干预**：QA序列/tell-hint对/拓扑标注有严重问题，需要重做

### 5b. 大问题处理（如适用） [ ]
- [ ] Master Agent自己重做了有问题的部分（具体重做了什么）：
- [ ] 发给另一个subagent重做（给的提示是什么）：
- [ ] **不允许**：标记"Pass 2重做"然后继续派发

### 5c. 流程改进（如适用） [ ]
- [ ] 这次审计发现了什么流程问题（checklist不够明确？SOP有盲区？Schema缺字段？）
- [ ] 需要更新什么文件（AGENTS.md / checklist-template.md / Schema）：
- [ ] 是否已经更新（如果是，commit hash）：

### 5d. 审计记录 [ ]
- [ ] 将本次审计结果记录到`subagents-dirs/review-log.md`

---

## ⚠️ 审计完成确认

**在提交审计结论前，必须确认**：
- [ ] Phase 0的所有材料已加载
- [ ] Phase 1的所有格式检查项已check
- [ ] Phase 2的所有数学内容审查项已check（2a-2k全部完成）
- [ ] Phase 3的拓扑分类体系审查已check
- [ ] Phase 4的超大规模前瞻审查已check
- [ ] Phase 5的审计结论已填写
- [ ] 审计结果已记录到review-log.md

**审计员签字**：我确认所有项目都已按照checklist要求检查完毕。
- 审计结论：______
- 日期：______
