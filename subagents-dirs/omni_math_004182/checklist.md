# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_004182
- **文件路径**: subagents-dirs/omni_math_004182/problem.lean
- **来源**: omni_math
- **ArangoDB progress记录_key**: 334062（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_004182/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：魔术师宣布正整数n和2n个实数x_1 < ... < x_{2n}，观众秘密选择一个n次多项式P(x)，计算P(x_1),...,P(x_{2n})并按非降序写在黑板上。魔术师能否找到策略恢复多项式P？
- 解答核心思路（1-2句话）：对于任意n和x_i，取非恒等置换σ，系统Q(x_i)=P(x_{σ(i)})有2n个方程、2n+2个未知数（P和Q的系数），解空间维度≥2，存在P≠Q使两者产生相同的排序值多重集，故魔术师无法区分，答案为No。
- 解答关键步骤列表：
  1. 识别排序破坏了值与x_i的配对信息
  2. 对n=1验证：递增和递减直线产生相同排序对
  3. 对一般n，取非恒等置换σ，建立Q(x_i)=P(x_{σ(i)})系统
  4. 维度计数：2n+2未知数 vs 2n方程 → 解空间维度≥2
  5. 非平凡解给出P≠Q，排序多重集相同
  6. 结论：对任意n策略不存在，答案No

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.3 | 描述题目结构：魔术师知道什么，排序丢失了什么信息，需要恢复什么？ | 魔术师知道n和有序实数x_1<...<x_{2n}。观众选n次多项式P，在2n个点求值后排序。排序破坏了值与x_i的配对。魔术师需从排序后的多重集恢复P。 |
| 2 | 自由列举 | 0.5 | 列出判断魔术师能否总是成功的所有可能方法，包括寻找反例的方法。 | (1)试小case n=1 (2)构造策略 (3)找反例：两个不同多项式产生相同排序多重集 (4)置换论证 (5)维度计数 |
| 3 | 小尝试 | 0.4 | 试n=1：给定两个排序值，两条不同的直线能否产生相同的排序对？ | n=1时P(x)=ax+b。a>0排序为{P(x_1),P(x_2)}，a<0排序为{P(x_2),P(x_1)}。给定{v_1,v_2}有两条不同直线（增/减），故n=1失败。 |
| 4 | 思维操作引导 | 0.6 | 对一般n，取非恒等置换σ，建立Q(x_i)=P(x_{σ(i)})。数未知数（P和Q的系数）和方程数。解空间维度说明什么？ | P有n+1系数，Q有n+1系数，共2n+2未知数。方程Q(x_i)=P(x_{σ(i)})共2n个。解空间维度≥2。归一化后≥1，存在非平凡解，P≠Q且均为n次。 |
| 5 | 推进 | 0.7 | 将维度论证连接到结论：P≠Q产生相同排序多重集意味着什么？ | P和Q产生相同排序多重集，魔术师看到相同输入但来自不同多项式，无法区分。对任意n和x_i都成立，故不存在通用策略。 |
| 6 | 能量传递引导 | 0.8 | 总结完整证明并给出最终答案。 | 答案No。对任意n和x_i，取非恒等置换σ，系统2n方程2n+2未知数，解空间≥2维，存在P≠Q产生相同排序多重集，魔术师无法区分，策略不存在。 |

**统计**：
- total_rounds: 6
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 1
- level_sum: 3.3
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R4
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R5

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence
- structure_features: 魔术师选择n和2n有序实数；观众选n次多项式P并排序值；排序破坏值与x_i的配对；需从排序多重集恢复P；问是否存在通用策略
- key_objects: n次多项式P(x)、2n有序实数x_1<...<x_{2n}、排序后的值多重集、{1,...,2n}的置换σ、方程组Q(x_i)=P(x_{σ(i)})

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: [structural_analysis, dimension_counting, small_case_to_general, proof_by_counterexample_construction]
- primary_pattern: dimension_counting
- knowledge_required: [polynomial degree and coefficients, multiset and sorting, permutation, linear algebra: dimension of solution space, degrees of freedom counting]
- key_insight: 非恒等置换σ创建2n方程2n+2未知数的系统，保证存在P≠Q产生相同排序多重集，证明对所有n不可能

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: combinatorial (permutation and sorting of values)
- translation_to: algebraic (dimension counting of linear system)
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: enumeration_brute_force, gap_type: knowledge_gap}
- tell_small_concepts: [sorted multiset, permutation ambiguity, dimension counting, non-injective recovery, degrees of freedom]
- expected_ai_method: enumeration_brute_force — AI试小case或试图构造策略，但找不到一般性的维度计数论证
- correct_method: dimension_counting — 对非恒等置换σ，系统Q(x_i)=P(x_{σ(i)})有2n+2未知数2n方程，非平凡解给出不同多项式产生相同排序多重集

### 6b. 反思拓扑分类

- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ **能**。structural_existence、enumeration_brute_force、logical_deduction、knowledge_gap等已有值均适用。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ **一致**。所有标注值均为已有值或同粒度。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ **足够**。三个维度能区分不同轮次的tell（R1用direct_calculation+method_problem_mismatch，R4用logical_deduction+knowledge_gap等）。
- [x] 如果发现拓扑分类需要进化，在此写出建议： **无需进化**。

**拓扑进化建议**（如有）：无。现有拓扑分类完全覆盖本题所有tell。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 6 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会试图为特定n构造策略，或正确解决n=1但无法推广。关键维度计数论证（2n+2未知数vs 2n方程）不直观，需要将置换理论与线性代数连接。AI可能错误地使用"n+1个点确定n次多项式"而不意识到排序破坏了点值配对。
- suitable_for_poc: [tell_hint_injection, dimension_argument_guidance, small_case_to_general_pattern, impossibility_proof_guidance]
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
- [x] answer（"No"）
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

**将完整JSON写入工作目录的 `profile.json` 文件** ✅

---

## Step 10: 入库ArangoDB [x]

**操作**：用exec工具执行Python脚本入库

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="334062"`的记录

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: omni_math_004182
- solution_method_type: dimension_counting_proof
- 局部(tell,hint)对数量: 6
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，现有拓扑分类完全覆盖
- 是否遇到异常: 无

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
