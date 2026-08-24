# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa1979p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa1979P5.lean
- **来源**: USA 1979 P5
- **ArangoDB progress记录_key**: 329320（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa1979P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：X has n members. Given n+1 subsets of X, each with 3 members, show that we can always find two which have just one member in common.
- 解答核心思路（1-2句话）：反证法——假设没有两个集合恰好交于一个元素（"好族"），用强归纳证明好族中3元子集的个数至多为n，与n+1矛盾。
- 解答关键步骤列表：
  1. 假设好族（任意两个3元子集的交集大小≠1），证明|S|≤n（强归纳）
  2. Case 1：某元素A出现在≥4个集合中。取s₀={A,B,C}，其他含A的集合与s₀交恰好2个元素，故含B或C
  3. 鸽巢原理：B或C中之一（记P）在≥2个其他含A的集合中，记为t₁={A,P,D}, t₂={A,P,E}
  4. 关键引理1：含A的集合必含P（否则需同时含Q,D,E→4个元素，矛盾）
  5. 关键引理2：含P的集合必含A（类似论证）
  6. 第三元素K互不相同且不出现在不含A的集合中；移除A,P,所有K→得T, |T|<n，对剩余集合用归纳假设
  7. Case 2：每个元素至多出现在3个集合中，双计数3|S|≤3n→|S|≤n
  8. 两种情况都得|S|≤n，与|S|=n+1矛盾

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.2 | 描述这道题的结构：已知什么对象？要证明什么结论？这是什么类型的问题？ | 已知n元集合X和n+1个3元子集，要证明存在两个子集恰好交于1个元素。这是一个组合存在性问题。 |
| 2 | 自由列举 | 0.4 | 列出所有可能用于此类组合存在性问题的证明策略 | 双计数、鸽巢原理、归纳法、反证法、概率方法、极值论证 |
| 3 | 小尝试 | 0.3 | 试着直接双计数：计算(元素,集合)关联对的总数。每个集合3个元素，总关联数=3(n+1)。能否限制每个元素属于多少个集合？ | 直接双计数得3(n+1)个关联对，但无法直接限制每个元素的度数——如果某元素出现在很多集合中，度数可以很高，无法得到矛盾。 |
| 4 | 思维操作引导 | 0.5 | 设反证法：假设没有两个集合恰好交于1个元素（"好族"）。那么任意两个相交的3元子集的交集大小是多少？ | 若两个3元子集相交且不等，交集大小≠1（假设），≠3（否则相等），所以恰好为2。即好族中相交的集合恰好共享2个元素。 |
| 5 | 推进 | 0.6 | 考虑一个出现在很多集合中的元素A（≥4个）。取s₀={A,B,C}。其他含A的集合与s₀的交集有什么性质？ | 其他含A的集合与s₀都含A，故交集≥1。由好族性质交集≠1，且≠3（集合不同），所以恰好为2。因此这些集合必含B或C。 |
| 6 | 思维操作引导 | 0.7 | 由鸽巢原理，B或C中之一（记P）在≥2个其他含A的集合中，记为t₁={A,P,D}, t₂={A,P,E}。证明：任何含A的集合必含P。 | 若某集合u含A不含P，则u与s₀交需含Q（s₀的第三元素），u与t₁交需含D，u与t₂交需含E。于是u至少含{A,Q,D,E}四个元素，但u只有3个元素，矛盾。故含A必含P。 |
| 7 | 推进 | 0.6 | 已知A和P总是同时出现。证明第三元素K互不相同且不出现在不含A的集合中，然后移除A,P,所有K得到更小的集合T，对剩余集合用归纳假设。 | 第三元素K互不相同（否则两个集合{A,P,K}相同）；K不出现在不含A的集合中（否则与含A,P,K的集合交于{K}，违反好族）。移除后|T|=n-|M|-2<n，剩余集合是T上的好族，由归纳假设≤|T|个。总|S|≤|M|+|T|=n-2≤n。 |
| 8 | 能量传递引导 | 0.3 | 如果每个元素至多出现在3个集合中呢？用双计数完成，然后总结。 | 3|S|=Σ度数≤3n→|S|≤n。两种情况都得|S|≤n，与|S|=n+1矛盾。证明完成！ |

**统计**：
- total_rounds: 8
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.6
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: discrete_combinatorial
- structure_features: n+1个3元子集分布在n元集合上，需证明存在两个子集恰好交于1个元素。核心结构是均匀集合族上的交集约束问题。
- key_objects: ["n-element set X", "3-element subsets (uniform family)", "pairwise intersection cardinality", "good family (no singleton intersection)", "incidence counting"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["contradiction", "strong_induction", "structural_reduction", "double_counting", "pigeonhole_principle", "case_analysis"]
- primary_pattern: structural_reduction
- knowledge_required: ["double counting (incidence counting)", "pigeonhole principle", "strong induction", "set intersection cardinality properties", "uniform set family constraints"]
- key_insight: 若某元素A出现在≥4个集合中，好族约束迫使A和另一个元素P总是一起出现（共现锁定），从而可以移除A、P和所有第三元素K，将问题归约到更小的实例上用归纳假设。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: direct counting / incidence enumeration（直接计数/关联枚举）
- translation_to: structural induction with case-based reduction（带分情况归约的结构归纳）
- translation_type: method_translation（方法翻译——从直接计数翻译到结构归纳）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "direct_calculation", gap_type: "structural_transformation"}
- tell_small_concepts: ["3-element subsets", "pairwise intersection", "good family", "popular element", "co-occurrence locking", "third element removal", "double counting", "strong induction"]
- expected_ai_method: 直接双计数或鸽巢原理，不设反证法框架，不识别需要结构归纳和分情况讨论
- correct_method: 反证法+强归纳：按是否有元素出现在≥4个集合中分情况，热门元素情况用共现锁定+结构归约，有界度数情况用双计数，两种情况都得|S|≤n与n+1矛盾

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type均可归入已有拓扑类别
- [x] 粒度是否一致——标注值与已有值粒度统一
- [x] 是否需要新的拓扑维度——三个维度足够区分此题的tell
- [x] 如果发现拓扑分类需要进化，在此写出建议：无

**拓扑进化建议**（如有）：无。已有拓扑分类体系足够覆盖此题。

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
- 局部tell_hint_pairs数量: 8 对
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 2 个，implicit型: 1 个

局部pair详见profile.json中的tell_hint_pairs字段。全局pair详见profile.json中的global_tell_hint_pairs字段。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI likely attempts direct double counting or pigeonhole without setting up the contradiction framework. It may count incidences but fail to recognize the need for structural induction and the case split on popular elements. The co-occurrence locking argument (A and P must always appear together) is a non-obvious structural insight that requires combining constraints from three different sets simultaneously — a bare AI is unlikely to discover this without guided hints.
- suitable_for_poc: ["tell_hint_injection", "structural_induction_guidance", "contradiction_setup", "co_occurrence_locking_discovery"]
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
2. 更新`problem_extraction_progress`集合中`_key="329320"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa1979p5"
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
    '_key': '329320',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa1979p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa1979p5')
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
- problem_id: compfiles_usa1979p5
- solution_method_type: strong_induction
- 局部(tell,hint)对数量: 8
- 全局(tell,hint)对数量: 3
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类体系足够覆盖此题
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
