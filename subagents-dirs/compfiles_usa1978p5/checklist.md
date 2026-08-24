# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa1978p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa1978P5.lean
- **来源**: USA 1978 P5
- **ArangoDB progress记录_key**: 329317（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa1978P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：9个代表参加会议，每人最多说3种语言。任意3个代表中至少有2人说同一种语言。证明：存在3个代表说同一种语言。
- 解答核心思路（1-2句话）：反证法。假设不存在3个代表共享语言，用鸽巢原理证明每个代表最多与3人共享语言，再用计数论证找到3个两两不共享语言的代表，与题设矛盾。
- 解答关键步骤列表：
  1. 假设不存在3个代表共享一种语言
  2. 鸽巢原理：每人最多3种语言，若某人与4+人共享语言，则其中两人共享同一种语言，三人共语矛盾 → 每人最多与3人共享
  3. 固定代表A，A及与A共享的人最多4个（3+1），9人中存在B不与A共享
  4. A的共享者+B的共享者+{A,B}最多3+3+2=8个，9人中存在C不与A也不与B共享
  5. A、B、C两两不共享语言，与"任意3人至少2人共享"矛盾，证毕

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
| 1 | 纯元认知观察 | 0.2 | 请描述这道题的结构：已知条件是什么？要证明什么？关键数字有哪些？ | 9个代表，每人最多3种语言；任意3人中至少2人共享语言；需证明存在3人共享同一种语言。关键数字：9人、3语言上限、3人组条件。 |
| 2 | 自由列举 | 0.5 | 列出所有可能的证明方法方向，不需要判断哪个最好。 | 直接构造三人共语；反证法假设无三人共语；鸽巢原理；图论建模（代表为点，共享语言为边）；计数论证；归纳法。 |
| 3 | 小尝试 | 0.3 | 试试直接构造：能否从9人中直接找出3个说同一种语言的代表？ | 直接构造困难：不知道哪些语言被哪些人说，信息不够具体。可能尝试统计每种语言的使用人数，但无法直接得出三人共语的结论。 |
| 4 | 思维操作引导 | 0.4 | 换用反证法：假设不存在3个代表共享语言。在这个假设下，每个代表最多能与多少人共享语言？为什么？ | 每人最多与3人共享语言。因为每人最多说3种语言，若与4+人共享，由鸽巢原理，4人中至少2人通过同一种语言与之共享，这3人就共语了，矛盾。所以每人最多与3人共享。 |
| 5 | 推进 | 0.5 | 已知每人最多与3人共享语言。固定一个代表A，A及其共享者最多多少人？能否找到一个不与A共享的代表B？再继续找C？ | A及共享者最多4人（3+1），9人中至少5人不在其中，取B不与A共享。A的共享者+B的共享者+{A,B}最多3+3+2=8人，9人中存在C不与A也不与B共享。 |
| 6 | 推进 | 0.3 | 现在你有A、B、C三个代表，两两不共享语言。这与题目条件有什么矛盾？ | 题目要求任意3人中至少2人共享语言，但A、B、C两两不共享，违反了这个条件。矛盾！所以假设错误，存在3人共享语言。 |
| 7 | 能量传递引导 | 0.7 | 请完整总结这个反证法证明的逻辑链条。 | 反证假设无三人共语→鸽巢原理得每人最多与3人共享→固定A找到不共享的B→A和B的共享圈最多覆盖8人，找到不与两者共享的C→A,B,C两两不共享，违反"任意3人至少2人共享"→矛盾，证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5
- knowledge_rounds（思维操作引导的轮数）: 1
- level_sum: 2.9
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

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
- problem_type: discrete_combinatorial
- structure_features: 9个有限元素（代表），每个元素关联≤3个标签（语言），任意3元素中至少2个共享标签，证明存在3元素共享同一标签。有限集计数+鸽巢原理+反证法。
- key_objects: ["delegates (Fin 9)", "languages (Finset L)", "sharing relation (Share)", "pigeonhole principle", "contradiction assumption"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["proof_by_contradiction", "pigeonhole_principle", "counting_argument", "degree_bounding"]
- primary_pattern: proof_by_contradiction
- knowledge_required: ["pigeonhole_principle", "finite_set_cardinality", "proof_by_contradiction", "union_bound"]
- key_insight: 假设无三人共语，则鸽巢原理迫使每人最多与3人共享语言，从而9人中能找到3人两两不共享，与"任意3人至少2人共享"矛盾。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: direct_existence_construction（直接构造存在性证明）
- translation_to: contradiction_with_pigeonhole_counting（反证法+鸽巢原理+计数论证）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "direct_calculation", gap_type: "method_problem_mismatch"}
- tell_small_concepts: ["pigeonhole", "contradiction", "counting", "pairwise_non_sharing", "language_sharing", "degree_bound"]
- expected_ai_method: 直接构造三人共语或简单计数共享对数，缺乏反证法框架
- correct_method: 反证法+鸽巢原理约束共享度+计数论证找到两两不共享的三人+矛盾

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 可以。discrete_combinatorial、direct_calculation、method_problem_mismatch均已存在且粒度合适。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 一致。均为中等抽象粒度。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。这道题的核心gap是"直接构造→反证法+鸽巢"的方法转换，method_problem_mismatch准确描述。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。

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
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs详情**：
- R1: tell="题目结构未识别", hint="描述题目结构：9人、≤3语言、任意3人≥2共享、证3人共语", hint_level=0.2, situation_type="纯元认知观察", is_knowledge_bottleneck=false, tell_topology={problem_type:"discrete_combinatorial", ai_method_type:"direct_calculation", gap_type:"method_problem_mismatch"}, tell_small_concepts=["delegate_count","language_limit","pairwise_condition"]
- R2: tell="方向未列举", hint="列出所有可能方法：直接构造、鸽巢、反证、图论、计数", hint_level=0.5, situation_type="自由列举", is_knowledge_bottleneck=false, tell_topology={problem_type:"discrete_combinatorial", ai_method_type:"enumeration_brute_force", gap_type:"search_space_estimation"}, tell_small_concepts=["approach_enumeration","contradiction","pigeonhole"]
- R3: tell="直接构造受阻", hint="试直接构造三人共语", hint_level=0.3, situation_type="小尝试", is_knowledge_bottleneck=false, tell_topology={problem_type:"discrete_combinatorial", ai_method_type:"direct_calculation", gap_type:"method_problem_mismatch"}, tell_small_concepts=["direct_construction","existence_proof"]
- R4: tell="鸽巢原理未应用", hint="反证法假设无三人共语，用鸽巢原理推导每人最多与3人共享", hint_level=0.4, situation_type="思维操作引导", is_knowledge_bottleneck=true, tell_topology={problem_type:"discrete_combinatorial", ai_method_type:"logical_deduction", gap_type:"knowledge_gap"}, tell_small_concepts=["pigeonhole","sharing_degree_bound","contradiction_assumption"]
- R5: tell="计数论证未推进", hint="用计数找到3人两两不共享语言", hint_level=0.5, situation_type="推进", is_knowledge_bottleneck=false, tell_topology={problem_type:"discrete_combinatorial", ai_method_type:"case_by_case", gap_type:"structural_transformation"}, tell_small_concepts=["counting_argument","union_bound","pairwise_non_sharing"]
- R6: tell="矛盾未识别", hint="A,B,C两两不共享与题设矛盾", hint_level=0.3, situation_type="推进", is_knowledge_bottleneck=false, tell_topology={problem_type:"discrete_combinatorial", ai_method_type:"logical_deduction", gap_type:"method_problem_mismatch"}, tell_small_concepts=["contradiction","pairwise_condition","hypothesis_violation"]
- R7: tell="证明未收束", hint="总结反证法完整证明", hint_level=0.7, situation_type="能量传递引导", is_knowledge_bottleneck=false, tell_topology={problem_type:"discrete_combinatorial", ai_method_type:"logical_deduction", gap_type:"method_problem_mismatch"}, tell_small_concepts=["proof_summary","contradiction_completion"]

