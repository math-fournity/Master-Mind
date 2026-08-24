# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1991p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1991P6.lean
- **来源**: IMO 1991 P6
- **ArangoDB progress记录_key**: 329137（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1991P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：给定任意实数 a > 1，构造一个有界无穷实数序列 x₀, x₁, x₂, ... 使得对所有不同的非负整数 i, j，有 |xᵢ - xⱼ|·|i - j|ᵃ ≥ 1。
- 解答核心思路（1-2句话）：构造 x_n = (2√2 + 2)·{n√2}（{·}为小数部分函数）。有界性来自{n√2}∈[0,1)；分离性来自√2的无理性给出的丢番图逼近下界 |{i√2}-{j√2}| > 1/(2(√2|i-j|+1))。
- 解答关键步骤列表：
  1. 构造 x_n = (2√2 + 2)·fract(√2·n)，其中 fract 是小数部分函数
  2. 证明有界性：|x_n| ≤ 2√2+2（因为 fract(√2·n) ∈ [0,1)）
  3. 引理 fract_sqrt_two_mul_gt：fract(√2·k) > 1/(2(√2·k+1))——利用 2k² 不是完全平方数，(k√2-y)(k√2+y) = 2k²-y² ≥ 1
  4. 引理 one_sub_fract_sqrt_two_mul_gt：1 - fract(√2·k) > 1/(2(√2·k+1))——类似地利用 (y+1)²-2k² ≥ 1
  5. 引理 abs_fract_sqrt_two_mul_sub_fract_sqrt_two_mul：|fract(√2·i) - fract(√2·j)| > 1/(2(√2·(i-j)+1))——利用 fract_sub_eq 将差分转化为 fract(√2·(i-j))
  6. 主证明：组合分离下界与缩放常数 C=2√2+2=2(√2+1)，验证 |xᵢ-xⱼ|·|i-j|^a ≥ C·|i-j|^a/(2(√2+1)|i-j|) = |i-j|^{a-1} ≥ 1

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
| 1 | 纯元认知观察 | 0.8 | 观察这道题的结构。我们需要构造一个有界序列，使得任意两个不同项的距离 |xᵢ-xⱼ| ≥ |i-j|^{-a}。这个约束告诉我们什么？a>1的条件在其中扮演什么角色？ | 序列必须有界（所有值在[-C,C]内），但任意两个值必须至少相差 |i-j|^{-a}。由于 a>1，所需分离随距离衰减得比 1/n 快，因此无限多个点有可能塞进一个有界区间内。a>1 是关键——如果 a≤1，点会太密无法有界。 |
| 2 | 自由列举 | 0.7 | 列出所有可能的构造方法来构造这样的有界序列。 | 1) 三角函数如 sin(nθ)；2) 无理数的小数部分 {nα}；3) 贪心构造逐个放置点；4) 指数序列；5) 对数间距；6) 利用均匀分布理论... |
| 3 | 小尝试 | 0.5 | 试试 x_n = sin(n)。这个构造可行吗？ | sin(n) 是有界的，但证明 |sin(i)-sin(j)| ≥ |i-j|^{-a} 很困难。sin(n) 的分布依赖于 n mod 2π 的分布，与 1/(2π) 的无理性有关，但分析很复杂，难以给出严格的定量下界。这条路似乎走不通。 |
| 4 | 思维操作引导 | 0.4 | 与其用 sin，考虑无理数 α 的小数部分 {nα}。我们需要 α 的什么性质？想想什么使得 {nα} 的值"充分分离"。 | 需要 α 是无理数，这样 {nα} 永不重复。更具体地，需要对 |{iα}-{jα}| 的接近程度有定量下界。对于 α=√2，可以利用 2k² 不是完全平方数这一代数性质，得到 |{i√2}-{j√2}| ≥ c/|i-j| 的下界。 |
| 5 | 推进 | 0.5 | 对于 α=√2，证明 {k√2} 远离 0 和 1。具体地，证明 {k√2} > 1/(2(√2k+1)) 且 1-{k√2} > 1/(2(√2k+1))。 | 令 y=⌊k√2⌋，则 {k√2}=k√2-y。有 (k√2-y)(k√2+y)=2k²-y²。因 y=⌊k√2⌋，故 y²<2k²<(y+1)²，所以 2k²-y²≥1（正整数）。又 k√2+y < 2√2k+1，故 {k√2}=(2k²-y²)/(k√2+y) ≥ 1/(2√2k+1) > 1/(2(√2k+1))。类似可证 1-{k√2} 的下界。 |
| 6 | 思维操作引导 | 0.3 | 利用上述下界证明 |{i√2}-{j√2}| > 1/(2(√2|i-j|+1))，然后确定常数 C 使得 x_n=C·{n√2} 满足所需不等式。 | 利用小数部分的差分性质，|{i√2}-{j√2}| 可归结为 {(i-j)√2} 或 1-{(i-j)√2}，故 > 1/(2(√2|i-j|+1))。取 C=2√2+2=2(√2+1)，则 |xᵢ-xⱼ|·|i-j|^a = C·|{i√2}-{j√2}|·|i-j|^a ≥ C·|i-j|^a/(2(√2+1)|i-j|) = |i-j|^{a-1} ≥ 1。 |
| 7 | 能量传递引导 | 0.6 | 验证：取 C=2√2+2=2(√2+1)，序列 x_n=C·{n√2} 有界且满足 |xᵢ-xⱼ|·|i-j|^a ≥ 1。确认构造完整。 | 是的：|x_n|=C·{n√2}≤C=2√2+2，序列有界。且 |xᵢ-xⱼ|·|i-j|^a ≥ C·|i-j|^a/(2(√2+1)|i-j|) = |i-j|^{a-1} ≥ 1（因 |i-j|≥1 且 a>1）。构造完整。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R5（丢番图逼近下界的证明）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R4（识别使用无理数小数部分作为构造工具）

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
- structure_features: 构造性问题——需要构造一个满足双重约束（有界性+多项式衰减分离）的无穷序列。核心张力在于"有界"与"任意两项分离"之间的平衡，a>1的条件使得这种平衡成为可能。
- key_objects: ["有界无穷实数序列", "小数部分函数 fract", "√2（二次无理数）", "丢番图逼近下界", "缩放常数 C=2√2+2"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["constraint_balancing（有界性与分离性的平衡）", "diophantine_approximation（丢番图逼近）", "construction_by_scaling（缩放构造）", "algebraic_number_theory（代数数论：利用2k²非完全平方数）"]
- primary_pattern: diophantine_approximation
- knowledge_required: ["小数部分函数及其性质", "√2的无理性", "丢番图逼近基本概念", "Pell方程性质（2k²-y²≥1）", "取整函数性质", "小数部分差分公式"]
- key_insight: 使用√2·n的小数部分构造序列——√2的代数性质（2k²永非完全平方数）给出了|{i√2}-{j√2}|的干净下界，再乘以适当常数即可满足分离条件。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 分析/解析语言（有界性+分离条件的连续性约束）
- translation_to: 数论/代数语言（无理数小数部分的丢番图逼近）
- translation_type: method_translation（跨域方法翻译——从分析约束到数论构造）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "direct_manipulation", gap_type: "method_translation"}
- tell_small_concepts: ["fractional_part", "diophantine_approximation", "quadratic_irrational", "separation_bound", "scaling_constant", "pell_equation_property"]
- expected_ai_method: bare AI预期会尝试直接的解析构造（如sin(n)或多项式序列），或贪心逐点构造，无法识别需要数论工具（无理数小数部分的丢番图逼近）
- correct_method: 使用√2·n的小数部分构造序列，利用√2的代数性质（2k²非完全平方数）证明分离下界，再缩放常数使不等式成立

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？是。structural_existence、direct_manipulation、method_translation均可归入已有类别。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？是。与已有值粒度一致。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？足够。三个维度能区分此题的跨域翻译特征。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。

