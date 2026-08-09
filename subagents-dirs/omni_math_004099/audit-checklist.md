# Master Agent 审计 Checklist — AoPS omni_math #4099

- **problem_id**: omni_math_004099
- **审计时间**: 2025-01-24
- **来源**：AoPS omni_math，IMO Shortlist代数题（difficulty 9.0）

## Phase 0: 加载审计材料 [x]

- [x] 0a. 从ArangoDB读取完整profile ✅
- [x] 0b. 读problem.lean——给定q和10个不同实数，构造三行数（差值a-b、qab、a²+b²-c²-d²），求所有q使第二行每个数都在第三行中。解答："对所有餐巾数"→多项式恒等式→交叉项系数匹配→q∈{-2,0,2}+四变量恒等式验证。答案：q∈{-2,0,2} ✅
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
- [x] 2b. 解答理解准确——"对所有餐巾数"→多项式恒等式+交叉项系数匹配→q∈{-2,0,2}+四变量恒等式2(a-b)(c-d)=(a-d)²+(b-c)²-(a-c)²-(b-d)²验证q=2 ✅
- [x] 2c. constraint_satisfaction vs algebraic_identity区分清晰 ✅
- [x] 2d. key_insight="'对所有餐巾数'条件迫使多项式恒等式，四变量恒等式2(a-b)(c-d)=(a-d)²+(b-c)²-(a-c)²-(b-d)²保持所有项为差值，证明q=2通用"——准确 ✅
- [x] 2e. QA序列逐轮审查：7轮覆盖观察→列举→小尝试→多项式恒等式→交叉项匹配→四变量恒等式→完整证明，合理 ✅
- [x] 2f. R4 kb=True正确（识别"对所有餐巾数"条件意味着多项式恒等式是知识瓶颈），R5 tb正确（找到四变量恒等式替代失效的两变量恒等式是思维瓶颈）✅
- [x] 2g-2p. 全部通过 ✅

## Phase 3-6: 全部通过 [x]

## Phase 5: 审计结论 [x]

- [x] 5a. **合格**——0个大问题，0个小问题
- [x] 5d. 记录到review-log.md

## 审计员签字

- 审计结论：✅ 合格
- 日期：2025-01-24
