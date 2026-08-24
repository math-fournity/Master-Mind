# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2015p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2015P6.lean
- **来源**: IMO 2015 P6
- **ArangoDB progress记录_key**: 329235（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2015P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：整数序列a_1, a_2, ...满足：(1) 1≤a_j≤2015对所有j≥1；(2) k+a_k≠l+a_l对所有1≤k<l。证明存在正整数b和N，使得|∑_{j=m+1}^{n}(a_j-b)|≤1007²对所有N≤m<n成立。
- 解答核心思路（1-2句话）：将序列翻译为抛接球(juggling)物理模型——a_j是时刻j抛球的高度，j+a_j是落地时间，条件2意味着没有两球同时落地。球数单调递增且有界，稳定后取b=最大球数、N=稳定时刻，利用高度和的望远镜求和将问题归结为|S_n-S_m|的界。
- 解答关键步骤列表：
  1. 构造pool(t)：时刻t空中球的高度集合，每步移除高度0的球、加入高度a_t的球、所有球高度减1
  2. 条件1保证高度在[0,2014]内，条件2保证同一时刻高度互异
  3. pool基数单调不减且有界→存在最大值b和稳定时刻N
  4. t≥N时pool恒有b个球→必有高度0的球→S_{t+1}=S_t+a_{t+1}-b
  5. 望远镜求和：∑(a_j-b)=S_n-S_m
  6. S_t在∑_{i=0}^{b-1}i和∑_{i=0}^{b-2}(2014-i)之间→|S_n-S_m|≤(b-1)(2015-b)≤1007²

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
| 1 | 纯元认知观察 | 0.3 | 观察这道题的结构：序列{a_j}满足(1)1≤a_j≤2015，(2)k+a_k互不相同。需证存在b,N使|∑(a_j-b)|≤1007²。描述两个条件各自给出什么信息？ | 条件1给值域约束，条件2给结构约束(j→j+a_j单射)。目标是存在性命题：找常数b和起始点N使部分和有界。 |
| 2 | 自由列举 | 0.5 | 列出所有可能方法，不要筛选。 | 直接分析部分和；利用单射性推导密度约束；生成函数；Erdős-Szekeres论证；抽屉原理；翻译到其他结构；物理/组合模型；归纳法。 |
| 3 | 小尝试 | 0.3 | 试试直接分析部分和∑(a_j-b)。利用k+a_k单射性能直接bound部分和吗？ | k+a_k单射→不同整数，落在一个宽度2015的滑动窗口中。有密度约束但不能直接bound部分和，a_j可在[1,2015]自由变化。直接方法走不通。 |
| 4 | 思维操作引导 | 0.2 | 关键操作：将序列翻译为物理模型。a_j是时刻j抛球高度，j+a_j是什么？条件2物理含义？ | j+a_j是球落地时刻。条件2=没有两球同时落地=合法抛接球(juggling)模式。 |
| 5 | 推进 | 0.4 | 发展抛接球模型。时刻t空中有多少球？随时间如何变化？能无限增长吗？ | pool(t)是空中球高度集合。每步移除0号球、加入a_t、全部减1。球数单调不减（有0号球不变，没有则加1），被2015 bound→稳定在最大值b，稳定时刻N。 |
| 6 | 思维操作引导 | 0.3 | 利用稳定状态。t≥N后pool恒有b个球意味着什么？设S_t为高度之和，计算S_{t+1}-S_t。 | 必有高度0的球（否则球数增加）。S_{t+1}=(S_t-0+a_{t+1})-b=S_t+a_{t+1}-b。望远镜求和：∑(a_j-b)=S_n-S_m。 |
| 7 | 能量传递引导 | 0.6 | 最后bound |S_n-S_m|。b个不同高度在[0,2014]内且含0，S_t的min和max？上界？ | min=∑_{i=0}^{b-1}i，max=∑_{i=0}^{b-2}(2014-i)。|S_n-S_m|≤(b-1)(2015-b)≤(2014/2)²=1007²。证毕！ |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 2.6
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
- problem_type: discrete_combinatorial
- structure_features: 整数序列满足值域约束+单射约束，需证存在性命题（存在b,N使部分和有界）。核心结构是条件2的单射性可翻译为物理模型。
- key_objects: ["整数序列{a_j}", "单射映射j→j+a_j", "部分和∑(a_j-b)", "抛接球pool(t)", "球高度之和S_t"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["physical_modeling", "monotone_bounded_stabilization", "telescoping_sum", "extremal_bound"]
- primary_pattern: physical_modeling
- knowledge_required: ["injective_functions", "monotone_bounded_sequences", "telescoping_sums", "AM-GM_inequality", "finset_operations"]
- key_insight: 将序列条件翻译为抛接球(juggling)物理模型——a_j是抛球高度，j+a_j是落地时间，injectivity意味着没有两球同时落地，从而pool基数单调有界稳定后给出b和N

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: sequence_analysis（序列分析语言：值域约束+单射约束+部分和有界）
- translation_to: physical_juggling_model（抛接球物理模型：球高度集合pool(t)、球数稳定、高度和望远镜求和）
- translation_type: structural_physical_modeling（将抽象序列条件翻译为具体物理过程，通过物理模型的结构性质推导目标不等式）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: discrete_combinatorial, ai_method_type: direct_calculation, gap_type: method_translation}
- tell_small_concepts: ["juggling_model", "injective_landing_time", "pool_stabilization", "telescoping_sum", "extremal_bound"]
- expected_ai_method: bare AI会尝试直接分析部分和，利用单射性推导密度约束，或做case analysis，但不会发现抛接球物理模型翻译
- correct_method: 抛接球物理模型——将序列翻译为球的抛接过程，利用pool基数单调有界稳定得到b和N，通过高度和望远镜求和将部分和归结为|S_n-S_m|的界

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 能。discrete_combinatorial、direct_calculation、method_translation均已存在且粒度合适。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 一致。三个维度都用了已有的抽象级值。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。这道题的核心gap是方法翻译（从序列分析到物理模型），method_translation准确描述了这个gap。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。现有拓扑分类体系能很好覆盖这道题。

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
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 1 个，implicit型: 2 个

