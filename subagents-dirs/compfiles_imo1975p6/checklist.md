# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1975p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1975P6.lean
- **来源**: IMO 1975 P6
- **ArangoDB progress记录_key**: 329075（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1975P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Find all polynomials P in two variables satisfying: (i) P is homogeneous of degree n: P(tx,ty) = t^n P(x,y) for all real t,x,y and positive integer n; (ii) P(b+c,a) + P(c+a,b) + P(a+b,c) = 0 for all real a,b,c; (iii) P(1,0) = 1.
- 解答核心思路（1-2句话）：定义辅助函数 f(x) = P(1-x, x) - 1，利用循环条件(ii)推导出 f 满足 Cauchy 函数方程 f(x+y) = f(x) + f(y)，由连续性得 f(x) = -3x，再用齐次性恢复 P(a,b) = (a-2b)(a+b)^(n-1)。
- 解答关键步骤列表：
  1. 定义 f(x) = P(1-x, x) - 1，证明 f 连续（多项式在直线上求值连续）
  2. 利用条件(ii)代入特定值，推导 f(x+y) = f(x) + f(y)（Cauchy函数方程）
  3. 由 f(1) = P(0,1) - 1 = -2 - 1 = -3（条件(ii)代入a=0,b=1,c=0得P(0,1)=-2）
  4. 连续Cauchy解必线性：f(x) = -3x（先整数→有理数→实数，用连续性延拓）
  5. 令 x = b/(a+b), y = a/(a+b)，用齐次性 P(a,b) = (a+b)^n · P(a/(a+b), b/(a+b)) = (a+b)^n · (-3b/(a+b) + 1) = (a-2b)(a+b)^(n-1)，对 a+b ≠ 0
  6. 由连续性（多项式恒等定理）延拓到所有 (a,b)
  7. 验证 P(1,0) = 1·1 = 1 ✓，解集为 {(X-2Y)(X+Y)^n : n ∈ ℕ}

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
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：三个条件分别给出了什么信息？我们要找的是什么？ | 三个条件分别给出：齐次性（P的度数结构和缩放行为）、循环函数方程（P在特定线性变换下的约束）、归一化（固定P的一个值）。我们要找的是满足所有三个条件的所有二元多项式。关键挑战在于将循环条件(ii)与P的具体形式联系起来。 |
| 2 | 自由列举 | 0.7 | 列出你能想到的所有可能方法来确定P的形式。 | 可能方法：直接代入特殊值（a=0,b=0,c=0等）获取P的特定值；尝试低次情形（n=1,2,3）猜测模式；利用齐次性将P写成单项式之和然后展开条件(ii)；试图从条件(ii)中提取函数方程；尝试因式分解P；利用P(1,0)=1和齐次性确定首项系数。 |
| 3 | 小尝试 | 0.4 | 试代入特殊值：a=0,b=1,c=0 和 a=0,b=0,c=0 到条件(ii)中，你得到什么？ | a=b=c=0: 3P(0,0)=0 → P(0,0)=0。a=0,b=1,c=0: P(1,0)+P(0,1)+P(1,0)=0 → 1+P(0,1)+1=0 → P(0,1)=-2。这些给出了P的特定值，但还看不出如何推广到一般形式。需要找到一种系统化的方法。 |
| 4 | 思维操作引导 | 0.5 | 考虑定义辅助函数 f(x) = P(1-x, x) - 1。尝试用条件(ii)证明 f(x+y) = f(x) + f(y)。提示：在条件(ii)中令 a = x+y, b = 1-x-y, c = 0，再令 a = x, b = y, c = 1-x-y。 | 代入 a=x+y, b=1-x-y, c=0: P(1-x-y, x+y) + P(x+y, 1-x-y) + P(1, 0) = 0。代入 a=x, b=y, c=1-x-y: P(1-x, x) + P(1-y, y) + P(x+y, 1-x-y) = 0。两式相减并利用 P(1,0)=1 和 f 的定义，可得 f(x+y) = f(x) + f(y)。这是 Cauchy 函数方程！ |
| 5 | 思维操作引导 | 0.4 | f 是连续的（因为 P 在直线上求值是连续的），且 f 满足 Cauchy 方程。连续的 Cauchy 解有什么性质？f(1) 等于多少？ | 连续的 Cauchy 解必为线性函数 f(x) = cx。f(1) = P(0,1) - 1 = -2 - 1 = -3。所以 f(x) = -3x。这给出了 P(1-x, x) = 1 - 3x 对所有实数 x 成立。 |
| 6 | 推进 | 0.5 | 现在利用齐次性条件(i)。令 x = b/(a+b), y = a/(a+b)（a+b≠0），用 P(1-x, x) = 1-3x 和 P(tx,ty) = t^n P(x,y) 推导 P(a,b) 的表达式。 | P(a/(a+b), b/(a+b)) = P(1 - b/(a+b), b/(a+b)) = 1 - 3b/(a+b) = (a-2b)/(a+b)。由齐次性 P(a,b) = (a+b)^n · P(a/(a+b), b/(a+b)) = (a+b)^n · (a-2b)/(a+b) = (a-2b)(a+b)^(n-1)。 |
| 7 | 能量传递引导 | 0.7 | 你已经得到 P(a,b) = (a-2b)(a+b)^(n-1) 对 a+b≠0 成立。由于 P 是多项式，这个等式可以延拓到所有 (a,b)。验证 P(1,0)=1 并写出最终答案。 | P(x,y) = (x-2y)(x+y)^(n-1) 对所有 (x,y) 成立（多项式恒等定理）。验证：P(1,0) = (1-0)(1+0)^(n-1) = 1 ✓。解集为 P(x,y) = (x-2y)(x+y)^n, n ∈ ℕ（其中 n = degree - 1）。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.8 + 0.7 + 0.4 + 0.5 + 0.4 + 0.5 + 0.7 = 4.0
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R5（知道连续Cauchy解必线性是纯知识瓶颈）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R4（想到定义 f(x)=P(1-x,x)-1 并识别Cauchy方程是思维瓶颈）

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
- problem_type: characterization（求所有满足条件的多项式——刻画问题）
- structure_features: 三个约束条件（齐次性、循环函数方程、归一化）联合确定多项式的唯一族。核心结构是循环条件(ii)中隐藏的 Cauchy 函数方程，需要通过辅助函数定义来揭示。
- key_objects: 二元齐次多项式 P(x,y), 辅助函数 f(x)=P(1-x,x)-1, Cauchy函数方程, 齐次性条件

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [structural_transformation, functional_equation_recognition, continuity_extension, homogeneity_exploitation, verification]
- primary_pattern: structural_transformation（将循环多项式条件转化为Cauchy函数方程）
- knowledge_required: [齐次多项式, Cauchy函数方程, 连续函数方程解的唯一性, 多项式恒等定理, 函数方程的连续性延拓]
- key_insight: 定义辅助函数 f(x) = P(1-x, x) - 1，循环条件(ii)在此代换下恰好变为 Cauchy 函数方程 f(x+y) = f(x) + f(y)，由连续性得 f(x) = -3x，再用齐次性恢复 P 的完整表达式。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 多项式约束条件（齐次性 + 循环函数方程 + 归一化）
- translation_to: 函数方程（Cauchy方程）+ 连续性论证 + 齐次性恢复
- translation_type: structural_transformation（通过辅助函数定义，将多项式上的循环约束翻译为一元函数的Cauchy方程，求解后再翻译回多项式）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: [齐次多项式, 循环函数方程, Cauchy函数方程, 辅助函数定义, 连续性延拓, 齐次性恢复]
- expected_ai_method: bare AI会尝试直接代入特殊值获取P的离散值，或展开P为单项式之和后逐项匹配条件(ii)，试图直接解方程组——但无法系统化推广到一般形式
- correct_method: 定义辅助函数f(x)=P(1-x,x)-1，将循环条件(ii)转化为Cauchy函数方程f(x+y)=f(x)+f(y)，由连续性得f(x)=-3x，再用齐次性恢复P(a,b)=(a-2b)(a+b)^(n-1)

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type=characterization、ai_method_type=direct_calculation、gap_type=structural_transformation均能归入已有拓扑类别，够用
- [x] 粒度是否一致——标注的值与已有值粒度统一，characterization是抽象级problem_type，direct_calculation是抽象级ai_method_type，structural_transformation是中等粒度gap_type
- [x] 是否需要新的拓扑维度——三个维度足以区分这道题的tell和已有tell，不需要新维度
- [x] 如果发现拓扑分类需要进化，在此写出建议：无进化建议，当前分类体系适用

