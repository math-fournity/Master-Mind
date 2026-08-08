# 事件溯源（event-sourcing）

## 定义
研究过程中的每一步都是不可变事件，在原始事件之上抽取语义事件（14种类型），系统状态是所有已发生事件的投影归约，事件一旦发生不可修改。

## 来源
- 出处：pangu-b: 123-P17；nuwa-a: 131-P3；fuxi: 250-P9；suiren: 202-P02

## 验证状态
[tested]
P0解析器原型实现（`xishujuzhen/research_runtime/parser/`），用GLM-5.2作为真实LLM解析253号A1-A10。6项准确率指标全部超过目标值：事件类型100%、数学对象100%、SymPy验证94.1%、六元组100%、前沿节点100%、卡点类型100%。14种语义事件类型在253号案例中验证了OBSERVATION/REPRESENTATION/RESOLUTION/CLAIM/STALL/VERIFICATION等类型。

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
