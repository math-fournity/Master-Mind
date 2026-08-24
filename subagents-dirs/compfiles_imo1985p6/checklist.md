# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1985p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1985P6.lean
- **来源**: IMO 1985 P6
- **ArangoDB progress记录_key**: 329112（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1985P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：For every real number x_1, construct the sequence {x_1,x_2,...} by setting x_{n+1} = x_n * (x_n + 1/n) for each n >= 1. Prove that there exists exactly one value of x_1 for which 0 < x_n, x_n < x_{n+1}, and x_{n+1} < 1 for every n.
- 解答核心思路（1-2句话）：Define inverse threshold sequences b_n = f_n^{-1}(1-1/n) and c_n = f_n^{-1}(1), squeeze them to prove existence, and prove uniqueness by showing the difference f_n(b)-f_n(a) has contradictory limit behavior (→∞ and →0).
- 解答关键步骤列表：
  1. Show f_n(x) > 0 for x > 0 (aux_1)
  2. Show f_n is strictly monotone increasing (aux_2)
  3. Show f_n(x) > 1 for x ≥ 1, n > 1 (aux_3)
  4. Show f_n is continuous (aux_6)
  5. Show f_n is surjective onto [0,∞) (aux_7)
  6. Define b_n = f_n^{-1}(1-1/n), c_n = f_n^{-1}(1) via inverse functions
  7. Show b_n < 1 (aux_8), b_n < c_n
  8. Show b_n strictly increasing (aux_9), c_n strictly decreasing
  9. Show sup{b_n} ≤ inf{c_n} (aux_11)
  10. Existence from squeeze: any value in [sup, inf] works (aux_exists)
  11. Uniqueness by contradiction: f_n(b)-f_n(a) → ∞ (growth) and → 0 (bounded) (aux_unique)

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
| 1 | 纯元认知观察 | 0.8 | Describe the problem structure: recurrence, three conditions, what 'exactly one x_1' means | f_n recurrence, conditions 0<x_n, x_n<x_{n+1}, x_{n+1}<1, unique initial value |
| 2 | 自由列举 | 0.7 | List all possible approaches: direct computation, induction, functional, squeeze, contradiction | Direct (fails), induction (hard), functional (promising), squeeze (promising), contradiction for uniqueness |
| 3 | 小尝试 | 0.3 | Try computing x_2, x_3 in terms of x_1. What is the degree? | Degree doubles: x_2 degree 2, x_3 degree 4, no closed form, direct approach infeasible |
| 4 | 思维操作引导 | 0.5 | Reformulate conditions as bounds: x_n<x_{n+1} implies what? x_{n+1}<1 implies what? | x_n > 1-1/n (from growth), x_n < 1 (from upper bound), so 1-1/n < x_n < 1 |
| 5 | 思维操作引导 | 0.4 | Consider f_n(x_1) as function. Show monotone+continuous. Define b_n=f_n^{-1}(1-1/n), c_n=f_n^{-1}(1) | f_n strictly monotone increasing, continuous, surjective. b_n and c_n are threshold values of x_1 |
| 6 | 推进 | 0.3 | Show b_n increasing, c_n decreasing, b_n<c_n, sup≤inf. How does this give existence? | Squeeze: any x_1 in [sup,inf] satisfies b_n<x_1<c_n for all n → existence |
| 7 | 思维操作引导 | 0.4 | For uniqueness: assume a<b both work. Show d_n=f_n(b)-f_n(a) grows geometrically but is bounded. Contradiction? | d_n ≥ d_2·(3/2)^{n-2} → ∞ but d_n < 1. Contradiction → a=b → uniqueness |
| 8 | 能量传递引导 | 0.8 | Combine existence and uniqueness to state final result | ∃! x_1 satisfying all conditions. QED |

