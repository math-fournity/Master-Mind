# 真值保险库（truth-vault）

## 定义
将正确答案和完整证明存储在隔离的truth_vault collection中，写入仅truth_curator，读取仅auditor，其他角色无权访问。

## 来源
- 出处：pangu-b: 122v3-P05；nuwa-a: 131-P24；fuxi: 248-P19；suiren: 200-P2

## 验证状态
[partial]
代码已实现但未在真实多角色运行中验证。

## 架构位置
泄漏检测的基础防线。通过role-isolation-matrix的capability token控制访问。

## 组合关系
- 连接到：role-isolation-matrix（权限控制）
- 包含了：待补充
- 被包含于：待补充
- 约束于：role-isolation-matrix

## 检索流程角色
知识悖论

## 系统演进角色
女娲

## 开放问题
多角色运行时如何验证权限隔离确实生效？truth_curator角色由谁担任？
