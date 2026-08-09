# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_004127
- **文件路径**: subagents-dirs/omni_math_004127/problem.lean
- **来源**: omni_math
- **ArangoDB progress记录_key**: 334006（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_004127/problem.lean`

**产出**：
- 题目原文（数学描述）：Let n≥3 be a fixed integer. There are m≥n+1 beads on a circular necklace. You wish to paint the beads using n colors, such that among any n+1 consecutive beads every color appears at least once. Find the largest value of m for which this task is not possible.
- 解答核心思路（1-2句话）：通过gap分析，n+1窗口条件迫使每种颜色的间距≤n，因此每种颜色至少出现⌈m/n⌉次；求和得到m≥n·⌈m/n⌉，当m=n²-n-1时产生矛盾。m=n²-n时周期涂色c_i=i mod n可行。
- 解答关键步骤列表：
  1. 构造m=n²-n的可行涂色：c_i = i mod n（周期为n，n²-n整除n）
  2. 分析必要条件：n+1窗口含所有n色 → 同色间距≤n
  3. 计数论证：每种颜色至少⌈m/n⌉次 → 总数≥n·⌈m/n⌉
  4. 代入m=n²-n-1：⌈(n²-n-1)/n⌉=n-1 → 总数≥n(n-1)=n²-n>m，矛盾
  5. 结论：n²-n-1不可能，n²-n可能，答案为n²-n-1

---

## Step 2: QA序列分析——局部视角7步 [x]

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.2 | 描述题目结构：n+1窗口含所有n色意味着什么？ | n+1珠n色，鸽巢原理恰一色重复，其余各一次 |
| 2 | 自由列举 | 0.3 | 列出所有可能方法：构造、计数、鸽巢、间距分析 | 构造、计数/鸽巢、间距分析、模运算；证明不可能用(2)+(3) |
| 3 | 小尝试 | 0.4 | 试构造m=n²-n的涂色，再试m=n²-n-1 | n²-n：c_i=i mod n可行；n²-n-1：不整除n，构造失败 |
| 4 | 思维操作引导 | 0.6 | 从构造转向必要条件：同色最大间距是多少？ | 间距>n则存在n+1窗口缺该色，故间距≤n |
| 5 | 推进 | 0.5 | 间距≤n → 每色至少⌈m/n⌉次，继续推理 | 圆上m个位置分count个间距，每个≤n → count≥⌈m/n⌉ |
| 6 | 思维操作引导 | 0.7 | 求和n·⌈m/n⌉，代入m=n²-n-1，是否矛盾？ | ⌈(n²-n-1)/n⌉=n-1 → 总数≥n²-n>m=n²-n-1，矛盾 |
| 7 | 能量传递引导 | 0.8 | 验证m=n²-n可行，答案为n²-n-1 | n²-n整除n，周期涂色可行；答案n²-n-1 |

**统计**：
- total_rounds: 7
- metacognitive_rounds: 4（R1纯元认知观察 + R2自由列举 + R5推进 + R7能量传递引导）
- knowledge_rounds: 2（R4 + R6思维操作引导）
- level_sum: 3.5
- knowledge_bottleneck: R4（gap分析——从覆盖条件到间距约束的转换）
- thinking_bottleneck: R6（ceiling计数论证导致矛盾）

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: discrete_combinatorial
- structure_features: 圆环排列、n+1滑动窗口覆盖条件、极值问题（求最大不可能m）、鸽巢结构（n+1珠n色恰一色重复）
- key_objects: 圆环项链m珠、n色、n+1滑动窗口、同色间距、ceiling函数⌈m/n⌉

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: [extremal_reasoning, gap_analysis, counting_argument, necessary_condition_analysis, constructive_verification]
- primary_pattern: gap_analysis
- knowledge_required: [鸽巢原理, 圆环组合学, ceiling函数与整除性, 必要与充分条件, 极值组合学]
- key_insight: n+1窗口条件迫使每种颜色间距≤n，因此每色至少⌈m/n⌉次；对n色求和得到计数矛盾，m=n²-n-1时⌈(n²-n-1)/n⌉=n-1导致总数≥n²-n>m。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: constructive_approach（构造法——尝试构建合法涂色）
- translation_to: necessary_condition_analysis（必要条件分析——间距约束+计数论证）
- translation_type: method_translation（从构造到必要条件分析的方法转换）

---

## Step 6: 标注tell拓扑层 + 反思拓扑进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: discrete_combinatorial, ai_method_type: enumeration_brute_force, gap_type: structural_transformation}
- tell_small_concepts: [circular arrangement, n+1 window, color coverage, gap bound, ceiling counting, pigeonhole contradiction]
- expected_ai_method: Bare AI会尝试构造各种m值的合法涂色或枚举情况，在证明极值不可能性时卡住
- correct_method: 从构造转向必要条件分析：用间距约束推导计数不等式，找到不等式失败的阈值

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=discrete_combinatorial, ai_method_type=enumeration_brute_force, gap_type=structural_transformation均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。现有分类体系足够。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

所有pair均包含tell_topology和tell_small_concepts字段。全局pair均包含why_not_visible_locally字段。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI会尝试构造合法涂色并经验性地寻找阈值，在证明极值不可能性时卡住——关键洞察（窗口覆盖→间距约束→计数矛盾）需要非显然的结构转换，AI可能遗漏ceiling函数计算
- suitable_for_poc: [tell_hint_injection, gap_analysis_guidance, structural_transformation_detection]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：完整profile JSON已写入工作目录的 `profile.json` 文件

所有字段已检查：_key, source_id, source_dataset, schema_version, problem_text, solution_text, solution_summary, domain, subfield, answer_type, answer, problem_type, solution_method_type, structure_features, key_objects, thinking_patterns, primary_pattern, knowledge_required, key_insight, translation_from, translation_to, translation_type, tell_topology, tell_small_concepts, expected_ai_method, correct_method, tell_hint_pairs, global_tell_hint_pairs, bare_ai_expected, bare_ai_error_prediction, suitable_for_poc, discriminates_levels, qa_sequence, analysis_metadata — 全部包含。

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功
- 验证结果: [x] 通过

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: omni_math_004127
- solution_method_type: counting_argument
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否
- 是否遇到异常: 否

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
