# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2014p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2014P6.lean
- **来源**: USA 2014 P6
- **ArangoDB progress记录_key**: 329459（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2014P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Prove that there is a constant c > 0 with the following property: If a, b, n are positive integers such that gcd(a+i, b+j) > 1 for all i, j ∈ {0, 1, ..., n}, then min{a, b} > (cn)^n.
- 解答核心思路（1-2句话）：取 c = 1/65536。将 (n+1)×(n+1) 网格中每格的共同素因子分为小素数(≤n²/1000)和大素数(>n²/1000)，用筛法证明小素数覆盖的格 < N²/2，鸽巢得某行有 >N/2 个大素数格，注入论证证明这些大素数互异，故 a+i₀ ≥ (n²/1000)^((n+3)/2) > (n/65536)^n。
- 解答关键步骤列表：
  1. 分小n（n<2^15，平凡：min≥2 > (n/65536)^n）和大n（n≥2^15，主论证）
  2. 定义 M = n²/1000，小素数集合 P = {素数 p ≤ M}
  3. 定义"小格" S = 网格中被某个小素数 p∈P 同时整除 a+i 和 b+j 的格
  4. 筛法计数：|S| ≤ Σ_{p∈P} (N/p+1)² = N²·Σ(1/p²) + 2N·Σ(1/p) + |P|
  5. 用调和和界 Σ(1/p) ≤ clog₂(M+1) ≤ n/100 和 Σ(1/p²) ≤ 47/100 证明 |S| < N²/2
  6. 鸽巢：>N²/2 个"大格"（仅有大素数因子），故某行 i₀ 有 >N/2 个大格
  7. 注入论证：行 i₀ 中每个大格的大素数 q > M 互异（若 q(j₁)=q(j₂) 则 q|(j₂-j₁) 但 |j₂-j₁|<n<q）
  8. 乘积界：a+i₀ ≥ (M+1)^(#大格) ≥ (n²/1000)^((n+3)/2)
  9. 数值不等式：(n²/1000)^((n+3)/2) > (n/65536)^n + n 对 n≥2^15 成立
  10. 对称论证得 b 也满足，故 min{a,b} > (n/65536)^n = (cn)^n

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
| 1 | 纯元认知观察 | 0.9 | 描述这道题的结构：已知条件是什么？要证明什么？常数c的角色是什么？ | 题目要求证明存在c>0使得：若对所有i,j∈{0,...,n}有gcd(a+i,b+j)>1，则min{a,b}>(cn)^n。c是一个不依赖于a,b,n的绝对常数。核心是从gcd网格条件推出a,b的下界。 |
| 2 | 自由列举 | 0.8 | 列出所有可能的方法来证明min{a,b}的下界：归纳法、直接gcd操作、计数论证、筛法、概率论证等 | 可能方法：1)对n归纳 2)直接从gcd条件提取信息 3)考虑(n+1)×(n+1)网格中每格的共同素因子 4)筛法计数 5)用中国剩余定理构造 6)概率/密度论证 |
| 3 | 小尝试 | 0.6 | 试试直接方法：能否对n归纳？或直接从gcd(a,b)>1推出min{a,b}的下界？ | 直接归纳困难：从n到n+1需要控制新增的gcd条件。直接从gcd(a,b)>1只能得min≥2，远不够。条件是(n+1)²个gcd同时>1，信息量很大但直接提取困难。 |
| 4 | 思维操作引导 | 0.5 | 重新框定问题：考虑(n+1)×(n+1)网格，每格(a+i,b+j)都有一个共同素因子。思考哪些素数能覆盖很多格？ | 每格有一个共同素因子p。小素数p能覆盖约(N/p)²个格（因为p|a+i约N/p个i，p|b+j约N/p个j）。大素数覆盖的格少。关键是：如果小素数覆盖不了所有格，剩余格必须用大素数，而大素数迫使a+i很大。 |
| 5 | 推进 | 0.4 | 将素数分为小(≤M=n²/1000)和大(>M)。用筛法界证明小素数覆盖的格|S|<N²/2。需要哪些求和界？ | |S|≤Σ_{p≤M}(N/p+1)²=N²Σ(1/p²)+2NΣ(1/p)+|P|。需要：Σ(1/p²)≤47/100（素数平方倒数和收敛），Σ(1/p)≤clog₂(M+1)≤n/100（调和和的对数界），|P|≤M<N²/100。三项相加<47/100·N²+2/100·N²+1/100·N²=N²/2。 |
| 6 | 思维操作引导 | 0.4 | 小素数格<半，故>半是"大格"。用鸽巢找到某行i₀有>N/2个大格。证明这些大格的大素数互异，并推出乘积界。 | 鸽巢：N行中某行有>N/2个大格。对行i₀的每个大格j，取大素数q_j>M整除a+i₀和b+j。注入：若q_{j1}=q_{j2}=q，则q|(b+j1)且q|(b+j2)，故q|(j2-j1)，但|j2-j1|<n<q（因q>M≥n），矛盾。故互异。a+i₀≥∏q_j≥(M+1)^{#大格}≥(n²/1000)^{(n+3)/2}。 |
| 7 | 能量传递引导 | 0.3 | 你已有a+i₀≥(n²/1000)^((n+3)/2)。数值不等式(n²/1000)^((n+3)/2)>(n/65536)^n+n对n≥2^15成立。对称论证得b也满足。小n情况平凡。收尾！ | 大n：a>(n/65536)^n且b>(n/65536)^n，故min{a,b}>(n/65536)^n=(cn)^n，c=1/65536。小n(n<2^15)：min≥2>(n/65536)^n因n/65536<1。证毕！ |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.9
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

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
- problem_type: inequality_proof
- structure_features: (n+1)×(n+1)网格的gcd条件，需证明存在性常数c使得min{a,b}>(cn)^n；核心是将数论约束翻译为组合计数问题
- key_objects: 正整数a,b,n，gcd(a+i,b+j)，素因子分解，(n+1)×(n+1)网格，筛法计数，鸽巢原理，注入论证，乘积界

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["sieve_counting", "pigeonhole_principle", "case_splitting", "injection_argument", "product_bound", "numerical_estimation"]
- primary_pattern: sieve_counting
- knowledge_required: ["gcd与素因子分解", "筛法/容斥计数", "调和和的对数界", "素数平方倒数和收敛", "鸽巢原理", "注入与互异性论证", "指数增长比较"]
- key_insight: 将网格中每格的共同素因子按大小阈值n²/1000分类，用筛法证明小素数覆盖不到一半的格，鸽巢提取一行大素数格，注入论证证明大素数互异，乘积迫使a+i₀巨大

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 数论约束语言（gcd网格条件）
- translation_to: 组合计数语言（网格上素数覆盖的筛法计数）
- translation_type: constraint_to_counting（将整除约束翻译为覆盖计数问题，再用鸽巢和注入提取乘积结构）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "inequality_proof", ai_method_type: "direct_manipulation", gap_type: "method_problem_mismatch"}
- tell_small_concepts: ["grid_gcd_condition", "sieve_counting", "pigeonhole", "large_prime_divisor", "injection_distinctness", "product_bound", "numerical_comparison"]
- expected_ai_method: direct_manipulation（bare AI会尝试直接操作gcd条件或归纳法，看不到网格-筛法翻译）
- correct_method: sieve_counting with pigeonhole and injection（实际方法用筛法计数+鸽巢+注入论证）

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是。inequality_proof + direct_manipulation + method_problem_mismatch 完全覆盖。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是。所有值均为已有值，粒度一致。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。这道题的核心gap是方法-问题不匹配（直接操作gcd vs 筛法计数），已有维度能区分。
- [x] 如果发现拓扑分类需要进化，在此写出建议：

