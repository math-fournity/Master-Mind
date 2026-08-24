# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1983p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1983P5.lean
- **来源**: IMO 1983 P5
- **ArangoDB progress记录_key**: 329103（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1983P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Is it possible to choose 1983 distinct positive integers, all ≤ 10^5, no three of which are consecutive terms of an arithmetic progression? Justify your answer.
- 解答核心思路（1-2句话）：将1到2^k-1的二进制数字串重新解释为三进制数，得到的集合无3项等差数列且元素个数和上界可控。取k=11，得2047个数，最大值88573 < 10^5，取其中1983个即可。
- 解答关键步骤列表：
  1. 定义base_two_to_base_three(n)：将n的二进制数字串在三进制下重新解释
  2. 证明该映射是单射（不同二进制→不同三进制重解释）
  3. 证明结果为正数
  4. 证明每个结果 ≤ (3^k-1)/2（几何级数上界，因为三进制数字只有0和1）
  5. 证明无3项AP：若x,y,z三进制数字只有0/1且x+z=2y，则三进制加法无进位，2y的数字只有0/2，迫使x的每位数字=z的对应位数字，故x=z矛盾
  6. 取k=11：2^11-1=2047≥1983，(3^11-1)/2=88573≤10^5

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**每轮必须标注**：
- **question**：给AI的提示/问题（Q）
- **expected_answer**：预期回复（A）
- **situation_type**：**⚠️ 只能取以下6个值之一，禁止自创**：
  - `纯元认知观察`——让AI描述题目结构、识别已知/未知
  - `自由列举`——让AI列出所有可能方向
  - `小尝试`——让AI试一个方向（可能走错的）
  - `思维操作引导`——给AI具体的思维操作指令
  - `推进`——让AI继续推进当前方向
  - `能量传递引导`——给AI信心/能量，收尾
- **level**：**⚠️ 必须是0-1之间的浮点数**（0=完全具体，1=完全抽象。禁止用1-4整数）

**QA序列设计原则**：
1. 第1轮通常是`纯元认知观察`——让AI描述题目结构
2. 第2轮通常是`自由列举`——让AI列出所有可能方向
3. 第3轮通常是`小尝试`——让AI试一个可能走错的方向
4. 中间几轮根据情况用`思维操作引导`或`推进`
5. 最后一轮通常是`能量传递引导`——收尾

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | Describe the structure of this problem. What are the knowns, unknowns, and what kind of answer is expected? | Existence question: can 1983 AP-free distinct positive integers ≤ 10^5 be chosen? Yes/no with justification. Key constraint: no x<y<z with x+z=2y. |
| 2 | 自由列举 | 0.7 | What approaches could you try to construct such a set or prove it's impossible? | Greedy construction, probabilistic method, explicit construction using number representations, density arguments (Roth's theorem), base conversion tricks, digit-restricted sets. |
| 3 | 小尝试 | 0.5 | Try a greedy approach: start picking numbers from 1 upward, skipping any that would create a 3-term AP. What sequence do you get? Can you prove 1983 fit under 10^5? | Greedy gives 1,2,4,5,10,11,13,14,... — numbers with only 0/1 digits in base 3! But proving the bound directly from greedy is hard. |
| 4 | 思维操作引导 | 0.4 | Consider representing numbers in different bases. What if you take numbers 1 to 2^k-1 (binary), and reinterpret their digit strings in base 3? What properties does the resulting set have? | Resulting numbers have only 0/1 digits in base 3. 2^k-1 of them (injective). Each ≤ (3^k-1)/2 by geometric series. Digit restriction is key for AP-freeness. |
| 5 | 思维操作引导 | 0.3 | For the no-AP property: if x, y, z all have only 0/1 digits in base 3 and x + z = 2y, analyze the base-3 digits. What does this force? | No carry in base-3 addition (max digit sum 2 < 3). 2y has only 0/2 digits. So x+z must have only 0/2 digits, meaning each digit of x equals corresponding digit of z. Hence x = z, contradicting x < y < z. |
| 6 | 推进 | 0.4 | Now compute: for k = 11, how many numbers do you get and what's the maximum value? Does this satisfy the constraints? | 2^11 - 1 = 2047 ≥ 1983. Max = (3^11 - 1)/2 = 88573 ≤ 10^5. Both constraints satisfied. Take any 1983 of the 2047 numbers. |
| 7 | 能量传递引导 | 0.6 | You've constructed the set and verified all constraints. Write up the complete proof. | Define S = {base_two_to_base_three(n) : 1 ≤ n ≤ 2^11 - 1}. |S| = 2047 ≥ 1983, all elements ≤ 88573 < 10^5, no 3-term AP by no-carry digit argument. Take any 1983 elements. |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.7
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: 5
- thinking_bottleneck（思维瓶颈在哪轮，或null）: 4

