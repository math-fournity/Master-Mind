# 版本链（version-chain）

## 定义
认知单元的演化历史——有序版本序列，每个版本记录来源和验证结果，current_version指针指向最新版本。

## 来源
- 出处：pangu-a: 89-P15；pangu-b: 100-P6；fuxi: 249-P30

## 验证状态
[tested]
POC中已实现，在ArangoDB中创建cog_versions集合和版本链边。

## 架构位置
认知演化的基础设施。挂在dependency-graph的节点上。

## 组合关系
- 连接到：dependency-graph（版本链依附于依赖图节点）
- 包含了：待补充
- 被包含于：dependency-graph
- 约束于：data-pedestal

## 检索流程角色
状态感知

## 系统演进角色
盘古

## 开放问题
版本冲突时如何合并？多来源版本如何追溯？
