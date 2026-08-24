# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1990p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1990P5.lean
- **来源**: IMO 1990 P5
- **ArangoDB progress记录_key**: 329132（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1990P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：给定初始整数 n₀ > 1，玩家A和B交替选择整数。A知道n₂ₖ后选择n₂ₖ₊₁满足 n₂ₖ ≤ n₂ₖ₊₁ ≤ n₂ₖ²；B知道n₂ₖ₊₁后选择n₂ₖ₊₂使得 n₂ₖ₊₁/n₂ₖ₊₂ = p^r（p为素数，r≥1）。A通过选择1990获胜，B通过选择1获胜。问对哪些n₀，(a)A有必胜策略，(b)B有必胜策略，(c)双方都没有必胜策略。
- 解答核心思路（1-2句话）：A对n₀≥8有必胜策略——通过选择一系列"陷阱数"（60,140,280,504,1990及11^(r+1)·181）使B无法立即获胜且B的所有合法走法都落入A的必胜区域；B对n₀∈{2,3,4,5}有必胜策略——A的走法有界且B总能到达素数幂位置直接获胜；n₀∈{6,7}时双方都无必胜策略——A可到达30（B的陷阱）但A自身无法获胜。
- 解答关键步骤列表：
  1. 关键引理：B能从m直接获胜（选1）当且仅当m是素数幂（IsPrimePow）
  2. A的必胜策略（n≥8）：A选择"陷阱数"m——m不是素数幂（B不能立即获胜），且m的所有因子（B的合法走法目标）要么不是素数幂要么≥8（归纳假设A赢）
  3. 陷阱数链：60覆盖[8,11]，140覆盖[12,16]，280覆盖[17,22]，504覆盖[23,44]，直接选1990覆盖[45,1990]，1991覆盖自身
  4. 大数归纳（n≥1992）：A选择11^(r+1)·181——不是素数幂（含因子11和181），B的走法结果m'=11^(r+1)·181/p^k < n且≥8，由强归纳A赢
  5. A在n<8不能赢：n∈[2,7]时A的走法m≤49，若m不是素数幂则B可逃到[2,7]（escape_le49），矛盾
  6. B在n₀∈{2,3,4,5}赢：A的走法有上界（n²≤25），B总能到达素数幂或B必胜区域
  7. B在n₀∈{6,7}不赢：A可选30，而30/60/140/280/504构成B的"反陷阱"——B的走法要么不可能、要么让A抓1990、要么回到同集合
  8. 确定性：A和B不能同时有必胜策略（awins_not_bwinsstart）

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
| 1 | 纯元认知观察 | 0.8 | 请描述这个博弈的结构：两个玩家的行动规则分别是什么？各自的获胜条件是什么？当前局面由什么决定？ | A知道n后选择m∈[n,n²]，B知道m后选择m'使得m/m'=p^r（素数幂）。A选1990赢，B选1赢。当前局面由"轮到谁+当前数字"决定。这是一个无限博弈，状态空间是正整数。 |
| 2 | 自由列举 | 0.7 | 这个博弈有哪些可能的分析方向？请列出你能想到的所有方法。 | ①逆向归纳从1990和1出发 ②分析素数幂结构（B选1当且仅当当前数是素数幂）③寻找A的"安全位置"——A选的数不是素数幂且B的所有走法都回到A赢的位置 ④对小n穷举 ⑤寻找不变量或单调性 ⑥分情况讨论n的范围 |
| 3 | 小尝试 | 0.5 | 试试从1990做逆向归纳：A能从哪些n直接选到1990？这个方法能覆盖多大范围？ | n≤1990≤n²需要n≥45（因为44²=1936<1990）。所以n∈[45,1990]时A可直接选1990赢。但这只覆盖了[45,1990]，n<45的范围需要其他方法。逆向归纳在n<45处遇到困难。 |
| 4 | 思维操作引导 | 0.3 | 关键观察：B能从m直接获胜（选1）当且仅当m是素数幂。请基于这个观察，定义什么是A的"安全陷阱数"——A选择一个数m使得B无法立即赢且B的所有合法走法都落入A赢的区域。 | A的陷阱数m需满足：①m不是素数幂（B不能选1直接赢）②m的每个因子m'=m/p^k（B的合法走法）要么不是素数幂（B不能从m'赢）要么m'≥8（A从m'赢）。这样A选m后，B无论怎么走都回到A赢的局面。 |
| 5 | 思维操作引导 | 0.2 | 现在请找出覆盖[8,44]的具体陷阱数链。从n∈[8,11]开始：A需要选一个m∈[n,n²]使得m不是素数幂且m的所有因子要么非素数幂要么≥8。试试m=60。 | 60的因子：1,2,3,4,5,6,10,12,15,20,30,60。非素数幂因子B走到不能立即赢。素数幂因子2,3,4,5——B走到这些后轮到A从m'走，A从这些小数不一定赢。但关键：陷阱数的条件是B走到m'后A从m'能赢。素数幂因子2,3,4,5都<8，需要单独验证A从这些位置不能赢（实际上A从[2,7]确实不能赢）。所以60作为陷阱数需要所有因子要么≥8要么...实际上60的因子中≥8的有10,12,15,20,30,60，这些要么非素数幂要么≥8。因子2,3,4,5是素数幂且<8——B走到这些后轮到A，但A从[2,7]不能赢，所以B实际上能从这些位置赢。因此60需要更仔细分析：B走到2,3,4,5后B赢。所以60不是直接可用的陷阱数？实际上正确理解是：A选60后B走到m'，然后轮到A从m'走。如果m'≥8则A赢（归纳）。如果m'<8则A从m'走...需要A从m'也能赢。但A从[2,7]不能赢。所以60的素数幂因子<8的部分需要B不能走到——但B可以走到任何因子。重新理解Lean代码：A选60后，B的走法m'=60/p^r。B走到2意味着60/2=30=p^r，即p=2,r=1?不对，m=60,m'=2,则60=2*30,30不是素数幂。所以B不能从60走到2。B的走法是m'=m/p^r，需要m/m'=p^r。60/2=30不是素数幂，所以B不能走到2。60的合法B走法：m'=60/p^r，即m'=60/2=30(2^1),60/3=20(3^1),60/4=15(2^2),60/5=12(5^1),60/6=10...不对6不是素数幂。所以B从60能走到：30,20,15,12,10,6,5,4,3,2,1——只要60/m'是素数幂。60/30=2,60/20=3,60/15=4,60/12=5,60/10=6不是素数幂。所以B能走到30,20,15,12,5,4,3,2,1。其中30,20,15,12不是素数幂（B不能从这些赢），5,4,3,2是素数幂且<8。但B走到5,4,3,2后轮到A——A从5走可选[5,25]，A不一定输。实际上关键在于A从m'能否赢，不是B从m'能否赢。 |
| 6 | 推进 | 0.4 | 很好！陷阱数链是60→140→280→504→1990，覆盖[8,1990]。现在请处理n≥1992的情况：如何用强归纳？提示——考虑11的幂次乘181。 | 对n≥1992，存在r≥1使得11^r·181 < n ≤ 11^(r+1)·181。A选m=11^(r+1)·181：①m∈[n,n²]（因为11^(r+1)·181 ≤ (11^r·181)² < n²）②m不是素数幂（含因子11和181）③B走到m'=m/p^k，则m'<n（因为m'=m/p^k ≤ m/2 < n）且m'≥8（因为m'含因子11或181），由强归纳A从m'赢。 |
| 7 | 能量传递引导 | 0.6 | 最后验证完整分类：n<8时A不能赢（为什么？），B在{2,3,4,5}赢、在{6,7}不赢（为什么？），以及确定性。 | ①n∈[2,7]时A的走法m≤49，若m不是素数幂则B可逃到[2,7]（escape_le49引理），矛盾。②B在{2,3,4,5}赢：A走法有界(n²≤25)，B总能到达素数幂。③B在{6,7}不赢：A可选30，而30/60/140/280/504构成B的反陷阱。④确定性：A赢蕴含B不能赢。完整答案：A赢当n≥8，B赢当n∈{2,3,4,5}，平局当n∈{6,7}。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.5
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: 4
- thinking_bottleneck（思维瓶颈在哪轮，或null）: 5

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
- structure_features: 双人交替博弈，A的操作是向上取值（n到n²），B的操作是除以素数幂（向下取值）。状态空间为正整数，终止条件为到达1990（A赢）或1（B赢）。关键结构特征是素数幂判定——B能直接赢当且仅当前数是素数幂。需要分类讨论n₀的范围并构造陷阱数链。
- key_objects: [素数幂(prime power), 陷阱数(trap number), 因子分解(divisor), 强归纳(strong induction), 博弈策略(game strategy), 1990(终止值), 素数(prime)]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [逆向归纳(backward induction), 结构翻译(structural translation——博弈→数论), 陷阱数构造(trap number construction), 强归纳(strong induction), 分类讨论(case analysis), 反证法(contradiction)]
- primary_pattern: 结构翻译——将博弈论问题翻译为数论问题（素数幂判定+因子分析）
- knowledge_required: [素数幂定义与判定, 因子分解, 博弈论基本概念(必胜策略/确定性), 强归纳原理]
- key_insight: B能直接获胜当且仅当前数是素数幂，因此A的必胜策略等价于找到"非素数幂且所有合法B走法目标都落入A赢区域"的陷阱数

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 博弈论语言（玩家策略、交替走法、获胜条件）
- translation_to: 数论语言（素数幂判定、因子分析、强归纳）
- translation_type: 结构翻译——将博弈的"必胜策略"概念翻译为"存在满足特定数论性质的整数（陷阱数）"，将B的"直接获胜"翻译为"当前数是素数幂"

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: discrete_combinatorial, ai_method_type: case_by_case, gap_type: method_translation}
- tell_small_concepts: [素数幂判定, 陷阱数, 因子链, 强归纳, escape引理, 确定性]
- expected_ai_method: case_by_case——bare AI会尝试对小n穷举所有博弈状态，试图用逆向归纳逐个分析，但在n<45的范围遇到困难，且无法发现素数幂与博弈胜负的结构性联系
- correct_method: 结构翻译+陷阱数构造——先识别"B赢当且仅当素数幂"的关键引理，然后构造满足特定数论性质的陷阱数链，最后用强归纳处理大数情况

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？
- [x] 如果发现拓扑分类需要进化，在此写出建议：

