# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000133
- **文件路径**: subagents-dirs/omni_math_000133/problem.lean
- **来源**: AoPS omni_math (china_team_selection_test)
- **ArangoDB progress记录_key**: 330004（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000133/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：对有理点(x,y)，若xy为整数且被2整除但不被3整除，染红色；若xy为整数且被3整除但不被2整除，染蓝色。问：平面上是否存在一条线段恰好包含2017个蓝色点和58个红色点？
- 解答核心思路（1-2句话）：构造直线y=ax+b（b=2，a为适当选取的素数乘积），利用有理点条件将问题转化为"1+az为完全平方数"的整数z的计数问题，再通过CRT选取素数使各z值的2/3整除性可控，精确控制红蓝点数量。
- 解答关键步骤列表：
  1. 取直线y=ax+b，b=2，a=p1p2...pm（素数乘积）
  2. 有理点(x,y)在直线上且xy=z∈Z ⟺ 1+az为完全平方数（由y²-by-az=0判别式推导）
  3. 选取素数p_i > 2017^2017，满足同余条件：3∏(k≠j)p_k ≡ 2 (mod p_j)（CRT可满足）
  4. 同余条件保证：对每个j，z = 3∏(k≠j)p_k 对应的1+az为完全平方数且z被3整除不被2整除（蓝色），z = 2∏(k≠j)p_k对应的为红色
  5. 通过选取适当的m和线段范围，精确得到2017蓝58红

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：已知什么、未知什么？染色规则的本质是什么？我们被问的是什么类型的问题？ | 题目给了一个基于xy整除性的有理点染色规则（红：2|xy且3∤xy；蓝：3|xy且2∤xy），问是否存在一条线段恰好含2017蓝点58红点。这是一个存在性问题，核心是构造而非证明不可能。 |
| 2 | 自由列举 | 0.7 | 列出所有可能用来解决这个存在性问题的方法方向。 | 方向包括：(a)直接取特殊直线如y=x或y=2x计算红蓝点数；(b)用代数数论工具如CRT控制整除性；(c)将几何条件转化为数论条件再构造；(d)用密度/计数论证说明某类直线必然有所需比例；(e)用乘积结构a=∏p_i来获得精细控制。 |
| 3 | 小尝试 | 0.4 | 试着取一条简单直线如y=x，看看上面的有理点中xy为整数的有多少、染色情况如何。能精确控制到2017和58吗？ | y=x上xy=x²，整数点x=n时xy=n²。n²被2整除当n偶数，被3整除当3|n。但有无穷多这样的点，且无法在有限线段上精确控制到2017蓝58红——简单直线缺乏对点数的精细控制能力。需要更灵活的直线参数化。 |
| 4 | 思维操作引导 | 0.5 | 对直线y=ax+b上的有理点(x,y)，将条件"xy为整数"转化为关于z=xy的代数条件。具体地，从y=ax+b出发，用z=xy消元，看y满足什么方程，有理解的条件是什么。 | 由y=ax+b和z=xy得x=z/y，代入y=a(z/y)+b得y²-by-az=0。y为有理数当且仅当判别式b²+4az为完全平方数。取b=2则4+4az=4(1+az)，故条件为1+az为完全平方数。这把几何问题转化为数论问题：找a使得恰有2017个z（3|z,2∤z）和58个z（2|z,3∤z）使1+az为完全平方数。 |
| 5 | 推进 | 0.6 | 现在需要选择a来控制哪些z使1+az为完全平方数。考虑取a为若干大素数的乘积a=p₁p₂...pₘ，思考：1+a·z为完全平方数时z应该有什么结构？ | 若1+az=n²则az=(n-1)(n+1)。当a=∏p_i且p_i很大时，n-1和n+1的因子分解受a的素因子结构约束。关键观察：若z=∏(k≠j)p_k·c（即z恰好缺少一个素因子p_j），则az=p_j·c·(∏p_k)²，可以配成完全平方。这给出了z的候选结构。 |
| 6 | 思维操作引导 | 0.5 | 现在用CRT来选取素数p_i，使得z=3∏(k≠j)p_k时z被3整除不被2整除（蓝色），z=2∏(k≠j)p_k时z被2整除不被3整除（红色）。写出需要的同余条件并说明CRT可满足。 | 需要对每个j：3∏(k≠j)p_k ≡ 2(mod p_j)，即3·a/p_j ≡ 2(mod p_j)。这等价于在模p_j下选取p_j使得3·(其余素数乘积)≡2。由CRT，对固定的其余素数，可选取p_j满足此同余（Dirichlet定理保证素数存在）。同时要求p_i>2017^2017以排除其他小的z值干扰。蓝色点来自z=3∏(k≠j)p_k（共m个候选），红色来自z=2∏(k≠j)p_k（共m个候选），通过选取m和线段范围精确控制为2017蓝58红。 |
| 7 | 能量传递引导 | 0.3 | 验证构造的完整性：确认线段上恰好有2017蓝58红，没有多余的染色点。总结答案。 | 取m=2017+58=2075个大素数满足CRT条件。对每个j，z=3∏(k≠j)p_k给出蓝色点（3|z,2∤z），z=2∏(k≠j)p_k给出红色点（2|z,3∤z）。因p_i>2017^2017，其他z值对应的1+az不可能为完全平方数（因子太小）。选取线段范围恰好覆盖2017个蓝色z和58个红色z。答案：Yes，存在这样的线段。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1+R2+R5+R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4+R6）
- level_sum: 0.8+0.7+0.4+0.5+0.6+0.5+0.3 = 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence（存在性构造问题，需要构造满足精确计数约束的几何对象）
- structure_features: 有理点染色基于xy的2/3整除性；问是否存在线段含精确数量的两种颜色点；解答通过直线参数化将几何计数转化为数论完全平方数条件，再用CRT构造素数乘积控制整除性
- key_objects: 有理点(x,y)、染色规则(2|xy且3∤xy→红, 3|xy且2∤xy→蓝)、线段、直线y=ax+b、素数乘积a=∏p_i、完全平方数条件1+az=n²、CRT同余条件

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["几何-数论转化（将线段上有理点xy为整数的条件转化为判别式/完全平方数条件）", "参数化构造（用素数乘积参数化直线斜率以获得精细控制）", "CRT精确控制（用中国剩余定理选取素数使整除性可控）", "排除干扰（选取大素数排除非目标z值的完全平方可能性）"]
- primary_pattern: 几何-数论转化（将几何计数问题通过判别式条件转化为数论完全平方数问题，再用CRT构造）
- knowledge_required: ["有理点与直线的关系", "二次方程判别式与有理性", "中国剩余定理(CRT)", "Dirichlet素数定理（素数在等差数列中的分布）", "整除性与染色的关系"]
- key_insight: 在直线y=ax+b上，有理点xy为整数当且仅当1+az为完全平方数（由y²-by-az=0的判别式导出），这把"线段上有多少红蓝点"转化为"哪些整数z使1+az为完全平方数且满足整除条件"

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 几何语言（线段上的有理点染色计数）
- translation_to: 数论语言（完全平方数条件1+az=n² + CRT素数构造控制整除性）
- translation_type: domain_translation（跨域翻译：从几何/组合域翻译到代数数论域，通过判别式条件作为桥梁）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: enumeration_brute_force, gap_type: method_translation}
- tell_small_concepts: ["有理点染色", "xy整除性", "线段计数", "判别式完全平方数条件", "素数乘积参数化", "CRT同余构造", "Dirichlet素数定理"]
- expected_ai_method: bare AI预期会尝试直接在简单直线（如y=x, y=2x）上枚举有理点并计数，或在特定直线上做case_by_case分析，但无法实现精确计数控制
- correct_method: 将几何计数通过判别式转化为数论完全平方数条件，再用素数乘积参数化+CRT构造实现精确整除性控制

