# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1997p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1997P5.lean
- **来源**: IMO 1997 P5
- **ArangoDB progress记录_key**: 329161（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1997P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Determine all pairs of integers 1 ≤ a, b that satisfy a^(b²) = b^a.
- 解答核心思路（1-2句话）：以2b²与a的大小关系做case split，在每个case中从指数方程提取整除关系（b²|a 或 a|b²），将指数方程降次为乘法方程d·b²=b^d（或a^d=b），再用不等式将参数限制在有限范围内，逐一验证。
- 解答关键步骤列表：
  1. Case 1 (2b² ≤ a)：将 b^a 拆为 (b²)^(b²)·b^(a-2b²)，由 aux₃ 推出 b²|a，令 a=d·b²
  2. 代入后得 d·b² = b^d（由 pow_left_inj），用 aux₁（n·b²=b^n → b≤1 或 n≤4）限制 d≤4
  3. interval_cases d=1,2,3,4：d=3→b=3,a=27；d=4→b=2,a=16；d=1→b=1,a=1；d=2无解
  4. Case 2 (a < 2b²)：将 (b²)^(b²) 拆为 a^(b²)·b^(2b²-a)，由 aux₃ 推出 a|b²，令 b²=d·a
  5. 代入后得 a^d = b（由 pow_left_inj），进而 (a^d)²=d·a，用 aux₂（b·n=(b^n)²→b≤1）推出 a≤1
  6. a=1→b=1，与Case 1重合
  7. 最终解集：{(1,1), (16,2), (27,3)}

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
| 1 | 纯元认知观察 | 0.85 | 观察方程 a^(b²) = b^a 的结构：两边各自的底数和指数是什么？底数和指数之间有什么交叉关系？ | 左边底数a指数b²，右边底数b指数a。底数和指数交叉出现——a既是左边底数又是右边指数，b既是右边底数又出现在左边指数中。这是一个交叉指数方程。 |
| 2 | 自由列举 | 0.75 | 对于寻找所有正整数解(a,b)，你能想到哪些可能的攻击方向？ | 取对数比较 b²·ln(a) = a·ln(b) → ln(a)/a = ln(b)/b²；试小值枚举；利用整除性分析；比较a与b²的大小做case split；利用素因子分解。 |
| 3 | 小尝试 | 0.4 | 试试取对数的方法：b²·ln(a) = a·ln(b)，即 ln(a)/a = ln(b)/b²。这个方向能帮你找到所有整数解吗？ | 取对数后得到连续函数方程，对整数解的离散结构没有直接帮助。f(x)=ln(x)/x 非单调，难以直接推导。这个方向对找所有整数解不太有效。 |
| 4 | 思维操作引导 | 0.6 | 回到整数结构。关键操作：比较 a 和 2b² 的大小。为什么选 2b² 而不是 b²？想想 b^a 的指数 a 和 (b²)^(b²) 的指数 b² 之间的关系。 | 选2b²是因为：如果a≥2b²，则b^a=(b²)^(b²)·b^(a-2b²)，这样(b²)^(b²)可以和a^(b²)的指数b²匹配，提取整除关系b²|a。类似地a<2b²时反方向提取a|b²。2b²是让分解后剩余指数非负的自然分界点。 |
| 5 | 推进 | 0.5 | 在Case 1 (a≥2b²)中，你已经得到b²|a，令a=d·b²。代入原方程后能简化成什么形式？ | a^(b²)=(d·b²)^(b²)=d^(b²)·b^(2b²)，b^a=b^(d·b²)。所以d^(b²)·b^(2b²)=b^(d·b²)，由pow_left_inj得d·b²=b^d。 |
| 6 | 思维操作引导 | 0.55 | 现在有d·b²=b^d。关键操作：用不等式给d设上界。对于b≥2,n≥5，n·b²<b^n。这意味着d·b²=b^d只能在d≤4或b≤1时成立。逐一检查d=1,2,3,4。 | b=1→a=d,d^1=1→d=1→(1,1)。d=1→b=1; d=2→2b²=b²矛盾; d=3→3b²=b³→b=3→a=27; d=4→4b²=b⁴→b=2→a=16。 |
| 7 | 能量传递引导 | 0.7 | 你已经在Case 1找到(1,1),(16,2),(27,3)。Case 2(a<2b²)用对称方法提取a|b²，得a^d=b，用不等式推出a≤1→a=1→b=1。验证所有解。 | Case 2推出a=1→b=1，与Case 1重合。最终解集={(1,1),(16,2),(27,3)}。验证：1^1=1^1✓; 16^4=2^16=65536✓; 27^9=3^27✓。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4 (R1,R2,R5,R7)
- knowledge_rounds（思维操作引导的轮数）: 2 (R4,R6)
- level_sum: 0.85+0.75+0.4+0.6+0.5+0.55+0.7 = 4.35
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R6（需要知道如何构造辅助不等式n·b²<b^n来限制参数范围）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R4（关键思维转折：选择2b²作为case split的分界点，而非直观的b²）

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
- problem_type: characterization（求所有满足条件的整数对，本质是刻画解集）
- structure_features: 交叉指数方程 a^(b²)=b^a，底数与指数交叉出现；需要case split + 整除性提取 + 不等式限制 + 有限枚举
- key_objects: 正整数对(a,b)，指数方程，整除关系 b²|a / a|b²，辅助不等式 n·b²<b^n

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [case_split_by_size_comparison, divisibility_extraction_from_exponentials, inequality_bounding, finite_enumeration, symmetric_argument]
- primary_pattern: divisibility_extraction_from_exponentials（从指数方程中提取整除关系是核心思维模式）
- knowledge_required: [指数定律与幂的injectivity, 整除与因数分解, 归纳法证明不等式, 自然数幂的比较]
- key_insight: 选择2b²（而非b²）作为case split分界点，使得分解后能匹配指数b²从而提取整除关系b²|a或a|b²

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接指数方程操作（取对数、幂比较）
- translation_to: 整除性分析 + 不等式限制 + 有限枚举（将指数方程翻译为乘法方程d·b²=b^d，再用不等式将连续无穷解空间截断为有限枚举）
- translation_type: structural_transformation（通过case split和整除提取，将指数方程的结构从"底数-指数交叉"翻译为"乘法-幂"的简单关系）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_manipulation, gap_type: structural_transformation}
- tell_small_concepts: [交叉指数方程, case split on 2b² vs a, 整除性提取 b²|a, 幂的injectivity, 辅助不等式 n·b²<b^n, 有限枚举 d≤4]
- expected_ai_method: direct_manipulation（bare AI会尝试取对数、直接比较幂的大小、或枚举小值，但不会想到通过case split提取整除关系）
- correct_method: case split by size comparison + divisibility extraction + inequality bounding + finite enumeration

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是。characterization已有，direct_manipulation已有，structural_transformation已有。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是，三个值都是中等偏抽象粒度。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。这道题的tell核心是"从指数方程提取整除关系"，由structural_transformation充分描述。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。

