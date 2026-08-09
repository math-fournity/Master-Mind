# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003955
- **文件路径**: subagents-dirs/omni_math_003955/problem.lean
- **来源**: omni_math
- **ArangoDB progress记录_key**: 333834（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003955/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：2022×2022棋盘上，园丁和伐木工交替行动。园丁选一个格子，该格子及周围8格的树高度+1（3×3块，最多9棵树）。伐木工选4个不同格子，正高度的树-1。雄伟树=高度≥10^6。求园丁能保证的最大雄伟树数量K。
- 解答核心思路（1-2句话）：速率论证——园丁每轮加9单位，伐木工每轮减4单位，净速率5/轮。均匀循环使每棵内部树增长率9/N，伐木工最多压制4N/9棵树，园丁保证5N/9=2271380棵雄伟树。
- 解答关键步骤列表：
  1. 识别每轮加法/减法速率：园丁+9，伐木工-4
  2. 园丁均匀循环所有N=2022²=4,088,484格，每棵内部树增长率9/N
  3. 伐木工集中k棵树时，每棵压制率4/k
  4. 增长>压制条件：9/N > 4/k，即k > 4N/9
  5. 伐木工最多压制⌊4N/9⌋棵，剩余⌈5N/9⌉=5×454,276=2,271,380
  6. 紧界论证：伐木工持续压制同一批4N/9棵树，每棵压制率=9/N恰好抵消增长

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.2 | 描述游戏结构：两个玩家的行动是什么？目标是什么？每个行动的关键数值参数是什么？ | 2022×2022棋盘(N=4,088,484)。园丁选格子使3×3块+1(最多9格)。伐木工选4格使正高度树-1。目标：最大化高度≥10^6的树数。关键数字：9 vs 4，阈值10^6。 |
| 2 | 自由列举 | 0.3 | 列出园丁所有可能的策略方法——包括具体策略和抽象方法（如速率分析、势函数、极小极大推理） | (1)均匀循环所有格子 (2)集中子集 (3)速率分析——比较每轮加减 (4)势函数——跟踪总高度 (5)自适应策略 (6)小棋盘模拟找规律 (7)极小极大——最坏情况分析 |
| 3 | 小尝试 | 0.4 | 尝试模拟小棋盘(如3×3或5×5)看能否发现模式。园丁均匀循环时会发生什么？能识别关键比率吗？ | 3×3棋盘上园丁每次影响全部9格，伐木工只能减4，净增+5/轮，所有树都增长。关键观察：每轮9:4的加减比率。 |
| 4 | 思维操作引导 | 0.6 | 不要模拟了，思考速率：园丁每轮加多少单位？伐木工减多少？净速率是多少？能连接到可保证的树的比例吗？ | 园丁每轮加9单位(3×3块)。伐木工每轮减4单位(4格)。净速率+5/轮。均匀循环时每棵内部树增长率9/N。伐木工可将4个减量分配给目标树。关键问题：伐木工能使多少棵树k的压制率超过增长率？ |
| 5 | 推进 | 0.7 | 园丁均匀循环所有N格时，每棵树增长率是多少？伐木工集中k棵树时，每棵压制率是多少？增长何时超过压制？ | 每棵树增长率：9/N每轮。伐木工集中k棵树时压制率：4/k每轮。增长>压制当9/N > 4/k，即k > 4N/9。伐木工最多压制⌊4N/9⌋棵树。 |
| 6 | 推进 | 0.7 | 解不等式9/N > 4/k求k。伐木工能压制多少棵树？剩余多少保证增长？计算5N/9，N=2022²=4,088,484。 | k > 4N/9。伐木工最多压制⌊4N/9⌋棵。剩余⌈5N/9⌉。N/9=454,276，5N/9=5×454,276=2,271,380。K=2,271,380。 |
| 7 | 能量传递引导 | 0.5 | 确认：伐木工确实能通过持续压制同一批4N/9棵树来达到压制上界，所以5N/9=2271380既可达到又是最优的。你找到了答案！ | 是的——伐木工每轮压制同一批4N/9=1,817,104棵树，每棵压制率4/(4N/9)=9/N恰好抵消园丁增长率。这证明界是紧的。K=2271380。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5
- knowledge_rounds（思维操作引导的轮数）: 1
- level_sum: 3.4
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R4
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R3

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: discrete_combinatorial（使用已有值，抽象粒度）
- structure_features: 两人交替博弈在2022×2022网格上；非对称行动（园丁3×3块+1影响最多9格，伐木工4格-1）；阈值条件（高度≥10^6）；对伐木工策略的最坏情况保证；关键结构比率9:4
- key_objects: 2022×2022网格(N=4,088,484格)、树高(初始0)、园丁行动(3×3块+1最多9格)、伐木工行动(4格-1仅正高度)、雄伟阈值(10^6)、9:4加减比率

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["rate_analysis", "potential_function", "worst_case_bound", "uniform_strategy", "adversarial_argument"]
- primary_pattern: rate_analysis（速率分析）
- knowledge_required: ["combinatorial game theory", "potential function method", "rate arguments in combinatorics", "minimax reasoning"]
- key_insight: 园丁每轮加9单位vs伐木工每轮减4单位的9:4比率意味着伐木工最多压制4/9的树，园丁保证5/9的树成为雄伟树

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: enumeration_brute_force（暴力枚举/模拟）
- translation_to: rate_analysis_potential（速率分析/势函数）
- translation_type: method_translation（方法翻译——从具体模拟翻译到抽象速率论证）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "method_translation"}
- tell_small_concepts: ["rate_ratio", "uniform_cycling", "net_growth", "suppression_capacity", "5/9_fraction", "9:4_ratio", "adversarial_tightness"]
- expected_ai_method: enumeration_brute_force — AI会尝试模拟游戏或枚举具体走法序列，在大棋盘复杂性中迷失，错过速率抽象
- correct_method: rate_analysis — 计算每轮9:4加减比率，推导均匀循环下的每棵树增长率，通过最坏情况伐木工分析得到5/9保证比例

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=discrete_combinatorial、ai_method_type=enumeration_brute_force、gap_type=method_translation均可归入已有拓扑类别
- [x] 粒度一致——所有标注值与已有值粒度统一
- [x] 不需要新拓扑维度——三个维度足够区分这道题的tell
- 无拓扑进化建议

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 1 个，implicit型: 2 个

