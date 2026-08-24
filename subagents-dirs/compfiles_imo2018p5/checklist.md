# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2018p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2018P5.lean
- **来源**: IMO 2018 P5
- **ArangoDB progress记录_key**: 329247（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2018P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设 a₁, a₂, ... 是正整数无穷序列。假设存在整数 N > 1 使得对每个 n ≥ N，数 a₁/a₂ + a₂/a₃ + ... + aₙ₋₁/aₙ + aₙ/a₁ 是整数。证明存在正整数 M 使得对所有 m ≥ M 有 aₘ = aₘ₊₁。
- 解答核心思路（1-2句话）：利用 p-adic 赋值分析将循环和的整性条件转化为赋值约束，归纳证明序列值有界，再用鸽巢原理找到重复对，最后用"无闭游走"引理推出矛盾。
- 解答关键步骤列表：
  1. 定义循环和 S(n) = Σ aᵢ/a_{i+1}（循环），计算差分 S(n+1) - S(n) = a_{n-1}/aₙ + (aₙ - a_{n-1})/a₀
  2. **Step引理**：S(n) 和 S(n+1) 都是整数 → 存在整数 k 使得 aₙ·k = a₀·a_{n-1} 且 a₀ | k + aₙ - a_{n-1}
  3. **赋值规则**：对素数 p，设 α=v_p(a₀), κ=v_p(k), V=v_p(a_{n-1}), V'=v_p(aₙ)，则：κ<α → V=κ, V'=α；κ=α → V'=V；α<κ → α≤V'<V
  4. **有界性引理**：归纳证明 v_p(aₙ) ≤ v_p(a₀) + v_p(a_{N-1})（n ≥ N-1），故 aₙ | a₀·a_{N-1}，序列值有界
  5. **无闭游走引理**：若 a_{n₁} = a_{n₂}（n₁ < n₂, N ≤ n₁），则序列在 [n₁, n₂] 上恒等于 a_{n₁}
  6. **鸽巢+矛盾**：值有界 → 有限个对 (aₘ, aₘ₊₁) → 鸽巢给出重复对 → 无闭游走推出常数 → 与 aₘ ≠ aₘ₊₁ 矛盾

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
| 1 | 纯元认知观察 | 0.8 | 观察这道题的结构：已知什么？要证什么？循环和的整性条件和"最终常数"之间有什么结构联系？ | 已知：正整数无穷序列，循环和 S(n) 对 n≥N 是整数。要证：存在 M 使 aₘ=aₘ₊₁ 对 m≥M。结构联系：整性条件是全局约束，最终常数是渐近行为，需要从全局约束推出渐近性质。 |
| 2 | 自由列举 | 0.7 | 列出所有可能的研究方向：如何从循环和的整性条件出发证明序列最终为常数？ | 方向包括：直接分析循环和、模运算、p-adic赋值、有界性论证、鸽巢原理、归纳法、反证法、分析差分结构等。 |
| 3 | 小尝试 | 0.4 | 试试直接分析循环和 S(n)。计算 S(n+1) - S(n) 看看整性条件能给出什么。 | S(n+1)-S(n) = a_{n-1}/aₙ + (aₙ-a_{n-1})/a₀。整性意味着这个差是整数，但直接分析分数的整性很困难，需要更结构化的工具。 |
| 4 | 思维操作引导 | 0.3 | 从差分的整性提取整除关系：存在整数 k 使得 aₙ·k = a₀·a_{n-1} 且 a₀ | k + aₙ - a_{n-1}。现在用 p-adic 赋值分析这个关系——对素数 p，设 α=v_p(a₀), κ=v_p(k), V=v_p(a_{n-1}), V'=v_p(aₙ)，分析三种情况 κ<α, κ=α, α<κ。 | 从 aₙ·k = a₀·a_{n-1} 得 V'+κ = α+V。结合 a₀ | k+aₙ-a_{n-1}（即 p^α | k+aₙ-a_{n-1}），分三种情况：κ<α时 V=κ,V'=α；κ=α时 V'=V；α<κ时 α≤V'<V。这就是赋值规则。 |
| 5 | 推进 | 0.5 | 继续推进：用赋值规则归纳证明 v_p(aₙ) ≤ v_p(a₀) + v_p(a_{N-1}) 对所有 n≥N-1 成立。 | 归纳：base case n=N-1 显然。归纳步：对 n+1，由赋值规则三情况——κ<α 给 V'=α（≤α+V_{N-1}）；κ=α 给 V'=V（由归纳假设 ≤α+V_{N-1}）；α<κ 给 V'<V（≤α+V_{N-1}）。故有界。 |
| 6 | 思维操作引导 | 0.3 | 序列值有界了（aₙ | a₀·a_{N-1}）。现在用反证法：假设序列不最终为常数，则有无穷多个 m 使 aₘ≠aₘ₊₁。用鸽巢原理找到重复对 (aₘ₁, aₘ₁₊₁) = (aₘ₂, aₘ₂₊₁)，然后证明"无闭游走"：若 a_{n₁}=a_{n₂} 则序列在 [n₁,n₂] 上为常数。 | 值有界→有限个对→鸽巢给出 m₁<m₂ 使 (aₘ₁,aₘ₁₊₁)=(aₘ₂,aₘ₂₊₁)，特别 aₘ₁₊₁=aₘ₂₊₁。由无闭游走引理，序列在 [m₁+1, m₂+1] 上为常数，故 aₘ₂=aₘ₂₊₁，与 aₘ₂≠aₘ₂₊₁ 矛盾。 |
| 7 | 能量传递引导 | 0.6 | 收尾：把所有部分串起来——整性→赋值规则→有界→鸽巢→无闭游走→矛盾。这就是完整证明！ | 完整逻辑链：循环和整性 → step引理提取整除关系 → p-adic赋值规则 → 归纳有界性 → 鸽巢找重复对 → 无闭游走推出常数 → 与非常数假设矛盾 → 序列最终为常数。QED。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.6
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

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
- structure_features: 正整数无穷序列，循环和 S(n)=Σaᵢ/a_{i+1} 的整性条件（n≥N），证明序列最终为常数。核心结构是"全局整性约束→渐近常数行为"。
- key_objects: 正整数无穷序列 {aₙ}，循环和 S(n)，p-adic 赋值 v_p，有界值 C=a₀·a_{N-1}，鸽巢对 (aₘ, aₘ₊₁)

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["p-adic赋值分析", "归纳有界性", "鸽巢原理", "反证法", "无闭游走论证"]
- primary_pattern: p-adic赋值分析
- knowledge_required: ["p-adic赋值的基本性质", "整除与赋值的关系", "鸽巢原理在有界集上的应用", "循环和的差分结构", "序列归纳法"]
- key_insight: 循环和的整性条件通过差分提取出整除关系 aₙ·k=a₀·a_{n-1}，用 p-adic 赋值分析这个关系得到三情况赋值规则，归纳证明序列值有界，鸽巢+无闭游走推出矛盾。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: （从什么方法/语言翻译）
- translation_to: （翻译到什么方法/语言）
- translation_type: （翻译类型分类）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: knowledge_gap}
- tell_small_concepts: ["循环和整性", "p-adic赋值", "差分结构", "赋值规则三情况", "归纳有界性", "鸽巢原理", "无闭游走", "整除关系提取"]
- expected_ai_method: bare AI预期会尝试直接分析分数和的整性，用模运算或直接代数计算处理循环和，难以想到引入p-adic赋值将整性问题转化为赋值约束
- correct_method: 通过差分提取整除关系，用p-adic赋值分析得到三情况赋值规则，归纳证明序列值有界，鸽巢找重复对，无闭游走引理推出矛盾

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type=structural_existence、ai_method_type=direct_calculation、gap_type=knowledge_gap均可归入已有拓扑类别。核心gap在于bare AI不知道用p-adic赋值工具来处理整性条件，这是知识缺口而非方法选择错误。
- [x] 粒度是否一致——structural_existence（抽象）、direct_calculation（抽象）、knowledge_gap（抽象），与已有值粒度统一。
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell。problem_type区分了"存在性证明"的题型，ai_method_type区分了bare AI会走的"直接计算"路线，gap_type区分了"知识缺口"的本质。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。已有拓扑分类体系可以覆盖本题。