**拓扑进化建议**（如有）：无。当前拓扑分类体系完全覆盖此题。

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

R1: tell="AI面对交叉指数方程a^(b²)=b^a，未识别底数-指数交叉结构", hint="观察方程结构，识别底数和指数的交叉关系", hint_level=0.85, situation_type=纯元认知观察, is_knowledge_bottleneck=false, tell_topology={problem_type:characterization, ai_method_type:direct_manipulation, gap_type:method_problem_mismatch}, tell_small_concepts=[交叉指数方程, 底数指数交叉]

R2: tell="AI列出方向但未注意到整除性分析这条路径", hint="列出所有可能方向，特别关注整数结构方向", hint_level=0.75, situation_type=自由列举, is_knowledge_bottleneck=false, tell_topology={problem_type:characterization, ai_method_type:enumeration_brute_force, gap_type:search_space_estimation}, tell_small_concepts=[取对数, 小值枚举, 整除性分析, case split]

R3: tell="AI选择了取对数方向，走入连续函数分析，偏离整数解的离散结构", hint="试取对数方法，评估其对整数解问题的有效性", hint_level=0.4, situation_type=小尝试, is_knowledge_bottleneck=false, tell_topology={problem_type:characterization, ai_method_type:continuous_analytic, gap_type:method_problem_mismatch}, tell_small_concepts=[取对数, 连续函数, 离散结构不匹配]

R4: tell="AI回到整数结构但未想到选择2b²作为分界点", hint="比较a与2b²的大小，理解为什么选2b²而非b²", hint_level=0.6, situation_type=思维操作引导, is_knowledge_bottleneck=false, tell_topology={problem_type:characterization, ai_method_type:direct_manipulation, gap_type:structural_transformation}, tell_small_concepts=[case split on 2b², 指数匹配, 整除提取]

R5: tell="AI得到b²|a但未完成代入简化", hint="令a=d·b²代入原方程，用幂的injectivity简化", hint_level=0.5, situation_type=推进, is_knowledge_bottleneck=false, tell_topology={problem_type:characterization, ai_method_type:algebraic_identity, gap_type:method_translation}, tell_small_concepts=[幂的injectivity, 代入简化, d·b²=b^d]

