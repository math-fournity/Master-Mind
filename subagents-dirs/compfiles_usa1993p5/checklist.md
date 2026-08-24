# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa1993p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa1993P5.lean
- **来源**: USA 1993 P5
- **ArangoDB progress记录_key**: 329372（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa1993P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：正实数序列 xₙ 满足 xₙ₋₁xₙ₊₁ ≤ xₙ²。令 aₙ 为 x₀, x₁, ..., xₙ 的平均值，bₙ 为 x₁, x₂, ..., xₙ 的平均值。证明 aₙbₙ₋₁ ≥ aₙ₋₁bₙ。
- 解答核心思路（1-2句话）：条件 xₙ₋₁xₙ₊₁ ≤ xₙ² 意味着相邻比值 xₙ₊₁/xₙ 非递增（对数凹性），由此推出 x₀·xₙ ≤ xᵢ·xₙ₋ᵢ，配对后用 AM-GM 得到 k ≥ (n-1)√(x₀·xₙ)，再结合 x₀+xₙ ≥ 2√(x₀·xₙ)，最终通过代数化简完成证明。
- 解答关键步骤列表：
  1. 识别条件为对数凹性：xₙ₋₁xₙ₊₁ ≤ xₙ² ⟺ 比值 xₙ₊₁/xₙ 非递增
  2. 由非递增比值推出 x₀·xₙ ≤ xᵢ·xₙ₋ᵢ（对称乘积界）
  3. 对每对 (xᵢ, xₙ₋ᵢ) 用 AM-GM：xᵢ + xₙ₋ᵢ ≥ 2√(x₀·xₙ)
  4. 求和得 k = x₁+...+xₙ₋₁ ≥ (n-1)√(x₀·xₙ)
  5. 再用 AM-GM：x₀+xₙ ≥ 2√(x₀·xₙ)
  6. 组合得关键不等式：(n²-1)·x₀·xₙ ≤ k·(k+x₀+xₙ)
  7. 最终代数：将 aₙ, bₙ 用 x₀, k, xₙ 表出，验证不等式等价于关键不等式

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
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：已知条件是什么？要证明的不等式涉及哪些对象？aₙ和bₙ分别是什么？ | 已知正实数序列xₙ满足xₙ₋₁xₙ₊₁≤xₙ²，aₙ是x₀到xₙ的平均值，bₙ是x₁到xₙ的平均值，要证aₙbₙ₋₁≥aₙ₋₁bₙ。涉及两个前缀平均的交叉比较。 |
| 2 | 自由列举 | 0.7 | 列出所有可能的证明方向：直接展开、归纳法、凸性/对数凹性、比值分析、其他不等式工具 | 直接展开aₙbₙ₋₁-aₙ₋₁bₙ；数学归纳法；利用条件xₙ₋₁xₙ₊₁≤xₙ²的某种结构解释；AM-GM；Cauchy-Schwarz；比值单调性分析 |
| 3 | 小尝试 | 0.3 | 试着直接展开aₙbₙ₋₁-aₙ₋₁bₙ，用部分和表示，看看能否直接利用条件 | 展开后得到涉及部分和Sₙ的表达式，代数非常复杂，条件xₙ₋₁xₙ₊₁≤xₙ²难以直接代入，此路不通 |
| 4 | 思维操作引导 | 0.4 | 将条件xₙ₋₁xₙ₊₁≤xₙ²改写为xₙ₊₁/xₙ≤xₙ/xₙ₋₁，这说明什么？这个结构性质如何利用？ | 这说明相邻比值xₙ₊₁/xₙ是非递增的，即序列是对数凹的。这意味着远离端点的项相对更大 |
| 5 | 思维操作引导 | 0.5 | 利用比值非递增，证明x₀·xₙ≤xᵢ·xₙ₋ᵢ对所有i≤n成立。提示：考虑从端点向中间移动时乘积如何变化 | 由比值非递增，xᵢ/x₀≥xₙ/xₙ₋ᵢ（通过链式比值比较），因此x₀·xₙ≤xᵢ·xₙ₋ᵢ。即对称位置的乘积至少和端点乘积一样大 |
| 6 | 推进 | 0.4 | 有了x₀·xₙ≤xᵢ·xₙ₋ᵢ后，对每对(xᵢ,xₙ₋ᵢ)用AM-GM，然后求和。令k=x₁+...+xₙ₋₁，能得到什么界？ | 每对xᵢ+xₙ₋ᵢ≥2√(x₀·xₙ)，求和得2k≥(n-1)·2√(x₀·xₙ)，即k≥(n-1)√(x₀·xₙ)。再用AM-GM得x₀+xₙ≥2√(x₀·xₙ)，组合得(n²-1)x₀xₙ≤k(k+x₀+xₙ) |
| 7 | 能量传递引导 | 0.3 | 现在将aₙ,bₙ用x₀,k,xₙ表示，验证aₙbₙ₋₁≥aₙ₋₁bₙ恰好等价于关键不等式(n²-1)x₀xₙ≤k(k+x₀+xₙ)，完成证明 | aₙ=(x₀+k+xₙ)/(n+1), bₙ₋₁=k/(n-1), aₙ₋₁=(x₀+k)/n, bₙ=(k+xₙ)/n，代入后交叉相乘，不等式恰等价于(n²-1)x₀xₙ≤k(k+x₀+xₙ)，由步骤6已证，QED |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.4
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
- problem_type: inequality_proof
- structure_features: 正实数序列满足对数凹性条件xₙ₋₁xₙ₊₁≤xₙ²，需要证明两个前缀平均的交叉不等式aₙbₙ₋₁≥aₙ₋₁bₙ
- key_objects: 正实数序列xₙ、相邻比值xₙ₊₁/xₙ、前缀平均aₙ和bₙ、中间和k=x₁+...+xₙ₋₁、AM-GM不等式

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["对数凹性识别（将乘法条件翻译为比值单调性）", "对称配对（xᵢ与xₙ₋ᵢ配对）", "AM-GM应用", "代数化归（将平均不等式归约为关键不等式）"]
- primary_pattern: 对数凹性识别（将乘法条件翻译为比值单调性）
- knowledge_required: ["AM-GM不等式", "对数凹性/比值单调性", "序列部分和的代数操作", "对称配对技巧"]
- key_insight: 条件xₙ₋₁xₙ₊₁≤xₙ²意味着相邻比值非递增（对数凹性），由此推出对称乘积界x₀·xₙ≤xᵢ·xₙ₋ᵢ，使得AM-GM配对成为可能

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接代数展开（将aₙbₙ₋₁-aₙ₋₁bₙ展开为部分和表达式）
- translation_to: 对数凹性分析+对称配对+AM-GM（将乘法条件翻译为比值单调性，再配对用AM-GM）
- translation_type: method_translation（从暴力代数到结构化不等式方法）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: method_problem_mismatch}
- tell_small_concepts: ["对数凹性", "非递增比值", "对称配对", "AM-GM", "前缀平均交叉比较", "关键不等式化归"]
- expected_ai_method: 直接展开aₙbₙ₋₁-aₙ₋₁bₙ为部分和表达式，试图用条件xₙ₋₁xₙ₊₁≤xₙ²逐项代入（暴力代数）
- correct_method: 将条件翻译为比值非递增（对数凹性），推导对称乘积界，配对用AM-GM得到中间和的下界，再代数化归为平均不等式

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？可以，inequality_proof + direct_calculation + method_problem_mismatch 都已有
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？一致
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？足够
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化