**统计**：
- total_rounds: 8
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 3
- level_sum: 4.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: 7
- thinking_bottleneck（思维瓶颈在哪轮，或null）: 5

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
- structure_features: recursive_sequence_with_quadratic_nonlinearity, existence_and_uniqueness_of_initial_value, three_simultaneous_inequality_constraints, monotone_function_composition_structure, squeeze_structure_via_inverse_thresholds
- key_objects: iterated_map f_n(x), threshold sequences b_n and c_n, supremum br and infimum cr, difference sequence f_n(b)-f_n(a)

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [functional_reframing, squeeze_principle, contradiction_with_contradictory_limits, monotonicity_exploitation, threshold_decomposition]
- primary_pattern: squeeze_principle
- knowledge_required: [strict monotonicity of iterated functions, continuity of polynomial compositions, surjectivity of continuous monotone functions, inverse functions of strictly monotone continuous functions, supremum and infimum properties, squeeze theorem / IVT, limit behavior: tendsto_atTop_atTop vs tendsto_atTop_nhds]
- key_insight: Define b_n = f_n^{-1}(1-1/n) and c_n = f_n^{-1}(1) as threshold sequences; they squeeze to a unique value, and uniqueness follows because f_n(b)-f_n(a) must tend to both infinity (from growth) and zero (from boundedness).

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: direct_sequence_computation
- translation_to: functional_analysis_with_inverse_thresholds
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: [inverse_threshold_sequence, squeeze_pair, supremum_infimum_gap, monotone_continuous_surjective, contradictory_limits, growth_condition_reformulation]
- expected_ai_method: Bare AI would try to compute the sequence explicitly, find a closed form for x_n in terms of x_1, or use direct algebraic manipulation to solve for x_1. The recurrence x_{n+1} = x_n(x_n + 1/n) is quadratic and has no closed form, so direct calculation fails.
- correct_method: Reframe f_n as a function of x_1, establish monotonicity/continuity/surjectivity, define inverse threshold sequences b_n and c_n, squeeze to prove existence, use contradictory limits for uniqueness.

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ → 是，structural_existence/direct_calculation/structural_transformation 都在已有值中
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ → 是，都是抽象/中等粒度
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ → 是，三个维度足够。per-pair拓扑中R7用了knowledge_gap区分唯一性证明的知识瓶颈
- [x] 如果发现拓扑分类需要进化，在此写出建议： → 无需进化

**拓扑进化建议**（如有）：无。已有拓扑分类完全够用。

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
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs详情**：见profile.json中tell_hint_pairs数组，每对含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts。R7为knowledge_bottleneck（gap_type=knowledge_gap）。

**全局pairs详情**：
1. path_feature型：squeeze结构（b_n↗, c_n↘, sup≤inf→存在性），why_not_visible_locally="需要同时看到两个阈值序列的构造和挤压关系，单步只能看到一个阈值或一个单调性"
2. implicit型（observation_point=Q7）：矛盾极限（d_n→∞且→0），why_not_visible_locally="需要同时结合增长条件（→发散）和有界条件（→收敛），单独一个条件不揭示矛盾"

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI will attempt to compute the sequence explicitly or find a closed form, fail due to the quadratic nonlinearity (degree doubles each step), and then lack the insight to reframe as a functional/squeeze problem. Even if it reformulates the conditions as bounds, it will struggle to define inverse threshold sequences and will almost certainly not discover the contradictory-limits uniqueness argument.
- suitable_for_poc: [hint_injection_experiment — test whether hint at Q4 and Q5 can guide AI to squeeze approach, tell_detection_experiment — test whether system can detect fork at Q3, level_discrimination_experiment — strongly discriminates bare AI (fail) vs hint-guided AI (potential pass)]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON

完整JSON已写入 `subagents-dirs/compfiles_imo1985p6/profile.json`。所有字段均已填写：
- _key=compfiles_imo1985p6, source_id, source_dataset, schema_version=3 ✓
- problem_text, solution_text, solution_summary ✓
- domain=analysis, subfield=sequences_and_dynamical_systems ✓
- answer_type=proof, answer="There exists exactly one value of x_1..." ✓
- problem_type=structural_existence, solution_method_type=squeeze_threshold_sequences ✓
- structure_features, key_objects ✓
- thinking_patterns, primary_pattern=squeeze_principle, knowledge_required, key_insight ✓
- translation_from/to/type ✓
- tell_topology (profile级), tell_small_concepts ✓
- expected_ai_method, correct_method ✓
- tell_hint_pairs (8对, 每对含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts) ✓
- global_tell_hint_pairs (2对, path_feature+implicit, 每对含why_not_visible_locally/tell_topology/tell_small_concepts) ✓
- bare_ai_expected=fail, bare_ai_error_prediction, suitable_for_poc, discriminates_levels=true ✓
- qa_sequence (8 rounds + stats) ✓
- analysis_metadata ✓

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
2. 更新`problem_extraction_progress`集合中`_key="329112"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1985p6"
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
    '_key': '329112',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1985p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1985p6')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证详情: compfiles_imo1985p6, 8 local pairs, 2 global pairs, answer非None, per-pair拓扑存在, why_not_visible_locally存在

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_imo1985p6
- solution_method_type: squeeze_threshold_sequences
- 局部(tell,hint)对数量: 8
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类完全够用
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
