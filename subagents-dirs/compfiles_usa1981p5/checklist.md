# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa1981p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa1981P5.lean
- **来源**: USA 1981 P5
- **ArangoDB progress记录_key**: 329326（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa1981P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Show that for any positive real number x and any nonnegative integer n, ∑_{k=1}^{n} ⌊kx⌋/k ≤ ⌊nx⌋, where the sum goes from k=1 to k=n inclusive.
- 解答核心思路（1-2句话）：将⌊kx⌋分解为kx - {kx}（整数部分=本身-小数部分），不等式转化为{nx} ≤ ∑{kx}/k。利用小数部分的次可加性{a(k+m)}≤{a(k)+a(m)}和强归纳法，通过选取使{m·x}/m最小的m来拆分求和完成归纳。
- 解答关键步骤列表：
  1. 分解：⌊kx⌋ = kx - {kx}，所以⌊kx⌋/k = x - {kx}/k，求和变为nx - ∑{kx}/k
  2. ⌊nx⌋ = nx - {nx}，不等式等价于 {nx} ≤ ∑_{k=1}^n {kx}/k
  3. 定义a(k) = {kx}，建立次可加性：a(k+m) ≤ a(k) + a(m)（小数部分性质）
  4. 对n用强归纳法。n=0时平凡
  5. n>0时，在{1,...,n}中选取使a(m)/m最小的m
  6. 由次可加性：a(n) ≤ a(n-m) + a(m)
  7. 由归纳假设：a(n-m) ≤ ∑_{k=1}^{n-m} a(k)/k
  8. 尾部求和：∑_{k=n-m+1}^{n} a(k)/k ≥ m·(a(m)/m) = a(m)（因为a(m)/m是最小值）
  9. 合并：a(n) ≤ a(n-m)+a(m) ≤ ∑_{k=1}^{n-m} a(k)/k + ∑_{k=n-m+1}^{n} a(k)/k = ∑_{k=1}^{n} a(k)/k

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
| 1 | 纯元认知观察 | 0.7 | 观察这个不等式：∑_{k=1}^{n} ⌊kx⌋/k ≤ ⌊nx⌋。左边是n项求和，右边是单项。题目中出现了什么数学对象？结构上有什么特征？ | 左边是取整函数⌊kx⌋除以k的求和，右边是⌊nx⌋。核心对象是取整函数（floor function）。结构特征：左边的每一项⌊kx⌋/k与右边的⌊nx⌋之间有k和n的对应关系。左边是"平均化"的取整值之和，右边是最大k对应的取整值。 |
| 2 | 自由列举 | 0.6 | 要处理取整函数⌊·⌋相关的不等式，你能想到哪些分解或变换的工具？列出所有可能的方向。 | 1) 取整函数基本性质⌊y⌋≤y<⌊y⌋+1；2) 分解⌊y⌋=y-{y}；3) 放缩法⌊kx⌋≤kx得左边≤nx但不够紧；4) 数学归纳法；5) Abel求和/分部求和；6) 逐项比较⌊kx⌋/k与⌊nx⌋/n |
| 3 | 小尝试 | 0.5 | 试试直接放缩：用⌊kx⌋≤kx，看看能得到什么，这个方向够不够？ | ⌊kx⌋/k≤x，所以∑⌊kx⌋/k≤nx。但需要≤⌊nx⌋=nx-{nx}，而nx≥⌊nx⌋，放缩太松，差了小数部分{nx}的量级。直接放缩不够，需要更精细的处理。 |
| 4 | 思维操作引导 | 0.4 | 既然直接放缩太松，试试用分解⌊y⌋=y-{y}把取整函数拆开。把左边和右边都做这个分解，看看不等式变成什么。 | 左边⌊kx⌋/k=(kx-{kx})/k=x-{kx}/k，求和= nx-∑{kx}/k。右边⌊nx⌋=nx-{nx}。不等式变为{nx}≤∑_{k=1}^n {kx}/k。需要证明小数部分的不等式。 |
| 5 | 思维操作引导 | 0.3 | 现在需要证明{nx}≤∑{kx}/k。设a(k)={kx}。小数部分有次可加性{a+b}≤{a}+{b}。想想怎么用这个性质和数学归纳法来证明。 | 由次可加性a(k+m)≤a(k)+a(m)。对n用强归纳法。n=0平凡。n>0时选使a(m)/m最小的m，a(n)≤a(n-m)+a(m)，a(n-m)由归纳假设控制，a(m)由最小性控制尾部求和。 |
| 6 | 推进 | 0.5 | 选定使a(m)/m最小的m后，具体把∑_{k=1}^n a(k)/k拆成两部分，分别用归纳假设和最小性来控制。 | 拆分为∑_{k=1}^{n-m}+∑_{k=n-m+1}^{n}。前半由归纳假设a(n-m)≤∑_{k=1}^{n-m}a(k)/k。后半每个a(k)/k≥a(m)/m共m项所以≥m·a(m)/m=a(m)。合并a(n)≤a(n-m)+a(m)≤∑_{k=1}^n a(k)/k。 |
| 7 | 能量传递引导 | 0.8 | 回顾整个证明：从取整分解到小数部分不等式，再到次可加性+强归纳+最小值选取。每一步都自然衔接。现在把完整证明写出来。 | 完整证明：1)分解⌊kx⌋=kx-{kx}转化为{nx}≤∑{kx}/k；2)a(k)={kx}有次可加性；3)强归纳选最小a(m)/m的m拆分求和，归纳假设控制前半，最小性控制后半。QED。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1+R2+R6+R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4+R5）
- level_sum: 0.7+0.6+0.5+0.4+0.3+0.5+0.8 = 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
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
- problem_type: inequality_proof
- structure_features: 含取整函数的求和不等式，左边是n项加权取整值之和，右边是单项取整值。需要通过取整函数分解转化为小数部分不等式，再用归纳法证明。
- key_objects: 取整函数⌊·⌋、小数部分{·}、求和∑、正实数x、非负整数n、次可加性

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["分解转化——将取整函数分解为整数部分减小数部分", "放缩试探——先试直接放缩发现不够紧", "归纳结构——强归纳法配合最小值选取", "次可加性利用——利用小数部分的次可加性建立递推", "求和拆分——按最小值位置拆分求和分别控制"]
- primary_pattern: 分解转化——将取整函数不等式通过⌊y⌋=y-{y}分解转化为小数部分不等式
- knowledge_required: ["取整函数的定义与性质", "小数部分（fractional part）的概念", "小数部分的次可加性{a+b}≤{a}+{b}", "强数学归纳法", "有限集上最小值的存在性"]
- key_insight: 选取使a(m)/m最小的m来拆分求和——归纳假设控制前半段，最小性控制后半段，两者恰好拼出完整不等式

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 取整函数的直接放缩语言（⌊kx⌋≤kx的粗糙估计）
- translation_to: 小数部分的次可加性+强归纳语言（通过⌊y⌋=y-{y}分解转化为{nx}≤∑{kx}/k，再用次可加性和归纳法）
- translation_type: method_translation（方法翻译——从直接放缩方法翻译到分解+归纳方法）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "inequality_proof", ai_method_type: "direct_calculation", gap_type: "method_translation"}
- tell_small_concepts: ["取整函数", "小数部分", "次可加性", "强归纳法", "最小值选取", "求和拆分"]
- expected_ai_method: 直接放缩——用⌊kx⌋≤kx得到∑⌊kx⌋/k≤nx，但nx≥⌊nx⌋所以放缩太松，无法完成证明
- correct_method: 分解转化+次可加性+强归纳——将⌊kx⌋=kx-{kx}分解后转化为小数部分不等式，利用次可加性和强归纳法，选取最小a(m)/m拆分求和完成归纳

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是，inequality_proof/direct_calculation/method_translation均可归入已有类别
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是，与已有值粒度一致
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够，三个维度可以区分
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化

