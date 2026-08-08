# 遗留处理（legacy-handling）

## 定义
旧数据和概念不原地清空或迁移，保留原貌作为只读历史数据，通过只读adapter访问，新数据写入新collection。

## 来源
- 出处：pangu-b: 121-P16；nuwa-b: 166-P35

## 验证状态
[tested]
Phase 0冻结旧数据后验证有效。

## 使用经验
创建只读adapter，新collection用幂等可回滚migration。

## 组合关系
- 组合了：phase-gate
- 替代了：___
- 约束于：___

## 检索流程角色
不直接服务于检索

## 系统演进角色
跨代

## 开放问题
只读adapter的性能开销如何？旧数据的保留期限如何确定？
