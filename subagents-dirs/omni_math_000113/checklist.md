# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000113
- **文件路径**: subagents-dirs/omni_math_000113/problem.lean
- **来源**: AoPS omni_math (china_team_selection_test)
- **ArangoDB progress记录_key**: 329984（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000113/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：是否存在2002个不同正整数k₁,...,k₂₀₀₂，使得对任意正整数n≥2001，k₁2^n+1, k₂2^n+1, ..., k₂₀₀₂2^n+1中至少有一个是素数？
- 解答核心思路（1-2句话）：答案No。将问题推广到F>2002，取F^F个不同素数p_i，令X=F^F·∏(p_i-1)，由费马小定理2^X≡1(mod p_i)，将问题归约为有限组合问题，再用CRT/鸽笼原理找到t使得对所有k_j，k_j·2^t+1被某个p_i整除。
- 解答关键步骤列表：
  1. 推广：将2002推广为F>2002
  2. 构造：取F^F个不同素数p₁,...,p_{F^F}，令X=F^F·∏(p_i-1)
  3. 费马小定理：2^{p_i-1}≡1(mod p_i)，故2^X≡1(mod p_i)
  4. 归约：n=X+t时，k_j·2^n+1≡k_j·2^t+1(mod p_i)
  5. 组合论证：找到t使得对每个k_j，存在p_i整除k_j·2^t+1
  6. CRT兼容性：F^F个素数提供足够选择，找到F个兼容的素数
  7. 结论：X极大，n=X+t≥2001，故答案No

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 请描述这道题的结构：已知什么、求什么、关键约束是什么？ | 这是一个存在性问题：是否存在2002个不同正整数k_i，使得对任意n≥2001，至少一个k_i·2^n+1为素数。关键约束是"对任意n≥2001"——这是一个全称量词条件，需要覆盖所有大n。 |
| 2 | 自由列举 | 0.7 | 对于这个存在/非存在问题，你能想到哪些可能的攻击方向？ | 1) 尝试构造这样的k_i（证明Yes）；2) 证明不存在（证明No）；3) 利用覆盖系统/Sierpiński数的概念；4) 用CRT找n使所有k_i·2^n+1合数；5) 用费马小定理建立周期性；6) 鸽笼原理。 |
| 3 | 小尝试 | 0.5 | 先考虑单个k的情况：对任意正整数k，是否存在无穷多个n使得k·2^n+1为合数？这对多个k的同时情况有什么启发？ | 对单个k，取任意素数p不整除k，若2是mod p的原根则存在唯一的n mod (p-1)使p|k·2^n+1。所以对单个k总存在n使其合数。但多个k的挑战在于需要同一个n使所有k_i·2^n+1同时合数——需要协调多个覆盖。 |
| 4 | 思维操作引导 | 0.6 | 尝试将问题推广：用F>2002代替2002，取F^F个不同素数p_1,...,p_{F^F}。思考为什么需要F^F个素数而不是F个？ | 推广到F>2002给了更多灵活性。需要F^F个素数是因为每个k_j需要从大量素数中选一个使CRT兼容——F^F提供了足够的选择空间来找到F个阶互素（或CRT兼容）的素数。 |
| 5 | 思维操作引导 | 0.4 | 令X=F^F·∏(p_i-1)。由费马小定理，2^X≡1(mod p_i)对所有i成立。这对n=X+t意味着什么？ | 由2^X≡1(mod p_i)，n=X+t时k_j·2^n+1≡k_j·2^t+1(mod p_i)。问题归约为：找t∈{0,...,F^F-1}使得对每个k_j，存在p_i整除k_j·2^t+1。这是一个有限组合问题。 |
| 6 | 推进 | 0.5 | 现在需要找到t使得对每个k_j，某个p_i整除k_j·2^t+1。如何用CRT和F^F个素数的丰富性来论证这样的t存在？ | 对每个k_j，选一个素数p_{i_j}使得-k_j^{-1}在<2> mod p_{i_j}中，得到t≡a_j(mod d_{i_j})。在F^F个素数中可以找到F个CRT兼容的素数（阶两两互素或同余兼容），由CRT存在t同时满足所有F个同余。 |
| 7 | 能量传递引导 | 0.3 | 验证n=X+t≥2001并完成证明。 | X=F^F·∏(p_i-1)极其巨大，远超2001，故n=X+t≥2001。因此对任意2002个不同正整数，存在n≥2001使所有k_i·2^n+1合数。答案为No。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence
- structure_features: 存在性问题，涉及2002个不同正整数和全称量词条件（对任意n≥2001），需要证明非存在性——对任意k_i集合存在n使所有k_i·2^n+1合数
- key_objects: 正整数序列k_i，素数p_i，2的阶ord_p(2)，费马小定理周期性，CRT同余系统，覆盖系统

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["generalization", "reduction_via_periodicity", "covering_argument", "crt_compatibility_search"]
- primary_pattern: generalization
- knowledge_required: ["费马小定理", "中国剩余定理", "2模素数的阶", "覆盖系统/Sierpiński数概念", "鸽笼原理"]
- key_insight: 将2002推广为F>2002，取F^F个素数并令X=F^F·∏(p_i-1)，用费马小定理将无穷问题归约为有限组合问题，再用CRT找到使所有k_i·2^n+1同时合数的n

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 直接存在性问题（具体数2002，无穷多个n的条件）
- translation_to: 推广后的有限组合覆盖问题（F个k_j，F^F个素数，CRT兼容性搜索）
- translation_type: generalization + structural_reduction（推广+结构归约：用费马小定理将无穷条件归约为有限同余问题）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: ["覆盖系统", "费马小定理", "中国剩余定理", "Sierpiński数", "推广", "2的阶", "周期性归约", "CRT兼容性"]
- expected_ai_method: bare AI会尝试直接处理2002个数，可能尝试构造或逐一分析，无法看到推广和费马小定理归约的路径
- correct_method: 推广到F>2002，用F^F个素数和费马小定理将无穷条件归约为有限组合问题，用CRT找到兼容解

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=structural_existence, ai_method_type=direct_calculation, gap_type=structural_transformation都能归入已有拓扑类别
- [x] 粒度一致——标注值和已有值粒度统一
- [x] 三个维度足够区分这道题的tell和已有tell
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。已有拓扑分类可以充分描述此题。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 2 个，implicit型: 1 个

