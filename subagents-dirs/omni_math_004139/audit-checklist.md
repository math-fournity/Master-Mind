# Master Agent 审计 Checklist — AoPS omni_math #4139

- **problem_id**: omni_math_004139
- **审计时间**: 2025-01-24
- **来源**：AoPS omni_math，IMO Shortlist代数/函数方程题（difficulty 9.0）

## Phase 0: 加载审计材料 [x]

- [x] 0a. 从ArangoDB读取完整profile ✅
- [x] 0b. 读problem.lean——求所有f:(0,∞)→R满足(x+1/x)f(y)=f(xy)+f(y/x)。解答：y=1代入→f(x)+f(1/x)=c(x+1/x)→猜f(x)=ax+b/x→验证。答案：f(x)=ax+b/x ✅
- [x] 0c. 读取subagent的checklist.md ✅
- [x] 0d. 数据库与profile.json一致 ✅

## Phase 1: 格式检查 [x]

- [x] 1a. situation_type：6个pair全规范 ✅
- [x] 1b. hint_level：全0-1浮点数 ✅
- [x] 1c. per-pair拓扑：6+2个pair全有tell_topology和tell_small_concepts ✅
- [x] 1d. 必填字段全部完整 ✅
- [x] 1e. QA序列结构：6轮（在5-8轮范围内），stats完整（kb="R4", tb="R3"字符串类型）✅

## Phase 2: 数学内容审查 [x]

- [x] 2a. 题目理解准确 ✅
- [x] 2b. 解答理解准确——y=1代入→f(x)+f(1/x)=c(x+1/x)→猜f(x)=ax+b/x→代入验证恒等 ✅
- [x] 2c. characterization vs ansatz_verification区分清晰 ✅
- [x] 2d. key_insight="从y=1代入得到的f(x)+f(1/x)=c(x+1/x)结构，暗示f(x)是x和1/x的线性组合ax+b/x"——准确 ✅
- [x] 2e. QA序列逐轮审查：6轮覆盖观察→列举→小尝试→y=1代入→ansatz猜测→验证，合理 ✅
- [x] 2f. R4 kb=True正确（从y=1代入结果的结构匹配到ansatz形式f(x)=ax+b/x的跳跃是知识瓶颈），R3 tb正确（选择正确特殊值代入——x=1给平凡等式需转向y=1是思维瓶颈）✅
- [x] 2g-2p. 全部通过 ✅

## Phase 3-6: 全部通过 [x]

## Phase 5: 审计结论 [x]

- [x] 5a. **合格**——0个大问题，0个小问题
- [x] 5d. 记录到review-log.md

## 审计员签字

- 审计结论：✅ 合格
- 日期：2025-01-24
