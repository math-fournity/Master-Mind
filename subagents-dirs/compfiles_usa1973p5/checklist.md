# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa1973p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa1973P5.lean
- **来源**: USA 1973 P5
- **ArangoDB progress记录_key**: 329302（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa1973P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Show that the cube roots of three distinct primes cannot be terms in an arithmetic progression (whether consecutive or not).
- 解答核心思路（1-2句话）：假设∛p, ∛q, ∛r在等差数列中，消去公差d得到线性关系n∛q - m∛r = (n-m)∛p，对此式立方后利用代数恒等式得到3mn(n-m)∛(pqr) = n³q - m³r - (n-m)³p，从而∛(pqr)可表为整数之比（有理数），但由素因子分解可证∛(pqr)对互异素数无理，矛盾。
- 解答关键步骤列表：
  1. 假设∛p, ∛q, ∛r在AP中，公差d，位置差m和n：∛q = ∛p + md, ∛r = ∛p + nd
  2. 消去d：n∛q - m∛r = (n-m)∛p
  3. 立方此关系，利用(a-b)³ = a³ - b³ - 3ab(a-b)恒等式：3mn(n-m)∛p∛q∛r = n³q - m³r - (n-m)³p
  4. 注意∛p∛q∛r = ∛(pqr)，故∛(pqr) = [n³q - m³r - (n-m)³p] / [3mn(n-m)]，为有理数
  5. 证明∛(pqr)无理：若∛(pqr) = A/B，则pqr·B³ = A³，比较p的指数得1+3k = 3j，不可能
  6. 矛盾，故∛p, ∛q, ∛r不能在AP中

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
| 1 | 纯元认知观察 | 0.8 | 这道题要你证明什么？题目中的核心数学对象是什么？已知条件和要证明的结论分别是什么？ | 要证明三个不同素数的立方根不能构成等差数列（无论是否连续）。核心对象是∛p, ∛q, ∛r（p,q,r为互异素数）和等差数列。这是一个非存在性证明——证明某种排列不可能存在。 |
| 2 | 自由列举 | 0.7 | 要证明"不可能在等差数列中"，你能想到哪些可能的证明策略？列出所有你能想到的方向。 | 反证法（假设在AP中推出矛盾）、域论方法（∛p在Q上次数为3，三个立方根在AP中会给出域扩张的约束）、直接计算/数值验证、代数恒等式方法、无理性论证 |
| 3 | 小尝试 | 0.5 | 用反证法：假设∛p, ∛q, ∛r在公差为d的等差数列中，位置差为m和n。写出这个假设的表达式，然后尝试消去d。 | ∛q = ∛p + md, ∛r = ∛p + nd。消去d：n∛q - m∛r = (n-m)∛p。得到一个关于立方根的线性关系，但不确定下一步该做什么。 |
| 4 | 思维操作引导 | 0.4 | 你现在有一个关于立方根的线性关系：n∛q - m∛r = (n-m)∛p。对线性关系做立方运算，利用恒等式(a-b)³ = a³ - b³ - 3ab(a-b)展开，观察会出现什么项。 | 立方后：[n∛q - m∛r]³ = [(n-m)∛p]³。展开左边用恒等式：n³q - m³r - 3mn∛q∛r(n∛q - m∛r) = (n-m)³p。代入n∛q - m∛r = (n-m)∛p：n³q - m³r - 3mn(n-m)∛p∛q∛r = (n-m)³p。整理得：3mn(n-m)∛(pqr) = n³q - m³r - (n-m)³p。 |
| 5 | 推进 | 0.5 | 从上一步的结果3mn(n-m)∛(pqr) = n³q - m³r - (n-m)³p，你能得出什么结论？右边和系数分别是什么？ | 右边n³q - m³r - (n-m)³p是整数，系数3mn(n-m)是非零整数（因为m≠0, n≠0, m≠n）。所以∛(pqr) = 整数/整数，即∛(pqr)是有理数。 |
| 6 | 思维操作引导 | 0.3 | 你得出了∛(pqr)是有理数的结论。现在需要证明∛(pqr)对互异素数p,q,r是无理数。用素因子分解的方法：假设∛(pqr) = A/B，推出什么矛盾？ | 若∛(pqr) = A/B，则pqr·B³ = A³。比较等式两边p的指数：左边p的指数为1+3v_p(B)，右边p的指数为3v_p(A)。即1+3k = 3j，左边模3余1，右边模3余0，矛盾。故∛(pqr)无理。 |
| 7 | 能量传递引导 | 0.6 | 把所有步骤串起来：AP假设→消去d→立方→∛(pqr)有理→∛(pqr)无理。矛盾来自哪里？证明完成了吗？ | AP假设导致∛(pqr)有理（步骤3-5），但素因子分解证明∛(pqr)无理（步骤6）。矛盾说明AP假设不成立。因此三个不同素数的立方根不能构成等差数列。证明完成。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.8
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
- problem_type: structural_existence
- structure_features: 非存在性证明，反证法。核心结构链：AP假设→消去公差d得到线性关系→立方运算产生∛(pqr)项→∛(pqr)有理性与无理性矛盾。代数恒等式桥接代数操作与数论论证。
- key_objects: ["∛p, ∛q, ∛r（素数立方根）", "等差数列（AP）", "代数恒等式(a-b)³", "素因子分解", "∛(pqr)无理性"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["proof_by_contradiction", "variable_elimination", "algebraic_identity_application", "irrationality_via_prime_factorization"]
- primary_pattern: algebraic_identity_application
- knowledge_required: ["等差数列定义", "素因子分解与指数比较", "立方根的无理性证明方法", "代数恒等式(a-b)³ = a³ - b³ - 3ab(a-b)"]
- key_insight: 对线性关系n∛q - m∛r = (n-m)∛p做立方运算后，交叉项产生∛(pqr)，这是连接代数操作与无理性论证的关键桥梁。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 立方根之间的线性关系（AP假设消去d后的代数关系）
- translation_to: ∛(pqr)的有理性→无理性矛盾（数论论证）
- translation_type: algebraic_identity_bridge（通过立方运算的代数恒等式，将线性关系翻译为包含∛(pqr)的等式，桥接到无理性论证）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: method_translation}
- tell_small_concepts: ["cube roots of primes", "arithmetic progression", "algebraic identity (a-b)³", "prime factorization exponent comparison", "irrationality of ∛(pqr)"]
- expected_ai_method: bare AI可能尝试域论方法（∛p在Q上次数为3，用域扩张约束论证）或直接计算，但不会想到对线性关系做立方来桥接到无理性论证
- correct_method: 反证法——消去d得到线性关系，立方后利用代数恒等式产生∛(pqr)项，证明∛(pqr)有理与无理矛盾

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能归入已有的拓扑类别？是。structural_existence（非存在性证明）、direct_calculation（bare AI可能用域论或直接计算）、method_translation（从代数关系到数论论证的翻译）都能归入已有类别。
- [x] 粒度是否一致——标注的值和已有值的粒度统一？是。三个维度都用了已有的抽象/中等粒度值。
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell？是。problem_type区分问题类型，ai_method_type区分AI预期方法，gap_type区分差距类型，足够。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。已有拓扑分类体系足够覆盖此题。

