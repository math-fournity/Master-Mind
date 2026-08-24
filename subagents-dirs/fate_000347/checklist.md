# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000347
- **文件路径**: subagents-dirs/fate_000347/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396457（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000347/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：K是数域，A是有限型K-代数且为整环，f:A→A是K-代数自同态且非有限阶（∀n>0, f^n≠id）。证明：存在极大理想m⊂A使得∀n∈ℕ₊, f^{-n}(m)≠m。
- 解答核心思路（1-2句话）：对每个n>0，利用f^n≠id和A是整环得出不动点理想J_n=(f^n(a)-a: a∈A)非零，故V(J_n)是真闭子集；再利用数域上有限型代数的闭点计数性质，证明可数个真闭子集的并不能覆盖所有极大理想。
- 解答关键步骤列表：
  1. 对每个n>0，定义不动点理想J_n=(f^n(a)-a : a∈A)
  2. 利用f^n≠id和A是整环证明J_n≠0（存在a使f^n(a)≠a，该元素非零，整环中含非零元素的理想非零）
  3. V(J_n)是Spec(A)的真闭子集，即非所有极大理想被f^n固定
  4. 排除0维平凡情形（A是域时必为K的有限扩张，K-自同构群有限，f必有限阶，与假设矛盾）
  5. 利用数域上闭点增长率：dim(A/J_n)<dim(A)导致V(J_n)中闭点数渐近少于MaxSpec(A)
  6. 可数个低维子集的并不能覆盖所有闭点（计数/对角论证）
  7. 结论：存在m∉∪V(J_n)，即f^{-n}(m)≠m对所有n>0

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
| 1 | 纯元认知观察 | 0.8 | 描述题目结构：K、A、f的条件是什么？结论要求什么？f与极大理想的关系是什么？ | K是数域，A是有限型K-代数且为整环，f:A→A是K-代数自同态且非有限阶。需证存在极大理想m使f^{-n}(m)≠m对所有n>0。f^{-n}(m)是m在f^n下的原像（收缩理想），f^{-n}(m)=m意味着m是f^n作用在Spec(A)上的不动点。 |
| 2 | 自由列举 | 0.7 | 列出所有可能的方法来证明这样的极大理想存在。 | (a)直接构造特定极大理想 (b)反证法：假设所有极大理想都被某个f^n固定，导出矛盾 (c)计数/密度论证：证明"坏"极大理想集合是全体的小子集 (d)利用Zariski拓扑：不动点集是闭集 (e)利用数域算术性质：A在数域上的闭点计数约束 |
| 3 | 小尝试 | 0.5 | 尝试直接构造方法：能否显式描述一个具有所需性质的极大理想？ | 此方法失败，因为A和f完全抽象——没有代数或自同态的显式描述，无法写出具体的元素或理想。需要非构造性或结构性论证。 |
| 4 | 思维操作引导 | 0.4 | 考虑反证/密度方法。对每个n>0，定义J_n=(f^n(a)-a : a∈A)。包含J_n的极大理想与被f^n固定的极大理想有什么关系？ | 极大理想m满足f^{-n}(m)=m当且仅当对所有a∈A有f^n(a)-a∈m，即J_n⊆m。所以被f^n固定的极大理想集恰为V(J_n)∩MaxSpec(A)。问题归结为证明∪_{n≥1}V(J_n)≠MaxSpec(A)。 |
| 5 | 思维操作引导 | 0.3 | 关键步骤：证明对每个n>0，J_n是非零理想。为什么f^n≠id加上A是整环能推出J_n≠0？ | 因f^n≠id，存在a∈A使f^n(a)≠a，故f^n(a)-a≠0。J_n包含此非零元素。因A是整环，含非零元素的理想必非零。故J_n≠0，V(J_n)是Spec(A)的真闭子集——非所有极大理想被f^n固定。 |
| 6 | 推进 | 0.4 | 现在证明可数并∪_{n≥1}V(J_n)不能覆盖A的所有极大理想。数域的什么性质使这成立？ | A是数域上有限型代数且为整环，0维情形平凡（A是域时为K有限扩张，K-自同构群有限，f必有限阶，矛盾）。故dim(A)≥1。每个J_n≠0导致dim(A/J_n)<dim(A)，V(J_n)中闭点增长率严格低于MaxSpec(A)。由计数/对角论证，可数个低维子集不能覆盖所有闭点。 |
| 7 | 能量传递引导 | 0.6 | 将所有步骤组合完成证明。 | 由步骤5，每个V(J_n)是真闭子集。由步骤6，∪V(J_n)≠MaxSpec(A)。故存在m∉任何V(J_n)，即J_n⊄m对所有n，即f^{-n}(m)≠m对所有n>0。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.7
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R5
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R6

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
- structure_features: existence_of_object_with_dynamical_property, countable_union_of_proper_closed_subsets, number_field_arithmetic_constraint, domain_property_connects_nonperiodicity_to_nonzero_ideals
- key_objects: number_field_K, finite_type_K_algebra_A, K_algebra_endomorphism_f, maximal_ideal_m, fixed_point_ideal_J_n, proper_closed_subset_V(J_n)

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [contradiction_via_density, structural_transformation, arithmetic_counting, vacuous_case_elimination]
- primary_pattern: contradiction_via_density
- knowledge_required: [finite_type_algebra_over_number_field, Jacobson_rings, Zariski_topology_of_Spec, closed_points_of_varieties_over_number_fields, growth_rate_of_closed_points_in_subvarieties, domain_property_and_nonzero_ideals, K_algebra_endomorphisms]
- key_insight: f^n≠id加上A是整环推出不动点理想J_n非零，使每个不动点集成为真闭子集；数域结构保证可数个真闭子集不能覆盖所有极大理想。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: dynamical_systems_language（动力学语言：轨道、周期性、不动点）
- translation_to: algebraic_geometry_over_number_fields（数域上代数几何语言：真闭子集、闭点计数、Zariski拓扑）
- translation_type: structural_transformation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: logical_deduction, gap_type: knowledge_gap}
- tell_small_concepts: [fixed_point_ideal, proper_closed_subset, countable_union_coverage, number_field_closed_points, domain_nonzero_ideal]
- expected_ai_method: 纯逻辑演绎，试图直接构造或论证极大理想存在性，不使用数域算术性质
- correct_method: 将存在性问题转化为证明可数个真闭子集（不动点集）不能覆盖所有极大理想，利用数域闭点计数

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ 是，structural_existence/logical_deduction/knowledge_gap均可归入已有类别
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ 是，与已有值粒度一致
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ 足够，无需新维度
- [x] 如果发现拓扑分类需要进化，在此写出建议： 无需进化

**拓扑进化建议**（如有）： 无

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
- bare_ai_error_prediction: bare AI会尝试纯逻辑演绎，可能正确识别每个不动点集是真闭子集，但在从代数到算术的过渡处卡住——不知道数域上可数个真闭子集不能覆盖所有闭点。也可能遗漏整环假设在保证J_n≠0中的关键作用。
- suitable_for_poc: [POC-VMS-8: hint注入——关于转化为密度论证的关键提示可注入, POC-VMS-9/10: tell识别——R5处缺失domain-nonzero-ideal连接是清晰的知识瓶颈tell]
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
2. 更新`problem_extraction_progress`集合中`_key="396457"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000347"
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
    '_key': '396457',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000347',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000347')
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
- problem_id: fate_000347
- solution_method_type: structural_existence
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，已有拓扑分类够用
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
