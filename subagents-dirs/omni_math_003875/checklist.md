# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003875
- **文件路径**: subagents-dirs/omni_math_003875/problem.lean
- **来源**: AoPS omni_math (imo)
- **ArangoDB progress记录_key**: 333754（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003875/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Find all integers n for which each cell of an n×n table can be filled with one of the letters I, M, O such that: (1) in each row and each column, one third of entries are I, one third M, one third O; (2) in any diagonal, if the number of entries is a multiple of three, then one third are I, one third M, one third O. (IMO 2016 Problem 2)
- 解答核心思路（1-2句话）：必要性用二重计数（double counting）：取行≡2 mod 3、列≡2 mod 3、长度为3倍数的对角线三类格子，交叉处格子被计4次而其余计1次，迫使k²个交叉格子平衡故3|k即9|n。充分性用9×9显式构造+平铺。
- 解答关键步骤列表：
  1. 由行条件得3|n，令n=3k
  2. 考察三类格子：第2,5,8,...,3k-1行的所有格子（第一类）、第2,5,8,...,3k-1列的所有格子（第二类）、长度为3倍数的所有对角线上的格子（第三类）
  3. 二重计数：既属第一类又属第二类的格子被计4次，其余格子被计1次
  4. 三类各自平衡（行条件、列条件、对角线条件），故交叉处k²个格子也必须平衡
  5. 3|k² → 3|k → 9|n
  6. n=9时构造9×9模式（3×3块循环移位）
  7. n=9l时平铺l²个9×9模式，验证对角线条件在块边界处保持

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构。有哪些约束条件？我们在寻找什么类型的答案？ | n×n表格用I,M,O填满，满足：(1)每行每列各1/3；(2)长度为3倍数的对角线各1/3。寻找所有满足条件的正整数n。 |
| 2 | 自由列举 | 0.7 | 列出所有可能的方法来处理这个问题 | 检查小case(n=3,6,9)；从行/列条件推导必要条件；利用对角线约束；尝试二重计数；构造显式填充；用平铺证明充分性 |
| 3 | 小尝试 | 0.3 | 从行条件能立即推出什么？然后试n=3 | 行条件给出3|n。n=3时每行是{I,M,O}的排列（拉丁方）。两条主对角线长度均为3，都需1/3各字母。但任何3×3拉丁方中至少一条对角线是常数，故n=3不行 |
| 4 | 思维操作引导 | 0.5 | 写n=3k。考虑第2,5,8,...,3k-1行的所有格子、第2,5,8,...,3k-1列的所有格子、以及长度为3倍数的所有对角线上的格子。每个格子在这三类中总共被计算了几次？ | 交叉处格子（既在选中行又在选中列）被计4次（行类1次+列类1次+两类对角线各1次），其余格子被计1次。三类各自平衡，故交叉处k²个格子也必须平衡 |
| 5 | 思维操作引导 | 0.6 | 从二重计数的结论，k²个交叉格子必须平衡意味着什么？ | k²个格子各有1/3的I,M,O，故3|k²，进而3|k，因此9|n |
| 6 | 推进 | 0.4 | 现在构造n=9的有效填充。什么模式可行？ | 用9×9模式：3×3块循环移位，如III MMM OOO / MMM OOO III / OOO III MMM 重复3次。验证行、列、对角线均满足条件 |
| 7 | 能量传递引导 | 0.6 | 将n=9的构造推广到n=9l。为什么平铺可行？ | 平铺l²个9×9模式。行/列由重复性满足。对角线：cell(i,j)在3|长度的对角线上当且仅当i≡j mod 3或i+j≡1 mod 3，故对角线在每个9×9块内的部分恰是该块的3|长度对角线，因此平衡 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.9
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: 网格填充平衡问题，行/列/对角线三类约束，二重计数利用选中行与选中列的交叉处过计因子
- key_objects: n×n网格, 三符号I/M/O, 两类对角线, 交叉处k²个格子, 9×9模式, 平铺

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["small_case_analysis", "double_counting", "necessary_condition_first", "explicit_construction", "tiling_extension"]
- primary_pattern: double_counting
- knowledge_required: [" divisibility from balanced conditions", "double counting / inclusion-exclusion", "diagonal structure in grids", "modular arithmetic", "Latin squares"]
- key_insight: 二重计数三类格子（选中行、选中列、平衡对角线），交叉处格子被计4次而其余计1次，迫使k²个交叉格子平衡，故3|k即9|n

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 组合网格填充约束（行/列/对角线平衡条件）
- translation_to: 二重计数/容斥论证（过计因子推导整除性）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "case_by_case", gap_type: "structural_transformation"}
- tell_small_concepts: ["double counting", "row-column intersection", "diagonal length divisibility", "overcounting factor", "9×9 pattern tiling"]
- expected_ai_method: 尝试小case和直接构造，可能找到3|n但错过二重计数论证导致9|n
- correct_method: 二重计数三类格子（选中行、选中列、平衡对角线）用过计因子推出9|n；9×9显式构造+平铺证明充分性

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=characterization, ai_method_type=case_by_case, gap_type=structural_transformation 均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 不需要新维度——三个维度足够区分
- 拓扑进化建议：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

局部pairs详见profile.json。全局pairs：
1. path_feature型：二重计数完整路径特征（从3|n到9|n的过计因子论证）
2. implicit型：对角线长度可整除性与cell坐标的mod 3刻画（R7观察点）

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI会从行条件找到3|n并尝试小case，但很可能错过二重计数论证导致9|n。可能尝试代数方法（单位根）或在发现n=3失败后无法推广到一般n=3m。
- suitable_for_poc: ["tell_hint_injection", "topology_matching", "knowledge_bottleneck_detection"]
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
2. 更新`problem_extraction_progress`集合中`_key="333754"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_003875"
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
    '_key': '333754',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_003875',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_003875')
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
