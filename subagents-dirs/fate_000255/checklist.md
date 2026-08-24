# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000255
- **文件路径**: subagents-dirs/fate_000255/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396365（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000255/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Prove that if #G = 396 then G is not simple. 即：设G是有限群，|G|=396，证明G不是单群。
- 解答核心思路（1-2句话）：利用Sylow定理分析n₁₁和n₃的可能值，通过元素计数（特别是N_G(P₁₁)≅C₃₃产生的240个33阶元素）排除困难情形n₃=22，其余情形用正规Sylow子群或群作用论证处理。
- 解答关键步骤列表：
  1. 分解 396 = 2² × 3² × 11
  2. Sylow 11: n₁₁ | 36, n₁₁ ≡ 1 (mod 11) → n₁₁ ∈ {1, 12}
  3. 若 n₁₁ = 1，Sylow 11-子群正规，G非单群
  4. 若 n₁₁ = 12，|N_G(P₁₁)| = 33 = 3×11，因3∤10故N_G(P₁₁)≅C₃₃（循环），每个N_G(P₁₁)含20个33阶元素，共12×20=240个33阶元素（互不相同），加上120个11阶元素和单位元共361个元素
  5. Sylow 3: n₃ | 44, n₃ ≡ 1 (mod 3) → n₃ ∈ {1, 4, 22}
  6. 若 n₃ = 1，Sylow 3-子群正规，G非单群
  7. 若 n₃ = 4，共轭作用给出同态φ: G → S₄，|G|=396 > 24=|S₄|，故ker(φ)非平凡，G非单群
  8. 若 n₃ = 22，22个9阶Sylow 3-子群两两交集至多3个元素，其并集至少9+21×6=135个元素。361+135-1=495 > 396，矛盾。故n₃≠22
  9. 所有情形下G均非单群 □

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
| 1 | 纯元认知观察 | 0.3 | 这道题要你证明什么？\|G\|=396这个数字的结构是什么？"G不是单群"意味着什么？ | \|G\|=396=2²×3²×11，三个素因子。G不是单群意味着G存在非平凡正规子群。需要用Sylow定理分析各Sylow子群的数量，找到正规子群或导出矛盾。 |
| 2 | 自由列举 | 0.5 | 对于证明有限群非单群，你有哪些可用的工具和策略？请列出所有你能想到的方向。 | 1) Sylow定理：若n_p=1则Sylow p-子群正规；2) 群作用：共轭作用给出到对称群的同态，核是非平凡正规子群；3) 元素计数：计算特定阶元素个数导出矛盾；4) 正规化子分析：分析N_G(P)的结构；5) Burnside定理（但396有三个素因子，不适用）。 |
| 3 | 小尝试 | 0.4 | 先试试Sylow 11-子群。计算n₁₁的可能值，看看能得出什么。 | n₁₁ \| 36且n₁₁ ≡ 1 (mod 11)。36的因子中≡1 mod 11的：1和12。若n₁₁=1，Sylow 11-子群正规，G非单群。若n₁₁=12，需要继续分析。目前看起来n₁₁=12是困难情形。 |
| 4 | 思维操作引导 | 0.3 | 在n₁₁=12的情形下，计算正规化子N_G(P₁₁)的阶。然后判断N_G(P₁₁)的结构——它是循环群吗？为什么？如果是循环群，它包含多少个33阶元素？ | \|N_G(P₁₁)\|=396/12=33=3×11。因为3∤(11-1)=10，所以N_G(P₁₁)是循环群C₃₃。C₃₃中φ(33)=20个元素阶为33。12个正规化子共给出12×20=240个33阶元素（每个33阶元素在唯一一个N_G(P₁₁)中）。加上120个11阶元素和单位元，共361个元素。 |
| 5 | 推进 | 0.5 | 现在转向Sylow 3-子群。计算n₃的可能值，并逐一分析每种情况。 | n₃ \| 44且n₃ ≡ 1 (mod 3)。44的因子中≡1 mod 3的：1, 4, 22。n₃=1时Sylow 3-子群正规，完成。n₃=4时，共轭作用给出同态G→S₄，\|G\|=396>24=\|S₄\|，核非平凡，G非单群。n₃=22是困难情形，需要进一步分析。 |
| 6 | 思维操作引导 | 0.2 | 在n₃=22的情形下，我们已经有361个元素（1个单位元+120个11阶+240个33阶）。现在考虑22个9阶Sylow 3-子群：任意两个不同的9阶子群的交集至多有多少元素？它们的并集至少有多少元素？这个数字加上361是否超过396？ | 两个不同的9阶子群交集至多3个元素（阶为1或3的子群）。并集至少9+21×6=135个元素（第一个贡献9个，之后每个至少贡献6个新元素）。361+135-1=495 > 396，矛盾！所以n₃=22不可能。所有情形都导致G非单群。 |
| 7 | 能量传递引导 | 0.7 | 回顾整个证明的结构：你通过Sylow计数分情况讨论，利用循环正规化子的结构产生元素计数约束，成功排除了所有困难情形。这种"Sylow计数+元素计数"的组合策略在非单群证明中非常有力。请总结证明的完整逻辑链。 | 证明逻辑链：396=2²×3²×11 → n₁₁∈{1,12} → n₁₁=1则完成 → n₁₁=12则N_G(P₁₁)≅C₃₃给出240个33阶元素 → n₃∈{1,4,22} → n₃=1则完成 → n₃=4则S₄作用给出非平凡核 → n₃=22则元素计数矛盾(361+135>396) → 所有情形G非单群 □ |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1+R2+R5+R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4+R6）
- level_sum: 0.3+0.5+0.4+0.3+0.5+0.2+0.7 = 2.9
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6"
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
- problem_type: structural_existence（证明存在非平凡正规子群，即非单群性）
- structure_features: 素数分解396=2²×3²×11；Sylow计数约束n₁₁∈{1,12}和n₃∈{1,4,22}；分情况讨论结构；元素计数矛盾作为困难情形排除手段；群作用同态到小对称群作为中间情形处理手段
- key_objects: G（396阶有限群），Sylow 11-子群（11阶），Sylow 3-子群（9阶），正规化子N_G(P₁₁)（33阶循环群），33阶元素，S₄群（用于n₃=4情形的群作用目标）

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["Sylow定理计数（计算n_p的可能值）", "分情况讨论（case analysis on n₁₁ and n₃）", "元素计数矛盾（counting elements of specific orders to exceed |G|）", "群作用论证（conjugation action to symmetric group, kernel argument）", "正规化子结构分析（analyzing N_G(P) structure, cyclic group classification）"]
- primary_pattern: 元素计数矛盾（element counting contradiction）
- knowledge_required: ["Sylow三大定理", "循环群分类定理（pq阶群当p∤(q-1)时循环）", "Euler函数φ的计算", "群作用与同态基本定理", "单群定义与正规子群", "子群交集的阶约束"]
- key_insight: 当n₁₁=12时，N_G(P₁₁)≅C₃₃是循环群，产生240个33阶元素，加上120个11阶元素和单位元共361个，剩余空间不足以容纳22个9阶Sylow 3-子群（并集至少135个元素），361+135>396矛盾。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: Sylow定理计数（计算n_p的可能值，分情况讨论）
- translation_to: 元素计数矛盾（计算复合阶元素个数，利用元素预算约束导出矛盾）
- translation_type: method_translation（从Sylow计数方法翻译到元素计数方法，关键翻译步骤是识别正规化子的循环结构产生复合阶元素）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "case_by_case", gap_type: "knowledge_gap"}
- tell_small_concepts: ["Sylow counting", "cyclic normalizer", "element counting", "composite order elements", "element budget contradiction", "conjugation action to S₄"]
- expected_ai_method: bare AI会使用Sylow定理分情况讨论，能处理n₁₁=1、n₃=1、n₃=4等简单情形，但在n₃=22时会卡住——可能尝试共轭作用到S₂₂但|S₂₂|太大无法导出矛盾，不会想到利用N_G(P₁₁)的循环结构产生33阶元素来做元素计数
- correct_method: 利用N_G(P₁₁)≅C₃₃的循环结构计算240个33阶元素，结合22个Sylow 3-子群并集下界135，得到361+135>396的元素计数矛盾排除n₃=22

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是。structural_existence（已有）、case_by_case（已有）、knowledge_gap（已有）均可归入。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是。三个维度的值都是中等偏抽象的粒度，与已有值一致。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 是。三个维度足够。这道题的独特性体现在small_concepts层面（cyclic normalizer, composite order elements, element budget），不需要新维度。
- [x] 如果发现拓扑分类需要进化，在此写出建议：

