# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2021p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2021P6.lean
- **来源**: IMO 2021 P6
- **ArangoDB progress记录_key**: 329262（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2021P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let m ≥ 2 be an integer, A a finite set of integers (not necessarily positive) and B₁, B₂, ... Bₘ subsets of A. Suppose that for every k = 1, 2, ..., m, the sum of the elements of Bₖ is m^k. Prove that A contains at least m/2 elements.
- 解答核心思路（1-2句话）：反证法。假设|A| < m/2，将子集包含关系编码为关联矩阵，用Siegel引理找到一个小范数非零整数零向量t（|t_k| < m），将零空间关系翻译为Σ t_k·m^k = 0，由m进制表示唯一性推出所有t_k = 0，与t ≠ 0矛盾。
- 解答关键步骤列表：
  1. 反证假设：2|A| < m
  2. 定义关联矩阵M[a,k] = 1 if a ∈ B_k，M有|A|行m列，行数<列数
  3. 应用Siegel引理：存在非零整数向量t，|t_k| < m，使M·t = 0（即对每个a∈A，Σ_k [a∈B_k]·t_k = 0）
  4. 利用子集和条件Σ_{b∈B_k} b = m^(k+1)和关联关系，推导出Σ_k t_k·m^(k+1) = 0
  5. 提取公因子m：m·Σ_k t_k·m^k = 0，故Σ_k t_k·m^k = 0
  6. 由于|t_k| < m对所有k成立，这是m进制下0的表示，系数绝对值严格小于m，强制所有t_k = 0
  7. 与t ≠ 0矛盾，故2|A| ≥ m

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 请描述这道题的结构：已知什么、未知什么、约束条件是什么？特别注意子集和m^k这个条件的形式。 | 已知：有限整数集合A，m个子集B₁...Bₘ⊆A，每个B_k的元素和为m^k。未知：证明|A| ≥ m/2。约束：m≥2，A中元素可负，子集不必互斥。关键观察：子集和构成等比数列m^1, m^2, ..., m^m。 |
| 2 | 自由列举 | 0.7 | 要证明|A| ≥ m/2这个下界，你能想到哪些可能的方法方向？请尽可能多地列举。 | 方向可能包括：直接计数论证、线性代数方法、生成函数、反证法、概率方法、多项式方法、数论方法（利用m^k的结构）等。 |
| 3 | 小尝试 | 0.5 | 试试直接计数的方法：能否通过分析每个B_k需要多少不同元素来得到下界？ | 直接计数困难：元素可以在多个B_k之间共享，且元素可以是负数，所以无法简单地从子集和的大小推断子集大小，进而推断|A|。负元素的存在使得求和约束几乎不限制元素个数。此路不通。 |
| 4 | 思维操作引导 | 0.4 | 将子集包含关系编码为矩阵：定义关联矩阵M，其中M[a,k]=1当且仅当a∈B_k。这个矩阵有多少行多少列？如果|A|<m/2，矩阵的行数和列数有什么关系？ | M是|A|×m的0-1矩阵。如果|A|<m/2<m，则行数<列数，这是一个"矮胖"的矩阵，行数严格小于列数，因此零空间非平凡——存在非零向量t使M·t=0。 |
| 5 | 推进 | 0.5 | 既然M·t=0有非零整数解，我们需要对t的分量大小有所控制。什么样的整数线性代数定理能保证存在范数有界的非零整数零向量？ | 需要某种"小范数零向量存在性"定理。普通的线性代数只保证零空间非平凡，但不控制解的大小。需要更精细的数论/几何数论工具来保证存在分量有界的整数解。 |
| 6 | 思维操作引导 | 0.3 | Siegel引理：对于整数矩阵M∈Z^{r×s}（r<s），存在非零整数向量t∈Z^s使M·t=0且|t_k|≤(c·‖M‖)^{r/(s-r)}。在我们的情形下，‖M‖≤1（0-1矩阵），且2|A|<m意味着|A|/(m-|A|)<1，因此|t_k|<m。请用这个引理。 | 由Siegel引理，存在非零整数向量t，|t_k|<m对所有k，且对每个a∈A有Σ_k [a∈B_k]·t_k=0。这个关联关系是关键的桥梁。 |
| 7 | 推进 | 0.4 | 现在利用关联关系Σ_k [a∈B_k]·t_k=0和子集和条件Σ_{b∈B_k} b=m^(k+1)，推导出关于t和m的幂的等式。然后分析这个等式能推出什么。 | 由关联关系和子集和条件交换求和顺序：Σ_k t_k·m^(k+1) = Σ_k t_k·Σ_{b∈B_k} b = Σ_{a∈A} a·(Σ_k [a∈B_k]·t_k) = 0。提取公因子m得Σ_k t_k·m^k=0。由于|t_k|<m，这是m进制下0的表示且系数绝对值严格小于m，故所有t_k=0，与t≠0矛盾。 |
| 8 | 能量传递引导 | 0.6 | 整个证明已经完成：反证假设→Siegel引理给出小范数零向量→关联关系翻译为幂等式→m进制唯一性强制t=0→矛盾。请总结这个证明的核心美感。 | 证明的精妙之处在于三重翻译：组合结构→线性代数（关联矩阵）→数论（m进制表示）。Siegel引理是连接线性代数和数论的桥梁，它保证零向量足够"小"使得m进制唯一性适用。整个论证一气呵成。 |