**拓扑进化建议**（如有）：无。当前拓扑分类足够。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**⚠️ 每个tell_hint_pair必须包含以下所有字段**：
- `qa_round`: int（对应QA序列的第几轮）
- `tell`: string（AI在这个位置的状态/分叉信号）
- `hint`: string（给AI的提示方向）
- `hint_level`: float（**⚠️ 0-1浮点数，禁止1-4整数**）
- `situation_type`: string（**⚠️ 只能取6个规范值之一**）
- `is_knowledge_bottleneck`: boolean（这轮是否是纯知识瓶颈）
- `tell_topology`: object（**⚠️ 每个pair都要有，不能全用profile级拓扑**）
  - `{problem_type, ai_method_type, gap_type}`
  - **不同轮次的pair可能有不同的拓扑**——比如R1是`(inequality_proof, direct_calculation, method_problem_mismatch)`，R2是`(structural_existence, case_by_case, structural_transformation)`
  - `is_knowledge_bottleneck=True`的pair，`gap_type`应该用`knowledge_gap`
- `tell_small_concepts`: array[string]（**⚠️ 每个pair都要有**，是这个tell特有的小概念信号词）

**同时提取全局(tell, hint)对**：
- `scope_type`: "path_feature"（路径特征型）或 "implicit"（蕴含型）
- `scope`: 具体范围描述
- `observation_point`: 蕴含型填Q编号，路径特征型填null
- `tell`: 全局tell
- `hint`: 全局hint
- `hint_level`: float（0-1）
- `generalizability`: "high/medium/low + 泛化描述"
- `why_not_visible_locally`: **必填字段，不能为None**。path_feature型和implicit型都要填。path_feature型填"完整路径特征为什么在局部视角看不到"；implicit型填"这个蕴含信息为什么在局部步骤中不可见"
- `tell_topology`: object（**⚠️ 每个全局pair也要有**）
- `tell_small_concepts`: array[string]（**⚠️ 每个全局pair也要有**）

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部(tell, hint)对详情**：

