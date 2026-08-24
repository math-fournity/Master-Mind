# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2024p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2024P5.lean
- **来源**: IMO 2024 P5
- **ArangoDB progress记录_key**: 329277（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2024P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Turbo蜗牛在2024行×2023列棋盘上玩游戏。2022个隐藏怪物，每行恰好一个（除第一行和最后一行），每列最多一个。Turbo从第一行出发到最后一行，每次尝试遇到怪物被送回第一行，记住访问过的格子是否有怪物。求最小n使得Turbo有策略在第n次尝试或之前保证到达最后一行。
- 解答核心思路（1-2句话）：答案n=3。下界：2次不够（对手自适应在第二行和第三行Turbo进入的格子放怪物）。上界：第一次侦察定位第二行怪物，中间位置两侧绕行利用列约束，边缘位置用zigzag路径+对称性。
- 解答关键步骤列表：
  1. 下界证明（not_forcesWinIn_two）：对手策略——第一次尝试进入第二行的第一个格子放怪物，第二次尝试进入第三行的第一个格子放怪物（两行不同列满足约束）
  2. 第一次尝试（path0）：沿第二行水平扫描，定位第二行怪物位置c₁
  3. 中间位置策略（path1OfNotEdge + path2OfNotEdge）：c₁不在边缘时，第二次从c₁-1列向下，第三次从c₁+1列向下，利用每列最多一个怪物保证至少一次成功
  4. 左边缘策略（path1OfEdge0 + path2OfEdge0）：c₁=0时，第二次走zigzag路径，若遇怪物第三次提前转弯到第0列向下
  5. 右边缘策略（path1OfEdgeN + path2OfEdgeNDef）：c₁=N时，通过对称反射（reflect）复用左边缘策略
  6. 整合（winningStrategy_forcesWinIn_three）：三种情况覆盖所有可能，3次尝试保证成功

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
| 1 | 纯元认知观察 | 0.2 | 这道题中Turbo知道什么、不知道什么？每次尝试后Turbo获得了什么信息？棋盘的约束条件有哪些？ | Turbo知道棋盘大小(2024行2023列)、怪物总数(2022个)、每行恰好一个(除首尾行)、每列最多一个。不知道怪物具体位置。每次尝试后Turbo知道访问过的格子是否有怪物——如果遇到怪物，精确知道怪物在哪个格子。关键约束：每列最多一个怪物意味着不同行的怪物在不同列。 |
| 2 | 自由列举 | 0.4 | Turbo可以采取什么类型的策略？列出所有可能的方向来保证到达最后一行。 | 可能方向：1) 每次尝试走不同路径逐步排除怪物位置；2) 用第一次尝试专门侦察某行怪物位置；3) 利用每列最多一个怪物的约束设计绕行路径；4) 从两侧绕过已知怪物；5) 之字形路径覆盖更多区域；6) 对称性简化分析。关键是要利用每次失败获得的信息。 |
| 3 | 小尝试 | 0.3 | 如果Turbo每次都走最短路径（直接从第一行到最后一行），需要多少次尝试？这个策略有什么问题？ | 直接向下走可能每次都遇到不同行的怪物，最坏情况需要2022次（每行一个怪物逐个排除）。问题是没有利用信息——每次尝试应该利用之前获得的信息来避开已知怪物。而且没有利用"每列最多一个怪物"这个关键约束。 |
| 4 | 思维操作引导 | 0.3 | 考虑用第一次尝试专门来定位第二行的怪物。如何设计一条路径，使得在一次尝试中确定第二行怪物的确切位置？ | 从(0,0)出发走到(1,0)，然后沿第二行水平移动：(1,0)→(1,1)→(1,2)→...→(1,N)。因为第二行恰好有一个怪物，Turbo会在遇到它时被送回，从而精确知道怪物在第二行的哪个列位置c₁。这是一次"侦察"尝试，牺牲这次尝试换取精确信息。 |
| 5 | 推进 | 0.5 | 已知第二行怪物在列c₁后，如果c₁不在边缘（c₁≠0且c₁≠N），如何设计第二次和第三次尝试？利用"每列最多一个怪物"的约束。 | 第二次尝试从c₁-1列向下走（绕过第二行怪物左侧），第三次尝试从c₁+1列向下走（绕过右侧）。关键推理：第三行的怪物最多在一个列中（每列最多一个怪物），不可能同时在c₁-1和c₁+1列。因此第二次或第三次尝试至少有一次不会在第三行遇到怪物，且后续行也不会遇到（因为走的列与第二行怪物列不同，而其他行的怪物也受列约束限制）。所以至少一次成功。 |
| 6 | 思维操作引导 | 0.6 | 如果c₁=0（怪物在最左列），无法从左侧绕行。如何设计策略？考虑用zigzag（之字形）路径，使得如果遇到怪物，第三次尝试可以避开所有怪物。 | 第二次尝试走zigzag路径：之字形穿越棋盘覆盖所有列。如果第二次成功，游戏结束。如果遇到怪物在某行r的某列，第三次尝试：沿着与zigzag相同的路径走，但在到达行r之前一行的位置提前转弯到第0列，然后沿第0列向下走到最后一行。因为第0列的怪物只在第二行（已知位置c₁=0），第三次沿第0列走时只需避开第二行（从第一行直接跳到第三行或更下面），不会遇到其他怪物。c₁=N的情况由棋盘左右对称性（reflect操作）直接复用左边缘策略。 |
| 7 | 思维操作引导 | 0.5 | 现在有了上界策略（3次足够），还需要证明下界。为什么2次尝试不够？构造对手策略。 | 对手策略是自适应的：看Turbo第一次尝试的路径，在Turbo进入第二行的第一个格子放怪物（第二行有且仅有一个怪物）。Turbo被送回后，第二次尝试的路径不同，对手在Turbo进入第三行的第一个格子放怪物（第三行有且仅有一个怪物）。两个怪物在不同行不同列，满足约束。因此2次尝试无法保证到达最后一行。 |
| 8 | 能量传递引导 | 0.7 | 总结完整策略，确认n=3既是上界也是下界。 | 下界：2次不够——对手自适应在第二行和第三行Turbo进入的格子放怪物。上界：3次足够——第一次侦察定位第二行怪物c₁；若c₁在中间，第二次走c₁-1列、第三次走c₁+1列，列约束保证至少一次成功；若c₁在边缘，第二次走zigzag、第三次提前转弯到边缘列，对称性处理右边缘。因此n=3。 |

