# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa1998p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa1998P5.lean
- **来源**: USA 1998 P5
- **ArangoDB progress记录_key**: 329392（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa1998P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Prove that for each n ≥ 2, there is a set S of n integers such that (a-b)² divides ab for every distinct a,b ∈ S.
- 解答核心思路（1-2句话）：对n做归纳。给定满足条件的n元集S_n，令L为所有 pairwise 差的平方之积，构造 S_{n+1} = {L+a : a ∈ S_n} ∪ {0}。关键在于L被每个(a-b)²整除，故 (L+a)(L+b) ≡ ab ≡ 0 mod (a-b)²。
- 解答关键步骤列表：
  1. 加强归纳假设：要求S中元素非负（使归纳步骤更干净）
  2. 基础情形 n=0：空集平凡满足
  3. 定义 L = ∏_{s∈S_n} ∏_{t∈S_n\{s}} (s-t)²（所有 pairwise 差的平方之积）
  4. 构造 S_{n+1} = {L+a : a ∈ S_n} ∪ {0}
  5. 情形1：一个元素为0时，(a-0)² | a·0 = 0，平凡
  6. 情形2：两个元素为 L+a, L+b 时，(L+a)-(L+b)=a-b，且 (L+a)(L+b) = L(L+a+b) + ab，两项均被 (a-b)² 整除
  7. 由归纳法，结论对所有 n ≥ 2 成立

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
| 1 | 纯元认知观察 | 0.3 | 这个题目要求我们做什么？它是什么类型的问题？已知条件和目标分别是什么？ | 这是一个存在性证明题：对每个n≥2，需要构造一个n个整数的集合S，使得对S中任意两个不同元素a,b，(a-b)²整除ab。已知：n是任意≥2的整数。目标：证明这样的集合S存在。 |
| 2 | 自由列举 | 0.5 | 构造这样的集合有哪些可能的策略？请列出你能想到的所有方法。 | 可能的策略：(1)对小的n直接构造具体例子；(2)用数学归纳法，从S_n构造S_{n+1}；(3)利用数论性质如完全平方数、整除关系；(4)用递推关系定义集合元素；(5)利用0的特殊性质（任何数与0的差的平方整除0）。 |
| 3 | 小尝试 | 0.2 | 试着为n=2和n=3构造具体的集合S。n=2时什么集合可行？ | n=2: {0, a}可行，因为(a-0)²=a²整除0。{a, b}需要(a-b)²|ab，例如{1,2}不行因为1∤2。{0,1}可行。n=3: {0, a, b}需要a²|0（平凡），b²|0（平凡），(a-b)²|ab。比如{0,1,?}需要找c使得c²|0和(1-c)²|c，即(1-c)²|c。c=0不行（重复），c=1不行。直接构造似乎不容易推广。 |
| 4 | 思维操作引导 | 0.6 | 小情形直接构造不易推广。请用归纳法的思路思考：如果你已经有一个满足条件的n元集S_n，如何添加一个新元素得到S_{n+1}？关键在于新元素与所有旧元素的关系。 | 用归纳法。假设S_n满足条件。要构造S_{n+1}，需要添加一个新元素x，使得对S_n中每个a，(x-a)²|xa。一个想法：把S_n中所有元素同时平移一个量L，然后添加0作为新元素。这样新元素0与L+a的关系是(L+a)²|0（平凡），而L+a与L+b的关系是(L+a)-(L+b)=a-b，需要(a-b)²|(L+a)(L+b)。 |
| 5 | 思维操作引导 | 0.7 | 你提到平移所有元素并添加0。如果S_{n+1} = {L+a : a ∈ S_n} ∪ {0}，那么L需要满足什么条件？什么样的L自然满足这个条件？ | 需要(a-b)² | (L+a)(L+b) 对所有a,b∈S_n。展开(L+a)(L+b) = L² + L(a+b) + ab = L(L+a+b) + ab。由归纳假设(a-b)²|ab，所以只需(a-b)²|L(L+a+b)，即(a-b)²|L。因此L需要被所有(a-b)²整除。自然的选择：L = ∏_{s≠t, s,t∈S_n} (s-t)²，即所有pairwise差的平方之积。 |
| 6 | 推进 | 0.4 | 你已经找到了L的定义和构造方式。现在请验证这个构造在两种情形下都成立：(1)一个元素是0；(2)两个元素都是L+a和L+b。 | 情形1：若一个元素是0，另一个是L+a，则(L+a-0)²=(L+a)²整除(L+a)·0=0，平凡成立。情形2：两个元素L+a和L+b，差为a-b。乘积(L+a)(L+b)=L(L+a+b)+ab。L被(a-b)²整除（因为L包含(s-t)²因子，其中s=a,t=b），ab被(a-b)²整除（归纳假设）。所以(a-b)²|(L+a)(L+b)。构造验证完成。 |
| 7 | 能量传递引导 | 0.8 | 你已经完成了归纳基础和归纳步骤的验证。请将完整的证明写出来，确保逻辑严密。 | 完整证明：对n归纳。基础n=0：空集平凡满足。归纳步骤：设S_n满足条件，令L=∏_{s,t∈S_n,s≠t}(s-t)²，构造S_{n+1}={L+a:a∈S_n}∪{0}。基数|S_{n+1}|=n+1。验证 divisibility：(1)含0的情形平凡；(2)L+a与L+b的情形，(L+a)(L+b)=L(L+a+b)+ab，两项均被(a-b)²整除。加强归纳假设：要求元素非负，L>0保证平移后仍非负，0非负。由归纳法，对所有n≥2成立。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1,R2,R6,R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4,R5）
- level_sum: 0.3+0.5+0.2+0.6+0.7+0.4+0.8 = 3.5
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
- problem_type: structural_existence
- structure_features: ["existence_proof_for_all_n", "pairwise_divisibility_condition", "inductive_construction_with_shift", "strengthened_induction_hypothesis"]
- key_objects: ["set S of n integers", "pairwise differences (a-b)", "product L of squared pairwise differences", "shifted set {L+a : a in S_n} union {0}"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["inductive_construction", "algebraic_shift", "strengthening_induction_hypothesis", "product_of_pairwise_differences", "case_analysis_on_zero"]
- primary_pattern: inductive_construction_with_algebraic_shift
- knowledge_required: ["mathematical_induction", "divisibility_and_modular_arithmetic", "product_of_pairwise_differences", "algebraic_expansion_of_products", "strengthening_induction_hypothesis"]
- key_insight: 将S_n中所有元素平移L（所有pairwise差平方之积）并添加0，利用 (L+a)(L+b) = L(L+a+b) + ab 且两项均被 (a-b)² 整除来保持整除性

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: direct_construction（直接构造具体集合）
- translation_to: inductive_construction_with_algebraic_shift（归纳构造+代数平移）
- translation_type: method_translation（从直接构造方法翻译到归纳构造方法）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "direct_construction", gap_type: "structural_transformation"}
- tell_small_concepts: ["inductive_construction", "product_of_pairwise_differences", "algebraic_shift", "divisibility_preservation", "strengthening_induction_hypothesis", "case_analysis_on_zero"]
- expected_ai_method: bare AI会尝试对小的n直接构造具体集合，或用枚举法寻找满足条件的集合，但无法发现归纳构造+代数平移的策略
- correct_method: 对n做归纳，将S_n中所有元素平移L（所有pairwise差平方之积）并添加0，利用代数恒等式 (L+a)(L+b) = L(L+a+b) + ab 保持整除性

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是。problem_type=structural_existence已有，ai_method_type=direct_construction可归入direct_calculation/direct_manipulation的粒度层级（但更精确，表示直接构造而非直接计算），gap_type=structural_transformation已有。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 基本一致。direct_construction与direct_calculation/direct_manipulation粒度相当。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。这道题的核心tell是"从直接构造到归纳构造的结构转换"，三个维度能区分。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。ai_method_type新增direct_construction（与direct_calculation/direct_manipulation同级，但强调"构造"而非"计算/操作"），粒度一致。

