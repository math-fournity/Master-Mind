# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000299
- **文件路径**: subagents-dirs/fate_000299/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396409（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000299/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let (A, m, K) be a complete local ring containing a field, and suppose that m is finitely generated over A. Then A is Noetherian. （Lean形式化：给定 R 是交换环、局部环、m-进完备，包含域 k 作为代数且 k→R 是单射（NoZeroSMulDivisors），m 有限生成，证明 R 是Noetherian环。）
- 解答核心思路（1-2句话）：利用 m 有限生成构造相伴分次环 gr_m(A) 为多项式环 k[x₁,...,xₙ] 的商，由Hilbert基定理得Noetherian，再由 m-进完备性将分次环的Noetherian性提升到 A 本身。
- 解答关键步骤列表：
  1. 设 m = (x₁,...,xₙ)，由 m 有限生成
  2. A 包含域 k，故 A/m ≅ k（或至少 A/m 是 k-代数），相伴分次环 gr_m(A) = ⊕ mⁿ/mⁿ⁺¹ 由 x̄₁,...,x̄ₙ 在 k 上生成
  3. gr_m(A) 是 k[x̄₁,...,x̄ₙ] 的商，由 Hilbert 基定理知 gr_m(A) Noetherian
  4. A 是 m-进完备且分离的，gr_m(A) Noetherian ⟹ A Noetherian（标准定理：完备分离 + Noetherian分次环 → Noetherian环）
  5. 注：Lean证明中 sorry 未填写，但数学证明路径如上

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**每轮必须标注**：
- **question**：给AI的提示/问题（Q）
- **expected_answer**：预期回复（A）
- **situation_type**：**⚠️ 只能取以下6个值之一，禁止自创**
- **level**：**⚠️ 必须是0-1之间的浮点数**

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.3 | 描述这道题的结构：已知条件有哪些？目标是什么？各条件之间的逻辑关系是什么？ | 已知：(1) A是局部环，有极大理想m；(2) A是m-进完备的；(3) A包含域k（k→A单射）；(4) m作为A的理想有限生成。目标：证明A是Noetherian环。逻辑关系：完备性+有限生成→Noetherian，"包含域"提供了系数域。 |
| 2 | 自由列举 | 0.5 | 列出所有能将"完备局部环+m有限生成"与"Noetherian"联系起来的可能方法。 | 可能方法：(a) 直接证明每个理想有限生成；(b) 用Cohen定理（若每个素理想有限生成则Noetherian）；(c) 用相伴分次环gr_m(A)；(d) 用m-进完备性将问题化归到截环A/mⁿ；(e) 用结构定理（完备局部环的结构定理）。 |
| 3 | 小尝试 | 0.4 | 尝试方法(a)：直接取A中任意理想I，用m-进完备性证明I有限生成。 | 取理想I，考虑I∩mⁿ。完备性给出I = lim(I/(I∩mⁿ))。但I/(I∩mⁿ)是A/mⁿ中的理想，A/mⁿ有限生成吗？需要mⁿ/mⁿ⁺¹有限生成——这需要m有限生成，但还没用到。直接方法卡在如何将m的有限生成性传递到A/mⁿ的Noetherian性上。 |
| 4 | 思维操作引导 | 0.6 | 放弃逐理想方法。考虑m-进滤过{mⁿ}，构造相伴分次环gr_m(A)=⊕mⁿ/mⁿ⁺¹。m有限生成对gr_m(A)意味着什么？A包含域k对gr_m(A)意味着什么？ | m=(x₁,...,xₙ)，则gr_m(A)由x̄₁,...,x̄ₙ在gr_m(A)₀=A/m上生成。A包含域k且k→A单射，故A/m是k-代数（实际上A/m≅k，因为m是极大理想且k嵌入A）。所以gr_m(A)是k[x̄₁,...,x̄ₙ]的商环。 |
| 5 | 思维操作引导 | 0.7 | gr_m(A)是k[x̄₁,...,x̄ₙ]的商。现在需要两步：(1) 证明gr_m(A) Noetherian；(2) 从gr_m(A) Noetherian + A完备推出A Noetherian。这两步分别用什么定理？ | (1) Hilbert基定理：k是域→k[x̄₁,...,x̄ₙ] Noetherian→其商gr_m(A) Noetherian。(2) 标准定理：若A是I-进完备且分离的，且gr_I(A) Noetherian，则A是Noetherian环。关键在于完备性允许从分次环的Noetherian性"提升"到原环。 |
| 6 | 推进 | 0.5 | 将以上各步组装成完整证明链，写出完整的论证。 | 完整链条：m=(x₁,...,xₙ) f.g. → gr_m(A)由n个元素在k=A/m上生成 → gr_m(A)是k[x₁,...,xₙ]的商 → Hilbert基定理→gr_m(A) Noetherian → A m-进完备+分离 → A Noetherian。QED。 |
| 7 | 能量传递引导 | 0.8 | 回顾整个证明，确认每一步的逻辑严密性。这个证明漂亮在哪里？ | 证明的精妙之处在于"分次环桥梁"：不直接处理A的理想，而是通过m-进滤过将问题转移到分次环，在分次环中有限生成性自然给出多项式环的商，Hilbert基定理直接适用，再由完备性将结论提升回来。完备性+包含域+m f.g.三个条件缺一不可。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.3+0.5+0.4+0.6+0.7+0.5+0.8 = 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: `characterization`（刻画完备局部环在何种条件下为Noetherian，是结构刻画型问题）
- structure_features: 给定三个结构性条件（局部环、m-进完备、包含域+m有限生成），推导一个全局性质（Noetherian）。证明需要通过中间结构（相伴分次环）作为桥梁，将局部信息（m有限生成）提升到全局结论。
- key_objects: 完备局部环(A, m, k)、极大理想m、相伴分次环gr_m(A)、多项式环k[x₁,...,xₙ]、m-进滤过{mⁿ}

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["结构桥梁法（通过中间结构传递性质）", "分次化降维（将环的问题转化为分次环问题）", "排除法（先试直接方法失败后转向间接方法）", "定理组装（Hilbert基定理+完备性提升定理）"]
- primary_pattern: 结构桥梁法（通过相伴分次环作为桥梁，将m的有限生成性传递到A的Noetherian性）
- knowledge_required: ["相伴分次环gr_m(A)的定义和性质", "Hilbert基定理", "m-进完备性和分离性", "完备+Noetherian分次环→Noetherian环的标准定理", "局部环和极大理想的基本性质"]
- key_insight: m有限生成→gr_m(A)是多项式环的商→Noetherian，完备性将分次环的Noetherian性提升到原环——"分次环桥梁"是关键转折

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 直接环论方法（逐理想证明有限生成）
- translation_to: 分次环方法（通过相伴分次环和m-进滤过间接证明）
- translation_type: structural_transformation（结构变换——将环的问题变换为分次环的问题，利用完备性做提升）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "direct_manipulation", gap_type: "knowledge_gap"}
- tell_small_concepts: ["相伴分次环", "m-进完备性", "Hilbert基定理", "有限生成理想", "Noetherian提升", "m-进滤过", "多项式环的商"]
- expected_ai_method: bare AI会尝试直接证明每个理想有限生成（direct_manipulation），试图用完备性直接处理理想，但不知道引入相伴分次环作为桥梁
- correct_method: 通过相伴分次环gr_m(A)间接证明：m f.g. → gr_m(A)是k[x₁,...,xₙ]的商 → Hilbert基定理 → gr_m(A) Noetherian → 完备性提升 → A Noetherian

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=characterization、ai_method_type=direct_manipulation、gap_type=knowledge_gap均能归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分——这道题的核心gap是"不知道相伴分次环这个工具"（knowledge_gap），bare AI会用direct_manipulation，正确方法需要结构变换
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。现有分类体系可以覆盖此题。

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