**拓扑进化建议**（如有）：无，当前拓扑分类足够使用

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

**局部tell_hint_pairs详情**：

R1: tell="面对含取整函数的求和不等式，AI可以描述结构但未识别取整函数分解的必要性", hint="观察题目中出现的数学对象和结构特征", hint_level=0.7, situation_type="纯元认知观察", is_knowledge_bottleneck=false, tell_topology={problem_type:"inequality_proof",ai_method_type:"direct_calculation",gap_type:"method_problem_mismatch"}, tell_small_concepts=["取整函数","求和结构","单项与多项对应"]

R2: tell="AI列举了多种工具但未识别小数部分分解是关键路径", hint="列出处理取整函数的所有可能方向", hint_level=0.6, situation_type="自由列举", is_knowledge_bottleneck=false, tell_topology={problem_type:"inequality_proof",ai_method_type:"direct_calculation",gap_type:"method_translation"}, tell_small_concepts=["取整函数性质","小数部分分解","放缩法","归纳法"]

R3: tell="AI尝试直接放缩⌊kx⌋≤kx得到∑≤nx，但nx≥⌊nx⌋放缩太松，陷入死路", hint="试试直接放缩看看够不够", hint_level=0.5, situation_type="小尝试", is_knowledge_bottleneck=false, tell_topology={problem_type:"inequality_proof",ai_method_type:"direct_calculation",gap_type:"method_problem_mismatch"}, tell_small_concepts=["放缩法","精度不足","小数部分差距"]

