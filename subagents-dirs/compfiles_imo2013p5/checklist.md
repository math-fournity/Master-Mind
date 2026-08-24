# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2013p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2013P5.lean
- **来源**: IMO 2013 P5
- **ArangoDB progress记录_key**: 329227（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2013P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设 ℚ>₀ 为正有理数集合。f: ℚ>₀ → ℝ 满足：(1) f(x)·f(y) ≥ f(xy)（次可乘性），(2) f(x+y) ≥ f(x)+f(y)（超可加性）。已知存在有理数 a > 1 使 f(a) = a，证明 f(x) = x 对所有 x ∈ ℚ>₀ 成立。
- 解答核心思路（1-2句话）：通过次可乘性和超可加性逐步建立下界链（f(1)≥1 → f(n)≥n → f(q)>0 → f(x)>x-1），再用幂比较解析引理得到 x≤f(x)（x>1），最后用 a^N 作为"桥"通过挤压证明 f(x)=x（x>1），再通过整数缩放推广到所有正有理数。
- 解答关键步骤列表：
  1. **le_of_all_pow_lt_succ**（解析引理）：若 1<x, 0<y 且对所有正整数 n 有 x^n-1 < y^n，则 x ≤ y。证明用反证法：若 x>y，取 z=max(y,1)，则 (x/z)^n 无界，存在 n 使 x^n > 2z^n ≥ z^n+1 ≥ y^n+1，矛盾。
  2. **f_pos_of_pos**：f(q)>0 对所有正有理数 q。利用 q = q.num/q.den，f(q.num) ≤ f(q)·f(q.den)，而 f(n)≥n（H4）保证 f(q.num)>0 和 f(q.den)>0。
  3. **fx_gt_xm1**：对 x≥1，f(x) > x-1。用取整分解 x = ⌊x⌋ + (x-⌊x⌋)，H4 给 f(⌊x⌋)≥⌊x⌋，f_pos 给 f(x-⌊x⌋)>0，超可加性合并。
  4. **pow_f_le_f_pow**：f(x^n) ≤ (f(x))^n，由次可乘性归纳。
  5. **fixed_point_of_pos_nat_pow**：f(a^n) = a^n。结合 H5（a^n ≤ f(a^n)）和 pow_f_le_f_pow（f(a^n) ≤ f(a)^n = a^n）。
  6. **fixed_point_of_gt_1**：对 x>1，f(x)=x。选 N 使 a^N > 1+x，则 a^N-x > 1。由超可加性：f(a^N) ≥ f(x)+f(a^N-x) ≥ x+(a^N-x) = a^N = f(a^N)，等号成立故 f(x)=x。
  7. **主证明**：先推导 H3（n·f(x)≤f(nx)，超可加性归纳）、H4（n≤f(n)，由 f(1)≥1 和 H3）、H5（x≤f(x) 对 x>1，用 fx_gt_xm1 + pow_f_le_f_pow + 解析引理）。再证 f(nx)=n·f(x)（H3 下界 + 次可乘性上界，整数 n≥2 时 f(n)=n）。最后对任意正有理 x，取大整数 n 使 nx>1，则 f(nx)=nx=n·f(x)，约去 n 得 f(x)=x。

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
| 1 | 纯元认知观察 | 0.8 | 观察这道题的结构：已知条件是什么？要证明什么？两个不等式条件分别给出了f的什么性质？ | 条件(1) f(x)f(y)≥f(xy) 是次可乘性，条件(2) f(x+y)≥f(x)+f(y) 是超可加性。已知f(a)=a（a>1）是一个不动点。要证明f是恒等函数。两个条件一个给上界一个给下界方向的约束。 |
| 2 | 自由列举 | 0.7 | 列出所有可能的研究方向：从这两个不等式和不动点条件出发，你能想到哪些途径来证明f(x)=x？ | (a)直接代入特殊值；(b)用不动点a生成更多不动点（如a的幂）；(c)先建立整数上的下界f(n)≥n；(d)用超可加性做归纳；(e)用次可乘性做幂的上界；(f)缩放法把一般x归结到x>1的情形；(g)挤压法：同时建立上下界。 |
| 3 | 小尝试 | 0.4 | 试着从条件出发推导一些基本性质。令y=1看看能得到什么？能否用超可加性归纳出f(n)的下界？ | 令y=1：f(x)f(1)≥f(x)，若f(x)>0则f(1)≥1。超可加性归纳：f(2)≥2f(1)≥2，f(n)≥n。但只有下界，不知道如何得到上界。卡在这里——下界链f(1)≥1→f(n)≥n看起来有用但不够。 |
| 4 | 思维操作引导 | 0.5 | 你已经有了f(n)≥n的下界。现在执行这个思维操作：用不动点a和次可乘性生成上界。具体地，f(a^n)和(f(a))^n之间有什么关系？结合下界能得出什么？ | 由次可乘性归纳：f(a^n)≤f(a)^n=a^n。又由f(n)≥n可推出f(q)>0（利用q=num/den分解），进而f(x)>x-1（取整分解+超可加性）。对x^n用f(x^n)>x^n-1和f(x^n)≤f(x)^n，得x^n-1<f(x)^n对所有n成立。 |
| 5 | 思维操作引导 | 0.4 | 你得到了x^n-1<f(x)^n对所有正整数n成立。现在执行关键思维操作：如何从这个"对所有n成立"的不等式推出x≤f(x)？想想如果x>f(x)会发生什么。 | 如果x>f(x)>0，则(x/f(x))^n无界增长，存在n使x^n>2·f(x)^n≥f(x)^n+1，即x^n-1>f(x)^n，矛盾！所以x≤f(x)对x>1成立。这是解析幂比较论证。 |
| 6 | 思维操作引导 | 0.5 | 现在你知道x≤f(x)对x>1成立，且a^n是不动点。执行这个思维操作：选N使a^N>1+x，把a^N拆成x+(a^N-x)，用超可加性挤压。能否得到f(x)=x？ | a^N>1+x意味着a^N-x>1。超可加性：f(a^N)≥f(x)+f(a^N-x)≥x+(a^N-x)=a^N。但f(a^N)=a^N，所以a^N≥f(x)+(a^N-x)≥a^N，等号成立，f(x)=x。对x>1证毕！ |
| 7 | 能量传递引导 | 0.7 | 太好了！你已经证明了x>1时f(x)=x。最后一步：对于0<x≤1的正有理数，如何用缩放把问题归结到已证情形？把所有片段组装起来。 | 取大整数n使nx>1。需证f(nx)=n·f(x)：超可加性给n·f(x)≤f(nx)（下界），次可乘性+f(n)=n（n≥2时已证）给f(nx)≤f(n)·f(x)=n·f(x)（上界）。故f(nx)=n·f(x)=nx，约去n得f(x)=x。完整证明链：f(1)≥1→f(n)≥n→f(q)>0→f(x)>x-1→幂比较得x≤f(x)→a^N桥挤压得f(x)=x(x>1)→缩放推广到所有正有理数。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 3
- knowledge_rounds（思维操作引导的轮数）: 3
- level_sum: 0.8+0.7+0.4+0.5+0.4+0.5+0.7 = 4.0
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R3"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

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
- problem_type: characterization（证明满足给定不等式条件的函数必为恒等函数——刻画问题）
- structure_features: 两个函数不等式（次可乘性+超可加性）联合约束+一个不动点条件，目标是唯一刻画f。结构上需要从下界链和上界链双向夹逼。
- key_objects: [正有理数域ℚ>₀, 函数f:ℚ>₀→ℝ, 不动点a>1, 正整数n, 幂a^n, 取整函数⌊x⌋]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["bounding_from_both_sides"（双向夹逼：下界链+上界链）, "fixed_point_propagation"（不动点传播：从a到a^n到所有x>1）, "bridge_argument"（桥论证：用a^N作为中介连接已知与未知）, "analytic_power_comparison"（解析幂比较：用指数增长率差异做反证）, "scaling_reduction"（缩放归约：把一般情形归结到已证情形）, "chain_building"（逐步建立推导链）]
- primary_pattern: bounding_from_both_sides（双向夹逼是整个证明的主导思维模式——次可乘性给上界，超可加性给下界，不动点连接两者）
- knowledge_required: ["次可乘性与超可加性的基本性质", "自然数归纳法", "指数函数增长率比较（(x/y)^n无界增长）", "取整函数分解", "有理数的分子分母表示", "挤压论证"]
- key_insight: 用a^N作为桥：因为f(a^N)=a^N且a^N=x+(a^N-x)，超可加性挤压出f(x)=x对所有x>1成立——不动点不仅是起点，更是连接已知与未知的桥梁。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 逐点不等式操作（直接对每个x用不等式条件做代数变形，只能得到逐点上下界）
- translation_to: 幂比较解析论证+桥挤压论证（把逐点界通过幂运算提升为全局界，再用不动点作为桥做挤压）
- translation_type: structural（从局部逐点操作到全局结构论证的翻译——需要看到整个推导链的结构而非单个步骤）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "direct_manipulation", gap_type: "structural_transformation"}
- tell_small_concepts: ["sub_multiplicativity", "super_additivity", "fixed_point", "power_comparison", "bridge_argument", "squeeze", "scaling_reduction", "lower_bound_chain"]
- expected_ai_method: direct_manipulation（bare AI会直接对不等式做代数变形，尝试逐点推导f(x)=x，能建立下界但看不到如何通过幂比较和桥论证获得上界）
- correct_method: bounding_and_squeeze（系统性地建立下界链，用幂比较解析引理获得全局下界，再用不动点a^N作为桥通过超可加性挤压得到等式，最后缩放推广）

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是。problem_type=characterization（已有），ai_method_type=direct_manipulation（已有），gap_type=structural_transformation（已有）。三个维度都能归入已有类别。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是。characterization与structural_existence/discrete_combinatorial同级，direct_manipulation与enumeration_brute_force/continuous_analytic同级，structural_transformation与method_translation/search_space_estimation同级。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。这道题的独特性通过small_concepts（bridge_argument, power_comparison, squeeze等）区分，不需要新拓扑维度。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。现有拓扑分类体系完全够用。