**拓扑进化建议**（如有）：无。当前三维度拓扑分类足以描述这道题的tell结构。这道题的核心特征——"利用正规化子的循环结构产生复合阶元素，再用元素预算约束排除困难情形"——可以通过small_concepts层面的概念词充分表达，不需要在拓扑层面新增维度。

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
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 2 个，implicit型: 1 个

**局部tell_hint_pairs详情**：

R1: tell="AI看到群论非单群证明题，识别了396的素数分解但尚未识别关键证明策略", hint="描述题目结构：396的素数分解、单群定义、Sylow定理作为工具", hint_level=0.3, situation_type="纯元认知观察", is_knowledge_bottleneck=false, tell_topology={problem_type:"structural_existence", ai_method_type:"logical_deduction", gap_type:"method_problem_mismatch"}, tell_small_concepts=["prime factorization", "simple group definition", "Sylow theorems"]

R2: tell="AI列举了Sylow定理、群作用、元素计数等方向，但未识别元素计数是关键策略", hint="列出所有可用工具：Sylow定理、群作用同态、元素计数、正规化子分析", hint_level=0.5, situation_type="自由列举", is_knowledge_bottleneck=false, tell_topology={problem_type:"structural_existence", ai_method_type:"enumeration_brute_force", gap_type:"knowledge_gap"}, tell_small_concepts=["Sylow theorems", "group action homomorphism", "element counting", "normalizer analysis", "Burnside theorem"]

