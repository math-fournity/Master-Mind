# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2022p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2022P6.lean
- **来源**: IMO 2022 P6
- **ArangoDB progress记录_key**: 329267（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2022P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设n为正整数。Nordic square是一个n×n棋盘，包含1到n²的所有整数，每格一个。两格相邻当且仅当共享一条边。谷（valley）是所有相邻格中数字都更大的格子。上坡路径（uphill path）是一个格子序列：(1)首格是谷，(2)每格与前格相邻，(3)序列中数字递增。求Nordic square中最少可能的上坡路径总数（作为n的函数）。
- 解答核心思路（1-2句话）：答案是2n(n-1)+1。下界通过注入证明：每个相邻格对（gap）确定至少一条上坡路径，加上从全局最小值出发的平凡路径，共2n(n-1)+1个。上界通过构造一个"好"的Nordic square达到此下界。
- 解答关键步骤列表：
  1. 下界：构造从(gaps ∪ {trivial})到uphill paths的注入。每个gap（相邻格对）确定一条上坡路径（从谷经过较小值格到较大值格），加上从值1的格（必为谷）出发的单格路径。gaps数量=2n(n-1)（水平n(n-1)+垂直n(n-1)），加1=2n(n-1)+1。
  2. 上界构造：定义"好"Nordic square——恰好一个谷、每个非谷非丘格恰好有一个更小邻居、丘两两不相邻。在好的square中，非丘格恰好1条路径到达，丘格的路径数=度数，总和=2n(n-1)+1。
  3. 计数定理（good_count）：路径总数=Σ(每格的路径数)=Σ(非丘格1 + 丘格度数)。利用"更小邻居"入射总数=2n(n-1)（=gaps数），减去谷的贡献0，得到丘格度数之和=2n(n-1)-（非谷非丘格数），最终路径数=2n(n-1)+1。
  4. 构造实现：用strip-based模式构造key函数，tree cells先排列（形成以(0,0)为根的生成树），hill cells后排列。验证满足Good条件。
  5. answer = 2*n^2 - 2*n + 1 = 2*n*(n-1) + 1。

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 请描述这道题的结构：我们在求什么？什么是上坡路径？上坡路径由什么决定？已知条件和未知量之间的关系是什么？ | 我们在求n×n棋盘上上坡路径总数的最小值。上坡路径从谷（局部最小）出发，沿相邻格递增行进。路径由起点（谷）和每步的选择决定。未知量是路径总数的下确界。关键关系：路径数取决于棋盘上数字的排列方式。 |
| 2 | 自由列举 | 0.7 | 列出所有可能用来估计上坡路径数量的方法或思路。不要筛选，尽可能多列。 | 1)对小n枚举所有排列找最小值；2)直接计数路径；3)找路径的必要条件建立下界；4)构造特殊排列使路径最少；5)分析路径与棋盘结构（边、度数）的关系；6)用图论模型（有向图、树）；7)用双射/注入将路径映射到其他可数对象；8)分析谷的数量和位置对路径数的影响。 |
| 3 | 小尝试 | 0.5 | 试n=1和n=2的情况。n=1时最少路径数是多少？n=2时呢？尝试找出规律。 | n=1：只有1个格子，它是谷，只有1条路径（自身），答案=1。n=2：4个格子，排列1-4。尝试几种排列发现最少5条路径。1和5对应2n(n-1)+1：n=1时2*1*0+1=1，n=2时2*2*1+1=5。猜测答案=2n(n-1)+1。但还不理解为什么。 |
| 4 | 思维操作引导 | 0.4 | 思考：每条长度≥2的上坡路径的最后一步是什么？它是一条边（相邻格对）。那么每条边能确定至少一条上坡路径吗？尝试构造这个映射。 | 每条长度≥2的上坡路径的最后一步是一条边(a,b)，其中ns(a)<ns(b)。反过来，给定一条边(a,b)且ns(a)<ns(b)，可以从a出发沿递减方向回溯到某个谷（每步选更小邻居），再正向走到b，得到一条上坡路径。但回溯路径可能不唯一——如果a有多个更小邻居。不过至少存在一条。加上从全局最小值（值1的格，必为谷）出发的单格路径，得到至少(边数+1)条路径。n×n棋盘有2n(n-1)条边，所以下界≥2n(n-1)+1。 |
| 5 | 思维操作引导 | 0.3 | 关键验证：上面的回溯为什么总能到达一个谷？这个映射为什么是注入（不同边/平凡路径对应不同上坡路径）？ | 回溯一定能到达谷：因为值严格递减且有限，最终到达没有更小邻居的格即谷。注入性：每条长度≥2的上坡路径的最后两个格确定一条边，而最后两格的值序确定边的方向。不同边给出不同的最后两格，所以路径不同。平凡路径（单格）长度为1，与长度≥2的路径不同。所以(gaps ∪ {trivial})→uphill paths是注入，下界2n(n-1)+1成立。 |
| 6 | 推进 | 0.4 | 现在需要构造达到下界的Nordic square。什么样的排列能让每条边恰好确定一条上坡路径？这需要什么结构条件？ | 需要每个非谷格恰好有一个更小邻居（这样回溯唯一），形成以谷为根的生成树。谷恰好一个（全局最小值）。局部最大值（丘）可以有多个更小邻居，但丘两两不相邻（避免额外路径）。这种"好"square中：非丘格恰好1条路径到达，丘格的路径数=度数（每个邻居给出一条路径）。路径总数=Σ(非丘格1)+Σ(丘格度数)=2n(n-1)+1。 |
| 7 | 能量传递引导 | 0.6 | 总结：答案是什么？为什么下界和上界匹配？这个问题的关键洞察是什么？ | 答案=2n(n-1)+1=2n²-2n+1。下界：每条边确定至少一条上坡路径（注入），加平凡路径。上界：构造"好"square（生成树结构+非相邻丘），使注入变双射。关键洞察：将"数路径"问题转化为"数边"问题——每条边对应至少一条路径，这是组合优化中经典的注入下界技巧。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.8+0.7+0.5+0.4+0.3+0.4+0.6=3.7
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: discrete_combinatorial
- structure_features: n×n棋盘上的排列优化问题，求上坡路径总数的最小值。核心结构是"路径"与"边"之间的双射/注入关系。路径由起点（谷）和递增序列决定，边由相邻格对决定。
- key_objects: Nordic square（n×n排列）、valley（谷/局部最小）、uphill path（上坡路径）、gap（相邻格对/边）、hill（丘/局部最大）、生成树结构

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["注入下界（injection lower bound）", "结构-计数转化（将路径计数转化为边计数）", "构造匹配上界（constructive upper bound）", "生成树模型（spanning tree model）", "分类计数（按终点格分类计数路径）"]
- primary_pattern: 注入下界——将"数路径"问题转化为"数边"问题，用注入建立下界，再构造使注入变双射的实例
- knowledge_required: ["图论基本概念（边、度数、生成树）", "注入/双射的概念", "组合优化中的下界-上界匹配方法", "棋盘图的结构（n×n网格的边数=2n(n-1)）", "良基递归（回溯到谷的终止性）"]
- key_insight: 每条边（相邻格对）确定至少一条上坡路径——将路径计数问题转化为边计数问题，下界=边数+1=2n(n-1)+1

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 路径计数（直接枚举/估计上坡路径数量）
- translation_to: 边计数+注入论证（将路径映射到边，用边数建立下界）
- translation_type: 结构转化型（structural_transformation）——将一个对象的计数问题转化为另一个更易计数的对象的计数问题，通过注入建立不等关系

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "structural_transformation"}
- tell_small_concepts: ["上坡路径", "谷", "边/gap", "注入", "生成树", "局部最小/最大", "回溯到谷", "边数=2n(n-1)", "平凡路径"]
- expected_ai_method: bare AI会尝试直接计数路径或枚举小case猜规律，不会想到用注入将路径映射到边
- correct_method: 构造从(gaps ∪ {trivial})到uphill paths的注入建立下界，再构造"好"square（生成树结构）匹配上界

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=discrete_combinatorial、ai_method_type=enumeration_brute_force、gap_type=structural_transformation都能归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 不需要新的拓扑维度——三个维度足够区分这道题的tell
- [ ] 无需进化建议

