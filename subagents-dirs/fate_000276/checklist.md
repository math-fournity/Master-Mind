# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000276
- **文件路径**: subagents-dirs/fate_000276/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396386（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000276/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let p be a prime number. Let K/ℚ be a finite extension, such that the p²-th root of unity is contained in K. Let L/K be a Galois extension of degree p, show that there exists a Galois extension L'/L of degree p, such that the extension L'/K is Galois.
- 解答核心思路（1-2句话）：由Kummer理论，因ζ_p∈K，L=K(a^{1/p})。构造L'=K(a^{1/p²})，因ζ_{p²}∈K保证L'/K是p²次循环Galois扩张，从而L'/L是p次Galois扩张。
- 解答关键步骤列表：
  1. 观察ζ_{p²}∈K蕴含ζ_p=ζ_{p²}^p∈K
  2. 应用Kummer理论：L/K是p次循环扩张且ζ_p∈K，故L=K(a^{1/p})对某a∈K
  3. 构造L'=K(a^{1/p²})，即 adjoining a的p²次根α
  4. 验证[L':K]=p²：α的共轭为ζ_{p²}^i·α，i=0,...,p²-1，因ζ_{p²}∈K⊂L'，所有共轭在L'中
  5. L'/K是Galois（正规+可分），Galois群循环p²阶
  6. 塔性质：[L':L]=p²/p=p，且L'/K正规蕴含L'/L正规，故L'/L是p次Galois扩张

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
| 1 | 纯元认知观察 | 0.7 | Describe the structure of this problem. What are the given objects, what is the hypothesis about roots of unity, and what needs to be shown? | We have p prime, K/ℚ finite with ζ_{p²}∈K, L/K Galois of degree p. We need to find L'/L Galois of degree p with L'/K Galois. The key given is ζ_{p²}∈K, and the goal is existence of a tower extension. |
| 2 | 自由列举 | 0.6 | What tools from algebraic number theory could be relevant here? List all possible approaches. | Kummer theory (since roots of unity present), cyclic extensions, Galois theory tower properties, character theory, Artin-Schreier theory, embedding problems. |
| 3 | 小尝试 | 0.4 | Try using just basic Galois theory without Kummer theory. Can you construct L' directly by adjoining some element to L? | Trying to adjoin some element to L... Without Kummer theory, it's hard to control the Galois group. The issue is ensuring L'/K is Galois (normality over K), not just L'/L. This approach seems stuck. |
| 4 | 思维操作引导 | 0.5 | Notice that ζ_{p²}∈K implies ζ_p∈K. What does Kummer theory tell you about the structure of L/K? | Since ζ_p∈K and L/K is cyclic (Galois of prime degree p), by Kummer theory L=K(a^{1/p}) for some a∈K. This is the Kummer extension structure. |
| 5 | 思维操作引导 | 0.4 | Given L=K(a^{1/p}), how can you 'lift' this to a degree p² extension? What element should you adjoin? | Consider L'=K(a^{1/p²}), i.e., adjoin α where α^{p²}=a. Then L=K(α^p)⊂L'. Need to check [L':K]=p² and that L'/K is Galois. |
| 6 | 推进 | 0.5 | Show that L'/K is Galois. What makes all conjugates of a^{1/p²} lie in L'? | The conjugates of α=a^{1/p²} are ζ_{p²}^i·α for i=0,...,p²-1. Since ζ_{p²}∈K⊂L', all conjugates are in L'. So L'/K is normal. Since char 0, separable, hence Galois. Galois group is cyclic of order p². |
| 7 | 能量传递引导 | 0.3 | Now conclude: what does L'/K being Galois of degree p² imply for L'/L? | By the tower, [L':L]=[L':K]/[L:K]=p²/p=p. Since L'/K is Galois (normal), L'/L is also Galois (normality passes to intermediate fields). So L'/L is Galois of degree p, and L'/K is Galois. Done. |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.4
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
- structure_features: Tower of Galois extensions with Kummer theory applicable due to roots of unity; existence construction via lifting from degree p to degree p²; the hypothesis ζ_{p²}∈K is stronger than needed for the immediate step but essential for the lift
- key_objects: ["prime p", "finite extension K/ℚ", "p²-th root of unity ζ_{p²}", "Galois extension L/K of degree p", "Galois extension L'/L of degree p", "Kummer extension K(a^{1/p})", "lifted extension K(a^{1/p²})"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["structural lifting", "Kummer theory application", "tower property reasoning", "normality inheritance", "hypothesis strength recognition"]
- primary_pattern: structural lifting
- knowledge_required: ["Kummer theory", "Galois theory", "cyclic extensions of prime degree", "roots of unity", "tower of field extensions", "normality in Galois theory"]
- key_insight: Lift the Kummer extension L=K(a^{1/p}) to L'=K(a^{1/p²}); the presence of ζ_{p²} in K (not just ζ_p) is exactly what guarantees L'/K is cyclic Galois of degree p²

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: Kummer theory at degree p (L=K(a^{1/p}))
- translation_to: Lifted Kummer extension at degree p² (L'=K(a^{1/p²}))
- translation_type: structural_transformation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "direct_manipulation", gap_type: "knowledge_gap"}
- tell_small_concepts: ["Kummer theory", "p²-th root of unity", "cyclic Galois extension", "tower property", "normality inheritance", "structural lifting"]
- expected_ai_method: direct_manipulation (bare AI might try to construct L' by ad hoc methods—compositum, adjoining arbitrary elements—without recognizing the Kummer theory structure and the lifting pattern)
- correct_method: Kummer theory lifting (use Kummer theory to express L=K(a^{1/p}), then lift to L'=K(a^{1/p²}) using the stronger hypothesis ζ_{p²}∈K)

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？是。structural_existence、direct_manipulation、knowledge_gap均可归入已有值。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？是。与已有值粒度一致。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？足够。这道题的核心gap是知识缺口（Kummer理论）+结构变换（lifting），现有维度可以区分。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。

**拓扑进化建议**（如有）：无。现有拓扑分类体系足以处理此题。

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

| R | tell | hint | level | sit_type | kb | topology | small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI sees a tower extension problem but doesn't identify the role of ζ_{p²} | Describe the structure: what is given and what is needed? | 0.7 | 纯元认知观察 | false | {structural_existence, direct_manipulation, method_problem_mismatch} | ["tower of extensions", "existence construction"] |
| 2 | AI lists approaches but may not recognize Kummer theory as the key tool | List all possible approaches from algebraic number theory | 0.6 | 自由列举 | false | {structural_existence, enumeration_brute_force, search_space_estimation} | ["Kummer theory", "cyclic extensions", "Galois tower"] |
| 3 | AI tries direct construction without Kummer theory, gets stuck on normality | Try constructing L' directly without Kummer theory | 0.4 | 小尝试 | false | {structural_existence, direct_manipulation, method_problem_mismatch} | ["normality over K", "ad hoc construction"] |
| 4 | AI doesn't see that ζ_p∈K enables Kummer theory | Notice ζ_{p²}∈K implies ζ_p∈K; apply Kummer theory to L/K | 0.5 | 思维操作引导 | true | {structural_existence, direct_manipulation, knowledge_gap} | ["Kummer theory", "ζ_p from ζ_{p²}", "cyclic degree p extension"] |
| 5 | AI has Kummer form L=K(a^{1/p}) but doesn't see the lifting idea | Given L=K(a^{1/p}), how to lift to degree p²? | 0.4 | 思维操作引导 | false | {structural_existence, algebraic_identity, structural_transformation} | ["p²-th root lifting", "Kummer extension lifting"] |
| 6 | AI has L'=K(a^{1/p²}) but hasn't verified Galois over K | Show L'/K is Galois using ζ_{p²}∈K | 0.5 | 推进 | false | {structural_existence, logical_deduction, knowledge_gap} | ["conjugates via ζ_{p²}", "cyclic Galois group", "normality"] |
| 7 | AI has shown L'/K Galois but needs to conclude L'/L properties | Conclude using tower properties | 0.3 | 能量传递引导 | false | {structural_existence, logical_deduction, method_problem_mismatch} | ["tower degree formula", "normality inheritance", "degree p"] |

**全局pairs详情**：

1. path_feature型:
- scope: "The full path from recognizing ζ_{p²}∈K → Kummer theory → lifting to p²-th root → Galois verification"
- observation_point: null
- tell: The entire solution path requires connecting Kummer theory (degree p) with a lifting to degree p², using the stronger hypothesis ζ_{p²}∈K (not just ζ_p)
- hint: The p²-th root of unity is not just for Kummer theory at degree p—it enables the lift to degree p² while maintaining Galois
- hint_level: 0.7
- generalizability: "high - the lifting pattern from K_n to K_{n+1} using higher roots of unity generalizes to other Kummer-type problems"
- why_not_visible_locally: Each local step focuses on one aspect (Kummer theory application, lifting construction, Galois verification), but the global insight—that the p²-th root of unity is precisely what enables the lift from degree p to degree p² while preserving Galois—is only visible from the complete path connecting all steps
- tell_topology: {structural_existence, direct_manipulation, structural_transformation}
- tell_small_concepts: ["Kummer theory lifting", "p²-th root of unity", "degree p² cyclic extension"]

2. implicit型:
- scope: "The relationship between the hypothesis strength (ζ_{p²} vs ζ_p) and the conclusion"
- observation_point: "R4"
- tell: The hypothesis gives ζ_{p²}∈K, which is stronger than needed for Kummer theory at degree p (which only needs ζ_p). The extra strength is exactly what's needed for the lift.
- hint: Ask: why does the problem give ζ_{p²} instead of just ζ_p? The extra root of unity must play a role in the construction.
- hint_level: 0.6
- generalizability: "high - recognizing when hypotheses are deliberately stronger than the obvious need is a generalizable meta-heuristic"
- why_not_visible_locally: In the local step of applying Kummer theory (R4), one only needs ζ_p and doesn't question why ζ_{p²} is given. The implicit signal—that the extra hypothesis strength is reserved for a later step—only becomes visible when comparing the hypothesis against the full solution path
- tell_topology: {structural_existence, direct_manipulation, knowledge_gap}
- tell_small_concepts: ["hypothesis strength", "ζ_{p²} vs ζ_p", "reserved hypothesis"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI likely tries to construct L' by ad hoc methods (e.g., compositum of L with another extension, or adjoining arbitrary elements to L) without recognizing the Kummer theory structure. Without the lifting insight (L=K(a^{1/p}) → L'=K(a^{1/p²})), it cannot guarantee L'/K is Galois. The key failure is not recognizing that ζ_{p²}∈K (not just ζ_p) is the crucial hypothesis enabling the degree p² lift.
- suitable_for_poc: ["tell_hint_injection", "knowledge_bottleneck_detection", "structural_transformation_recognition", "hypothesis_strength_recognition"]
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
2. 更新`problem_extraction_progress`集合中`_key="396386"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000276"
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
    '_key': '396386',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000276',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000276')
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
- problem_id: fate_000276
- solution_method_type: existence_construction (Kummer theory lifting)
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有拓扑分类体系（structural_existence / direct_manipulation / knowledge_gap等）足以处理此题。
- 是否遇到异常: 无异常。Lean文件中proof为sorry（无形式化证明），解答从数学知识重建。

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
