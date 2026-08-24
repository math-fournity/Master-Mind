# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2021p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2021P5.lean
- **来源**: USA 2021 P5
- **ArangoDB progress记录_key**: 329492（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2021P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设 n ≥ 4 为整数。求以下 2n 个方程组的所有正实数解：
  - 奇数下标：a₁ = 1/a₂ₙ + 1/a₂, a₃ = 1/a₂ + 1/a₄, ..., a₂ₙ₋₁ = 1/a₂ₙ₋₂ + 1/a₂ₙ
  - 偶数下标：a₂ = a₁ + a₃, a₄ = a₃ + a₅, ..., a₂ₙ = a₂ₙ₋₁ + a₁
  - 即奇数下标变量 = 相邻偶数下标变量的倒数和，偶数下标变量 = 相邻奇数下标变量的和
- 解答核心思路（1-2句话）：消去奇数下标变量得到偶数下标变量的递推关系 a_k = 1/a_{k-1} + 2/a_k + 1/a_{k+1}，然后用极值法（min-max argument）证明所有偶数下标变量相等，解出常数为2，再回代得奇数下标变量为1。
- 解答关键步骤列表：
  1. 消去奇数下标变量：将 b_k = 1/a_{k-1} + 1/a_k 代入 a_k = b_k + b_{k+1}，得 a_k = 1/a_{k-1} + 2/a_k + 1/a_{k+1}
  2. 取偶数下标变量序列的最小值点 i 和最大值点 j
  3. 在最小值点 i：由 1/a_{i-1} ≥ 1/a_j 和 1/a_{i+1} ≥ 1/a_j，得 2/a_i + 2/a_j ≤ a_i
  4. 在最大值点 j：由 1/a_{j-1} ≤ 1/a_i 和 1/a_{j+1} ≤ 1/a_i，得 a_j ≤ 2/a_i + 2/a_j
  5. 结合 a_i ≤ a_j 和上述两个不等式，得 a_i = a_j，故所有偶数下标变量相等
  6. 常数 c 满足 c = 4/c，即 c² = 4，正解 c = 2
  7. 回代得 b_k = 1/2 + 1/2 = 1，验证 (1,2,1,2,...) 确为解

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
| 1 | 纯元认知观察 | 0.7 | 观察这个方程组的结构，你能描述出它的特征吗？特别注意奇数下标和偶数下标变量的方程有什么不同。 | 这是一个循环的2n方程组。奇数下标变量满足 a_{2k-1} = 1/a_{2k-2} + 1/a_{2k}（相邻偶数变量的倒数和），偶数下标变量满足 a_{2k} = a_{2k-1} + a_{2k+1}（相邻奇数变量的和）。系统是循环的：a_{2n}与a_1相连。两类方程交替出现，结构上有明显的奇偶分层特征。 |
| 2 | 自由列举 | 0.7 | 对于这样的循环方程组，你有哪些可能的解题方向？ | 可能方向：1) 假设所有变量相等直接求解；2) 消元法逐步代入；3) 利用循环对称性；4) 极值法（min-max argument）；5) 生成函数/母函数方法；6) 不动点迭代；7) 矩阵表示求特征值。 |
| 3 | 小尝试 | 0.3 | 试试假设所有偶数下标变量相等为c，所有奇数下标变量相等为d，看看能得到什么。 | 若 a_{2k}=c, a_{2k-1}=d，则 c = 2d 且 d = 2/c。解得 c=2, d=1。所以 (1,2,1,2,...) 是一个解。但这只证明了存在性，没有证明唯一性——需要证明所有正实数解都必须是这个形式。 |
| 4 | 思维操作引导 | 0.4 | 你找到了一个解但需要证明唯一性。尝试消去奇数下标变量，只保留偶数下标变量之间的关系。具体地，将奇数变量的表达式代入偶数变量的方程中。 | 将 b_k = 1/a_{k-1} + 1/a_k 代入 a_k = b_k + b_{k+1}，得 a_k = 1/a_{k-1} + 1/a_k + 1/a_k + 1/a_{k+1} = 1/a_{k-1} + 2/a_k + 1/a_{k+1}。这是一个只关于偶数下标变量的递推关系。 |
| 5 | 思维操作引导 | 0.5 | 现在你有了一个只关于偶数下标变量的关系 a_k = 1/a_{k-1} + 2/a_k + 1/a_{k+1}。考虑用极值法：设a在某点i取最小值，某点j取最大值。在最小值点和最大值点分别能推出什么不等式？ | 在最小值点i：a_{i-1} ≥ a_i, a_{i+1} ≥ a_i，所以 1/a_{i-1} ≤ 1/a_j（因为a_j是最大值），1/a_{i+1} ≤ 1/a_j。因此 a_i = 1/a_{i-1} + 2/a_i + 1/a_{i+1} ≤ ... 等等，需要更仔细：1/a_{i-1} ≥ 1/a_j（因为a_{i-1} ≤ a_j），所以 a_i ≥ 1/a_j + 2/a_i + 1/a_j = 2/a_i + 2/a_j。在最大值点j类似得 a_j ≤ 2/a_i + 2/a_j。 |
| 6 | 推进 | 0.5 | 从这两个不等式 2/a_i + 2/a_j ≤ a_i 和 a_j ≤ 2/a_i + 2/a_j，结合 a_i ≤ a_j，能推出什么？ | 由 a_j ≤ 2/a_i + 2/a_j ≤ a_i，而 a_i ≤ a_j，所以 a_i = a_j。既然最小值等于最大值，所有偶数下标变量都相等，即a是常数。 |
| 7 | 能量传递引导 | 0.3 | 既然所有偶数下标变量都是常数c，求出c的值，然后回代求奇数下标变量。 | c = 1/c + 2/c + 1/c = 4/c，所以 c² = 4，c = 2（正解）。然后 b_k = 1/a_{k-1} + 1/a_k = 1/2 + 1/2 = 1。验证：a_{2k} = 1+1 = 2 ✓，a_{2k-1} = 1/2+1/2 = 1 ✓。唯一正实数解为 (1,2,1,2,...)。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.7+0.7+0.3+0.4+0.5+0.5+0.3 = 3.4
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
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
- problem_type: characterization（求所有正实数解，即刻画全部解的结构）
- structure_features: 循环方程组，2n个方程2n个未知数，奇偶下标交替使用不同类型的方程（倒数和 vs 直接和），循环边界条件连接首尾
- key_objects: 正实数序列 {a_k}（偶数下标子序列和奇数下标子序列），循环指标 ZMod n，递推关系 a_k = 1/a_{k-1} + 2/a_k + 1/a_{k+1}

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["奇偶分层消元", "极值原理（min-max argument）", "不等式夹逼", "常数化降维", "回代验证"]
- primary_pattern: 极值原理（min-max argument）——通过取最小值和最大值点构造夹逼不等式，证明所有变量相等
- knowledge_required: ["循环方程组", "消元法", "极值原理/最大最小值论证", "倒数函数的单调性", "不等式夹逼"]
- key_insight: 在偶数下标变量的递推关系中取最小值点和最大值点，利用倒数函数的单调性构造两个方向相反的不等式，夹逼出 min=max 从而所有变量相等

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接方程求解（假设所有变量相等，代入验证）
- translation_to: 极值论证（消元后用min-max argument证明唯一性）
- translation_type: method_translation（从代数求解方法翻译到极值论证方法，方法层面的根本转换）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "equation_solving", gap_type: "method_problem_mismatch"}
- tell_small_concepts: ["循环方程组", "奇偶分层", "消元", "极值原理", "min-max argument", "倒数单调性", "夹逼不等式", "常数化"]
- expected_ai_method: bare AI会尝试直接假设所有变量相等或逐步消元求解，能找到解但无法证明唯一性——缺乏极值论证的思维跳跃
- correct_method: 消去奇数下标变量得到偶数下标递推关系，用极值法（min-max argument）构造夹逼不等式证明所有偶数下标变量相等，再解常数和回代

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 可以。problem_type=characterization（已有），ai_method_type=equation_solving（已有），gap_type=method_problem_mismatch（已有）
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 一致，都是中等抽象粒度
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。这道题的核心tell是"从方程求解到极值论证的方法转换"，三个维度能区分
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化，现有分类体系完全覆盖

