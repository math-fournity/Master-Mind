# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1979p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1979P5.lean
- **来源**: IMO 1979 P5
- **ArangoDB progress记录_key**: 329092（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1979P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：找出所有实数a，使得存在非负实数x1,x2,x3,x4,x5满足：
  - x1 + 2x2 + 3x3 + 4x4 + 5x5 = a
  - x1 + 2³x2 + 3³x3 + 4³x4 + 5³x5 = a²
  - x1 + 2⁵x2 + 3⁵x3 + 4⁵x4 + 5⁵x5 = a³
- 解答核心思路（1-2句话）：对三个方程做线性组合 a²·(eq1) - 2a·(eq2) + (eq3)，利用 k·(a-k²)² = a²·k - 2a·k³ + k⁵ 得到 Σ k·(a-k²)²·xk = 0，每项非负故每项为零，推出a∈{0,1,4,9,16,25}。
- 解答关键步骤列表：
  1. 构造线性组合 a²·h₁ + h₃ - 2a·h₂，得到 (a-1)²x1 + 2(a-4)²x2 + 3(a-9)²x3 + 4(a-16)²x4 + 5(a-25)²x5 = 0
  2. 由xi≥0和(a-k²)²≥0，每项k·(a-k²)²·xk≥0，和为0故每项为0
  3. 推出每个xi要么为0要么a=对应k²，故a∈{0,1,4,9,16,25}
  4. 反向验证：a=0时全取0；a=k²时取xk=k,其余为0，逐一验证

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 请描述这道题的结构：已知什么、未知什么、三个方程的系数有什么规律？ | 三个方程的系数分别是k, k³, k⁵（k=1..5），右边是a, a², a³。未知是a的取值集合和对应的非负xi。系数的幂次和右边的幂次形成对应关系。 |
| 2 | 自由列举 | 0.7 | 列出所有可能用来处理"三方程五未知数+非负约束"的方法方向 | 1)直接解线性方程组（3方程5未知，欠定）；2)消元法；3)尝试特殊值；4)利用非负性构造不等式；5)寻找三个方程之间的代数恒等式组合；6)用矩/加权和方法 |
| 3 | 小尝试 | 0.4 | 试试直接把这三个方程当作线性方程组来解，看看能得到什么 | 3个方程5个未知数，系统欠定，无法唯一确定xi。但可以表示部分xi为自由变量的函数。非负约束限制了可行域，但直接解无法给出a的所有可能值。这条路不够有效。 |
| 4 | 思维操作引导 | 0.6 | 注意三个方程系数的幂次是1,3,5，右边幂次是1,2,3。请尝试找到一个关于a的线性组合系数(α,β,γ)，使得α·(eq1)+β·(eq2)+γ·(eq3)能把每个变量的系数变成完全平方形式。提示：想想k·(a-k²)²展开后是什么 | k·(a-k²)² = k·a² - 2k³·a + k⁵ = a²·k - 2a·k³ + k⁵。所以取α=a², β=-2a, γ=1，线性组合a²·(eq1) - 2a·(eq2) + (eq3)就得到Σ k·(a-k²)²·xk = 0 |
| 5 | 推进 | 0.5 | 你得到了Σ k·(a-k²)²·xk = 0。现在利用xi≥0的性质，能推出什么结论？ | 每项k·(a-k²)²·xk中，k>0, (a-k²)²≥0, xk≥0，所以每项≥0。和为0意味着每项都必须为0。因此对每个k，要么xk=0要么a=k²。 |
| 6 | 推进 | 0.4 | 既然每个xk要么为0要么a=k²，而a的值由非零xi决定，请确定a的所有可能值 | 如果所有xi=0，则a=0。如果某个xk≠0，则a=k²，即a∈{1,4,9,16,25}。但需要验证这些值确实可行。 |
| 7 | 能量传递引导 | 0.3 | 验证a=0和a=k²都能找到对应的非负xi，然后总结答案 | a=0: 全取xi=0。a=1: x1=1,其余0，验证1+0+0+0+0=1, 1+0=1, 1+0=1 ✓。a=4: x2=2, 验证2·2=4, 2·8=16=4², 2·32=64=4³ ✓。类似验证a=9,16,25。最终答案a∈{0,1,4,9,16,25}。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5
- knowledge_rounds（思维操作引导的轮数）: 1
- level_sum: 0.8+0.7+0.4+0.6+0.5+0.4+0.3 = 3.7
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: 4
- thinking_bottleneck（思维瓶颈在哪轮，或null）: 4

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: constraint_satisfaction
- structure_features: 三方程五未知数的欠定线性系统，系数幂次为1,3,5，右边幂次为1,2,3，变量有非负约束，求参数a的所有可行值
- key_objects: 非负实数变量x1..x5，参数a，系数k的幂k¹,k³,k⁵，完全平方(a-k²)²

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["结构观察——识别系数幂次1,3,5与右边幂次1,2,3的对应关系", "代数恒等式构造——寻找线性组合使系数变为完全平方", "非负性利用——和为零且每项非负则每项为零", "枚举验证——逐一验证可行值"]
- primary_pattern: 代数恒等式构造（通过线性组合将方程组转化为非负项之和为零的形式）
- knowledge_required: ["线性组合/加权求和", "完全平方展开", "非负数之和为零的性质", "幂次运算"]
- key_insight: 识别k·(a-k²)² = a²·k - 2a·k³ + k⁵，从而用a²·(eq1) - 2a·(eq2) + (eq3)将三方程组合为非负项之和为零

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 线性方程组直接求解（将三方程视为独立的线性约束）
- translation_to: 代数恒等式构造+非负性论证（通过加权线性组合将方程组转化为非负项之和为零）
- translation_type: method_translation（方法翻译：从直接求解翻译为恒等式构造）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: constraint_satisfaction, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: ["幂次对应关系", "线性组合系数选择", "完全平方展开", "非负项之和为零", "欠定系统"]
- expected_ai_method: 直接将三方程视为线性方程组求解，尝试消元或代入，因欠定而无法确定a的所有值
- correct_method: 构造线性组合a²·(eq1)-2a·(eq2)+(eq3)利用代数恒等式k·(a-k²)²将方程组转化为非负项之和为零

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——constraint_satisfaction/direct_calculation/structural_transformation均可归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无

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

