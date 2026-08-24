# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1987p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1987P6.lean
- **来源**: IMO 1987 P6
- **ArangoDB progress记录_key**: 329120（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1987P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设 n ≥ 2 为整数。证明：如果对所有满足 0 ≤ k ≤ √(n/3) 的整数 k，k² + k + n 都是素数，那么对所有满足 0 ≤ k ≤ n-2 的整数 k，k² + k + n 也是素数。
- 解答核心思路（1-2句话）：对 k 施加强归纳。对于 k > √(n/3)，利用代数恒等式 f(k) = f(ss) + (2k - j + 1)·j（其中 ss = j - k - 1）将 f(k) 与某个 j 的 gcd 归约为 f(ss) 与 j 的 gcd，由归纳假设 f(ss) 素数推出矛盾，从而证明 f(k) 与 (k, 2k] 中所有整数互素；再结合 f(k) < (2k+1)² 的界，用"互素+界→素数"的引理完成证明。
- 解答关键步骤列表：
  1. 定义 f(x) = x² + x + p，r = ⌊√(p/3)⌋，对 k 施加强归纳
  2. 基础情形 k=0 及 k+1 ≤ r 时直接用假设 h₁
  3. 当 k+1 > r 时，令 s = k+1 - r，N = f(k+1)，证明 N < (2(k+1)+1)²（利用 p ≤ 3r² + 6r + 2）
  4. 证明 N 与 (k+1, 2(k+1)] 中所有整数互素：假设存在 j 不互素，令 ss = j - (k+2)，则 ss ≤ k
  5. 关键恒等式：f(k+1) = f(ss) + (2(k+1) - j + 1)·j，故 gcd(N, j) = gcd(f(ss), j)
  6. 由归纳假设 f(ss) 素数，且 f(ss) | j，又 f(ss) ≥ p 而 j < 2p，故 f(ss) = j
  7. 代入得 ss² + p = k + 2，推出 p ≤ k + 2 ≤ p - 1，矛盾
  8. 由互素 + 界 N < (2(k+1)+1)²，用 key_lemma' 得 N 素数

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
| 1 | 纯元认知观察 | 0.3 | 描述这道题的结构：假设条件是什么？要证明的结论是什么？假设的范围和结论的范围之间有什么关系？ | 假设条件是 k²+k+n 对 0≤k≤√(n/3) 为素数，结论是 k²+k+n 对 0≤k≤n-2 为素数。结论范围远大于假设范围，需要将小范围的素性"传播"到大范围。 |
| 2 | 自由列举 | 0.5 | 列出所有可能的证明方向：直接验证、归纳、反证、互素性、大小估计…… | 可能方向：强归纳（利用小k的结论推大k）、反证（假设某k处f(k)合数）、直接因式分解、互素性判素性、Eratosthenes筛法思想、多项式值的代数关系…… |
| 3 | 小尝试 | 0.4 | 假设存在某个 k > √(n/3) 使得 f(k) = k²+k+n 是合数，尝试直接分析它的因子。你能得到什么？ | f(k) 合数意味着有因子 d 满足 1 < d < f(k)。但直接分析因子结构没有明显进展——f(k) 是二次多项式，没有简单的因式分解。卡住了。 |
| 4 | 思维操作引导 | 0.6 | 计算代数恒等式 f(k) - f(j) = (k-j)(k+j+1)。这个恒等式如何将 f(k) 与更小的 f(j) 联系起来？特别地，如果想让 f(k) ≡ f(j) (mod m)，应该如何选取 j？ | f(k) - f(j) = (k-j)(k+j+1)。要让 f(k) ≡ f(j) (mod m)，需要 m | (k-j)(k+j+1)。最简单的方式是令 k+j+1 = m，即 j = m - k - 1。这样 f(k) - f(j) = (k - (m-k-1)) · m = (2k - m + 1) · m，确实是 m 的倍数。 |
| 5 | 思维操作引导 | 0.7 | 用强归纳：假设对所有 j < k，f(j) 是素数。如果 f(k) 与某个 m ∈ (k, 2k] 不互素，取 j = m - k - 1，用上面的恒等式证明 gcd(f(k), m) = gcd(f(j), m)。由此推出什么矛盾？ | gcd(f(k), m) = gcd(f(j), m)，由归纳 f(j) 素数，所以 f(j) | m。又 f(j) = j²+j+n ≥ n，而 m ≤ 2k ≤ 2(n-2) < 2n，所以 f(j) = m。代入得 j² + n = k + 1，即 n ≤ k + 1 ≤ n - 1，矛盾。 |
| 6 | 推进 | 0.6 | 上面的矛盾证明了 f(k) 与 (k, 2k] 中所有整数互素。现在需要证明 f(k) 是素数。回忆：如果一个数 m > 1 与所有满足 d² ≤ m 的整数 d 互素，则 m 是素数。你需要什么额外条件？ | 需要证明 f(k) < (2k+1)²，这样所有 f(k) 的潜在素因子 d ≤ √f(k) < 2k+1，而我们已经证明了 f(k) 与 (k, 2k] 互素。还需要处理 d ≤ k 的部分——可以用 dyadic argument 将互素性从 (k, 2k] 扩展到 (1, 2k]。 |
| 7 | 推进 | 0.65 | 证明 f(k) < (2k+1)²。利用 r = ⌊√(n/3)⌋ 和 k > r，推导出 n ≤ 3r² + 6r + 2，然后完成界的估计。 | 由 √(n/3) < r+1 得 n < 3(r+1)² = 3r² + 6r + 3，故 n ≤ 3r² + 6r + 2。设 s = k - r ≥ 1，则 f(k) = k² + k + n = (s+r)² + (s+r) + n ≤ (s+r)² + (s+r) + 3r² + 6r + 2。展开后与 (2k+1)² = (2(s+r)+1)² 比较可得 f(k) < (2k+1)²。 |
| 8 | 能量传递引导 | 0.8 | 现在所有零件都齐了：归纳基础来自假设，互素性来自反证矛盾，素性来自界+互素。把完整的证明组装起来。 | 强归纳：基础情形 k ≤ r 由假设给出。归纳步：k > r 时，(1) 证明 f(k) < (2k+1)²，(2) 证明 f(k) 与 (k, 2k] 互素（反证+恒等式+归纳假设），(3) 用 dyadic argument 扩展互素性到 (1, 2k]，(4) 由 f(k) < (2k+1)² 和互素性得 f(k) 素数。证毕。 |

