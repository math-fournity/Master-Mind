# 假完成检测（false-completion-detection）

## 定义
AI可能给出错误证明但自认为完成——需要实验后对照标准答案验证，用独立于AI的机制检测假完成。

## 来源
- 出处：suiren: 210-P5, 215-P25

## 验证状态
[tested]
MathArena baseline中检测到假完成案例。

## 使用经验
用SymPy数值验证+人工抽查。在MathArena baseline中检测到假完成案例。

## 组合关系
- 组合了：multiple-independent-verification
- 替代了：___
- 约束于：___

## 检索流程角色
不直接服务于检索

## 系统演进角色
燧人

## 开放问题
假完成的检测覆盖率如何？人工抽查的比例如何确定？
