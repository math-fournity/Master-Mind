# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000304
- **文件路径**: subagents-dirs/fate_000304/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396414（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000304/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设 M 是环 R 上的模。M 是"稳定自由"的，如果存在一个有限生成自由模 F 使得 M⊕F 是自由模。证明：如果 M 是稳定自由的且不是有限生成的，那么 M 是自由的。形式化版本为 iff：在 ¬Module.Finite R M 条件下，Module.Free R M ↔ IsStablyFree R M。
- 解答核心思路（1-2句话）：正向（free→stably free）取 N=0 平凡。反向利用 M 非有限生成迫使 M⊕N 具有无穷秩 κ，而无穷秩自由模可吸收有限直和项（R^κ ≅ R^κ ⊕ R^n），通过 Eilenberg swindle 推出 M⊕R^κ ≅ R^κ，进而 M ≅ R^κ 即 M 自由。
- 解答关键步骤列表：
  1. 正向：M 自由 → 取 N=0（有限生成自由模）→ M⊕0=M 自由 → stably free
  2. 反向：M stably free → ∃ N 有限生成自由, M⊕N 自由
  3. M 非有限生成 + N 有限生成 → M⊕N 非有限生成 → M⊕N ≅ R^κ, κ 无穷
  4. 无穷秩吸收：R^κ ≅ R^κ ⊕ R^n（N≅R^n），故 M⊕R^n ≅ R^κ ⊕ R^n
  5. Eilenberg swindle：M⊕R^n⊕R^κ ≅ R^κ⊕R^κ ≅ R^κ，而 R^n⊕R^κ ≅ R^κ，故 M⊕R^κ ≅ R^κ
  6. 迭代分解：R^κ = M₁⊕F₁, F₁≅R^κ → F₁=M₂⊕F₂ → ... → R^κ ≅ (⊕∞ M) ⊕ R^κ
  7. 结合 M⊕R^κ ≅ R^κ 与无穷吸收推出 M ≅ R^κ，即 M 自由

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：已知条件是什么？要证明什么？iff的两个方向分别是什么难度？ | 已知：M是stably free（∃有限生成自由模N使M⊕N自由），M不是有限生成的。要证：M自由。iff正向（free→stably free）平凡，取N=0即可。反向（stably free+非fg→free）是核心难点。 |
| 2 | 自由列举 | 0.7 | 对于反向方向，列出你能想到的所有可能证明路径。 | (1)直接从M⊕N的基构造M的基；(2)利用M是自由模的直和项→投射模→再证自由；(3)分析M⊕N的秩，利用无穷秩性质；(4)Eilenberg swindle；(5)Kaplansky定理分解投射模；(6)消去定理（cancellation）... |
| 3 | 小尝试 | 0.5 | 尝试路径(1)：M⊕N有基B，N有限生成所以N包含在有限个基元素的张成中。能否直接从剩余基元素得到M的基？ | M⊕N≅R^κ有基B。N有限生成，N⊂span(B₀)，B₀有限。B\B₀张成的自由子模R^{B\B₀}与N交集为0，故注入M。但这只说明M包含一个秩κ的自由子模，不能直接推出M自由——M可能是R^κ⊕P其中P是有限生成投射但非自由的。此路不通。 |
| 4 | 思维操作引导 | 0.4 | 关键转折：M非有限生成这个条件起了什么作用？分析M⊕N的秩，然后利用无穷秩自由模的性质。 | M非fg + N有限生成 → M⊕N非fg → M⊕N≅R^κ其中κ是无穷基数。关键性质：对无穷κ，R^κ ≅ R^κ ⊕ R^n（无穷秩吸收有限直和项）。因此M⊕R^n ≅ R^κ ≅ R^κ ⊕ R^n。非有限生成条件迫使κ无穷，使吸收引理可用。 |
| 5 | 思维操作引导 | 0.5 | 现在用Eilenberg swindle：从M⊕R^n≅R^κ出发，两侧加R^κ，利用R^κ⊕R^κ≅R^κ和R^n⊕R^κ≅R^κ，推导M⊕R^κ≅R^κ。 | M⊕R^n≅R^κ。两侧加R^κ：M⊕R^n⊕R^κ ≅ R^κ⊕R^κ ≅ R^κ（无穷κ满足κ+κ=κ）。而R^n⊕R^κ≅R^κ（有限加无穷=无穷），故M⊕R^κ≅R^κ。这意味着M是R^κ的直和项且补项同构于R^κ。 |
| 6 | 推进 | 0.6 | 从M⊕R^κ≅R^κ出发，通过迭代分解推出M≅R^κ。 | R^κ=M₁⊕F₁, M₁≅M, F₁≅R^κ。对F₁重复：F₁=M₂⊕F₂, M₂≅M, F₂≅R^κ。迭代得R^κ≅(⊕∞M)⊕R^κ。又M⊕R^κ≅R^κ，故M是R^κ的直和项且补项≅R^κ。结合R^κ≅R^κ⊕R^κ和迭代结构，M的秩=κ且M作为无穷秩自由模的直和项具有自由性，最终M≅R^κ即M自由。 |
| 7 | 能量传递引导 | 0.8 | 你已经掌握了所有关键步骤。现在组装完整证明，处理iff两个方向。 | 正向：M自由→取N=0→M⊕0=M自由→stably free✓。反向：M stably free→∃N fg free, M⊕N自由→M非fg+N fg→M⊕N非fg→rank=κ无穷→R^κ≅R^κ⊕R^n→Eilenberg swindle: M⊕R^κ≅R^κ→迭代分解→M≅R^κ→M自由✓。QED。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.8+0.7+0.5+0.4+0.5+0.6+0.8 = 4.3
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R3"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence
- structure_features: iff结构（双向蕴含），正向平凡反向非平凡；核心难点在于利用"非有限生成"条件触发无穷秩吸收机制；涉及模的直和分解与基数算术
- key_objects: ["stably free module M", "finitely generated free module N/F", "free module R^κ of infinite rank", "direct sum M⊕N", "infinite cardinal κ"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["rank_analysis", "infinite_cardinal_arithmetic", "eilenberg_swindle", "direct_sum_decomposition", "condition_activation"]
- primary_pattern: infinite_cardinal_arithmetic
- knowledge_required: ["stably free modules", "free modules of infinite rank", "cardinal arithmetic for infinite sets (κ+n=κ, κ+κ=κ)", "Eilenberg swindle", "direct sum decomposition of modules", "projective vs free modules"]
- key_insight: M非有限生成迫使M⊕N有无穷秩κ，而无穷秩自由模可吸收有限直和项（R^κ≅R^κ⊕R^n），通过Eilenberg swindle推出M⊕R^κ≅R^κ进而M≅R^κ即M自由

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 有限生成模理论（投射模、stably free的有限秩直觉）
- translation_to: 无穷秩模理论配合基数算术（无穷吸收引理、Eilenberg swindle）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_manipulation, gap_type: knowledge_gap}
- tell_small_concepts: ["infinite rank absorption", "Eilenberg swindle", "non-finite generation", "cardinal arithmetic", "direct summand", "stably free"]
- expected_ai_method: bare AI会尝试直接从M⊕N的基构造M的基（direct_manipulation），或止步于"M是自由模的直和项→投射模"而无法推进到自由
- correct_method: 利用非有限生成条件触发无穷秩分析，通过无穷秩吸收引理和Eilenberg swindle推出M≅R^κ

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——structural_existence/direct_manipulation/knowledge_gap能归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell
- 拓扑进化建议：无。已有分类体系可覆盖此题。

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

