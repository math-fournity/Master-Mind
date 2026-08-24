# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2006p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2006P5.lean
- **来源**: USA 2006 P5
- **ArangoDB progress记录_key**: 329426（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2006P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：一只数学青蛙沿数轴跳跃。青蛙从1出发，跳跃规则为：若青蛙在整数n处，则可跳到n+1或n+2^(m_n+1)，其中2^m_n是整除n的最大的2的幂。证明：若k≥2是正整数，i是非负整数，则到达2^i·k所需的最少跳跃次数大于到达2^i所需的最少跳跃次数。
- 解答核心思路（1-2句话）：从到达2^i·k的任意有效路径中，通过"过滤"操作删除落在2^i之后的特定大小的跳跃，证明剩余路径仍然有效且到达2^i，且长度严格更短。通过对最大跳跃大小做归纳，提取出一条到达2^i的严格更短的有效路径。
- 解答关键步骤列表：
  1. 定义2-adic赋值ν₂(n)和有效路径ValidPath
  2. 定义过滤操作filt：删除长度被2^(e+1)整除且落在阈值c之后的跳跃
  3. 证明nu_congr：若2^e | (y-y')且ν₂(y)<e则ν₂(y')=ν₂(y)（2-adic赋值在平移下不变）
  4. 证明filt_valid：过滤后路径仍然有效（核心引理，依赖nu_congr）
  5. 证明filt_count：被删除的跳跃总数和长度都是2^(e+1)的倍数
  6. 证明filt_lower：若有跳跃被删除，则存在位置p'使ν₂(p')=e
  7. 证明filt_bigbound：过滤后剩余跳跃的长度不超过2^e
  8. key_lemma（对e归纳）：从到达≥2^i的有效路径中提取到达2^i的有效路径，长度不超过原路径，端点超过2^i时严格更短
  9. 主定理：对到达2^i·k的最短路径应用key_lemma，因k≥2故2^i·k>2^i，提取的路径严格更短，故minJumps(2^i)<minJumps(2^i·k)

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
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：跳跃规则是什么？ν₂(n)在这里起什么作用？需要证明什么？已知和未知分别是什么？ | 题目定义了一个青蛙跳跃问题：从1出发，在n处可跳到n+1或n+2^(ν₂(n)+1)。需要证明对k≥2和i≥0，到达2^i·k的最少跳跃次数严格大于到达2^i的最少跳跃次数。已知是跳跃规则，未知是两个最少跳跃次数的大小关系。 |
| 2 | 自由列举 | 0.7 | 列出所有可能的方法来比较到达2^i·k和2^i的最少跳跃次数：直接计算、贪心策略、对i归纳、对k归纳、路径操作、路径提取等 | 可能的方法包括：(1)直接计算小例子找规律；(2)贪心策略——总跳最大步；(3)对i归纳；(4)对k归纳；(5)路径操作——从一条路径变换出另一条；(6)路径提取——从到达2^i·k的路径中提取到达2^i的更短路径 |
| 3 | 小尝试 | 0.4 | 试着直接计算小例子：minJumps(2), minJumps(4), minJumps(6), minJumps(8)等，看看能否发现规律 | 计算小例子：从1出发，1→2(1步), 1→2→4(2步), 1→2→4→8(3步)...到达6: 1→2→4→5→6(4步)或1→2→3→6(3步,因ν₂(3)=0故跳2^1=2)。到达2^i的步数似乎与i有关，但一般性规律难以直接总结。 |
| 4 | 思维操作引导 | 0.3 | 不要直接计算minJumps。换一个角度思考：给定到达2^i·k（其中k≥2，所以2^i·k>2^i）的任意一条有效路径，能否从中"提取"出一条到达2^i的有效路径，且这条新路径严格更短？ | 关键思路转变：不是直接比较两个minJumps，而是从到达更大目标的路径中提取到达更小目标的更短路径。如果能证明对任意到达2^i·k的路径都能提取出严格更短的到达2^i的路径，则minJumps(2^i)<minJumps(2^i·k)自然成立。 |
| 5 | 思维操作引导 | 0.3 | 考虑从有效路径中"删除"某些跳跃。关键问题：删除一个长度为2^(e+1)的跳跃后，后续位置的2-adic赋值是否改变？思考：若2^e整除位置差y-y'，且ν₂(y)<e，则ν₂(y')=ν₂(y)是否成立？ | 这是核心知识瓶颈。当删除一个长度为2^(e+1)的跳跃时，后续所有位置都平移了2^(e+1)的倍数。关键引理nu_congr：若2^e | (y-y')且ν₂(y)<e，则ν₂(y')=ν₂(y)。这意味着只要后续位置的赋值小于e，删除2^(e+1)大小的跳跃不会改变这些位置的赋值，从而保持路径有效性。 |
| 6 | 推进 | 0.2 | 定义过滤操作filt：删除所有长度被2^(e+1)整除且落在2^i之后的跳跃。证明：(1)过滤后路径仍有效(filt_valid)；(2)删除的跳跃数和长度都是2^(e+1)的倍数(filt_count)；(3)剩余跳跃长度≤2^e(filt_bigbound)。然后对e做归纳建立key_lemma。 | 过滤操作的核心性质：filt_valid依赖nu_congr保证删除跳跃后路径有效性不变；filt_count保证过滤后端点仍被2^min(i,e)整除；filt_bigbound保证剩余跳跃的界降一级。对e归纳：e=0时所有超过2^i的跳跃长度为1，前缀恰好到达2^i；e→e+1时先过滤2^(e+1)大小的跳跃，再用归纳假设处理剩余的≤2^e的跳跃。 |
| 7 | 能量传递引导 | 0.5 | 现在将key_lemma应用到主定理：取到达2^i·k的最短路径，验证条件后应用key_lemma提取到达2^i的严格更短路径，完成证明。 | 主定理证明：取ss为到达2^i·k的最短路径(长度=minJumps(2^i·k))。因k≥2，端点2^i·k>2^i。所有跳跃长度≤2^(i+ss.sum)（因每步≤sum≤2^sum）。端点被2^i整除。应用key_lemma(i, i+ss.sum, ss)得到到达2^i的有效路径ss'，长度严格小于ss。故minJumps(2^i)≤|ss'|<|ss|=minJumps(2^i·k)。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4 (R1, R2, R6, R7)
- knowledge_rounds（思维操作引导的轮数）: 2 (R4, R5)
- level_sum: 3.2
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
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
- problem_type: discrete_combinatorial
- structure_features: 路径优化比较问题；2-adic赋值依赖的跳跃规则；过滤/删除操作保持路径有效性；对最大跳跃大小做归纳提取更短路径
- key_objects: 2-adic赋值ν₂(n), 有效路径(ValidPath), 跳跃序列, 过滤操作(filt), 最少跳跃次数(minJumps), BigBound界

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["filtration/deletion（过滤删除）", "structural_induction（结构归纳）", "path_extraction（路径提取）", "2-adic_valuation_preservation（2-adic赋值不变性）", "bound_reduction（界递降）"]
- primary_pattern: filtration/deletion（过滤删除）——核心思想是从有效路径中删除特定跳跃，证明剩余路径仍有效且更短
- knowledge_required: ["2-adic赋值ν₂(n)的定义和性质", "2的幂的整除性", "路径有效性条件", "自然数归纳法", "整数的整除传递性"]
- key_insight: 删除长度为2^(e+1)的跳跃后，后续位置平移了2^(e+1)的倍数，而2-adic赋值在平移2^e的倍数下不变（当赋值<e时），因此过滤后路径仍然有效

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接路径比较/贪心优化（试图直接计算或比较两个minJumps）
- translation_to: 过滤操作+结构归纳（从到达更大目标的路径中提取到达更小目标的更短路径）
- translation_type: method_translation（方法翻译——从直接比较翻译为路径提取）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "direct_calculation", gap_type: "structural_transformation"}
- tell_small_concepts: ["2-adic赋值", "路径过滤", "跳跃删除", "有效性保持", "归纳提取", "最少跳跃比较"]
- expected_ai_method: direct_calculation——bare AI会试图直接计算minJumps或对小例子找规律，可能尝试贪心策略
- correct_method: 过滤删除+结构归纳——正确方法是从到达更大目标的路径中通过过滤操作提取到达更小目标的严格更短路径

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type(discrete_combinatorial)/ai_method_type(direct_calculation)/gap_type(structural_transformation)都能归入已有的拓扑类别
- [x] 粒度是否一致——标注的值和已有值的粒度统一，都是中等抽象级别
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化，现有拓扑分类充分

