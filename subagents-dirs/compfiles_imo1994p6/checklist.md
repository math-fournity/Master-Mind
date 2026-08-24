# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1994p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1994P6.lean
- **来源**: IMO 1994 P6
- **ArangoDB progress记录_key**: 329151（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1994P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：证明存在一个正整数集合A，使得对任意无限素数集合S，存在两个正整数m∈A和n∉A，每个都是S中k个不同元素的乘积，其中k≥2。
- 解答核心思路（1-2句话）：定义A={x>1 : p_{ω(x)-1} < minFac(x)}，其中p_i是第i个素数，ω(x)是x的不同素因子个数。对任意无限素数集S，枚举S中素数，选择k使得p_{k-1}=p_S(1)（S中第二小的素数的全局索引+1），取m为从p_S(2)开始的k个连续素数乘积（m∈A），n为从p_S(1)开始的k个连续素数乘积（n∉A）。
- 解答关键步骤列表：
  1. 定义A = {x > 1 : primes_iso(ω(x)-1) < minFac(x)}，即第(ω(x)-1)个素数小于x的最小素因子
  2. 对任意无限素数集S，按递增枚举为p_S(0) < p_S(1) < p_S(2) < ...
  3. 选择k = (p_S(1)在全局素数枚举中的索引) + 1，保证k≥2
  4. 关键引理1：对从p_S(i)开始的k个连续素数乘积，ω = k，故primes_iso(ω-1) = primes_iso(k-1) = p_S(1)
  5. 关键引理2：该乘积的minFac = p_S(i)（起始素数）
  6. m = 从p_S(2)开始的k个素数乘积：minFac(m)=p_S(2) > p_S(1) = primes_iso(ω(m)-1)，故m∈A
  7. n = 从p_S(1)开始的k个素数乘积：minFac(n)=p_S(1) = primes_iso(ω(n)-1)，不满足严格不等式，故n∉A

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
| 1 | 纯元认知观察 | 0.3 | 描述这个问题的逻辑结构：量词的嵌套顺序是什么？A需要满足什么条件？ | 问题是∃A∀S∃k,m,n的结构。A是一个固定的正整数集合，需要对任意无限素数集S，存在k≥2和m∈A, n∉A，使得m和n都是S中k个不同素数的乘积。关键难点是A必须预先固定，但对所有S都有效。 |
| 2 | 自由列举 | 0.5 | 列出所有可能构造集合A的方向。哪些数论性质可以用来分类正整数？ | 可以基于：ω(x)（素因子个数的奇偶性）、x的大小阈值、最小素因子minFac(x)、最大素因子、素因子的某种加权和、x的模某个数的余数等。但需要注意A必须对所有S同时有效。 |
| 3 | 小尝试 | 0.3 | 尝试定义A = {x : ω(x)为偶数}，验证是否可行。 | 不可行。因为对给定的S和k，S中k个不同素数的乘积都有ω=k，所以它们要么全在A中要么全不在A中，无法同时找到m∈A和n∉A。这说明仅基于ω的分类不够。 |
| 4 | 思维操作引导 | 0.6 | 在S中k个不同素数的乘积中，哪些性质可以随选取的素数不同而变化？思考连续取k个素数的情况。 | 如果取S中连续的k个素数（按递增排列），不同起始位置的乘积有不同的最小素因子minFac。例如从p_S(i)开始取k个，minFac = p_S(i)。这是一个可以变化的量。关键是要把minFac和ω结合起来。 |
| 5 | 思维操作引导 | 0.7 | 如何将ω(x)和minFac(x)结合，构造一个分类边界？考虑用全局素数枚举来索引。提示：定义A = {x>1 : p_{ω(x)-1} < minFac(x)}，其中p_i是第i个素数。 | 定义A = {x > 1 : p_{ω(x)-1} < minFac(x)}。这里p_{ω(x)-1}是全局第(ω(x)-1)个素数，minFac(x)是x的最小素因子。这个分类边界取决于x有多少个素因子（决定比较哪个全局素数）和x的最小素因子是什么（局部信息）。 |
| 6 | 推进 | 0.4 | 给定A的定义，对任意无限素数集S，如何选择k并找到m∈A和n∉A？ | 枚举S为p_S(0)<p_S(1)<...，选k = p_S(1)在全局素数枚举中的索引+1。则p_{k-1} = p_S(1)。取m = p_S(2)·...·p_S(k+1)（从p_S(2)开始k个），n = p_S(1)·...·p_S(k)（从p_S(1)开始k个）。两者ω=k，故p_{ω-1}=p_{k-1}=p_S(1)。 |
| 7 | 能量传递引导 | 0.3 | 验证：m∈A吗？n∉A吗？k≥2吗？ | minFac(m)=p_S(2) > p_S(1) = p_{ω(m)-1}，故m∈A ✓。minFac(n)=p_S(1) = p_S(1) = p_{ω(n)-1}，不满足严格不等式，故n∉A ✓。k≥2因为p_S(0)<p_S(1)所以p_S(1)的全局索引≥1，k≥2 ✓。证明完成。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1,R2,R6,R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4,R5）
- level_sum: 0.3+0.5+0.3+0.6+0.7+0.4+0.3 = 3.1
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R5（关键洞察：定义A = {x>1 : p_{ω(x)-1} < minFac(x)}）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R4（识别minFac为可变量，需要思维操作引导）

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
- problem_type: structural_existence（存在性构造：证明存在集合A满足性质）
- structure_features: ∃A∀S∃k,m,n的嵌套量词结构；A需预先固定但对所有无限素数集S有效；m和n都是S中k个不同素数的乘积，k≥2；关键约束是同一S同一k下需要一个在A中一个不在A中
- key_objects: [正整数集合A, 无限素数集合S, 素数乘积, ω(x)（不同素因子个数）, minFac(x)（最小素因子）, 全局素数枚举primes_iso, 滑动窗口（连续k个素数的乘积）]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["existence_to_construction（从存在性命题转化为显式构造）", "global_local_bridge（全局素数枚举与局部最小素因子的桥接）", "sliding_window（连续素数块的滑动窗口技术）", "comparison_based_classification（基于比较的分类边界构造）", "failed_attempt_informs_direction（失败尝试揭示方向）"]
- primary_pattern: global_local_bridge（全局-局部桥接：用全局素数索引和局部最小素因子的比较来定义分类边界）
- knowledge_required: ["素数因子分解", "ω(x)（不同素因子个数）", "minFac(x)（最小素因子）", "素数枚举与索引", "有限素数乘积的性质", "严格不等式"]
- key_insight: 定义A = {x > 1 : p_{ω(x)-1} < minFac(x)}——比较全局第(ω(x)-1)个素数与x的最小素因子，使得分类边界随素因子个数移动，从而同一S中不同起始位置的k个素数乘积可以分属A内外

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 存在性命题（∃A使得∀S ∃m∈A, n∉A满足条件）——抽象的量词嵌套结构
- translation_to: 显式构造（A = {x > 1 : p_{ω(x)-1} < minFac(x)} + 滑动窗口选m,n）——具体的比较分类与连续块技术
- translation_type: existence_to_construction（从存在性证明翻译为显式构造，核心是将"什么样的A能工作"翻译为"用全局-局部比较定义A"）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: enumeration_brute_force, gap_type: structural_transformation}
- tell_small_concepts: ["global_local_comparison", "omega_minFac_comparison", "sliding_window_consecutive_primes", "k_choice_global_index_bridge", "existence_to_explicit_construction", "strict_inequality_boundary"]
- expected_ai_method: bare AI会尝试基于单一属性（如ω(x)的奇偶性、大小阈值）定义A，或尝试迭代构造A。不会想到将全局素数索引与局部最小素因子比较来定义分类边界。
- correct_method: 定义A = {x > 1 : p_{ω(x)-1} < minFac(x)}，利用全局-局部比较创建随ω移动的分类边界，再用滑动窗口（连续k个素数的乘积）和精心选择的k（= p_S(1)的全局索引+1）找到m∈A和n∉A。

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ → 可以。problem_type=structural_existence已有；ai_method_type=enumeration_brute_force已有（bare AI会枚举简单分类方式）；gap_type=structural_transformation已有（需要从存在性结构转化为显式比较构造）。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ → 一致。三个维度都用了已有的抽象/中等粒度值。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ → 足够。这道题的核心特征（全局-局部桥接）通过structural_transformation gap_type和tell_small_concepts中的"global_local_comparison"可以充分表达。
- [x] 如果发现拓扑分类需要进化，在此写出建议： → 无需进化。现有拓扑分类体系可以很好地容纳这道题。

