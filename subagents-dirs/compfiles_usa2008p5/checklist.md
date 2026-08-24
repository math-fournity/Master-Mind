# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2008p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2008P5.lean
- **来源**: USA 2008 P5
- **ArangoDB progress记录_key**: 329433（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2008P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：三个非负实数 r₁, r₂, r₃ 写在黑板上，存在不全为零的整数 a₁, a₂, a₃ 满足 a₁r₁ + a₂r₂ + a₃r₃ = 0。允许操作：选 x ≤ y，擦去 y 写 y−x。证明：有限次操作后黑板上至少出现一个 0。
- 解答核心思路（1-2句话）：维护整数线性关系作为不变量，用系数权重 |a₁|+|a₂|+|a₃| 作为严格递减的非负整数测度，迫使某个系数变为零后归约到两变量欧几里得算法。
- 解答关键步骤列表：
  1. **move_lemma**：当 rₖ ≤ rᵢ 时，用 rₖ 减 rᵢ，更新系数 aₖ → aₖ+aᵢ，保持零和关系且权重严格递减
  2. **phase1_pos / phase1_core**：当无系数为零时，通过符号和大小关系的分类讨论，总存在一步使权重严格递减
  3. **euclid**：减法欧几里得算法——若两数为正整数倍公共实数 t，反复用大减小可到达 0
  4. **phase2**：某系数为零时（如 a₃=0），得 a₁r₁+a₂r₂=0，故 r₁/r₂ 为有理数，两数是公共 t 的有理倍数，用欧几里得算法终结
  5. **key**：对权重做强归纳——板上已有0则完成；两数相等则一步得0；否则全正且互异，有系数为零走phase2，无系数为零走phase1递减权重后归纳假设

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述题目结构：已知条件（包括整数关系）、允许的操作、需要证明什么？ | 三个非负实数 r₁,r₂,r₃ 满足整数线性关系 a₁r₁+a₂r₂+a₃r₃=0（aᵢ不全为零）。操作：选 x≤y，用 y−x 替换 y。目标：证明有限次操作后出现 0。 |
| 2 | 自由列举 | 0.7 | 列出所有可能的方法来证明有限次操作后能到达 0。 | 欧几里得算法、不变量方法、归纳法、递减测度/权重、分类讨论、归约到两变量。 |
| 3 | 小尝试 | 0.4 | 尝试直接对三个数用欧几里得算法。三个数比两个数多了什么困难？ | 两个数时减法欧几里得算法因和递减而终止。三个数时数字本身没有明显的递减测度，过程可能不终止于 0。 |
| 4 | 思维操作引导 | 0.5 | 关键在于整数关系 a₁r₁+a₂r₂+a₃r₃=0。当我们用 rⱼ 减 rᵢ（替换 rᵢ 为 rᵢ−rⱼ）时，应如何更新系数以保持这个关系？ | 将 aⱼ 更新为 aⱼ+aᵢ。则 (aⱼ+aᵢ)rⱼ + aᵢ(rᵢ−rⱼ) + ... = aⱼrⱼ + aᵢrᵢ + ... = 0。关系保持。这将问题从实数操作转化为整数系数追踪。 |
| 5 | 推进 | 0.6 | 定义权重为 |a₁|+|a₂|+|a₃|。证明只要没有系数为零，总存在一步合法操作使权重严格递减。 | 通过对系数符号和 r 值大小关系的分类讨论：最大的 r 值总可以被一个较小的值减，对应的系数更新使权重递减。具体地，若 aᵢ>0 对应最大 rᵢ，选合适的 j 使 |aⱼ+aᵢ|<|aⱼ|。 |
| 6 | 推进 | 0.5 | 当某个系数变为零（如 a₃=0）时，这对剩余两个数意味着什么？如何完成证明？ | a₁r₁+a₂r₂=0 且 a₁,a₂≠0，故 r₁/r₂=−a₂/a₁ 为有理数。两数是公共实数 t 的有理倍数，减法欧几里得算法在有限步内产生 0。 |
| 7 | 能量传递引导 | 0.8 | 将两个阶段与权重上的强归纳结合，完成完整证明。 | 对权重做强归纳：已有0则完成；两数相等则一步得0；否则全正互异，有系数为零走phase2，无系数为零走phase1递减权重后用归纳假设。权重是非负整数，过程终止。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5
- knowledge_rounds（思维操作引导的轮数）: 1
- level_sum: 4.3
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence
- structure_features: 三个非负实数具有整数线性依赖关系；允许操作为减法替换（y→y−x for x≤y）；目标是证明有限步内可到达含零状态。核心结构是整数系数向量及其权重作为递减测度。
- key_objects: 非负实数 r₁,r₂,r₃；整数系数 a₁,a₂,a₃（不全为零）；减法操作（y→y−x）；权重函数 |a₁|+|a₂|+|a₃|；欧几里得算法

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["invariant_identification", "measure_decreasing", "phase_decomposition", "strong_induction", "reduction_to_two_variables"]
- primary_pattern: measure_decreasing
- knowledge_required: ["减法欧几里得算法", "整数线性关系", "不变量方法", "强归纳", "绝对值性质"]
- key_insight: 整数线性关系可作为不变量在每次操作中通过更新系数来维护，权重 |a₁|+|a₂|+|a₃| 严格递减，迫使某系数为零后归约到两变量欧几里得算法。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 黑板上实数的直接操作（减法替换）
- translation_to: 整数系数向量的追踪与权重递减分析
- translation_type: structural_transformation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_manipulation, gap_type: structural_transformation}
- tell_small_concepts: ["integer linear relation", "subtractive operation", "weight decreasing", "Euclidean algorithm", "strong induction", "invariant maintenance", "rational ratio", "two-phase strategy"]
- expected_ai_method: direct_manipulation — bare AI会直接对三个实数尝试欧几里得算法，不追踪整数系数
- correct_method: invariant_induction — 维护整数关系不变量 + 权重递减 + 强归纳

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=structural_existence、ai_method_type=direct_manipulation、gap_type=structural_transformation 均可归入已有拓扑类别
- [x] 粒度一致——标注值与已有值粒度统一
- [x] 不需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell
- [ ] 无需进化建议

