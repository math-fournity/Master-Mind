# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2007p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2007P6.lean
- **来源**: IMO 2007 P6
- **ArangoDB progress记录_key**: 329203（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2007P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设n为正整数，S = {(x,y,z) : x,y,z ∈ {0,1,...,n}, x+y+z > 0}是三维空间中(n+1)³-1个点的集合。求最少的平面数，使其并集包含S但不包含原点(0,0,0)。
- 解答核心思路（1-2句话）：答案是3n。上界用3n个坐标平面x_i=k构造；下界用多项式方法——平面方程的乘积给出在S上消失但原点非零的多项式B，构造辅助网格多项式A，用Combinatorial Nullstellensatz证明deg(B)≥3n。
- 解答关键步骤列表：
  1. 上界构造：3n个平面x_i=k（i=1,2,3, k=1,...,n），覆盖S且不过原点
  2. 下界翻译：m个平面的方程乘积B，deg(B)=m，B在S上消失，B(0)≠0
  3. 构造辅助多项式A = ∏∏(x_i - k)，deg(A)=3n，(n,n,n)系数为1
  4. 构造P = A - (A(0)/B(0))·B，P在整个网格上消失
  5. P在x_1^n x_2^n x_3^n处系数为1（若deg(B)<3n）
  6. Combinatorial Nullstellensatz给出矛盾：P应在网格某处非零
  7. 结论：m ≥ 3n，答案为3n

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
| 1 | 纯元认知观察 | 0.8 | S的结构是什么？原点排除施加了什么约束？什么数学对象能自然编码"一组覆盖点的平面"？ | S是{0,...,n}³去掉原点，含(n+1)³-1个点。需要平面的并集包含S但排除原点。每个平面是线性方程，原点排除意味着没有平面过原点。 |
| 2 | 自由列举 | 0.7 | 列出所有你能想到的方法。不仅考虑组合方法，也考虑代数方法——能否将覆盖条件代数化编码？ | 直接计数、归纳、线性代数、代数方法（平面是线性多项式，乘积在因子零点处为零）、多项式次数论证 |
| 3 | 小尝试 | 0.3 | 试直接方法：能否数每个平面覆盖多少网格点，由此导出下界？哪里出了问题？ | 平面最多覆盖O(n²)个网格点，(n+1)³-1个点给出约n的下界，远弱于3n。平面重叠复杂，原点排除是全局约束，局部计数无法捕捉。 |
| 4 | 思维操作引导 | 0.4 | 每个平面由线性多项式定义。若平面P_1,...,P_m覆盖S，乘积B=P_1·...·P_m有什么性质？B在哪里消失？在哪里不消失？ | B在S上消失（至少一个因子为零），B(0)≠0（无平面过原点），deg(B)=m。得到次数为m、在S上消失但原点非零的多项式。 |
| 5 | 推进 | 0.5 | 你现在有B：deg(B)=m，B(0)≠0，B在S上消失。需证m≥3n。什么多项式定理能给出网格上消逝多项式的次数下界？ | 需要Combinatorial Nullstellensatz：若多项式P在网格上消逝但有特定非零系数，则P在网格某处非零。用逆否命题：若P在整个网格上消逝，其次数必须足够大。 |
| 6 | 思维操作引导 | 0.3 | 构造A=∏∏(x_i-k)。deg(A)是多少？x_1^n x_2^n x_3^n系数是多少？令P=A-(A(0)/B(0))·B，P的该单项系数是多少？对P在网格{0,...,n}³上用CNS。 | deg(A)=3n，系数为1。若deg(B)<3n，B在该单项系数为0，故P系数为1。P在整个网格上消逝（S上A和B都消逝，原点处P(0)=0）。但CNS说P应在网格某处非零——矛盾！ |
| 7 | 能量传递引导 | 0.6 | P在整个网格上消逝，但x_1^n x_2^n x_3^n系数为1，CNS说P应在网格某处非零。矛盾——所以deg(B)≥3n，即m≥3n。完成了！ | 矛盾表明m<3n不可能。结合上界3n个平面的构造，答案恰为3n。证明优雅地结合了多项式翻译、辅助多项式构造和CNS。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.6
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

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
- problem_type: discrete_combinatorial
- structure_features: 离散网格{0,...,n}³去掉原点；求最少平面数覆盖所有非原点网格点同时排除原点；上界由显式构造给出，下界由代数多项式方法给出
- key_objects: 网格点{0,...,n}³, 原点(0,0,0), 平面（线性多项式）, 乘积多项式B, 辅助网格多项式A, Combinatorial Nullstellensatz

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["combinatorial_to_algebraic_translation", "polynomial_method", "combinatorial_nullstellensatz", "degree_counting", "contradiction_argument"]
- primary_pattern: combinatorial_to_algebraic_translation
- knowledge_required: ["Combinatorial Nullstellensatz", "multivariate polynomial degree theory", "plane equations as linear polynomials", "product of polynomials and vanishing sets"]
- key_insight: 将几何覆盖问题翻译为多项式代数：平面方程的乘积给出在S上消失但原点非零的多项式B，然后用Combinatorial Nullstellensatz证明其次数至少为3n

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: geometric plane covering（几何平面覆盖）
- translation_to: polynomial algebra (vanishing ideals, degree bounds via Combinatorial Nullstellensatz)（多项式代数：消逝理想、通过CNS的次数界）
- translation_type: geometric_to_algebraic（几何到代数）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: discrete_combinatorial, ai_method_type: direct_calculation, gap_type: method_translation}
- tell_small_concepts: ["grid point covering", "plane product polynomial", "Combinatorial Nullstellensatz", "degree lower bound", "origin exclusion", "auxiliary grid polynomial"]
- expected_ai_method: 直接计数或对n归纳，试图用组合论证说明需要多少平面覆盖网格点
- correct_method: 多项式方法+Combinatorial Nullstellensatz：平面方程乘积给出消逝多项式，辅助网格多项式+系数论证+CNS证明次数下界3n

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 可以，discrete_combinatorial/direct_calculation/method_translation均已存在
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 一致，均为抽象级别
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化

**拓扑进化建议**（如有）：无。现有拓扑分类完全够用。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

详见profile.json中的tell_hint_pairs和global_tell_hint_pairs字段。每个pair均包含tell_topology和tell_small_concepts。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI会尝试直接组合计数或对n归纳，试图通过论证每个平面能覆盖多少网格点来导出下界。这种方法会卡住，因为平面之间的重叠和原点排除约束的交互难以用组合方式捕捉——平面的朝向不同覆盖的点数不同，原点排除创造了局部计数无法捕捉的全局约束。多项式方法和Combinatorial Nullstellensatz不太可能在没有具体引导的情况下被考虑到，因为从几何覆盖到多项式消逝的翻译是非显然的方法选择。
- suitable_for_poc: ["tell_hint_injection", "knowledge_bottleneck_detection", "method_translation_verification"]
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
- [x] answer（"3n"）
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

**将完整JSON写入工作目录的 `profile.json` 文件** → 已写入 `subagents-dirs/compfiles_imo2007p6/profile.json`

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
2. 更新`problem_extraction_progress`集合中`_key="329203"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2007p6"
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
    '_key': '329203',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2007p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2007p6')
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
- problem_id: compfiles_imo2007p6
- solution_method_type: polynomial_method
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有拓扑分类（discrete_combinatorial / direct_calculation / method_translation / knowledge_gap / structural_transformation / algebraic_identity / logical_deduction / case_by_case / enumeration_brute_force）完全够用，粒度一致。
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
