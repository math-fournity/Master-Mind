# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2017p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2017P6.lean
- **来源**: USA 2017 P6
- **ArangoDB progress记录_key**: 329473（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2017P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Find the minimum possible value of a/(b³+4) + b/(c³+4) + c/(d³+4) + d/(a³+4), given that a,b,c,d are nonnegative real numbers such that a+b+c+d=4.
- 解答核心思路（1-2句话）：最小值为2/3，在(a,b,c,d)=(2,2,0,0)处取到。证明用切线 trick：对 1/(k³+4) 找线性下界 1/4 - k/12（在k=2处紧），求和后归约为约束循环积和 Σx_i·x_{i+1} ≤ 4，再用配对因式分解(x0+x2)(x1+x3) ≤ ((sum)/2)² = 4。
- 解答关键步骤列表：
  1. 验证(2,2,0,0)取到2/3：f = 2/(8+4) + 2/(0+4) + 0 + 0 = 1/6 + 1/2 = 2/3
  2. 关键引理：对k≥0，1/(k³+4) ≥ 1/4 - k/12。因为 12-(3-k)(k³+4) = k(k+1)(k-2)² ≥ 0
  3. 用引理对每项做线性下界：x_i/(x_{i+1}³+4) ≥ x_i/4 - x_i·x_{i+1}/12
  4. 求和：f ≥ Σ(x_i/4) - Σ(x_i·x_{i+1})/12 = 1 - Σ(x_i·x_{i+1})/12
  5. 循环积和上界：Σx_i·x_{i+1} = x0x1+x1x2+x2x3+x3x0 = (x0+x2)(x1+x3) ≤ ((x0+x1+x2+x3)/2)² = 4
  6. 最终：f ≥ 1 - 4/12 = 1 - 1/3 = 2/3

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.7 | 描述这道题的结构：表达式是什么形式？约束是什么？有什么对称性？ | 表达式是4个变量的循环和，每项形如 x_i/(x_{i+1}³+4)，约束为 x_i≥0 且 Σx_i=4。表达式具有循环对称性（不是完全对称），分母是三次多项式。 |
| 2 | 自由列举 | 0.8 | 列出所有可能的求解方向：哪些不等式技术可能适用于这个循环分数和的最小值问题？ | AM-GM、Cauchy-Schwarz（Titu引理）、切线trick（线性下界）、Lagrange乘数法、凸性分析、变量替换、Jensen不等式。 |
| 3 | 小尝试 | 0.5 | 试着直接对每项用AM-GM或Cauchy-Schwarz，看看能否得到有用的下界。 | 直接用AM-GM：b³+4 ≥ 某常数，但b³的变化范围太大（0到4），无法给出统一的好的下界。Cauchy-Schwarz（Titu）：Σx_i/(x_{i+1}³+4) ≥ (Σx_i)²/Σx_i(x_{i+1}³+4) = 16/Σx_i(x_{i+1}³+4)，但分母难以控制。直接方法不work。 |
| 4 | 思维操作引导 | 0.3 | 试试切线trick：对函数 g(k)=1/(k³+4) 找一个形如 α-βk 的线性下界，在某个k值处紧。先猜等号成立的点——什么样的(a,b,c,d)配置可能取最小值？ | 猜等号点：尝试简单配置。若所有变量相等，a=b=c=d=1，f=4/(1+4)=4/5=0.8。若(2,2,0,0)，f=2/12+2/4=1/6+1/2=2/3≈0.667，更小。所以猜等号在k=2处紧。构造 1/(k³+4) ≥ 1/4 - k/12：验证k=2时两边=1/12=1/12 ✓。证明：12-(3-k)(k³+4)=k(k+1)(k-2)²≥0 对k≥0成立。 |
| 5 | 推进 | 0.5 | 用这个线性下界对每项做估计，然后求和。表达式简化为什么？ | x_i/(x_{i+1}³+4) ≥ x_i·(1/4 - x_{i+1}/12) = x_i/4 - x_i·x_{i+1}/12。求和：f ≥ Σx_i/4 - Σ(x_i·x_{i+1})/12 = (Σx_i)/4 - (Σx_i·x_{i+1})/12 = 1 - (Σx_i·x_{i+1})/12。现在需要证明 Σx_i·x_{i+1} ≤ 4。 |
| 6 | 思维操作引导 | 0.3 | 现在需要证明循环积和 Σx_i·x_{i+1} = x0x1+x1x2+x2x3+x3x0 ≤ 4。试试把四项重新配对——能否因式分解？ | 展开 (x0+x2)(x1+x3) = x0x1+x0x3+x2x1+x2x3 = x0x1+x1x2+x2x3+x3x0 = Σx_i·x_{i+1}。所以 Σx_i·x_{i+1} = (x0+x2)(x1+x3)。由4ab≤(a+b)²，(x0+x2)(x1+x3) ≤ ((x0+x2+x1+x3)/2)² = (4/2)² = 4。 |
| 7 | 能量传递引导 | 0.6 | 合并所有结果，完成证明。验证等号在(2,2,0,0)处成立。 | f ≥ 1 - 4/12 = 1 - 1/3 = 2/3。等号条件：切线trick在k=2和k=0处紧（x_{i+1}=2或0时），且4ab=(a+b)²即x0+x2=x1+x3=2。(2,2,0,0)满足所有条件。证毕！ |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.7
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: inequality_proof
- structure_features: 循环和最小值问题，4变量循环分数和（分母为三次多项式），线性等式约束Σx_i=4，非负约束。循环对称性（非完全对称），等号在边界点(2,2,0,0)取到。
- key_objects: ["cyclic_sum_of_fractions", "cubic_denominator", "linear_constraint", "tangent_line_lower_bound", "cyclic_product_sum"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["tangent_line_trick", "decomposition", "cyclic_regrouping", "equality_case_analysis"]
- primary_pattern: tangent_line_trick
- knowledge_required: ["AM-GM inequality", "tangent line trick for function lower bounds", "cyclic sum manipulation", "polynomial factorization", "4ab ≤ (a+b)²"]
- key_insight: 对 1/(k³+4) 找在k=2处紧的线性下界 1/4-k/12，将分数最小值问题归约为循环积和上界问题，再用对角配对因式分解 (x0+x2)(x1+x3) ≤ 4 完成证明。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 直接分数最小值（对 x_i/(x_{i+1}³+4) 直接用不等式）
- translation_to: 线性下界 + 循环积和上界（切线trick将非线性分母线性化，归约为可处理的循环积和约束）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "inequality_proof", ai_method_type: "direct_calculation", gap_type: "method_translation"}
- tell_small_concepts: ["tangent_line_trick", "linear_lower_bound", "cyclic_product_sum", "opposite_index_pairing", "equality_case_at_boundary"]
- expected_ai_method: bare AI预期会直接对循环分数和用AM-GM或Cauchy-Schwarz，但三次分母导致无法给出统一的好的下界，直接方法失效
- correct_method: 切线trick找线性下界 + 循环积和对角配对因式分解

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=inequality_proof、ai_method_type=direct_calculation、gap_type=method_translation均可归入已有拓扑类别
- [x] 粒度一致——标注值与已有值粒度统一
- [x] 三个维度足够区分这道题的tell
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。已有拓扑分类足够覆盖此题。

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

**局部和全局tell_hint_pairs详见profile.json**

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会直接对循环分数和用AM-GM或Cauchy-Schwarz（Titu引理），但三次分母b³+4的变化范围太大（b从0到4），无法给出统一的好的下界。Cauchy-Schwarz后分母Σx_i(x_{i+1}³+4)难以控制。AI不会想到切线trick（对1/(k³+4)找线性下界），也不会想到将循环积和因式分解为(x0+x2)(x1+x3)。
- suitable_for_poc: ["tangent_line_trick_injection", "decomposition_guidance", "equality_case_guided_proof", "cyclic_regrouping_hint"]
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
2. 更新`problem_extraction_progress`集合中`_key="329473"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa2017p6"
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
    '_key': '329473',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa2017p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa2017p6')
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
- problem_id: compfiles_usa2017p6
- solution_method_type: tangent_line_trick
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3（2个path_feature型，1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，已有拓扑分类足够覆盖此题
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