**拓扑进化建议**（如有）：无。现有分类体系足够。

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
- 全局pair中path_feature型: 1 个，implicit型: 2 个

### 局部tell_hint_pairs

**R1** (纯元认知观察, level=0.3):
- tell: AI识别了∃A∀S∃k,m,n的嵌套量词结构，但尚未意识到A必须预先固定但对所有S有效的核心张力
- hint: 描述这个问题的逻辑结构：量词的嵌套顺序是什么？A需要满足什么条件？
- is_knowledge_bottleneck: false
- tell_topology: {problem_type: structural_existence, ai_method_type: logical_deduction, gap_type: structural_transformation}
- tell_small_concepts: ["quantifier_nesting_structure", "fixed_A_vs_arbitrary_S_tension"]

**R2** (自由列举, level=0.5):
- tell: AI列举了通用数论性质（ω奇偶性、大小阈值、模余数等），但未识别全局-局部比较方向
- hint: 列出所有可能构造集合A的方向。哪些数论性质可以用来分类正整数？
- is_knowledge_bottleneck: false
- tell_topology: {problem_type: structural_existence, ai_method_type: enumeration_brute_force, gap_type: search_space_estimation}
- tell_small_concepts: ["generic_property_listing", "omega_parity_candidate", "size_threshold_candidate"]

