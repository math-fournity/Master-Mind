# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000306
- **文件路径**: subagents-dirs/fate_000306/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396416（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000306/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let A be a domain and K its field of fractions. x ∈ K is called almost integral if there exists r ∈ A, r ≠ 0 such that rx^n ∈ A for all n ≥ 0. A is called completely integrally closed if every almost integral element of K is contained in A. Show that if A is completely integrally closed, so is A[X].
- 解答核心思路（1-2句话）：分两阶段归约：先用K[X]的PID性质和互素性将K(X)中的几乎整元素归约为K[X]中的多项式，再用首系数分析+归纳法证明每个系数在A中几乎整，从而属于A。
- 解答关键步骤列表：
  1. 确认Frac(A[X]) = K(X)（有理函数域）
  2. 取f ∈ K(X)几乎整于A[X]，即∃ g ∈ A[X]\{0}, g·f^n ∈ A[X] ∀n≥0
  3. 写f = p/q，p,q ∈ K[X]互素；由g·(p/q)^n ∈ A[X] ⊂ K[X]得q^n | g·p^n；由gcd(p^n,q^n)=1得q^n | g ∀n；g为固定多项式故q ∈ K*，即f ∈ K[X]
  4. 设f = a_d X^d + ... + a_0 ∈ K[X]；考察g·f^n的首系数 = lc(g)·a_d^n ∈ A ∀n，故a_d几乎整于A，由A完全整闭得a_d ∈ A
  5. 对次数归纳：减去a_d X^d后对剩余部分重复论证，得所有a_i ∈ A
  6. 结论f ∈ A[X]，故A[X]完全整闭

**注意**：Lean文件中theorem用sorry占位，无形式化证明。以上为标准数学证明。

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.3 | 描述这道题的结构：已知什么对象？需要证明什么？A[X]的分式域是什么？ | 已知A是整环，K=Frac(A)，A完全整闭。需证A[X]完全整闭。A[X]的分式域是K(X)（有理函数域）。几乎整元素的定义：∃r∈A\{0}, rx^n∈A ∀n≥0。 |
| 2 | 自由列举 | 0.5 | 列出证明A[X]完全整闭的所有可能方向。 | (1)直接用定义：取K(X)中几乎整元素，证其属于A[X]。(2)利用完全整闭等价于A=∩A_p（height-1素理想）。(3)Gauss引理型论证。(4)系数分析。 |
| 3 | 小尝试 | 0.4 | 尝试方向(1)：直接用定义。取f∈K(X)几乎整于A[X]，即∃g∈A[X]\{0}使g·f^n∈A[X]∀n。f是有理函数而非多项式，这里会遇到什么困难？ | f∈K(X)是有理函数p/q，不是多项式。直接分析系数行不通，因为f可能不是多项式。需要先证明f实际上是多项式。 |
| 4 | 思维操作引导 | 0.6 | 写f=p/q，p,q∈K[X]互素。利用K[X]是PID的性质，从g·(p/q)^n∈A[X]⊂K[X]推导q满足什么条件？ | g·p^n/q^n∈K[X]意味着q^n|g·p^n在K[X]中。由gcd(p^n,q^n)=1（PID中互素元素的幂仍互素），得q^n|g ∀n≥0。g是固定非零多项式，deg有界，故q必须是常数即q∈K*，因此f∈K[X]。 |
| 5 | 思维操作引导 | 0.7 | 现在f=a_dX^d+...+a_0∈K[X]。考察g·f^n的首系数，能得到什么结论？ | g·f^n的首系数=lc(g)·a_d^n。因g·f^n∈A[X]，此首系数∈A ∀n≥0。即lc(g)·a_d^n∈A ∀n，这正是a_d几乎整于A的定义。由A完全整闭，a_d∈A。 |
| 6 | 推进 | 0.6 | 已证a_d∈A。如何处理剩余系数？ | 对次数归纳。令f'=f-a_dX^d，则f'∈K[X]且deg(f')<d。需证g·f'^n∈A[X]——更精确地，用类似首系数分析或直接展开g·f^n的各项系数，逐个提取几乎整条件。归纳得所有a_i∈A，故f∈A[X]。 |
| 7 | 能量传递引导 | 0.3 | 总结完整证明结构。 | 三步走：(1)PID互素性将K(X)归约到K[X]；(2)首系数分析+完全整闭性将最高次系数归入A；(3)对次数归纳，所有系数∈A。故f∈A[X]，A[X]完全整闭。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.4
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence
- structure_features: 整环A的多项式环A[X]保持完全整闭性质；需从K(X)中几乎整元素出发证明其属于A[X]；涉及分式域从K到K(X)的升维
- key_objects: ["domain A", "fraction field K", "polynomial ring A[X]", "rational function field K(X)", "almost integral element", "completely integrally closed property"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["structural_reduction", "coefficient_analysis", "induction_on_degree", "coprimality_argument"]
- primary_pattern: structural_reduction
- knowledge_required: ["almost integral elements", "completely integrally closed domains", "fraction field of polynomial ring", "PID property of K[X]", "coprimality in PID", "leading coefficient analysis"]
- key_insight: 用K[X]的PID互素性将K(X)中有理函数归约为多项式，再用首系数分析提取每个系数的几乎整性，最后对次数归纳

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 有理函数域K(X)中的几乎整性分析
- translation_to: 多项式系数在K中的逐个几乎整性分析
- translation_type: structural_transformation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "direct_manipulation", gap_type: "structural_transformation"}
- tell_small_concepts: ["almost integral", "completely integrally closed", "polynomial ring", "fraction field K(X)", "coprimality", "leading coefficient", "PID", "induction on degree"]
- expected_ai_method: direct_manipulation — bare AI可能直接用定义操作，试图在有理函数层面直接论证，不意识到需要先归约到多项式
- correct_method: structural_reduction via PID coprimality then coefficient-wise almost integrality induction

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=structural_existence, ai_method_type=direct_manipulation, gap_type=structural_transformation均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell
- [x] 无需进化

**拓扑进化建议**：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs详见profile.json中的tell_hint_pairs字段**
**全局pairs详见profile.json中的global_tell_hint_pairs字段**

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI很可能在有理函数层面直接操作定义，不意识到需要先用PID互素性将f从K(X)归约到K[X]。没有这一步归约，系数分析无法开始，证明卡在第一步。即使AI想到系数分析，也可能跳过"f是有理函数而非多项式"这一关键障碍。
- suitable_for_poc: ["POC-VMS-hint-injection", "POC-VMS-tell-detection", "POC-VMS-knowledge-bottleneck"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON，写入profile.json

**完成**：profile.json已写入 subagents-dirs/fate_000306/profile.json，包含所有必填字段。

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

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="396416"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000306"
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
    '_key': '396416',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000306',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000306')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [ ] 成功 / [ ] 失败
- 验证结果: [ ] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: fate_000306
- solution_method_type: structural_reduction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无，已有拓扑分类够用
- 是否遇到异常: 无

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
