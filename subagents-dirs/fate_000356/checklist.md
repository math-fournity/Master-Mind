# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000356
- **文件路径**: subagents-dirs/fate_000356/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396466（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000356/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let R be a Noetherian ring. Let M be a Cohen-Macaulay module over R. Then M ⊗_R R[x₁,...,xₙ] is a Cohen-Macaulay module over R[x₁,...,xₙ]. （CM模在多项式环标量延拓下保持CM性质）
- 解答核心思路（1-2句话）：Lean证明为sorry（未提供），但数学证明核心是：CM是局部性质，故只需在每个素理想处验证；多项式环的素理想收缩到R的素理想后，局部化归约到R_p上的局部情形；多项式变量构成正则序列，使depth和dimension同时增加n，从而depth=dim的等式保持不变。
- 解答关键步骤列表：
  1. CM是局部性质——Module.IsCohenMacaulay定义为"在每个素理想p处局部化后是CM"，故只需对R[x₁,...,xₙ]的每个素理想P验证
  2. 素理想收缩——P ∈ Spec(R[x₁,...,xₙ])收缩到p = P ∩ R ∈ Spec(R)，局部化(R[x₁,...,xₙ])_P是R_p[x₁,...,xₙ]的进一步局部化
  3. 局部化传递——M_p是R_p上的CM模（由假设），需证M_p ⊗_{R_p} R_p[x₁,...,xₙ]在局部化后仍CM
  4. 正则序列论证——多项式变量x₁,...,xₙ构成R_p[x₁,...,xₙ]上的正则序列，添加n个正则元素使depth增加n
  5. 维度计算——dim(M_p ⊗ R_p[x₁,...,xₙ]) = dim(M_p) + n（多项式环使维度增加n）
  6. 等式保持——depth和dim同时增加n，故depth = dim的等式保持，CM性质得证

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
| 1 | 纯元认知观察 | 0.8 | 请描述这道题目的结构：已知什么数学对象？需要证明什么结论？CM模的定义中关键的等式是什么？ | 已知：Noetherian环R，R上的CM模M。需证：M⊗_R R[x₁,...,xₙ]是R[x₁,...,xₙ]上的CM模。CM模的定义关键在于depth = dimension（在每个素理想处局部化后），即模的深度等于其支撑的Krull维数。 |
| 2 | 自由列举 | 0.7 | 要证明CM性质在多项式环标量延拓下保持，你能想到哪些可能的证明方向？请列出所有你能想到的途径。 | 方向包括：(1)直接计算depth和dim；(2)利用CM的局部性质逐个素理想验证；(3)利用正则序列刻画CM；(4)利用Ext消逝刻画CM；(5)利用多项式环是自由R模的结构；(6)归纳法对变量个数n归纳。 |
| 3 | 小尝试 | 0.4 | 试试方向(1)：直接计算M⊗R R[x₁,...,xₙ]的depth和dimension，不做局部化，看看能否直接得到等式。 | 直接计算遇到困难：depth和dimension都是局部概念，在非局部环上直接计算depth需要指定理想，而CM的定义要求在所有素理想处局部化后depth=dim。不做局部化无法直接比较全局的depth和dim。此路不通。 |
| 4 | 思维操作引导 | 0.5 | 既然直接计算行不通，请执行以下思维操作：利用CM的局部性质，将问题归约到局部情形——对R[x₁,...,xₙ]的任意素理想P，只需验证局部化后是CM。然后思考P如何与R的素理想产生联系。 | CM是局部性质：Module.IsCohenMacaulay定义为对每个素理想p，局部化后是CM。所以对R[x₁,...,xₙ]的任意素理想P，需证(M⊗R R[x])_P在(R[x])_P上是CM。P收缩到R给出p=P∩R∈Spec(R)，且(R[x])_P是R_p[x]的进一步局部化。由假设M_p是R_p上CM模。 |
| 5 | 推进 | 0.6 | 继续推进：现在已归约到局部情形R_p，M_p是R_p上CM模。请进一步分析M_p⊗_{R_p} R_p[x₁,...,xₙ]的depth和dimension分别是什么，它们如何与M_p的depth和dim联系起来。 | M_p是R_p上CM模，故depth(M_p)=dim(M_p)。对于M_p⊗R_p R_p[x₁,...,xₙ]：维度方面，多项式环使维数增加n，即dim(M_p⊗R_p R_p[x])=dim(M_p)+n。深度方面，需要分析多项式变量对depth的影响——关键在于x₁,...,xₙ是否构成正则序列。 |
| 6 | 思维操作引导 | 0.4 | 关键步骤：请论证多项式变量x₁,...,xₙ在R_p[x₁,...,xₙ]上构成M_p⊗R_p R_p[x₁,...,xₙ]的正则序列。正则序列如何影响depth？ | 多项式变量x₁,...,xₙ是R_p[x₁,...,xₙ]中的非零因子（因为多项式环中变量不是零因子），且依次商模仍保持此性质，故构成正则序列。每添加一个正则元素，depth增加1。因此depth(M_p⊗R_p R_p[x])=depth(M_p)+n。结合R5的dim(M_p)+n，两者同时增加n。 |
| 7 | 能量传递引导 | 0.7 | 现在所有要素都已就位：depth和dim同时增加n，等式保持。请完成最终论证，确认CM性质得证。 | depth(M_p⊗R_p R_p[x])=depth(M_p)+n=dim(M_p)+n=dim(M_p⊗R_p R_p[x])。等式depth=dim保持，故M_p⊗R_p R_p[x₁,...,xₙ]在(R_p[x])_P上是CM模。由于P任意，M⊗R R[x₁,...,xₙ]在R[x₁,...,xₙ]上是CM模。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.8+0.7+0.4+0.5+0.6+0.4+0.7 = 4.1
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6"
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
- problem_type: structural_existence（需证明一个结构性质在代数操作下保持存在）
- structure_features: 给定Noetherian环R和CM模M，证明M⊗_R R[x₁,...,xₙ]在多项式环R[x₁,...,xₙ]上保持CM性质。核心结构是"性质在标量延拓下的保持性"，通过局部化归约和正则序列论证完成。
- key_objects: Noetherian环R, Cohen-Macaulay模M, 多项式环R[x₁,...,xₙ], 张量积M⊗_R R[x₁,...,xₙ], 素理想P及其收缩p=P∩R, 局部化R_p, depth(深度), Krull dimension(维数), 正则序列x₁,...,xₙ

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [局部化归约, 正则序列论证, 维度-深度联合计算, 素理想收缩映射, 性质保持性证明]
- primary_pattern: 局部化归约（将全局问题归约到局部情形，在局部情形中利用正则序列完成论证）
- knowledge_required: [Cohen-Macaulay模定义, depth与Krull dimension的关系, 正则序列与深度的关系, 多项式环的素理想结构, 素理想收缩与局部化的交换性, 张量积与标量延拓]
- key_insight: 多项式变量x₁,...,xₙ构成正则序列，使depth和dimension同时增加n，从而depth=dim的等式保持不变——这是CM性质在多项式延拓下保持的核心原因。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 全局直接计算（试图在非局部环上直接计算depth和dimension）
- translation_to: 局部化归约+正则序列论证（将问题翻译到局部情形，利用正则序列的性质完成depth和dim的联合计算）
- translation_type: structural_transformation（从全局计算结构翻译到局部化结构，再利用正则序列的代数结构完成论证）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: knowledge_gap}
- tell_small_concepts: [Cohen-Macaulay模, 多项式环标量延拓, 局部化归约, 正则序列, depth与dimension等式, 素理想收缩]
- expected_ai_method: bare AI预期会尝试直接计算M⊗R R[x₁,...,xₙ]的depth和dimension，不进行局部化归约，卡在depth和dim是局部概念这一步
- correct_method: 局部化归约到R_p情形，利用多项式变量构成正则序列使depth和dim同时增加n，保持等式

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ 能。structural_existence（性质保持的存在性证明）、direct_calculation（bare AI预期直接计算）、knowledge_gap（关键知识是正则序列与depth/dim的关系）均可归入已有类别。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ 是。三个维度的值都是抽象粒度，与已有值一致。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ 足够。这道题的tell特征（局部化归约+正则序列）可以通过problem_type=structural_existence和gap_type=knowledge_gap的组合区分。
- [x] 如果发现拓扑分类需要进化，在此写出建议： 无需进化。当前三维拓扑分类足以描述此题。

