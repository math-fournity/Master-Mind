# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000254
- **文件路径**: subagents-dirs/fate_000254/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396364（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000254/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let p be a prime, let G be a finite p-group. Let A be a maximal normal abelian subgroup of G. Prove that A is also a maximal abelian subgroup of G.
- 解答核心思路（1-2句话）：证明A = C_G(A)（中心化子等于自身）。若A < C_G(A)，利用p-群商群G/A的中心非平凡性，找到x ∈ C_G(A)\A使xA ∈ Z(G/A)，则⟨A,x⟩是真正包含A的正规交换子群，矛盾。因此A = C_G(A)，而任何包含A的交换子群B都满足B ≤ C_G(A) = A。
- 解答关键步骤列表：
  1. 假设存在交换子群B满足A < B，则B ≤ C_G(A)（因B交换且A ≤ B，B中元素与A中元素交换）
  2. 因此 A < C_G(A)
  3. C_G(A) ⊴ G（正规子群的中心化子是正规的）
  4. C_G(A)/A 是 p-群 G/A 的非平凡子群
  5. p-群中心非平凡：存在 x ∈ C_G(A)\A 使 xA ∈ Z(G/A)
  6. ⟨A,x⟩ ⊴ G（因xA在G/A的中心中，⟨A,x⟩/A是G/A的中心子群，故正规）且⟨A,x⟩交换（x ∈ C_G(A)故x与A交换，⟨x⟩循环故交换）
  7. ⟨A,x⟩是真正包含A的正规交换子群，与A的极大性矛盾
  8. 因此 A = C_G(A)，任何交换B ≥ A满足 B ≤ C_G(A) = A，故B = A

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
| 1 | 纯元认知观察 | 0.3 | Describe the structure of this problem. What are the key objects, and what is the gap between "maximal normal abelian" and "maximal abelian"? | We have a finite p-group G and a maximal normal abelian subgroup A. We need to show A is maximal among ALL abelian subgroups, not just normal ones. The gap: there could be non-normal abelian subgroups properly containing A. |
| 2 | 自由列举 | 0.5 | List all possible approaches to bridge from "maximal normal abelian" to "maximal abelian". | 1) Direct: show any abelian B ≥ A must be normal. 2) Centralizer: show A = C_G(A). 3) Normalizer growth in p-groups. 4) Quotient G/A and its center. 5) Contradiction: assume A < B abelian, derive contradiction. |
| 3 | 小尝试 | 0.4 | Try the direct approach: if B is abelian and A ≤ B, can you show B is normal in G? | This fails. An abelian subgroup containing a normal subgroup need not be normal. Normality of A doesn't transfer to B. The direct approach is a dead end. |
| 4 | 思维操作引导 | 0.6 | Instead of making B normal, think about where B must sit. If B is abelian and A ≤ B, what subgroup of G must contain B? | Since B is abelian and A ≤ B, every element of B commutes with every element of A. So B ≤ C_G(A), the centralizer of A in G. If A < B, then A < C_G(A). |
| 5 | 思维操作引导 | 0.7 | Now focus on C_G(A). What properties does it have? Is it normal in G? What can you say about C_G(A)/A? | Since A ⊴ G, C_G(A) ⊴ G (centralizer of a normal subgroup is normal). If A < C_G(A), then C_G(A)/A is a nontrivial subgroup of G/A. Since G is a p-group, G/A is a p-group, so C_G(A)/A is a nontrivial p-group. |
| 6 | 思维操作引导 | 0.7 | Use the key property that p-groups have nontrivial centers. How can you use this to find a normal abelian subgroup of G properly containing A? | Since G/A is a p-group, Z(G/A) is nontrivial. There exists x ∈ C_G(A)\A with xA ∈ Z(G/A). Then ⟨A,x⟩ is normal in G (xA central in G/A implies ⟨A,x⟩/A central hence normal in G/A) and abelian (x ∈ C_G(A) commutes with A, ⟨x⟩ cyclic). This contradicts A's maximality as normal abelian. |
| 7 | 能量传递引导 | 0.4 | Complete the proof. You have the contradiction — now close the argument. | The contradiction shows A = C_G(A). Now any abelian B with A ≤ B satisfies B ≤ C_G(A) = A, so B = A. Therefore A is maximal abelian. QED. |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 3
- knowledge_rounds（思维操作引导的轮数）: 3
- level_sum: 3.6
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
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
- structure_features: "p-group structure, maximal normal abelian subgroup, centralizer argument, quotient group center, contradiction via p-group center nontriviality"
- key_objects: ["finite p-group G", "maximal normal abelian subgroup A", "centralizer C_G(A)", "quotient group G/A", "center Z(G/A)", "abelian subgroup B containing A"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["contradiction", "centralizer reduction", "quotient group center argument", "p-group center nontriviality"]
- primary_pattern: centralizer reduction
- knowledge_required: ["p-groups have nontrivial centers", "centralizer of a normal subgroup is normal", "abelian subgroup containing A lies in C_G(A)", "central subgroup of quotient implies normal subgroup of parent"]
- key_insight: Show A = C_G(A) by contradiction: if A < C_G(A), use nontrivial center of p-group G/A to construct a normal abelian subgroup properly containing A, contradicting maximality

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: maximality among normal abelian subgroups
- translation_to: maximality among all abelian subgroups via centralizer equality A = C_G(A)
- translation_type: structural_transformation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "logical_deduction", gap_type: "knowledge_gap"}
- tell_small_concepts: ["centralizer of normal subgroup", "p-group center nontrivial", "maximal normal abelian", "quotient group center", "centralizer equality A = C_G(A)"]
- expected_ai_method: direct_manipulation — AI will try to directly show any abelian B containing A must be normal, which fails because normality doesn't transfer upward
- correct_method: centralizer reduction — show A = C_G(A) via contradiction using p-group center property, then deduce maximal abelian from centralizer equality

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ → 是。structural_existence + logical_deduction + knowledge_gap 完全适用。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ → 是。与已有抽象级值一致。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ → 足够。
- [x] 如果发现拓扑分类需要进化，在此写出建议： → 无需进化。

