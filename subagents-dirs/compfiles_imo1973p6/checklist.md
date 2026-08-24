# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1973p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1973P6.lean
- **来源**: IMO 1973 P6
- **ArangoDB progress记录_key**: 329065（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1973P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let $a_1, a_2, \cdots, a_n$ be $n$ positive numbers, and let $q$ be a given real number such that $0 < q < 1$. Find $n$ numbers $b_1, b_2, \cdots, b_n$ for which (a) $a_k < b_k$ for $k=1,\cdots,n$, (b) $q < b_{k+1}/b_k < 1/q$ for $k=1,\cdots,n-1$, (c) $\sum b_k < \frac{1+q}{1-q} \sum a_k$.
- 解答核心思路（1-2句话）：定义 $b_k = \sum_{j=1}^n q^{|k-j|} a_j$（即 $b = Q \cdot a$，其中 $Q_{ij} = q^{|i-j|}$），利用几何核的移位性质和衰减性质同时满足三个约束。
- 解答关键步骤列表：
  1. 构造矩阵 $Q_{ij} = q^{|i-j|}$，令 $b = Q \cdot a$，即 $b_k = \sum_j q^{|k-j|} a_j$
  2. 验证(a)：$b_k = a_k + \sum_{j \neq k} q^{|k-j|} a_j > a_k$（对角项为1，其余正项）
  3. 验证(b)：将求和按 $Q_{k+1,j}$ 与 $Q_{k,j}$ 的关系分为两组 $X$（比值=$q$）和 $Y$（比值=$q^{-1}$），则 $b_k = X+Y$，$b_{k+1} = qX + q^{-1}Y$，因 $X,Y>0$ 得 $q < b_{k+1}/b_k < 1/q$
  4. 验证(c)：$\sum_k b_k = \sum_j a_j \sum_k q^{|k-j|}$，内层求和 $\leq 1 + 2\sum_{d=1}^{n-1} q^d < 1 + \frac{2q}{1-q} = \frac{1+q}{1-q}$

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
| 1 | 纯元认知观察 | 0.8 | 这道题的结构是什么？我们需要找到什么，有哪些约束条件？ | 这是一个构造性问题：给定正数序列 $a_k$ 和参数 $q\in(0,1)$，需要构造序列 $b_k$ 同时满足三个约束：(a)逐点支配 $b_k > a_k$，(b)相邻比值有界 $q < b_{k+1}/b_k < 1/q$，(c)总和有界 $\sum b_k < \frac{1+q}{1-q}\sum a_k$。三个约束相互关联——比值约束迫使某种平滑操作，总和约束限制了平滑的幅度。 |
| 2 | 自由列举 | 0.7 | 有哪些可能的构造 $b_k$ 的方法？列出所有你能想到的方向。 | 可能方向：(1)常数缩放 $b_k = c \cdot a_k$；(2)加常数 $b_k = a_k + \epsilon$；(3)滑动平均/平滑 $b_k = \sum w_{k-j} a_j$；(4)递推构造 $b_{k+1} = f(b_k, a_k)$；(5)矩阵变换 $b = M \cdot a$；(6)分段线性插值。关键是找到一个能同时控制比值和总和的构造。 |
| 3 | 小尝试 | 0.3 | 试试最简单的构造 $b_k = c \cdot a_k$（$c>1$），看看哪里不行。 | 条件(a)满足（$c>1$时 $b_k > a_k$）。但条件(b)要求 $q < a_{k+1}/a_k < 1/q$，而 $a_k$ 是任意正数，其比值不受控制，所以简单缩放不能保证比值约束。条件(c)也需要 $c < \frac{1+q}{1-q}$，但即使满足(c)，(b)仍然失败。这个方向走不通。 |
| 4 | 思维操作引导 | 0.5 | 简单缩放失败是因为 $a_k$ 的比值不受控。$b_k$ 需要"平滑"$a_k$ 使相邻比值可控。想想什么操作能产生比值受控的序列？ | 需要一种平滑/卷积操作，将相邻的 $a_k$ 值混合起来。如果用衰减权重的卷积 $b_k = \sum_j w_{k-j} a_j$，权重 $w_d$ 随距离衰减，那么 $b_k$ 和 $b_{k+1}$ 共享大部分项，只是权重移位了一步。如果权重有几何衰减性质，移位恰好乘以一个常数因子，这样比值就能被控制。 |
| 5 | 思维操作引导 | 0.3 | 考虑具体的几何核 $w_d = q^{|d|}$，定义 $b_k = \sum_{j=1}^n q^{|k-j|} a_j$。验证条件(a)。 | $b_k = q^0 \cdot a_k + \sum_{j \neq k} q^{|k-j|} a_j = a_k + \text{正项} > a_k$。对角项 $q^0 = 1$ 给出 $a_k$ 本身，所有其他项 $q^{|k-j|} a_j > 0$（因 $q > 0$ 且 $a_j > 0$）。所以条件(a)满足。 |
| 6 | 推进 | 0.4 | 现在验证条件(b)。观察 $b_{k+1}/b_k$ 的结构——$Q_{k+1,j}$ 和 $Q_{k,j}$ 之间有什么关系？ | 对每个 $j$，$Q_{k+1,j} = q^{|k+1-j|}$ 和 $Q_{k,j} = q^{|k-j|}$ 的比值要么是 $q$（当 $j \leq k$ 时距离增加1），要么是 $q^{-1}$（当 $j > k$ 时距离减少1）。将求和分为两组：$X = \sum_{j \leq k} Q_{k,j} a_j$（比值=$q$），$Y = \sum_{j > k} Q_{k,j} a_j$（比值=$q^{-1}$）。则 $b_k = X+Y$，$b_{k+1} = qX + q^{-1}Y$。因 $X, Y > 0$，$b_{k+1}/b_k$ 是 $q$ 和 $q^{-1}$ 的凸组合的比值，故 $q < b_{k+1}/b_k < 1/q$。 |
| 7 | 推进 | 0.4 | 验证条件(c)。计算 $\sum_k b_k$ 并用几何级数界定。 | $\sum_k b_k = \sum_j a_j \sum_k q^{|k-j|}$。内层求和 $\sum_k q^{|k-j|} = 1 + \sum_{d=1}^{j-1} q^d + \sum_{d=1}^{n-j} q^d \leq 1 + 2\sum_{d=1}^{n-1} q^d < 1 + \frac{2q}{1-q} = \frac{1+q}{1-q}$。因每个 $a_j > 0$，严格不等式成立：$\sum b_k < \frac{1+q}{1-q} \sum a_k$。 |
| 8 | 能量传递引导 | 0.6 | 三个条件全部验证完毕。总结一下：为什么几何核 $q^{|k-j|}$ 能同时满足所有约束？ | 几何核 $q^{|k-j|}$ 的三个性质恰好对应三个约束：(1)对角占优（$q^0=1$加上正项）→条件(a)；(2)移位性质（移一步乘$q$或$q^{-1}$）→X/Y分解→条件(b)；(3)几何衰减（$\sum q^d$收敛）→行和$< \frac{1+q}{1-q}$→条件(c)。常数$\frac{1+q}{1-q}$正是无穷几何级数$1 + 2\cdot\frac{q}{1-q}$的和，是最优的上界。 |