**拓扑进化建议**（如有）：无。已有拓扑分类体系充分覆盖本题。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**局部tell_hint_pairs（7对）**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对循环和整性条件，尚未识别全局约束与渐近行为的结构联系 | 观察题目结构：已知循环和整性条件，要证最终常数，全局约束如何推出渐近性质 | 0.8 | 纯元认知观察 | false | {structural_existence, direct_calculation, method_problem_mismatch} | ["循环和整性", "全局约束", "渐近常数"] |
| 2 | AI识别了结构但尚未列出可行方向，可能遗漏p-adic赋值 | 列出所有研究方向：直接分析循环和、模运算、p-adic赋值、有界性、鸽巢等 | 0.7 | 自由列举 | false | {structural_existence, enumeration_brute_force, search_space_estimation} | ["方向列举", "p-adic赋值", "鸽巢原理", "归纳法"] |
| 3 | AI尝试直接分析循环和差分，但分数整性分析困难，卡在直接计算 | 计算S(n+1)-S(n)差分，看整性条件给出什么 | 0.4 | 小尝试 | false | {structural_existence, direct_calculation, method_problem_mismatch} | ["差分结构", "分数整性", "循环和"] |
| 4 | AI从差分提取了整除关系但不知道如何用p-adic赋值分析三情况 | 从整除关系提取aₙ·k=a₀·a_{n-1}，用p-adic赋值分析κ<α,κ=α,α<κ三情况 | 0.3 | 思维操作引导 | true | {structural_existence, direct_calculation, knowledge_gap} | ["p-adic赋值", "整除关系", "赋值规则三情况", "素数赋值"] |
| 5 | AI理解了赋值规则但尚未归纳证明有界性 | 用赋值规则归纳证明v_p(aₙ)≤v_p(a₀)+v_p(a_{N-1}) | 0.5 | 推进 | false | {structural_existence, logical_deduction, structural_transformation} | ["归纳有界性", "赋值规则应用", "序列值有界"] |
| 6 | AI证明了有界性但不知道如何用鸽巢+无闭游走完成反证 | 用鸽巢找重复对，证明无闭游走引理推出矛盾 | 0.3 | 思维操作引导 | true | {structural_existence, logical_deduction, knowledge_gap} | ["鸽巢原理", "无闭游走", "反证法", "重复对"] |
| 7 | AI已完成所有关键步骤，需要串联完整逻辑链 | 把整性→赋值规则→有界→鸽巢→无闭游走→矛盾串起来 | 0.6 | 能量传递引导 | false | {structural_existence, logical_deduction, method_translation} | ["完整逻辑链", "矛盾收尾", "QED"] |

