# 拓扑覆盖验证（topology-coverage-verification）

## 定义
构造拓扑骨架G'_topo，用AQL集合差集验证覆盖所有节点/边/跨领域边/螺旋环路圈数——差集为空即100%覆盖。

## 来源
- 出处：pangu-a: 78-P9；fuxi: 248-P6

## 验证状态
[tested]
POC中多次使用TopologyVerifier。

## 使用经验
用AQL集合差集运算实现，在POC-1/3/4/5/6中多次使用。

## 组合关系
- 组合了：dependency-graph
- 替代了：待补充
- 约束于：data-pedestal（已有）

## 检索流程角色
不直接服务于检索

## 系统演进角色
盘古

## 开放问题
拓扑骨架的构造是否自动化？覆盖100%是否是必要标准？
