"""
Phase 3: 离线候选启发

对应133号Check List。

Phase 3目标：发现候选规则，但绝不在线自动提示。

模块结构：
- models.py: HeuristicRule dataclass（覆盖127号§7全部字段）
- state_aligner.py: P3-1/P3-2 状态对齐+共同状态+分叉点检测
- rule_extractor.py: P3-3 LHS/interface/RHS/guard/eta抽取
- activation_packet.py: P3-4 H0/H1/H2激活包设计
- leakage_audit.py: P3-5/P3-6 答案等价性审计+泄漏审计
- rule_store.py: P3-7/P3-8 规则存储+生命周期管理
- sparse_view.py: P3-9 H图稀疏表示
- matcher.py: P3-ROLE-1 HeuristicMatcher类（离线模式）
- migrate.py: ArangoDB migration
- test_phase3.py: 集成测试

冻结声明（127号§7/§9）：
- 模式匹配必须返回被匹配实体、字段约束和时间窗口
- 动作只能提出候选状态扩展，真正写入V_t仍需Reducer与Verifier
- 激活包不应直接把目标结论加入V_t
- candidate规则禁止在线自动提示（R-4核心防线）
- candidate规则禁止自动写入H图（NO-8约束）
"""