**拓扑进化建议**（如有）：无，现有拓扑分类体系完全够用

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

**局部pair详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到循环方程组但未识别奇偶分层的交替结构 | 观察奇数下标和偶数下标方程的不同类型 | 0.7 | 纯元认知观察 | false | {characterization, direct_calculation, method_problem_mismatch} | ["循环方程组", "奇偶分层", "方程类型交替"] |
| 2 | AI列出方向但未优先考虑极值法 | 考虑极值法/min-max argument作为可能方向 | 0.7 | 自由列举 | false | {characterization, enumeration_brute_force, method_problem_mismatch} | ["极值法", "方法列举", "min-max argument"] |
| 3 | AI假设所有变量相等找到解但无法证明唯一性 | 需要证明唯一性，尝试消元 | 0.3 | 小尝试 | false | {characterization, equation_solving, method_problem_mismatch} | ["假设相等", "存在性vs唯一性", "消元"] |
| 4 | AI不知道如何消去奇数变量 | 将奇数变量表达式代入偶数变量方程 | 0.4 | 思维操作引导 | false | {characterization, direct_manipulation, structural_transformation} | ["消元", "代入", "递推关系"] |
| 5 | AI有递推关系但未想到用极值法 | 取最小值点和最大值点，利用倒数单调性构造不等式 | 0.5 | 思维操作引导 | true | {characterization, direct_calculation, knowledge_gap} | ["极值原理", "min-max argument", "倒数单调性", "夹逼不等式"] |
| 6 | AI有两个不等式但未想到夹逼出min=max | 结合a_i≤a_j和两个不等式夹逼出a_i=a_j | 0.5 | 推进 | false | {characterization, logical_deduction, method_problem_mismatch} | ["夹逼", "min=max", "常数化"] |
| 7 | AI知道a是常数但未求解具体值 | 代入递推关系解c²=4，回代求b | 0.3 | 能量传递引导 | false | {characterization, direct_calculation, knowledge_gap} | ["常数求解", "回代验证", "c²=4"] |

