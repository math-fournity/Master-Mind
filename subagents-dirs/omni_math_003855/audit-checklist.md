# Master Agent 审计 Checklist — AoPS omni_math #3855

- **problem_id**: omni_math_003855
- **审计时间**: 2025-01-24
- **来源**：AoPS omni_math，IMO Shortlist（±1序列+势函数+max-of-two反消去）

## Phase 0: 加载审计材料 [x]

- [x] 0a. 从ArangoDB读取完整profile ✅
- [x] 0b. 读problem.lean——±1序列a_1,...,a_2022。解答：定义F[i]=max(0,f[i])和G[i]=max(0,-g[i])，DP的max-of-two机制防止平衡块中正负贡献完全消去，保证每4个位置max(F,G)至少增长1。答案：506 ✅
- [x] 0c. 读取subagent的checklist.md ✅
- [x] 0d. 数据库与profile.json一致 ✅

## Phase 1: 格式检查 [x]

- [x] 1a. situation_type：7个pair全规范 ✅
- [x] 1b. hint_level：0.4-0.8全0-1浮点数 ✅
- [x] 1c. per-pair拓扑：7+2个pair全有tell_topology和tell_small_concepts ✅
- [x] 1d. 必填字段全部完整 ✅
- [x] 1e. QA序列结构：7轮，stats完整（kb="R6", tb="R4"字符串类型）✅

## Phase 2: 数学内容审查 [x]

- [x] 2a. 题目理解准确 ✅
- [x] 2b. 解答理解准确——势函数F/G+max-of-two反消去机制+每4个位置max(F,G)至少增长1+周期4 pattern (+1,-1,-1,+1) ✅
- [x] 2c. discrete_combinatorial vs structural_transformation区分清晰 ✅
- [x] 2d. key_insight="定义F[i]=max(0,f[i])和G[i]=max(0,-g[i])，DP的max-of-two机制防止平衡块中正负贡献完全消去，保证每4个位置max(F,G)至少增长1"——准确 ✅
- [x] 2e. QA序列逐轮审查：7轮覆盖观察→列举→小尝试→周期4 pattern识别→势函数构造→max-of-two反消去→综合，合理 ✅
- [x] 2f. R4/R6 kb=True正确（周期4 pattern识别和势函数F/G及max-of-two机制是知识瓶颈），R4 tb正确（找到正确的周期4 pattern是思维瓶颈）✅
- [x] 2g-2p. 全部通过 ✅

## Phase 3-6: 全部通过 [x]

## Phase 5: 审计结论 [x]

- [x] 5a. **合格**——0个大问题，0个小问题
- [x] 5d. 记录到review-log.md

## 审计员签字

- 审计结论：✅ 合格
- 日期：2025-01-24
