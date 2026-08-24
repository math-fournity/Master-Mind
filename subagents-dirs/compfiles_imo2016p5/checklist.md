# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2016p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2016P5.lean
- **来源**: IMO 2016 P5
- **ArangoDB progress记录_key**: 329238（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2016P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：黑板上有方程(x-1)(x-2)...(x-2016) = (x-1)(x-2)...(x-2016)，共4032个因子。求最小的k，使得恰好擦除k个因子后（每边至少留一个），剩余方程无实数解。
- 解答核心思路（1-2句话）：答案是k=2016。构造：左边擦除所有n%4∈{2,3}的因子，右边擦除所有n%4∈{0,1}的因子，各1008个共2016个；利用恒等式(x-(4k+2))(x-(4k+3))=(x-(4k+1))(x-(4k+4))+2证明两边乘积永不相等。下界由鸽巢原理给出：k<2016时必有公共因子，x=i即为实数解。
- 解答关键步骤列表：
  1. 下界证明：k<2016时剩余因子总数>2016，由鸽巢原理存在(x-i)同时出现在两边，x=i是解，故k≥2016
  2. 构造：按模4分组，左留{4k+1,4k+4}，右留{4k+2,4k+3}，各504对
  3. 关键恒等式：(x-(4k+2))(x-(4k+3)) = (x-(4k+1))(x-(4k+4)) + 2，每对右因子比左因子大2
  4. 无实数解证明：分情况讨论x相对于根的位置——x等于某根时一边为0另一边非0；x落在区间(4m+1,4m+4)内时左乘积为负右乘积为正（或用重配对+恒等式比较）；x在所有区间外时每对右>左故乘积右>左
  5. 最优性：下界2016与构造2016匹配，答案k=2016

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
| 1 | 纯元认知观察 | 0.3 | 观察这道题的结构：黑板上有4032个因子（左右各2016个），需要擦除恰好k个使得剩余方程无实数解。请描述题目的已知条件和目标。 | 已知左右两边都是(x-1)(x-2)...(x-2016)，共4032个因子。需要擦除恰好k个（每边至少留一个），使剩余方程∏(x-a_i)=∏(x-b_j)无实数解。目标是求最小的k。 |
| 2 | 自由列举 | 0.5 | 要让一个方程无实数解，有哪些可能的策略？请列出你能想到的所有方向。 | 1)让两边永远不相等（如一边恒大于另一边）；2)让两边符号相反；3)利用多项式性质比较根集；4)减少因子使两边根集不重叠；5)鸽巢原理考虑下界…… |
| 3 | 小尝试 | 0.4 | 先考虑下界：如果k很小（比如k<2016），擦除后两边剩余的因子总数是多少？这会带来什么问题？ | 如果k<2016，两边剩余因子总数>2016。但因子只涉及(x-1)到(x-2016)共2016种。由鸽巢原理，至少有一个(x-i)同时出现在两边，则x=i是方程的解。所以k≥2016。 |
| 4 | 思维操作引导 | 0.6 | 很好，下界k≥2016已得。现在需要构造k=2016的方案。请思考：如何将1到2016的因子分成两组，使得两组的乘积方程永远无实数解？考虑将因子配对，注意2016=4×504。 | 将因子按模4分组。{4k+1,4k+4}配一组放左边，{4k+2,4k+3}配一组放右边。每组504对，共擦除2016个因子。需要验证两边乘积永不相等。 |
| 5 | 思维操作引导 | 0.7 | 关键观察：计算(x-(4k+2))(x-(4k+3))和(x-(4k+1))(x-(4k+4))的差。这个差有什么特殊性质？ | (x-(4k+2))(x-(4k+3))=x²-(4k+5)x+(4k+2)(4k+3)，(x-(4k+1))(x-(4k+4))=x²-(4k+5)x+(4k+1)(4k+4)。差为(4k+2)(4k+3)-(4k+1)(4k+4)=2。所以每对右因子比左因子恰好大2。 |
| 6 | 推进 | 0.6 | 利用这个恒等式，证明∏(x-(4k+1))(x-(4k+4))≠∏(x-(4k+2))(x-(4k+3))对所有实数x成立。需要分情况讨论x相对于根的位置。 | 分情况：1)x等于某根→对应乘积为0而另一边非0；2)x落在(4m+1,4m+4)内→左乘积为负右乘积为正，或用重配对+恒等式比较；3)x在所有区间外→每对右>左故乘积右>左。 |
| 7 | 能量传递引导 | 0.8 | 总结：下界k≥2016由鸽巢原理给出，构造k=2016由模4分组配对实现，恒等式保证无实数解。答案是什么？ | k=2016。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.9
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
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
- structure_features: 两侧多项式因子的擦除优化问题，需要构造性证明（存在性）+ 下界证明（最优性），涉及模4分组配对和鸽巢原理
- key_objects: 多项式乘积, 因子擦除, 模4分组, 配对恒等式, 鸽巢原理

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["鸽巢原理下界", "模4分组配对", "代数恒等式构造", "符号分析分类讨论"]
- primary_pattern: 模4分组配对
- knowledge_required: ["多项式乘积的性质", "鸽巢原理", "二次多项式配对恒等式", "连续函数符号分析"]
- key_insight: 将因子按模4分成{4k+1,4k+4}和{4k+2,4k+3}两组，利用恒等式(x-(4k+2))(x-(4k+3))=(x-(4k+1))(x-(4k+4))+2保证两边乘积永不相等

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 枚举式搜索（尝试各种擦除方案逐一验证）
- translation_to: 结构化分组配对（模4分组+代数恒等式构造）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "method_translation"}
- tell_small_concepts: ["模4分组", "配对恒等式", "鸽巢原理", "因子擦除", "无实数解"]
- expected_ai_method: 枚举各种擦除方案，尝试小规模验证后推广，或仅用鸽巢原理得下界但无法构造
- correct_method: 模4分组配对+代数恒等式构造+鸽巢原理下界

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？可以，discrete_combinatorial + enumeration_brute_force + method_translation均已有
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？一致
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？足够
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化

**拓扑进化建议**（如有）：无

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
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 1 个，implicit型: 2 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI可能通过鸽巢原理得到下界k≥2016，但无法发现模4分组配对的构造方案，会卡在构造性证明部分，可能尝试随机分组或小规模枚举但无法找到使两边恒不等的配对
- suitable_for_poc: ["hint_injection_poc", "tell_identification_poc", "topology_matching_poc"]
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
2. 更新`problem_extraction_progress`集合中`_key="329238"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2016p5"
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
    '_key': '329238',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2016p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2016p5')
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
- problem_id: compfiles_imo2016p5
- solution_method_type: structural_construction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类（discrete_combinatorial + enumeration_brute_force + method_translation）足够覆盖
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
