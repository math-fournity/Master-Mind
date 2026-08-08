# 证书拉回（certificate-pullback）

## 定义
给定表示变换τ:S'→S，将S上的证书翻译到S'上的操作——跨表示检索的基础操作。

## 来源
- 出处：fuxi: 227-P14, 230-P21

## 验证状态
[untested]
设计完成但未在真实跨域推理中验证。

## 使用经验
定义证书翻译规则，执行拉回操作。

## 组合关系
- 组合了：certificate（已有原语）, representation-atlas
- 替代了：___
- 约束于：base-change（已有原语，证书拉回是换表示后的证书翻译）, obstruction-detection

## 检索流程角色
Pattern提取

## 系统演进角色
伏羲

## 开放问题
证书翻译规则的完备性如何保证？拉回操作的计算复杂度如何？
