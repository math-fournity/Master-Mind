# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000007
- **文件路径**: subagents-dirs/omni_math_000007/problem.lean
- **来源**: AoPS omni_math (china_national_olympiad)
- **ArangoDB progress记录_key**: 329878（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000007/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：乒乓球俱乐部举办双打比赛系列，约束：(i)每个选手最多属于两个对；(ii)任意两个不同的对最多比赛一次；(iii)同一对中的选手在各自与其他选手配对时不对抗。每个选手参赛的场数构成"比赛集合"。给定A={a1,...,ak}为正整数集合且每个元素被6整除，求使比赛集合等于A所需的最少选手数。
- 解答核心思路（1-2句话）：将问题建模为图论问题——顶点=选手，边=对，最大度2意味着图是路径和环的并集。分析条件(iii)对比赛兼容性的约束（图距离≥3才能比赛），利用A中元素被6整除的性质构造最优方案。
- 解答关键步骤列表：
  1. 建立图模型：顶点=选手，边=对，最大度2→路径和环的并集
  2. 分析条件(iii)：同一对的两个选手各自在其他对中时，这两个对不能比赛→图中距离<3的对不能比赛
  3. 计算每种图结构（路径/环）中选手的最大比赛数
  4. 利用A中元素被6整除的性质设计最优构造
  5. 得到最小选手数 = (1/2)max(A) + 3

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：有哪些约束条件？什么是"比赛集合"？我们要优化什么？ | 识别三个约束(i)(ii)(iii)，比赛集合是各选手参赛场数的不同值构成的集合，目标是求最小选手数使比赛集合等于A |
| 2 | 自由列举 | 0.7 | 列出所有可能的数学建模方法来处理这个组合优化问题 | 图论、组合设计、线性规划、直接枚举、超图模型等 |
| 3 | 小尝试 | 0.5 | 尝试用图论建模：顶点和边分别代表什么？"每个选手最多属于两个对"对图的度数意味着什么？ | 顶点=选手，边=对，最大度2→图是路径和环的并集 |
| 4 | 思维操作引导 | 0.4 | 给定图是路径和环的并集，分析条件(iii)如何约束哪些对之间可以比赛。考虑两个对在图中共享一个中间对的情况。 | 条件(iii)转化为：如果对ei=(vi,v(i+1))和对ej=(vj,v(j+1))之间有一个中间对ek使得ek的两个端点分别在ei和ej中，则ei和ej不能比赛。在路径/环中这意味着|i-j|≥3 |
| 5 | 推进 | 0.5 | 继续推进：计算环中n个顶点时每个选手的最大比赛数，以及路径中n个顶点时的最大比赛数 | 环中每个对可比赛n-5场，每个选手(在2个对中)最多2(n-5)场；路径中各选手比赛数不同，中间选手最多约n-6场 |
| 6 | 思维操作引导 | 0.3 | 利用A中每个元素被6整除的性质，设计最优构造方案使选手数最少。考虑环结构中2(n-5)与6的整除关系。 | 被6整除意味着M=6m，环中2(n-5)=M→n=M/2+5，但利用整除性可以优化构造（如调整路径端点等），最终得到n=(1/2)max(A)+3 |
| 7 | 能量传递引导 | 0.6 | 验证你的答案：对简单情况检验(1/2)max(A)+3是否正确，确认构造的赛程确实使比赛集合等于A | 对A={6}验证n=6，对A={6,12}验证n=9等，确认构造正确 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: discrete_combinatorial
- structure_features: 组合约束优化问题，三个约束条件（度数限制、比赛限制、队友不对抗），目标是最小化选手数使得比赛集合等于给定集合A（元素均被6整除）
- key_objects: ["选手", "对（双人组合）", "比赛", "比赛集合", "集合A（元素被6整除）", "图（顶点和边）", "路径和环"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["graph_modeling", "constraint_analysis", "optimization", "constructive_proof", "number_theory_utilization"]
- primary_pattern: graph_modeling
- knowledge_required: ["图论基础", "最大度2图的结构（路径和环的并集）", "组合优化", "整除性", "构造性证明"]
- key_insight: 将选手建模为顶点、对建模为边，最大度2意味着图是路径和环的并集，条件(iii)转化为图距离约束（距离≥3才能比赛），再利用被6整除的性质优化构造

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 组合约束文字描述（乒乓球比赛规则）
- translation_to: 图论模型（度数约束+距离约束+整除性优化）
- translation_type: structural_transformation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "structural_transformation"}
- tell_small_concepts: ["图论建模", "度数约束", "路径和环", "兼容性距离", "整除性优化", "构造性证明"]
- expected_ai_method: 枚举所有可能的赛程安排，暴力搜索最小选手数
- correct_method: 图论建模+兼容性分析+整除性优化构造

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=discrete_combinatorial、ai_method_type=enumeration_brute_force、gap_type=structural_transformation均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 不需要新的拓扑维度——三个维度足够区分这道题的tell
- 无拓扑进化建议

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

局部pair摘要：
- R1: tell=未识别图论建模方向, hint=描述题目结构, level=0.8, 纯元认知观察, topology=(discrete_combinatorial, direct_calculation, structural_transformation)
- R2: tell=未将图论作为优先方向, hint=列举所有建模方法, level=0.7, 自由列举, topology=(discrete_combinatorial, enumeration_brute_force, method_problem_mismatch)
- R3: tell=图论建模可能出错, hint=尝试顶点/边建模, level=0.5, 小尝试, topology=(discrete_combinatorial, direct_manipulation, structural_transformation)
- R4: tell=未推导兼容性约束, hint=分析条件iii, level=0.4, 思维操作引导, knowledge_bottleneck=True, topology=(discrete_combinatorial, logical_deduction, knowledge_gap)
- R5: tell=未计算最大比赛数, hint=计算环/路径中比赛数, level=0.5, 推进, topology=(discrete_combinatorial, direct_calculation, search_space_estimation)
- R6: tell=未利用整除性优化, hint=利用被6整除设计最优构造, level=0.3, 思维操作引导, knowledge_bottleneck=True, topology=(discrete_combinatorial, direct_calculation, knowledge_gap)
- R7: tell=未验证构造正确性, hint=验证简单情况, level=0.6, 能量传递引导, topology=(discrete_combinatorial, direct_calculation, method_translation)

全局pair摘要：
- G1(path_feature): 三步关键转换路径不可见, level=0.7
- G2(implicit): 答案公式结构与图参数的隐含对应, level=0.6

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI可能尝试直接枚举赛程或用组合设计方法，无法识别图论建模的关键转换，也无法利用被6整除的性质进行优化。即使识别出图论建模，也可能在兼容性约束分析（条件iii→距离≥3）上出错，或在从图结构分析到利用整除性优化的转换上卡住。
- suitable_for_poc: ["tell端验证：图论建模分叉信号识别", "hint端验证：结构转换提示有效性", "多重转换路径验证：三步转换的tell识别"]
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
- [x] answer（**⚠️ 必填，不能为None**）
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

**将完整JSON写入工作目录的 `profile.json` 文件** ✅ 已写入

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
2. 更新`problem_extraction_progress`集合中`_key="329878"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_000007"
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
    '_key': '329878',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_000007',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_000007')
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
- problem_id: omni_math_000007
- solution_method_type: graph_theory_modeling
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类够用
- 是否遇到异常: 题目解答在problem.lean中被截断（仅15行），solution_text为基于Answer和Solution开头的重构

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
