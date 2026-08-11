# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1974p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1974P5.lean
- **来源**: IMO 1974 P5
- **ArangoDB progress记录_key**: 329069（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1974P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：求 S = a/(a+b+d) + b/(a+b+c) + c/(b+c+d) + d/(a+c+d) 在 a,b,c,d 为正实数时的所有可能取值。
- 解答核心思路（1-2句话）：通过分母与总和比较得下界1，通过配对放缩得上界2，再通过参数化+介值定理证明(1,2)中所有值可达。
- 解答关键步骤列表：
  1. 下界：每个分母 < a+b+c+d（缺一个正项），故每项 > 分子/(a+b+c+d)，求和 = 1，所以 S > 1
  2. 上界：配对放缩——a/(a+b+d) < a/(a+b), b/(a+b+c) < b/(a+b), c/(b+c+d) < c/(c+d), d/(a+c+d) < d/(c+d)，求和 = 1+1 = 2，所以 S < 2
  3. 可达性：取参数化 a=1, b=1-t, c=t, d=t(1-t)，定义 T(t)=S(1,1-t,t,t(1-t))，T在[0,1]上连续，T(0)=1, T(1)=2，由介值定理(1,2)中所有值都能取到
  4. 结论：取值集合为开区间 (1, 2)

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
| 1 | 纯元认知观察 | 0.8 | 观察表达式 a/(a+b+d) + b/(a+b+c) + c/(b+c+d) + d/(a+c+d)，每个分母和分子有什么关系？四个分母之间有什么共同点和差异？ | 每个分子是a,b,c,d之一，分母都是三个变量之和，但每个分母缺失的变量不同：第一项缺c，第二项缺d，第三项缺a，第四项缺b。分母都是a+b+c+d减去一个变量。 |
| 2 | 自由列举 | 0.7 | 要确定这个表达式在正实数上的取值范围，你能想到哪些可能的方向？ | 1) 取特殊值（如a=b=c=d）；2) 求偏导数找极值；3) 对每个分母做放缩比较；4) 用不等式上下界夹逼；5) 用连续性+参数化证明所有中间值可达。 |
| 3 | 小尝试 | 0.4 | 试试令a=b=c=d=1，表达式值是多少？再试试让某个变量趋于0或趋于无穷，值会怎样变化？ | a=b=c=d=1时每项=1/3，总和=4/3。当a→∞时第一项→1，其余→0，总和→1附近。当某个变量趋于0时类似。值似乎在1到2之间变化，但需要严格证明。 |
| 4 | 思维操作引导 | 0.3 | 对每一项，把分母和a+b+c+d比较——每个分母都比a+b+c+d小（因为缺了一个正项），所以每一项都比对应的分子/(a+b+c+d)大。这给出了什么下界？ | 因为a+b+d < a+b+c+d（缺c>0），所以a/(a+b+d) > a/(a+b+c+d)。同理每项都大于对应分子/(a+b+c+d)。四项求和 = (a+b+c+d)/(a+b+c+d) = 1。所以 S > 1。 |
| 5 | 思维操作引导 | 0.3 | 对于上界，尝试把分母配对：a/(a+b+d)和b/(a+b+c)的分母都包含a+b，c/(b+c+d)和d/(a+c+d)的分母都包含c+d。能否把每项的分母缩小到只剩两个变量来放缩？ | a/(a+b+d) < a/(a+b)（因为a+b+d > a+b），b/(a+b+c) < b/(a+b)，c/(b+c+d) < c/(c+d)，d/(a+c+d) < d/(c+d)。所以 S < a/(a+b)+b/(a+b)+c/(c+d)+d/(c+d) = 1+1 = 2。 |
| 6 | 推进 | 0.5 | 现在你知道S∈(1,2)。还需要证明(1,2)中每个值都能取到。能否构造一个连续参数化，让表达式从1连续变到2？ | 取a=1, b=1-t, c=t, d=t(1-t)，t∈[0,1]。定义T(t)=S(1,1-t,t,t(1-t))。T连续，T(0)=1（c=d=0退化），T(1)=2（b=d=0退化）。由介值定理，(1,2)中每个值都能取到。 |
| 7 | 能量传递引导 | 0.8 | 你已经完成了完整的证明：下界1通过分母与总和比较，上界2通过配对放缩，可达性通过参数化+介值定理。总结一下解答的结构。 | 三部分：(1) S>1：每项分母<a+b+c+d，故每项>分子/(a+b+c+d)，求和=1；(2) S<2：配对放缩至a/(a+b)+b/(a+b)+c/(c+d)+d/(c+d)=2；(3) (1,2)全部可达：参数化a=1,b=1-t,c=t,d=t(1-t)，IVT。答案为开区间(1,2)。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.8+0.7+0.4+0.3+0.3+0.5+0.8 = 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R6（介值定理+参数化构造是知识瓶颈）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R5（配对放缩的洞察是思维瓶颈）

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
- problem_type: characterization（确定表达式的取值集合——刻画所有可能值）
- structure_features: 4个分式之和，每个分母是3个正实数之和（缺失模式非对称：缺c,d,a,b），分子与缺失变量不同。需要同时证明上下界和可达性。
- key_objects: ["4变量分式和S", "分母缺失模式", "配对分组(a+b)/(c+d)", "连续参数化T(t)", "介值定理"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["结构观察（分母缺失模式）", "放缩夹逼（上下界分别估计）", "配对分组（将4项分成2对）", "连续性论证（参数化+介值定理）", "特殊值试探"]
- primary_pattern: 放缩夹逼与连续性论证（sandwich bounding + continuity argument）
- knowledge_required: ["分数大小比较（分母大则分数小）", "介值定理（连续函数在区间上取遍中间值）", "不等式放缩", "函数连续性验证", "参数化构造"]
- key_insight: 将每个分母与a+b+c+d比较得下界1，将分母配对为(a+b)和(c+d)两组得上界2，再用参数化a=1,b=1-t,c=t,d=t(1-t)配合介值定理证明(1,2)全部可达。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接计算/枚举（bare AI会尝试直接计算表达式值或枚举特殊值来确定范围）
- translation_to: 结构性放缩+连续性论证（通过分母结构比较做不等式夹逼，再通过参数化+介值定理证明可达性）
- translation_type: method_translation（从直接计算方法翻译到结构比较+连续性方法）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: ["分母缺失模式", "配对放缩", "上下界夹逼", "介值定理", "参数化构造", "连续性论证"]
- expected_ai_method: direct_calculation——bare AI会尝试直接计算表达式或枚举特殊值来确定取值范围，无法发现结构性放缩和连续性论证
- correct_method: 结构性放缩（分母与总和比较得下界，配对放缩得上界）+ 连续性参数化+介值定理证明可达性

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type(characterization)/ai_method_type(direct_calculation)/gap_type(structural_transformation)都能归入已有的拓扑类别，够用。
- [x] 粒度是否一致——characterization是已有抽象值，direct_calculation是已有抽象值，structural_transformation是已有中等粒度值，粒度一致。
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell。这道题的特殊性在于"同一问题中混合了inequality_proof（上下界）和characterization（可达性）两个problem_type"，但profile级用characterization（最终目标）即可，per-pair级别可以区分。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。已有的characterization + structural_transformation组合能准确描述这道题的拓扑。

**拓扑进化建议**（如有）：无。当前拓扑分类体系足够。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs详情**：

| qa_round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对4变量分式和，不确定如何确定取值范围，未注意到分母缺失模式 | 观察分母结构与a+b+c+d的关系，识别缺失模式 | 0.8 | 纯元认知观察 | false | {characterization, direct_calculation, method_problem_mismatch} | ["分母缺失模式","4变量分式和","取值范围"] |
| 2 | AI列出多个方向但无法判断哪个有效，搜索空间未收敛 | 放缩比较和连续性是两个关键方向 | 0.7 | 自由列举 | false | {characterization, enumeration_brute_force, search_space_estimation} | ["放缩方向","连续性参数化","特殊值试探"] |
| 3 | AI试特殊值得到4/3但无法推广到一般情况 | 特殊值给出范围内部的点，需要找边界 | 0.4 | 小尝试 | false | {characterization, direct_calculation, method_problem_mismatch} | ["a=b=c=d","4/3","边界行为"] |
| 4 | AI未注意到分母与总和a+b+c+d的比较关系，卡在下界 | 将每项分母与a+b+c+d比较，利用分母更小则分数更大 | 0.3 | 思维操作引导 | false | {inequality_proof, direct_calculation, structural_transformation} | ["分母比较","下界1","放缩"] |
| 5 | AI未发现配对放缩技巧，卡在上界 | 将分母配对为(a+b)和(c+d)两组，分别缩小分母 | 0.3 | 思维操作引导 | false | {inequality_proof, algebraic_identity, structural_transformation} | ["配对放缩","上界2","a/(a+b)","c/(c+d)"] |
| 6 | AI知道S∈(1,2)但不会构造参数化证明可达性，知识瓶颈 | 用介值定理，构造连续参数化a=1,b=1-t,c=t,d=t(1-t) | 0.5 | 推进 | true | {characterization, continuous_analytic, knowledge_gap} | ["介值定理","参数化","连续函数","T(0)=1,T(1)=2"] |
| 7 | AI完成证明但需要整理三段式结构 | 总结下界、上界、可达性三个部分 | 0.8 | 能量传递引导 | false | {characterization, logical_deduction, knowledge_gap} | ["三段式证明","下界上界可达性","开区间(1,2)"] |

**全局pairs详情**：

1. path_feature型：
- scope: 整个证明路径从"确定取值范围"到"三段式夹逼+IVT"
- observation_point: null
- tell: 证明路径需要三个不同层次的方法——不等式放缩（下界）、配对技巧（上界）、连续性论证（可达性），bare AI通常只会用一种方法试图解决整个问题
- hint: 将问题分解为三个子目标：证明S>1、证明S<2、证明(1,2)全部可达，每个子目标用不同方法
- hint_level: 0.6
- generalizability: high——"将刻画问题分解为上下界+可达性三部分"的模式可泛化到所有确定取值范围的问题
- tell_topology: {characterization, direct_calculation, structural_transformation}
- tell_small_concepts: ["三段式分解","上下界+可达性","方法组合"]

2. implicit型：
- scope: 分母缺失模式的非对称性贯穿整个证明
- observation_point: R1
- tell: 分母缺失模式是非对称的（缺c,d,a,b），这种非对称性使得配对放缩成为可能——bare AI可能认为分母模式是对称的而错过配对机会
- hint: 识别分母缺失模式的非对称性，利用a+b和c+d的配对结构
- hint_level: 0.5
- generalizability: medium——"利用非对称结构进行配对"可泛化到类似分式和问题
- why_not_visible_locally: 在局部看每一项时，缺失模式的具体排列不明显，需要同时观察四个分母才能发现配对可能性
- tell_topology: {inequality_proof, algebraic_identity, structural_transformation}
- tell_small_concepts: ["非对称缺失模式","配对结构","a+b和c+d分组"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI可能能猜到取值范围在(1,2)附近（通过特殊值试探），但大概率无法完成完整证明：1) 可能无法发现配对放缩的上界技巧；2) 可能无法构造正确的参数化来证明可达性；3) 可能只给出部分证明（如只有下界）就停止。
- suitable_for_poc: ["POC-VMS-8脉络继承验证（hint端：配对放缩+IVT提示能否引导AI完成证明）", "POC-VMS-9/10 tell端验证（识别AI在配对放缩处的分叉信号）", "方法翻译POC（从直接计算到结构比较+连续性）"]
- discriminates_levels: true——这道题需要三种不同方法的组合（放缩、配对、连续性），能区分只会单一方法的AI和能灵活切换方法的AI

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

**将完整JSON写入工作目录的 `profile.json` 文件** — 已完成

---

## Step 10: 入库ArangoDB [x]

**操作**：用exec工具执行Python脚本入库

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证输出: compfiles_imo1974p5, 7 local pairs, 2 global pairs

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_imo1974p5
- solution_method_type: bounding_and_continuity（放缩夹逼+连续性论证）
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。当前拓扑分类体系（characterization + structural_transformation等）足够描述这道题。
- 是否遇到异常: 无异常，全部步骤顺利完成。

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
