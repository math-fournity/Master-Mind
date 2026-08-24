# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000251
- **文件路径**: subagents-dirs/fate_000251/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396361（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000251/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let G be a finite group and L a maximal subgroup of G. Suppose L is non-Abelian and simple. Then there exist at most two minimal normal subgroups in G.
- 解答核心思路（1-2句话）：利用极大性给出二分法（每个极小正规子群N要么N≤L即N=L，要么N∩L={e}且G=NL），然后分L◁G和L≁G两种情况用反证法。L≁G时用Burnside定理推出|N|=|L|不是素数幂从而N非交换且Z(N)={e}，第三个极小正规子群被困在Z(N1)×Z(N2)={e}中；L◁G时用正规交集论证限制最多一个N=L和一个N≰L。
- 解答关键步骤列表：
  1. 二分法：N≤L（推出N=L）或N∩L={e}且G=NL
  2. 情形1（L≁G）：所有N满足|N|=|G|/|L|，两个N1,N2中心化彼此且G=N1N2
  3. 第三个N3 ≤ Z(N1)×Z(N2)
  4. Burnside定理：|L|非素数幂 → N非交换 → Z(N)={e} → N3={e}，矛盾
  5. 情形2（L◁G）：至多一个N=L，至多一个N≰L（正规交集论证），总计≤2

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
| 1 | 纯元认知观察 | 0.8 | Describe the structure of this problem. What are the given objects, what are we trying to prove, and what type of result is this? | We have a finite group G with a maximal subgroup L that is non-abelian and simple. We need to prove G has at most 2 minimal normal subgroups. This is a structural bound theorem in finite group theory. |
| 2 | 自由列举 | 0.7 | List all relevant facts and tools about maximal subgroups, minimal normal subgroups, and simple groups that might help. | (1) Minimal normal subgroups are characteristically simple. (2) Distinct minimal normal subgroups centralize each other. (3) Maximality gives dichotomy N≤L or G=NL. (4) L simple means normal subgroups of L are trivial or L. (5) Burnside's p^a q^b theorem: |L| not a prime power. |
| 3 | 小尝试 | 0.5 | Try a direct approach: assume three minimal normal subgroups N1, N2, N3 exist and try to derive a contradiction using just definitions. | For each Ni, either Ni ≤ L (forcing Ni = L by simplicity) or Ni ∩ L = {e} and G = NiL. At most one can equal L. But stuck on how to get a contradiction from the remaining ones. |
| 4 | 思维操作引导 | 0.4 | For N∩L={e} and G=NL, compute |N|. For two such N1,N2, determine structure of G=N1N2. | |N|=|G|/|L|. N1N2∩L ◁ L so it's {e} or L. If {e}, |N1N2L|>|G|, contradiction. So G=N1N2 and |N2|=|L|. |
| 5 | 推进 | 0.5 | For a third N3: since G=N1N2 and N3◁G, where must N3 live? Use centralization property. | N3 ≤ G = N1×N2 (direct product). N3 centralizes N1 and N2, so N3 ≤ Z(N1)×Z(N2). Need to determine Z(N1). |
| 6 | 思维操作引导 | 0.3 | What is |N1|? Is N1 abelian or non-abelian? Use Burnside's p^a q^b theorem. | |N1|=|L|, not a prime power by Burnside. So N1 non-abelian, Z(N1)={e}. Similarly Z(N2)={e}. N3≤{e}, contradiction. |
| 7 | 能量传递引导 | 0.6 | Handle the case L◁G and conclude the proof. | At most one N=L. For N≰L: |N|=|G/L|, G/L simple. Two such N2,N3 give N2N3∩L ◁ L non-trivial and proper, contradicting L simple. Total ≤ 2. QED. |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R6
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
- problem_type: structural_existence
- structure_features: 有限群与非交换单极大子群；对极小正规子群数量的结构界；反证法+情形分裂（L是否正规）
- key_objects: ["finite group G", "maximal subgroup L", "non-abelian simple group L", "minimal normal subgroups", "Burnside p^a q^b theorem"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["proof_by_contradiction", "case_splitting", "counting_argument", "structural_classification", "knowledge_application"]
- primary_pattern: case_splitting
- knowledge_required: ["minimal normal subgroups are characteristically simple", "distinct minimal normal subgroups centralize each other", "maximality gives dichotomy N≤L or G=NL", "Burnside's p^a q^b theorem", "non-abelian simple groups have trivial center", "elementary abelian groups have prime power order"]
- key_insight: Burnside's p^a q^b theorem forces |L| to not be a prime power, which makes minimal normal subgroups with |N|=|L| non-abelian and hence centerless, trapping any third minimal normal subgroup in Z(N1)×Z(N2)={e}

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: group-theoretic structural analysis
- translation_to: order arithmetic with Burnside's theorem
- translation_type: structural_to_arithmetic

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: logical_deduction, gap_type: knowledge_gap}
- tell_small_concepts: ["maximality dichotomy", "centralization of minimal normal subgroups", "Burnside p^a q^b theorem", "case split on L normal", "center trapping argument"]
- expected_ai_method: direct manipulation of subgroup definitions and Lagrange's theorem without invoking Burnside's theorem or the centralization property
- correct_method: case split on L◁G vs L≁G with contradiction using centralization, order counting, and Burnside's theorem

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ → 是，structural_existence/logical_deduction/knowledge_gap都能归入已有类别
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ → 是，与已有值粒度一致
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ → 是，三个维度足够。不同轮次的pair有不同的拓扑（R1是method_problem_mismatch，R2/R6是knowledge_gap，R3/R4/R5是structural_transformation，R7是method_problem_mismatch），能区分
- [x] 如果发现拓扑分类需要进化，在此写出建议： → 无需进化

