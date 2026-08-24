# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa1996p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa1996P6.lean
- **来源**: USA 1996 P6
- **ArangoDB progress记录_key**: 329384（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa1996P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Determine, with proof, whether there is a subset X of the integers with the following property: for any integer n there is exactly one pair (a, b) of elements of X satisfying a + 2b = n.
- 解答核心思路（1-2句话）：答案是存在。利用负四进制（base -4）表示——每个整数在base -4下有唯一展开（数字{0,1,2,3}），每个数字d可拆分为d = lowBit(d) + 2·highBit(d)（两个二进制位），从而n = a + 2b，其中a和b都是base -4下用二进制数字{0,1}表示的数。X定义为所有可用base -4二进制数字表示的整数集合。
- 解答关键步骤列表：
  1. 定义negFourValue：用base -4对数字列表求值
  2. 证明每个整数都有base -4展开（exists_negFourExpansion，用良基归纳）
  3. 定义lowBit/highBit：将{0,1,2,3}的数字拆分为两个{0,1}位
  4. 证明negFourValue_split：negFourValue(digits) = negFourValue(lowBits) + 2·negFourValue(highBits)
  5. 定义X = Set.range(negFourValue(b:=2))，即所有base -4二进制数字表示的整数
  6. 存在性：对任意n，取其base -4展开，拆分为lowBits和highBits，得到a,b∈X且a+2b=n
  7. 唯一性：binary_pair_unique证明——若negFourValue(cs)+2·negFourValue(ds) = negFourValue(as)+2·negFourValue(bs)，则cs=as且ds=bs（逐位归纳）

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.3 | 描述这道题的结构：已知条件是什么？我们要找什么？这个"恰好一对"的约束意味着什么？ | 我们需要找到一个整数子集X，使得对任意整数n，恰好存在一对(a,b)∈X²满足a+2b=n。这是一个存在性问题，带有唯一性约束。"恰好一对"意味着存在性（覆盖所有整数）和唯一性（不重复表示）双重要求。 |
| 2 | 自由列举 | 0.5 | 列出所有可能的构造X的方法方向，不需要深入任何一个方向。 | 贪心构造（逐个添加元素）、模运算分析（利用a+2b的模性质）、进制表示（用某种进制的数字分解）、奇偶性论证、递归构造、概率方法…… |
| 3 | 小尝试 | 0.2 | 试着用贪心方法构造X：从空集开始，逐个添加整数，每次添加时检查是否维持唯一表示性质。 | 尝试贪心构造：添加0后，n=0需要(0,0)。添加1后，n=1需要(1,0)，n=2需要(0,1)。但继续添加会遇到矛盾——某些n会被多对(a,b)表示。贪心方法难以系统性地覆盖所有整数，且唯一性约束极难在增量构造中维护。这条路看起来走不通。 |
| 4 | 思维操作引导 | 0.4 | 放弃逐元素构造。换一个思维操作：思考什么样的"表示系统"能自然地给出a+2b=n的唯一分解。如果每个整数n有一个唯一的"展开"，这个展开自然分成两部分a和b，那X就是其中一部分的值域。想想进位制。 | 如果n在某种进制下有唯一展开n=Σd_i·r^i，且每个数字d_i可以分解为d_i = a_i + 2·b_i，那么a=Σa_i·r^i和b=Σb_i·r^i就给出a+2b=n。关键是找到一个进制r，使得{0,1,2,3}的数字能唯一地拆成两个二进制位，且整个系统对所有整数（包括负数）都有唯一展开。 |
| 5 | 思维操作引导 | 0.3 | 考虑负四进制（base -4）。每个整数在base -4下有唯一展开，数字取{0,1,2,3}。如何将每个数字d∈{0,1,2,3}拆分为两个二进制分量？ | 每个数字d∈{0,1,2,3}可以写为d = lowBit(d) + 2·highBit(d)，其中lowBit和highBit∈{0,1}。具体：0=(0,0), 1=(1,0), 2=(0,1), 3=(1,1)。这样base -4展开n=Σd_i·(-4)^i就分解为a=ΣlowBit(d_i)·(-4)^i和b=ΣhighBit(d_i)·(-4)^i，两者都是base -4下用二进制数字{0,1}表示的数。 |
| 6 | 推进 | 0.3 | 现在定义X为所有可用base -4二进制数字{0,1}表示的整数集合。证明对任意n，存在唯一的(a,b)∈X²使a+2b=n。 | 存在性：取n的base -4展开，按lowBit/highBit拆分得到a,b∈X，a+2b=n。唯一性：若另有(c,d)∈X²使c+2d=n，则c和d也有base -4二进制展开。由a+2b=c+2d，逐位比较（利用base -4二进制表示的唯一性），可得a=c且b=d。 |
| 7 | 能量传递引导 | 0.2 | 验证构造的正确性，整理完整证明。结论是什么？ | 构造验证通过：X存在，即所有可用base -4二进制数字{0,1}表示的整数集合。每个整数n的base -4展开给出唯一的(a,b)对。存在性由base -4展开的完备性保证，唯一性由二进制位拆分的双射性和base -4展开的唯一性保证。答案是：这样的子集X存在。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 2.2
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence
- structure_features: 存在性问题——寻找整数子集X，使得线性形式a+2b=n对每个整数n有唯一表示。核心是"唯一表示"约束与"全覆盖"要求的结合。
- key_objects: 整数子集X, 线性形式a+2b, 唯一表示对(a,b), 负四进制展开, 二进制数字拆分

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["structural_construction", "base_representation", "digit_decomposition", "uniqueness_proof", "negative_base_system"]
- primary_pattern: structural_construction
- knowledge_required: ["负进制表示（base -4的唯一展开定理）", "数字拆分（digit splitting into binary components）", "进位制中唯一表示的性质", "良基归纳法"]
- key_insight: 用负四进制（base -4）表示每个整数，每个数字{0,1,2,3}拆分为两个二进制位d=lowBit+2·highBit，从而a+2b=n的分解自然对应于base -4展开的数字拆分，X取base -4二进制数字表示的整数集合即可。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 逐元素贪心构造（incremental/greedy construction of set X）
- translation_to: 负四进制全局表示系统（base -4 positional number system with binary digit splitting）
- translation_type: structural_transformation（从局部增量构造翻译到全局代数结构）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: enumeration_brute_force, gap_type: structural_transformation}
- tell_small_concepts: ["unique representation", "a+2b decomposition", "negative base -4", "digit splitting", "binary decomposition", "positional number system"]
- expected_ai_method: enumeration_brute_force（bare AI会尝试逐元素贪心构造或模运算分析，无法系统覆盖所有整数）
- correct_method: structural construction via negative base -4 representation with binary digit splitting

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=structural_existence、ai_method_type=enumeration_brute_force、gap_type=structural_transformation都能归入已有拓扑类别
- [x] 粒度一致——标注值与已有值粒度统一
- [x] 三个维度足够区分这道题的tell和已有tell
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。已有拓扑分类足以覆盖此题。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs**：

