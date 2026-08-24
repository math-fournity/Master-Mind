# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000358
- **文件路径**: subagents-dirs/omni_math_000358/problem.lean
- **来源**: AoPS omni_math (alibaba_global_contest)
- **ArangoDB progress记录_key**: 330230（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000358/problem.lean`

**产出**：
- 题目原文（数学描述）：2022冬奥会无人机编队问题。Part1: 证明u₁>1时N(t)=∫₀^∞vρ dv发散。Part2: 证明p(t,x,v)在圆周上趋于均匀分布。PDE: ρ_t+((u-v)ρ)_v=ρ_vv, p_t+vp_x+((u-v)p)_v=p_vv。
- 解答核心思路（1-2句话）：Part1定义辅助量M(t)=∫vρ dv，通过分部积分得dM/dt=u₀+u₁N-M，用M≤N得Gronwall不等式证明指数发散。Part2用Fourier分解证明k≠0模衰减。
- 解答关键步骤列表：
  1. 定义M(t)=∫vρ dv（辅助量替换N）
  2. 分部积分计算dM/dt=u₀+u₁N-M（边界项消失）
  3. 利用M≤N得dM/dt≥u₀+(u₁-1)M（Gronwall不等式）
  4. u₁>1时M(t)指数增长→N(t)→+∞
  5. Fourier分解p=Σp_k e^{ikx}
  6. 能量估计E_k=∫|p_k|²dv，耗散项主导k≠0模衰减
  7. p→(1/π)p_0（空间均匀分布）
- 注：problem.lean中Solution文本在"Because M(t)≤N(t) a"处截断，完整解答根据标准PDE技术和Answer部分重构。

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
| 1 | 纯元认知观察 | 0.7 | 描述题目结构，识别关键对象和PDE | 两部分PDE问题：Part1证N(t)发散，Part2证p均匀分布 |
| 2 | 自由列举 | 0.6 | 列出分析N(t)行为的所有方法 | 直接计算dN/dt、矩方法、能量估计、Gronwall、Fourier |
| 3 | 小尝试 | 0.4 | 试直接计算dN/dt | 半线积分产生v=0边界项，直接方法受阻 |
| 4 | 思维操作引导 | 0.3 | 定义M(t)=∫vρ dv，用PDE计算dM/dt | 分部积分得dM/dt=u₀+u₁N-M，边界项消失 |
| 5 | 思维操作引导 | 0.3 | 用M≤N关闭ODE为微分不等式，用Gronwall | dM/dt≥u₀+(u₁-1)M，u₁>1时指数增长→N→∞ |
| 6 | 思维操作引导 | 0.4 | Part2用Fourier分解，写出模方程 | p=Σp_k e^{ikx}，k≠0模有ikv项，需证E_k→0 |
| 7 | 能量传递引导 | 0.6 | 完成k≠0模能量估计，结论 | 耗散项主导，E_k→0，p→(1/π)p_0均匀分布 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 3
- knowledge_rounds（思维操作引导的轮数）: 3
- level_sum: 3.3
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R4
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R3

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
- problem_type: inequality_proof（核心技巧是微分不等式+能量估计，均为不等式方法）
- structure_features: 两部分PDE问题（发散证明+收敛证明），传输-扩散方程带反馈控制，矩方法+Gronwall+Fourier+能量估计
- key_objects: ρ(t,v)速度密度, p(t,x,v)联合密度, N(t)正部平均, M(t)全平均, u(t)=u₀+u₁N(t)命令速度, Fourier模p_k(t,v), 能量E_k(t)

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: [矩方法, 辅助量替换, 微分不等式/Gronwall, Fourier分解, 能量估计, 表示翻译]
- primary_pattern: auxiliary_quantity_substitution（辅助量替换：N→M绕过边界项）
- knowledge_required: [PDE分部积分+消失边界条件, Gronwall不等式, 周期域Fourier分析, 抛物PDE能量估计, M与N的符号关系]
- key_insight: 直接计算dN/dt被v=0边界项阻塞，但切换到M(t)=∫vρ dv（全平均）得到干净ODE dM/dt=u₀+u₁N-M，再用M≤N关闭Gronwall论证。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: direct_computation_of_N（直接计算N(t)的微分）
- translation_to: moment_method_via_M_with_Gronwall（通过辅助量M的矩方法+Gronwall不等式）
- translation_type: method_translation（方法翻译：从直接计算翻译到矩方法+不等式闭合）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: method_translation}
- tell_small_concepts: [moment substitution N to M, differential inequality Gronwall, Fourier decomposition on circle, energy estimate dissipation, boundary terms at v=0, M(t)<=N(t) closure]
- expected_ai_method: direct_calculation——AI会尝试直接计算dN/dt，在v=0半线边界项处受阻
- correct_method: continuous_analytic——定义辅助M(t)，分部积分得干净ODE，用M≤N关闭Gronwall，Fourier分解+能量估计证均匀分布

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？是，inequality_proof/direct_calculation/method_translation均可归入已有值。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？是，与已有值粒度一致。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？足够。本题的per-pair拓扑有变化（R1用structural_transformation, R3用method_translation, R4/R5用knowledge_gap），三维度能区分。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。

**拓扑进化建议**（如有）：无。已有拓扑分类足够。

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
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: AI会尝试直接计算dN/dt，在v=0半线边界项处受阻，不会想到定义辅助量M(t)。Part2可能不会想到Fourier分解或无法正确设置能量估计。
- suitable_for_poc: [method_translation POC: 测试N→M替换提示能否引导AI绕过边界项阻塞, knowledge_gap POC: 测试Gronwall闭合提示能否帮助AI完成发散证明, multi-step POC: 测试AI能否从Part1洞察延续到Part2 Fourier方法]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

已完成。profile.json已写入 `subagents-dirs/omni_math_000358/profile.json`。所有字段已逐项检查。

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
2. 更新`problem_extraction_progress`集合中`_key="330230"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_000358"
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
    '_key': '330230',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_000358',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_000358')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

- problem_id: omni_math_000358
- solution_method_type: continuous_analytic
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无，已有拓扑分类足够
- 是否遇到异常: problem.lean中Solution文本截断（在"Because M(t)≤N(t) a"处），根据标准PDE技术和Answer部分重构完整解答

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
