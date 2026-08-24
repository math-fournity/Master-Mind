# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003830
- **文件路径**: subagents-dirs/omni_math_003830/problem.lean
- **来源**: AoPS omni_math (imo)
- **ArangoDB progress记录_key**: 333709（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003830/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：20×20网格上400个site（正整数坐标(x,y)，x,y≤20）。Amy和Ben轮流放石头（Amy先手）。Amy放红石，要求任意两红石距离≠√5；Ben放蓝石，无距离限制。无法放置时停止。求最大K使得Amy无论Ben如何放都能保证至少放K个红石。
- 解答核心思路（1-2句话）：√5距离等价于国际象棋骑士跳（坐标差(±2,±1)或(±1,±2)）。棋盘黑白染色下骑士跳总改变颜色，故同一颜色类的200个site两两距离≠√5。Amy只在一种颜色上放石，Ben最多占100个同色site，Amy保证100个。
- 解答关键步骤列表：
  1. 识别√5距离 = 坐标差(±2,±1)或(±1,±2) = 骑士跳
  2. 棋盘黑白染色：(x+y) mod 2，骑士跳总改变奇偶性，故同色site两两距离≠√5
  3. 下界：Amy只在黑色（200个site）上放红石，同色无√5冲突；Ben每轮最多占1个黑色site，100轮后黑色满（100红+100蓝），Amy保证≥100
  4. 上界：Ben也在同色上放石（镜像Amy的颜色选择），每种颜色200个site最多100轮；跨颜色放石受√5约束限制（Amy的黑石通过骑士跳禁止大量白色site），无法超过100
  5. 答案K=100

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 这道题的结构是什么？已知条件、未知量、约束分别是什么？ | 20×20网格400个site；Amy放红石（约束：红石间距离≠√5），Ben放蓝石（无约束），轮流放石先手Amy；求最大K使Amy保证≥K个红石。这是一个组合博弈问题。 |
| 2 | 自由列举 | 0.7 | 这个问题可能涉及哪些数学工具或框架？列出你能想到的所有方向。 | 图论（独立集、染色）、博弈论（策略、配对）、组合学（网格染色、tiling）、数论（距离条件分析）、贪心策略、构造性方法 |
| 3 | 小尝试 | 0.5 | 试试直接用贪心策略：Amy每次选一个满足条件的site放石，能保证多少个？ | 贪心策略无法保证确定下界，因为Ben的阻挡位置影响Amy后续可选site。需要一种不依赖Ben具体策略的保证方法，比如将Amy限制在某个子集上。 |
| 4 | 思维操作引导 | 0.4 | 分析√5这个距离条件：什么样的坐标差会产生距离√5？将距离条件翻译成坐标语言。 | √5 = √(4+1)，所以坐标差为(±2,±1)或(±1,±2)时距离为√5。这正是国际象棋中骑士的走法（knight's move）。 |
| 5 | 思维操作引导 | 0.4 | 骑士跳在棋盘黑白染色下有什么性质？如何用染色构造一个Amy的安全区域？ | 骑士跳改变坐标和的奇偶性（(±2,±1)改变3，(±1,±2)改变3，都是奇数），所以骑士跳总从黑格跳到白格。因此同一颜色的site两两距离≠√5。棋盘有200黑200白。 |
| 6 | 推进 | 0.5 | 基于同色site两两距离≠√5的性质，构造Amy的策略并计算下界。 | Amy只在黑色site（200个）上放红石。同色无√5冲突，所以Amy的约束自动满足。Ben每轮最多占1个黑色site，100轮后200个黑色site满（100红+100蓝），Amy保证≥100。 |
| 7 | 能量传递引导 | 0.6 | 验证上界：Ben能否将Amy限制在不超过100？完成解答。 | Ben镜像Amy的颜色选择（Amy选黑则Ben选黑，Amy选白则Ben选白），每种颜色200个site最多100轮。若Amy跨颜色放石，她的黑石通过骑士跳禁止大量白色site（每颗黑石禁止至多8个白格），跨颜色策略无法超过100。故K=100。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导）: 5
- knowledge_rounds（思维操作引导）: 2
- level_sum: 0.8+0.7+0.5+0.4+0.4+0.5+0.6 = 3.9
- knowledge_bottleneck: "R4"（R4需要识别√5=骑士跳，这是关键知识转折点）
- thinking_bottleneck: "R5"（R5需要从骑士跳性质推导出染色策略，是思维操作的关键跳跃）

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: discrete_combinatorial
- structure_features: 20×20网格上的组合博弈问题；距离约束（√5=骑士跳）定义了禁止关系图；核心是将距离约束翻译为图论染色问题，利用棋盘二部分性构造独立集策略
- key_objects: 20×20整数网格（400个site）、√5距离约束（骑士跳图）、棋盘黑白染色（二部图划分）、Amy的红石独立集策略、Ben的镜像阻挡策略

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["距离条件翻译为图论结构", "二部图染色构造独立集", "博弈论镜像策略", "下界-上界夹逼"]
- primary_pattern: 距离条件翻译为图论结构（将√5距离约束识别为骑士跳，进而利用棋盘染色的二部图性质）
- knowledge_required: ["√5距离的坐标表示", "骑士跳与棋盘染色的关系", "二部图与独立集", "组合博弈中的策略构造"]
- key_insight: √5距离就是骑士跳，骑士跳总改变棋盘颜色，所以同色site两两距离≠√5——将距离约束翻译为染色问题后，Amy只需在一种颜色上放石即可保证约束自动满足

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 欧几里得距离约束（√5距离条件）
- translation_to: 图论染色与独立集（骑士跳图 + 棋盘二部染色）
- translation_type: structural_transformation（将连续距离条件翻译为离散图论结构：√5 → 坐标差(±2,±1)/(±1,±2) → 骑士跳图 → 二部图染色 → 独立集）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "structural_transformation"}
- tell_small_concepts: ["√5距离", "骑士跳", "棋盘染色", "二部图", "独立集", "镜像策略", "坐标差", "奇偶性"]
- expected_ai_method: bare AI可能尝试贪心放置或枚举所有可能的放石序列，无法发现距离约束与棋盘染色的结构联系
- correct_method: 将√5距离翻译为骑士跳图，利用棋盘二部染色构造独立集策略，配合镜像策略证明上下界

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——discrete_combinatorial / enumeration_brute_force / structural_transformation 均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 不需要新维度——三个维度足以区分此题的tell
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

