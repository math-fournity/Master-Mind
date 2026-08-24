# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003872
- **文件路径**: subagents-dirs/omni_math_003872/problem.lean
- **来源**: AoPS omni_math (imo_shortlist)
- **ArangoDB progress记录_key**: 333751（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003872/problem.lean`

**产出**：
- 题目原文（数学描述）：A和B在黑板上玩游戏，初始2020个1。每轮A擦去两个数x,y，B写入x+y或|x-y|之一。游戏终止条件：(1)某个数>其余所有数之和；(2)全为0。B给A的cookies数=黑板上数字个数。A最大化cookies，B最小化。求最优博弈下A获得的cookies数。
- 解答核心思路（1-2句话）：答案等于2020的二进制数字和S₂(2020)=7。A的策略是总选两个相等的数（保证剩余数都是0或2的幂，至少S₂(n)个）；B的策略是维护"平衡符号集合数不被2^(s+1)整除"的不变量（利用Legendre公式和递推N=N₊+N₋），保证终止时至多s个数。
- 解答关键步骤列表：
  1. 定义S₂(n)为n的二进制数字和，2020=11111100100₂，S₂(2020)=7
  2. A的策略：总选两个相等的非零数，归纳证明所有数为0或2的幂；无法继续时非零数为不同的2的幂，最大者>其余之和
  3. 定义"range"：非零数k的range=k，零的range=2的幂；range之和=n；由S₂(a+b)≤S₂(a)+S₂(b)，n不能表示为少于S₂(n)个2的幂之和，故A保证≥S₂(n)个
  4. B的策略：定义"平衡集合"（符号选择使加权和=0），"好局面"=平衡集合数不被2^(s+1)整除
  5. Lemma 1：初始局面好（ν₂(C(n,n/2))=S₂(n)=s，由Legendre公式）
  6. Lemma 2：B可维护好局面（N=N₊+N₋，2^(s+1)∤N则至少一个不被整除）
  7. Lemma 3：好局面终止时≤s个数（一个数>其余之和时N=0不good；全零时N=2^k，k≤s）

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
| 1 | 纯元认知观察 | 0.8 | 描述这个博弈的结构：谁控制什么，每轮如何变化，终止条件是什么？ | A选两个数，B选x+y或|x-y|；每轮数字个数减1；终止条件(1)某数>其余之和(2)全零；A最大化剩余个数，B最小化 |
| 2 | 自由列举 | 0.7 | 列出所有可能有助于分析这个博弈的不变量或数量 | 数字之和、奇偶性、数字个数、最大数、数之间的关系、二进制表示、三角不等式（一个>其余之和）、符号和等 |
| 3 | 小尝试 | 0.4 | 假设B总是写x+y，分析会发生什么 | 和保持2020不变，B需要创造>1010的数，A可以尝试阻止，但这忽略了|x-y|选项，分析不完整 |
| 4 | 思维操作引导 | 0.3 | 考虑A总选两个相等的数的策略，能推出什么结构？ | 归纳证明所有数为0或2的幂；无法继续时非零数为不同的2的幂，最大者>其余之和，游戏终止 |
| 5 | 思维操作引导 | 0.2 | 定义每个数的"range"（它由多少个原始1得到），证明range的性质并联系2020的二进制表示 | 非零数k的range=k，零的range=2的幂；range之和=2020；由S₂(a+b)≤S₂(a)+S₂(b)，2020不能表示为少于S₂(2020)=7个2的幂之和，故A保证≥7 |
| 6 | 思维操作引导 | 0.3 | 对B的策略，考虑"平衡符号集合"的数量如何随B的选择变化？ | N=N₊+N₋，其中N₊是同号平衡集合数，N₋是异号平衡集合数；写x+y得N₊，写|x-y|得N₋；这是关键递推 |
| 7 | 能量传递引导 | 0.2 | 利用Legendre公式计算初始平衡集合数的2-adic valuation，完成B的策略并得出结论 | ν₂(C(2020,1010))=S₂(2020)=7；B维护"好局面"(2^8∤N)；终止时若一个数>其余之和则N=0不good，若全零则N=2^k且k≤7；故B保证≤7，结合A的≥7，答案为7 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 3
- knowledge_rounds（思维操作引导的轮数）: 3
- level_sum: 2.9
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: discrete_combinatorial
- structure_features: 两人博弈，A控制配对选择，B控制运算选择（加法/绝对差），两个终止条件，目标为最终数字个数
- key_objects: ["黑板上的数字", "博弈轮次", "终止条件", "cookies数", "二进制表示", "平衡符号集合", "2-adic valuation"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["invariant_analysis", "strategy_pairing", "binary_representation", "2_adic_valuation", "induction_on_game_rounds", "potential_function"]
- primary_pattern: binary_representation
- knowledge_required: ["二进制表示/popcount", "Legendre公式/2-adic valuation", "平衡符号集合/符号和", "博弈论策略配对"]
- key_insight: 答案等于2020的二进制数字和S₂(2020)=7，将博弈动力学转化为数论不变量（二进制表示和2-adic valuation）

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 博弈策略分析（配对选择和运算选择）
- translation_to: 数论不变量（二进制数字和与平衡集合的2-adic valuation）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "case_by_case", gap_type: "structural_transformation"}
- tell_small_concepts: ["binary digit sum", "popcount", "balanced collections", "2-adic valuation", "equal number pairing", "range invariant", "powers of 2", "Legendre formula"]
- expected_ai_method: case_by_case — bare AI会尝试逐案分析博弈状态或枚举策略，但无法发现二进制表示和平衡集合的联系
- correct_method: structural_transformation — 解答将博弈动力学转化为数论不变量（二进制数字和与2-adic valuation）

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——discrete_combinatorial/case_by_case/structural_transformation能归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 不需要新的拓扑维度——三个维度足够区分这道题的tell

**拓扑进化建议**：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

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
- 局部tell_hint_pairs数量: __ 对
- 全局tell_hint_pairs数量: __ 对
- 全局pair中path_feature型: __ 个，implicit型: __ 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试模拟博弈或分析小案例，但会错过二进制表示与平衡集合的联系。缺乏2-adic valuation和Legendre公式的知识，无法构造B的最优策略。
- suitable_for_poc: ["tell_hint_injection", "knowledge_bottleneck_detection", "strategy_translation"]
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
2. 更新`problem_extraction_progress`集合中`_key="333751"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_003872"
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
    '_key': '333751',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_003872',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_003872')
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
