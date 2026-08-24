# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000253
- **文件路径**: subagents-dirs/fate_000253/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396363（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000253/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let p be an odd prime, G a finite group of order p(p+1). Assume G does not have a normal Sylow p-subgroup. Prove that p+1 is a power of 2.
- 解答核心思路（1-2句话）：Sylow counting gives n_p=p+1; Burnside's normal p-complement theorem yields normal subgroup N of order p+1; faithful conjugation action forces all non-identity elements to have same prime order d; if d odd then p=d^a-1 is composite, contradiction; hence d=2 and p+1=2^n.
- 解答关键步骤列表：
  1. Sylow counting: n_p | (p+1), n_p ≡ 1 (mod p), n_p > 1 → n_p = p+1
  2. |N_G(P)| = |G|/n_p = p → N_G(P) = P (self-normalizing), P abelian → P ⊆ Z(N_G(P))
  3. Burnside's normal p-complement theorem → N ◁ G, |N| = p+1
  4. G = N ⋊ P, P acts faithfully on N (else P normal, contradiction)
  5. Orbit counting: |C_N(P)| ≡ 1 (mod p), |C_N(P)| ≠ p+1 → C_N(P) = {e} → single orbit → all non-identity elements same order d
  6. d prime (composite → g^a has smaller order), |N| = d^a = p+1 by Cauchy
  7. d odd → p = d^a-1 = (d-1)(...) composite (a≥2) or p = d-1 even (a=1) → contradiction
  8. d = 2 → p+1 = 2^a, QED

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
| 1 | 纯元认知观察 | 0.3 | Describe the structure of this problem. What are the given conditions and what needs to be proved? What is the gap? | Given: \|G\|=p(p+1), p odd prime, no normal Sylow p-subgroup. Prove: p+1=2^n. Gap: connecting group theory to number theory. |
| 2 | 自由列举 | 0.5 | What tools from group theory could connect the Sylow condition to the arithmetic conclusion? List all possible approaches. | Sylow counting, normalizer analysis, normal p-complement theorems, element counting, group actions, conjugation actions, representation theory. |
| 3 | 小尝试 | 0.2 | Try using Sylow's theorem directly. What can you determine about n_p? | n_p \|(p+1), n_p≡1(mod p), n_p>1 → n_p=p+1. Also \|N_G(P)\|=p so N_G(P)=P (self-normalizing). |
| 4 | 思维操作引导 | 0.4 | You have n_p=p+1 and N_G(P)=P. P is abelian. What theorem applies when a Sylow p-subgroup is self-normalizing and in the center of its normalizer? | Burnside's normal p-complement theorem: P≤Z(N_G(P)) → G has normal p-complement N of order p+1. |
| 5 | 思维操作引导 | 0.6 | G=N⋊P with N normal of order p+1. Analyze the conjugation action of P on N. Is it faithful? What are the fixed points? What does orbit structure tell you? | Faithful (else P normal). \|C_N(P)\|≡1(mod p), ≠p+1 → C_N(P)={e}. Single orbit → all non-identity elements same order d. |
| 6 | 推进 | 0.7 | All non-identity elements of N have same order d. Show d is prime, determine \|N\| in terms of d, derive contradiction if d odd. | d prime (composite→g^a smaller order). \|N\|=d^a=p+1. d odd: p=d^a-1=(d-1)(...) composite or p=d-1 even. So d=2. |
| 7 | 能量传递引导 | 0.3 | You've shown d=2. Write the final conclusion. | N is elementary abelian 2-group, \|N\|=2^a=p+1. Therefore p+1 is a power of 2. QED. |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.0
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
- problem_type: structural_existence
- structure_features: Finite group of order p(p+1) with p odd prime, non-normal Sylow p-subgroup; requires bridging group-theoretic hypotheses to number-theoretic conclusion via normal p-complement theorem and conjugation action orbit analysis
- key_objects: ["finite group G", "odd prime p", "Sylow p-subgroup P", "normal p-complement N", "conjugation action of P on N"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["Sylow counting", "normalizer analysis", "Burnside normal p-complement theorem", "group action orbit counting", "arithmetic contradiction via factorization"]
- primary_pattern: structural_transformation
- knowledge_required: ["Sylow theorems", "Burnside's normal p-complement theorem", "group actions and orbit counting", "Cauchy's theorem", "factorization of d^a - 1"]
- key_insight: All non-identity elements of the normal p-complement N have the same prime order d; if d is odd, then p = d^a - 1 = (d-1)(d^{a-1}+...+1) is composite (or even when a=1), contradicting p being an odd prime; hence d = 2 and p+1 = 2^a.

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: Sylow counting and group-theoretic structure
- translation_to: arithmetic constraint on p+1 via factorization of d^a - 1
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: logical_deduction, gap_type: structural_transformation}
- tell_small_concepts: ["Sylow counting", "normal p-complement", "faithful conjugation action", "orbit analysis", "prime order", "factorization d^a-1"]
- expected_ai_method: Direct Sylow counting followed by attempted arithmetic manipulation without identifying the normal p-complement or orbit structure
- correct_method: Sylow counting to get n_p=p+1, Burnside's normal p-complement theorem for normal subgroup N, faithful conjugation action orbit analysis, arithmetic contradiction via factorization of d^a-1

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ → 是，structural_existence/logical_deduction/structural_transformation 均为已有值
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ → 是，与已有值粒度一致
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ → 足够，无需新维度
- [x] 如果发现拓扑分类需要进化，在此写出建议： → 无需进化

**拓扑进化建议**（如有）：无。现有拓扑分类体系（structural_existence + logical_deduction + structural_transformation/knowledge_gap/method_translation）完全覆盖此题的tell结构。

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

详见 profile.json 中 tell_hint_pairs 和 global_tell_hint_pairs 字段。每个pair均含 tell_topology 和 tell_small_concepts。global pair 的 why_not_visible_locally 均已填写。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI will likely correctly perform Sylow counting to get n_p = p+1, then get stuck without knowing Burnside's normal p-complement theorem. Even if it identifies the normal subgroup N by element counting, it will likely fail to analyze the conjugation action orbit structure to deduce all non-identity elements have the same order. It will almost certainly not see the factorization d^a - 1 = (d-1)(...) contradiction that connects group element orders to the primality of p.
- suitable_for_poc: ["POC-VMS-8 (hint injection)", "POC-VMS-9/10 (tell identification)"]
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
- [x] answer（"p + 1 = 2^n for some positive integer n"）
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
- [x] tell_hint_pairs（7个pair，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（2个pair，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象，stats中knowledge_bottleneck="R4", thinking_bottleneck="R6"）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**将完整JSON写入工作目录的 `profile.json` 文件** → 已写入 subagents-dirs/fate_000253/profile.json

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
2. 更新`problem_extraction_progress`集合中`_key="396363"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000253"
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
    '_key': '396363',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000253',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000253')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

验证输出: fate_000253, 7 local pairs, 2 global pairs。所有per-pair拓扑、why_not_visible_locally、answer字段、knowledge_bottleneck="R4"、thinking_bottleneck="R6" 均验证通过。

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: fate_000253
- solution_method_type: structural_argument
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有拓扑分类体系完全覆盖此题。
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
