# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2000p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2000P6.lean
- **来源**: USA 2000 P6
- **ArangoDB progress记录_key**: 329401（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2000P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let a₁, b₁, a₂, b₂, ..., aₙ, bₙ be nonnegative real numbers. Prove that ∑ᵢⱼ min(aᵢaⱼ, bᵢbⱼ) ≤ ∑ᵢⱼ min(aᵢbⱼ, aⱼbᵢ), where each sum is taken over all n² pairs (i, j).
- 解答核心思路（1-2句话）：将每对(i,j)的差Dᵢⱼ = min(aᵢbⱼ,aⱼbᵢ) - min(aᵢaⱼ,bᵢbⱼ)分解为σᵢσⱼ·min(uᵢwⱼ,uⱼwᵢ)（u=min(a,b), w=|a-b|, σ=sign），将不等式归约为min-kernel的正半定性，再用归纳法（剥离最小值指标）证明min-kernel PSD。
- 解答关键步骤列表：
  1. 定义Dᵢⱼ = min(aᵢbⱼ, aⱼbᵢ) - min(aᵢaⱼ, bᵢbⱼ)，将不等式转化为∑Dᵢⱼ ≥ 0
  2. 关键代数恒等式：Dᵢⱼ = σᵢσⱼ·min(uᵢwⱼ, uⱼwᵢ)，其中uᵢ=min(aᵢ,bᵢ), wᵢ=|aᵢ-bᵢ|, σᵢ=sign(bᵢ≤aᵢ)
  3. 将∑Dᵢⱼ = ∑σᵢσⱼMᵢⱼ = σᵀMσ识别为二次型，需要证明M正半定
  4. 在w的支撑上，Mᵢⱼ = wᵢwⱼ·min(uᵢ/wᵢ, uⱼ/wⱼ)，归约为min-kernel K(sᵢ,sⱼ)=min(sᵢ,sⱼ)的PSD
  5. 用强归纳法证明min-kernel PSD：剥离s最小的指标i₀，min(sᵢ,sⱼ)=t+min(sᵢ-t,sⱼ-t)，平移核在i₀行列为零，归纳完成

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
| 1 | 纯元认知观察 | 0.8 | 观察这个不等式的结构：左边和右边各是什么？每个求和项涉及哪些变量？这个不等式在什么意义上是非平凡的？ | 左边∑min(aᵢaⱼ,bᵢbⱼ)是"同侧乘积的min"，右边∑min(aᵢbⱼ,aⱼbᵢ)是"交叉乘积的min"。每个项涉及两个指标对(i,j)和四个非负实数。非平凡性在于：逐项比较时两边大小关系不确定，需要全局求和后才能比较。 |
| 2 | 自由列举 | 0.7 | 列出你能想到的所有可能证明方向：直接展开、逐项分析、已知不等式、代数恒等式、核方法等 | 可能方向：1)逐对case分析哪个min更小 2)用排序/重排不等式 3)寻找代数恒等式分解差 4)用Schur凸性 5)转化为矩阵/二次型问题 6)用积分表示 |
| 3 | 小尝试 | 0.5 | 试着对单个对(i,j)计算差Dᵢⱼ=min(aᵢbⱼ,aⱼbᵢ)-min(aᵢaⱼ,bᵢbⱼ)，分情况讨论。你能发现什么模式吗？ | 分四种情况（aᵢ≥bᵢ或<, aⱼ≥bⱼ或<），每种情况Dᵢⱼ有不同表达式。但n²个对的情况太多，逐项分析无法直接求和。关键观察：Dᵢⱼ的符号取决于aᵢ-bᵢ和aⱼ-bⱼ的符号是否一致。 |
| 4 | 思维操作引导 | 0.3 | 将每个(aᵢ,bᵢ)分解为uᵢ=min(aᵢ,bᵢ), wᵢ=|aᵢ-bᵢ|, σᵢ=sign(bᵢ≤aᵢ)。用这些量表达Dᵢⱼ，你能得到什么恒等式？ | 关键恒等式：Dᵢⱼ = σᵢσⱼ·min(uᵢwⱼ, uⱼwᵢ)。这个分解将差的符号完全吸收到σᵢσⱼ中，剩余部分是非负的min-kernel项。 |
| 5 | 推进 | 0.4 | 现在∑Dᵢⱼ = ∑σᵢσⱼMᵢⱼ，其中Mᵢⱼ=min(uᵢwⱼ,uⱼwᵢ)。这个表达式是什么数学结构？需要证明什么性质？ | 这是二次型σᵀMσ，需要证明矩阵M=(Mᵢⱼ)是正半定的(PSD)。如果M正半定，则对所有实向量σ有σᵀMσ≥0，不等式得证。 |
| 6 | 思维操作引导 | 0.2 | 在w的支撑上，Mᵢⱼ=wᵢwⱼ·min(uᵢ/wᵢ,uⱼ/wⱼ)。这归约为证明min-kernel K(sᵢ,sⱼ)=min(sᵢ,sⱼ)正半定。用归纳法证明：剥离s最小的指标i₀，观察平移后的核有什么性质？ | 设t=s(i₀)为最小值。min(sᵢ,sⱼ)=t+min(sᵢ-t,sⱼ-t)。∑zᵢzⱼmin(sᵢ,sⱼ)=t(∑zᵢ)²+∑zᵢzⱼmin(sᵢ-t,sⱼ-t)。平移核min(sᵢ-t,sⱼ-t)在i₀行和列全为零（因为s(i₀)-t=0），所以剩余求和可限制在更小的指标集上，用归纳假设完成。 |
| 7 | 能量传递引导 | 0.1 | 验证归纳的基例和递推都成立：空集平凡，剥离后指标集严格变小，平移核在i₀行列消失。整个证明链条是否完整？ | 基例：空集求和为0≥0。递推：剥离i₀后T\{i₀}是T的真子集，归纳假设适用。t(∑zᵢ)²≥0因为t≥0且平方非负。平移核项由归纳假设≥0。整个链条完整：恒等式分解→二次型→PSD→归纳。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.0
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
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
- problem_type: inequality_proof
- structure_features: 双重求和n²对，min(乘积)的不等式，非负实数，对称结构，逐项不可比但全局求和后可比
- key_objects: ["非负实数序列aᵢ,bᵢ", "min函数", "双重求和∑ᵢⱼ", "代数恒等式Dᵢⱼ=σᵢσⱼmin(uᵢwⱼ,uⱼwᵢ)", "正半定核Mᵢⱼ=min(uᵢwⱼ,uⱼwᵢ)", "min-kernel K(sᵢ,sⱼ)=min(sᵢ,sⱼ)", "符号向量σ", "二次型σᵀMσ"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["difference factorization", "algebraic identity decomposition", "quadratic form recognition", "PSD kernel reduction", "induction on index set", "minimum peeling"]
- primary_pattern: "algebraic identity decomposition → PSD kernel reduction"
- knowledge_required: ["min代数运算", "正半定矩阵与二次型", "绝对值分解u/w/σ", "数学归纳法", "Finset求和操作"]
- key_insight: 将逐对差Dᵢⱼ分解为符号×非负min-kernel项σᵢσⱼmin(uᵢwⱼ,uⱼwᵢ)，把min-乘积不等式转化为min-kernel的正半定性证明

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 逐对min-乘积不等式（组合/代数语言）
- translation_to: 正半定核的二次型非负性（线性代数/核方法语言）
- translation_type: structural_transformation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "inequality_proof", ai_method_type: "case_by_case", gap_type: "structural_transformation"}
- tell_small_concepts: ["min factorization", "sign decomposition", "PSD kernel", "min kernel", "induction peeling", "quadratic form"]
- expected_ai_method: case_by_case — bare AI会对每对(i,j)分情况讨论哪个min更小，陷入n²个case无法求和
- correct_method: algebraic_identity_decomposition + PSD_kernel_reduction — 用u/w/σ分解得到恒等式，归约为min-kernel PSD，归纳证明

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？是，inequality_proof/case_by_case/structural_transformation均可归入已有类别
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？是，与已有值粒度一致
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？够用，三个维度足以区分
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化