**拓扑进化建议**（如有）：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs**：

| qa_round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI描述了题目结构但未识别"路径与边"的关系，只看到路径由起点和选择决定 | 描述题目结构，识别已知/未知，注意路径的组成部分 | 0.8 | 纯元认知观察 | false | {problem_type: "discrete_combinatorial", ai_method_type: "direct_calculation", gap_type: "method_problem_mismatch"} | ["上坡路径", "谷", "已知/未知"] |
| 2 | AI列出了多种方法但未突出"注入/双射"方向，列举分散 | 列出所有可能方向，包括将路径映射到其他可数对象 | 0.7 | 自由列举 | false | {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "search_space_estimation"} | ["枚举", "双射", "图论模型", "边度数"] |
| 3 | AI试了小case猜出2n(n-1)+1但不理解为什么，停留在模式猜测 | 试n=1和n=2，找规律但不要停留在猜测 | 0.5 | 小尝试 | false | {problem_type: "discrete_combinatorial", ai_method_type: "case_by_case", gap_type: "search_space_estimation"} | ["小case", "n=1", "n=2", "模式猜测"] |
| 4 | AI未注意到每条路径的最后一步是边，未建立边到路径的映射 | 思考路径的最后一步是什么，每条边能否确定一条路径 | 0.4 | 思维操作引导 | false | {problem_type: "discrete_combinatorial", ai_method_type: "direct_manipulation", gap_type: "structural_transformation"} | ["最后一步", "边/gap", "回溯到谷", "边数"] |
| 5 | AI理解了映射思路但未验证注入性和回溯终止性 | 验证回溯为何到达谷，映射为何是注入 | 0.3 | 思维操作引导 | true | {problem_type: "discrete_combinatorial", ai_method_type: "logical_deduction", gap_type: "knowledge_gap"} | ["注入性", "良基递归", "回溯终止", "值严格递减"] |
| 6 | AI有下界但不知道如何构造匹配上界的square | 构造"好"square：生成树结构+非相邻丘 | 0.4 | 推进 | false | {problem_type: "discrete_combinatorial", ai_method_type: "direct_manipulation", gap_type: "method_translation"} | ["生成树", "好square", "丘不相邻", "唯一更小邻居"] |
| 7 | AI已完成证明但需要总结关键洞察 | 总结答案和关键洞察，确认下界上界匹配 | 0.6 | 能量传递引导 | false | {problem_type: "discrete_combinatorial", ai_method_type: "logical_deduction", gap_type: "method_problem_mismatch"} | ["下界上界匹配", "注入变双射", "路径↔边"] |

