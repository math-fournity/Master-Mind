# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2015p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2015P6.lean
- **来源**: USA 2015 P6
- **ArangoDB progress记录_key**: 329464（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2015P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Fix 0 < λ < 1, and let A be a multiset of positive integers. Let A_n = {a ∈ A : a ≤ n}. Assume that for every n ∈ ℕ, the multiset A_n contains at most nλ numbers. Show that there are infinitely many n ∈ ℕ for which the sum of the elements in A_n is at most n(n+1)/2 · λ.
- 解答核心思路（1-2句话）：反证法——假设只有有限个n满足不等式，定义"缺陷序列"x(n) = λn - |A_n| ≥ 0，通过Abel求和将求和不等式转化为"每个缺陷小于之前缺陷的平均值"，再利用A(n+1)是整数导致相邻缺陷差至少min(λ,1-λ)>0，证明这样的非负序列不可能存在（运行平均最终变负，与调和级数比较矛盾）。
- 解答关键步骤列表：
  1. 反证：假设只有有限个n满足，则∃N，所有n≥N+1违反不等式
  2. 定义缺陷序列x(n) = λn - |A_n| ≥ 0（由计数约束保证非负）
  3. Abel求和：A_n中元素之和 = (n+1)|A_n| - Σ_{k≤n} |A_k|
  4. 代入缺陷：反证假设推出 x(n) < 之前缺陷的平均值（对所有n≥N+1）
  5. 利用A(n+1)是整数：|x(n+1)-x(n)| = |λ - A(n+1)| ≥ min(λ,1-λ) = ε > 0
  6. 核心解析引理：非负序列满足x(n)<运行平均且相邻差≥ε → 矛盾（运行平均每两步下降ε/(n+2)，累加后与调和级数比较，平均最终变负）
  7. 应用核心引理 → 矛盾 → 证毕

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.3 | 描述这道题的结构：已知什么约束？要证明什么？A_n的定义是什么？ | 已知：多重集A，对每个n，A_n中元素个数≤nλ。要证：无穷多个n使得A_n中元素之和≤n(n+1)λ/2。A_n = {a∈A : a≤n}。这是一个密度约束下的求和不等式存在性问题。 |
| 2 | 自由列举 | 0.5 | 列出所有可能的证明方向：如何证明"有无穷多个n满足某个不等式"？ | 方向列举：(1)直接构造满足的n；(2)密度/遍历论证——如果只有有限个满足则矛盾；(3)反证法——假设只有有限个满足；(4)平均论证——用某种平均不等式；(5)Abel求和/分部求和；(6)解析方法——转化为序列性质。 |
| 3 | 小尝试 | 0.4 | 尝试直接构造：能否找到具体的n使得sum(A_n)≤n(n+1)λ/2？ | 尝试直接构造很困难——A是任意多重集，无法控制具体哪些n满足。计数约束只限制了个数，不直接控制求和。直接构造特定n的路径看起来走不通，因为A的结构太自由。 |
| 4 | 思维操作引导 | 0.7 | 考虑反证法：假设只有有限个n满足不等式。定义"缺陷序列"x(n) = λn - |A_n|（其中|A_n|是A_n的元素个数）。这个序列有什么性质？反证假设能推出什么？ | x(n) ≥ 0（由计数约束保证）。反证假设意味着对所有足够大的n，sum(A_n) > n(n+1)λ/2。需要将这个求和不等式与x(n)联系起来。 |
| 5 | 推进 | 0.6 | 用Abel求和（分部求和）将A_n中元素之和用|A_k|表示，然后代入x(k) = λk - |A_k|。你能得到关于x(n)和之前缺陷平均值的关系吗？ | Abel求和：sum(A_n中元素) = (n+1)|A_n| - Σ_{k=1}^{n} |A_k|。代入|A_k| = λk - x(k)，利用高斯求和Σk = n(n+1)/2，化简后得到：n·x(n) < Σ_{k=0}^{n-1} x(k)，即每个缺陷小于之前缺陷的平均值。 |
| 6 | 思维操作引导 | 0.8 | 现在需要证明这样的非负序列不可能存在。关键：A(n+1)是非负整数，所以x(n+1)-x(n) = λ - A(n+1)。这对相邻缺陷的差的绝对值意味着什么？如何由此推出矛盾？ | |x(n+1)-x(n)| = |λ - A(n+1)| ≥ min(λ, 1-λ) = ε > 0（因为A(n+1)是整数，λ∈(0,1)，所以距离最近的整数至少min(λ,1-λ)）。于是非负序列满足：每个项<运行平均 + 相邻差≥ε。运行平均每两步至少下降ε/(n+2)，累加后与发散的调和级数比较，平均最终变负——与非负性矛盾。 |
| 7 | 能量传递引导 | 0.5 | 将所有部分组装起来：反证假设→缺陷序列→Abel求和→缺陷低于平均→整数性保证步长≥ε→解析引理给出矛盾。证明完成。 | 完整逻辑链：反证→有限个n满足→大n违反不等式→定义缺陷x(n)≥0→Abel求和转化→x(n)<运行平均→整数性→步长≥ε→运行平均递减且与调和级数比较→平均变负→与非负矛盾→反证不成立→有无穷多个n满足。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: inequality_proof
- structure_features: 多重集密度约束（计数≤nλ）下的求和不等式存在性证明；需要证明无穷多个n满足；反证法将存在性转化为全局矛盾
- key_objects: 多重集A, 缺陷序列x(n)=λn-|A_n|, Abel求和, 运行平均, 调和级数, ε=min(λ,1-λ)

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["contradiction", "defect_sequence_construction", "abel_summation", "analytic_lemma_extraction", "harmonic_series_comparison", "integrality_exploitation"]
- primary_pattern: contradiction
- knowledge_required: ["Abel summation (分部求和)", "harmonic series divergence (调和级数发散)", "running average analysis (运行平均分析)", "multiset counting (多重集计数)", "Gauss sum formula"]
- key_insight: 定义缺陷序列x(n)=λn-|A_n|，反证假设迫使每个缺陷低于运行平均，而A(n+1)的整数性迫使相邻缺陷差≥min(λ,1-λ)>0，两者结合使运行平均最终变负——与非负性矛盾。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: combinatorial_counting (组合计数/多重集密度约束)
- translation_to: analytic_sequence_analysis (解析序列分析/运行平均与调和级数)
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "inequality_proof", ai_method_type: "direct_calculation", gap_type: "method_translation"}
- tell_small_concepts: ["defect sequence", "Abel summation", "running average", "harmonic series", "contradiction", "recurrent averages", "integrality step bound"]
- expected_ai_method: direct_calculation（裸AI预期会尝试直接构造满足的n或直接计算求和，不走反证+缺陷序列路线）
- correct_method: contradiction with defect sequence and analytic impossibility lemma

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=inequality_proof, ai_method_type=direct_calculation, gap_type=method_translation均可归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。已有拓扑分类足够。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

局部(tell, hint)对详见profile.json中tell_hint_pairs字段。
全局(tell, hint)对详见profile.json中global_tell_hint_pairs字段。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: 裸AI会尝试直接构造满足不等式的n，或用简单的密度/平均论证，但不会想到反证法+缺陷序列的翻译路线。即使想到反证法，也难以自行发现Abel求和将求和不等式转化为缺陷低于平均的关系，更难以发现利用整数性得到步长下界并用调和级数比较的解析引理。
- suitable_for_poc: ["tell_hint_injection", "path_feature_retrieval", "knowledge_bottleneck_detection", "method_translation_verification"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

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
2. 更新`problem_extraction_progress`集合中`_key="329464"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa2015p6"
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
    '_key': '329464',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa2015p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa2015p6')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_usa2015p6
- solution_method_type: contradiction_with_analytic_lemma
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，已有拓扑分类足够
- 是否遇到异常: 无

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
