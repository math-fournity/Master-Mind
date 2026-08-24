# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000253
- **文件路径**: subagents-dirs/omni_math_000253/problem.lean
- **来源**: AoPS omni_math (china_team_selection_test)
- **ArangoDB progress记录_key**: 330125（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000253/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：求所有整数对(m,n)使得存在两个monic多项式P(x),Q(x)，deg P=m, deg Q=n，满足P(Q(t))≠Q(P(t))对所有实数t成立。
- 解答核心思路（1-2句话）：分析P(Q(x))-Q(P(x))的次数奇偶性——奇次多项式必有实根（不可能），偶次多项式可构造为恒正/恒负（可能）。排除(1,1)（线性多项式必交换）和(2k,1),(1,2k)（差多项式为奇次），其余均可构造。
- 解答关键步骤列表：
  1. (1,1)不可能：P(x)=x+a, Q(x)=x+b，P(Q(x))=Q(P(x))=x+a+b恒成立
  2. (2k,1)或(1,2k)不可能：Q(x)=x+b时，P(Q(x))-Q(P(x))=P(x+b)-P(x)-b，次数为m-1（奇数），奇次多项式必有实根
  3. (m,1)且m为奇数≥3可行：取P(x)=x^m, Q(x)=x+a，差多项式(x+a)^m-x^m-a次数m-1（偶数），取a足够大可使其恒正
  4. (m,n)且m,n≥2可行：取P(x)=x^m+c, Q(x)=x^n+d，首项x^{mn}消去，次高项次数为max(n(m-1),m(n-1))，通过选择c,d（必要时添加低次项）使差多项式为偶次恒正

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
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：已知什么，求什么？P(Q(t))≠Q(P(t))对所有实数t成立意味着什么？ | 这是一个刻画问题：求所有整数对(m,n)使得存在monic多项式P,Q（deg P=m, deg Q=n）满足P(Q(t))≠Q(P(t))对所有实数t。关键观察：P(Q(x))-Q(P(x))是一个多项式，条件等价于该多项式无实根。 |
| 2 | 自由列举 | 0.7 | P(Q(x))-Q(P(x))是一个多项式，要让它无实根需要什么条件？列出所有可能的切入方向。 | 无实根的多项式必须是偶次且恒正或恒负。可能方向：(1)分析差多项式的次数和奇偶性；(2)从小case入手如(1,1),(2,1),(3,1)；(3)尝试具体构造P,Q；(4)分析首项消去后的次高项。 |
| 3 | 小尝试 | 0.3 | 试试(m,n)=(1,1)的情况。能构造出满足条件的P,Q吗？ | P(x)=x+a, Q(x)=x+b。P(Q(x))=x+b+a=Q(P(x))。线性monic多项式总是交换的，所以(1,1)不行。 |
| 4 | 思维操作引导 | 0.4 | 考虑(m,1)即Q(x)=x+b的情况。计算P(Q(x))-Q(P(x))的次数。这个次数的奇偶性意味着什么？ | P(Q(x))-Q(P(x))=P(x+b)-P(x)-b。若deg P=m，则P(x+b)-P(x)的首项来自(x+b)^m-x^m的展开，次数为m-1。所以差多项式次数为m-1。若m为偶数，m-1为奇数，奇次多项式必有实根→不可能。若m为奇数，m-1为偶数→可能。 |
| 5 | 推进 | 0.5 | 对于(m,1)且m为奇数≥3，构造具体的P,Q使差多项式恒正。 | 取P(x)=x^m, Q(x)=x+a (a>0)。差多项式=(x+a)^m-x^m-a，次数m-1（偶数），首项系数ma>0。当a足够大时，该多项式恒正（偶次正首项+足够大的常数偏移）。 |
| 6 | 思维操作引导 | 0.4 | 现在考虑m,n≥2。取P(x)=x^m+c, Q(x)=x^n+d。分析P(Q(x))-Q(P(x))的首项消去和次高项。如何选择c,d使差多项式无实根？ | P(Q(x))=(x^n+d)^m+c, Q(P(x))=(x^m+c)^n+d。首项x^{mn}消去。次高项：若m>n，次数为n(m-1)，系数md；若m<n，次数为m(n-1)，系数-nc。通过选择c,d使次高项为偶次且系数符号正确。当简单构造给出奇次时，添加低次项（如P(x)=x^m+ax+c）改变次数结构。 |
| 7 | 能量传递引导 | 0.6 | 综合所有情况，写出完整答案。哪些(m,n)不可能，哪些可能？ | 不可能：(1,1)（线性交换）、(2k,1)和(1,2k)（差多项式奇次必有实根）。可能：其余所有对——(m,1)和(1,m)当m为奇数≥3时可构造；(m,n)当m,n≥2时均可构造。答案：除(1,1),(1,2k),(2k,1)外所有整数对。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.7
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
- structure_features: 存在性刻画问题——求所有整数对(m,n)使得存在monic多项式P,Q满足P∘Q≠Q∘P处处成立。核心结构是差多项式P(Q(x))-Q(P(x))的次数奇偶性决定可行性。
- key_objects: ["monic多项式P,Q", "复合多项式P(Q(x))", "差多项式P(Q(x))-Q(P(x))", "多项式次数与奇偶性", "实根存在性"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["case_analysis", "degree_parity_analysis", "constructive_existence", "obstruction_identification", "leading_term_cancellation"]
- primary_pattern: degree_parity_analysis
- knowledge_required: ["多项式复合", "中间值定理（奇次多项式必有实根）", "monic多项式", "二项式展开", "首项消去分析"]
- key_insight: P(Q(x))-Q(P(x))的次数的奇偶性是主变量——奇次多项式必有实根（不可能构造），偶次多项式可构造为恒正/恒负（可能构造）。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 存在性刻画问题（求哪些(m,n)存在满足条件的P,Q）
- translation_to: 差多项式次数奇偶性分析（分析P(Q(x))-Q(P(x))的次数与实根存在性）
- translation_type: structural_transformation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: case_by_case, gap_type: structural_transformation}
- tell_small_concepts: ["差多项式无实根", "次数奇偶性", "首项消去", "构造性证明", "奇次必有实根", "monic多项式复合"]
- expected_ai_method: bare AI预期会枚举小case并尝试具体多项式，但可能错过差多项式次数奇偶性这一结构主变量，尤其在m,n≥2时首项消去后的次高项分析
- correct_method: 系统性分类分析——按(m,1)/(1,m)/(m,n≥2)分类，每类分析差多项式次数奇偶性，奇次→不可能（IVT），偶次→构造性证明

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=characterization、ai_method_type=case_by_case、gap_type=structural_transformation均可归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell
- [ ] 无需新拓扑维度

