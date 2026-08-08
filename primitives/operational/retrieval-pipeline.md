# 多级检索管线（retrieval-pipeline）

## 定义
多级递进检索机制——种子选择（层次索引定位+语义检索top-K）→图遍历扩展（BFS/DFS有界深度）→预算剪枝（深度/宽度/token控制）→返回结构化子图。

## 来源
- 出处：pangu-a: 63-P5；pangu-b: 100-P3；fuxi: 234-P10；nuwa-b: 166-P08

## 验证状态
[tested]
检索管线模块已实现（`xishujuzhen/research_runtime/retrieval/`），泛化验证通过。三级递进检索（种子选择→图遍历→预算剪枝）在3个领域均正确工作。253号A7验证Q8在top-5结果中；数论案例A3验证Q4在top-5（top-2）；组合案例A3验证Q4在top-5（top-1）。种子选择从前沿节点数学对象出发，activation-score粗筛+pattern-matching精排+预算剪枝的管线流程跨领域泛化。

## 使用经验
POC中用AQL图遍历查询实现，三级递进。种子选择和子图提取是管线的子组件。

## 组合关系
- 组合了：dependency-graph, layered-storage
- 替代了：全量扫描检索
- 约束于：budget-management（预算剪枝）

## 检索流程角色
状态感知 + Pattern提取

## 系统演进角色
盘古

## 开放问题
种子选择的质量如何评估？图遍历的深度/宽度预算如何自适应？
