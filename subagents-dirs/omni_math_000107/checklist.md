# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000107
- **文件路径**: subagents-dirs/omni_math_000107/problem.lean
- **来源**: AoPS omni_math (china_team_selection_test)
- **ArangoDB progress记录_key**: 329978（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000107/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：给定正整数a,b,c,p,q,r（p,q,r≥2），定义Q={(x,y,z)∈Z³: 0≤x≤a, 0≤y≤b, 0≤z≤c}。在Q的每个点上放若干棋子，共M个。三种操作：(1)从(x,y,z)移除p个，在(x-1,y,z)放1个；(2)移除q个放(x,y-1,z)；(3)移除r个放(x,y,z-1)。求最小M使得无论初始分布如何，总能通过操作在(0,0,0)放一个棋子。
- 解答核心思路（1-2句话）：下界用最不利分布（全放(a,b,c)）得p^a·q^b·r^c；上界用权函数w(x,y,z)=p^{-x}·q^{-y}·r^{-z}（操作不变量）+归纳法证明p^a·q^b·r^c个棋子总够。
- 解答关键步骤列表：
  1. 下界：所有M个棋子放在(a,b,c)，到(0,0,0)需p^a·q^b·r^c个
  2. 权函数构造：w(x,y,z)=p^{-x}·q^{-y}·r^{-z}，验证三种操作下守恒
  3. 总权值≥M·p^{-a}·q^{-b}·r^{-c}=1（当M=p^a·q^b·r^c时）
  4. 一维归纳：p^a个棋子在{0,...,a}上总能到达0（归纳于a）
  5. 三维推广：逐维消去——z维用r^c消去，y维用q^b消去，x维用p^a消去
  6. 下界=上界=p^a·q^b·r^c

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
| 1 | 纯元认知观察 | 0.8 | 描述题目结构：已知/未知/操作本质 | 识别三维格点pebbling，操作是k→1压缩 |
| 2 | 自由列举 | 0.7 | 列出所有可能方法方向 | 枚举/归纳/最不利/不变量/DP等 |
| 3 | 小尝试 | 0.3 | 尝试一维情形，求最小M | 猜p^a，归纳证明p^a个棋子够 |
| 4 | 思维操作引导 | 0.4 | 考虑最不利分布建立下界 | 全放(a,b,c)，需p^a·q^b·r^c |
| 5 | 思维操作引导 | 0.3 | 构造操作不变量权函数 | w=p^{-x}·q^{-y}·r^{-z}，守恒 |
| 6 | 推进 | 0.5 | 归纳证明上界，一维推广三维 | 逐维消去z→y→x |
| 7 | 能量传递引导 | 0.6 | 综合确认答案 | p^a·q^b·r^c |

**统计**：
- total_rounds: 7
- metacognitive_rounds: 4
- knowledge_rounds: 2
- level_sum: 3.6
- knowledge_bottleneck: R5
- thinking_bottleneck: R6

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: discrete_combinatorial
- structure_features: 三维整数格点上的棋子操作问题，三种操作沿坐标轴以不同压缩比率(p,q,r)移动棋子，求保证到达原点的最小棋子总数。图pebbling问题的三维推广。
- key_objects: 格点集合Q, 棋子分布, 三种压缩操作, 权函数w(x,y,z)=p^{-x}·q^{-y}·r^{-z}, 原点(0,0,0)

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["adversarial_argument", "invariant_construction", "induction_on_dimension", "reduction_to_simpler_case"]
- primary_pattern: invariant_construction
- knowledge_required: ["graph_pebbling", "weight_functions", "mathematical_induction", "extremal_arguments", "invariant_method"]
- key_insight: 构造权函数w(x,y,z)=p^{-x}·q^{-y}·r^{-z}作为操作不变量，将"能否到达原点"转化为"总权值是否>=1"，底数精确匹配操作压缩比率

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 组合操作语言（棋子在格点上以压缩比率移动）
- translation_to: 代数不变量语言（权函数守恒+归纳论证）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: discrete_combinatorial, ai_method_type: case_by_case, gap_type: knowledge_gap}
- tell_small_concepts: ["权函数", "操作不变量", "逐维归纳", "最不利分布", "压缩比率匹配", "p^{-x}·q^{-y}·r^{-z}"]
- expected_ai_method: 枚举小情况尝试找规律，可能猜到p^a·q^b·r^c但无法严格证明上界
- correct_method: 权函数不变量+逐维归纳：下界用最不利分布，上界用w=p^{-x}q^{-y}r^{-z}守恒+归纳

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——discrete_combinatorial/case_by_case/knowledge_gap均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell
- [ ] 不需要新维度

**拓扑进化建议**：无。已有拓扑分类足够。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: AI可能通过小案例猜到答案p^a·q^b·r^c，但无法严格证明上界。关键错误：不会构造权函数不变量w=p^{-x}q^{-y}r^{-z}，缺乏graph pebbling背景知识。可能尝试枚举或归纳但无法完成逐维推广的严格论证。
- suitable_for_poc: ["tell_hint_injection", "knowledge_bottleneck_identification", "invariant_construction_guidance"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

完整profile JSON已写入 `subagents-dirs/omni_math_000107/profile.json`。所有字段清单已逐项检查。

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

- problem_id: omni_math_000107
- solution_method_type: invariant_induction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，已有拓扑分类足够
- 是否遇到异常: problem.lean中solution文本被截断（仅18行），从标准graph pebbling论证重构solution_text

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
