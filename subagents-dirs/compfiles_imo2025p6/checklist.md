# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2025p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2025P6.lean
- **来源**: IMO 2025 P6
- **ArangoDB progress记录_key**: 329284（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2025P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：2025×2025网格，放矩形瓷砖（每边在网格线上，每个单位格最多被一个瓷砖覆盖），使得每行每列恰好一个未覆盖格子。求最少瓷砖数。
- 解答核心思路（1-2句话）：未覆盖格子构成排列，用Erdős-Szekeres找到单调链u(长a)和v(长b)满足ab≥n，通过方向标签+incidence counting得瓷砖数≥n+a+b-3，AM-GM优化为n+√(4n)-3；模运算构造达到k²+2k-3。
- 解答关键步骤列表：
  1. 未覆盖格子构成排列（每行每列一个）
  2. Erdős-Szekeres：存在递增链u(长a)和递减链v(长b)，ab≥n
  3. 定义四方向区域(W/N/E/S)，给未覆盖格子打方向标签
  4. Incidence counting：pivot=4, u\\{pivot}每个=2, v\\{pivot}每个=2, 其他=1，总标签=n+a+b-3
  5. 每个瓷砖最多覆盖每种类型一个标签 → 瓷砖数≥标签数
  6. AM-GM：√(4n)≤a+b → 瓷砖数≥n+√(4n)-3
  7. 构造：模运算(val_s, val_t, 模k²+1)，非角点对(s,t)定义瓷砖，数=(k+1)²-4=k²+2k-3
  8. n=2025=45² → 答案=45²+90-3=2112

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
| 1 | 纯元认知观察 | 0.8 | 观察题目结构：2025×2025网格，放矩形瓷砖，每行每列恰好一个未覆盖格子。这些未覆盖的格子有什么特殊性质？ | n个未覆盖格子构成排列——每行恰好一个、每列恰好一个。可编码为函数f:行→列的置换。 |
| 2 | 自由列举 | 0.7 | 要找最少瓷砖数，有哪些可能的方向？特别地，关于排列有哪些经典定理可能相关？ | 直接构造、面积计数、图论模型、贪心。排列经典定理有Erdős-Szekeres、Dilworth等。 |
| 3 | 小尝试 | 0.5 | 试试直接面积计数：n²-n个格子要被覆盖，每个瓷砖最多覆盖多少？为什么太弱？ | 面积论证太弱，瓷砖可以很大。缺少结构信息——需利用排列的顺序性质。 |
| 4 | 思维操作引导 | 0.3 | 对排列f应用Erdős-Szekeres定理。设递增链u(长a)和递减链v(长b)，a和b有什么关系？ | Erdős-Szekeres：n≤a·b。u是递增链(x增则y增)，v是递减链(x增则y减)。 |
| 5 | 推进 | 0.4 | 有了链u和v，如何利用它们给瓷砖数找下界？提示：定义方向区域(W/N/E/S)，给每个未覆盖格子打标签。 | 定义四方向区域，每个未覆盖格子根据所在区域获得标签，标签指向相邻已覆盖格子。 |
| 6 | 思维操作引导 | 0.2 | 计算incidence count：pivot=4, u\\{pivot}每个=2, v\\{pivot}每个=2, 其他=1。标签总数？每个瓷砖最多覆盖几个标签？如何用AM-GM？ | 标签总数=n+a+b-3。每个瓷砖最多覆盖每种类型一个标签。AM-GM: √(4n)≤a+b, 得瓷砖数≥n+√(4n)-3。 |
| 7 | 能量传递引导 | 0.5 | 下界n+√(4n)-3已得。对n=2025=45²，下界=2112。构造达到此界的配置，验证答案。 | 模运算构造：val_s, val_t, 模k²+1。非角点对(s,t)定义瓷砖，数=(k+1)²-4=k²+2k-3=2112。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.4
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R4
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R5

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: discrete_combinatorial
- structure_features: n×n网格矩形瓷砖覆盖优化，未覆盖格子构成排列矩阵，下界用Erdős-Szekeres+标签计数+AM-GM，上界用模运算构造
- key_objects: n×n网格, 矩形瓷砖, 未覆盖格子(排列), 递增链u(长a), 递减链v(长b), 方向标签(W/N/E/S), incidence count, 模运算构造(val_s/val_t/模k²+1)

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
- problem_type:
- structure_features:
- key_objects:

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: [problem_reformulation_as_permutation, external_theorem_import_erdos_szekeres, double_counting_incidence, labeling_argument, am_gm_optimization, constructive_upper_bound_via_modular_arithmetic]
- primary_pattern: external_theorem_import_erdos_szekeres
- knowledge_required: [Erdős-Szekeres定理, AM-GM不等式, 排列矩阵, 双重计数/incidence counting, 模运算组合构造]
- key_insight: 未覆盖格子构成排列，应用Erdős-Szekeres得单调链(ab≥n)，标签/incidence counting论证将链结构转化为瓷砖下界n+a+b-3，AM-GM优化为n+√(4n)-3

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [列表]
- primary_pattern: （主导思维模式）
- knowledge_required: [前置知识列表]
- key_insight: （一句话关键转折点——"啊哈时刻"）

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: geometric_tiling_grid（几何瓷砖覆盖问题）
- translation_to: permutation_erdos_szekeres_labeling（排列+Erdős-Szekeres+标签计数）
- translation_type: domain_translation（跨领域翻译：从几何覆盖到组合序列论）

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: （从什么方法/语言翻译）
- translation_to: （翻译到什么方法/语言）
- translation_type: （翻译类型分类）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: discrete_combinatorial, ai_method_type: direct_calculation, gap_type: method_translation}
- tell_small_concepts: [permutation_of_uncovered_squares, erdos_szekeres_monotone_subsequence, directional_labeling, incidence_counting, am_gm_bound, modular_arithmetic_construction]
- expected_ai_method: direct_calculation（bare AI会尝试直接面积计数或贪心构造）
- correct_method: erdos_szekeres_labeling_amgm（实际需要Erdős-Szekeres+标签计数+AM-GM）

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=discrete_combinatorial, ai_method_type=direct_calculation, gap_type=method_translation均可归入已有拓扑类别
- [x] 粒度一致——标注值和已有值粒度统一
- [x] 三个维度足够区分——这道题的tell（跨领域翻译：tiling→permutation→Erdős-Szekeres）与已有tell可通过gap_type=method_translation区分
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。当前拓扑分类足够。

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: __, ai_method_type: __, gap_type: __}
- tell_small_concepts: [关键概念词列表]
- expected_ai_method: （bare AI预期会用的方法——可能走错的路）
- correct_method: （正确方法——解答实际用的方法）

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

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 2 个，implicit型: 1 个

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
- 局部tell_hint_pairs数量: __ 对
- 全局tell_hint_pairs数量: __ 对
- 全局pair中path_feature型: __ 个，implicit型: __ 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接面积计数或贪心构造，得到弱界。不会识别排列结构，不会想到Erdős-Szekeres，更不会发现标签/incidence counting论证。即使得到下界，模运算构造也极不显然。
- suitable_for_poc: [tell_detection_vms, hint_injection_vms, cross_domain_translation_vms, knowledge_bottleneck_identification]
- discriminates_levels: true

