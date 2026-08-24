# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000056
- **文件路径**: subagents-dirs/omni_math_000056/problem.lean
- **来源**: AoPS omni_math (china_team_selection_test)
- **ArangoDB progress记录_key**: 329927（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000056/problem.lean`

**产出**：
- 题目原文：求所有正整数a,b,c和素数p满足 2^a·p^b = (p+2)^c + 1
- 解答核心思路：用模4分析分层分情况(a>=2 vs a=1)，再用因式分解处理c奇数情况，用多模联合排除p=3子情况，最终c=1直接求解
- 解答关键步骤：1) p≠2(奇偶性) 2) a>=2: p≡1(mod4), c奇, p+3=2^m, 因式分解+模分析排除 3) a=1,c=1: 直接求解得(1,1,1,3) 4) a=1,c奇>=3: (p+3)|2p^b排除p≠3, p=3用模7模9联合排除 5) a=1,c偶>=2: 高斯整数排除
- 注：problem.lean中解答被截断(仅19行)，已根据数学分析重构完整解答

---

## Step 2: QA序列分析——局部视角7步 [x]

7轮QA已设计完成，详见profile.json的qa_sequence.rounds。

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.3 | 描述方程结构 | 识别指数丢番图方程，变量约束 |
| 2 | 自由列举 | 0.5 | 列出所有入手方向 | 模运算、因式分解、LTE、高斯整数等 |
| 3 | 小尝试 | 0.4 | 尝试p=2 | 奇偶性矛盾，p≠2 |
| 4 | 思维操作引导 | 0.6 | 模4分析分a=1/a>=2 | a>=2需p≡1(mod4)且c奇 |
| 5 | 思维操作引导 | 0.7 | c奇>=3用因式分解分析(p+3)|2p^b | p≠3时(p+3)|2矛盾，p=3需进一步 |
| 6 | 推进 | 0.6 | p=3用模7模9联合，c偶用高斯整数 | 多模联合排除所有c>=2 |
| 7 | 能量传递引导 | 0.4 | c=1直接求解 | p(2p^{b-1}-1)=3, p=3,b=1 |

**统计**：total_rounds=7, metacognitive_rounds=4, knowledge_rounds=2, level_sum=3.5, knowledge_bottleneck=R5, thinking_bottleneck=R6

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
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |

**统计**：
- total_rounds:
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）:
- knowledge_rounds（思维操作引导的轮数）:
- level_sum:
- knowledge_bottleneck（知识瓶颈在哪轮，或null）:
- thinking_bottleneck（思维瓶颈在哪轮，或null）:

---

## Step 3: 标注问题拓扑层 [x]

- problem_type: characterization
- structure_features: 指数丢番图方程，左边两个素数幂乘积，右边(p+2)幂加1，需多层级情况分析
- key_objects: 指数丢番图方程, 素数p, 模4分析, x^n+1因式分解, 模7与模9联合约束, 高斯整数, 整除性分析

---

## Step 4: 标注解答思维模式层 [x]

- thinking_patterns: [分情况讨论, 模分析分层排除, 因式分解降维, 多模联合约束, 奇偶性分析, 从特殊到一般]
- primary_pattern: 模分析分层排除
- knowledge_required: [模运算基本性质, x^n+1在n奇数时的因式分解, gcd与整除性, 二次剩余概念, 高斯整数基础, LTE引理（可选）]
- key_insight: 用模4分析将问题分裂为a>=2和a=1两大情况，再对a=1用x^n+1因式分解将c奇数情况转化为整除性问题(p+3)|2p^b，从而大幅缩小搜索空间

---

## Step 5: 标注翻译方向层 [x]

- translation_from: 枚举搜索/直接计算
- translation_to: 模分析+因式分解分层排除
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑
- tell_topology: {problem_type: characterization, ai_method_type: enumeration_brute_force, gap_type: method_translation}
- tell_small_concepts: [指数丢番图方程, 模4分析, 因式分解x^n+1, 整除性分析, 模7模9联合, 高斯整数, 奇偶分析, 素数约束]
- expected_ai_method: bare AI会尝试枚举小值找解，可能找到(1,1,1,3)但无法系统证明唯一性
- correct_method: 用模4分析分层分情况，再用因式分解处理c奇数情况，用多模联合排除p=3子情况

### 6b. 反思拓扑分类
- [x] 当前拓扑分类够用——problem_type=characterization, ai_method_type=enumeration_brute_force, gap_type=method_translation均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分——无需新维度
- 拓扑进化建议：无

---

## Step 7: 提取(tell, hint)对 [x]

- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个
- 每个pair均含tell_topology和tell_small_concepts，详见profile.json

---

## Step 8: 标注实验适用性层 [x]

- bare_ai_expected: fail
- bare_ai_error_prediction: bare AI可能枚举小值找到(1,1,1,3)但无法系统证明唯一性；或尝试直接代数变形但不知如何用模4分层分情况；在p=3,c奇>=3子情况中不知道需要模7模9联合排除
- suitable_for_poc: [tell_degeneralization, multi_modular_combination, case_tree_structure_visibility]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

完整profile JSON已写入 `subagents-dirs/omni_math_000056/profile.json`。所有字段均已包含并通过验证。

---

## Step 10: 入库ArangoDB [x]

- 入库结果: [x] 成功
- 验证结果: [x] 通过（7 local pairs, 2 global pairs, tell_topology/tell_small_concepts/why_not_visible_locally均存在）

---

## Step 11: 汇报 [x]

- problem_id: omni_math_000056
- solution_method_type: modular_arithmetic_case_analysis
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，已有拓扑分类足够
- 是否遇到异常: problem.lean中解答被截断(仅19行)，已根据数学分析重构完整解答

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
