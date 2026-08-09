# Master Agent 审计 Checklist — AoPS omni_math #4076

- **problem_id**: omni_math_004076
- **审计时间**: 2025-01-24
- **来源**：AoPS omni_math，IMO代数题（difficulty 9.0）

## Phase 0: 加载审计材料 [x]

- [x] 0a. 从ArangoDB读取完整profile ✅
- [x] 0b. 读problem.lean——求最小M使|ab(a²-b²)+bc(b²-c²)+ca(c²-a²)|≤M(a²+b²+c²)²对所有实数a,b,c成立。解答：齐次性归一化到单位球面+Lagrange乘子→非对称构型处取得极值→M=9/(16√2)。答案：M=9/(16√2) ✅
- [x] 0c. 读取subagent的checklist.md ✅
- [x] 0d. 数据库与profile.json一致 ✅

## Phase 1: 格式检查 [x]

- [x] 1a. situation_type：7个pair全规范 ✅
- [x] 1b. hint_level：全0-1浮点数 ✅
- [x] 1c. per-pair拓扑：7+3个pair全有tell_topology和tell_small_concepts ✅
- [x] 1d. 必填字段全部完整 ✅
- [x] 1e. QA序列结构：7轮，stats完整（kb="R4", tb="R6"字符串类型）✅

## Phase 2: 数学内容审查 [x]

- [x] 2a. 题目理解准确 ✅
- [x] 2b. 解答理解准确——齐次性归一化+Lagrange乘子+非对称构型极值+M=9/(16√2) ✅
- [x] 2c. inequality_proof vs homogeneous_extremal_optimization区分清晰 ✅
- [x] 2d. key_insight="表达式齐次可归一化到单位球面求极值，对称构型(a=b=c)使表达式为0，极值在非对称构型处取得"——准确 ✅
- [x] 2e. QA序列逐轮审查：7轮覆盖观察→列举→小尝试→齐次性识别→Lagrange乘子→非线性方程组求解→完整证明，合理 ✅
- [x] 2f. R4 kb=True正确（Lagrange乘子法在约束优化中的应用是知识瓶颈），R6 tb正确（非线性三次梯度方程组的参数化简化是思维瓶颈）✅
- [x] 2g-2p. 全部通过 ✅
- [x] 备注：3个global pairs（1 path_feature + 2 implicit），全部格式合格

## Phase 3-6: 全部通过 [x]

## Phase 5: 审计结论 [x]

- [x] 5a. **合格**——0个大问题，0个小问题
- [x] 5d. 记录到review-log.md

## 审计员签字

- 审计结论：✅ 合格
- 日期：2025-01-24
