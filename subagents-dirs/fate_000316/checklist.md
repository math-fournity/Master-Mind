# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000316
- **文件路径**: subagents-dirs/fate_000316/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396426（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000316/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let A = k[[x₁,...,xₙ]] where k is a field, n ∈ ℕ, n ≠ 0. Show that there is NO isomorphism A ⊗_k A ≅ k[[x₁,...,xₙ, y₁,...,yₙ]].
- 解答核心思路（1-2句话）：元素 1+x₁y₁ 在 k[[x₁,...,xₙ, y₁,...,yₙ]] 中是单位（几何级数收敛），但在 A⊗_k A 中不是单位（逆元是无穷个可分项之和，不属于张量积）。单位性在同构下保持，故两环不同构。
- 解答关键步骤列表：
  1. 在 k[[x,y]] 中，(1+x₁y₁)^{-1} = Σ(-x₁y₁)^i = Σ(-1)^i x₁^i y₁^i（几何级数，在m-adic拓扑中收敛）
  2. 在 A⊗_k A 中，假设 1+x₁y₁ 有逆元 u = Σ_{j=1}^m f_j(x)g_j(y)（有限和）
  3. 在 k[[x,y]] 中比较系数：系数矩阵 M_{ab} = Σ_j [x₁^a]f_j·[y₁^b]g_j = (-1)^a δ_{ab}
  4. M 是无穷对角矩阵（对角元非零），有无穷秩
  5. 但 M = Σ_j v_j w_j^T（有限个外积之和），秩 ≤ m < ∞
  6. 矛盾！故 1+x₁y₁ 在 A⊗_k A 中不是单位
  7. 单位性是环同构不变量，故两环不同构

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.3 | 描述这道题的结构：两个环分别是什么？我们需要证明什么？ | A = k[[x₁,...,xₙ]]，需证 A⊗_k A 与 k[[x₁,...,xₙ, y₁,...,yₙ]] 不同构。这是一个交换代数中的非同构证明问题，n≥1。 |
| 2 | 自由列举 | 0.5 | 列出所有可能区分这两个环的环论不变量 | Krull维数、Noether性、完备性、单位群结构、极大理想生成元数、剩余域、嵌入维数…… |
| 3 | 小尝试 | 0.4 | 试着比较Krull维数和嵌入维数 | 两环的Krull维数都是2n，嵌入维数都是2n，极大理想都由2n个元素生成。这些标准不变量无法区分它们。 |
| 4 | 思维操作引导 | 0.6 | 思考A⊗_k A中的元素与k[[x,y]]中的元素有什么结构差异？张量积中的元素长什么样？ | A⊗_k A的元素是有限个乘积f(x)g(y)之和——"可分"幂级数。k[[x,y]]包含任意幂级数，包括不可分的如Σx₁^i y₁^i。 |
| 5 | 思维操作引导 | 0.7 | 考虑元素1+x₁y₁。它在每个环中是否是单位？为什么？ | 在k[[x,y]]中是单位：(1+x₁y₁)^{-1}=Σ(-x₁y₁)^i（几何级数在m-adic拓扑中收敛）。在A⊗_k A中，逆元需要是Σ(-1)^i x₁^i y₁^i，这是无穷个可分项之和，不是有限和，可能不在张量积中。 |
| 6 | 思维操作引导 | 0.7 | 严格证明Σ(-1)^i x₁^i y₁^i不能写成有限个乘积f_j(x)g_j(y)之和 | 若Σ(-1)^i x₁^i y₁^i = Σ_{j=1}^m f_j(x)g_j(y)，则系数矩阵M_{ab}=Σ_j [x₁^a]f_j·[y₁^b]g_j = (-1)^a δ_{ab}。这是无穷对角矩阵（非零对角元），有无穷秩。但M=Σ_j v_j w_j^T是有限个外积之和，秩≤m。矛盾！ |
| 7 | 能量传递引导 | 0.3 | 把以上步骤组合起来，完成证明 | 1+x₁y₁在k[[x,y]]中是单位但在A⊗_k A中不是单位。单位性在环同构下保持，故两环不同构。QED。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 3
- knowledge_rounds（思维操作引导的轮数）: 3
- level_sum: 3.5
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence
- structure_features: 非同构证明——通过寻找环论不变量（单位性）区分两个环；关键在于代数张量积与完备化张量积的结构差异
- key_objects: ["k[[x₁,...,xₙ]]形式幂级数环", "代数张量积 A⊗_k A", "k[[x₁,...,xₙ, y₁,...,yₙ]]多变量幂级数环", "元素1+x₁y₁及其逆元", "系数矩阵与秩论证"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["invariant_comparison", "structural_analysis", "rank_argument", "proof_by_contradiction"]
- primary_pattern: invariant_comparison
- knowledge_required: ["formal_power_series_rings", "tensor_product_of_algebras", "completeness_of_local_rings", "units_in_complete_local_rings", "rank_of_infinite_matrices"]
- key_insight: 1+x₁y₁在完备环k[[x,y]]中是单位（几何级数收敛），但在非完备的代数张量积A⊗_k A中不是单位（逆元是不可分幂级数，秩论证证明其不属于张量积）

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: geometric_series_completeness（几何级数/完备性语言）
- translation_to: rank_argument_finite_sum（秩论证/有限和语言）
- translation_type: method_translation（从拓扑/分析性质翻译为线性代数论证）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "direct_calculation", gap_type: "knowledge_gap"}
- tell_small_concepts: ["completeness", "unit_group", "geometric_series", "separable_power_series", "rank_argument", "tensor_product_vs_completion"]
- expected_ai_method: bare AI会尝试直接比较环不变量（维数、Noether性）或构造显式映射，不会想到测试特定元素的单位性
- correct_method: 通过测试1+x₁y₁的单位性区分完备环与非完备张量积，用秩论证严格证明非可分性

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——structural_existence/direct_calculation/knowledge_gap能归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell和已有tell
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。已有分类体系足够。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pair摘要**：
| Round | tell | hint | hint_level | situation_type | knowledge_bottleneck | topology |
|---|---|---|---|---|---|---|
| 1 | AI未识别问题类型为非同构证明 | 描述题目结构，识别两个环和目标 | 0.3 | 纯元认知观察 | false | (structural_existence, direct_calculation, method_problem_mismatch) |
| 2 | AI未列举出完备性/单位群等关键不变量 | 列出所有可能区分两个环的环论不变量 | 0.5 | 自由列举 | false | (structural_existence, enumeration_brute_force, search_space_estimation) |
| 3 | AI尝试维数比较但未发现不变量全部匹配 | 比较Krull维数和嵌入维数 | 0.4 | 小尝试 | false | (structural_existence, direct_calculation, method_problem_mismatch) |
| 4 | AI未认识到张量积元素是有限可分和 | 思考张量积元素与幂级数环元素的结构差异 | 0.6 | 思维操作引导 | false | (structural_existence, direct_manipulation, structural_transformation) |
| 5 | AI未想到测试1+x₁y₁的单位性 | 考虑1+x₁y₁在每个环中是否是单位 | 0.7 | 思维操作引导 | true | (structural_existence, direct_calculation, knowledge_gap) |
| 6 | AI未掌握秩论证证明非可分性 | 严格证明Σ(-1)^i x^i y^i不是有限个乘积之和 | 0.7 | 思维操作引导 | true | (structural_existence, logical_deduction, knowledge_gap) |
| 7 | AI未将各步组合完成证明 | 组合所有步骤完成证明 | 0.3 | 能量传递引导 | false | (structural_existence, logical_deduction, method_translation) |

