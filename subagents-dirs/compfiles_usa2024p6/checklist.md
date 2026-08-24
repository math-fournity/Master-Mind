# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2024p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2024P6.lean
- **来源**: USA 2024 P6
- **ArangoDB progress记录_key**: 329504（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2024P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设 n > 2 为整数，ℓ ∈ {1,2,...,n}。集合族 A₁,...,Aₖ（不必互异）为 {1,...,n} 的子集，若 |Aᵢ| ≥ ℓ 对所有 i 成立则称为 ℓ-large。求最大的实数 c（用 n 和 ℓ 表示），使得不等式 ∑ᵢ∑ⱼ xᵢxⱼ|Aᵢ∩Aⱼ|²/(|Aᵢ|·|Aⱼ|) ≥ c(∑ᵢxᵢ)² 对所有正整数 k、所有非负实数 x₁,...,xₖ 和所有 ℓ-large 集合族成立。
- 解答核心思路（1-2句话）：用指示函数重写 |Aᵢ∩Aⱼ| 并交换求和顺序，将左边转化为 ∑_{p,q} v_{p,q}² 的平方和形式，然后分为对角项和非对角项分别用 QM-AM 不等式得到下界，最后用所有 ℓ-子集的对称构造验证最优性。
- 解答关键步骤列表：
  1. 定义 v_{p,q} = ∑ᵢ (xᵢ/|Aᵢ|)·1_{p,q∈Aᵢ}，用指示函数重写 |Aᵢ∩Aⱼ|² = (∑_p 1_{p∈Aᵢ}·1_{p∈Aⱼ})²
  2. 交换求和顺序，证明 LHS = ∑_{p,q} v_{p,q}²（lhs_eq_sum_v_sq）
  3. 分割为对角项 ∑_p v_{p,p}² 和非对角项 ∑_{p≠q} v_{p,q}²（sum_sq_split）
  4. 对角项：∑_p v_{p,p} = ∑ᵢ xᵢ = S，由 QM-AM 得 ∑_p v_{p,p}² ≥ S²/n
  5. 非对角项：∑_{p≠q} v_{p,q} = ∑ᵢ(|Aᵢ|-1)xᵢ ≥ (ℓ-1)S，由 QM-AM 得 ∑_{p≠q} v_{p,q}² ≥ (ℓ-1)²S²/(n(n-1))
  6. 合并得 c = S²/n + (ℓ-1)²S²/(n(n-1)) = (n+ℓ²-2ℓ)S²/(n(n-1))，即 c = (n+ℓ²-2ℓ)/(n(n-1))
  7. 最优性：取所有 ℓ-子集各一次、权重全为1，由对称性 v_{p,p}=k/n, v_{p,q}=k(ℓ-1)/(n(n-1))，等号成立

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
| 1 | 纯元认知观察 | 0.8 | 观察这个不等式的结构。左边是一个关于集合交集的双求和，右边是一个关于权重的平方。你能描述出左边的代数结构吗？它类似于什么？ | 左边是 ∑ᵢ∑ⱼ xᵢxⱼ·|Aᵢ∩Aⱼ|²/(|Aᵢ||Aⱼ|)，这是一个关于 x 的二次型。矩阵的第(i,j)项是 |Aᵢ∩Aⱼ|²/(|Aᵢ||Aⱼ|)。我们需要找到这个二次型在所有ℓ-large集合族下的最大下界c。 |
| 2 | 自由列举 | 0.7 | 列出所有可能用来处理这个不等式的方法。特别是，|Aᵢ∩Aⱼ| 这个量有哪些不同的表达方式？ | 方法包括：1) 直接Cauchy-Schwarz；2) 用指示函数表示|Aᵢ∩Aⱼ|=∑_p 1_{p∈Aᵢ}·1_{p∈Aⱼ}；3) 谱方法/矩阵特征值；4) 概率方法；5) 对偶方法。|Aᵢ∩Aⱼ|可以用指示函数求和表示，也可以用内积表示。 |
| 3 | 小尝试 | 0.5 | 尝试直接对原始表达式应用Cauchy-Schwarz不等式。看看能得到什么下界。 | 直接对∑ᵢ∑ⱼ xᵢxⱼ·|Aᵢ∩Aⱼ|²/(|Aᵢ||Aⱼ|)应用Cauchy-Schwarz比较困难，因为|Aᵢ∩Aⱼ|²/(|Aᵢ||Aⱼ|)的结构复杂。如果尝试把xᵢ/√|Aᵢ|作为一组，会得到∑(xᵢ)²·∑|Aᵢ∩Aⱼ|²/|Aⱼ|之类，但不直接给出(∑xᵢ)²的下界。直接方法似乎难以利用ℓ-large条件。 |
| 4 | 思维操作引导 | 0.4 | 用指示函数重写|Aᵢ∩Aⱼ|：|Aᵢ∩Aⱼ| = ∑_p 1_{p∈Aᵢ}·1_{p∈Aⱼ}。然后代入左边的表达式，尝试交换求和顺序——先对p,q求和，再对i,j求和。定义v_{p,q} = ∑ᵢ (xᵢ/|Aᵢ|)·1_{p∈Aᵢ∧q∈Aᵢ}。你能把左边表示成什么形式？ | 代入后，|Aᵢ∩Aⱼ|² = (∑_p 1_{p∈Aᵢ}·1_{p∈Aⱼ})² = ∑_p∑_q 1_{p∈Aᵢ}·1_{q∈Aᵢ}·1_{p∈Aⱼ}·1_{q∈Aⱼ}。所以左边 = ∑_p∑_q (∑ᵢ xᵢ/|Aᵢ|·1_{p,q∈Aᵢ})² = ∑_p∑_q v_{p,q}²。这是一个平方和！ |
| 5 | 思维操作引导 | 0.4 | 现在左边 = ∑_p∑_q v_{p,q}²。将这个和分成对角项(p=q)和非对角项(p≠q)两部分。对每部分分别应用QM-AM不等式。先计算对角项的和∑_p v_{p,p}等于什么？ | v_{p,p} = ∑ᵢ xᵢ/|Aᵢ|·1_{p∈Aᵢ}。∑_p v_{p,p} = ∑_p ∑ᵢ xᵢ/|Aᵢ|·1_{p∈Aᵢ} = ∑ᵢ xᵢ/|Aᵢ|·|Aᵢ| = ∑ᵢ xᵢ = S。由QM-AM：∑_p v_{p,p}² ≥ (∑_p v_{p,p})²/n = S²/n。 |
| 6 | 推进 | 0.5 | 现在处理非对角项。计算∑_{p≠q} v_{p,q}等于什么？然后利用ℓ-large条件（|Aᵢ|≥ℓ）来得到下界。 | ∑_{p≠q} v_{p,q} = ∑_{p≠q} ∑ᵢ xᵢ/|Aᵢ|·1_{p,q∈Aᵢ} = ∑ᵢ xᵢ/|Aᵢ|·|Aᵢ|(|Aᵢ|-1) = ∑ᵢ (|Aᵢ|-1)xᵢ ≥ (ℓ-1)∑ᵢxᵢ = (ℓ-1)S。由QM-AM：∑_{p≠q} v_{p,q}² ≥ ((ℓ-1)S)²/(n(n-1))。所以LHS ≥ S²/n + (ℓ-1)²S²/(n(n-1)) = (n+ℓ²-2ℓ)S²/(n(n-1))。 |
| 7 | 能量传递引导 | 0.6 | 现在需要证明这个常数是最优的。考虑取所有ℓ-子集各一次，权重全为1。验证在这个例子中等号成立。 | 取A₁,...,Aₖ为[n]的所有ℓ-子集（k=C(n,ℓ)），xᵢ=1。由对称性，每个点出现在kℓ/n个子集中，每对点出现在kℓ(ℓ-1)/(n(n-1))个子集中。所以v_{p,p}=k/n，v_{p,q}=k(ℓ-1)/(n(n-1))。LHS = n·(k/n)² + n(n-1)·(k(ℓ-1)/(n(n-1)))² = k²/n + (ℓ-1)²k²/(n(n-1)) = c·k² = c·S²。等号成立！ |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.9
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

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
- structure_features: 在集合族上定义的归一化交集二次型的最优常数问题。左边是关于权重x的二次型，矩阵元素为|Aᵢ∩Aⱼ|²/(|Aᵢ||Aⱼ|)，需要在所有ℓ-large集合族下找到最大下界c。关键结构是交集基数可以用指示函数表示，从而交换求和顺序。
- key_objects: ["ℓ-large集合族", "归一化交集二次型 |Aᵢ∩Aⱼ|²/(|Aᵢ||Aⱼ|)", "指示函数 1_{p∈Aᵢ}", "归一化权重 v_{p,q}", "QM-AM不等式", "对称极值构造（所有ℓ-子集）"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["indicator_rewriting", "sum_of_squares_decomposition", "diagonal_off_diagonal_split", "qm_am_cauchy_schwarz", "double_counting", "symmetric_extremal_construction"]
- primary_pattern: indicator_rewriting（指示函数重写——从集合交集语言翻译到平方和语言的核心操作）
- knowledge_required: ["Cauchy-Schwarz不等式（QM-AM形式）", "指示函数/特征函数", "双重计数", "集合交集基数", "对称群在子集上的作用", "求和顺序交换"]
- key_insight: 用指示函数重写|Aᵢ∩Aⱼ|并交换求和顺序，将集合交集的二次型转化为归一化权重的平方和∑_{p,q} v_{p,q}²，然后分对角/非对角两部分分别用QM-AM得到下界

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 集合交集的二次型语言（combinatorial set-intersection quadratic form）
- translation_to: 归一化权重的平方和语言（sum-of-squares of normalized weights v_{p,q}）
- translation_type: structural_transformation（通过指示函数重写和求和顺序交换，将组合语言的结构转化为代数语言的结构）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "inequality_proof", ai_method_type: "direct_calculation", gap_type: "structural_transformation"}
- tell_small_concepts: ["indicator_function", "sum_of_squares", "qm_am", "diagonal_off_diagonal", "double_counting", "normalized_weight", "extremal_construction"]
- expected_ai_method: direct_calculation（bare AI会尝试直接对原始二次型应用Cauchy-Schwarz，不经过指示函数重写）
- correct_method: indicator_rewriting + sum_of_squares + diagonal/off-diagonal split + QM-AM（指示函数重写→平方和→对角/非对角分割→QM-AM）

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ → 可以。problem_type=inequality_proof（已有），ai_method_type=direct_calculation（已有），gap_type=structural_transformation（已有）。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ → 一致。三个维度都使用了中等抽象粒度的已有值。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ → 足够。这道题的核心tell是"需要做语言转换（从组合到代数）"，这由gap_type=structural_transformation和ai_method_type=direct_calculation的组合已经能区分。
- [x] 如果发现拓扑分类需要进化，在此写出建议： → 无需进化。已有拓扑分类完全够用。

