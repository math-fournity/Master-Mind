# Master Agent 审计 Checklist — AoPS omni_math #4047

- **problem_id**: omni_math_004047
- **审计时间**: 2025-01-24
- **来源**：AoPS omni_math，IMO Shortlist代数/数论题（difficulty 9.0）

## Phase 0: 加载审计材料 [x]

- [x] 0a. 从ArangoDB读取完整profile ✅
- [x] 0b. 读problem.lean——求所有正整数n使存在正整数对(a,b)，a²+b+3不被任何素数立方整除，且n=(ab+3b+8)/(a²+b+3)。解答：固定n=2→2a²-ab-b-2=0→b=2(a-1)→a=2,b=2→验证cube-free→n=2。答案：2 ✅
- [x] 0c. 读取subagent的checklist.md ✅
- [x] 0d. 数据库与profile.json一致 ✅

## Phase 1: 格式检查 [x]

- [x] 1a. situation_type：7个pair全规范 ✅
- [x] 1b. hint_level：全0-1浮点数 ✅
- [x] 1c. per-pair拓扑：7+2个pair全有tell_topology和tell_small_concepts ✅
- [x] 1d. 必填字段全部完整 ✅
- [x] 1e. QA序列结构：7轮，stats完整（kb="R6", tb="R4"字符串类型）✅

## Phase 2: 数学内容审查 [x]

- [x] 2a. 题目理解准确 ✅
- [x] 2b. 解答理解准确——固定n=2+交叉相乘2a²-ab-b-2=0+b=2(a-1)+a=2,b=2+验证cube-free→n=2 ✅
- [x] 2c. constraint_satisfaction vs trial_and_verify区分清晰 ✅
- [x] 2d. key_insight="固定n=2后交叉相乘，b(a+1)=2(a-1)(a+1)约分得b=2(a-1)，取a=2时b=2，验证cube-free"——准确 ✅
- [x] 2e. QA序列逐轮审查：7轮覆盖观察→列举→小尝试→固定n策略→因式分解→cube-free验证→完整证明，合理 ✅
- [x] 2f. R6 kb=True正确（因式分解2a²-ab-b-2=0为b=2(a-1)的代数操作是知识瓶颈），R4 tb正确（从枚举(a,b)转向固定n的策略转换是思维瓶颈）✅
- [x] 2g-2p. 全部通过 ✅

## Phase 3-6: 全部通过 [x]

## Phase 5: 审计结论 [x]

- [x] 5a. **合格**——0个大问题，0个小问题
- [x] 5d. 记录到review-log.md

## 审计员签字

- 审计结论：✅ 合格
- 日期：2025-01-24
