# Master Agent 审计 Checklist — AoPS omni_math #4014

- **problem_id**: omni_math_004014
- **审计时间**: 2025-01-24
- **来源**：AoPS omni_math，IMO Shortlist代数题（difficulty 9.0）

## Phase 0: 加载审计材料 [x]

- [x] 0a. 从ArangoDB读取完整profile ✅
- [x] 0b. 读problem.lean——求所有f:R→R满足f(xf(x+y))=f(yf(x))+x²。解答：y=0和x=0代入得f(0)=0和f(xf(x))=x²→猜f(x)=±x验证。答案：f(x)=x和f(x)=-x ✅
- [x] 0c. 读取subagent的checklist.md ✅
- [x] 0d. 数据库与profile.json一致 ✅

## Phase 1: 格式检查 [x]

- [x] 1a. situation_type：7个pair全规范 ✅
- [x] 1b. hint_level：全0-1浮点数 ✅
- [x] 1c. per-pair拓扑：7+2个pair全有tell_topology和tell_small_concepts ✅
- [x] 1d. 必填字段全部完整 ✅
- [x] 1e. QA序列结构：7轮，stats完整（kb="R5", tb="R6"字符串类型）✅

## Phase 2: 数学内容审查 [x]

- [x] 2a. 题目理解准确 ✅
- [x] 2b. 解答理解准确——y=0,x=0特化代入→f(0)=0,f(xf(x))=x²→猜f(x)=±x验证 ✅
- [x] 2c. characterization vs specialization_and_candidate_verification区分清晰 ✅
- [x] 2d. key_insight="x=0时f(0)=f(cy)+x²项排除常函数→f(0)=0→搜索范围缩小到非常函数→猜f(x)=±x验证"——准确 ✅
- [x] 2e. QA序列逐轮审查：7轮覆盖观察→列举→小尝试→y=0代入→x=0代入→候选猜测→验证，合理 ✅
- [x] 2f. R5 kb=True正确（用x²项排除常函数推导f(0)=0是知识瓶颈），R6 tb正确（猜测正确候选f(x)=±x并验证是思维瓶颈）✅
- [x] 2g-2p. 全部通过 ✅

## Phase 3-6: 全部通过 [x]

## Phase 5: 审计结论 [x]

- [x] 5a. **合格**——0个大问题，0个小问题
- [x] 5d. 记录到review-log.md

## 审计员签字

- 审计结论：✅ 合格
- 日期：2025-01-24
