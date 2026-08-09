# Master Agent 审计 Checklist — AoPS omni_math #324

- **problem_id**: omni_math_000324
- **审计时间**: 2025-01-24
- **来源**：AoPS omni_math，IMC（e级数部分和既约分母）

## Phase 0: 加载审计材料 [x]

- [x] 0a. 从ArangoDB读取完整profile ✅
- [x] 0b. 读problem.lean——判断是否存在正整数n使g(n)>n^{0.999n}，其中f(n),g(n)是某最小/最大值。解答：定义"特殊素数"概念（密度阈值ε=10^{-10}），证明只有有限个，用非特殊素数构造n。答案：Yes ✅
- [x] 0c. 读取subagent的checklist.md ✅
- [x] 0d. 数据库与profile.json一致 ✅

## Phase 1: 格式检查 [x]

- [x] 1a. situation_type：7个pair全规范 ✅
- [x] 1b. hint_level：0.3-0.8全0-1浮点数 ✅
- [x] 1c. per-pair拓扑：7+2个pair全有tell_topology和tell_small_concepts ✅
- [x] 1d. 必填字段全部完整 ✅
- [x] 1e. QA序列结构：7轮，stats完整（kb="R4", tb="R5"字符串类型）✅

## Phase 2: 数学内容审查 [x]

- [x] 2a. 题目理解准确 ✅
- [x] 2b. 解答理解准确——特殊素数概念+密度阈值+有限个+非特殊素数构造n ✅
- [x] 2c. structural_existence vs existence_proof_by_construction区分清晰 ✅
- [x] 2d. key_insight="定义特殊素数（以密度ε为阈值区分素数对f(j)的整除行为），证明只有有限个，从而非特殊素数足够多以构造g(n)大的n"——准确 ✅
- [x] 2e. QA序列逐轮审查：7轮覆盖观察→列举→小n尝试→约分机制理解→特殊素数概念定义→构造n→综合，合理 ✅
- [x] 2f. R4 kb=True正确（理解约分机制——素数整除f(n)导致分母变小是知识瓶颈），R5 tb正确（创造性定义"特殊素数"概念是思维瓶颈）✅
- [x] 2g-2p. 全部通过 ✅

## Phase 3-6: 全部通过 [x]

## Phase 5: 审计结论 [x]

- [x] 5a. **合格**——0个大问题，0个小问题
- [x] 5d. 记录到review-log.md

## 审计员签字

- 审计结论：✅ 合格
- 日期：2025-01-24