**R3** (小尝试, level=0.3):
- tell: AI尝试A={x:ω(x)为偶数}失败，发现同一S同一k的所有乘积ω相同，无法区分m和n
- hint: 尝试定义A = {x : ω(x)为偶数}，验证是否可行。
- is_knowledge_bottleneck: false
- tell_topology: {problem_type: structural_existence, ai_method_type: enumeration_brute_force, gap_type: method_problem_mismatch}
- tell_small_concepts: ["omega_parity_failure", "same_omega_for_same_k", "need_variable_property_among_k_products"]

**R4** (思维操作引导, level=0.6):
- tell: AI识别出minFac随滑动窗口起始位置变化，是k个素数乘积中可变化的量
- hint: 在S中k个不同素数的乘积中，哪些性质可以随选取的素数不同而变化？思考连续取k个素数的情况。
- is_knowledge_bottleneck: false
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: method_translation}
- tell_small_concepts: ["minFac_varies_with_start", "sliding_window_identification", "variable_property_discovery"]

**R5** (思维操作引导, level=0.7) **知识瓶颈**:
- tell: AI需要关键构造A = {x>1 : p_{ω(x)-1} < minFac(x)}，将全局素数索引与局部最小素因子比较
- hint: 如何将ω(x)和minFac(x)结合，构造一个分类边界？考虑用全局素数枚举来索引。提示：定义A = {x>1 : p_{ω(x)-1} < minFac(x)}。
- is_knowledge_bottleneck: true
- tell_topology: {problem_type: structural_existence, ai_method_type: logical_deduction, gap_type: knowledge_gap}
- tell_small_concepts: ["global_local_comparison", "omega_minFac_comparison", "primes_iso_index_bridge", "comparison_boundary_construction"]

**R6** (推进, level=0.4):
- tell: AI需要将k的选择与p_S(1)的全局索引连接，使比较边界p_{k-1}=p_S(1)
- hint: 给定A的定义，对任意无限素数集S，如何选择k并找到m∈A和n∉A？
- is_knowledge_bottleneck: false
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: ["k_equals_global_index_plus_1", "sliding_window_m_n_selection", "consecutive_prime_blocks"]

**R7** (能量传递引导, level=0.3):
- tell: AI验证m∈A（minFac(m)>p_{ω-1}）、n∉A（minFac(n)=p_{ω-1}不满足严格不等式）、k≥2
- hint: 验证：m∈A吗？n∉A吗？k≥2吗？
- is_knowledge_bottleneck: false
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: method_translation}
- tell_small_concepts: ["strict_inequality_verification", "m_in_A_proof", "n_not_in_A_proof", "k_ge_2_proof"]

### 全局tell_hint_pairs

