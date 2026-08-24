# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2017p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2017P5.lean
- **来源**: IMO 2017 P5
- **ArangoDB progress记录_key**: 329242（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2017P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Fix N ≥ 1. N(N+1)名身高互异的球员排成一行。需要从中移除N(N-1)名球员，得到2N名球员的新行，满足以下N个条件：最高的两人之间无人、第三和第四高之间无人、……、最矮的两人之间无人。证明这是可行的。
- 解答核心思路（1-2句话）：将球员按身高分成N组（每组N+1个连续身高），用颜色标记每组。通过归纳法证明一个组合引理：对N种颜色、每种颜色至少出现N+1次的序列，可以选出2N个元素使每种颜色恰好选2个且同色对相邻。颜色分组保证同色相邻即对应身高排名的配对相邻。
- 解答关键步骤列表：
  1. 定义着色 c(i) = ρ(i)/(N+1)，其中ρ(i)是比球员i矮的人数。这给出N种颜色，每种恰好N+1次。
  2. 证明组合引理aux（对N归纳）：扫描序列直到某颜色重复，保留该对（放在新行最左），删除已扫描的和该颜色的所有人，对剩余部分归纳。
  3. 归纳关键：删除后每种剩余颜色仍至少出现N+1次（因为重复对之前每种其他颜色最多出现1次）。
  4. 将引理应用于着色后的球员序列，得到2N个选中的球员，每种颜色恰好2个且相邻。
  5. 验证：同色相邻意味着同身高组的两人相邻，恰好对应"第(2k+1)高和第(2k+2)高之间无人"的条件。

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
| 1 | 纯元认知观察 | 0.3 | 描述这道题的结构：已知什么、要求什么？"两人之间无人"在子序列中意味着什么？ | 给定N(N+1)个身高互异的球员排成一行，要选出2N个保持原顺序，使得按身高排名的第(2k-1)和第2k名在子序列中相邻。本质是在排列中找一个保序子序列，使得特定配对在子序列中相邻。 |
| 2 | 自由列举 | 0.5 | 列出所有可能的方法来构造这样的子序列。哪些方向看起来有希望？ | 可能方向：1)贪心从最高到最低逐对选取；2)动态规划；3)归纳法；4)将问题转化为图论匹配；5)用着色/分组简化约束；6)直接构造。贪心和归纳看起来有希望。 |
| 3 | 小尝试 | 0.4 | 试一试贪心方法：从最高的两人开始，在原行中找到他们，确保他们之间没有其他被选中的人。这个方法可行吗？ | 贪心从最高对开始会遇到困难：选了最高对后，次高对的选择受最高对位置约束，各对之间相互影响。直接贪心难以处理这种交互，因为前面选的对会限制后面选对的空间。 |
| 4 | 思维操作引导 | 0.6 | 考虑将球员按身高分组：把N(N+1)个身高分成N组，每组N+1个连续身高。用颜色标记每组。这样每种颜色恰好出现N+1次。这种着色如何简化原问题？ | 着色后，"第(2k-1)和第2k高相邻"的条件可以转化为"同色对相邻"——因为同组的两人恰好是连续身高。如果能在子序列中保证每种颜色的两人相邻，就自动满足原条件。问题从身高排名约束转化为颜色相邻约束。 |
| 5 | 思维操作引导 | 0.5 | 现在需要证明：对N种颜色、每种至少N+1次的序列，能选2N个使每种颜色恰好2个且同色对相邻。试用归纳法：扫描序列直到某颜色首次重复，保留该对。为什么这样可行？ | 扫描时由鸽巢原理，前N+2个元素中必有同色对（N+1种颜色）。取最早的重复对(s₀,t₀)，t₀之前每种其他颜色最多出现1次。保留(s₀,t₀)放在新行最左，删除t₀之前所有元素和所有同色元素。剩余每种颜色至少N+1-1=N次……不对，需要更仔细的计数。 |
| 6 | 推进 | 0.4 | 验证删除后每种剩余颜色仍至少出现N+1次。关键：t₀之前每种其他颜色最多出现1次（因为t₀是首次重复的位置），所以删除t₀之前的元素最多去掉每种颜色1个。 | t₀是首次出现颜色重复的位置，所以t₀之前所有颜色互不相同（由t₀的最小性）。删除t₀之前的元素后，每种非p颜色最多被删1个，原本N+1个变为至少N个。但归纳需要N+1次……实际上剩余颜色数从N+1种变为N种，所以需要的是N次而非N+1次。对N种颜色需要每种≥N+1次，而剩余每种≥(N+1)-1=N次……需要重新检查归纳参数。 |
| 7 | 能量传递引导 | 0.3 | 梳理完整论证：着色将身高约束转化为颜色约束，引理保证同色相邻，而同色即同身高组即配对相邻。完成证明。 | 完整论证：1)着色c(i)=ρ(i)/(N+1)给出N色各N+1次；2)引理（归纳）保证选出2N个元素每色2个且同色相邻；3)同色=同身高组=第(2k-1)和第2k高，所以同色相邻即满足原条件。引理归纳：N=0平凡；N→N+1时扫描找首次重复对，保留并删除，剩余N色各≥N+1次（因首次重复前每色≤1），归纳得2N个，前置保留对得2(N+1)个。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1+R2+R6+R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4+R5）
- level_sum: 0.3+0.5+0.4+0.6+0.5+0.4+0.3 = 3.0
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
- problem_type: structural_existence
- structure_features: N(N+1)个身高互异的元素排成一行（排列），需要选出2N个保序子序列使得按身高排名的特定配对在子序列中相邻。核心结构是"排列中的保序子序列选择+配对相邻约束"。
- key_objects: 排列（球员行）、身高排名（全序）、保序子序列、配对相邻约束、着色（按身高分组）、鸽巢原理

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["coloring/grouping（着色分组简化约束）", "induction on structure（对颜色数归纳）", "greedy scan（从左扫描找首次重复）", "constraint relaxation via translation（约束松弛翻译）", "pigeonhole principle（鸽巢原理保证重复）"]
- primary_pattern: coloring/grouping（着色分组简化约束）
- knowledge_required: ["鸽巢原理", "数学归纳法", "组合着色", "保序子序列", "排列与排名"]
- key_insight: 将球员按身高分成N组（每组N+1个连续身高）并着色，把"身高排名配对相邻"的刚性约束翻译为"同色对相邻"的柔性约束，再用扫描+归纳证明组合引理。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 身高排名配对相邻约束（rigid height-rank adjacency constraint——直接在排列上要求特定身高对相邻）
- translation_to: 颜色相邻约束（color-adjacency constraint——着色后要求同色对相邻，通过组合引理可归纳证明）
- translation_type: constraint_relaxation_via_coloring（通过着色实现约束松弛翻译——将刚性的全局排名约束松弛为柔性的分组颜色约束）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "case_by_case", gap_type: "structural_transformation"}
- tell_small_concepts: ["height grouping", "coloring by height", "scan from left", "induction on colors", "adjacency in subsequence", "pigeonhole principle", "first repeated color", "constraint relaxation"]
- expected_ai_method: case_by_case（bare AI会尝试直接按身高排名逐对构造子序列，用case analysis处理配对间的交互）
- correct_method: coloring + scan-and-induct（着色将身高约束转化为颜色约束，再用扫描+归纳证明组合引理）

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ → 是。structural_existence（存在性证明）、case_by_case（AI会逐case构造）、structural_transformation（需要着色变换问题结构）都能归入已有类别。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ → 是。三个维度的值都是中等抽象粒度，与已有值一致。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ → 足够。这道题的tell核心是"需要着色变换问题结构"，structural_transformation准确捕捉了这个gap。
- [x] 如果发现拓扑分类需要进化，在此写出建议： → 无需进化。当前分类体系足够。