**统计**：
- total_rounds: 8
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 4.55
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R5（gcd恒等式+归纳假设推出矛盾是纯知识瓶颈——需要知道如何用代数恒等式将gcd归约）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R4（从直接因式分解转向代数恒等式是关键思维转折——需要意识到f(k)-f(j)可因式分解）

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
- structure_features: 二次多项式 f(k)=k²+k+n 的素性从短区间 [0, √(n/3)] 传播到长区间 [0, n-2]，强归纳+互素性判素性+代数恒等式联系不同点的值
- key_objects: ["二次多项式 k²+k+n", "素性", "强归纳", "互素性", "⌊√(n/3)⌋", "代数恒等式 f(k)-f(j)=(k-j)(k+j+1)"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["strong_induction", "coprimality_primality_bridge", "algebraic_identity_relating_values", "contradiction_from_size_bounds", "range_extension", "dyadic_argument"]
- primary_pattern: coprimality_primality_bridge
- knowledge_required: ["互素性判素性（若m与所有d²≤m的d互素则m素数）", "强归纳原理", "二次多项式差值因式分解 f(k)-f(j)=(k-j)(k+j+1)", "gcd加法性质 gcd(a+bm, b)=gcd(a,b)", "dyadic argument（互素性区间倍增）"]
- key_insight: 利用代数恒等式 f(k)-f(j)=(k-j)(k+j+1)，选取 j=m-k-1 使 f(k)≡f(j)(mod m)，将 gcd(f(k),m) 归约为 gcd(f(j),m)，再用归纳假设 f(j) 素数推出矛盾——这是将素性从短区间传播到长区间核心机制

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接素性验证（尝试直接分析f(k)的因子结构）
- translation_to: 互素性判素性（通过证明f(k)与一段区间内所有整数互素+大小界来证明素性）
- translation_type: method_translation（从直接方法翻译到间接的互素性框架）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: method_translation}
- tell_small_concepts: ["coprimality_primality_bridge", "strong_induction", "quadratic_value_identity", "range_extension", "size_bound_for_primality", "gcd_reduction"]
- expected_ai_method: direct_calculation（bare AI会尝试直接验证素性或分析因子结构，不会想到互素性框架）
- correct_method: coprimality_based_primality_via_induction（用互素性+大小界+强归纳间接证明素性）

