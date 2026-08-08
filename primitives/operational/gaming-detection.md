# 博弈检测（gaming-detection）

## 定义
三元判定机制检测工作智能体是否在"gaming"——（停滞词=True）AND（工具证据=False）AND（结构进展=False）三条件全部满足才判定。

## 来源
- 出处：nuwa-a: 136-P23；nuwa-b: 175-P12

## 验证状态
[partial]
代码已实现但未在真实gaming行为上验证。

## 使用经验
实现三元AND判定逻辑。

## 组合关系
- 组合了：stall-detection
- 替代了：待补充
- 约束于：constrained-policy

## 检索流程角色
不直接服务于检索

## 系统演进角色
女娲

## 开放问题
三元判定的假阳性率如何？gaming行为的边界案例如何处理？
