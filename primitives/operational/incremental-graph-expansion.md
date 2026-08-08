# 增量图扩展（incremental-graph-expansion）

## 定义
在已有依赖图基础上新增节点和边，保留已有子图结构不变——而非重新设计。扩展时保留已验证的节点/意识，在新上下文中复用。

## 来源
- 出处：pangu-a: 64-P17, 65-P01

## 验证状态
[tested]
POC中多次使用。

## 使用经验
在ArangoDB中新增节点/边，标记新增vs复用。

## 组合关系
- 组合了：dependency-graph, multi-level-knowledge-extraction
- 替代了：待补充
- 约束于：data-pedestal（已有）

## 检索流程角色
状态感知

## 系统演进角色
盘古

## 开放问题
增量扩展时如何避免图膨胀？旧节点何时应该归档或删除？