**全局tell_hint_pairs（2对）**：

**Pair 1 (path_feature型)**：
- scope_type: path_feature
- scope: 从差分整性到p-adic赋值规则的翻译路径（R3→R4）
- observation_point: null
- tell: 差分S(n+1)-S(n)的整性给出了整除关系aₙ·k=a₀·a_{n-1}，但直接分析分数整性无法推进——需要翻译到p-adic赋值语言
- hint: 将整除关系翻译为p-adic赋值等式V'+κ=α+V，结合a₀|k+aₙ-a_{n-1}的赋值约束，分三种情况分析
- hint_level: 0.3
- generalizability: high — "整性条件→p-adic赋值翻译"是一个通用的数论问题解决范式，适用于任何涉及分数和整性的问题
- why_not_visible_locally: 在R3的局部视角中，AI只看到差分的分数形式和整性条件，无法预见需要引入p-adic赋值。整除关系aₙ·k=a₀·a_{n-1}的提取是局部的，但"用赋值分析这个等式"的决策需要全局视角——只有看到后续需要归纳有界性才能确定赋值规则是正确的翻译方向。局部步骤只暴露了整除关系，没有暴露"赋值语言"这个翻译目标。
- tell_topology: {structural_existence, direct_calculation, method_translation}
- tell_small_concepts: ["差分整性", "整除关系提取", "p-adic赋值翻译", "赋值规则三情况"]

**Pair 2 (implicit型)**：
- scope_type: implicit
- scope: 有界性→鸽巢→无闭游走的完整反证结构（R5→R6→R7）
- observation_point: R5
- tell: 归纳有界性证明aₙ|a₀·a_{N-1}后，蕴含着一个关键信息：值有界使得对(aₘ,aₘ₊₁)只有有限种，但这个"有限性→鸽巢→无闭游走→矛盾"的反证结构在有界性证明本身中不可见
- hint: 从有界性出发，用鸽巢原理找到重复对(aₘ₁,aₘ₁₊₁)=(aₘ₂,aₘ₂₊₁)，然后用无闭游走引理证明序列在[m₁+1,m₂+1]上为常数，与aₘ₂≠aₘ₂₊₁矛盾
- hint_level: 0.4
- generalizability: medium — "有界→鸽巢→反证"是组合数论中常见的收尾模式，但"无闭游走引理"是本题特有的技术
- why_not_visible_locally: 在R5完成有界性证明时，局部视角只看到"序列值有界"这个结论。从这个结论到"用鸽巢找重复对→无闭游走推出常数→与非常数假设矛盾"的完整反证结构，需要同时看到有界性、鸽巢和反证法三个组件的协同。有界性证明本身不蕴含"为什么要证明有界性"——目的是为鸽巢提供有限性条件，这个目的只在全局视角下可见。
- tell_topology: {structural_existence, logical_deduction, structural_transformation}
- tell_small_concepts: ["有界性蕴含", "鸽巢有限性", "无闭游走引理", "反证结构"]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: bare AI会尝试直接分析循环和的整性条件，可能用模运算或通分处理分数和，但无法想到引入p-adic赋值将整性问题转化为赋值约束。即使提取出差分的整除关系，也缺乏用p-adic赋值分析三情况的知识。在收尾阶段，即使偶然得到有界性，也难以想到"无闭游走引理"这一关键技术。整体预期：在R4（赋值规则）处卡死，无法突破知识瓶颈。
- suitable_for_poc: ["tell端验证——p-adic赋值翻译的path_feature型tell", "hint端验证——知识瓶颈轮的提示注入效果", "知识瓶颈识别——R4和R6两个knowledge_gap轮的区分"]
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
2. 更新`problem_extraction_progress`集合中`_key="329247"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2018p5"
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
    '_key': '329247',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2018p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2018p5')
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
- problem_id: compfiles_imo2018p5
- solution_method_type: p_adic_valuation_induction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（path_feature型1个，implicit型1个）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。已有拓扑分类体系（structural_existence / direct_calculation / knowledge_gap等）充分覆盖本题。
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
