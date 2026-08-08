# 事件溯源（event-sourcing）

## 定义
研究过程中的每一步都是不可变事件，在原始事件之上抽取语义事件（14种类型），系统状态是所有已发生事件的投影归约，事件一旦发生不可修改。

## 来源
- 出处：pangu-b: 123-P17；nuwa-a: 131-P3；fuxi: 250-P9；suiren: 202-P02

## 验证状态
[partial]
设计完成，解析器原型已实现（`xishujuzhen/research_runtime/parser/`），用253号A7案例验证了从自然语言推理输出到14种语义事件类型的解析。Mock LLM+SymPy验证的混合架构测试通过。尚未接真实LLM验证解析准确率。

## 架构位置
不可变事件流，是动态工作区、思维轨迹图、检查点的基础设施。

## 组合关系
- 连接到：dynamic-workspace, thinking-trajectory-graph, checkpoint, trajectory-recording
- 包含了：待补充
- 被包含于：待补充
- 约束于：不可变性（immutability）概念

## 检索流程角色
状态感知

## 系统演进角色
女娲

## 开放问题
14种语义事件类型是否完备？事件流增长后如何做快照压缩？
