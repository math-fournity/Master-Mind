# 假设驱动验证（hypothesis-driven-validation）

## 定义
实验前预设明确假设并冻结所有决策参数，冻结后不可回改，用ATE+CI下界+passes_exit_gate三步验证因果效应。

## 来源
- 出处：pangu-b: 106-P21；nuwa-a: 134-P8；nuwa-b: 174-P05

## 验证状态
[tested]
POC-1/3/4/5/6均使用。

## 使用经验
创建预注册文档，冻结参数。POC中多次使用。

## 组合关系
- 组合了：待补充
- 替代了：待补充
- 约束于：controlled-experiment

## 检索流程角色
不直接服务于检索

## 系统演进角色
跨代

## 开放问题
参数冻结后如果发现设计缺陷如何处理？ATE+CI下界的置信水平如何选择？
