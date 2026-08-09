# Master Agent 审计 Checklist — AoPS omni_math #3988

- **problem_id**: omni_math_003988
- **审计时间**: 2025-01-24
- **来源**：AoPS omni_math，IMO Shortlist代数题（difficulty 9.0）

## Phase 0: 加载审计材料 [x]

- [x] 0a. 从ArangoDB读取完整profile ✅
- [x] 0b. 读problem.lean——求所有f:Z→Z满足f(f(m)+n)+f(m)=f(n)+f(3m)+2014。解答：m=0得准周期性关系f(c+n)=f(n)+2014，暗示线性，假设f(n)=an+b代入比较系数得a=2,b=1007。答案：f(m)=2m+1007 ✅
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
- [x] 2b. 解答理解准确——m=0得准周期性→线性假设f(n)=an+b→比较系数a=2,b=1007。subagent发现原解答代数错误（b=2014应为1007）但boxed答案正确，已标注 ✅
- [x] 2c. functional_equation_periodicity vs special_substitution_linear_assumption区分清晰 ✅
- [x] 2d. key_insight="m=0得f(c+n)=f(n)+2014的准周期性关系，强烈暗示f是线性函数，将函数方程转化为系数求解"——准确 ✅
- [x] 2e. QA序列逐轮审查：7轮覆盖观察→列举→小尝试→m=0特殊赋值→准周期性识别→线性假设+系数比较→完整验证，合理 ✅
- [x] 2f. R5 kb=True正确（从准周期性推断线性形式是知识瓶颈），R6 tb正确（系数比较代数化简是思维瓶颈）✅
- [x] 2g-2p. 全部通过 ✅

## Phase 3-6: 全部通过 [x]

## Phase 5: 审计结论 [x]

- [x] 5a. **合格**——0个大问题，0个小问题（原解答代数错误b=2014应为1007已被subagent发现并标注，boxed答案正确）
- [x] 5d. 记录到review-log.md

## 审计员签字

- 审计结论：✅ 合格
- 日期：2025-01-24
