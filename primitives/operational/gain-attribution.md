# 增益归因（gain-attribution）

## 定义
对每次干预验证并归因其产生的增益——记录提示链，进展归因给首次引入H关系的提示，反事实估计"没有该提示是否也会达到进展"。

## 来源
- 出处：suiren: 200-P12；fuxi: 252-P19；nuwa-a: 136-P26

## 验证状态
[tested]
增益归因模块已实现（`xishujuzhen/research_runtime/attribution/`），253号10轮QA验证提示链记录和进展归因。A8进展增量归因给Q8（progress_delta=1.0），反事实估计通过U_t severity判断——blocking义务"估计D的下界"对应"没有Q8不太可能自发达到进展"，minor义务对应"也可能达到进展"。归因和反事实估计逻辑验证正确。

## 使用经验
记录提示链，计算归因，做反事实估计。

## 组合关系
- 组合了：controlled-experiment
- 替代了：___
- 约束于：pattern-lifecycle

## 检索流程角色
不直接服务于检索

## 系统演进角色
跨代

## 开放问题
反事实估计的可靠性如何？多提示联合贡献如何分解？
