# 审计标准回测（audit-standard-backtesting）

## 定义
用已知结果的历史run验证审计标准能否正确发现问题和正确判定通过——用已知失败run验证召回率，用已知通过run验证精确率。

## 来源
- 出处：nuwa-b: 196-P01

## 验证状态
[untested]
设计完成但未在真实回测中验证。

## 使用经验
用历史run回测审计标准。

## 组合关系
- 组合了：design-degradation-detection, trajectory-recording
- 替代了：___
- 约束于：___

## 检索流程角色
不直接服务于检索

## 系统演进角色
女娲

## 开放问题
历史run的代表性如何保证？召回率和精确率的平衡如何确定？
