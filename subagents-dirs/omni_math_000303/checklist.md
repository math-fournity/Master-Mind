# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000303
- **文件路径**: subagents-dirs/omni_math_000303/problem.lean
- **来源**: AoPS omni_math (china_team_selection_test)
- **ArangoDB progress记录_key**: 330175（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000303/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：固定正整数n。证明：对任意不超过3n²+4n的正整数a,b,c，存在绝对值不超过2n且不全为0的整数x,y,z，使得ax+by+cz=0。
- 解答核心思路（1-2句话）：WLOG设c=max(a,b,c)，在0≤x≤2n, -2n≤y≤0的网格上生成4n²+4n个ax+by值，用鸽巢原理（因c≤3n²+4n<4n²+4n）找到同余重复，对差值做符号分析，分情况处理：差值异号直接得解，差值同正则用两组差值之差或分析固定差值(A,B)情形。
- 解答关键步骤列表：
  1. WLOG c=max(a,b,c)
  2. 构造网格：0≤x≤2n, -2n≤y≤0, (x,y)≠(0,0)，共(2n+1)²-1=4n²+4n个值
  3. 若某ax+by≡0(mod c)，则|ax+by|≤2nc，直接得解（z=-(ax+by)/c, |z|≤2n）
  4. 否则4n²+4n个值均非零mod c，因c≤3n²+4n<4n²+4n，鸽巢原理得重复
  5. 若ax₁+by₁≡ax₂+by₂(mod c)，则a(x₂-x₁)+b(y₂-y₁)≡0(mod c)
  6. 若差值不同号，|差值|≤2n，直接得解
  7. 若差值同正且和>2n，需进一步分析：同一剩余类至多2个(x,y)
  8. 两组同正差值之差仍满足同余且分量有界，可得解
  9. 若所有对差值固定为(A,B)，则A+B=2n+1，Aa+Bb≡0(mod c)，0≤Aa+Bb≤(2n+1)c
  10. 若Aa+Bb=(2n+1)c则A(c-a)+B(c-b)=0，推出c=a或c=b（平凡情形），否则k≤2n直接得解

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
| 1 | 纯元认知观察 | 0.3 | 描述题目结构：我们要证明什么？关键约束是什么？ | 这是一个存在性命题：对任意a,b,c≤3n²+4n，存在|x|,|y|,|z|≤2n且不全为0的整数x,y,z使ax+by+cz=0。核心是证明有界整数解的存在性。 |
| 2 | 自由列举 | 0.5 | 有哪些方法可以证明ax+by+cz=0的有界解存在？ | 可能的方法：(1)鸽巢原理取余数，(2)Minkowski定理（格点），(3)直接构造，(4)生成函数，(5)连分数/Diophantine逼近 |
| 3 | 小尝试 | 0.4 | 试试Minkowski定理：能否设置格和凸体来保证非平凡解？ | Minkowski需要对称凸体体积足够大。|x|,|y|,|z|≤2n给出体积(4n+1)³的立方体，格{ax+by+cz=0}的行列式与gcd(a,b,c)相关。但3n²+4n和2n的界与Minkowski要求不干净匹配，且问题是整数而非实格点。 |
| 4 | 思维操作引导 | 0.3 | 不用Minkowski，考虑鸽巢原理。WLOG设c=max(a,b,c)。你能生成多少个ax+by的值？mod c有多少个剩余类？ | 取0≤x≤2n, -2n≤y≤0（不同时为0），共(2n+1)²-1=4n²+4n个ax+by值。因c≤3n²+4n<4n²+4n，鸽巢原理保证有两个值同余mod c。 |
| 5 | 推进 | 0.2 | 给定ax₁+by₁≡ax₂+by₂(mod c)，关于(x₂-x₁, y₂-y₁)能得出什么？何时直接给出解？ | a(x₂-x₁)+b(y₂-y₁)≡0(mod c)。若差值不同号（一正一负或含零），则|a·差+b·差|≤2nc，等于cz且|z|≤2n，直接得解。麻烦情形是差值同正且和>2n。 |
| 6 | 思维操作引导 | 0.4 | 在差值同正的麻烦情形中，如何利用多组同余对来找到解？ | 若有两组同余对，差值分别为(X₁,Y₁)和(X₂,Y₂)且均同正，则(X₁-X₂, Y₁-Y₂)也满足同余mod c，且各分量绝对值≤2n。若符号合适则直接得解。 |
| 7 | 推进 | 0.3 | 若所有同余对的差值都固定为(A,B)，分析这个情形。 | 若所有对差值固定(A,B)且A+B>2n，则有效(x₁,y₁)位置至多(2n+1-A)(2n+1-B)≤n²个。但鸽巢给出至少n²+1对，矛盾，除非A+B=2n+1。此时Aa+Bb≡0(mod c)，0≤Aa+Bb≤(2n+1)c。若k≤2n直接得解；若k=2n+1则A(c-a)+B(c-b)=0推出c=a或c=b（平凡）。 |
| 8 | 能量传递引导 | 0.6 | 总结完整证明结构，验证所有情形都已覆盖。 | 证明完整：(1)WLOG c=max，(2)生成4n²+4n个值，(3)鸽巢得重复剩余，(4)差值异号直接得解，(5)差值同正用两组之差或分析固定差值情形，(6)固定差值推出A+B=2n+1，要么直接得解要么平凡。QED。 |

