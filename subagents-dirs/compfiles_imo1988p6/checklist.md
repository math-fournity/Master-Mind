# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1988p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1988P6.lean
- **来源**: IMO 1988 P6
- **ArangoDB progress记录_key**: 329124（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1988P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：If a and b are two natural numbers such that ab+1 divides a²+b², show that their quotient (a²+b²)/(ab+1) is a perfect square.
- 解答核心思路（1-2句话）：设 k=(a²+b²)/(ab+1)，将方程 a²+b²=k(ab+1) 视为关于 b 的二次方程，利用 Vieta 公式找到另一个根 b'=ka-b，证明 b' 是非负整数且 b'<a（下降步骤），通过无穷递降到达基例（b=0 时 k=a²；a=b 时 k≤1），此时 k 显然是完全平方数。
- 解答关键步骤列表：
  1. 设 k=(a²+b²)/(ab+1)，将方程改写为 b²-kab+(a²-k)=0（关于 b 的二次方程）
  2. 利用 Vieta 公式：若 (a,b) 是解，则另一个根 b'=ka-b，且 b·b'=a²-k
  3. 证明下降步骤：当 0<a<b 时，b' 是非负整数且 b'≤a，故 (b',a) 是"更小"的解
  4. 对称性：解集关于 a↔b 对称（H_symm）
  5. 基例1：b=0 时 a²=k，k=a² 是完全平方数
  6. 基例2：a=b 时 2a²=(a²+1)k，迫使 k≤1，故 k=0 或 k=1，都是完全平方数
  7. 无穷递降：取 b 最小的解，下降产生更小解，矛盾，故必到达基例

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：已知什么？要证什么？商 k=(a²+b²)/(ab+1) 是什么类型的数学对象？ | 已知 a,b∈ℕ 且 (ab+1)∣(a²+b²)。要证 (a²+b²)/(ab+1) 是完全平方数。商 k 是自然数，需证 ∃d: d²=k。这是连接整除性与完全平方数的数论问题。 |
| 2 | 自由列举 | 0.7 | 列出所有可能的方法来证明由整除条件产生的商是完全平方数。 | 1) 直接计算找模式 2) 模运算 3) 整除关系的代数变形 4) 二次型/Pell方程 5) 无穷递降 6) Vieta公式 7) 解的参数化描述 |
| 3 | 小尝试 | 0.3 | 试算几组小的 (a,b) 对，看商有什么模式。 | a=1,b=1: k=1=1²。a=2,b=8: k=4=2²。a=3,b=27: k=9=3²。模式：b=a³ 时 k=a²。但这只覆盖特殊情况，无法证明一般结论。 |
| 4 | 思维操作引导 | 0.5 | 固定 k=(a²+b²)/(ab+1)，将方程 a²+b²=k(ab+1) 改写为关于 b 的二次方程。这揭示了什么结构？ | 整理得 b²-kab+(a²-k)=0，这是关于 b 的二次方程。若 (a,b) 是解，由 Vieta 公式另一个根 b' 满足 b+b'=ka 且 b·b'=a²-k。 |
| 5 | 推进 | 0.4 | 给定另一个根 b'=ka-b 且 b·b'=a²-k，能否证明当 b>a>0 时 b' 是非负整数且 b'<a？这会给出一个"更小"的解。 | b'=(a²-k)/b，因 b>a 故 b'<a²/b<a。b'=ka-b 是整数。非负性：由 b·b'=a²-k 和 k 的界可证 b'≥0。故 (b',a) 是同一曲线上更小的解。 |
| 6 | 思维操作引导 | 0.5 | 现在建立无穷递降：取 b 最小的解，下降给出更小解，产生矛盾。基例是什么？基例中 k 是完全平方数吗？ | 若 b 最小，下降产生 (b',a) 且 b'<a≤b，矛盾，除非 b'=0 或 b'=a。b'=0 时 a²=k，k=a² 是完全平方数。b'=a 时 2a²=(a²+1)k，迫使 k≤1，故 k=0 或 1，都是完全平方数。 |
| 7 | 能量传递引导 | 0.8 | 你已有所有组件：二次方程重构、Vieta公式下降步骤、基例分析。综合成完整证明。 | 设 k=(a²+b²)/(ab+1)。方程 b²-kab+(a²-k)=0 有解 b，另一根 b'=ka-b。对 b>a>0，b' 非负且 b'<a，给出更小解。由无穷递降（b 的最小性），到达 b'=0（k=a²）或 b'=a（k≤1）。故 k 恒为完全平方数。QED。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1+R2+R5+R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4+R6）
- level_sum: 0.8+0.7+0.3+0.5+0.4+0.5+0.8 = 4.0
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R4（需要知道Vieta公式并识别二次方程结构）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R6（需要建立完整的无穷递降论证并识别基例）

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
- problem_type: structural_existence（需证存在 d 使得 d²=k，即 k 具有特定结构）
- structure_features: 整除条件 (ab+1)∣(a²+b²) 定义了一个双曲线上的整数点集；商 k 在所有解对上保持常数；解集关于 a↔b 对称
- key_objects: ["自然数对 (a,b)", "商 k=(a²+b²)/(ab+1)", "二次方程 b²-kab+(a²-k)=0", "Vieta公式另一根 b'=ka-b", "双曲线上的整数点集"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["二次方程重构（将整除条件视为二次方程）", "Vieta公式应用（利用根与系数关系）", "无穷递降（通过最小性论证到达基例）", "对称性利用（解集关于a↔b对称）", "基例分析（b=0和a=b两种情况）"]
- primary_pattern: Vieta jumping（Vieta公式驱动的常数递降）
- knowledge_required: ["整除性与完全平方数", "二次方程的Vieta公式", "无穷递降原理", "良序原理/最小元论证"]
- key_insight: 将整除条件 a²+b²=k(ab+1) 重构为关于 b 的二次方程，用 Vieta 公式找到"更小"的解，通过无穷递降到达 k 显然是完全平方数的基例。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 整除性/数论语言（直接计算商并试图证明是完全平方数）
- translation_to: 二次方程/递降语言（将整除条件重构为二次方程，用Vieta公式驱动递降）
- translation_type: structural_transformation（问题结构的根本性转换——从"计算并验证"到"二次方程+递降"）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: ["divisibility", "perfect_square", "quadratic_equation", "vieta_formulas", "infinite_descent", "vieta_jumping", "constant_descent"]
- expected_ai_method: 直接代数变形和试算例子，试图找到模式或用模运算，无法看到二次方程重构和Vieta递降
- correct_method: Vieta jumping（常数递降）：将整除条件重构为二次方程，用Vieta公式找到更小的解，应用无穷递降到达基例

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
- [x] 当前拓扑分类是否够用——这道题的problem_type(structural_existence)/ai_method_type(direct_calculation)/gap_type(structural_transformation)都能归入已有的拓扑类别
- [x] 粒度是否一致——标注值与已有值粒度统一
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化，现有分类体系可覆盖

**拓扑进化建议**（如有）：无。现有 problem_type/ai_method_type/gap_type 三个维度足以刻画此题的拓扑特征。

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

**局部pair拓扑分布**：R1-R3为{structural_existence, direct_calculation/enumeration_brute_force, method_problem_mismatch}；R4为{structural_existence, algebraic_identity, knowledge_gap}（知识瓶颈）；R5-R7为{structural_existence, algebraic_identity/logical_deduction, method_translation}

**全局pair详情**：
1. path_feature型：完整Vieta jumping路径（二次重构→Vieta公式→递降→基例），why_not_visible_locally=递降结构只有看到完整链条才显现
2. implicit型：k在递降中的常数性（observation_point=Q4），why_not_visible_locally=k被保持来自二次方程结构但在单步中未明确强调

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI会尝试直接代数变形或模运算，在特殊情况找到模式（如b=a³时k=a²），但无法看到二次方程重构和Vieta jumping递降。可能卡在尝试参数化所有解或用不等式估计k的范围。
- suitable_for_poc: ["tell_hint_injection", "method_translation_poc", "structural_transformation_poc", "knowledge_bottleneck_poc"]
- discriminates_levels: true（此题清晰区分知道Vieta jumping和不知道的AI，是IMO历史上最难的题之一）

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

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_imo1988p6
- solution_method_type: vieta_jumping_descent
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有problem_type/ai_method_type/gap_type三个维度足以刻画此题拓扑特征。
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
