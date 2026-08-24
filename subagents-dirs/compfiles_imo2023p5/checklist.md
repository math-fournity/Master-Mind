# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2023p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2023P5.lean
- **来源**: IMO 2023 P5
- **ArangoDB progress记录_key**: 329272（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2023P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设n为正整数。"日本三角形"是1+2+...+n个点排成等边三角形的点集，每行恰有一个红点。"忍者路径"是从顶行开始，每步走到正下方相邻点之一，直到底行的n个点的序列。求最大的k，使得对每个日本三角形，都存在一条至少包含k个红点的忍者路径。
- 解答核心思路（1-2句话）：答案为k=⌈log₂(n+1)⌉。下界通过定义DP函数f(i,p)（到第i行位置p的最大红点数），证明行和S(i)满足递推S(i+1)≥S(i)+⌈S(i)/i⌉+1，归纳得S(i)≥log₂(i)·i+2·(i-2^log₂(i))+1，再由鸽巢原理取最大值得到路径。上界通过构造极反例三角形（第i行红点在位置2^⌈log₂(i+1)⌉-1-i），证明任意路径至多命中⌈log₂(n+1)⌉个红点。
- 解答关键步骤列表：
  1. 定义f(j,i,p)：从顶行到第i行位置p的忍者路径的最大红点数（DP递推）
  2. 证明exists_good_path：对每个有效位置p存在路径达到f(j,i,p)个红点
  3. 证明关键递推S_rec：S(i+1) ≥ S(i) + ⌈S(i)/i⌉ + 1，其中S(i)=Σ f(j,i,p)
  4. 归纳证明S_lower：S(i) ≥ log₂(i)·i + 2·(i-2^log₂(i)) + 1
  5. 下界lower_bound：由S(n)/n的鸽巢论证，存在位置m使f(j,n,m)≥⌈log₂(n+1)⌉，再由exists_good_path得到路径
  6. 构造极反例extremal：第i行红点位置为2^⌈log₂(i+1)⌉-1-i
  7. 上界upper_bound：证明映射k→⌈log₂(k+1)⌉在路径命中红点的行集合上单射，故红点数≤⌈log₂(n+1)⌉

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
| 1 | 纯元认知观察 | 0.3 | 这道题的结构是什么？已知条件是什么，要求什么？特别注意"对每个日本三角形都存在一条路径"这个全称量词的含义。 | 题目要求的是一个对所有染色方案都成立的最大k。结构上是一个三角点阵，每行一个红点，路径从顶到底每步向左下或右下走一格。这是一个最坏情况下的保证值问题——需要在所有可能的染色中找到最小值，再取最大。 |
| 2 | 自由列举 | 0.5 | 对于这类"最坏情况下保证至少k个"的组合极值问题，有哪些可能的攻击方向？列出你能想到的所有方法。 | 可能方向：(1)直接构造路径贪心选择红点；(2)用概率/计数方法证明平均路径命中红点数；(3)定义DP函数记录到每个位置的最大红点数；(4)构造极反例给出上界；(5)用归纳法；(6)用鸽巢原理。 |
| 3 | 小尝试 | 0.4 | 试试直接贪心：从顶行开始，每步选择能命中红点的方向。这个策略能保证多少个红点？ | 贪心策略的问题在于它是短视的——选择当前命中红点的方向可能错过后面更多的红点。而且红点位置是任意的，贪心无法保证对所有染色都有效。最坏情况下贪心可能只命中1个红点（如果红点位置总是让贪心选错）。 |
| 4 | 思维操作引导 | 0.6 | 定义DP函数f(i,p)为从顶行到第i行位置p的忍者路径能命中的最大红点数。写出f的递推关系，然后考虑行和S(i)=Σ_p f(i,p)的性质。 | f(i+1,p) = max(f(i,p-1), f(i,p)) + [redPos(i+1)=p]。行和S(i+1) = Σ max(f(i,p-1),f(i,p)) + 1（因为每行恰一个红点）。关键观察：max(f(i,p-1),f(i,p)) ≥ f(i,p)，且max ≥ f(i,p-1)，所以S(i+1) ≥ S(i) + 某个额外项。 |
| 5 | 推进 | 0.6 | 继续分析S(i+1)与S(i)的关系。具体地，设m是第i行中f值最大的位置，能否得到S(i+1) ≥ S(i) + ⌈S(i)/i⌉ + 1？ | 是的。将求和按m的位置分成两部分：前半每个max ≥ f(i,p)贡献S(i)的前半部分，后半每个max ≥ f(i,p-1)贡献S(i)的后半部分。加上红点的+1。而⌈S(i)/i⌉ ≤ f(i,m)（因为f(i,m)是最大值，S(i) ≤ i·f(i,m)），所以S(i+1) ≥ S(i) + ⌈S(i)/i⌉ + 1。 |
| 6 | 思维操作引导 | 0.7 | 现在你有了递推S(i+1) ≥ S(i) + ⌈S(i)/i⌉ + 1。用归纳法证明S(i) ≥ log₂(i)·i + 2·(i - 2^log₂(i)) + 1。然后如何从S(n)得到下界k？ | 归纳：base case i=1时S(1)=1=f(1,0)，成立。归纳步：设i=2^c+r, r<2^c，则⌈S(i)/i⌉ ≥ c+1（由归纳假设），代入递推得S(i+1) ≥ (c·i+2r+1) + (c+1) + 1。分两种情况（log₂(i+1)=c或c+1）验证。最后由S(n) ≤ n·max_p f(n,p)，得max_p f(n,p) ≥ S(n)/n ≥ ⌈log₂(n+1)⌉，由exists_good_path存在路径达到此值。 |
| 7 | 能量传递引导 | 0.8 | 下界已经完成，现在需要构造极反例给出上界。考虑第i行红点放在位置2^⌈log₂(i+1)⌉-1-i。证明任意路径至多命中⌈log₂(n+1)⌉个红点——关键是映射k→⌈log₂(k+1)⌉在命中红点的行集合上单射。你已经掌握了所有工具，完成最后的上界证明。 | 对极反例，若路径在第a行和第b行都命中红点（a<b），则pathPos单调递增，而redPos(i)=2^⌈log₂(i+1)⌉-1-i。若⌈log₂(a+1)⌉=⌈log₂(b+1)⌉=c，则redPos(a)-redPos(b)=b-a>0但pathPos(b)-pathPos(a)≥0，结合redPos(a)=2^c-1-a和redPos(b)=2^c-1-b，矛盾。故映射单射，红点数≤⌈log₂(n+1)⌉。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1+R2+R5+R7）
- knowledge_rounds（思维操作引导的轮数）: 3（R4+R6+R7部分）
- level_sum: 0.3+0.5+0.4+0.6+0.6+0.7+0.8 = 3.9
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
- problem_type: discrete_combinatorial
- structure_features: 三角点阵上的路径极值问题，每行一个红点的约束，全称量词（对每个染色方案存在路径），需要上下界匹配。核心是对称的DP+鸽巢下界与极反例构造上界。
- key_objects: ["日本三角形（三角点阵染色）", "忍者路径（单调路径）", "DP函数f(i,p)（到位置p的最大红点数）", "行和S(i)（f值的行求和）", "极反例三角形（extremal构造）", "⌈log₂(n+1)⌉（答案）"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["DP递推与行和聚合", "鸽巢原理（从行和到最大值）", "归纳法（递推到显式下界）", "极反例构造（上界）", "单射论证（极反例中红点计数）", "上下界匹配"]
- primary_pattern: DP递推与行和聚合
- knowledge_required: ["动态规划/递推", "鸽巢原理", "数学归纳法", "对数与二进制结构", "单射与计数论证"]
- key_insight: 定义DP函数f(i,p)后不直接分析单个f值，而是聚合为行和S(i)并证明递推S(i+1)≥S(i)+⌈S(i)/i⌉+1，由此归纳出S(i)的对数增长，再用鸽巢原理从行和提取最大值。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 逐位置贪心/局部路径选择
- translation_to: 行和聚合+递推分析+鸽巢提取
- translation_type: structural_transformation（从局部路径视角翻译到全局行和视角，再回到局部最大值）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "direct_calculation", gap_type: "structural_transformation"}
- tell_small_concepts: ["DP函数f(i,p)", "行和S(i)", "鸽巢原理", "递推S(i+1)≥S(i)+⌈S(i)/i⌉+1", "极反例构造", "单射论证", "⌈log₂(n+1)⌉"]
- expected_ai_method: bare AI预期会尝试直接贪心路径选择或逐行分析单个f值，无法看到行和聚合的必要性
- correct_method: 定义DP函数f(i,p)，聚合为行和S(i)，证明递推关系，归纳得到对数下界，鸽巢提取最大值；构造极反例用单射论证给上界

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？——可以。discrete_combinatorial + direct_calculation + structural_transformation 都在已有值中。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？——一致。都是中等抽象级别。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？——足够。这道题的核心gap是从局部视角到全局聚合的结构转换，structural_transformation准确描述。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。

