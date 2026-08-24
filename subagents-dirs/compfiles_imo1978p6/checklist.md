# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1978p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1978P6.lean
- **来源**: IMO 1978 P6
- **ArangoDB progress记录_key**: 329089（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1978P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：一个国际学会的成员来自6个不同国家。成员名单有1978个名字，编号为1, 2, ..., 1978。证明至少有一个成员的编号等于同国两名（不一定不同）成员编号之和。即：对任意划分 C: {1,...,1978} → {1,...,6}，存在 i, j, k 使得 C(i)=C(j)=C(k) 且 i+k=j。
- 解答核心思路（1-2句话）：反证法——假设不存在同国三数和关系，则每个国家的成员集都是sum-free的。通过归纳地逐国处理，每步用鸽巢原理在剩余国家中找到一个国家在当前集合Δ中占有足够多元素，然后用最小元素做平移变换，将|Δ|缩减为⌈|Δ|/(剩余国家数)⌉-1。从1978开始经6步缩减得1>0，但所有国家处理完后Δ必须为空——矛盾。
- 解答关键步骤列表：
  1. 反证假设：对所有同国的 i, j, k，i+k≠j（每个国家成员集是sum-free的）
  2. 定义归纳不变量motive：已处理国家集Cdone + 平移集Δ，满足(1)每个已处理国家有base元素a0使得x+a0同属该国，(2)Δ的元素所属国家与Cdone不相交，(3)|Δ|≥k
  3. 基础情形：Cdone=∅, Δ={1,...,1978}, k=1978
  4. 归纳步：鸽巢原理——在N-n个剩余国家中，某国y在Δ中至少有⌈|Δ|/(N-n)⌉个元素；取xmin为Δ∩country_y的最小元素，构造新Δ'={(x-xmin): x∈Δ∩y, x≠xmin}，大小为⌈|Δ|/(N-n)⌉-1
  5. 平移保持不变量：对每个已处理国家的base a0，(x-xmin)+(a0+xmin)=x+a0仍在该国（归纳假设）；xmin成为y国的base
  6. 数值验证：k(0)=1978 → k(1)=⌈1978/6⌉-1=329 → k(2)=⌈329/5⌉-1=65 → k(3)=⌈65/4⌉-1=16 → k(4)=⌈16/3⌉-1=5 → k(5)=⌈5/2⌉-1=2 → k(6)=⌈2/1⌉-1=1
  7. 矛盾：k(6)=1>0要求|Δ|≥1，但6个国家全在Cdone中，Δ的元素所属国家必在Cdone中，违反不相交性——矛盾

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.2 | 描述题目结构：给定什么（1978个数分成6组的划分），要证什么（存在同国三数i+k=j），这是什么类型的数学对象？ | 这是Ramsey型问题：对{1,...,1978}的6-着色，证明存在单色x+y=z。核心对象是划分函数和sum-free性质。 |
| 2 | 自由列举 | 0.5 | 列出所有可能方法：鸽巢原理、归纳法、反证法、密度论证、Schur定理、生成函数。哪些最有前景？ | 鸽巢原理自然（6国1978人）。Schur定理直接相关（保证大集合中有单色x+y=z）。归纳和反证是标准框架。最有前景的是鸽巢+反证+归纳的组合。 |
| 3 | 小尝试 | 0.3 | 试最简单的鸽巢：最大的国家至少有⌈1978/6⌉=330个成员。能在330个数中保证存在i+k=j吗？哪里出了问题？ | 330个数不一定包含和三元组。sum-free集可以很大（如所有奇数到1978构成大小989的sum-free集）。所以对单个国家的直接鸽巢不够——需要同时利用所有国家的结构。 |
| 4 | 思维操作引导 | 0.6 | 假设不存在这样的三元组（反证）。这意味着每个国家的成员集都是sum-free的。思考这个约束对划分施加了什么结构性限制。 | 若无三元组，每个国家成员集sum-free。这是强约束。需要证明6个sum-free集不能覆盖{1,...,1978}。关键是如何利用这个约束推出矛盾。 |
| 5 | 思维操作引导 | 0.7 | 逐国处理。每步取出一个国家在当前集合Δ中的元素，取最小元素xmin做平移（其余元素减去xmin）。这个平移保持了什么结构？ | 若Δ中country y有若干元素，xmin为最小，平移集{(x-xmin): x∈Δ∩y, x≠xmin}满足：对每个已处理国家的base a0，(x-xmin)+(a0+xmin)=x+a0仍在该国（归纳假设）。xmin成为y国的base。sum-free性质对所有已处理国家同时保持。 |
| 6 | 推进 | 0.6 | 形式化归纳步：鸽巢原理保证在N-n个剩余国家中，某国y在Δ中至少有⌈|Δ|/(N-n)⌉个元素。平移后新Δ大小为⌈|Δ|/(N-n)⌉-1。追踪缩减过程。 | 第n步（n国已处理），|Δ|≥k(n)。鸽巢保证某剩余国家有≥⌈k(n)/(N-n)⌉个Δ元素。去掉xmin后平移，新|Δ|=⌈k(n)/(N-n)⌉-1=k(n+1)。不变量保持：|Δ|≥k(n+1)且所有已处理国家有合法base。 |
| 7 | 能量传递引导 | 0.3 | 计算缩减链：1978→⌈1978/6⌉-1=329→⌈329/5⌉-1=65→⌈65/4⌉-1=16→⌈16/3⌉-1=5→⌈5/2⌉-1=2→⌈2/1⌉-1=1>0。但6国全处理后Δ必须为空。矛盾！ | k(0)=1978, k(1)=329, k(2)=65, k(3)=16, k(4)=5, k(5)=2, k(6)=1。6国全在Cdone后，Δ必须为空（其元素所属国家全在Cdone中，违反不相交性），但k(6)=1>0要求|Δ|≥1。矛盾！故假设不成立，单色和三元组必存在。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.2
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: 5（平移技术的发现是纯知识瓶颈）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: 4（从直接鸽巢转向反证+sum-free约束的思维转换）

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: `discrete_combinatorial`（Ramsey型组合存在性问题，6-着色中证明单色和三元组存在）
- structure_features:
  - 1978个元素划分为6组的划分结构
  - sum-free约束（反证假设下每个国家成员集的性质）
  - 迭代缩减via鸽巢和平移
  - 数值矛盾链验证
