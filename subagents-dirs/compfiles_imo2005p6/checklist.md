# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2005p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2005P6.lean
- **来源**: IMO 2005 P6
- **ArangoDB progress记录_key**: 329196（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2005P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：In a mathematical competition 6 problems were posed to the contestants. Each pair of problems was solved by more than 2/5 of the contestants. Nobody solved all 6 problems. Show that there were at least 2 contestants who each solved exactly 5 problems.
- 解答核心思路（1-2句话）：反证法假设至多一人解5题，归一化为一解5题其余解4题，双计数得15对计数之和=6n+4，结合每对≥(2n+1)/5推出2n+1≡0(mod 5)且恰一对计数为k+1，再用模3同余式（4题解者贡献0 mod 3，5题解者贡献-2≡1 mod 3）对15种情况逐一导出矛盾。
- 解答关键步骤列表：
  1. 反证：假设至多一人恰好解5题
  2. 归一化：提升选手解题数（不削弱对条件），使得一人解5题、其余解4题
  3. 双计数：Σ(15对的计数) = C(5,2) + (n-1)·C(4,2) = 10 + 6(n-1) = 6n+4
  4. 下界：每对计数 ≥ (2n+1)/5 = k，故 15k ≤ 6n+4 = 15k+1，推出 2n+1≡0(mod 5)，恰一对计数为k+1
  5. 模3同余：对{0,1,2,3,4}中每对P，pairCount(P) ≡ 1 + Σ(补三元组与5的配对计数) + Σ(补三元组内配对计数) (mod 3)
  6. 逐案检验：15种"哪对计数为k+1"的情况，每种都有两条同余式冲突（5k≡0 vs 5k+1≡0 mod 3），全部矛盾

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
| 1 | 纯元认知观察 | 0.3 | 描述这道题的结构：已知条件是什么？要证明什么？核心数学对象有哪些？ | 已知：n个选手，6道题，每对题被>2/5选手解出，无人解全部6题。求证：≥2人恰好解5题。核心对象：选手解题集合s_i⊆{1..6}，对计数t_{pq}=#解出p和q的选手数。 |
| 2 | 自由列举 | 0.5 | 列出所有可能的方法方向：双计数、鸽巢、反证法、模运算、线性代数……哪些可能有用？ | 双计数（Σ对计数=Σ C(\|s_i\|,2)）、反证法（假设≤1人解5题）、鸽巢原理、模运算同余、线性代数。双计数和反证法看起来最有前景。 |
| 3 | 小尝试 | 0.2 | 试用双计数直接做：Σ对计数 = Σ C(\|s_i\|,2)，对条件给出什么？能推出什么？ | Σ对计数 > 15·(2n/5) = 6n。但无人解6题所以\|s_i\|≤5，C(\|s_i\|,2)≤10。这给出6n < Σ ≤ 10n，但还不够精确，无法区分解5题和解4题的选手。直接双计数信息不足。 |
| 4 | 思维操作引导 | 0.6 | 直接计数信息不足。尝试反证法+归一化：假设至多1人解5题，然后提升选手解题数（只加强对条件），化归为一人解5题、其余解4题的标准形。 | 反证假设≤1人解5题。若无人解5题，选一人提升到5题；若一人解5题，其余提升到4题。提升只增加解题集，对条件更强（不削弱）。得到标准形：c0解5题，其余n-1人各解4题。 |
| 5 | 推进 | 0.4 | 在标准形下精确计算：15对计数之和是多少？每对计数的下界是多少？这给出什么约束？ | 和 = C(5,2)+(n-1)·C(4,2) = 10+6(n-1) = 6n+4。每对≥(2n+1)/5。设k=(2n+1)/5，则15k=6n+3，和=6n+4=15k+1。故2n+1≡0(mod 5)，且恰一对计数为k+1，其余14对为k。 |
| 6 | 思维操作引导 | 0.7 | 现在需要模3同余式。对{0,1,2,3,4}中每对P，分析每个选手对pairCount(P)与相关对计数的贡献：4题解者贡献0 mod 3，5题解者c0贡献-2≡1 mod 3。推导同余式。 | 对P⊆{0,1,2,3,4}，补三元组T={0,1,2,3,4}\P。每个4题解者对 [pairCount(P) - Σ_{u∈T}pairCount({u,5}) - Σ_{Q⊆T,|Q|=2}pairCount(Q)] 的贡献≡0 mod 3。c0贡献-2≡1。故pairCount(P) ≡ 1 + Σ_{u∈T}t_{u5} + Σ_{Q⊆T}t_Q (mod 3)。共10条同余式。 |
| 7 | 能量传递引导 | 0.5 | 现在有了精确约束：恰一对计数为k+1，其余为k，加上10条模3同余式。检查15种情况，每种是否都矛盾？ | 逐案检验：若某对P计数为k+1=5k/5+1，代入相关同余式。例如t01=k+1时，其余14对为k=5k/5。同余式c01给出5k+1≡1+6k≡1+0≡1(mod 3)，但5k+1≡2k+1(mod 3)；同余式c02给出5k≡1+6k≡1(mod 3)，但5k≡2k(mod 3)。当k≡0时2k+1≡1✓但2k≡0≠1✗。每种情况都有两条同余式冲突。全部矛盾，证毕！ |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.2
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: discrete_combinatorial
- structure_features: 6道题n个选手，每对题被>2/5选手解出（对计数下界），无人解全部6题（|s_i|≤5），证明≥2人恰好解5题（存在性下界）。核心是对计数t_{pq}满足的算术约束与组合结构之间的矛盾。
- key_objects: ["选手解题集合 s_i ⊆ {1,...,6}", "对计数 t_{pq}（15个）", "模3同余式（10条）", "归一化标准形（一人解5题，其余解4题）"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["contradiction", "normalization_reduction", "double_counting", "modular_arithmetic", "case_analysis"]
- primary_pattern: modular_arithmetic_contradiction
- knowledge_required: ["double counting (双计数)", "modular arithmetic (模运算同余)", "binomial coefficients (组合数)", "combinatorial normalization (组合归一化/提升)", "per-element contribution analysis (逐元素贡献分析)"]
- key_insight: 归一化后4题解者对组合结构的贡献C(4,2)=6≡0 mod 3使他们在同余式中"消失"，5题解者贡献C(5,2)-相关=−2≡1 mod 3留下痕迹，模3同余式与近均匀分布（恰一对为k+1）产生不可调和的矛盾。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: combinatorial counting（组合计数——对计数与双计数）
- translation_to: modular arithmetic constraints（模算术约束——模3同余式体系）
- translation_type: structural_to_arithmetic（将组合结构翻译为算术同余约束）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: discrete_combinatorial, ai_method_type: direct_calculation, gap_type: method_translation}
- tell_small_concepts: ["pair count", "double counting", "mod 3 congruence", "normalization", "per-contestant contribution", "case analysis contradiction"]
- expected_ai_method: bare AI会尝试直接双计数或鸽巢原理，得到sum > 6n的粗界后就卡住，不会想到归一化和模3同余
- correct_method: 反证法+归一化+双计数精确求和+模3同余式+15种逐案检验矛盾

