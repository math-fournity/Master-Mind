# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1994p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1994P5.lean
- **来源**: IMO 1994 P5
- **ArangoDB progress记录_key**: 329150（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1994P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let S be the set of all real numbers greater than -1. Find all functions f : S→S such that f(x + f(y) + xf(y)) = y + f(x) + yf(x) for all x and y, and f(x)/x is strictly increasing on each of the intervals -1 < x < 0 and 0 < x.
- 解答核心思路（1-2句话）：令x=y发现x+f(x)+xf(x)总是f的不动点；利用单调性条件证明f的唯一不动点是0；从而x+f(x)+xf(x)=0，解得f(x)=-x/(1+x)。
- 解答关键步骤列表：
  1. 验证f(x)=-x/(1+x)满足函数方程和单调性条件（直接代入）
  2. 若f(a)=a（不动点），令x=y=a得f(2a+a²)=2a+a²，即b=2a+a²也是不动点
  3. 若-1<a<0，则b<a，但f(a)/a=f(b)/b=1，与严格递增矛盾
  4. 若a>0，则b>a，同样f(a)/a=f(b)/b=1，与严格递增矛盾
  5. 故f的唯一不动点是0
  6. 令x=y得f(x+f(x)+xf(x))=x+f(x)+xf(x)，即x+f(x)+xf(x)是不动点，故=0
  7. 解x+f(x)+xf(x)=0得f(x)=-x/(1+x)

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.3 | 描述这道题的结构：已知条件有哪些？未知是什么？两个条件之间有什么潜在联系？ | 题目要求找所有f:S→S满足：(1)函数方程f(x+f(y)+xf(y))=y+f(x)+yf(x)；(2)f(x)/x在(-1,0)和(0,∞)上严格递增。两个条件约束同一个函数f，单调性条件可能是排除多余解的关键。 |
| 2 | 自由列举 | 0.5 | 列出你能想到的所有解题方向：可以尝试哪些特殊值代入？有哪些结构可以利用？ | 方向包括：令x=0或y=0看能得到什么关系；令x=y看是否有特殊结构；寻找不动点f(a)=a；猜函数形式后验证；利用单调性条件作为约束；观察x+f(y)+xf(y)的结构。 |
| 3 | 小尝试 | 0.2 | 试试令x=0和y=0分别代入函数方程，能得到什么关系？这些关系足够解题吗？ | x=0: f(f(y))=y(1+f(0))+f(0)；y=0: f(x+f(0)+xf(0))=f(x)(1+x)。这些给出一些关系但不足以确定f，需要更强的观察。 |
| 4 | 思维操作引导 | 0.4 | 令x=y代入函数方程。f(x+f(x)+xf(x))=x+f(x)+xf(x)告诉你什么？表达式x+f(x)+xf(x)有什么特殊性质？ | 令x=y得f(x+f(x)+xf(x))=x+f(x)+xf(x)，说明k=x+f(x)+xf(x)是f的不动点（f(k)=k）对任意x成立。这是连接函数方程和不动点的关键桥梁。 |
| 5 | 思维操作引导 | 0.5 | 现在利用单调性条件。如果a是不动点(f(a)=a)且a≠0，令x=y=a能得到什么矛盾？ | 若f(a)=a，令x=y=a得f(2a+a²)=2a+a²，即b=2a+a²也是不动点。若-1<a<0则b<a，但f(a)/a=f(b)/b=1，与f(x)/x严格递增矛盾。若a>0则b>a，同理矛盾。故唯一不动点是0。 |
| 6 | 推进 | 0.6 | 结合两个结论：每个x+f(x)+xf(x)都是不动点，而唯一不动点是0。由此能解出f(x)吗？ | x+f(x)+xf(x)=0对所有x成立，解得f(x)=-x/(1+x)。这就是唯一的候选函数。 |
| 7 | 能量传递引导 | 0.7 | 验证f(x)=-x/(1+x)确实满足函数方程和单调性条件。你快完成了！ | 直接代入验证函数方程成立（利用(1+x)(1+f(y))的乘法结构）。f(x)/x=-1/(1+x)在(-1,0)和(0,∞)上严格递增。验证完毕，f(x)=-x/(1+x)是唯一解。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.2
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R5（需要知道不动点如何与单调性条件交互产生矛盾）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R4（x=y代入得到不动点结构是关键思维转折）

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization（求所有满足条件的函数，是刻画问题）
- structure_features: 函数方程f(x+f(y)+xf(y))=y+f(x)+yf(x)具有对称性结构；操作x+f(y)+xf(y)=(1+x)(1+f(y))-1有隐藏乘法结构；单调性条件f(x)/x严格递增作为附加约束排除多余解；两条件通过不动点产生交互
- key_objects: 函数f:S→S、操作op(x,y)=x+f(y)+xf(y)、不动点、f(x)/x的单调性

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["specialization（x=y代入）", "fixed point analysis（不动点分析）", "contradiction via monotonicity（单调性矛盾）", "constraint propagation（约束传播）", "verification（验证）"]
- primary_pattern: fixed point analysis with monotonicity contradiction（不动点分析+单调性矛盾）
- knowledge_required: ["函数方程", "不动点概念", "严格单调性", "代数运算", "矛盾法"]
- key_insight: 令x=y发现x+f(x)+xf(x)总是f的不动点，而单调性条件迫使唯一不动点为0，从而x+f(x)+xf(x)=0直接解出f(x)=-x/(1+x)

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 函数方程语言（直接操作函数方程的代数关系）
- translation_to: 不动点+单调性矛盾语言（将函数方程转化为不动点命题，再用单调性条件约束不动点）
- translation_type: structural_transformation（通过x=y特化将函数方程的结构翻译为不动点结构，再利用单调性条件作为独立约束消元）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_manipulation, gap_type: structural_transformation}
- tell_small_concepts: ["x=y代入", "不动点", "单调性矛盾", "x+f(x)+xf(x)=0", "唯一不动点"]
- expected_ai_method: direct_manipulation——bare AI会尝试直接操作函数方程（如x=0, y=0代入）试图代数求解，不会识别不动点结构
- correct_method: 通过x=y特化将函数方程翻译为不动点命题，再用单调性条件证明唯一不动点为0，最后解方程

