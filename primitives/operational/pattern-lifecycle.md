# 规则生命周期（pattern-lifecycle）

## 定义
启发规则经历observed→candidate→intervened→validated→published→retired完整生命周期，每次状态转移需满足明确条件，candidate状态禁止在线匹配。

## 来源
- 出处：pangu-b: 122v2-P31；nuwa-a: 133-P30；nuwa-b: 176-P04；fuxi: 250-P13

## 验证状态
[partial]
生命周期管理模块已实现（`xishujuzhen/research_runtime/lifecycle/`），253号10个Q初始化为published。状态转移链observed→candidate→intervened→validated→published验证正确。

## 使用经验
定义状态枚举和转移条件。

## 组合关系
- 组合了：controlled-experiment, leakage-detection, activation-score
- 替代了：待补充
- 约束于：heuristic-rule-graph

## 检索流程角色
Pattern提取

## 系统演进角色
跨代

## 开放问题
candidate状态禁止在线匹配是否过于保守？retired状态的规则是否永久失效？
