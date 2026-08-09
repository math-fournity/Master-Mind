# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_004116
- **文件路径**: subagents-dirs/omni_math_004116/problem.lean
- **来源**: omni_math
- **ArangoDB progress记录_key**: 333995（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_004116/problem.lean`

**产出**：
- 题目原文（数学描述）：Find all polynomials P(x) of odd degree d with integer coefficients satisfying: for each positive integer n, there exist n positive integers x_1,...,x_n such that 1/2 < P(x_i)/P(x_j) < 2 and P(x_i)/P(x_j) is the d-th power of a rational number for every pair i,j.
- 解答核心思路（1-2句话）："对每个正整数n"这个全称量词迫使P(x)必须是线性多项式的d次幂乘以常数。必要性：非d次幂因子在大n时破坏比值条件；充分性：a(rx+s)^d的比值自然是d次有理数幂。
- 解答关键步骤列表：
  1. 识别"对每个n"是关键结构约束
  2. 分析d次幂比值条件对P(x)因式结构的限制
  3. 推导P(x) = a·Q(x)^d（非d次幂因子在大n时不可能满足）
  4. 由deg(P)=d推出Q(x)为线性（rx+s）
  5. 验证所有条件：整系数（(r,s)=1）、比值界（取x_i足够近）、非零（a≠0）

---

## Step 2: QA序列分析——局部视角7步 [x]

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.3 | 请描述这道题的结构：已知条件是什么？未知量是什么？关键约束有哪些？特别注意'对每个正整数n'这个量词的含义。 | 已知P(x)是奇数次整系数多项式，未知是所有满足条件的P(x)。关键约束有两个：(1)比值在(1/2,2)内，(2)比值是d次有理数幂。'对每个正整数n'意味着条件对任意大的n都成立，是非常强的结构约束。 |
| 2 | 自由列举 | 0.5 | 对于满足条件的多项式，你能列出哪些可能的候选形式？什么样的多项式结构天然产生d次有理数幂的比值？ | 可能形式：x^d、a(rx+s)^d、一般多项式等。d次幂比值条件暗示P(x)可能是某个多项式的d次幂。 |
| 3 | 小尝试 | 0.4 | 尝试验证P(x) = x^d是否满足条件。如果满足，能否推广？ | P(x)=x^d时比值=(x_i/x_j)^d是有理数d次幂。取x_i=k+i对足够大k，比值接近1在(1/2,2)内。推广方向：P(x)=a(rx+s)^d。 |
| 4 | 思维操作引导 | 0.6 | 如果P(x)不是某个多项式的d次幂，即P(x)=a·Q(x)^d·R(x)其中R(x)不是d次幂，这个条件对任意大的n还能满足吗？ | R(x_i)/R(x_j)一般不是d次幂。对任意大n需要越来越多比值都是d次幂，一般不可能。因此R(x)必须是常数，P(x)必须是某个多项式的d次幂乘以常数。 |
| 5 | 推进 | 0.5 | 既然P(x) = a·Q(x)^d，Q(x)需要满足什么条件？deg(Q)是多少？ | deg(P)=d，Q(x)^d度为d，所以Q(x)度为1，即Q(x)=rx+s。整系数要求r,s为整数。 |
| 6 | 思维操作引导 | 0.7 | 验证P(x)=a(rx+s)^d满足所有条件：(1)为什么需要(r,s)=1？(2)比值界如何保证？(3)a≠0和r≥1的作用？ | (1)(r,s)=1确保展开后系数为整数。(2)取x_i足够近，比值接近1在(1/2,2)内。(3)a≠0确保非零，r≥1确保度为d。 |
| 7 | 能量传递引导 | 0.4 | 总结你的发现：所有满足条件的多项式是什么形式？完整性如何保证？ | P(x)=a(rx+s)^d，a,r,s为整数，a≠0，r≥1，(r,s)=1。必要性来自d次幂比值约束对任意n的限制，充分性通过直接验证。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds: 4（R1纯元认知观察 + R2自由列举 + R5推进 + R7能量传递引导）
- knowledge_rounds: 2（R4思维操作引导 + R6思维操作引导）
- level_sum: 3.4
- knowledge_bottleneck: R4
- thinking_bottleneck: R3

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: Characterization problem: find ALL polynomials of odd degree with integer coefficients satisfying a ratio condition. The condition has two parts: (1) ratio bounded in (1/2, 2), (2) ratio is d-th power of rational. The 'for each positive integer n' quantifier is the driving constraint that forces rigid structure.
- key_objects: polynomial P(x) with integer coefficients, odd degree d, d-th power of rational number, ratio P(x_i)/P(x_j) bounded in (1/2, 2), universal quantifier over n, linear polynomial rx + s

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["structural_characterization", "necessity_sufficiency_analysis", "asymptotic_reasoning", "form_guessing_and_validation"]
- primary_pattern: structural_characterization
- knowledge_required: ["polynomial factorization theory", "properties of d-th powers of rational numbers", "integer coefficient polynomial expansion", "density of integers near a value for ratio control", "coprimality and integer coefficient conditions"]
- key_insight: The 'for all n' quantifier combined with the d-th power ratio condition forces P(x) to be a constant times a perfect d-th power of a linear polynomial; any non-d-th-power factor would break the ratio condition for sufficiently large n.

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: ratio_constraint_analysis
- translation_to: polynomial_factorization_structure
- translation_type: structural_transformation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: case_by_case, gap_type: structural_transformation}
- tell_small_concepts: ["d-th power of rational", "ratio bound (1/2, 2)", "universal quantifier over n", "odd degree", "integer coefficients", "linear polynomial d-th power", "polynomial factorization", "coprimality condition"]
- expected_ai_method: case_by_case
- correct_method: structural_characterization

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=characterization, ai_method_type=case_by_case, gap_type=structural_transformation 都能归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。已有分类体系足够覆盖此题。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI will likely attempt to verify specific polynomial forms without recognizing the necessity argument. It may not properly handle the 'for each positive integer n' quantifier as a structural constraint. The key gap is connecting the d-th power ratio condition to the factorization structure of P(x) - AI may verify sufficiency but fail to prove necessity.
- suitable_for_poc: ["tell_extraction", "hint_injection", "level_discrimination"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：完整profile JSON已写入工作目录的 `profile.json` 文件。

所有字段已逐项检查：
- [x] _key（=omni_math_004116）
- [x] source_id
- [x] source_dataset
- [x] schema_version（=3）
- [x] problem_text
- [x] solution_text
- [x] solution_summary
- [x] domain
- [x] subfield
- [x] answer_type
- [x] answer
- [x] problem_type
- [x] solution_method_type
- [x] structure_features
- [x] key_objects
- [x] thinking_patterns
- [x] primary_pattern
- [x] knowledge_required
- [x] key_insight
- [x] translation_from
- [x] translation_to
- [x] translation_type
- [x] tell_topology（profile级）
- [x] tell_small_concepts（profile级）
- [x] expected_ai_method
- [x] correct_method
- [x] tell_hint_pairs（7个pair，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（2个pair，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象）
- [x] analysis_metadata

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功
- 验证结果: [x] 通过

---

## Step 11: 汇报 [x]

- problem_id: omni_math_004116
- solution_method_type: structural_characterization
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，已有分类体系足够
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