### 6b. 反思拓扑分类

- [x] 当前拓扑分类是否够用——这道题的problem_type(characterization)/ai_method_type(direct_manipulation)/gap_type(structural_transformation)都能归入已有拓扑类别
- [x] 粒度是否一致——标注值和已有值粒度统一
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化

**拓扑进化建议**（如有）：无，当前分类体系足够

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs详情**：

| R | tell | hint | level | situation_type | kb | tell_topology | small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对函数方程+单调性两个条件，不知道从哪里入手 | 描述题目结构：两个条件约束同一个函数f，单调性可能是排除多余解的关键 | 0.3 | 纯元认知观察 | F | (characterization, direct_manipulation, method_problem_mismatch) | ["函数方程", "单调性条件", "两个约束"] |
| 2 | AI列出方向但可能不优先考虑x=y代入 | 列出所有可能方向：特殊值代入、不动点、猜形式验证、利用单调性 | 0.5 | 自由列举 | F | (characterization, enumeration_brute_force, search_space_estimation) | ["特殊值代入", "不动点", "单调性约束"] |
| 3 | AI尝试x=0/y=0得到部分关系但无法突破 | 试x=0和y=0，得到f(f(y))=y(1+f(0))+f(0)等关系，但不足以确定f | 0.2 | 小尝试 | F | (characterization, direct_calculation, method_problem_mismatch) | ["x=0代入", "y=0代入", "部分关系"] |
| 4 | AI没有考虑x=y，错过了不动点结构 | 令x=y代入，发现x+f(x)+xf(x)是f的不动点 | 0.4 | 思维操作引导 | F | (characterization, direct_manipulation, structural_transformation) | ["x=y代入", "不动点", "x+f(x)+xf(x)"] |
| 5 | AI知道x+f(x)+xf(x)是不动点但不知道如何用单调性约束不动点 | 若f(a)=a且a≠0，令x=y=a得b=2a+a²也是不动点，用单调性矛盾 | 0.5 | 思维操作引导 | T | (characterization, logical_deduction, knowledge_gap) | ["不动点传播", "单调性矛盾", "2a+a²", "f(a)/a=f(b)/b"] |
| 6 | AI知道唯一不动点是0且x+f(x)+xf(x)总是不动点，但没结合 | 结合两个结论：x+f(x)+xf(x)=0，解得f(x)=-x/(1+x) | 0.6 | 推进 | F | (characterization, algebraic_identity, method_translation) | ["不动点=0", "x+f(x)+xf(x)=0", "解f(x)"] |
| 7 | AI得出f(x)=-x/(1+x)但未验证 | 验证f(x)=-x/(1+x)满足函数方程和单调性条件 | 0.7 | 能量传递引导 | F | (characterization, direct_calculation, method_problem_mismatch) | ["验证", "函数方程检验", "单调性检验"] |