**拓扑进化建议**（如有）：无。当前拓扑分类体系（structural_existence / case_by_case / structural_transformation）完全适用。

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
| 1 | AI看到选择问题但未识别配对相邻的结构本质 | 描述"两人之间无人"在子序列中意味着什么——本质是保序子序列中特定配对相邻 | 0.3 | 纯元认知观察 | false | {structural_existence, case_by_case, structural_transformation} | ["paired adjacency", "height rank", "subsequence"] |
| 2 | AI列出直接构造方向但未考虑着色/分组 | 考虑分组球员是否能简化相邻约束 | 0.5 | 自由列举 | false | {structural_existence, enumeration_brute_force, search_space_estimation} | ["direct construction", "greedy selection", "height grouping"] |
| 3 | AI尝试贪心从最高到最低但卡在配对交互 | 直接贪心因配对间交互而失败，需要不同抽象层次 | 0.4 | 小尝试 | false | {structural_existence, direct_manipulation, method_problem_mismatch} | ["greedy selection", "pair interaction", "tallest-first"] |
| 4 | AI未考虑按身高着色分组——这是关键知识缺口 | 将N(N+1)球员按身高分N组每组N+1个连续身高并着色，每种颜色恰好N+1次 | 0.6 | 思维操作引导 | true | {structural_existence, case_by_case, knowledge_gap} | ["coloring by height", "N groups of N+1", "pigeonhole"] |
| 5 | AI有着色但不知如何选出每色2个且同色相邻 | 证明引理：对N色各≥N+1次的序列，归纳法扫描找首次重复对，保留并删除，归纳 | 0.5 | 思维操作引导 | false | {structural_existence, logical_deduction, structural_transformation} | ["scan from left", "first repeated color", "induction", "adjacency"] |
| 6 | AI在归纳中需验证剩余颜色仍有足够数量 | t₀是首次重复位置，之前每色≤1次，删除后每色≥N+1-1=N次，满足归纳假设 | 0.4 | 推进 | false | {structural_existence, logical_deduction, knowledge_gap} | ["color count preservation", "at most one before repeat", "induction hypothesis"] |
| 7 | AI有引理但需连接回原身高排名条件 | 同色=同身高组=第(2k-1)和第2k高，同色相邻即满足原条件，完成证明 | 0.3 | 能量传递引导 | false | {structural_existence, logical_deduction, method_translation} | ["height block", "color-to-height translation", "conclusion"] |

