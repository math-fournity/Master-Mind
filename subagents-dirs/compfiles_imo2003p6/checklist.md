# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2003p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2003P6.lean
- **来源**: IMO 2003 P6
- **ArangoDB progress记录_key**: 329188（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2003P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设p为素数。证明存在素数q，使得对任意整数n，n^p - p不被q整除。
- 解答核心思路（1-2句话）：构造N=(p^p-1)/(p-1)=1+p+...+p^(p-1)，找到N的素因子q满足q≢1(mod p²)，然后假设n^p≡p(mod q)推出ord(n)|p²，分d=1,p,p²三种情况及n≡0的情况导出矛盾。
- 解答关键步骤列表：
  1. p=2时取q=5，直接验证n²-2≢0(mod 5)（检查n mod 5的所有剩余系）
  2. p>2时令N=Σ_{i=0}^{p-1} p^i，证明N≠0且N mod p² = p+1 ≠ 1
  3. 用引理exists_prime_mod_m_ne_1_and_dvd：若n%m≠1且m≠1，则存在素数q|n且q%m≠1。取m=p²，得到素数q|N且q≢1(mod p²)
  4. 证明q|p^p-1（因为N|(p^p-1)，具体N*(p-1)=p^p-1）
  5. 反证：假设存在n使n^p≡p(mod q)，则n^(p²)=(n^p)^p≡p^p≡1(mod q)
  6. 设d=ord(n mod q)，则d|p²，所以d=p^k，k∈{0,1,2}
  7. k<2（d=1或d=p）时：n^p≡1(mod q)，结合n^p≡p得p≡1(mod q)，即q|p-1。但gcd(N,p-1)=1（因N≡1(mod p-1)），而q|N，矛盾
  8. k=2且n≡0(mod q)时：p≡0(mod q)即q|p，但gcd(N,p)=1（因N≡1(mod p)），矛盾
  9. k=2且n≢0(mod q)时：由Fermat小定理n^(q-1)≡1(mod q)，所以p²|(q-1)即q≡1(mod p²)，与q≢1(mod p²)矛盾

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
| 1 | 纯元认知观察 | 0.7 | 这个题目要求我们做什么？关键数学对象是什么？p和q之间需要满足什么关系？ | 题目要求证明：对任意素数p，存在素数q，使得对所有整数n，q不整除n^p-p。关键对象是素数p和q，以及表达式n^p-p。我们需要找到q使得n^p≢p(mod q)对所有n成立。 |
| 2 | 自由列举 | 0.6 | 要找到一个素数q使得n^p≢p(mod q)对所有n成立，有哪些可能的方向？ | 方向1：直接取q=某个固定素数验证。方向2：利用Fermat小定理n^(q-1)≡1(mod q)来约束。方向3：考虑n^p在mod q下的取值范围。方向4：反证法——假设存在n使得q|n^p-p，推出对q的约束。方向5：构造特殊的数N，从N的素因子中选取q。 |
| 3 | 小尝试 | 0.4 | 试试方向1：对p=2，能找到具体的q吗？对一般的p呢？ | p=2时，取q=5：n² mod 5 ∈ {0,1,4}，而2 mod 5=2，所以n²-2≢0(mod 5)。但对一般p，直接试素数没有系统方法，因为需要保证对所有n成立，搜索空间太大。 |
| 4 | 思维操作引导 | 0.5 | 用反证法思考：如果存在n使得n^p≡p(mod q)，这告诉我们关于q的什么信息？特别地，如果同时有q|p^p-1（即p^p≡1(mod q)），能否结合这两个条件？ | 如果n^p≡p(mod q)且p^p≡1(mod q)，那么n^(p²)=(n^p)^p≡p^p≡1(mod q)。这意味着n在mod q下的乘法阶整除p²。 |
| 5 | 思维操作引导 | 0.6 | n的阶d整除p²，所以d∈{1,p,p²}。每种情况下能推出什么结论？ | d=1：n≡1(mod q)，所以p≡1(mod q)，即q|p-1。d=p：n^p≡1(mod q)，结合n^p≡p得p≡1(mod q)，同样q|p-1。d=p²：由Fermat小定理n^(q-1)≡1(mod q)，所以p²|q-1，即q≡1(mod p²)。所以如果q≢1(mod p²)且q不整除p-1，就能避免所有情况。 |
| 6 | 思维操作引导 | 0.5 | 我们需要q满足：(1)q|p^p-1，(2)q≢1(mod p²)。如何构造这样的q？考虑N=(p^p-1)/(p-1)=1+p+p²+...+p^(p-1)。 | N=(p^p-1)/(p-1)。如果q|N且q≢1(mod p²)，则q|p^p-1。需要证明N有素因子q满足q≢1(mod p²)。计算N mod p²：N≡1+p(mod p²)（因为p^i≡0(mod p²)对i≥2），所以N mod p²=p+1≠1。如果N的所有素因子都≡1(mod p²)，则N≡1(mod p²)，矛盾。所以存在q|N且q≢1(mod p²)。 |
| 7 | 能量传递引导 | 0.7 | 现在验证所有情况都导出矛盾，完成证明。 | 取q|N且q≢1(mod p²)。假设存在n使n^p≡p(mod q)。d=1或d=p时，p≡1(mod q)，即q|p-1。但q|N且gcd(N,p-1)=1（因为N≡1(mod p-1)），矛盾。d=p²且n≡0时：p≡0(mod q)即q|p，但gcd(N,p)=1（因为N≡1(mod p)），矛盾。d=p²且n≢0时：q≡1(mod p²)，与q≢1(mod p²)矛盾。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 3（R1+R2+R7）
- knowledge_rounds（思维操作引导的轮数）: 4（R4+R5+R6+R7中R7含知识但归为能量传递引导）
- level_sum: 0.7+0.6+0.4+0.5+0.6+0.5+0.7 = 4.0
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R5（需要知道乘法阶的概念及其整除性质）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R6（需要构造N并证明其素因子满足特定模条件）

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
- problem_type: structural_existence（证明存在满足特定条件的素数q）
- structure_features: 存在性命题，需要对所有整数n成立的全称约束，涉及素数p和q的模运算关系，需要构造辅助数N并利用其素因子性质
- key_objects: ["素数p", "素数q", "整数n", "表达式n^p-p", "辅助数N=(p^p-1)/(p-1)", "乘法阶ord(n mod q)", "模p²条件"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["反证法", "构造性存在证明", "情况分析（阶的分情况讨论）", "模运算推导", "辅助数构造", "互素性论证"]
- primary_pattern: 构造性存在证明（构造辅助数N，从中选取满足条件的素数q，再用反证法证明q满足要求）
- knowledge_required: ["乘法阶（multiplicative order）", "Fermat小定理", "素因子分解", "模运算", "几何级数", "gcd与互素性", "Zmod q上的群结构"]
- key_insight: 构造N=(p^p-1)/(p-1)并找到其素因子q满足q≢1(mod p²)，这样n^p≡p(mod q)推出ord(n)|p²，而q≢1(mod p²)排除了d=p²的情况，q不整除p-1排除了d=1,p的情况

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 存在性命题（"存在素数q使得对所有n，q不整除n^p-p"）
- translation_to: 阶论论证（"构造N，找q|N且q≢1(mod p²)，用ord(n)|p²分情况导出矛盾"）
- translation_type: structural_transformation（将存在性命题翻译为构造辅助数+阶论反证的结构性论证）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "enumeration_brute_force", gap_type: "knowledge_gap"}
- tell_small_concepts: ["乘法阶", "几何级数构造", "模p²条件", "素因子选取", "反证法", "Fermat小定理", "gcd互素"]
- expected_ai_method: bare AI会尝试直接枚举素数q验证，或用Fermat小定理直接推导，但无法系统构造辅助数N和利用乘法阶论证
- correct_method: 构造N=(p^p-1)/(p-1)，找到其素因子q满足q≢1(mod p²)，利用n^p≡p(mod q)推出ord(n)|p²，分d=1,p,p²及n≡0四种情况导出矛盾

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 可以。structural_existence + enumeration_brute_force + knowledge_gap 完全覆盖。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 一致。三个维度都是抽象级别。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。不同轮次的pair通过不同的tell_topology区分（如R5是knowledge_gap，R6是method_translation，R7是method_problem_mismatch）。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。现有分类体系充分。

