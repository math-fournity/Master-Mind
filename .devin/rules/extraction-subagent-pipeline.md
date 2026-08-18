---
description: >
  题海梳理Subagent流水线并发。题海梳理与数据基座建设中，Master Agent派发题目给subagent做QA序列分析和profile提取时。
  WHEN to use: 题海梳理subagent派发、QA序列分析、profile提取时。
  WHEN NOT to use: 非题海梳理的subagent使用。
trigger: model_decision
---

# 题海梳理 Subagent 流水线并发

**触发场景**：题海梳理与数据基座建设工作中，Master Agent 派发题目给 subagent 做 QA 序列分析和 profile 提取时。

## 硬约束

1. **最多 5 个 subagent 同时运行**——任何时刻并发 subagent 数不得超过 5。

2. **流水线并发，不是批处理并发**——始终保持 5 个 subagent 在运行。一个 subagent 完成了一道题，立刻启动下一个 subagent 处理下一道题，补满 5 个槽位。
   - ❌ 错误做法：启动 5 个 subagent，等 5 个都结束了再启动下一组 5 个——这浪费并发槽位（快的 subagent 结束后空等慢的）
   - ✅ 正确做法：任何时刻都有 5 个槽位在被使用。一个完成立刻补一个。

3. **Master Agent 绝对不要停下来汇报工作**——我们有海量的题目，没有完成这些题目之前，Master Agent 绝对不要停下来汇报工作。持续翻找剩余的最难的题目，继续派发工作给 subagent。
   - ❌ 错误做法：跑了 5 道题就停下来汇报"已完成 5 道，进度如下..."
   - ❌ 错误做法：等一组 5 个 subagent 都结束，汇报结果，再启动下一组
   - ✅ 正确做法：subagent 完成一个立刻补一个，Master Agent 持续翻找剩余的最难的题目派发，不停下来汇报，直到所有可处理的题目都处理完

4. **优先处理最难的题目**——"持续翻找剩余的最难的题目"：不是按顺序处理，而是优先派发难度最高的题目给 subagent。难题优先，因为难题的 (tell, hint) 对价值最高——bare AI 更可能在难题上走错路，走错路的分叉信号更有价值。

5. **subagent 三次失败后跳过，Master Agent 不得亲自分析**——如果同一道题的 subagent 连续 3 次失败（空通知、未入库、未写 profile.json 等），则：
   - 将该题记录到 `subagents-dirs/skipped-problems.md`，注明题目ID、失败次数、失败模式
   - 在 ArangoDB 的 `problem_extraction_progress` 中将该题标记为 `skipped`（不是 `completed`，也不是 `pending`）
   - **绝对不要由 Master Agent 亲自分析该题**——Master Agent 亲自做分析可能导致上下文过长、输出过载，进而导致 Master Agent 崩溃
   - 继续处理下一道题，不要在失败题目上纠缠
   - ❌ 错误做法：subagent 失败后 Master Agent 自己上手分析（fate_000283 就是先例，风险极高）
   - ✅ 正确做法：记录、跳过、继续流水线

## 为什么

- 题海规模是海量（AoPS-Instruct 60 万题），批处理并发会浪费大量等待时间
- 流水线并发最大化利用 5 个并发槽位，吞吐量最优
- Master Agent 停下来汇报会中断流水线，浪费槽位
- 难题的 (tell, hint) 对价值最高——bare AI 在难题上走错路的分叉信号比简单题更有教学价值

## 适用于

- 题海梳理与数据基座建设工作线（AGENTS.md §当前工作线：题海梳理与数据基座建设）
- 所有通过 `run_subagent` 启动的题海梳理 subagent
- Pass 1（探索性·发现维度）和 Pass 2（穷举性·完整标注）都适用

## 与 solver-concurrency 规则的关系

- `solver-concurrency.md`：Solver AI（devin cli 实例）最多 2 个并发——这是推理 AI 的约束
- 本规则：题海梳理 subagent 最多 5 个并发——这是提取 subagent 的约束
- 两者是不同场景的独立约束，互不影响
