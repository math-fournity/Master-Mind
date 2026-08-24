# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003252
- **文件路径**: subagents-dirs/omni_math_003252/problem.lean
- **来源**: AoPS omni_math (putnam)
- **ArangoDB progress记录_key**: 333130（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003252/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：非负整数n，严格递增实数序列t_0,...,t_n，f(t)由条件(a)-(d)定义：连续、f(t_0)=1/2、右导数极限为0、分段二阶导数为k+1。约束t_k≥t_{k-1}+1。求使f(t_0+T)=2023的最小T。
- 解答核心思路（1-2句话）：在每个区间积分得到f的增量公式，将问题转化为约束优化问题（最小化Σs_k s.t. Σk·s_k²=4045, s_k≥1），用拉格朗日乘数法求解，对离散参数n取最优。
- 解答关键步骤列表：
  1. 定义s_k=t_k-t_{k-1}，t_{n+1}=t_0+T
  2. 在[t_{k-1},t_k]上积分：f'(t)=k(t-t_{k-1})，f(t_k)-f(t_{k-1})=(k/2)s_k²
  3. 由f(t_0)=1/2和f(t_0+T)=2023得Σk·s_k²=4045
  4. 转化为优化：min T=Σs_k s.t. Σk·s_k²=4045, s_k≥1(k≤n), n≥0整数
  5. 紧致性论证最小值存在
  6. 拉格朗日乘数法+不等式约束(KKT)：s_k=max(1,1/(2λk))(k≤n), s_{n+1}=1/(2λ(n+1))
  7. 对不同n值求解λ并计算T，取最优得T=29

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
| 1 | 纯元认知观察 | 0.3 | 描述这道题的结构：f(t)是如何被条件(a)-(d)定义的？已知什么、求什么？约束条件是什么？ | f是分段二次函数：在每个区间(t_k,t_{k+1})上f''=k+1，右导数在分点处为0，f(t_0)=1/2。求最小T使f(t_0+T)=2023，约束t_k≥t_{k-1}+1。 |
| 2 | 自由列举 | 0.5 | 列出所有可能的研究方向：如何处理这个分段定义的函数f？ | 直接逐段积分求f显式表达式；考虑每个区间上f值的增量；将问题看作优化问题（最小化T）；拉格朗日乘数法；尝试小的n值枚举；利用f''的结构。 |
| 3 | 小尝试 | 0.4 | 在每个区间[t_{k-1},t_k]上，利用f''(t)=k和f'(t_{k-1}^+)=0，计算f(t_k)-f(t_{k-1})的表达式。用s_k=t_k-t_{k-1}表示。 | f'(t)=k(t-t_{k-1})，积分得f(t_k)-f(t_{k-1})=(k/2)s_k^2。因此f(t_0+T)=1/2+(1/2)Σk·s_k^2。 |
| 4 | 思维操作引导 | 0.6 | 现在你有了f(t_0+T)的表达式。请将问题重新表述为一个优化问题：目标函数是什么？等式约束是什么？不等式约束是什么？离散参数是什么？ | 最小化T=Σs_k，约束：Σk·s_k^2=4045（等式），s_k≥1 for k≤n（不等式），n≥0整数（离散参数），s_{n+1}>0。 |
| 5 | 思维操作引导 | 0.7 | 对这个带不等式约束的优化问题，如何用拉格朗日乘数法（KKT条件）求解？s_k的最优值应该是什么形式？ | 由KKT条件：对s_k求导得1=2λk·s_k（当约束不紧时），所以s_k=max(1,1/(2λk)) for k≤n，s_{n+1}=1/(2λ(n+1))。需要找到使Σk·s_k^2=4045的λ，并对每个n计算T。 |
| 6 | 推进 | 0.6 | 现在需要确定最优的n值。对于给定的n，如何计算T？哪些s_k的约束是紧的（s_k=1），哪些是松的？尝试分析约束紧/松的分界点。 | 设c=2λ，则s_k=1当k≤1/c，s_k=1/(ck)当k>1/c。约束g=4045确定c，T=Σs_k。对每个n计算T并取最小。通过数值计算找到最优n，得T=29。 |
| 7 | 能量传递引导 | 0.4 | 验证T=29的可行性：能否找到具体的n和s_k值满足所有约束并给出T=29？由优化理论这是否确实是最小值？ | 可以找到具体的n和s_k值使Σk·s_k^2=4045且Σs_k=29。由拉格朗日乘数法和紧致性论证，这是全局最小值。答案为29。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.3+0.5+0.4+0.6+0.7+0.6+0.4 = 3.5
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
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
- problem_type: constraint_satisfaction
- structure_features: 分段二次函数由递增序列定义，积分递推得到二次型约束，最小化线性目标函数，带不等式约束和离散参数的优化问题
- key_objects: ["分段二次函数f(t)", "严格递增序列t_0,...,t_n", "区间长度s_k", "二次型约束Σk·s_k²=4045", "拉格朗日乘数λ", "离散参数n"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["积分递推", "问题重构（从微积分到优化）", "拉格朗日乘数法", "KKT不等式约束处理", "离散参数优化", "紧致性论证"]
- primary_pattern: 问题重构——从分段函数积分转化为约束优化问题
- knowledge_required: ["分段函数积分", "拉格朗日乘数法", "KKT条件/不等式约束优化", "紧致性论证"]
- key_insight: 将f(t_0+T)的值通过逐段积分表示为Σ(k/2)s_k²，从而把"求最小T"问题重构为"最小化Σs_k s.t. Σk·s_k²=4045"的约束优化问题

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 微积分/分析语言（分段二次函数、积分、导数极限）
- translation_to: 约束优化语言（目标函数、等式/不等式约束、拉格朗日乘数、KKT条件）
- translation_type: method_translation（从分析方法翻译到优化方法）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "constraint_satisfaction", ai_method_type: "direct_calculation", gap_type: "method_problem_mismatch"}
- tell_small_concepts: ["分段二次函数", "积分递推", "二次型约束", "约束优化", "拉格朗日乘数", "KKT条件", "不等式约束", "紧约束分界", "离散参数优化"]
- expected_ai_method: direct_calculation——bare AI会尝试直接积分求f的显式表达式，然后枚举小的n值尝试计算，但不会意识到需要将问题重构为优化问题并用拉格朗日乘数法
- correct_method: 逐段积分得到二次型约束后，将问题重构为带不等式约束和离散参数的优化问题，用KKT条件求解

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是，constraint_satisfaction + direct_calculation + method_problem_mismatch 完全适用
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是，都是中等粒度
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。这道题的核心gap是"从计算视角到优化视角的方法转换"，method_problem_mismatch准确描述
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化

