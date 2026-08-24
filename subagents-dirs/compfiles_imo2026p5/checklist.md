# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2026p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2026P5.lean
- **来源**: IMO 2026 P5
- **ArangoDB progress记录_key**: 329288（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2026P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：求所有函数 f: ℝ_{>0} → ℝ_{>0}，使得对任意 x, y ∈ ℝ_{>0}，有 √((x²+f(y)²)/2) ≥ (f(x)+y)/2 ≥ √(x·f(y))。这是一个双侧不等式，左边是 QM(x,f(y)) ≥ AM(f(x),y)，右边是 AM(f(x),y) ≥ GM(x,f(y))，但变量交叉耦合。
- 解答核心思路（1-2句话）：将两个不等式平方后，代入 x=f(y) 夹逼得到迭代关系 f(f(y))=2f(y)-y，从而轨道为等差数列；定义缺陷 g(x)=f(x)-x，证明 g≥0 且所有正缺陷值相等，再用球密度论证证明零缺陷与正缺陷不能共存，最终得出 f(x)=x+c (c≥0)。
- 解答关键步骤列表：
  1. 平方两个不等式：4xf(y) ≤ (f(x)+y)² ≤ 2(x²+f(y)²)（hB, hA引理）
  2. 代入 x=f(y) 夹逼：(f(f(y))+y)² = (2f(y))²，得 f(f(y))=2f(y)-y（fcomp引理）
  3. 归纳得轨道公式 f^n(y) = y + n·(f(y)-y)（orbit引理）
  4. 由正性约束证明缺陷 g(y)=f(y)-y ≥ 0（g_nonneg引理）
  5. 用轨道点代入交叉不等式，通过floor逼近构造矛盾，证明所有正缺陷值相等（cross, absurd_lt, eq_of_pos引理）
  6. 球引理：零缺陷附近 √(2d·t) 范围内的点缺陷也为零（ball引理）
  7. 递升引理：从零缺陷点出发，用球链覆盖所有更大的点（ascend引理）
  8. 零缺陷与正缺陷不能共存（zero_contra引理）
  9. 结论：f(x)=x+c, c≥0（验证充分性用 nlinarith）

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
| 1 | 纯元认知观察 | 0.3 | 观察这个双侧不等式 √((x²+f(y)²)/2) ≥ (f(x)+y)/2 ≥ √(x·f(y))，描述它的结构。左边、中间项、右边分别是什么类型的均值？变量如何耦合？ | 左边 √((x²+f(y)²)/2) 是 x 和 f(y) 的QM（二次均值），中间 (f(x)+y)/2 是 f(x) 和 y 的AM（算术均值），右边 √(x·f(y)) 是 x 和 f(y) 的GM（几何均值）。结构是 QM ≥ AM ≥ GM，但变量交叉耦合：左边和右边用 (x, f(y))，中间用 (f(x), y)。 |
| 2 | 自由列举 | 0.5 | 列出所有可能的研究方向来处理这个函数不等式系统。 | (1) 试特值如 f(x)=x, f(x)=x+c, f(x)=kx；(2) 两边平方消根号；(3) 代入特殊值 x=y 或 y=f(x)；(4) 研究 f 的迭代 f(f(y))；(5) 定义缺陷 g(x)=f(x)-x 并分析其性质；(6) 利用正性约束 f: ℝ_{>0}→ℝ_{>0} 限制轨道行为。 |
| 3 | 小尝试 | 0.2 | 试试直接代入 x=y，看看能得到什么信息。 | 代入 x=y 得 √((x²+f(x)²)/2) ≥ (f(x)+x)/2 ≥ √(x·f(x))。右边是 AM≥GM 恒成立，左边是 QM≥AM 恒成立。所以 x=y 不给出任何非平凡信息——这是死路。需要尝试非对称代入。 |
| 4 | 思维操作引导 | 0.6 | 将两个不等式两边平方消除根号，然后用 x=f(y) 代入消元，看看能否得到 f 的迭代关系。 | 平方得 4xf(y) ≤ (f(x)+y)² ≤ 2(x²+f(y)²)。代入 x=f(y)：下界 4f(y)f(y) ≤ (f(f(y))+y)²，上界 (f(f(y))+y)² ≤ 2(f(y)²+f(y)²)=4f(y)²。两个界都是 4f(y)²，所以 (f(f(y))+y)²=4f(y)²，即 f(f(y))+y=2f(y)（取正根），得 f(f(y))=2f(y)-y。 |
| 5 | 推进 | 0.5 | 从 f(f(y))=2f(y)-y 出发，定义缺陷 g(x)=f(x)-x，推导 g 的性质。 | 迭代关系意味着 g(f(y))=g(y)（缺陷沿轨道不变）。归纳得 f^n(y)=y+n·g(y)，轨道是公差为 g(y) 的等差数列。因为 f^n(y)∈ℝ_{>0} 对所有 n 成立，若 g(y)<0 则 n 充分大时 f^n(y)<0，矛盾。所以 g(y)≥0 对所有 y 成立。 |
| 6 | 思维操作引导 | 0.7 | 现在需要证明所有正的 g 值都相等。考虑两点 a,b 满足 g(a)>0, g(b)>0，用轨道点 f^m(b) 和 f^n(a) 代入平方后的右不等式，通过 floor 逼近选择 m,n 构造矛盾。 | 用 hB 不等式代入轨道点得 4·f^m(b)·(g(a)-g(b)) ≤ (f^m(b)-f^n(a)-g(b))²。设 p=g(b), q=g(a)，若 p<q，选 n 使 nq 足够大，选 m=⌊nq/p+1/2⌋ 使 mp≈nq（误差≤p/2）。则左边 ~4·(b+nq)·(q-p) 随 n 增长，右边被 K² 有界，矛盾。所以所有正缺陷值相等。 |
| 7 | 能量传递引导 | 0.6 | 最后一步：证明零缺陷和正缺陷不能共存，然后总结结论。 | 若 g(t)=0 且 g(a)=d>0 共存：球引理表明零缺陷点 t 附近 √(2dt) 范围内的点缺陷也为零；递升引理用球链从 t 出发覆盖所有更大的点；从任意零缺陷点 b 出发向下取整也可找到 ≤2d 的零缺陷点 t₀。于是所有点缺陷为零，与 g(a)=d>0 矛盾。所以要么所有 g=0（f(x)=x, c=0），要么所有 g=d>0（f(x)=x+d, c=d>0）。答案：f(x)=x+c, c≥0。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.4
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

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
- problem_type: characterization
- structure_features: 双侧函数不等式系统，含根号（QM-AM-GM结构），变量交叉耦合，要求确定所有满足条件的函数。核心结构是 QM(x,f(y)) ≥ AM(f(x),y) ≥ GM(x,f(y))。
- key_objects: [f: ℝ_{>0}→ℝ_{>0}, 缺陷函数 g(x)=f(x)-x, 轨道 f^n(y), 等差数列, 球邻域 √(2d·t)]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["squeeze_bounding", "orbit_iteration", "defect_analysis", "contradiction_via_density", "case_analysis_on_defect"]
- primary_pattern: orbit_iteration（主导思维模式：通过夹逼得到迭代公式，将函数不等式转化为轨道分析）
- knowledge_required: ["AM-GM-QM不等式结构", "函数迭代", "等差数列", "floor函数逼近", "密度论证/球链覆盖", "反证法"]
- key_insight: 平方两个不等式后代入 x=f(y)，上下界同时变为 4f(y)²，夹逼出精确迭代关系 f(f(y))=2f(y)-y，使轨道成为等差数列，将问题归结为缺陷 g(x)=f(x)-x 的分析。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: inequality_system（含根号的双侧函数不等式系统）
- translation_to: algebraic_iteration（f的迭代关系与缺陷分析）
- translation_type: structural_transformation（通过平方+夹逼代入，将不等式系统结构性转化为精确迭代关系）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_manipulation, gap_type: structural_transformation}
- tell_small_concepts: ["QM-AM-GM结构", "缺陷函数", "轨道等差数列", "夹逼代入", "交叉不等式", "球密度论证"]
- expected_ai_method: direct_manipulation（bare AI会尝试直接操作不等式、代入特值、或验证候选函数，但不会发现夹逼代入得到迭代关系这一关键步骤）
- correct_method: orbit_iteration_with_defect_analysis（正确方法是通过夹逼得到迭代公式，研究轨道，分析缺陷，用密度论证完成反证）

