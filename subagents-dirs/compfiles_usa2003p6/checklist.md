# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2003p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2003P6.lean
- **来源**: USA 2003 P6
- **ArangoDB progress记录_key**: 329414（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2003P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：正六边形六个顶点上写六个非负整数，其和为2003^2003。Bert可以选择一个顶点，将该顶点上的数替换为其两个相邻顶点上数之差的绝对值。证明Bert可以通过一系列操作使得六个顶点上都出现0。
- 解答核心思路（1-2句话）：利用奇偶性分析（mod 2下|a-b|≡a+b，移动变为线性操作），将奇和配置归约为恰好一个奇数项的配置，然后对最大值做强归纳——每轮要么直接归零，要么保持奇和且严格降低最大值，由归纳终止。
- 解答关键步骤列表：
  1. 2003^2003为奇数（2003奇，奇数的幂仍奇），故六数之和为奇
  2. 奇偶性机器：在ZMod 2中，|a-b| ≡ a+b，故移动在奇偶向量上是线性操作（替换v(j)为v(j-1)+v(j+1)）
  3. Phase 1：从任意奇和奇偶向量，通过8组候选操作序列（穷举验证decide），到达恰好一个奇数项的配置
  4. 旋转对称性：可将唯一奇数项旋转到顶点0
  5. Phase 2：从顶点0为唯一奇数项的配置出发，分情况讨论最大值位置：
     a. 最大值在顶点0（奇数最大值）：再分顶点2、4是否为0的子情况，要么直接6步归零，要么降低最大值
     b. 最大值在偶数顶点（非0）：用序列[1,2,3,4,5]降低最大值，同时保持奇和
  6. 强归纳：对cmax做强归纳，Phase 1+Phase 2要么直接归零，要么cmax严格递减且保持奇和，由归纳到达全零
  7. 桥接：从ℕ配置提升到ℤ配置（Nat.dist ↔ |·-·|），完成证明

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
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：已知什么、操作是什么、目标是什么？特别地，2003^2003这个数有什么特殊性质？ | 六个非负整数放在正六边形顶点上，和为2003^2003。操作：选一个顶点，用其两个邻居之差的绝对值替换。目标：到达全零。2003是奇数，故2003^2003是奇数，因此六数之和为奇。 |
| 2 | 自由列举 | 0.7 | 列出所有可能用来分析这个问题的数学工具和方向。 | 不变量/单调量分析、奇偶性分析、归纳法（对最大值/总和）、直接构造操作序列、穷举案例分析、图上的博弈论、模运算 |
| 3 | 小尝试 | 0.5 | 试着找一个不变量：每次操作后，六个数的总和如何变化？这个方向有前途吗？ | 总和会变化：新和=旧和-f(j)+|f(j-1)-f(j+1)|。总和不是不变量。但可以看模2：|a-b|≡a+b(mod 2)，所以模2下新和≡旧和-f(j)+f(j-1)+f(j+1)。这看起来有奇偶性的线索。 |
| 4 | 思维操作引导 | 0.4 | 聚焦奇偶性：在ZMod 2中，|a-b|变成什么？移动在奇偶向量上是什么操作？从奇和出发，能否利用这一点？ | 在ZMod 2中|a-b|≡a+b，所以移动变为：将v(j)替换为v(j-1)+v(j+1)，这是线性操作。奇和意味着奇偶向量中有奇数个1。关键问题：能否通过一系列线性操作将奇偶向量归约为恰好一个1？ |
| 5 | 推进 | 0.5 | 验证：从任意有奇数个1的6位奇偶向量出发，是否总能通过操作到达恰好一个1的向量？有多少种奇和奇偶向量？能否穷举验证？ | 有2^5=32种奇和奇偶向量（6位中奇数个1）。可以构造若干候选操作序列，用穷举验证（finite case analysis）确认每组序列覆盖哪些奇偶模式。解答中用了8组候选序列覆盖全部32种情况。 |
| 6 | 思维操作引导 | 0.4 | 现在有恰好一个奇数项（设在顶点0）。如何利用这个结构？考虑最大值的位置——最大值在顶点0还是在其他位置？分别能做什么？ | 若最大值在顶点0（奇数最大值）：其他项都是偶数且小于最大值。看顶点2和4是否为0——若都是0，可用6步直接归零；否则可用操作降低最大值。若最大值在偶数顶点（非0）：顶点0的值严格小于最大值，可用序列[1,2,3,4,5]依次操作，每步结果都≤cmax-1，降低最大值。 |
| 7 | 推进 | 0.5 | 将Phase 1和Phase 2组合：如何用归纳法完成证明？归纳变量是什么？终止条件是什么？ | 对cmax做强归纳。Phase 1将任意奇和配置归约为单奇数项配置（cmax不增），Phase 2要么直接归零（终止），要么cmax严格递减且保持奇和（归纳假设适用）。由于cmax是非负整数且严格递减，过程必然终止于全零。 |
| 8 | 能量传递引导 | 0.6 | 整合所有部分，写出完整的证明框架。关键转折点是什么？ | 完整框架：2003^2003奇→奇和→Phase 1奇偶归约（穷举验证8组序列）→单奇数项→旋转到顶点0→Phase 2案例分析（最大值位置）→归零或cmax递减→强归纳→全零。关键转折点是奇偶性洞察：mod 2下绝对差变为和，使移动线性化。 |

