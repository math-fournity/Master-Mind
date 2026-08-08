# 受控对照实验（controlled-experiment）

## 定义
设置对照组和实验组在相同隔离条件下并行执行，通过组间差异量化因果效果——A/B对照、三组对照、双路线对照、检查点分层因果实验。

## 来源
- 出处：pangu-b: 100-P15；suiren: 200-P28；fuxi: 229-P4；nuwa-a: 134-P2

## 验证状态
[tested]
POC-1/3/4/5/6多次使用。

## 使用经验
设置隔离环境，并行执行，计算组间差异。POC中多次使用。

## 组合关系
- 组合了：role-isolation-matrix, checkpoint, hypothesis-driven-validation
- 替代了：待补充
- 约束于：execution-contract（已有原语，Phase门控是执行契约的验证机制）

## 检索流程角色
不直接服务于检索

## 系统演进角色
跨代

## 开放问题
隔离条件的严格性如何保证？组间差异的统计显著性如何判定？
