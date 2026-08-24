# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: matharena_MathArena_hmmt_feb_2025_0029
- **文件路径**: subagents-dirs/matharena_MathArena_hmmt_feb_2025_0029/problem.lean
- **来源**: MathArena MathArena_hmmt_feb_2025
- **ArangoDB progress记录_key**: 329701（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/matharena_MathArena_hmmt_feb_2025_0029/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：A plane P intersects a rectangular prism at a hexagon which has side lengths 45,66,63,55,54,77 in that order. Compute the distance from the center of the rectangular prism to plane P.
- 解答核心思路（1-2句话）：设长方体为[0,a]×[0,b]×[0,c]，平面为lx+my+nz=d。六边形三对对边平行，分别对应三对对面。由对边比值推出la=mb=nc=K，d=31K/20；由对边之和建立三个方程解出l,m,n比例关系，最终距离=K/(20√(l²+m²+n²))=√(95/24)。
- 解答关键步骤列表：
  1. 建立坐标系，长方体[0,a]×[0,b]×[0,c]，平面lx+my+nz=d（l,m,n>0）
  2. 确定六边形六个顶点在棱上的位置，计算六条边长公式
  3. 识别三对对边：(s1,s4),(s2,s5),(s3,s6)分别对应x面、z面、y面对
  4. 由对边比值s1/s4=9/11, s2/s5=11/9, s3/s6=9/11推出la=mb=nc=K, d=31K/20
  5. 由对边之和100,120,140建立K·√(m²+n²)/(mn)=100等三个方程
  6. 解方程组得m²/n²=19/6, l²/n²=19/30, K²=7600n², l²+m²+n²=24n²/5
  7. 距离=|3K/2-31K/20|/√(l²+m²+n²)=K/(20√(l²+m²+n²))=√(95/24)

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**每轮必须标注**：
- **question**：给AI的提示/问题（Q）
- **expected_answer**：预期回复（A）
- **situation_type**：**⚠️ 只能取以下6个值之一，禁止自创**
- **level**：**⚠️ 必须是0-1之间的浮点数**

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.7 | 题目给出了什么？一个平面截长方体得到六边形，六条边长已知，要求长方体中心到平面的距离。请描述这个几何构型的结构特征——六边形的边和长方体的面之间有什么关系？ | 六边形是平面与长方体六个面的交线段组成。长方体有三对平行对面，每对对面产生一对平行边，所以六边形有三对平行对边。 |
| 2 | 自由列举 | 0.6 | 要从六边形边长求中心到平面距离，有哪些可能的方向？列出你能想到的所有方法。 | 方向包括：①建坐标系直接计算边长公式再反解；②用体积/面积关系；③利用对边平行性质找比例关系；④用仿射变换化简；⑤用对角线或对称性。 |
| 3 | 小尝试 | 0.4 | 试试方向③：六条边长45,66,63,55,54,77按顺序排列，三对对边分别是哪两条？它们的比值有什么规律？ | 对边是(s1,s4)=(45,55), (s2,s5)=(66,54), (s3,s6)=(63,77)。比值：45/55=9/11, 66/54=11/9, 63/77=9/11。两个比值相同是9/11，一个是11/9。 |
| 4 | 思维操作引导 | 0.3 | 设长方体[0,a]×[0,b]×[0,c]，平面lx+my+nz=d。建立坐标系，计算六条边长用l,m,n,a,b,c,d表示。然后利用对边比值，你能推出什么约束？ | 计算得s1=(mb+nc-d)√(m²+n²)/(mn)等。由三个比值方程联立，推出la=mb=nc=K，且d=31K/20。这是关键约束——平面法向量与棱长乘积相等。 |
| 5 | 思维操作引导 | 0.3 | 现在la=mb=nc=K，d=31K/20。利用对边之和（100,120,140）建立三个方程，解出l,m,n之间的比例关系和K的值。 | 三个方程：K√(m²+n²)/(mn)=100, K√(l²+m²)/(lm)=120, K√(l²+n²)/(ln)=140。设p=l²,q=m²,r=n²，解得q/r=19/6, p/r=19/30, K²=7600r, l²+m²+n²=24r/5。 |
| 6 | 推进 | 0.5 | 有了K²=7600n²和l²+m²+n²=24n²/5，计算中心(a/2,b/2,c/2)到平面的距离。 | 距离=|l·a/2+m·b/2+n·c/2-d|/√(l²+m²+n²)=|3K/2-31K/20|/√(l²+m²+n²)=K/(20√(l²+m²+n²))=√(7600n²/(400·24n²/5))=√(95/24)。 |
| 7 | 能量传递引导 | 0.8 | 你已经完成了所有关键计算。确认最终答案，检查每一步的逻辑是否自洽。 | 答案是√(95/24)。验证：对边比值约束→la=mb=nc，对边之和约束→l,m,n比例，距离公式→√(95/24)。逻辑链完整自洽。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.7+0.6+0.4+0.3+0.3+0.5+0.8=3.6
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R3"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: constraint_satisfaction
- structure_features: 平面截长方体产生六边形，六条边长作为约束条件，需反解长方体参数和平面位置。三对对边平行，对边比值和对边之和提供两组独立约束。
- key_objects: 长方体(rectangular prism)、平面(plane)、截面六边形(hexagon cross-section)、对边平行对(opposite side pairs)、中心到平面距离(distance from center to plane)

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: [坐标化建模, 对边比值模式识别, 约束消元, 代数方程组求解, 距离公式应用]
- primary_pattern: 对边比值模式识别（从对边比值中识别出la=mb=nc的隐藏对称性是解题的核心转折）
- knowledge_required: [平面截长方体的截面几何, 六边形对边平行性质, 坐标系中点到平面距离公式, 多变量代数方程组求解]
- key_insight: 六边形对边比值9/11和11/9不是偶然的——它们编码了la=mb=nc这一隐藏对称性，将6个未知数压缩为1个参数K，使问题可解。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 几何直观（平面截长方体的截面六边形边长）
- translation_to: 代数方程组（坐标系参数化+对边比值/和约束+距离公式）
- translation_type: structural_transformation（将几何构型翻译为代数约束系统，关键在于识别对边比值编码的隐藏对称性）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "constraint_satisfaction", ai_method_type: "direct_calculation", gap_type: "structural_transformation"}
- tell_small_concepts: ["对边平行对", "对边比值", "隐藏对称性la=mb=nc", "对边之和约束", "坐标参数化边长公式", "距离公式"]
- expected_ai_method: bare AI会尝试直接建坐标系计算边长公式，但面对6个未知数(a,b,c,l,m,n,d)的复杂方程组会陷入代数泥潭，不会注意到对边比值的模式。
- correct_method: 先识别对边比值模式→推出la=mb=nc对称性→消元简化→解缩减后的方程组→套距离公式。

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——constraint_satisfaction/direct_calculation/structural_transformation能准确描述这道题的tell
- [x] 粒度一致——与已有值粒度统一
- [x] 不需要新维度——三维度足够区分
- [ ] 无需进化建议

**拓扑进化建议**（如有）：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

局部pairs详见profile.json。

全局pairs：
1. path_feature型：对边比值编码隐藏对称性——完整路径上"先比值后求和"的顺序是关键路径特征，局部视角只看到比值或只看到和，看不到两者的配合关系。
2. implicit型：la=mb=nc这一约束蕴含在三个对边比值的联立中，任何单个比值方程都看不出这个结论，必须三个同时成立才能推出。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会建坐标系尝试直接计算，但面对6个未知数和复杂的边长公式会陷入代数运算泥潭。关键错误是不会先检查对边比值的模式（9/11, 11/9, 9/11），而是试图暴力求解所有方程，导致方程组过于复杂无法推进。
- suitable_for_poc: ["POC-VMS-hint-injection", "POC-VMS-tell-detection", "POC-VMS-pattern-recognition"]
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
- [x] answer（√(95/24)）
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
- [x] tell_hint_pairs（7个，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（2个，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**将完整JSON写入工作目录的 `profile.json` 文件** ✅

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: matharena_MathArena_hmmt_feb_2025_0029
- solution_method_type: coordinate_parametrization_with_pattern_recognition
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否（constraint_satisfaction/direct_calculation/structural_transformation 三维度足够）
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