**统计**：
- total_rounds: 8
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5（R1纯元认知观察+R2自由列举+R6推进+R7推进+R8能量传递引导）
- knowledge_rounds（思维操作引导的轮数）: 2（R4+R5）
- level_sum: 0.8+0.7+0.3+0.5+0.3+0.4+0.4+0.6 = 4.0
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R5（需要知道使用几何核 $q^{|k-j|}$ 作为卷积核）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R6（需要发现X/Y分解来验证比值约束）

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
- problem_type: constraint_satisfaction
- structure_features: 三个同时约束的构造性问题——逐点支配约束(a)、相邻比值约束(b)、全局总和约束(c)。三个约束相互关联：比值约束迫使平滑操作，总和约束限制平滑幅度。关键在于找到一个构造使三个约束同时满足。
- key_objects: 正数序列 $a_k$，参数 $q\in(0,1)$，目标序列 $b_k$，几何核矩阵 $Q_{ij}=q^{|i-j|}$，X/Y分解的两组求和

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [construction_by_convolution, decomposition_splitting, geometric_series_bounding, kernel_method, shift_property_exploitation]
- primary_pattern: construction_by_convolution
- knowledge_required: [geometric series, matrix-vector products, ratio analysis, convex combinations, convolution kernels, shift-invariant kernels]
- key_insight: 定义 $b_k = \sum_j q^{|k-j|} a_j$——几何核 $q^{|k-j|}$ 的移位性质（移一步乘$q$或$q^{-1}$）给出比值控制，几何衰减给出总和控制，对角占优给出逐点支配，三个性质恰好对应三个约束。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: direct_manipulation（直接对 $a_k$ 做简单缩放/变换）
- translation_to: matrix_convolution（用几何核矩阵 $Q_{ij}=q^{|i-j|}$ 做卷积，将逐点操作翻译为全局平滑操作）
- translation_type: method_translation（从朴素缩放方法翻译到结构化卷积方法，核心是认识到需要平滑操作而非逐点变换）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: constraint_satisfaction, ai_method_type: direct_calculation, gap_type: method_translation}
- tell_small_concepts: ["geometric kernel", "q^{|i-j|}", "convolution", "ratio bound", "X/Y decomposition", "geometric series bound", "smoothing", "matrix-vector product", "shift property"]
- expected_ai_method: direct_calculation（bare AI预期会用简单缩放或直接变换，如 $b_k = c \cdot a_k$，因不认识需要卷积平滑而失败）
- correct_method: 用几何核矩阵 $Q_{ij}=q^{|i-j|}$ 做卷积构造 $b = Q \cdot a$，利用核的移位性质和几何衰减同时满足三个约束

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type(constraint_satisfaction)/ai_method_type(direct_calculation)/gap_type(method_translation)均能归入已有的拓扑类别，够用。
- [x] 粒度是否一致——标注的值和已有值粒度统一，均为中等抽象级别。
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。

