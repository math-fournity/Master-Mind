# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1986p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1986P6.lean
- **来源**: IMO 1986 P6
- **ArangoDB progress记录_key**: 329116（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1986P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：给定平面上有限个整数坐标点的集合，是否总能将这些点染成红色或白色，使得对于任何平行于坐标轴的直线L，L上白点数与红点数之差的绝对值不超过1？
- 解答核心思路（1-2句话）：对点数做归纳。归纳步骤分两种情况：若某点在其所在行或列中独占（Case A），则删去该点归纳后选择其符号平衡该行/列；若每个点在行和列上都有邻居（Case B），则找到一个交替路径（水平-竖直交替步），由极大性论证其必闭合为偶长交替环，用交替符号染色环（对每行每列贡献为0），删去环后归纳。
- 解答关键步骤列表：
  1. 定义Balanced签名：ε(p)∈{+1,-1}，每行每列的ε之和绝对值≤1
  2. 归纳基例：空集平凡满足
  3. Case A（孤独点）：点P在其列中独占→删P归纳→选P符号使行平衡（列自动平衡因为只有P）
  4. Case A对称版：点P在其行中独占→坐标交换后同上
  5. Case B（无孤独点）：每个点在行和列上都有邻居→构造交替路径（水平步在偶数位置，竖直步在奇数位置）
  6. 取极大交替路径L，论证L必闭合为环：最后一步的行/列邻居若在路径中则成环，若不在则可延长路径（矛盾极大性）
  7. 环为偶长≥4，用交替符号(+1,-1,+1,-1,...)染色，pair_sum_zero引理保证每行每列贡献为0
  8. 删去环中点，归纳剩余部分，合并染色（环部分贡献0，不干扰剩余部分的平衡）

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
| 1 | 纯元认知观察 | 0.3 | 请描述这道题的结构：已知什么、要求什么、约束条件是什么？将染色问题翻译为数学语言。 | 已知有限整数坐标点集S，要求给每个点分配+1（白）或-1（红），使得对每条平行于坐标轴的直线L，L上所有点的符号之和的绝对值≤1。这是一个组合存在性问题。 |
| 2 | 自由列举 | 0.5 | 列出所有可能解决这个染色存在性问题的方法方向。 | 可能方向：贪心逐点染色、归纳法（对点数归纳）、概率方法、代数方法（线性代数/矩阵）、构造性方法、Hall定理类匹配论证。 |
| 3 | 小尝试 | 0.4 | 试试贪心方法：逐点分配颜色，每次选择使当前行平衡的颜色。这个方法在哪里会出问题？ | 贪心方法的问题：给某行选颜色平衡了该行，但可能破坏该点所在列的平衡。行和列的约束相互耦合，局部贪心无法同时满足两个方向的约束。需要全局结构。 |
| 4 | 思维操作引导 | 0.6 | 考虑对点数做归纳。归纳步骤中，你需要删去一些点后归纳再扩展。什么样的点删去后最容易扩展染色？ | 如果某个点P在其所在行（或列）中是唯一的点，那么删去P后对剩余点集归纳得到平衡染色，然后只需选择P的符号使其所在行平衡即可——列自动平衡因为P是列中唯一点。这是"孤独点"情形。 |
| 5 | 思维操作引导 | 0.7 | 如果没有孤独点——即每个点在行和列上都至少有一个邻居——什么组合结构必然存在？考虑交替走水平步和竖直步的路径。 | 如果每个点在行和列上都有邻居，可以构造交替路径：从任意点出发，先水平走到同行另一个点，再竖直走到同列另一个点，如此交替。取极大交替路径L，其最后一步的行（或列）邻居要么在路径中（形成环），要么不在（可延长路径，矛盾极大性）。因此L必闭合为偶长交替环。 |
| 6 | 推进 | 0.5 | 你找到了偶长交替环。如何染色这个环使其对每行每列贡献为0？然后如何与归纳结合？ | 用交替符号染色环：偶数位置+1，奇数位置-1。由于环中每对相邻的同行（或同列）点恰好一个+1一个-1，每行每列在环中的贡献恰好为0。删去环中点，对剩余点集归纳，合并染色——环贡献0不干扰剩余部分的平衡。 |
| 7 | 能量传递引导 | 0.8 | 现在你有了两种情况的完整论证：孤独点（删去扩展）和交替环（染色删除）。将它们组装成完整的归纳证明。 | 对|S|做强归纳。基例|S|=0平凡。归纳步骤：若存在孤独点（行或列中独占），Case A删去归纳扩展；若不存在孤独点（每点行列都有邻居），Case B找极大交替路径→闭合为偶长交替环→交替染色→删环归纳。两种情况穷尽，归纳完成。□ |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.3+0.5+0.4+0.6+0.7+0.5+0.8 = 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R5（交替路径→环的构造是纯知识瓶颈，需要知道交替路径和极大性论证）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R4（识别归纳结构和"孤独点"概念是思维瓶颈）

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
- structure_features: 有限整数坐标点集，行/列双方向平衡约束（|符号和|≤1），需要证明平衡签名总存在
- key_objects: [有限格点集合S, 符号函数ε:ℤ×ℤ→{+1,-1}, 行和/列和, 交替路径(AltPath), 偶长交替环, 极大路径]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [归纳法(对点数强归纳), 情形二分(孤独点vs交替环), 极大性论证(极大路径必闭合), 交替结构利用, 配对消去(交替符号使行/列贡献为0), 对称性利用(坐标交换)]
- primary_pattern: 归纳法配合情形二分
- knowledge_required: [归纳原理, 图论中路径与环的概念, 交替路径(alternating path), 符号函数与绝对值不等式, 极大性论证技巧]
- key_insight: 归纳步骤的自然二分：要么存在"孤独点"（行或列中独占，删去后易扩展），要么每点行列都有邻居（此时极大交替路径必闭合为偶长交替环，交替染色使环对每行每列贡献为0，删环归纳即可）

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 贪心/局部逐点染色
- translation_to: 结构化归纳配合交替环删除
- translation_type: method_translation（从局部贪心方法翻译到全局结构归纳方法）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: case_by_case, gap_type: structural_transformation}
- tell_small_concepts: [归纳二分, 交替环, 孤独点删除, 平衡签名, 极大路径闭合]
- expected_ai_method: 贪心逐点染色或逐情形枚举——逐点分配颜色试图同时满足行列约束，但行列耦合导致局部方法失败
- correct_method: 对点数归纳，归纳步骤二分：孤独点情形（删去归纳扩展）vs 交替环情形（极大交替路径闭合为偶长环，交替染色贡献0，删环归纳）

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？
  - problem_type=structural_existence ✅ 已有
  - ai_method_type=case_by_case ✅ 已有（bare AI会尝试逐情形处理）
  - gap_type=structural_transformation ✅ 已有（关键是从局部贪心翻译到结构归纳+交替环）
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？
  - 是，三个维度都在已有值的抽象层级上
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？
  - 足够。这道题的tell特征（归纳二分+交替环）可以用(structural_existence, case_by_case, structural_transformation)充分区分
