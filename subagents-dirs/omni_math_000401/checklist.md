# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000401
- **文件路径**: subagents-dirs/omni_math_000401/problem.lean
- **来源**: AoPS omni_math (yau_contest)
- **ArangoDB progress记录_key**: 330273（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000401/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设p为素数，证明Euler定理：方程p=x²+3y²有整数解当且仅当p=3或p≡1(mod 3)。可使用Q(√-3)的整数环是PID这一事实。
- 解答核心思路（1-2句话）：用二次互反律证明(-3/p)=1从而p在Q(√-3)中分裂，再利用PID性质得到范数为p的元素π，从范数方程导出p=x²+3y²的整数解。
- 解答关键步骤列表：
  1. "仅当"方向：对p=x²+3y²取模3分析，p≠3时x²≡p(mod 3)要求p≡1(mod 3)
  2. p=3时直接取(x,y)=(0,1)
  3. p≡1(mod 3)时，由二次互反律计算Legendre符号(-3/p)=(p/3)=1
  4. 因此p在Q(√-3)中分裂
  5. Q(√-3)的整数环为Z[ω]，ω=(-1+√-3)/2
  6. 由PID性质，存在π∈Z[ω]使N(π)=p
  7. 设π=a+bω，计算范数N(π)=a²-ab+b²，通过变量替换得到p=x²+3y²形式

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 这道题的结构是什么？需要证明什么方向？已知条件和可用工具分别是什么？ | 这是一个双向充要条件证明。"仅当"方向（⇒）需要从p=x²+3y²推出p=3或p≡1(mod 3)；"当"方向（⇐）需要从p=3或p≡1(mod 3)推出p=x²+3y²有整数解。可用工具是Q(√-3)的整数环为PID。 |
| 2 | 自由列举 | 0.7 | 对于"当"方向（p≡1(mod 3) ⇒ p=x²+3y²有解），你能想到哪些可能的证明路径？ | 可能路径：(a)直接构造法——尝试对给定p找到x,y；(b)模运算/初等数论方法；(c)二次互反律与Legendre符号；(d)代数数论方法——利用Q(√-3)的整数环和范数；(e)二次型的表示理论——用x²+3y²作为二次型。 |
| 3 | 小尝试 | 0.5 | 试试用初等方法：对p≡1(mod 3)，能否直接通过模运算或简单构造找到x,y使p=x²+3y²？ | 初等方法困难。对小的p（如p=7: 7=2²+3·1², p=13: 13=1²+3·2²）可以验证，但无法推广到任意p≡1(mod 3)。模运算只能给出必要条件，不能保证存在性。需要更深层的工具。 |
| 4 | 思维操作引导 | 0.4 | 题目提示了Q(√-3)的整数环是PID。请思考：p=x²+3y²这个方程与Q(√-3)有什么联系？范数N(a+b√-3)=a²+3b²是否相关？能否用二次互反律先证明(-3/p)=1？ | 关键联系：x²+3y²正是Q(√-3)中元素的范数形式。由二次互反律，(-3/p)=(-1/p)(3/p)，且(-1/p)·(3/p)可简化为(p/3)。当p≡1(mod 3)时，(p/3)=(1/3)=1，所以(-3/p)=1。这意味着-3是模p的二次剩余，p在Q(√-3)中分裂。 |
| 5 | 推进 | 0.5 | 既然(-3/p)=1且p在Q(√-3)中分裂，继续推进：分裂意味着什么？如何利用PID性质得到我们需要的结论？ | p在Q(√-3)中分裂意味着(p)=𝔭₁𝔭₂，其中𝔭₁,𝔭₂是不同的素理想。由于Z[ω]是PID，𝔭₁=(π)由一个元素生成。因此N(π)=N(𝔭₁)=p，即存在π∈Z[ω]使得其范数恰好为p。 |
| 6 | 思维操作引导 | 0.3 | 现在已知存在π∈Z[ω]使N(π)=p，其中ω=(-1+√-3)/2。请具体写出π=a+bω的范数公式，并通过变量替换将其转化为x²+3y²的形式。 | π=a+bω，范数N(π)=a²-ab+b²（因为ω+ω̄=1, ωω̄=1... 实际上ω̄=(-1-√-3)/2, ωω̄=1, ω+ω̄=-1... 需要重新计算：N(a+bω)=(a+bω)(a+bω̄)=a²+ab(ω+ω̄)+b²ωω̄=a²-ab+b²）。令x=2a-b, y=b（或类似替换），则a²-ab+b²=(2a-b)²/4+3b²/4... 需要处理分母。实际上a²-ab+b²=((2a-b)²+3b²)/4，当a,b同奇偶时x=2a-b, y=b为偶数，可整除。需要分情况讨论奇偶性，最终得到p=x²+3y²。 |
| 7 | 能量传递引导 | 0.6 | 你已经完成了最关键的部分——从代数数论框架回到具体的Diophantine方程。请整理完整证明，确认"仅当"和"当"两个方向都完整，并检查范数公式到x²+3y²的转换是否严谨。 | 完整证明："仅当"——若p=x²+3y²，则p≡x²(mod 3)，平方模3只能为0或1，故p≡0或1(mod 3)，p=3或p≡1(mod 3)。"当"——p=3取(0,1)；p≡1(mod 3)时由上述步骤得(-3/p)=1→p分裂→PID给范数p的π→范数公式转换得p=x²+3y²。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4 (R1,R2,R5,R7)
- knowledge_rounds（思维操作引导的轮数）: 2 (R4,R6)
- level_sum: 0.8+0.7+0.5+0.4+0.5+0.3+0.6 = 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: 双向充要条件证明，将素数的同余条件（p≡1 mod 3）与二次型表示（p=x²+3y²）通过代数数论桥梁（二次互反律→分裂→PID→范数）连接
- key_objects: 素数p, 二次型x²+3y², Legendre符号(-3/p), 二次域Q(√-3), 整数环Z[ω], 范数映射N, PID性质

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["双向分解——将充要条件拆为'仅当'和'当'两个方向分别处理", "代数翻译——将Diophantine方程p=x²+3y²翻译为Q(√-3)中的范数问题", "互反律计算——用二次互反律计算Legendre符号(-3/p)建立分裂条件", "结构利用——利用PID性质从理想分解提取具体元素", "范数桥接——用范数映射连接代数数论与初等数论"]
- primary_pattern: 代数翻译（将Diophantine问题翻译为代数数论框架下的范数问题）
- knowledge_required: ["二次互反律与Legendre符号", "素数在数域中的分裂", "Q(√-3)的整数环Z[ω]", "PID性质与范数方程的关系", "二次域中的范数形式"]
- key_insight: 识别x²+3y²是Q(√-3)的范数形式，从而将"p能否表示为x²+3y²"翻译为"p在Q(√-3)中是否有范数为p的元素"，后者由二次互反律（分裂条件）和PID（主理想→具体元素）共同保证。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 初等数论/Diophantine方程（素数p的二次型表示问题p=x²+3y²）
- translation_to: 代数数论（二次域Q(√-3)中的素数分裂与范数方程）
- translation_type: 方法翻译（从初等数论的语言翻译到代数数论的语言，通过范数映射作为桥梁）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "direct_calculation", gap_type: "knowledge_gap"}
- tell_small_concepts: ["Legendre符号(-3/p)", "二次互反律", "素数分裂", "范数形式x²+3y²", "PID性质", "Z[ω]整数环", "范数到二次型的变量替换"]
- expected_ai_method: bare AI会尝试初等方法——直接构造x,y、模运算分析、或暴力验证小素数，不会想到用代数数论框架
- correct_method: 用二次互反律建立(-3/p)=1→p在Q(√-3)中分裂→PID给出范数p的元素π→范数公式变量替换得到p=x²+3y²

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=characterization, ai_method_type=direct_calculation, gap_type=knowledge_gap均可归入已有拓扑类别
- [x] 粒度一致——与已有值的粒度统一
- [x] 三个维度足够区分这道题的tell
- [x] 无需进化建议