**全局tell_hint_pairs详情**：

1. path_feature型：
- scope: "整个解题路径从问题到证明"
- observation_point: null
- tell: "解题需要非显然的问题变换：着色将刚性身高排名约束转化为柔性颜色相邻约束，再用扫描+归纳证明"
- hint: "面对排列上的配对相邻约束，考虑着色/分组将约束松弛为可用归纳处理的颜色约束"
- hint_level: 0.7
- generalizability: "high — 着色松弛约束的模式适用于许多组合选择问题"
- why_not_visible_locally: "着色变换是全局策略，在任何单一步骤中不可见——局部只看到身高约束或颜色约束之一，看不到两者之间的桥梁"
- tell_topology: {structural_existence, case_by_case, structural_transformation}
- tell_small_concepts: ["coloring by height groups", "constraint relaxation", "problem transformation", "scan-and-induct"]

2. implicit型：
- scope: "扫描+归纳引理"
- observation_point: "R5"
- tell: "扫描直到重复的技术隐含使用鸽巢原理：前N+2个元素中N+1种颜色必有重复"
- hint: "颜色约束选择时扫描直到鸽巢迫使重复——这给出归纳的手柄"
- hint_level: 0.6
- generalizability: "medium — 鸽巢扫描技术适用于颜色选择问题但需要N+1倍数的特定结构"
- why_not_visible_locally: "鸽巢应用隐含在扫描中——局部只看到'扫描直到重复'，但重复在N+2步内保证的原因是鸽巢原理，这在扫描步骤本身不可见"
- tell_topology: {structural_existence, logical_deduction, knowledge_gap}
- tell_small_concepts: ["pigeonhole principle", "scan from left", "first repeated color", "N+2 items N+1 colors"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "Bare AI会尝试直接按身高排名逐对构造子序列（从最高对开始贪心），在处理配对间的交互约束时陷入case analysis的泥潭。它不会想到用着色/分组将身高排名约束松弛为颜色约束，因此无法找到归纳结构。即使想到归纳，也会因为缺乏着色变换而无法建立归纳假设。"
- suitable_for_poc: ["POC-VMS-hint-injection（着色提示注入验证）", "POC-VMS-tell-detection（识别AI未走着色方向的tell）", "POC-VMS-level-discrimination（区分能否想到着色变换的AI水平）"]
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

✅ 已写入 `subagents-dirs/compfiles_imo2017p5/profile.json`

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
2. 更新`problem_extraction_progress`集合中`_key="329242"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2017p5"
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
    '_key': '329242',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2017p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2017p5')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

验证输出：`验证通过: compfiles_imo2017p5, 7 local pairs, 2 global pairs`

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_imo2017p5
- solution_method_type: coloring_and_induction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型，1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否。当前分类体系（structural_existence / case_by_case / structural_transformation）完全适用。
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
