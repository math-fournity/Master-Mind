# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2021p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2021P5.lean
- **来源**: IMO 2021 P5
- **ArangoDB progress记录_key**: 329261（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2021P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：两只松鼠Bushy和Jumpy收集了2021个核桃。Jumpy将核桃编号1到2021，并在树周围挖了2021个洞排成圆形。Bushy将每个核桃放入一个洞（任意排列）。Jumpy决定通过2021次移动重新排列：在第k次移动中，Jumpy交换核桃k相邻的两个核桃的位置。证明：存在某个k值，使得在第k次移动中，Jumpy交换的两个核桃a和b满足a < k < b。
- 解答核心思路（1-2句话）：反证法——假设不存在这样的k，则定义染色不变量（第j步后将编号<j的洞染红色、其余染黑色），计算相邻黑洞对数的mod 2值。初始全黑时该值为2021≡1(mod 2)，最终全红时为0，但不变量证明该值不变，矛盾。
- 解答关键步骤列表：
  1. 反证法：假设对所有k，交换的两个核桃a,b不满足a<k<b
  2. 定义染色：第j步后，洞x染红色当且仅当其中核桃编号<j，否则黑色
  3. 定义blackPairs：相邻黑洞对数（mod 2）
  4. 关键引理coloring_succ：若无"好移动"，则第j步后恰好将一个黑洞翻为红色，且其两个邻居颜色相同
  5. 关键引理blackPairs_update：将一个黑洞翻红且邻居同色时，blackPairs不变
  6. 初始状态(j=0)：全黑，blackPairs=2021≡1(mod 2)
  7. 最终状态(j=2021)：全红，blackPairs=0
  8. 归纳：blackPairs恒等于1，与最终值0矛盾

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
| 1 | 纯元认知观察 | 0.8 | 仔细阅读这道题。题目中有哪些关键结构？圆环排列、2021个核桃、第k次移动交换核桃k的邻居——这些要素之间有什么关系？已知什么、要求证明什么？ | 题目核心结构：2021个核桃排列在圆环上的2021个洞中，第k次移动交换核桃k的两个邻居。要证明存在k使得交换的两个核桃a,b满足a<k<b。关键观察：移动序号k与核桃编号a,b之间有大小关系约束。圆环结构意味着相邻关系是循环的。2021是奇数。 |
| 2 | 自由列举 | 0.7 | 面对这个"存在某个k使得a<k<b"的证明，你能想到哪些可能的攻击方向？列出所有你能想到的方法。 | 可能方向：1) 直接构造/反证法 2) 考虑排列的逆序数/置换奇偶性 3) 染色法/不变量方法 4) 归纳法 5) 考虑每步移动对排列的影响 6) 分析每个核桃的位置变化轨迹 7) 用mod 2论证 |
| 3 | 小尝试 | 0.5 | 试试逆序数方向：每次交换两个元素会改变逆序数的奇偶性。能否用逆序数奇偶性来证明？ | 尝试逆序数：每次交换改变逆序数奇偶性。2021次交换后逆序数奇偶性改变了2021次（奇数次）。但逆序数与"a<k<b"的关系不直接——逆序数只记录全局的逆序对，无法精确捕捉"第k步交换的两个核桃是否跨越k"。这个方向似乎难以直接得到结论。 |
| 4 | 思维操作引导 | 0.4 | 逆序数方向不够精确。现在做一个思维操作：定义一个"染色"方案——在第j步之后，将编号小于j的核桃所在的洞染成红色，其余染成黑色。这个染色方案每步如何变化？ | 第j步后：编号<j的核桃在红洞，编号≥j的在黑洞。每步j→j+1时，核桃j从"≥j"变为"<j+1"，所以恰好核桃j所在的洞从黑色翻为红色。其余洞颜色不变（除非被交换影响位置）。关键：第j步交换的是核桃j的两个邻居a和b，如果a<j<b不成立，则a和b要么都<j要么都≥j，即它们的颜色相同。 |
| 5 | 思维操作引导 | 0.3 | 现在定义一个不变量：相邻黑洞对数（mod 2）。在"无好移动"假设下，每步翻一个黑洞为红色且其邻居同色时，这个不变量如何变化？ | 定义blackPairs = 相邻黑洞对数 mod 2。在无好移动假设下：第j步将核桃j所在的洞从黑翻红，且其两个邻居颜色相同（因为a,b要么都<j要么都≥j）。翻一个黑洞为红色时，如果两个邻居同色（都红或都黑），则与该洞相关的两个相邻对同时增减，blackPairs不变。所以blackPairs是常数。 |
| 6 | 推进 | 0.5 | 计算初始状态(j=0)和最终状态(j=2021)的blackPairs值，看看是否矛盾。 | 初始(j=0)：所有核桃编号≥0，全黑。2021个洞排成圆环，有2021个相邻对，全黑，所以blackPairs=2021≡1(mod 2)。最终(j=2021)：所有核桃编号<2021，全红，blackPairs=0。但不变量说blackPairs恒等于1，与最终值0矛盾！所以假设不成立，存在k使得a<k<b。 |
| 7 | 能量传递引导 | 0.6 | 回顾整个证明：反证法→染色不变量→奇偶性矛盾。这个证明结构非常优美——用mod 2的不变量捕捉了"跨越"的本质。请总结这个证明的核心思想。 | 核心思想：通过染色将"编号大小关系"转化为"颜色"，用mod 2不变量捕捉排列在圆环上的结构特征。反证法假设"无跨越"使得每步翻色时邻居同色，从而不变量守恒。但初始全黑(奇数个对≡1)与最终全红(0)矛盾。关键洞察是2021为奇数——初始全黑时相邻对数为奇数，这是矛盾的根源。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1,R2,R6,R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4,R5）
- level_sum: 0.8+0.7+0.5+0.4+0.3+0.5+0.6=3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"（染色方案的定义是关键知识转折点）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"（不变量的构造和邻居同色的推理是思维瓶颈）

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
- problem_type: structural_existence（证明存在某个k满足特定结构性质）
- structure_features: 圆环排列上的置换操作序列，每步操作由当前步序号决定操作对象（核桃k的邻居），需证明存在某步使得操作对象跨越当前步序号。本质是离散结构上的存在性证明，用反证法+不变量。
- key_objects: ["圆环排列(2021个洞)", "置换/排列", "交换操作序列", "染色方案(红/黑)", "mod 2不变量(blackPairs)", "奇偶性"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["反证法", "染色不变量", "奇偶性论证", "归纳法", "结构-操作-不变量三步法"]
- primary_pattern: 染色不变量（通过染色将大小关系转化为颜色，用mod 2不变量守恒推出矛盾）
- knowledge_required: ["置换与排列", "圆环上的相邻关系", "mod 2算术/奇偶性", "染色论证", "不变量方法", "反证法"]
- key_insight: 将"核桃编号与步序号的大小关系"翻译为"洞的染色（红/黑）"，使得"无跨越"条件等价于"翻色时邻居同色"，从而mod 2不变量守恒——而初始全黑(奇数)与最终全红(0)的矛盾恰好来自2021为奇数。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 大小关系比较（a < k < b 的直接分析）
- translation_to: 染色+mod 2不变量（将大小关系翻译为颜色，将"跨越"翻译为"邻居异色"）
- translation_type: 结构翻译（将序号大小关系的代数结构翻译为圆环染色的拓扑结构，再用mod 2不变量捕捉守恒性）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "logical_deduction", gap_type: "structural_transformation"}
- tell_small_concepts: ["染色方案", "mod 2不变量", "圆环相邻对", "反证法矛盾", "邻居同色", "奇偶性守恒"]
- expected_ai_method: bare AI预期会尝试逆序数/置换奇偶性直接分析，或枚举具体排列验证——这些都是method_problem_mismatch，因为直接分析大小关系无法捕捉圆环拓扑结构
- correct_method: 染色不变量法——将大小关系翻译为染色，用mod 2不变量守恒推出初始(全黑,奇数)与最终(全红,0)的矛盾

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ → 可以。problem_type=structural_existence已有，ai_method_type=logical_deduction已有（bare AI会用逻辑推理直接分析），gap_type=structural_transformation已有（需要将大小关系结构翻译为染色结构）。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ → 一致。都是中等抽象粒度。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ → 足够。三个维度能区分：bare AI用logical_deduction直接推理大小关系，但需要structural_transformation将问题翻译到染色不变量框架。
- [x] 如果发现拓扑分类需要进化，在此写出建议： → 无需进化，现有分类够用。