**已有ai_method_type值**（优先使用）：
- `enumeration_brute_force` ✅ 抽象
- `continuous_analytic` ✅ 抽象
- `direct_calculation` ✅ 抽象
- `logical_deduction` ✅ 抽象
- `case_by_case` ✅ 抽象
- `algebraic_identity` ✅ 中等
- `equation_solving` ✅ 抽象
- `direct_manipulation` ✅ 抽象
- **❌ 不要用太长太具体的值**

**已有gap_type值**（优先使用）：
- `method_problem_mismatch` ✅ 抽象
- `knowledge_gap` ✅ 抽象
- `structural_transformation` ✅ 中等
- `search_space_estimation` ✅ 中等
- `method_translation` ✅ 中等
- `global_sorting` ⚠️ 偏具体
- **❌ 不要用太具体的值**

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ → 可以。characterization（已有）、direct_manipulation（已有）、structural_transformation（已有）均适用。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ → 一致。三个值都是中等偏抽象的粒度。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ → 足够。这道题的tell特征（夹逼代入→迭代→缺陷分析→密度论证）可以用现有三维区分。
- [x] 如果发现拓扑分类需要进化，在此写出建议： → 无需进化。

**拓扑进化建议**（如有）：无。现有拓扑分类体系完全覆盖本题。

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
- 全局pair中path_feature型: 1 个，implicit型: 2 个

详见 profile.json 中的 tell_hint_pairs 和 global_tell_hint_pairs 字段。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接代入特值（如x=y，得到恒等式死路），或试图验证f(x)=x+c而不证明唯一性，或平方后无法发现夹逼代入x=f(y)这一关键步骤。核心错误是看不到两个不等式在x=f(y)处上下界同时变为4f(y)²的夹逼结构，从而无法得到迭代公式f(f(y))=2f(y)-y，后续所有步骤（轨道、缺陷、密度论证）都无从展开。
- suitable_for_poc: ["tell_extraction_poc", "hint_injection_poc", "path_feature_visibility_poc"]
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
2. 更新`problem_extraction_progress`集合中`_key="329288"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2026p5"
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
    '_key': '329288',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2026p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2026p5')
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
- problem_id: compfiles_imo2026p5
- solution_method_type: orbit_iteration_with_defect_analysis
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3（1个path_feature型 + 2个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否。现有拓扑分类体系（characterization / direct_manipulation / structural_transformation等）完全覆盖本题。
- 是否遇到异常: 否。入库和验证均一次通过。

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