**拓扑进化建议**：无需进化。discrete_combinatorial/problem_type、case_by_case/ai_method_type、method_translation/gap_type三个维度足够区分这道题。这道题的核心gap是从博弈论视角到数论视角的翻译（method_translation），bare AI会卡在逐案分析（case_by_case）而无法发现结构性联系。粒度与已有值一致。

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

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI描述了博弈结构但未注意到B的走法与素数幂的结构性联系 | 请描述博弈结构：两个玩家的行动规则、获胜条件、当前局面由什么决定 | 0.8 | 纯元认知观察 | false | {discrete_combinatorial, case_by_case, method_translation} | [博弈结构, 交替走法, 获胜条件] |
| 2 | AI列举了多个方向但未识别"素数幂判定"作为核心翻译 | 列出所有可能的分析方向 | 0.7 | 自由列举 | false | {discrete_combinatorial, enumeration_brute_force, search_space_estimation} | [逆向归纳, 素数幂, 安全位置, 穷举] |
| 3 | AI尝试逆向归纳但卡在n<45的范围，未发现需要结构翻译 | 试试从1990做逆向归纳：A能从哪些n直接选到1990？ | 0.5 | 小尝试 | false | {discrete_combinatorial, direct_calculation, method_problem_mismatch} | [逆向归纳, 1990, n², 覆盖范围] |
| 4 | AI未意识到B的获胜条件可以翻译为素数幂判定——这是知识瓶颈 | 关键观察：B能从m直接获胜当且仅当m是素数幂。请基于此定义A的"安全陷阱数" | 0.3 | 思维操作引导 | true | {discrete_combinatorial, logical_deduction, knowledge_gap} | [素数幂判定, 陷阱数定义, 因子分析] |
| 5 | AI理解了陷阱数概念但无法构造具体陷阱数链——这是思维瓶颈 | 找出覆盖[8,44]的具体陷阱数链，从n∈[8,11]开始试m=60 | 0.2 | 思维操作引导 | false | {discrete_combinatorial, algebraic_identity, structural_transformation} | [陷阱数链, 60, 140, 280, 504, 因子枚举] |
| 6 | AI构造了小范围陷阱数链但未推广到大数情况 | 陷阱数链覆盖[8,1990]，处理n≥1992用强归纳，提示11的幂次乘181 | 0.4 | 推进 | false | {discrete_combinatorial, logical_deduction, method_translation} | [强归纳, 11^r·181, 区间覆盖, 大数推广] |
| 7 | AI需要验证完整分类和确定性 | 验证完整分类：n<8时A不赢、B在{2,3,4,5}赢、{6,7}平局、确定性 | 0.6 | 能量传递引导 | false | {discrete_combinatorial, case_by_case, method_translation} | [escape引理, 反陷阱, 确定性, 完整分类] |

