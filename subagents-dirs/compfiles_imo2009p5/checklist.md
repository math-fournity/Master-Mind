# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2009p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2009P5.lean
- **来源**: IMO 2009 P5
- **ArangoDB progress记录_key**: 329210（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2009P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Determine all functions f: ℤ>0 → ℤ>0 such that for all positive integers a and b, the numbers a, f(b), and f(b + f(a) - 1) form the sides of a nondegenerate triangle.
- 解答核心思路（1-2句话）：唯一解是f(x)=x（恒等函数）。证明通过将三角形条件转化为三个严格不等式，依次证明f(0)=0（周期性反证法）、f(f(x))=x（对合性）、f(1)=1（强归纳），最后用强归纳得出f(x)=x。
- 解答关键步骤列表：
  1. 三角形条件 → 三个严格不等式：f(y+f(x))≤f(y)+x, x≤f(y)+f(y+f(x)), f(y)≤f(y+f(x))+x
  2. 证明f(0)=0：假设f(0)>0，利用有界性和周期性导出矛盾
  3. 证明f(f(x))=x（对合）：不等式(1)和(3)在y=0时给出f(f(x))≤x和x≤f(f(x))
  4. 证明f(1)=1：强归纳证明f(n·f(1))=n，再用对合性得f(1)=1
  5. 证明f(x)=x：强归纳，利用f(x+1)≤f(x)+1和对合性

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
| 1 | 纯元认知观察 | 0.8 | What is the structure of this problem? What are the knowns and unknowns? What does the nondegenerate triangle condition give you? | We need to find all f: ℤ>0→ℤ>0 such that a, f(b), f(b+f(a)-1) form a nondegenerate triangle for all a,b. The triangle condition gives three strict inequalities. |
| 2 | 自由列举 | 0.7 | What approaches could work for this functional equation? List all possible directions. | Direct substitution, proving injectivity/surjectivity, establishing involution, induction, contradiction, periodicity arguments, boundedness arguments. |
| 3 | 小尝试 | 0.4 | Try substituting specific values of a and b. What do you notice about the self-referential structure? | Setting a=1,b=1 gives triangle with sides 1, f(1), f(f(1)). Key observation: f(a) appears inside the argument of f in f(b+f(a)-1), creating self-referential composition. |
| 4 | 思维操作引导 | 0.5 | Write out the three inequalities explicitly. Can you combine inequality (1) and (3) to derive a structural property? | Inequalities: (1) f(y+f(x))≤f(y)+x, (2) x≤f(y)+f(y+f(x)), (3) f(y)≤f(y+f(x))+x. Setting y=0 with f(0)=0: (1) gives f(f(x))≤x, (3) gives x≤f(f(x)), hence f(f(x))=x (involution). |
| 5 | 思维操作引导 | 0.4 | You need f(0)=0 first. Try assuming f(0)>0 and deriving a contradiction using boundedness and periodicity. | Assume f(0)>0. f is bounded on {0,...,f(0)-1} by K. Periodicity from inequality (1) implies f is periodic mod f(0). Find large n where f(n) is small, violating inequality (2). Contradiction, so f(0)=0. |
| 6 | 推进 | 0.5 | Now that you have f(0)=0 and f(f(x))=x, prove f(1)=1 using strong induction on f(n·f(1))=n. | Using f(y+f(1))≤f(y)+1, strong induction gives f(n·f(1))=n. Applying f: f(n)=n·f(1). Setting n=f(1) with f(f(1))=1: f(1)²=1, so f(1)=1. |
| 7 | 能量传递引导 | 0.3 | You have all key properties. Complete the proof by strong induction to show f(x)=x. | With f(0)=0, f(f(x))=x, f(1)=1: f(x+1)≤f(x)+1 by inequality. Induction gives f(x)=x, then f(x+1)≤x+1. Involution forces f(x+1)=x+1. Done. |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.6
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
- problem_type: characterization（确定所有满足条件的函数）
- structure_features: 三角形不等式约束作用于函数值，含复合结构f(b+f(a)-1)；定义域和值域为正整数；约束将f(a)嵌入另一个f求值的参数中，形成自指结构
- key_objects: f: ℤ>0→ℤ>0, 非退化三角形条件, 三个严格三角形不等式, 对合性质f(f(x))=x, 强归纳

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [constraint_extraction, contradiction_argument, involution_recognition, strong_induction, specialization_to_generalization]
- primary_pattern: involution_recognition（对合识别——从配对不等式中识别出f(f(x))=x）
- knowledge_required: [triangle inequality, functional equations, strong induction, involution, periodicity arguments, boundedness on finite sets]
- key_insight: 三个三角形不等式配对组合后编码了对合性质f(f(x))=x，而f(0)=0的周期性反证法是解锁归纳结构的门户

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: geometric triangle constraint（几何三角形约束语言）
- translation_to: algebraic inequality system with involution structure（代数不等式系统+对合结构）
- translation_type: geometric_to_algebraic（几何到代数的翻译——将三角形条件翻译为三个严格不等式，再从不等式系统中提取对合结构）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_manipulation, gap_type: structural_transformation}
- tell_small_concepts: [triangle inequality, involution, periodicity contradiction, strong induction, f(f(x))=x, f(0)=0]
- expected_ai_method: direct_manipulation — bare AI会尝试直接代入小值并进行case analysis，不会识别对合结构或周期性反证法
- correct_method: structural_transformation via involution recognition and periodicity contradiction, followed by strong induction

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是。characterization（已有）、direct_manipulation（已有）、structural_transformation（已有）都能覆盖。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是。三个维度的值都是中等抽象粒度，与已有值一致。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。三个维度能区分这道题的tell（characterization + direct_manipulation + structural_transformation）与其他题目的tell。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。当前拓扑分类足够。

**拓扑进化建议**（如有）：无。当前三个维度（problem_type, ai_method_type, gap_type）的已有值完全覆盖这道题。

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
- 局部tell_hint_pairs数量: 7 对（每轮一个，含per-pair tell_topology和tell_small_concepts）
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个
- 所有pair均包含tell_topology和tell_small_concepts字段
- 所有global pair的why_not_visible_locally字段已填写（非None）
- R5的is_knowledge_bottleneck=True，gap_type=knowledge_gap
- knowledge_bottleneck="R5", thinking_bottleneck="R4"（字符串类型）

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI会尝试直接代入小值（a=1, b=1等）并陷入无产出的case analysis。不会识别三个三角形不等式编码了对合性质f(f(x))=x，也不会知道f(0)=0所需的周期性反证法技术。没有这些结构洞察，AI无法超越验证f(x)=x满足条件这一步。
- suitable_for_poc: [tell_extraction, hint_injection, topology_matching, knowledge_bottleneck_identification]
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

**将完整JSON写入工作目录的 `profile.json` 文件**：已写入 `subagents-dirs/compfiles_imo2009p5/profile.json`

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
2. 更新`problem_extraction_progress`集合中`_key="329210"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2009p5"
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
    '_key': '329210',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2009p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2009p5')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证详情: compfiles_imo2009p5, 7 local pairs, 2 global pairs, answer非None, knowledge_bottleneck="R5"(str类型)

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_imo2009p5
- solution_method_type: structural_deduction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否。当前三个维度（problem_type=characterization, ai_method_type=direct_manipulation, gap_type=structural_transformation）的已有值完全覆盖这道题，粒度一致，无需进化。
- 是否遇到异常: 否。所有字段验证通过，入库成功。

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