**局部tell_hint_pairs摘要**：
- R1: tell=AI看到存在性问题但不确定方向, hint=描述题目结构, topology=(structural_existence, direct_calculation, method_problem_mismatch)
- R2: tell=AI列举方向但未识别推广+费马组合, hint=列举所有可能方向, topology=(structural_existence, enumeration_brute_force, search_space_estimation)
- R3: tell=AI试单个k但未推广到多k, hint=试单个k情况, topology=(structural_existence, case_by_case, structural_transformation)
- R4: tell=AI被引导推广但未看到具体构造, hint=推广到F>2002, topology=(structural_existence, logical_deduction, structural_transformation)
- R5: tell=AI需要应用费马小定理建立周期性, hint=构造X并应用费马小定理, topology=(structural_existence, algebraic_identity, knowledge_gap), is_knowledge_bottleneck=True
- R6: tell=AI需要用CRT找兼容解, hint=用CRT和组合论证, topology=(structural_existence, equation_solving, method_translation)
- R7: tell=AI需要验证并收尾, hint=验证n≥2001并结论, topology=(structural_existence, logical_deduction, method_problem_mismatch)

**全局tell_hint_pairs摘要**：
- G1 (implicit): tell=AI假设答案可能是Yes并尝试构造, hint=考虑证明非存在性, why_not_visible=问题问"是否存在"自然引导构造方向
- G2 (path_feature): tell=AI直接处理2002卡住, hint=推广到F>2002, why_not_visible=具体数2002看似重要但论证对任意F成立
- G3 (path_feature): tell=AI未看到费马小定理与此题的联系, hint=用X=∏(p_i-1)的倍数建立周期性, why_not_visible=费马小定理与存在性问题的联系需要跨步骤综合

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接处理2002个数，可能尝试构造k_i或逐一分析，无法看到推广到F>2002的必要性，也无法将费马小定理与存在性问题联系起来。即使想到覆盖系统概念，也难以处理多k同时合数的要求。
- suitable_for_poc: ["POC-VMS-hint-injection", "POC-VMS-tell-detection", "POC-VMS-path-feature"]
- discriminates_levels: True

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON，已写入 `profile.json`

**所有字段已包含**：_key, source_id, source_dataset, schema_version, problem_text, solution_text, solution_summary, domain, subfield, answer_type, answer, problem_type, solution_method_type, structure_features, key_objects, thinking_patterns, primary_pattern, knowledge_required, key_insight, translation_from, translation_to, translation_type, tell_topology, tell_small_concepts, expected_ai_method, correct_method, tell_hint_pairs(7个), global_tell_hint_pairs(3个), bare_ai_expected, bare_ai_error_prediction, suitable_for_poc, discriminates_levels, qa_sequence, analysis_metadata

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

- problem_id: omni_math_000113
- solution_method_type: covering_crt_generalization
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3 (1 implicit + 2 path_feature)
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，已有拓扑分类充分
- 是否遇到异常: 题目解答在problem.lean中被截断（仅10行），通过数学推理和文献搜索重构完整解答思路

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
