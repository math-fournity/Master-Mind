# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000310
- **文件路径**: subagents-dirs/fate_000310/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396420（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000310/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设 R → S 是环映射，I ⊂ R 是理想，满足：(1) I²=0，(2) R→S 平坦，(3) R/I → S/IS 形式光滑。证明 R→S 形式光滑。
- 解答核心思路（1-2句话）：利用形式光滑的无穷小提升性质，将提升问题分解为商层面的提升（用 R/I→S/IS 的形式光滑性）和从商到原环的扩张（用平坦性和 I²=0 消除障碍）。
- 解答关键步骤列表：
  1. 回顾形式光滑 = 对平方零扩张的无穷小提升性质
  2. 设定提升问题：给定平方零扩张 T→T/J 和映射 S→T/J，需构造提升 S→T
  3. 利用 I²=0 使 I 成为平方零理想，R→R/I 是平方零扩张
  4. 利用平坦性得 S/IS ≅ S⊗_R R/I，将提升问题转化到商层面
  5. 用 R/I→S/IS 的形式光滑性在商层面获得提升
  6. 用平坦性和 I²=0 消除从 S/IS 提升到 S 的障碍
  7. 组合得到 S→T 的提升， conclude R→S 形式光滑

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：有哪些假设条件？需要证明什么？各条件之间有什么潜在联系？ | 题目有环映射R→S、理想I满足I²=0、R→S平坦、R/I→S/IS形式光滑。需证R→S形式光滑。关键联系：I²=0是平方零条件，平坦性给出S/IS≅S⊗_R R/I，形式光滑可传递。 |
| 2 | 自由列举 | 0.7 | 列出证明环映射形式光滑的所有可能方法。 | 1)无穷小提升性质（定义）；2)余切复形刻画；3)Jacobian准则；4)局部形式光滑准则；5)形式光滑的传递性；6)直接用定义验证提升性质。 |
| 3 | 小尝试 | 0.4 | 尝试用Jacobian准则来证明。会遇到什么困难？ | Jacobian准则要求S是R上有限表示代数且有具体表示，但题目没有给出S的表示。无法直接计算Jacobian矩阵，此路不通。 |
| 4 | 思维操作引导 | 0.3 | 用无穷小提升性质的定义：给定平方零扩张T→T/J和映射S→T/J，写出需要构造什么，以及从假设中能得到什么信息。 | 需构造提升S→T。从R→S→T/J和R-代数结构R→T得到交换图。I在T中的像α(I)满足α(I)²=0（因I²=0）。需要利用商的信息来辅助构造。 |
| 5 | 思维操作引导 | 0.3 | I²=0意味着I是平方零理想，R→R/I是平方零扩张。如何利用这个事实和R/I→S/IS的形式光滑性来获得商层面的提升？ | 因I²=0，R→R/I是平方零扩张。平坦性给出S/IS≅S⊗_R R/I。将提升问题限制到商：S/IS→T/J可用R/I→S/IS的形式光滑性提升到S/IS→T（需处理I在T中的像）。 |
| 6 | 推进 | 0.4 | 现在有了商层面的提升S/IS→T。如何用平坦性将其扩展为完整的提升S→T？障碍在哪里？I²=0如何消除障碍？ | 障碍在于从S/IS到S的"加厚"。平坦性确保S是R上平坦的，相关正合列保持正合。障碍模涉及I，而I²=0使得障碍映射的合成因子通过I/I²=I/0=I，平方零条件杀死高阶障碍，使提升存在。 |
| 7 | 能量传递引导 | 0.6 | 组合所有部分：商层面提升（形式光滑性）+扩展（平坦性）+障碍消除（I²=0），写出完整结论。 | 综合三步：(1)形式光滑性给出S/IS层面的提升，(2)平坦性将问题转化为张量积关系使扩展可行，(3)I²=0消除扩展障碍。因此S→T的提升存在，R→S满足无穷小提升性质，故形式光滑。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.5
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence
- structure_features: 环映射的形式光滑性证明，通过无穷小提升性质（存在性证明）实现。核心结构是将提升问题分解为商层面和扩张层面两个子问题。
- key_objects: ["环映射R→S", "平方零理想I（I²=0）", "商环R/I和S/IS", "形式光滑性", "平坦性", "无穷小提升性质", "平方零扩张T→T/J"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["分解策略（将提升问题分为商层面+扩张层面）", "商归约（利用R/I→S/IS的形式光滑性）", "障碍分析（分析提升障碍模并用I²=0消除）", "假设利用（将I²=0识别为平方零扩张条件）"]
- primary_pattern: 商归约
- knowledge_required: ["形式光滑性的无穷小提升性质定义", "平坦性与张量积的关系", "平方零理想与平方零扩张", "局部形式光滑准则", "障碍模理论"]
- key_insight: I²=0使I成为平方零理想，R→R/I是平方零扩张——这恰好与形式光滑性定义中的平方零扩张对接，使商层面的形式光滑性可以"提升"回原环。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 抽象的形式光滑性定义（无穷小提升性质）
- translation_to: 具体的提升问题分解（商层面提升+扩张层面障碍消除）
- translation_type: structural_transformation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "direct_manipulation", gap_type: "knowledge_gap"}
- tell_small_concepts: ["形式光滑性", "无穷小提升性质", "平方零理想", "I²=0", "平坦性", "商归约", "障碍模"]
- expected_ai_method: bare AI会尝试直接操作定义或用Jacobian准则，但缺乏对"局部形式光滑准则"这一关键定理的知识
- correct_method: 利用无穷小提升性质定义，将提升问题分解为商层面（形式光滑性）和扩张层面（平坦性+I²=0消除障碍）

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——structural_existence/direct_manipulation/knowledge_gap可以归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。已有拓扑分类足够。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

局部pairs详见profile.json中的tell_hint_pairs字段。
全局pairs详见profile.json中的global_tell_hint_pairs字段。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试用Jacobian准则或直接操作定义，但缺乏"局部形式光滑准则"的知识——不知道如何将I²=0与平方零扩张联系起来，也不知道如何用平坦性消除提升障碍。很可能在设定提升问题后卡住，无法看到商归约的分解策略。
- suitable_for_poc: ["POC-VMS-8（脉络继承+方向注入验证）", "POC-VMS-9（tell去特化验证）", "POC-VMS-10（小概念标记分辨验证）"]
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

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: fate_000310
- solution_method_type: logical_deduction（无穷小提升性质+商归约分解）
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature + 1个implicit）
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，已有拓扑分类足够
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