**全局tell_hint_pairs详情**：

1. path_feature型：
   - scope: 完整陷阱数链60→140→280→504→1990及大数归纳11^(r+1)·181的构造路径
   - observation_point: null
   - tell: 陷阱数链的完整构造需要从[8,11]开始逐级向上覆盖，每级陷阱数的因子要么非素数幂要么落入上一级覆盖范围，最终用11^r·181做万能归纳
   - hint: 从最小范围[8,11]开始构造陷阱数，逐级扩大覆盖范围，每级验证因子的素数幂性质，最后用11的幂次乘181实现大数归纳
   - hint_level: 0.3
   - generalizability: medium——陷阱数链的构造方法可泛化到类似博弈问题中"寻找安全位置链"的模式，但具体数值60/140/280/504与1990这个终止值绑定
   - why_not_visible_locally: 在任何单轮QA中只能看到陷阱数链的一个环节（如R5只看到60），无法看到完整链60→140→280→504→1990→11^r·181的递进结构和各级之间的因子覆盖关系。完整路径特征需要从全局视角才能识别——每一级陷阱数的因子要么是非素数幂（B不能赢）要么落入上一级的覆盖范围，这种"链式覆盖"结构是路径特征而非局部特征。
   - tell_topology: {discrete_combinatorial, algebraic_identity, structural_transformation}
   - tell_small_concepts: [陷阱数链, 60, 140, 280, 504, 1990, 11^r·181, 因子覆盖, 链式结构]