**拓扑进化建议**（如有）：无需进化。ai_method_type建议新增`direct_construction`，与已有`direct_calculation`/`direct_manipulation`同级，强调"直接构造对象"而非"直接计算/操作"。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI将问题视为需要直接计算/构造，但未识别出归纳结构 | 描述题目类型和结构：这是存在性证明，需要对每个n构造满足pairwise整除条件的集合 | 0.3 | 纯元认知观察 | false | {structural_existence, direct_calculation, method_problem_mismatch} | ["existence_proof", "divisibility_condition", "set_construction"] |
| 2 | AI列举了直接构造和归纳法等方向，但未意识到归纳+代数平移的组合策略 | 列出所有可能方法：直接构造小情形、归纳法、数论性质、递推、利用0的特殊性 | 0.5 | 自由列举 | false | {structural_existence, enumeration_brute_force, search_space_estimation} | ["direct_construction", "small_cases", "induction", "zero_element"] |
| 3 | AI成功构造n=2的情形（含0），但n=3直接构造困难，未看到推广路径 | 试构造n=2和n=3的集合，观察哪些可行、哪些不可行 | 0.2 | 小尝试 | false | {structural_existence, case_by_case, method_problem_mismatch} | ["small_case_construction", "trivial_divisibility", "zero_element"] |
| 4 | AI有小情形但未看到归纳结构——如何从S_n构造S_{n+1}是思维瓶颈 | 用归纳法思考：已有S_n，如何添加新元素？考虑平移所有元素并添加0 | 0.6 | 思维操作引导 | false | {structural_existence, logical_deduction, structural_transformation} | ["induction_on_n", "inductive_step", "adding_element", "shift_and_add_zero"] |
| 5 | AI考虑归纳但不知道L应取什么——product of pairwise differences是知识瓶颈 | L需被所有(a-b)²整除。什么自然的选择满足？取所有pairwise差平方之积 | 0.7 | 思维操作引导 | true | {structural_existence, algebraic_identity, knowledge_gap} | ["product_of_differences", "divisibility_by_shift", "common_multiple", "algebraic_shift"] |
| 6 | AI有构造但需验证两种情形（含0和shifted pairs） | 验证：含0时平凡；L+a与L+b时展开(L+a)(L+b)=L(L+a+b)+ab，两项均被(a-b)²整除 | 0.4 | 推进 | false | {structural_existence, direct_manipulation, method_translation} | ["case_analysis", "modular_arithmetic", "algebraic_expansion", "divisibility_verification"] |
| 7 | AI已验证构造，需整理完整证明并注意加强归纳假设 | 已完成基础和归纳步骤，写出完整证明，注意加强归纳假设（元素非负） | 0.8 | 能量传递引导 | false | {structural_existence, logical_deduction, method_problem_mismatch} | ["induction_conclusion", "strengthened_hypothesis", "base_case", "complete_proof"] |