**全局pair详情**：

1. path_feature型:
- scope: "整个证明路径：消元→极值→夹逼→常数化→回代"
- observation_point: null
- tell: "从直接求解到极值论证的完整路径转换——需要先消元降维，再用极值法证明唯一性，最后回代求解"
- hint: "将问题分解为三个阶段：1)消元得到单变量族递推关系 2)极值法证明所有变量相等 3)解常数并回代"
- hint_level: 0.6
- generalizability: "high — 极值法证明变量相等是循环/对称方程组求唯一解的通用策略"
- why_not_visible_locally: "在任何一个单独步骤中，AI只能看到当前的代数操作，看不到'消元→极值→夹逼'这个三阶段路径的全局结构。特别是R3找到解后，AI会认为问题已解决而停止，看不到还需要极值法来证明唯一性这个全局需求"
- tell_topology: {characterization, equation_solving, method_problem_mismatch}
- tell_small_concepts: ["消元降维", "极值论证", "夹逼证明唯一性", "三阶段路径"]

2. implicit型:
- scope: "递推关系 a_k = 1/a_{k-1} + 2/a_k + 1/a_{k+1} 中蕴含的极值结构"
- observation_point: "R5"
- tell: "递推关系中的倒数项在极值点处会产生方向相反的不等式——这是递推关系本身蕴含的但需要极值视角才能看到的结构"
- hint: "在递推关系中取最小值点和最大值点，利用倒数函数的递减性：最小值点的邻居≥最小值→倒数≤最大值的倒数；最大值点的邻居≤最大值→倒数≥最小值的倒数"
- hint_level: 0.5
- generalizability: "medium — 倒数单调性+极值法的组合在含倒数的递推关系中通用，但具体不等式方向需根据问题调整"
- why_not_visible_locally: "在R4得到递推关系后，AI看到的是一个代数等式，不会自动想到'在这个等式上取极值点'。极值法的适用性隐含在等式的结构中（每项都是正数的倒数，且变量在循环指标上取值），但这个蕴含关系在局部视角下不可见——需要从全局角度意识到'要证明所有变量相等'这个目标，才能反向推导出'需要用极值法'"
- tell_topology: {characterization, direct_calculation, knowledge_gap}
- tell_small_concepts: ["递推关系蕴含极值结构", "倒数单调性", "极值点不等式方向"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会假设所有偶数下标变量相等、所有奇数下标变量相等，找到(1,2,1,2,...)这个解后就停止，认为问题已解决。不会意识到需要证明唯一性，更不会想到用极值法（min-max argument）来证明所有变量必须相等。这是典型的"找到解≠求出所有解"的错误。
- suitable_for_poc: ["POC-VMS-hint-injection（hint端验证：注入极值法方向后能否引导AI完成唯一性证明）", "POC-VMS-tell-detection（tell端验证：能否从AI的thinking中检测到'找到解后停止'的分叉信号）", "POC-VMS-level-discrimination（区分能做存在性vs能做唯一性的AI水平）"]
- discriminates_levels: true（能区分只会找解的AI和能证明唯一性的AI，极值法是明显的水平分界线）

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
2. 更新`problem_extraction_progress`集合中`_key="329492"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa2021p5"
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
    '_key': '329492',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa2021p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa2021p5')
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
- problem_id: compfiles_usa2021p5
- solution_method_type: extremal_argument
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，现有拓扑分类体系完全够用（characterization / equation_solving / method_problem_mismatch 均为已有值）
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
