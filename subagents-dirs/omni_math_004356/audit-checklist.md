# Master Agent 审计 Checklist — AoPS omni_math #4356

- **problem_id**: omni_math_004356
- **审计时间**: 2025-01-24
- **来源**：AoPS omni_math，IMO Shortlist数论题（difficulty 9.0）

## Phase 0: 加载审计材料 [x]

- [x] 0a. 从ArangoDB读取完整profile ✅
- [x] 0b. 读problem.lean——圆上四整数a,b,c,d每步替换为(a-b,b-c,c-d,d-a)，1996步后|bc-ad|,|ac-bd|,|ab-cd|能否全为素数。解答：不变量a+b+c+d=0→d=-(a+b+c)→三式因式分解为(a+b)(a+c),(a+b)(b+c),(a+c)(b+c)→至少两个因子绝对值为1→第三乘积=1非素数→矛盾。答案：No ✅
- [x] 0c. 读取subagent的checklist.md ✅
- [x] 0d. 数据库与profile.json一致 ✅
- [x] 备注：原Lean解答模糊（"numbers tend toward zero"），实际正确解法是精确因式分解+矛盾论证，subagent已注明

## Phase 1: 格式检查 [x]

- [x] 1a. situation_type：7个pair全规范 ✅
- [x] 1b. hint_level：全0-1浮点数 ✅
- [x] 1c. per-pair拓扑：7+2个pair全有tell_topology和tell_small_concepts ✅
- [x] 1d. 必填字段全部完整 ✅
- [x] 1e. QA序列结构：7轮，stats完整（kb="R4", tb="R6"字符串类型）✅

## Phase 2: 数学内容审查 [x]

- [x] 2a. 题目理解准确 ✅
- [x] 2b. 解答理解准确——任意≥1步后a+b+c+d=0（差分变换不变量）+d=-(a+b+c)代入三式得(a+b)(a+c),(a+b)(b+c),(a+c)(b+c)+令x=a+b,y=a+c,z=b+c+若|xy|,|xz|,|yz|全素数则至少两个绝对值为1→第三乘积=1非素数→矛盾 ✅
- [x] 2c. constraint_satisfaction vs invariant_factoring_contradiction区分清晰 ✅
- [x] 2d. key_insight="a+b+c+d=0使三式因式分解为(a+b)(a+c)等，三个值中至少两个绝对值为1使第三乘积=1非素数"——准确 ✅
- [x] 2e. QA序列逐轮审查：7轮覆盖观察→列举→小尝试→不变量发现→因式分解→case分析→矛盾，合理 ✅
- [x] 2f. R4 kb=True正确（因式分解a²+ab+ac+bc=(a+b)(a+c)的代数恒等式识别是知识瓶颈），R6 tb正确（case分析发现至少两个因子绝对值为1导致矛盾是思维瓶颈）✅
- [x] 2g-2p. 全部通过 ✅

## Phase 3-6: 全部通过 [x]

## Phase 5: 审计结论 [x]

- [x] 5a. **合格**——0个大问题，0个小问题（原解答模糊已由subagent用精确因式分解+矛盾论证重构）
- [x] 5d. 记录到review-log.md

## 审计员签字

- 审计结论：✅ 合格
- 日期：2025-01-24
