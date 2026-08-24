# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000102
- **文件路径**: subagents-dirs/omni_math_000102/problem.lean
- **来源**: AoPS omni_math (china_team_selection_test)
- **ArangoDB progress记录_key**: 329973（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000102/problem.lean`

**产出**：
- 题目原文（数学描述）：Find the minimum $a$ such that $\forall a_1,a_2,a_3,a_4\in\mathbb{R}$, $\exists$ integers $k_1,k_2,k_3,k_4$ with $\sum_{i<j}((a_i-k_i)-(a_j-k_j))^2 \leq a$.
- 解答核心思路（1-2句话）：Reduce to fractional parts on a circle of circumference 1; the worst case is equally spaced points giving sum 5/4.
- 解答关键步骤列表：
  1. Recognize that choosing integers $k_i$ is equivalent to choosing representatives mod 1 (fractional parts on a circle)
  2. Lower bound: equally spaced points $a_i = i/4$ give sum $5/4$ for any integer choice
  3. Upper bound: for any 4 points on circle, cut at largest gap (span $\leq 3/4$), use algebraic identity to show sum $\leq 5/4$
  4. Answer: $a = 5/4 = 1.25$

---

## Step 2: QA序列分析——局部视角7步 [x]

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | Describe the structure: what is universally quantified, what is existentially chosen, what is the objective? | Minimax structure: for all reals, exists integers, minimize sum of squared pairwise differences |
| 2 | 自由列举 | 0.7 | List all possible approaches | Direct computation, fractional parts, circle interpretation, extremal, pigeonhole, optimization |
| 3 | 小尝试 | 0.3 | Try a_i = i/4, compute the sum | Equally spaced gives sum 5/4, lower bound a >= 5/4 |
| 4 | 思维操作引导 | 0.5 | Recognize integer choice = mod 1 representatives, reformulate on circle | 4 points on circle of circumference 1, choose cut to minimize sum |
| 5 | 推进 | 0.6 | What configuration maximizes the minimum? | Equally spaced (gaps all 1/4), every cut gives 5/4 |
| 6 | 思维操作引导 | 0.5 | Prove upper bound using identity and gap analysis | Span <= 3/4 after largest gap cut, sum <= 5/4 via algebraic identity |
| 7 | 能量传递引导 | 0.8 | Verify lower=upper=5/4, confirm proof complete | Answer a = 5/4 = 1.25, extremal case is equally spaced |

**统计**：
- total_rounds: 7
- metacognitive_rounds: 4 (R1,R2,R5,R7)
- knowledge_rounds: 2 (R4,R6)
- level_sum: 4.2
- knowledge_bottleneck: R4
- thinking_bottleneck: R6

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization（刻画极值常数的最优值）
- structure_features: universal_quantifier_over_reals, existential_quantifier_over_integers, sum_of_squared_pairwise_differences, minimax_structure, modular_arithmetic_structure
- key_objects: real numbers a_i, integers k_i, fractional parts x_i, circle of circumference 1, sum of squared pairwise differences

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: [extremal_principle, structural_reduction_to_circle, minimax_reasoning, symmetry_exploitation, algebraic_identity_application]
- primary_pattern: structural_reduction_to_circle_with_extremal_analysis
- knowledge_required: [fractional parts and modular arithmetic, sum of squared differences identity, circle geometry interpretation of mod 1, minimax/extremal principle, gap analysis on circle]
- key_insight: Choosing integers k_i is equivalent to placing 4 points on a circle of circumference 1; the worst case is equally spaced points giving sum 5/4

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: integer_optimization（整数选择优化）
- translation_to: circle_geometry（圆上几何/分数部分）
- translation_type: structural_transformation（结构变换——从整数优化语言翻译到圆上几何语言）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: [fractional parts, circle of circumference 1, equally spaced points, largest gap cut, sum of squared differences identity]
- expected_ai_method: Bare AI would try direct calculation: test specific configurations, attempt to compute the sum algebraically without recognizing the circle/fractional parts reduction
- correct_method: Reduce to fractional parts on a circle of circumference 1, identify equally spaced points as the extremal case, prove upper bound using gap analysis and the algebraic identity

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——characterization/direct_calculation/structural_transformation均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 不需要新维度——三个维度足够区分这道题的tell
- 拓扑进化建议：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

每轮pair含独立tell_topology和tell_small_concepts，详见profile.json。全局pair含why_not_visible_locally（非None）。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: Bare AI would try direct computation without recognizing the circle/fractional parts reduction. Might guess 5/4 from equally spaced case but cannot prove the upper bound without the structural transformation.
- suitable_for_poc: [tell_extraction, hint_injection, structural_transformation_detection]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON

**⚠️ 完整字段清单（逐项检查，不能遗漏）**：
- [x] _key（=problem_id）
- [x] source_id
- [x] source_dataset
- [x] schema_version（=3）
- [x] problem_text
- [x] solution_text
- [x] solution_summary
- [x] domain
- [x] subfield
- [x] answer_type
- [x] answer（=5/4，非None）
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

已写入 `subagents-dirs/omni_math_000102/profile.json`

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功
- 验证结果: [x] 通过（7 local pairs, 2 global pairs, answer=5/4, knowledge_bottleneck=R4, thinking_bottleneck=R6）

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: omni_math_000102
- solution_method_type: extremal_analysis
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无，已有分类够用
- 是否遇到异常: 否（problem.lean解答文本被截断，已根据数学内容和答案5/4重构solution_text）

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
