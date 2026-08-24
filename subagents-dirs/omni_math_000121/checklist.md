# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000121
- **文件路径**: subagents-dirs/omni_math_000121/problem.lean
- **来源**: AoPS omni_math (china_team_selection_test)
- **ArangoDB progress记录_key**: 329992（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000121/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：给定正实数α，求所有f:N⁺→R使得f(k+m)=f(k)+f(m)对所有满足αm≤k≤(α+1)m的正整数k,m成立。
- 解答核心思路（1-2句话）：将约束条件转化为n=k+m时k的有效区间[αn/(α+1), (α+1)n/(α+2)]，区间长度n/((α+1)(α+2))随n增长，对足够大的n必含整数，从而用强归纳证明f(n)=cn；小n用反向传播处理。
- 解答关键步骤列表：
  1. 识别为受限Cauchy方程，f(n)=cn平凡满足条件
  2. 将约束αm≤k≤(α+1)m用n=k+m改写为k∈[αn/(α+1), (α+1)n/(α+2)]
  3. 区间长度=n/((α+1)(α+2))，当n>(α+1)(α+2)时区间长度>1，必含整数k
  4. 强归纳：对大n，f(n)=f(k)+f(n-k)=ck+c(n-k)=cn
  5. 反向传播：取大N，分解N=k+n（k大、n小），则f(n)=f(N)-f(k)=cN-ck=cn
  6. 结论：f(n)=cn对所有n∈N⁺成立

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.3 | 观察这道题的结构：函数方程f(k+m)=f(k)+f(m)的形式让你想到什么？约束条件αm≤k≤(α+1)m与普通Cauchy方程有何不同？ | 这是Cauchy函数方程的受限版本。普通Cauchy方程f(k+m)=f(k)+f(m)对所有k,m成立，解为f(n)=cn。这里约束αm≤k≤(α+1)m限制了方程成立的范围，即k/m∈[α,α+1]。需要证明这个受限条件仍足以确定f(n)=cn。 |
| 2 | 自由列举 | 0.5 | 列出处理这类受限函数方程的所有可能策略方向。 | 1)直接代入特殊值（k=m等）获取信息；2)尝试归纳法证明f(n)=cn；3)将约束改写为关于n和k的关系；4)利用区间密度论证有效分解的存在性；5)反向传播：用大n的结论推导小n。 |
| 3 | 小尝试 | 0.3 | 试一试直接代入k=m，能得到什么？这足够确定f吗？ | 当α≤1时，αm≤m≤(α+1)m成立，得f(2m)=2f(m)。但这只给出2的幂次上的信息，无法确定所有n的值。当α>1时k=m不满足约束。直接代入特殊值信息有限，需要更系统的方法。 |
| 4 | 思维操作引导 | 0.6 | 执行以下思维操作：将约束条件αm≤k≤(α+1)m用n=k+m（即m=n-k）改写，消去m，得到关于k和n的不等式。观察k的有效区间。 | 代入m=n-k：α(n-k)≤k≤(α+1)(n-k)，化简得k≥αn/(α+1)且k≤(α+1)n/(α+2)。所以k的有效区间为[αn/(α+1), (α+1)n/(α+2)]，区间长度=(α+1)n/(α+2)-αn/(α+1)=n/((α+1)(α+2))。 |
| 5 | 推进 | 0.5 | 继续推进：区间长度n/((α+1)(α+2))随n增长意味着什么？这对证明有什么用？ | 区间长度随n线性增长。当n>(α+1)(α+2)时，区间长度>1，必含至少一个整数k。且k∈[1,n-1]（因为k≥αn/(α+1)>0且k≤(α+1)n/(α+2)<n）。这意味着对足够大的n，总存在有效的分解n=k+m，且k,m<n，可以用强归纳。 |
| 6 | 思维操作引导 | 0.7 | 现在执行关键思维操作：设计完整的归纳证明框架。大n用强归纳，小n怎么办？提示——可以用大n的结论反向推导小n。 | 强归纳：对n>(α+1)(α+2)，存在有效分解n=k+m，k,m<n，由归纳假设f(k)=ck, f(m)=cm，故f(n)=ck+cm=cn。对小n：取足够大的N使N=k+n为有效分解且k足够大（f(k)=ck已知），则f(n)=f(N)-f(k)=cN-ck=cn。 |
| 7 | 能量传递引导 | 0.4 | 你已经掌握了所有关键组件——区间密度、强归纳、反向传播。现在把它们组装成完整证明，确认f(n)=cn是唯一解。 | 完整证明：(1)f(n)=cn平凡满足条件。(2)唯一性：对n>N₀=(α+1)(α+2)用强归纳，区间含整数k，f(n)=f(k)+f(n-k)=cn。(3)对小n，取大N使N=k+n有效且k>N₀，则f(n)=f(N)-f(k)=c(N-k)=cn。(4)故f(n)=cn∀n。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.3+0.5+0.3+0.6+0.5+0.7+0.4=3.3
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: null
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization（求所有满足条件的函数，即刻画类问题）
- structure_features: 受限Cauchy函数方程，约束αm≤k≤(α+1)m限制了加性关系成立的范围，需要从受限条件推导全局线性结构
- key_objects: [正整数函数f:N⁺→R, 正实数参数α, Cauchy加性方程, 约束区间[αm,(α+1)m], 有效分解区间[αn/(α+1),(α+1)n/(α+2)]]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["restricted_to_general_extension", "constraint_reformulation", "interval_density_argument", "strong_induction", "backward_propagation"]
- primary_pattern: restricted_to_general_extension（从受限条件扩展到全局结论）
- knowledge_required: ["Cauchy函数方程", "强归纳法", "区间算术", "加性函数理论"]
- key_insight: 将约束改写为k的有效区间后，区间长度n/((α+1)(α+2))随n线性增长，对大n必含整数，使强归纳成立；小n用反向传播处理

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: restricted_additivity_with_constraint（带约束的受限加性方程，直接代入视角）
- translation_to: interval_density_induction（区间密度驱动的强归纳+反向传播框架）
- translation_type: domain_extension（将受限域上的性质扩展到全域）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_manipulation, gap_type: structural_transformation}
- tell_small_concepts: ["受限Cauchy方程", "约束区间改写", "区间密度", "强归纳", "反向传播"]
- expected_ai_method: 直接代入特殊值（k=m等），试图从特殊情形归纳出一般规律，但无法系统性地处理约束条件
- correct_method: 将约束改写为关于n和k的区间，利用区间长度随n增长的密度性质驱动强归纳，配合反向传播处理小n

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——characterization/direct_manipulation/structural_transformation能归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell
- [x] 无需新的拓扑维度