---

## Step 3: 标注问题拓扑层 [x]

**操作**：从题目结构中提取

**要求**：
- `problem_type`：问题类型大概念。**优先使用已有值**（见下方拓扑分类体系），如需新建确保粒度一致
- `structure_features`：题目结构特征描述
- `key_objects`：核心数学对象列表

**已有problem_type值**（优先使用）：
- `structural_existence` ✅ 抽象
- `discrete_combinatorial` ✅ 抽象
- `trigonometric_identity` ✅ 中等
- `constraint_satisfaction` ✅ 中等
- `characterization` ✅ 抽象
- `inequality_proof` ✅ 中等
- `absolute_value_system` ⚠️ 偏具体
- `functional_equation_periodicity` ⚠️ 偏具体
- **❌ 不要用太具体的值**（如`word_problem_with_diophantine_constraint`是错误粒度）

**产出**：
- problem_type: structural_existence
- structure_features: Existence of a large AP-free subset within a bounded interval; the construction exploits digit restrictions across different bases (binary digits reinterpreted in base 3)
- key_objects: positive integers, arithmetic progressions, binary representation, base-3 representation, digit reinterpretation, no-carry addition

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [base_conversion_trick, digit_analysis, constructive_existence, no_carry_argument]
- primary_pattern: base_conversion_trick
- knowledge_required: [arithmetic progressions, positional number systems, base conversion, geometric series, injectivity of digit maps, modular arithmetic]
- key_insight: Reinterpret binary digit strings as base-3 numbers — the digit restriction (0,1 only) in base 3 prevents 3-term APs because addition without carry forces digit-wise equality

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: base-2 (binary) representation
- translation_to: base-3 representation with restricted digits (0 and 1 only)
- translation_type: base_reinterpretation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: enumeration_brute_force, gap_type: method_translation}
- tell_small_concepts: [base_conversion, digit_restriction, no_carry, 3-term AP, geometric_series_bound]
- expected_ai_method: Greedy construction or probabilistic method — AI would try to build the set incrementally or use density arguments, getting stuck on proving the bound
- correct_method: Explicit construction via base-2 to base-3 digit reinterpretation, using no-carry addition to prove AP-freeness

### 6b. 反思拓扑分类

- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是，structural_existence + enumeration_brute_force + method_translation 均为已有值
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是，粒度一致
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化

**拓扑进化建议**（如有）：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

详见 profile.json 中的 tell_hint_pairs 和 global_tell_hint_pairs 字段。每个pair均包含tell_topology和tell_small_concepts。全局pair的why_not_visible_locally已填写。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: AI would try greedy construction or probabilistic method, getting stuck on proving that 1983 AP-free numbers can fit under 10^5. The base-2-to-base-3 digit reinterpretation trick is non-obvious and requires a creative leap that connects number representation with additive combinatorics.
- suitable_for_poc: [tell_hint_validation, method_translation_poc, construction_discovery_poc]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON

完整JSON已写入 `subagents-dirs/compfiles_imo1983p5/profile.json`。所有字段均已填写：
- _key, source_id, source_dataset, schema_version=3 ✓
- problem_text, solution_text, solution_summary ✓
- domain, subfield, answer_type, answer（必填，非None）✓
- problem_type, solution_method_type, structure_features, key_objects ✓
- thinking_patterns, primary_pattern, knowledge_required, key_insight ✓
- translation_from, translation_to, translation_type ✓
- tell_topology（profile级）, tell_small_concepts（profile级）✓
- expected_ai_method, correct_method ✓
- tell_hint_pairs（7个，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）✓
- global_tell_hint_pairs（2个，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）✓
- bare_ai_expected, bare_ai_error_prediction, suitable_for_poc, discriminates_levels ✓
- qa_sequence（含rounds数组和stats子对象）✓
- analysis_metadata ✓

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

验证输出：验证通过: compfiles_imo1983p5, 7 local pairs, 2 global pairs

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_imo1983p5
- solution_method_type: constructive_existence
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类（structural_existence + enumeration_brute_force + method_translation）足够覆盖
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
