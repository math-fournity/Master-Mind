# 进展度量（progress-measurement）

## 定义
进展由5个可测量分量定义的偏序P_κ(S_t)，不同任务类型有不同权重，进展向量比较产生4种结果。

## 来源
- 出处：pangu-b: 123-P21；nuwa-a: 132-P22；nuwa-b: 188-P03

## 验证状态
[untested]
设计完成但未在真实运行中验证。

## 使用经验
从动态工作区提取5个分量，计算偏序。

## 组合关系
- 组合了：dynamic-workspace, obligation-hypergraph, evidence-system
- 替代了：___
- 约束于：constrained-policy

## 检索流程角色
状态感知

## 系统演进角色
伏羲

## 开放问题
5个可测量分量是否完备？不同任务类型的权重如何确定？
