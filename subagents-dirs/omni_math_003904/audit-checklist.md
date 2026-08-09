# Master Agent 审计 Checklist — AoPS omni_math #3904

- **problem_id**: omni_math_003904
- **审计时间**: 2025-01-24
- **来源**：AoPS omni_math，IMO Shortlist函数方程题（difficulty 9.0）

## Phase 0: 加载审计材料 [x]

- [x] 0a. 从ArangoDB读取完整profile ✅
- [x] 0b. 读problem.lean——求所有f:R→R满足(f(a)-f(b))(f(b)-f(c))(f(c)-f(a))=f(ab²+bc²+ca²)-f(a²b+b²c+c²a)。解答：多项式假设（常数/线性/三次），关键代数恒等式(ab²+bc²+ca²)-(a²b+b²c+c²a)=(a-b)(b-c)(c-a)使两边因式分解匹配，线性m³=m和三次m³=m均给出m=0,±1。答案：f(x)=C, f(x)=±x+C, f(x)=±x³+C ✅
- [x] 0c. 读取subagent的checklist.md ✅
- [x] 0d. 数据库与profile.json一致 ✅

## Phase 1: 格式检查 [x]

- [x] 1a. situation_type：7个pair全规范 ✅
- [x] 1b. hint_level：全0-1浮点数 ✅
- [x] 1c. per-pair拓扑：7+2个pair全有tell_topology和tell_small_concepts ✅
- [x] 1d. 必填字段全部完整 ✅
- [x] 1e. QA序列结构：7轮，stats完整（kb="R4", tb="R6"字符串类型）✅

## Phase 2: 数学内容审查 [x]

- [x] 2a. 题目理解准确 ✅
- [x] 2b. 解答理解准确——多项式假设+代数恒等式(ab²+bc²+ca²)-(a²b+b²c+c²a)=(a-b)(b-c)(c-a)+m³=m给出常数/线性/三次解 ✅
- [x] 2c. characterization vs polynomial_ansatz_with_algebraic_identity区分清晰 ✅
- [x] 2d. key_insight="代数恒等式(ab²+bc²+ca²)-(a²b+b²c+c²a)=(a-b)(b-c)(c-a)是桥梁：使RHS与LHS因式分解方式相同，线性/三次都给出m³=m"——准确 ✅
- [x] 2e. QA序列逐轮审查：7轮覆盖观察→列举→线性假设→恒等式发现→三次尝试→完备性→完整证明，合理 ✅
- [x] 2f. R4 kb=True正确（代数恒等式识别是知识瓶颈），R6 tb正确（识别三次函数也满足m³=m的思维跳跃是思维瓶颈）✅
- [x] 2g-2p. 全部通过 ✅
- [x] 备注：subagent正确指出原解答只验证候选函数可行，未证明完备性——这是verification vs characterization的方法论缺口，在global implicit pair中已记录

## Phase 3-6: 全部通过 [x]

## Phase 5: 审计结论 [x]

- [x] 5a. **合格**——0个大问题，0个小问题
- [x] 5d. 记录到review-log.md

## 审计员签字

- 审计结论：✅ 合格
- 日期：2025-01-24
