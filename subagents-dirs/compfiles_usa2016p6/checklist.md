# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2016p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2016P6.lean
- **来源**: USA 2016 P6
- **ArangoDB progress记录_key**: 329468（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2016P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：给定整数 n 和 k，n ≥ k ≥ 2。巫师有 2n 张卡片，每对标签 i=1..n 有两张。卡片面朝下排成一行。每轮玩家指定 k 张卡片，巫师翻开。若有两张匹配则玩家赢。否则巫师任意置换这 k 张卡片再翻回去。问：对哪些 (n,k) 游戏可赢（存在有限步内必胜策略）？
- 解答核心思路（1-2句话）：游戏可赢当且仅当 k < n。k<n 时用滑动窗口策略+鸽巢原理；k=n 时巫师维持排列在下一次查询集上单射的不变量来永远逃避。
- 解答关键步骤列表：
  1. **k < n 可赢（滑动窗口策略）**：查询位置 {j,...,j+k-1}，j=0..2n-k，共 2n-k+1 次查询
  2. 若任一查询有匹配则直接赢；否则每个窗口的 k 张牌都互不相同
  3. 相邻窗口重叠 k-1 个位置，通过标签集合差可推断位置 j 的标签
  4. 共推断 2n-k 个位置的标签；因 k<n 故 2n-k>n，但只有 n 种标签，鸽巢原理得两个位置标签相同
  5. 查询包含这两个位置的 k 张牌即赢，总计至多 2n-k+2 步
  6. **k = n 不可赢（巫师逃避策略）**：巫师初始排列使查询集和补集各自双射到所有标签
  7. 维持不变量：当前排列在上次查询集和下次查询集上都单射
  8. 关键引理：给定排列在 S 和 Q（均大小 n）上单射，对任意下次查询 Qn（大小 n），存在置换 τ 固定 Q 外所有点使 a∘τ 在 Qn 上单射
  9. 因 a 在 Q 和 Q^c 上都双射到所有 n 个标签，巫师可在 Q 内重排以避免 Qn 中的碰撞

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
| 1 | 纯元认知观察 | 0.8 | 描述这个游戏的结构：关键参数是什么，玩家随时间累积什么信息，巫师有什么权力？ | 游戏有2n张配对卡片面朝下排列。玩家每轮查询k张，巫师翻开。若两张匹配则赢。否则巫师置换这k张再翻回。关键参数n≥k≥2。玩家累积观测（哪些标签出现在哪些位置），但巫师每轮可重排被查的牌。游戏可赢=存在有限步必胜策略。 |
| 2 | 自由列举 | 0.7 | 列出所有可能的方法来确定可赢性。应该考虑哪些情况，每种情况可能用什么技巧？ | 考虑分k<n和k=n两种情况。k<n需要构造性必胜策略——可能利用多次查询的信息推断牌的位置。k=n可能需要证明巫师总能逃避。可能技巧：信息论、鸽巢原理、滑动窗口查询、基于不变量的对抗策略。 |
| 3 | 小尝试 | 0.5 | 试k=n的情况。当k=n时每次查询恰好n张牌。若n张都不同则覆盖所有n个标签。巫师能否总通过置换使下次查询也全不同？ | k=n时若查询n张牌无匹配则所有n个标签各出现一次。巫师可能可以置换被查的牌使下次查询也全不同。这需要排列在下一次查询集上保持单射。关键洞察：查询集和补集都双射到所有n个标签，给巫师足够的重排自由度。 |
| 4 | 思维操作引导 | 0.4 | 对k<n，想想重叠查询给你什么信息。若查询位置{i,...,i+k-1}再查{i+1,...,i+k}，比较揭示的标签能推断什么？ | 两个连续窗口重叠k-1个位置。若无匹配则每个窗口的k张牌都不同。窗口j的标签集减窗口j+1的标签集恰好给出一个标签——位置j的标签（它离开了窗口）。这就是滑动窗口技巧：通过比较连续重叠观测推断单个标签。 |
| 5 | 推进 | 0.5 | 完整展开滑动窗口策略。能推断多少个位置的标签？k<n时鸽巢原理如何应用？ | 从j=0滑到j=2n-k共2n-k+1次查询。从相邻对推断位置0到2n-k-1的标签，共2n-k个位置。因k<n故2n-k>n，但只有n种标签。鸽巢原理得两个位置标签相同。查询包含这两个位置的k张牌即赢。总计至多2n-k+2步。 |
| 6 | 思维操作引导 | 0.4 | 形式化巫师对k=n的逃避策略。巫师维持什么不变量？为什么合适的置换总存在？ | 巫师维持：当前排列在上次查询集和下次查询集上都单射。关键引理：给定排列a在S和Q（均大小n）上单射，对任意下次查询Qn（大小n），存在置换τ固定Q外所有点使a∘τ在Qn上单射。因a在Q和Q^c上都双射到所有n个标签，巫师可在Q内重排以对Qn实现任意目标标记。 |
| 7 | 能量传递引导 | 0.6 | 结合两个方向，给出完整答案和步数界。 | 游戏可赢当且仅当k<n。k<n：滑动窗口策略至多2n-k+2步获胜。k=n：逃避巫师维持每次查询上的单射性，阻止玩家获胜。答案：k<n。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.9
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
- problem_type: characterization
- structure_features: 两人对抗博弈含隐藏信息；玩家查询k张2n张牌中的牌，巫师揭示并置换；获胜条件是找到匹配对；需要构造性策略(k<n)和不可能性证明(k=n)两个方向
- key_objects: ["card arrangement", "player strategy", "wizard permutation", "sliding window of k positions", "injective function on query set", "pigeonhole principle"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["case_analysis", "sliding_window", "pigeonhole_principle", "invariant_maintenance", "adversarial_strategy"]
- primary_pattern: case_analysis
- knowledge_required: ["combinatorial game theory", "pigeonhole principle", "permutation groups", "injective functions", "set difference computation"]
- key_insight: 当k<n时滑动k个位置的窗口能推断2n-k>n个位置的标签，鸽巢原理迫使出现匹配对；当k=n时查询集和补集都双射到所有标签，巫师总能置换使下次查询保持单射。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 博弈论表述（卡片、巫师、查询、翻面）
- translation_to: 组合表述（有限集上的单射函数、鸽巢原理、置换群）
- translation_type: structural_transformation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: case_by_case, gap_type: structural_transformation}
- tell_small_concepts: ["sliding window", "pigeonhole principle", "injective on query set", "overlapping windows", "evasive wizard", "permutation invariant", "two-case split"]
- expected_ai_method: enumeration_brute_force（裸AI可能尝试暴力枚举所有查询模式）
- correct_method: case_by_case——k<n用滑动窗口+鸽巢，k=n用基于不变量的对抗策略