R4: tell="AI知道放缩不够但未想到用⌊y⌋=y-{y}分解来转化不等式", hint="用分解⌊y⌋=y-{y}把取整函数拆开", hint_level=0.4, situation_type="思维操作引导", is_knowledge_bottleneck=true, tell_topology={problem_type:"inequality_proof",ai_method_type:"direct_calculation",gap_type:"knowledge_gap"}, tell_small_concepts=["取整函数分解","小数部分","不等式转化"]

R5: tell="AI已将不等式转化为{nx}≤∑{kx}/k，但不知道如何利用次可加性和归纳法来证明", hint="利用小数部分次可加性和强归纳法", hint_level=0.3, situation_type="思维操作引导", is_knowledge_bottleneck=true, tell_topology={problem_type:"inequality_proof",ai_method_type:"direct_calculation",gap_type:"knowledge_gap"}, tell_small_concepts=["次可加性","强归纳法","最小值选取","求和拆分"]

R6: tell="AI已选定最小a(m)/m的m，但需要具体拆分求和并分别控制两部分", hint="把求和拆成两部分分别用归纳假设和最小性控制", hint_level=0.5, situation_type="推进", is_knowledge_bottleneck=false, tell_topology={problem_type:"inequality_proof",ai_method_type:"logical_deduction",gap_type:"structural_transformation"}, tell_small_concepts=["求和拆分","归纳假设","最小性控制","尾部求和"]

R7: tell="AI已完成所有关键步骤，需要整合写出完整证明", hint="回顾整个证明写出完整解答", hint_level=0.8, situation_type="能量传递引导", is_knowledge_bottleneck=false, tell_topology={problem_type:"inequality_proof",ai_method_type:"logical_deduction",gap_type:"method_translation"}, tell_small_concepts=["证明整合","完整叙述","QED"]

**全局tell_hint_pairs详情**：

G1 (path_feature型):
- scope_type: "path_feature"
- scope: "从直接放缩失败到分解转化再到归纳证明的完整路径"
- observation_point: null
- tell: "直接放缩⌊kx⌋≤kx只能得到∑≤nx，但目标⌊nx⌋=nx-{nx}比nx小一个小数部分。完整路径需要：先识别放缩精度不足→分解取整函数转化问题→利用次可加性+强归纳+最小值选取完成证明。这条路径的关键转折是从'直接估计取整值'翻译到'估计小数部分'。"
- hint: "当直接放缩精度不够时，尝试分解取整函数⌊y⌋=y-{y}将问题转化到小数部分空间，再利用小数部分的代数性质（次可加性）配合归纳法"
- hint_level: 0.5
- generalizability: "high——'直接放缩不够时分解转化到更精细的空间'是一个通用的解题模式，适用于含取整函数、绝对值等分段函数的不等式"
- why_not_visible_locally: "在R3的局部视角中，AI只看到'放缩太松'这个失败信号，但看不到'分解取整函数→小数部分空间'这个完整转化路径。转化路径需要同时知道小数部分的次可加性和归纳法的配合方式，这些在局部步骤中不可见。"
- tell_topology: {problem_type:"inequality_proof",ai_method_type:"direct_calculation",gap_type:"method_translation"}
- tell_small_concepts: ["放缩精度不足","取整函数分解","小数部分转化","次可加性","强归纳法"]

