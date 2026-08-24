# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1974p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1974P6.lean
- **来源**: IMO 1974 P6
- **ArangoDB progress记录_key**: 329070（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1974P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let P be a non-constant polynomial with integer coefficients. If n(P) is the number of different integers k such that (P(k))² = 1, prove that n(P) - deg(P) ≤ 2.
- 解答核心思路（1-2句话）：将P(k)²=1分解为P(k)=1或P(k)=-1两个集合，前者由根计数至多deg(P)个，后者由整系数多项式的整除性(P(k)-P(r)被k-r整除)约束至多2个，合计n(P)≤deg(P)+2。
- 解答关键步骤列表：
  1. P(k)²=1 ⟺ P(k)=1 ∨ P(k)=-1，将问题分解为两个根集
  2. {k : P(k)=1} = roots of (P-1)，至多deg(P)个（因P非常数故P-1≠0且deg(P-1)=deg(P)）
  3. 关键整除性：若P(r)=1且P(k)=-1，则(k-r) | (P(k)-P(r)) = -2，故(k-r) | 2
  4. 取r为{k : P(k)=±1}中最小元且P(r)=1，则对任意P(k)=-1的k，有k>r且(k-r)|2，故k∈{r+1, r+2}，至多2个
  5. 对称情况：若最小元r满足P(r)=-1，对-P应用同一论证（度数不变，集合不变）
  6. 合并：n(P) = |{k:P(k)=1}| + |{k:P(k)=-1}| ≤ deg(P) + 2

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
| 1 | 纯元认知观察 | 0.8 | 请描述这道题的结构：已知什么？要求证什么？P(k)²=1这个条件意味着什么？ | 已知：P是整系数非常数多项式，n(P)是满足P(k)²=1的不同整数k的个数。求证：n(P)-deg(P)≤2。P(k)²=1意味着P(k)=1或P(k)=-1，即k是P-1或P+1的根。 |
| 2 | 自由列举 | 0.7 | 列出所有可能的approach来bound n(P)。每种approach能给出什么bound？ | (1) 直接根计数：P-1至多deg(P)个根，P+1至多deg(P)个根，合计2·deg(P)——太弱。(2) 利用P(k)²-1=(P(k)-1)(P(k)+1)的因式分解。(3) 利用整系数多项式的特殊性质。(4) 考虑两个根集之间的关系。 |
| 3 | 小尝试 | 0.3 | 试一下直接根计数的方法：分别计算P-1和P+1的根的个数，能得到什么bound？这个bound够用吗？ | P-1是deg(P)次多项式，至多deg(P)个整数根；P+1也是deg(P)次，至多deg(P)个根。所以n(P)≤2·deg(P)。但需要n(P)-deg(P)≤2即n(P)≤deg(P)+2，而2·deg(P)远大于deg(P)+2（当deg(P)>2时）。这个bound太弱了。 |
| 4 | 思维操作引导 | 0.4 | 关键操作：思考整系数多项式的特殊性质。如果P(r)=1且P(k)=-1，那么P(k)-P(r)=-2。对于整系数多项式，P(k)-P(r)和k-r之间有什么整除关系？ | 对于整系数多项式P，P(k)-P(r)总是被k-r整除（因为P(x)-P(y)的每个单项式x^n-y^n都含因子x-y）。所以如果P(r)=1且P(k)=-1，则(k-r) | (P(k)-P(r)) = -2，即(k-r) | 2。这意味着k-r∈{±1,±2}。 |
| 5 | 推进 | 0.3 | 利用这个整除关系来bound {k:P(k)=-1}。取r为集合{k:P(k)=±1}中的最小整数且P(r)=1，对任意P(k)=-1的k能推出什么？ | 由r的最小性，k≥r。又k≠r（因为P(r)=1≠-1），故k>r。由整除关系(k-r)|2且k-r>0，得k-r∈{1,2}，即k∈{r+1,r+2}。所以{k:P(k)=-1}⊆{r+1,r+2}，至多2个元素。 |
| 6 | 思维操作引导 | 0.4 | 如果最小元r满足的是P(r)=-1而不是P(r)=1呢？如何处理这个对称情况？ | 对-P应用同样的论证。-P也是整系数非常数多项式，deg(-P)=deg(P)，且{k:(-P(k))²=1}={k:P(k)²=1}。对-P而言，P(r)=-1变成(-P)(r)=1，可以用之前的论证得到同样的bound。 |
| 7 | 能量传递引导 | 0.5 | 现在把所有部分组合起来，写出完整的bound。 | n(P)=|{k:P(k)=1}|+|{k:P(k)=-1}|≤deg(P)+2。其中|{k:P(k)=1}|≤deg(P)（根计数），|{k:P(k)=-1}|≤2（整除性约束）。故n(P)-deg(P)≤2。∎ |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1,R2,R5,R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4,R6）
- level_sum: 0.8+0.7+0.3+0.4+0.3+0.4+0.5 = 3.4
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R4（整系数多项式的整除性质P(k)-P(r)被k-r整除是关键知识瓶颈）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R3（直接根计数给出2·deg(P)太弱，需要思维转向寻找两个根集之间的关系）

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
- structure_features: 整系数多项式的整数根计数问题，P(k)²=1分解为两个根集{k:P(k)=1}和{k:P(k)=-1}，前者由根计数bound至多deg(P)个，后者由整系数多项式整除性约束至多2个，合计deg(P)+2
- key_objects: 整系数非常数多项式P, 根集{k:P(k)=1}=roots of (P-1), 根集{k:P(k)=-1}=roots of (P+1), 整除关系(k-r)|2, 最小元r

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["集合分解", "根计数", "整除性利用", "极值选取", "对称化归"]
- primary_pattern: 集合分解+整除性约束
- knowledge_required: ["整系数多项式P(k)-P(r)被k-r整除", "多项式根的个数不超过次数", "P(k)²=1等价于P(k)=±1"]
- key_insight: 利用整系数多项式的整除性质P(k)-P(r)被k-r整除，当P(r)=1且P(k)=-1时得到(k-r)|2，取最小元r后{k:P(k)=-1}⊆{r+1,r+2}至多2个

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接根计数（分别对P-1和P+1独立计数，得到2·deg(P)）
- translation_to: 关联约束（利用两个根集之间的整除性关系，将一个集合约束到至多2个）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: method_problem_mismatch}
- tell_small_concepts: ["P(k)²=1分解为P(k)=±1", "根计数bound", "整系数多项式整除性", "极值选取", "对称化归"]
- expected_ai_method: 直接根计数——分别对P-1和P+1的根计数，得到n(P)≤2·deg(P)，无法改进到deg(P)+2
- correct_method: 集合分解+整除性约束——利用P(k)-P(r)被k-r整除，取最小元将{k:P(k)=-1}约束到至多2个

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是，inequality_proof + direct_calculation + method_problem_mismatch 完全归入已有类别
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是，与已有值粒度一致
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 是，三个维度足够
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 不需要进化