**拓扑进化建议**（如有）：无。当前三维度拓扑分类足够。

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

**局部tell_hint_pairs详情**：

| R | tell | hint | level | situation_type | kb | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到构造问题有有界+分离双约束，但不知道该用什么结构来构造 | 描述约束：有界性与分离性的权衡，a>1的角色 | 0.8 | 纯元认知观察 | false | {structural_existence, direct_manipulation, method_problem_mismatch} | ["bounded_sequence", "separation_condition", "decay_rate"] |
| 2 | AI列出可能方向但可能未识别无理数小数部分这一数论工具 | 列出所有构造方法，包括数论方法 | 0.7 | 自由列举 | false | {structural_existence, enumeration_brute_force, search_space_estimation} | ["construction_methods", "trigonometric_sequences", "fractional_parts", "greedy_construction"] |
| 3 | AI尝试sin(n)等解析构造，难以给出严格定量分离下界 | 试一个解析构造，看它在哪里失败 | 0.5 | 小尝试 | false | {structural_existence, continuous_analytic, method_problem_mismatch} | ["sin_construction", "rigorous_bound_difficulty"] |
| 4 | AI未考虑使用无理数小数部分作为构造工具——这是知识瓶颈 | 考虑{nα}，需要α的什么性质？ | 0.4 | 思维操作引导 | true | {structural_existence, direct_manipulation, knowledge_gap} | ["fractional_part", "irrational_number", "diophantine_approximation", "separation_bound"] |
| 5 | AI需要用√2的代数性质证明小数部分的分离下界——知识瓶颈 | 利用2k²非完全平方数，证明{k√2}远离0和1 | 0.5 | 推进 | true | {structural_existence, algebraic_identity, knowledge_gap} | ["pell_equation", "floor_function", "algebraic_integer", "quadratic_irrational"] |
| 6 | AI有分离下界但未确定缩放常数使最终不等式成立 | 确定C使得C·{n√2}满足|xᵢ-xⱼ|·|i-j|^a≥1 | 0.3 | 思维操作引导 | false | {structural_existence, direct_calculation, method_translation} | ["scaling_constant", "inequality_combination", "exponent_bound"] |
| 7 | AI有所有组件，需要端到端验证构造完整 | 验证C=2√2+2给出有界序列且满足不等式 | 0.6 | 能量传递引导 | false | {structural_existence, direct_calculation, method_problem_mismatch} | ["verification", "boundedness_check", "inequality_check"] |

