# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000258
- **文件路径**: subagents-dirs/fate_000258/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396368（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000258/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let G be a finite group and let Syl_p(G) denote its set of Sylow p-subgroups. Suppose that S and T are distinct members of Syl_p(G) chosen so that #(S ∩ T) is maximal among all such intersections. Prove that the normalizer N_G(S ∩ T) does not admit normal Sylow p-subgroup.
- 解答核心思路（1-2句话）：反证法。假设 N_G(D) 有正规 Sylow p-子群 P（D = S ∩ T）。利用 p-群的正规化子增长性质，在 S\D 和 T\D 中找到正规化 D 的元素 s, t，它们必属于 P。P 含于 G 的某 Sylow p-子群 S'，但 S' 不能是 S 或 T（否则 s 或 t 落入 D，矛盾），而 S' ∩ S ⊇ P ∩ S ⊋ D 违反 D 的极大性，矛盾。
- 解答关键步骤列表：
  1. 设 D = S ∩ T，假设 N_G(D) 有正规 Sylow p-子群 P
  2. D 是 N_G(D) 的 p-子群，故 D ⊆ P（P 是 N_G(D) 唯一 Sylow p-子群）
  3. S 是 p-群，D ⊊ S，由正规化子增长性质 N_S(D) ⊋ D，取 s ∈ N_S(D) \ D
  4. 同理取 t ∈ N_T(D) \ D
  5. s, t 是 N_G(D) 中的 p-元素，故 s, t ∈ P
  6. P 是 G 的 p-子群，含于某 Sylow p-子群 S' 中
  7. 若 S' = S，则 t ∈ P ⊆ S，t ∈ T，故 t ∈ D，矛盾；若 S' = T，同理 s ∈ D，矛盾
  8. 故 S' ≠ S 且 S' ≠ T，但 S' ∩ S ⊇ P ∩ S ⊋ D（因 s ∈ P ∩ S \ D），违反极大性，矛盾

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
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：已知什么（G有限群，S和T是不同的Sylow p-子群，#(S∩T)极大），要证什么（N_G(S∩T)没有正规Sylow p-子群）？关键数学对象有哪些？ | 已知G有限群，S≠T是Sylow p-子群，D=S∩T的阶在所有不同Sylow p-子群交中极大。要证N_G(D)没有正规Sylow p-子群。关键对象：D=S∩T, N_G(D), Sylow p-子群。 |
| 2 | 自由列举 | 0.7 | 列出所有可能用来分析N_G(D)的工具和方法。p-群有哪些特殊性质？正规化子有什么性质？ | 可能工具：Sylow定理（计数、共轭、包含关系）、正规化子的定义、p-群的性质（中心非平凡、正规化子增长）、反证法。p-群的关键性质：每个真子群严格含于其正规化子中。 |
| 3 | 小尝试 | 0.5 | 试一个方向：假设N_G(D)有正规Sylow p-子群P，直接分析D和P的关系。能得出什么？ | D是p-子群（因为D⊆S，S是p-群），D⊆N_G(D)。P是N_G(D)唯一的Sylow p-子群（因为正规），所以D⊆P。但仅此无法直接得到矛盾，需要更多信息。 |
| 4 | 思维操作引导 | 0.3 | 关键操作：思考p-群的正规化子增长性质——在p-群中，每个真子群H满足H严格小于N_G(H)。将此性质应用到D在S中和D在T中的情况。 | S是p-群，D=S∩T是S的真子群（因S≠T且|S|=|T|），故N_S(D)⊋D，存在s∈S\D使s正规化D。同理存在t∈T\D使t正规化D。s,t∈N_G(D)且是p-元素。 |
| 5 | 推进 | 0.4 | 既然s和t是N_G(D)中的p-元素，而P是N_G(D)唯一的Sylow p-子群，能得出什么？进一步，P作为G的p-子群含于哪个Sylow p-子群？ | s,t∈P（因为P是N_G(D)唯一Sylow p-子群，所有p-元素都在P中）。P是G的p-子群，由Sylow定理P⊆S'对某个S'∈Syl_p(G)。 |
| 6 | 推进 | 0.3 | 检查S'能否等于S或T。如果S'=S会怎样？如果S'=T呢？ | 若S'=S：t∈P⊆S，又t∈T，故t∈S∩T=D，但t∉D，矛盾。若S'=T：s∈P⊆T，又s∈S，故s∈D，但s∉D，矛盾。故S'≠S且S'≠T。 |
| 7 | 能量传递引导 | 0.2 | 你已经排除了S'=S和S'=T！现在S'≠S，但S'∩S⊇P∩S，而s∈P∩S且s∉D，所以S'∩S⊋D。这与D的极大性矛盾吗？完成证明！ | 是的！S'≠S，由极大性#(S'∩S)≤#(S∩T)=#D。但S'∩S⊇P∩S⊋D（因s∈P∩S\D），故#(S'∩S)>#D，矛盾。因此N_G(D)没有正规Sylow p-子群。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5
- knowledge_rounds（思维操作引导的轮数）: 1
- level_sum: 3.2
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
- problem_type: structural_existence
- structure_features: 有限群G，S和T是不同的Sylow p-子群，D=S∩T的阶在所有不同Sylow p-子群对的交中极大。要证N_G(D)没有正规Sylow p-子群。这是一个"不存在性"证明——证明某结构（正规Sylow p-子群）不存在。
- key_objects: ["有限群G", "Sylow p-子群S, T", "交集D=S∩T", "正规化子N_G(D)", "假设的正规Sylow p-子群P", "G的另一个Sylow p-子群S'"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["contradiction_setup", "property_extraction_from_p_group", "element_chasing", "case_elimination", "maximality_argument"]
- primary_pattern: contradiction_with_element_chasing
- knowledge_required: ["Sylow定理（包含关系、共轭、计数）", "p-群的正规化子增长性质", "正规Sylow p-子群的唯一性", "极大性论证"]
- key_insight: 利用p-群的正规化子增长性质在S\D和T\D中找到正规化D的元素s,t，这些元素被迫属于假设的正规Sylow p-子群P，而P含于G的某个Sylow p-子群S'中，S'既不能是S也不能是T，最终S'∩S严格大于D违反极大性。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: direct_structural_analysis_of_normalizer（直接分析正规化子结构）
- translation_to: element_chasing_via_normalizer_growth_in_p_groups（通过p-群正规化子增长性质进行元素追踪）
- translation_type: method_translation（从直接结构分析翻译到利用p-群内部性质的元素追踪方法）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "logical_deduction", gap_type: "knowledge_gap"}
- tell_small_concepts: ["Sylow p-子群", "正规化子", "极大交", "p-群正规化子增长", "正规Sylow唯一性", "元素追踪", "极大性矛盾"]
- expected_ai_method: bare AI会尝试直接用Sylow定理和正规化子定义做逻辑推导，可能尝试计数论证或直接分析N_G(D)的结构，但不会想到利用p-群的正规化子增长性质来在D外部找元素
- correct_method: 反证法 + p-群正规化子增长性质 + 元素追踪 + 情况排除 + 极大性矛盾

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是。structural_existence（不存在性证明）、logical_deduction（bare AI预期方法）、knowledge_gap（关键知识缺口是p-群正规化子增长性质）都能归入已有类别。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是。三个值都是抽象级别。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。这道题的核心区分在于knowledge_gap（p-群正规化子增长性质是一个不显见于题目但决定证明路径的知识点），已有gap_type可以覆盖。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。现有拓扑分类体系足够。