**拓扑进化建议**（如有）：无。现有拓扑分类体系完全覆盖本题。

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
- R1: tell="AI sees problem but doesn't recognize gap between normal-abelian and abelian maximality", hint="Describe problem structure: what does maximal normal abelian mean vs maximal abelian?", hint_level=0.3, situation_type=纯元认知观察, is_knowledge_bottleneck=false, tell_topology={structural_existence, logical_deduction, method_problem_mismatch}, tell_small_concepts=["maximal normal abelian", "maximal abelian", "normality gap"]
- R2: tell="AI lists approaches but may not identify centralizer as key tool", hint="List all approaches to bridge normal-abelian to abelian maximality", hint_level=0.5, situation_type=自由列举, is_knowledge_bottleneck=false, tell_topology={structural_existence, enumeration_brute_force, search_space_estimation}, tell_small_concepts=["centralizer approach", "normalizer growth", "quotient center", "direct normality"]
- R3: tell="AI tries to show B is normal directly, which fails", hint="Try showing any abelian B containing A must be normal", hint_level=0.4, situation_type=小尝试, is_knowledge_bottleneck=false, tell_topology={structural_existence, direct_manipulation, method_problem_mismatch}, tell_small_concepts=["normality transfer", "abelian containing normal", "failed direct approach"]
- R4: tell="AI doesn't see that abelian B containing A must lie in C_G(A)", hint="If B is abelian and A ≤ B, what subgroup must contain B?", hint_level=0.6, situation_type=思维操作引导, is_knowledge_bottleneck=true, tell_topology={structural_existence, logical_deduction, knowledge_gap}, tell_small_concepts=["centralizer C_G(A)", "abelian implies centralization", "B ≤ C_G(A)"]
- R5: tell="AI doesn't know centralizer of normal is normal, or G/A is p-group with nontrivial center", hint="What properties does C_G(A) have? Is it normal? What about C_G(A)/A?", hint_level=0.7, situation_type=思维操作引导, is_knowledge_bottleneck=true, tell_topology={structural_existence, logical_deduction, knowledge_gap}, tell_small_concepts=["centralizer of normal is normal", "G/A p-group", "nontrivial center of p-group"]
- R6: tell="AI knows ingredients but doesn't see how to combine them for contradiction", hint="Use nontrivial center of G/A to find x, show ⟨A,x⟩ normal abelian, contradict maximality", hint_level=0.7, situation_type=思维操作引导, is_knowledge_bottleneck=false, tell_topology={structural_existence, logical_deduction, structural_transformation}, tell_small_concepts=["center element lift", "⟨A,x⟩ normal abelian", "contradiction construction"]
- R7: tell="AI has contradiction but needs to close argument cleanly", hint="Conclude A = C_G(A), then any abelian B ≥ A satisfies B ≤ C_G(A) = A", hint_level=0.4, situation_type=能量传递引导, is_knowledge_bottleneck=false, tell_topology={structural_existence, logical_deduction, method_problem_mismatch}, tell_small_concepts=["C_G(A) = A", "maximal abelian conclusion", "centralizer equality"]