| R | tell | hint | level | sit_type | kn_bottleneck | topology | small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到一个关于唯一表示的存在性问题，但不知道该寻找什么结构 | 描述题目结构：需要X⊆Z使得每个n恰好有一对(a,b)∈X²满足a+2b=n，这是存在性+唯一性双重要求 | 0.3 | 纯元认知观察 | false | (structural_existence, direct_calculation, method_problem_mismatch) | ["unique representation", "existence", "a+2b form"] |
| 2 | AI列出可能方向但未识别到进制表示系统的关键连接 | 列出所有可能方向：贪心构造、模运算、进制表示、奇偶性论证、递归构造 | 0.5 | 自由列举 | false | (structural_existence, enumeration_brute_force, search_space_estimation) | ["greedy construction", "modular arithmetic", "base representation", "positional system"] |
| 3 | AI尝试贪心构造遇到矛盾——唯一性约束在增量构造中极难维护 | 试贪心构造：从空集开始逐个添加元素，检查唯一表示性质是否维持 | 0.2 | 小尝试 | false | (structural_existence, enumeration_brute_force, method_problem_mismatch) | ["greedy construction", "incremental building", "contradiction", "coverage"] |
| 4 | AI困在逐元素构造中，未考虑全局表示系统 | 放弃逐元素构造，思考什么样的表示系统能自然给出a+2b=n的唯一分解，想想进位制 | 0.4 | 思维操作引导 | false | (structural_existence, direct_manipulation, structural_transformation) | ["positional number system", "representation", "decomposition", "unique expansion"] |
| 5 | AI考虑进制表示但不知道负四进制或如何拆分数字为二进制分量 | 考虑base -4：每个整数有唯一展开（数字{0,1,2,3}），每个数字d=lowBit(d)+2·highBit(d)拆为两个二进制位 | 0.3 | 思维操作引导 | true | (structural_existence, direct_calculation, knowledge_gap) | ["negative base", "base -4", "digit splitting", "binary decomposition", "lowBit", "highBit"] |
| 6 | AI理解数字拆分但需要连接到集合X的定义并证明唯一性 | 定义X为base -4二进制数字{0,1}表示的整数集合，证明存在性和唯一性 | 0.3 | 推进 | false | (structural_existence, algebraic_identity, method_translation) | ["binary digits", "set construction", "existence proof", "uniqueness proof", "base -4 expansion"] |
| 7 | AI已有构造，需要验证并整理完整证明 | 验证构造：检查存在性（base -4展开给出对）和唯一性（二进制对唯一性），整理完整证明 | 0.2 | 能量传递引导 | false | (structural_existence, logical_deduction, method_translation) | ["verification", "existence", "uniqueness", "complete proof"] |