**已有ai_method_type值**（优先使用）：
- `enumeration_brute_force` ✅ 抽象
- `continuous_analytic` ✅ 抽象
- `direct_calculation` ✅ 抽象
- `logical_deduction` ✅ 抽象
- `case_by_case` ✅ 抽象
- `algebraic_identity` ✅ 中等
- `equation_solving` ✅ 抽象
- `direct_manipulation` ✅ 抽象
- **❌ 不要用太长太具体的值**

**已有gap_type值**（优先使用）：
- `method_problem_mismatch` ✅ 抽象
- `knowledge_gap` ✅ 抽象
- `structural_transformation` ✅ 中等
- `search_space_estimation` ✅ 中等
- `method_translation` ✅ 中等
- `global_sorting` ⚠️ 偏具体
- **❌ 不要用太具体的值**

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ 是。characterization已有，case_by_case已有，structural_transformation已有。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ 是。所有值都是抽象粒度。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ 足够。三个维度能区分这道题的特征性tell（两方向证明+滑动窗口+鸽巢+置换不变量）。
- [x] 如果发现拓扑分类需要进化，在此写出建议： 无需进化。当前拓扑分类体系完全够用。

**拓扑进化建议**（如有）：无。

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

**局部pair摘要**：
| Round | tell | hint | hint_level | situation_type | knowledge_bottleneck | topology |
|---|---|---|---|---|---|---|
| 1 | AI看到博弈题但没识别两情况结构和隐藏信息动态 | 描述游戏结构和关键参数 | 0.8 | 纯元认知观察 | false | (characterization, direct_calculation, method_problem_mismatch) |
| 2 | AI列出策略但没识别滑动窗口、鸽巢、k=n不可能方向 | 列举所有方法，考虑k<n和k=n分情况 | 0.7 | 自由列举 | false | (characterization, enumeration_brute_force, search_space_estimation) |
| 3 | AI试k=n但没看到巫师能维持单射不变量 | 试k=n：巫师能否总置换使下次查询全不同？ | 0.5 | 小尝试 | true | (characterization, case_by_case, knowledge_gap) |
| 4 | AI没看到重叠窗口通过集合差揭示单个标签 | 想想重叠查询给什么信息，集合差能推断什么 | 0.4 | 思维操作引导 | false | (characterization, direct_manipulation, structural_transformation) |
| 5 | AI有滑动窗口但没连接2n-k计数到鸽巢 | 完整展开滑动窗口，能推断多少位置？鸽巢如何应用？ | 0.5 | 推进 | false | (characterization, direct_calculation, method_problem_mismatch) |
| 6 | AI没形式化巫师不变量或置换扩展引理 | 形式化巫师逃避策略，什么不变量？置换为何总存在？ | 0.4 | 思维操作引导 | true | (characterization, logical_deduction, knowledge_gap) |
| 7 | AI有两个方向但没合成完整刻画 | 结合两方向给出完整答案和步数界 | 0.6 | 能量传递引导 | false | (characterization, logical_deduction, method_translation) |

**全局pair摘要**：
1. (path_feature) 两情况分拆+构造与不可能性不同技术——完整路径特征
2. (implicit, Q4) 重叠窗口通过集合差揭示单个标签——蕴含信息
3. (implicit, Q5) 2n-k推断标签与n种标签的鸽巢应用——蕴含信息

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: 裸AI可能尝试找通用策略而不分情况，或在k=n不可能性方向卡住（不知道置换不变量技巧），也可能错过滑动窗口洞察而尝试暴力枚举查询模式
- suitable_for_poc: ["tell_extraction", "hint_injection", "two_case_split_detection", "structural_transformation_detection"]
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
- [x] answer（**⚠️ 必填，不能为None**。proof类型填要证明的结论，如"sum >= ..."；existence_construction类型填构造的存在性结论；numerical类型填数值答案）
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
- [x] tell_hint_pairs（每个pair含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（每个pair含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**将完整JSON写入工作目录的 `profile.json` 文件** ✅ 已写入 subagents-dirs/compfiles_usa2016p6/profile.json

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
2. 更新`problem_extraction_progress`集合中`_key="329468"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa2016p6"
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
    '_key': '329468',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa2016p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa2016p6')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证详情: 7 local pairs, 3 global pairs, answer="The game is winnable if and only if k < n", knowledge_bottleneck="R6", thinking_bottleneck="R4"

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_usa2016p6
- solution_method_type: case_analysis
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3 (1 path_feature + 2 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否。已有拓扑分类（characterization/case_by_case/structural_transformation等）完全够用，粒度一致。
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