**拓扑进化建议**（如有）：无。已有拓扑分类体系完全覆盖本题。

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

**局部pairs详情**：
- R1: tell="AI识别出二次型结构但停留在集合交集的原始语言中", hint="观察左边的代数结构——它是关于x的二次型，矩阵元素涉及集合交集", hint_level=0.8, situation_type=纯元认知观察, is_knowledge_bottleneck=false, topology={inequality_proof, direct_calculation, structural_transformation}, concepts=[quadratic_form, intersection_cardinality, normalized_weight]
- R2: tell="AI列出了多种方法包括指示函数表示，但没意识到这是关键", hint="指示函数表示是关键——它允许交换求和顺序", hint_level=0.7, situation_type=自由列举, is_knowledge_bottleneck=false, topology={inequality_proof, enumeration_brute_force, method_translation}, concepts=[indicator_function, cauchy_schwarz, spectral_method, sum_order_swap]
- R3: tell="AI尝试直接Cauchy-Schwarz但受阻——无法利用ℓ-large条件", hint="直接方法受阻是因为还在集合交集的语言中——需要换一种语言", hint_level=0.5, situation_type=小尝试, is_knowledge_bottleneck=false, topology={inequality_proof, direct_calculation, method_problem_mismatch}, concepts=[cauchy_schwarz, intersection_cardinality, ell_large_condition]
- R4: tell="AI需要知道指示函数重写技术——这是纯知识瓶颈", hint="用指示函数重写|Aᵢ∩Aⱼ|并交换求和顺序，定义v_{p,q}", hint_level=0.4, situation_type=思维操作引导, is_knowledge_bottleneck=true, topology={inequality_proof, algebraic_identity, knowledge_gap}, concepts=[indicator_function, sum_of_squares, sum_order_swap, normalized_weight]
- R5: tell="AI需要想到分割对角/非对角并分别用QM-AM", hint="将对角项和非对角项分开，分别应用QM-AM不等式", hint_level=0.4, situation_type=思维操作引导, is_knowledge_bottleneck=false, topology={inequality_proof, logical_deduction, knowledge_gap}, concepts=[diagonal_off_diagonal, qm_am, cauchy_schwarz, sum_of_squares]
- R6: tell="AI需要将ℓ-large条件连接到非对角项的下界", hint="计算∑_{p≠q} v_{p,q}并利用|Aᵢ|≥ℓ得到下界", hint_level=0.5, situation_type=推进, is_knowledge_bottleneck=false, topology={inequality_proof, logical_deduction, knowledge_gap}, concepts=[ell_large_condition, qm_am, off_diagonal_sum, cauchy_schwarz]
- R7: tell="AI需要构造对称极值例子验证最优性", hint="取所有ℓ-子集各一次权重为1，由对称性验证等号成立", hint_level=0.6, situation_type=能量传递引导, is_knowledge_bottleneck=false, topology={inequality_proof, case_by_case, method_translation}, concepts=[symmetric_construction, extremal_example, all_ell_subsets, equality_condition]

