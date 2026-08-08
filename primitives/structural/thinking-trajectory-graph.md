# 思维轨迹图（thinking-trajectory-graph）

## 定义
对Agent的当前思维过程建模为外显思维图T_t，节点有10种类型，是启发规则匹配的输入。

## 来源
- 出处：pangu-b: 122v2-P07；fuxi: 248-P3

## 验证状态
[partial]
设计完成，解析器原型已实现（`xishujuzhen/research_runtime/parser/`），用253号A7案例验证了从语义事件流构建10种节点类型的思维轨迹图。Mock LLM解析的节点结构和前沿节点标记测试通过。尚未接真实LLM验证。

## 架构位置
从Agent输出中解析事件构建图。是模式匹配和卡点检测的输入。

## 组合关系
- 连接到：event-sourcing（从事件流构建）
- 包含了：待补充
- 被包含于：kth-three-graph-architecture（T图的实现）
- 约束于：thinking-trajectory概念

## 检索流程角色
Pattern提取

## 系统演进角色
女娲

## 开放问题
10种节点类型是否完备？从自然语言推理输出中如何可靠解析为结构化图节点？