**Global 1 (path_feature型)**:
- scope: "完整解答路径：从存在性命题到显式构造A的全程"
- observation_point: null
- tell: 解答路径需要桥接全局素数枚举与局部最小素因子——通过比较p_{ω(x)-1}与minFac(x)构造分类边界，使同一S中不同起始位置的k个素数乘积可分属A内外
- hint: 定义A = {x > 1 : p_{ω(x)-1} < minFac(x)}，利用全局-局部比较创建随ω移动的分类边界
- hint_level: 0.7
- generalizability: "high - 全局-局部桥接模式适用于其他需要固定对象对所有实例有效的存在性问题"
- why_not_visible_locally: "在任何单一步骤中，全局素数索引与局部最小素因子之间的连接不可见——每一步只揭示一面（全局枚举或局部性质），桥接需要同时看到两面并理解它们的比较关系，这在局部视角中无法浮现"
- tell_topology: {problem_type: structural_existence, ai_method_type: logical_deduction, gap_type: structural_transformation}
- tell_small_concepts: ["global_local_bridge", "existence_to_construction_path", "comparison_based_classification"]

**Global 2 (implicit型)**:
- scope: "R3失败尝试隐含揭示正确方向"
- observation_point: "R3"
- tell: ω奇偶性分类的失败隐含揭示：分类边界必须使用在相同S相同k的乘积中会变化的性质，而minFac随滑动窗口起始位置变化
- hint: 从失败中提取：哪些性质在相同S相同k的乘积中会变化？minFac随起始位置变化
- hint_level: 0.5
- generalizability: "medium - 从失败分类尝试中学习正确方向的模式具有中等泛化性"
- why_not_visible_locally: "在R3中，失败只显示什么不行；minFac是正确可变性质的洞察需要将失败与滑动窗口结构连接，这在失败本身中不可见"
- tell_topology: {problem_type: structural_existence, ai_method_type: enumeration_brute_force, gap_type: method_problem_mismatch}
- tell_small_concepts: ["failed_attempt_informs_direction", "variable_property_requirement", "minFac_as_key_variable"]

**Global 3 (implicit型)**:
- scope: "R6中k的选择是连接全局与局面的关键铰链"
- observation_point: "R6"
- tell: k的特定选择（= p_S(1)的全局索引+1）是使全局-局部比较工作的关键铰链——k决定比较哪个全局素数，选为使p_{k-1}=p_S(1)
- hint: 选择k使p_{k-1}=p_S(1)，让比较边界与S的第二小素数对齐
- hint_level: 0.6
- generalizability: "medium - 选择参数使全局与局部索引对齐的模式适用于此类构造问题"
- why_not_visible_locally: "在R6中，验证步骤只显示选定的k有效；为什么选择这个特定k的推理——连接p_S(1)的全局索引到比较边界——在验证本身中不可见"
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: ["k_choice_global_index_bridge", "parameter_alignment_for_comparison", "linchpin_parameter_choice"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "Bare AI会尝试基于单一属性（如ω(x)奇偶性、大小阈值、模余数）定义A，发现同一S同一k的所有乘积共享相同ω后陷入困境。不会想到将全局素数索引primes_iso与局部最小素因子minFac比较来定义分类边界。即使想到minFac可变，也不会想到用ω(x)决定比较哪个全局素数来构造随ω移动的分类边界。"
- suitable_for_poc: ["POC-VMS-tell-extraction: 测试系统能否从AI的失败尝试（ω奇偶性）中识别出'需要可变性质'的tell并检索到全局-局部比较方向", "POC-VMS-hint-injection: 测试注入全局-局部比较hint（定义A = {x>1 : p_{ω(x)-1} < minFac(x)}）后AI能否完成构造", "POC-VMS-knowledge-bottleneck: 测试R5知识瓶颈处的tell提取——系统能否识别这是纯知识gap而非思维gap"]
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
2. 更新`problem_extraction_progress`集合中`_key="329151"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1994p6"
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
    '_key': '329151',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1994p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1994p6')
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
- problem_id: compfiles_imo1994p6
- solution_method_type: existence_to_explicit_construction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3（1个path_feature型 + 2个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有分类体系（structural_existence / enumeration_brute_force / structural_transformation / knowledge_gap / method_problem_mismatch / method_translation / search_space_estimation / direct_calculation / logical_deduction）足够容纳这道题的所有tell
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
