# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000331
- **文件路径**: subagents-dirs/fate_000331/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396441（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000331/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设A是Noetherian完备局部环，维数d，混合特征（Char A=0, Char A/m=p），ht(pA)=1。证明A是子环B⊂A上的有限生成模，且B≅C[[x₁,...,x_{d-1}]]，其中C是DVR。
- 解答核心思路（1-2句话）：这是Cohen结构定理的混合特征情形——ht(pA)=1迫使系数环为DVR，选取d-1个参数元由完备性得到形式幂级数环，Noetherian性保证模有限性。Lean文件中proof为sorry，无实际证明代码。
- 解答关键步骤列表：
  1. 识别此为Cohen结构定理应用
  2. ht(pA)=1 → 系数环为DVR（而非一般Cohen环）
  3. 选取d-1个参数元x₁,...,x_{d-1}，与DVR一起生成B
  4. 完备性保证B≅C[[x₁,...,x_{d-1}]]
  5. Noetherian性保证A在B上模有限

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
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：已知条件有哪些？要证明的结论是什么？结论中B的结构C[[x₁,...,x_{d-1}]]暗示了什么？ | A是Noetherian完备局部环，维数d，混合特征(Char A=0, Char A/m=p)，ht(pA)=1。结论：A是子环B上的有限生成模，B≅C[[x₁,...,x_{d-1}]]，C是DVR。B的结构暗示A被一个DVR上的d-1元形式幂级数环控制。 |
| 2 | 自由列举 | 0.7 | 对于完备Noetherian局部环，有哪些可用的结构定理和工具？列出所有你能想到的。 | Cohen结构定理、Krull交定理、参数系、结合素理想、p-adic完备化、系数环、正规化引理、完备化忠实平坦性…… |
| 3 | 小尝试 | 0.5 | 尝试直接构造B：取A中由p和某个参数系生成的子环，看看能否得到C[[x₁,...,x_{d-1}]]的结构？ | 直接取子环生成会遇到困难：需要保证子环同构于形式幂级数环（需要完备性），且系数环需要是DVR而非一般环。不使用Cohen结构定理很难从零构造。 |
| 4 | 思维操作引导 | 0.6 | 分析条件ht(pA)=1的含义。在Cohen结构定理中，混合特征完备局部环的系数环由什么决定？ht(pA)=1如何影响系数环的类型？ | Cohen结构定理中，混合特征完备局部环有系数环。当ht(pA)=1时，p生成高度1的素理想，系数环是DVR（而非一般Cohen环，后者对应ht(pA)>1的情形）。这是关键：ht(pA)=1将系数环从一般Cohen环提升为DVR。 |
| 5 | 推进 | 0.5 | 已知系数环C是DVR，如何构造B≅C[[x₁,...,x_{d-1}]]？需要选取什么元素？完备性如何发挥作用？ | 选取d-1个元素x₁,...,x_{d-1}构成部分参数系（与p一起构成参数系）。由A的完备性，C和x₁,...,x_{d-1}生成的子环同构于C[[x₁,...,x_{d-1}]]。维数d意味着除DVR外还需d-1个参数。 |
| 6 | 思维操作引导 | 0.4 | 现在证明A在B上是有限生成模。A的什么性质保证了这一点？ | A是Noetherian的，B是完备局部子环。由Cohen结构定理的模有限性部分：A在系数环和参数系生成的子环上是有限生成模。Noetherian性保证生成元有限。具体地，A的剩余元在B上的整性给出模有限性。 |
| 7 | 能量传递引导 | 0.3 | 将所有步骤组装：这正是Cohen结构定理的混合特征+ht(p)=1情形。总结完整证明。 | (1)由Cohen结构定理，A有系数环；(2)ht(pA)=1使系数环C为DVR；(3)选d-1个参数元，完备性给出B≅C[[x₁,...,x_{d-1}]]；(4)Noetherian性给出A在B上模有限。QED。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5（R1,R2,R3,R5,R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4,R6）
- level_sum: 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
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
- structure_features: 存在性证明——证明完备局部环A存在特定结构的子环B（DVR上的形式幂级数环），使得A在B上模有限。核心是识别结构定理并应用。
- key_objects: Noetherian完备局部环A、维数d、混合特征、素数p、理想高度ht(pA)、DVR C、形式幂级数环C[[x₁,...,x_{d-1}]]、子环B、有限生成模

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [theorem_recognition, hypothesis_analysis, parameter_selection, synthesis]
- primary_pattern: theorem_recognition（识别并应用Cohen结构定理）
- knowledge_required: [Cohen结构定理, 混合特征局部环, 理想高度, DVR与系数环, 参数系, 形式幂级数环, 模有限性]
- key_insight: ht(pA)=1将Cohen结构定理中的系数环从一般Cohen环提升为DVR，这是连接假设与结论的关键枢纽

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 抽象环论条件（完备、Noetherian、混合特征、ht(p)=1）
- translation_to: Cohen结构定理框架（系数环+参数系→形式幂级数环+模有限性）
- translation_type: structure_theorem_recognition（从具体环论条件识别为经典结构定理的特定情形）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_manipulation, gap_type: knowledge_gap}
- tell_small_concepts: [Cohen结构定理, 混合特征, 系数环, ht(pA)=1, DVR, 形式幂级数环, 参数系, 模有限性, 完备局部环]
- expected_ai_method: bare AI会尝试直接构造子环B（取p和参数系生成的子环），但不知道Cohen结构定理，无法保证子环同构于形式幂级数环也无法证明模有限性
- correct_method: 识别为Cohen结构定理的混合特征+ht(p)=1情形，利用系数环为DVR+参数系+完备性+Noetherian性完成证明

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ → 可以。structural_existence + direct_manipulation + knowledge_gap 均为已有值，完全适用。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ → 一致。三个维度都是抽象级别。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ → 足够。本题的核心gap是知识gap（不知道Cohen结构定理），三个维度能区分。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。

**拓扑进化建议**（如有）：无。已有拓扑分类完全适用。

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
- bare_ai_error_prediction: bare AI不知道Cohen结构定理，会尝试直接构造子环B但无法保证同构于形式幂级数环，也无法利用ht(pA)=1推出系数环为DVR。会陷入从零推导结构定理的困境。
- suitable_for_poc: ["knowledge_bottleneck_detection", "theorem_recognition_hint_injection", "hint_level_calibration"]
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
- [x] answer
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
- [x] tell_hint_pairs
- [x] global_tell_hint_pairs
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence
- [x] analysis_metadata

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
2. 更新`problem_extraction_progress`集合中`_key="396441"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000331"
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
    '_key': '396441',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000331',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000331')
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
- problem_id: fate_000331
- solution_method_type: structure_theorem_application
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，已有拓扑分类完全适用
- 是否遇到异常: 无

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
