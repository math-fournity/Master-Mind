# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa1980p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa1980P5.lean
- **来源**: USA 1980 P5
- **ArangoDB progress记录_key**: 329324（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa1980P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let x,y,z be real numbers in [0,1]. Show that x/(y+z+1) + y/(z+x+1) + z/(x+y+1) ≤ 1 + (1-x)(1-y)(1-z).
- 解答核心思路（1-2句话）：将不等式拆分为LHS≤1和1≤1+(1-x)(1-y)(1-z)两部分。第二部分由(1-x)(1-y)(1-z)≥0显然成立；第一部分利用x,y,z∈[0,1]推出x+y+z≤y+z+1等，将每个分式放缩到分母为x+y+z，求和后等于1。
- 解答关键步骤列表：
  1. 证明(1-x)(1-y)(1-z)≥0（positivity，因每个因子非负）
  2. 分情况讨论x+y+z=0（此时x=y=z=0，LHS=0≤1）和x+y+z>0
  3. 当x+y+z>0时，由x≤1得x+y+z≤y+z+1，故x/(y+z+1)≤x/(x+y+z)
  4. 同理y/(z+x+1)≤y/(x+y+z)，z/(x+y+1)≤z/(x+y+z)
  5. 三式相加：LHS≤(x+y+z)/(x+y+z)=1
  6. 由LHS≤1≤1+(1-x)(1-y)(1-z)得证

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.3 | 观察这个不等式：左边是三个分式之和，右边是1加上一个乘积。你能描述一下这个结构的特征吗？已知条件和目标分别是什么？ | 左边是x/(y+z+1)+y/(z+x+1)+z/(x+y+1)，每个分式分子是一个变量，分母是另外两个变量加1。右边是1+(1-x)(1-y)(1-z)。已知x,y,z∈[0,1]，目标是证明LHS≤RHS。 |
| 2 | 自由列举 | 0.4 | 对于这个不等式，你能想到哪些可能的证明方向？ | 1)直接通分展开比较 2)用经典不等式(AM-GM/Cauchy-Schwarz) 3)固定两个变量对第三个优化 4)把右边拆开分别证明 5)利用x,y,z∈[0,1]的范围做放缩 6)对称性分析 |
| 3 | 小尝试 | 0.2 | 试试直接通分展开，看看会怎样？ | 通分后分母是(y+z+1)(z+x+1)(x+y+1)，分子展开后项数极多，涉及x²y、xyz等交叉项，难以直接与右边比较。这条路非常繁琐，几乎不可行。 |
| 4 | 思维操作引导 | 0.5 | 既然直接展开太复杂，试试把不等式拆成两部分：先证左边≤1，再证1≤右边。第二部分是否显然？ | 第二部分：(1-x)(1-y)(1-z)≥0，因为x,y,z∈[0,1]所以每个因子∈[0,1]非负，乘积非负，故1≤1+(1-x)(1-y)(1-z)。所以只需证明左边≤1即可。 |
| 5 | 思维操作引导 | 0.6 | 现在需要证明x/(y+z+1)+y/(z+x+1)+z/(x+y+1)≤1。注意x,y,z∈[0,1]意味着x≤1，所以x+y+z≤y+z+1。这能给你什么启发？ | 因为x≤1，所以x+y+z≤y+z+1，当x+y+z>0时1/(y+z+1)≤1/(x+y+z)，故x/(y+z+1)≤x/(x+y+z)。同理y/(z+x+1)≤y/(x+y+z)，z/(x+y+1)≤z/(x+y+z)。 |
| 6 | 推进 | 0.3 | 继续，把这三个不等式加起来，能得到什么？别忘了检查边界情况。 | 三式相加：LHS≤x/(x+y+z)+y/(x+y+z)+z/(x+y+z)=(x+y+z)/(x+y+z)=1。当x+y+z>0时成立。当x+y+z=0时x=y=z=0，LHS=0≤1也成立。所以LHS≤1恒成立。 |
| 7 | 能量传递引导 | 0.4 | 现在两部分都证明了，把整个证明组合起来完成收尾。 | 由LHS≤1且1≤1+(1-x)(1-y)(1-z)，得LHS≤1+(1-x)(1-y)(1-z)。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 2.7
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: inequality_proof
- structure_features: 三分式求和≤常数+非负乘积项；变量约束在[0,1]；分母为"其余两变量+1"的对称结构
- key_objects: ["三分式和 x/(y+z+1)+y/(z+x+1)+z/(x+y+1)", "非负乘积 (1-x)(1-y)(1-z)", "统一分母 x+y+z", "变量范围约束 [0,1]"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["结构拆分(decomposition)", "放缩比较(bounding/comparison)", "分情况讨论(case_analysis)", "非负性利用(nonnegativity)"]
- primary_pattern: decomposition_and_comparison
- knowledge_required: ["分式不等式放缩", "变量范围约束利用", "非负乘积性质", "分母统一化技巧"]
- key_insight: 把不等式拆成LHS≤1和1≤RHS两部分，利用x≤1推出分母放缩到x+y+z使三分式和等于1

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: direct_algebraic_expansion（直接通分展开的代数计算方法）
- translation_to: structural_decomposition_with_comparison（结构拆分+放缩比较方法）
- translation_type: method_translation（从暴力代数展开翻译到结构化拆分+放缩策略）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "inequality_proof", ai_method_type: "direct_calculation", gap_type: "structural_transformation"}
- tell_small_concepts: ["inequality_splitting", "nonnegativity_bounding", "denominator_comparison", "unified_denominator", "variable_range_constraint"]
- expected_ai_method: direct_calculation——bare AI会尝试直接通分展开，陷入代数复杂度
- correct_method: decomposition_comparison——拆分不等式为LHS≤1和1≤RHS，用分母放缩证明LHS≤1

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=inequality_proof、ai_method_type=direct_calculation、gap_type=structural_transformation都能归入已有拓扑类别
- [x] 粒度一致——标注值与已有值粒度统一
- [x] 不需要新的拓扑维度——三个维度足够区分这道题的tell
- 无拓扑进化建议

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

局部pairs详见profile.json中的tell_hint_pairs字段。
全局pairs详见profile.json中的global_tell_hint_pairs字段。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接通分展开，陷入大量代数项的复杂比较中，无法有效简化。或者尝试用经典不等式（Cauchy-Schwarz等）但找不到合适的匹配形式。关键在于不会想到拆分不等式为LHS≤1和1≤RHS两部分，也不会想到利用x≤1做分母放缩到x+y+z。
- suitable_for_poc: ["POC-VMS-hint注入：验证拆分策略hint能否引导AI找到正确路径", "POC-VMS-tell识别：验证direct_calculation→structural_transformation的tell能否被形式化过滤命中"]
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
- [x] answer（proof类型，填要证明的结论）
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
- [x] tell_hint_pairs（7个pair，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（2个pair，含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象，stats中knowledge_bottleneck="R5", thinking_bottleneck="R4"均为字符串）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

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
2. 更新`problem_extraction_progress`集合中`_key="329324"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa1980p5"
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
    '_key': '329324',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa1980p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa1980p5')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_usa1980p5
- solution_method_type: decomposition_comparison
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，现有拓扑分类(inequality_proof/direct_calculation/structural_transformation)足够覆盖
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
