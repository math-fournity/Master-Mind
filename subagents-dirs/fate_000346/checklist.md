# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000346
- **文件路径**: subagents-dirs/fate_000346/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396456（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000346/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设k是特征零的域，n∈ℕ且n≠0，φ:k[x₁,...,xₙ]→k[x₁,...,xₙ]是由(x₁,...,xₙ)↦(f₁(x₁),...,fₙ(xₙ))给出的自同态，其中fᵢ(xᵢ)∈k[xᵢ]且deg(fᵢ)≥2。则存在点a∈kⁿ使得对任意非零多项式p∈k[x₁,...,xₙ]，存在m∈ℕ使得p(φᵐ(a))≠0。
- 解答核心思路（1-2句话）：证明存在一个点a其在φ下的轨道{φᵐ(a)}是Zariski稠密的。关键利用deg≥2保证φ在多项式环上的单射性和p∘φᵐ的次数指数增长，使得每个"坏集"B_p足够小，它们的并集不能覆盖kⁿ。
- 解答关键步骤列表：
  1. 证明φ在k[x₁,...,xₙ]上是单射的（因为每个fᵢ的次数≥2≥1，代入不消灭非零多项式）
  2. 对每个非零p，p∘φᵐ对所有m都是非零多项式（由步骤1归纳）
  3. 定义坏集B_p={a: p(φᵐ(a))=0 ∀m}，则B_p⊆V(p)是真代数集的子集
  4. 利用p∘φᵐ的次数随m指数增长，分析B_p比V(p)更小（维度更低）
  5. 利用char 0保证k是无限域（k⊇ℚ），结合次数增长结构证明∪_p B_p≠kⁿ
  6. 得到存在a∉∪_p B_p，即a的轨道是Zariski稠密的

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
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：有哪些关键数学对象？要求证明什么性质？量词顺序是什么？ | 关键对象：域k(char 0)、多项式环k[x₁,...,xₙ]、自同态φ(xᵢ↦fᵢ(xᵢ), deg≥2)、点a∈kⁿ、轨道{φᵐ(a)}、非零多项式p。要求证明∃a∀p≠0∃m: p(φᵐ(a))≠0，即存在一个点其轨道不被任何非零多项式的零集完全包含——轨道是Zariski稠密的。量词顺序是∃a∀p∃m。 |
| 2 | 自由列举 | 0.7 | 列出所有可能的证明方法。哪些方法可能适用于所有char 0域（包括可数域如ℚ）？ | 1. 不可数性论证（k不可数时可数并不能覆盖）2. 代数无关性论证（选代数无关的坐标）3. 直接构造a 4. Zariski拓扑+维数论证 5. 次数增长分析 6. 测度论方法。对于可数域如ℚ，不可数性和测度论方法失效，需要纯代数论证。 |
| 3 | 小尝试 | 0.5 | 尝试用k的不可数性来论证：可数个真代数集的并不能覆盖kⁿ。这个方法对一般char 0域成立吗？ | 当k不可数（如ℝ或ℂ）时，可数个真代数集的并确实不能覆盖kⁿ。但char 0只保证k⊇ℚ即k是无限域，不保证k不可数。对于k=ℚ（可数），可数个真代数集的并可以覆盖ℚⁿ（如ℚ¹=∪_{a∈ℚ}{a}）。所以不可数性方法对一般char 0域不充分。 |
| 4 | 思维操作引导 | 0.4 | 聚焦deg≥2条件。φ作为多项式环上的映射是否单射？p∘φᵐ作为x的多项式，其次数随m如何变化？ | deg≥2≥1保证φ单射：若p≠0，其首项在代入xᵢ↦fᵢ(xᵢ)后不会消消（因为各变量独立代入且fᵢ非常数）。因此p∘φᵐ≠0对所有m成立。次数方面，若p的总次数为d，则p∘φᵐ的总次数至少为d·2^m（因为每个fᵢ次数≥2），呈指数增长。 |
| 5 | 思维操作引导 | 0.5 | 对每个非零p，定义坏集B_p={a: p(φᵐ(a))=0 ∀m≥0}。分析B_p的结构：它比V(p)小多少？ | B_p⊆V(p)（取m=0），V(p)是真代数集（超曲面，维数n-1）。但B_p⊆V(p)∩V(p∘φ)∩...，而p和p∘φ次数不同故不共线，V(p)∩V(p∘φ)维数≤n-2。继续迭代，B_p⊆∩_{m=0}^{n-1}V(p∘φᵐ)，维数≤0，即B_p是有限集（或空集）。次数增长使交集越来越小。 |
| 6 | 推进 | 0.6 | 综合各步：每个B_p是有限集，∪_p B_p不能覆盖kⁿ。如何严格论证？ | 按次数分层：对每个次数d，次数≤d的非零多项式构成有限维k-向量空间。对应的坏集并集是有限个有限集的并（因为每个B_p有限，且本质不同的多项式只有有限个等价类）。有限集不能覆盖kⁿ（k无限）。对所有d取并，得到可数个有限集的并。但关键在于：对于固定的次数d，B_p的非空性要求轨道被困在超曲面中，而次数增长使这几乎不可能——更精确地，用k无限性和代数集的有限性直接构造a。 |
| 7 | 能量传递引导 | 0.7 | 确认完整证明策略：deg≥2给出单射性和次数增长，char 0给出k无限，两者结合确保坏集足够小。总结证明。 | 完整策略：(1)φ单射→p∘φᵐ≠0 (2)B_p⊆∩V(p∘φᵐ)是有限集 (3)k无限→有限个有限集不能覆盖kⁿ (4)按次数分层→每层只有有限个本质不同的坏集 (5)可数层的并仍不能覆盖kⁿ（因为每层有限且k无限，可用对角论证或直接构造）。因此存在a∉∪B_p，其轨道Zariski稠密。√ |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 4.2
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
- structure_features: 存在性证明——存在一个点其在多项式自同态下的轨道是Zariski稠密的；坐标独立的多项式映射，每个分量次数≥2；char 0域上的代数动力学
- key_objects: 域k(char 0), 多项式环k[x₁,...,xₙ], 自同态φ, 多项式fᵢ(deg≥2), 点a∈kⁿ, 轨道{φᵐ(a)}, 非零多项式p, 坏集B_p, 真代数集V(p)

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["structural_analysis", "counterexample_elimination", "degree_growth_argument", "algebraic_set_dimension_argument", "method_translation"]
- primary_pattern: degree_growth_argument
- knowledge_required: ["多项式环上的自同态", "代数集与Zariski拓扑", "多项式代入的单射性", "特征零域的性质", "代数集的维数理论", "轨道与Zariski稠密性"]
- key_insight: deg≥2条件同时保证了φ的单射性和p∘φᵐ的次数指数增长，使得每个坏集B_p被压缩到有限集，从而它们的并集无法覆盖无限域kⁿ

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 解析/拓扑直觉（不可数性论证、测度论方法）
- translation_to: 代数论证（Zariski拓扑、次数增长、真代数集的维数分析）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: method_problem_mismatch}
- tell_small_concepts: ["Zariski density", "orbit", "polynomial endomorphism", "degree growth", "proper algebraic set", "algebraic independence", "char zero", "injectivity"]
- expected_ai_method: 不可数性论证——bare AI会用k的不可数性来论证可数个真代数集的并不能覆盖kⁿ，未意识到char 0只保证k无限而非不可数
- correct_method: 代数轨道论证——利用φ的单射性和p∘φᵐ的次数指数增长将每个坏集B_p压缩到有限集，再用k的无限性和次数分层论证并集不能覆盖kⁿ

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？是。structural_existence + direct_calculation + method_problem_mismatch 完全适用。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？是。三个维度都使用了已有的抽象级别值。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？足够。这道题的核心gap是"方法与问题不匹配"（不可数性方法vs一般char 0域问题），用method_problem_mismatch可以准确描述。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。现有拓扑分类体系可以充分描述这道题的tell结构。

