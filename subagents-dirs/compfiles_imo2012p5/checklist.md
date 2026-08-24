# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2012p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2012P5.lean
- **来源**: IMO 2012 P5
- **ArangoDB progress记录_key**: 329223（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2012P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let ABC be a triangle with ∠BCA = 90°, D the foot of the altitude from C. X is a point in the interior of segment CD. K is on segment AX with BK = BC. L is on segment BX with AL = AC. M is the intersection of AL and BK. Show that MK = ML.
- 解答核心思路（1-2句话）：引入圆ωA(以A为圆心,半径AC)和ωB(以B为圆心,半径BC),定义K'和L'为AX/BX与ωB/ωA的第二交点,证明K,K',L',L'共圆,且MK和ML是该圆的切线,从而MK=ML。
- 解答关键步骤列表：
  1. C'是C关于AB的反射,在ωA和ωB上(反射保持到A和B的距离)
  2. X在C和C'之间(因为D是CC'中点且X在CD上)
  3. 由幂定理: KX·K'X = CX·C'X(对ωB), LX·L'X = CX·C'X(对ωA), 故KX·K'X = LX·L'X
  4. 由相交弦定理逆定理, K,K',L,L'共圆
  5. 由切线-割线关系: AC² = AK·AK'(从A到ωB,CA切线), 又AL=AC, 故AL²=AK·AK', 说明AL是共圆的切线
  6. 同理BK是共圆的切线
  7. M在两条切线上,切线长相等: MK = ML

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
| 1 | 纯元认知观察 | 0.2 | 观察这道题的结构。已知什么？要证明什么？关键的关系是什么？ | 已知直角三角形ABC(∠C=90°),D是C到AB的垂足,X在CD上。K在AX上且BK=BC,L在BX上且AL=AC。M是AL和BK的交点。要证明MK=ML。关键关系是BK=BC和AL=AC这两个等距约束,以及X在CD上的位置约束。 |
| 2 | 自由列举 | 0.5 | 要证明MK=ML,即M到K和L等距,有哪些可能的方向？ | (1)直接计算MK和ML的长度;(2)证明M在KL的垂直平分线上;(3)利用对称性;(4)引入辅助圆,证明MK和ML是某圆的切线(切线长相等);(5)利用相似三角形或全等三角形;(6)坐标几何方法。 |
| 3 | 小尝试 | 0.3 | 试试坐标几何方法,设C为原点,CA和CB为坐标轴,看看能否直接计算。 | 设C=(0,0),A=(a,0),B=(0,b)。D在AB上,X=(0,t)其中0<t<...。K在AX上且BK=BC=b,需要解方程组。L在BX上且AL=AC=a。计算变得非常复杂,参数太多,难以处理。这个方向看起来计算量太大。 |
| 4 | 思维操作引导 | 0.4 | 注意到BK=BC意味着K在以B为圆心、BC为半径的圆上,AL=AC意味着L在以A为圆心、AC为半径的圆上。这两个圆有什么特殊性质？特别是,∠BCA=90°这个条件与这两个圆有什么关系？ | 设ωB是以B为圆心、BC为半径的圆,ωA是以A为圆心、AC为半径的圆。因为∠BCA=90°,所以CA是ωB在C处的切线,CB是ωA在C处的切线。这是一个关键的结构——切线关系。 |
| 5 | 推进 | 0.4 | 既然CA切ωB于C,AX是ωB的割线(经过K),利用切线-割线定理能得出什么关系？类似地,对ωA呢？ | 对ωB:从A出发,CA是切线,AKK'是割线(K'是AX与ωB的第二交点),所以AC²=AK·AK'。对ωA:从B出发,CB是切线,BLL'是割线(L'是BX与ωA的第二交点),所以BC²=BL·BL'。又因为AL=AC和BK=BC,所以AL²=AK·AK',BK²=BL·BL'。 |
| 6 | 思维操作引导 | 0.5 | 现在考虑K,K',L,L'这四个点。能否证明它们共圆？提示:考虑X对ωB和ωA的幂,以及C关于AB的反射C'。 | C'是C关于AB的反射,因为D是C到AB的垂足且X在CD上,所以X在CC'上。C'在ωA上(因为反射保持到A的距离),也在ωB上(反射保持到B的距离)。由幂定理:KX·K'X=CX·C'X(对ωB),LX·L'X=CX·C'X(对ωA)。所以KX·K'X=LX·L'X,由相交弦定理的逆定理,K,K',L,L'共圆。 |
| 7 | 推进 | 0.4 | K,K',L,L'共圆于某圆s。现在利用AL²=AK·AK'和BK²=BL·BL',以及K,K'在s上,能得出什么关于AL和BK与圆s的关系？ | AL²=AK·AK',而K,K'在s上,A在KK'线上,所以AL的平方等于A对s的幂。这意味着AL是s在L处的切线。同理BK是s在K处的切线。M是AL和BK的交点,即M是s的两条切线的交点,所以MK=ML(从外点到圆的切线长相等)。 |
| 8 | 能量传递引导 | 0.6 | 完美！整个证明通过引入辅助圆,利用切线-割线定理和相交弦定理,最终归结为切线长相等。请总结这个证明的核心思路。 | 核心思路是"翻译到圆的语言":将BK=BC和AL=AC翻译为K在ωB上、L在ωA上,利用∠C=90°得到切线关系,通过反射C'和幂定理证明K,K',L,L'共圆,最后用切线-割线关系证明AL和BK是该圆的切线,从而MK=ML。 |

**统计**：
- total_rounds: 8
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.3
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

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
- problem_type: structural_existence
- structure_features: 直角三角形配置,垂足,内点,等距约束(BK=BC, AL=AC),交点等距结论(MK=ML)
- key_objects: 直角三角形ABC, 垂足D, 内点X, 等距点K和L, 交点M, 辅助圆ωA和ωB, 反射点C', 第二交点K'和L'

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["辅助圆引入", "切线-割线定理", "幂定理应用", "反射对称", "相交弦定理逆定理", "切线长相等"]
- primary_pattern: 辅助圆引入
- knowledge_required: ["切线-割线定理", "幂定理", "相交弦定理及其逆定理", "反射对称性", "切线长相等定理"]
- key_insight: 将BK=BC和AL=AC翻译为K在ωB上、L在ωA上,利用∠C=90°得到切线关系,通过反射C'和幂定理证明K,K',L,L'共圆,最终归结为切线长相等

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 距离等式语言(BK=BC, AL=AC, MK=ML)
- translation_to: 圆的几何语言(共圆, 切线, 幂, 割线)
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: method_translation}
- tell_small_concepts: ["辅助圆", "切线-割线定理", "幂定理", "相交弦定理逆定理", "反射点C'", "共圆", "切线长相等"]
- expected_ai_method: 坐标几何直接计算MK和ML的长度
- correct_method: 引入辅助圆ωA和ωB,利用切线-割线定理和幂定理证明K,K',L,L'共圆,再证明MK和ML是切线从而相等

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？是的,structural_existence + direct_calculation + method_translation可以描述这道题
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？是的,粒度一致
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？足够
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化

**拓扑进化建议**（如有）：无

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 8 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs详见profile.json中的tell_hint_pairs字段**
**全局pairs详见profile.json中的global_tell_hint_pairs字段**

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试坐标几何直接计算,陷入参数过多的代数运算中,无法发现辅助圆的翻译策略。即使想到引入圆,也难以独立发现反射点C'作为桥梁的技巧和相交弦定理逆定理的应用。
- suitable_for_poc: ["tell端验证——检测AI是否在R3坐标计算失败后识别出需要翻译到圆的语言", "hint端验证——注入辅助圆+切线的方向后AI能否完成证明"]
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

**将完整JSON写入工作目录的 `profile.json` 文件** ✅ 已写入

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
2. 更新`problem_extraction_progress`集合中`_key="329223"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2012p5"
   - extracted_by改为"subagent"

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2012p5')
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
- problem_id: compfiles_imo2012p5
- solution_method_type: auxiliary_circle_tangent
- 局部(tell,hint)对数量: 8
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无,现有拓扑分类(structural_existence + direct_calculation + method_translation)足够描述这道题
- 是否遇到异常: 无

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