**拓扑进化建议**：无

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

**局部pair详情**（见profile.json中tell_hint_pairs数组）：
- R1: tell=看到函数方程但未识别为受限Cauchy类型, topology=(characterization, direct_manipulation, method_problem_mismatch)
- R2: tell=列出方向但未识别约束改写是关键, topology=(characterization, enumeration_brute_force, search_space_estimation)
- R3: tell=直接代入k=m只得到局部信息, topology=(characterization, direct_calculation, method_problem_mismatch)
- R4: tell=未将约束改写为关于n和k的区间, topology=(characterization, direct_manipulation, structural_transformation)
- R5: tell=看到区间但未连接到归纳可行性, topology=(characterization, algebraic_identity, method_translation)
- R6: tell=有区间密度但未设计完整归纳+反向传播框架, topology=(characterization, logical_deduction, method_translation)
- R7: tell=有所有组件但未组装成完整证明, topology=(characterization, logical_deduction, method_problem_mismatch)

**全局pair详情**（见profile.json中global_tell_hint_pairs数组）：
- GP1 (path_feature): 完整证明路径"约束改写→区间密度→强归纳→反向传播"作为整体策略不可在单步中看到
- GP2 (implicit): f(n)=cn是唯一解（非仅一个解）需要完整归纳论证，蕴含在问题结构中

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会识别出这是Cauchy型方程并尝试直接代入特殊值，但会卡在如何从受限条件系统性地扩展到全局结论。关键错误：不会想到将约束改写为关于n和k的区间来利用区间密度，也不会设计反向传播处理小n的base case。可能只证明α为特殊值（如α=1）的情形，无法处理一般α。
- suitable_for_poc: ["POC-VMS-hint-injection", "POC-VMS-tell-detection", "POC-VMS-path-feature"]
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
- [x] answer（**⚠️ 必填，不能为None**。proof类型填要证明的结论，如"sum >= ..."；existence_construction类型填构造的存在性结论；numerical类型填数值答案）
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
2. 更新`problem_extraction_progress`集合中`_key="329992"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_000121"
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
    '_key': '329992',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_000121',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_000121')
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
