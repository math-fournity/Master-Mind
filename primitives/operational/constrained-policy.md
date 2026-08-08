# 受约束多目标策略（constrained-policy）

## 定义
策略π在进展最大化、泄漏最小化、依赖最小化、成本控制多个约束下选择最优动作，ABSTAIN（不干预）是合法选择，AI按需介入。

## 来源
- 出处：nuwa-a: 136-P32；suiren: 200-P23

## 验证状态
[tested]
受约束多目标策略模块已实现（`xishujuzhen/research_runtime/policy/`），泛化验证通过。253号A7端到端测试验证选中Q8而非Q9；数论案例A3验证选中Q4（Pareto最优：progress=1.0, leakage=0.14）；组合案例A3验证选中Q4（Pareto最优：progress=1.0, leakage=0.24）。义务ID匹配破解进展估计，Pareto最优选择在3个领域均正确。泛化改进：obligation匹配从仅open扩展为open+in_progress，支持更多案例的义务状态。

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