**拓扑进化建议**（如有）：无，已有拓扑分类完全够用。

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

| qa_round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对一个涉及序列平均的不等式，但尚未识别条件的结构含义 | 描述题目结构：已知条件、要证的不等式、aₙ和bₙ的定义 | 0.8 | 纯元认知观察 | false | {inequality_proof, direct_calculation, method_problem_mismatch} | ["前缀平均", "交叉比较", "序列条件"] |
| 2 | AI需要探索方向但尚未看到对数凹性这条关键路径 | 列出所有可能方向：直接展开、归纳、凸性、比值分析、不等式工具 | 0.7 | 自由列举 | false | {inequality_proof, enumeration_brute_force, search_space_estimation} | ["方向列举", "对数凹性", "AM-GM", "归纳法"] |
| 3 | AI尝试直接展开代数但陷入复杂表达式，条件难以直接代入 | 试直接展开aₙbₙ₋₁-aₙ₋₁bₙ用部分和表示 | 0.3 | 小尝试 | false | {inequality_proof, direct_calculation, method_problem_mismatch} | ["部分和展开", "代数复杂度", "条件代入困难"] |
| 4 | AI未识别条件xₙ₋₁xₙ₊₁≤xₙ²为对数凹性/比值非递增 | 将条件改写为xₙ₊₁/xₙ≤xₙ/xₙ₋₁，识别比值非递增 | 0.4 | 思维操作引导 | true | {inequality_proof, direct_calculation, knowledge_gap} | ["对数凹性", "比值单调性", "条件重写"] |
| 5 | AI有比值非递增但未看到如何推出对称乘积界 | 利用比值非递增证明x₀·xₙ≤xᵢ·xₙ₋ᵢ | 0.5 | 思维操作引导 | false | {inequality_proof, logical_deduction, structural_transformation} | ["对称乘积界", "端点乘积", "链式比值比较"] |
| 6 | AI有对称乘积界但未看到AM-GM配对求和的路径 | 对每对(xᵢ,xₙ₋ᵢ)用AM-GM再求和，得到k的下界 | 0.4 | 推进 | false | {inequality_proof, algebraic_identity, method_translation} | ["AM-GM配对", "求和下界", "中间和k", "关键不等式"] |
| 7 | AI有关键不等式但需要将其与目标不等式aₙbₙ₋₁≥aₙ₋₁bₙ联系起来 | 将aₙ,bₙ用x₀,k,xₙ表示，验证等价性 | 0.3 | 能量传递引导 | false | {inequality_proof, direct_manipulation, method_translation} | ["代数化归", "平均表示", "等价验证"] |

