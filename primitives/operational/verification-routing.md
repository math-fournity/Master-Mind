# 验证路由（verification-routing）

## 定义
根据命题类型选择验证工具并分层路由——formal→Lean 4、symbolic→SymPy、numerical→NumPy、human→人工，验证器输出6种状态。

## 来源
- 出处：nuwa-a: 135-P23；nuwa-b: 183-P39

## 验证状态
[partial]
代码已实现但未在真实混合型命题上验证。

## 使用经验
实现路由逻辑，调用对应验证工具。

## 组合关系
- 组合了：evidence-system
- 替代了：待补充
- 约束于：certificate（已有原语）

## 检索流程角色
不直接服务于检索

## 系统演进角色
伏羲

## 开放问题
混合型命题的路由优先级如何确定？6种验证器状态是否完备？
