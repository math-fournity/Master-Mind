# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa1999p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa1999P5.lean
- **来源**: USA 1999 P5
- **ArangoDB progress记录_key**: 329396（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa1999P5.lean`（共1087行，分3段读完）

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：The Y2K Game is played on a 1×2000 grid. Two players in turn write either S or O in an empty square. The first player who produces three consecutive boxes that spell SOS wins. If all boxes are filled without producing SOS then the game is a draw. Show that the second player has a winning strategy.
- 解答核心思路（1-2句话）：第二玩家通过两阶段策略获胜：开局构造"陷阱"（S _ _ S模式），然后用奇偶论证（losing squares成对出现→安全走法总存在）维持不变量并归纳证明。
- 解答关键步骤列表：
  1. 定义棋盘、SOS、威胁、陷阱（S _ _ S）等基本概念
  2. 证明陷阱中间两格是losing squares（trap_middle引理）
  3. 证明threat-free棋盘上losing squares恰为陷阱中间格（losing_char引理）
  4. 证明不同陷阱的中间格不相交（trap_disjoint引理）
  5. 推出losing squares成对出现，数量为偶数（even_card_losing引理）
  6. 奇偶论证：odd空格+even losing → 存在safe move（exists_safe_move引理）
  7. 第二玩家策略：先远距离放S，再完成陷阱，再用safe move维持不变量
  8. 主归纳：不变量（threat-free + trap + 正确奇偶）维持到游戏结束
  9. 开局阶段证明：远距离S保证第二步能完成陷阱（exists_second_setup引理）

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造7轮Q&A对话

**产出**（每轮详见profile.json的qa_sequence.rounds）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.2 | 描述Y2K游戏规则、获胜条件、第二玩家必胜策略的含义 | 棋盘1×2000，轮流放S/O，先组成SOS者胜，第二玩家必胜=无论第一玩家如何走都能强制获胜 |
| 2 | 自由列举 | 0.3 | 列出第二玩家所有可能的策略方向 | 镜像、配对、陷阱构造、奇偶论证、不变量法 |
| 3 | 小尝试 | 0.4 | 试镜像/配对策略，SOS不对称会怎样 | 镜像失败因为SOS不对称，配对也失败，需要结构性方法 |
| 4 | 思维操作引导 | 0.6 | 什么棋盘模式能创造losing squares？ | S _ _ S模式，中间两格无论放O还是S对手都能完成SOS |
| 5 | 推进 | 0.5 | 展开陷阱概念，证明中间两格是losing | 对a+1放O→对手放S于a+2完成SOS；放S→对手放O于a+2完成SOS。a+2同理 |
| 6 | 思维操作引导 | 0.7 | 用奇偶论证：losing squares成对→even，odd空格→safe move存在 | 每个陷阱贡献2个losing squares，陷阱不相交→总数even；第二玩家回合空格odd→存在非losing空格→safe move |
| 7 | 能量传递引导 | 0.8 | 组装完整策略并归纳验证不变量 | 两阶段：开局远距离S+完成陷阱；维持：奇偶论证保证safe move，归纳维持不变量(threat-free+trap+正确奇偶) |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.5
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence（证明第二玩家存在必胜策略=存在性构造）
- structure_features: 1×2000棋盘上的两人组合博弈；SOS模式匹配获胜条件；非对称获胜模式；第二玩家优势证明；两阶段策略（陷阱构造+奇偶维持）
- key_objects: 1x2000_grid, SOS_pattern, trap_pattern_S_blank_blank_S, losing_squares, parity_of_empty_squares, safe_move, game_invariant

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: [structural_invariant, parity_argument, strategic_construction, two_phase_strategy, induction]
- primary_pattern: structural_invariant（维持不变量是主导思维模式）
- knowledge_required: [combinatorial_game_theory_basics, parity_arguments, strategy_stealing, invariant_method, induction]
- key_insight: S _ _ S陷阱模式创造成对的losing squares，losing squares的偶数性保证了第二玩家回合（奇数空格）时safe move总存在

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: game_tree_enumeration（暴力枚举博弈树）
- translation_to: structural_invariant_with_parity（结构不变量+奇偶论证）
- translation_type: structural_transformation（从暴力枚举翻译为结构性论证）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: enumeration_brute_force, gap_type: structural_transformation}
- tell_small_concepts: [trap_pattern, losing_squares, parity_argument, safe_move, invariant, two_phase_strategy]
- expected_ai_method: bare AI会尝试枚举博弈状态或镜像/配对策略，不会发现陷阱结构和奇偶论证
- correct_method: 开局构造陷阱(S _ _ S)，然后用奇偶论证(losing squares偶数→safe move存在)维持不变量并归纳

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——structural_existence/enumeration_brute_force/structural_transformation均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 不需要新拓扑维度——三个维度足够区分这道题的tell
- 拓扑进化建议：无。已有拓扑分类体系完全覆盖本题。

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
- 局部tell_hint_pairs数量: 7 对（每轮一个，含per-pair拓扑和小概念）
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 1 个，implicit型: 2 个
  - path_feature: 两阶段策略的路径特征（陷阱构造+奇偶维持的循环依赖）
  - implicit 1: 奇偶关系（losing squares偶数性→safe move存在）蕴含在陷阱结构中
  - implicit 2: 开局远距离S的战略目的（为第二步完成陷阱做准备）
- 所有pair均包含tell_topology和tell_small_concepts字段
- 所有global pair的why_not_visible_locally已填写（非None）

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试镜像策略（因SOS不对称而失败），或尝试枚举博弈状态（2000格不可行），或简单配对而不识别陷阱结构。不会自发发现S _ _ S陷阱模式和连接losing squares到safe move存在的奇偶论证。
- suitable_for_poc: ["tell_extraction", "hint_injection", "topology_classification", "path_feature_detection"]
- discriminates_levels: true（R4知识瓶颈和R6思维瓶颈清晰区分不同能力水平）

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON，已写入 `subagents-dirs/compfiles_usa1999p5/profile.json`

**⚠️ 完整字段清单（逐项检查，不能遗漏）**：
- [x] _key（=compfiles_usa1999p5）
- [x] source_id
- [x] source_dataset
- [x] schema_version（=3）
- [x] problem_text
- [x] solution_text
- [x] solution_summary
- [x] domain
- [x] subfield
- [x] answer_type
- [x] answer（="The second player has a winning strategy"，proof类型填要证明的结论）
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
- [x] tell_hint_pairs（7个pair，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（3个pair，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象，stats中knowledge_bottleneck="R4", thinking_bottleneck="R6"为字符串类型）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**将完整JSON写入工作目录的 `profile.json` 文件** ✅

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
2. 更新`problem_extraction_progress`集合中`_key="329396"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa1999p5"
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
    '_key': '329396',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa1999p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa1999p5')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
  - 7 local pairs, 3 global pairs
  - answer非None: "The second player has a winning strategy"
  - knowledge_bottleneck="R4" (str), thinking_bottleneck="R6" (str)
  - 所有global pair的why_not_visible_locally非None
  - 所有pair含tell_topology和tell_small_concepts

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_usa1999p5
- solution_method_type: structural_invariant
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3（1个path_feature型 + 2个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类体系完全覆盖本题（structural_existence / enumeration_brute_force / structural_transformation）
- 是否遇到异常: 否，入库和验证均一次通过

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
