# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000340
- **文件路径**: subagents-dirs/fate_000340/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396450（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000340/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设 k 是域，A := k[x,y]/(xy(x+y-1))，证明 Pic(A) ≅ k×（Picard群同构于k的乘法群）。
- 解答核心思路（1-2句话）：A是三条直线x=0, y=0, x+y=1构成的三角形的坐标环。利用Picard群的粘贴正合序列，每条线Pic=0，三个交点给出(k×)³粘贴数据，全局单位给出(k×)²子群，商即k×。
- 解答关键步骤列表：
  1. 因式分解xy(x+y-1)=0，识别Spec(A)为三条仿射直线的并（三角形，顶点(0,0),(0,1),(1,0)）
  2. 每条直线≅A¹_k，Pic(A¹)=0（因k[t]是PID，所有可逆模自由）
  3. 应用Picard群的粘贴正合序列（Mayer-Vietoris型）：0→O_X*→⊕O_{X_i}*→⊕_{p∈X_i∩X_j}k*→Pic(X)→⊕Pic(X_i)→0
  4. 计算粘贴映射：(u₁,u₂,u₃)→(u₁/u₂, u₁/u₃, u₂/u₃)，像满足关系(u₁/u₂)·(u₂/u₃)=u₁/u₃，是2维子环面
  5. 商群(k×)³/(k×)²≅k×，故Pic(A)≅k×

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
| 1 | 纯元认知观察 | 0.8 | 观察这道题的结构：A是什么？Pic(A)是什么？我们要证明什么？ | A=k[x,y]/(xy(x+y-1))是多项式环的商环。Pic(A)是A的可逆模类构成的群（Picard群）。需要证明Pic(A)≅k×，即Picard群同构于域k的乘法群。 |
| 2 | 自由列举 | 0.7 | 列出所有可能计算Picard群的方法。 | 直接分类可逆模；用K-理论；用几何解释（坐标环→代数簇）；用局部化；用Mayer-Vietoris正合序列；用中国剩余定理分解环…… |
| 3 | 小尝试 | 0.5 | 试着直接分类A上的可逆模，看看会怎样。 | A=k[x,y]/(xy(x+y-1))有零因子（xy=0但x,y≠0），不是PID不是UFD，直接分类可逆模非常困难。代数方法在此受阻。 |
| 4 | 思维操作引导 | 0.4 | 因式分解xy(x+y-1)，然后思考Spec(A)对应什么几何对象？ | xy(x+y-1)=0定义三条直线：x=0, y=0, x+y=1。Spec(A)是A²中三条仿射直线的并，构成三角形，顶点在(0,0),(0,1),(1,0)。 |
| 5 | 思维操作引导 | 0.3 | 对于横截相交的曲线并，有什么正合序列可以计算Picard群？ | 有粘贴正合序列：0→O_X*→⊕O_{X_i}*→⊕_{p∈X_i∩X_j}k*→Pic(X)→⊕Pic(X_i)→0。每条线≅A¹的Pic=0，所以Pic(X)≅(k×)³/im(⊕k*→⊕k*)。 |
| 6 | 推进 | 0.4 | 计算粘贴映射(k×)³→(k×)³的具体表达式，它的像是什么？商群是什么？ | 映射(u₁,u₂,u₃)→(u₁/u₂, u₁/u₃, u₂/u₃)在三个交点处取比值。像满足(u₁/u₂)·(u₂/u₃)=u₁/u₃，是2维子环面。商群(k×)³/(k×)²≅k×。 |
| 7 | 能量传递引导 | 0.6 | 得出结论：Pic(A)是什么？ | Pic(A)≅k×。三条直线构成三角形的坐标环，其Picard群恰好同构于基域的乘法群。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.7
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R5
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R4

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
- problem_type: characterization
- structure_features: 商环k[x,y]/(xy(x+y-1))的Picard群计算。多项式xy(x+y-1)是三个线性因子的乘积，对应三条仿射直线的并。问题是刻画一个代数不变量（Picard群）的结构。
- key_objects: ["域k", "商环A=k[x,y]/(xy(x+y-1))", "Picard群Pic(A)", "乘法群k×", "三条仿射直线", "粘贴正合序列", "交点(0,0),(0,1),(1,0)"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["algebra_geometry_translation", "decomposition_gluing", "exact_sequence_computation", "counting_dimension_argument"]
- primary_pattern: algebra_geometry_translation
- knowledge_required: ["Picard群定义（可逆模的同构类）", "坐标环与代数簇的对应", "仿射直线的Picard群平凡（k[t]是PID）", "Picard群的粘贴正合序列（Mayer-Vietoris型）", "横截相交曲线并的Picard群计算"]
- key_insight: A=k[x,y]/(xy(x+y-1))是三条直线构成三角形的坐标环，粘贴正合序列将Pic(A)归结为(k×)³/(k×)²≅k×

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 交换代数/环论语言（商环、可逆模分类）
- translation_to: 代数几何语言（三条直线的并、粘贴正合序列、交点处的gluing data）
- translation_type: algebra_to_geometry

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: ["Picard群", "商环", "三条直线", "粘贴正合序列", "三角形", "k×", "可逆模", "gluing data"]
- expected_ai_method: bare AI会尝试直接在环论层面分类可逆模或用中国剩余定理朴素分解，不识别几何结构
- correct_method: 因式分解识别三条直线→用粘贴正合序列→计算gluing data的商→得k×

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？可以。characterization + direct_calculation + structural_transformation均已有且粒度合适。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？一致，均为中等抽象粒度。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？足够。这道题的核心gap是"从代数到几何的结构转换"，structural_transformation准确描述。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。现有分类体系覆盖良好。

**拓扑进化建议**（如有）：无。现有拓扑分类体系（characterization, direct_calculation, structural_transformation）完全适用。

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
- bare_ai_error_prediction: bare AI会在环论层面打转——尝试直接分类可逆模、用中国剩余定理朴素分解环，但不识别xy(x+y-1)对应三条直线的几何结构，也不知道粘贴正合序列这一关键工具。即使识别了几何结构，也难以正确计算gluing map的像和商群。
- suitable_for_poc: ["tell_identification", "knowledge_bottleneck_detection", "algebra_geometry_translation"]
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
- [x] answer（**⚠️ 必填，不能为None**。proof类型填要证明的结论，如"sum >= ..."；existence_construction类型填构造的存在性结论；numerical类型填数值答案）
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
2. 更新`problem_extraction_progress`集合中`_key="396450"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000340"
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
    '_key': '396450',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000340',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000340')
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
- problem_id: fate_000340
- solution_method_type: structural_transformation
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有分类体系（characterization, direct_calculation, structural_transformation）完全适用。
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
