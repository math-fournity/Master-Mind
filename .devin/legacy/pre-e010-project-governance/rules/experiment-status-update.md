---
description: >
  实验后设计元素验证状态更新触发规则。
  WHEN to use: 一个实验run完成并产出结果后，或用户要求更新验证状态时，
  触发 experiment-status-update skill，更新受影响原语的验证状态。
  WHEN NOT to use: 一般代码编写、非实验相关的更新、新增设计元素（用design-element-creation，待建）。
trigger: model_decision
---

# experiment-status-update rule

当以下场景发生时，触发设计元素验证状态更新：

## 触发条件

### 1. 实验run完成后
任何一次guided loop run或bare run结束后，更新受影响原语的验证状态。
- guided run：从引导者决策和Solver输出中识别测试了哪些原语
- bare run：从裸跑结果中识别AI自发使用了哪些原语（如base-change、constraint-solver-engine功能）

### 2. 用户要求更新验证状态
用户明确要求"更新验证状态"或"更新原语"时触发。

### 3. 实验结果修正后
如243号修正（实验解读的重大修正）发生后，需要重新评估受影响原语的验证状态。

## 更新执行

更新触发后，加载 `experiment-status-update` skill，按以下流程执行：
1. 识别实验测试了哪些原语（从run数据提取）
2. 对每个受影响的原语，判断验证状态变化
3. 更新原语文件的验证状态section
4. 更新使用经验/架构位置section
5. 更新 primitives/README.md 的验证状态分布统计
6. 如果实验结果影响面相理解，更新 facets/ 对应文件
7. commit

## 验证状态转换规则

| 当前状态 | 实验结果 | 新状态 |
|---|---|---|
| untested | 实验中用了且有效 | tested |
| untested | 实验中用了且无效 | tested_negative |
| untested | 效应存在但未证明核心声称 | partial |
| partial | 进一步实验证明核心声称 | tested |
| partial | 进一步实验否定核心声称 | tested_negative |
| tested | 保持，但可细化说明 | tested（更新使用经验） |
| tested_negative | 新实验证明其实关键 | tested（罕见，需充分证据） |

## 不做什么

- 不自动修改概念框架（concepts/）的"适用边界"——概念不需要验证状态
- 不自动修改性质标准（criteria/）——标准不需要验证状态
- 不因单次实验结果就大幅改写原语定义——定义是稳定的，验证状态是变化的