**拓扑进化建议**（如有）：无。现有拓扑分类体系完全覆盖本题需求。

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

R1: tell="AI面对存在性命题，尚未识别出需要用反证法和阶论", hint="描述题目结构，识别已知条件和目标", hint_level=0.7, situation_type="纯元认知观察", is_knowledge_bottleneck=false
- tell_topology: {problem_type: "structural_existence", ai_method_type: "enumeration_brute_force", gap_type: "method_problem_mismatch"}
- tell_small_concepts: ["存在性命题", "素数", "整除关系"]

R2: tell="AI列出方向但未识别阶论和构造N的关键方向", hint="列出所有可能方向，包括反证法和构造法", hint_level=0.6, situation_type="自由列举", is_knowledge_bottleneck=false
- tell_topology: {problem_type: "structural_existence", ai_method_type: "enumeration_brute_force", gap_type: "knowledge_gap"}
- tell_small_concepts: ["Fermat小定理", "反证法", "构造法"]

R3: tell="AI尝试直接取素数但无法系统化，搜索空间过大", hint="试p=2的特殊情况取q=5验证", hint_level=0.4, situation_type="小尝试", is_knowledge_bottleneck=false
- tell_topology: {problem_type: "structural_existence", ai_method_type: "enumeration_brute_force", gap_type: "search_space_estimation"}
- tell_small_concepts: ["特殊情况验证", "模运算", "二次剩余"]

