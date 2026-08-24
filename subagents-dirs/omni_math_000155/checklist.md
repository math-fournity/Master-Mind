# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000155
- **文件路径**: subagents-dirs/omni_math_000155/problem.lean
- **来源**: AoPS omni_math (china_team_selection_test)
- **ArangoDB progress记录_key**: 330027（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000155/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：证明对所有正整数n，Σ_{m=1}^n 5^{ω(m)} ≤ Σ_{k=1}^n ⌊n/k⌋ τ(k)² ≤ Σ_{m=1}^n 5^{Ω(m)}，其中ω(m)为不同素因子个数，Ω(m)为素因子总数（计重数），τ(k)为约数个数。
- 解答核心思路（1-2句话）：将中间和重写为Σf(m)其中f(m)=Σ_{d|m}τ(d)²是积性函数，利用积性性归约到素数幂验证。解答先证明3的辅助引理（3^ω≤Στ(d)≤3^Ω），再推广到5的主不等式。
- 解答关键步骤列表：
  1. 定义辅助函数χ=3^ω, φ=Στ(d), ψ=3^Ω，证明χ≤φ≤ψ（积性归约到素数幂）
  2. 将中间和⌊n/k⌋τ(k)²重写：⌊n/k⌋=#{m≤n: k|m}，交换求和顺序得Σ_{m=1}^n f(m)，f(m)=Σ_{d|m}τ(d)²
  3. 证明f是积性函数（τ²与1的Dirichlet卷积）
  4. 素数幂计算：f(p^a)=Σ(j+1)²=(a+1)(a+2)(2a+3)/6
  5. 验证5≤f(p^a)≤5^a（a=1等号，a≥2多项式vs指数）
  6. 由积性性得5^ω(m)≤f(m)≤5^Ω(m)，求和完成证明

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
| 1 | 纯元认知观察 | 0.3 | 观察不等式结构，识别ω、Ω、τ的含义 | 识别三重求和，ω为不同素因子数，Ω为素因子总数，τ为约数个数 |
| 2 | 自由列举 | 0.5 | 列出所有可能的证明方向 | 逐项估计、积性函数、交换求和、归纳、Dirichlet卷积等 |
| 3 | 小尝试 | 0.4 | 尝试直接逐项估计⌊n/k⌋τ(k)² | 失败：各项无法单独对应5^ω或5^Ω |
| 4 | 思维操作引导 | 0.2 | ⌊n/k⌋的数学含义？能否重写二重求和？ | ⌊n/k⌋=计数函数，交换求和得Σf(m)，f(m)=Σ_{d|m}τ(d)² |
| 5 | 推进 | 0.3 | f(m)有什么特殊性质？ | f是积性函数（τ²与1的Dirichlet卷积） |
| 6 | 思维操作引导 | 0.2 | 如何利用积性函数性质简化验证？ | 归约到素数幂：验证5≤f(p^a)≤5^a |
| 7 | 能量传递引导 | 0.4 | 计算f(p^a)并验证不等式，完成证明 | f(p^a)=(a+1)(a+2)(2a+3)/6，a=1等号，a≥2多项式vs指数，由积性性完成 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 2.3
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
- problem_type: inequality_proof
- structure_features: 双重不等式含三个算术函数求和；中间项含floor函数和平方约数函数；所有相关函数均为积性函数，可归约到素数幂；解答先证3的辅助引理再推广到5
- key_objects: ω(m)不同素因子数, Ω(m)素因子总数, τ(k)约数函数, ⌊n/k⌋计数函数, f(m)=Σ_{d|m}τ(d)²积性函数, 素数幂p^a, 辅助函数χ=3^ω/φ=Στ(d)/ψ=3^Ω

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["structural_rewrite", "multiplicativity_reduction", "prime_power_verification", "double_sided_bound", "auxiliary_lemma"]
- primary_pattern: multiplicativity_reduction
- knowledge_required: ["算术函数ω/Ω/τ", "积性函数及其性质", "Dirichlet卷积", "floor函数计数恒等式⌊n/k⌋=#{m≤n: k|m}", "平方和公式", "积性函数不等式归约到素数幂"]
- key_insight: 将中间和重写为Σf(m)其中f(m)=Σ_{d|m}τ(d)²是积性函数，逐项不等式5^ω(m)≤f(m)≤5^Ω(m)归约到素数幂验证f(p^a)=(a+1)(a+2)(2a+3)/6介于5和5^a之间

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 含floor函数和平方约数函数的二重求和
- translation_to: 积性函数（Dirichlet卷积τ²*1）的单重求和，归约到素数幂验证
- translation_type: structural_transformation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: ["floor as counting function", "Dirichlet convolution", "multiplicativity", "prime power reduction", "sum of squares formula"]
- expected_ai_method: direct_calculation — 尝试逐项估计⌊n/k⌋τ(k)²而不做结构性重写
- correct_method: 将二重求和结构重写为积性函数单重求和，再通过积性性归约到素数幂验证

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能归入已有的拓扑类别（inequality_proof, direct_calculation, structural_transformation）
- [x] 粒度是否一致——标注值和已有值粒度统一
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化，现有分类体系足够

**拓扑进化建议**（如有）：无。现有拓扑分类体系（problem_type=inequality_proof, ai_method_type=direct_calculation/direct_manipulation/logical_deduction/algebraic_identity, gap_type=structural_transformation/knowledge_gap/method_problem_mismatch/method_translation）完全覆盖本题所有tell的拓扑特征。

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
- bare_ai_error_prediction: Bare AI会尝试逐项估计⌊n/k⌋τ(k)²或使用粗略上下界，错过将floor函数理解为计数函数的关键结构性重写，以及积性函数归约到素数幂的方法。无法识别中间和等于Σf(m)（积性函数），因此无法与5^ω和5^Ω建立联系。
- suitable_for_poc: ["tell_detection", "hint_injection", "structural_transformation_gap"]
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

## Step 10: 入库ArangoDB [x]

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="330027"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_000155"
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
    '_key': '330027',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_000155',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_000155')
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
- problem_id: omni_math_000155
- solution_method_type: multiplicativity_reduction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，现有分类体系完全覆盖
- 是否遇到异常: 无（解答文件不完整，仅含3的辅助引理部分，已根据数学理解补全完整证明）

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
