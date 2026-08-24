# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000256
- **文件路径**: subagents-dirs/fate_000256/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396366（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000256/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Prove that if #G = 1785 then G is not simple. （证明如果群G的阶为1785，则G不是单群）
- 解答核心思路（1-2句话）：利用Sylow定理分析1785=3×5×7×17的Sylow子群数量，通过正规化子链论证证明存在正规子群。关键在于Sylow 17-子群的正规化子是循环群（阶51），迫使它包含Sylow 3-子群，进而导出矛盾。
- 解答关键步骤列表：
  1. 分解 1785 = 3 × 5 × 7 × 17
  2. 由Sylow定理，n_17 | 105 且 n_17 ≡ 1 (mod 17)，得 n_17 ∈ {1, 35}
  3. 若 n_17 = 1，Sylow 17-子群正规，G非单群，完成
  4. 若 n_17 = 35，则 |N_G(P_17)| = 51 = 3 × 17。因 3 ∤ 16，阶51的群是循环群
  5. N_G(P_17) 循环⇒交换⇒包含并中心化G的某个Sylow 3-子群Q ⇒ N_G(P_17) ≤ N_G(Q)
  6. |N_G(Q)| ≥ 51 ⇒ n_3 ≤ 35。由Sylow约束 n_3 ∈ {1, 7, 85, 595}，故 n_3 ∈ {1, 7}
  7. 若 n_3 = 1，Sylow 3-子群正规，完成
  8. 若 n_3 = 7，则 |N_G(Q)| = 255 = 3 × 5 × 17。在N_G(Q)中，n_17 | 15 且 n_17 ≡ 1 (mod 17)，只有n_17=1，故Sylow 17-子群P'在N_G(Q)中正规
  9. N_G(Q) ≤ N_G(P') ⇒ |N_G(P')| ≥ 255 > 51 = |N_G(P')|（因n_17=35），矛盾
  10. 因此G不是单群

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
| 1 | 纯元认知观察 | 0.3 | 描述这道题的结构：你已知什么？要证明什么？1785有什么特殊结构？ | 已知有限群G的阶\|G\|=1785=3×5×7×17，要证明G不是单群（即存在非平凡正规子群）。1785是四个不同素数的乘积。 |
| 2 | 自由列举 | 0.5 | 列出你所知道的所有证明群非单群的方法 | Sylow定理（证明某个Sylow子群正规）、元素计数法（元素太多放不下）、群作用（嵌入对称群导出矛盾）、正规化子论证、Burnside p^a q^b定理（不适用，因为有4个素因子）…… |
| 3 | 小尝试 | 0.4 | 试试元素计数法：假设没有Sylow子群正规，计算各阶元素总数 | n_17=35→560个17阶元素；n_7≥15→90个7阶元素；n_5≥21→84个5阶元素；n_3≥7→14个3阶元素。总计748+1=749<1785。计数法不够，无法直接导出矛盾。 |
| 4 | 思维操作引导 | 0.6 | 计数法失败了。现在看Sylow 17-子群的正规化子：若n_17=35，它的阶是多少？这个阶的群有什么特殊结构？ | \|N_G(P_17)\|=1785/35=51=3×17。因为3不整除17-1=16，所以阶51的群是循环群Z_51。这意味着N_G(P_17)是交换群。 |
| 5 | 思维操作引导 | 0.7 | N_G(P_17)是交换群且包含一个Sylow 3-子群Q。这告诉你关于N_G(Q)的什么信息？ | 因为N_G(P_17)交换，它正规化Q，所以N_G(P_17)≤N_G(Q)。因此\|N_G(Q)\|≥51，即n_3≤35。结合Sylow约束n_3∈{1,7,85,595}，得n_3∈{1,7}。 |
| 6 | 推进 | 0.7 | 若n_3=7，分析N_G(Q)（阶255=3×5×17）中的Sylow 17-子群。能导出什么矛盾？ | 在N_G(Q)中，n_17\|15且n_17≡1(mod 17)，只有n_17=1，故Sylow 17-子群P'在N_G(Q)中正规。所以N_G(Q)≤N_G(P')，\|N_G(P')\|≥255。但\|N_G(P')\|=1785/35=51，255>51，矛盾！ |
| 7 | 能量传递引导 | 0.4 | 完整总结这个证明 | 1785=3×5×7×17。n_17∈{1,35}：若1则完成；若35，\|N_G(P_17)\|=51循环⇒包含Sylow 3-子群Q⇒n_3∈{1,7}：若1则完成；若7，\|N_G(Q)\|=255中有正规Sylow 17-子群⇒\|N_G(P')\|≥255>51矛盾。故G非单群。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1+R2+R6+R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4+R5）
- level_sum: 0.3+0.5+0.4+0.6+0.7+0.7+0.4=3.6
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

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
- structure_features: 证明阶为1785=3×5×7×17的有限群不是单群。需要通过Sylow定理分析各Sylow子群数量，利用正规化子的结构性质（循环性⇒交换性⇒包含关系）构建矛盾链。核心结构是"素因子间的互不整除关系驱动正规化子结构"。
- key_objects: ["有限群G", "Sylow 17-子群P_17", "Sylow 3-子群Q", "正规化子N_G(P_17)", "正规化子N_G(Q)", "阶1785=3×5×7×17", "循环群Z_51"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["Sylow计数分析", "元素计数法（失败尝试）", "正规化子结构分析", "正规化子链论证", "反证法", "分情况讨论"]
- primary_pattern: 正规化子链论证
- knowledge_required: ["Sylow定理", "单群定义", "正规化子", "阶pq群的分类（p∤(q-1)⇒循环）", "Sylow子群的共轭性", "正规化子的包含关系"]
- key_insight: 阶51=3×17的正规化子是循环群（因为3不整除16），这意味着它交换地包含Sylow 3-子群，从而迫使正规化子包含关系链最终导出矛盾

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 逐个Sylow子群独立分析（对每个素数p独立计算n_p，试图证明某个n_p=1）
- translation_to: 跨素数正规化子链论证（利用一个Sylow子群的正规化子结构约束另一个Sylow子群的数量）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: case_by_case, gap_type: method_translation}
- tell_small_concepts: ["Sylow子群数量", "正规化子阶", "循环群判定", "正规化子包含链", "素因子互不整除", "矛盾"]
- expected_ai_method: bare AI会逐个独立分析每个Sylow子群的数量（case_by_case），尝试证明某个n_p=1，或尝试元素计数法。当计数法失败后，不知道如何利用不同素数Sylow子群之间的交互关系。
- correct_method: 跨素数正规化子链论证——利用Sylow 17-子群正规化子的循环性（阶51）迫使它包含Sylow 3-子群，再通过Sylow 3-子群的正规化子中的Sylow 17-子群正规性导出阶的矛盾。

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？——可以。structural_existence、case_by_case、method_translation都是已有值，且粒度匹配。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？——一致。case_by_case和method_translation都是中等抽象粒度。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？——足够。这道题的tell特征（正规化子链、跨素数交互）可以通过small_concepts区分，不需要新维度。
- [x] 如果发现拓扑分类需要进化，在此写出建议：——无需进化。

**拓扑进化建议**（如有）：无。已有拓扑分类完全够用。

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

**局部pairs详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对抽象群论问题不知道从何入手 | 描述题目结构：已知|G|=1785=3×5×7×17，要证G非单群 | 0.3 | 纯元认知观察 | false | {structural_existence, direct_calculation, method_problem_mismatch} | ["群阶", "单群", "正规子群", "素因子分解"] |
| 2 | AI列出标准工具但看不到跨素数交互 | 列出所有证明群非单群的方法 | 0.5 | 自由列举 | false | {structural_existence, enumeration_brute_force, search_space_estimation} | ["Sylow定理", "计数法", "正规化子", "群作用"] |
| 3 | AI尝试计数法但749<1785，计数法失败 | 试试元素计数法计算各阶元素总数 | 0.4 | 小尝试 | false | {structural_existence, direct_calculation, method_problem_mismatch} | ["元素计数", "Sylow数量", "1785分解", "计数失败"] |
| 4 | AI不知道正规化子阶51是循环群（3∤16） | 看Sylow 17-子群正规化子的阶和结构 | 0.6 | 思维操作引导 | true | {structural_existence, logical_deduction, knowledge_gap} | ["正规化子阶", "循环群Z_51", "3不整除16", "交换群"] |
| 5 | AI看不到交换正规化子迫使包含关系 | N_G(P_17)交换⇒包含Sylow 3-子群Q⇒N_G(P_17)≤N_G(Q) | 0.7 | 思维操作引导 | false | {structural_existence, logical_deduction, structural_transformation} | ["交换正规化子", "Sylow 3-子群包含", "正规化子包含关系", "n_3约束"] |
| 6 | AI需要在N_G(Q)中发现Sylow 17正规性导出矛盾 | 分析N_G(Q)中Sylow 17-子群的正规性 | 0.7 | 推进 | false | {structural_existence, logical_deduction, structural_transformation} | ["N_G(Q)中Sylow 17", "正规子群", "正规化子链", "阶矛盾255>51"] |
| 7 | AI需要组装完整证明 | 完整总结证明 | 0.4 | 能量传递引导 | false | {structural_existence, logical_deduction, method_translation} | ["分情况讨论", "反证法", "完整证明", "矛盾收束"] |

**全局pairs详情**：

1. path_feature型：
- scope: 完整证明路径（P_17→循环正规化子→Q→N_G(Q)→P'→矛盾）
- observation_point: null
- tell: 证明需要一条连接不同素数Sylow子群的正规化子包含链，从P_17的循环正规化子出发，经过Q的正规化子，回到P'的正规化子，形成阶的矛盾
- hint: 沿着正规化子链追踪：P_17的正规化子循环⇒包含Q⇒Q的正规化子大⇒其中有正规Sylow 17⇒P'的正规化子更大⇒矛盾
- hint_level: 0.8
- generalizability: "high — 适用于任何阶为多个不同素数乘积的群非单群证明，关键是找到形成正规化子链的素数对"
- why_not_visible_locally: 每个单独步骤（循环正规化子、包含关系、Sylow在正规化子中正规）看起来都是常规操作，但将P_17→Q→P'连接成矛盾链的完整路径只有从全局视角才能看到——局部步骤中看不出"为什么要从17跳到3再跳回17"
- tell_topology: {structural_existence, logical_deduction, structural_transformation}
- tell_small_concepts: ["正规化子链", "跨素数Sylow交互", "循环正规化子", "包含关系传递", "阶矛盾"]

2. implicit型：
- scope: 3∤16这个数论条件在整个证明中的隐含驱动作用
- observation_point: "R4"
- tell: 素因子对(3,17)满足3不整除17-1=16，这个隐含的数论条件是驱动整个正规化子链论证的引擎——它迫使阶51的群循环，进而迫使包含关系
- hint: 检查分解中哪些素数对(p,q)满足p不整除q-1——这决定了哪些正规化子是循环的，从而决定了正规化子链的起点
- hint_level: 0.9
- generalizability: "high — 对任何阶为不同素数乘积的群，检查素数对是否满足p∤(q-1)是构造正规化子链论证的第一步"
- why_not_visible_locally: 条件3∤16在R4中作为"阶51的群是循环群"的判定条件出现，看起来只是一个局部的事实检查。但它在整个证明中扮演的"引擎"角色——驱动循环性⇒交换性⇒包含⇒矛盾链——在任何单个步骤中都不可见
- tell_topology: {structural_existence, logical_deduction, knowledge_gap}
- tell_small_concepts: ["素数对互不整除", "p不整除q-1", "循环群判定", "隐含驱动条件", "数论条件"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试元素计数法，发现749<1785后认为计数法不够，然后可能尝试逐个分析每个Sylow子群数量但无法发现跨素数的正规化子链论证。关键错误是停留在"每个素数独立分析"的框架中，不知道利用一个Sylow子群的正规化子结构来约束另一个素数的Sylow子群数量。
- suitable_for_poc: ["tell_extraction", "hint_injection", "knowledge_bottleneck_detection", "method_translation_detection"]
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
- [x] answer（**⚠ 必填，不能为None**。proof类型填要证明的结论，如"sum >= ..."；existence_construction类型填构造的存在性结论；numerical类型填数值答案）
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

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="396366"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000256"
   - extracted_by改为"subagent"

**示例代码**：
```python
from arango import ArangoClient
from datetime import datetime, timezone
import json

client = ArangoClient(hosts='http://localhost:8529')
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
now = datetime.now(timezone.utc).isoformat()

# 读取profile.json
with open('profile.json', 'r') as f:
    profile = json.load(f)

# 写入problem_profiles
db.collection('problem_profiles').insert(profile, overwrite=True)

# 更新problem_extraction_progress
db.collection('problem_extraction_progress').update({
    '_key': '396366',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000256',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000256')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: fate_000256
- solution_method_type: normalizer_chain_argument
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。已有拓扑分类（structural_existence / case_by_case / method_translation等）完全够用，粒度一致。
- 是否遇到异常: 无异常，入库和验证均一次通过

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
