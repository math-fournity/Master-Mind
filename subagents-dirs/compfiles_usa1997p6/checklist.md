# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa1997p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa1997P6.lean
- **来源**: USA 1997 P6
- **ArangoDB progress记录_key**: 329388（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa1997P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：非负整数序列a₁,a₂,...,a₁₉₉₇满足对所有i,j≥1且i+j≤1997有aᵢ+aⱼ≤aᵢ₊ⱼ≤aᵢ+aⱼ+1。证明存在实数x使得对所有1≤n≤1997有aₙ=⌊nx⌋。
- 解答核心思路（1-2句话）：通过强归纳证明交叉不等式n·a_m+1≤m·a_n+m（即a_m/m<(a_n+1)/n），然后取x=a_p/p（p为使a_n/n最大的指标），用双侧夹逼验证floor条件。
- 解答关键步骤列表：
  1. 证明关键不等式：对所有1≤m,n≤1997，n·a_m+1≤m·a_n+m，即a_m/m<(a_n+1)/n。用m+n的强归纳：m<n时用超可加性a_m+a_s≤a_n+归纳假设(m,s)；m>n时用次可加性a_m≤a_n+a_r+1+归纳假设(r,n)；m=n时平凡。
  2. 取x=a_p/p，其中p∈{1,...,1997}使a_n/n最大（由有限集最大值存在性保证）。
  3. 下界：a_n/n≤a_p/p=x，故a_n≤nx。
  4. 上界：由关键不等式(p,n)得n·a_p+1≤p·a_n+p，故nx=n·a_p/p<(a_n+1)。
  5. 由a_n≤nx<a_n+1得aₙ=⌊nx⌋。

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 观察这道题的结构：已知条件是什么？要证明什么？条件和结论之间的核心距离在哪里？ | 已知序列满足近似可加性aᵢ+aⱼ≤aᵢ₊ⱼ≤aᵢ+aⱼ+1，要证存在x使aₙ=⌊nx⌋。核心距离在于：条件是关于加法/组合性质的，而结论是关于floor函数表示的——需要建立从"近似可加"到"floor序列"的桥梁。 |
| 2 | 自由列举 | 0.7 | 列出所有可能建立这个桥梁的方向。 | 直接构造x（如x=a₁）、对n做归纳逐个确定aₙ、研究比值aₙ/n的性质、利用Archimedean性质、生成函数方法、将条件重写为aᵢ₊ⱼ-aᵢ-aⱼ∈{0,1}并研究误差累积。 |
| 3 | 小尝试 | 0.5 | 试着直接对n做归纳，看看能不能逐个确定aₙ的值或找到x。 | 直接归纳困难：条件涉及的是成对的(i,j)而非单个n，aₙ的值依赖于a₁,...,aₙ₋₁的各种组合，不能从单个前驱确定。a₁只给出x的下界a₁≤x<a₁+1，但后续项的约束更复杂。这条路走不通。 |
| 4 | 思维操作引导 | 0.4 | 考虑比值aₙ/n。近似可加性aᵢ+aⱼ≤aᵢ₊ⱼ≤aᵢ+aⱼ+1对比值aₙ/n意味着什么？尝试形式化。 | 近似可加性意味着a_{i+j}/(i+j)介于(a_i+a_j)/(i+j)和(a_i+a_j+1)/(i+j)之间。直觉上比值aₙ/n应该"几乎常数"——它们之间的差异被1/n控制。如果所有比值都接近某个x，那么aₙ≈nx，且误差不超过1，这正是floor函数的特征。需要形式化"比值几乎常数"这个直觉。 |
| 5 | 推进 | 0.6 | 将"比值几乎常数"形式化：证明对所有1≤m,n≤1997，有n·a_m+1≤m·a_n+m，即a_m/m<(a_n+1)/n。用m+n的强归纳。 | 强归纳on m+n：若m<n，记n=m+s，由超可加性a_m+a_s≤a_n和IH(m,s)得s·a_m+1≤m·a_s+m，组合得(m+s)·a_m+1≤m·a_{m+s}+m。若m>n，记m=n+r，由次可加性a_m≤a_n+a_r+1和IH(r,n)得n·a_r+1≤r·a_n+r，组合得n·a_m+1≤m·a_n+m。若m=n，因n≥1平凡。 |
| 6 | 思维操作引导 | 0.3 | 现在取x=a_p/p，其中p是使aₙ/n在{1,...,1997}中最大的指标。证明aₙ=⌊nx⌋。 | 需证aₙ≤nx<aₙ+1。下界：由p的最大性，aₙ/n≤a_p/p=x，故aₙ≤nx。上界：由关键不等式取(m,n)=(p,n)，得n·a_p+1≤p·aₙ+p，即n·a_p/p<(aₙ+1)，即nx<aₙ+1。由aₙ≤nx<aₙ+1及aₙ为整数，得aₙ=⌊nx⌋。 |
| 7 | 能量传递引导 | 0.8 | 整合所有步骤，写出完整证明。 | 完整证明：1)强归纳证明交叉不等式n·a_m+1≤m·a_n+m；2)取x=a_p/p为最大比值；3)由最大性得下界aₙ≤nx；4)由交叉不等式得上界nx<aₙ+1；5)由floor等价条件得aₙ=⌊nx⌋。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1+R2+R5+R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4+R6）
- level_sum: 0.8+0.7+0.5+0.4+0.6+0.3+0.8=4.1
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization（刻画满足近似可加性的序列为floor序列）
- structure_features: 序列满足双向近似可加性约束（超可加+次可加+1），需证明存在性实数x使序列等于floor(nx)。核心结构是从加法约束到比值约束的翻译。
- key_objects: 非负整数序列{aₙ}, 近似可加性不等式, 比值aₙ/n, 交叉不等式n·a_m+1≤m·a_n+m, 实数x=最大比值, floor函数⌊·⌋

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["ratio_analysis（比值分析）", "strong_induction（强归纳）", "extremal_selection（极值选取）", "two_sided_bound（双侧夹逼）", "structural_translation（结构翻译：加法→比值）"]
- primary_pattern: ratio_analysis（比值分析——将加法约束翻译为比值约束是整个证明的核心驱动力）
- knowledge_required: ["近似可加性（超可加性与次可加性）", "floor函数的等价刻画（a≤x<a+1⟺⌊x⌋=a）", "强归纳法", "极值原理（有限集最大值存在）", "Archimedean性质"]
- key_insight: 近似可加性蕴含比值aₙ/n几乎常数——形式化为交叉不等式n·a_m+1≤m·a_n+m后，取最大比值a_p/p作为x即可满足floor条件aₙ≤nx<aₙ+1。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 加法约束语言（aᵢ+aⱼ≤aᵢ₊ⱼ≤aᵢ+aⱼ+1，关于序列项的加法组合关系）
- translation_to: 比值约束语言（n·a_m+1≤m·a_n+m，即a_m/m<(a_n+1)/n，关于序列项比值的交叉不等式）
- translation_type: structural_transformation（结构翻译——将加法域的不等式翻译为比值域的交叉不等式，翻译工具是强归纳，归纳中m<n用超可加性、m>n用次可加性）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: ["approximate additivity", "ratio a_n/n", "cross-inequality", "strong induction", "maximizing ratio", "floor condition", "two-sided bound"]
- expected_ai_method: bare AI预期会尝试直接构造x（如x=a₁）或对n做归纳逐个确定aₙ，因为条件看起来像递推关系。不会想到研究比值aₙ/n并证明交叉不等式。
- correct_method: 研究比值aₙ/n，通过强归纳证明交叉不等式n·a_m+1≤m·a_n+m，取最大比值a_p/p作为x，用双侧夹逼验证floor条件。

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type=characterization、ai_method_type=direct_calculation、gap_type=structural_transformation都能归入已有拓扑类别。
- [x] 粒度是否一致——characterization是抽象级，direct_calculation是抽象级，structural_transformation是中等级，与已有值粒度一致。
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell。核心gap是"从加法域到比值域的结构翻译"，用structural_transformation可以表达。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。现有分类体系覆盖良好。