**拓扑进化建议**（如有）：无。现有拓扑分类体系完全够用。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs详情**：

| R | tell | hint | level | situation_type | kb | topology(pt,aim,gap) | small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对圆环排列+步序号决定操作的存在性问题，尚未识别出"大小关系→染色"的翻译路径 | 观察题目结构——圆环排列、步序号k与核桃编号a,b的大小关系约束 | 0.8 | 纯元认知观察 | false | structural_existence, logical_deduction, structural_transformation | ["圆环排列","步序号与编号关系","存在性证明"] |
| 2 | AI列出了多个方向但未识别出染色不变量是正确路径 | 列出所有可能方向，包括染色法/不变量方法 | 0.7 | 自由列举 | false | structural_existence, enumeration_brute_force, method_translation | ["方向列举","逆序数","染色法","不变量"] |
| 3 | AI尝试逆序数方向，发现逆序数无法精确捕捉"第k步交换是否跨越k"——方法与问题不匹配 | 试逆序数方向，发现其不足 | 0.5 | 小尝试 | false | structural_existence, direct_calculation, method_problem_mismatch | ["逆序数奇偶性","全局vs局部","跨越k"] |
| 4 | AI需要从逆序数方向转向染色方案——这是知识瓶颈，需要知道"将编号翻译为染色"的技巧 | 定义染色方案：编号<j的核桃所在洞染红，其余染黑 | 0.4 | 思维操作引导 | true | structural_existence, logical_deduction, knowledge_gap | ["染色方案","红/黑","编号<j","翻色"] |
| 5 | AI需要构造mod 2不变量并理解"邻居同色导致守恒"——这是思维瓶颈 | 定义blackPairs不变量，分析翻色时邻居同色的影响 | 0.3 | 思维操作引导 | false | structural_existence, logical_deduction, structural_transformation | ["mod 2不变量","相邻黑洞对","邻居同色","守恒性"] |
| 6 | AI已有不变量，需要计算初始和最终值并发现矛盾 | 计算初始(全黑,2021≡1)和最终(全红,0)的blackPairs值 | 0.5 | 推进 | false | structural_existence, direct_calculation, method_problem_mismatch | ["初始全黑","最终全红","2021为奇数","矛盾"] |
| 7 | AI已完成证明，需要总结核心思想 | 总结证明结构——反证法→染色不变量→奇偶性矛盾 | 0.6 | 能量传递引导 | false | structural_existence, logical_deduction, structural_transformation | ["反证法","染色不变量","奇偶性矛盾","2021奇数"] |

