# K/T/H三图架构（kth-three-graph-architecture）

## 定义
系统由三张图构成——K数学知识图、T外显思维图、H启发激活图，三图是投影而非独立真相库。

## 来源
- 出处：pangu-b: 122v2-P07；fuxi: 248-P3；nuwa-b: 174-P13；suiren: 213-P14

## 验证状态
[partial]
当前只有K图已实现，T/H图未实现。

## 架构位置
系统数据架构的核心框架。K图=dependency-graph，T图=thinking-trajectory-graph，H图=heuristic-rule-graph。

## 组合关系
- 连接到：待补充
- 包含了：dependency-graph, thinking-trajectory-graph, heuristic-rule-graph
- 被包含于：待补充
- 约束于：formalization-boundary概念

## 检索流程角色
知识悖论

## 系统演进角色
跨代

## 开放问题
三图之间的投影关系如何形式化？T图和H图未实现时，系统如何降级运行？