**拓扑进化建议**（如有）：无。当前拓扑分类体系足够。

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

| R | tell | hint | level | sit_type | kb | topology | small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对题目尚未识别CM的局部性质，只看到depth=dim的表面等式 | 描述题目结构，识别已知/未知和CM定义的关键等式 | 0.8 | 纯元认知观察 | false | (structural_existence, direct_calculation, method_problem_mismatch) | [CM模定义, depth=dim等式, Noetherian环] |
| 2 | AI列出多个方向但未优先排序局部化归约，直接计算排在首位 | 列出所有可能的证明方向 | 0.7 | 自由列举 | false | (structural_existence, direct_calculation, method_problem_mismatch) | [直接计算, 局部化, 正则序列, Ext消逝, 归纳法] |
| 3 | AI尝试直接计算depth和dim，卡在depth/dim是局部概念这一步 | 试方向(1)直接计算，不做局部化 | 0.4 | 小尝试 | false | (structural_existence, direct_calculation, method_problem_mismatch) | [全局depth, 局部概念, 理想指定, 此路不通] |
| 4 | AI未将问题归约到局部情形，未利用CM定义中的素理想局部化结构 | 利用CM局部性质归约到局部情形，思考P与R素理想的联系 | 0.5 | 思维操作引导 | false | (structural_existence, logical_deduction, structural_transformation) | [局部化归约, 素理想P, 收缩p=P∩R, R_p局部化] |
| 5 | AI已归约到局部情形但未分析depth和dim如何随多项式环变化 | 分析M_p⊗R_p R_p[x]的depth和dim如何与M_p联系 | 0.6 | 推进 | false | (structural_existence, logical_deduction, structural_transformation) | [素理想收缩, 维数增加n, depth待分析, 多项式环结构] |
| 6 | AI未识别多项式变量构成正则序列这一关键知识 | 论证多项式变量构成正则序列，分析正则序列对depth的影响 | 0.4 | 思维操作引导 | true | (structural_existence, direct_calculation, knowledge_gap) | [正则序列, 非零因子, depth增加n, 依次商模] |
| 7 | AI已掌握所有要素但未组装最终论证 | 完成最终论证，确认CM性质得证 | 0.7 | 能量传递引导 | false | (structural_existence, logical_deduction, knowledge_gap) | [depth=dim等式保持, P任意, CM性质得证, 证毕] |