**全局tell_hint_pairs**：

1. path_feature型：
   - scope: 整个证明路径（从R1到R7）
   - observation_point: null
   - tell: 整个解题路径的核心特征是"将路径计数转化为边计数"——这个转化在局部步骤中不可见，需要看到完整路径才能识别
   - hint: 将"数路径"问题转化为"数边"问题，用注入建立下界，再构造使注入变双射的实例
   - hint_level: 0.5
   - generalizability: "high——注入下界是组合优化中的通用技巧，适用于任何'求某结构最小数量'的问题"
   - why_not_visible_locally: "在局部视角中，AI看到的是'描述结构'、'列举方法'、'试小case'等具体操作，无法看到这些操作共同指向的'路径↔边'转化。只有看到从R4（发现边确定路径）到R5（验证注入）到R6（构造匹配）的完整链条，才能识别出这个转化是整个证明的核心特征。局部步骤中的每个操作看起来都是独立的，转化关系是跨步骤的。"
   - tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "structural_transformation"}
   - tell_small_concepts: ["路径↔边转化", "注入下界", "下界上界匹配", "完整证明链条"]

2. implicit型：
   - scope: R4-R6之间的蕴含关系
   - observation_point: "R5"
   - tell: 下界的注入论证蕴含了上界构造的条件——注入变双射要求每个非谷格恰好一个更小邻居（生成树），这个蕴含在局部验证注入性时不可见
   - hint: 从注入的紧性条件推导构造要求：注入变双射需要回溯唯一（生成树结构）+平凡路径唯一（单一谷）
   - hint_level: 0.4
   - generalizability: "medium——'注入紧性蕴含构造条件'的思路适用于注入下界方法，但具体构造（strip-based生成树）是本题特有的"
   - why_not_visible_locally: "在R5验证注入性时，AI关注的是'回溯能到达谷'和'不同边给不同路径'，不会注意到'回溯唯一'这个使注入变双射的额外条件。这个蕴含关系需要从下界论证反推上界构造时才显现——它是注入论证的'紧性条件'，在局部验证步骤中被跳过了。"
   - tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "logical_deduction", gap_type: "method_translation"}
   - tell_small_concepts: ["注入紧性", "回溯唯一", "生成树条件", "双射要求"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试枚举小case猜出公式2n(n-1)+1，但无法证明下界（想不到注入论证）和上界（想不到生成树构造）。可能停留在"猜测答案但无法证明"的状态，或者尝试错误的计数方法（如直接计算路径数公式）导致无法闭合。
- suitable_for_poc: ["tell端验证——测试系统能否从AI thinking中识别'未注意到边-路径关系'的分叉信号", "hint端验证——测试注入'思考最后一步是边'的提示能否引导AI走向正确方向", "拓扑匹配验证——测试discrete_combinatorial+structural_transformation拓扑的tell能否被形式化过滤命中"]
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
- [x] answer（"2n(n-1)+1 = 2n^2 - 2n + 1"）
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
- [x] tell_hint_pairs（7个，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（2个，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象，stats中knowledge_bottleneck="R5"、thinking_bottleneck="R4"为字符串）
- [x] analysis_metadata

**将完整JSON写入工作目录的 `profile.json` 文件** ✅

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_imo2022p6
- solution_method_type: injection_lower_bound_and_constructive_upper_bound
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，已有拓扑分类（discrete_combinatorial + enumeration_brute_force + structural_transformation）足够覆盖
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
