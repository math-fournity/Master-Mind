# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2020p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2020P5.lean
- **来源**: USA 2020 P5
- **ArangoDB progress记录_key**: 329487（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2020P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：平面上有限点集S称为"overdetermined"（超定的），若|S|≥2且存在一个非零实系数多项式P(t)，次数≤|S|-2，使得对S中每个点(x,y)都有P(x)=y。对每个整数n≥2，求最大整数k（关于n的函数），使得存在一个n个不同点的集合，它本身不是overdetermined的，但有k个overdetermined子集。
- 解答核心思路（1-2句话）：定义"flooded"=不是overdetermined的。关键引理：一个flooded的m点集最多有一个overdetermined的(m-1)-子集（因为两个不同的overdetermined删除集会给出两个次数≤m-3的插值多项式在m-2个点上相等，故相等，从而整个集合overdetermined——矛盾）。用flooded m-子集和flooded (m+1)-子集之间的关联做double counting，归纳得出flooded n-集至少有C(n-1,m-1)个flooded m-子集，因此overdetermined子集数≤2^(n-1)-n。构造{(1,1),(2,2),(3,2),...,(n,2)}达到此界。
- 解答关键步骤列表：
  1. 定义flooded = not overdetermined
  2. 关键引理：flooded m点集最多1个overdetermined (m-1)-子集（多项式插值唯一性）
  3. Double counting：flooded m-子集与flooded (m+1)-子集的关联不等式
  4. 归纳：flooded n-集至少有C(n-1,m-1)个flooded m-子集（对每个2≤m≤n）
  5. 上界：overdetermined子集数 ≤ Σ_{m=2}^{n} C(n-1,m) = 2^(n-1)-n
  6. 构造达到界：{(1,1),(2,2),...,(n,2)}，overdetermined子集恰为tail的≥2元子集，共2^(n-1)-n个

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：什么是"overdetermined"？我们在优化什么？已知条件和目标分别是什么？ | overdetermined意味着一个点集可以被一个次数≤|S|-2的多项式拟合（比正常插值次数|S|-1更低）。我们需要找一个n点集，本身不是overdetermined的，但最大化其overdetermined子集数k。这是一个极值组合问题。 |
| 2 | 自由列举 | 0.7 | 对于这个极值组合问题，列出你能想到的所有可能方向和策略。 | 直接枚举overdetermined子集并计数；构造特殊点集计算；用互补计数（数不是overdetermined的子集）；用归纳法；用double counting；用多项式插值理论分析结构。 |
| 3 | 小尝试 | 0.5 | 试着直接计数：一个n点集有多少个子集？其中多少可能是overdetermined的？能直接给出上界吗？ | n点集有2^n个子集，其中≥2元的有2^n-n-1个。直接计数overdetermined子集很难，因为依赖于点集的具体几何结构。需要找到结构性的约束。 |
| 4 | 思维操作引导 | 0.4 | 定义"flooded"=不是overdetermined。考虑一个flooded的m点集（m≥3），它的(m-1)-子集中最多有多少个是overdetermined的？用多项式插值唯一性来分析。 | 最多1个。如果有两个不同的overdetermined (m-1)-子集U1=S\{p1}和U2=S\{p2}，它们对应次数≤m-3的多项式f,g。f和g在U1∩U2的m-2个点上相等，而m-3 < m-2，由插值唯一性f=g。但这样f就通过了S的所有点，说明S本身overdetermined——矛盾。 |
| 5 | 思维操作引导 | 0.3 | 利用上面的关键引理，建立flooded m-子集和flooded (m+1)-子集之间的double counting不等式。 | 设F_m是flooded m-子集数。每个flooded (m+1)-集至少有m个flooded m-子集（因为最多1个overdetermined的），每个flooded m-子集最多属于(n-m)个flooded (m+1)-子集。所以m·F_{m+1} ≤ (n-m)·F_m。 |
| 6 | 推进 | 0.4 | 用这个递推不等式和归纳法，推导出flooded n-集的flooded m-子集数的下界，然后求出overdetermined子集数的上界。 | 归纳得F_m ≥ C(n-1,m-1)。overdetermined m-子集数 = C(n,m) - F_m ≤ C(n,m) - C(n-1,m-1) = C(n-1,m)。求和Σ_{m=2}^{n} C(n-1,m) = 2^{n-1}-n。所以k ≤ 2^{n-1}-n。 |
| 7 | 能量传递引导 | 0.6 | 构造一个达到上界的例子。考虑点集{(1,1),(2,2),(3,2),...,(n,2)}，验证它不是overdetermined的，且恰有2^{n-1}-n个overdetermined子集。 | 这个集合不是overdetermined的：任何通过所有点的多项式P满足P(i)=2对i=2,...,n（n-1个点），若deg P ≤ n-2则P-2有n-1个根但次数≤n-2，矛盾（除非P≡2，但P(1)=1≠2）。overdetermined子集恰为tail {(2,2),...,(n,2)}的≥2元子集（常数多项式P≡2通过它们，次数0≤|S|-2），共2^{n-1}-n个。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.7
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: discrete_combinatorial
- structure_features: 极值组合优化问题，涉及点集的多项式拟合性质（overdetermined定义），需要在"本身不overdetermined"约束下最大化overdetermined子集数。核心结构是flooded/overdetermined的互补关系和子集层次结构。
- key_objects: 有限点集S、实系数多项式P(t)、overdetermined子集、flooded子集（非overdetermined）、二项式系数C(n-1,m)、double counting关联矩阵

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["complementary_counting", "double_counting", "polynomial_interpolation_uniqueness", "structural_induction", "extremal_construction"]
- primary_pattern: double_counting
- knowledge_required: ["多项式插值唯一性（次数≤|T|-1的多项式在|T|个点上唯一确定）", "double counting / 关联计数技巧", "二项式系数恒等式（Pascal恒等式、求和公式）", "极值构造方法"]
- key_insight: 一个flooded的m点集最多有1个overdetermined (m-1)-子集——因为两个不同的overdetermined删除集会给出两个次数≤m-3的多项式在m-2个点上相等，由插值唯一性它们相等，从而整个集合overdetermined，矛盾。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 直接枚举overdetermined子集计数（brute force enumeration）
- translation_to: 互补计数（数flooded子集）+ double counting关联不等式 + 归纳 + 极值构造
- translation_type: method_translation（从直接枚举翻译到结构性互补计数+double counting）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "structural_transformation"}
- tell_small_concepts: ["overdetermined", "flooded", "polynomial interpolation uniqueness", "double counting", "complementary counting", "extremal construction", "binomial identity", "Pascal identity"]
- expected_ai_method: enumeration_brute_force（bare AI会尝试直接枚举/计数overdetermined子集，但无法给出紧的上界）
- correct_method: 互补计数flooded子集 + 多项式插值唯一性引理 + double counting关联不等式 + 归纳 + 极值构造

