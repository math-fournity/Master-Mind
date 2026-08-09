# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003886
- **文件路径**: subagents-dirs/omni_math_003886/problem.lean
- **来源**: AoPS omni_math (imo)
- **ArangoDB progress记录_key**: 333765（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003886/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Determine all functions f:R→R satisfying f(x+f(x+y))+f(xy)=x+f(x+y)+yf(x) for all x,y∈R. (IMO 2015 P5)
- 解答核心思路（1-2句话）：通过特殊化代入(x=0,y=0,y=1等)推导f(0)∈{0,2}，再分两种情况利用不动点分析分别证明f(x)=2-x和f(x)=x。
- 解答关键步骤列表：
  1. P(0,0): f(f(0))=0
  2. P(0,f(0)): f(0)²=2f(0)，故f(0)=0或f(0)=2
  3. P(x,1): f(x+f(x+1))=x+f(x+1)，即x+f(x+1)是f的不动点
  4. Case f(0)=2: 任意不动点t满足P(0,t)→t=1，故x+f(x+1)=1→f(x)=2-x
  5. Case f(0)=0: P(x,0)→x+f(x)是不动点; P(x-1,1)→x-1+f(x)是不动点; P(1,-1),P(-1,1)→f(1)=1,f(-1)=-1; 证明f是奇函数; P(x,-x)与P(-x,x)联立→f(x)=x

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
| 1 | 纯元认知观察 | 0.7 | 观察这个函数方程f(x+f(x+y))+f(xy)=x+f(x+y)+yf(x)的结构，有哪些变量、哪些嵌套层次？哪些项是简单的，哪些是嵌套的？ | 方程有两个自由变量x,y。左侧f(x+f(x+y))是深层嵌套，f(xy)是中等复杂；右侧f(x+y)和yf(x)相对简单。嵌套核心在f(x+f(x+y))。 |
| 2 | 自由列举 | 0.6 | 对于这类函数方程，通常有哪些入手方向？请列出所有你能想到的方法。 | 特殊化代入(x=0,y=0,y=1等)；证明单射/满射；假设多项式形式代入；寻找不动点；变量替换；归纳法。 |
| 3 | 小尝试 | 0.4 | 假设f是线性函数f(x)=ax+b，代入方程试试，能找到什么候选解？ | 代入后匹配系数得a²=1，a=1时b=0→f(x)=x；a=-1时b=2→f(x)=2-x。两个候选解都满足方程，但线性假设无法证明这是全部解。 |
| 4 | 思维操作引导 | 0.3 | 代入x=0和y=0，分别能得到什么？再代入x=0,y=f(0)呢？ | P(0,0): f(f(0))=0。P(0,y): f(f(y))+f(0)=f(y)+yf(0)。P(0,f(0)): 利用f(f(0))=0得f(0)²=2f(0)，故f(0)=0或f(0)=2。 |
| 5 | 思维操作引导 | 0.3 | 代入y=1，能得到什么关于f的不动点的信息？ | P(x,1): f(x+f(x+1))+f(x)=x+f(x+1)+f(x)，故f(x+f(x+1))=x+f(x+1)。这意味着对所有x，x+f(x+1)是f的不动点。 |
| 6 | 思维操作引导 | 0.2 | 现在分两种情况讨论。f(0)=2时，不动点有什么性质？f(0)=0时呢？ | f(0)=2: 任意不动点t，P(0,t)给出t+2=3t故t=1，所有不动点为1。由R5，x+f(x+1)=1→f(x)=2-x。f(0)=0: P(x,0)→x+f(x)是不动点；P(x-1,1)→x-1+f(x)是不动点。需要更多工作。 |
| 7 | 能量传递引导 | 0.5 | f(0)=0的情况还需要证明f是奇函数才能完成。试试P(1,-1)和P(-1,1)，然后用P(x,-x)和P(-x,x)配合奇性来完成。 | P(1,-1),P(-1,1)→f(1)=1,f(-1)=-1。利用不动点性质证明f(-x)=-f(x)。然后P(x,-x): f(x)-f(x²)=x-xf(x)；P(-x,x): f(x)+f(x²)=x+xf(x)。两式相加得2f(x)=2x，故f(x)=x。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 3
- knowledge_rounds（思维操作引导的轮数）: 3
- level_sum: 3.0
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R7"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: 函数方程含嵌套f(x+f(x+y))，两个自由变量，需对f(0)分情况讨论，不动点分析是核心工具
- key_objects: ["函数方程", "不动点集", "特殊化代入", "f(0)分情况", "奇函数证明"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["specialization (特殊化代入)", "case analysis (分情况讨论)", "fixed point analysis (不动点分析)", "parity argument (奇函数证明)", "system of equations elimination (方程组消元)"]
- primary_pattern: specialization (特殊化代入)
- knowledge_required: ["函数方程技巧", "不动点概念", "分情况讨论", "奇函数性质", "线性假设验证"]
- key_insight: 代入y=1发现x+f(x+1)总是f的不动点，而f(0)的值(0或2)决定了不动点集的结构——f(0)=2时所有不动点为1直接给出f(x)=2-x，f(0)=0时不动点丰富需通过奇性证明完成

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: brute-force substitution exploration (暴力代入探索)
- translation_to: structured fixed-point analysis with case split (结构化不动点分析+分情况)
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "equation_solving", gap_type: "method_translation"}
- tell_small_concepts: ["specialization substitution", "fixed point set", "case split on f(0)", "odd function proof", "P(x,-x) parity"]
- expected_ai_method: 直接代入和代数操作，缺乏系统的不动点分析和分情况策略
- correct_method: 战略性特殊化代入后进行不动点分析并按f(0)分情况讨论

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——characterization/equation_solving/method_translation均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell和已有tell
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无，当前分类体系足够。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "marginal"
- bare_ai_error_prediction: AI很可能通过线性假设找到f(x)=x和f(x)=2-x两个候选解，但无法证明这是全部解；在f(0)=0的情况下可能卡在奇函数证明步骤，缺乏从不动点性质到奇性的桥梁
- suitable_for_poc: ["tell_hint_injection", "case_split_guidance", "fixed_point_analysis"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

profile.json已写入 `subagents-dirs/omni_math_003886/profile.json`

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: omni_math_003886
- solution_method_type: specialization_and_case_analysis
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，当前分类体系足够
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