**局部pairs摘要**：
- R1: tell=AI未识别iff双向结构, hint=描述题目结构, level=0.8, 纯元认知观察, topology=(structural_existence, direct_manipulation, method_problem_mismatch), concepts=[iff structure, stably free definition]
- R2: tell=AI未列举出无穷秩路径, hint=列出所有可能方向, level=0.7, 自由列举, topology=(structural_existence, enumeration_brute_force, search_space_estimation), concepts=[rank analysis, Eilenberg swindle, Kaplansky theorem]
- R3: tell=AI尝试直接构造基但卡住, hint=试直接构造基, level=0.5, 小尝试, topology=(structural_existence, direct_calculation, method_problem_mismatch), concepts=[basis construction, finite subset, free submodule]
- R4: tell=AI未利用非fg条件分析秩, hint=分析M⊕N的秩利用无穷性质, level=0.4, 思维操作引导, is_knowledge_bottleneck=True, topology=(structural_existence, direct_calculation, knowledge_gap), concepts=[infinite rank, cardinal arithmetic, absorption lemma]
- R5: tell=AI不知道Eilenberg swindle, hint=用swindle推导M⊕R^κ≅R^κ, level=0.5, 思维操作引导, is_knowledge_bottleneck=True, topology=(structural_existence, direct_calculation, knowledge_gap), concepts=[Eilenberg swindle, direct sum, infinite absorption]
- R6: tell=AI需从swindle结果推出M≅R^κ, hint=迭代分解推出结论, level=0.6, 推进, topology=(structural_existence, logical_deduction, method_translation), concepts=[iterative decomposition, direct summand, rank equality]
- R7: tell=AI需组装完整证明, hint=组装两方向证明, level=0.8, 能量传递引导, topology=(structural_existence, logical_deduction, method_translation), concepts=[iff proof, forward direction, backward direction]

**全局pairs摘要**：
- G1 (path_feature): tell=完整路径"非fg→无穷秩→吸收→swindle→自由"是一个不可分割的推理链, hint=识别非有限生成条件作为触发无穷秩分析的关键激活信号, level=0.7, generalizability=high, why_not_visible_locally=在任意单步中只能看到局部操作（如加R^κ到两侧），看不到整个推理链为何必须从"非fg"出发才能走通——缺少非fg条件时整条路径不成立
- G2 (implicit): tell=Eilenberg swindle本身是一种隐含的元方法——不是从题目结构直接读出的, hint=当面对A⊕B≅F且F无穷秩时系统性地考虑"加F到两侧"的swindle操作, level=0.6, generalizability=high, why_not_visible_locally=在局部步骤中"两侧加R^κ"看起来是任意的代数操作，其作为swindle的元模式不可见——只有从全局视角才能识别这是一种可泛化的推理范式

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会止步于"M是自由模的直和项→投射模"，无法从投射模推进到自由模。或者尝试直接从M⊕N的基构造M的基，但无法处理"对角"嵌入的情况。关键缺失：不知道无穷秩吸收引理和Eilenberg swindle，无法利用"非有限生成"条件触发无穷秩分析。
- suitable_for_poc: ["POC-VMS hint端验证（bare fail → tree pass）", "tell端去特化验证（knowledge_gap拓扑匹配）", "Eilenberg swindle作为implicit tell的泛化性验证"]
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
- [x] answer（**⚠️ 必填，不能为None**）
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
2. 更新`problem_extraction_progress`集合中`_key="396414"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000304"
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
    '_key': '396414',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000304',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000304')
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
