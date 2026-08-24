# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003855
- **文件路径**: subagents-dirs/omni_math_003855/problem.lean
- **来源**: AoPS omni_math (imo_shortlist)
- **ArangoDB progress记录_key**: 333734（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003855/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：±1序列a_1,...,a_2022，每个a_i∈{+1,-1}。求最大C，使得对任意±1序列，存在k和索引1≤t_1<...<t_k≤2022，t_{i+1}-t_i≤2，且|Σa_{t_i}|≥C。
- 解答核心思路（1-2句话）：上界用构造(+1,-1,-1,+1)重复505次后接(+1,-1)验证max|sum|=506；下界用势函数F[i]=max(0,f[i])和G[i]=max(0,-g[i])证明每4个位置max(F,G)至少增长1，506个块共增长506。
- 解答关键步骤列表：
  1. 上界构造：pattern (+1,-1,-1,+1) 重复505次 + (+1,-1)，DP验证max|sum|=506
  2. 下界DP定义：f[i]=a_i+max(0,f[i-1],f[i-2])（最大和），g[i]=a_i+min(0,g[i-1],g[i-2])（最小和）
  3. 势函数定义：F[i]=max(0,f[i]), G[i]=max(0,-g[i])
  4. 分块论证：2022=4×505+2，505个4块+1个2块=506块
  5. 每块增长≥1的case analysis（p=0,4:增≥4; p=1,3:增≥2; p=2:max-of-two反消去保证增≥1）
  6. 结论：C=506

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：已知什么、约束什么、要求什么？gap≤2在子序列选择中意味着什么？ | 这是一个minimax问题：对任意±1序列求最大C使得存在gap≤2的子序列|sum|≥C。gap≤2意味着相邻选中元素间最多跳过1个，等价于未选元素不能连续2个。需要同时证上界（构造序列使max|sum|≤506）和下界（任意序列max|sum|≥506）。 |
| 2 | 自由列举 | 0.7 | 列出所有可能用来bound C的方法：上界构造和下界证明分别有哪些方向？ | 上界：尝试具体pattern（交替、常数、周期4等）并用DP验证max|sum|。下界：DP直接分析、分块+势函数、鸽巢原理、贪心走法。关键观察2022=4×505+2，506=⌈2022/4⌉暗示分块大小为4。 |
| 3 | 小尝试 | 0.5 | 试交替序列(+1,-1,+1,-1,...)，计算可达到的最大|sum|。 | 选所有奇数位（gap=2）得sum=1011，太大。交替序列不是好的上界构造，因为它允许选出所有同号元素。需要找一种pattern使得在任何gap≤2的子序列中正负贡献相互抵消。 |
| 4 | 思维操作引导 | 0.4 | 考虑将2022个位置分成4个一组。什么样的周期4的±1 pattern能最小化每块内可达到的最大|sum|？验证pattern (+1,-1,-1,+1) 的性质。 | (+1,-1,-1,+1)是平衡的：块内和为0，且对称结构使得DP值在块边界处增长缓慢。用DP f[i]=a_i+max(0,f[i-1],f[i-2])和g[i]=a_i+min(0,g[i-1],g[i-2])验证，重复505次后接(+1,-1)，max|f|和max|g|恰好=506。 |
| 5 | 推进 | 0.5 | 对pattern (+1,-1,-1,+1)×505+(+1,-1)，具体计算DP值，确认上界为506。 | 每个完整4块结束后dp值增加1（block j结束时dp[4j]=j, dn[4j]=-(j+1)）。505块后dp[2020]=505, dn[2020]=-506。最后两个位置(+1,-1)使dp[2021]=506, dn[2022]=-506。全局max|sum|=506，上界成立。 |
| 6 | 思维操作引导 | 0.4 | 下界证明：定义F[i]=max(0,f[i])和G[i]=max(0,-g[i])。证明在任意4个连续位置中max(F,G)至少增长1。 | 对4块中+1个数p做case analysis：p=0或4时增≥4；p=1或3时增≥2；p=2时（关键case），DP的max-of-two机制防止完全消去——一个-1导致的F下降不影响下一个+1的增量，因为max(f[i-1],f[i-2])保留了高水位。6种p=2排列逐一验证均增≥1。 |
| 7 | 能量传递引导 | 0.6 | 综合上下界：505个4块+1个2块=506块，每块增≥1，得max(F,G)≥506，即存在子序列|sum|≥506。结合上界构造得C=506。 | 2022=4×505+2自然分解为506块。下界：每块max(F,G)增≥1，506块后≥506。上界：(+1,-1,-1,+1) pattern给出max|sum|=506。因此C=506。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds: 4（R1纯元认知观察+R2自由列举+R5推进+R7能量传递引导）
- knowledge_rounds: 2（R4+R6思维操作引导）
- level_sum: 0.8+0.7+0.5+0.4+0.5+0.4+0.6=3.9
- knowledge_bottleneck: "R6"（势函数F/G及max-of-two反消去是核心知识瓶颈）
- thinking_bottleneck: "R4"（找到正确的周期4 pattern是核心思维瓶颈）

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: discrete_combinatorial
- structure_features: "±1序列长度2022，子序列gap≤2约束（等价于未选元素无连续2个），minimax问题（对任意序列求保证的最大|sum|），2022=4×505+2暗示分块大小4"
- key_objects: ["±1 sequence of length 2022", "gap-constrained subsequence (gap ≤ 2)", "DP recurrence f[i]=a_i+max(0,f[i-1],f[i-2])", "potential function F[i]=max(0,f[i]) and G[i]=max(0,-g[i])", "blocks of 4 positions", "pattern (+1,-1,-1,+1)"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["minimax duality (adversarial construction + universal proof)", "block decomposition (grouping into blocks of 4)", "potential function argument (F and G tracking max/min sums with floor at 0)", "DP formulation (skip-at-most-one subsequence as path with steps 1 or 2)", "case analysis on block composition (p=0,1,2,3,4 positives per block)", "max-of-two anti-cancellation insight"]
- primary_pattern: "block decomposition with potential function"
- knowledge_required: ["dynamic programming on sequences", "minimax / optimal value problems", "combinatorial constructions for upper bounds", "potential function / amortized analysis", "gap-constrained subsequence DP"]
- key_insight: "定义F[i]=max(0,f[i])和G[i]=max(0,-g[i])，DP的max-of-two机制保证每4个位置max(F,G)至少增长1，506个块给出506"

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: "combinatorial subsequence selection (which elements to pick with gap ≤ 2)"
- translation_to: "potential function dynamics (F and G tracking running max/min sums with floor at 0, block increment analysis)"
- translation_type: "method_translation"

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "case_by_case", gap_type: "structural_transformation"}
- tell_small_concepts: ["block decomposition", "potential function F and G", "gap constraint ≤ 2", "minimax duality", "DP with max-of-two", "pattern (+1,-1,-1,+1)", "max-of-two anti-cancellation"]
- expected_ai_method: "case_by_case"（bare AI会尝试枚举pattern或暴力DP，缺乏分块+势函数的结构性洞察）
- correct_method: "block decomposition with potential function"（关键是将序列分成4块并用F/G势函数证明每块增长≥1）

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——discrete_combinatorial/case_by_case/structural_transformation能准确描述这道题
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分——无需新维度
- [ ] 无需进化建议

**拓扑进化建议**：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "Bare AI会尝试暴力DP或枚举pattern，但缺乏分块+势函数的结构性洞察。上界可能尝试交替/常数序列得到过大的bound。下界无法发现max-of-two反消去机制，无法证明每块增长≥1。"
- suitable_for_poc: ["POC-VMS tell端验证：暴力DP与分块+势函数之间的method translation gap清晰", "POC-VMS hint端验证：分块+势函数的hint应显著提升AI表现"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

profile.json已写入 `subagents-dirs/omni_math_003855/profile.json`

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

## Step 10: 入库ArangoDB [ ]

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="333734"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_003855"
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
    '_key': '333734',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_003855',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_003855')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功
- 验证结果: [x] 通过（7 local pairs, 2 global pairs, answer=506, per-pair拓扑存在, why_not_visible_locally非None）

---

## Step 11: 汇报 [x]

- problem_id: omni_math_003855
- solution_method_type: structural_transformation（分块+势函数）
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1 path_feature + 1 implicit）
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，已有拓扑分类（discrete_combinatorial / case_by_case / structural_transformation）足够
- 是否遇到异常: problem.lean的solution文本被截断（仅11行），基于题目描述和answer=506独立重建了完整解答

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