R3: tell="AI计算n₁₁∈{1,12}，处理了n₁₁=1但不知如何处理n₁₁=12", hint="计算n₁₁的可能值，分析每种情况", hint_level=0.4, situation_type="小尝试", is_knowledge_bottleneck=false, tell_topology={problem_type:"structural_existence", ai_method_type:"case_by_case", gap_type:"knowledge_gap"}, tell_small_concepts=["Sylow 11 counting", "n₁₁ constraints", "divisibility and congruence"]

R4: tell="AI在n₁₁=12处卡住，不知N_G(P₁₁)的循环结构是关键资源", hint="计算N_G(P₁₁)的阶，判断其循环性，计算33阶元素个数", hint_level=0.3, situation_type="思维操作引导", is_knowledge_bottleneck=true, tell_topology={problem_type:"structural_existence", ai_method_type:"direct_calculation", gap_type:"knowledge_gap"}, tell_small_concepts=["normalizer order", "cyclic group classification", "Euler totient", "composite order elements", "coprimality condition"]

R5: tell="AI能处理n₃=1和n₃=4但在n₃=22处卡住，不知如何排除此情形", hint="计算n₃可能值，逐一分析n₃=1（正规）、n₃=4（S₄作用）、n₃=22（待定）", hint_level=0.5, situation_type="推进", is_knowledge_bottleneck=false, tell_topology={problem_type:"structural_existence", ai_method_type:"case_by_case", gap_type:"structural_transformation"}, tell_small_concepts=["Sylow 3 counting", "conjugation action to S₄", "kernel argument", "order comparison"]

R6: tell="AI在n₃=22处完全卡住，可能尝试S₂₂作用但|S₂₂|太大无法导出矛盾，未意识到可用已有361个元素做预算约束", hint="利用已计数的361个元素，计算22个9阶子群并集下界，导出元素总数矛盾", hint_level=0.2, situation_type="思维操作引导", is_knowledge_bottleneck=true, tell_topology={problem_type:"structural_existence", ai_method_type:"direct_calculation", gap_type:"knowledge_gap"}, tell_small_concepts=["element budget", "subgroup intersection bound", "union lower bound", "counting contradiction", "composite order element count"]

R7: tell="AI已完成所有情形分析，需要整合逻辑链形成完整证明", hint="总结证明逻辑链，确认所有情形已覆盖", hint_level=0.7, situation_type="能量传递引导", is_knowledge_bottleneck=false, tell_topology={problem_type:"structural_existence", ai_method_type:"logical_deduction", gap_type:"method_problem_mismatch"}, tell_small_concepts=["case analysis summary", "proof logic chain", "Sylow counting strategy", "element counting strategy"]

**全局tell_hint_pairs详情**：

Global 1 (path_feature):
- scope: "整个证明路径：从n₁₁=12的正规化子结构到n₃=22的元素计数矛盾"
- observation_point: null
- tell: "证明需要跨情况整合元素计数：n₁₁=12产生240个33阶元素（361个已计数元素），这个来自Sylow 11分析的预算约束是排除n₃=22的关键资源。从任何单一情况分析步骤看不到这个跨情况依赖。"
- hint: "当Sylow计数留下多个困难情形时，利用一个情形中正规化子结构产生的复合阶元素计数，作为元素预算约束来排除另一个情形。"
- hint_level: 0.6
- generalizability: "high — '利用正规化子结构产生复合阶元素做元素预算'是非单群证明的通用策略，适用于多种群阶"
- why_not_visible_locally: "在n₃=22的局部步骤中，AI看到的是22个9阶子群需要容纳，但看不到n₁₁=12情形中已经产生的361个元素预算。这个预算来自前序步骤对N_G(P₁₁)循环结构的分析，是跨情况的资源整合，在局部视角中完全不可见。"
- tell_topology: {problem_type:"structural_existence", ai_method_type:"case_by_case", gap_type:"structural_transformation"}
- tell_small_concepts: ["cross-case element budget", "composite order elements from normalizer", "element counting contradiction", "Sylow subgroup union lower bound"]