**拓扑进化建议**（如有）：无。当前三个维度（problem_type/ai_method_type/gap_type）足以区分此题。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到充要条件证明但未识别关键工具方向 | 描述题目结构，识别两个方向和可用工具 | 0.8 | 纯元认知观察 | false | {characterization, direct_calculation, method_problem_mismatch} | ["充要条件", "双向证明", "素数表示", "二次型"] |
| 2 | AI列举路径但可能未优先代数数论路线 | 列出所有可能证明路径 | 0.7 | 自由列举 | false | {characterization, enumeration_brute_force, search_space_estimation} | ["证明路径列举", "初等数论", "代数数论", "二次型表示理论"] |
| 3 | AI尝试初等方法后卡住——能验证小例但无法推广 | 试用初等方法看是否可行 | 0.5 | 小尝试 | false | {characterization, direct_calculation, method_problem_mismatch} | ["模运算", "直接构造", "小素数验证", "存在性困难"] |
| 4 | AI未将x²+3y²联系到Q(√-3)范数，未想到二次互反律 | 联系方程与Q(√-3)，用二次互反律计算(-3/p) | 0.4 | 思维操作引导 | false | {characterization, direct_calculation, method_translation} | ["范数形式", "二次互反律", "Legendre符号(-3/p)", "素数分裂"] |
| 5 | AI已建立(-3/p)=1和分裂，但未用PID提取具体元素 | 从分裂继续推进——用PID得到范数p的元素 | 0.5 | 推进 | false | {characterization, logical_deduction, structural_transformation} | ["素理想分解", "PID", "主理想", "范数等于p"] |
| 6 | AI有范数p的元素π但不知如何将N(π)=a²-ab+b²转为x²+3y² | 写出范数公式并做变量替换 | 0.3 | 思维操作引导 | true | {characterization, direct_manipulation, knowledge_gap} | ["范数公式a²-ab+b²", "变量替换", "奇偶性讨论", "x²+3y²形式转换"] |
| 7 | AI有所有部件但需组装完整证明并验证 | 整理完整证明，确认两个方向完整 | 0.6 | 能量传递引导 | false | {characterization, logical_deduction, method_problem_mismatch} | ["证明组装", "双向验证", "范数转换严谨性"] |

