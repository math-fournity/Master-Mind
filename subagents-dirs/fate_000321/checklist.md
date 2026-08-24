# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000321
- **文件路径**: subagents-dirs/fate_000321/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396431（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000321/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let R be a Noetherian ring. Let M be a Cohen-Macaulay module over R. Then M ⊗_R R[x_1,…,x_n] is a Cohen-Macaulay module over R[x_1,…,x_n]. Lean中定义了Module.IsCohenMacaulay（全局CM：在每个素理想局部化处depth=dim），MvPolynomial (Fin n) R即R[x_1,…,x_n]。
- 解答核心思路（1-2句话）：CM是局部性质，对S=R[x_1,…,x_n]的每个素理想P局部化后归结为M_p ⊗_{R_p} R_p[x_1,…,x_n]的CM性。多项式变量x_1,…,x_n构成正则序列，使depth和dimension同时增加n，保持depth=dim的等式。
- 解答关键步骤列表：
  1. CM是局部性质 → 只需在每个素理想P处验证
  2. 对S的素理想P，设p=P∩R，则(M⊗_R S)_P ≅ M_p ⊗_{R_p} S_P，S_P是R_p[x_1,…,x_n]的局部化
  3. M_p在R_p上CM（由假设）
  4. x_1,…,x_n在R_p[x_1,…,x_n]中构成M_p-正则序列（多项式变量是非零因子）
  5. 正则序列使depth增加n，多项式扩张使dimension增加n → depth=dim保持
  6. 局部化保持CM → (M⊗_R S)_P在S_P上CM
  7. 对所有P成立 → M⊗_R S在S上CM

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
| 1 | 纯元认知观察 | 0.3 | 描述这道题的结构：CM模的定义是什么（depth=dimension）？我们要证明什么操作保持CM性质？ | R是Noetherian环，M是R上的CM模（在每个素理想处depth=dim）。需要证明M⊗_R R[x_1,…,x_n]在R[x_1,…,x_n]上也是CM模。操作是多项式环扩张下的标量延拓。 |
| 2 | 自由列举 | 0.4 | 列出你所知道的所有证明CM性质的工具和方法 | 局部化（CM是局部性质）、正则序列、平坦基变换、维数/深度计算、Ext群、support分析、归纳法（对n归纳）… |
| 3 | 小尝试 | 0.3 | 尝试直接全局计算M⊗R[x]的depth和dimension，看看能否直接得到depth=dim | 直接全局计算困难：CM是局部性质，全局的depth和dimension不一定相等。需要对每个素理想分别验证，全局方法无法直接work。 |
| 4 | 思维操作引导 | 0.5 | 既然CM是局部性质，做局部化归约：对S=R[x]的素理想P，设p=P∩R，(M⊗_R S)_P同构于什么？ | (M⊗_R S)_P ≅ M_p ⊗_{R_p} S_P，其中S_P是R_p[x_1,…,x_n]在P对应素理想处的局部化。因此只需证M_p ⊗_{R_p} R_p[x_1,…,x_n]在R_p[x_1,…,x_n]上CM。 |
| 5 | 思维操作引导 | 0.6 | 现在需要证M_p ⊗ R_p[x_1,…,x_n]在R_p[x]上CM，已知M_p在R_p上CM。x_1,…,x_n在R_p[x]中有什么特殊性质？ | x_1,…,x_n是R_p[x_1,…,x_n]中的多项式变量（不定元），它们构成M_p⊗R_p[x]上的正则序列：每个x_i是M_p⊗R_p[x_1,…,x_{i-1}]/(x_1,…,x_{i-1})上的非零因子。 |
| 6 | 推进 | 0.5 | 验证：正则序列x_1,…,x_n使depth增加n，多项式扩张使dimension增加n。为什么两者增量相同？ | 正则序列长度n → depth增加n（每次添加一个正则元depth+1）。多项式环R_p[x_1,…,x_n]的维数=dim(R_p)+n → M_p⊗R_p[x]的support维数=dim(M_p)+n。因为M_p是CM（depth=dim），所以depth+n=dim+n，等式保持。 |
| 7 | 能量传递引导 | 0.7 | 把所有部分组装起来：局部化归约 + 正则序列论证 + 局部化保持CM。完成证明。 | 对S的每个素理想P：局部化→M_p⊗R_p[x]→正则序列使depth和dim同时+n→depth=dim保持→CM→局部化保持CM→(M⊗S)_P在S_P上CM→对所有P成立→M⊗S在S上CM。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.3
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
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
- problem_type: structural_existence（证明某个代数结构性质在操作下保持存在）
- structure_features: 给定Noetherian环R和CM模M，证明多项式环扩张M⊗_R R[x_1,…,x_n]保持CM性质。核心结构是"性质在环扩张下的保持"，需要局部化归约+正则序列论证。
- key_objects: ["Noetherian ring R", "Cohen-Macaulay module M", "polynomial ring R[x_1,...,x_n]", "tensor product M⊗_R R[x_1,...,x_n]", "prime ideals", "regular sequence x_1,...,x_n", "depth", "dimension"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["local_global_principle", "regular_sequence_argument", "dimension_depth_tracking", "structural_preservation"]
- primary_pattern: local_global_principle
- knowledge_required: ["Cohen-Macaulay modules (depth=dimension at each prime)", "regular sequences", "localization of modules and tensor products", "polynomial ring extensions", "depth and dimension theory", "tensor products of modules"]
- key_insight: 多项式变量x_1,…,x_n构成正则序列，使depth和dimension同时增加n，保持CM的depth=dim等式

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: global module property (全局模性质验证)
- translation_to: local prime-by-prime verification using regular sequences (逐素理想的局部验证+正则序列论证)
- translation_type: local_global_reduction

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: knowledge_gap}
- tell_small_concepts: ["Cohen-Macaulay", "polynomial ring extension", "regular sequence", "localization", "depth", "dimension"]
- expected_ai_method: bare AI会尝试直接从定义出发计算depth和dimension，或试图用Ext群直接验证，缺乏局部化归约和正则序列的洞察
- correct_method: 局部化归约到每个素理想 + 利用多项式变量构成正则序列使depth和dim同时增加n + 局部化保持CM

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ → 可以。structural_existence / direct_calculation / knowledge_gap 均已有。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ → 一致，都是抽象粒度。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ → 足够。这道题的核心gap是知识性的（正则序列保持CM），knowledge_gap能准确描述。
- [x] 如果发现拓扑分类需要进化，在此写出建议： → 无需进化。现有分类体系足够。