### 6b. 反思拓扑分类

- [x] 当前拓扑分类是否够用——这道题的problem_type(discrete_combinatorial)/ai_method_type(enumeration_brute_force)/gap_type(structural_transformation)都能归入已有的拓扑类别，够用。
- [x] 粒度是否一致——标注的值和已有值的粒度统一。
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。

**拓扑进化建议**（如有）：无。已有拓扑分类体系可以很好地容纳这道题。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到极值优化问题但未识别互补结构——overdetermined与flooded的互补关系 | 描述overdetermined的结构含义，思考"不overdetermined"意味着什么 | 0.8 | 纯元认知观察 | false | {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "method_problem_mismatch"} | ["overdetermined", "polynomial degree bound", "extremal optimization"] |
| 2 | AI列出方向但遗漏互补计数和double counting | 列出所有方向，特别注意互补计数（数不是overdetermined的子集） | 0.7 | 自由列举 | false | {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "search_space_estimation"} | ["complementary counting", "approach enumeration", "double counting"] |
| 3 | AI尝试直接计数overdetermined子集但无法给出紧的上界 | 试直接计数——发现2^n个子集中难以区分哪些overdetermined，需要结构性约束 | 0.5 | 小尝试 | false | {problem_type: "discrete_combinatorial", ai_method_type: "direct_calculation", gap_type: "method_problem_mismatch"} | ["subset counting", "2^n subsets", "structural constraint needed"] |
| 4 | AI未发现关键引理：flooded m点集最多1个overdetermined (m-1)-子集 | 定义flooded=非overdetermined，用多项式插值唯一性分析flooded集的子集结构 | 0.4 | 思维操作引导 | true | {problem_type: "discrete_combinatorial", ai_method_type: "logical_deduction", gap_type: "knowledge_gap"} | ["flooded", "polynomial interpolation uniqueness", "at most one overdetermined deletion"] |
| 5 | AI有引理但不知如何用于计数——未想到double counting | 用flooded m-子集和flooded (m+1)-子集的关联建立double counting不等式 | 0.3 | 思维操作引导 | false | {problem_type: "discrete_combinatorial", ai_method_type: "logical_deduction", gap_type: "method_translation"} | ["double counting", "incidence relation", "recursive inequality"] |
| 6 | AI有递推不等式但未归纳出闭式下界 | 用归纳法和递推不等式推导F_m≥C(n-1,m-1)，求和得overdetermined上界2^{n-1}-n | 0.4 | 推进 | false | {problem_type: "discrete_combinatorial", ai_method_type: "logical_deduction", gap_type: "structural_transformation"} | ["induction", "binomial coefficient", "Pascal identity", "sum formula"] |
| 7 | AI有上界但需构造达到界的例子 | 构造{(1,1),(2,2),...,(n,2)}验证非overdetermined且恰有2^{n-1}-n个overdetermined子集 | 0.6 | 能量传递引导 | false | {problem_type: "discrete_combinatorial", ai_method_type: "direct_manipulation", gap_type: "structural_transformation"} | ["extremal construction", "constant polynomial", "tail subset", "tightness"] |

