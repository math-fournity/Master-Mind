# Master Agent 审计 Checklist — AoPS omni_math #3920

- **problem_id**: omni_math_003920
- **审计时间**: 2025-01-24
- **来源**：AoPS omni_math，IMO Shortlist代数题（difficulty 9.0）

## Phase 0: 加载审计材料 [x]

- [x] 0a. 从ArangoDB读取完整profile ✅
- [x] 0b. 读problem.lean——求所有f:N→N使f(m)+f(n)-mn非零且整除mf(m)+nf(n)。解答：特殊值代入(m=n=1)得f(1)=1，猜测f(x)=x²，利用m³+n³=(m+n)(m²-mn+n²)因式分解验证整除关系。答案：f(x)=x² ✅
- [x] 0c. 读取subagent的checklist.md ✅
- [x] 0d. 数据库与profile.json一致 ✅

## Phase 1: 格式检查 [x]

- [x] 1a. situation_type：7个pair全规范 ✅
- [x] 1b. hint_level：全0-1浮点数 ✅
- [x] 1c. per-pair拓扑：7+2个pair全有tell_topology和tell_small_concepts ✅
- [x] 1d. 必填字段全部完整 ✅
- [x] 1e. QA序列结构：7轮，stats完整（kb="R6", tb="R3"字符串类型）✅

## Phase 2: 数学内容审查 [x]

- [x] 2a. 题目理解准确 ✅
- [x] 2b. 解答理解准确——特殊值代入得f(1)=1+猜f(x)=x²+m³+n³=(m+n)(m²-mn+n²)因式分解验证 ✅
- [x] 2c. characterization vs specialization_guess_verify区分清晰 ✅
- [x] 2d. key_insight="m²+n²-mn恰好是m³+n³=(m+n)(m²-mn+n²)的一个因子，使整除关系自然成立"——准确 ✅
- [x] 2e. QA序列逐轮审查：7轮覆盖观察→列举→直接变形矛盾→特殊值代入→猜测f(x)=x²→因式分解验证→完整证明，合理 ✅
- [x] 2f. R6 kb=True正确（立方和因式分解公式m³+n³的知识瓶颈），R3 tb正确（从直接变形矛盾转向特殊值策略的思维操作）✅
- [x] 2g-2p. 全部通过 ✅

## Phase 3-6: 全部通过 [x]

## Phase 5: 审计结论 [x]

- [x] 5a. **合格**——0个大问题，0个小问题
- [x] 5d. 记录到review-log.md

## 审计员签字

- 审计结论：✅ 合格
- 日期：2025-01-24