**全局pairs详情**：

1. path_feature型:
- scope: "完整证明路径：从逆序数直接分析到染色不变量的翻译"
- observation_point: null
- tell: bare AI会在逆序数/置换奇偶性方向停留，不会想到用染色将大小关系翻译为拓扑结构。完整路径的特征是"方法翻译"——从代数大小关系翻译到染色+mod 2不变量。
- hint: 当直接分析大小关系无法捕捉圆环拓扑时，考虑染色+mod 2不变量翻译——将"编号<j"翻译为"红色"，将"跨越k"翻译为"邻居异色"
- hint_level: 0.6
- generalizability: "high - 适用于任何需要将代数大小关系翻译为拓扑结构的离散组合问题，特别是圆环/排列上的存在性证明"
- why_not_visible_locally: "在局部步骤中，AI看到的是'第k步交换两个核桃a,b'这个具体操作，无法从这个局部视角看到'将编号翻译为染色'这个全局翻译路径。染色方案的灵感来自对整个操作序列的宏观观察——每步恰好将一个核桃从'≥j'变为'<j'，这个模式只有在观察完整序列时才浮现。"
- tell_topology: {problem_type: "structural_existence", ai_method_type: "logical_deduction", gap_type: "structural_transformation"}
- tell_small_concepts: ["染色翻译","mod 2不变量","宏观序列观察","大小关系→颜色"]

2. implicit型:
- scope: "初始与最终状态的奇偶性差异"
- observation_point: "R6"
- tell: 2021为奇数这个事实是矛盾的核心——初始全黑时相邻对数为奇数(≡1 mod 2)，最终全红时为0，但不变量守恒。奇数性是隐含的驱动力。
- hint: 注意2021为奇数——初始全黑时blackPairs=2021≡1(mod 2)，这是矛盾的关键
- hint_level: 0.4
- generalizability: "medium - 奇偶性矛盾在圆环排列问题中常见，但具体到'奇数个相邻对'的洞察需要结合染色方案"
- why_not_visible_locally: "在R4和R5的局部步骤中，AI关注的是染色方案的定义和不变量的守恒性，2021为奇数这个事实隐含在初始值的计算中，只有在R6计算初始值时才显化。在定义染色和不变量时，无法预见到奇数性将成为矛盾的核心。"
- tell_topology: {problem_type: "structural_existence", ai_method_type: "direct_calculation", gap_type: "knowledge_gap"}
- tell_small_concepts: ["2021奇数","初始全黑","奇偶性矛盾","mod 2"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试逆序数/置换奇偶性方向，分析每次交换对全局逆序数的影响，但无法将"第k步交换的两个核桃是否跨越k"这个局部条件与逆序数的全局变化联系起来。AI可能尝试枚举小例子但无法发现染色不变量的模式。即使想到染色，也可能无法构造出正确的mod 2不变量（blackPairs），或无法意识到"邻居同色导致守恒"这个关键引理。最终在反证法框架内无法找到合适的不变量导致矛盾。
- suitable_for_poc: ["POC-VMS-8（脉络继承+方向注入验证）", "POC-VMS-9/10（tell端去特化+形式化过滤验证）", "染色不变量方向注入实验", "知识瓶颈突破实验（R4染色方案注入）"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON，已写入 `profile.json`

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
2. 更新`problem_extraction_progress`集合中`_key="329261"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2021p5"
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
    '_key': '329261',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2021p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2021p5')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证详情: 7 local pairs, 2 global pairs, knowledge_bottleneck=R4(str), thinking_bottleneck=R5(str), answer非None

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_imo2021p5
- solution_method_type: coloring_invariant_contradiction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，现有拓扑分类体系完全够用
- 是否遇到异常: 是——初次写入profile.json时中文引号被转为ASCII双引号导致JSON解析失败，后用Python json.dump重新生成解决

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
