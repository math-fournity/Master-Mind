# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000264
- **文件路径**: subagents-dirs/fate_000264/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396374（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000264/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let p,q,r be three distinct primes, t a positive integer. G finite group, H normal subgroup with |G/H|=r^t. H has composition series length 2: {e}=H_0◁H_1◁H_2=H, H_1/H_0≅Z/pZ, H_2/H_1≅Z/qZ. G has composition series with Z/qZ at position i < j (Z/pZ). Show H has composition series length 2 with factors [Z/qZ, Z/pZ].
- 解答核心思路（1-2句话）：Use Schreier refinement theorem and Zassenhaus lemma to derive H's composition series from G's, preserving factor ordering. The distinctness of r from p,q ensures r-factors belong to G/H, so only Z/qZ and Z/pZ appear in H's series with Z/qZ first.
- 解答关键步骤列表：
  1. |H|=pq from given composition series; |G|=pq·r^t
  2. Consider subnormal series {e}◁H◁G and G's composition series
  3. Apply Schreier refinement theorem — both have equivalent refinements
  4. Apply Zassenhaus lemma — non-r factors of G's series contribute to H's composition series
  5. Since r≠p,q, all r-factors belong to G/H; only Z/pZ and Z/qZ contribute to H
  6. Since Z/qZ at position i < j (Z/pZ) in G's series, H's derived series has Z/qZ before Z/pZ
  7. Result: composition series of H length 2 with factors [Z/qZ, Z/pZ]. QED.

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
| 1 | 纯元认知观察 | 0.2 | What is the structure of this problem? Describe given conditions and what info each provides. | Identify |G/H|=r^t separates r-factors; G's series has Z/qZ before Z/pZ; H's series has Z/pZ before Z/qZ; goal is to swap H's ordering. |
| 2 | 自由列举 | 0.5 | List all theorems relating composition series of a group and its normal subgroup. | Jordan-Hölder, Schreier refinement, Zassenhaus lemma, Sylow theorems, correspondence theorem. Schreier+Zassenhaus are key for ordering transfer. |
| 3 | 小尝试 | 0.3 | Try Sylow theorems on H directly to show normal subgroup of order q. What happens when p>q and p≡1 mod q? | Works when p<q (n_q=1). Fails when p>q, p≡1 mod q (non-abelian case). Direct approach insufficient — need G's composition series info. |
| 4 | 思维操作引导 | 0.4 | Apply Schreier refinement theorem to {e}◁H◁G and G's composition series. What does refinement produce? | Both series have equivalent refinements. Refining {e}◁H◁G gives composition series of H + t copies of Z/rZ. G's series is already a composition series. |
| 5 | 思维操作引导 | 0.6 | Use Zassenhaus lemma to track which factors of G contribute to H. Why do r-factors not appear in H? | Non-r factors contribute to H. Since r≠p,q, r-factors belong to G/H. Z/qZ at position i<j gives Z/qZ before Z/pZ in H's derived series. |
| 6 | 推进 | 0.4 | Verify derived series has length 2 with factors [Z/qZ, Z/pZ]. Check r-factors belong to G/H. | |H|=pq → exactly 2 non-trivial factors. r-factors excluded (belong to G/H). Z/qZ from position i precedes Z/pZ from position j. Length 2 confirmed. |
| 7 | 能量传递引导 | 0.3 | Assemble complete proof: Schreier refinement + Zassenhaus + factor ordering. | Full proof: Schreier refinement → Zassenhaus → r-factors to G/H → Z/qZ before Z/pZ → composition series [Z/qZ, Z/pZ]. QED. |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 2.7
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R5
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R3

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence
- structure_features: Composition series with specified factor ordering; normal subgroup quotient constraint |G/H|=r^t with r distinct from p,q; ambient group composition series provides ordering information for subgroup's factors; three distinct primes create clean factor separation
- key_objects: finite group G, normal subgroup H, composition series, quotient groups Z/pZ/Z/qZ/Z/rZ, Schreier refinement theorem, Zassenhaus lemma, Jordan-Hölder theorem, subnormal series {e}◁H◁G

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["structural_analysis", "theorem_application", "refinement_argument", "factor_tracking", "counterexample_elimination"]
- primary_pattern: refinement_argument
- knowledge_required: ["Jordan-Hölder theorem", "Schreier refinement theorem", "Zassenhaus lemma (butterfly lemma)", "Sylow theorems", "composition series", "normal subgroups", "quotient groups", "group order and prime factorization"]
- key_insight: G's composition series induces a composition series on H via Schreier refinement, preserving the relative order of H's factors; the distinctness of r from p,q ensures clean separation of factors between H and G/H

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: Sylow-theoretic direct analysis of H's internal structure
- translation_to: Refinement-theoretic analysis via G's composition series and Zassenhaus lemma
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: method_translation}
- tell_small_concepts: ["composition series", "factor ordering", "Schreier refinement", "Zassenhaus lemma", "normal subgroup quotient", "Jordan-Hölder", "prime distinctness"]
- expected_ai_method: Direct Sylow analysis of H (|H|=pq), trying to show normal subgroup of order q exists without using G's composition series information
- correct_method: Schreier refinement theorem applied to G's composition series and the subnormal series {e}◁H◁G, using Zassenhaus lemma to track which factors belong to H and their ordering

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——structural_existence/direct_calculation/method_translation均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 不需要新的拓扑维度——三个维度足够区分
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

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI will likely try to use Sylow theorems directly on H (|H|=pq) to show a normal subgroup of order q exists. This works when p < q but fails when p > q and p ≡ 1 mod q (non-abelian case). The AI will not think to use G's composition series as a source of structural information about H, missing the Schreier refinement + Zassenhaus approach entirely. The key error is treating H in isolation rather than using the ambient group G's composition series ordering as a constraint.
- suitable_for_poc: ["POC-VMS-hint-injection", "POC-VMS-tell-detection", "POC-VMS-method-translation"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

完整JSON已写入 `subagents-dirs/fate_000264/profile.json`。所有字段已逐项检查，包括：
- _key=fate_000264, source_id=FATE-X-15, source_dataset=FATE-X, schema_version=3
- problem_text, solution_text, solution_summary, domain, subfield, answer_type, answer
- problem_type, solution_method_type, structure_features, key_objects
- thinking_patterns, primary_pattern, knowledge_required, key_insight
- translation_from/to/type, tell_topology, tell_small_concepts
- expected_ai_method, correct_method
- tell_hint_pairs (7对，每对含tell_topology和tell_small_concepts)
- global_tell_hint_pairs (2对，含why_not_visible_locally)
- bare_ai_expected, bare_ai_error_prediction, suitable_for_poc, discriminates_levels
- qa_sequence (7轮 + stats)
- analysis_metadata

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
2. 更新`problem_extraction_progress`集合中`_key="396374"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000264"
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
    '_key': '396374',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000264',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000264')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

- problem_id: fate_000264
- solution_method_type: refinement_argument
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无
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
