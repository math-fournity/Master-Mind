# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2003p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2003P5.lean
- **来源**: IMO 2003 P5
- **ArangoDB progress记录_key**: 329187（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2003P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Given n > 2 and reals x₁ ≤ x₂ ≤ ... ≤ xₙ, show that (∑ᵢⱼ |xᵢ - xⱼ|)² ≤ (2/3)(n² - 1) ∑ᵢⱼ (xᵢ - xⱼ)². Show that equality holds iff the sequence is an arithmetic progression.
- 解答核心思路（1-2句话）：利用平移不变性归一化使∑xᵢ=0，利用单调性将绝对差之和转化为线性形式2∑(2i+1-n)xᵢ，再对线性形式应用Cauchy-Schwarz不等式，等号条件直接给出等差数列。
- 解答关键步骤列表：
  1. 平移归一化：令yᵢ = xᵢ - m（m为均值），使∑yᵢ = 0，不等式在平移下不变
  2. 关键恒等式：对非递减序列，∑ᵢⱼ|yᵢ-yⱼ| = 2∑(2i+1-n)yᵢ（由归纳法证明，利用单调性消去绝对值）
  3. 平方差和恒等式：∑ᵢⱼ(yᵢ-yⱼ)² = 2n∑yᵢ² - 2(∑yᵢ)² = 2n∑yᵢ²（当∑yᵢ=0时）
  4. Cauchy-Schwarz应用：(∑cᵢyᵢ)² ≤ (∑cᵢ²)(∑yᵢ²)，其中cᵢ = 2i+1-n
  5. 计算系数平方和：∑(2i+1-n)² = n(n²-1)/3
  6. 组合得：(2∑cᵢyᵢ)² ≤ 4·n(n²-1)/3·∑yᵢ² = (2/3)(n²-1)·2n∑yᵢ² = (2/3)(n²-1)∑ᵢⱼ(yᵢ-yⱼ)²
  7. 等号条件：Cauchy-Schwarz等号成立 ⟺ yᵢ = t·cᵢ = t(2i+1-n) ⟺ xᵢ是i的仿射函数 ⟺ 等差数列

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
| 1 | 纯元认知观察 | 0.8 | 观察这道题的结构：给定条件是什么？要证明什么？涉及哪些数学对象？绝对值和排序条件分别扮演什么角色？ | 给定n>2个非递减实数x₁≤...≤xₙ，要证明关于双重求和的不等式：绝对差之和的平方≤常数×平方差之和，且等号当且仅当等差数列时成立。核心对象：有序实数序列、双重求和、绝对值、平方、等差数列。排序条件是处理绝对值的关键——它告诉我们|xᵢ-xⱼ|的符号。 |
| 2 | 自由列举 | 0.7 | 列出证明这个不等式的所有可能方法方向。 | 可能方向：(1)直接展开双重求和；(2)Cauchy-Schwarz不等式；(3)归纳法；(4)归一化/平移简化；(5)利用排序消去绝对值；(6)Lagrange乘数法；(7)排序不等式；(8)将绝对差之和转化为线性形式。 |
| 3 | 小尝试 | 0.4 | 试一试直接展开双重求和。∑ᵢⱼ(xᵢ-xⱼ)²能展开成什么？∑ᵢⱼ|xᵢ-xⱼ|能直接展开吗？遇到什么困难？ | 平方差之和可以展开：∑ᵢⱼ(xᵢ-xⱼ)² = 2n∑xᵢ² - 2(∑xᵢ)²。但绝对差之和∑ᵢⱼ|xᵢ-xⱼ|无法直接展开——绝对值的符号取决于i和j的大小关系，需要利用排序条件逐项消去绝对值。这是核心困难。 |
| 4 | 思维操作引导 | 0.5 | 利用序列非递减的条件消去绝对值。对i<j，|xᵢ-xⱼ|等于什么？能否将∑ᵢⱼ|xᵢ-xⱼ|表示为xᵢ的线性组合？计算每个xₖ前面的系数。 | 对i<j，|xᵢ-xⱼ|=xⱼ-xᵢ。所以∑ᵢⱼ|xᵢ-xⱼ|=2∑_{i<j}(xⱼ-xᵢ)。每个xₖ在∑_{i<j}(xⱼ-xᵢ)中：作为xⱼ出现(n-1-k)次（j=k, i<k），作为xᵢ出现k次（i=k, j>k）。系数为(n-1-k)-k = n-1-2k。用0-indexed：∑ᵢⱼ|xᵢ-xⱼ|=2∑(2i+1-n)xᵢ。 |
| 5 | 推进 | 0.6 | 现在你有了线性形式2∑cᵢxᵢ（cᵢ=2i+1-n）。不等式变为(2∑cᵢxᵢ)²≤(2/3)(n²-1)·∑ᵢⱼ(xᵢ-xⱼ)²。什么经典不等式能将线性形式的平方与平方和联系起来？需要做什么简化？ | Cauchy-Schwarz不等式：(∑cᵢxᵢ)²≤(∑cᵢ²)(∑xᵢ²)。需要简化：(1)平移归一化使∑xᵢ=0，则∑ᵢⱼ(xᵢ-xⱼ)²=2n∑xᵢ²；(2)计算∑cᵢ²=∑(2i+1-n)²=n(n²-1)/3。然后(2∑cᵢxᵢ)²≤4·n(n²-1)/3·∑xᵢ²=(2/3)(n²-1)·2n∑xᵢ²=(2/3)(n²-1)∑ᵢⱼ(xᵢ-xⱼ)²。 |
| 6 | 思维操作引导 | 0.4 | 验证∑(2i+1-n)²=n(n²-1)/3的计算，并确认平移不变性为什么成立——为什么可以假设∑xᵢ=0？ | 平移不变性：令yᵢ=xᵢ-m（m为均值），则|yᵢ-yⱼ|=|xᵢ-xⱼ|且(yᵢ-yⱼ)²=(xᵢ-xⱼ)²，不等式两边在平移下不变。计算∑(2i+1-n)²：展开(2i+1-n)²=4i²+(4-4n)i+(1-n)²，用求和公式∑i=n(n-1)/2，∑i²=n(n-1)(2n-1)/6，整理得n(n²-1)/3。 |
| 7 | 能量传递引导 | 0.7 | 最后处理等号条件。Cauchy-Schwarz的等号条件是什么？它如何给出等差数列？反过来，等差数列为什么达到等号？ | Cauchy-Schwarz等号成立⟺xᵢ=t·cᵢ=t(2i+1-n)对某个常数t。这意味着xᵢ是i的一次函数，即等差数列（公差为2t）。反过来，若xᵢ=a+di，则∑cᵢxᵢ=d·n(n²-1)/6（常数项因∑cᵢ=0而消去），可直接验证等号成立。证明完成！ |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1,R2,R5,R7）
- knowledge_rounds（思维操作引导的轮数）: 3（R4,R6,以及R5中的CS知识）
- level_sum: 0.8+0.7+0.4+0.5+0.6+0.4+0.7 = 4.1
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R4（绝对差之和的线性化恒等式是关键知识瓶颈）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R3（意识到绝对值不能直接展开，需要利用排序条件做结构转换）

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
- structure_features: 双重求和的不等式，左侧为绝对差之和的平方，右侧为平方差之和乘以常数因子；附带等号条件刻画（等差数列）；序列的排序条件是关键结构约束，使得绝对值可以被消去
- key_objects: ["非递减实数序列", "双重求和∑ᵢⱼ", "绝对差|xᵢ-xⱼ|", "平方差(xᵢ-xⱼ)²", "等差数列", "Cauchy-Schwarz不等式", "线性系数cᵢ=2i+1-n"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["结构转换——利用排序消去绝对值转为线性形式", "归一化——平移使∑xᵢ=0简化计算", "经典不等式应用——Cauchy-Schwarz连接线性形式与平方和", "等号条件分析——从CS等号条件反推序列结构", "系数计算——利用求和公式计算∑cᵢ²"]
- primary_pattern: 结构转换——利用排序条件将绝对差之和转化为线性形式，使Cauchy-Schwarz可用
- knowledge_required: ["Cauchy-Schwarz不等式及其等号条件", "绝对值消去（利用单调性）", "双重求和展开与求和公式", "平移不变性", "等差数列的等价刻画"]
- key_insight: 利用序列非递减条件将∑ᵢⱼ|xᵢ-xⱼ|转化为线性形式2∑(2i+1-n)xᵢ，从而可以用Cauchy-Schwarz一步到位

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 绝对值双重求和（含绝对值的非线性表达式）
- translation_to: 线性形式+Cauchy-Schwarz（线性组合的平方≤系数平方和×变量平方和）
- translation_type: structural_transformation（利用排序条件做结构转换，将含绝对值的表达式转化为线性表达式）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "inequality_proof", ai_method_type: "direct_calculation", gap_type: "structural_transformation"}
- tell_small_concepts: ["绝对差之和线性化", "排序消去绝对值", "Cauchy-Schwarz", "平移归一化", "等差数列等号条件", "系数平方和n(n²-1)/3"]
- expected_ai_method: bare AI会尝试直接展开双重求和或对绝对值用三角不等式放缩，但无法有效处理绝对差之和的结构
- correct_method: 利用单调性将绝对差之和转化为线性形式，再用Cauchy-Schwarz

