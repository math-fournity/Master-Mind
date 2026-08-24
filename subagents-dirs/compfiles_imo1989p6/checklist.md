# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1989p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1989P6.lean
- **来源**: IMO 1989 P6
- **ArangoDB progress记录_key**: 329128（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1989P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：{1,2,...,2n}的一个排列{x_1,...,x_{2n}}称为具有性质T，如果至少存在一个i∈{1,...,2n-1}使得|x_i - x_{i+1}| = n。证明：对每个正整数n，具有性质T的排列比不具有性质T的排列多。
- 解答核心思路（1-2句话）：构造从"无T排列"集合A到"有T排列+唯一T位置"对集合B的双射，再将B单射嵌入"有T排列"集合并证明该单射不满射，从而|A|=|B|<|{有T}|。
- 解答关键步骤列表：
  1. 定义A={无T排列}，B={(排列x, 位置k) : k是x中唯一使|x_k-x_{k+1}|=n的位置，k∈{2,...,2n-1}}
  2. 定义partial_cycle操作：对位置1..k做左循环移位（位置1←x(2), ..., 位置k←x(1)）
  3. transform_A_to_B：对无T排列x，找x(1)的n-差伴侣值的位置k（k≥3），对位置1..k-1做partial_cycle，使得新排列在位置k-1处唯一地有T
  4. transform_B_to_A：对(有唯一T的排列x, 位置k)，对位置1..k做partial_cycle的逆（右循环移位），消除T得到无T排列
  5. 证明A_equiv_B：两个变换互逆，A与B等势
  6. embed_B：将B单射嵌入{有T排列}（遗忘位置k）
  7. 证明embed_B不满射：构造具体排列（交换位置1和2的值为n+1和2的swap排列），它有T但不在像中
  8. 结论：|B| < |{有T}|，且|A| = |B|，故|A| < |{有T}|

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
| 1 | 纯元认知观察 | 0.8 | 这个问题的结构是什么？我们需要比较哪两类对象的大小关系？已知条件和目标分别是什么？ | 问题要求比较{1,...,2n}的排列中"具有性质T"和"不具有性质T"的两类排列的数量。性质T定义为存在相邻两项之差的绝对值等于n。目标是证明有T的比无T的多。这是一个集合基数比较问题。 |
| 2 | 自由列举 | 0.7 | 要比较两个集合的大小，有哪些可能的数学方法？请列出所有你能想到的方向。 | 直接计数、容斥原理、生成函数、构造单射/双射、概率方法、归纳法、对称性论证等。 |
| 3 | 小尝试 | 0.3 | 试着直接计算不具有性质T的排列数量。用容斥原理或分类讨论来计数。 | 尝试后发现极其困难：要保证所有相邻对之差都不为n，涉及复杂的约束满足问题，n个"禁对"之间有重叠和依赖关系，容斥展开后项数指数增长，难以得到闭式。 |
| 4 | 思维操作引导 | 0.4 | 直接计数行不通。换一个思路：能否构造一个从"无T排列"到"有T排列"的单射？如果能再证明这个单射不满射，就能得到严格不等式。 | 这是一个好方向。如果能构造单射f: A→{有T}并证明f不满射，则|A|<|{有T}|。关键是如何把一个无T排列变成有T排列。 |
| 5 | 推进 | 0.5 | 给定一个无T排列x，x(1)的值有一个唯一的"n-差伴侣"（即与x(1)相差n的值）。这个伴侣值在排列中的某个位置k。如何利用这个位置k来构造一个有T的排列？ | 可以对位置1到k-1做循环移位：把x(1)的值移到位置k-1，这样位置k-1和k就相邻了，它们的值之差恰好为n。这个操作是partial_cycle。移位后，原来无T的排列变成了在位置k-1处唯一有T的排列。 |
| 6 | 思维操作引导 | 0.3 | 现在你有了从A到"有唯一T位置的排列对"的双射。但还需要证明遗忘位置的嵌入B→{有T}不满射。能否构造一个有T但不在B的像中的具体排列？ | 构造一个在位置1处就有T的排列（如交换位置1和2的值为n+1和1的swap排列），使得|x_1-x_2|=n。但B中要求唯一T位置k≥2，所以位置1有T的排列不在B中。或者构造有多个T位置的排列。 |
| 7 | 能量传递引导 | 0.6 | 现在把所有部分组装起来：你有A↔B的双射、B→{有T}的单射、以及不满射的证明。如何得出最终结论？ | 由A_equiv_B得|A|=|B|，由embed_B单射得|B|≤|{有T}|，由不满射得|B|<|{有T}|，因此|A|<|{有T}|，即无T排列比有T排列少。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 3
- level_sum: 3.6
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: 5
- thinking_bottleneck（思维瓶颈在哪轮，或null）: 4

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
- structure_features: 排列集合基数比较问题，需要比较"具有某性质的排列"和"不具有某性质的排列"的数量。性质T是关于相邻元素差值的局部条件。核心结构是通过构造双射和单射来比较集合大小，而非直接计数。
- key_objects: 排列(permutation)、性质T(相邻元素差为n)、partial_cycle(循环移位操作)、双射A↔B、单射B→{有T}、不满射见证排列

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["injection_argument", "bijection_construction", "non_surjectivity_witness", "structural_transformation", "cyclic_shift_operation"]
- primary_pattern: injection_argument
- knowledge_required: ["排列与置换", "单射/满射/双射", "集合基数比较", "循环移位(cyclic shift)", "Cantor-Bernstein式论证"]
- key_insight: 无T排列中x(1)的n-差伴侣值必在位置≥3，对位置1..k-1做循环移位可将x(1)移到与伴侣相邻的位置，从而唯一地创造T——这个操作是可逆双射。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接计数/容斥原理（试图直接计算两类排列的数量）
- translation_to: 构造性集合论论证（通过双射+单射+不满射比较集合大小）
- translation_type: method_translation（从计数方法翻译到构造性映射方法）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "method_translation"}
- tell_small_concepts: ["injection", "non_surjectivity", "partial_cycle", "bijection", "adjacent_difference_n", "cyclic_shift", "unique_partner"]
- expected_ai_method: bare AI会尝试直接计数或容斥原理来计算有T和无T的排列数量，陷入复杂的约束满足和容斥展开中
- correct_method: 构造从无T排列到有T排列的单射链（通过partial_cycle双射+遗忘位置单射），再证明不满射

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？是，discrete_combinatorial + enumeration_brute_force + method_translation 完全适用。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？是，三个维度都使用了已有的抽象级别值。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？是，足够。这道题的核心gap是"从计数方法翻译到构造性映射方法"，method_translation已覆盖。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。现有拓扑分类体系完全适用。

