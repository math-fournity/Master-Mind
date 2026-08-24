# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2019p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2019P6.lean
- **来源**: USA 2019 P6
- **ArangoDB progress记录_key**: 329483（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2019P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Find all polynomials P with real coefficients such that P(x)/yz + P(y)/zx + P(z)/xy = P(x−y) + P(y−z) + P(z−x) for all nonzero real numbers x, y, z obeying 2xyz = x + y + z.
- 解答核心思路（1-2句话）：答案为 P = c·(x² + 3)。通过通分将函数方程转化为约束曲面上的多项式恒等式，参数化曲面后用维度论证（二元多项式在无穷多点上为零则恒为零）得到PhiPoly=0，由此推出P为偶函数；再通过复数延拓和二阶差分将度数限制到≤2，最后用特殊代入确定系数关系a=3b。
- 解答关键步骤列表：
  1. 通分：乘以xyz得Qfun P x y z = xP(x)+yP(y)+zP(z)−xyz(P(x−y)+P(y−z)+P(z−x)) = 0在曲面2xyz=x+y+z上
  2. 参数化曲面：z = (x+y)/(2xy−1)，构造二元多项式PhiPoly，其在2xy≠1的所有(x,y)上为零
  3. 维度论证：PhiPoly在无穷多个点上为零→PhiPoly = 0（一元多项式有无穷多根则恒为零，逐系数应用）
  4. 推出P为偶函数：从PhiPoly=0取y=0得Qfun P t 0 (−t) = 0，推出t(P(t)−P(−t))=0，故P(−x)=P(x)
  5. 复数延拓+二阶差分：取h²=−1/2的复数h，在曲面点(x, h, −h)上评估，得二阶差分关系Pc(X+h)+Pc(X−h)−2Pc = 常数，比较首项系数k(k−1)h²≠0迫使deg P ≤ 2
  6. 确定系数：偶函数+度数≤2→P = a+bx²，代入(1,1,2)得a = 3b，故P = b(x²+3)

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 请描述这道题的结构：已知条件是什么？未知对象是什么？约束条件2xyz=x+y+z在几何上代表什么？ | 题目要求找所有实系数多项式P使得对约束曲面2xyz=x+y+z上的所有非零(x,y,z)满足P(x)/yz+P(y)/zx+P(z)/xy=P(x−y)+P(y−z)+P(z−x)。约束2xyz=x+y+z定义了一个2维曲面（3个变量1个约束），方程左边有分母yz/zx/xy，右边是平移后的多项式值。 |
| 2 | 自由列举 | 0.7 | 列出你可能用来处理这道题的所有方法方向，包括代数操作、特殊代入、度数分析等。 | 可能方向：①直接特殊代入(如(1,1,2))获取系数约束；②通分消去分母转化为多项式恒等式；③参数化约束曲面z=(x+y)/(2xy−1)；④利用对称性分析P的奇偶性；⑤度数分析——假设P是n次然后比较最高次项；⑥利用曲面的参数化做维度论证。 |
| 3 | 小尝试 | 0.4 | 试一下直接代入特殊值(1,1,2)，它满足2xyz=x+y+z吗？能得到什么约束？这足够确定P吗？ | (1,1,2)满足2·1·1·2=4=1+1+2。代入得P(1)/2+P(1)/2+P(2)/1=P(0)+P(−1)+P(1)，即P(1)+P(2)=P(0)+P(−1)+P(1)，化简P(2)=P(0)+P(−1)。这只是一个约束，远不足以确定P的所有系数。需要更强的结构论证。 |
| 4 | 思维操作引导 | 0.3 | 将方程两边乘以xyz进行通分，得到一个在曲面2xyz=x+y+z上成立的多项式恒等式Qfun=0。写出Qfun的具体形式。 | Qfun P x y z = xP(x)+yP(y)+zP(z)−xyz(P(x−y)+P(y−z)+P(z−x))=0对所有满足2xyz=x+y+z的非零(x,y,z)成立。这是一个多项式在2维曲面上的恒等式。 |
| 5 | 思维操作引导 | 0.2 | 参数化曲面：令z=(x+y)/(2xy−1)（当2xy≠1），将Qfun乘以(2xy−1)^(n+1)消去分母得到二元多项式PhiPoly(x,y)。PhiPoly在无穷多个(x,y)上为零，利用"一元多项式有无穷多根则恒为零"的论证推出PhiPoly≡0。 | 将z=(x+y)/(2xy−1)代入Qfun，乘以(2xy−1)^(n+1)消去分母得PhiPoly(x,y)。对每个固定的x≠0，PhiPoly作为y的多项式在无穷多个y上为零（排除有限个例外点），故恒为零；再对每个系数作为x的多项式同样论证，得PhiPoly≡0。 |
| 6 | 推进 | 0.3 | 从PhiPoly≡0出发：(a)取y=0推出P是偶函数；(b)将P延拓到复数，取h²=−1/2的复数h，在曲面点(x,h,−h)上评估Qfun，得到二阶差分关系Pc(X+h)+Pc(X−h)−2Pc=常数，比较首项系数k(k−1)h²≠0推出deg P≤2。 | (a) y=0时z=(x+0)/(−1)=−x，Qfun P x 0 (−x)=x(P(x)−P(−x))=0对所有x成立，故P为偶函数。(b)取h²=−1/2，则2x·h·(−h)=−2xh²=x=x+h+(−h)，故(x,h,−h)在曲面上。Qfun=0给出Pc(x+h)+Pc(x−h)−2Pc(x)=常数。二阶差分(X+h)^k+(X−h)^k−2X^k的度数≤k−2且k−2次项系数为k(k−1)h²≠0，若deg P=n>2则n−2次项系数为P的n次系数·n(n−1)h²≠0，矛盾。故deg P≤2。 |
| 7 | 能量传递引导 | 0.2 | 现在已知P是偶函数且deg P≤2，所以P=a+bx²。代入(1,1,2)确定a和b的关系，写出最终答案。 | P=a+bx²，代入(1,1,2)：P(1)/2+P(1)/2+P(2)=P(0)+P(−1)+P(1)，即(a+b)+(a+4b)=(a)+(a+b)+(a+b)，化简得a+4b=2a+2b，故a=2b... 重新计算：(a+b)+(a+4b)=a+(a+b)+(a+b)→2a+5b=3a+2b→3b=a，即a=3b。故P=b(x²+3)，验证通过。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.8+0.7+0.4+0.3+0.2+0.3+0.2 = 2.9
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: 函数方程在约束曲面2xyz=x+y+z上成立，需参数化曲面并用维度论证将曲面上的恒等式转化为多项式恒为零；再通过复数延拓和二阶差分做度数限制
- key_objects: ["实系数多项式P", "约束曲面2xyz=x+y+z", "通分后的多项式Qfun", "二元多项式PhiPoly", "二阶差分(X+h)^k+(X-h)^k-2X^k", "复数h满足h²=−1/2"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["constraint_surface_parametrization", "dimension_argument_infinite_roots", "denominator_clearing", "complex_extension", "finite_difference_degree_bound", "specialization_coefficient_determination"]
- primary_pattern: constraint_surface_parametrization
- knowledge_required: ["多项式恒等式与无穷多根", "约束曲面的参数化", "二元多项式逐系数维度论证", "二阶差分的度数与首项系数", "复数延拓技术", "多项式函数方程"]
- key_insight: 约束2xyz=x+y+z定义的2维曲面可参数化为z=(x+y)/(2xy−1)，通分后得到在曲面上恒为零的多项式，用维度论证推出恒为零；再延拓到复数取h²=−1/2使(x,h,−h)落在曲面上，二阶差分关系迫使deg P≤2

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 约束曲面上的函数方程（带分母的三元多项式方程在2xyz=x+y+z上成立）
- translation_to: 二元多项式恒为零的维度论证 + 复数域上的二阶差分度数分析
- translation_type: structural_transformation（从曲面上的函数方程翻译为多项式恒等式，再翻译为度数限制）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "direct_calculation", gap_type: "structural_transformation"}
- tell_small_concepts: ["constraint_surface", "denominator_clearing", "surface_parametrization", "dimension_argument", "infinite_roots", "even_polynomial", "complex_extension", "finite_difference", "degree_bound", "coefficient_determination"]
- expected_ai_method: bare AI会尝试直接特殊代入和系数匹配，获取一些约束但无法确定所有系数；不会想到参数化曲面和维度论证
- correct_method: 通分→参数化曲面→维度论证得PhiPoly=0→偶函数→复数延拓+二阶差分得度数≤2→特殊代入确定系数

