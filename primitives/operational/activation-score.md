# 激活分数（activation-score）

## 定义
在H图稀疏表示上计算候选激活分数a_t = W^T * p_t，权重组合7种数值维度，激活分数作为候选Pattern的排序依据。

## 来源
- 出处：nuwa-a: 135-P40；nuwa-b: 166-P16

## 验证状态
[tested]
激活分数模块已实现（`xishujuzhen/research_runtime/activation/`），泛化验证通过。253号A7验证Q8激活分数排top-3（score=2.0）；数论案例A3验证Q4排top-3（score=4.0，top-2）；组合案例A3验证Q4排top-3（score=4.0，top-1）。7维特征提取和权重标定完成，泛化关键词扩展后3个领域（代数/分析、数论、组合/概率）均正确排序。权重标定方法从253号单关键词扩展为多关键词列表，新增关键词经向后兼容验证不影响253号结果。

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