**拓扑进化建议**（如有）：无。现有拓扑分类完全够用。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI未识别全称量词结构——"对每个染色存在路径"是min-max结构 | 观察题目结构，识别全称量词含义 | 0.3 | 纯元认知观察 | false | {discrete_combinatorial, direct_calculation, method_problem_mismatch} | ["全称量词", "min-max结构", "最坏情况保证"] |
| 2 | AI列出方向但未注意到DP+行和聚合这个关键方向 | 列出所有可能攻击方向 | 0.5 | 自由列举 | false | {discrete_combinatorial, enumeration_brute_force, search_space_estimation} | ["贪心", "概率方法", "DP", "极反例", "鸽巢"] |
| 3 | AI尝试贪心但失败——贪心短视无法保证全局最优 | 试贪心策略看能否work | 0.4 | 小尝试 | false | {discrete_combinatorial, direct_calculation, method_problem_mismatch} | ["贪心策略", "短视性", "最坏情况"] |
| 4 | AI未定义DP函数——不知道如何系统记录到每个位置的最大红点数 | 定义f(i,p)并写出递推，考虑行和S(i) | 0.6 | 思维操作引导 | true | {discrete_combinatorial, direct_calculation, knowledge_gap} | ["DP函数f(i,p)", "递推关系", "行和S(i)"] |
| 5 | AI有递推但未发现S(i+1)≥S(i)+⌈S(i)/i⌉+1——需要按最大值位置分割求和 | 用最大值位置m分割求和证明递推 | 0.6 | 推进 | false | {discrete_combinatorial, direct_calculation, structural_transformation} | ["最大值位置m", "求和分割", "⌈S(i)/i⌉", "鸽巢"] |
| 6 | AI有递推但未归纳出显式下界——需要二进制分解i=2^c+r | 用归纳法证明S(i)的对数下界，再鸽巢提取 | 0.7 | 思维操作引导 | true | {discrete_combinatorial, logical_deduction, knowledge_gap} | ["归纳法", "二进制分解", "log₂下界", "鸽巢提取"] |
| 7 | AI有下界但缺上界——未构造极反例 | 构造极反例并用单射论证给上界 | 0.8 | 能量传递引导 | false | {discrete_combinatorial, case_by_case, structural_transformation} | ["极反例构造", "单射论证", "⌈log₂(k+1)⌉", "pathPos单调性"] |