### 6b. 反思拓扑分类

- [x] 当前拓扑分类是否够用——这道题的problem_type(characterization)/ai_method_type(direct_calculation)/gap_type(structural_transformation)均可归入已有拓扑类别
- [x] 粒度是否一致——标注值和已有值粒度统一
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化

**拓扑进化建议**（如有）：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs明细**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到函数方程和约束条件但未识别约束曲面的2维结构 | 描述题目结构：约束2xyz=x+y+z定义2维曲面，方程有分母需通分 | 0.8 | 纯元认知观察 | false | {characterization, direct_calculation, method_problem_mismatch} | ["constraint_surface", "polynomial_identity", "functional_equation"] |
| 2 | AI列出方向但未优先考虑曲面参数化和维度论证 | 列出所有方向包括通分、参数化曲面、度数分析 | 0.7 | 自由列举 | false | {characterization, enumeration_brute_force, search_space_estimation} | ["denominator_clearing", "surface_parametrization", "degree_analysis"] |
| 3 | AI尝试特殊代入但得到约束不足，未意识到需要结构论证 | 试(1,1,2)得P(2)=P(0)+P(−1)，一个约束不够 | 0.4 | 小尝试 | false | {characterization, direct_calculation, method_problem_mismatch} | ["specific_substitution", "insufficient_constraints", "coefficient_relation"] |
| 4 | AI未看到通分可将函数方程转化为曲面上的多项式恒等式 | 乘xyz通分得Qfun=0在曲面上 | 0.3 | 思维操作引导 | false | {characterization, direct_manipulation, knowledge_gap} | ["denominator_clearing", "polynomial_identity", "surface_vanishing"] |
| 5 | AI未看到参数化曲面+维度论证可推出PhiPoly≡0 | 参数化z=(x+y)/(2xy−1)，构造PhiPoly，无穷多根→恒为零 | 0.2 | 思维操作引导 | true | {characterization, direct_calculation, structural_transformation} | ["surface_parametrization", "bivariate_polynomial", "infinite_roots", "dimension_argument"] |
| 6 | AI有PhiPoly=0但未看到如何通过复数延拓+二阶差分限制度数 | 取y=0得偶函数，延拓到ℂ取h²=−1/2，二阶差分迫使deg≤2 | 0.3 | 推进 | false | {characterization, algebraic_identity, method_translation} | ["even_polynomial", "complex_evaluation", "finite_difference", "degree_bound"] |
| 7 | AI有偶函数+度数≤2但未完成系数确定 | 写P=a+bx²，代入(1,1,2)得a=3b，P=c(x²+3) | 0.2 | 能量传递引导 | false | {characterization, direct_calculation, method_problem_mismatch} | ["coefficient_determination", "final_substitution", "solution_form"] |