**拓扑进化建议**（如有）：无

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**局部tell_hint_pairs（7对）**：

| Round | situation_type | hint_level | is_knowledge_bottleneck | tell | hint | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | false | AI面对三个约束条件但尚未识别循环条件中隐藏的函数方程结构，只看到表面条件 | 描述这道题的结构：三个条件分别给出了什么信息？我们要找的是什么？ | {characterization, direct_calculation, method_problem_mismatch} | [齐次性条件, 循环函数方程, 归一化条件, 条件联合] |
| 2 | 自由列举 | 0.7 | false | AI列出多种方法但未识别"定义辅助函数"这一关键方向，列举偏向直接计算 | 列出你能想到的所有可能方法来确定P的形式 | {characterization, enumeration_brute_force, search_space_estimation} | [特殊值代入, 低次猜测, 单项式展开, 因式分解, 首项系数] |
| 3 | 小尝试 | 0.4 | false | AI通过特殊值代入获得P(0,0)=0和P(0,1)=-2，但无法系统化推广，停留在离散值 | 试代入特殊值a=0,b=1,c=0和a=b=c=0到条件(ii)中，你得到什么？ | {characterization, direct_calculation, method_problem_mismatch} | [特殊值代入, P(0,0)=0, P(0,1)=-2, 离散值约束] |
| 4 | 思维操作引导 | 0.5 | false | AI未想到定义辅助函数f(x)=P(1-x,x)-1来揭示Cauchy方程结构——这是核心思维瓶颈 | 考虑定义辅助函数f(x)=P(1-x,x)-1，尝试用条件(ii)证明f(x+y)=f(x)+f(y) | {characterization, direct_manipulation, structural_transformation} | [辅助函数定义, Cauchy函数方程, 变量代换, 循环条件转化] |
| 5 | 思维操作引导 | 0.4 | true | AI已有Cauchy方程但可能不知道连续Cauchy解必线性——纯知识瓶颈 | f是连续的且满足Cauchy方程，连续Cauchy解有什么性质？f(1)等于多少？ | {characterization, logical_deduction, knowledge_gap} | [Cauchy函数方程, 连续性, 线性解, f(1)=-3, 整数到有理数到实数] |
| 6 | 推进 | 0.5 | false | AI已得f(x)=-3x但未利用齐次性将一维结果翻译回二维多项式 | 利用齐次性条件(i)，令x=b/(a+b),y=a/(a+b)，推导P(a,b)的表达式 | {characterization, algebraic_identity, method_translation} | [齐次性恢复, 变量代换, 一维到二维, (a-2b)(a+b)^(n-1)] |
| 7 | 能量传递引导 | 0.7 | false | AI已得P(a,b)对a+b≠0成立，但未完成延拓和验证 | 用多项式恒等定理延拓到所有(a,b)，验证P(1,0)=1并写出最终答案 | {characterization, direct_manipulation, method_translation} | [多项式恒等定理, 连续性延拓, 验证P(1,0)=1, 解集] |