- key_objects:
  - 划分函数 C: {1,...,1978} → {1,...,6}
  - sum-free集（反证下各国成员集）
  - 平移集Δ（归纳不变量）
  - 最小元素xmin（每步的平移锚点）

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["proof_by_contradiction", "inductive_construction", "iterative_pigeonhole", "shifting_transformation", "numerical_verification"]
- primary_pattern: `inductive_shifting_with_iterative_pigeonhole`（归纳平移+迭代鸽巢——主导思维模式）
- knowledge_required: ["鸽巢原理", "sum-free集", "数学归纳法", "反证法", "Schur型Ramsey问题"]
- key_insight: 不在全集上做一次性鸽巢，而是逐国处理：每步用鸽巢在当前平移集Δ中找到一个国家占有足够多元素，然后用最小元素做平移以对所有已处理国家同时保持sum-free不变量，将|Δ|缩减为⌈|Δ|/(剩余国家数)⌉-1。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: `static_pigeonhole_on_fixed_partition`（在固定划分上做静态鸽巢——直接找最大国家然后试图在和三元组中找解）
- translation_to: `dynamic_inductive_shifting_with_iterative_pigeonhole`（动态归纳平移+迭代鸽巢——逐国处理，每步平移缩减集合）
- translation_type: `method_translation`（从静态一次性方法翻译为动态迭代方法）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: `discrete_combinatorial`, ai_method_type: `enumeration_brute_force`, gap_type: `structural_transformation`}
- tell_small_concepts: ["sum-free partition", "pigeonhole", "inductive shifting", "iterative reduction", "numerical contradiction"]
- expected_ai_method: 直接鸽巢——最大国家有≥330个成员，试图在330个数中找和三元组，或引用Schur定理但不构造具体的归纳平移论证。
- correct_method: 归纳平移+迭代鸽巢——逐国处理，每步用最小元素平移保持sum-free不变量，追踪缩减链1978→329→65→16→5→2→1>0得矛盾。

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type(`discrete_combinatorial`)/ai_method_type(`enumeration_brute_force`)/gap_type(`structural_transformation`)均能归入已有拓扑类别，无需新建。
- [x] 粒度是否一致——`discrete_combinatorial`是抽象粒度（与已有值一致），`enumeration_brute_force`是抽象粒度（与已有值一致），`structural_transformation`是中等粒度（与已有值一致）。
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell。problem_type区分了问题类型，ai_method_type区分了bare AI的错误方法，gap_type区分了从错误方法到正确方法的鸿沟性质（需要结构性变换——平移操作）。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。已有拓扑分类体系完全覆盖本题。