**拓扑进化建议**（如有）：无。现有分类体系充分。

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

**局部pairs详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到存在性问题关于轨道和多项式自同态，但可能未识别Zariski稠密性联系 | 描述题目结构：关键对象有哪些？要求证明什么性质？量词顺序是什么？ | 0.8 | 纯元认知观察 | false | {structural_existence, logical_deduction, method_problem_mismatch} | ["orbit", "polynomial endomorphism", "existence", "Zariski density"] |
| 2 | AI列举方法但偏向解析/拓扑论证（不可数性、测度），未考虑纯代数方法 | 列出所有可能方法。哪些适用于所有char 0域包括可数域如ℚ？ | 0.7 | 自由列举 | false | {structural_existence, enumeration_brute_force, search_space_estimation} | ["uncountability", "algebraic independence", "generic point", "Zariski topology", "countable field"] |
| 3 | AI尝试不可数性论证，发现对可数域如ℚ失效 | 尝试用k的不可数性论证可数个真代数集的并不能覆盖kⁿ。这对一般char 0域成立吗？ | 0.5 | 小尝试 | false | {structural_existence, direct_calculation, method_problem_mismatch} | ["uncountability", "countable field", "char zero", "proper algebraic set", "covering argument"] |
| 4 | AI需要识别deg≥2在单射性和次数增长中的双重作用 | 聚焦deg≥2条件。φ作为多项式环映射是否单射？p∘φᵐ的次数随m如何变化？ | 0.4 | 思维操作引导 | true | {structural_existence, algebraic_identity, knowledge_gap} | ["degree growth", "injectivity", "polynomial substitution", "composition", "leading term"] |
| 5 | AI需要分析坏集B_p的结构并理解为何它比V(p)小得多 | 对每个非零p定义B_p={a: p(φᵐ(a))=0 ∀m}。分析B_p比V(p)小多少？ | 0.5 | 思维操作引导 | false | {structural_existence, logical_deduction, structural_transformation} | ["bad set", "proper algebraic set", "intersection", "dimension", "degree growth"] |
| 6 | AI需要综合各步证明坏集并集不能覆盖kⁿ | 综合各步：每个B_p是有限集，∪B_p不能覆盖kⁿ。如何严格论证？ | 0.6 | 推进 | false | {structural_existence, logical_deduction, method_translation} | ["countable union", "infinite field", "degree partition", "covering argument", "Zariski density"] |
| 7 | AI已组装证明策略，需确认完整性 | 确认完整策略：deg≥2给单射性和次数增长，char 0给k无限，两者结合确保坏集足够小 | 0.7 | 能量传递引导 | false | {structural_existence, logical_deduction, method_translation} | ["Zariski dense orbit", "existence", "char zero", "degree ≥ 2", "injectivity"] |