**拓扑进化建议**：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs摘要**：
- R1: tell=AI未识别差多项式无实根这一核心转化 / hint=识别P(Q(x))-Q(P(x))无实根等价条件 / level=0.8 / topology=(characterization, direct_calculation, structural_transformation) / concepts=["差多项式无实根","复合多项式"]
- R2: tell=AI列举方向但未优先差多项式次数分析 / hint=优先分析次数奇偶性 / level=0.7 / topology=(characterization, enumeration_brute_force, search_space_estimation) / concepts=["次数分析","奇偶性","方向优先级"]
- R3: tell=AI试(1,1)发现失败但未推广到次数模式 / hint=从(1,1)失败推广到一般模式 / level=0.3 / topology=(characterization, direct_calculation, method_problem_mismatch) / concepts=["线性多项式交换","复合恒等"]
- R4: tell=AI未看到m-1次决定可行性 / hint=分析差多项式次数=m-1及奇偶性 / level=0.4 / topology=(characterization, direct_calculation, knowledge_gap) / concepts=["差多项式次数","奇次必有实根","偶次可无实根"] / is_knowledge_bottleneck=True
- R5: tell=AI需要为可行case构造具体例子 / hint=取P=x^m,Q=x+a构造恒正差多项式 / level=0.5 / topology=(characterization, direct_manipulation, method_translation) / concepts=["构造性证明","平移幂函数","恒正多项式"]
- R6: tell=AI未处理m,n≥2时首项消去后的次高项 / hint=分析首项消去与次高项次数 / level=0.4 / topology=(characterization, algebraic_identity, structural_transformation) / concepts=["首项消去","次高项分析","系数选择"] / is_knowledge_bottleneck=False
- R7: tell=AI需综合所有case给出完整答案 / hint=综合分类结果 / level=0.6 / topology=(characterization, logical_deduction, method_problem_mismatch) / concepts=["分类综合","排除法"]

**全局pairs摘要**：
- GP1 (path_feature): tell=完整排除模式(1,1),(1,2k),(2k,1)仅在全部case分析后可见 / hint=系统性按(m,1)/(1,m)/(m,n≥2)分类 / level=0.7 / why_not_visible_locally=单个case分析只能看到该case是否可行，全局排除模式需要跨case比较——(1,2k)和(2k,1)被排除但(1,奇数)不被排除，这一对比在单个case中不可见 / topology=(characterization, case_by_case, structural_transformation) / concepts=["全局排除模式","跨case比较","奇偶性对比"]
- GP2 (implicit): tell=奇次多项式必有实根（IVT）是贯穿所有case的隐含原理 / hint=将次数奇偶性识别为主变量 / level=0.6 / why_not_visible_locally=该原理在每个case中以不同方式应用（(m,1)时直接用m-1奇偶性，(m,n≥2)时需先做首项消去再分析次高项奇偶性），跨case的统一原理在单个步骤中不可见 / topology=(characterization, logical_deduction, knowledge_gap) / concepts=["IVT隐含原理","奇次必有实根","次数奇偶性主变量"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI可能测试几个小case（如(1,1),(2,1)）发现模式，但在m,n≥2的情况会卡住——首项消去后的次高项分析需要精细的代数操作，且当简单构造给出奇次差多项式时需要添加低次项来改变次数结构，这一步需要创造性的构造思维。
- suitable_for_poc: ["tell识别在分类分析中", "构造引导（m,n≥2 case的构造性证明）", "跨case全局模式识别"]
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
2. 更新`problem_extraction_progress`集合中`_key="330125"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_000253"
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
    '_key': '330125',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_000253',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_000253')
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
- problem_id: omni_math_000253
- solution_method_type: case_analysis_with_construction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，已有拓扑分类（characterization/case_by_case/structural_transformation）足够覆盖
- 是否遇到异常: problem.lean中解答被截断（仅13行），基于题目描述和Answer重构了完整解答

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