详细数据见 profile.json 中的 tell_hint_pairs 和 global_tell_hint_pairs 字段。
每个局部pair包含独立的tell_topology和tell_small_concepts。
每个全局pair包含tell_topology、tell_small_concepts和why_not_visible_locally。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI会尝试在2022×2022大棋盘上模拟游戏或枚举具体走法序列，在巨大棋盘和高阈值的复杂性中迷失。会错过每轮速率(9加vs 4减)的关键抽象，无法将此比率连接到可保证的树的比例。大棋盘(4百万格)和阈值(10^6)会进一步误导它走向计算而非分析方法。可能也无法证明最优性(伐木工确实能压制4N/9棵树)，只给出下界而缺少匹配的上界。
- suitable_for_poc: ["hint_injection", "tell_identification", "method_translation"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON

**⚠️ 完整字段清单（逐项检查，不能遗漏）**：
- [x] _key（=problem_id）
- [x] source_id
- [x] source_dataset
- [x] schema_version（=3）
- [x] problem_text
- [x] solution_text
- [x] solution_summary
- [x] domain
- [x] subfield
- [x] answer_type
- [x] answer（"2271380"）
- [x] problem_type
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
- [x] tell_hint_pairs（7个，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（3个，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**完整JSON已写入工作目录的 `profile.json` 文件**

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
2. 更新`problem_extraction_progress`集合中`_key="333834"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_003955"
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
    '_key': '333834',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_003955',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_003955')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

验证输出：验证通过: omni_math_003955, 7 local pairs, 3 global pairs, answer: 2271380

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: omni_math_003955
- solution_method_type: rate_analysis
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，已有拓扑分类完全够用
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