**拓扑进化建议**（如有）：无，当前三维度拓扑分类完全够用

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
- `why_not_visible_locally`: 蕴含型专用——为什么在局部不可见
- `tell_topology`: object（**⚠️ 每个全局pair也要有**）
- `tell_small_concepts`: array[string]（**⚠️ 每个全局pair也要有**）

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

### 局部(tell, hint)对详情：

**R1** (纯元认知观察, level=0.8)
- tell: AI面对题目尚未识别P(k)²=1的分解结构，不知道问题可拆分为两个根集
- hint: 描述题目结构，识别P(k)²=1意味着P(k)=1或P(k)=-1，即k是P-1或P+1的根
- is_knowledge_bottleneck: false
- tell_topology: {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: method_problem_mismatch}
- tell_small_concepts: ["P(k)²=1分解", "根集结构识别", "已知未知识别"]

**R2** (自由列举, level=0.7)
- tell: AI列出多种approach但未识别两个根集之间的关系是关键方向
- hint: 列出所有approach，特别关注两个根集之间的关系而非独立计数
- is_knowledge_bottleneck: false
- tell_topology: {problem_type: inequality_proof, ai_method_type: enumeration_brute_force, gap_type: search_space_estimation}
- tell_small_concepts: ["approach列举", "根集关系", "bound强弱比较"]

**R3** (小尝试, level=0.3)
- tell: AI尝试直接根计数得到2·deg(P)，发现bound太弱但不知道如何改进
- hint: 试直接根计数，发现2·deg(P)远大于deg(P)+2，需要思维转向
- is_knowledge_bottleneck: false
- tell_topology: {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: method_problem_mismatch}
- tell_small_concepts: ["2·deg(P)太弱", "独立计数", "bound不足", "思维转向信号"]