**已有ai_method_type值**（优先使用）：
- `enumeration_brute_force` ✅ 抽象
- `continuous_analytic` ✅ 抽象
- `direct_calculation` ✅ 抽象
- `logical_deduction` ✅ 抽象
- `case_by_case` ✅ 抽象
- `algebraic_identity` ✅ 中等
- `equation_solving` ✅ 抽象
- `direct_manipulation` ✅ 抽象
- **❌ 不要用太长太具体的值**

**已有gap_type值**（优先使用）：
- `method_problem_mismatch` ✅ 抽象
- `knowledge_gap` ✅ 抽象
- `structural_transformation` ✅ 中等
- `search_space_estimation` ✅ 中等
- `method_translation` ✅ 中等
- `global_sorting` ⚠️ 偏具体
- **❌ 不要用太具体的值**

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 可以。structural_existence（素性结构存在性传播）、direct_calculation（bare AI直接验证）、method_translation（从直接验证翻译到互素性框架）都归入已有类别。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 一致。三个维度都是中等偏抽象的粒度。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。这道题的核心gap是"方法翻译"——从直接素性验证到互素性框架，已有gap_type=method_translation精确匹配。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。已有分类体系完全覆盖。

**拓扑进化建议**（如有）：无。已有拓扑分类完全够用。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 8 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部(tell, hint)对**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到条件命题但未识别假设范围与结论范围的结构关系 | 描述题目结构：假设范围√(n/3)与结论范围n-2的关系 | 0.3 | 纯元认知观察 | false | {structural_existence, direct_calculation, search_space_estimation} | ["hypothesis_range", "conclusion_range", "range_extension"] |
| 2 | AI列举方向但未考虑互素性作为素性的桥梁 | 列出所有方向：归纳、反证、互素性、大小估计 | 0.5 | 自由列举 | false | {structural_existence, enumeration_brute_force, method_problem_mismatch} | ["approach_enumeration", "coprimality_bridge", "induction"] |
| 3 | AI尝试直接分析f(k)的因子结构但卡住——二次多项式无简单分解 | 假设f(k)合数，直接分析因子，发现卡住 | 0.4 | 小尝试 | false | {structural_existence, direct_calculation, method_problem_mismatch} | ["composite_assumption", "factor_analysis", "stuck_point"] |
| 4 | AI卡在直接因式分解，需要转向f(k)与f(j)的代数关系 | 计算f(k)-f(j)=(k-j)(k+j+1)，选取j=m-k-1使f(k)≡f(j)(mod m) | 0.6 | 思维操作引导 | false | {structural_existence, algebraic_identity, structural_transformation} | ["quadratic_value_identity", "difference_factorization", "modular_reduction"] |
| 5 | AI有恒等式但不知如何与归纳结合推出矛盾 | 用强归纳+恒等式证明gcd(f(k),m)=gcd(f(j),m)，由f(j)素数推出矛盾 | 0.7 | 思维操作引导 | true | {structural_existence, logical_deduction, knowledge_gap} | ["strong_induction", "gcd_identity", "coprime_propagation", "size_bound_contradiction"] |
| 6 | AI证明了互素性但未建立素性判据所需的界 | 需要f(k)<(2k+1)²使潜在素因子落在互素区间内 | 0.6 | 推进 | false | {structural_existence, direct_calculation, structural_transformation} | ["size_bound_for_primality", "coprimality_primality_bridge", "dyadic_argument"] |
| 7 | AI需要从r=⌊√(n/3)⌋推导出f(k)<(2k+1)²的界 | 利用n≤3r²+6r+2和s=k-r≥1完成界估计 | 0.65 | 推进 | false | {structural_existence, direct_calculation, structural_transformation} | ["range_bound", "sqrt_n_over_3", "inequality_estimation"] |
| 8 | 所有零件就位但未组装成完整证明 | 组装：归纳基础+互素性+界→素性，证毕 | 0.8 | 能量传递引导 | false | {structural_existence, logical_deduction, method_translation} | ["induction_assembly", "proof_completion", "range_extension"] |

**全局(tell, hint)对**：

**Global Pair 1 (path_feature)**:
- scope_type: path_feature
- scope: 从假设范围到结论范围的完整归纳链——代数恒等式→gcd归约→互素性→大小界→素性
- observation_point: null
- tell: 证明需要一条非显然的链条：代数恒等式将不同点的值联系起来→gcd归约到更小的值→归纳假设给出素数→矛盾推出互素性→大小界+互素性给出素性。没有任何单一步骤揭示完整链条。
- hint: 关键路径是：(1)建立f(k)<(2k+1)²，(2)用恒等式+归纳证明互素性，(3)用互素性+界推出素性
- hint_level: 0.7
- generalizability: high——互素性判素性+归纳的范式可推广到许多多项式序列的素性证明
- why_not_visible_locally: 每个局部步骤（恒等式、gcd、界）看起来是独立的计算。全局链条——这些步骤组合成一个素性判据——只有从完整路径视角才可见。没有任何单个步骤揭示最终目标是互素性判素性。
- tell_topology: {structural_existence, logical_deduction, method_translation}
- tell_small_concepts: ["coprimality_primality_bridge", "induction_chain", "size_bound_for_primality"]

