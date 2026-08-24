# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000351
- **文件路径**: subagents-dirs/fate_000351/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396461（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000351/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let G be a finite group acting as automorphisms of an algebra R over a field of characteristic 0. Show that if R is Cohen-Macaulay, then the ring of invariants R^G is Cohen-Macaulay. （Lean中theorem为sorry，即未形式化证明的经典定理——Boutot/Hochster-Eagon定理）
- 解答核心思路（1-2句话）：利用char 0使|G|可逆，构造Reynolds算子ρ(r)=(1/|G|)Σg(r)得到R^G作为R^G-模是R的直和分量；再利用CM在有限扩张下传递+直和分量保持CM，完成证明。
- 解答关键步骤列表：
  1. 构造Reynolds算子：ρ: R → R^G, ρ(r) = (1/|G|)Σ_{g∈G} g(r)，char 0保证|G|可逆
  2. 证明ρ是R^G-线性映射且ρ∘i = id（i: R^G → R为包含映射），故R^G是R作为R^G-模的直和分量
  3. 证明R在R^G上是有限的（每个r满足∏(x-g(r))=0，系数在R^G中，R是Noetherian有限生成）
  4. CM在有限扩张下传递：R作为R-模是CM ⟹ R作为R^G-模是CM
  5. 直和分量保持CM：R^G是R(R^G-模)的直和分量 ⟹ R^G作为R^G-模是CM ⟹ R^G是CM环

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
| 1 | 纯元认知观察 | 0.8 | 描述题目结构：关键对象(G, R, R^G, k)是什么？需要从R传递到R^G的是什么性质？ | 有限群G作用在char 0域k上的CM Noetherian代数R上，需证不变子环R^G也是CM。关键对象：G(有限群)、R(CM环)、R^G(不变子环)、k(char 0域)。传递的性质是Cohen-Macaulay条件(depth=Krull维数，在所有局部化处成立)。 |
| 2 | 自由列举 | 0.7 | 列出所有可能的方法将群作用与R^G的环论性质联系起来。char 0启用了哪些工具？ | (1)群上平均(Reynolds算子)——char 0使|G|可逆；(2)整性论证——R在R^G上整(每个r满足∏(x-g(r))=0)；(3)模分裂——若R作为R^G-模可分裂，直和分量继承性质；(4)有限扩张下depth/dimension传递；(5)直接计算R^G的depth和维数。 |
| 3 | 小尝试 | 0.5 | 尝试直接验证R^G的CM条件：在素理想p处局部化，计算depth和Krull维数。在哪里卡住？ | 局部化R^G_p后需证depth(R^G_p)=dim(R^G_p)。dim可通过going-up/down对有限扩张R^G⊂R计算。但depth(R^G_p)直接计算非常困难——没有R^G_p和R_p之间的结构关系来构造正则序列。直接方法失败因为没有分裂映射。 |
| 4 | 思维操作引导 | 0.3 | 构造Reynolds算子ρ: R → R^G, ρ(r)=(1/|G|)Σg(r)。char 0为什么使其良定义？证明ρ是R^G-线性且ρ∘i=id。 | char(k)=0且G有限⟹|G|是k中非零元故可逆，1/|G|存在。ρ(r)是G-不变的(任意h∈G置换求和)，故ρ(r)∈R^G。R^G-线性：对a∈R^G, ρ(ar)=a·ρ(r)因a被G固定。包含映射i: R^G→R满足ρ(i(a))=(1/|G|)Σg(a)=(1/|G|)·|G|·a=a。故ρ∘i=id，R^G是R作为R^G-模的直和分量。 |
| 5 | 思维操作引导 | 0.4 | Reynolds算子表明R^G是R作为R^G-模的直和分量。回忆定理：CM模的直和分量是CM。还需要什么才能完成证明？ | 直和分量定理：若M是S上CM模且N是M作为S-模的直和分量，则N是S上CM模。这里S=R^G, M=R, N=R^G。需要R作为R^G-模是CM(不仅仅是作为R-模)。由于R作为R-模是CM且R在R^G上有限，需要CM在有限扩张下传递的定理。 |
| 6 | 推进 | 0.5 | R在R^G上是有限的(G有限给出整性)。CM在有限扩张下传递。完成论证。 | R在R^G上有限：每个r∈R在R^G上整(满足∏(x-g(r))=0，系数在R^G中)，R作为k-代数有限生成(Noetherian)，故R作为R^G-模有限。R作为R-模CM + R在R^G上有限 ⟹ R作为R^G-模CM(CM在有限扩张下传递)。R^G是R(R^G-模)的直和分量(Reynolds算子) + 直和分量保持CM ⟹ R^G作为R^G-模CM ⟹ R^G是CM环。 |
| 7 | 能量传递引导 | 0.7 | 你已有所有要素：Reynolds算子→R^G是R的直和分量→R作为R^G-模CM(有限扩张传递)→R^G是CM(直和分量保持)。写出完整证明。 | 完整证明：(1)char(k)=0且G有限⟹|G|可逆。定义ρ:R→R^G, ρ(r)=(1/|G|)Σg(r)。R^G-线性且ρ∘i=id⟹R^G是R作为R^G-模的直和分量。(2)R在R^G上有限(整性+Noetherian)。(3)R作为R-模CM + 有限扩张⟹R作为R^G-模CM。(4)直和分量保持CM⟹R^G作为R^G-模CM。(5)故R^G是Cohen-Macaulay环。QED。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.9
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
- structure_features: 有限群作用在char 0域上Noetherian代数上；从R到不变子环R^G的性质传递；关键结构特征是char 0使得|G|可逆从而存在R^G-线性分裂(Reynolds算子)
- key_objects: ["有限群G", "代数R over field k", "不变子环R^G", "Reynolds算子", "Cohen-Macaulay性质", "直和分量"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["structural_decomposition", "transfer_reasoning", "algebraic_construction", "splitting_argument"]
- primary_pattern: transfer_reasoning
- knowledge_required: ["Cohen-Macaulay环与模", "有限群作用的Reynolds算子", "CM模的直和分量定理", "CM在有限扩张下传递", "有限群作用下环的整性"]
- key_insight: Reynolds算子(群上平均)使R^G成为R作为R^G-模的直和分量，而CM模的直和分量仍是CM——char 0是使这一切成立的关键。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: group_action_invariant_theory（群作用与不变量理论的语言）
- translation_to: module_theory_direct_summand（模论与直和分量的语言）
- translation_type: method_translation（将群作用问题翻译为模论中的直和分量问题）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "direct_manipulation", gap_type: "knowledge_gap"}
- tell_small_concepts: ["Reynolds_operator", "direct_summand", "CM_transfer", "char_zero_averaging", "finite_group_invariants"]
- expected_ai_method: 直接验证R^G的CM条件——在素理想处局部化并独立计算depth和Krull维数，不使用Reynolds算子和直和分量论证
- correct_method: Reynolds算子构造得到R^G-线性分裂，结合CM在有限扩张下传递定理和直和分量保持CM定理完成证明

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？是。structural_existence + direct_manipulation + knowledge_gap 均为已有值，且粒度匹配。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？是。均为抽象级别，不过于具体。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？是。三个维度足够——这道题的核心gap是知识gap(不知道Reynolds算子和直和分量定理)，不需要新维度。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。