**拓扑进化建议**（如有）：无。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到非存在性证明题目但未识别关键结构——立方根与AP的组合 | 描述题目结构：三个不同素数的立方根不能在AP中，这是非存在性证明 | 0.8 | 纯元认知观察 | false | {structural_existence, direct_calculation, method_problem_mismatch} | ["non-existence proof", "arithmetic progression", "cube roots of primes"] |
| 2 | AI列出可能方向但未看到立方运算桥接无理性论证这一路径 | 列出所有策略：反证法、域论、直接计算、代数恒等式、无理性论证 | 0.7 | 自由列举 | false | {structural_existence, enumeration_brute_force, search_space_estimation} | ["proof by contradiction", "field theory", "algebraic identity", "irrationality"] |
| 3 | AI设AP假设并消去d，得到线性关系n∛q-m∛r=(n-m)∛p，但不知道下一步 | 写出AP假设表达式，尝试消去公差d | 0.5 | 小尝试 | false | {structural_existence, direct_manipulation, method_translation} | ["eliminate d", "linear relation", "cube roots"] |
| 4 | AI有线性关系但未想到立方运算能产生∛(pqr)桥接项 | 对线性关系做立方，用恒等式(a-b)³展开，观察出现的项 | 0.4 | 思维操作引导 | false | {structural_existence, algebraic_identity, method_translation} | ["cubing", "algebraic identity (a-b)³", "∛(pqr) bridge term"] |
| 5 | AI得到3mn(n-m)∛(pqr)=整数，看出∛(pqr)有理但不确定是否矛盾 | 分析右边是整数，系数是非零整数，故∛(pqr)有理 | 0.5 | 推进 | false | {structural_existence, logical_deduction, knowledge_gap} | ["rationality", "∛(pqr)", "integer ratio"] |
| 6 | AI需要证明∛(pqr)无理但可能不知道素因子分解指数比较法 | 用素因子分解：若∛(pqr)=A/B则pqr·B³=A³，比较p的指数得1+3k=3j矛盾 | 0.3 | 思维操作引导 | true | {structural_existence, direct_calculation, knowledge_gap} | ["prime factorization", "exponent comparison", "irrationality proof"] |
| 7 | AI有所有片段但需要组装最终矛盾 | 串联所有步骤：AP假设→∛(pqr)有理→∛(pqr)无理→矛盾 | 0.6 | 能量传递引导 | false | {structural_existence, logical_deduction, method_problem_mismatch} | ["contradiction", "rational vs irrational", "proof complete"] |