R6: tell="AI得到d·b²=b^d但未想到用不等式限制d的范围", hint="用辅助不等式n·b²<b^n给d设上界，限制到d≤4", hint_level=0.55, situation_type=思维操作引导, is_knowledge_bottleneck=true, tell_topology={problem_type:characterization, ai_method_type:direct_calculation, gap_type:knowledge_gap}, tell_small_concepts=[辅助不等式, n·b²<b^n, 有限枚举, d≤4]

R7: tell="AI已找到Case 1的解，需要完成Case 2并验证", hint="对称处理Case 2，验证所有解", hint_level=0.7, situation_type=能量传递引导, is_knowledge_bottleneck=false, tell_topology={problem_type:characterization, ai_method_type:logical_deduction, gap_type:method_translation}, tell_small_concepts=[对称论证, a|b², 解集验证]

**全局tell_hint_pairs详情**：

Global 1 (path_feature):
- scope_type: path_feature
- scope: 整个解题路径——从交叉指数方程到case split到整除提取到不等式限制到有限枚举
- observation_point: null
- tell: "完整路径特征是'指数方程→整除关系→不等式限制→有限枚举'的降维链条，bare AI只看到指数方程的直接操作"
- hint: "识别指数方程中隐藏的整除结构，通过case split提取整除关系，将无穷搜索空间压缩为有限枚举"
- hint_level: 0.8
- generalizability: "high——此路径模式适用于所有交叉指数方程的整数解问题"
- why_not_visible_locally: "在局部视角中，AI看到的是a^(b²)=b^a这个整体方程，每一步的操作（取对数、比较大小）都是对整个方程的直接操作。'通过case split提取整除关系'这个路径特征需要同时看到：(1)方程的指数结构允许分解，(2)分解后可以匹配指数提取整除，(3)整除关系可以降次——这三步在局部视角中不可见，因为它们需要从全局角度理解指数方程的代数结构。"
- tell_topology: {problem_type: characterization, ai_method_type: direct_manipulation, gap_type: structural_transformation}
- tell_small_concepts: [指数方程降维, 整除性提取, case split, 不等式限制, 有限枚举]

Global 2 (implicit):
- scope_type: implicit
- scope: R4中的关键分叉——选择2b²而非b²作为分界点
- observation_point: "R4"
- tell: "在R4处，AI面临分叉：选择b²还是2b²作为case split分界点。选择b²是直觉的但无法提取整除关系（分解后剩余指数可能为负），选择2b²才能让(b²)^(b²)项与a^(b²)的指数匹配。这个蕴含信息在R4局部不可见。"
- hint: "选择分界点时要考虑分解后指数的非负性和可匹配性，2b²是让b^a=(b²)^(b²)·b^(a-2b²)成立的自然分界"
- hint_level: 0.65
- generalizability: "medium——'选择分界点使分解后指数非负且可匹配'是一个可泛化的启发式，但具体选2b²依赖于本题的b²指数结构"
- why_not_visible_locally: "在R4局部视角中，AI看到的是'比较a和某个量的大小'，直觉选择b²作为分界点。但选择2b²的真正原因是：只有当a≥2b²时，b^a才能分解为(b²)^(b²)·b^(a-2b²)，使得(b²)^(b²)的指数b²与a^(b²)的指数b²匹配，从而提取整除关系。这个'匹配指数以提取整除'的蕴含信息在R4的局部视角中不可见——它需要预见到后续的整除提取步骤。"
- tell_topology: {problem_type: characterization, ai_method_type: direct_manipulation, gap_type: structural_transformation}
- tell_small_concepts: [分界点选择, 2b² vs b², 指数匹配, 分解后非负性]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试取对数得到ln(a)/a=ln(b)/b²，然后试图用连续函数分析找整数解，但这条路无法系统枚举所有解。也可能试小值枚举找到(1,1)但遗漏(16,2)和(27,3)。关键失败在于不会想到通过case split on 2b²提取整除关系，从而无法将无穷搜索空间压缩为有限枚举。
- suitable_for_poc: ["POC-VMS-8（脉络继承+方向注入验证）", "POC-VMS-9/10（tell端去特化+形式化过滤验证）", "bare_vs_guided对照实验（验证hint端有效性）"]
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
2. 更新`problem_extraction_progress`集合中`_key="329161"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1997p5"
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
    '_key': '329161',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1997p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1997p5')
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
- problem_id: compfiles_imo1997p5
- solution_method_type: case_split_by_size_comparison + divisibility_extraction + inequality_bounding + finite_enumeration
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。当前拓扑分类体系（problem_type/ai_method_type/gap_type）完全覆盖此题，三个维度均使用已有值，粒度一致。
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