**拓扑进化建议**（如有）：无，现有拓扑分类体系足够覆盖此题

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

| qa_round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到双重求和min-乘积不等式，不知道从哪里入手 | 描述结构：左右各是什么？为什么逐项不可比？ | 0.8 | 纯元认知观察 | false | {inequality_proof, case_by_case, search_space_estimation} | [double sum structure, min of products, n² pairs] |
| 2 | AI列出方向但可能遗漏代数恒等式/核方法路线 | 列出所有可能方向：直接展开、case分析、恒等式、核方法 | 0.7 | 自由列举 | false | {inequality_proof, enumeration_brute_force, method_problem_mismatch} | [approach enumeration, case analysis, algebraic identity, kernel method] |
| 3 | AI尝试逐对case分析，陷入n²个情况无法求和 | 试算单对Dᵢⱼ，分情况讨论，找模式 | 0.5 | 小尝试 | false | {inequality_proof, case_by_case, method_problem_mismatch} | [pairwise difference, case analysis, min comparison] |
| 4 | AI在算差但看不到u/w/σ分解的恒等式 | 将(aᵢ,bᵢ)分解为uᵢ,wᵢ,σᵢ，用这些量表达Dᵢⱼ | 0.3 | 思维操作引导 | true | {inequality_proof, algebraic_identity, knowledge_gap} | [u-w-sigma decomposition, sign factorization, min kernel entry] |
| 5 | AI有恒等式但没认出σᵀMσ是二次型 | ∑σᵢσⱼMᵢⱼ是什么结构？需要M的什么性质？ | 0.4 | 推进 | false | {inequality_proof, direct_calculation, structural_transformation} | [quadratic form, positive semidefinite, sign vector] |
| 6 | AI知道需要PSD但不会证min-kernel PSD | 在w支撑上归约到min(sᵢ,sⱼ) PSD，用归纳法剥离最小值 | 0.2 | 思维操作引导 | true | {inequality_proof, direct_manipulation, knowledge_gap} | [min kernel, induction peeling, shifted kernel, support restriction] |
| 7 | AI做归纳但需确认平移核在i₀行列消失 | 验证基例和递推：平移核vanish，归纳链条完整 | 0.1 | 能量传递引导 | false | {inequality_proof, logical_deduction, method_problem_mismatch} | [induction base case, vanishing row, minimum peeling, completion] |

