# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2010p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2010P5.lean
- **来源**: IMO 2010 P5
- **ArangoDB progress记录_key**: 329214（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2010P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：六个盒子B1-B6各含1枚硬币。两种操作：(1) 从非空B_j(1≤j≤5)取1枚，向B_{j+1}放2枚；(2) 从非空B_k(1≤k≤4)取1枚，交换B_{k+1}和B_{k+2}的内容。问是否存在有限操作序列使B1-B5为空且B6恰好有2010^{2010^{2010}}枚硬币？
- 解答核心思路（1-2句话）：发现move1(push)和move2(swap)组合产生指数放大——从(n,0,0)可达(0,2^n,0)。迭代构建幂塔2^2^2^2^2^11远超目标2010^{2010^{2010}}，再用move2缩减到精确值T/4，最后push到T。
- 解答关键步骤列表：
  1. 从初始(1,1,1,1,1,1)经push操作到达(0,0,5,11,0,0)
  2. 发现exp操作：(n,0,0) → (0, 2^n, 0)，通过move1+move2迭代实现
  3. 迭代exp构建幂塔：2^2^2^2^2^11 >> 2010^{2010^{2010}}
  4. 用move2缩减：所有硬币在box4时，swap空box5/6可逐次递减
  5. 缩减到T/4，再push两次得到T/2和T（利用T被4整除）

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.2 | 描述这道题的结构：有哪些操作？初始状态是什么？目标状态是什么？目标数字有什么特点？ | 有两种操作：move1是从B_j取1枚向B_{j+1}放2枚（线性增长），move2是从B_k取1枚并交换B_{k+1}和B_{k+2}（涉及swap）。初始6个盒子各1枚。目标是B1-B5空、B6恰好2010^{2010^{2010}}枚。目标数字极大，是三重幂。 |
| 2 | 自由列举 | 0.4 | 列出所有可能的研究方向：直接模拟、不变量分析、寻找特殊操作组合、分析操作的增长率…… | 方向包括：(a)直接模拟操作看能到达哪些状态；(b)寻找不变量判断可达性；(c)分析move1的增长率——每次取1放2是线性翻倍；(d)考虑move2的swap功能是否有特殊用途；(e)考虑两种操作的组合效应。 |
| 3 | 小尝试 | 0.3 | 如果只用move1，硬币增长有多快？从初始状态出发，最多能在B6积累多少硬币？ | 只用move1时，每次操作净增1枚硬币（取1放2）。从6枚开始，经过有限次操作最多在B6得到很少的硬币。move1只能线性增长，远不足以达到2010^{2010^{2010}}。单靠move1不可行。 |
| 4 | 思维操作引导 | 0.5 | 仔细分析move2：当B_{k+2}为空时，swap B_{k+1}和B_{k+2}意味着什么？这能否用来"重置"一个盒子？ | 当B_{k+2}为空时，swap会把B_{k+1}的内容移到B_{k+2}，同时B_{k+1}变空。这相当于把硬币"搬"到后面的盒子同时清空前一个。关键：move2可以用来重置B_{k+1}为空，同时保留其硬币到B_{k+2}。这与move1配合可能产生非线性效应。 |
| 5 | 思维操作引导 | 0.7 | 试试这个序列：从(n,0,0)出发，move1得(n-1,2,0)，push到(n-1,0,4)，move2得(n-2,4,0)，push到(n-2,0,8)，move2得(n-3,8,0)……你看到了什么模式？ | 模式是：每次循环将B_i减1，B_{i+1}翻倍。从(n,0,0)出发，经过n次循环后到达(0, 2^n, 0)。这是指数放大！move1的push加上move2的swap组合实现了n→2^n的变换。 |
| 6 | 推进 | 0.6 | 如果(n,0,0)→(0,2^n,0)是指数放大，那么迭代这个操作能构建什么？2^2^2^2^2^11和2010^{2010^{2010}}相比如何？ | 迭代exp操作构建幂塔：从(5,11,0,0)出发，(5,0,2^11,0)→(4,2^11,0,0)→(4,0,2^2^11,0)→...→(0,2^2^2^2^2^11,0,0)。幂塔2^2^2^2^2^11是天文数字，远超2010^{2010^{2010}}（因为2010<2^11，且幂塔高度5远超3）。所以我们能获得比目标多得多的硬币。 |
| 7 | 能量传递引导 | 0.3 | 现在你有远超目标的硬币全在box4。如何精确缩减到T=2010^{2010^{2010}}？提示：T被4整除，且move2可以swap空的box5/6来递减box4。 | 用move2反复swap空的box5和box6，每次从box4取1枚（box4减1，swap空盒不变），将box4从2^2^2^2^2^11递减到T/4。然后push box4到box5得T/2，再push box5到box6得T。因为T=2010^{2010^{2010}}被4整除（2010被4整除），所以T/4是整数，操作可行。答案：存在这样的序列。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.2+0.4+0.3+0.5+0.7+0.6+0.3 = 3.0
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence
- structure_features: 六盒子系统，两种操作（move1线性增长+move2含swap），目标是构造性存在性证明——需要到达一个极大的精确目标数2010^{2010^{2010}}
- key_objects: ["六个盒子B1-B6", "move1操作(取1放2)", "move2操作(取1+swap)", "指数放大模式(n,0,0)→(0,2^n,0)", "幂塔2^2^2^2^2^11", "目标数2010^{2010^{2010}}", "缩减机制(move2递减)"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["operation_combination", "exponential_amplification", "bound_comparison", "constructive_existence", "divisibility_exploitation"]
- primary_pattern: "exponential_amplification"（主导思维模式是发现两种操作的组合产生指数放大）
- knowledge_required: ["组合操作分析", "指数塔比较", "整除性分析", "构造性存在性证明方法"]
- key_insight: 将move1(push)和move2(swap)组合在三个相邻盒子(n,0,0)上可实现n→2^n的指数放大，迭代构建的幂塔远超目标，再用move2的递减机制精确到达目标

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: "sequential_operation_analysis"（逐步分析单个操作的效果）
- translation_to: "compound_operation_pattern"（发现操作组合的指数放大模式）
- translation_type: "method_translation"（从线性操作思维翻译到指数模式识别）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "enumeration_brute_force", gap_type: "method_translation"}
- tell_small_concepts: ["exponential amplification", "power tower", "operation composition", "swap+push pattern", "bound comparison", "divisibility exploitation"]
- expected_ai_method: "enumeration_brute_force"（bare AI会尝试枚举可达状态或只用move1线性增长，无法发现操作组合的指数放大）
- correct_method: "compound operation pattern discovery"（正确方法是发现move1+move2组合产生指数放大的模式，构建幂塔后缩减到精确目标）

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=structural_existence、ai_method_type=enumeration_brute_force、gap_type=method_translation均可归入已有拓扑类别
- [x] 粒度一致——标注值与已有值粒度统一
- [x] 三个维度足够区分这道题的tell和已有tell
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。已有拓扑分类可以充分描述此题。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到组合操作问题但未识别操作组合的结构特征 | 描述两种操作、初始状态、目标状态和目标数字特点 | 0.2 | 纯元认知观察 | false | {structural_existence, enumeration_brute_force, method_problem_mismatch} | ["operation description", "box configuration", "target number"] |
| 2 | AI列举方向但未考虑复合操作模式 | 列出所有方向：直接模拟、不变量、操作组合、增长率分析 | 0.4 | 自由列举 | false | {structural_existence, enumeration_brute_force, search_space_estimation} | ["approach enumeration", "invariant", "operation combination"] |
| 3 | AI只用move1尝试，看到线性增长，认为目标不可达 | 只用move1时硬币增长多快？能否达到2010^{2010^{2010}}？ | 0.3 | 小尝试 | false | {structural_existence, direct_calculation, method_problem_mismatch} | ["linear growth", "move1 only", "growth rate comparison"] |
| 4 | AI未考虑move2(swap)与move1组合的效果 | 当B_{k+2}为空时swap意味着什么？能否重置盒子？ | 0.5 | 思维操作引导 | true | {structural_existence, direct_manipulation, knowledge_gap} | ["swap operation", "box reset", "move2 mechanics", "empty box utilization"] |
| 5 | AI理解swap可重置盒子但未发现指数放大模式 | 试序列(n,0,0)→(n-1,2,0)→(n-1,0,4)→(n-2,4,0)→...看到什么模式？ | 0.7 | 思维操作引导 | true | {structural_existence, direct_manipulation, structural_transformation} | ["exponential amplification", "doubling pattern", "compound operation", "n to 2^n"] |
| 6 | AI发现指数模式但未连接到目标数的比较 | 迭代exp构建幂塔，2^2^2^2^2^11与2010^{2010^{2010}}相比如何？ | 0.6 | 推进 | false | {structural_existence, direct_calculation, search_space_estimation} | ["power tower iteration", "bound comparison", "tower inequality", "target exceeding"] |
| 7 | AI有足够硬币但需精确缩减到目标 | T被4整除，move2可swap空box5/6递减box4，如何精确到达T？ | 0.3 | 能量传递引导 | false | {structural_existence, direct_manipulation, method_translation} | ["reduction mechanism", "divisibility by 4", "decrement via swap", "exact target matching"] |