**拓扑进化建议**（如有）：无。已有拓扑分类体系足够。

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

| qa_round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到排列计数比较问题但未识别集合基数比较的核心结构 | 观察问题要求比较两类排列数量，识别为集合基数比较问题 | 0.8 | 纯元认知观察 | false | {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "method_problem_mismatch"} | ["set_size_comparison", "permutation_property"] |
| 2 | AI列举计数方法但未考虑构造性映射方法（单射/双射） | 列举比较集合大小的所有方法，包括非计数方法 | 0.7 | 自由列举 | false | {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "method_translation"} | ["injection_argument", "structural_relation", "bijection"] |
| 3 | AI尝试直接计数无T排列，陷入容斥原理的复杂展开 | 尝试用容斥原理计数无T排列，发现约束依赖导致不可行 | 0.3 | 小尝试 | false | {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "search_space_estimation"} | ["inclusion_exclusion", "case_analysis", "constraint_satisfaction"] |
| 4 | AI未想到用单射+不满射来比较集合大小 | 从计数转向构造：构造从无T到有T的单射并证明不满射 | 0.4 | 思维操作引导 | false | {problem_type: "discrete_combinatorial", ai_method_type: "logical_deduction", gap_type: "method_translation"} | ["injection", "non_surjectivity", "cardinality_comparison"] |
| 5 | AI考虑单射但不知道如何用循环移位将无T排列变为有T排列 | 利用x(1)的n-差伴侣值位置k，对位置1..k-1做循环移位创造T | 0.5 | 推进 | true | {problem_type: "discrete_combinatorial", ai_method_type: "direct_manipulation", gap_type: "knowledge_gap"} | ["partial_cycle", "cyclic_shift", "adjacent_difference_n", "unique_partner"] |
| 6 | AI有单射但未证明不满射，缺少见证排列 | 构造在位置1处有T的具体排列，证明它不在B的像中 | 0.3 | 思维操作引导 | false | {problem_type: "discrete_combinatorial", ai_method_type: "case_by_case", gap_type: "structural_transformation"} | ["non_surjectivity_witness", "swap_construction", "position_1_T"] |
| 7 | AI有所有部件但未组装完整论证链 | 组装：双射A↔B + 单射B→{有T} + 不满射 → |A|<|{有T}| | 0.6 | 能量传递引导 | false | {problem_type: "discrete_combinatorial", ai_method_type: "logical_deduction", gap_type: "method_translation"} | ["bijection", "injection", "cardinality_inequality", "chain_argument"] |