### 6b. 反思拓扑分类

- [x] 当前拓扑分类是否够用——这道题的problem_type(inequality_proof)/ai_method_type(direct_calculation)/gap_type(structural_transformation)能归入已有的拓扑类别
- [x] 粒度是否一致——inequality_proof是中等粒度，direct_calculation是抽象粒度，structural_transformation是中等粒度，与已有值一致
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化，现有分类体系足够

**拓扑进化建议**（如有）：无

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 2 个，implicit型: 1 个

**局部tell_hint_pairs详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对含绝对值的双重求和不等式，不确定绝对值和排序条件如何配合 | 观察题目结构，识别排序条件是处理绝对值的关键 | 0.8 | 纯元认知观察 | false | {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: method_problem_mismatch} | ["绝对值双重求和", "排序条件", "等号条件刻画"] |
| 2 | AI列出多种方法但不确定哪条路有效，可能选择直接展开或归纳法 | 列出所有可能方向，包括利用排序消去绝对值和Cauchy-Schwarz | 0.7 | 自由列举 | false | {problem_type: inequality_proof, ai_method_type: enumeration_brute_force, gap_type: search_space_estimation} | ["Cauchy-Schwarz", "排序消去绝对值", "归一化", "归纳法"] |
| 3 | AI尝试直接展开发现平方差可以展开但绝对差无法直接展开，卡在绝对值上 | 试直接展开，发现绝对值是核心障碍 | 0.4 | 小尝试 | false | {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: method_problem_mismatch} | ["平方差展开", "绝对值障碍", "符号依赖排序"] |
| 4 | AI意识到需要利用排序消去绝对值但不知道如何将双重求和转化为线性形式 | 利用单调性消去绝对值，计算每个xₖ的系数得到线性组合 | 0.5 | 思维操作引导 | true | {problem_type: inequality_proof, ai_method_type: direct_manipulation, gap_type: knowledge_gap} | ["绝对差线性化", "系数计算", "单调性消去绝对值"] |
| 5 | AI得到线性形式后不确定如何与平方差之和建立不等式关系 | 用Cauchy-Schwarz连接线性形式平方与平方和，需要归一化简化 | 0.6 | 推进 | false | {problem_type: inequality_proof, ai_method_type: algebraic_identity, gap_type: method_translation} | ["Cauchy-Schwarz", "平移归一化", "线性形式到平方和"] |
| 6 | AI需要验证系数平方和的计算和确认平移不变性的合理性 | 验证∑(2i+1-n)²=n(n²-1)/3和∑xᵢ=0的平移不变性 | 0.4 | 思维操作引导 | true | {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: knowledge_gap} | ["系数平方和公式", "求和公式", "平移不变性"] |
| 7 | AI需要从Cauchy-Schwarz等号条件推导等差数列刻画 | CS等号条件给出xᵢ=t·cᵢ即等差数列，反向验证也成立 | 0.7 | 能量传递引导 | false | {problem_type: inequality_proof, ai_method_type: logical_deduction, gap_type: method_translation} | ["CS等号条件", "等差数列刻画", "仿射函数"] |

