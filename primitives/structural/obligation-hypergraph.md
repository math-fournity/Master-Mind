# 义务超图（obligation-hypergraph）

## 定义
开放义务用AND/OR有向超图表达——AND约束（所有子目标都必须解决）、OR约束（任一路径成功即可），义务有10种类型和4种状态。

## 来源
- 出处：pangu-b: 123-P12；nuwa-a: 132-P7；nuwa-b: 188-P06；fuxi: 250-P12

## 验证状态
[partial]
代码已实现并集成测试通过。

## 架构位置
进展度量和动态工作区的核心组件。在ArangoDB中创建超边本体和participant edges。

## 组合关系
- 连接到：event-sourcing（从事件流更新义务状态）
- 包含了：待补充
- 被包含于：dynamic-workspace（O_t字段）
- 约束于：evidence-system

## 检索流程角色
状态感知

## 系统演进角色
伏羲

## 开放问题
AND/OR嵌套深度是否有上限？义务状态转移的条件是否需要形式化验证？
