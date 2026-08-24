# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2004p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2004P6.lean
- **来源**: IMO 2004 P6
- **ArangoDB progress记录_key**: 329192（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2004P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：称一个正整数为"交替的"（alternating），如果其十进制表示中每两个相邻数字的奇偶性不同。求所有正整数n，使得n有一个交替的倍数。
- 解答核心思路（1-2句话）：n有交替倍数当且仅当20∤n。必要性：20|n的倍数末两位都是偶数，不交替。充分性：将n分解为2^a·5^b·u（gcd(u,10)=1），构造奇偶性受控的"Nice"数字块分别处理2-部分和5-部分，再用Euler定理处理与10互素的部分u。
- 解答关键步骤列表：
  1. 必要性：20|n → 任何倍数末位为0且倒数第二位也为偶数 → 不交替
  2. 定义Nice数字块：位置i的数字奇偶性为i mod 2，保证交替性
  3. Nice块可拼接（偶数长度时）和可追加
  4. dvd_geom_sum：gcd(x,u)=1且x≥2时，u整除某个几何级数和1+x+...+x^{t-1}（Euler定理）
  5. nice_flatten_replicate：重复Nice块t次得到的数 = 块值 × 几何级数和(10^L, t)
  6. exists_alternating_multiple：组合上述引理，若Nice块整除n的一部分且u与10互素，则n·u有交替倍数
  7. two_block：归纳构造长度2k+2的Nice块，被2^{2k+3}整除（处理2-部分）
  8. five_block：归纳构造长度b+1的Nice块，被10·5^b整除（处理5-部分，用数字选择模5）
  9. exists_alternating_multiple'：分5|n和5∤n两种情况，组合two_block/five_block + Euler定理
  10. 主定理：SolutionSet = {n | 0<n ∧ ¬20|n}

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
| 1 | 纯元认知观察 | 0.8 | 这个问题的结构是什么？我们需要找到什么，"交替"的定义对数字施加了什么约束？ | 这是一个刻画问题——找到所有正整数n使得n有一个交替倍数。交替意味着十进制中相邻数字奇偶性不同。需要双向证明：哪些n不行（必要性），哪些n行（充分性）。 |
| 2 | 自由列举 | 0.7 | 这个问题有哪些可能的攻击方向？尽可能多地列出。 | 检查小例子找规律；检查哪些n明显失败（如20的倍数）；尝试为特定n构造交替倍数；用模运算分析；考虑十进制数字结构；思考奇偶交替对整除性的约束；用Euler定理处理与10互素的部分。 |
| 3 | 小尝试 | 0.5 | 试着检查：哪些小的n明显不能有交替倍数？20的倍数的末尾数字长什么样？ | 如果20|n，n的任何倍数也是20的倍数，末位为0。20的倍数末两位是00,20,40,60,80——都是偶数！所以末两位奇偶性相同，不交替。因此20|n是不能有交替倍数的充分条件。 |
| 4 | 思维操作引导 | 0.4 | 现在处理困难方向：若20∤n，证明n有交替倍数。考虑将n分解为2-部分、5-部分和其余部分，如何分别处理？ | 写n=2^a·5^b·u，其中gcd(u,10)=1。需要找到交替数被2^a·5^b·u整除。可以用数字块构造处理2^a和5^b，用Euler定理处理u（因为gcd(u,10)=1）。 |
| 5 | 思维操作引导 | 0.3 | 关键思想：构造"Nice"数字块——位置i的数字奇偶性为i mod 2。如果重复这个块t次，得到什么数？如何用Euler定理使它被u整除？ | 若块值为V、长度为L，重复t次得到V·(1+10^L+10^{2L}+...+10^{(t-1)L})。因gcd(10^L,u)=1，由Euler定理，几何级数和1+10^L+...+10^{(t-1)L}对某个t被u整除。若V被2^a·5^b整除，则重复后的数被n整除。 |
| 6 | 推进 | 0.5 | 现在需要构造被2^a整除（当5∤n时）或被10·5^b整除（当5|n时）的Nice块。如何归纳地构造这样的块？ | 对2-部分：归纳构造偶数长度块，从[6,1]（被8整除）开始，每步追加[d,1]其中d选择使2-adic整除性增加。对5-部分：归纳构造，每步追加一个数字e，选择e使新数被额外的5因子整除，利用0-9中可选合适奇偶性的数字。 |
| 7 | 能量传递引导 | 0.7 | 把所有部分组合起来：结合必要性（20|n失败）和充分性（20∤n时构造交替倍数），给出完整的刻画。 | 答案：n有交替倍数当且仅当20∤n。必要性：20|n的倍数末两位皆偶数。充分性：分解n，为2-部分和5-部分构造Nice数字块，用Euler定理处理互素部分，重复块得到n的交替倍数。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.9
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
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
- structure_features: 刻画问题，需要双向证明（必要性+充分性）；十进制数字奇偶交替约束；整除性关系；分解为2-部分、5-部分和互素部分分别处理
- key_objects: 正整数n，交替数（alternating number），十进制数字，奇偶性（parity），整除性（divisibility），Nice数字块，几何级数和，Euler定理/φ函数

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["necessity_sufficiency_split", "digit_block_construction", "repetition_with_geometric_sum", "case_analysis_on_valuations", "inductive_construction"]
- primary_pattern: digit_block_construction_with_repetition
- knowledge_required: ["Euler's theorem (totient function)", "geometric sums", "modular arithmetic", "p-adic valuations", "decimal representation", "parity", "coprimality"]
- key_insight: 构造奇偶性受控的Nice数字块，重复t次使结果分解为"块值×几何级数和"，用Euler定理保证几何级数和被与10互素的部分u整除

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 存在性问题（找到n的交替倍数）
- translation_to: 构造性数字操作 + 数论（Euler定理/几何级数和）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: enumeration_brute_force, gap_type: method_translation}
- tell_small_concepts: ["alternating digits", "parity constraint", "digit block construction", "Euler's theorem", "geometric sum repetition", "20 divisibility obstruction"]
- expected_ai_method: bare AI预期会用暴力枚举或直接构造尝试找交替倍数，不会想到数字块+重复+Euler定理的组合
- correct_method: 构造Nice数字块处理2-部分和5-部分，用Euler定理处理互素部分，重复块得到交替倍数

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type=characterization、ai_method_type=enumeration_brute_force、gap_type=method_translation均能归入已有的拓扑类别
- [x] 粒度是否一致——标注值与已有值粒度统一
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化

**拓扑进化建议**（如有）：无，现有拓扑分类足够

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试暴力枚举交替数检查特定n，或直接构造而不想到数字块+重复+Euler定理的组合。可能找到20|n的必要性方向，但在充分性方向上失败——不会想到构造Nice数字块、重复块产生几何级数和、用Euler定理处理互素部分这条路径。
- suitable_for_poc: ["tell_extraction", "hint_injection", "topology_classification"]
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
2. 更新`problem_extraction_progress`集合中`_key="329192"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2004p6"
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
    '_key': '329192',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2004p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2004p6')
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
- problem_id: compfiles_imo2004p6
- solution_method_type: constructive_existence
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，现有拓扑分类（characterization / enumeration_brute_force / method_translation等）足够覆盖
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
