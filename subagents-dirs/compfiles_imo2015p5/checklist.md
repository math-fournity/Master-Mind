# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2015p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2015P5.lean
- **来源**: IMO 2015 P5
- **ArangoDB progress记录_key**: 329234（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2015P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：确定所有满足函数方程 f(x + f(x + y)) + f(xy) = x + f(x + y) + y·f(x) 的函数 f : ℝ → ℝ。
- 解答核心思路（1-2句话）：通过代入特殊值(x=y=0, x=0,y=f(0), y=1)提取关键约束，定义不动点集S={t | f(t)=t}，按f(0)∈{0,2}分两种情况分别推导出f(x)=2-x和f(x)=x。
- 解答关键步骤列表：
  1. 验证f(x)=x和f(x)=2-x都满足方程（正向方向，用ring tactic）
  2. 令x=y=0：得f(f(0))=0
  3. 令x=0, y=f(0)：得f(0)·(f(0)-2)=0，即f(0)∈{0,2}
  4. 令y=1：得x+f(x+1)∈S对所有x成立（S是不动点集）
  5. 情况1 f(0)=2：证明S中所有元素等于1，故x+f(x+1)=1，即f(x)=2-x
  6. 情况2 f(0)=0：先证f(1)=1（用x=1,y=-1和x=-1,y=1），再证f为奇函数f(-x)=-f(x)，最后用x和-x代入方程得f(x)=x

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 观察这个函数方程 f(x+f(x+y))+f(xy)=x+f(x+y)+yf(x)，描述它的结构特征：方程中f出现了几次？每次的参数形式是什么？未知量是什么？ | 方程中f出现4次：f(x+f(x+y))、f(xy)、f(x+y)、f(x)。参数形式涉及复合嵌套x+f(x+y)和乘积xy。未知量是函数f:ℝ→ℝ本身。目标是确定所有满足方程的f。这是一个函数方程 characterization 问题。 |
| 2 | 自由列举 | 0.7 | 列出所有你可能用来处理这个函数方程的方向和方法。 | 1) 代入特殊值(x=0,y=0等)提取约束；2) 假设f是线性函数f(x)=ax+b尝试；3) 研究不动点集；4) 证明f的单射/满射性；5) 研究f的奇偶性；6) 交换x,y的角色看对称性；7) 令y=-x消去项；8) 尝试递推关系。 |
| 3 | 小尝试 | 0.4 | 试一个最直接的方向：先假设f是线性函数f(x)=ax+b，代入方程看看能否确定a和b。 | 代入f(x)=ax+b：左边=a(x+a(x+y)+b)+b+a·xy+b=a(1+a)x+a²y+ab+2b+axy，右边=x+a(x+y)+b+y(ax+b)=(1+a)x+ay+b+axy+b。比较系数：y的系数a²=a→a=0或1。a=0时ab+2b=b+b→0=2b-b→b=0，但f=0不满足。a=1时ab+2b=2b+b=3b，右边2b，故b=0，得f(x)=x。但这个方法漏掉了f(x)=2-x这个解！因为f(x)=2-x不是线性的（是仿射的但a=-1时需重新检查）。实际上f(x)=2-x即a=-1,b=2，但代入时a²=1≠a=-1，说明直接假设线性会漏解。 |
| 4 | 思维操作引导 | 0.5 | 你发现直接假设线性函数会漏解。现在执行一个关键思维操作：定义不动点集S={t∈ℝ | f(t)=t}，然后令y=1代入原方程，看看能得到什么关于S的结论。 | 令y=1：f(x+f(x+1))+f(x)=x+f(x+1)+f(x)，两边消去f(x)得f(x+f(x+1))=x+f(x+1)。这说明x+f(x+1)∈S对所有x成立。即：对每个x，x+f(x+1)是f的不动点。 |
| 5 | 推进 | 0.4 | 继续推进：先令x=y=0和x=0,y=f(0)，提取关于f(0)的关键信息，然后基于f(0)的值分情况讨论。 | x=y=0：f(f(0))+f(0)=f(0)→f(f(0))=0。x=0,y=f(0)：f(f(0))+f(0)=f(0)+f(0)·f(0)→0+f(0)=f(0)+f(0)²→f(0)²=0... 等等需要更仔细：f(0+f(0))+f(0)=0+f(0)+f(0)·f(0)，即f(f(0))+f(0)=f(0)+f(0)²，用f(f(0))=0得f(0)=f(0)+f(0)²，故f(0)²=0... 不对，让我重新算。实际上从Lean代码看：x=0,y=f(0)给出f(f(0))+f(0)=f(0)+f(0)·f(0)，化简得f(0)·(f(0)-2)=0，所以f(0)∈{0,2}。 |
| 6 | 思维操作引导 | 0.5 | 现在处理f(0)=0的情况。执行以下思维操作：先令x=1,y=-1和x=-1,y=1求f(1)，然后利用y=0时x+f(x)∈S，以及y=1时x-1+f(x)∈S和x+1+f(x)∈S，推导f是奇函数。 | x=1,y=-1：f(1+f(0))+f(-1)=1+f(0)+(-1)f(1)→f(1)+f(-1)=1-f(1)（用f(0)=0）。x=-1,y=1：f(-1+f(0))+f(-1)=-1+f(0)+f(-1)→f(-1)+f(-1)=-1+f(-1)→f(-1)=-1。代回得f(1)=1。然后y=0给出x+f(x)∈S，y=1给出x-1+f(x)∈S。结合这些可推出f(-x)=-f(x)（奇函数）。 |
| 7 | 能量传递引导 | 0.6 | 你已经完成了最困难的部分：f(0)=0时f是奇函数，f(0)=2时f(x)=2-x。现在收尾：在f(0)=0且f为奇函数的条件下，令y=-x代入原方程，导出f(x)=x。 | 令y=-x：f(x+f(0))+f(-x²)=x+f(0)+(-x)f(x)→f(x)+f(-x²)=x-xf(x)（用f(0)=0和f(-x²)=-f(x²)）。再令x→-x,y=x：f(-x+f(0))+f(-x²)=-x+f(0)+xf(-x)→f(-x)+f(-x²)=-x+xf(-x)→-f(x)-f(x²)=-x-xf(x)。两个方程结合：f(x)+(-f(x²))=x-xf(x)和-f(x)+(-f(x²))=-x-xf(x)，相减得2f(x)=2x，即f(x)=x。完成！ |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 3
- level_sum: 0.8+0.7+0.4+0.5+0.4+0.5+0.6=3.9
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: 函数方程含4次f的复合与乘积参数，需确定所有满足方程的函数；方程中f的参数形式包括嵌套复合x+f(x+y)和乘积xy，具有代数与函数复合混合结构
- key_objects: [函数f:ℝ→ℝ, 不动点集S={t|f(t)=t}, f(0)的值, 奇函数性质f(-x)=-f(x)]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: [特殊值代入提取约束, 不动点集构造, 分情况讨论, 奇函数性质推导, 对称代入消元]
- primary_pattern: 不动点集构造+分情况讨论
- knowledge_required: [函数方程基本技巧, 不动点概念, 奇函数定义, 特殊值代入法, 分情况讨论]
- key_insight: 定义不动点集S并令y=1发现x+f(x+1)∈S，这是连接两个case的枢纽——f(0)=2时S={1}直接得f(x)=2-x，f(0)=0时通过S中元素的性质推导奇函数性。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 直接代数代入与线性假设（bare AI会尝试的方法）
- translation_to: 不动点集构造+分情况讨论的结构化方法（正确方法）
- translation_type: method_translation（从直接计算翻译到结构化分析）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: [不动点集, 特殊值代入, f(0)的值, 奇函数, 分情况讨论, y=1代入, x+f(x+1)∈S]
- expected_ai_method: 直接假设f为线性函数并代入方程比较系数，或盲目代入特殊值而不组织结构
- correct_method: 定义不动点集S，通过y=1代入发现x+f(x+1)∈S，按f(0)∈{0,2}分情况分别推导