**统计**：
- total_rounds: 8
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 4.4
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
- problem_type: discrete_combinatorial
- structure_features: 六边形顶点上的非负整数配置，操作为局部替换（用邻居之差的绝对值替换当前值），目标是到达全零配置。关键结构：奇偶性使操作在ZMod 2上线性化，最大值作为归纳变量单调递减。
- key_objects: 正六边形配置(ZMod 6 → ℤ)、绝对差操作|f(j-1)-f(j+1)|、奇偶向量(ZMod 6 → ZMod 2)、最大值cmax、奇和不变量

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["parity_reduction（奇偶归约：将整数问题降到ZMod 2）", "invariant_analysis（奇和作为不变量）", "exhaustive_verification（穷举验证Phase 1的32种奇偶模式）", "case_analysis（Phase 2按最大值位置分情况）", "strong_induction（对cmax做强归纳）"]
- primary_pattern: parity_reduction_with_induction（奇偶归约+强归纳）
- knowledge_required: ["模运算（ZMod 2上的线性操作）", "绝对值的奇偶性质（|a-b|≡a+b mod 2）", "强归纳法", "奇数的幂仍为奇", "有限域上的向量操作"]
- key_insight: 在ZMod 2中|a-b|≡a+b，使移动在奇偶向量上变为线性操作（替换v(j)为v(j-1)+v(j+1)），结合奇和条件可将配置归约为单奇数项，再对最大值做强归纳。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 整数上的绝对差操作（直接在ℤ上分析|f(j-1)-f(j+1)|的移动）
- translation_to: ZMod 2上的线性操作（奇偶向量上的v(j)→v(j-1)+v(j+1)）
- translation_type: structural_simplification（结构简化：将非线性绝对值操作通过模2约简为线性操作，降低问题复杂度）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "direct_manipulation", gap_type: "method_translation"}
- tell_small_concepts: ["parity_reduction", "ZMod2_linearization", "absolute_difference_mod2", "odd_sum_invariant", "single_odd_entry", "maximum_induction", "exhaustive_parity_verification", "two_phase_strategy"]
- expected_ai_method: 直接在整数上尝试构造操作序列或寻找数值不变量，不利用奇偶性约简
- correct_method: 奇偶性归约（ZMod 2线性化）→穷举验证Phase 1→单奇数项→Phase 2案例分析→强归纳

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是。discrete_combinatorial覆盖问题类型，direct_manipulation覆盖bare AI预期方法，method_translation覆盖从直接操作到奇偶分析的翻译。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是，均为中等抽象粒度。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。

**拓扑进化建议**（如有）：无。现有拓扑分类足够。

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
- [ ] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？
- [ ] 粒度是否一致——你标注的值和已有值的粒度是否统一？
- [ ] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？
- [ ] 如果发现拓扑分类需要进化，在此写出建议：

**拓扑进化建议**（如有）：

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
- 局部tell_hint_pairs数量: 8 对
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 2 个，implicit型: 1 个

**局部pairs详情**：

| qa_round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到六边形配置和绝对差操作，但未注意到2003^2003的奇偶性 | 注意2003是奇数，故2003^2003是奇数，六数之和为奇——这是整个证明的起点 | 0.8 | 纯元认知观察 | false | {discrete_combinatorial, direct_manipulation, method_problem_mismatch} | ["hexagon_configuration", "absolute_difference_move", "odd_sum_start"] |
| 2 | AI列出方向但未将奇偶性分析作为核心工具 | 将奇偶性分析和归纳法列为重点方向，特别关注模运算 | 0.7 | 自由列举 | false | {discrete_combinatorial, enumeration_brute_force, search_space_estimation} | ["invariant", "parity_analysis", "induction", "modular_arithmetic"] |
| 3 | AI尝试找总和不变量但发现总和会变化，可能放弃 | 总和不是不变量，但模2下|a-b|≡a+b是关键线索——从总和转向奇偶性 | 0.5 | 小尝试 | false | {discrete_combinatorial, direct_calculation, method_problem_mismatch} | ["sum_change", "parity_mod2", "absolute_value_mod2"] |
| 4 | AI未意识到在ZMod 2中绝对差变为和，使操作线性化 | 在ZMod 2中|a-b|≡a+b，移动变为线性操作v(j)→v(j-1)+v(j+1)，从奇和出发可归约为单奇数项 | 0.4 | 思维操作引导 | false | {discrete_combinatorial, direct_manipulation, method_translation} | ["ZMod2_linearization", "linear_operation", "parity_vector", "odd_sum_reduction"] |
| 5 | AI知道要归约奇偶向量但不知道如何验证所有32种情况 | 用穷举验证（finite case analysis/decide），构造8组候选操作序列覆盖全部32种奇和奇偶模式 | 0.5 | 推进 | true | {discrete_combinatorial, case_by_case, knowledge_gap} | ["exhaustive_verification", "32_parity_patterns", "8_candidate_sequences", "single_odd_entry"] |
| 6 | AI有单奇数项配置但不知道如何利用最大值位置做案例分析 | 按最大值位置分情况：最大值在顶点0（奇）→看顶点2,4是否为0；最大值在偶数顶点→用[1,2,3,4,5]降低最大值 | 0.4 | 思维操作引导 | false | {discrete_combinatorial, case_by_case, structural_transformation} | ["maximum_position", "case_analysis", "vertex_zero_subcase", "cmax_reduction"] |
| 7 | AI有Phase 1和Phase 2但未将它们组合为归纳框架 | 对cmax做强归纳：Phase 1归约（cmax不增）→Phase 2归零或cmax严格递减→归纳终止 | 0.5 | 推进 | false | {discrete_combinatorial, logical_deduction, method_translation} | ["strong_induction", "cmax_monovariant", "termination", "two_phase_composition"] |
| 8 | AI有所有部件但未整合为完整证明 | 整合：奇和→Phase 1→单奇数项→旋转→Phase 2→归零或归纳→全零。关键转折是奇偶性线性化 | 0.6 | 能量传递引导 | false | {discrete_combinatorial, logical_deduction, method_problem_mismatch} | ["complete_proof_framework", "parity_linearization_insight", "two_phase_synthesis"] |

