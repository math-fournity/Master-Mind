# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2010p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2010P6.lean
- **来源**: IMO 2010 P6
- **ArangoDB progress记录_key**: 329215（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2010P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let a₁, a₂, a₃, ... be a sequence of positive real numbers. Suppose that for some positive integer s, we have aₙ = max{aₖ + aₙ₋ₖ | 1 ≤ k ≤ n − 1} for all n > s. Prove that there exist positive integers l and N, with l ≤ s and such that aₙ = aₗ + aₙ₋ₗ for all n ≥ N.
- 解答核心思路（1-2句话）：Choose l ∈ {1,...,s} maximizing aₗ/l. Define residual res(n) = aₙ - n·(aₗ/l), show it's bounded and eventually periodic with period l, then translate back to get aₙ = aₗ + aₙ₋ₗ.
- 解答关键步骤列表：
  1. exists_max_ratio: Choose l ∈ {1,...,s} maximizing aₗ/l
  2. res_rec: Define res(n) = aₙ - n·(aₗ/l), show res satisfies the same max-recurrence
  3. res_nonpos: res(k) ≤ 0 for k ∈ {1,...,s} (because l maximizes ratio)
  4. res_bounded_above: res(n) ≤ 0 for all n (decompose into sum of res values from {1,...,s})
  5. res_bounded_below: res bounded below (step monotonicity: res(n) ≤ res(n+l))
  6. res_range_finite: res takes finitely many values (bounded + recurrence + bounded number of nonzero terms)
  7. res_eventually_t_step_eq → res_eventually_step_eq: finite range + monotonicity in steps of l → eventual periodicity with period l
  8. step_eq_of_res_step_eq → eventual_step_eq: translate res(n) = res(n+l) back to aₙ = aₗ + aₙ₋ₗ

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.9 | Describe the recurrence structure: what does aₙ = max{aₖ + aₙ₋ₖ} tell you about the sequence? What are the knowns and unknowns? | The sequence satisfies a max-convolution recurrence for n > s. a₁,...,aₛ are arbitrary positive reals; for n > s, aₙ = max of aₖ + aₙ₋ₖ. Need to show eventual fixed splitting at some l ≤ s. |
| 2 | 自由列举 | 0.8 | List all possible approaches: induction, generating functions, ratio analysis, linearization, convexity arguments. Which seem most promising? | Induction, generating functions, ratio analysis, linearization, convexity, combinatorial splits. Ratio analysis and linearization most promising because recurrence is additive. |
| 3 | 小尝试 | 0.5 | Try proving by induction that the splitting point stabilizes. What goes wrong with the max? | Direct induction fails because max makes splitting point non-deterministic — different n may have different optimal k. |
| 4 | 思维操作引导 | 0.4 | Consider the ratio aₙ/n. Which l ≤ s maximizes aₗ/l? | aₖ/k bounded above by max_{i≤s} aᵢ/i. l = argmax plays special role — highest efficiency per unit. |
| 5 | 思维操作引导 | 0.3 | Define residual res(n) = aₙ - n·(aₗ/l). Show res satisfies same recurrence and res(k) ≤ 0 for k ≤ s. | res(n) = max(res(k) + res(n-k)) because linear parts cancel. res(k) ≤ 0 because u = aₗ/l ≥ aₖ/k. |
| 6 | 推进 | 0.5 | Show res bounded above (≤0) and below, finite range, then eventual periodicity with period l. | Bounded above by 0 (decompose into parts ≤ s). Bounded below (step monotonicity). Finite range (bounded nonzero terms). Finite range + monotonicity → eventual periodicity. |
| 7 | 能量传递引导 | 0.6 | Translate res(n) = res(n+l) back to aₙ = aₗ + aₙ₋ₗ. You're almost there! | res(n) = res(n+l) → aₙ₊ₗ = aₙ + aₗ → aₙ = aₗ + aₙ₋ₗ for n ≥ N. Done! |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 4.0
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R5
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R4

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence
- structure_features: max-convolution recurrence for n > s; eventual periodicity of splitting point; positive real sequence; ratio optimization determines the splitting point
- key_objects: ["sequence {aₙ}", "max-recurrence aₙ = max{aₖ + aₙ₋ₖ}", "ratio aₗ/l", "residual function res(n) = aₙ - n·(aₗ/l)", "eventual step-equality with period l"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["linearization_decomposition", "ratio_optimization", "boundedness_argument", "finite_range_implies_eventual_periodicity", "translation_back"]
- primary_pattern: linearization_decomposition
- knowledge_required: ["max-convolution recurrence", "ratio analysis and optimization over finite set", "bounded sequences and finite range", "finite range + monotonicity implies eventual periodicity", "residual decomposition technique"]
- key_insight: Subtract the linear part n·(aₗ/l) to get a bounded residual that satisfies the same recurrence, then use finite range + monotonicity to deduce eventual periodicity with period l

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: max-convolution recurrence on potentially unbounded sequence
- translation_to: bounded residual with same recurrence → finite range → eventual periodicity → translate back to original sequence
- translation_type: structural_transformation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_manipulation, gap_type: structural_transformation}
- tell_small_concepts: ["max-convolution", "ratio maximization", "residual", "linear part", "eventual periodicity", "finite range", "boundedness"]
- expected_ai_method: direct_manipulation — bare AI would try to directly manipulate the max-recurrence or use induction on the splitting point, failing because the max makes the splitting non-deterministic
- correct_method: structural transformation via linearization — define residual res(n) = aₙ - n·(aₗ/l) where l maximizes aₗ/l, show boundedness and finite range, deduce eventual periodicity with period l, translate back to aₙ = aₗ + aₙ₋ₗ

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——structural_existence / direct_manipulation / structural_transformation 完全适配
- [x] 粒度一致——与已有值粒度统一
- [x] 不需要新维度——三个维度足够区分
- 无拓扑进化建议

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

详见 profile.json 中的 tell_hint_pairs 和 global_tell_hint_pairs 字段。每个pair都包含 tell_topology 和 tell_small_concepts。why_not_visible_locally 已填写。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: Bare AI would likely try direct induction or case analysis on the splitting point, failing because the max-recurrence doesn't give a deterministic splitting. Without the linearization insight (subtracting n·(aₗ/l) to get a bounded residual), AI cannot make progress on this problem.
- suitable_for_poc: ["POC-VMS-tell-identification", "POC-VMS-hint-injection", "POC-VMS-knowledge-bottleneck"]
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
- [x] answer（proof类型填要证明的结论）
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
- [x] tell_hint_pairs（每个pair含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（每个pair含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**完整JSON已写入 `subagents-dirs/compfiles_imo2010p6/profile.json`**

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功
- 验证结果: [x] 通过（7 local pairs, 2 global pairs, answer非None, why_not_visible_locally非None, knowledge_bottleneck=R5, thinking_bottleneck=R4）

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_imo2010p6
- solution_method_type: structural_transformation
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类完全适配
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
