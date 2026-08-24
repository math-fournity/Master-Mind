# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2020p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2020P5.lean
- **来源**: IMO 2020 P5
- **ArangoDB progress记录_key**: 329256（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2020P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：A deck of n > 1 cards is given. A positive integer is written on each card. The deck has the property that the arithmetic mean of the numbers on each pair of cards is also the geometric mean of the numbers on some collection of one or more cards. For which n does it follow that the numbers on the cards are all equal?
- 解答核心思路（1-2句话）：对所有 n > 1 成立。将所有数除以gcd（性质在缩放下不变），化为互质情形；若最大值 M ≥ 2，取素数 P | M 及不被 P 整除的最大值 b，对 (M, b) 用AM-GM性质推出 P | b 矛盾，故 M = 1 所有数相等。
- 解答关键步骤列表：
  1. 除以gcd——AM-GM性质在缩放下不变，化为互质情形
  2. 互质后gcd=1
  3. 取最大值所在卡片 i1，若最大值 ≤ 1 则所有值为1，完成
  4. 若最大值 ≥ 2：取素数 P | 最大值，因gcd=1故存在不被P整除的值，取其中最大者 b
  5. 对 (M, b) 用性质：(M+b)/2 = 某集合S的几何平均
  6. 因 (M+b)/2 > b，S中必含 > b 的值，该值被P整除（由b的选取），故P | ∏S
  7. 由 (M+b)^|S| = 2^|S| · ∏S，P | (M+b)^|S|，P素数故P | M+b，又P | M故P | b，矛盾
  8. 结论：M=1，所有值=1（互质），原值全等于gcd=d，答案为所有 n > 1

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
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：已知条件是什么？未知是什么？AM-GM条件在什么变换下不变？ | 已知：n>1张卡片上有正整数，每对卡片的算术平均等于某组卡片的几何平均。未知：对哪些n这迫使所有数相等。不变性：缩放下AM和GM同时缩放，性质保持。 |
| 2 | 自由列举 | 0.7 | 列出所有可能的解题方向：小情形验证、缩放归约、极值论证、数论方法等 | 1)验证n=2,3小情形；2)除以gcd化为互质；3)取最大值做极值论证；4)用素数整除性；5)直接代数操作AM=GM条件；6)归纳法 |
| 3 | 小尝试 | 0.4 | 试n=2：对每对卡片，AM等于某子集的GM。子集有哪些可能？能推出什么？ | n=2时子集只能是{a},{b},{a,b}。{a}:(a+b)/2=a→a=b；{b}:同理a=b；{a,b}:(a+b)/2=√(ab)→a=b。n=2平凡成立，但此方法难以推广到一般n。 |
| 4 | 思维操作引导 | 0.5 | 将所有卡片值除以它们的gcd。验证AM-GM性质在缩放下不变，从而可以假设所有值互质。 | 设d=gcd，g_i=f_i/d。AM: (f_a+f_b)/2=d·(g_a+g_b)/2。GM: (∏f_i)^(1/k)=d·(∏g_i)^(1/k)。两边消去d，性质保持。互质后gcd(g_i)=1。 |
| 5 | 思维操作引导 | 0.4 | 在互质情形下，设最大值M≥2。取素数P|M，因gcd=1存在不被P整除的值，取其中最大者b。对(M,b)用AM-GM性质，分析集合S中必含大于b的值。 | (M+b)/2>b，若S中所有值≤b则GM≤b<(M+b)/2矛盾。故S含值>b，由b的选取该值被P整除。故P|∏S。由(M+b)^|S|=2^|S|·∏S得P|(M+b)^|S|，P素数故P|M+b，又P|M故P|b，矛盾。 |
| 6 | 推进 | 0.3 | 完成矛盾推导：从P|∏S到P|b的完整链条 | P|∏S（因S含被P整除的值），(M+b)^k=2^k·∏S故P|(M+b)^k，P素数→P|M+b，P|M→P|b，但b选取时要求P∤b，矛盾。故M=1。 |
| 7 | 能量传递引导 | 0.6 | 总结：M=1意味着什么？原始值如何？最终答案是什么？ | M=1且互质→所有g_i=1→所有f_i=d。故对所有n>1，性质迫使所有卡片值相等。答案：所有n>1。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.7
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: 逐对AM-GM条件约束卡片值；缩放不变性（除以gcd）；极值选取+素数整除性导出矛盾
- key_objects: ["卡片上的正整数", "算术平均（逐对）", "几何平均（子集）", "所有值的gcd", "最大值M", "整除最大值的素数P", "不被P整除的最大值b"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["extremal_principle", "scaling_reduction", "contradiction_argument", "prime_divisibility_argument", "strategic_pair_selection"]
- primary_pattern: extremal_contradiction_with_number_theoretic_reduction
- knowledge_required: ["算术平均与几何平均", "gcd与互质性", "素数分解与整除性", "AM-GM条件的缩放不变性", "极值原理", "反证法"]
- key_insight: 除以gcd化为互质情形后，取整除最大值的素数P和不被P整除的最大值b，对(M,b)用AM-GM条件推出P|b的矛盾

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 解析AM-GM条件（分析/代数语言）
- translation_to: 数论整除性论证（素数、gcd、整除链）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_manipulation, gap_type: method_translation}
- tell_small_concepts: ["gcd scaling", "coprime reduction", "prime divisibility", "extremal selection", "AM-GM to number theory", "contradiction"]
- expected_ai_method: 直接操作AM=GM条件，尝试代数变形或逐案验证小情形
- correct_method: 除以gcd化为互质，用素数整除性和极值选取构造矛盾

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——characterization/direct_manipulation/method_translation均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell
- [x] 无需进化建议