**全局tell_hint_pairs详情**：

| scope_type | scope | observation_point | tell | hint | hint_level | generalizability | why_not_visible_locally | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|---|---|
| path_feature | 整个证明路径R1→R7 | null | 完整路径"条件→对数凹性→对称乘积界→AM-GM配对→关键不等式→代数化归"是一条链式推导，每一步依赖前一步的结构性结论 | 识别乘法条件可翻译为比值单调性，这是整条推导链的起点；后续每一步都是在前一步的结构结论上构建 | 0.6 | high——任何对数凹性序列的不等式问题都可以用"翻译为比值单调性→对称配对→AM-GM"的路径模式 | 在局部视角中，AI只看到当前步骤的代数操作，看不到"对数凹性识别"如何最终通向"平均不等式"——中间隔着4步推导，每步引入新结构（对称界、AM-GM、关键不等式），这些结构间的因果关系在局部不可见 | {inequality_proof, direct_calculation, method_problem_mismatch} | ["对数凹性", "对称配对", "AM-GM", "关键不等式", "代数化归"] |
| implicit | 条件xₙ₋₁xₙ₊₁≤xₙ²的隐藏结构 | R4 | 条件xₙ₋₁xₙ₊₁≤xₙ²表面上是一个三项乘积不等式，但隐含了序列的对数凹性——这个结构性质不是条件本身直接显示的，需要通过比值重写才能看到 | 将乘法条件改写为比值形式xₙ₊₁/xₙ≤xₙ/xₙ₋₁，识别出比值非递增这一隐藏结构 | 0.5 | high——任何形如aₙ₋₁aₙ₊₁≤aₙ²的序列条件都隐含对数凹性，这一翻译操作可泛化到所有类似条件 | 在局部步骤中，条件以乘法形式出现，AI自然倾向于在乘法框架下操作（如直接代入、配凑），而"改写为比值"这一翻译操作不在条件的表面形式中可见——需要主动的视角转换才能发现 | {inequality_proof, direct_calculation, knowledge_gap} | ["对数凹性", "比值单调性", "条件重写", "隐藏结构"] |

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会直接展开aₙbₙ₋₁-aₙ₋₁bₙ为部分和表达式，试图用条件xₙ₋₁xₙ₊₁≤xₙ²逐项代入，但代数过于复杂无法推进。关键错误是未能识别条件隐含的对数凹性（比值非递增），因此无法走到对称配对+AM-GM的路径。
- suitable_for_poc: ["hint注入验证——R4的对数凹性识别hint是否能引导AI走上正确路径", "tell识别验证——R3到R4的分叉（从直接展开失败到比值重写）是否能被系统识别", "路径特征验证——path_feature型全局pair的泛化性测试"]
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
2. 更新`problem_extraction_progress`集合中`_key="329372"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa1993p5"
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
    '_key': '329372',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa1993p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa1993p5')
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
- problem_id: compfiles_usa1993p5
- solution_method_type: log_concavity_symmetric_pairing_amgm
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类完全够用（inequality_proof / direct_calculation / method_problem_mismatch 等均已有）
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