- [x] 如果发现拓扑分类需要进化，在此写出建议：
  - 无需进化，已有拓扑分类够用

**拓扑进化建议**（如有）：
- 无需进化。当前拓扑分类体系可以充分描述本题的tell特征。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs详见profile.json**

**全局tell_hint_pairs详见profile.json**

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: Bare AI会尝试贪心逐点染色或局部方法，在行约束和列约束的耦合处卡住。它不会发现归纳步骤需要二分（孤独点vs交替环），尤其不会构造交替路径并用极大性论证得到交替环。即使想到归纳，也难以独立发现"无孤独点时每点行列有邻居→极大交替路径必闭合为环"这一关键结构。
- suitable_for_poc: [tell-hint注入POC（验证结构变换型hint能否引导AI发现交替环）, 知识瓶颈POC（R5的交替路径知识注入）, 归纳引导POC（验证归纳结构hint的有效性）]
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

**将完整JSON写入工作目录的 `profile.json` 文件** ✅ 已写入

---

## Step 10: 入库ArangoDB [x]

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id） ✅
2. 更新`problem_extraction_progress`集合中`_key="329116"`的记录 ✅

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证输出: compfiles_imo1986p6, 7 local pairs, 2 global pairs

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_imo1986p6
- solution_method_type: induction_with_case_dichotomy
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类体系充分够用
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