**全局pairs详情**：

1. path_feature型:
- scope_type: path_feature
- scope: 整个证明路径从AP假设到矛盾
- observation_point: null
- tell: 证明需要一条特定的非显然路径：消去d→立方线性关系→识别∛(pqr)有理性→素因子分解证无理。没有任何单步能揭示为什么前一步是必要的。
- hint: 沿链条走：AP给线性关系，立方给∛(pqr)有理，素因子分解给无理，矛盾。每步的动机来自它启用的下一步。
- hint_level: 0.7
- generalizability: high——"代数操作产生桥接项连接到已知不可能性"的模式在许多无理性/非存在性证明中出现
- why_not_visible_locally: 从任何单步看，该步的动机来自它启用的未来步骤。消去d看似无意义直到你立方；立方看似纯代数直到你识别∛(pqr)；识别有理性看似死胡同直到你知道无理性证明。路径特征只有在整条链一起看时才可见。
- tell_topology: {structural_existence, algebraic_identity, method_translation}
- tell_small_concepts: ["path dependency", "step motivation", "bridge term ∛(pqr)"]

2. implicit型:
- scope_type: implicit
- scope: 立方步骤(R4)隐含创建了到无理性论证的桥梁
- observation_point: Q4
- tell: 立方n∛q-m∛r=(n-m)∛p时，交叉项3mn(n-m)∛p∛q∛r=3mn(n-m)∛(pqr)出现。这个∛(pqr)项是到无理性论证的隐含桥梁，但在代数操作过程中不可见为此。
- hint: 立方后，孤立∛(pqr)项——它是到矛盾的关键桥梁。
- hint_level: 0.5
- generalizability: medium——"代数操作产生连接到已知不可能性的项"模式常见但具体桥接项因题而异
- why_not_visible_locally: 在立方步骤中，注意力集中在正确展开代数恒等式上。∛(pqr)项的意义——它代表一个已知无理的数——只有当你退后一步问"这个等式告诉我关于∛(pqr)的什么"时才显现。局部视角是纯代数；全局视角揭示数论意义。
- tell_topology: {structural_existence, algebraic_identity, method_translation}
- tell_small_concepts: ["bridge term", "∛(pqr)", "cross term from cubing"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI可能尝试域论方法（∛p在Q上次数为3，试图用域扩张的线性无关性论证），但域论方法难以直接处理"在AP中"这个条件。或者AI可能在消去d后卡住，不知道对线性关系做立方运算。即使想到立方，也可能不识别∛(pqr)项的数论意义。关键思维瓶颈在R4（立方运算桥接）和R6（素因子分解无理性证明）。
- suitable_for_poc: ["POC-VMS-8_hint_injection（hint端验证：注入立方运算提示能否引导AI找到正确路径）", "POC-VMS-9_tell_detection（tell端验证：检测AI在R3消去d后不知道下一步的分叉信号）", "POC-VMS-10_tell_despecialization（tell去特化：将'线性关系后不知道做立方'去特化为method_translation拓扑）"]
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
2. 更新`problem_extraction_progress`集合中`_key="329302"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa1973p5"
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
    '_key': '329302',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa1973p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa1973p5')
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
- problem_id: compfiles_usa1973p5
- solution_method_type: proof_by_contradiction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。已有拓扑分类体系（structural_existence / direct_calculation / method_translation等）足够覆盖此题。
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