**拓扑进化建议**（如有）：无。当前拓扑分类体系完全够用。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 8 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs详情**（已写入profile.json）：
- R1: tell=未识别三约束的交互性, hint=描述问题结构, level=0.8, 纯元认知观察, topology=(constraint_satisfaction, direct_calculation, method_problem_mismatch)
- R2: tell=未列出卷积/平滑方向, hint=列举所有构造方法, level=0.7, 自由列举, topology=(constraint_satisfaction, enumeration_brute_force, search_space_estimation)
- R3: tell=尝试简单缩放失败, hint=试最简单构造看失败点, level=0.3, 小尝试, topology=(constraint_satisfaction, direct_calculation, method_problem_mismatch)
- R4: tell=认识到需要平滑但不知用什么核, hint=引导到卷积/平滑思路, level=0.5, 思维操作引导, is_knowledge_bottleneck=true, topology=(constraint_satisfaction, direct_manipulation, knowledge_gap)
- R5: tell=考虑卷积但未识别几何核, hint=给定几何核验证(a), level=0.3, 思维操作引导, is_knowledge_bottleneck=true, topology=(constraint_satisfaction, algebraic_identity, knowledge_gap)
- R6: tell=有构造但未见X/Y分解, hint=引导发现移位性质和分组, level=0.4, 推进, topology=(constraint_satisfaction, case_by_case, structural_transformation)
- R7: tell=需用几何级数界定总和, hint=计算行和用几何级数, level=0.4, 推进, topology=(constraint_satisfaction, direct_calculation, structural_transformation)
- R8: tell=全部验证完毕需综合, hint=总结为何几何核同时满足, level=0.6, 能量传递引导, topology=(constraint_satisfaction, logical_deduction, method_translation)

**全局pairs详情**（已写入profile.json）：
- GP1 (path_feature): 几何核选择——从三约束交互中涌现的构造，非任何单一约束可见
- GP2 (implicit): X/Y分解——隐含在核的移位结构中，需观察 $Q_{k+1,j}$ 与 $Q_{k,j}$ 关系才可见

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试简单缩放 $b_k = c \cdot a_k$ 或加常数 $b_k = a_k + \epsilon$，在条件(b)上失败——因为 $a_k$ 的比值不受控制。AI不会想到用几何核卷积来平滑序列，因为"用矩阵 $Q_{ij}=q^{|i-j|}$ 构造 $b$"这个ansatz非常不显然，需要同时认识到三个约束的交互性以及几何核的移位性质。
- suitable_for_poc: ["hint_injection_effectiveness", "knowledge_gap_identification", "construction_method_discovery", "topology_discrimination"]
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
- [x] answer
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

**将完整JSON写入工作目录的 `profile.json` 文件** — 已完成

---

## Step 10: 入库ArangoDB [x]

**操作**：用exec工具执行Python脚本入库

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="329065"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1973p6"
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
    '_key': '329065',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1973p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1973p6')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [ ] 成功 / [ ] 失败
- 验证结果: [ ] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_imo1973p6
- solution_method_type: matrix_convolution
- 局部(tell,hint)对数量: 8
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，当前拓扑分类体系完全够用
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
