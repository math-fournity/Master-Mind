# 模式匹配（pattern-matching）

## 定义
用规则库匹配替代硬编码提示——规则以(LHS, Guard, RHS)形式定义，匹配基于结构形状而非文本相似性，利用稀疏性只匹配可能相关的规则子集。

## 来源
- 出处：pangu-b: 122v2-P19；suiren: 200-P20, 214-P6；fuxi: 238-P7

## 验证状态
[tested]
模式匹配模块已实现（`xishujuzhen/research_runtime/matching/`），泛化验证通过。253号A7验证Q8匹配分数0.8+guard通过；数论案例A3验证Q4 match_score=1.0+guard通过；组合案例A3验证Q4 match_score=1.0+guard通过。近似匹配容差（对称差0→1.0，1→0.8，2→0.6，≥3同规模→0.5）在3个领域均正确工作。Guard条件检查的默认关键词搜索机制支持跨领域guard文本匹配。

## 使用经验
设计阶段提出，实现LHS子图匹配+Guard条件检查+RHS动作输出。

## 组合关系
- 组合了：thinking-trajectory-graph, heuristic-rule-graph
- 替代了：待补充
- 约束于：activation-score

## 检索流程角色
Pattern提取

## 系统演进角色
燧人

## 开放问题
结构形状匹配的算法复杂度如何？近似匹配的容差如何确定？