**全局pairs详情**：

| scope_type | scope | observation_point | tell | hint | hint_level | generalizability | why_not_visible_locally | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|---|---|
| path_feature | 整个证明路径：奇偶归约→单奇数项→最大值归纳 | null | AI试图直接构造到达全零的操作序列，看不到两阶段策略 | 先用奇偶性归约到单奇数项配置，再对最大值做强归纳——两阶段策略 | 0.5 | high——"先归约到特殊结构再做归纳"的模式可泛化到许多组合博弈问题 | 两阶段策略（Phase 1奇偶归约+Phase 2最大值递减）的整体结构只有在看完整个证明路径后才显现；每个阶段单独看时，无法预知下一阶段的存在和作用 | {discrete_combinatorial, direct_manipulation, method_translation} | ["two_phase_strategy", "parity_reduction", "maximum_induction", "structural_simplification"] |
| implicit | 2003^2003的奇偶性与整个策略的关联 | Q1 | AI看到2003^2003只觉得是一个大数，不意识到其奇偶性是证明的根基 | 2003是奇数→2003^2003是奇→六数之和为奇→奇偶性策略可用 | 0.7 | high——"特定数值的奇偶性决定策略可行性"的模式可泛化 | 2003^2003的奇偶性与整个奇偶归约策略的因果关系是隐含的：需要同时认识到(a)2003是奇数(b)奇数的幂仍奇(c)奇和是奇偶归约的前提——这三步推理在局部步骤中不可见 | {discrete_combinatorial, direct_manipulation, knowledge_gap} | ["odd_base", "odd_power", "odd_sum_invariant", "parity_strategy_foundation"] |
| path_feature | Phase 1的穷举验证：8组候选序列覆盖32种奇偶模式 | null | AI可能试图理论证明Phase 1而非穷举验证，或不知道需要多少组序列 | 用有限案例分析（decide）穷举验证32种奇和奇偶模式，8组候选序列即可覆盖 | 0.4 | medium——"有限状态空间用穷举验证"可泛化，但具体序列数依赖问题结构 | 8组候选序列的完整集合及其对32种奇偶模式的覆盖关系是全局路径特征：需要同时知道所有候选序列和所有需覆盖的模式才能验证完备性，局部看任何单组序列都无法确认覆盖性 | {discrete_combinatorial, case_by_case, knowledge_gap} | ["exhaustive_case_check", "finite_verification", "8_sequences_cover_32_patterns", "parity_completeness"] |

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会在整数层面直接尝试构造操作序列或寻找不变量，不会想到将问题降到ZMod 2做奇偶分析。即使注意到2003^2003是奇数，也不会意识到|a-b|≡a+b(mod 2)使操作线性化。缺乏穷举验证Phase 1和两阶段归纳策略，大概率无法完成证明。
- suitable_for_poc: ["tell端验证：parity_reduction的tell能否被形式化过滤命中", "hint端验证：奇偶性线性化的hint注入后bare AI能否走通", "两阶段策略的path_feature型tell能否被识别"]
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
2. 更新`problem_extraction_progress`集合中`_key="329414"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa2003p6"
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
    '_key': '329414',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa2003p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa2003p6')
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
- problem_id: compfiles_usa2003p6
- solution_method_type: parity_invariant_induction
- 局部(tell,hint)对数量: 8
- 全局(tell,hint)对数量: 3（2个path_feature型，1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，现有拓扑分类足够覆盖
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