**统计**：
- total_rounds: 8
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5（R1+R2+R5+R7+R8）
- knowledge_rounds（思维操作引导的轮数）: 2（R4+R6）
- level_sum: 0.8+0.7+0.5+0.4+0.5+0.3+0.4+0.6 = 4.2
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: `discrete_combinatorial`
- structure_features: ["有限整数集合A与m个子集B_k", "子集和构成等比数列m^1, m^2, ..., m^m", "子集不必互斥，元素可为负", "目标是集合基数的下界", "组合约束+数论结构（m的幂）的混合问题"]
- key_objects: ["有限整数集合A", "子集族B_1,...,B_m", "关联矩阵M", "Siegel引理零向量t", "m进制表示"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["反证法", "结构编码（组合→矩阵）", "Siegel引理应用（存在性+界控制）", "求和交换（关联关系→幂等式翻译）", "m进制表示唯一性", "矛盾收束"]
- primary_pattern: "contradiction_via_siegel_lemma_and_base_m_uniqueness"
- knowledge_required: ["Siegel引理（几何数论）", "m进制表示唯一性", "线性代数（欠定系统零空间）", "关联矩阵", "反证法"]
- key_insight: "将子集包含关系编码为关联矩阵后，Siegel引理给出分量|m|以内的非零零向量，关联关系翻译为m的幂的等式后，m进制唯一性强制零向量为零——矛盾。三重翻译（组合→线性代数→数论）是核心。"

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: "组合子集和约束（B_k的元素和为m^k）"
- translation_to: "线性代数零空间问题 + 数论m进制表示唯一性"
- translation_type: "structural_transformation"

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "knowledge_gap"}
- tell_small_concepts: ["incidence matrix", "Siegel's lemma", "null vector", "base-m representation", "subset sum", "contradiction", "bounded coefficients", "underdetermined system"]
- expected_ai_method: "直接计数论证或基本线性代数——尝试从子集和大小推断子集大小，但忽略负元素和共享元素的复杂性；即使想到线性代数也不知道Siegel引理"
- correct_method: "反证法+Siegel引理（有界零向量）+m进制表示唯一性——三重翻译：组合→线性代数→数论"

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——discrete_combinatorial / enumeration_brute_force / knowledge_gap 均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell
- [ ] 无需新拓扑维度

**拓扑进化建议**：无。已有拓扑分类体系可以很好地覆盖本题。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 8 对
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 1 个，implicit型: 2 个

**局部pairs详见profile.json中的tell_hint_pairs字段**

**全局pairs详见profile.json中的global_tell_hint_pairs字段**：

1. path_feature型：完整证明路径"反证→Siegel引理→关联翻译→m进制唯一性→矛盾"作为整体路径特征，在局部视角中不可见——没有任何单步能揭示Siegel引理的界与m进制唯一性的组合会产生矛盾。
2. implicit型（observation_point=R4）：关联矩阵作为组合到线性代数的桥梁，在题目中不出现，在局部步骤中不可见。
3. implicit型（observation_point=R7）：子集和m^k与m进制表示之间的隐含联系，只在求和交换后才显现。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "Bare AI会尝试直接计数论证或基本线性代数。直接计数失败因为元素可负可共享；即使想到线性代数（零空间非平凡），也不知道Siegel引理来控制零向量范数；即使偶然得到幂等式，也可能不识别m进制唯一性。这是一道IMO P6级别的难题，需要非常专业的几何数论知识。"
- suitable_for_poc: ["tell_hint_validation", "knowledge_bottleneck_detection", "method_translation_identification", "structural_transformation_recognition"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON，写入 `profile.json`

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
- [x] answer
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
- [x] tell_hint_pairs（8个局部pair，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（3个全局pair，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象）
- [x] analysis_metadata

**已写入 `subagents-dirs/compfiles_imo2021p6/profile.json`**

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
2. 更新`problem_extraction_progress`集合中`_key="329262"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2021p6"
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
    '_key': '329262',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2021p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2021p6')
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
- problem_id: compfiles_imo2021p6
- solution_method_type: siegel_lemma_contradiction
- 局部(tell,hint)对数量: 8
- 全局(tell,hint)对数量: 3（1个path_feature + 2个implicit）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否。已有拓扑分类体系（discrete_combinatorial / enumeration_brute_force / knowledge_gap等）可完整覆盖本题。
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