**全局tell_hint_pairs**：

1. path_feature型：
- scope_type: "path_feature"
- scope: "完整证明路径：互补计数→关键引理→double counting→归纳→极值构造"
- observation_point: null
- tell: "整道题的解答需要从直接枚举翻译到互补计数+double counting的结构性方法，这个路径特征在任何单一步骤中都看不到"
- hint: "不要直接数overdetermined子集——定义flooded=非overdetermined，用插值唯一性建立结构引理，再用double counting和归纳得到紧的上界，最后构造极值例子"
- hint_level: 0.7
- generalizability: "high — 互补计数+double counting是极值组合问题的通用范式，可泛化到任何'在约束下最大化某类子集数'的问题"
- why_not_visible_locally: "完整路径特征——从直接枚举到互补计数再到double counting的方法翻译，以及关键引理→递推→归纳→构造的完整链条——在任何单一步骤中只能看到局部片段，无法看到全局的方法选择和步骤间的因果依赖"
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "structural_transformation"}
- tell_small_concepts: ["complementary counting", "double counting", "polynomial interpolation uniqueness", "structural induction", "extremal construction"]

2. implicit型：
- scope_type: "implicit"
- scope: "多项式插值唯一性在overdetermined定义中的蕴含信息"
- observation_point: "R4"
- tell: "overdetermined的定义中隐含了多项式插值唯一性——次数≤|S|-2的多项式在|S|个点上被唯一确定（如果存在的话），这个蕴含信息在定义本身中不可见，需要通过分析flooded集的子集结构才能发现"
- hint: "overdetermined意味着多项式次数比正常插值低1次——利用这个'低1次'的结构：两个低次多项式在足够多点上相等则必相等，这就是插值唯一性"
- hint_level: 0.4
- generalizability: "high — 多项式插值唯一性是代数几何/组合中的通用工具，可泛化到任何涉及多项式拟合与点集关系的问题"
- why_not_visible_locally: "overdetermined的定义只说'存在一个低次多项式通过所有点'，但'低1次'这个条件隐含的插值唯一性约束——两个这样的多项式在|S|-1个点上相等则必相等——在定义的局部表述中完全不可见，需要跨步骤分析flooded集的子集关系才能提取"
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "logical_deduction", gap_type: "knowledge_gap"}
- tell_small_concepts: ["polynomial interpolation uniqueness", "degree bound", "flooded subset structure", "at most one overdetermined deletion"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "bare AI会尝试直接枚举overdetermined子集或对小n做归纳，但无法发现'flooded集最多1个overdetermined (m-1)-子集'这个关键引理，也无法想到互补计数+double counting的方法翻译，因此无法给出紧的上界2^{n-1}-n。AI可能给出一些松的上界如2^n-n-1，但无法证明最优性。"
- suitable_for_poc: ["POC-VMS-hint-injection（hint端验证：注入互补计数+double counting方向后AI能否完成）", "POC-VMS-tell-detection（tell端验证：从AI thinking中检测到直接枚举的分叉信号）", "POC-VMS-level-discrimination（区分能力强弱AI：能想到double counting的AI vs 只会直接枚举的AI）"]
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
- [x] answer（k = 2^(n-1) - n）
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

**将完整JSON写入工作目录的 `profile.json` 文件** — 已完成

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证详情: 7 local pairs, 2 global pairs, answer="k = 2^(n-1) - n", knowledge_bottleneck="R4", thinking_bottleneck="R5"

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_usa2020p5
- solution_method_type: double_counting
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类体系（discrete_combinatorial / enumeration_brute_force / structural_transformation等）可以很好地容纳这道题
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
