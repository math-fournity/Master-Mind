# 上下文编译器（context-compiler）

## 定义
把检索到的数学子图编译为AI此刻能可靠使用的最小上下文包——决定节点展开顺序和分辨率、翻译边为思考关系、token预算删减、三项最小性审计（冗余/缺失/预载）、从checkpoint增量编译。

## 来源
- 出处：pangu-b: 122v1-P15；nuwa-a: 135-P17；nuwa-b: 183-P33；fuxi: 250-P6

## 验证状态
[partial]
代码已实现并集成测试通过。

## 架构位置
检索管线和认知激活之间的编译桥梁。实现编译管线（8步）。

## 组合关系
- 连接到：retrieval-pipeline, layered-storage
- 包含了：待补充
- 被包含于：待补充
- 约束于：minimal-knowledge-transfer（已有原语），non-specificity（已有原语）

## 检索流程角色
知识悖论

## 系统演进角色
跨代

## 开放问题
三项最小性审计的阈值如何设定？增量编译的checkpoint粒度如何选择？