### 6b. 反思拓扑分类

- [x] 当前拓扑分类是否够用——这道题的problem_type=characterization、ai_method_type=direct_calculation、gap_type=structural_transformation都能归入已有的拓扑类别，够用。
- [x] 粒度是否一致——标注的值和已有值的粒度统一，都是中等抽象层级。
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。

**拓扑进化建议**（如有）：无，现有拓扑分类体系足够。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs详情**：

| qa_round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对复杂函数方程，未识别出这是characterization问题，未注意到f出现4次的结构 | 观察方程结构，识别f的4次出现和参数形式，明确这是确定所有满足方程的函数的问题 | 0.8 | 纯元认知观察 | false | {problem_type: characterization, ai_method_type: direct_calculation, gap_type: method_problem_mismatch} | [函数方程结构, f的复合嵌套, 乘积参数xy] |
| 2 | AI列出方向但未意识到不动点集是关键枢纽，可能只想到直接代入 | 列出所有可能方向包括特殊值代入、不动点集、奇偶性、对称性等 | 0.7 | 自由列举 | false | {problem_type: characterization, ai_method_type: enumeration_brute_force, gap_type: search_space_estimation} | [特殊值代入, 不动点集, 奇偶性, 对称性] |
| 3 | AI假设f为线性函数f(x)=ax+b代入比较系数，只找到f(x)=x而漏掉f(x)=2-x | 试假设f(x)=ax+b代入方程，发现只得到f(x)=x，意识到线性假设会漏解 | 0.4 | 小尝试 | false | {problem_type: characterization, ai_method_type: direct_calculation, gap_type: method_problem_mismatch} | [线性假设, 系数比较, 漏解, f(x)=2-x] |
| 4 | AI未想到定义不动点集S作为结构化工具，停留在直接代入层面 | 定义不动点集S={t|f(t)=t}，令y=1代入发现x+f(x+1)∈S | 0.5 | 思维操作引导 | true | {problem_type: characterization, ai_method_type: direct_calculation, gap_type: knowledge_gap} | [不动点集S, y=1代入, x+f(x+1)∈S, 结构化工具] |
| 5 | AI未系统提取f(0)的约束，未想到按f(0)分情况 | 令x=y=0得f(f(0))=0，令x=0,y=f(0)得f(0)∈{0,2}，分情况讨论 | 0.4 | 推进 | false | {problem_type: characterization, ai_method_type: case_by_case, gap_type: structural_transformation} | [f(f(0))=0, f(0)∈{0,2}, 分情况讨论] |
| 6 | AI在f(0)=0情况下未想到先求f(1)再推导奇函数性，缺乏系统性的S元素分析 | 令x=1,y=-1和x=-1,y=1求f(1)=1，利用y=0和y=1时S的性质推导f为奇函数 | 0.5 | 思维操作引导 | true | {problem_type: characterization, ai_method_type: direct_calculation, gap_type: knowledge_gap} | [f(1)=1, 奇函数f(-x)=-f(x), S元素分析, y=0代入] |
| 7 | AI已得到f(0)=0时f为奇函数，但未想到用y=-x对称代入消元来最终确定f(x)=x | 在f为奇函数条件下令y=-x代入，结合x→-x,y=x的对称代入，相减得f(x)=x | 0.6 | 能量传递引导 | false | {problem_type: characterization, ai_method_type: logical_deduction, gap_type: method_translation} | [y=-x代入, 对称消元, f(x)=x, 收尾] |