**拓扑进化建议**（如有）：无。现有分类体系充分覆盖本题。

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
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 2 个，implicit型: 1 个

**局部tell_hint_pairs详情**：

| qa_round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对两个函数不等式+不动点条件，需要识别这是刻画问题但尚未看到双向夹逼的结构 | 观察题目结构：两个条件分别给什么方向的约束？ | 0.8 | 纯元认知观察 | false | {problem_type:"characterization", ai_method_type:"direct_manipulation", gap_type:"method_problem_mismatch"} | ["functional_inequality","sub_multiplicativity","super_additivity","fixed_point_condition"] |
| 2 | AI列出方向但未识别"不动点传播"和"桥论证"是关键路径 | 列出所有可能方向，特别关注如何利用不动点a | 0.7 | 自由列举 | false | {problem_type:"characterization", ai_method_type:"enumeration_brute_force", gap_type:"search_space_estimation"} | ["direct_substitution","induction","bounding","fixed_point_propagation","scaling"] |
| 3 | AI推导出f(n)≥n下界链后卡住——只有下界没有上界，不知道如何继续 | 令y=1推导f(1)≥1，用超可加性归纳f(n)≥n | 0.4 | 小尝试 | true | {problem_type:"characterization", ai_method_type:"direct_calculation", gap_type:"knowledge_gap"} | ["lower_bound","f(1)_geq_1","f(n)_geq_n","positivity","stuck_without_upper_bound"] |
| 4 | AI需要将逐点下界通过幂运算提升为全局界——这是从局部到全局的关键翻译 | 用次可乘性得f(a^n)≤a^n，结合f(x)>x-1对x^n使用，得x^n-1<f(x)^n | 0.5 | 思维操作引导 | false | {problem_type:"characterization", ai_method_type:"algebraic_identity", gap_type:"structural_transformation"} | ["power_of_fixed_point","sub_multiplicativity_upper_bound","pointwise_to_global"] |
| 5 | AI有x^n-1<f(x)^n对所有n但不知道如何推出x≤f(x)——需要解析幂比较的反证思维 | 如果x>f(x)则(x/f(x))^n无界，存在n使x^n>2f(x)^n，矛盾 | 0.4 | 思维操作引导 | false | {problem_type:"characterization", ai_method_type:"logical_deduction", gap_type:"method_translation"} | ["power_comparison_lemma","exponential_growth_rate","proof_by_contradiction"] |
| 6 | AI知道x≤f(x)和a^n是不动点但看不到如何连接——桥论证是关键结构洞 | 选N使a^N>1+x，拆a^N=x+(a^N-x)，超可加性挤压 | 0.5 | 思维操作引导 | false | {problem_type:"characterization", ai_method_type:"direct_manipulation", gap_type:"structural_transformation"} | ["bridge_argument","a^N_intermediary","squeeze_via_super_additivity"] |
| 7 | AI已证x>1情形，需要缩放推广到所有正有理数——组装完整证明链 | 取大n使nx>1，证f(nx)=n·f(x)用双向夹逼，约去n | 0.7 | 能量传递引导 | false | {problem_type:"characterization", ai_method_type:"direct_manipulation", gap_type:"method_translation"} | ["scaling_reduction","integer_multiplication_commutativity","complete_chain_assembly"] |