**拓扑进化建议**：无。当前拓扑分类体系足够覆盖此题。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 2 个，implicit型: 1 个

**局部pair概要**：
| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到减法操作立即想到欧几里得算法，但未注意到整数线性关系这一关键结构元素 | 描述完整题目结构：已知条件（含整数关系）、操作、目标 | 0.8 | 纯元认知观察 | false | (structural_existence, direct_manipulation, method_problem_mismatch) | blackboard operation, integer linear relation, nonnegative reals |
| 2 | AI列出欧几里得算法和直接方法，但未考虑不变量方法或系数追踪 | 列出所有可能方法，包括不变量方法、递减测度、归纳策略 | 0.7 | 自由列举 | false | (structural_existence, enumeration_brute_force, search_space_estimation) | Euclidean algorithm, invariant, induction, termination |
| 3 | AI尝试对三个数直接用欧几里得算法，卡在三变量终止性 | 尝试直接对三个数用欧几里得算法，三个数比两个数多了什么困难？ | 0.4 | 小尝试 | false | (structural_existence, direct_calculation, method_problem_mismatch) | three-number Euclidean, termination failure, cycling risk |
| 4 | AI未将整数关系与操作联系起来——不知道系数可以更新以保持关系 | 关键是整数关系。用 rⱼ 减 rᵢ 时如何更新系数保持关系？ | 0.5 | 思维操作引导 | true | (structural_existence, direct_manipulation, structural_transformation) | coefficient update, invariant maintenance, weight function |
| 5 | AI有权重概念但看不出为何必递减——需要符号和大小关系的分类讨论 | 定义权重为 |a₁|+|a₂|+|a₃|。证明无系数为零时总存在一步使权重严格递减 | 0.6 | 推进 | false | (discrete_combinatorial, case_by_case, knowledge_gap) | sign analysis, weight decrease, case analysis, absolute value |
| 6 | AI看不出零系数将问题归约到可解的两变量情形 | 某系数为零时这对剩余两数意味着什么？如何完成？ | 0.5 | 推进 | true | (structural_existence, direct_calculation, knowledge_gap) | rational ratio, two-variable Euclidean, coefficient zero |
| 7 | AI有所有拼图（不变量、递减权重、两阶段归约）但未组装成完整归纳证明 | 将两阶段与权重上的强归纳结合，完成完整证明 | 0.8 | 能量传递引导 | false | (structural_existence, logical_deduction, method_translation) | strong induction, two-phase composition, termination proof |

**全局pair概要**：
1. (path_feature) 两阶段策略：Phase 1 递减权重→Phase 2 欧几里得算法。why_not_visible_locally: 两阶段结构是全局路径特征，从任何单步只能看到权重递减阶段或欧几里得阶段之一，看不到它们如何连接。
2. (implicit, Q4) 整数线性关系作为可维护不变量。why_not_visible_locally: 题目只说关系存在，未说可通过操作维护。系数可更新的洞察需要看到减法操作与线性代数的联系，这在任何单步中不可见。
3. (path_feature) 权重作为全局递减测度。why_not_visible_locally: 权重函数仅在结构转换到系数追踪后才有意义。从原始实数操作视角无 obvious 递减测度。权重是从不变量与操作的交互中涌现的路径特征。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会直接对三个实数尝试欧几里得算法，不追踪整数系数，卡在三变量终止性证明上。不会看到整数关系可作为不变量维护的关键洞察，也不会想到用权重作为递减测度。
- suitable_for_poc: ["tell_extraction", "hint_injection", "structural_transformation_detection"]
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
- [x] answer（proof类型填要证明的结论）
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

**将完整JSON写入工作目录的 `profile.json` 文件** — 已完成

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
2. 更新`problem_extraction_progress`集合中`_key="329433"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa2008p5"
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
    '_key': '329433',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa2008p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa2008p5')
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
- problem_id: compfiles_usa2008p5
- solution_method_type: invariant_induction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，当前拓扑分类体系足够覆盖此题
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
