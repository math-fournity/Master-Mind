# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000357
- **文件路径**: subagents-dirs/fate_000357/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396467（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000357/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let A be a local Cohen-Macaulay (CM) ring that is a quotient of a regular local ring. If A is a UFD, then A is Gorenstein.
- 解答核心思路（1-2句话）：Lean证明为sorry（未证明）。数学证明重构：利用canonical module作为桥梁——A是正则局部环的商→canonical module ω_A存在且rank 1 reflexive；A是UFD→rank 1 reflexive模自由→ω_A≅A；ω_A≅A iff Gorenstein。
- 解答关键步骤列表：
  1. A是正则局部环B的商→A在B上有有限投射维数
  2. Auslander-Buchsbaum公式：pd_B(A) = dim(B) - dim(A)（因A是CM，depth_B(A)=dim(A)）
  3. 构造canonical module ω_A = Ext^{pd_B(A)}_B(A, B)，它是rank 1 reflexive A-模
  4. A是UFD→每个rank 1 reflexive模自由→ω_A ≅ A
  5. ω_A ≅ A iff A是Gorenstein→结论

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
| 1 | 纯元认知观察 | 0.8 | Describe the hypotheses and conclusion. What properties does A have, and what do you need to show? What seems to be the gap? | A is local CM, domain, UFD, quotient of regular local ring B. Need to show Gorenstein. Gap: UFD and Gorenstein seem unrelated. |
| 2 | 自由列举 | 0.7 | List all approaches to prove a ring is Gorenstein. Consider direct (inj. dim) and indirect (canonical module, duality). | (1) directly show finite inj. dim, (2) canonical module criterion ω_A≅A, (3) local duality, (4) CM + type 1 = Gorenstein |
| 3 | 小尝试 | 0.5 | Try proving A is Gorenstein directly from definition (finite inj. dim). Where do you get stuck? | Need inj.dim_A(A)<∞. CM gives depth=dim but not finite inj. dim. UFD doesn't help directly. Stuck. |
| 4 | 思维操作引导 | 0.4 | What does UFD tell you about modules over A? Think about rank 1 modules and reflexivity. | Over a UFD, every rank 1 reflexive module is free (≅A). Rank 1 reflexive ↔ divisorial ideals, UFD → all divisorial ideals principal. |
| 5 | 推进 | 0.5 | If rank 1 reflexive modules over a UFD are free, what module related to Gorenstein might be rank 1 reflexive? | The canonical module ω_A characterizes Gorenstein: A is Gorenstein iff ω_A≅A. If ω_A is rank 1 reflexive, UFD gives ω_A≅A. |
| 6 | 思维操作引导 | 0.3 | Since A is a quotient of regular local ring B, A has finite pd over B. Use Auslander-Buchsbaum to compute pd_B(A), construct ω_A=Ext^pd_B(A,B). | pd_B(A)+depth_B(A)=dim(B). A is CM→depth_B(A)=dim(A). So pd_B(A)=dim(B)-dim(A). ω_A=Ext^pd_B(A)_B(A,B) is rank 1 reflexive. |
| 7 | 能量传递引导 | 0.6 | Put it together: ω_A rank 1 reflexive (CM+quotient), UFD→free (≅A), ω_A≅A iff Gorenstein. Assemble! | (1) pd_B(A)=dim(B)-dim(A) by AB. (2) ω_A=Ext^pd_B(A)_B(A,B) rank 1 reflexive. (3) UFD→ω_A≅A. (4) ω_A≅A iff Gorenstein. QED. |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R4
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R5

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
- problem_type: structural_existence（证明结构性质成立，属于已有分类）
- structure_features: 蕴含链：CM + 正则局部环的商 + UFD → Gorenstein。证明需要通过模论中介（canonical module, rank 1 reflexive modules）桥接环论性质。每个假设贡献桥的不同部分。
- key_objects: local Cohen-Macaulay ring, regular local ring, UFD, Gorenstein ring, canonical module, rank 1 reflexive module, Auslander-Buchsbaum formula

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["property_transfer", "canonical_module_bridge", "reflexivity_argument", "chain_of_implications"]
- primary_pattern: canonical_module_bridge（用canonical module作为UFD和Gorenstein之间的桥梁）
- knowledge_required: ["Cohen-Macaulay rings", "regular local rings", "Gorenstein rings", "canonical module", "Auslander-Buchsbaum formula", "UFD and reflexive modules", "injective dimension", "projective dimension"]
- key_insight: UFD意味着每个rank 1 reflexive模都是自由的；CM环作为正则局部环的商，其canonical module是rank 1 reflexive；因此canonical module ≅ A，这等价于A是Gorenstein。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 环论性质（UFD, CM, 正则局部环的商）——从环的代数性质出发
- translation_to: 模论性质（rank 1 reflexive模, canonical module, 投射维数）——翻译到模论语言
- translation_type: property_to_module（将环论性质翻译为模论性质，通过模论中介完成证明）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: logical_deduction, gap_type: knowledge_gap}
- tell_small_concepts: ["canonical module", "rank 1 reflexive", "UFD", "Auslander-Buchsbaum", "injective dimension", "Gorenstein", "projective dimension"]
- expected_ai_method: 直接从定义出发的逻辑演绎——试图直接从CM+UFD性质证明有限内射维数，不使用canonical module中介
- correct_method: canonical module桥梁——通过Ext在正则局部环上构造canonical module，用CM证明rank 1 reflexive，用UFD得出自由，从而Gorenstein

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是，structural_existence/logical_deduction/knowledge_gap均可归入已有分类
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是，与已有值粒度一致
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 是，三个维度足够。不同轮次使用了不同的gap_type（knowledge_gap, method_problem_mismatch, structural_transformation, method_translation）来区分不同阶段的瓶颈
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化，现有拓扑分类体系足够

**拓扑进化建议**（如有）：无，现有分类体系足够覆盖此题。

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
- bare_ai_error_prediction: Bare AI会尝试直接从定义（有限内射维数）证明Gorenstein，然后卡住。它不会知道canonical module桥梁或UFD到reflexive模的翻译。没有canonical module构造（通过Ext在正则局部环上）的知识，这个证明基本上不可能完成。
- suitable_for_poc: ["tell_extraction", "hint_injection", "knowledge_bottleneck_detection"]
- discriminates_levels: true（此题需要深层的交换代数知识——canonical module理论、Auslander-Buchsbaum公式、UFD与reflexive模的关系——能有效区分AI的知识水平）

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
- [x] answer（"A is Gorenstein (IsGorensteinRing A)"）
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
- [x] tell_hint_pairs（7个局部pair，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（2个全局pair，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**将完整JSON写入工作目录的 `profile.json` 文件** → 已写入 subagents-dirs/fate_000357/profile.json

---

## Step 10: 入库ArangoDB [ ]

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="396467"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000357"
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
    '_key': '396467',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000357',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000357')
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
- problem_id: fate_000357
- solution_method_type: canonical_module_bridge
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，现有分类体系（structural_existence / logical_deduction / knowledge_gap等）足够覆盖此题
- 是否遇到异常: 否，Lean证明为sorry（未证明），数学证明已从标准交换代数结果重构

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