**拓扑进化建议**（如有）：无

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
- 每个pair均含tell_topology和tell_small_concepts
- 全局pair均含why_not_visible_locally（非None）
- knowledge_bottleneck: R4 (is_knowledge_bottleneck=True)
- thinking_bottleneck: R5 (is_knowledge_bottleneck=False, gap_type=method_translation)

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI would likely attempt direct algebraic manipulation of AM=GM condition or verify small cases (n=2,3) without finding a generalizable pattern. Would miss the critical step of dividing by gcd to reach coprime integers, and would not think to use prime divisibility arguments on what appears to be an algebra/analysis problem. The translation from continuous AM-GM conditions to discrete number theory is the key gap.
- suitable_for_poc: ["method_translation_detection", "knowledge_bottleneck_detection", "scaling_invariance_insight", "strategic_pair_selection", "extremal_prime_argument"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**已写入** `subagents-dirs/compfiles_imo2020p5/profile.json`

**字段清单逐项检查**：
- [x] _key（=compfiles_imo2020p5）
- [x] source_id（IMO 2020 Problem 5）
- [x] source_dataset（compfiles）
- [x] schema_version（=3）
- [x] problem_text
- [x] solution_text
- [x] solution_summary
- [x] domain（number_theory）
- [x] subfield（combinatorial_number_theory）
- [x] answer_type（proof）
- [x] answer（"For all n > 1, the property forces all numbers on the cards to be equal"）
- [x] problem_type（characterization）
- [x] solution_method_type
- [x] structure_features
- [x] key_objects
- [x] thinking_patterns
- [x] primary_pattern
- [x] knowledge_required
- [x] key_insight
- [x] translation_from
- [x] translation_to
- [x] translation_type
- [x] tell_topology（profile级）
- [x] tell_small_concepts（profile级）
- [x] expected_ai_method
- [x] correct_method
- [x] tell_hint_pairs（7对，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（3对，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象，stats中knowledge_bottleneck="R4", thinking_bottleneck="R5"）
- [x] analysis_metadata

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
2. 更新`problem_extraction_progress`集合中`_key="329256"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2020p5"
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
    '_key': '329256',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2020p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2020p5')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证详情: 7 local pairs, 3 global pairs, knowledge_bottleneck=R4, thinking_bottleneck=R5, answer非None, 所有全局pair的why_not_visible_locally非None

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_imo2020p5
- solution_method_type: gcd_scaling_with_extremal_prime_divisibility_contradiction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3（1个path_feature型，2个implicit型）
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无——characterization/direct_manipulation/method_translation均可归入已有类别，粒度一致
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
