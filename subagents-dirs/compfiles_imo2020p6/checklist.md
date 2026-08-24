# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2020p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2020P6.lean
- **来源**: IMO 2020 P6
- **ArangoDB progress记录_key**: 329257（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2020P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Consider an integer n > 1, and a set S of n points in the plane such that the distance between any two points in S is at least 1. Prove that there is a line l separating S such that the distance from any point of S to l is at least Ω(n^(-1/3)). (A line l separates a set of points S if some segment joining two points in S crosses l.)
- 解答核心思路（1-2句话）：对点集直径D做情况分析：若D≥n^(2/3)，沿直径方向投影后用鸽巢原理得到间距D/(2n)≥n^(-1/3)/2；若D<n^(2/3)，在端点附近取宽1/2的条带，用勾股定理 bound 垂直坐标≤√D，条带内点数≤6√D≤6n^(1/3)，再在垂直方向用鸽巢原理得到间距≥1/(24√D)≥Ω(n^(-1/3))。
- 解答关键步骤列表：
  1. exists_between_and_separated：将区间[a,b]分成n个等距子区间，若每个子区间都有点则用鸽巢矛盾（点数<n），否则取空子区间中点，所有点到该点距离≥(b-a)/(2n)
  2. exists_affine_between_and_separated：将上述1D结果推广到几何——沿ab方向投影，找到垂直于ab的超平面l，使所有点到l的距离≥(j-i)/(2n)
  3. card_le_of_separated：在区间[a,b]内间距≥ε的点集大小≤⌊(b-a)/ε+1⌋
  4. card_le_of_separated_in_strip：宽1/2条带内、点间距≥1、垂直坐标|y|≤N的点数≤6N-1
  5. Case 1（D≥n^(2/3)）：直接沿ab方向投影，n个点在[0,D]中，鸽巢给出间距≥D/(2n)≥n^(-1/3)/2
  6. Case 2（D<n^(2/3)）：取最大距离对a,b，建立坐标系（a为原点，ab为x轴），条带{x∈(0,1/2)}内点的垂直坐标≤√D（因到b的距离≤D且x方向偏移<D/2），条带内点数≤6√D，在垂直方向用鸽巢得到间距≥(1/2)/(2·6√D)≥Ω(n^(-1/3))
  7. 取常数c=1/100，两种情况均满足c·n^(-1/3)的界

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
| 1 | 纯元认知观察 | 0.7 | 这道题的结构是什么？我们需要找什么？"分离"条件对这条线施加了什么约束？ | 需要找一条线l，使得S中某两点的连线段穿过l（分离条件），且S中所有点到l的距离≥c·n^(-1/3)。分离条件意味着l必须在S中两个点之间。关键是在"两个点之间"和"远离所有点"之间找平衡。 |
| 2 | 自由列举 | 0.6 | 列出所有可能的方法来找到这条线。考虑：投影到某个方向、利用点集直径、鸽巢原理、概率方法等。 | 1) 沿某方向投影后用鸽巢原理找空隙；2) 利用点集直径D，沿直径方向投影；3) 概率方法随机选方向；4) 归纳法；5) 利用最小距离条件做计数论证。关键观察：沿直径方向投影后n个点落在长度D的区间内，鸽巢给出间距D/n。 |
| 3 | 小尝试 | 0.4 | 试沿直径方向投影并用鸽巢原理。你得到什么界？这个界如何依赖于直径D？ | n个点投影到长度D的区间，分成n个子区间，至少有一个空区间，取中点得到间距≥D/(2n)。但这个界依赖于D——如果D很大（如D≥n^(2/3)），则D/(2n)≥n^(-1/3)/2足够好。但如果D很小呢？此时D/n可能远小于n^(-1/3)。 |
| 4 | 思维操作引导 | 0.5 | 你得到了D/(2n)的界，但它依赖于D。当D很大和D很小时分别会发生什么？能否以某个阈值做情况分析？阈值应该取多少才能让两种情况都给出n^(-1/3)？ | 若D≥n^(2/3)，则D/(2n)≥n^(-1/3)/2，直接完成。若D<n^(2/3)，需要不同方法。阈值n^(2/3)的选择使得：大D情况给出D/n≥n^(-1/3)，小D情况中√D≤n^(1/3)，两种情况的界都匹配n^(-1/3)。 |
| 5 | 推进 | 0.4 | 在D<n^(2/3)的情况中，取最大距离对a,b建立坐标系（a为原点，ab为x轴）。考虑a附近宽1/2的条带{x∈(0,1/2)}，条带内点的垂直坐标有什么上界？ | 条带内点p到b的距离≤D（因a,b是最大距离对）。p的x坐标∈(0,1/2)，b的x坐标=D，所以x方向差≤D。由距离≤D和勾股定理：y²≤D²-x²≤D²，更精确地y²≤D²-(D-1/2)²≈D-1/4，所以|y|≤√D。 |
| 6 | 思维操作引导 | 0.3 | 现在你知道条带内点的垂直坐标≤√D。利用最小距离≥1的条件，条带内能有多少个点？然后如何用鸽巢原理在垂直方向找空隙？ | 条带内点间距≥1，垂直坐标|y|≤√D，用间距计数：点数≤2√D/(1/2)+1≈4√D+1≤6√D（用card_le_of_separated）。然后在垂直方向[−√D,√D]中对≤6√D个点用鸽巢：间距≥2√D/(2·6√D)=1/12。但需要的是在条带[0,1/2]的垂直方向找分离线，间距≥(1/2)/(2·6√D)≥1/(24n^(1/3))=Ω(n^(-1/3))。 |
| 7 | 能量传递引导 | 0.8 | 两种情况都给出了Ω(n^(-1/3))的界。验证指数匹配并合并结果，取适当的常数c。 | Case 1: D/(2n)≥n^(2/3)/(2n)=n^(-1/3)/2。Case 2: (1/2)/(12√D)≥1/(24n^(1/3))=n^(-1/3)/24。两种情况都给出Ω(n^(-1/3))，取c=1/100即可统一。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.7
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
- structure_features: 情况分析基于直径阈值n^(2/3)；1D投影+鸽巢原理；条带论证用于有界直径情况；指数平衡n^(2/3)使两种情况均给出n^(-1/3)
- key_objects: ["最小间距≥1的点集", "分离线", "点集直径D", "投影方向", "宽1/2条带", "垂直坐标√D上界"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["情况分析(按直径阈值n^(2/3))", "降维投影(2D→1D鸽巢)", "参数化界+指数匹配", "条带计数+二次鸽巢", "勾股定理bound垂直坐标"]
- primary_pattern: 情况分析+降维投影+鸽巢
- knowledge_required: ["鸽巢原理(区间分箱找空隙)", "点集直径", "勾股定理距离bound", "间距计数引理(card_le_of_separated)", "仿射投影与分离线", "指数平衡n^(-1/3)"]
- key_insight: 以直径D与n^(2/3)为阈值分情况——大D直接沿直径方向投影鸽巢得D/(2n)≥n^(-1/3)/2；小D取最大距离对建坐标系，在宽1/2条带内用勾股定理bound垂直坐标≤√D，间距计数得点数≤6√D，再在垂直方向鸽巢得间距≥1/(24√D)≥Ω(n^(-1/3))

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 1D区间鸽巢原理（区间分箱找空隙）
- translation_to: 2D几何分离线存在性（仿射投影+垂直超平面）
- translation_type: 维度提升翻译（1D鸽巢→2D几何投影→分离线存在性）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: case_by_case, gap_type: structural_transformation}
- tell_small_concepts: ["直径阈值n^(2/3)", "1D投影鸽巢", "条带计数", "勾股定理bound垂直坐标", "指数平衡n^(-1/3)", "间距计数引理"]
- expected_ai_method: direct_calculation（bare AI可能直接沿一个方向投影用鸽巢，不处理D小的情况）
- correct_method: case_by_case（按直径阈值n^(2/3)分两种情况，每种用不同策略）

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 可以。problem_type=structural_existence（存在性证明），ai_method_type=case_by_case（分情况讨论），gap_type=structural_transformation（需要将1D鸽巢翻译到2D几何并做情况分析的结构变换）均已有。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 一致。都是抽象层级的大概念。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。三个维度能区分这道题的tell（structural_existence + case_by_case + structural_transformation）。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。已有分类体系完全覆盖。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**局部tell_hint_pairs**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对存在性证明题，尚未识别"分离条件"与"距离下界"之间的张力——不知道需要在"两点之间"和"远离所有点"之间找平衡 | 描述题目结构，识别已知/未知，分离条件对线施加什么约束 | 0.7 | 纯元认知观察 | false | {structural_existence, direct_calculation, method_problem_mismatch} | ["分离条件", "距离下界Ω(n^(-1/3))", "点集间距≥1"] |
| 2 | AI列出方向但未识别"直径D"是关键参数——枚举了投影/鸽巢/概率/归纳但未聚焦 | 列出所有可能方法，考虑投影、鸽巢、直径等 | 0.6 | 自由列举 | false | {structural_existence, enumeration_brute_force, search_space_estimation} | ["投影方向", "鸽巢原理", "点集直径D", "概率方法"] |
| 3 | AI沿直径方向投影得到D/(2n)的界，但未注意到D小时的失效——只处理了一种情况 | 试沿直径方向投影用鸽巢，分析界对D的依赖 | 0.4 | 小尝试 | false | {structural_existence, direct_calculation, method_problem_mismatch} | ["直径投影", "鸽巢间距D/(2n)", "D依赖性"] |
| 4 | AI得到D/(2n)界但未想到分情况处理，未找到阈值n^(2/3)——思维瓶颈在于指数匹配 | 分析D大和D小两种情况，找阈值使两种情况都给出n^(-1/3) | 0.5 | 思维操作引导 | false | {structural_existence, case_by_case, structural_transformation} | ["直径阈值n^(2/3)", "情况分析", "指数平衡n^(-1/3)"] |
| 5 | AI在D<n^(2/3)情况中，未想到用条带和勾股定理bound垂直坐标——知识瓶颈 | 建立坐标系，考虑a附近宽1/2条带，bound条带内点的垂直坐标 | 0.4 | 推进 | true | {structural_existence, direct_calculation, knowledge_gap} | ["坐标系建立", "宽1/2条带", "勾股定理bound", "垂直坐标≤√D"] |
| 6 | AI知道垂直坐标≤√D但未想到用间距计数+垂直方向鸽巢——知识瓶颈 | 利用最小距离≥1计数条带内点数，再用鸽巢在垂直方向找空隙 | 0.3 | 思维操作引导 | true | {structural_existence, direct_calculation, knowledge_gap} | ["间距计数", "条带内点数≤6√D", "垂直方向鸽巢", "间距≥1/(24√D)"] |
| 7 | AI两种情况都得到Ω(n^(-1/3))界，需要合并验证并取常数 | 验证指数匹配，合并结果，取常数c | 0.8 | 能量传递引导 | false | {structural_existence, direct_calculation, method_problem_mismatch} | ["指数匹配", "常数c=1/100", "两种情况合并"] |

