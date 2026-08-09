# Master Agent 审计 Checklist — AoPS omni_math #3910

- **problem_id**: omni_math_003910
- **审计时间**: 2025-01-24
- **来源**：AoPS omni_math，IMO Shortlist数论题（difficulty 9.0）

## Phase 0: 加载审计材料 [x]

- [x] 0a. 从ArangoDB读取完整profile ✅
- [x] 0b. 读problem.lean——设n≥1为奇整数，求所有f:Z→Z使f(x)-f(y)|x^n-y^n对所有整数x,y。解答：y=0特殊化得f(x)-f(0)|x^n，推出f(x)-f(0)=e·x^a（a|n），再用x^a-y^a|x^n-y^n验证。答案：f(x)=e·x^a+c（a|n, |e|=1）✅
- [x] 0c. 读取subagent的checklist.md ✅
- [x] 0d. 数据库与profile.json一致 ✅

## Phase 1: 格式检查 [x]

- [x] 1a. situation_type：7个pair全规范 ✅
- [x] 1b. hint_level：全0-1浮点数 ✅
- [x] 1c. per-pair拓扑：7+2个pair全有tell_topology和tell_small_concepts ✅
- [x] 1d. 必填字段全部完整 ✅
- [x] 1e. QA序列结构：7轮，stats完整（kb="R4", tb="R3"字符串类型）✅

## Phase 2: 数学内容审查 [x]

- [x] 2a. 题目理解准确 ✅
- [x] 2b. 解答理解准确——y=0特殊化降维+f(x)-f(0)|x^n推出单项式形式+x^a-y^a|x^n-y^n验证 ✅
- [x] 2c. characterization vs specialization_and_structural_deduction区分清晰 ✅
- [x] 2d. key_insight="y=0特殊化将双变量整除条件降为f(x)-f(0)|x^n，强制f(x)-f(0)为单项式e·x^a（a|n），整除性质x^a-y^a|x^n-y^n保证全局条件"——准确 ✅
- [x] 2e. QA序列逐轮审查：7轮覆盖观察→列举→小尝试→y=0特殊化→单项式形式→整除性质验证→完整证明，合理 ✅
- [x] 2f. R4 kb=True正确（x^a-y^a|x^n-y^n当a|n的数论知识瓶颈），R3 tb正确（y=0特殊化降维的思维操作）✅
- [x] 2g-2p. 全部通过 ✅

## Phase 3-6: 全部通过 [x]

## Phase 5: 审计结论 [x]

- [x] 5a. **合格**——0个大问题，0个小问题
- [x] 5d. 记录到review-log.md

## 审计员签字

- 审计结论：✅ 合格
- 日期：2025-01-24