**拓扑进化建议**（如有）：无，当前拓扑分类足够

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs摘要**：
- R1: (纯元认知观察, level=0.8) tell=AI看到群论问题但未识别关键结构性质 → topology=(structural_existence, logical_deduction, method_problem_mismatch)
- R2: (自由列举, level=0.7) tell=AI知道定义但未连接相关群论事实 → topology=(structural_existence, enumeration_brute_force, knowledge_gap)
- R3: (小尝试, level=0.5) tell=AI尝试反证法但二分法后卡住 → topology=(structural_existence, logical_deduction, structural_transformation)
- R4: (思维操作引导, level=0.4) tell=AI有二分法但未见计数论证 → topology=(structural_existence, direct_calculation, structural_transformation)
- R5: (推进, level=0.5) tell=AI有G=N1N2但不知N3在哪 → topology=(structural_existence, logical_deduction, structural_transformation)
- R6: (思维操作引导, level=0.3) tell=AI有N3≤Z(N1)×Z(N2)但不知Z(N1)是否平凡（知识瓶颈） → topology=(structural_existence, direct_calculation, knowledge_gap), is_knowledge_bottleneck=true
- R7: (能量传递引导, level=0.6) tell=AI处理了L≁G但未处理L◁G → topology=(structural_existence, case_by_case, method_problem_mismatch)

**全局pairs摘要**：
- path_feature型: 证明需要L◁G vs L≁G的情形分裂，从任何单步不可见 → topology=(structural_existence, case_by_case, structural_transformation)
- implicit型: Burnside定理作为隐藏关键成分，在R6处不可见 → topology=(structural_existence, direct_calculation, knowledge_gap)

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI will likely attempt direct manipulation of subgroup definitions and Lagrange's theorem without knowing Burnside's p^a q^b theorem or the centralization property of distinct minimal normal subgroups. It will miss the case split on L◁G vs L≁G, and will be unable to determine whether Z(N1) is trivial, getting stuck at the center trapping step. It may also fail to see the counting argument that forces G = N1N2.
- suitable_for_poc: ["tell_hint_injection", "knowledge_bottleneck_detection", "case_split_completeness"]
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
- [x] answer（proof类型填要证明的结论）
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

**将完整JSON写入工作目录的 `profile.json` 文件** → 已写入 subagents-dirs/fate_000251/profile.json

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
2. 更新`problem_extraction_progress`集合中`_key="396361"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000251"
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
    '_key': '396361',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000251',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000251')
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
- problem_id: fate_000251
- solution_method_type: case_analysis_with_contradiction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，当前拓扑分类足够覆盖此题
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