**全局pairs详情**：

| # | scope_type | scope | observation_point | tell | hint | hint_level | generalizability | why_not_visible_locally | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | path_feature | 整个证明策略从题目到解答 | null | 证明需要从解析直觉（不可数性）全局翻译为代数论证（次数增长+真代数集），且deg≥2的双重作用（单射性AND次数增长）只有从完整路径才能看到 | 利用代数结构：deg≥2同时给出φ的单射性和p∘φᵐ的次数指数增长，使每个坏集B_p足够小；char 0保证k无限；两者结合确保∪B_p≠kⁿ | 0.6 | high - 利用次数增长控制坏集的方法可推广到其他代数动力学问题 | deg≥2的双重作用和从解析到代数的方法翻译是全局策略特征，无法从任何单个步骤观察到 | {structural_existence, direct_calculation, method_translation} | ["degree growth", "injectivity", "Zariski density", "method translation", "proper algebraic set"] |
| 2 | implicit | char 0条件与证明策略的关联 | R3 | char 0隐含保证k无限（k⊇ℚ），这是覆盖论证的必要但不充分条件；真正的工作由次数增长结构完成 | 认识char 0→k无限是必要的，但关键论证利用deg≥2的次数增长使每个B_p小到即使可数并集也不能覆盖kⁿ | 0.5 | medium - 特定于char 0域上的多项式动力学，但利用代数结构超越基数论证的原则广泛适用 | char 0的角色是隐含的——它出现在题目中但与证明策略的联系（保证k无限，再结合次数增长给出覆盖论证）在任何单个步骤中不可见 | {structural_existence, direct_calculation, knowledge_gap} | ["char zero", "infinite field", "covering argument", "degree growth", "countable union"] |

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会用k的不可数性来论证可数个真代数集的并不能覆盖kⁿ，未意识到char 0只保证k无限而非不可数（k=ℚ是反例）。AI还可能错过deg≥2在单射性和次数增长中的双重作用，以及坏集B_p比V(p)小得多这一关键结构特征。AI可能混淆量词顺序（∃a∀p∃m vs ∀p∃a∃m）。
- suitable_for_poc: ["tell_hint_injection", "topology_filtering", "knowledge_bottleneck_detection", "method_translation_verification"]
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

✅ 已写入 `subagents-dirs/fate_000346/profile.json`，JSON验证通过（34个字段，7个局部pairs，2个全局pairs，7轮QA）

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
2. 更新`problem_extraction_progress`集合中`_key="396456"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000346"
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
    '_key': '396456',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000346',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000346')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功
- 验证结果: [x] 通过

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: fate_000346
- solution_method_type: algebraic_existence_argument
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，现有分类体系充分
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