**全局tell_hint_pairs**：

1. path_feature型：
- scope: "从贪心构造失败到负四进制构造的完整解题路径"
- observation_point: null
- tell: "解题路径需要放弃增量构造，转向全局表示系统。关键转折是从逐元素贪心尝试失败到识别负四进制提供结构框架。"
- hint: "当唯一表示存在性问题抗拒增量构造时，寻找全局代数结构（如进位制表示系统）来内在地提供唯一性。"
- hint_level: 0.7
- generalizability: "high——从局部/增量转向全局/结构的模式适用于许多带唯一性约束的存在性问题"
- why_not_visible_locally: "从贪心构造的任何单步看，失败表现为可能通过更努力尝试来解决的局部矛盾。只有看到从失败的贪心尝试到成功的负四进制构造的完整路径，才显现出模式：问题需要全局结构方法，而非局部优化。"
- tell_topology: {problem_type: structural_existence, ai_method_type: enumeration_brute_force, gap_type: structural_transformation}
- tell_small_concepts: ["incremental to global", "representation system", "negative base", "structural approach"]

2. implicit型：
- scope: "a+2b分解与base -4数字拆分之间的隐含连接"
- observation_point: "R5"
- tell: "a+2b的形式自然对应于将base-4数字拆分为两个二进制数字。问题中线性形式的系数2与表示系统中数字拆分之间的连接从题目本身不可见。"
- hint: "当问题涉及线性形式a+2b=n且带唯一性时，考虑系数2是否暗示进位制表示中的二进制数字拆分。"
- hint_level: 0.6
- generalizability: "medium——线性形式系数与数字拆分的连接特定于进位制表示问题，但将问题结构匹配到表示结构的模式是通用的"
- why_not_visible_locally: "在计算base -4展开的局部步骤中，将数字拆分为lowBit和highBit是机械操作。隐含洞见——a+2b中系数2正是使二进制数字拆分可行的关键——只有将问题的线性形式连接到表示系统结构时才可见。这个连接在任何单一计算步骤中都不可见。"
- tell_topology: {problem_type: structural_existence, ai_method_type: algebraic_identity, gap_type: method_translation}
- tell_small_concepts: ["linear form coefficient", "digit splitting", "binary decomposition", "base -4", "a+2b structure"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "Bare AI会尝试贪心构造或模运算分析，无法识别负四进制表示的连接。它会在维护唯一表示性质的局部调整中陷入困境，可能错误地认为这样的X不存在，或给出不完整的构造。"
- suitable_for_poc: ["tell_extraction", "hint_injection", "knowledge_bottleneck_detection"]
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
- [x] answer（"Yes, such a subset X exists..."）
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

**将完整JSON写入工作目录的 `profile.json` 文件** ✅

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证输出: compfiles_usa1996p6, 7 local pairs, 2 global pairs

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_usa1996p6
- solution_method_type: structural_construction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。已有拓扑分类（structural_existence / enumeration_brute_force / structural_transformation等）足以覆盖此题。
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