**全局pairs详情**：
- Global 1 (path_feature): tell="Full proof path requires recognizing centralizer C_G(A) as bridge: A = C_G(A) via p-group center, then maximal abelian follows", hint="Key structural insight: maximal normal abelian implies A = C_G(A) in p-groups, stronger than maximal abelian", hint_level=0.7, generalizability="high — centralizer reduction applies to many p-group subgroup maximality problems", why_not_visible_locally="Each local step (centralizer containment, normality of centralizer, center of p-group) is a standard fact, but the global path of combining them into a contradiction establishing A = C_G(A) is not visible from any single step", tell_topology={structural_existence, logical_deduction, structural_transformation}, tell_small_concepts=["centralizer equality", "p-group center contradiction", "maximal normal abelian to maximal abelian"]
- Global 2 (implicit): tell="Implicit fact that abelian B containing A satisfies B ≤ C_G(A) is the entry point to entire proof, not obvious from problem statement", hint="Recognize abelian B with A ≤ B implies B ≤ C_G(A) — translates problem from maximal abelian to A = C_G(A)", hint_level=0.6, generalizability="high — abelian-to-centralizer translation is universal in group theory", why_not_visible_locally="This connection between 'B abelian containing A' and 'B centralizes A' requires recognizing centralizer as the right framing — not stated in problem, emerges only when asking where does an abelian subgroup containing A live", tell_topology={structural_existence, logical_deduction, knowledge_gap}, tell_small_concepts=["abelian implies centralization", "centralizer as container", "problem reframing"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "Bare AI will likely try to directly show that any abelian subgroup B containing A must be normal in G, which fails because normality doesn't transfer upward. It may not recognize the centralizer reduction strategy (A = C_G(A)) or the p-group center property needed for the contradiction argument."
- suitable_for_poc: ["POC-VMS-8 (hint injection — centralizer reduction hint)", "POC-VMS-9 (tell de-specialization — structural_existence + knowledge_gap topology)", "POC-VMS-10 (small concept disambiguation — centralizer vs normalizer vs direct normality)"]
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
- [x] answer（proof类型填要证明的结论）
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

**将完整JSON写入工作目录的 `profile.json` 文件** — 已完成

---

## Step 10: 入库ArangoDB [x]

**操作**：用exec工具执行Python脚本入库

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="396364"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000254"
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
    '_key': '396364',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000254',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000254')
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
- problem_id: fate_000254
- solution_method_type: centralizer_reduction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有拓扑分类体系（structural_existence + logical_deduction + knowledge_gap）完全覆盖本题。
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
