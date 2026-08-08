# 检查点（checkpoint）

## 定义
用SHA-256内容哈希标识状态快照，相同内容产生相同哈希使状态可去重和精确引用。提示后从当前checkpoint继续而非从原题重做。

## 来源
- 出处：pangu-b: 122v2-P37；nuwa-a: 131-P9；fuxi: 251-P12

## 验证状态
[untested]
设计了完整机制但未在因果实验中验证。

## 架构位置
受控实验和反应式救援的状态管理基础设施。计算状态哈希，存储checkpoint快照。

## 组合关系
- 连接到：event-sourcing（从事件流生成快照）
- 包含了：待补充
- 被包含于：待补充
- 约束于：backtrack-fresh-session（已有原语，checkpoint续行是回溯的具体实现）

## 检索流程角色
状态感知

## 系统演进角色
女娲

## 开放问题
状态哈希的粒度如何选择——整个session还是单步？checkpoint存储增长如何管理？