**全局pairs详情**：
- GP1 (path_feature): scope="从题目到解答的完整路径：指示函数重写→求和顺序交换→平方和表示→对角/非对角分割→QM-AM→ℓ-large条件利用→对称极值构造", tell="整个解题路径的核心结构是'语言转换'——从集合交集的组合语言转换到归一化权重的代数语言，这个转换在局部步骤中不可见", hint="识别出需要做语言转换——从组合语言到代数语言，通过指示函数重写实现", hint_level=0.7, generalizability="high - 指示函数重写+求和顺序交换是处理集合交集二次型的通用技术", why_not_visible_locally="在任何一个单独的步骤中，AI只能看到当前的操作（如应用Cauchy-Schwarz），但看不到整个路径的'语言转换'结构——从集合语言到代数语言的转换是一个全局性的战略选择，不是局部战术", topology={inequality_proof, direct_calculation, structural_transformation}, concepts=[indicator_function, sum_of_squares, language_translation, sum_order_swap]
- GP2 (implicit): scope="答案c = 1/n + (ℓ-1)²/(n(n-1))的自然分解对应对角项和非对角项", observation_point="R6", tell="答案的自然分解形式c = 1/n + (ℓ-1)²/(n(n-1))隐含了对角/非对角分割的结构", hint="观察答案的形式——它可以分解为两个部分，分别对应不同的求和区域（对角和非对角）", hint_level=0.6, generalizability="medium - 答案的分解形式暗示证明方法的结构，这是一种常见的元认知技巧", why_not_visible_locally="在局部步骤中，AI只关注当前的计算，不会回头观察最终答案的形式来推断证明结构——答案的分解形式与证明方法之间的对应关系是隐含的，需要从全局视角才能看到", topology={inequality_proof, direct_calculation, structural_transformation}, concepts=[answer_decomposition, diagonal_off_diagonal, structural_hint]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI会尝试直接对原始二次型应用Cauchy-Schwarz或分析矩阵特征值，不会意识到需要用指示函数重写|Aᵢ∩Aⱼ|并交换求和顺序。它无法利用ℓ-large条件，也不会发现平方和分解。极可能给出错误的常数或无法完成证明。
- suitable_for_poc: ["tell_identification", "hint_injection", "language_translation_poc"]
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
2. 更新`problem_extraction_progress`集合中`_key="329504"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa2024p6"
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
    '_key': '329504',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa2024p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa2024p6')
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
- problem_id: compfiles_usa2024p6
- solution_method_type: indicator_rewriting_sum_of_squares
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。已有拓扑分类体系（inequality_proof / direct_calculation / structural_transformation等）完全覆盖本题。
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
