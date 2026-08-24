# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1984p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1984P6.lean
- **来源**: IMO 1984 P6
- **ArangoDB progress记录_key**: 329108（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1984P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let a, b, c, d be odd integers such that 0 < a < b < c < d and ad = bc. Prove that if a + d = 2^k and b + c = 2^m for some integers k and m, then a = 1.
- 解答核心思路（1-2句话）：将c=2^m-b和d=2^k-a代入ad=bc得到关键恒等式b²-a²=2^m·b-2^k·a，利用m<k提取2^m|(b-a)(b+a)，再由奇数性质gcd(b-a,b+a)=2迫使2^(m-1)|b+a，结合大小排除得b+a=2^(m-1)，回代得a|2^(2(m-1))，奇数a整除2的幂故a=1。
- 解答关键步骤列表：
  1. 证明m≥3（因b+c≥8，b,c为奇数且b<c）
  2. 证明m<k（因ad=bc且{a,d}比{b,c}更分散，故a+d>b+c）
  3. 代入c=2^m-b, d=2^k-a到ad=bc，得关键恒等式b²-a²=2^m·b-2^k·a
  4. 利用m<k，从恒等式提取2^m|(b-a)(b+a)
  5. 引理：对奇数x<y，若2^m|(y-x)(y+x)则2^(m-1)|y-x或2^(m-1)|y+x（因gcd(y-x,y+x)=2）
  6. 排除2^(m-1)|b-a（因0<b-a<2^(m-1)）
  7. 得b+a=2^(m-1)（2^(m-1)的正倍数且<2^m，故倍数q=1）
  8. 回代b=2^(m-1)-a到恒等式，得a·2^k=2^(2(m-1))
  9. a为奇数且整除2的幂，故a=1

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
| 1 | 纯元认知观察 | 0.7 | 观察这道题的结构——已知条件和待证结论分别是什么？ad=bc这个乘法关系和a+d=2^k、b+c=2^m这两个加法关系之间有什么结构性联系？ | a,b,c,d为奇数，0<a<b<c<d，ad=bc（乘法约束），a+d=2^k且b+c=2^m（加法约束为2的幂），需证a=1。乘法约束ad=bc和加法约束之间需要找到桥梁——可能通过消元将乘法关系转化为加法关系。 |
| 2 | 自由列举 | 0.6 | 列出所有可能的方向来利用这些条件——尤其是ad=bc和两个2的幂之和条件如何结合？ | 方向包括：①直接代入消元（用c=2^m-b, d=2^k-a代入ad=bc）；②研究{a,d}和{b,c}作为乘积相同但和不同的数对的关系；③利用奇数性质分析2的幂整除性；④尝试具体数值建立直觉；⑤利用差平方分解b²-a²=(b-a)(b+a)。 |
| 3 | 小尝试 | 0.3 | 尝试用具体数值来理解结构——a=1时能否找到满足条件的b,c,d？a=3时呢？ | a=1,b=3,c=5,d=15：1+15=16=2^4, 3+5=8=2^3, 1×15=3×5=15。成立。a=3时需要3d=bc, 3+d=2^k, b+c=2^m，很难找到满足条件的例子，暗示a=1可能是唯一可能。 |
| 4 | 思维操作引导 | 0.2 | 从ad=bc出发，用b+c=2^m和a+d=2^k消元——把c=2^m-b和d=2^k-a代入ad=bc，你能得到什么恒等式？ | a(2^k-a)=b(2^m-b)，展开得2^k·a-a²=2^m·b-b²，即b²-a²=2^m·b-2^k·a。左边可分解为(b-a)(b+a)。 |
| 5 | 思维操作引导 | 0.3 | 你得到了b²-a²=2^m·b-2^k·a，即(b-a)(b+a)=2^m·b-2^k·a。先证明m<k（提示：ad=bc且{a,d}比{b,c}更分散），然后利用m<k从右边提取2^m。 | 因ad=bc且a<b<c<d，{a,d}比{b,c}更分散，故a+d>b+c，即2^k>2^m，所以m<k。于是2^k=2^m·2^(k-m)，右边=2^m(b-2^(k-m)·a)，故2^m|(b-a)(b+a)。 |
| 6 | 思维操作引导 | 0.4 | 现在知道2^m|(b-a)(b+a)，且a,b都是奇数。分析gcd(b-a,b+a)——两个因子共享多少个2？由此2^m的2-adic valuation如何分配？ | a,b奇数⇒b-a和b+a都是偶数，且gcd(b-a,b+a)=2（因为gcd(b-a,b+a)|2a且|2b，而a,b奇数故gcd含恰好一个2）。所以2^m=(b-a)(b+a)中的2的幂几乎全部落在一个因子中：2^(m-1)|b-a或2^(m-1)|b+a。 |
| 7 | 能量传递引导 | 0.3 | 现在排除2^(m-1)|b-a（因0<b-a<2^(m-1)），得b+a=2^(m-1)。代入回关键恒等式，你能推出a=1吗？ | b=2^(m-1)-a代入b²-a²=2^m·b-2^k·a，化简得a·2^k=2^(2(m-1))。a为奇数且整除2^(2(m-1))，而奇数与2互质，故a=1。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 3
- knowledge_rounds（思维操作引导的轮数）: 3
- level_sum: 2.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R4（关键恒等式的代入消元）和R6（gcd(b-a,b+a)=2的性质）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R5（从恒等式到整除性的转化需要先建立m<k）

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
- problem_type: characterization
- structure_features: 四个奇数满足乘法约束ad=bc和加法约束（和为2的幂），需证最小值a被唯一确定为1。核心结构是乘法约束与加法约束的桥接——通过代入消元将乘法关系转化为差平方恒等式，再利用2-adic valuation分配性质。
- key_objects: ["奇数a,b,c,d", "2的幂和a+d=2^k, b+c=2^m", "差平方b²-a²=(b-a)(b+a)", "gcd(b-a,b+a)=2", "2-adic valuation分配"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["algebraic_substitution（代入消元）", "divisibility_analysis（整除性分析）", "gcd_argument（gcd论证）", "size_estimation_exclusion（大小排除）", "parity_analysis（奇偶性分析）", "back_substitution（回代求解）"]
- primary_pattern: divisibility_analysis
- knowledge_required: ["奇数的算术性质", "gcd(y-x,y+x)=2对奇数x,y", "2的幂整除性", "互质论证（coprime argument）", "差平方分解", "AM-GM类型的不等式直觉（更分散的数对和更大）"]
- key_insight: 将c=2^m-b和d=2^k-a代入ad=bc得到差平方恒等式b²-a²=2^m·b-2^k·a，利用gcd(b-a,b+a)=2迫使2^(m-1)|b+a，大小排除后b+a=2^(m-1)，回代得奇数a整除2的幂故a=1

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 乘法约束语言（ad=bc，四个变量的乘积关系）
- translation_to: 加法/差平方整除性语言（b²-a²=2^m·b-2^k·a，2-adic valuation分配）
- translation_type: structural_transformation（通过代入消元将乘法约束结构性地转化为差平方恒等式，再转入整除性分析框架）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "case_by_case", gap_type: "structural_transformation"}
- tell_small_concepts: ["差平方分解", "代入消元", "2-adic valuation分配", "gcd(b-a,b+a)=2", "大小排除", "奇数整除2的幂", "m<k不等式"]
- expected_ai_method: bare AI预期会尝试具体数值枚举（case_by_case）或直接代数变形，但看不到将乘法约束通过代入消元转化为差平方恒等式这一关键结构变换，也不熟悉gcd(b-a,b+a)=2的2-adic valuation分配论证。
- correct_method: 代入消元得到差平方恒等式→利用m<k提取整除性→gcd=2论证分配2-adic valuation→大小排除确定b+a=2^(m-1)→回代得a|2的幂→奇数故a=1

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ → 可以。characterization（problem_type）、case_by_case（ai_method_type）、structural_transformation（gap_type）均已存在且粒度合适。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ → 一致。三个值都是中等偏抽象粒度。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ → 足够。这道题的tell特征（乘法→加法结构变换+2-adic valuation分配）可以通过现有三维区分。
- [x] 如果发现拓扑分类需要进化，在此写出建议： → 无需进化。

