# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa1997p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa1997P5.lean
- **来源**: USA 1997 P5
- **ArangoDB progress记录_key**: 329387（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa1997P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设 a, b, c 为正实数。证明：1/(a³+b³+abc) + 1/(b³+c³+abc) + 1/(c³+a³+abc) ≤ 1/(abc)
- 解答核心思路（1-2句话）：利用因式分解 a³+b³ ≥ a²b+ab²（即 (a-b)²(a+b)≥0），将每个分式的分母放大为 ab(a+b+c)，循环求和后三个分式恰好消去为 1/(abc)。
- 解答关键步骤列表：
  1. 证明核心引理：a³+b³ ≥ a²b+ab²（因 (a-b)²(a+b) ≥ 0），故 a³+b³+abc ≥ a²b+ab²+abc = ab(a+b+c)
  2. 由分母放大得 1/(a³+b³+abc) ≤ 1/(ab(a+b+c)) = c/(abc(a+b+c))
  3. 循环求和三个不等式：Σ 1/(a³+b³+abc) ≤ (a+b+c)/(abc(a+b+c)) = 1/(abc)
  4. 结论成立

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
| 1 | 纯元认知观察 | 0.7 | 观察这个不等式：1/(a³+b³+abc) + 1/(b³+c³+abc) + 1/(c³+a³+abc) ≤ 1/(abc)。描述它的结构特征——左边是什么形式？右边是什么形式？三个分母之间有什么关系？ | 左边是三个分式之和，每个分母是两个变量的立方和加上abc。三个分母按(a,b)、(b,c)、(c,a)循环排列。右边是1/(abc)。结构上是对称循环的，右边可以看作三个 1/(abc) 的和除以3，或者每个分母都含有abc这一项。 |
| 2 | 自由列举 | 0.6 | 面对这个不等式，列出你能想到的所有可能证明方向。 | 1) 直接通分后展开比较；2) 用AM-GM等经典不等式逐项放缩；3) 利用a³+b³的因式分解；4) 对每个分式分别找到上界再求和；5) 用Schur不等式或Muirhead；6) 齐次化后设abc=1简化；7) 用Cauchy-Schwarz或Holder不等式。 |
| 3 | 小尝试 | 0.5 | 试试用AM-GM不等式来放缩每个分式：a³+b³ ≥ 2a^(3/2)b^(3/2)，看看这条路能不能走通。 | 用AM-GM得 a³+b³ ≥ 2(ab)^(3/2)，所以分母 ≥ 2(ab)^(3/2)+abc。但这样得到的上界 1/(2(ab)^(3/2)+abc) 求和后很难化简到 1/(abc)，因为涉及 (ab)^(3/2) 而不是多项式形式，循环求和后无法约分。这条路看起来不太行。 |
| 4 | 思维操作引导 | 0.4 | 回到a³+b³的代数恒等式。执行这个操作：将a³+b³因式分解，并找出a³+b³与a²b+ab²之间的关系（差是什么？差的符号如何？）。 | a³+b³ = (a+b)(a²-ab+b²)，a²b+ab² = ab(a+b)。差 = (a+b)(a²-ab+b²) - ab(a+b) = (a+b)(a²-2ab+b²) = (a+b)(a-b)² ≥ 0。所以 a³+b³ ≥ a²b+ab²，等号当a=b时成立。 |
| 5 | 推进 | 0.5 | 既然 a³+b³ ≥ a²b+ab²，那么 a³+b³+abc ≥ a²b+ab²+abc = ab(a+b+c)。用这个结果对单个分式放缩，然后循环求和。 | 1/(a³+b³+abc) ≤ 1/(ab(a+b+c)) = c/(abc(a+b+c))。循环求和：c/(abc(a+b+c)) + a/(abc(a+b+c)) + b/(abc(a+b+c)) = (a+b+c)/(abc(a+b+c)) = 1/(abc)。证毕！ |
| 6 | 能量传递引导 | 0.7 | 回顾整个证明路径：从因式分解到放缩到循环求和消元，每一步都很自然。你能总结一下这个证明的核心美感在哪里吗？ | 核心美感在于"分母放大后恰好消元"——a³+b³放缩为ab(a+b)后，加上abc变成ab(a+b+c)，循环求和时分子恰好凑出(a+b+c)与分母约掉，得到干净的1/(abc)。关键洞察是认识到a²b+ab²+abc=ab(a+b+c)这个因式分解让循环求和变得可行。 |

**统计**：
- total_rounds: 6
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5
- knowledge_rounds（思维操作引导的轮数）: 1
- level_sum: 3.4
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R3"

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
- problem_type: inequality_proof
- structure_features: 三个循环对称的分式之和 ≤ 单个分式，每个分母含两个变量的立方和加abc，右侧1/(abc)可分解为循环求和消元目标
- key_objects: 正实数a,b,c；循环对称分式和；立方和a³+b³；因式分解(a+b)(a-b)²；公因式ab(a+b+c)

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [分母放缩, 因式分解识别, 循环对称求和消元, 逐项上界估计]
- primary_pattern: 分母放缩后循环求和消元
- knowledge_required: [a³+b³因式分解, (a-b)²(a+b)≥0非负性, 分母放大则分式缩小, 循环对称求和]
- key_insight: 将a³+b³放缩为a²b+ab²后加abc得到ab(a+b+c)，循环求和时分子恰好凑出(a+b+c)与分母约掉

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: AM-GM不等式放缩（非多项式路径，走错的）
- translation_to: 代数恒等式因式分解+循环求和消元（多项式路径，正确的）
- translation_type: method_translation（从非多项式不等式工具翻译到多项式代数恒等式工具）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: inequality_proof, ai_method_type: enumeration_brute_force, gap_type: method_problem_mismatch}
- tell_small_concepts: [立方和因式分解, 分母放缩, 循环对称求和, ab(a+b+c)公因式, (a-b)²非负性]
- expected_ai_method: bare AI预期会用AM-GM或Cauchy-Schwarz等经典不等式工具逐项放缩，但放缩后的表达式无法循环消元
- correct_method: 利用a³+b³≥a²b+ab²的代数恒等式放缩分母，使分母变为ab(a+b+c)，循环求和后分子恰好消去(a+b+c)

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是，inequality_proof + enumeration_brute_force + method_problem_mismatch 完全覆盖
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是，都是中等抽象粒度
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化

