# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000263
- **文件路径**: subagents-dirs/fate_000263/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396373（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000263/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Show that if R is a unique factorization domain such that the quotient field of R is isomorphic to ℝ, then R is isomorphic to ℝ.
- 解答核心思路（1-2句话）：反证法——假设R不是域，则R有素元p；利用ℝ中正实数有平方根的性质，在Frac(R)中取√p=a/b（gcd(a,b)=1），平方得a²=pb²，由p素性推出p|a且p|b，矛盾。故R无素元，R是域，R≅ℝ。
- 解答关键步骤列表：
  1. 假设R不是域 → R有非零非单位元 → UFD中必有素元p
  2. 在同构Frac(R)≅ℝ下，p或-p映射为正实数 → √p（或√(-p)）在Frac(R)中存在
  3. 写√p=a/b，gcd(a,b)=1 → a²=pb² → p|a² → p|a（素性）→ p|b² → p|b
  4. p|a且p|b与gcd(a,b)=1矛盾 → R无素元 → R是域 → R=Frac(R)≅ℝ

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
| 1 | 纯元认知观察 | 0.8 | 描述题目结构：已知条件（R是UFD，Frac(R)≅ℝ）和需要证明的结论（R≅ℝ）是什么？R和其分式域之间有什么关系？ | R是UFD，分式域同构于ℝ。需证R本身同构于ℝ。Frac(R)是包含R的最小域，所以R⊆Frac(R)≅ℝ。问题是R能否是分式域的真子环。 |
| 2 | 自由列举 | 0.7 | 列出UFD和ℝ的所有可能相关性质。ℝ相比其他域有什么特殊之处？ | UFD性质：非零非单位元可分解为素元乘积、UFD整闭、gcd存在。ℝ性质：正实数有平方根、ℝ是实闭域、不可数、有序域、代数闭包是ℂ。平方根性质和实闭性是ℝ的显著特征。 |
| 3 | 小尝试 | 0.5 | 尝试利用UFD在其分式域中整闭的性质。这能推出R=Frac(R)吗？ | R在Frac(R)≅ℝ中整闭。即若x∈Frac(R)在R上整（满足R系数的首一多项式），则x∈R。但这不能直接推出R=Frac(R)，因为Frac(R)\R中的元素未必在R上整（如1/p对素元p不整）。此路不通。 |
| 4 | 思维操作引导 | 0.4 | 不用整闭性，改用反证法：假设R不是域。R此时有什么域没有的结构？ | 若R不是域，则R有非零非单位元。UFD中每个非零非单位元有素因子，故存在素元p∈R。目标是利用Frac(R)≅ℝ导出矛盾。 |
| 5 | 思维操作引导 | 0.3 | 利用ℝ的特殊性质：每个正实数有平方根。在同构Frac(R)≅ℝ下，p或-p映射为正实数。这对Frac(R)中的√p意味着什么？能导出矛盾吗？ | 在φ:Frac(R)→ℝ下，φ(p)>0或<0。若φ(p)>0则√φ(p)存在，故有x∈Frac(R)使x²=p。写x=a/b，gcd(a,b)=1。则a²=pb²。p素且p|a²→p|a。写a=pc则pc²=b²→p|b²→p|b。但p|a且p|b与gcd(a,b)=1矛盾。 |
| 6 | 推进 | 0.5 | 从矛盾中能得出什么结论？如果R没有素元，R是什么？这如何推出R≅ℝ？ | 矛盾说明R无素元。UFD中非零非单位元必有素因子，故无素元意味着无非零非单位元，即每个非零元都是单位，R是域。R是域则R=Frac(R)≅ℝ。 |
| 7 | 能量传递引导 | 0.8 | 完整总结证明，确保每步逻辑衔接。 | 假设R不是域→R有素元p→在Frac(R)≅ℝ下p或-p为正→√p存在→写√p=a/b(gcd=1)→a²=pb²→p|a→p|b→与gcd=1矛盾→R无素元→R是域→R≅ℝ。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 4.0
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R5
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R4

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
- problem_type: characterization（刻画UFD何时等于其分式域，即何时UFD是域）
- structure_features: 结构蕴含题——UFD + 分式域≅ℝ ⟹ R≅ℝ。证明用反证法，将代数性质（UFD素分解）与分析性质（ℝ中正实数有平方根）跨域结合导出矛盾。
- key_objects: UFD R, FractionRing R, 环同构, 素元, ℝ中的平方根, UFD中的gcd

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [proof_by_contradiction, cross_domain_connection, structural_implication_analysis, prime_factorization_argument]
- primary_pattern: cross_domain_connection（跨域连接——将ℝ的分析性质与UFD的代数结构连接）
- knowledge_required: [UFD（唯一分解环）, 分式域/商域, UFD中的素元, 域同构, ℝ中正实数有平方根, UFD中的gcd]
- key_insight: 若R有素元p，则√p（或√(-p)）在Frac(R)≅ℝ中存在，写√p=a/b（gcd(a,b)=1）平方得a²=pb²，由p素性推出p|a且p|b，矛盾——故R无素元，R是域，R≅ℝ。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 代数结构理论（UFD、素分解、分式域）
- translation_to: 有序域/实分析性质（ℝ中正实数有平方根）
- translation_type: cross_domain_translation（跨域翻译——从纯代数结构翻译到利用ℝ的分析性质，再用代数结论收尾）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: logical_deduction, gap_type: knowledge_gap}
- tell_small_concepts: [prime element, square root in ℝ, UFD, fraction field, proof by contradiction, gcd argument]
- expected_ai_method: bare AI会尝试整闭性论证或直接代数操作，试图证明R在Frac(R)中整闭然后推出R=Frac(R)，但无法找到平方根与素分解的跨域连接
- correct_method: 反证法——假设R有素元p，利用ℝ中正实数有平方根的性质在Frac(R)中取√p=a/b（gcd=1），平方后用素性推出p|a且p|b，矛盾

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ → 是。characterization/logical_deduction/knowledge_gap均可归入已有类别。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ → 是。characterization是已有抽象级problem_type，logical_deduction是已有抽象级ai_method_type，knowledge_gap是已有抽象级gap_type。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ → 足够。这道题的跨域特征（代数↔分析）在gap_type=knowledge_gap中已体现，不需要新维度。
- [x] 如果发现拓扑分类需要进化，在此写出建议： → 无需进化。现有拓扑分类体系可覆盖此题。

