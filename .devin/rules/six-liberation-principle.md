---
description: >
  解放思想原则。设计或修改six/中任何函数时。
  WHEN to use: 设计或修改six/中任何函数时。
  WHEN NOT to use: 不涉及six/中函数设计的操作。
trigger: model_decision
---

# 解放思想原则

**触发条件**：设计或修改six/中任何函数时。
**来源文档**：318号、`six/principles.py`

## 规则

设计或修改任何函数时，时时考虑三个维度：

1. **多种方式**——同一个函数可以用多种方式实现，用POC验证决定哪种方式可行（如VMS-28/29/30验证三种格化方式）
2. **多个AI**——同一个函数可以由多个AI实例并发执行（如311号的并发Telling AI）
3. **多个子pipe**——一个函数可以进一步迭代，拆分为多个子函数，每个子pipe独立验证、独立实现（如`pipe_1_parser()`可拆为`step_1_analyze_vein()` + `step_2_grid_vein()` + `step_3_identify_traces()`三个子pipe）

如果某种维度适用，在`principles.py`中记录决策，在函数docstring中标注。