**全局pairs详情**：

1. path_feature型：
   - scope: "完整解题路径从DP定义到行和递推到归纳下界到鸽巢提取到极反例上界"
   - observation_point: null
   - tell: "bare AI会停留在逐位置/逐行的局部视角，看不到'聚合为行和再分析递推'这个全局结构转换"
   - hint: "从局部f值聚合到行和S(i)，证明递推，归纳出对数增长，鸽巢提取——这是完整的结构转换路径"
   - hint_level: 0.7
   - generalizability: "high——'局部到全局聚合再回到局部提取'的模式适用于许多组合极值问题"
   - why_not_visible_locally: "在任意单轮中只能看到当前步骤，无法看到'定义DP→聚合行和→证明递推→归纳→鸽巢'这条完整路径的必要性。局部视角看到的是分散的技巧，看不到它们如何串联成一个完整论证链。"
   - tell_topology: {discrete_combinatorial, direct_calculation, structural_transformation}
   - tell_small_concepts: ["DP函数f(i,p)", "行和S(i)", "递推S(i+1)≥S(i)+⌈S(i)/i⌉+1", "归纳下界", "鸽巢提取", "极反例"]

2. implicit型：
   - scope: "极反例构造中redPos(i)=2^⌈log₂(i+1)⌉-1-i的隐含意义"
   - observation_point: "R7"
   - tell: "极反例的红点位置公式2^⌈log₂(i+1)⌉-1-i隐含了'相同⌈log₂⌉值的行中红点位置严格递减'这一性质，与pathPos单调性矛盾"
   - hint: "注意极反例公式中⌈log₂(i+1)⌉的分层结构——相同层内红点位置随行号递减，而路径位置单调递增，二者矛盾导致单射"
   - hint_level: 0.6
   - generalizability: "medium——'构造中隐含的单调性矛盾'模式适用于需要极反例的组合问题"
   - why_not_visible_locally: "在R7的单步中，AI看到的是极反例公式和单射论证，但公式2^⌈log₂(i+1)⌉-1-i为什么这样设计——其隐含的分层递减结构——在局部步骤中不可见，需要理解整个上界论证的逻辑才能看出这个设计的意图。"
   - tell_topology: {discrete_combinatorial, case_by_case, structural_transformation}
   - tell_small_concepts: ["极反例公式", "⌈log₂(i+1)⌉分层", "红点位置递减", "pathPos单调性", "单射矛盾"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "bare AI会尝试直接贪心路径选择或枚举小情形，无法想到'定义DP函数后聚合为行和S(i)再证明递推'这个关键结构转换。即使定义了DP函数，也很难发现S(i+1)≥S(i)+⌈S(i)/i⌉+1这个递推（需要按最大值位置分割求和的技巧），更难完成归纳证明和极反例构造。"
- suitable_for_poc: ["POC-VMS-hint注入验证（验证行和聚合hint能否引导AI走对方向）", "POC-VMS-tell识别验证（验证能否从AI thinking中读出'停留在局部视角'的tell）", "POC-VMS-结构转换gap验证（验证structural_transformation类gap的hint有效性）"]
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
- [x] answer（"k = ceil(log2(n+1))"）
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

**将完整JSON写入工作目录的 `profile.json` 文件** ✅

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_imo2023p5
- solution_method_type: DP_aggregation_with_extremal_construction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有拓扑分类（discrete_combinatorial + direct_calculation/enumeration_brute_force/logical_deduction/case_by_case + method_problem_mismatch/knowledge_gap/structural_transformation/search_space_estimation）完全够用。
- 是否遇到异常: 无

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