**全局tell_hint_pairs（2对）**：

| # | scope_type | scope | observation_point | tell | hint | hint_level | generalizability | why_not_visible_locally | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | implicit | 整个解题路径的核心转化步骤 | R4 | 循环条件(ii)中隐藏的Cauchy函数方程结构在直接代入特殊值时不可见，需要通过辅助函数定义来揭示 | 定义辅助函数将二元多项式的循环约束降维为一元函数方程 | 0.6 | high - "通过辅助函数将高维约束降维到低维函数方程"的技巧在多项式问题和函数方程问题中广泛适用 | 在R3的特殊值代入中，AI只看到离散的P值，无法识别循环条件背后的函数方程结构；只有当定义了f(x)=P(1-x,x)-1并做特定代换后，Cauchy方程结构才显现 | {characterization, direct_calculation, structural_transformation} | [辅助函数定义, Cauchy函数方程, 降维转化, 循环条件隐藏结构] |
| 2 | path_feature | 从一维函数方程解到恢复二维多项式的完整路径 | null | 解出f(x)=-3x后需要利用齐次性将一维结果翻译回二维多项式，这一步需要选择正确的变量代换并处理a+b=0的边界 | 令x=b/(a+b)用齐次性恢复P(a,b)，再用多项式恒等定理延拓 | 0.5 | medium - 齐次性恢复是齐次多项式问题的通用技巧，但具体代换依赖于问题结构 | N/A（path_feature型） | {characterization, algebraic_identity, method_translation} | [齐次性恢复, 变量代换, 一维到二维翻译, 多项式恒等定理延拓] |

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: bare AI会尝试直接代入特殊值（a=0,b=0,c=0等）获取P的离散值，或展开P为单项式之和后逐项匹配条件(ii)试图直接解方程组。核心思维瓶颈在于AI不会想到定义辅助函数f(x)=P(1-x,x)-1来将循环条件转化为Cauchy方程——这一步需要创造性的结构变换而非计算。即使偶然得到f满足Cauchy方程，AI也可能不知道"连续Cauchy解必线性"这一知识点（知识瓶颈R5）。最后从一维结果恢复二维多项式的齐次性代换也是AI容易遗漏的步骤。
- suitable_for_poc: ["tell_hint_injection", "knowledge_bottleneck_detection", "structural_transformation_recognition"]
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

**将完整JSON写入工作目录的 `profile.json` 文件**：已写入 subagents-dirs/compfiles_imo1975p6/profile.json

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
2. 更新`problem_extraction_progress`集合中`_key="329075"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1975p6"
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
    '_key': '329075',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1975p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1975p6')
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
- problem_id: compfiles_imo1975p6
- solution_method_type: structural_transformation
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，当前分类体系（problem_type/ai_method_type/gap_type三维度）足以覆盖本题
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
