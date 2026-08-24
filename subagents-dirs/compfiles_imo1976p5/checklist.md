# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1976p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1976P5.lean
- **来源**: IMO 1976 P5
- **ArangoDB progress记录_key**: 329079（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1976P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：n为正整数，m=2n，a_{ij}∈{0,1,-1}，m个未知数x_1,...,x_m满足n个齐次线性方程。证明存在绝对值≤m的非零整数解。
- 解答核心思路（1-2句话）：用鸽巢原理——计算|x_j|≤n的候选元组数(2n+1)^{2n}和可能LHS值数(4n²+1)^n，前者大于后者，故两个不同元组有相同LHS，其差即为所求解。
- 解答关键步骤列表：
  1. 定义候选元组集合：每个x_j∈{-n,...,n}，共(2n+1)^{2n}个
  2. 计算LHS值范围：每个|Σa_{ij}x_j|≤2n²，共(4n²+1)^n个可能LHS向量
  3. 验证(2n+1)^{2n} > (4n²+1)^n（因为(2n+1)²=4n²+4n+1>4n²+1）
  4. 鸽巢原理：两个不同元组x,x'有相同LHS
  5. 取差y=x-x'：非零、|y_j|≤2n=m、满足齐次系统

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
| 1 | 纯元认知观察 | 0.3 | 描述题目结构：方程数vs未知数？系数约束？解的界意味着什么？ | n个方程，m=2n个未知数（未知数多于方程），系数∈{0,±1}，需要|y_j|≤2n的非零整数解，齐次系统 |
| 2 | 自由列举 | 0.5 | 列出所有可能方法：代数法、计数法、鸽巢原理、格论、Siegel引理... | 高斯消元、有理数域线性代数、鸽巢计数、Minkowski定理、Siegel引理、概率法 |
| 3 | 小尝试 | 0.4 | 试高斯消元，能否控制解的界？ | 消元给出参数化解但entry可能很大，|x_j|≤2n的界难以保证，直接代数法无法控制解大小 |
| 4 | 思维操作引导 | 0.6 | 不直接解，改为计数：|x_j|≤n的元组有多少？LHS向量可能取多少值？ | 元组数(2n+1)^{2n}；每个|LHS_i|≤2n²故(4n²+1)^n个可能LHS向量 |
| 5 | 推进 | 0.5 | 比较(2n+1)^{2n}和(4n²+1)^n，哪个大？意味着什么？ | (2n+1)^{2n}=((2n+1)²)^n=(4n²+4n+1)^n>(4n²+1)^n，元组多于LHS值，鸽巢原理保证两个不同元组有相同LHS |
| 6 | 推进 | 0.5 | 两个不同元组x,x'有相同LHS，x-x'满足什么？ | y=x-x'满足系统（线性性）、非零（x≠x'）、|y_j|≤2n（三角不等式） |
| 7 | 能量传递引导 | 0.7 | 验证三个条件：非零、有界、满足系统。完成！ | y≠0、|y_j|≤2n=m、Σa_{ij}y_j=0，证明完成 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5
- knowledge_rounds（思维操作引导的轮数）: 1
- level_sum: 3.5
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: null
- thinking_bottleneck（思维瓶颈在哪轮，或null）: 4

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
- structure_features: 齐次线性系统，n个方程m=2n个未知数，系数∈{0,±1}，要求|y_j|≤2n的非零整数解；m=2n的参数选择精确校准使鸽巢不等式成立
- key_objects: 系数矩阵a(n×2n, 元素∈{0,±1})、整数解向量x(长度2n)、候选元组集合(|x_j|≤n)、LHS值集合(|Σ|≤2n²)、鸽巢原理

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["pigeonhole_principle", "counting_argument", "bounded_search", "difference_trick"]
- primary_pattern: pigeonhole_principle
- knowledge_required: ["pigeonhole_principle", "linear_algebra_basics", "integer_bounds", "counting_finite_sets", "triangle_inequality"]
- key_insight: 计数有界候选元组(2n+1)^{2n}和可能LHS值(4n²+1)^n，前者大于后者，鸽巢原理给出两个相同LHS的元组，其差即为所求非零有界解

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: algebraic_equation_solving（直接代数求解线性系统）
- translation_to: combinatorial_counting（组合计数+鸽巢原理）
- translation_type: method_translation（方法翻译：从代数到组合）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: equation_solving, gap_type: method_translation}
- tell_small_concepts: ["pigeonhole", "bounded_integer_tuple", "lhs_value_count", "difference_of_tuples", "nontrivial_solution"]
- expected_ai_method: 直接用高斯消元或有理数域线性代数求解，得到解但无法控制绝对值的界
- correct_method: 计数有界候选元组和可能LHS值，用鸽巢原理找到两个相同LHS的元组，取差作为解

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是，structural_existence/equation_solving/method_translation均可归入已有类别
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是，与已有值粒度一致
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够，无需新维度
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化

**拓扑进化建议**（如有）：无。现有拓扑分类完全够用。

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
- `why_not_visible_locally`: 蕴含型专用——为什么在局部不可见
- `tell_topology`: object（**⚠️ 每个全局pair也要有**）
- `tell_small_concepts`: array[string]（**⚠️ 每个全局pair也要有**）

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**每轮pair拓扑标注（逐pair不同）**：
- R1: (structural_existence, direct_calculation, structural_transformation)
- R2: (structural_existence, enumeration_brute_force, search_space_estimation)
- R3: (structural_existence, equation_solving, method_problem_mismatch)
- R4: (structural_existence, enumeration_brute_force, knowledge_gap) ← knowledge_bottleneck
- R5: (structural_existence, direct_calculation, structural_transformation)
- R6: (structural_existence, logical_deduction, method_translation)
- R7: (structural_existence, logical_deduction, method_problem_mismatch)
- Global1(path_feature): (structural_existence, equation_solving, method_translation)
- Global2(implicit): (structural_existence, direct_calculation, structural_transformation)

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: AI会用高斯消元或有理数域线性代数求解，得到有理解但无法控制整数解的绝对值界。鸽巢计数法不直观，因为题目以线性代数形式呈现而非组合形式。
- suitable_for_poc: ["tell_hint_injection", "method_translation_poc", "pigeonhole_recognition"]
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
- [x] tell_hint_pairs（每个pair含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（每个pair含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

→ profile.json已写入 `subagents-dirs/compfiles_imo1976p5/profile.json`

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
2. 更新`problem_extraction_progress`集合中`_key="329079"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1976p5"
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
    '_key': '329079',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1976p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1976p5')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证输出: compfiles_imo1976p5, 7 local pairs, 2 global pairs

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_imo1976p5
- solution_method_type: pigeonhole_counting
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature + 1个implicit）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，现有拓扑分类（structural_existence / equation_solving / method_translation等）完全够用
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
