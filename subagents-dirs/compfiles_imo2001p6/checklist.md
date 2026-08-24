# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2001p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2001P6.lean
- **来源**: IMO 2001 P6
- **ArangoDB progress记录_key**: 329180（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2001P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let a, b, c, d be integers with a > b > c > d > 0. Suppose that ac + bd = (a + b - c + d)(-a + b + c + d). Prove that ab + cd is not prime.
- 解答核心思路（1-2句话）：通过建立恒等式证明 ac+bd 整除 (ab+cd)(ad+bc)，再假设 ab+cd 为素数利用素数整除性质分两种情形，每种情形用排序条件导出矛盾。
- 解答关键步骤列表：
  1. 建立关键恒等式：(ab+cd)(ad+bc) = (ac+bd)(b²+bd+d²)，即 ac+bd | (ab+cd)(ad+bc)
  2. 假设 ab+cd 为素数，由素数性质（若 p 素且 d | p·n 则 p | d 或 d | n）推出：ab+cd | ac+bd 或 ac+bd | ad+bc
  3. 情形1：ab+cd | ac+bd → ab+cd ≤ ac+bd，但 ab+cd - ac - bd = (a-d)(b-c) > 0（因 a>d, b>c），矛盾
  4. 情形2：ac+bd | ad+bc → ac+bd ≤ ad+bc，但 ac+bd - ad - bc = (a-b)(c-d) > 0（因 a>b, c>d），矛盾

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
| 1 | 纯元认知观察 | 0.8 | 请描述这道题的结构：已知什么、求证什么、有哪些约束条件？这些条件之间有什么联系？ | 已知 a>b>c>d>0 为整数，ac+bd=(a+b-c+d)(-a+b+c+d)，求证 ab+cd 非素数。约束包括严格排序和那个乘法等式。等式左边 ac+bd 是交叉乘积之和，右边是两个线性式的乘积。 |
| 2 | 自由列举 | 0.7 | 证明一个数"不是素数"有哪些常见策略？请列出你能想到的所有方向。 | ①直接因式分解 ab+cd ②反证法假设 ab+cd 是素数，利用等式推出矛盾 ③寻找整除关系 ④模运算分析 ⑤利用给定等式变形，看能否构造出 ab+cd 的非平凡因子 ⑥利用排序条件做不等式估计 |
| 3 | 小尝试 | 0.4 | 尝试直接对 ab+cd 进行因式分解，看看能否找到非平凡因子。 | ab+cd = ab + cd，无法直接因式分解。a,b,c,d 是独立变量，没有公因子可提取。直接分解这条路走不通。 |
| 4 | 思维操作引导 | 0.3 | 回到给定的等式 ac+bd=(a+b-c+d)(-a+b+c+d)。注意题目中出现了三个交叉乘积：ab+cd, ac+bd, ad+bc。尝试计算 (ab+cd)(ad+bc) 并利用给定等式观察它与 ac+bd 的整除关系。 | 展开 (ab+cd)(ad+bc) = a²bd+ab²c+acd²+bc²d。利用 ac+bd=(a+b-c+d)(-a+b+c+d) 代入变形，发现 (ab+cd)(ad+bc) = (ac+bd)(b²+bd+d²)。因此 ac+bd | (ab+cd)(ad+bc)。这是关键恒等式。 |
| 5 | 思维操作引导 | 0.3 | 现在已知 ac+bd | (ab+cd)(ad+bc)。如果用反证法假设 ab+cd 是素数 p，由素数的整除性质（若 p 素且 d | p·n 则 p | d 或 d | n）能推出什么？ | 若 p=ab+cd 素且 ac+bd | p·(ad+bc)，则 p | ac+bd 或 ac+bd | ad+bc。这把问题分成两种情形。 |
| 6 | 推进 | 0.2 | 分别分析两种情形，利用 a>b>c>d>0 的排序条件推导矛盾。 | 情形1：ab+cd | ac+bd → ab+cd ≤ ac+bd，但 ab+cd-ac-bd=(a-d)(b-c)>0（因 a>d, b>c），矛盾。情形2：ac+bd | ad+bc → ac+bd ≤ ad+bc，但 ac+bd-ad-bc=(a-b)(c-d)>0（因 a>b, c>d），矛盾。两种情形都矛盾，故 ab+cd 非素数。 |
| 7 | 能量传递引导 | 0.8 | 回顾整个证明，确认逻辑链条完整：恒等式→素数性质→分情形→排序矛盾。这个证明漂亮在哪里？ | 证明完整。关键在于发现 (ab+cd)(ad+bc) 能被 ac+bd 整除这一隐藏恒等式，将"非素数"问题转化为整除+排序矛盾。漂亮之处在于三个交叉乘积 ab+cd, ac+bd, ad+bc 之间的代数联系，以及排序条件在最后一步的精准应用。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.5
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R4（关键恒等式 (ab+cd)(ad+bc)=(ac+bd)(b²+bd+d²) 的发现是纯知识瓶颈）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R3（直接因式分解走不通后需要思维转换——从"分解 ab+cd"转向"寻找 ab+cd 与其他乘积的整除关系"）

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
- problem_type: constraint_satisfaction（给定等式约束+排序约束，证明关于 ab+cd 的性质）
- structure_features: 四个有序正整数 a>b>c>d>0 满足交叉乘积等式 ac+bd=(a+b-c+d)(-a+b+c+d)，需证明 ab+cd 非素数。核心结构是三个交叉乘积 ab+cd, ac+bd, ad+bc 之间的隐藏恒等关系，结合素数整除性质和排序不等式。
- key_objects: [有序整数组(a,b,c,d), 交叉乘积 ac+bd, 交叉乘积 ab+cd, 交叉乘积 ad+bc, 素数性质, 整除关系, 排序不等式]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [反证法, 隐藏恒等式发现, 整除传递, 分情形讨论, 排序不等式矛盾]
- primary_pattern: 隐藏恒等式发现（从给定约束中发现三个交叉乘积之间的代数恒等式，是整个证明的关键转折点）
- knowledge_required: [素数整除性质（Euclid引理推广：若p素且d|p·n则p|d或d|n）, 整数整除与大小关系（d|n且n>0则d≤n）, 代数恒等式展开与因式分解, 排序不等式估计]
- key_insight: 发现 (ab+cd)(ad+bc) = (ac+bd)(b²+bd+d²) 这一隐藏恒等式，将"ab+cd非素数"问题转化为"ac+bd整除含ab+cd的乘积"，从而可用素数性质分情形导出矛盾

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接因式分解/素性检测（对 ab+cd 直接操作的局部视角）
- translation_to: 交叉乘积间的整除关系+素数性质+排序矛盾（全局代数结构视角）
- translation_type: method_translation（从"直接操作目标表达式"翻译到"利用隐藏恒等式建立整除链，再借助素数性质和排序条件间接导出矛盾"）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: constraint_satisfaction, ai_method_type: direct_manipulation, gap_type: method_translation}
- tell_small_concepts: [交叉乘积, 隐藏恒等式, 整除传递, 素数性质, 排序不等式, 反证法]
- expected_ai_method: bare AI预期会直接尝试因式分解 ab+cd 或对给定等式做直接代数变形，试图直接构造出 ab+cd 的非平凡因子——这条路走不通
- correct_method: 发现 (ab+cd)(ad+bc)=(ac+bd)(b²+bd+d²) 隐藏恒等式，建立 ac+bd | (ab+cd)(ad+bc) 整除关系，用素数性质分情形，排序条件导出矛盾

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 可以。constraint_satisfaction 捕捉了"给定约束证明性质"的结构，direct_manipulation 捕捉了 bare AI 直接操作目标表达式的倾向，method_translation 捕捉了从直接操作到间接整除链的翻译需求。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 一致。三个值都是中等抽象粒度。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。这道题的核心 tell 是"AI 不会想到去计算 (ab+cd)(ad+bc) 并寻找它与 ac+bd 的整除关系"，这被 method_translation gap_type 很好地捕捉。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。

