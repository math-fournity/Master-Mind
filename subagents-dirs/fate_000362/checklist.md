# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000362
- **文件路径**: subagents-dirs/fate_000362/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396472（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000362/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：If I is a homogeneous ideal of k[x₀,...,xₙ], R = k[x₀,...,xₙ]/I, then R is Cohen-Macaulay if and only if R_P is Cohen-Macaulay, where P = (x₀,...,xₙ) is the irrelevant ideal.
- 解答核心思路（1-2句话）：正向方向由定义平凡（CM at all primes蕴含CM at P）；反向方向利用标准分次k-代数的分次结构——在无关理想处的CM性质通过齐次参数系传播到所有素理想。
- 解答关键步骤列表：
  1. 正向：IsCohenMacaulayRing定义要求所有素理想处CM，故R_P是CM（平凡特化）
  2. 反向：R是标准分次k-代数，P是极大齐次理想
  3. 每个素理想包含一个齐次素理想
  4. 齐次素理想q⊆P：R_P的齐次参数系也是R_q的参数系
  5. depth-dim等式在P处成立⇒在q处也成立（正则序列传播）
  6. 非齐次素理想：通过包含的齐次素理想，CM性质下降
  7. R在所有素理想处CM⇒R是CM环

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
| 1 | 纯元认知观察 | 0.3 | 描述这个问题的结构：iff的两个方向分别假设什么、结论什么？ | 这是双向蕴含：(→)R是CM蕴含R_P是CM；(←)R_P是CM蕴含R是CM。R是多项式环商齐次理想，P=(x₀,...,xₙ)是无关理想。 |
| 2 | 自由列举 | 0.5 | 列出证明这个iff的所有可能方法。考虑R作为多项式环商齐次理想有什么特殊性质。 | 可能方法：(1)逐个素理想验证，(2)用CM定义(depth=dim)，(3)利用分次环性质，(4)用局部化理论，(5)用齐次参数系。关键特殊性质：R是标准分次k-代数。 |
| 3 | 小尝试 | 0.2 | 试正向方向：如果R是CM（所有素理想处），R_P是否CM？IsCohenMacaulayRing的定义是什么？ | 是的，平凡成立。IsCohenMacaulayRing要求所有素理想处CM，R_P是其中一个特例。正向方向由定义直接得到。 |
| 4 | 思维操作引导 | 0.7 | 反向方向：P=(x₀,...,xₙ)作为分次环的无关理想有什么特殊性？分次结构如何将素理想与P联系起来？ | P是极大齐次理想。每个素理想包含一个齐次素理想。对于齐次素理想q⊆P，R_q的局部化可与R_P关联。分次结构使齐次元素在决定depth和dim时起特殊作用。 |
| 5 | 推进 | 0.6 | 继续：利用R是标准分次k-代数的事实。每个素理想包含齐次素理想，齐次素理想处的depth/dim可通过齐次参数系与P处的关联。 | 标准分次k-代数存在齐次参数系(hsop)。R_P的hsop在q⊆P时也是R_q的hsop。由于depth和dim可用hsop计算，P处的depth-dim等式蕴含q处相同等式。 |
| 6 | 思维操作引导 | 0.8 | 思考R_P的齐次参数系如何同时作为R_q的参数系（q是含于P的齐次素理想）。P处的depth-dim等式如何强制q处相同等式成立。 | 若R_P是CM，则depth(R_P)=dim(R_P)。hsop x₁,...,x_d是R_P中的正则序列。因q⊆P，这些元素也在q中，且由分次结构它们在R_q中也是正则序列。故depth(R_q)=d=dim(R_q)，R_q是CM。非齐次素理想通过包含的齐次素理想下降。 |
| 7 | 能量传递引导 | 0.4 | 现在整合：正向由定义，反向由分次结构传播。证明完成。 | 完整证明：(→)由IsCohenMacaulayRing定义，R在所有素理想处CM，故R_P是CM。(←)若R_P是CM，对任意齐次素理想q⊆P，R_P的hsop是R_q的正则序列，给出depth=dim。非齐次素理想通过包含齐次素理想下降。故R在所有素理想处CM。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.5
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
- problem_type: characterization
- structure_features: 双向蕴含(iff)——全局环性质(CM at all primes)与局部性质(CM at one specific prime: irrelevant ideal)之间的等价。关键结构特征是分次环结构使得local-to-global reduction成为可能。
- key_objects: ["齐次理想I", "多项式环k[x₀,...,xₙ]", "商环R=k[x₀,...,xₙ]/I", "无关理想P=(x₀,...,xₙ)", "局部化R_P", "Cohen-Macaulay性质", "depth", "Krull维数", "分次环结构", "齐次参数系"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["bidirectional_analysis", "local_global_reduction", "graded_structure_exploitation", "definition_unpacking"]
- primary_pattern: local_global_reduction
- knowledge_required: ["Cohen-Macaulay环与局部环", "分次环理论", "素理想处的局部化", "depth与Krull维数", "齐次理想与齐次参数系", "Ext群与depth", "标准分次k-代数"]
- key_insight: 对于标准分次k-代数，CM性质可在单个无关极大理想处检验，因为分次结构通过齐次参数系将depth-dim等式从无关理想传播到所有素理想。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 局部环理论（单个素理想处的CM）
- translation_to: 分次环理论（通过无关理想的标准分次k-代数的CM）
- translation_type: local_to_global

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "logical_deduction", gap_type: "knowledge_gap"}
- tell_small_concepts: ["irrelevant ideal", "graded ring", "homogeneous system of parameters", "depth-dimension equality", "localization at prime", "standard graded algebra"]
- expected_ai_method: Bare AI会尝试直接逻辑演绎：正向方向平凡处理，反向方向试图逐个素理想验证CM，不识别分次结构的关键作用。
- correct_method: 利用R作为标准分次k-代数的分次结构：正向由定义，反向利用分次环理论中CM在无关理想处蕴含CM在所有素理想处的定理，通过齐次参数系传播。

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？是。characterization + logical_deduction + knowledge_gap 均为已有值，粒度一致。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？是。characterization与已有structural_existence/characterization同粒度，logical_deduction与已有值同粒度，knowledge_gap与已有值同粒度。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？是。三个维度足够。这道题的local-to-global reduction特征通过gap_type=knowledge_gap和tell_small_concepts中的"graded ring"/"irrelevant ideal"可区分。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。已有拓扑分类足够覆盖此题。

**拓扑进化建议**（如有）：无。已有拓扑分类体系可充分覆盖此题。

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
- bare_ai_error_prediction: Bare AI能正确处理正向方向（由IsCohenMacaulayRing定义平凡），但在反向方向会失败。会试图直接在任意素理想处验证CM，不使用分次结构，或尝试一般局部化性质而不识别无关理想在分次环中的特殊角色。
- suitable_for_poc: ["local_global_reduction", "knowledge_gap_identification", "graded_structure_exploitation", "definition_unpacking"]
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
2. 更新`problem_extraction_progress`集合中`_key="396472"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000362"
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
    '_key': '396472',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000362',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000362')
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
