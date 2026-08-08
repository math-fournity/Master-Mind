# 激活分数（activation-score）

## 定义
在H图稀疏表示上计算候选激活分数a_t = W^T * p_t，权重组合7种数值维度，激活分数作为候选Pattern的排序依据。

## 来源
- 出处：nuwa-a: 135-P40；nuwa-b: 166-P16

## 验证状态
[partial]
激活分数模块已实现（`xishujuzhen/research_runtime/activation/`），253号A7验证Q8激活分数排top-3。7维特征提取和权重标定完成，但权重泛化性需后续验证。

## 使用经验
实现稀疏矩阵乘法。

## 组合关系
- 组合了：heuristic-rule-graph, pattern-lifecycle
- 替代了：待补充
- 约束于：cognitive-activation（已有原语，激活分数是认知激活的计算机制）

## 检索流程角色
Pattern提取

## 系统演进角色
女娲

## 开放问题
7种数值维度的权重如何确定？激活分数的阈值如何设定？