**统计**：
- total_rounds: 8
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.0
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R4
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R7

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
- structure_features: 有界整数解存在性证明；线性Diophantine方程ax+by+cz=0；鸽巢原理取余数mod c；差值符号分类讨论；固定差值(A,B)子情形分析
- key_objects: 正整数a,b,c（≤3n²+4n）；整数x,y,z（|·|≤2n）；mod c剩余类；网格点对(x,y)及其差值；固定差值(A,B)

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["pigeonhole_principle", "case_analysis", "counting_argument", "modular_arithmetic", "wlog_symmetry", "contradiction_argument"]
- primary_pattern: pigeonhole_principle
- knowledge_required: ["鸽巢原理", "模运算/同余", "有界整数解", "线性Diophantine方程", "Minkowski定理（作为对比排除）"]
- key_insight: 在0≤x≤2n, -2n≤y≤0的网格上生成4n²+4n个ax+by值，因c≤3n²+4n<4n²+4n用鸽巢原理找到同余重复，再对差值做符号分类讨论提取有界解

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 几何/格点直觉（Minkowski定理式的连续格点方法）
- translation_to: 组合/鸽巢计数取余数（离散的mod c剩余类计数）
- translation_type: method_translation（从几何连续方法翻译到组合离散方法）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: enumeration_brute_force, gap_type: method_translation}
- tell_small_concepts: ["鸽巢原理取余数mod c", "4n²+4n网格值计数", "差值符号分类", "固定差值(A,B)情形", "同余重复对", "有界解提取"]
- expected_ai_method: direct_calculation（bare AI可能尝试直接构造x,y,z或用Minkowski定理）
- correct_method: 鸽巢原理取余数mod c + 差值符号分类讨论

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ 可以。structural_existence + enumeration_brute_force + method_translation 均为已有值，粒度匹配。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ 一致。problem_type为抽象层，ai_method_type为抽象层，gap_type为中等层，与已有标注体系一致。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ 足够。这道题的核心gap是从直接构造/几何方法翻译到鸽巢计数方法，method_translation已覆盖。
- [x] 如果发现拓扑分类需要进化，在此写出建议： 无需进化。现有分类体系充分。

**拓扑进化建议**（如有）：无。现有拓扑分类体系充分覆盖本题。

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
- 局部tell_hint_pairs数量: 8 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

局部pair摘要：
- R1: (structural_existence, direct_calculation, method_problem_mismatch) — AI看到存在性命题可能尝试直接构造
- R2: (structural_existence, enumeration_brute_force, search_space_estimation) — AI列举方法但可能不优先鸽巢
- R3: (structural_existence, continuous_analytic, method_problem_mismatch) — AI试Minkowski定理，不适用于整数问题
- R4: (structural_existence, enumeration_brute_force, knowledge_gap) — 知识瓶颈：鸽巢取余数mod c是关键方法论
- R5: (structural_existence, direct_calculation, structural_transformation) — 差值分析，从同余重复提取有界解
- R6: (structural_existence, case_by_case, structural_transformation) — 多组同余对差值之差
- R7: (structural_existence, case_by_case, method_translation) — 固定差值(A,B)情形分析
- R8: (structural_existence, logical_deduction, method_problem_mismatch) — 证明组装与验证

全局pair摘要：
1. path_feature型：完整证明路径（鸽巢→符号分析→固定差值情形），局部步骤看不到全局路径
2. implicit型：界3n²+4n与计数4n²+4n的数值关系，在题目陈述中隐含不显式

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "Bare AI大概率尝试Minkowski定理或直接构造，无法发现鸽巢取余数mod c的方法。即使偶然想到鸽巢，差值符号分类讨论（特别是固定差值(A,B)子情形）的非平凡case分析很可能不完整。难度9.0的竞赛题对bare AI极具挑战性。"
- suitable_for_poc: ["tell_hint_injection", "path_guidance", "knowledge_bottleneck_identification"]
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
2. 更新`problem_extraction_progress`集合中`_key="330175"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_000303"
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
    '_key': '330175',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_000303',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_000303')
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
- problem_id: omni_math_000303
- solution_method_type: pigeonhole_residue_case_analysis
- 局部(tell,hint)对数量: 8
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，现有分类体系充分覆盖
- 是否遇到异常: 解答在Lean文件中被截断，从HuggingFace omni_math数据集获取完整解答后完成分析

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
