# 依赖图（dependency-graph）

## 定义
用有向图表示知识间的依赖关系——节点带类型、上下文元数据、知识内容、版本指针；边带类型（depends_on/calls/cross-domain）；可有跨域边和螺旋环路。用ArangoDB图数据库存储。

## 来源
- 出处：pangu-a: 63-P1, 68-P1；pangu-b: 100-P18, 103-P1；fuxi: 223-P8, 248-P2

## 验证状态
[tested]
POC-1/3/4/5/6中B组引用了依赖图结构，A/B对照验证增量。

## 架构位置
检索、验证、提取等所有上层原语的存储基础设施。用ArangoDB创建节点和边集合，AQL查询遍历。

## 组合关系
- 连接到：layered-storage（分级存储的后端数据结构）
- 包含了：version-chain（版本链是依赖图中节点的演化历史）
- 被包含于：kth-three-graph-architecture（K图的实现）
- 约束于：data-pedestal（已有原语，依赖图是数据基座的存储实现）

## 检索流程角色
状态感知

## 系统演进角色
盘古

## 开放问题
跨域边的语义是否需要统一编码？螺旋环路在检索时如何处理（是障碍还是线索）？