**R4** (思维操作引导, level=0.4)
- tell: AI不知道如何利用整系数多项式的特殊性质来改进bound
- hint: 引导思考整系数多项式的整除性P(k)-P(r)被k-r整除
- is_knowledge_bottleneck: true
- tell_topology: {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: knowledge_gap}
- tell_small_concepts: ["整系数多项式整除性", "P(k)-P(r)被k-r整除", "(k-r)|2"]

**R5** (推进, level=0.3)
- tell: AI知道整除关系但未想到用极值选取来约束集合大小
- hint: 取最小元r，利用整除关系和最小性约束{k:P(k)=-1}⊆{r+1,r+2}至多2个
- is_knowledge_bottleneck: false
- tell_topology: {problem_type: inequality_proof, ai_method_type: logical_deduction, gap_type: structural_transformation}
- tell_small_concepts: ["极值选取", "最小元约束", "k∈{r+1,r+2}", "集合包含关系"]

**R6** (思维操作引导, level=0.4)
- tell: AI只处理了P(r)=1的情况，未考虑P(r)=-1的对称情况
- hint: 对-P应用同一论证处理对称情况，度数不变集合不变
- is_knowledge_bottleneck: false
- tell_topology: {problem_type: inequality_proof, ai_method_type: case_by_case, gap_type: structural_transformation}
- tell_small_concepts: ["对称情况", "对-P应用", "度数不变", "case完备性"]

**R7** (能量传递引导, level=0.5)
- tell: AI有所有部件但未组合成完整证明
- hint: 组合所有部分写出完整bound: n(P)≤deg(P)+2
- is_knowledge_bottleneck: false
- tell_topology: {problem_type: inequality_proof, ai_method_type: logical_deduction, gap_type: method_translation}
- tell_small_concepts: ["组合bound", "deg(P)+2", "证明收尾"]

### 全局(tell, hint)对详情：

**G1** (path_feature型)
- scope: 整个证明路径中从独立计数到关联约束的转向
- observation_point: null
- tell: 直接根计数给出2·deg(P)太弱，关键在于利用两个根集之间的整除性关系而非独立计数
- hint: 不要独立计数两个根集，而要利用它们之间的关系——整系数多项式的整除性P(k)-P(r)被k-r整除
- hint_level: 0.6
- generalizability: "high - 整系数多项式的整除性质P(k)-P(r)被k-r整除是广泛适用的数论工具，在多项式根计数类问题中可泛化"
- tell_topology: {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: method_problem_mismatch}
- tell_small_concepts: ["独立计数vs关联约束", "整除性关系", "根集间关系", "bound改进"]

**G2** (implicit型)
- scope: 极值选取+对称化归的组合策略
- observation_point: R5
- tell: 取最小元约束一个集合的大小，再用对称化归处理另一种情况——这个组合策略作为整体路径特征在局部不可见
- hint: 极值选取+对称化归是处理"两个集合中一个需要强约束"的标准组合策略
- hint_level: 0.7
- generalizability: "medium - 极值选取+对称化归的组合在多项式根计数类问题中可泛化，但需要整除性前提"
- why_not_visible_locally: "在R5只看到极值选取，在R6只看到对称化归，但两者的组合策略作为整体路径特征在单个轮次中不可见"
- tell_topology: {problem_type: inequality_proof, ai_method_type: logical_deduction, gap_type: structural_transformation}
- tell_small_concepts: ["极值选取", "对称化归", "组合策略", "路径特征"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会分别对P-1和P+1的根计数，得到n(P)≤2·deg(P)，无法改进到deg(P)+2。关键知识瓶颈是整系数多项式的整除性质P(k)-P(r)被k-r整除，bare AI不太可能自发想到利用两个根集之间的关系来改进bound。
- suitable_for_poc: ["hint端验证——注入整除性知识能否引导AI找到正确bound", "tell端验证——能否从AI的thinking中识别'只做独立计数'的分叉信号"]
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
- [ ] answer
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

## Step 10: 入库ArangoDB [ ]

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="329070"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1974p6"
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
    '_key': '329070',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1974p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1974p6')
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
- problem_id: compfiles_imo1974p6
- solution_method_type: set_decomposition_divisibility_constraint
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，当前三维度拓扑分类完全够用
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
