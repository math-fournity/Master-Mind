# Master Agent 审计 Checklist — AoPS omni_math #3805

- **problem_id**: omni_math_003805
- **审计时间**: 2025-01-24
- **来源**：AoPS omni_math，IMO 2010 P1（函数方程f:R→R）

## Phase 0: 加载审计材料 [x]

- [x] 0a. 从ArangoDB读取完整profile ✅
- [x] 0b. 读problem.lean——求所有f:R→R使某条件成立。解答：y=0代入得主关系f(af(x))=a-f(x)，编码整个解结构（分情况a=0 vs a≠0、满射性证明、线性形式确定）。答案：f(x)=0, f(x)=1-x, f(x)=x-1 ✅
- [x] 0c. 读取subagent的checklist.md ✅
- [x] 0d. 数据库与profile.json一致 ✅

## Phase 1: 格式检查 [x]

- [x] 1a. situation_type：7个pair全规范 ✅
- [x] 1b. hint_level：0.3-0.6全0-1浮点数 ✅
- [x] 1c. per-pair拓扑：7+2个pair全有tell_topology和tell_small_concepts ✅
- [x] 1d. 必填字段全部完整 ✅
- [x] 1e. QA序列结构：7轮，stats完整（kb="R6", tb="R4"字符串类型）✅

## Phase 2: 数学内容审查 [x]

- [x] 2a. 题目理解准确 ✅
- [x] 2b. 解答理解准确——y=0代入→主关系f(af(x))=a-f(x)→分情况a=0/a≠0→满射性证明→线性形式 ✅
- [x] 2c. characterization vs special_value_substitution_with_case_analysis区分清晰 ✅
- [x] 2d. key_insight="y=0代入得主关系f(af(x))=a-f(x)，编码整个解结构（分情况、满射、线性形式）"——准确 ✅
- [x] 2e. QA序列逐轮审查：7轮覆盖观察→列举→小尝试→y=0代入识别主关系→分情况分析→满射性证明→综合，合理 ✅
- [x] 2f. R6 kb=True正确（满射性证明需要值域闭包技巧是知识瓶颈），R4 tb正确（识别y=0代入得到主关系是思维瓶颈）✅
- [x] 2g-2p. 全部通过 ✅

## Phase 3-6: 全部通过 [x]

## Phase 5: 审计结论 [x]

- [x] 5a. **合格**——0个大问题，0个小问题
- [x] 5d. 记录到review-log.md

## 审计员签字

- 审计结论：✅ 合格
- 日期：2025-01-24
