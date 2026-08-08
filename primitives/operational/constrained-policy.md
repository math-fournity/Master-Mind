# 受约束多目标策略（constrained-policy）

## 定义
策略π在进展最大化、泄漏最小化、依赖最小化、成本控制多个约束下选择最优动作，ABSTAIN（不干预）是合法选择，AI按需介入。

## 来源
- 出处：nuwa-a: 136-P32；suiren: 200-P23

## 验证状态
[untested]
公式已定义但未在真实运行中验证。

## 使用经验
定义目标函数和约束，实现优化求解。

## 组合关系
- 组合了：progress-measurement, leakage-detection, budget-management
- 替代了：___
- 约束于：constraint-solver-engine（已有原语，受约束多目标策略是多约束求解的具体化）

## 检索流程角色
知识悖论

## 系统演进角色
伏羲

## 开放问题
多目标之间的权重如何确定？ABSTAIN的触发条件是什么？