**拓扑进化建议**（如有）：无。现有拓扑分类足够。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 2 个，implicit型: 1 个

**局部pairs详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对题目尚未识别三个交叉乘积间的隐藏关系，只看到表面结构 | 描述题目结构，识别已知/未知/约束 | 0.8 | 纯元认知观察 | false | {constraint_satisfaction, direct_manipulation, method_problem_mismatch} | [题目结构, 已知未知, 约束条件] |
| 2 | AI列出多种策略但未列出"寻找交叉乘积间恒等式"方向 | 列出所有可能方向 | 0.7 | 自由列举 | false | {constraint_satisfaction, enumeration_brute_force, search_space_estimation} | [策略列举, 方向选择, 非素数证明] |
| 3 | AI尝试直接因式分解ab+cd失败，卡在无法直接操作目标表达式 | 尝试直接因式分解 | 0.4 | 小尝试 | false | {constraint_satisfaction, direct_manipulation, method_problem_mismatch} | [因式分解, 直接操作, 目标表达式] |
| 4 | AI未意识到要计算(ab+cd)(ad+bc)并寻找与ac+bd的整除关系——知识瓶颈 | 计算交叉乘积乘积并观察整除关系 | 0.3 | 思维操作引导 | true | {constraint_satisfaction, algebraic_identity, knowledge_gap} | [交叉乘积乘积, 隐藏恒等式, 整除关系, ac+bd] |
| 5 | AI有整除关系但不知如何用素数性质推进——知识瓶颈 | 用素数整除性质分情形 | 0.3 | 思维操作引导 | true | {constraint_satisfaction, logical_deduction, knowledge_gap} | [素数性质, Euclid引理, 整除分情形] |
| 6 | AI分出两种情形需用排序条件导出矛盾 | 用排序条件推导矛盾 | 0.2 | 推进 | false | {constraint_satisfaction, case_by_case, structural_transformation} | [排序不等式, 矛盾推导, 分情形] |
| 7 | 证明完成需回顾确认 | 回顾证明逻辑链 | 0.8 | 能量传递引导 | false | {constraint_satisfaction, logical_deduction, method_translation} | [逻辑链条, 证明回顾, 关键转折] |