**全局tell_hint_pairs详情**：

1. path_feature型：
- scope: 整个解题路径从逐对不等式到PSD核
- observation_point: null
- tell: 不等式∑min(aᵢaⱼ,bᵢbⱼ)≤∑min(aᵢbⱼ,aⱼbᵢ)无法逐项比较证明——需要全局结构变换从min-乘积不等式到PSD核二次型
- hint: 将逐对差分解为符号×非负min-kernel项，归约为PSD核再用归纳法证明
- hint_level: 0.6
- generalizability: high — min-kernel PSD技术适用于许多min-基不等式
- why_not_visible_locally: 在任意单对(i,j)，差Dᵢⱼ可正可负，局部比较必然失败。只有对所有对的全局求和，视为二次型σᵀMσ，才暴露PSD结构。σᵢσⱼMᵢⱼ的因式分解需要同时分解所有对才可见——局部视角下每个Dᵢⱼ只是min的差，看不到全局的核结构。
- tell_topology: {inequality_proof, case_by_case, structural_transformation}
- tell_small_concepts: [global quadratic form, PSD kernel, sign-weighted sum, structural transformation]

2. implicit型：
- scope: min-kernel min(s,t)的正半定性——Brownian运动协方差的离散影子
- observation_point: R6
- tell: min-kernel K(sᵢ,sⱼ)=min(sᵢ,sⱼ)正半定是连接不等式与核理论的隐藏关键事实
- hint: 认出min(s,t)是协方差核（Brownian运动），用归纳剥离证明PSD
- hint_level: 0.5
- generalizability: high — min-kernel PSD是概率论和分析中的基本结果
- why_not_visible_locally: min(sᵢ,sⱼ)的PSD性质从代数形式本身不可见——需要积分表示min(s,t)=∫₁[s≥r]₁[t≥r]dr或归纳剥离论证才能揭示。这个联系在单项层面完全不可见，只有在尝试证明整个核非负时才浮现。
- tell_topology: {inequality_proof, direct_manipulation, knowledge_gap}
- tell_small_concepts: [min kernel PSD, Brownian motion covariance, integral representation, induction peeling]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会对每对(i,j)分情况讨论哪个min更小，陷入n²个case的组合爆炸中，无法找到全局因式分解。不会想到将(aᵢ,bᵢ)分解为u/w/σ三个分量，也不会识别出二次型σᵀMσ的PSD结构。即使偶然发现差的符号模式，也缺乏正半定核的知识来完成归约。
- suitable_for_poc: ["tell_injection_POC", "knowledge_bottleneck_POC", "structural_transformation_POC"]
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

**将完整JSON写入工作目录的 `profile.json` 文件** — 已写入 subagents-dirs/compfiles_usa2000p6/profile.json

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
2. 更新`problem_extraction_progress`集合中`_key="329401"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa2000p6"
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
    '_key': '329401',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa2000p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa2000p6')
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
- problem_id: compfiles_usa2000p6
- solution_method_type: algebraic_identity_decomposition_and_psd_kernel_reduction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，现有拓扑分类体系（inequality_proof/case_by_case/structural_transformation等）足够覆盖此题
- 是否遇到异常: 否，入库和验证均一次通过

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
