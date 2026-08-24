# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000320
- **文件路径**: subagents-dirs/fate_000320/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396430（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000320/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let G be a finite group acting as automorphisms of an algebra R over a field of characteristic 0. Show that if R is Cohen-Macaulay, then the ring of invariants R^G is Cohen-Macaulay.
- 解答核心思路（1-2句话）：利用特征0条件定义Reynolds算子（平均映射），使R^G成为R作为R^G-模的直和项，然后应用直和项定理（Hochster-Roberts/Boutot）证明CM性质保持。
- 解答关键步骤列表：
  1. char(k)=0且G有限→|G|可逆→Reynolds算子ρ(r)=(1/|G|)Σg·r良定义
  2. ρ是R^G-线性的（a∈R^G被G固定）
  3. ρ|_{R^G}=id（r∈R^G时g·r=r）→R^G是R的直和项
  4. R在R^G上有限生成（有限群作用→整扩张）
  5. R是CM作为R^G-模
  6. 直和项定理：CM环的直和项是CM→R^G是CM
  - 注：Lean文件中proof为sorry（未填写），解答为数学重构

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
| 1 | 纯元认知观察 | 0.8 | 这道题的结构是什么？关键数学对象有哪些？特征0条件在这里可能扮演什么角色？ | 关键对象：R（CM环）、G（有限群）、R^G（不变量环）、k（特征0域）。特征0可能确保某些除法可行。 |
| 2 | 自由列举 | 0.7 | 从'R是CM'到'R^G是CM'，有哪些可能的证明路径？ | (1)直接计算depth/dim (2)利用模关系 (3)利用特征0定义平均算子 (4)同调方法 (5)利用有限生成性 |
| 3 | 小尝试 | 0.5 | 尝试直接计算R^G的depth和Krull dimension | 直接计算困难，素理想关系复杂，无法直接控制R^G的局部化结构 |
| 4 | 思维操作引导 | 0.4 | 定义平均映射ρ(r)=(1/\|G\|)Σg·r，证明R^G-线性且ρ\|_{R^G}=id | ρ是R^G-线性的，ρ\|_{R^G}=id，R^G是R的直和项 |
| 5 | 推进 | 0.6 | R^G是R的直和项，R是CM。什么定理联系直和项与CM？ | Hochster-Roberts/Boutot定理：CM环的直和项是CM |
| 6 | 思维操作引导 | 0.3 | 验证Reynolds算子的三个关键性质 | (1)char0→\|G\|可逆 (2)a∈R^G被G固定→R^G-线性 (3)r∈R^G时g·r=r→ρ\|_{R^G}=id |
| 7 | 能量传递引导 | 0.8 | 将所有要素串联，写出完整证明 | Reynolds算子→直和项→CM保持，五步完成证明 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 4.1
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
- structure_features: 有限群作用下的不变量环保持CM性质；特征0条件是关键enabler；需要从环论性质转换到模论论证；Reynolds算子提供分裂映射；直和项定理连接R与R^G的CM性
- key_objects: R（CM环）、G（有限群）、R^G（不变量环）、k（特征0域）、Reynolds算子ρ、直和结构R^G⊕M≅R

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [模论化归, 算子构造, 定理应用, 假设利用, 方法翻译]
- primary_pattern: 模论化归
- knowledge_required: [Cohen-Macaulay环定义与性质, 群作用与不变量环理论, Reynolds算子, 直和项定理(Hochster-Roberts/Boutot), 有限群作用下的整性扩张, depth与Krull dimension理论, 模的直和分解与分裂映射]
- key_insight: 特征0条件使|G|可逆，从而可以定义Reynolds算子（平均映射），它使R^G成为R作为R^G-模的直和项；然后直和项定理给出CM性质的保持。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接计算不变量环的depth和Krull dimension
- translation_to: 模论直和项论证（Reynolds算子 + 直和项定理）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: knowledge_gap}
- tell_small_concepts: [Reynolds operator, direct summand, characteristic 0, averaging map, Hochster-Roberts theorem, Boutot's theorem, Cohen-Macaulay preservation, invariant ring, finite group action]
- expected_ai_method: 直接计算R^G的depth和Krull dimension，试图通过素理想关系（lying over, going up）建立等式
- correct_method: 构造Reynolds算子使R^G成为R的直和项，应用直和项定理（Hochster-Roberts/Boutot）证明CM性质保持

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是，structural_existence/direct_calculation/knowledge_gap均可归入已有类别
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是，粒度一致
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够，无需新维度
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化

**拓扑进化建议**（如有）：无。已有拓扑分类（structural_existence, direct_calculation, knowledge_gap, method_translation, method_problem_mismatch等）完全够用。

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
- bare_ai_error_prediction: Bare AI会尝试直接计算R^G的depth和Krull dimension，通过素理想的lying-over和going-up关系试图建立depth = dimension的等式。这种方法在一般情况下极其困难。AI不太可能自发想到Reynolds算子和直和项定理这条路径，因为这是交换代数中的深层结果（Hochster-Roberts定理）。
- suitable_for_poc: [POC-VMS-knowledge-gap: 测试AI能否识别Reynolds算子知识瓶颈, POC-VMS-method-translation: 测试从直接计算到模论论证的路径转换, POC-VMS-hint-injection: 测试注入Reynolds算子提示后AI能否完成证明]
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
- [x] answer（**⚠️ 必填，不能为None**）
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

**将完整JSON写入工作目录的 `profile.json` 文件** → 已写入 `subagents-dirs/fate_000320/profile.json`

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
2. 更新`problem_extraction_progress`集合中`_key="396430"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000320"
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
    '_key': '396430',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000320',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000320')
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