**统计**：
- total_rounds: 8
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4 (R1纯元认知观察, R2自由列举, R5推进, R8能量传递引导)
- knowledge_rounds（思维操作引导的轮数）: 3 (R4, R6, R7)
- level_sum: 0.2+0.4+0.3+0.3+0.5+0.6+0.5+0.7 = 3.5
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6" (zigzag路径设计+对称性论证是最难的知识点)
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5" (利用每列最多一个怪物约束设计两侧绕行是关键思维转折)

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
- problem_type: discrete_combinatorial
- structure_features: 网格上的路径规划博弈，信息不完全（怪物隐藏），策略需要利用失败获取的信息+约束条件（每列最多一个怪物）设计保证性策略。上下界证明结构——下界用对手自适应策略，上界用构造性策略分情况讨论。
- key_objects: ["棋盘网格(2024行×2023列)", "隐藏怪物(每行一个/每列最多一个)", "路径(相邻格子移动)", "策略(基于历史信息的自适应路径选择)", "尝试次数n(最小化)"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["信息获取优先——先牺牲一次尝试获取精确信息", "约束利用——利用每列最多一个怪物的约束设计绕行", "分情况讨论——中间位置vs边缘位置不同策略", "对称性论证——右边缘复用左边缘策略", "上下界证明——下界用对手策略+上界用构造性策略"]
- primary_pattern: 信息获取优先（先侦察再利用信息+约束设计策略）
- knowledge_required: ["网格路径规划", "组合博弈论基础", "信息论概念（信息获取与利用）", "对称性论证(reflect操作)", "对手策略构造(最坏情况分析)"]
- key_insight: 第一次尝试用于侦察第二行怪物位置，然后利用"每列最多一个怪物"约束从两侧绕行——中间位置两侧必有一侧安全，边缘位置用zigzag路径+对称性处理

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 逐次尝试排除法（每次尝试走不同路径逐步排除怪物位置，不系统利用约束）
- translation_to: 信息获取+约束利用的结构化策略（先侦察定位，再利用列约束设计绕行路径，分情况处理边缘）
- translation_type: method_translation（从朴素的逐次排除翻译到结构化的信息获取+约束利用策略）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "case_by_case", gap_type: "structural_transformation"}
- tell_small_concepts: ["信息获取策略", "每列最多一个怪物约束", "zigzag路径", "对称性论证", "上下界证明", "侦察-绕行", "边缘情况处理"]
- expected_ai_method: 逐次尝试走不同路径排除怪物位置，不系统利用"每列最多一个怪物"约束，不区分中间和边缘情况
- correct_method: 三阶段策略——第一次侦察定位第二行怪物，中间位置两侧绕行利用列约束，边缘位置zigzag+对称性，下界用对手自适应策略

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
- [x] 当前拓扑分类是否够用——这道题的problem_type(discrete_combinatorial)/ai_method_type(case_by_case)/gap_type(structural_transformation)都能归入已有的拓扑类别，够用。
- [x] 粒度是否一致——discrete_combinatorial和case_by_case都是抽象粒度，structural_transformation是中等粒度，与已有值粒度一致。
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell。problem_type区分问题领域，ai_method_type区分AI的方法倾向，gap_type区分需要跨越的认知鸿沟。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。

**拓扑进化建议**（如有）：无，当前拓扑分类足够。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 8 对
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 1 个，implicit型: 2 个

**局部tell_hint_pairs详见profile.json**

**全局tell_hint_pairs详见profile.json**

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试逐次排除怪物位置，走不同路径逐步缩小搜索空间，但不会系统利用"每列最多一个怪物"约束来设计保证性策略。具体错误：1) 不会想到用第一次尝试专门侦察第二行怪物；2) 即使定位了怪物，不会想到两侧绕行利用列约束；3) 边缘情况不会设计zigzag路径；4) 不会用对称性简化右边缘情况；5) 下界证明不会构造自适应对手策略。
- suitable_for_poc: ["hint注入验证——验证侦察策略hint能否引导AI找到正确方向", "tell识别验证——验证系统能否从AI的thinking中识别'未利用列约束'的tell", "拓扑匹配验证——验证discrete_combinatorial+case_by_case+structural_transformation拓扑能否匹配"]
- discriminates_levels: true（这道题区分度高——需要信息获取策略、约束利用、分情况讨论、对称性论证多个认知层次，bare AI几乎不可能自发完成）

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
- [x] answer（="3"，numerical类型填数值答案）
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

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_imo2024p5
- solution_method_type: constructive_strategy_with_bounds
- 局部(tell,hint)对数量: 8
- 全局(tell,hint)对数量: 3 (1个path_feature型 + 2个implicit型)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，当前拓扑分类(discrete_combinatorial + case_by_case + structural_transformation)足够覆盖
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
