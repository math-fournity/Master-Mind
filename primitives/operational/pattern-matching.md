# 模式匹配（pattern-matching）

## 定义
用规则库匹配替代硬编码提示——规则以(LHS, Guard, RHS)形式定义，匹配基于结构形状而非文本相似性，利用稀疏性只匹配可能相关的规则子集。

## 来源
- 出处：pangu-b: 122v2-P19；suiren: 200-P20, 214-P6；fuxi: 238-P7

## 验证状态
[untested]
设计阶段提出，未在真实Pattern库上验证。

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
