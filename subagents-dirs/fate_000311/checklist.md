# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000311
- **文件路径**: subagents-dirs/fate_000311/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396421（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000311/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设 φ:R→S 是光滑环映射，σ:S→R 是 φ 的左逆，I=Ker(σ)。若 I/I² 是自由 R-模，证明 S^∧ ≅ R[[t₁,...,t_d]] 作为 R-代数同构，其中 S^∧ 是 S 的 I-adic 完备化。
- 解答核心思路（1-2句话）：利用 σ 给出的分裂结构将 S 分解为 R⊕I，I/I² 的自由性给出变量个数 d，光滑性提供形式提升性质使完备化成为形式幂级数环。
- 解答关键步骤列表：
  1. 由 σ∘φ=id_R 得到分裂正合序列，S 作为 R-模同构于 R⊕I
  2. I/I² 自由秩 d 给出完备化的"维数"——d 个形式变量
  3. 光滑性 ⟹ 形式光滑 ⟹ 提升性质：I/I² 的生成元可提升为完备化中的形式坐标
  4. 组合三个要素得到 S^∧ ≅ R[[t₁,...,t_d]]

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
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：已知哪些对象？它们之间有什么关系？需要证明什么？ | 已知光滑环映射 φ:R→S，左逆 σ:S→R，I=Ker(σ)，I/I² 自由。需证 I-adic 完备化 S^∧ ≅ R[[t₁,...,t_d]]。关键对象：光滑映射、截面、核理想、余正规模、完备化。 |
| 2 | 自由列举 | 0.7 | 列出所有可能用来证明 S^∧ ≅ R[[t₁,...,t_d]] 的结构工具和方法方向。 | 可能方向：直接构造同态并验证同构；利用分裂结构 S≅R⊕I；利用 I/I² 的自由性确定变量个数；利用光滑性的形式提升性质；利用完备化的泛性质；利用形式光滑性定理。 |
| 3 | 小尝试 | 0.5 | 尝试直接构造 S^∧ → R[[t₁,...,t_d]] 的映射，看看需要什么额外信息。 | 直接构造困难：需要知道 d 是什么（I/I² 的秩），需要知道完备化中元素的坐标表示。直接构造缺少从 I/I² 到形式变量的桥梁。 |
| 4 | 思维操作引导 | 0.4 | σ 是 φ 的左逆意味着什么？这对 S 作为 R-模的结构有什么影响？ | σ∘φ=id_R 给出分裂正合序列 0→I→S→R→0，所以 S≅R⊕I 作为 R-模。I 是核理想，σ 是投影到 R 的分量。这是关键的结构分解。 |
| 5 | 推进 | 0.4 | 给定 S≅R⊕I 且 I/I² 自由秩 d，如何将 I/I² 的生成元与形式幂级数变量联系起来？ | I/I² 的 d 个自由生成元对应完备化中的 d 个形式坐标 t₁,...,t_d。I 的生成元在 I-adic 完备化中成为形式变量，I/I² 的自由性保证这些变量独立。 |
| 6 | 思维操作引导 | 0.3 | 光滑性在这里起什么作用？它如何保证完备化确实是形式幂级数环而非更一般的完备环？ | 光滑性 ⟹ 形式光滑：给定 R→R/I 的提升问题，光滑性保证存在（非唯一）提升。在完备化中，这意味着 I/I² 的生成元可提升为形式坐标，且完备化具有 R[[t₁,...,t_d]] 的泛性质。光滑性排除了"扭曲"项，保证完备化是纯幂级数环。 |
| 7 | 能量传递引导 | 0.2 | 现在把三个要素组合起来：分裂给出 R⊕I，I/I² 自由给出 d 个变量，光滑性给出形式幂级数结构。写出完整的证明结论。 | 由分裂 S≅R⊕I，I/I² 自由秩 d 给出 d 个形式变量，光滑性的形式提升性质保证 S 的 I-adic 完备化同构于 R[[t₁,...,t_d]] 作为 R-代数。QED。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.3
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

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
- structure_features: 光滑环映射+左逆截面+核理想的余正规自由性→完备化的形式幂级数结构。三个独立结构条件组合推出一个存在性同构结论。
- key_objects: ["光滑环映射 φ:R→S", "左逆截面 σ:S→R", "核理想 I=Ker(σ)", "余正规模 I/I²", "I-adic 完备化 S^∧", "形式幂级数环 R[[t₁,...,t_d]]"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["结构分解（分裂正合序列→模分解）", "维数识别（余正规自由性→变量个数）", "形式提升（光滑性→完备化结构）", "组合收敛（三要素合成结论）"]
- primary_pattern: 结构分解→形式提升→组合收敛
- knowledge_required: ["光滑环映射与形式光滑性", "分裂正合序列与模分解", "I-adic 完备化的泛性质", "余正规模 I/I² 与形式坐标的关系", "形式幂级数环的完备化结构定理"]
- key_insight: 光滑性不仅是正则性条件，它主动提供形式提升性质，使 I/I² 的生成元提升为完备化中的形式坐标，从而完备化成为纯幂级数环。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 模论语言（分裂正合序列、余正规模自由性）
- translation_to: 完备化代数语言（形式幂级数环、I-adic 完备化同构）
- translation_type: structural_transformation（从模结构到完备环结构的翻译）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_manipulation, gap_type: structural_transformation}
- tell_small_concepts: ["光滑环映射", "左逆截面", "分裂正合序列", "余正规模 I/I²", "I-adic 完备化", "形式幂级数环", "形式光滑性", "提升性质"]
- expected_ai_method: 直接构造同态并逐项验证同构（direct_manipulation），忽略分裂结构和光滑性的形式提升性质
- correct_method: 结构分解（分裂）+ 维数识别（I/I²自由）+ 形式提升（光滑性）三步组合，利用完备化泛性质得到同构

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能归入已有的拓扑类别？ 是。structural_existence + direct_manipulation + structural_transformation 均已有且粒度合适。
- [x] 粒度是否一致——标注的值和已有值的粒度是否统一？ 是。三个维度均为抽象级别。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ 足够。这道题的核心gap是"需要将三个独立结构条件翻译组合为完备化结构"，structural_transformation 准确描述。
- [x] 如果发现拓扑分类需要进化，在此写出建议： 无需进化。

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
- [ ] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？
- [ ] 粒度是否一致——你标注的值和已有值的粒度是否统一？
- [ ] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？
- [ ] 如果发现拓扑分类需要进化，在此写出建议：

**拓扑进化建议**（如有）：

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
- bare_ai_error_prediction: bare AI 会尝试直接构造完备化到幂级数环的映射，但不会利用 σ 的左逆性得到分裂结构，也不会将光滑性翻译为形式提升性质。缺少将三个独立条件（光滑、截面、余正规自由）组合为完备化结构定理的知识桥梁。
- suitable_for_poc: ["tell端形式化过滤POC（structural_existence拓扑）", "知识瓶颈POC（R4分裂结构识别）", "思维瓶颈POC（R6光滑性→形式提升翻译）"]
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
2. 更新`problem_extraction_progress`集合中`_key="396421"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000311"
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
    '_key': '396421',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000311',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000311')
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
- problem_id: fate_000311
- solution_method_type: structural_decomposition_and_formal_lifting
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。structural_existence + direct_manipulation + structural_transformation 均已有且粒度合适。
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