G2 (implicit型):
- scope_type: "implicit"
- scope: "选取最小a(m)/m来拆分求和的策略蕴含在整个归纳结构中"
- observation_point: "R5"
- tell: "在强归纳法中，如何选取拆分点m是隐含的关键决策。解答选取使a(m)/m最小的m，这样尾部m项每项都≥a(m)/m，总和≥a(m)，恰好与次可加性给出的a(n)≤a(n-m)+a(m)中的a(m)匹配。这个'最小值选取'策略不是显而易见的——它同时服务于两个目的：控制尾部求和的下界和匹配次可加性的分解。"
- hint: "在归纳法中需要拆分求和时，考虑选取使某种比值最小（或最大）的元素作为拆分点，使得拆分后的两部分能分别被归纳假设和极值性质控制"
- hint_level: 0.4
- generalizability: "medium——'选取极值元素作为归纳拆分点'在涉及求和不等式的归纳证明中有一定泛化性，但需要具体问题中存在合适的比值结构"
- why_not_visible_locally: "在R5的局部视角中，AI看到'需要用次可加性和归纳法'，但'选取最小a(m)/m'这个具体策略在局部步骤中不可见——它是一个全局性的设计决策，需要同时考虑次可加性分解的形式和尾部求和的控制方式才能自然得出。只有看到完整的归纳结构（R6）后才能理解为什么选最小值。"
- tell_topology: {problem_type:"inequality_proof",ai_method_type:"logical_deduction",gap_type:"structural_transformation"}
- tell_small_concepts: ["最小值选取","归纳拆分点","尾部求和控制","次可加性匹配"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会用直接放缩⌊kx⌋≤kx得到∑≤nx，但无法跨越nx到⌊nx⌋的差距。即使想到分解⌊y⌋=y-{y}，也很难想到利用小数部分次可加性配合强归纳法，更难想到选取最小a(m)/m作为归纳拆分点的策略。关键瓶颈在于从'小数部分不等式'到'次可加性+强归纳+最小值选取'的方法翻译。
- suitable_for_poc: ["tell端验证——测试系统能否从AI的放缩失败中识别出需要方法翻译的tell", "hint端验证——测试注入'分解取整函数'方向后AI能否继续推进", "path_feature型tell验证——测试完整路径特征的去特化过滤"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON

**⚠️ 完整字段清单（逐项检查，不能遗漏）**：
- [ ] _key（=problem_id）
- [ ] source_id
- [ ] source_dataset
- [ ] schema_version（=3）
- [ ] problem_text
- [ ] solution_text
- [ ] solution_summary
- [ ] domain
- [ ] subfield
- [ ] answer_type
- [ ] answer（**⚠️ 必填，不能为None**。proof类型填要证明的结论，如"sum >= ..."；existence_construction类型填构造的存在性结论；numerical类型填数值答案）
- [ ] problem_type
- [ ] solution_method_type
- [ ] structure_features
- [ ] key_objects
- [ ] thinking_patterns
- [ ] primary_pattern
- [ ] knowledge_required
- [ ] key_insight
- [ ] translation_from
- [ ] translation_to
- [ ] translation_type
- [ ] tell_topology（profile级）
- [ ] tell_small_concepts（profile级）
- [ ] expected_ai_method
- [ ] correct_method
- [ ] tell_hint_pairs（每个pair含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [ ] global_tell_hint_pairs（每个pair含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [ ] bare_ai_expected
- [ ] bare_ai_error_prediction
- [ ] suitable_for_poc
- [ ] discriminates_levels
- [ ] qa_sequence（含rounds数组和stats子对象）
- [ ] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

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
2. 更新`problem_extraction_progress`集合中`_key="329326"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa1981p5"
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
    '_key': '329326',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa1981p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa1981p5')
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
- problem_id: compfiles_usa1981p5
- solution_method_type: decomposition_induction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，当前拓扑分类（inequality_proof/direct_calculation/method_translation等）足够使用
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