**全局pairs详情**：

1. path_feature型:
- scope: 完整证明路径中R3失败到R4恒等式发现的转折
- observation_point: null
- tell: 从"直接因式分解ab+cd失败"到"发现交叉乘积间隐藏恒等式"的路径转折——整个证明的关键转折点
- hint: 当直接操作目标表达式失败时，寻找目标表达式与其他相关表达式之间的隐藏代数恒等关系
- hint_level: 0.6
- generalizability: high — 适用于任何"证明某表达式具有某性质"且直接操作失败的数论/代数问题
- why_not_visible_locally: 在R3局部视角中，AI只看到"ab+cd无法因式分解"这个失败信号，无法从这个局部失败推断出"应该去计算(ab+cd)(ad+bc)并寻找与ac+bd的整除关系"——这个路径特征需要同时看到R3的失败和R4的成功才能识别
- tell_topology: {constraint_satisfaction, direct_manipulation, method_translation}
- tell_small_concepts: [路径转折, 失败转向, 隐藏恒等式, 交叉乘积]

2. implicit型:
- scope: 给定等式 ac+bd=(a+b-c+d)(-a+b+c+d) 蕴含的隐藏整除关系
- observation_point: R4
- tell: 给定等式隐含了ac+bd与三个交叉乘积ab+cd,ad+bc之间的整除关系——这个蕴含信息在等式表面不可见
- hint: 从给定等式出发，寻找ac+bd与(ab+cd)(ad+bc)之间的整除关系
- hint_level: 0.5
- generalizability: medium — 适用于有给定代数约束的数论问题，但具体恒等式因题而异
- why_not_visible_locally: 在R1-R3的局部步骤中，AI看到等式ac+bd=(a+b-c+d)(-a+b+c+d)只会想到直接代入或变形，不会想到去计算一个看似无关的乘积(ab+cd)(ad+bc)——这个蕴含关系需要跨步骤的代数洞察才能发现
- tell_topology: {constraint_satisfaction, algebraic_identity, knowledge_gap}
- tell_small_concepts: [给定等式蕴含, 隐藏整除关系, 交叉乘积乘积, ac+bd]

3. path_feature型:
- scope: 素数性质+排序条件的协同使用路径（R5-R6）
- observation_point: null
- tell: 证明后半段的路径特征是"素数整除性质分情形+排序不等式导出矛盾"的协同——单独看素数性质或排序条件都无法完成证明
- hint: 当有整除关系和素数假设时，用素数性质分情形，再用排序/大小关系导出矛盾
- hint_level: 0.4
- generalizability: medium — 适用于"假设某数为素数+有整除关系+有大小约束"的数论反证法
- why_not_visible_locally: 在R5局部视角中，AI看到素数性质分出两种情形后，不会自动想到用排序条件来导出矛盾——需要同时看到R5的分情形结果和R6的排序应用才能识别这个协同模式
- tell_topology: {constraint_satisfaction, logical_deduction, structural_transformation}
- tell_small_concepts: [素数性质, 排序条件, 协同使用, 分情形矛盾]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会陷入直接因式分解ab+cd的死胡同，或对给定等式做表面变形但无法发现(ab+cd)(ad+bc)=(ac+bd)(b²+bd+d²)这一隐藏恒等式。即使想到反证法，也难以将素数整除性质与排序条件协同使用来导出矛盾。
- suitable_for_poc: ["tell端验证——隐藏恒等式发现的tell能否被形式化过滤命中", "hint端验证——从直接操作到间接整除链的方法翻译hint能否引导AI找到正确路径", "分阶段引导验证——R4恒等式发现是关键瓶颈，适合测试知识瓶颈注入的效果"]
- discriminates_levels: true（这道题需要发现非平凡的代数恒等式，bare AI几乎不可能自发发现，能有效区分有引导和无引导的AI表现）

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
2. 更新`problem_extraction_progress`集合中`_key="329180"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2001p6"
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
    '_key': '329180',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2001p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2001p6')
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
- problem_id: compfiles_imo2001p6
- solution_method_type: hidden_identity_with_prime_divisibility_contradiction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3（2个path_feature型，1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有拓扑分类（constraint_satisfaction / direct_manipulation / method_translation等）足够覆盖此题。
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