**局部pairs详见profile.json**

**全局pairs**：
1. (path_feature) 完整证明链：m f.g. → gr_m(A)是k[x₁,...,xₙ]的商 → Hilbert基定理 → Noetherian → 完备性提升 → A Noetherian。why_not_visible_locally: 每个局部步骤只看到一个环节，无法看到"分次环桥梁"这个完整路径特征——需要同时看到"为什么要构造分次环"和"为什么完备性能提升回来"才能理解整个策略。
2. (implicit) "A包含域k"蕴含A/m≅k是域，使得gr_m(A)₀是域，从而gr_m(A)是域上多项式环的商，Hilbert基定理可用。why_not_visible_locally: "包含域"这个条件在局部步骤中只被当作"有一个系数域"，其深层作用——保证A/m是域从而使分次环的零次部分是Noetherian——只有在构造分次环并分析其结构时才显现。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接证明A中每个理想有限生成，或试图用Cohen定理（素理想有限生成→Noetherian），但不知道引入相伴分次环作为桥梁。即使知道完备性的定义，也无法将"m有限生成"与"完备性"这两个条件通过分次环连接起来。核心知识缺口是"完备+Noetherian分次环→Noetherian环"这个标准定理。
- suitable_for_poc: ["POC-VMS-hint（hint端验证：注入分次环方向后能否引导AI完成证明）", "POC-VMS-tell（tell端验证：从AI的thinking中识别出'未考虑分次环'的分叉信号）"]
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

## Step 10: 入库ArangoDB [x]

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="396409"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000299"
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
    '_key': '396409',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000299',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000299')
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
