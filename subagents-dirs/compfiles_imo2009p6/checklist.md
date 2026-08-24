# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2009p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2009P6.lean
- **来源**: IMO 2009 P6
- **ArangoDB progress记录_key**: 329211（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2009P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let a₁, a₂, ..., aₙ be distinct positive integers and let M be a set of n-1 positive integers not containing s = a₁ + a₂ + ... + aₙ. A grasshopper is to jump along the real axis, starting at the point 0 and making n jumps to the right with lengths a₁, a₂, ..., aₙ in some order. Prove that the order can be chosen in such a way that the grasshopper never lands on any point in M.
- 解答核心思路（1-2句话）：通过强归纳对n归纳，WLOG排序后定义关键变量x=去掉最大元素后的和，按M中元素相对于x的位置分三种情况，在最难的情况中用鸽巢论证找安全元素。
- 解答关键步骤列表：
  1. WLOG排序a₁<...<aₙ，定义x=∑ᵢ₌₁ⁿ⁻¹aᵢ
  2. 情况1（x∈M且∃y∈M,y>x）：鸽巢论证找安全元素r使x-aᵣ∉M且s-aᵣ∉M，归纳n-2个元素
  3. 情况2（x∉M且∃y∈M,y>x）：M中≤x的元素≤n-2个，归纳前n-1个元素，aₙ放最后
  4. 情况3（所有m∈M,m≤x）：取z=max(M)，归纳避开M\\{z}，若命中z则交换跳过
  5. 一般情况通过排序置换归约到已排序情况

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.9 | 观察这道题的结构。已知什么？要求什么？什么是固定的，什么是可以选择的？ | 已知n个不同正整数和n-1元禁止集M（不含s），要求证明存在排列使前缀和避开M |
| 2 | 自由列举 | 0.8 | 列出所有可能方法方向 | 贪心、归纳、概率方法、匹配论、构造性、反证法 |
| 3 | 小尝试 | 0.6 | 尝试贪心：排序后从小到大跳跃 | 贪心排序失败，反例a={1,2,3},M={1,3,5} |
| 4 | 思维操作引导 | 0.5 | 对n做强归纳，定义x=去掉最大元素后的和，按M中元素相对x的位置分情况 | 三种情况：x∈M且∃y>x；x∉M且∃y>x；所有m≤x |
| 5 | 推进 | 0.4 | 情况2中M中≤x的元素最多多少个？如何用归纳假设？ | ≤n-2个，归纳前n-1个元素，aₙ放最后 |
| 6 | 思维操作引导 | 0.3 | 情况1中用鸽巢论证证明存在安全元素bᵢ | 坏元素经注入映射到M\\{x}（n-2个），共n-1个元素，至少一个好元素 |
| 7 | 能量传递引导 | 0.7 | 情况3如何处理？整合所有情况完成归纳 | 取z=max(M)，归纳避开M\\{z}，若命中z则交换跳过 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 4.2
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence
- structure_features: 排列存在性问题：n个不同正整数的排列使前缀和避开n-1元禁止集合M，M不含总和s。关键结构是前缀和的单调递增性和M的基数约束|M|=n-1
- key_objects: 正整数序列a₁,...,aₙ（互不相同）, 禁止集合M（|M|=n-1）, 前缀和/部分和, 排列/置换, 关键变量x=去掉最大元素后的和, 鸽巢论证中的坏元素集合Bad

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["强归纳", "情况分析", "鸽巢原理/计数论证", "交换技巧", "WLOG排序"]
- primary_pattern: 强归纳与情况分析
- knowledge_required: ["鸽巢原理", "强数学归纳法", "排列/置换", "前缀和", "有限集基数不等式", "注入映射与基数约束"]
- key_insight: 定义关键变量x=去掉最大元素后的和，按M中元素相对于x的位置分三种情况，在最难的情况中用鸽巢论证找到一个'安全'元素使得去掉它后归纳假设可用

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 贪心/枚举方法
- translation_to: 强归纳+情况分析+鸽巢计数
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: enumeration_brute_force, gap_type: structural_transformation}
- tell_small_concepts: ["强归纳", "关键变量x", "鸽巢计数", "情况分析", "交换技巧"]
- expected_ai_method: 贪心排序后依次跳跃，或枚举所有n!排列检查
- correct_method: 强归纳+按M中元素位置分三种情况+鸽巢论证找安全元素+交换技巧跳过最大mine

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=structural_existence, ai_method_type=enumeration_brute_force, gap_type=structural_transformation均可归入已有拓扑类别
- [x] 粒度一致——标注值和已有值粒度统一
- [x] 三个维度足够区分——per-pair拓扑中R6用knowledge_gap区分知识瓶颈，R5用search_space_estimation区分基数约束，其余用structural_transformation
- [x] 不需要新的拓扑维度

**拓扑进化建议**：无，当前拓扑分类体系足够覆盖此题

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

局部pairs详见profile.json中tell_hint_pairs数组（R1-R7），每个pair含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts。

全局pairs：
1. path_feature型：完整归纳证明路径特征（从贪心失败到强归纳+鸽巢的组合策略），why_not_visible_locally解释了三个层面协同在局部不可见
2. implicit型：鸽巢论证与归纳假设基数约束的隐含联系（observation_point=R6），why_not_visible_locally解释了安全元素选择需同时满足鸽巢存在性和归纳基数约束

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试贪心方法（排序后依次跳跃）或直接枚举排列，无法识别强归纳结构和关键变量x的作用。即使想到归纳，也难以发现需要按M中元素相对于x的位置分三种情况，尤其无法在情况1中构造鸽巢论证找到安全元素并验证归纳假设的基数约束。
- suitable_for_poc: ["tell_hint_injection", "topology_matching", "knowledge_bottleneck_detection"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

完整profile JSON已写入 `subagents-dirs/compfiles_imo2009p6/profile.json`。所有字段清单逐项检查通过。

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
2. 更新`problem_extraction_progress`集合中`_key="329211"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2009p6"
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
    '_key': '329211',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2009p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2009p6')
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
- problem_id: compfiles_imo2009p6
- solution_method_type: inductive_case_analysis
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，当前拓扑分类体系（structural_existence / enumeration_brute_force / structural_transformation等）足够覆盖此题
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