**全局pairs详情**：

1. path_feature型: 完整解题路径需要"特化→不动点→单调性矛盾→消元"两阶段策略
   - scope: "complete solution path"
   - tell: 解题需要两阶段策略——先用x=y特化建立不动点结构，再用单调性条件消元
   - hint: 函数方程和单调性条件不是独立约束，它们通过不动点产生交互
   - hint_level: 0.8
   - generalizability: high——"用特化揭示隐藏结构（不动点），再用辅助条件约束该结构"的模式在许多函数方程问题中出现
   - why_not_visible_locally: 从任何单步看（如试x=0、或验证答案），两阶段策略不可见。x=y代入看起来只是又一次特化尝试，但它是连接函数方程和单调性条件的桥梁。只有看到完整路径才理解这个策略。
   - tell_topology: (characterization, direct_manipulation, structural_transformation)
   - tell_small_concepts: ["两阶段策略", "不动点桥梁", "特化到结构", "约束交互"]

2. implicit型: 操作x+f(y)+xf(y)=(1+x)(1+f(y))-1的隐藏乘法结构
   - scope: "hidden algebraic structure of the operation"
   - observation_point: R4
   - tell: 表达式x+f(y)+xf(y)可改写为(1+x)(1+f(y))-1，揭示隐藏乘法结构
   - hint: 寻找简化操作的变量替换——u=1+x将操作转化为乘法
   - hint_level: 0.7
   - generalizability: medium——(1+x)替换技巧对x+f(y)+xf(y)结构的问题特定，但识别加法表达式中隐藏乘法结构的模式广泛适用
   - why_not_visible_locally: 在R4中焦点是x=y得不动点。乘法结构(1+x)(1+f(y))-1对不动点路径不是必需的，但它解释了答案为何有-x/(1+x)的形式以及函数方程的对称性。这个结构洞察隐含在答案形式中但在不动点方法的任何单步中都不可见。
   - tell_topology: (characterization, algebraic_identity, structural_transformation)
   - tell_small_concepts: ["乘法结构", "(1+x)替换", "隐藏对称性", "操作简化"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试x=0和y=0代入得到部分关系后试图代数求解函数方程，不会识别x=y代入的不动点结构。它会将函数方程和单调性条件视为两个独立约束分别处理，而非通过不动点建立交互。大概率卡在部分关系无法推进。
- suitable_for_poc: ["tell_extraction_poc", "hint_injection_poc", "path_feature_poc"]
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
- [x] answer（f(x) = -x/(1+x) for all x in S）
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
- [x] tell_hint_pairs（7对，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（2对，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象）
- [x] analysis_metadata

**已将完整JSON写入 `subagents-dirs/compfiles_imo1994p5/profile.json`**

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
2. 更新`problem_extraction_progress`集合中`_key="329150"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1994p5"
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
    '_key': '329150',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1994p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1994p5')
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
- problem_id: compfiles_imo1994p5
- solution_method_type: fixed_point_monotonicity_contradiction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，当前分类体系（problem_type/ai_method_type/gap_type三维）足够覆盖此题
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