**拓扑进化建议**（如有）：无。现有拓扑分类完全适用。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs摘要**：
- R1: tell="看到分段二次函数定义但未识别优化结构", hint="描述题目结构", topology=(constraint_satisfaction, direct_calculation, method_problem_mismatch)
- R2: tell="列出方向时可能遗漏优化视角", hint="列举所有方向", topology=(constraint_satisfaction, enumeration_brute_force, search_space_estimation)
- R3: tell="直接积分可得到增量公式但未看到优化", hint="逐段积分计算增量", topology=(constraint_satisfaction, direct_calculation, method_translation)
- R4: tell="有增量公式但未重构为优化问题", hint="将问题表述为优化问题", topology=(constraint_satisfaction, direct_calculation, structural_transformation)
- R5: tell="有优化问题但不知如何处理不等式约束", hint="用KKT条件求解", topology=(constraint_satisfaction, equation_solving, knowledge_gap)
- R6: tell="有KKT解但未确定最优n", hint="分析紧/松约束分界确定最优n", topology=(constraint_satisfaction, logical_deduction, method_problem_mismatch)
- R7: tell="得到T=29但未验证", hint="验证可行性", topology=(constraint_satisfaction, direct_calculation, method_problem_mismatch)

**全局pairs摘要**：
- G1 (path_feature): tell="从微积分到优化的完整路径特征", hint="积分递推→二次型约束→拉格朗日乘数→离散优化", why_not_visible_locally="局部步骤中每一步都是机械计算，看不到整体从分析到优化的方法转换"
- G2 (implicit): tell="f(t_0)=1/2与f(t_0+T)=2023隐含Σk·s_k²=4045这一关键约束", hint="从端点值差提取等式约束", why_not_visible_locally="局部积分只给出每个区间的增量公式，等式约束需要将所有增量求和并代入端点值才能显现"

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会直接积分得到f的增量公式，但停留在计算视角，不会将问题重构为约束优化问题。即使意识到需要优化，也可能不熟悉带不等式约束的拉格朗日乘数法（KKT条件），或无法正确处理离散参数n的优化。大概率无法在合理时间内得到T=29。
- suitable_for_poc: ["tell端验证：识别AI在积分后未转向优化的分叉信号", "hint端验证：注入优化视角的脉络能否引导AI完成方法转换", "知识瓶颈验证：KKT条件作为知识瓶颈的识别与注入"]
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

## Step 10: 入库ArangoDB [ ]

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="333130"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_003252"
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
    '_key': '333130',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_003252',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_003252')
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
- problem_id: omni_math_003252
- solution_method_type: constrained_optimization
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，现有拓扑分类完全适用
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