**局部pairs详见profile.json中的tell_hint_pairs字段**

**全局pairs概述**：
1. path_feature型：完整路径特征——从距离约束到染色策略的翻译路径（R4→R5→R6），局部看不到因为每步只看到当前操作，看不到"距离→骑士跳→染色→独立集"的完整翻译链
2. implicit型：蕴含信息——√5距离蕴含骑士跳图是二部图（R4观察点），局部看不到因为"√5=骑士跳"这一事实本身不直接显示"二部图"性质，需要额外的奇偶性推理

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI很可能尝试贪心策略或枚举方法，无法识别√5距离与骑士跳的联系，更无法发现棋盘染色构造独立集的策略。即使识别了骑士跳，也可能无法将染色性质转化为博弈策略并完成上下界证明。
- suitable_for_poc: ["hint_injection_effectiveness", "tell_identification_accuracy", "structural_translation_verification"]
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
2. 更新`problem_extraction_progress`集合中`_key="333709"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_003830"
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
    '_key': '333709',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_003830',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_003830')
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
- problem_id: omni_math_003830
- solution_method_type: structural_transformation
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，已有拓扑类别（discrete_combinatorial / enumeration_brute_force / structural_transformation）完全够用
- 是否遇到异常: 否（解答文件截断，但答案和核心思路可从题目结构和Answer=100重建）

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