**全局tell_hint_pairs详情**：

| # | scope_type | scope | observation_point | tell | hint | hint_level | generalizability | why_not_visible_locally | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | path_feature | 从R3到R5的完整路径：绝对值障碍→线性化→CS应用 | null | 绝对差之和的线性化是整个证明的枢纽——从"绝对值无法展开"到"线性形式可用CS"的转换需要看到完整路径 | 利用排序条件将绝对差之和转为线性形式是连接两个求和的关键桥梁 | 0.5 | high——任何含绝对值的有序序列求和问题都可用此模式：先消去绝对值转线性，再用经典不等式 | 在R3只看到绝对值是障碍，在R5只看到线性形式可用CS，但"绝对值→线性形式"这个转换的必要性只有在看到两端时才能理解——局部视角下AI不知道消去绝对值后能得到什么 | {problem_type: inequality_proof, ai_method_type: direct_manipulation, gap_type: structural_transformation} | ["绝对差线性化", "排序消去绝对值", "线性形式到CS"] |
| 2 | path_feature | 从R4到R6的完整路径：线性化→归一化→系数计算 | null | 平移归一化（∑xᵢ=0）同时简化了两个求和——绝对差线性形式不受影响，平方差之和消去交叉项——这个"一石二鸟"只有在看到两个简化效果时才明显 | 先做平移归一化再分别处理两个求和，归一化同时简化了两侧 | 0.4 | high——任何平移不变的不等式都应先归一化简化 | 在R4只关注线性化绝对差，在R6只关注系数计算，但归一化"同时简化两侧"的效果只有在看到完整路径时才理解——局部视角下AI可能跳过归一化直接处理原始序列 | {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: structural_transformation} | ["平移归一化", "一石二鸟简化", "∑xᵢ=0"] |
| 3 | implicit | 整个证明的等号条件分析 | R7 | Cauchy-Schwarz的等号条件直接编码了等差数列的结构——xᵢ=t·cᵢ=t(2i+1-n)意味着xᵢ是i的仿射函数——这个蕴含关系在证明不等式本身时完全不可见 | 从CS等号条件出发反推序列结构，得到等差数列刻画 | 0.7 | medium——CS等号条件给出线性关系的模式可泛化到其他用CS证明的等号问题 | 在R5-R6只关注证明不等式成立，等号条件的分析是额外步骤——CS等号条件与"等差数列"之间的对应关系蕴含在CS的应用中，但在证明不等式的局部步骤中完全不可见 | {problem_type: inequality_proof, ai_method_type: logical_deduction, gap_type: method_translation} | ["CS等号条件", "等差数列蕴含", "仿射函数刻画"] |

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接展开双重求和或用三角不等式|a-b|≤|a|+|b|放缩，但无法利用排序条件将绝对差之和转化为精确的线性形式。即使想到Cauchy-Schwarz，也无法将含绝对值的表达式与CS的线性形式要求对接。可能卡在绝对值处理上无法突破，或给出不精确的放缩导致常数因子不匹配。
- suitable_for_poc: ["tell端验证——结构转换型tell的识别", "hint端验证——绝对值线性化hint的注入效果", "路径特征型tell的泛化验证"]
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
- [x] answer（**⚠️ 必填，不能为None**）
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

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_imo2003p5
- solution_method_type: cauchy_schwarz_with_normalization
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3（2个path_feature型，1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，现有分类体系足够覆盖
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