**产出**：
- bare_ai_expected: "pass" | "fail" | "marginal"
- bare_ai_error_prediction: （bare AI会犯什么错的具体描述）
- suitable_for_poc: [适合哪些POC实验]
- discriminates_levels: boolean

---

## Step 9: 输出完整profile JSON [x]

完整profile JSON已写入 `subagents-dirs/compfiles_imo2025p6/profile.json`。所有字段已检查：
- [x] _key=compfiles_imo2025p6
- [x] source_id, source_dataset, schema_version=3
- [x] problem_text, solution_text, solution_summary
- [x] domain=combinatorics, subfield=combinatorial_optimization
- [x] answer_type=numerical, answer=2112
- [x] problem_type, solution_method_type, structure_features, key_objects
- [x] thinking_patterns, primary_pattern, knowledge_required, key_insight
- [x] translation_from/to/type
- [x] tell_topology(profile级), tell_small_concepts(profile级)
- [x] expected_ai_method, correct_method
- [x] tell_hint_pairs(7个局部pair，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts)
- [x] global_tell_hint_pairs(3个全局pair，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts)
- [x] bare_ai_expected, bare_ai_error_prediction, suitable_for_poc, discriminates_levels
- [x] qa_sequence(含rounds数组和stats子对象，knowledge_bottleneck="R4", thinking_bottleneck="R5")
- [x] analysis_metadata

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
2. 更新`problem_extraction_progress`集合中`_key="329284"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2025p6"
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
    '_key': '329284',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2025p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2025p6')
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
- problem_id: compfiles_imo2025p6
- solution_method_type: erdos_szekeres_labeling_amgm
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3 (2个path_feature型, 1个implicit型)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。当前拓扑分类(discrete_combinatorial, direct_calculation, method_translation)足够覆盖此题。
- 是否遇到异常: 无。入库和验证均一次通过。

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
