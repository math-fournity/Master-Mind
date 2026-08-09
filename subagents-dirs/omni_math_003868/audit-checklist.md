# Master Agent 审计 Checklist — AoPS omni_math #3868

- **problem_id**: omni_math_003868
- **审计时间**: 2025-01-24
- **来源**：AoPS omni_math，IMO（函数方程f:(0,∞)→(0,∞)+不变量识别+因式分解）

## Phase 0: 加载审计材料 [x]

- [x] 0a. 从ArangoDB读取完整profile ✅
- [x] 0b. 读problem.lean——求f:(0,∞)→(0,∞)使(f(w)²+f(x)²)/(f(y²)+f(z²))=(w²+x²)/(y²+z²)（wx=yz）。解答：令w=y,x=z发现f(x)²-f(x²)是不变量（常数0），从而f(x²)=f(x)²将四变量方程降维为二变量比值方程，再用g(x)=f(x)/x代换因式分解得到逐点解。答案：f(x)=x或f(x)=1/x ✅
- [x] 0c. 读取subagent的checklist.md ✅
- [x] 0d. 数据库与profile.json一致 ✅

## Phase 1: 格式检查 [x]

- [x] 1a. situation_type：7个pair全规范 ✅
- [x] 1b. hint_level：0.4-0.8全0-1浮点数 ✅
- [x] 1c. per-pair拓扑：7+2个pair全有tell_topology和tell_small_concepts ✅
- [x] 1d. 必填字段全部完整 ✅
- [x] 1e. QA序列结构：7轮，stats完整（kb="R5", tb="R4"字符串类型）✅

## Phase 2: 数学内容审查 [x]

- [x] 2a. 题目理解准确 ✅
- [x] 2b. 解答理解准确——w=y,x=z对称代换→f(x²)=f(x)²不变量→降维→g(x)=f(x)/x因式分解→逐点f(x)∈{x,1/x}→全局一致性 ✅
- [x] 2c. characterization vs 不变量识别+变量替换+因式分解区分清晰 ✅
- [x] 2d. key_insight="令w=y,x=z发现f(x)²-f(x²)是不变量（常数0），从而f(x²)=f(x)²将四变量方程降维为二变量比值方程，再用g(x)=f(x)/x代换因式分解得到逐点解"——准确 ✅
- [x] 2e. QA序列逐轮审查：7轮覆盖观察→列举→小尝试→不变量识别→g(x)替换+因式分解→全局一致性→综合，合理 ✅
- [x] 2f. R5 kb=True正确（g(x)替换+因式分解是知识瓶颈），R4 tb正确（不变量识别是思维瓶颈）✅
- [x] 2g-2p. 全部通过 ✅

## Phase 3-6: 全部通过 [x]

## Phase 5: 审计结论 [x]

- [x] 5a. **合格**——0个大问题，0个小问题
- [x] 5d. 记录到review-log.md

## 审计员签字

- 审计结论：✅ 合格
- 日期：2025-01-24