R4: tell="AI未意识到n^p≡p和p^p≡1可以结合推出n^(p²)≡1", hint="用反证法，假设q|n^p-p，结合q|p^p-1推导n^(p²)≡1", hint_level=0.5, situation_type="思维操作引导", is_knowledge_bottleneck=false
- tell_topology: {problem_type: "structural_existence", ai_method_type: "logical_deduction", gap_type: "structural_transformation"}
- tell_small_concepts: ["反证法", "模等式结合", "幂次代入"]

R5: tell="AI不知道乘法阶的概念及其整除性质", hint="分析n在mod q下的阶d，d|p²所以d∈{1,p,p²}", hint_level=0.6, situation_type="思维操作引导", is_knowledge_bottleneck=true
- tell_topology: {problem_type: "structural_existence", ai_method_type: "direct_calculation", gap_type: "knowledge_gap"}
- tell_small_concepts: ["乘法阶", "阶整除", "Fermat小定理"]

R6: tell="AI需要构造N=(p^p-1)/(p-1)并证明其有合适的素因子", hint="构造N=1+p+...+p^(p-1)，分析N mod p²=p+1≠1，用反证法证明存在素因子q≢1(mod p²)", hint_level=0.5, situation_type="思维操作引导", is_knowledge_bottleneck=false
- tell_topology: {problem_type: "structural_existence", ai_method_type: "algebraic_identity", gap_type: "method_translation"}
- tell_small_concepts: ["几何级数", "模p²分析", "素因子存在性"]

R7: tell="AI需要验证所有情况（d=1,p,p²及n≡0）都导出矛盾", hint="逐一验证每种情况，利用gcd(N,p-1)=1和gcd(N,p)=1和q≢1(mod p²)导出矛盾", hint_level=0.7, situation_type="能量传递引导", is_knowledge_bottleneck=false
- tell_topology: {problem_type: "structural_existence", ai_method_type: "case_by_case", gap_type: "method_problem_mismatch"}
- tell_small_concepts: ["gcd互素", "情况分析", "矛盾推导"]

**全局tell_hint_pairs详情**：

G1 (path_feature):
- scope_type: "path_feature"
- scope: "整个证明路径：从构造N到阶论矛盾"
- observation_point: null
- tell: "证明的关键路径是构造N=(p^p-1)/(p-1)，找到其素因子q满足q≢1(mod p²)，然后利用n^p≡p(mod q)推出ord(n)|p²，分情况导出矛盾"
- hint: "考虑几何级数N=1+p+...+p^(p-1)的素因子，选择满足特定模条件的素因子作为q"
- hint_level: 0.8
- generalizability: "high - 构造辅助数并利用其素因子性质是数论存在性证明的通用模式"
- why_not_visible_locally: "N的选择动机完全来自后续的阶论论证——只有知道ord(n)|p²需要q≢1(mod p²)且q|p^p-1，才能理解为什么要构造这个特定的N。局部步骤中无法预见这个构造的目的"
- tell_topology: {problem_type: "structural_existence", ai_method_type: "algebraic_identity", gap_type: "method_translation"}
- tell_small_concepts: ["几何级数构造", "素因子选取", "模条件", "阶论矛盾"]

G2 (implicit):
- scope_type: "implicit"
- scope: "n^p≡p(mod q)与p^p≡1(mod q)的结合推出n^(p²)≡1(mod q)"
- observation_point: "R4"
- tell: "从n^p≡p(mod q)和p^p≡1(mod q)可以推出n^(p²)=(n^p)^p≡p^p≡1(mod q)，这蕴含ord(n)|p²"
- hint: "将n^p≡p代入(n^p)^p的计算中，结合q|p^p-1得到n^(p²)≡1"
- hint_level: 0.6
- generalizability: "medium - 幂次代入结合是模运算中的常见技巧，但需要识别两个独立条件的结合点"
- why_not_visible_locally: "n^p≡p来自反证假设，p^p≡1来自q|N的构造，两者来自证明的不同部分。在局部视角中，只看其中一个条件无法预见它们的结合会产生阶的约束"
- tell_topology: {problem_type: "structural_existence", ai_method_type: "logical_deduction", gap_type: "structural_transformation"}
- tell_small_concepts: ["幂次代入", "模等式结合", "阶约束"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接枚举素数q验证或用Fermat小定理直接推导，但无法系统构造辅助数N=(p^p-1)/(p-1)和利用乘法阶论证。具体错误：(1)不知道构造N的动机；(2)不知道乘法阶的概念；(3)无法将n^p≡p和p^p≡1结合推出n^(p²)≡1；(4)无法分情况讨论ord(n)的所有可能值。
- suitable_for_poc: ["tell_extraction", "hint_injection", "topology_classification", "knowledge_bottleneck_detection"]
- discriminates_levels: true（IMO P6级别极高，bare AI几乎必然失败，有提示后可能推进到阶论论证）

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
2. 更新`problem_extraction_progress`集合中`_key="329188"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2003p6"
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
    '_key': '329188',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2003p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2003p6')
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
- problem_id: compfiles_imo2003p6
- solution_method_type: constructive_existence_proof
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature + 1个implicit）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，现有拓扑分类体系完全覆盖本题需求
- 是否遇到异常: 否，入库和验证均一次通过

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