Global 2 (implicit):
- scope: "N_G(P₁₁)的循环结构及其对元素计数的隐含影响"
- observation_point: "R4"
- tell: "N_G(P₁₁)≅C₃₃的循环性隐含产生240个33阶元素，这是后续排除n₃=22的隐藏资源。仅计算|N_G(P₁₁)|=33看不到这个隐含影响——需要进一步推断循环性→φ(33)=20→240个33阶元素。"
- hint: "当正规化子阶为pq且p∤(q-1)时，它是循环群，其φ(pq)个pq阶元素是后续元素计数的隐藏资源。"
- hint_level: 0.5
- generalizability: "medium — 适用于正规化子有循环结构的非单群证明，但具体计数依赖于群阶"
- why_not_visible_locally: "在计算|N_G(P₁₁)|=33的步骤中，AI看到一个数字33，但'循环性→20个33阶元素→240个总33阶元素→元素预算约束'是一个多步推理链，每一步的结论在局部步骤中都不可见。特别是'循环性'本身需要额外的数论判断（3∤10），这个判断的后果在计算正规化子阶时完全隐含。"
- tell_topology: {problem_type:"structural_existence", ai_method_type:"direct_calculation", gap_type:"knowledge_gap"}
- tell_small_concepts: ["cyclic normalizer", "Euler totient φ(33)", "composite order elements", "coprimality condition 3∤10", "hidden element resource"]

Global 3 (path_feature):
- scope: "n₃=4情形的方法转换：从Sylow计数到群作用论证"
- observation_point: null
- tell: "n₃=4的解决不是通过更多Sylow计数，而是通过方法转换——构造共轭作用同态G→S₄并用阶比较论证核非平凡。这个从'计数模式'到'作用模式'的方法转换在计数视角中不可见。"
- hint: "当Sylow p-子群数量较少（如4个）时，用共轭作用构造到小对称群的同态，通过阶比较|G|>|S_n|导出非平凡核。"
- hint_level: 0.4
- generalizability: "high — '共轭作用到小对称群+阶比较'是非单群证明的标准工具，适用于n_p较小的多种情形"
- why_not_visible_locally: "当AI处于Sylow计数模式（计算n₁₁、n₃的可能值）时，向群作用模式（构造同态、分析核）的转换是方法层面的跳跃。AI可能继续尝试计数方法（如计算n₂或做更细致的元素计数）而不是转换到作用论证，因为局部步骤中没有信号指示应该换方法。"
- tell_topology: {problem_type:"structural_existence", ai_method_type:"case_by_case", gap_type:"method_translation"}
- tell_small_concepts: ["conjugation action", "homomorphism to S₄", "kernel argument", "order comparison |G|>|S₄|", "method shift from counting to action"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "Bare AI能正确处理n₁₁=1、n₃=1、n₃=4等简单情形，但在n₃=22时会卡住。最可能的错误路径：(1)尝试共轭作用G→S₂₂，但|S₂₂|远大于396无法导出矛盾；(2)尝试计算n₂的可能值但无法从中得到矛盾；(3)不会想到利用N_G(P₁₁)≅C₃₃的循环结构产生240个33阶元素来做元素预算约束。关键缺失：不识别'正规化子循环性→复合阶元素→元素预算'这条推理链。"
- suitable_for_poc: ["tell_hint_injection（注入元素计数方向提示）", "element_counting_guidance（引导AI计算复合阶元素）", "sylow_non_simplicity（Sylow非单群证明策略验证）", "cross_case_resource_integration（跨情况资源整合能力验证）"]
- discriminates_levels: true（此题区分知道元素计数技巧和不知道的AI，n₃=22情形是明确的分水岭）

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
- [x] answer（"If |G| = 396, then G is not a simple group"）
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
- [x] tell_hint_pairs（7个局部pair，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（3个全局pair，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
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
2. 更新`problem_extraction_progress`集合中`_key="396365"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000255"
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
    '_key': '396365',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000255',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000255')
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
- problem_id: fate_000255
- solution_method_type: logical_deduction（Sylow计数+元素计数矛盾+群作用论证的组合）
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3（2个path_feature型，1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否。现有三维度（problem_type/ai_method_type/gap_type）足以描述此题。核心特征通过small_concepts层面表达。
- 是否遇到异常: 否

**操作**：向Master Agent报告

**汇报内容**：
- problem_id:
- solution_method_type:
- 局部(tell,hint)对数量:
- 全局(tell,hint)对数量:
- 是否发现新维度:
- **拓扑分类是否有进化建议**:
- 是否遇到异常:

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
