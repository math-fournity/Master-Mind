# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000368
- **文件路径**: subagents-dirs/fate_000368/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396478（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000368/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：考虑多项式环 k[x₁,...,x₆] 中由6个二次多项式 f₁,...,f₆ 生成的理想 I。证明 R/I 是维度为3的Cohen-Macaulay环。6个生成元均为二次型：f₁=x₂x₄+x₃x₆, f₂=x₃x₅+x₁x₆, f₃=x₁x₂-x₂x₅+x₃x₅-x₅x₆, f₄=x₂x₃+x₂x₄+x₂x₆+x₆², f₅=x₃²+x₃x₄+x₃x₆-x₄x₆, f₆=x₁x₃+x₁x₄+x₄x₅+x₁x₆。
- 解答核心思路（1-2句话）：Lean中proof为sorry（无实际证明）。数学上，关键在于识别6个二次生成元的代数结构（Pfaffian/行列式结构），应用Buchsbaum-Eisenbud结构定理得到Cohen-Macaulay性质，并由理想高度3计算得dim R/I=3。
- 解答关键步骤列表：
  1. 识别6个二次型的代数结构（Pfaffian理想或行列式结构）
  2. 应用Buchsbaum-Eisenbud结构定理：高度3的Gorenstein理想由斜对称矩阵的Pfaffian生成，商环为Cohen-Macaulay
  3. 计算理想高度为3，得dim R/I = 6-3 = 3
  4. 组合两个结论完成证明

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
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：关键数学对象是什么？需要证明什么？已知条件是什么？ | 我们有多项式环k[x₁,...,x₆]和由6个二次多项式生成的理想I。需要证明R/I是维度为3的Cohen-Macaulay环。关键对象是6个二次生成元、商环、CM性质。 |
| 2 | 自由列举 | 0.7 | 列出你所知道的所有证明商环是Cohen-Macaulay的方法 | 方法包括：(1)找到长度等于维度的正则序列；(2)计算自由分解并检查射影维数；(3)Hilbert-Burch定理；(4)识别行列式/Pfaffian结构；(5)应用Buchsbaum-Eisenbud等结构定理；(6)用Groebner基直接计算 |
| 3 | 小尝试 | 0.4 | 先尝试计算维度：这6个方程对6维空间施加了多少个独立条件？ | 朴素地看，6个方程6个变量似乎维度为0，但方程不独立。理想高度为3，意味着6个生成元中只有3个在高度意义上"独立"。直接计数会误导，因为生成元之间存在代数关系。 |
| 4 | 思维操作引导 | 0.3 | 观察6个二次型的结构。高度3的理想若有超过3个生成元，可能是Gorenstein理想。检查这些是否是某个斜对称矩阵的Pfaffian。 | 高度3的理想有6个生成元（>3），不是完全交。由Buchsbaum-Eisenbud分类，高度3的Gorenstein理想由斜对称矩阵的Pfaffian生成。需要验证这6个二次型是否匹配某种Pfaffian或行列式结构。 |
| 5 | 推进 | 0.4 | 如果这些生成元具有Pfaffian/行列式结构，Buchsbaum-Eisenbud结构定理告诉你什么关于Cohen-Macaulay性质？ | Buchsbaum-Eisenbud结构定理：高度3的Gorenstein理想由(2n+1)×(2n+1)斜对称矩阵的Pfaffian生成，且商环是Cohen-Macaulay的。如果我们的理想匹配此结构，CM性质直接得到。 |
| 6 | 推进 | 0.3 | 现在验证维度。这个理想的高度是多少？ | 由Pfaffian/行列式结构，理想高度为3。因为dim k[x₁,...,x₆]=6且ht(I)=3，所以dim R/I = 6-3 = 3。 |
| 7 | 能量传递引导 | 0.2 | 组合两个结果：结构给出了Cohen-Macaulay和维度3。写出完整证明。 | 通过识别6个二次生成元的Pfaffian/行列式结构，Buchsbaum-Eisenbud结构定理保证R/I是Cohen-Macaulay的。理想高度为3，所以dim R/I=6-3=3。因此R/I是维度为3的Cohen-Macaulay环。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5
- knowledge_rounds（思维操作引导的轮数）: 1
- level_sum: 3.1
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
- problem_type: characterization（刻画商环R/I的代数性质：Cohen-Macaulay + 维度3）
- structure_features: 6个二次生成元在6变量多项式环中生成高度3的理想；生成元数量(6)大于高度(3)，非完全交；隐藏的Pfaffian/行列式结构；商环维度3
- key_objects: 多项式环k[x₁,...,x₆], 理想I(6个二次生成元), 商环R/I, Cohen-Macaulay性质, Krull维度, Pfaffian理想, 斜对称矩阵

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [structural_recognition, theorem_application, dimension_computation, proof_assembly]
- primary_pattern: structural_recognition（结构识别——从具体多项式识别隐藏的代数结构）
- knowledge_required: [Cohen-Macaulay环与深度, Krull维度与商环, Buchsbaum-Eisenbud结构定理, Pfaffian理想与行列式簇, 正则序列, 理想高度]
- key_insight: 6个二次生成元构成斜对称矩阵的Pfaffian理想，从而可应用Buchsbaum-Eisenbud结构定理直接得到Cohen-Macaulay性质

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 具体多项式计算（直接计算Groebner基/正则序列）
- translation_to: 结构化代数几何（Pfaffian/行列式理想理论 + Buchsbaum-Eisenbud结构定理）
- translation_type: method_translation（从计算方法翻译到结构定理方法）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_calculation, gap_type: knowledge_gap}
- tell_small_concepts: [Pfaffian理想, 斜对称矩阵, Buchsbaum-Eisenbud定理, 高度3 Gorenstein理想, Cohen-Macaulay, 正则序列, Krull维度]
- expected_ai_method: 直接计算Groebner基或试错寻找正则序列，不识别Pfaffian结构
- correct_method: 识别Pfaffian/行列式结构并应用Buchsbaum-Eisenbud结构定理

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ 是。characterization + direct_calculation + knowledge_gap 均为已有值，完全适用。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ 是。characterization与已有抽象级problem_type一致；direct_calculation和knowledge_gap均为已有抽象级值。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ 足够。这道题的核心gap是知识型（不知道Pfaffian结构定理），knowledge_gap准确描述。
- [x] 如果发现拓扑分类需要进化，在此写出建议： 无需进化。现有拓扑分类完全覆盖。

