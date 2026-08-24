# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1992p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1992P6.lean
- **来源**: IMO 1992 P6
- **ArangoDB progress记录_key**: 329142（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1992P6.lean`（共1075行，分两段读完）

**产出**：
- 题目原文（数学描述）：For each positive integer n, S(n) is the greatest integer such that, for every positive integer k ≤ S(n), n² can be written as the sum of k positive squares. (a) Prove S(n) ≤ n²−14 for n ≥ 4. (b) Find n with S(n) = n²−14. (c) Prove infinitely many such n exist.
- 解答核心思路（1-2句话）：用"余量"(excess = n²−k)框架统一三部分——(a)余量13不能表示为3a+8b（因s_i∈{1,2,3}贡献{0,3,8}），矛盾；(b) n=13，用shift操作(4i²→(2i)²,计数减3)覆盖所有k≤155；(c)完全性的乘法闭包给出13^e无穷族。
- 解答关键步骤列表：
  1. (a) 反证法：假设S(n)>n²−14，则n²是n²−13个正平方和
  2. (a) 每个s_i<4（否则s_i²≥16使总和超过n²），故s_i∈{1,2,3}，对余量的贡献为{0,3,8}
  3. (a) 余量13=3a+8b无解（b=0: 13/3∉ℤ; b=1: 5/3∉ℤ），矛盾
  4. (b) n=13：shift操作4i²=(2i)²替换4个i为1个2i，保持平方和不变，计数减3
  5. (b) 对每个mod 3剩余类给出169的小k显式分解，再用shift扩展到所有k≤155
  6. (c) 乘法闭包：complete(n₁)∧complete(n₂)→complete(n₁n₂)，由平方和的乘性
  7. (c) 13完全→13^e完全（归纳），给出无穷多个n

---

## Step 2: QA序列分析——局部视角7步 [x]

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.7 | 描述这道题的结构。S(n)是什么？三个部分分别问什么？ | S(n)是使n²能写成k个正平方和的最大整数（对所有k≤S(n)成立）。Part(a)求上界，(b)求达到上界的例子，(c)求无穷多个这样的n。 |
| 2 | 自由列举 | 0.6 | 列出证明S(n)≤n²−14的可能方法。 | 反证法（假设S(n)>n²−14，则n²是n²−13个正平方和）；直接分析每个平方项的可能值；对余量做模运算。 |
| 3 | 小尝试 | 0.3 | 尝试把n²写成n²−13个正平方和。每个平方项至少为1给出什么约束？ | 每个s_i≥1，s_i²≥1，最小总和为n²−13。余量=n²−(n²−13)=13，需作为Σ(s_i²−1)分配。 |
| 4 | 思维操作引导 | 0.2 | 分类每个s_i的可能值。证明s_i<4并确定每个值对余量的贡献。 | 若s_i≥4则s_i²≥16，总和≥(n²−14)·1+16>n²，矛盾。故s_i∈{1,2,3}，贡献{0,3,8}。需13=3a+8b。 |
| 5 | 推进 | 0.3 | 检查13=3a+8b是否有非负整数解。这说明了什么？ | b=0: 13/3∉ℤ; b=1: 5/3∉ℤ。无解。矛盾，故S(n)≤n²−14。 |
| 6 | 思维操作引导 | 0.4 | 对part(b)，找一个保持平方和不变但改变项数的操作。如何用n=13？ | shift操作：4i²=(2i)²，4个i替换为1个2i，保持和不变，计数减3。n=13时对每个mod 3剩余类给出169的小k分解，再用shift覆盖所有k≤155。 |
| 7 | 能量传递引导 | 0.5 | 对part(c)，如何从n=13的基础情形得到无穷多个n？ | 乘法闭包：complete(n₁)∧complete(n₂)→complete(n₁n₂)（由平方和乘性）。13完全→13^e完全（归纳），无穷多个n。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.0
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: 4
- thinking_bottleneck（思维瓶颈在哪轮，或null）: 3

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization（刻画S(n)的性质并找到达到上界的n）
- structure_features: 三部分问题——(a)上界证明（反证法+余量模运算障碍），(b)显式构造达到上界（shift操作），(c)无穷族（乘法闭包）。统一参数是"余量"n²−k及其模表示性。
- key_objects: ["S(n)函数", "正平方和表示", "余量=n²−k", "shift操作4i²→(2i)²", "完全性S(n)=n²−14"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["contradiction（反证法）", "excess_decomposition（余量分解）", "modular_obstruction（模运算障碍）", "algebraic_identity_shift（代数恒等式shift）", "multiplicative_closure（乘法闭包）", "mathematical_induction（数学归纳）"]
- primary_pattern: excess_modular_analysis（余量模分析——用余量n²−k的模表示性统一三部分）
- knowledge_required: ["正平方和表示", "模运算", "Frobenius型表示问题（硬币问题）", "multiset操作", "数学归纳法", "平方和的乘性"]
- key_insight: 余量n²−k必须表示为3a+8b（由s_i∈{1,2,3}贡献{0,3,8}），而13是最小的不可表示余量——同时13本身是达到等式S(n)=n²−14的基础情形n值。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: direct_construction（直接构造——试图直接找到n²的k项正平方和表示）
- translation_to: excess_modular_analysis（余量模分析——将问题转化为余量n²−k的3a+8b表示性问题）
- translation_type: structural_transformation（结构变换——从"能否构造表示"翻译到"余量能否被分配"的模表示性问题）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: ["余量框架", "3a+8b模运算障碍", "shift操作4i²→(2i)²", "乘法闭包", "完全性"]
- expected_ai_method: bare AI会尝试直接构造n²的k项正平方和表示（枚举或贪心），不会识别余量框架和模运算障碍
- correct_method: 余量模分析——将问题转化为余量n²−k的3a+8b表示性问题；上界由不可表示性得到，构造由shift操作得到，无穷族由乘法闭包得到

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——characterization/direct_calculation/structural_transformation均可归入已有类别
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
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 2 个，implicit型: 1 个

**局部pairs摘要**：
| Round | tell | hint | level | situation_type | kb | topology |
|---|---|---|---|---|---|---|
| 1 | 看到三部分问题不知从何入手 | 描述结构：S(n)定义+三部分关系 | 0.7 | 纯元认知观察 | F | (characterization, direct_calculation, method_problem_mismatch) |
| 2 | 理解结构但不知如何证上界 | 列举方法：反证法/直接分析/模运算 | 0.6 | 自由列举 | F | (characterization, enumeration_brute_force, search_space_estimation) |
| 3 | 尝试直接构造但看不到障碍 | 每项≥1，余量=13需分配 | 0.3 | 小尝试 | F | (inequality_proof, direct_calculation, structural_transformation) |
| 4 | 有余量13但不知s_i取值范围 | s_i<4→{1,2,3}→贡献{0,3,8} | 0.2 | 思维操作引导 | T | (inequality_proof, case_by_case, knowledge_gap) |
| 5 | 有13=3a+8b但未检查可解性 | 检查无解→矛盾→上界 | 0.3 | 推进 | F | (inequality_proof, logical_deduction, method_problem_mismatch) |
| 6 | 需构造n但不知技术 | shift操作4i²→(2i)²+n=13 | 0.4 | 思维操作引导 | T | (structural_existence, algebraic_identity, knowledge_gap) |
| 7 | 有n=13但需无穷多 | 乘法闭包→13^e无穷族 | 0.5 | 能量传递引导 | F | (structural_existence, logical_deduction, method_translation) |

**全局pairs摘要**：
1. path_feature型：余量框架统一三部分（excess=n²−k作为统一参数）
2. implicit型：13的双重角色——障碍数=基础情形n值（observation_point=Q5）
3. path_feature型：shift操作作为构造与无穷族的桥梁

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接构造n²的k项正平方和表示（枚举或贪心方法），不会识别余量框架和模运算障碍（13=3a+8b无解）。会遗漏shift操作技术（4i²→(2i)²）和乘法闭包论证。
- suitable_for_poc: ["tell_hint_injection（注入余量框架tell）", "excess_framework_recognition（识别余量框架的翻译操作）", "shift_operation_discovery（发现shift操作的思维操作引导）"]
- discriminates_levels: true（这道题需要余量框架的翻译、模运算障碍的识别、shift操作的发现——三个不同层次的认知能力）

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
2. 更新`problem_extraction_progress`集合中`_key="329142"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1992p6"
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
    '_key': '329142',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1992p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1992p6')
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
- problem_id: compfiles_imo1992p6
- solution_method_type: excess_modular_analysis
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3（path_feature型2个，implicit型1个）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类（characterization/direct_calculation/structural_transformation等）足够覆盖
- 是否遇到异常: 否，入库和验证均一次通过

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