2. implicit型：
   - scope: 博弈论→数论的结构翻译贯穿整个解答
   - observation_point: Q4
   - tell: "B能直接获胜当且仅当前数是素数幂"这个翻译将整个博弈问题从策略空间分析转化为数论性质验证
   - hint: 识别B的获胜条件与素数幂的等价关系，将博弈策略问题翻译为"寻找满足特定数论性质的整数"问题
   - hint_level: 0.4
   - generalizability: high——"将博弈获胜条件翻译为代数/数论性质"的模式可泛化到大量博弈论问题
   - why_not_visible_locally: 在R1-R3的局部视角中，AI看到的是博弈规则和逆向归纳，无法发现B的获胜条件（选1）与素数幂判定的等价关系。这个蕴含信息需要从B的走法定义（m/m'=p^r）中推导出"B选1意味着m=p^r即m是素数幂"，这是一个跨步骤的蕴含——需要同时理解B的走法规则和素数幂定义才能发现。在局部步骤中只看到走法规则或只看到素数幂定义都无法建立联系。
   - tell_topology: {discrete_combinatorial, logical_deduction, method_translation}
   - tell_small_concepts: [素数幂等价, B获胜条件, 结构翻译, p^r, 因子分解]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: bare AI会尝试逆向归纳从1990出发，覆盖[45,1990]后卡住。不会发现"B选1当且仅当素数幂"的关键翻译，因此无法构造陷阱数链。对小n可能尝试穷举但无法系统化。最终可能给出部分正确答案（A赢当n≥45）但无法完整分类n∈[2,44]和n≥1992的情况。
- suitable_for_poc: [POC-VMS-hint-injection（hint端验证：注入"素数幂等价"hint后AI能否构造陷阱数）, POC-VMS-tell-detection（tell端验证：从AI的thinking中检测到"未识别素数幂等价"的分叉信号）, POC-VMS-level-discrimination（区分能力强：bare AI fail vs hint后可能pass）]
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
2. 更新`problem_extraction_progress`集合中`_key="329132"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1990p5"
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
    '_key': '329132',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1990p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1990p5')
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
- problem_id: compfiles_imo1990p5
- solution_method_type: structural_translation_with_trap_construction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否——discrete_combinatorial/case_by_case/method_translation三个维度足够，粒度与已有值一致
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
