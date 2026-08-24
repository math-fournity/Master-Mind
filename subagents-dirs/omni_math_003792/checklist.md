# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003792
- **文件路径**: subagents-dirs/omni_math_003792/problem.lean
- **来源**: AoPS omni_math (imo)
- **ArangoDB progress记录_key**: 333671（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003792/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Turbo蜗牛在2024行2023列棋盘上游戏。2022个隐藏怪物，每行（除第一行和最后一行）恰好一个怪物，每列至多一个怪物。Turbo从第一行出发，每次尝试选第一行一个格子开始，移动到相邻格子（可回访）。遇到怪物则尝试结束并回到第一行。Turbo记住每个访问过的格子是否有怪物。到达最后一行则游戏结束。求最小的n使得Turbo有策略保证在第n次尝试或之前到达最后一行。
- 解答核心思路（1-2句话）：利用鸽巢原理（2023列2022怪物→至少一列无怪物）和"每列至多一个怪物"的结构约束，先定位第2行怪物，再利用怪物所在列的安全性绕过它到达底部。边界情况用zigzag路径，若遇怪物则通过左逃走廊到达第1列（安全）再直下。
- 解答关键步骤列表：
  1. **下界(n≥3)**：第1次尝试第2行首个格子可能有怪物，第2次尝试第3行首个格子可能有怪物，故2次不够
  2. **尝试1**：扫掠第2行找到怪物位置(2,c)
  3. **非边界情况(2≤c≤2022)**：尝试2走c-1列到第3行，若无怪物则移到(3,c)直下c列到底（c列仅row2有怪物）；若有怪物在(3,c-1)，尝试3走c+1列到第3行（安全，因row3怪物在c-1），移到(3,c)直下到底
  4. **边界情况(c=1)**：尝试2走zigzag路径(1,2)→(2,2)→(2,3)→(3,3)→(3,4)→...(k,k)→(k,k+1)→...
  5. **zigzag无怪物**：直达底部，2次成功
  6. **zigzag遇怪物(r,r)或(r,r+1)**：尝试3沿zigzag安全段到row r-1，下到(r,r-1)（安全，row r怪物在r或r+1），左行到(1,r)即第1列（安全），直下第1列到底（第1列仅row2有怪物，r≥3故安全）

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
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：棋盘规模、怪物放置规则、Turbo的行动规则、优化目标是什么？已知量和未知量分别是什么？ | 2024行2023列棋盘，2022个怪物（每行2-2023恰好一个，每列至多一个），Turbo从第1行到第2024行，遇怪物回第1行，记住访问过的格子。优化目标是最小化保证到达的尝试次数n。已知：棋盘尺寸、怪物数量和分布规则。未知：每个怪物的具体位置。 |
| 2 | 自由列举 | 0.7 | 列出Turbo可能采取的所有策略方向。考虑信息收集型策略和直接冲刺型策略。 | 逐列探索（每列走一遍找怪物）、逐行扫掠（沿某行找该行怪物）、对角线/zigzag路径、二分搜索无怪物列、利用结构约束推导、混合策略（先收集信息再利用）等。 |
| 3 | 小尝试 | 0.4 | 试最简单的策略：直接走某一列到底。最坏情况需要多少次尝试？ | 如果走第c列，要么成功（c列无怪物），要么在(r,c)遇怪物。每次只了解一列，2023列最坏需2023次。太低效，需要利用结构约束。 |
| 4 | 思维操作引导 | 0.5 | 数一数：2023列、2022个怪物、每列至多一个怪物。这告诉你什么？进一步，如果怪物在(r,c)，"每列至多一个"对c列其他行意味着什么？ | 鸽巢原理：2023列2022怪物→至少一列无怪物。关键推论：若怪物在(r,c)，则c列在所有其他行都安全！这意味着知道一个怪物位置就能安全使用该列的其他行。 |
| 5 | 思维操作引导 | 0.4 | 先定位第2行的怪物（沿第2行扫掠）。若怪物在(2,c)且c不在边界，如何利用"c列在row 3及以下安全"来到达底部？ | 扫第2行找到(2,c)。若2≤c≤2022：尝试2走c-1列到row 3，若无怪物则移到(3,c)（安全，c列仅row2有怪物），直下c列到底。若(3,c-1)有怪物，尝试3走c+1列到row 3（安全，row3怪物在c-1），移到(3,c)直下到底。2-3次足够。 |
| 6 | 推进 | 0.5 | 处理边界情况：若第2行怪物在第1列(c=1)，只有一列相邻。设计一个zigzag路径作为尝试2，使得：(a)若无怪物直达底部，(b)若遇怪物在row r，则row r中路径左侧所有列安全，可左逃到第1列再直下。 | zigzag路径：(1,2)→(2,2)→(2,3)→(3,3)→(3,4)→...(k,k)→(k,k+1)→...→(2024,2023)。若遇怪物在(r,r)或(r,r+1)，则row r的怪物在col r或r+1，故col 1到r-1在row r都安全。尝试3：沿zigzag安全段到row r-1，下到(r,r-1)，左行到(r,1)，直下第1列到底（第1列仅row2有怪物，r≥3故安全）。 |
| 7 | 能量传递引导 | 0.6 | 你已经证明了3次足够。现在验证下界：为什么2次不够？考虑对手能做什么。 | 对手可以在Turbo第1次尝试进入row 2的第一个格子放怪物，在第2次尝试进入row 3的第一个格子放怪物。因此2次尝试无法保证成功，n≥3。结合上界n≤3，答案为3。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.9
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: discrete_combinatorial
- structure_features: 网格上的路径规划问题，带有隐藏障碍物（怪物）。障碍物满足部分置换约束（每行至多一个，每列至多一个）。信息不完全但可通过探索获取。策略需要保证最坏情况下成功。关键结构：2023列vs2022怪物→鸽巢原理保证一列无怪物；每列至多一个怪物→知道一个怪物位置即可安全使用该列其他行。
- key_objects: ["2024×2023棋盘", "2022个隐藏怪物（部分置换结构）", "Turbo的路径（从第1行到第2024行）", "尝试次数n", "zigzag对角线路径", "左逃走廊（row r中col 1到r-1）"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["鸽巢原理计数（2023列vs2022怪物）", "结构约束推导（每列至多一个→列安全性）", "分情况讨论（边界vs非边界）", "路径设计双重目的（直达或信息收集+逃逸）", "对手论证（下界证明）", "信息利用（已知安全格子作为路径基础）"]
- primary_pattern: 结构约束推导——利用"每列至多一个怪物"的约束，从局部信息（一个怪物位置）推导全局安全性（整列安全），并据此设计路径
- knowledge_required: ["鸽巢原理", "部分置换/匹配概念", "网格路径规划", "博弈论中的策略保证概念", "分情况讨论方法"]
- key_insight: 知道怪物在(r,c)意味着c列在所有其他行都安全——这个"一列至多一个怪物"的推论将局部信息转化为全局导航资源，使得3次尝试足以找到安全路径

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 逐列枚举搜索（暴力探索每列是否有怪物）
- translation_to: 结构约束导航（利用"每列至多一个怪物"的约束，从已知怪物位置推导列安全性，设计利用部分信息的路径）
- translation_type: method_translation——从暴力枚举方法翻译到结构利用方法，核心是将"每列至多一个怪物"从描述性约束转化为操作性资源

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "structural_transformation"}
- tell_small_concepts: ["鸽巢原理", "列安全性推论", "zigzag路径", "左逃走廊", "边界vs非边界分情况", "路径双重目的设计", "对手论证下界"]
- expected_ai_method: 逐列枚举——bare AI会尝试逐列探索或逐行扫掠所有怪物位置，试图收集完整信息后再规划路径，导致需要O(n)次尝试
- correct_method: 结构约束导航——利用"每列至多一个怪物"将局部怪物位置转化为整列安全性，设计3次尝试的分情况策略（非边界用相邻列绕过，边界用zigzag+左逃走廊）

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=discrete_combinatorial、ai_method_type=enumeration_brute_force、gap_type=structural_transformation都能归入已有拓扑类别
- [x] 粒度一致——标注值和已有值粒度统一
- [x] 三个维度足够区分——这道题的tell（暴力枚举→结构利用）和已有tell可以区分
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。当前分类体系足够。

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

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试逐列或逐行枚举策略，试图收集所有怪物位置后再规划路径。不会注意到"每列至多一个怪物"可以作为导航资源使用。在边界情况下更会卡住，因为只有一列相邻，无法直接绕过。预计会给出远大于3的答案或无法给出保证策略。
- suitable_for_poc: ["tell端验证：检测AI是否注意到鸽巢原理和列安全性推论", "hint端验证：注入结构约束导航方向后AI能否设计3次策略", "分叉检测：AI在边界情况处是否分叉到zigzag路径设计"]
- discriminates_levels: true——这道题区分了暴力枚举思维和结构利用思维，能区分不同水平的AI

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON，写入 `profile.json` 文件。已完成。

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
2. 更新`problem_extraction_progress`集合中`_key="333671"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_003792"
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
    '_key': '333671',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_003792',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_003792')
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
- problem_id: omni_math_003792
- solution_method_type: structural_constraint_navigation
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，当前分类体系（discrete_combinatorial / enumeration_brute_force / structural_transformation）足够
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