**拓扑进化建议**（如有）：无。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs详见profile.json**

**全局tell_hint_pairs详见profile.json**

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI预期会犯以下错误：1) 尝试直接构造x（如x=a₁），但无法验证floor条件对所有n成立；2) 尝试对n做归纳，但条件是成对的(i,j)而非单个n，归纳无法推进；3) 不会想到研究比值aₙ/n并证明交叉不等式——这个"从加法域到比值域"的翻译是关键转折点，bare AI缺乏这种结构翻译能力；4) 即使想到比值分析，也可能无法正确组织强归纳（需要区分m<n和m>n两种情况分别使用超可加性和次可加性）。
- suitable_for_poc: ["tell_extraction（tell端验证：从AI thinking中识别'没走比值分析方向'的分叉信号）", "hint_injection（hint端验证：注入'研究比值aₙ/n'的方向后AI能否完成）", "path_divergence（路径分叉验证：bare AI走直接构造/归纳路径vs正确路径走比值分析）"]
- discriminates_levels: true（这道题区分度高：能做出需要结构翻译+强归纳+极值选取三重能力，bare AI几乎不可能自发完成）

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
- [x] answer（proof类型填要证明的结论）
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
- [x] tell_hint_pairs（7个局部pair，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（2个全局pair，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象，stats中knowledge_bottleneck="R5", thinking_bottleneck="R4"为字符串类型）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**已将完整JSON写入 `profile.json` 文件**

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功
- 验证结果: [x] 通过
- 验证详情: compfiles_usa1997p6, 7 local pairs, 2 global pairs, knowledge_bottleneck=R5(str), thinking_bottleneck=R4(str), answer非None, why_not_visible_locally非None

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_usa1997p6
- solution_method_type: structural_transformation
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，现有分类体系覆盖良好。problem_type=characterization, ai_method_type=direct_calculation, gap_type=structural_transformation均可归入已有值。
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
