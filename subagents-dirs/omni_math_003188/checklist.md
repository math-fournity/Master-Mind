# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003188
- **文件路径**: subagents-dirs/omni_math_003188/problem.lean
- **来源**: AoPS omni_math (putnam)
- **ArangoDB progress记录_key**: 333066（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003188/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：正二十面体的30条边标号1-30，每条边染红/白/蓝三色之一，要求20个三角面中每个面的三条边恰好两同色一异色。求不同的染色方式数。
- 解答核心思路（1-2句话）：将三种颜色对应到F_3的三个元素，"两同一异"条件等价于每个面的三边颜色之和非0 mod 3。定义线性映射L: F_3^E→F_3^F（边染色→面和向量），证明L满射（rank=20），则答案=|ker(L)|×|{1,2}^20|=3^10×2^20=61917364224。
- 解答关键步骤列表：
  1. 颜色→F_3元素：red/white/blue ↔ {0,1,2} mod 3
  2. 条件翻译："两同一异" ⟺ 面和≠0 mod 3（全同则3a=0，全异则0+1+2=0）
  3. 建立线性映射L: F_3^30→F_3^20，将边染色映射到各面边色之和
  4. 证明L满射：对偶映射L^T的核=0（正二十面体对偶图=正十二面体有奇圈/五边形面，迫使交替权重为0）
  5. 计数：|ker(L)|=3^(30-20)=3^10，合法染色=3^10×2^20=61917364224

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
| 1 | 纯元认知观察 | 0.8 | 观察这道题的结构：正二十面体有30条边、20个三角面，每条边染3色之一，要求每个面恰好两同色一异色。题目在问什么类型的数学问题？关键对象有哪些？ | 这是一个组合计数问题。关键对象：30条边、20个面、3种颜色、每面的约束条件。需要在所有满足逐面约束的染色中计数。 |
| 2 | 自由列举 | 0.7 | 对于这个组合计数问题，你能想到哪些可能的解题方向？ | 可能方向：1) Burnside引理/Polya计数考虑对称性；2) 直接递推/容斥原理；3) 将问题转化为代数问题；4) 图论方法；5) 利用正二十面体的特殊结构。 |
| 3 | 小尝试 | 0.4 | 试试用Burnside引理或直接容斥来处理。每条边3种选择共3^30种，需满足20个面约束。这个方向可行吗？ | 直接计数困难：3^30≈2×10^14太大。Burnside需要分析60阶对称群，但约束是逐面的不是全局的。容斥需处理2^20项交集。这个方向似乎走不通。 |
| 4 | 思维操作引导 | 0.3 | 关键思维操作：尝试将颜色与代数结构对应。三种颜色能否对应到某个3元代数结构的元素？特别是"两同一异"这个条件能否用代数运算表达？ | 将三种颜色对应到F_3={0,1,2}。对每个面的三边a,b,c：全同→a+b+c=3a=0(mod3)；全异→{0,1,2}→和=0(mod3)；两同一异→和≠0(mod3)。所以条件等价于面和≠0 mod 3！ |
| 5 | 推进 | 0.4 | 现在条件变成每个面的边色之和非0 mod 3。定义线性映射L: F_3^E→F_3^F将边染色映射到各面和。继续推进：如何用这个框架计数？ | L是线性映射，要求L(c)每个分量非零即L(c)∈{1,2}^20。若L满射(rank=20)，则|ker(L)|=3^10，且{1,2}^20中每个向量有3^10个原像。答案=3^10×2^20。关键是证明L满射。 |
| 6 | 思维操作引导 | 0.5 | 需要证明L满射即rank(L)=20。思维操作：考虑对偶映射L^T，证明其核为零。正二十面体的对偶图是什么？它有什么结构性质能帮助证明？ | 对偶映射L^T的核：面权重w使得每条边的两个邻面权重和=0 mod 3，即邻面权重比为1:2。正二十面体对偶=正十二面体，有五边形面（奇圈）。沿奇圈交替w,2w回到起点要求w=2w即w=0。所以L^T核=0，L满射。 |
| 7 | 能量传递引导 | 0.6 | 所有要素齐了：颜色→F_3，条件→面和≠0，L满射→3^10×2^20。完成最终计算。 | 答案=3^10×2^20=59049×1048576=61917364224。步骤回顾：1)颜色→F_3；2)两同一异→面和≠0；3)线性映射L:F_3^30→F_3^20；4)对偶图奇圈证明满射；5)计数=3^10×2^20。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5（R1纯元认知观察+R2自由列举+R3小尝试+R5推进+R7能量传递引导）
- knowledge_rounds（思维操作引导的轮数）: 2（R4+R6）
- level_sum: 0.8+0.7+0.4+0.3+0.4+0.5+0.6=3.7
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
- structure_features: 正二十面体（30边20面12顶点）的边3-染色，逐面约束（每个三角面两同色一异色），计数满足所有面约束的染色方案数
- key_objects: ["正二十面体（30边20面）", "3-染色（红白蓝）", "逐面约束（两同一异）", "F_3有限域", "线性映射L:F_3^E→F_3^F", "正十二面体（对偶图，奇圈）"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["algebraic_translation", "linear_algebra_over_finite_fields", "surjectivity_via_dual_injectivity", "counting_via_kernel_and_image", "odd_cycle_argument"]
- primary_pattern: algebraic_translation
- knowledge_required: ["F_3有限域结构", "有限域上线性代数", "rank-nullity定理", "正二十面体/正十二面体对偶关系", "面-边关联矩阵", "对偶映射与满射性"]
- key_insight: 将三种颜色对应到F_3的三个元素，使"两同一异"条件转化为"面和≠0 mod 3"的线性代数条件，从而用线性映射的核与像来计数

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: combinatorial_coloring（组合染色计数，逐面约束）
- translation_to: linear_algebra_over_F3（有限域F_3上的线性代数，核与像的计数）
- translation_type: method_translation（方法翻译：将组合条件翻译为线性代数条件）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "method_translation"}
- tell_small_concepts: ["F3_color_mapping", "face_sum_nonzero", "linear_map_surjectivity", "dodecahedron_odd_cycle", "kernel_image_counting"]
- expected_ai_method: bare AI会尝试Burnside引理/Polya计数或直接容斥原理，面对3^30的搜索空间和20个面约束的复杂交集，无法有效处理
- correct_method: 将颜色对应到F_3元素，条件翻译为面和≠0 mod 3，建立线性映射L:F_3^E→F_3^F，利用对偶图奇圈证明满射，用核与像计数得3^10×2^20

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type(discrete_combinatorial)/ai_method_type(enumeration_brute_force)/gap_type(method_translation)都能归入已有拓扑类别
- [x] 粒度是否一致——标注值和已有值粒度统一
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化，现有拓扑分类体系足够

**拓扑进化建议**（如有）：无，现有分类体系足够覆盖此题

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
- bare_ai_error_prediction: Bare AI会尝试Burnside引理或直接容斥原理，面对3^30的巨大搜索空间和20个面约束的复杂交集，无法有效处理。不会想到将颜色对应到F_3并使用有限域线性代数。即使想到代数化，也可能无法完成满射性证明（需要利用正十二面体对偶图的奇圈性质）。
- suitable_for_poc: ["hint_injection_effectiveness", "tell_identification_accuracy", "knowledge_bottleneck_detection", "method_translation_guidance"]
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

✅ profile.json已写入 subagents-dirs/omni_math_003188/profile.json

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
2. 更新`problem_extraction_progress`集合中`_key="333066"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_003188"
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
    '_key': '333066',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_003188',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_003188')
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
- problem_id: omni_math_003188
- solution_method_type: linear_algebra_over_finite_fields
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature + 1个implicit）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，现有分类体系足够覆盖
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
