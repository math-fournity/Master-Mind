# 角色隔离矩阵（role-isolation-matrix）

## 定义
系统功能拆分为8个隔离角色，每个角色有明确的职责和权限边界，通过可见性标签+能力令牌+物理隔离等机制在代码层面强制执行角色间的信息隔离，防止审计者与被审计者耦合。

## 来源
- 出处：pangu-a: 78-P11；pangu-b: 116-P4；nuwa-b: 176-P07；fuxi: 250-P20；suiren: 215-P17

## 验证状态
[partial]
POC中用物理目录+AGENTS.md实现了简化版。

## 架构位置
交叉审计、真值保险库、受控实验的角色隔离基础设施。定义角色枚举、可见性矩阵、capability token验证逻辑。

## 组合关系
- 连接到：truth-vault, cross-audit-loop, controlled-experiment
- 包含了：待补充
- 被包含于：待补充
- 约束于：pipe（已有原语，角色间信息隔离是Pipe合法性的保障）

## 检索流程角色
知识悖论

## 系统演进角色
女娲

## 开放问题
8个角色是否都必要？简化场景下可以合并哪些角色？capability token的颁发和撤销机制如何设计？