**全局pairs详情**：
1. path_feature型: scope="完整证明路径", tell="反证法→鸽巢约束共享度→计数找三人不共享→矛盾，这条完整路径", hint="识别这是一条反证法路径：先假设否定结论，用鸽巢约束参数，用计数找到反例三元组", hint_level=0.6, generalizability="high — 适用于所有'存在性证明+有限结构+参数约束'的组合问题", why_not_visible_locally="局部步骤中只看到'每人最多与3人共享'或'找到B不与A共享'等单步操作，无法看到这些步骤串起来构成完整的反证法路径。关键在于鸽巢约束和计数找反例这两步的协同——单独看任何一步都不知道它在为最终矛盾服务。"
2. implicit型: scope="鸽巢约束的隐含信息", observation_point="R4", tell="反证假设下鸽巢原理隐含的共享度上界≤3", hint="在反证假设下，鸽巢原理不仅给出上界，还隐含了'9人减去覆盖集'的计数空间足够大", hint_level=0.5, generalizability="medium — 适用于'鸽巢原理+反证法'组合的有限结构问题", why_not_visible_locally="在R4局部视角中，鸽巢原理只被用来推导'每人最多与3人共享'这个单步结论。这个上界≤3隐含的信息——它使得覆盖集最多4人(1个+3个)、两个不相交覆盖集最多8人——在R4的局部步骤中完全不可见，需要后续计数步骤才能显现。"

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI可能尝试直接构造三人共语或简单计数共享对数，但缺乏反证法框架。关键错误是想不到"假设无三人共语→鸽巢约束共享度≤3→计数找两两不共享的三人→矛盾"这条路径。即使想到反证法，也可能卡在"如何利用鸽巢原理约束共享度"这一步。
- suitable_for_poc: ["tell_hint_injection", "contradiction_guidance", "pigeonhole_recognition", "method_translation_poc"]
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

**将完整JSON写入工作目录的 `profile.json` 文件** — 已完成，写入 `subagents-dirs/compfiles_usa1978p5/profile.json`

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
2. 更新`problem_extraction_progress`集合中`_key="329317"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa1978p5"
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
    '_key': '329317',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa1978p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa1978p5')
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
- problem_id: compfiles_usa1978p5
- solution_method_type: contradiction_with_pigeonhole_counting
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，现有拓扑分类足够覆盖
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
