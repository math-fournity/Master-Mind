# Master Agent 审计 Checklist — AoPS omni_math #4213

- **problem_id**: omni_math_004213
- **审计时间**: 2025-01-24
- **来源**：AoPS omni_math，IMO Shortlist代数/多项式题（difficulty 9.0）

## Phase 0: 加载审计材料 [x]

- [x] 0a. 从ArangoDB读取完整profile ✅
- [x] 0b. 读problem.lean——求所有整数对(a,b)使存在P(x)∈Z[X]令(x²+ax+b)·P(x)所有系数±1。解答：常数项bc₀=±1→b=±1+一次项约束→a有限集→8对。答案：8对 ✅
- [x] 0c. 读取subagent的checklist.md ✅
- [x] 0d. 数据库与profile.json一致 ✅

## Phase 1: 格式检查 [x]

- [x] 1a. situation_type：7个pair全规范 ✅
- [x] 1b. hint_level：全0-1浮点数 ✅
- [x] 1c. per-pair拓扑：7+2个pair全有tell_topology和tell_small_concepts ✅
- [x] 1d. 必填字段全部完整 ✅
- [x] 1e. QA序列结构：7轮，stats完整（kb="R3", tb="R4"字符串类型）✅

## Phase 2: 数学内容审查 [x]

- [x] 2a. 题目理解准确 ✅
- [x] 2b. 解答理解准确——常数项bc₀=±1(c₀整数)→b=±1+b=1时a∈{-2,-1,0,1,2}+b=-1时a∈{-1,0,1}+逐一构造P(x)验证→8对 ✅
- [x] 2c. characterization vs coefficient_constraint_case_analysis区分清晰 ✅
- [x] 2d. key_insight="常数项bc₀=±1迫使b=±1，将无穷搜索空间坍缩为两种情况，一次项约束系统缩小a到有限集"——准确 ✅
- [x] 2e. QA序列逐轮审查：7轮覆盖观察→列举→小尝试→常数项约束→一次项传播→构造验证→完整枚举，合理 ✅
- [x] 2f. R3 kb=True正确（常数项bc₀=±1→b=±1的整除性洞察是知识瓶颈），R4 tb正确（从一次项系数系统传播约束到a的有限集是思维瓶颈）✅
- [x] 2g-2p. 全部通过 ✅

## Phase 3-6: 全部通过 [x]

## Phase 5: 审计结论 [x]

- [x] 5a. **合格**——0个大问题，0个小问题
- [x] 5d. 记录到review-log.md

## 审计员签字

- 审计结论：✅ 合格
- 日期：2025-01-24