**拓扑进化建议**（如有）：无。现有拓扑分类体系完全覆盖此题。

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

**局部pairs详情**：
- R1: tell=看到题目但不知从何入手; hint=描述结构; level=0.8; 纯元认知观察; topology=(structural_existence, direct_manipulation, knowledge_gap); concepts=[finite_group_action, Cohen-Macaulay, ring_of_invariants, characteristic_zero]
- R2: tell=已描述结构但未识别关键工具; hint=列举方法; level=0.7; 自由列举; topology=(structural_existence, enumeration_brute_force, knowledge_gap); concepts=[averaging_map, integrality, Reynolds_operator, direct_summand, depth_transfer]
- R3: tell=尝试直接计算depth失败; hint=试直接验证; level=0.5; 小尝试; topology=(structural_existence, direct_calculation, method_problem_mismatch); concepts=[localization, depth, Krull_dimension, prime_ideal, direct_computation]
- R4: tell=直接计算depth不可行缺结构关系; hint=构造Reynolds算子; level=0.3; 思维操作引导; knowledge_bottleneck=True; topology=(structural_existence, algebraic_identity, knowledge_gap); concepts=[Reynolds_operator, averaging, char_zero, group_order_invertible, R^G_linear_splitting]
- R5: tell=有Reynolds算子但未连接到CM; hint=直和分量定理; level=0.4; 思维操作引导; knowledge_bottleneck=True; topology=(structural_existence, logical_deduction, knowledge_gap); concepts=[direct_summand, module_splitting, CM_module, direct_summand_of_CM]
- R6: tell=知直和分量但需验证R作为R^G-模CM; hint=有限扩张传递; level=0.5; 推进; topology=(structural_existence, logical_deduction, knowledge_gap); concepts=[finite_extension, integral_extension, CM_transfer, depth_transfer, Noetherian_finite]
- R7: tell=所有要素齐备待组装; hint=组装完整证明; level=0.7; 能量传递引导; topology=(structural_existence, logical_deduction, method_translation); concepts=[proof_assembly, Reynolds_operator, direct_summand, CM_transfer, conclusion]

**全局pairs详情**：
- Global 1 (path_feature): tell=三步序列(Reynolds算子→直和分量→CM传递)无法从单步看出; hint=完整路径: char0→平均→分裂→CM保持; level=0.7; why_not_visible_locally=每步是独立知识片段，步骤间连接(char0使平均可行→平均给分裂→分裂保持CM)是全局路径特征
- Global 2 (implicit): tell=char 0作为假设其关键角色不显见; hint=char 0仅用一次但是证明的支点; level=0.6; observation_point=4; why_not_visible_locally=在构造Reynolds算子的局部步骤中char 0仅是良定义的技术条件，其作为使整个证明策略可行的唯一支点的角色从局部步骤不可见

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI会尝试直接验证R^G的CM条件——在素理想处局部化并独立计算depth和Krull维数，不识别Reynolds算子和直和分量论证的必要性。会在尝试关联R^G的depth与R的depth时卡住，因为没有分裂映射。不会识别char 0作为平均构造的关键使能条件。
- suitable_for_poc: ["tell_identification", "knowledge_bottleneck_detection", "hint_injection_effectiveness"]
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
2. 更新`problem_extraction_progress`集合中`_key="396461"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000351"
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
    '_key': '396461',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000351',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000351')
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