**拓扑进化建议**（如有）：无。现有分类体系充分覆盖此题。

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
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到Sylow p-子群和正规化子的题目但未识别关键性质 | 描述题目结构：已知什么，要证什么，关键对象有哪些 | 0.8 | 纯元认知观察 | false | {structural_existence, logical_deduction, method_problem_mismatch} | ["Sylow p-子群", "正规化子", "极大交"] |
| 2 | AI已描述结构但未列出可用工具 | 列出所有可能工具：p-群性质、Sylow定理、正规化子性质 | 0.7 | 自由列举 | false | {structural_existence, enumeration_brute_force, search_space_estimation} | ["p-群性质", "Sylow定理", "正规化子"] |
| 3 | AI尝试直接分析D和P的关系但卡住 | 假设N_G(D)有正规Sylow p-子群P，分析D⊆P | 0.5 | 小尝试 | false | {structural_existence, logical_deduction, method_problem_mismatch} | ["反证法", "正规Sylow", "包含关系"] |
| 4 | AI已设好反证框架但不知道如何在D外找元素 | 应用p-群正规化子增长性质：N_S(D)⊋D, N_T(D)⊋D | 0.3 | 思维操作引导 | true | {structural_existence, logical_deduction, knowledge_gap} | ["正规化子增长", "p-群", "真子群", "N_S(D)⊋D"] |
| 5 | AI找到s,t但未连接到P和S' | s,t∈P（唯一Sylow），P⊆S'（某Sylow p-子群） | 0.4 | 推进 | false | {structural_existence, logical_deduction, structural_transformation} | ["p-元素", "唯一Sylow", "Sylow包含"] |
| 6 | AI知道P⊆S'但未排除S'=S或S'=T | 检查S'=S→t∈D矛盾；S'=T→s∈D矛盾 | 0.3 | 推进 | false | {structural_existence, case_by_case, structural_transformation} | ["情况排除", "S'≠S", "S'≠T", "矛盾"] |
| 7 | AI已排除S'=S,T，需要完成极大性矛盾 | S'∩S⊋D违反极大性，完成证明 | 0.2 | 能量传递引导 | false | {structural_existence, logical_deduction, method_problem_mismatch} | ["极大性矛盾", "S'∩S⊋D", "证毕"] |