**全局tell_hint_pairs详情**：

| scope_type | scope | observation_point | tell | hint | hint_level | generalizability | why_not_visible_locally | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|---|---|
| path_feature | 整个解答路径：从计数失败到构造双射+单射+不满射的完整论证链 | null | 解答需要一条非显然的论证链：先构造A↔B双射（通过partial_cycle），再嵌入B→{有T}，最后证明不满射。每一步都依赖前一步的构造 | 关键结构洞察是：无T排列与"有唯一T位置的排列对"双射，而遗忘位置的映射从对到有T排列是单射不满射 | 0.7 | high — "双射+单射+不满射"的论证模式适用于许多集合比较问题，不限于排列 | 完整路径特征在局部视角看不到：从任何单一步骤（如构造partial_cycle、证明双射互逆、构造见证排列）都无法看出整个论证链的全貌。双射A↔B和单射B→{有T}不满射是全局结构特征，需要理解整条构造链才能识别 | {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "method_translation"} | ["bijection_construction", "non_surjectivity", "injection_chain", "partial_cycle"] |
| implicit | partial_cycle操作的双射性 | R5 | partial_cycle操作不仅是创造T的工具，更是A与B之间的可逆双射——它的逆操作可以消除T。这个可逆性是整个论证的基础 | 循环移位在位置1..k上的操作是可逆的：左移创造唯一T，右移消除T。可逆性来自循环移位是置换群的元素 | 0.4 | medium — 循环移位作为可逆变换在排列问题中通用，但具体哪个移位创造/消除T依赖于n-差伴侣的结构 | 这个蕴含信息在局部步骤中不可见：从构造partial_cycle这一步只能看到它把x(1)移到与伴侣相邻的位置，但看不出这个操作对ALL位置的效果（其他位置也移位了但不产生T），更看不出逆操作能消除T——需要同时看到两个方向的变换才能理解可逆性 | {problem_type: "discrete_combinatorial", ai_method_type: "direct_manipulation", gap_type: "structural_transformation"} | ["partial_cycle", "cyclic_shift", "bijection_inverse", "reversibility"] |

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接计数或容斥原理来比较两类排列数量。对于小n可能枚举验证，但对一般n无法得到闭式。关键错误是想不到用partial_cycle构造双射——这个操作需要识别"x(1)的n-差伴侣值必在位置≥3"这一结构性质，并设计循环移位来创造/消除T。bare AI不太可能自发发现这个构造。
- suitable_for_poc: ["tell_hint_injection", "method_translation_poc", "structural_insight_poc"]
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

**将完整JSON写入工作目录的 `profile.json` 文件** ✅ 已写入

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
2. 更新`problem_extraction_progress`集合中`_key="329128"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1989p6"
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
    '_key': '329128',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1989p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1989p6')
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
- problem_id: compfiles_imo1989p6
- solution_method_type: injection_bijection_argument
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，现有拓扑分类体系完全适用
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
