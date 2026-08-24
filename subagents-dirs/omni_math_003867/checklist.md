# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003867
- **文件路径**: subagents-dirs/omni_math_003867/problem.lean
- **来源**: AoPS omni_math (imo_shortlist)
- **ArangoDB progress记录_key**: 333746（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003867/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：求所有函数 f:R→R 满足 f(0)≠0 且对所有 x,y∈R，f(x+y)² = 2f(x)f(y) + max{f(x²+y²), f(x²)+f(y²)}。
- 解答核心思路（1-2句话）：先代入x=y=0确定f(0)=-1，再令y=0利用f(0)<0简化max项得到递推关系f(x²)=f(x)(f(x)+2)，通过变量替换g=f+1转化为乘性方程g(x²)=g(x)²，结合max分支分析完成唯一性证明。
- 解答关键步骤列表：
  1. 代入x=y=0：f(0)²=2f(0)²+max{f(0),2f(0)}，分析符号得f(0)=-1
  2. 令y=0：max{f(x²),f(x²)+f(0)}=max{f(x²),f(x²)-1}=f(x²)，得f(x²)=f(x)²+2f(x)=f(x)(f(x)+2)
  3. 测试常数函数f=-1和线性函数f=x-1，验证满足完整方程
  4. 设g(x)=f(x)+1，递推关系变为g(x²)=g(x)²（乘性方程）
  5. 结合max两个分支分析：f(x²+y²)≥f(x²)+f(y²)对应f=-1，反之对应f=x-1
  6. 完成唯一性证明：g只能是常数1或恒等函数x

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.3 | 观察这个函数方程的结构：f(x+y)² = 2f(x)f(y) + max{f(x²+y²), f(x²)+f(y²)}。方程中有哪些关键结构特征？f(0)≠0这个条件意味着什么？ | LHS是f(x+y)的平方，RHS有两部分：2f(x)f(y)和一个max项。max项的两个参数分别是f(x²+y²)和f(x²)+f(y²)。f(0)≠0排除了f≡0的平凡解。max项的存在意味着需要分支讨论。 |
| 2 | 自由列举 | 0.5 | 对于这类函数方程，你可以尝试哪些方向？列出所有你能想到的方法。 | 1) 代入特殊值x=y=0；2) 测试常数函数f(x)=c；3) 测试线性函数f(x)=ax+b；4) 分析max项何时取哪个分支；5) 令y=0得到关于f(x)的递推关系；6) 利用x²+y²的结构。 |
| 3 | 小尝试 | 0.4 | 先代入x=y=0，看看能得到什么约束。 | 设f(0)=a≠0。a²=2a²+max{a,2a}。若a>0，max=2a，得a²+2a=0，a=-2矛盾。若a<0，max=a，得a²+a=0，a=-1。所以f(0)=-1。 |
| 4 | 思维操作引导 | 0.6 | 你已知道f(0)=-1。现在令y=0，注意f(0)=-1<0，所以max{f(x²),f(x²)+f(0)}=max{f(x²),f(x²)-1}=f(x²)。用这个简化方程，提取递推关系。 | 令y=0：f(x)²=2f(x)f(0)+max{f(x²),f(x²)-1}=-2f(x)+f(x²)。所以f(x²)=f(x)²+2f(x)=f(x)(f(x)+2)。 |
| 5 | 推进 | 0.5 | 你得到了f(x²)=f(x)(f(x)+2)。现在测试常数函数和线性函数，利用这个递推关系筛选候选解。 | 常数f=c：c=c²+2c即c²+c=0，c=-1。线性f=ax+b：ax²+b=(ax+b)(ax+b+2)，比较系数得a=a², 2ab+2a=0, b²+b=0。解为(a=0,b=-1)→f=-1和(a=1,b=-1)→f=x-1。验证f=x-1满足完整方程。 |
| 6 | 思维操作引导 | 0.7 | 你找到两个候选解。现在需要证明唯一性。关键思路：设g(x)=f(x)+1，分析g满足什么关系。同时利用max项的两个分支来约束g的形态。 | 设g(x)=f(x)+1，则f(x)=g(x)-1。f(x²)=f(x)(f(x)+2)变为g(x²)-1=(g(x)-1)(g(x)+1)=g(x)²-1，即g(x²)=g(x)²。这是乘性方程。结合max分支分析g的结构。 |
| 7 | 能量传递引导 | 0.8 | 你已有g(x²)=g(x)²和两个候选解。完成唯一性证明：利用max两个分支分别对应两种解，g只能是常数1或恒等函数x。 | max两个分支恰好对应两种解：f(x²+y²)≥f(x²)+f(y²)时推出g≡1（f=-1），反之推出g(x)=x（f=x-1）。结合g(x²)=g(x)²和连续性/单调性约束完成唯一性。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: null
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization（求所有满足条件的函数，属于刻画型问题）
- structure_features: 含max项的函数方程，LHS为f(x+y)的平方，RHS含乘积项2f(x)f(y)和max{f(x²+y²), f(x²)+f(y²)}，条件f(0)≠0排除平凡解。max项的两个分支对应两种解。
- key_objects: ["f:R→R", "max{f(x²+y²), f(x²)+f(y²)}", "f(0)=-1", "递推关系f(x²)=f(x)(f(x)+2)", "g(x)=f(x)+1", "乘性方程g(x²)=g(x)²"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["特殊值代入确定参数", "利用已知参数简化max项", "递推关系提取", "候选函数测试与筛选", "变量替换转化方程结构", "分支分析与唯一性证明"]
- primary_pattern: 结构简化与变量替换（通过y=0代入简化max项，再通过g=f+1将递推关系转化为乘性方程）
- knowledge_required: ["函数方程基本技巧", "max/min项处理方法", "特殊值代入法", "变量替换技巧", "乘性函数方程g(x²)=g(x)²的性质"]
- key_insight: 令y=0时f(0)=-1<0使max简化为f(x²)，得到f(x²)=f(x)(f(x)+2)，再设g=f+1转化为乘性方程g(x²)=g(x)²，max的两个分支恰好对应两个解。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 含max项的函数方程（直接处理max分支困难）
- translation_to: 乘性函数方程g(x²)=g(x)²（结构清晰，易于分析解的结构）
- translation_type: structural_transformation（通过变量替换g=f+1将含max的复杂方程转化为简洁的乘性方程）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "equation_solving", gap_type: "structural_transformation"}
- tell_small_concepts: ["max项简化", "y=0代入", "递推关系f(x²)=f(x)(f(x)+2)", "变量替换g=f+1", "乘性方程g(x²)=g(x)²", "max分支对应解"]
- expected_ai_method: bare AI会尝试直接代入特殊值和测试简单函数，但可能忽略y=0代入对max项的简化作用，无法系统性地从递推关系出发完成唯一性证明
- correct_method: 先确定f(0)=-1，利用y=0简化max得到递推关系，变量替换g=f+1转化为乘性方程，结合max分支分析完成唯一性

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=characterization、ai_method_type=equation_solving、gap_type=structural_transformation均可归入已有拓扑类别
- [x] 粒度一致——标注值与已有值粒度统一
- [x] 三个维度足够区分这道题的tell和已有tell
- 拓扑进化建议：无，当前分类体系足够

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs摘要**：
| Round | tell | hint | hint_level | situation_type | topology |
|---|---|---|---|---|---|
| 1 | AI面对含max项的函数方程，尚未识别关键结构 | 观察方程结构，识别LHS平方、RHS的max项和f(0)≠0条件 | 0.3 | 纯元认知观察 | (characterization, direct_observation, structural_transformation) |
| 2 | AI已识别结构但未列举方向 | 列出所有可能方法：特殊值代入、测试简单函数、分支分析 | 0.5 | 自由列举 | (characterization, enumeration_brute_force, search_space_estimation) |
| 3 | AI列举了方向但未开始尝试 | 代入x=y=0得到f(0)的约束 | 0.4 | 小尝试 | (characterization, direct_calculation, method_problem_mismatch) |
| 4 | AI得到f(0)=-1但未利用y=0简化max项 | 令y=0，利用f(0)=-1<0简化max，得到f(x²)=f(x)(f(x)+2) | 0.6 | 思维操作引导 | (characterization, direct_manipulation, structural_transformation) |
| 5 | AI得到递推关系但未测试具体函数 | 测试常数和线性函数，利用递推关系筛选 | 0.5 | 推进 | (characterization, equation_solving, method_problem_mismatch) |
| 6 | AI找到候选解但未开始唯一性证明 | 设g(x)=f(x)+1，将递推关系转化为g(x²)=g(x)²，结合max分支分析 | 0.7 | 思维操作引导 | (characterization, algebraic_identity, method_translation) |
| 7 | AI有g关系和候选解，需要完成唯一性论证 | 利用max两个分支分别对应两种解，完成收尾 | 0.8 | 能量传递引导 | (characterization, logical_deduction, structural_transformation) |

**全局pairs摘要**：
1. path_feature型：完整解题路径的关键转折——从y=0简化max到变量替换g=f+1再到分支对应解
2. implicit型：max两个分支与两个解的对应关系（observation_point=R6）

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI可能直接尝试代入特殊值但不系统，可能忽略y=0代入对max项的简化作用（关键转折点），在找到候选解后无法完成唯一性证明——max分支与解的对应关系需要全局视角
- suitable_for_poc: ["POC-VMS-8 hint端验证", "POC-VMS-9 tell端验证", "POC-VMS-10 小概念标记分辨"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON，已写入 `subagents-dirs/omni_math_003867/profile.json`

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
- [x] answer（f(x)=-1和f(x)=x-1）
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
- [x] tell_hint_pairs（7个pair，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（2个pair，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
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
- 验证详情: 7 local pairs, 2 global pairs, answer非None, 所有global pair的why_not_visible_locally非None, per-pair拓扑存在, knowledge_bottleneck=None, thinking_bottleneck=R4

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: omni_math_003867
- solution_method_type: structural_analysis
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无，当前分类体系足够
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
