# 动态工作区（dynamic-workspace）

## 定义
系统在时刻t的完整状态用六元组表示——V_t（已验证核心）、F_t（猜想前沿）、O_t（开放义务）、R_t（表示状态）、E_t（证据）、U_t（未解决问题），状态由版本化Reducer从事件流归约得出，不可直接修改，状态等价通过规范化键判定。

## 来源
- 出处：fuxi: 250-P11；pangu-b: 123-P14；nuwa-b: 188-P01；suiren: 200-P18

## 验证状态
[tested]
P0解析器原型实现（`xishujuzhen/research_runtime/parser/`），253号A1-A10的六元组构建验证通过。六元组字段准确率100%（91/91字段正确）。V_t/F_t/O_t/R_t/E_t/U_t的累积更新逻辑验证正确。U_t正确识别了A5和A7的blocking卡点。

## 架构位置
卡点检测、增量编译、进展度量的状态基础。实现版本化Reducer，从事件流归约六元组状态。

## 组合关系
- 连接到：event-sourcing, obligation-hypergraph（O_t字段）, evidence-system（E_t字段）
- 包含了：待补充
- 被包含于：待补充
- 约束于：不可变性（immutability）概念

## 检索流程角色
状态感知

## 系统演进角色
伏羲

## 开放问题
六元组是否完备？状态等价的规范化键如何设计？Reducer的版本化如何实现？
