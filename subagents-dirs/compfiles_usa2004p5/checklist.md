# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2004p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2004P5.lean
- **来源**: USA 2004 P5
- **ArangoDB progress记录_key**: 329417（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2004P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Prove that for a, b, c > 0, (a⁵ - a² + 3)(b⁵ - b² + 3)(c⁵ - c² + 3) ≥ (a + b + c)³.
- 解答核心思路（1-2句话）：引入中间表达式 (a³+2)(b³+2)(c³+2) 作为桥梁：先证每个因子 x⁵-x²+3 ≥ x³+2（通过因式分解 (x-1)²(x+1)(x²+x+1) ≥ 0），再用三元Hölder不等式得 (a+b+c)³ ≤ (a³+2)(b³+2)(c³+2)，最后链式传递。
- 解答关键步骤列表：
  1. poly_bound: 证 x³+2 ≤ x⁵-x²+3（因式分解差为 (x-1)²(x+1)(x²+x+1) ≥ 0）
  2. poly_nonneg: 证 0 ≤ x⁵-x²+3（由 x³+2 ≥ 0 和 poly_bound 传递）
  3. multiplied_bound: 三个 poly_bound 相乘得 (a³+2)(b³+2)(c³+2) ≤ (a⁵-a²+3)(b⁵-b²+3)(c⁵-c²+3)
  4. triple_holder: 三元Hölder不等式 (Σf₁f₂f₃)³ ≤ (Σf₁³)(Σf₂³)(Σf₃³)
  5. key_holder: 取序列 f₁=(a,1,1), f₂=(1,b,1), f₃=(1,1,c) 得 (a+b+c)³ ≤ (a³+2)(b³+2)(c³+2)
  6. 链式传递: (a+b+c)³ ≤ (a³+2)(b³+2)(c³+2) ≤ (a⁵-a²+3)(b⁵-b²+3)(c⁵-c²+3)

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.2 | 描述题目结构：LHS乘积和RHS立方之间有什么关系？LHS每个因子取什么形式？ | LHS是三个形如x⁵-x²+3的五次多项式因子的乘积，RHS是(a+b+c)³。每个因子是单变量的五次多项式，RHS是三变量之和的立方。 |
| 2 | 自由列举 | 0.4 | 列出你所知的所有将和的立方与乘积联系起来的不等式技术。思考(a+b+c)³相对于乘积的结构。 | 可能的技术：AM-GM、Hölder不等式、Cauchy-Schwarz、幂平均不等式、直接展开、Jensen不等式。Hölder不等式特别相关，因为它直接将(乘积之和)³与立方之和的乘积联系起来。 |
| 3 | 小尝试 | 0.3 | 尝试直接展开乘积或对每个因子用AM-GM。结果如何？代数是否可控？ | 直接展开产生大量混合幂次高达15次的项，完全不可控。对单个因子用AM-GM不能明显联系到(a+b+c)³。此路不通。 |
| 4 | 思维操作引导 | 0.6 | 不要直接比较五次乘积和(a+b+c)³，寻找一个中间表达式：它同时≤每个五次因子，且其乘积能通过已知不等式与(a+b+c)³联系。什么更简单的多项式接近x⁵-x²+3？ | 观察x⁵-x²+3，x³+2可能可行，因为x³是Hölder的"自然"幂次。验证：x⁵-x²+3-(x³+2)=x⁵-x³-x²+1=(x-1)²(x+1)(x²+x+1)≥0对x>0成立。所以x³+2≤x⁵-x²+3。 |
| 5 | 推进 | 0.5 | 你已找到x³+2≤x⁵-x²+3。现在什么已知不等式给出(a+b+c)³≤(a³+2)(b³+2)(c³+2)？思考三元Hölder不等式。 | 三元Hölder不等式：(Σf₁ᵢf₂ᵢf₃ᵢ)³≤(Σf₁ᵢ³)(Σf₂ᵢ³)(Σf₃ᵢ³)。选择合适的序列应能在左边得到(a+b+c)，右边得到(a³+2)(b³+2)(c³+2)。 |
| 6 | 思维操作引导 | 0.5 | 应用三元Hölder不等式，选择{0,1,2}上的序列使左边产生(a+b+c)，右边产生(a³+2),(b³+2),(c³+2)。 | 取f₁=(a,1,1), f₂=(1,b,1), f₃=(1,1,c)。则Σf₁ᵢf₂ᵢf₃ᵢ=a+b+c，Σf₁ᵢ³=a³+2，同理f₂,f₃。故(a+b+c)³≤(a³+2)(b³+2)(c³+2)。 |
| 7 | 能量传递引导 | 0.3 | 将两个不等式链起来：(a+b+c)³≤(a³+2)(b³+2)(c³+2)≤(a⁵-a²+3)(b⁵-b²+3)(c⁵-c²+3)。完成了！ | 由传递性：(a+b+c)³≤(a³+2)(b³+2)(c³+2)≤(a⁵-a²+3)(b⁵-b²+3)(c⁵-c²+3)。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 2.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: inequality_proof
- structure_features: 三个相似五次多项式因子的乘积 ≥ 三正变量之和的立方；对称结构，每个因子形如 x⁵-x²+3
- key_objects: [五次多项式 x⁵-x²+3, 中间表达式 x³+2, 三元Hölder不等式, 多项式恒等式 (x-1)²(x+1)(x²+x+1)]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["bridge_intermediate", "inequality_chaining", "pattern_matching_to_known_inequality", "polynomial_factoring"]
- primary_pattern: bridge_intermediate
- knowledge_required: ["三元Hölder不等式", "多项式因式分解", "不等式乘法(mul_le_mul)", "多项式非负性"]
- key_insight: 引入中间表达式 (a³+2)(b³+2)(c³+2) 作为桥梁：证明每个因子 x⁵-x²+3 ≥ x³+2（差因式分解为 (x-1)²(x+1)(x²+x+1) ≥ 0），再用三元Hölder得 (a+b+c)³ ≤ (a³+2)(b³+2)(c³+2)

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: direct_comparison（直接比较五次乘积与和的立方）
- translation_to: bridge_through_intermediate（通过中间表达式桥接）
- translation_type: structural_transformation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: ["bridge_expression", "Hölder_inequality", "intermediate_bound", "polynomial_factoring", "inequality_chaining"]
- expected_ai_method: 直接展开五次多项式乘积并与(a+b+c)³比较，或对单个因子用AM-GM
- correct_method: 引入中间表达式(a³+2)(b³+2)(c³+2)，通过因式分解证x⁵-x²+3≥x³+2，应用三元Hölder不等式，然后链式传递

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=inequality_proof（已有）、ai_method_type=direct_calculation（已有）、gap_type=structural_transformation（已有），均可归入已有拓扑类别
- [x] 粒度一致——标注值与已有值粒度统一
- [x] 不需要新的拓扑维度——三个维度足以区分这道题的tell

