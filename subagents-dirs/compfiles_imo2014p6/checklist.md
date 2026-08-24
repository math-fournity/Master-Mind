# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2014p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2014P6.lean
- **来源**: IMO 2014 P6
- **ArangoDB progress记录_key**: 329232（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2014P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：平面上一组直线处于一般位置（无两条平行、无三条共点），将平面切成若干区域，其中有界区域称为有限区域。证明对所有足够大的n，在任意n条一般位置的直线中，可以给至少√n条线染蓝色，使得没有有限区域的边界全为蓝色。
- 解答核心思路（1-2句话）：取一个极大的合法蓝色集合B（无有限区域边界全蓝），对每条红线利用极大性得到一个见证区域（边界除该红线外全蓝），将每条红线关联到一个蓝色点（两蓝线交点），证明每个蓝点至多关联2条红线（否则三条共点矛盾），从而n-k ≤ 2·C(k,2) = k²-k，得n ≤ k²即k ≥ √n。
- 解答关键步骤列表：
  1. 定义ValidBlue（无有限区域边界全蓝），取极大合法蓝色集合B
  2. 极大性保证：每条红线ℓ都有一个见证区域（有限区域，边界线除ℓ外全蓝）
  3. 沿见证区域边界顺时针走，识别红点r（红线×蓝线交点）和蓝点b（蓝线×蓝线交点）
  4. 构造关联映射：红线ℓ → 蓝点b
  5. 关键引理：每个蓝点至多关联2条红线——若3条红线关联同一蓝点b，由抽屉原理两条红点在同一蓝线上（b的两侧），第三条红线的区域在b处转向某个红点，迫使三条线共点，与一般位置矛盾
  6. 计数：蓝点数 = C(k,2) = k(k-1)/2，红线数 ≤ 2·k(k-1)/2 = k²-k，故n = k + (n-k) ≤ k + k²-k = k²，得k ≥ √n

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
| 1 | 纯元认知观察 | 0.3 | 描述这道题的结构：给定什么，要证明什么，关键约束是什么？ | 给定n条一般位置的直线，要证明可以给≥√n条线染蓝色，使得没有有限区域的边界全为蓝色。关键约束是有限区域的边界不能全蓝。 |
| 2 | 自由列举 | 0.5 | 列出所有可能的方法来证明存在这样的染色（至少√n条蓝线）。 | 贪心染色、概率方法、归纳法、极大性论证、直接构造、计数/双射论证 |
| 3 | 小尝试 | 0.4 | 试贪心方法：逐条染蓝，如果加入后不产生全蓝边界就加。这会出什么问题？ | 贪心可能过早停止——逐条加入可能阻塞很多未来添加。问题在于贪心不保证√n，可能停得太早。需要一种方法来界定未被染色的线的数量。 |
| 4 | 思维操作引导 | 0.6 | 换个角度：取一个极大的（按包含关系）合法蓝色集合B。极大性对每条非蓝（红）线意味着什么？ | 对每条红线ℓ，由于B极大，加入ℓ会破坏合法性。所以存在一个有限区域，加入ℓ后边界全蓝——即该区域边界线除ℓ外全蓝。这是ℓ的"见证区域"。 |
| 5 | 思维操作引导 | 0.7 | 对每条红线ℓ及其见证区域，沿边界顺时针走。边界有一条红边（在ℓ上）其余蓝边。识别红点r（红边端点，红线×蓝线交点）和下一个顶点b（蓝×蓝交点）。你能把ℓ关联到什么？ | 每条红线ℓ映射到一个蓝点b（两条蓝线的交点）。这给出了从红线到蓝点的关联映射。 |
| 6 | 推进 | 0.7 | 证明关键引理：每个蓝点至多关联2条红线。如果3条红线关联同一蓝点b会怎样？ | b处恰好有2条蓝线穿过。3条红线的红点中，由抽屉原理两条在同一蓝线上（b的两侧）。第三条红线的区域在b处必须转向某个红点，但这迫使第三条线经过该红点，导致三条线共点，与一般位置矛盾。 |
| 7 | 推进 | 0.5 | 完成计数论证。若k=|B|条蓝线，蓝点有多少个？红线至多多少条？ | 蓝点数=C(k,2)=k(k-1)/2。每个蓝点至多2条红线，故红线≤2·k(k-1)/2=k²-k。总n=k+(n-k)≤k+k²-k=k²，所以k≥√n。 |
| 8 | 能量传递引导 | 0.8 | 总结完整证明结构。关键洞见是什么？ | 1)取极大合法蓝色集B；2)每条红线有见证区域；3)关联红线到蓝点；4)每个蓝点至多2条红线（一般位置矛盾）；5)n≤k²得k≥√n。关键洞见是极大性论证将染色存在性问题转化为计数问题。 |

**统计**：
- total_rounds: 8
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 4.5
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

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
- problem_type: structural_existence
- structure_features: 一般位置直线排列，有限区域边界约束，√n下界的存在性证明，极大性论证+关联映射计数
- key_objects: 一般位置直线集合，有限区域，蓝色/红色染色，极大合法蓝色集合，见证区域，红点r，蓝点b，关联映射

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["极大性论证", "关联映射计数", "反证法利用一般位置", "几何-组合翻译", "抽屉原理"]
- primary_pattern: 极大性论证
- knowledge_required: ["直线排列与区域", "一般位置条件", "极大性原理", "双计数/关联映射", "组合几何"]
- key_insight: 取极大合法蓝色集，每条红线有见证区域，关联到蓝点后每个蓝点至多2条红线（一般位置矛盾），得n≤k²即k≥√n

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 几何/组合（直线排列、区域边界染色约束）
- translation_to: 计数/双射论证（极大性→见证区域→关联映射→纤维计数→√n界）
- translation_type: structural_transformation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: enumeration_brute_force, gap_type: structural_transformation}
- tell_small_concepts: ["极大性", "见证区域", "关联映射", "纤维计数", "一般位置矛盾", "边界遍历", "蓝点", "红点"]
- expected_ai_method: enumeration_brute_force（bare AI预期会尝试贪心或穷举染色，不利用极大性结构）
- correct_method: 极大性论证+关联映射计数（取极大合法蓝色集，关联红线到蓝点，纤维界至多2，计数得n≤k²）

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能归入已有的拓扑类别？ 是。structural_existence、enumeration_brute_force、structural_transformation均已存在且粒度合适。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ 是。均为抽象层级。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ 足够。这道题的核心gap是将染色存在性问题通过极大性翻译为计数问题，属于structural_transformation。
- [x] 如果发现拓扑分类需要进化，在此写出建议： 无需进化。

**拓扑进化建议**（如有）：无。现有拓扑分类足够。

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

局部pairs详见profile.json中的tell_hint_pairs字段。
全局pairs详见profile.json中的global_tell_hint_pairs字段。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI预期会尝试贪心染色或概率方法，不利用极大性结构。没有极大性→见证区域→关联映射的洞见，无法导出√n下界。可能尝试直接构造或归纳但无法得到正确的界。
- suitable_for_poc: ["tell_hint_injection", "path_comparison", "bottleneck_identification"]
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
2. 更新`problem_extraction_progress`集合中`_key="329232"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2014p6"
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
    '_key': '329232',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2014p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2014p6')
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
- problem_id: compfiles_imo2014p6
- solution_method_type: maximality_argument
- 局部(tell,hint)对数量: 8
- 全局(tell,hint)对数量: 3
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有拓扑分类（structural_existence / enumeration_brute_force / structural_transformation等）足够覆盖此题。
- 是否遇到异常: 无

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