**全局tell_hint_pairs详情**：

| # | scope_type | scope | observation_point | tell | hint | hint_level | generalizability | why_not_visible_locally | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | path_feature | 完整推导链：f(1)≥1→f(n)≥n→f(q)>0→f(x)>x-1→幂比较得x≤f(x)→桥挤压得f(x)=x→缩放推广 | null | AI看到各个不等式操作但看不到这些步骤构成一条从基础下界到完整刻意的系统性推导链 | 系统性地构建推导链：先建立整数下界，再正性，再逐点界，再幂比较全局界，最后桥挤压 | 0.6 | high——链式构建模式适用于许多函数不等式问题 | 每个单独步骤（推导f(1)≥1、推导f(n)≥n等）看起来是独立的不等式操作。这些步骤构成一条通向最终结果的刻意链条这一事实，只有在看到完整路径时才可见。从任何单个步骤，你无法看到链条通向哪里。 | {problem_type:"characterization", ai_method_type:"direct_manipulation", gap_type:"structural_transformation"} | ["derivation_chain","lower_bound_propagation","positivity_from_integer_bounds","chain_building"] |
| 2 | implicit | 解析幂比较引理的使用：x^n-1<y^n对所有n成立蕴含x≤y | R5 | AI推导出f(x)>x-1和f(x^n)≤f(x)^n但没有识别出组合后得到x^n-1<f(x)^n对所有n，进而由解析引理推出x≤f(x) | 组合逐点界f(x^n)>x^n-1与幂界f(x^n)≤f(x)^n得x^n-1<f(x)^n对所有n。若x>f(x)则(x/f(x))^n无界，矛盾。故x≤f(x) | 0.3 | medium——幂比较技巧特定于涉及乘法结构和增长率的问题 | 解析引理（x^n-1<y^n对所有n⟹x≤y）不是标准代数恒等式——它需要认识到指数增长率可以比较，这是在任何单个代数操作步骤中不可见的解析洞察。逐点界和幂界之间的联系也只有在同时看到两者时才明显。 | {problem_type:"characterization", ai_method_type:"direct_calculation", gap_type:"knowledge_gap"} | ["power_comparison_lemma","exponential_growth_rate","analytic_limit_argument","combining_bounds"] |
| 3 | path_feature | 桥论证：用a^N作为中介证明f(x)=x对所有x>1 | null | AI知道a^n是不动点且有下界f(x)≥x但看不到如何连接——通过a^N=x+(a^N-x)的桥不可见 | 选N使a^N>1+x，则a^N-x>1。写a^N=x+(a^N-x)，超可加性：f(a^N)≥f(x)+f(a^N-x)≥x+(a^N-x)=a^N=f(a^N)，等号成立故f(x)=x | 0.2 | high——通过已知不动点作为中介的桥/挤压论证是函数方程中的一般技巧 | 桥论证需要同时知道a^N是不动点、f(x)≥x和f(a^N-x)≥a^N-x（都>1）、以及超可加性提供挤压。没有单个步骤揭示这一点——这是关于如何利用已知不动点作为中介到达未知值的结构洞察。 | {problem_type:"characterization", ai_method_type:"direct_manipulation", gap_type:"structural_transformation"} | ["bridge_argument","squeeze_via_super_additivity","fixed_point_as_intermediary","a^N_decomposition"] |

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会推导出f(1)≥1和f(n)≥n的下界链，可能还能得到f(q)>0，但会在建立上界时卡住。它不会想到：(1)用幂比较解析引理（x^n-1<y^n对所有n⟹x≤y）把逐点界提升为全局界；(2)用a^N作为桥通过超可加性挤压得到f(x)=x。bare AI会反复尝试直接代数变形，无法突破从下界到等式的鸿沟。
- suitable_for_poc: ["tell_hint_validation"（验证tell_hint_pair能否引导AI走通正确路径）, "topology_matching"（验证拓扑匹配能否区分direct_manipulation与bounding_and_squeeze）, "knowledge_bottleneck_detection"（R3的知识瓶颈检测——AI只有下界没有上界）, "implicit_tell_detection"（验证implicit型tell——解析幂比较引理——能否被识别）]
- discriminates_levels: true（这道题能区分高水平AI——能看到桥论证和幂比较——与低水平AI——只能做直接代数变形）

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
- [x] answer（=f(x) = x for all x ∈ ℚ>₀）
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
- [x] global_tell_hint_pairs（3个pair，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**将完整JSON写入工作目录的 `profile.json` 文件** → 已写入 `subagents-dirs/compfiles_imo2013p5/profile.json`

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
2. 更新`problem_extraction_progress`集合中`_key="329227"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2013p5"
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
    '_key': '329227',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2013p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2013p5')
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
- problem_id: compfiles_imo2013p5
- solution_method_type: bounding_and_squeeze
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3（2个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否。现有分类体系（characterization / direct_manipulation / structural_transformation等）完全覆盖本题，粒度一致，无需新增维度。
- 是否遇到异常: 否。所有步骤顺利完成，JSON验证通过，ArangoDB入库和验证均成功。

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
