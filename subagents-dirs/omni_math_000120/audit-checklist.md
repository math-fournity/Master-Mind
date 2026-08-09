# Master Agent 审计 Checklist — AoPS omni_math #120

- **problem_id**: omni_math_000120
- **审计时间**: 2025-01-24
- **来源**：AoPS omni_math，中国国家队奥林匹克（递推数列）

## Phase 0: 加载审计材料 [x]

- [x] 0a. 从ArangoDB读取完整profile ✅
- [x] 0b. 读problem.lean——两个数列a_n（递减）、b_n（递增），递推式中含倒数部分和，条件a₁₀₀b₁₀₀=a₁₀₁b₁₀₁，求a₁-b₁。解答：辅助量A_n=1+Σ1/a_i消去部分和→联立A_{n+1}两个表达式交叉相乘→a_{n+1}²=a_n·a_{n+2}（等比）→b_n不变量b_n·B_n=2n+b₁-1→比值闭式→条件分解为比值乘积=1→a₁-b₁=199 ✅
- [x] 0c. 读取subagent的checklist.md ✅
- [x] 0d. 数据库与profile.json一致 ✅

## Phase 1: 格式检查 [x]

- [x] 1a. situation_type：7个pair全规范 ✅
- [x] 1b. hint_level：0.2-0.7全0-1浮点数 ✅
- [x] 1c. per-pair拓扑：7+2个pair全有tell_topology和tell_small_concepts ✅
- [x] 1d. 必填字段全部完整 ✅
- [x] 1e. QA序列结构：7轮，stats完整（kb="R4", tb="R6"字符串类型）✅

## Phase 2: 数学内容审查 [x]

- [x] 2a. 题目理解准确 ✅
- [x] 2b. 解答理解准确——辅助量A_n消去部分和+交叉相乘得等比+b_n不变量+比值闭式+条件分解 ✅
- [x] 2c. characterization vs algebraic_manipulation区分清晰 ✅
- [x] 2d. key_insight="辅助量A_n=1+Σ1/a_i将递推式改写为A_n=1/(a_n-a_{n+1})，联立A_{n+1}的两个表达式交叉相乘得a_{n+1}²=a_n·a_{n+2}（等比）；对b_n发现不变量b_n·B_n=2n+b₁-1"——准确 ✅
- [x] 2e. QA序列逐轮审查：7轮覆盖观察→列举→小规模尝试→辅助量法→等比结构→不变量发现→综合，合理 ✅
- [x] 2f. R4 kb=True正确（辅助量法消去部分和推导等比结构是知识瓶颈），R6 tb正确（发现b_n的不变量是思维瓶颈）✅
- [x] 2g-2p. 全部通过 ✅

## Phase 3-6: 全部通过 [x]

## Phase 5: 审计结论 [x]

- [x] 5a. **合格**——0个大问题，0个小问题
- [x] 5d. 记录到review-log.md

## 审计员签字

- 审计结论：✅ 合格
- 日期：2025-01-24