**全局tell_hint_pairs详情**：

| scope_type | scope | obs_pt | tell | hint | level | generalizability | why_not_visible_locally | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|---|---|
| path_feature | 完整解路径：从"有界序列+分离"到"√2小数部分构造" | null | 问题要求构造有界序列且满足多项式衰减分离——这需要数论构造（二次无理数小数部分的丢番图逼近），而非解析或直接方法 | 使用√2·n的小数部分乘以适当常数，同时实现有界性和分离性 | 0.7 | high——无理数小数部分用于分离构造的技术可推广到许多有界序列问题 | 完整路径从"有界+分离"到"√2小数部分"需要连接分析（分离条件）与数论（丢番图逼近）——这种跨域连接在任何单一步骤中都不可见 | {structural_existence, direct_manipulation, method_translation} | ["fractional_part_construction", "quadratic_irrational", "diophantine_approximation", "bounded_separation"] |
| implicit | √2的特定选择和常数2√2+2的确定 | R5 | 选择√2（而非任意无理数）是关键的，因为其代数性质（2k²非完全平方数）给出紧的分离下界；常数2√2+2=2(√2+1)恰好使不等式紧致 | 选择α=√2利用其代数性质，取C=2(√2+1)使最终不等式成立 | 0.4 | medium——二次无理数用于丢番图逼近的技术可推广，但具体常数依赖于问题 | 选择√2而非其他无理数的原因（其代数性质给出干净下界）和常数的精确值（取决于分离下界的紧致程度）在任何单一步骤中都不可见——它们从丢番图下界与缩放要求的交互中涌现 | {structural_existence, algebraic_identity, knowledge_gap} | ["sqrt2_choice", "scaling_constant", "quadratic_irrational_property", "tight_bound"] |

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI大概率会尝试解析构造（如sin(nθ)）或贪心逐点构造，无法识别需要数论工具（无理数小数部分的丢番图逼近）。即使考虑到小数部分方法，也可能不知道如何利用√2的代数性质（2k²非完全平方数）来证明定量的分离下界，更难以确定正确的缩放常数。
- suitable_for_poc: ["tell_identification（识别跨域翻译tell）", "method_translation_poc（验证方法翻译hint有效性）", "knowledge_gap_detection（检测丢番图逼近知识缺口）"]
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
- [x] answer（**⚠️ 必填，不能为None**。proof类型填要证明的结论，如"sum >= ..."；existence_construction类型填构造的存在性结论；numerical类型填数值答案）
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
2. 更新`problem_extraction_progress`集合中`_key="329137"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1991p6"
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
    '_key': '329137',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1991p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1991p6')
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
- problem_id: compfiles_imo1991p6
- solution_method_type: diophantine_construction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否。当前三维度拓扑分类（problem_type/ai_method_type/gap_type）足够覆盖此题的tell特征。
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