**拓扑进化建议**（如有）：无，现有拓扑分类体系充分覆盖此题。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs摘要**：
- R1: tell=青蛙跳跃问题结构未识别, hint=描述题目结构和已知/未知, level=0.8, 纯元认知观察, topology=(discrete_combinatorial, direct_calculation, structural_transformation)
- R2: tell=未识别关键结构方法, hint=列举所有可能方法, level=0.7, 自由列举, topology=(discrete_combinatorial, enumeration_brute_force, method_problem_mismatch)
- R3: tell=直接计算小例子陷入搜索空间, hint=试算小例子, level=0.4, 小尝试, topology=(discrete_combinatorial, direct_calculation, search_space_estimation)
- R4: tell=未想到路径提取策略, hint=从到达更大目标的路径提取更短路径, level=0.3, 思维操作引导, topology=(discrete_combinatorial, direct_calculation, structural_transformation)
- R5: tell=不知道2-adic赋值平移不变性, hint=证明nu_congr引理, level=0.3, 思维操作引导, is_knowledge_bottleneck=true, topology=(discrete_combinatorial, direct_manipulation, knowledge_gap)
- R6: tell=理解赋值不变性但未形式化过滤操作, hint=定义filt并证明其性质+归纳, level=0.2, 推进, topology=(discrete_combinatorial, logical_deduction, structural_transformation)
- R7: tell=有key_lemma需组装主定理, hint=应用key_lemma完成证明, level=0.5, 能量传递引导, topology=(discrete_combinatorial, logical_deduction, method_problem_mismatch)

**全局tell_hint_pairs摘要**：
- path_feature型: tell=需要非显然的结构变换（路径提取而非直接比较）, hint=用过滤操作从到达2^i·k的路径提取到达2^i的更短路径, level=0.3, generalizability=high
- implicit型: tell=2-adic赋值在平移2^e倍数下不变是隐藏的数学事实, hint=证明nu_congr引理, level=0.2, observation_point=R5, generalizability=medium

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接计算minJumps的小例子或使用贪心策略，可能证明特殊情况但无法发现过滤/删除操作这一关键结构变换。AI可能陷入搜索空间的计算而无法跳出到路径提取的抽象层面。
- suitable_for_poc: ["tell_de_specialization", "formal_filtering", "concept_disambiguation"]
- discriminates_levels: true——此题需要深层结构洞察（路径提取+2-adic赋值不变性），能有效区分强/弱数学推理能力

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
2. 更新`problem_extraction_progress`集合中`_key="329426"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa2006p5"
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
    '_key': '329426',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa2006p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa2006p5')
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
- problem_id: compfiles_usa2006p5
- solution_method_type: filtration_induction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，现有拓扑分类体系（discrete_combinatorial / direct_calculation / structural_transformation等）充分覆盖此题
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