**全局pairs详情**：

Global pair 1 (implicit):
- scope_type: "implicit"
- scope: "整个证明的关键翻译步骤：从Diophantine方程到代数数论框架"
- observation_point: "R4"
- tell: AI在处理p=x²+3y²时停留在初等数论层面，没有识别出x²+3y²是Q(√-3)的范数形式
- hint: 识别x²+3y²=Norm(a+b√-3)，将问题翻译为"p在Q(√-3)中是否有范数p的元素"
- hint_level: 0.4
- generalizability: "high — 范数-二次型对应是代数数论中的通用翻译技术，适用于所有二次域中的表示问题"
- why_not_visible_locally: "在R1-R3的局部视角中，AI看到的是具体的Diophantine方程和模运算，无法看到这个方程与Q(√-3)范数形式的同构关系——这个对应关系需要从代数数论的全局视角才能识别，局部步骤中x²+3y²只是一个普通的二次型"
- tell_topology: {characterization, direct_calculation, method_translation}
- tell_small_concepts: ["范数形式识别", "Diophantine到代数数论翻译", "x²+3y²=Norm", "Q(√-3)"]

Global pair 2 (path_feature):
- scope_type: "path_feature"
- scope: "完整证明路径：二次互反律→分裂→PID→范数→变量替换"
- observation_point: null
- tell: 整个证明路径的特征是"通过三层代数结构（Legendre符号→分裂→PID）逐步从同余条件到达具体元素，再通过范数公式回到初等形式"——这个多层桥接路径无法在任何单一步骤中看到
- hint: 理解证明的整体架构是"同余条件→代数结构→具体元素→初等形式"的四步桥接
- hint_level: 0.5
- generalizability: "medium — 这种多层桥接路径在代数数论证明中常见，但具体层数和桥接方式因问题而异"
- why_not_visible_locally: "在R4只看到二次互反律，在R5只看到分裂和PID，在R6只看到范数公式——每一步都是局部的代数操作，无法从任何单一步骤看出整个'同余→分裂→PID→范数→初等形式'的完整桥接路径"
- tell_topology: {characterization, direct_calculation, structural_transformation}
- tell_small_concepts: ["多层桥接路径", "同余到代数结构", "代数结构到具体元素", "范数回到初等形式", "证明整体架构"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI能正确证明"仅当"方向（模3分析简单），但在"当"方向会失败：会尝试初等构造法和模运算，无法识别x²+3y²与Q(√-3)范数形式的联系，不会使用二次互反律计算(-3/p)，更不会利用PID性质从理想分解提取具体元素。最终产出不完整的证明（只有"仅当"方向）。
- suitable_for_poc: ["method_translation_poc——测试AI能否从初等数论翻译到代数数论框架", "knowledge_gap_poc——测试知识瓶颈检测（二次互反律+分裂+PID+范数）", "tell_hint_injection_poc——测试在R4注入范数识别hint后AI能否完成后续步骤"]
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

**将完整JSON写入工作目录的 `profile.json` 文件** — 已完成

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
- problem_id: omni_math_000401
- solution_method_type: algebraic_translation
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 implicit + 1 path_feature)
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，当前三维度（characterization/direct_calculation/knowledge_gap）足够
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