| qa_round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到存在性常数c的证明题，gcd网格条件，但未识别核心结构 | 描述题目结构：已知条件、目标、c的角色 | 0.9 | 纯元认知观察 | false | {inequality_proof, direct_manipulation, method_problem_mismatch} | ["existence_constant", "gcd_grid_condition", "min_lower_bound"] |
| 2 | AI列举方法但可能遗漏筛法计数 | 列举所有方法：归纳、直接gcd、计数、筛法、概率 | 0.8 | 自由列举 | false | {inequality_proof, enumeration_brute_force, search_space_estimation} | ["approach_enumeration", "sieve_method", "induction", "counting"] |
| 3 | AI尝试归纳/直接操作gcd，卡住 | 试直接方法：归纳或从gcd(a,b)>1推下界 | 0.6 | 小尝试 | false | {inequality_proof, direct_manipulation, method_problem_mismatch} | ["induction_attempt", "direct_gcd_manipulation", "stuck"] |
| 4 | AI卡在直接方法，需要重新框定为网格计数 | 重新框定：(n+1)×(n+1)网格，每格有共同素因子，哪些素数覆盖多 | 0.5 | 思维操作引导 | false | {inequality_proof, case_by_case, structural_transformation} | ["grid_reframing", "prime_coverage", "common_prime_divisor"] |
| 5 | AI已框定为网格，需要筛法计数知识来分大小素数 | 分素数为小(≤n²/1000)大(>M)，用筛法界证明小素数格<N²/2 | 0.4 | 推进 | true | {inequality_proof, enumeration_brute_force, knowledge_gap} | ["small_large_prime_split", "sieve_bound", "harmonic_sum", "cell_counting"] |
| 6 | AI有小素数格<半，需鸽巢+注入提取乘积结构 | 鸽巢找行i₀有>N/2大格，注入证明大素数互异，推乘积界 | 0.4 | 思维操作引导 | false | {inequality_proof, logical_deduction, structural_transformation} | ["pigeonhole", "injection_distinctness", "large_prime_product", "row_extraction"] |
| 7 | AI有乘积界，需数值不等式收尾 | 数值不等式+(n/65536)^n对比，对称论证，小n平凡，收尾 | 0.3 | 能量传递引导 | false | {inequality_proof, direct_calculation, method_translation} | ["numerical_inequality", "exponential_comparison", "case_split_small_large", "symmetric_bound"] |

**全局(tell, hint)对详情**：

1. path_feature型：
- scope: "complete solution path"
- observation_point: null
- tell: 从gcd网格条件到min{a,b}>(cn)^n的完整路径需要非显然的翻译：网格→筛法计数→鸽巢→注入→乘积界→数值比较
- hint: 关键翻译是从数论gcd条件到组合网格计数，再用鸽巢和注入提取乘积结构
- hint_level: 0.7
- generalizability: "high — 筛法→鸽巢→乘积的模式可泛化到许多基于网格的数论问题"
- why_not_visible_locally: "每个局部步骤（计数小素数、鸽巢、注入）看似独立技术，但完整路径——尤其是初始的gcd到网格计数的翻译——从任何单一步骤都看不到。按大小阈值n²/1000分素数的决定以及具体的调和和界，只有在看到最终数值不等式需要什么时才有动机。"
- tell_topology: {inequality_proof, direct_manipulation, method_problem_mismatch}
- tell_small_concepts: ["grid_reframing", "sieve_counting", "pigeonhole", "injection_distinctness", "product_bound", "numerical_comparison"]

2. implicit型：
- scope: "choice of prime threshold M = n²/1000"
- observation_point: "R5"
- tell: 阈值M=n²/1000不是任意的——它被校准使得(1)筛法界给出|S|<N²/2（需Σ1/p²<1/2对p≤M）且(2)乘积(M+1)^((n+3)/2)压倒(n/65536)^n
- hint: 选择素数分界阈值时，必须同时满足计数界和最终增长比较。n²/1000是平衡点。
- hint_level: 0.6
- generalizability: "medium — 校准原理可泛化但具体阈值取决于问题"
- why_not_visible_locally: "在R5中，AI看到大小素数分割但阈值M=n²/1000看似任意选择。这个具体值的原因——它必须同时使Σ1/p²<1/2（让筛法界给出<半）和使(M+1)^((n+3)/2)>(n/65536)^n（让最终不等式成立）——只有同时看R5和R7才能看到。"
- tell_topology: {inequality_proof, direct_calculation, method_translation}
- tell_small_concepts: ["threshold_calibration", "sieve_bound_balance", "exponential_comparison", "n_squared_over_1000"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "Bare AI会尝试直接操作gcd条件或对n归纳，看不到从gcd网格到筛法计数的翻译。即使考虑到网格，也会在阈值校准（M=n²/1000的选择需要同时满足筛法界和最终指数比较）和注入论证（利用q>n>|j₂-j₁|证明大素数互异）上卡住。"
- suitable_for_poc: ["POC-VMS-hint-injection", "POC-VMS-tell-detection", "POC-VMS-path-feature"]
- discriminates_levels: true

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

## Step 10: 入库ArangoDB [x]

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="329459"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa2014p6"
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
    '_key': '329459',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa2014p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa2014p6')
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
- problem_id: compfiles_usa2014p6
- solution_method_type: sieve_counting_pigeonhole
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。当前拓扑分类(inequality_proof + direct_manipulation + method_problem_mismatch)完全覆盖。
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