**全局tell_hint_pairs详情**：

Global pair 1 (path_feature):
- scope_type: "path_feature"
- scope: "整个证明路径——从反证假设到极大性矛盾"
- observation_point: null
- tell: "证明需要组合三个非显然的要素：p-群正规化子增长、正规Sylow唯一性、极大性矛盾。单独看任何一步都无法预见完整路径。"
- hint: "路径是：假设正规Sylow P存在 → 用正规化子增长在D外找元素s,t → s,t∈P → P⊆某Sylow S' → S'≠S,T → S'∩S⊋D违反极大性"
- hint_level: 0.5
- generalizability: "medium — 正规化子增长技术可泛化到许多p-群论证，但具体的极大性矛盾结构是本题特有的"
- why_not_visible_locally: "完整矛盾结构只有在三个要素全部组合后才显现。从任何单一步骤看，其他两个步骤的角色不可见——R3只看到D⊆P但看不到为什么需要在D外找元素，R4找到s,t但看不到为什么需要放入S'，R6排除S'=S,T但看不到极大性矛盾如何收尾。"
- tell_topology: {structural_existence, logical_deduction, method_translation}
- tell_small_concepts: ["正规化子增长", "矛盾结构", "极大性", "路径组合"]

Global pair 2 (implicit):
- scope_type: "implicit"
- scope: "从反证框架到找到关键元素的过渡"
- observation_point: "Q4"
- tell: "关键缺失要素是p-群的正规化子增长性质——没有它，无法在D外部找到正规化D的元素，整个证明路径断裂"
- hint: "在p-群中，每个真子群H满足H严格小于其正规化子N_G(H)。这是在S\D和T\D中找到正规化D的元素的关键。"
- hint_level: 0.3
- generalizability: "high — 正规化子增长是p-群理论的基础工具，在许多群论证明中反复出现"
- why_not_visible_locally: "正规化子增长性质是关于p-群内部结构的一般定理，题目只提到Sylow p-子群和正规化子，不暗示p-群内部结构相关。在R3的直接分析中，AI只看到D⊆P但完全没有理由去思考S作为p-群的内部结构——这个蕴含信息在局部步骤中完全不可见。"
- tell_topology: {structural_existence, logical_deduction, knowledge_gap}
- tell_small_concepts: ["正规化子增长", "p-群", "真子群严格包含"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会用Sylow定理和正规化子定义做直接逻辑推导，可能正确设出反证框架并得到D⊆P，但不会想到利用p-群的正规化子增长性质在D外部找元素。没有这一步，整个矛盾链条断裂——AI会在D⊆P后陷入停滞，不知道如何从N_G(D)的结构中获得矛盾。可能尝试错误的计数论证或不相关的Sylow计数定理。
- suitable_for_poc: ["tell_detection_poc", "knowledge_gap_poc", "hint_injection_poc"]
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
2. 更新`problem_extraction_progress`集合中`_key="396368"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000258"
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
    '_key': '396368',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000258',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000258')
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
- problem_id: fate_000258
- solution_method_type: contradiction_with_normalizer_growth
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有拓扑分类体系（structural_existence / logical_deduction / knowledge_gap等）充分覆盖此题。
- 是否遇到异常: 无异常。所有字段验证通过，ArangoDB入库和验证成功。

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
