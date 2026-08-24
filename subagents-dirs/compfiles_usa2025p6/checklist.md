# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2025p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2025P6.lean
- **来源**: USA 2025 P6
- **ArangoDB progress记录_key**: 329510（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2025P6.lean`（2062行，分段读完）

**产出**：
- 题目原文（数学描述）：设m,n为正整数，m≥n。m个不同口味的cupcake排成圆圈，n个人各给每个cupcake打非负实数分。假设对每个人P，都能将圆圈分成n组连续cupcake使P对每组的总分≥1。证明存在一种分配方案将m个cupcake分给n个人，使每人P按自己的评分获得总分≥1。
- 解答核心思路（1-2句话）：对n做强归纳。固定一个人（person 0）的圆圈分割，用Hall亏值定理将人分为匹配集M和未匹配集B，匹配的人直接获得对应弧段；对未匹配的人，用圆形手术(surgery)删除已分配弧段得到更小圆圈，利用"删除弧段对B中人得分<1"的性质通过合并引理(mergeValues)保持剩余弧段得分≥1，对更小圆圈用归纳假设。
- 解答关键步骤列表：
  1. 基础情形n=1：一个人获得全部cupcake，分割条件直接给出得分≥1
  2. 归纳步骤n≥2：固定person 0的分割Pπ为n个弧段，每人得分≥1
  3. 应用Hall亏值定理(hall_deficiency)：得到匹配集M、弧段集T、双射f:M→T，person 0∈M，M外的人对T中弧段得分<1
  4. 若B=∅（全部匹配）：每个cupcake分配给其所属弧段对应的人，每人得分≥1
  5. 若B≠∅：用surgeryMany删除M对应弧段，得到更小圆圈(m'=m-Σla)和圆形嵌入φ
  6. 对B中每人：其原分割在删除弧段上得分<1（Hall亏值性质），用mergeValues合并引理得到更小圆圈上的有效分割（k-t个弧段，每个得分≥1）
  7. 对更小圆圈(|B|<n人)应用归纳假设，得到B中人的分配
  8. 合并：删除弧段中的cupcake分给M中人（通过匹配f），圆圈外cupcake通过φ映射分给B中人（通过归纳分配）

---

## Step 2: QA序列分析——局部视角7步 [x]

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构。关键对象有哪些？已知条件和待证结论之间的核心张力是什么？ | 题目有m个cupcake排成圆圈、n个人各打非负分。每人都有自己的圆圈分割使每组得分≥1，但需要证明存在一个全局分配方案使每人总分≥1。核心张力：每人有各自的分割，但需要统一的分配——个体分割条件如何推出全局分配存在性。 |
| 2 | 自由列举 | 0.7 | 列出所有可能解决这个问题的方法方向。 | 可能方向：Hall婚配定理、对n做归纳、贪心分配、线性规划、组合论证、圆形结构利用、分治法、概率方法等。 |
| 3 | 小尝试 | 0.5 | 试一个直接贪心方法：把每个cupcake分给打分最高的人。这能保证每人得分≥1吗？ | 不能。贪心分配不尊重分割条件——每人得分≥1的保证来自连续弧段，贪心打散了连续性。一个人可能得到分散的cupcake，总分无法保证≥1。 |
| 4 | 思维操作引导 | 0.4 | 考虑对n做强归纳。n=1时平凡。归纳步骤中，固定一个人的分割为n个弧段，思考如何将问题分解为已解决部分和更小的子问题。 | 固定person 0的分割Pπ为n个弧段。如果能把某些弧段分配给某些人（他们在该弧段得分≥1），剩余问题就缩小了。但不同人有不同分割，需要一种系统方法确定哪些人能匹配到哪些弧段。 |
| 5 | 思维操作引导 | 0.3 | 应用Hall婚配定理的亏值形式(deficiency version)。每人需要一个弧段（来自person 0的分割）使其得分≥1。Hall亏值定理给出什么结构？ | Hall亏值定理给出匹配集M、弧段集T和双射f:M→T，使M中人在f(p)弧段得分≥1。关键：M外的人（集合B）对T中所有弧段得分<1。person 0一定在M中（他对所有弧段得分≥1）。 |
| 6 | 推进 | 0.4 | 现在有M匹配到T中弧段，B未匹配。T中弧段覆盖的cupcake可以分给M中人。对B中人，删除这些弧段后得到更小圆圈。B中人的原分割在删除弧段上得分<1，能否合并相邻弧段保持得分≥1？ | 可以。合并引理(mergeValues)：若一个弧段得分<1被删除，它两侧的分割弧段各得分≥1，合并后弧段得分≥1+1-1=1。因此B中每人都能在更小圆圈上得到有效分割（弧段数从n减到n-|M|）。 |
| 7 | 能量传递引导 | 0.6 | 更小圆圈上有|B|<n个人，每人都有有效分割。对更小问题用归纳假设得到B中人的分配，再与M中人的匹配合并。完整证明就完成了！ | 对更小圆圈（m'=m-Σ删除弧段长度，|B|<n人）应用归纳假设，得到分配方案a'。最终分配：删除弧段中的cupcake分给M中人（通过f），圆圈外cupcake通过圆形嵌入φ映射分给B中人（通过a'）。每人得分≥1，归纳完成。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.8+0.7+0.5+0.4+0.3+0.4+0.6 = 3.7
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: constraint_satisfaction
- structure_features: 圆形排列的m个对象，n个主体各有非负评分函数，每人存在圆圈分割使各段得分≥1，需证明全局分配存在性。核心结构张力：个体分割条件→全局分配。
- key_objects: cupcake圆圈(ZMod m)、人(Fin n)、评分函数(like: Fin n → ZMod m → ℝ)、圆圈分割(CirclePartition)、Hall亏值匹配(M, T, f)、圆形嵌入/手术(skipMap, CircleEmb)

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["strong_induction", "hall_deficiency_matching", "structural_reduction_surgery", "merge_conquer", "circular_embedding"]
- primary_pattern: strong_induction
- knowledge_required: ["Hall婚配定理亏值形式", "圆圈分割与弧段", "强归纳", "圆形嵌入与手术(skipMap)", "合并引理(mergeValues)"]
- key_insight: 用Hall亏值定理将人分为匹配集M和未匹配集B，对B中人利用"匹配弧段上得分<1"的性质通过合并引理在更小圆圈上保持有效分割，从而对更小问题用归纳假设

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 匹配论(Hall亏值定理)与圆形组合结构
- translation_to: 组合分配存在性证明（通过强归纳+圆形手术）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "constraint_satisfaction", ai_method_type: "direct_calculation", gap_type: "structural_transformation"}
- tell_small_concepts: ["Hall亏值定理", "圆圈分割", "圆形手术", "合并弧段", "强归纳", "得分<1蕴含可合并", "匹配集与未匹配集"]
- expected_ai_method: 贪心分配或直接匹配，忽略圆形结构和归纳分解的需求
- correct_method: 强归纳+Hall亏值定理+圆形手术+合并引理

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=constraint_satisfaction、ai_method_type=direct_calculation、gap_type=structural_transformation都能归入已有拓扑类别
- [x] 粒度一致——标注值和已有值粒度统一
- [x] 三个维度足够区分——这道题的tell（需要从直接计算翻译到结构化归纳+匹配）与已有tell有足够区分度
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。当前拓扑分类足够。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs详见profile.json**

**全局tell_hint_pairs**：
1. path_feature型：完整解题路径（Hall亏值→圆形手术→合并→归纳→合并分配）在局部步骤中不可见
2. implicit型：合并引理的核心不等式（得分<1的弧段删除后，相邻弧段合并仍≥1）需要同时掌握三个条件才能发现

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI会尝试贪心分配或标准Hall定理（非亏值形式），忽略圆形结构和归纳分解的需求。不会想到用Hall亏值定理创建匹配/未匹配分割，不会想到用圆形手术删除弧段后通过合并引理保持有效分割，也不会想到将三个工具（Hall亏值+手术+归纳）组合使用。
- suitable_for_poc: ["tell_extraction", "hint_injection", "topology_matching"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON，写入 `subagents-dirs/compfiles_usa2025p6/profile.json`

**⚠️ 完整字段清单（逐项检查）**：
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
- [x] answer
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

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证输出: compfiles_usa2025p6, 7 local pairs, 2 global pairs

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_usa2025p6
- solution_method_type: strong_induction_with_matching
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。当前拓扑分类（constraint_satisfaction / direct_calculation / structural_transformation）足够覆盖此题。
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
