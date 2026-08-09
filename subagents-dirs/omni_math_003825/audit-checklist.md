# Master Agent 审计 Checklist — AoPS omni_math #3825

- **problem_id**: omni_math_003825
- **审计时间**: 2025-01-24
- **来源**：AoPS omni_math，IMO Shortlist（n位二进制串Hamming距离k邻域唯一性）

## Phase 0: 加载审计材料 [x]

- [x] 0a. 从ArangoDB读取完整profile ✅
- [x] 0b. 读problem.lean——IMO队长选n和k（n>k），宣布给副队长和队员，关于n位二进制串Hamming距离k邻域的唯一性。解答：n=2k时2次（补串共享邻域，因为d(x,z)=k iff d(complement(x),z)=n-k=k），否则1次（Vandermonde恒等式参数化迫使唯一）。答案：n=2k时为2，否则为1 ✅
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
- [x] 2b. 解答理解准确——d(x,z)+d(complement(x),z)=n恒等式+n=2k时k=n-k导致邻域重合+Vandermonde恒等式参数化 ✅
- [x] 2c. discrete_combinatorial vs structural_argument区分清晰 ✅
- [x] 2d. key_insight="n=2k时串和补串有相同k-邻域因为d(x,z)=k iff d(complement(x),z)=n-k=k；n≠2k时Vandermonde代数条件迫使唯一"——准确 ✅
- [x] 2e. QA序列逐轮审查：7轮覆盖观察→列举→小n,k尝试→Vandermonde恒等式参数化→从代数条件推出d=2k且n=2k→补串邻域重合→综合，合理 ✅
- [x] 2f. R4 kb=True正确（Vandermonde恒等式参数化是知识瓶颈），R5 tb正确（从代数条件推出d=2k且n=2k是思维瓶颈）✅
- [x] 2g-2p. 全部通过 ✅

## Phase 3-6: 全部通过 [x]

## Phase 5: 审计结论 [x]

- [x] 5a. **合格**——0个大问题，0个小问题
- [x] 5d. 记录到review-log.md

## 审计员签字

- 审计结论：✅ 合格
- 日期：2025-01-24