**全局tell_hint_pairs详情**：

1. path_feature型：
- scope_type: path_feature
- scope: 整个解答路径——从特殊值代入到不动点集构造到分情况讨论到奇函数推导
- observation_point: null
- tell: 完整解答路径的特征是"先提取f(0)约束→定义不动点集S→按f(0)分两种情况→每种情况独立推导"。这个路径的关键转折在于R4定义S和R5分情况，而非R3的线性假设。
- hint: 不要停在直接代入或线性假设，需要引入不动点集作为结构化工具，并按f(0)的值分情况讨论
- hint_level: 0.6
- generalizability: high——函数方程characterization问题中，"提取关键参数值→定义辅助集合→分情况讨论"是通用路径模式
- why_not_visible_locally: 在局部视角中，每一步（如x=y=0代入、y=1代入）看起来都是独立的特殊值代入，无法看到这些代入需要被组织成"提取f(0)约束"和"建立不动点集S"两个阶段，更无法看到f(0)∈{0,2}会成为分情况的关键分岔点。完整路径的"先约束后分情况"结构只有在看到所有特殊值代入的结果后才能识别。
- tell_topology: {problem_type: characterization, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: [不动点集S, f(0)∈{0,2}, 分情况讨论, 路径组织, 特殊值代入系统化]

2. implicit型：
- scope_type: implicit
- scope: R3的线性假设尝试中隐含的信息——f(x)=2-x是非线性解，说明直接假设线性形式会漏解
- observation_point: R3
- tell: R3中AI假设f(x)=ax+b只找到f(x)=x，漏掉了f(x)=2-x。这隐含地告诉AI：这个函数方程的解空间不是纯线性的，需要更一般的分析方法。漏解本身是一个信号——说明解空间的结构比线性假设更丰富。
- hint: 从漏解信号中读出"解空间包含仿射函数f(x)=2-x"，放弃线性假设，转向不动点集分析
- hint_level: 0.5
- generalizability: medium——函数方程中"线性假设漏解"信号在其他问题中也可能出现，但具体漏哪个解因题而异
- why_not_visible_locally: 在R3的局部视角中，AI只看到"线性假设找到了f(x)=x但可能漏解"，这个漏解信号在局部步骤中表现为一个疑问而非明确方向。AI无法从单个步骤中看出f(x)=2-x是另一个解，也无法看出漏解意味着需要引入不动点集。这个蕴含信息需要跨步骤回看才能识别——只有当后续步骤引入S并发现f(0)=2对应f(x)=2-x时，R3的漏解才被解释。
- tell_topology: {problem_type: characterization, ai_method_type: direct_calculation, gap_type: method_problem_mismatch}
- tell_small_concepts: [线性假设漏解, f(x)=2-x, 解空间非纯线性, 仿射函数]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: bare AI会假设f为线性函数f(x)=ax+b，通过系数比较只找到f(x)=x，漏掉f(x)=2-x。即使尝试代入特殊值，也缺乏定义不动点集S并按f(0)分情况讨论的结构化思维，无法系统性地覆盖所有解。
- suitable_for_poc: [POC-VMS-hint-injection（hint端验证：注入不动点集定义的hint能否引导AI找到完整解）, POC-VMS-tell-detection（tell端验证：能否从AI的线性假设尝试中检测到漏解信号）, POC-VMS-level-discrimination（区分能力强：bare AI fail vs tree AI pass的对比明显）]
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
2. 更新`problem_extraction_progress`集合中`_key="329234"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2015p5"
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
    '_key': '329234',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2015p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2015p5')
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
- problem_id: compfiles_imo2015p5
- solution_method_type: fixed_point_set_case_analysis
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，现有拓扑分类体系（characterization / direct_calculation / structural_transformation等）足够覆盖本题
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