**Global Pair 2 (implicit)**:
- scope_type: implicit
- scope: 假设范围√(n/3)与结论范围n-2之间的隐含关系
- observation_point: R7
- tell: √(n/3)这个阈值不是任意的——它恰好是使f(k)<(2k+1)²成立的临界点，这是互素性判素性步骤的必要条件
- hint: 假设范围√(n/3)的选择使得当k>√(n/3)时界f(k)<(2k+1)²成立，这对互素性→素性步骤是必要的
- hint_level: 0.75
- generalizability: medium——具体阈值依赖于多项式形式，但"假设范围匹配证明需求"的范式是通用的
- why_not_visible_locally: 在局部计算界f(k)<(2k+1)²时，与"为什么√(n/3)是假设阈值"的联系是隐含的——只有当你看到界需要n≤3r²+...时，√(n/3)的选择才变得清晰
- tell_topology: {structural_existence, direct_calculation, structural_transformation}
- tell_small_concepts: ["hypothesis_threshold", "range_bound_connection", "sqrt_n_over_3"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: bare AI会尝试直接因式分解或简单归纳，不会发现关键恒等式f(k)-f(j)=(k-j)(k+j+1)及其在gcd归约中的应用，也不会想到"互素性+大小界→素性"的间接框架。最可能在R3（直接分析因子）处卡住，无法完成从直接验证到互素性框架的方法翻译。
- suitable_for_poc: ["tell_hint_injection", "topology_matching", "path_feature_extraction", "knowledge_bottleneck_detection"]
- discriminates_levels: true（这道题需要深层的方法翻译和知识瓶颈突破，能有效区分有/无引导的AI表现）

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON

**⚠️ 完整字段清单（逐项检查，不能遗漏）**：
- [ ] _key（=problem_id）
- [ ] source_id
- [ ] source_dataset
- [ ] schema_version（=3）
- [ ] problem_text
- [ ] solution_text
- [ ] solution_summary
- [ ] domain
- [ ] subfield
- [ ] answer_type
- [ ] answer（**⚠️ 必填，不能为None**。proof类型填要证明的结论，如"sum >= ..."；existence_construction类型填构造的存在性结论；numerical类型填数值答案）
- [ ] problem_type
- [ ] solution_method_type
- [ ] structure_features
- [ ] key_objects
- [ ] thinking_patterns
- [ ] primary_pattern
- [ ] knowledge_required
- [ ] key_insight
- [ ] translation_from
- [ ] translation_to
- [ ] translation_type
- [ ] tell_topology（profile级）
- [ ] tell_small_concepts（profile级）
- [ ] expected_ai_method
- [ ] correct_method
- [ ] tell_hint_pairs（每个pair含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [ ] global_tell_hint_pairs（每个pair含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [ ] bare_ai_expected
- [ ] bare_ai_error_prediction
- [ ] suitable_for_poc
- [ ] discriminates_levels
- [ ] qa_sequence（含rounds数组和stats子对象）
- [ ] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**将完整JSON写入工作目录的 `profile.json` 文件**

---

## Step 10: 入库ArangoDB [ ]

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="329120"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1987p6"
   - extracted_by改为"subagent"

**示例代码**：
```python
from arango import ArangoClient
from datetime import datetime, timezone
import json

client = ArangoClient(hosts='http://localhost:8529')
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
now = datetime.now(timezone.utc).isoformat()

# 读取profile.json
with open('profile.json', 'r') as f:
    profile = json.load(f)

# 写入problem_profiles
db.collection('problem_profiles').insert(profile, overwrite=True)

# 更新problem_extraction_progress
db.collection('problem_extraction_progress').update({
    '_key': '329120',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1987p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1987p6')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_imo1987p6
- solution_method_type: strong_induction_coprimality
- 局部(tell,hint)对数量: 8
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否。已有拓扑分类完全覆盖（structural_existence / direct_calculation / method_translation等均归入已有类别，粒度一致）
- 是否遇到异常: 否。入库和验证均一次通过。

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