**拓扑进化建议**（如有）：无。当前拓扑分类体系足够覆盖此题。

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

| R | tell | hint | hint_level | situation_type | is_kb | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到四个变量有混合的乘法和加法约束，但未识别乘法与加法之间的结构性桥梁 | 观察结构：ad=bc是乘法约束，a+d和b+c是加法约束为2的幂——如何桥接？ | 0.7 | 纯元认知观察 | false | {characterization, direct_calculation, method_problem_mismatch} | ["乘法约束", "加法约束", "2的幂"] |
| 2 | AI列出方向但可能未看到代入消元这一关键桥接操作 | 列出所有结合ad=bc与和条件的方式——尤其是代入消元 | 0.6 | 自由列举 | false | {characterization, enumeration_brute_force, search_space_estimation} | ["代入消元", "差平方分解", "数对分散性"] |
| 3 | AI尝试具体数值，看到a=1可行但无法推广到一般证明 | 用具体数值建立直觉——a=1和a=3分别会发生什么？ | 0.3 | 小尝试 | false | {characterization, case_by_case, method_problem_mismatch} | ["具体数值", "模式识别", "唯一性暗示"] |
| 4 | AI未看到将c=2^m-b, d=2^k-a代入ad=bc可得到差平方恒等式 | 从ad=bc出发，用b+c=2^m和a+d=2^k消元——代入后得到什么恒等式？ | 0.2 | 思维操作引导 | true | {characterization, direct_manipulation, structural_transformation} | ["差平方", "代入消元", "关键恒等式"] |
| 5 | AI有恒等式但未看到m<k是提取整除性的前提 | 先证m<k（{a,d}比{b,c}更分散故a+d>b+c），再利用m<k从右边提取2^m | 0.3 | 思维操作引导 | false | {characterization, algebraic_identity, method_translation} | ["m<k不等式", "2的幂整除性", "提取公因子"] |
| 6 | AI知道2^m|(b-a)(b+a)但不熟悉gcd(b-a,b+a)=2对奇数的性质 | 对奇数a,b：gcd(b-a,b+a)=2，故2-adic valuation几乎全部落入一个因子——2^(m-1)|b-a或2^(m-1)|b+a | 0.4 | 思维操作引导 | true | {characterization, direct_calculation, knowledge_gap} | ["gcd(b-a,b+a)=2", "2-adic valuation分配", "互质论证"] |
| 7 | AI有b+a=2^(m-1)但未将其回代到恒等式得到a=1 | 排除2^(m-1)|b-a后得b+a=2^(m-1)，回代得a·2^k=2^(2(m-1))，奇数a整除2的幂故a=1 | 0.3 | 能量传递引导 | false | {characterization, logical_deduction, method_translation} | ["回代求解", "奇数整除2的幂", "与2互质"] |

