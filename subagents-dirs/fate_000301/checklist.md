# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000301
- **文件路径**: subagents-dirs/fate_000301/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396411（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000301/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设R是交换环，m是R的Jacobson根中的理想，G₁,G₂∈R[x]且G₁是monic的。若G₁,G₂ mod m生成R/m[x]的单位理想，则G₁,G₂在R[x]中生成单位理想。
- 解答核心思路（1-2句话）：利用G₁ monic使M=R[x]/(G₁)成为有限自由R-模，将问题转化为模论，再用Nakayama引理将mod m的生成性提升到R上。
- 解答关键步骤列表：
  1. G₁ monic → M=R[x]/(G₁)是有限自由R-模（rank=deg G₁）
  2. 假设条件翻译为：G₂在M/mM中的像是unit
  3. m⊆Jac(R) + M有限生成 → Nakayama引理适用 → G₂生成M
  4. G₂生成M → ∃B: B·G₂≡1(mod G₁) → C·G₁+B·G₂=1

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
| 1 | 纯元认知观察 | 0.8 | 描述题目结构：已知什么，要证什么，哪个假设最restrictive？ | 识别monic条件和Jacobson根条件是最关键假设 |
| 2 | 自由列举 | 0.7 | 列出所有可能方向证明G₁,G₂生成单位理想 | 直接构造、Nakayama、局部化、Euclidean除法等 |
| 3 | 小尝试 | 0.5 | 尝试直接从mod m等式提升：A₁G₁+A₂G₂=1+H, H∈m[x]，能否直接用Jacobson根性质？ | 失败：H是m[x]中元素不是m中标量，Jacobson根单位性质不直接适用 |
| 4 | 思维操作引导 | 0.6 | G₁是monic的，这在R[x]中有什么特殊性质？ | monic→可做Euclidean除法→R[x]/(G₁)是有限自由R-模 |
| 5 | 思维操作引导 | 0.5 | 考虑M=R[x]/(G₁)是有限自由R-模，假设条件对G₂在M/mM中的像说了什么？ | G₂在M/mM中是unit，即生成M/mM |
| 6 | 推进 | 0.4 | M有限自由，m在Jacobson根中，G₂生成M/mM，什么定理适用？ | Nakayama引理→G₂生成M |
| 7 | 能量传递引导 | 0.3 | G₂生成M意味着∃B: B·G₂≡1(mod G₁)，写出完整证明 | C·G₁+B·G₂=1，完整证明链组装 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

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
- structure_features: 环论中的提升问题——从商环R/m到原环R[x]的提升，利用monic条件和Jacobson根条件
- key_objects: 交换环R, Jacobson根中的理想m, 多项式环R[x], monic多项式G₁, 有限自由R-模M=R[x]/(G₁), Nakayama引理

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["module_theoretic_reduction", "nakayama_lemma_application", "quotient_lifting", "finite_free_module_exploitation"]
- primary_pattern: module_theoretic_reduction——将多项式环中的理想生成问题转化为有限自由模上的生成问题
- knowledge_required: ["Nakayama引理", "Jacobson根的刻画", "monic多项式与有限自由模的关系", "多项式环的商环结构"]
- key_insight: G₁ monic使R[x]/(G₁)成为有限自由R-模，从而可以应用Nakayama引理将mod m的生成性提升到R上

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 多项式环中的理想生成问题（环论语言）
- translation_to: 有限自由模上的元素生成问题（模论语言+Nakayama引理）
- translation_type: structural_transformation——通过构造M=R[x]/(G₁)将问题从环论转化到模论

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_manipulation, gap_type: structural_transformation}
- tell_small_concepts: ["monic polynomial", "finite free module", "Nakayama's lemma", "Jacobson radical", "quotient lifting", "Euclidean division"]
- expected_ai_method: direct_manipulation——bare AI会尝试直接从mod m的等式出发构造，试图直接提升
- correct_method: 通过M=R[x]/(G₁)的模论转化，应用Nakayama引理

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——structural_existence/direct_manipulation/structural_transformation能归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell和已有tell
- [x] 不需要新的拓扑维度

**拓扑进化建议**：无。已有拓扑分类足够覆盖此题。

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
- bare_ai_error_prediction: bare AI会尝试直接从mod m的Bezout等式出发，得到A₁G₁+A₂G₂=1+H（H∈m[x]），然后试图用Jacobson根的单位性质证明1+H是unit。但H是多项式不是标量，Jacobson根性质（1+ay是unit）只对R中元素适用，不直接适用于m[x]中的多项式。AI在直接提升失败后不知道如何利用monic条件进行模论转化。
- suitable_for_poc: ["POC-VMS-tell-detection: 检测系统能否识别AI困在直接操作中而未看到模论转化路径", "POC-VMS-hint-injection: 测试关于monic→有限自由模→Nakayama的hint能否将AI从失败的直接方法中重定向", "POC-VMS-topology-matching: 测试structural_existence+direct_manipulation+structural_transformation拓扑是否正确匹配此题"]
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

**将完整JSON写入工作目录的 `profile.json` 文件** ✅ 已写入

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
2. 更新`problem_extraction_progress`集合中`_key="396411"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000301"
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
    '_key': '396411',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000301',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000301')
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
- problem_id: fate_000301
- solution_method_type: module_theoretic_reduction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类（structural_existence/direct_manipulation/structural_transformation/knowledge_gap）足够覆盖
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