**拓扑进化建议**（如有）：无

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

**局部pair详情**：

| R | tell | hint | level | situation_type | kb | topology | small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到CM保持问题但未识别关键结构特征 | 描述CM定义(depth=dim)和多项式扩张操作 | 0.3 | 纯元认知观察 | false | (structural_existence, direct_calculation, method_problem_mismatch) | ["Cohen-Macaulay", "polynomial ring extension", "depth", "dimension"] |
| 2 | AI列举方法但未识别正则序列路线 | 列出所有CM证明工具：局部化、正则序列、平坦基变换… | 0.4 | 自由列举 | false | (structural_existence, enumeration_brute_force, search_space_estimation) | ["localization", "regular sequence", "flat base change", "dimension theory"] |
| 3 | AI尝试全局计算depth/dim，因CM是局部性质而卡住 | 尝试直接全局计算，发现CM是局部性质无法直接work | 0.3 | 小尝试 | false | (structural_existence, direct_calculation, method_problem_mismatch) | ["global depth", "global dimension", "local property"] |
| 4 | AI认识到需局部化但不知如何分解张量积局部化 | 局部化归约：(M⊗S)_P ≅ M_p⊗_{R_p} S_P | 0.5 | 思维操作引导 | true | (structural_existence, logical_deduction, knowledge_gap) | ["prime localization", "tensor product localization", "lying over"] |
| 5 | AI已归约到局部但不知为何M_p⊗R_p[x]是CM | x_1,…,x_n构成正则序列——多项式变量是非零因子 | 0.6 | 思维操作引导 | true | (structural_existence, logical_deduction, knowledge_gap) | ["regular sequence", "polynomial indeterminates", "non-zero-divisor", "depth increment"] |
| 6 | AI知道正则序列是关键但需验证depth和dim增量相同 | 验证：正则序列使depth+n，多项式扩张使dim+n，等式保持 | 0.5 | 推进 | false | (structural_existence, direct_calculation, structural_transformation) | ["depth increment", "dimension increment", "regular sequence length", "equality preservation"] |
| 7 | AI有所有拼图，需组装完整论证 | 组装：局部化归约+正则序列+局部化保持CM=完整证明 | 0.7 | 能量传递引导 | false | (structural_existence, logical_deduction, method_translation) | ["local reduction", "regular sequence argument", "localization preservation", "proof assembly"] |

**全局pair详情**：

1. (path_feature) scope=整个证明路径（全局→局部→正则序列→重组装）
   - tell: 证明需要非显然路径：全局→局部化归约→正则序列论证→重组装。任何单步都看不出这个路径。
   - hint: 证明策略是：在每个素理想处局部化，利用多项式变量构成正则序列（depth和dim同时+n），再局部化回去。
   - hint_level: 0.7
   - generalizability: high — 局部-全局+正则序列模式适用于许多CM保持定理
   - why_not_visible_locally: 完整路径（局部化→正则序列→重组装）是全局策略。在任何单步只能看到一个片段。先局部化、再用正则序列、最后重组装的决策是路径级特征，无法从任何单步推断。
   - topology: (structural_existence, direct_calculation, method_translation)
   - small_concepts: ["local-to-global", "regular sequence strategy", "proof path structure"]

2. (implicit) scope=多项式变量构成正则序列这一隐含事实, observation_point=R5
   - tell: 关键隐含事实是x_1,…,x_n对任何模都构成正则序列。题目未陈述但这是证明的关键。
   - hint: 多项式不定元是多项式环上任何模的非零因子——这正是它们构成正则序列并保持CM的原因。
   - hint_level: 0.6
   - generalizability: high — 多项式变量的正则序列性质是交换代数中的基本事实
   - why_not_visible_locally: 多项式变量构成正则序列是隐含的代数事实，在题目陈述和任何单步中都不可见。它是需要回忆的背景定理，不能从局部上下文推导。
   - topology: (structural_existence, direct_calculation, knowledge_gap)
   - small_concepts: ["regular sequence of indeterminates", "non-zero-divisor property", "polynomial ring structure"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接从Lean定义出发（Ext群、support、krullDim），试图直接计算或归纳，但缺乏局部化归约和正则序列的关键洞察。可能在Lean形式化层面陷入定义展开的泥潭，无法识别"多项式变量构成正则序列"这一核心数学事实。
- suitable_for_poc: ["POC-VMS-tell-detection: 测试系统能否从AI的thinking中识别出'未走正则序列路线'的tell", "POC-VMS-hint-injection: 测试注入'局部化+正则序列'方向Q后AI能否完成证明", "POC-VMS-knowledge-bottleneck: 测试knowledge_gap类tell的识别和翻译"]
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
2. 更新`problem_extraction_progress`集合中`_key="396431"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000321"
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
    '_key': '396431',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000321',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000321')
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
- problem_id: fate_000321
- solution_method_type: local_reduction_and_regular_sequence
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，现有分类体系足够
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
