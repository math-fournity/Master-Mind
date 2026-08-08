# 反应式救援（reactive-rescue）

## 定义
Agent先独立尝试解题，检测到真实停滞后才匹配启发规则并注入最小提示，从当前checkpoint继续。反应式是默认模式，主动导航需经验证后开启。

## 来源
- 出处：pangu-b: 122v2-P34；nuwa-a: 136-P28

## 验证状态
[untested]
设计阶段提出，尚未实现在线运行时。

## 使用经验
设计阶段提出，检测卡点→匹配规则→注入提示→从checkpoint继续。

## 组合关系
- 组合了：stall-detection, checkpoint, context-compiler
- 替代了：主动导航（proactive navigation，需验证后才开启）
- 约束于：constrained-policy, safe-first-step（已有）

## 检索流程角色
知识悖论

## 系统演进角色
燧人

## 开放问题
反应式和主动导航的切换条件是什么？反应式模式的延迟是否可接受？