**全局pairs详情**：

1. path_feature型:
- scope: "完整解答路径从初始状态到精确目标"
- observation_point: null
- tell: 整个解答路径需要发现两个简单操作组合成指数放大模式，这在任何单步操作中都不可见
- hint: 寻找复合操作模式产生非线性增长，然后用得到的巨大数字缩减到精确目标
- hint_level: 0.7
- generalizability: "high - 发现复合操作放大的模式适用于许多组合操作问题"
- why_not_visible_locally: 从任何单步看只能看到线性增长或swap操作，指数放大只在push+swap的特定迭代组合中涌现，需要跨多步看到完整模式
- tell_topology: {structural_existence, enumeration_brute_force, method_translation}
- tell_small_concepts: ["compound operation", "exponential amplification", "power tower", "operation composition"]

2. implicit型:
- scope: "目标数的整除性与缩减机制的关系"
- observation_point: "R7"
- tell: 目标T=2010^{2010^{2010}}被4整除不是巧合——它是缩减步骤可行的必要条件
- hint: 检查目标数的整除性质。为什么T必须被4整除才能完成最后的push步骤？
- hint_level: 0.5
- generalizability: "medium - 整除性感知的缩减在带精确目标的构造性存在性问题中常见"
- why_not_visible_locally: 整除性要求只在到达缩减步骤时才显现——之前关注的是获得足够硬币，而非目标的精确算术性质
- tell_topology: {structural_existence, direct_calculation, knowledge_gap}
- tell_small_concepts: ["divisibility by 4", "target arithmetic", "reduction feasibility", "push decomposition"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试只用move1线性增长或枚举可达状态，得出目标数太大不可达的错误结论。关键错误是未能发现move1+move2组合产生指数放大的模式——这是跨操作的非线性涌现，需要从单操作分析翻译到复合操作模式识别。
- suitable_for_poc: ["POC-VMS-hint-injection", "POC-VMS-tell-detection", "POC-VMS-compound-pattern"]
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
- [x] answer（"Yes, such a finite sequence exists..."）
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
- [x] global_tell_hint_pairs（2个pair，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象，stats中knowledge_bottleneck="R4", thinking_bottleneck="R5"为字符串）
- [x] analysis_metadata

**已将完整JSON写入 `profile.json`**

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
2. 更新`problem_extraction_progress`集合中`_key="329214"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2010p5"
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
    '_key': '329214',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2010p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2010p5')
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
- problem_id: compfiles_imo2010p5
- solution_method_type: constructive_existence
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类（structural_existence / enumeration_brute_force / method_translation等）可充分描述此题
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