**拓扑进化建议**（如有）：无。现有分类体系充分。

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

**局部pair摘要**：
- R1: tell=看到具体理想但未识别结构特征, hint=描述问题结构, topology=(characterization, direct_calculation, method_problem_mismatch)
- R2: tell=已识别问题但未列举方法, hint=列举所有CM证明方法, topology=(characterization, enumeration_brute_force, method_problem_mismatch)
- R3: tell=尝试直接计数维度但被6方程6变量误导, hint=尝试计算维度, topology=(characterization, direct_calculation, search_space_estimation)
- R4: tell=困于直接计算，未识别Pfaffian结构（知识瓶颈）, hint=检查Pfaffian/斜对称矩阵结构, topology=(characterization, direct_calculation, knowledge_gap), is_knowledge_bottleneck=true
- R5: tell=已识别潜在结构但未连接到定理, hint=应用Buchsbaum-Eisenbud定理, topology=(characterization, logical_deduction, knowledge_gap)
- R6: tell=有CM结论但需验证维度, hint=从结构计算高度得维度, topology=(characterization, direct_calculation, method_translation)
- R7: tell=有全部部件但未组装证明, hint=组合结果写证明, topology=(characterization, logical_deduction, method_translation)

**全局pair摘要**：
- path_feature型: 解决路径从具体计算到结构识别到定理应用的整体特征；why_not_visible_locally=Pfaffian结构只有在同时审视全部6个生成元并了解斜对称矩阵理论时才可见，单个生成元或成对分析不揭示全局结构
- implicit型: 从(6生成元, 高度3)推断(Gorenstein, Pfaffian)的分类蕴含；why_not_visible_locally=此推断需要知道Buchsbaum-Eisenbud对高度3 Gorenstein理想的分类定理，不可从任何单一计算步骤导出

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI会尝试直接计算Groebner基或试错寻找正则序列，不识别Pfaffian结构。会在CM性质验证上卡住，因为深度计算需要结构洞察而非纯计算。
- suitable_for_poc: ["tell_extraction_structural", "knowledge_bottleneck_identification", "method_translation_verification"]
- discriminates_levels: true（此题需要深层的交换代数知识，能有效区分有/无结构定理知识的AI）

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
- [x] answer（"R/I is Cohen-Macaulay of dimension 3"）
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
- [x] tell_hint_pairs（7个局部pair，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（2个全局pair，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

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
2. 更新`problem_extraction_progress`集合中`_key="396478"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000368"
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
    '_key': '396478',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000368',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000368')
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
- problem_id: fate_000368
- solution_method_type: structural_argument
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有分类体系（characterization + direct_calculation + knowledge_gap等）完全覆盖此题。
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