**局部pairs详情**：
- R1: tell=AI看到值域约束+单射约束+部分和有界目标，但未识别结构 | hint=描述两个条件各自给出什么信息 | level=0.3 | 纯元认知观察 | kb=false | topo=(discrete_combinatorial, direct_calculation, method_problem_mismatch) | concepts=[bounded_sequence, injective_condition, partial_sum_bound]
- R2: tell=AI列出多种方法但未识别物理模型方向 | hint=列出所有可能方法 | level=0.5 | 自由列举 | kb=false | topo=(discrete_combinatorial, enumeration_brute_force, search_space_estimation) | concepts=[injective_mapping, physical_interpretation, juggling_model]
- R3: tell=AI尝试直接分析部分和，发现单射性只给密度约束不能bound部分和 | hint=试试直接分析 | level=0.3 | 小尝试 | kb=false | topo=(discrete_combinatorial, direct_calculation, method_problem_mismatch) | concepts=[direct_sum_analysis, structural_condition, value_bound]
- R4: tell=AI未考虑将序列翻译为物理模型 | hint=将a_j翻译为抛球高度，j+a_j为落地时间 | level=0.2 | 思维操作引导 | kb=true | topo=(discrete_combinatorial, direct_calculation, knowledge_gap) | concepts=[juggling_model, ball_height, landing_time, physical_translation]
- R5: tell=AI有抛接球模型但需发展pool概念和稳定性 | hint=发展模型，追踪球数变化 | level=0.4 | 推进 | kb=false | topo=(structural_existence, logical_deduction, structural_transformation) | concepts=[pool_cardinality, monotone_bounded, stabilization, maximum_reached]
- R6: tell=AI有稳定pool但未连接到部分和 | hint=利用稳定状态，必有0号球，计算S_{t+1}-S_t | level=0.3 | 思维操作引导 | kb=false | topo=(structural_existence, direct_calculation, structural_transformation) | concepts=[height_sum, telescoping_sum, zero_height_ball, key_observation]
- R7: tell=AI有望远镜求和需bound |S_n-S_m| | hint=bound S_t的极值，AM-GM | level=0.6 | 能量传递引导 | kb=false | topo=(inequality_proof, algebraic_identity, method_translation) | concepts=[height_bound, sum_extremal, AM_GM_bound, 1007_squared]

**全局pairs详情**：
- G1 (path_feature): tell=完整解答路径需要将抽象序列翻译为物理抛接球模型 | hint=juggling模型翻译是关键桥梁 | level=0.7 | generalizability=high | why_not_visible_locally=抛接球模型是全局翻译，无法从任何单一局部步骤推导。每个局部步骤（值域约束、单射性、部分和有界）单独看都有意义，但它们之间的联系需要物理模型的全局洞察。没有任何局部分析能揭示juggling解释。 | topo=(discrete_combinatorial, direct_calculation, method_translation) | concepts=[juggling_model, physical_translation, global_bridge, sequence_to_model]
- G2 (implicit, R5): tell=pool稳定同时定义了b和N，这个双重定义在稳定点不可见 | hint=最大pool基数同时给出b（值）和N（时刻） | level=0.5 | generalizability=medium | why_not_visible_locally=在pool稳定时(R5)，焦点在单调性和有界性论证上。这个单一事件同时定义b和N的隐含后果只有在后续需要两个参数用于部分和bound时才显现。稳定点的双重角色从局部步骤不可见。 | topo=(structural_existence, logical_deduction, structural_transformation) | concepts=[dual_parameter_extraction, stabilization_point, simultaneous_definition, extremal_event]
- G3 (implicit, R7): tell=1007²=(2015-1)/2²是(b-1)(2015-b)的最大值，由条件1的值域[1,2015]隐含决定 | hint=1007=(2015-1)/2来自AM-GM优化 | level=0.6 | generalizability=medium | why_not_visible_locally=在最终bound步骤(R7)，焦点在计算极值和之差。1007²恰好是(b-1)(2015-b)的最大值且在b=1008取到这一隐含联系需要识别二次优化。局部计算和差不会自动揭示bound的紧性或1007的来源。 | topo=(inequality_proof, algebraic_identity, method_translation) | concepts=[AM_GM_optimization, quadratic_maximum, constant_origin, tight_bound]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI会尝试直接分析部分和，利用k+a_k单射性推导密度约束，或做case analysis on a_j的值。不会发现将序列翻译为抛接球物理模型的关键洞察。可能尝试用Erdős-Szekeres或抽屉原理但无法建立从条件到部分和bound的桥梁。最终卡在"条件是结构性的，但目标是关于部分和的"这一gap上。
- suitable_for_poc: ["tell_extraction", "hint_injection", "method_translation_poc"]
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
2. 更新`problem_extraction_progress`集合中`_key="329235"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2015p6"
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
    '_key': '329235',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2015p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2015p6')
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
- problem_id: compfiles_imo2015p6
- solution_method_type: combinatorial_physical_model
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3 (1 path_feature + 2 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有分类体系(discrete_combinatorial / direct_calculation / method_translation等)充分覆盖这道题的拓扑特征。
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
