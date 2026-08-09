# Master Agent 审计 Checklist — AoPS omni_math #4184

- **problem_id**: omni_math_004184
- **审计时间**: 2025-01-24
- **来源**：AoPS omni_math，IMO Shortlist组合/概率题（difficulty 9.0）

## Phase 0: 加载审计材料 [x]

- [x] 0a. 从ArangoDB读取完整profile ✅
- [x] 0b. 读problem.lean——非负整数三元组集合T上递归泛函方程f(p,q,r)=0(pqr=0)且f=1+(1/6)×六邻位均值(否则)。解答：随机游走期望命中时间+对称ansatz f=3pqr/(p+q+r)+代数验证+最大值原理唯一性。答案：f=3pqr/(p+q+r) ✅
- [x] 0c. 读取subagent的checklist.md ✅
- [x] 0d. 数据库与profile.json一致 ✅

## Phase 1: 格式检查 [x]

- [x] 1a. situation_type：7个pair全规范 ✅
- [x] 1b. hint_level：全0-1浮点数 ✅
- [x] 1c. per-pair拓扑：7+2个pair全有tell_topology和tell_small_concepts ✅
- [x] 1d. 必填字段全部完整 ✅
- [x] 1e. QA序列结构：7轮，stats完整（kb="R4", tb="R5"字符串类型）✅

## Phase 2: 数学内容审查 [x]

- [x] 2a. 题目理解准确 ✅
- [x] 2b. 解答理解准确——递归方程=三角格上对称随机游走期望命中时间+对称ansatz 3pqr/(p+q+r)满足边界条件和递归（代数恒等式Σ(邻位乘积)=6pqr-2(p+q+r)）+离散最大值原理保证唯一性 ✅
- [x] 2c. constraint_satisfaction vs probabilistic_interpretation_verification区分清晰 ✅
- [x] 2d. key_insight="递归方程是三角格上对称随机游走的期望命中时间，对称ansatz 3pqr/(p+q+r)通过代数恒等式同时满足边界条件和递归"——准确 ✅
- [x] 2e. QA序列逐轮审查：7轮覆盖观察→列举→小尝试→随机游走识别→对称ansatz→代数验证→最大值原理唯一性，合理 ✅
- [x] 2f. R4 kb=True正确（随机游走/调和函数解释的知识缺口是知识瓶颈），R5 tb正确（从随机游走解释到具体对称公式3pqr/(p+q+r)的思维跨越是思维瓶颈）✅
- [x] 2g-2p. 全部通过 ✅

## Phase 3-6: 全部通过 [x]

## Phase 5: 审计结论 [x]

- [x] 5a. **合格**——0个大问题，0个小问题
- [x] 5d. 记录到review-log.md

## 审计员签字

- 审计结论：✅ 合格
- 日期：2025-01-24