### 6b. 反思拓扑分类

- [x] 当前拓扑分类是否够用——这道题的problem_type(structural_existence)/ai_method_type(enumeration_brute_force)/gap_type(method_translation)均能归入已有拓扑类别
- [x] 粒度是否一致——structural_existence是抽象级，enumeration_brute_force是抽象级，method_translation是中等级，与已有值粒度统一
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell。关键区分点在于gap_type=method_translation准确描述了"需要从几何域翻译到数论域"这一核心gap
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化，现有拓扑分类体系可覆盖

**拓扑进化建议**（如有）：无，现有分类体系足够

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对有理点染色+精确计数存在性问题，尚未识别问题类型为构造性而非排除性 | 描述题目结构，识别这是存在性构造问题，核心是构造而非证明不可能 | 0.8 | 纯元认知观察 | false | {structural_existence, enumeration_brute_force, method_problem_mismatch} | ["有理点染色", "精确计数", "存在性构造"] |
| 2 | AI已识别问题类型但方法空间窄，可能只想到直接枚举特定直线 | 列出所有可能方向，特别包括跨域转化和CRT控制 | 0.7 | 自由列举 | false | {structural_existence, enumeration_brute_force, method_problem_mismatch} | ["方法方向列举", "跨域转化", "CRT控制"] |
| 3 | AI尝试简单直线y=x，发现无穷多点且无法精确控制计数——走错路的信号 | 试简单直线并发现其局限性，意识到需要更灵活的参数化 | 0.4 | 小尝试 | false | {structural_existence, direct_calculation, method_problem_mismatch} | ["简单直线", "无穷多点", "无法精确控制"] |
| 4 | AI知道需要更灵活的直线但不知道如何将几何条件转化为数论条件——思维瓶颈 | 用判别式将xy为整数的条件转化为1+az为完全平方数 | 0.5 | 思维操作引导 | false | {structural_existence, direct_manipulation, method_translation} | ["判别式", "完全平方数条件", "几何-数论转化"] |
| 5 | AI已得到1+az=n²条件但不知道如何选择a来控制哪些z满足条件 | 考虑a=素数乘积，分析z缺少一个素因子时的完全平方结构 | 0.6 | 推进 | false | {structural_existence, algebraic_identity, structural_transformation} | ["素数乘积", "z结构分析", "因子配对"] |
| 6 | AI知道用素数乘积但不知道如何用CRT控制整除性——知识瓶颈 | 用CRT设置同余条件3∏(k≠j)p_k≡2(mod p_j)控制z的2/3整除性 | 0.5 | 思维操作引导 | true | {structural_existence, logical_deduction, knowledge_gap} | ["CRT同余条件", "Dirichlet素数定理", "整除性控制"] |
| 7 | AI已有完整构造方案，需要验证计数正确性并排除干扰 | 验证大素数排除非目标z值，确认精确计数2017蓝58红 | 0.3 | 能量传递引导 | false | {structural_existence, logical_deduction, method_translation} | ["计数验证", "排除干扰", "大素数排除"] |

