# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000275
- **文件路径**: subagents-dirs/fate_000275/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396385（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000275/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let K/ℚ be a finite extension. Let H be a closed subgroup of the absolute Galois group G(K) of K. If H is finite, then the cardinality of H is either one or two.
- 解答核心思路（1-2句话）：利用Galois对应将H转化为某个域L=K̄^H的绝对Galois群G(L)=H（因H闭），然后应用Artin-Schreier定理：绝对Galois群有限的域要么代数闭（|G|=1）要么实闭（|G|=2）。
- 解答关键步骤列表：
  1. 设 L = K̄^H（H在可分闭包中的不动点域）
  2. 因H是G(K)的闭子群，由无限Galois对应的基本定理，G(L) ≅ H
  3. H有限 ⟹ G(L)有限
  4. 应用Artin-Schreier定理：绝对Galois群有限的域要么代数闭（平凡群，|G|=1），要么实闭（ℤ/2ℤ，|G|=2）
  5. 因此 |H| = |G(L)| = 1 或 2

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
| 1 | 纯元认知观察 | 0.7 | 请描述这道题的结构：已知条件有哪些？要证明什么结论？核心数学对象是什么？ | 已知：K/ℚ有限扩张，H是G(K)的闭子群且H有限。结论：|H|=1或2。核心对象：绝对Galois群、闭子群、profinite拓扑、有限群。关键在于"闭子群"和"有限"两个条件的交互。 |
| 2 | 自由列举 | 0.6 | 列出所有可能用来证明"绝对Galois群的有限闭子群阶≤2"的方向和方法。 | 方向包括：(1)直接群论分析有限子群结构；(2)利用Galois对应考虑不动点域；(3)Artin-Schreier定理；(4)Kummer理论；(5)profinite群的 torsion 元素分析；(6)实闭域理论；(7)代数数论中的局部-全局原理。 |
| 3 | 小尝试 | 0.4 | 尝试直接用群论方法分析G(K)的有限子群——能否不借助域论就给出阶的上界？ | 直接群论方法困难。G(K)是profinite群，其有限子群在拓扑意义上可能很复杂。纯群论无法利用K/ℚ有限这个条件——需要将群论信息翻译回域论。关键障碍：群论方法缺少与域结构的联系。 |
| 4 | 思维操作引导 | 0.3 | 执行以下思维操作：考虑H的不动点域L=K̄^H。利用H是闭子群这一条件，通过无限Galois对应的基本定理，G(L)与H之间有什么关系？ | 因H是G(K)的闭子群，由无限Galois对应的基本定理（闭子群↔中间域），L=K̄^H满足G(L)≅H。因此G(L)是有限群。问题转化为：什么样的域有有限的绝对Galois群？ |
| 5 | 推进 | 0.5 | 继续推进：现在问题变为"绝对Galois群有限的域有什么结构？"请深入分析这个等价问题。 | 这是Artin-Schreier定理的经典设置。Artin-Schreier定理说：如果一个域的绝对Galois群有限，则该域要么代数闭（G平凡），要么实闭（G≅ℤ/2ℤ）。需要回忆或推导这个定理。 |
| 6 | 思维操作引导 | 0.2 | 应用Artin-Schreier定理：域L的绝对Galois群G(L)≅H有限。根据定理，L要么代数闭（|G(L)|=1），要么实闭（|G(L)|=2）。请写出最终结论。 | 由Artin-Schreier定理：G(L)有限⟹L代数闭或L实闭。若L代数闭，G(L)={1}，|H|=1。若L实闭，G(L)≅ℤ/2ℤ，|H|=2。因此|H|=1或|H|=2。QED。 |
| 7 | 能量传递引导 | 0.3 | 回顾整个证明路径：从Galois对应到Artin-Schreier定理，每一步都自然衔接。请总结这个证明的核心思路，确认逻辑链完整。 | 核心思路：闭子群H→不动点域L→G(L)≅H（Galois对应）→G(L)有限→Artin-Schreier定理→|G(L)|∈{1,2}→|H|∈{1,2}。逻辑链完整，关键转折在于将群论问题翻译为域论问题，再应用Artin-Schreier定理。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.7+0.6+0.4+0.3+0.5+0.2+0.3 = 3.0
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

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
- problem_type: characterization
- structure_features: 给定一个代数对象（绝对Galois群的闭子群）满足特定条件（有限），证明其基数只能取两个特定值（1或2）。这是对一类对象可能结构的刻划（characterization），而非存在性或不等式。
- key_objects: ["绝对Galois群 G(K)", "闭子群 H", "有限群", "profinite拓扑", "不动点域 L=K̄^H", "Artin-Schreier定理", "实闭域", "代数闭域"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["结构翻译（群论→域论）", "Galois对应（闭子群↔不动点域）", "定理调用（Artin-Schreier）", "分类讨论（代数闭vs实闭）", "反例排除（纯群论方法不可行）"]
- primary_pattern: 结构翻译——将群论问题通过Galois对应翻译为域论问题，再应用经典定理
- knowledge_required: ["绝对Galois群的定义与profinite拓扑", "无限Galois对应的基本定理（闭子群↔中间域）", "Artin-Schreier定理（绝对Galois群有限的域的分类）", "实闭域与代数闭域的基本性质"]
- key_insight: 将"绝对Galois群的有限闭子群"通过不动点域翻译为"绝对Galois群有限的域"，从而可以应用Artin-Schreier定理完成分类

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 群论语言（绝对Galois群的有限闭子群的阶的上界）
- translation_to: 域论语言（绝对Galois群有限的域的分类，即Artin-Schreier定理）
- translation_type: 结构翻译——通过Galois对应将群论对象（闭子群）翻译为域论对象（不动点域的绝对Galois群），使问题从"群的有限子群结构"变为"域的绝对Galois群分类"

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "logical_deduction", gap_type: "knowledge_gap"}
- tell_small_concepts: ["绝对Galois群", "闭子群", "不动点域", "Galois对应", "Artin-Schreier定理", "实闭域", "代数闭域", "profinite拓扑"]
- expected_ai_method: bare AI可能尝试直接用群论方法分析有限子群结构，试图通过群的阶的整除性或Sylow定理给出上界，而不考虑将问题翻译到域论
- correct_method: 通过Galois对应将闭子群翻译为不动点域的绝对Galois群，再应用Artin-Schreier定理完成分类

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ → 可以。characterization已有，logical_deduction已有，knowledge_gap已有。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ → 一致。都是抽象级别的分类。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ → 足够。这道题的核心gap是知识缺口（不知道Artin-Schreier定理），用knowledge_gap可以准确表达。
- [x] 如果发现拓扑分类需要进化，在此写出建议： → 无需进化。现有拓扑分类足够。