**全局tell_hint_pairs**：

| # | scope_type | scope | observation_point | tell | hint | hint_level | generalizability | why_not_visible_locally | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | path_feature | 整个证明的分情况策略 | null | 证明的核心结构是按直径D与n^(2/3)比较分两种情况，阈值选择使两种情况的界都匹配n^(-1/3) | 当一个参数依赖的界在不同参数范围有不同行为时，找阈值使两种情况都给出目标指数 | 0.7 | high——适用于任何参数依赖界的存在性证明，指数匹配是通用技巧 | 在单步视角中AI只看到D/(2n)的界，无法看到"为什么阈值是n^(2/3)"——需要同时看到两种情况的界并做指数匹配，是完整路径的全局特征 | {structural_existence, case_by_case, structural_transformation} | ["直径阈值n^(2/3)", "指数平衡", "情况分析"] |
| 2 | path_feature | 从1D鸽巢到2D分离线的翻译链 | null | 1D区间鸽巢原理通过投影推广到2D几何——沿某方向投影后找垂直分离线 | 当2D问题难以直接处理时，投影到1D用鸽巢找空隙，再翻译回2D几何 | 0.6 | high——投影降维+鸽巢是通用的组合几何技巧 | 在局部步骤中AI看到的是具体投影计算，无法看到"1D鸽巢→2D几何"这个翻译模式——需要理解整个证明的降维策略 | {structural_existence, direct_calculation, method_translation} | ["1D鸽巢", "投影降维", "垂直分离线", "affine subspace"] |
| 3 | implicit | R5-R6中的条带论证 | "R5" | 条带内点的垂直坐标≤√D这个bound来自勾股定理和最大距离对的定义——蕴含关系跨步骤 | 当点在条带内且到远端点距离≤D时，用勾股定理bound垂直坐标 | 0.4 | medium——适用于条带+距离约束的几何问题 | 在局部步骤中AI只看到"垂直坐标≤√D"的结论，但这个bound的来源（勾股定理+最大距离对+条带宽度）是跨步骤的蕴含信息 | {structural_existence, direct_calculation, knowledge_gap} | ["勾股定理bound", "最大距离对", "条带宽度1/2", "垂直坐标≤√D"] |

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 2 个，implicit型: 1 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI大概率沿一个方向（如直径方向）投影用鸽巢得到D/(2n)的界，但不处理D小的情况——不会想到按n^(2/3)分情况，也不会想到条带+勾股定理bound+二次鸽巢的策略。即使想到分情况，也很难自己发现阈值n^(2/3)使两种情况的指数都匹配n^(-1/3)。
- suitable_for_poc: ["tell_hint_injection（验证tell+hint注入能否引导AI发现分情况策略）", "topology_matching（验证形式化过滤能否命中structural_transformation拓扑的tell）", "concept_resolution（验证小概念标记分辨能否区分R5的knowledge_gap和R4的structural_transformation）"]
- discriminates_levels: true（这道题区分度高——bare AI几乎不可能完成，但给定正确的tell+hint后中等水平AI应该能推进）

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
2. 更新`problem_extraction_progress`集合中`_key="329257"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2020p6"
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
    '_key': '329257',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2020p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2020p6')
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
- problem_id: compfiles_imo2020p6
- solution_method_type: case_by_case
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3（path_feature型2个，implicit型1个）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有分类体系完全覆盖
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