**全局tell_hint_pairs详情**：

1. path_feature型：
- scope: "完整解答路径：从约束到结论"
- observation_point: null
- tell: 解答需要一条特定路径：代入消元→差平方恒等式→m<k提取整除性→gcd=2分配2-adic valuation→大小排除→回代→a|2^n→a=1
- hint: 关键路径是：代数代入创造差平方恒等式，结合奇数的gcd性质迫使2-adic valuation落入一个因子，大小约束钉住精确值，回代后奇数整除2的幂得a=1
- hint_level: 0.8
- generalizability: "high — 乘法约束通过代入转化为差平方恒等式、再用gcd性质分配2-adic valuation的模式，可推广到许多混合加法/乘法约束的数论问题"
- why_not_visible_locally: 每一步单独看都是标准代数操作，但完整路径——尤其是从恒等式到gcd论证到大小排除到回代的转化链——只有作为完整链条才可见。没有任何单步揭示代入会导致整除性论证会导致大小排除会导致回代得a=1。
- tell_topology: {characterization, direct_manipulation, structural_transformation}
- tell_small_concepts: ["差平方恒等式", "2-adic valuation分配", "gcd=2", "大小排除", "回代", "奇数整除2的幂"]

2. implicit型：
- scope: "m<k与整除性论证之间的依赖关系"
- observation_point: "R5"
- tell: m<k不仅是大小比较，而是整个整除性链条的使能条件——没有m<k，2^m无法从关键恒等式中提取出来
- hint: 先建立m<k（通过分散性论证），再用它提取2^m——步骤顺序很重要
- hint_level: 0.6
- generalizability: "medium — 先建立指数不等式再用于整除性提取的模式，出现在涉及2的幂的数论问题中"
- why_not_visible_locally: 在R5中，整除性步骤看起来只需要恒等式，但它隐含依赖m<k——而m<k是在R4的上下文中建立的。这个依赖在使用点不可见。
- tell_topology: {characterization, algebraic_identity, method_translation}
- tell_small_concepts: ["指数比较m<k", "整除性提取", "步骤顺序依赖"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI很可能在写下约束条件后卡住——可能尝试具体数值枚举或直接代数变形，但看不到将c=2^m-b和d=2^k-a代入ad=bc得到差平方恒等式这一关键结构变换。即使偶然发现恒等式，也不熟悉gcd(b-a,b+a)=2的2-adic valuation分配论证，无法从2^m|(b-a)(b+a)推进到2^(m-1)|b+a。此外可能忽略先证明m<k这一前置步骤。
- suitable_for_poc: ["tell_hint_injection（测试代入消元hint能否引导AI发现关键恒等式）", "knowledge_gap_detection（测试gcd(b-a,b+a)=2知识缺口识别）", "structural_transformation_recognition（测试乘法→加法结构变换的tell识别）"]
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
2. 更新`problem_extraction_progress`集合中`_key="329108"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1984p6"
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
    '_key': '329108',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1984p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1984p6')
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
- problem_id: compfiles_imo1984p6
- solution_method_type: algebraic_substitution_with_divisibility_argument
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否。当前三维拓扑（characterization / case_by_case / structural_transformation）足够覆盖此题。
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