**全局pairs详情**：

Global 1 (path_feature):
- scope_type: path_feature
- scope: 整个解题路径从几何到数论的跨域转化
- observation_point: null
- tell: AI在整个路径中倾向于停留在几何域内枚举，不会主动跨域到数论用判别式条件
- hint: 需要在R4处完成关键的几何-数论转化（判别式→完全平方数条件），这是整条路径的枢纽
- hint_level: 0.6
- generalizability: "high - 任何'几何对象上的精确计数'问题都可能需要类似的跨域转化到数论"
- why_not_visible_locally: "在局部步骤中AI看到的是'线段上有理点计数'这一几何问题，无法从任何单一步骤看出需要转化为完全平方数条件——这个转化需要同时掌握直线参数化、判别式和整除性三个领域的知识并主动建立联系，局部视角只能看到各自的步骤而看不到跨域桥梁"
- tell_topology: {structural_existence, enumeration_brute_force, method_translation}
- tell_small_concepts: ["几何-数论转化", "判别式桥梁", "跨域知识整合"]

Global 2 (implicit):
- scope_type: implicit
- scope: CRT构造中素数选取的可行性
- observation_point: R6
- tell: AI可能知道需要用CRT但不确定满足特定同余条件的素数是否实际存在
- hint: Dirichlet素数定理保证等差数列中素数存在，因此CRT同余条件总可满足
- hint_level: 0.4
- generalizability: "medium - Dirichlet素数定理在需要'素数满足特定同余条件'的构造中普遍适用"
- why_not_visible_locally: "在R6的局部步骤中AI看到的是具体的同余方程3∏(k≠j)p_k≡2(mod p_j)，需要知道Dirichlet定理才能确认满足此条件的素数存在——这个蕴含信息在同余方程本身中不可见，需要额外的数论知识"
- tell_topology: {structural_existence, logical_deduction, knowledge_gap}
- tell_small_concepts: ["Dirichlet素数定理", "等差数列素数存在性", "CRT可满足性"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI大概率会在简单直线上枚举有理点并尝试计数，但无法想到用判别式将几何条件转化为完全平方数条件，更不会想到用素数乘积参数化+CRT来精确控制整除性。可能给出"不存在"的错误答案，或在简单直线上做不完整的分析后放弃。
- suitable_for_poc: ["tell端验证：检测AI是否停留在几何域内而不跨域到数论（path_feature型tell）", "hint端验证：注入判别式转化提示后AI能否继续推进到CRT构造", "知识瓶颈验证：检测AI在CRT同余条件处是否卡住（implicit型tell）", "跨域转化POC：验证domain_translation类hint的有效性"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

完整profile JSON已写入 `subagents-dirs/omni_math_000133/profile.json`，包含所有必填字段。

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
2. 更新`problem_extraction_progress`集合中`_key="330004"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_000133"
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
    '_key': '330004',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_000133',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_000133')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

- problem_id: omni_math_000133
- solution_method_type: constructive_number_theory
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1 path_feature + 1 implicit）
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无，现有分类体系足够覆盖
- 是否遇到异常: 无

**操作**：向Master Agent报告

**汇报内容**：
- problem_id:
- solution_method_type:
- 局部(tell,hint)对数量:
- 全局(tell,hint)对数量:
- 是否发现新维度:
- **拓扑分类是否有进化建议**:
- 是否遇到异常:

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