**拓扑进化建议**（如有）：无

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 6 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对循环对称分式不等式，尚未识别分母结构中的因式分解线索 | 描述题目结构特征，识别三个分母的循环对称性和abc公共项 | 0.7 | 纯元认知观察 | false | {inequality_proof, direct_calculation, method_problem_mismatch} | [循环对称分式和, abc公共项, 分母结构观察] |
| 2 | AI已识别结构但未确定方向，可能尝试多种经典不等式工具 | 列出所有可能证明方向包括因式分解路径 | 0.6 | 自由列举 | false | {inequality_proof, enumeration_brute_force, method_problem_mismatch} | [AM-GM, Cauchy-Schwarz, 因式分解, Schur不等式, 齐次化] |
| 3 | AI选择了AM-GM放缩路径，得到非多项式表达式无法循环消元 | AM-GM路径走不通，需要回到多项式代数恒等式 | 0.5 | 小尝试 | false | {inequality_proof, continuous_analytic, method_problem_mismatch} | [AM-GM放缩, 非多项式表达式, 循环消元失败] |
| 4 | AI需要知道a³+b³与a²b+ab²的关系但尚未建立联系 | 执行因式分解操作：a³+b³-(a²b+ab²)=(a+b)(a-b)²≥0 | 0.4 | 思维操作引导 | true | {inequality_proof, algebraic_identity, knowledge_gap} | [立方和因式分解, (a-b)²非负性, a²b+ab²=ab(a+b)] |
| 5 | AI已建立a³+b³≥a²b+ab²但未看到循环求和消元的完整路径 | 用ab(a+b+c)放缩分母并循环求和，分子恰好凑出(a+b+c) | 0.5 | 推进 | false | {inequality_proof, algebraic_identity, structural_transformation} | [ab(a+b+c)公因式, 循环求和消元, 分母放缩] |
| 6 | AI已完成证明，需要反思核心美感以巩固认知 | 总结"分母放大后恰好消元"的证明美感 | 0.7 | 能量传递引导 | false | {inequality_proof, algebraic_identity, method_translation} | [分母放大消元, 因式分解美感, 循环对称] |

**全局tell_hint_pairs详情**：

1. path_feature型：
- scope_type: path_feature
- scope: 整个证明路径从R3(AM-GM走错)到R4(因式分解纠正)到R5(循环消元完成)
- observation_point: null
- tell: AM-GM放缩路径产生非多项式表达式无法循环消元，需要翻译到多项式代数恒等式路径
- hint: 从走错的AM-GM路径翻译到正确的因式分解路径——关键在于a³+b³与a²b+ab²的关系
- hint_level: 0.5
- generalizability: high——适用于所有"经典不等式工具放缩后无法消元"的不等式证明场景
- why_not_visible_locally: 在R3单独看AM-GM尝试时，只能看到"这条路走不通"，但看不到正确的因式分解路径是什么——完整路径特征(走错→纠正→消元)需要从全局视角才能识别
- tell_topology: {inequality_proof, enumeration_brute_force, method_translation}
- tell_small_concepts: [AM-GM路径失败, 多项式代数恒等式翻译, 循环消元目标]

2. implicit型：
- scope_type: implicit
- scope: R4-R5之间的隐含连接
- observation_point: Q4
- tell: a³+b³≥a²b+ab²这个不等式本身不暗示ab(a+b+c)的因式分解——需要额外识别a²b+ab²+abc=ab(a+b+c)这一步
- hint: 在建立a³+b³≥a²b+ab²后，主动执行a²b+ab²+abc=ab(a+b+c)的因式分解，这是连接放缩到消元的关键桥梁
- hint_level: 0.4
- generalizability: medium——适用于"分母放缩后需要提取公因式以实现循环消元"的场景
- why_not_visible_locally: 在R4单独完成因式分解a³+b³≥a²b+ab²时，看不到加abc后提取公因式ab(a+b+c)这一步——这步需要同时看到放缩结果和循环求和目标才能发现
- tell_topology: {inequality_proof, algebraic_identity, structural_transformation}
- tell_small_concepts: [a²b+ab²+abc因式分解, ab(a+b+c)公因式提取, 放缩到消元的桥梁]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会倾向于用AM-GM或Cauchy-Schwarz等经典不等式工具逐项放缩，但放缩后得到非多项式表达式（如(ab)^(3/2)），循环求和时无法约分消元到1/(abc)。AI不会想到回到a³+b³的代数恒等式因式分解路径，因为AM-GM看起来是更"标准"的不等式工具。
- suitable_for_poc: ["POC-VMS-8脉络注入验证", "POC-VMS-9 tell去特化验证", "POC-VMS-10小概念标记分辨验证"]
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

## Step 10: 入库ArangoDB [ ]

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="329387"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa1997p5"
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
    '_key': '329387',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa1997p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa1997p5')
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
- problem_id: compfiles_usa1997p5
- solution_method_type: 分母放缩后循环求和消元
- 局部(tell,hint)对数量: 6
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，已有拓扑分类(inequality_proof + enumeration_brute_force/algebraic_identity + method_problem_mismatch/knowledge_gap/structural_transformation/method_translation)完全覆盖
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