**拓扑进化建议**（如有）：无。

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

**局部pairs摘要**：
| Round | tell_topology | gap_type | is_knowledge_bottleneck | tell_small_concepts |
|---|---|---|---|---|
| 1 | (discrete_combinatorial, direct_calculation, method_problem_mismatch) | method_problem_mismatch | false | partition, sum-free, monochromatic triple |
| 2 | (discrete_combinatorial, enumeration_brute_force, search_space_estimation) | search_space_estimation | false | pigeonhole, induction, sum-free set, Schur number |
| 3 | (discrete_combinatorial, direct_calculation, method_problem_mismatch) | method_problem_mismatch | false | pigeonhole, 330, sum-free, largest country |
| 4 | (discrete_combinatorial, logical_deduction, knowledge_gap) | knowledge_gap | false | sum-free, contradiction, constraint |
| 5 | (discrete_combinatorial, direct_manipulation, structural_transformation) | structural_transformation | true | shifting, inductive step, minimum element, shift anchor |
| 6 | (discrete_combinatorial, algebraic_identity, structural_transformation) | structural_transformation | false | ceil division, size reduction, pigeonhole, iterative |
| 7 | (discrete_combinatorial, direct_calculation, method_problem_mismatch) | method_problem_mismatch | false | numerical verification, contradiction, 1978, 6 countries, reduction chain |

**全局pairs摘要**：
| # | scope_type | tell_topology | tell_small_concepts | why_not_visible_locally |
|---|---|---|---|---|
| 1 | path_feature | (discrete_combinatorial, direct_calculation, search_space_estimation) | iterative reduction, ceil division chain, numerical contradiction, 6-step path | 每个归纳步只显示局部缩减（如1978→329），但整条6步链恰好到达1>0（产生矛盾）需要看到所有步骤——没有任何单步或两步能揭示链条始终保持正数并终止于正值 |
| 2 | implicit | (discrete_combinatorial, direct_manipulation, structural_transformation) | shift preservation, sum-free invariant, inductive maintenance, base element | 平移操作保持sum-free性质对已处理国家同时成立——这在任何单步中都不可见。第n步的平移必须保持第1到n-1步建立的性质，这是对局部操作的全局约束 |

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI会尝试直接鸽巢（最大国家≥330成员），试图在330个数中找和三元组，或引用Schur定理但不构造具体的归纳平移论证。不会发现迭代平移技术——即逐国处理、用最小元素平移以同时保持所有已处理国家的sum-free不变量、追踪缩减链得矛盾的方法。
- suitable_for_poc: ["tell_extraction", "hint_injection", "topology_matching", "path_feature_detection"]
- discriminates_levels: true（这道题的难度在于发现平移技术这一非显然的归纳构造，能区分有无此知识的AI水平）

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
2. 更新`problem_extraction_progress`集合中`_key="329089"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1978p6"
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
    '_key': '329089',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1978p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1978p6')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证详情: compfiles_imo1978p6, 7 local pairs, 2 global pairs, answer非None, per-pair拓扑存在, why_not_visible_locally存在

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_imo1978p6
- solution_method_type: inductive_contradiction_with_pigeonhole
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否。已有拓扑分类体系完全覆盖本题。problem_type=discrete_combinatorial, ai_method_type=enumeration_brute_force, gap_type=structural_transformation均归入已有类别，粒度一致。
- 是否遇到异常: 否。入库和验证均一次通过。

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