**全局tell_hint_pairs明细**：

1. path_feature型：
- scope: "full solution path"
- observation_point: null
- tell: "完整解答需要多步管线：通分→参数化曲面→维度论证→偶函数→复数二阶差分→度数限制→系数确定"
- hint: "关键洞察是约束2xyz=x+y+z定义2维曲面，参数化后多项式在曲面上恒为零则恒为零；复数延拓取h²=−1/2使(x,h,−h)落在曲面上，二阶差分限制度数"
- hint_level: 0.8
- generalizability: "high - 曲面参数化和维度论证技术可推广到约束曲面上的多项式恒等式问题"
- why_not_visible_locally: "每个局部步骤（通分、参数化、特殊代入）看起来是孤立的代数操作。全局策略——利用2维曲面结构迫使多项式恒等式，以及选择h²=−1/2做复数延拓使二阶差分关系成立——只有从完整路径才能看到。没有任何单步能揭示曲面参数化最终会通过复数有限差分导出度数限制。"
- tell_topology: {characterization, structural_transformation, method_translation}
- tell_small_concepts: ["surface_parametrization", "dimension_argument", "complex_finite_difference", "degree_bound"]

2. implicit型：
- scope: "degree bound step"
- observation_point: "R6"
- tell: "二阶差分(X+h)^k+(X−h)^k−2X^k在k−2次的系数为k(k−1)h²。选择h²=−1/2使曲面点(x,h,−h)满足约束，同时使该系数非零，从而迫使deg P≤2"
- hint: "延拓到复数域取h²=−1/2。曲面点(x,h,−h)满足2x·h·(−h)=x+h+(−h)当且仅当h²=−1/2。这个特殊评估将函数方程转化为二阶差分关系"
- hint_level: 0.3
- generalizability: "medium - 复数延拓技术通用，但h²=−1/2的具体选择是问题特化的"
- why_not_visible_locally: "从局部步骤看，h²=−1/2的选择没有动机——它看起来像魔法常数。只有全局视角才能揭示h²=−1/2恰好是使(x,h,−h)落在约束曲面上同时使二阶差分首项系数k(k−1)h²非零的值。"
- tell_topology: {characterization, algebraic_identity, method_translation}
- tell_small_concepts: ["complex_evaluation", "finite_difference", "constraint_satisfaction", "degree_bound"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "Bare AI会尝试直接特殊代入和系数匹配，获取一些约束（如P(2)=P(0)+P(−1)）但无法确定所有系数。不会想到参数化约束曲面和维度论证来获得PhiPoly=0，也不会想到延拓到复数域用二阶差分限制度数。最终可能猜测P是低次多项式但无法严格证明度数限制。"
- suitable_for_poc: ["tell_extraction", "hint_injection", "topology_classification", "path_feature_detection"]
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

**将完整JSON写入工作目录的 `profile.json` 文件**：已完成

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证输出: 验证通过: compfiles_usa2019p6, 7 local pairs, 2 global pairs

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_usa2019p6
- solution_method_type: structural_transformation
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，已有拓扑分类足够覆盖
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