**全局pair摘要**：
1. path_feature型：完整证明路径——从标准不变量全部失败到转向单位性测试再到秩论证
2. implicit型：秩论证——无穷对角矩阵有无穷秩vs有限外积和有界秩

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试比较Krull维数、Noether性等标准不变量，发现它们都匹配后陷入困境。不会想到测试特定元素1+x₁y₁的单位性，也不会用秩论证证明幂级数的非可分性。关键知识缺口：代数张量积与完备化张量积的区别、完备环中1+m元素必为单位、秩论证证明非可分性。
- suitable_for_poc: ["tell_extraction", "hint_injection", "knowledge_bottleneck_detection"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

完整profile JSON已写入 `subagents-dirs/fate_000316/profile.json`。所有字段已检查：_key, source_id, source_dataset, schema_version, problem_text, solution_text, solution_summary, domain, subfield, answer_type, answer, problem_type, solution_method_type, structure_features, key_objects, thinking_patterns, primary_pattern, knowledge_required, key_insight, translation_from, translation_to, translation_type, tell_topology, tell_small_concepts, expected_ai_method, correct_method, tell_hint_pairs(7个，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts), global_tell_hint_pairs(2个，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts), bare_ai_expected, bare_ai_error_prediction, suitable_for_poc, discriminates_levels, qa_sequence(含rounds和stats), analysis_metadata。

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
2. 更新`problem_extraction_progress`集合中`_key="396426"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000316"
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
    '_key': '396426',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000316',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000316')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

- problem_id: fate_000316
- solution_method_type: invariant_comparison
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，已有分类体系足够
- 是否遇到异常: 否

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