**全局pair详情**：

| # | scope_type | scope | obs_pt | tell | hint | level | generalizability | why_not_visible_locally | topology | small_concepts |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | path_feature | 从R3直接计算失败到R6正则序列论证的完整路径 | null | 直接计算depth和dim在全局层面失败后，正确路径是局部化归约→素理想收缩→正则序列论证→等式保持。路径特征是每次归约都同时追踪depth和dim的变化 | 当直接计算行不通时，寻找定义中蕴含的局部结构，归约到局部情形后利用代数结构完成论证 | 0.7 | high — 局部化归约+正则序列的路径特征适用于所有CM性质保持类证明 | 在R3的局部视角中AI只看到直接计算失败，但看不到'失败后应局部化'这一路径特征——需要纵观从失败到成功的完整过程才能识别 | (structural_existence, direct_calculation, structural_transformation) | [局部化归约路径, 正则序列, depth-dim同步增加] |
| 2 | implicit | R5-R6中depth和dim同时增加n的蕴含信息 | R6 | 多项式变量构成正则序列蕴含depth增加n，多项式环维度公式蕴含dim增加n——两者增量相同这一蕴含信息是CM保持的关键 | 当分别计算depth和dim变化时，注意比较两者变化量是否相同——相同增量意味着等式保持 | 0.5 | high — '两个量同步变化保持等式'的蕴含信息适用于所有等式保持类证明 | 在R5中只计算了dim增加n，在R6中只计算了depth增加n——两者在不同步骤中独立计算，'增量相同'这一蕴含信息在任一局部步骤中都不可见，需要跨步骤综合才能发现 | (structural_existence, direct_calculation, knowledge_gap) | [depth增量, dim增量, 增量相同, 等式保持] |

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接计算M⊗R R[x₁,...,xₙ]的depth和dimension，不进行局部化归约。由于depth和dim是局部概念，在非局部环上直接计算会遇到定义困难。即使AI想到局部化，也可能不知道多项式变量构成正则序列这一关键事实，无法完成depth增加n的论证。这是一道高难度的交换代数证明题，需要深厚的CM模和正则序列知识。
- suitable_for_poc: ["POC-VMS-hint-injection（hint端验证：注入局部化归约+正则序列方向后能否引导AI完成证明）", "POC-VMS-tell-detection（tell端验证：能否从AI的thinking中检测到'未进行局部化'和'未识别正则序列'的分叉信号）", "POC-VMS-knowledge-gap（知识瓶颈验证：R6正则序列知识是否是关键瓶颈）"]
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

**将完整JSON写入工作目录的 `profile.json` 文件** — 已写入 subagents-dirs/fate_000356/profile.json

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
2. 更新`problem_extraction_progress`集合中`_key="396466"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000356"
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
    '_key': '396466',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000356',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000356')
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
- problem_id: fate_000356
- solution_method_type: localization_reduction_with_regular_sequence
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1 path_feature + 1 implicit）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，当前三维拓扑分类（structural_existence / direct_calculation / knowledge_gap）足以描述此题
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