**局部pairs详见profile.json中的tell_hint_pairs字段**

**全局pairs详见profile.json中的global_tell_hint_pairs字段**

全局pair 1 (path_feature): 完整路径特征——从"欠定线性系统"到"代数恒等式构造"的翻译路径，局部视角只能看到方程组欠定，看不到幂次对应关系可以构造完全平方。
全局pair 2 (implicit): 蕴含信息——系数幂次1,3,5与右边幂次1,2,3的对应关系蕴含了k·(a-k²)²的恒等式，这个蕴含在局部步骤中不可见，需要整体观察三方程的结构。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接解线性方程组或尝试特殊值代入，但无法发现a²·(eq1)-2a·(eq2)+(eq3)的线性组合技巧。可能尝试数值方法搜索a的范围，但无法给出完整的解集{0,1,4,9,16,25}。可能遗漏a=0的情况或无法证明完备性。
- suitable_for_poc: ["POC-VMS-8 hint端验证——验证线性组合hint能否引导AI发现恒等式", "POC-VMS-9 tell端验证——验证从直接求解到恒等式构造的翻译tell能否被识别", "tell+hint联合验证——测试完整(tell,hint)对能否引导bare AI从欠定系统走向非负项之和为零"]
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
2. 更新`problem_extraction_progress`集合中`_key="329092"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1979p5"
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
    '_key': '329092',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1979p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1979p5')
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
- problem_id: compfiles_imo1979p5
- solution_method_type: algebraic_identity
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类（constraint_satisfaction/direct_calculation/structural_transformation等）足够覆盖
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