**拓扑进化建议**（如有）：无。现有分类体系足够。

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

**全局pair详情**：
1. path_feature型：完整证明路径（UFD假设→假设非域→素元存在→ℝ平方根→gcd矛盾→R是域），路径特征在局部不可见因为每步看似独立但跨域连接只在全景视角下显现。why_not_visible_locally: 各步（UFD有素元、ℝ有平方根、gcd论证）局部可见，但分析性质与代数结构的跨域连接只在完整路径视角下可见——没有任何单步揭示"应该用平方根来矛盾素分解"。
2. implicit型：ℝ平方根性质与UFD素分解之间的蕴含连接，观察点在R5。why_not_visible_locally: ℝ有平方根是已知分析事实，UFD有素分解是已知代数事实，但两者之间的连接——用平方根通过gcd论证矛盾素性——在任一单独事实中都不可见，只有在分式域同构的语境下同时考虑两者才浮现。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试整闭性论证（UFD整闭）或超越次数论证，试图直接证明R=Frac(R)但找不到平方根与素分解的跨域连接。整闭性不足以推出R=Frac(R)因为Frac(R)\R中的元素未必在R上整。跨域洞察（用ℝ的平方根性质矛盾素分解）是非显然的，不太可能被自发发现。
- suitable_for_poc: ["tell_extraction", "hint_injection", "knowledge_bottleneck_detection", "cross_domain_connection"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

完整profile JSON已写入 `subagents-dirs/fate_000263/profile.json`。所有字段已逐项检查：
- _key=fate_000263 ✓
- source_id=FATE-X-14 ✓
- source_dataset=FATE-X ✓
- schema_version=3 ✓
- problem_text ✓
- solution_text ✓
- solution_summary ✓
- domain=Abstract Algebra ✓
- subfield=Field Theory / Commutative Algebra ✓
- answer_type=proof ✓
- answer="R is isomorphic to ℝ" ✓（非None）
- problem_type=characterization ✓
- solution_method_type=proof_by_contradiction ✓
- structure_features ✓
- key_objects ✓
- thinking_patterns ✓
- primary_pattern=cross_domain_connection ✓
- knowledge_required ✓
- key_insight ✓
- translation_from/to/type ✓
- tell_topology（profile级）✓
- tell_small_concepts（profile级）✓
- expected_ai_method ✓
- correct_method ✓
- tell_hint_pairs（7对，每对含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）✓
- global_tell_hint_pairs（2对，含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）✓
- bare_ai_expected=fail ✓
- bare_ai_error_prediction ✓
- suitable_for_poc ✓
- discriminates_levels=true ✓
- qa_sequence（含rounds数组和stats子对象，stats中knowledge_bottleneck="R5"、thinking_bottleneck="R4"为字符串类型）✓
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
2. 更新`problem_extraction_progress`集合中`_key="396373"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000263"
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
    '_key': '396373',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000263',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000263')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证输出: fate_000263, 7 local pairs, 2 global pairs

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: fate_000263
- solution_method_type: proof_by_contradiction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型，1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有分类体系（characterization / logical_deduction / knowledge_gap）足够覆盖此题。
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