### 6b. 反思拓扑分类

- [x] 当前拓扑分类是否够用——这道题的problem_type(discrete_combinatorial)/ai_method_type(direct_calculation)/gap_type(method_translation)能归入已有的拓扑类别
- [x] 粒度是否一致——discrete_combinatorial和direct_calculation都是抽象粒度，method_translation是中等粒度，与已有值一致
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化，现有分类体系够用

**拓扑进化建议**（如有）：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs摘要**：
| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到组合计数题，想直接开始计数 | 先描述结构：已知条件、目标、核心对象 | 0.3 | 纯元认知观察 | false | (discrete_combinatorial, direct_calculation, method_problem_mismatch) | ["pair counting", "contestant problem set", "fraction threshold"] |
| 2 | AI描述完结构，准备选方向但未纵览全局 | 列出所有可能方法：双计数、鸽巢、反证、模运算、线性代数 | 0.5 | 自由列举 | false | (discrete_combinatorial, enumeration_brute_force, search_space_estimation) | ["double counting", "pigeonhole", "contradiction", "modular arithmetic"] |
| 3 | AI试双计数直接做，得sum>6n但信息不足 | 试算Σ对计数=ΣC(|s_i|,2)，看能推出什么 | 0.2 | 小尝试 | false | (discrete_combinatorial, direct_calculation, method_problem_mismatch) | ["pair count sum", "binomial coefficient", "lower bound"] |
| 4 | AI直接计数卡住，未想到归一化 | 反证法+归一化：假设≤1人解5题，提升选手到标准形 | 0.6 | 思维操作引导 | false | (discrete_combinatorial, direct_calculation, structural_transformation) | ["normalization", "promotion", "contradiction assumption", "canonical form"] |
| 5 | AI有标准形，需提取算术约束 | 精确计算sum=6n+4，每对≥k=(2n+1)/5，推出2n+1≡0(mod5)且恰一对为k+1 | 0.4 | 推进 | false | (discrete_combinatorial, direct_calculation, method_problem_mismatch) | ["exact sum", "pair count lower bound", "divisibility", "near-uniform distribution"] |
| 6 | AI有算术约束但未连接到模3同余 | 推导模3同余式：4题解者贡献0 mod 3，5题解者贡献1 mod 3 | 0.7 | 思维操作引导 | true | (discrete_combinatorial, direct_calculation, knowledge_gap) | ["mod 3 congruence", "per-contestant contribution", "complementary triple", "indicator function"] |
| 7 | AI有约束+同余式，需组合导出矛盾 | 检查15种情况，每种两条同余式冲突，全部矛盾 | 0.5 | 能量传递引导 | false | (discrete_combinatorial, case_by_case, method_translation) | ["case analysis", "congruence clash", "arithmetic contradiction", "fifteen pairs"] |

**全局pairs摘要**：
1. path_feature型：证明需要归一化+双计数+模3同余三技合用，单技不足。why_not_visible_locally: 每个局部步骤（计数、同余推导）看起来都是标准技巧，但需要三者组合以及模3（而非模2或模5）的特定选择只有从完整路径才可见。
2. implicit型（observation_point=R6）：模3的选择不是任意的——C(4,2)=6≡0 mod 3使4题解者"消失"，C(5,2)相关贡献=−2≡1留下痕迹。why_not_visible_locally: 在局部推导同余式时能看到逐选手贡献，但模3为何是正确选择（而非模2或模5）的原因是隐含的——它来自6=C(4,2)≡0 mod 3这一结构事实，局部代数运算中不可见。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: bare AI会尝试直接双计数或鸽巢原理，得到sum > 6n的粗界后卡住。不会想到归一化（提升选手到标准形），更不会想到从逐选手贡献推导模3同余式。缺少模3同余这一关键步骤，计数界本身不足以导出矛盾。
- suitable_for_poc: ["hint_injection_poc", "tell_identification_poc", "multi_step_reasoning_poc"]
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

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证详情: 7 local pairs, 2 global pairs, knowledge_bottleneck=R6(str), thinking_bottleneck=R4(str), answer非None

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_imo2005p6
- solution_method_type: double_counting_with_modular_congruence
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，现有分类体系（discrete_combinatorial / direct_calculation / method_translation等）够用
- 是否遇到异常: JSON中solution_summary字段有未转义中文引号导致解析失败，已修复

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