**拓扑进化建议**（如有）：无。现有拓扑分类体系完全够用。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对题目，尚未开始分析，处于结构识别阶段，尚未识别出群论-域论翻译的可能性 | 描述题目结构，识别已知/未知和核心数学对象 | 0.7 | 纯元认知观察 | false | {characterization, logical_deduction, method_problem_mismatch} | ["绝对Galois群", "闭子群", "有限群"] |
| 2 | AI已识别题目结构，开始列举方向，但可能遗漏关键的"Galois对应+Artin-Schreier"路径 | 列出所有可能方向，包括群论和域论两类方法 | 0.6 | 自由列举 | false | {characterization, logical_deduction, method_problem_mismatch} | ["Galois对应", "Artin-Schreier定理", "Kummer理论", "profinite群"] |
| 3 | AI尝试纯群论方法分析有限子群，走错方向——缺少与域结构的联系 | 尝试直接群论方法，发现不可行，需要域论 | 0.4 | 小尝试 | false | {characterization, logical_deduction, method_problem_mismatch} | ["有限子群", "Sylow定理", "profinite群", "群论方法"] |
| 4 | AI从群论方法转向域论，需要知道无限Galois对应的基本定理——这是思维转折点 | 考虑H的不动点域L=K̄^H，利用闭子群条件通过Galois对应得到G(L)≅H | 0.3 | 思维操作引导 | false | {characterization, logical_deduction, method_translation} | ["不动点域", "Galois对应", "闭子群", "中间域"] |
| 5 | AI已将问题翻译为"绝对Galois群有限的域"，需要识别这是Artin-Schreier定理的设置 | 推进到"绝对Galois群有限的域有什么结构"——引出Artin-Schreier定理 | 0.5 | 推进 | true | {characterization, logical_deduction, knowledge_gap} | ["Artin-Schreier定理", "绝对Galois群有限", "代数闭域", "实闭域"] |
| 6 | AI需要知道并应用Artin-Schreier定理——纯知识瓶颈，定理内容是分类的核心 | 应用Artin-Schreier定理：L代数闭则|G(L)|=1，L实闭则|G(L)|=2 | 0.2 | 思维操作引导 | true | {characterization, logical_deduction, knowledge_gap} | ["Artin-Schreier定理", "代数闭域", "实闭域", "ℤ/2ℤ"] |
| 7 | AI已完成证明，需要总结确认逻辑链完整 | 回顾证明路径，确认从Galois对应到Artin-Schreier的逻辑链完整 | 0.3 | 能量传递引导 | false | {characterization, logical_deduction, knowledge_gap} | ["Galois对应", "Artin-Schreier定理", "逻辑链"] |

