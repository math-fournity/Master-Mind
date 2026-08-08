# 启发规则图（heuristic-rule-graph）

## 定义
H图保存经过实验验证的"触发→激活"关系，每条规则形式化为(LHS, Guard, RHS)，附带适用信号、证书模板、失败案例和验证脚本。

## 来源
- 出处：pangu-b: 122v2-P13；fuxi: 248-P17

## 验证状态
[tested]
H图存储模块已实现（`xishujuzhen/research_runtime/hgraph/`），泛化验证通过。253号10个Q、数论案例6个Q、组合案例6个Q分别作为Pattern初始化到H图，全部published状态可被检索。LHS图模式定义覆盖3个领域（代数/分析、数论、组合/概率），node_types+feature双字段描述支持跨领域规则定义。泛化验证中3个案例的正确Q均被成功检索和选中。

## 架构位置
启发式干预的知识库。是pattern-matching和activation-score的数据源。

## 组合关系
- 连接到：thinking-trajectory-graph（LHS匹配T图）
- 包含了：待补充
- 被包含于：kth-three-graph-architecture（H图的实现）
- 约束于：pattern-lifecycle（规则必须经过生命周期验证）

## 检索流程角色
Pattern提取

## 系统演进角色
燧人

## 开放问题
规则数量增长后如何避免组合爆炸？Guard条件的形式化程度需要多高？
