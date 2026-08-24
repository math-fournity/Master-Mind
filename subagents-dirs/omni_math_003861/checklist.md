# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003861
- **文件路径**: subagents-dirs/omni_math_003861/problem.lean
- **来源**: AoPS omni_math (imo_shortlist)
- **ArangoDB progress记录_key**: 333740（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003861/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Find all functions f: Z>0 → Z>0 such that a+f(b) divides a²+bf(a) for all positive integers a and b with a+b>2019.
- 解答核心思路（1-2句话）：验证f(a)=ka可行；固定a，研究商q_b=(a²+bf(a))/(a+f(b))当b→∞时的行为，证明其稳定，从而推出f线性。
- 解答关键步骤列表：
  1. 验证f(a)=ka：a+kb | a²+bka = a(a+kb) ✓
  2. 上界：取a=1，1+f(b)|1+bf(1) ⇒ f(b) ≤ bf(1)
  3. 固定a，定义q_b=(a²+bf(a))/(a+f(b))∈Z>0，利用f(b)≤bf(1)得q_b≥f(a)/f(1)
  4. 证明q_b对充分大的b稳定为常数q(a)
  5. 由q(a)(a+f(b))=a²+bf(a)推出f(b)=(f(a)/q(a))b+(a²-q(a)a)/q(a)
  6. f(b)不依赖a ⇒ f(a)/q(a)=k常数且(a²-q(a)a)/q(a)=0 ⇒ q(a)=a ⇒ f(a)=ka

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.3 | 描述这道题的结构：已知什么、求什么、条件a+b>2019的作用是什么？ | 函数方程f:Z>0→Z>0，整除条件a+f(b)|a²+bf(a)，阈值a+b>2019意味着只需对充分大的a+b验证，这允许取极限 |
| 2 | 自由列举 | 0.5 | 列出所有可能的解题方向 | (1)试f(a)=ka/常数等特定形式 (2)固定一个变量研究另一个 (3)利用阈值取极限 (4)研究f的增长率 (5)用整除提取模约束 |
| 3 | 小尝试 | 0.4 | 试f(a)=ka是否可行？再试f(a)=c（常数）是否可行？ | f(a)=ka：a+kb|a(a+kb)✓。f(a)=c：a+c|a²+bc，固定a令b→∞得a+c|a(a-c)，取a=c+1得2c+1|c+1⇒c≤0矛盾 |
| 4 | 思维操作引导 | 0.6 | 固定a=1，整除条件告诉你f(b)的增长率有什么约束？ | 1+f(b)|1+bf(1)⇒1+f(b)≤1+bf(1)⇒f(b)≤bf(1)，f至多线性增长 |
| 5 | 思维操作引导 | 0.7 | 固定一般a，对充分大的b定义q_b=(a²+bf(a))/(a+f(b))。利用f(b)≤bf(1)，q_b有什么下界？能否证明q_b稳定？ | q_b≥f(a)/f(1)，q_b是正整数有下界。对充分大的b可证q_b稳定为常数q(a)（因为q_b有界且取整数值） |
| 6 | 推进 | 0.6 | 假设q_b稳定为q(a)，从q(a)(a+f(b))=a²+bf(a)能推出f(b)什么形式？如何利用f(b)不依赖a得出结论？ | f(b)=(f(a)/q(a))b+(a²-q(a)a)/q(a)。f(b)不依赖a⇒f(a)/q(a)=k常数且常数项=0⇒q(a)=a⇒f(a)=ka |
| 7 | 能量传递引导 | 0.4 | 你已识别答案和关键步骤，请写出完整证明 | 完整证明：验证→上界→商稳定→线性推导 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.5
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: 函数方程+整除条件，阈值条件a+b>2019允许渐近分析，需固定一个变量研究另一个趋于无穷时的行为
- key_objects: f:Z>0→Z>0, 整除关系a+f(b)|a²+bf(a), 商q_b, 增长率

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["verify_candidate", "growth_analysis", "fix_one_variable", "quotient_stabilization", "asymptotic_deduction", "coefficient_matching"]
- primary_pattern: quotient_stabilization
- knowledge_required: ["divisibility properties", "asymptotic analysis on integers", "functional equations on positive integers", "growth rate bounds", "quotient stabilization argument"]
- key_insight: 固定a，研究商q_b=(a²+bf(a))/(a+f(b))当b→∞时稳定为常数，再由f(b)不依赖a推出f(a)=ka

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: divisibility_relation（整除关系的直接操作）
- translation_to: asymptotic_growth_analysis（固定变量+商的渐近稳定分析）
- translation_type: method_translation（将整除问题翻译为渐近增长分析问题）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_manipulation, gap_type: method_translation}
- tell_small_concepts: ["divisibility condition", "threshold a+b>2019", "growth rate", "quotient stabilization", "fix one variable", "linear function"]
- expected_ai_method: direct_manipulation（AI可能直接操作整除关系，尝试各种代数变形而不引入渐近分析）
- correct_method: 固定一个变量，研究商当另一个变量趋于无穷时的稳定行为，推出线性

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——characterization/direct_manipulation/method_translation均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 不需要新维度——三个维度足够区分
- 无拓扑进化建议

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

局部pair摘要：
- R1: tell=AI看到函数方程+整除但未识别阈值条件作用, hint=描述结构注意阈值, level=0.3, 纯元认知观察, topology=(characterization, direct_manipulation, method_problem_mismatch)
- R2: tell=AI未列举可能方向, hint=列出所有方向, level=0.5, 自由列举, topology=(characterization, enumeration_brute_force, search_space_estimation)
- R3: tell=AI试线性形式但未排除其他, hint=试常数形式, level=0.4, 小尝试, topology=(characterization, direct_calculation, method_problem_mismatch)
- R4: tell=AI未看到增长率约束, hint=固定a=1求上界, level=0.6, 思维操作引导, topology=(characterization, direct_manipulation, structural_transformation)
- R5: tell=AI有上界但未看到商稳定论证, hint=定义q_b研究稳定, level=0.7, 思维操作引导, is_knowledge_bottleneck=true, topology=(characterization, direct_manipulation, knowledge_gap)
- R6: tell=AI看到商稳定但未推出线性, hint=解f(b)利用不依赖a, level=0.6, 推进, topology=(characterization, algebraic_identity, method_translation)
- R7: tell=AI有所有部件需组装, hint=写完整证明, level=0.4, 能量传递引导, topology=(characterization, logical_deduction, method_problem_mismatch)

全局pair摘要：
- G1(path_feature): tell=整除条件需翻译为渐近增长分析, hint=固定变量研究商的稳定, level=0.7, why_not_visible_locally=每步看似标准操作但全局策略需看到从整除到渐近到线性的完整路径
- G2(implicit): tell=阈值a+b>2019不是技术限制而是渐近分析关键, hint=阈值允许取极限, level=0.6, observation_point=R1, why_not_visible_locally=阈值看似技术限制实则使能渐近论证

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: AI能验证f(a)=ka可行，但无法独立发现商稳定论证——关键步骤是固定a研究q_b当b→∞的行为，这需要将整除条件翻译为渐近分析的非显然洞察
- suitable_for_poc: ["hint_injection_poc", "tell_identification_poc", "quotient_stabilization_method_poc"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

完整profile JSON已写入 `subagents-dirs/omni_math_003861/profile.json`

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
2. 更新`problem_extraction_progress`集合中`_key="333740"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_003861"
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
    '_key': '333740',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_003861',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_003861')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

- problem_id: omni_math_003861
- solution_method_type: quotient_stabilization
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，已有分类体系足够
- 是否遇到异常: 否

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
