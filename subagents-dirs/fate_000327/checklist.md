# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000327
- **文件路径**: subagents-dirs/fate_000327/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396437（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000327/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let A be a local Cohen–Macaulay (CM) ring that is a quotient of a regular local ring. If A is a UFD, then A is Gorenstein. 形式化：A有IsCohenMacaulayLocalRing, IsDomain, UniqueFactorizationMonoid实例，B有IsRegularLocalRing实例，f:B→A满射，结论IsGorensteinRing A。
- 解答核心思路（1-2句话）：A是正则局部环B的商→A有canonical module ω_A=Ext^d_B(A,B)；A是CM→ω_A是MCM且rank 1 reflexive；A是UFD→class group平凡→ω_A自由→ω_A≅A→A是Gorenstein。
- 解答关键步骤列表：
  1. B正则局部→B是Gorenstein→A=B/I有canonical module ω_A=Ext^d_B(A,B)（d=dim B - dim A）
  2. A是CM→ω_A是maximal Cohen-Macaulay module（MCM）
  3. ω_A是rank 1 reflexive module（canonical module的一般性质）
  4. A是UFD→divisor class group Cl(A)=0→每个rank 1 reflexive module是free→ω_A≅A
  5. ω_A≅A→A是Gorenstein（canonical module同构于环本身是Gorenstein的刻画）

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
| 1 | 纯元认知观察 | 0.7 | 观察这道题的结构：已知条件有哪些？结论是什么？这些条件之间有什么联系？ | A是局部CM环，是正则局部环B的商（满射f:B→A），A是UFD。结论：A是Gorenstein。三个条件（CM、正则环商、UFD）分别属于不同的环论性质范畴，需要找到连接它们到Gorenstein的桥梁。 |
| 2 | 自由列举 | 0.6 | 列出所有可能证明A是Gorenstein的方向。 | (1)直接用Gorenstein定义验证inj.dim有限 (2)canonical module方法 (3)对偶化复形方法 (4)complete intersection性质 (5)type（类型）的概念 (6)Ext消解方法 |
| 3 | 小尝试 | 0.4 | 尝试直接用Gorenstein的定义（inj.dim_R R < ∞）来证明，看看UFD条件如何使用。 | 直接验证内射维数有限很困难：需要构造具体的内射分解或使用Ext消没性质，但UFD条件（唯一分解性）难以直接与内射维数联系起来。这条路走不通。 |
| 4 | 思维操作引导 | 0.5 | 考虑canonical module方法：A是正则局部环的商，这给了我们什么结构？ | B正则局部→B是Gorenstein→A=B/I有canonical module ω_A=Ext^d_B(A,B)，其中d=dim B - dim A。这是canonical module存在的充分条件——正则局部环的商天然具有canonical module。 |
| 5 | 思维操作引导 | 0.6 | 现在A是CM环，ω_A有什么性质？UFD条件如何使用？ | A是CM→ω_A是maximal CM module（MCM）。ω_A是rank 1 reflexive module。A是UFD→divisor class group Cl(A)=0→每个rank 1 reflexive module都是free→ω_A≅A。而ω_A≅A意味着A是Gorenstein。 |
| 6 | 推进 | 0.5 | 将上述推理链条完整组织：从B正则局部→canonical module存在→CM→MCM→UFD→free→Gorenstein。 | 完整证明链：(1)B正则局部→B Gorenstein (2)A=B/I→ω_A=Ext^d_B(A,B)存在 (3)A CM→ω_A MCM (4)ω_A rank 1 reflexive (5)A UFD→Cl(A)=0→ω_A free→ω_A≅A (6)ω_A≅A→A Gorenstein。 |
| 7 | 能量传递引导 | 0.3 | 总结这个证明的核心洞察：UFD条件通过canonical module的free性桥接到Gorenstein性质。这个思路可以推广到哪些类似问题？ | 核心洞察是"UFD→class group平凡→canonical module free→Gorenstein"。推广：任何通过class group或divisor class group控制canonical module性质的环论问题，如Q-Gorenstein环、F-正则环等。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.6
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R3"

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
- structure_features: 多个环论性质的蕴含关系链：CM + 正则局部环的商 + UFD → Gorenstein。需要通过canonical module作为中间桥梁对象连接UFD和Gorenstein两个远距离性质。
- key_objects: 局部CM环A, 正则局部环B, 满射环同态f:B→A, canonical module ω_A, divisor class group Cl(A), rank 1 reflexive module

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["结构桥接", "canonical module方法", "性质传递链", "反例排除（直接定义法不可行）", "中间对象引入"]
- primary_pattern: 结构桥接 — 通过canonical module将UFD性质桥接到Gorenstein性质
- knowledge_required: ["Cohen-Macaulay环", "正则局部环", "Gorenstein环", "canonical module（典型模）", "UFD与divisor class group", "reflexive module", "Ext函子", "maximal Cohen-Macaulay module"]
- key_insight: UFD意味着divisor class group平凡，使canonical module（rank 1 reflexive）成为自由模，而canonical module同构于环本身等价于Gorenstein

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 内射维数/Ext消没的直接定义验证方法
- translation_to: canonical module + divisor class group的代数结构性方法
- translation_type: method_translation — 从直接验证定义翻译到通过canonical module的结构性论证

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "direct_calculation", gap_type: "method_translation"}
- tell_small_concepts: ["canonical module", "divisor class group", "rank 1 reflexive", "maximal Cohen-Macaulay", "Gorenstein", "Ext函子", "UFD"]
- expected_ai_method: direct_calculation — bare AI可能尝试直接用Gorenstein定义验证inj.dim有限，但无法将UFD条件与内射维数联系起来
- correct_method: 通过canonical module的结构性论证：正则环商→canonical module存在→CM→MCM→UFD→class group平凡→free→≅A→Gorenstein

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是。structural_existence + direct_calculation + method_translation 完全适用。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是。三个维度都使用了已有值，粒度一致。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。这道题的核心特征（方法翻译：从直接定义法到canonical module法）已被method_translation捕获。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。

**拓扑进化建议**（如有）：无。已有拓扑分类体系完全适用。

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
- bare_ai_error_prediction: bare AI会尝试直接用Gorenstein定义验证内射维数有限，但无法将UFD条件（唯一分解性）与内射维数联系起来，陷入循环论证或停滞。不会想到引入canonical module作为中间桥梁对象。
- suitable_for_poc: ["POC-VMS-9 (tell端形式化过滤)", "POC-VMS-10 (小概念标记分辨)", "知识瓶颈POC——canonical module方法的知识门槛"]
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
2. 更新`problem_extraction_progress`集合中`_key="396437"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000327"
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
    '_key': '396437',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000327',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000327')
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