**全局tell_hint_pairs详情**：

| # | scope_type | scope | observation_point | tell | hint | hint_level | generalizability | why_not_visible_locally | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | path_feature | 整个归纳构造策略 | null | 问题需要归纳构造：每步将元素平移所有pairwise差平方之积L并添加0，利用代数恒等式保持整除性 | 用归纳法。给定S_n，令L=∏(s-t)²，构造S_{n+1}={L+a:a∈S_n}∪{0} | 0.8 | high——归纳构造+product-of-differences平移是整除性保持集合构造的通用技术 | 没有任何一个单独步骤能揭示完整的归纳策略。L的定义和平移操作只有在全局要求"同时保持所有pair的整除性"时才被激发，局部视角只能看到单个pair的验证 | {structural_existence, direct_construction, structural_transformation} | ["inductive_construction", "product_of_pairwise_differences", "algebraic_shift", "divisibility_preservation"] |
| 2 | implicit | 归纳假设的加强 | "R4" | 归纳假设需要加强非负性约束，才能使归纳步骤干净地通过 | 加强命题：要求S中元素非负，使归纳步骤中L>0保证平移后仍非负 | 0.7 | medium——加强归纳假设是通用技巧，但具体的非负约束是问题相关的 | 非负性的需要在任何单步中都不可见。它只在尝试验证归纳步骤时才浮现——需要保证构造的元素满足加强后的条件，这个需求在局部步骤中无法被察觉 | {structural_existence, logical_deduction, knowledge_gap} | ["strengthening_induction_hypothesis", "nonnegativity_constraint", "inductive_step"] |

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试对小的n直接构造具体集合（如n=2用{0,a}），但无法发现归纳构造+代数平移的策略。关键知识瓶颈在于：(1)意识到需要归纳法而非直接构造；(2)知道用product of pairwise differences作为平移量L；(3)知道加强归纳假设（非负性）。bare AI很可能卡在n=3或n=4的直接构造上，无法推广。
- suitable_for_poc: ["tell_identification", "hint_injection", "knowledge_bottleneck_detection", "structural_transformation_detection"]
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
2. 更新`problem_extraction_progress`集合中`_key="329392"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa1998p5"
   - extracted_by改为"subagent"

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_usa1998p5
- solution_method_type: inductive_construction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型，1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 建议在ai_method_type中新增`direct_construction`（与`direct_calculation`/`direct_manipulation`同级，强调"直接构造对象"而非"直接计算/操作"），但无需新增拓扑维度
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
