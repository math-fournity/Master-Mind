# 多次独立验证（multiple-independent-verification）

## 定义
通过多次（≥3次）独立运行判定结果是稳定的还是偶然的——3次全错才算"做不出来"，用独立于AI的机制验证结果正确性。

## 来源
- 出处：suiren: 210-P4

## 验证状态
[tested]
在MathArena baseline中已使用。

## 使用经验
多次运行同一题目，用SymPy/Lean验证。在MathArena baseline中使用。

## 组合关系
- 组合了：___
- 替代了：___
- 约束于：false-completion-detection

## 检索流程角色
不直接服务于检索

## 系统演进角色
跨代

## 开放问题
3次是否足够？独立运行之间如何保证独立性？