**拓扑进化建议**：无，当前拓扑分类体系足够覆盖此题。

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

**局部pair拓扑详情**：
- R1: (inequality_proof, direct_calculation, method_problem_mismatch) — 纯元认知观察
- R2: (inequality_proof, enumeration_brute_force, search_space_estimation) — 自由列举
- R3: (inequality_proof, direct_calculation, method_problem_mismatch) — 小尝试
- R4: (inequality_proof, direct_manipulation, structural_transformation) — 思维操作引导
- R5: (inequality_proof, algebraic_identity, method_translation) — 推进
- R6: (inequality_proof, direct_calculation, knowledge_gap) — 思维操作引导（知识瓶颈）
- R7: (inequality_proof, logical_deduction, method_translation) — 能量传递引导

**全局pair详情**：
1. path_feature型: 两步桥接路径特征——完整证明需要通过(a³+2)(b³+2)(c³+2)桥接，局部步骤看不到全局桥接策略
2. implicit型: 多项式隐含分解——x⁵-x²+3隐含包含x³+2加非负余项，需要知道桥接目标才能发现此分解

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI会尝试直接展开五次多项式乘积或对单个因子用AM-GM，陷入代数复杂性中无法脱身。不会识别中间桥接表达式(a³+2)(b³+2)(c³+2)，也不会意识到需要三元Hölder不等式。没有桥接洞察，证明无法完成。
- suitable_for_poc: ["tell_extraction", "hint_injection", "bridge_identification"]
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
2. 更新`problem_extraction_progress`集合中`_key="329417"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa2004p5"
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
    '_key': '329417',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa2004p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa2004p5')
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
- problem_id: compfiles_usa2004p5
- solution_method_type: bridge_intermediate_inequality
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，当前拓扑分类体系（inequality_proof / direct_calculation / structural_transformation）足够覆盖此题
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