**全局tell_hint_pairs详情**：

**Global pair 1 (path_feature)**:
- scope_type: "path_feature"
- scope: 整个证明路径从群论到域论的翻译链条
- observation_point: null
- tell: 证明的核心路径是"群论→域论"的结构翻译——通过Galois对应将闭子群问题转化为域的绝对Galois群分类问题，再应用Artin-Schreier定理
- hint: 当面对绝对Galois群的子群问题时，考虑通过不动点域和Galois对应将问题翻译到域论，再寻找域论中的分类定理
- hint_level: 0.4
- generalizability: "high——这种'通过Galois对应在群论和域论之间翻译'的策略适用于所有涉及绝对Galois群子群结构的问题"
- why_not_visible_locally: "在局部视角中，每一轮只看到当前步骤（列举方向、尝试群论、考虑不动点域等），无法看到完整的'群论→域论→Artin-Schreier'翻译链条。只有从全局视角才能识别出这个翻译路径是一个连贯的策略，而非零散的步骤。"
- tell_topology: {problem_type: "characterization", ai_method_type: "logical_deduction", gap_type: "method_translation"}
- tell_small_concepts: ["Galois对应", "不动点域", "结构翻译", "群论到域论"]

**Global pair 2 (implicit)**:
- scope_type: "implicit"
- scope: Artin-Schreier定理作为隐藏的分类工具
- observation_point: "Q5"
- tell: Artin-Schreier定理隐含在问题结构中——"绝对Galois群有限的域"这个条件直接触发该定理，但题目表面只提到"闭子群有限"，定理的适用性需要通过翻译才能显现
- hint: 当遇到"绝对Galois群有限"的条件时，立即联想到Artin-Schreier定理：这样的域只能是代数闭（|G|=1）或实闭（|G|=2）
- hint_level: 0.3
- generalizability: "high——Artin-Schreier定理是代数数论中的基本分类定理，适用于所有涉及绝对Galois群有限性的问题"
- why_not_visible_locally: "在局部步骤中，AI看到的是'G(L)有限'这个中间结论，但这个结论与Artin-Schreier定理的联系不是局部可见的——需要知道这个定理的存在才能建立联系。定理本身是蕴含在问题结构中的分类工具，不在题目文字中显式出现。"
- tell_topology: {problem_type: "characterization", ai_method_type: "logical_deduction", gap_type: "knowledge_gap"}
- tell_small_concepts: ["Artin-Schreier定理", "绝对Galois群有限", "代数闭域", "实闭域"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI很可能不知道Artin-Schreier定理，或者即使知道也难以主动将"闭子群有限"翻译为"不动点域的绝对Galois群有限"。AI可能会尝试纯群论方法（Sylow定理、群的阶分析）或试图用Kummer理论，但都无法到达正确结论。核心障碍是知识缺口（Artin-Schreier定理）和思维翻译（群论→域论）。
- suitable_for_poc: ["POC-VMS-8（脉络继承+方向注入）——测试注入Galois对应+Artin-Schreier方向后AI能否完成证明", "POC-VMS-9/10（tell端验证）——测试从AI thinking中识别'走纯群论方向'的tell并注入域论翻译方向"]
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

## Step 10: 入库ArangoDB [ ]

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="396385"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000275"
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
    '_key': '396385',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000275',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000275')
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
- problem_id: fate_000275
- solution_method_type: structural_translation
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有拓扑分类体系（characterization / logical_deduction / knowledge_gap / method_translation / method_problem_mismatch）完全够用。
- 是否遇到异常: JSON文件初次写入时因字符串内含ASCII双引号导致解析失败，已用Python json.dumps重新生成修复。

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
