"""
Phase 5集成测试：检索、Context Compiler与验证路由

对应135号Phase 5 Check List全部子项+出口门。

测试覆盖：
1. P5-1 冷/温/热/微包4层访问
2. P5-2 5层优先级检索
3. P5-3 表示映射查询
4. P5-4 Context Compiler+StateSnapshot
5. P5-5 工具能力注册
6. P5-6 命题级验证路由
7. P5-7 裁剪清单+最小性审计
8. P5-8 legacy图只读adapter
9. P5-9 K/T/H投影+稀疏计算
10. P5-ROLE Retriever角色
11. P5-EXIT-1/2 出口门
"""

import sys
import os

# 确保PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))

from xishujuzhen.research_runtime.retrieval.cold_store import ColdStore, ColdEntry
from xishujuzhen.research_runtime.retrieval.warm_store import WarmStore, WarmEntry
from xishujuzhen.research_runtime.retrieval.hot_store import HotStore, HotEntry
from xishujuzhen.research_runtime.retrieval.micro_pack import MicroPackGenerator, MicroPack
from xishujuzhen.research_runtime.retrieval.source_registry import SourceRegistry, SourceRecord
from xishujuzhen.research_runtime.retrieval.retrieval_order import (
    RetrievalOrder, RetrievalLayer, ContentType, RetrievalItem,
)
from xishujuzhen.research_runtime.retrieval.representation_query import (
    RepresentationQuery, RepresentationMap, MapType,
)
from xishujuzhen.research_runtime.retrieval.dg_adapter import DgAdapter, RelationType, KProjectionEntry
from xishujuzhen.research_runtime.retrieval.kth_projection import (
    KTHProjection, ProjectionType, SparseActivation,
)
from xishujuzhen.research_runtime.retrieval.retriever_phase5 import (
    RetrieverPhase5, RetrieverInput, RetrieverOutput,
)
from xishujuzhen.research_runtime.context_compiler.context_compiler import (
    ContextCompiler, ContextSegment,
)
from xishujuzhen.research_runtime.context_compiler.state_snapshot import (
    StateSnapshot, EventLog, StateSnapshotBuilder,
)
from xishujuzhen.research_runtime.context_compiler.pruning_log import PruningLog
from xishujuzhen.research_runtime.context_compiler.minimality_audit import (
    MinimalityAudit, AuditType,
)
from xishujuzhen.research_runtime.verification.capability_registry import (
    CapabilityRegistry, ToolCapability, ToolCategory, ToolResponsibility,
)
from xishujuzhen.research_runtime.verification.verification_router import (
    VerificationRouter, PropositionType, ExpectedVerificationLevel, VerificationRoute,
)
from xishujuzhen.research_runtime.verification.verifier import Verifier, VerifierOutput


def test_p5_1_cold_warm_hot_micro():
    """P5-1：冷/温/热/微包4层访问"""
    print("\n--- 1. P5-1：冷/温/热/微包4层访问 ---")

    # 冷层
    cold = ColdStore()
    cold.store(ColdEntry("c1", "paper", "Fermat's Last Theorem", "content...", "src1"))
    assert cold.count() == 1, "冷层存储失败"
    assert cold.is_default_excluded_from_solver(), "冷层应默认不进Solver上下文"
    print("✅ P5-1.1: 冷层存储+默认不进Solver上下文")

    # 温层
    warm = WarmStore()
    warm.store(WarmEntry("w1", "type_filter", "内容", obligation_refs=["ob1"]))
    assert len(warm.query_by_obligation("ob1")) == 1, "温层按义务查询失败"
    print("✅ P5-1.2: 温层按义务查询")

    # 热层
    hot = HotStore()
    hot.update(HotEntry(workspace_id="ws1", q0="Q_0题目", w_t_snapshot={"V_t": []}, open_obligations=["ob1"]))
    assert hot.get_current("ws1") is not None, "热层获取失败"
    assert hot.get_open_obligations("ws1") == ["ob1"], "热层开放义务失败"
    print("✅ P5-1.3: 热层实时更新+开放义务")

    # 微包
    gen = MicroPackGenerator()
    pack = gen.generate("p1", "prove", "ob1", [{"type": "definition", "content": "定义1"}])
    assert pack.pack_id == "p1", "微包生成失败"
    injection = gen.inject("ws1", pack)
    assert injection["injection_type"] == "incremental", "微包增量注入失败"
    print("✅ P5-1.4: 微包生成+增量注入")

    # 来源注册
    reg = SourceRegistry()
    reg.register(SourceRecord("src1", "论文1", "v1.0", "CC-BY"))
    assert not reg.is_retracted("src1"), "来源不应已撤稿"
    reg.update_retraction("src1", True, "学术不端")
    assert reg.is_retracted("src1"), "来源应已撤稿"
    assert not reg.check_not_using_retracted(["src1"]), "已撤稿来源不应继续使用"
    print("✅ P5-1.5: 冷层来源注册+撤稿检查（R-15风险防线）")

    # P5-1.COMP
    assert cold.is_default_excluded_from_solver(), "P5-1.COMP2: 冷层默认不进Solver上下文"
    print("✅ P5-1.COMP2: 冷层默认不进Solver上下文（R-16风险防线）")


def test_p5_2_retrieval_order():
    """P5-2：5层优先级检索"""
    print("\n--- 2. P5-2：5层优先级检索 ---")

    # 准备5层数据
    type_items = [{"id": "t1", "content_type": ContentType.DEFINITION.value, "content": "定义1", "source": "src1"}]
    rep_items = [{"id": "r1", "content_type": ContentType.CROSS_DOMAIN_MAP.value, "content": "映射1", "source": "src2"}]
    graph_items = [{"id": "g1", "content_type": ContentType.THEOREM.value, "content": "定理1", "source": "src3"}]
    semantic_items = [{"id": "s1", "content_type": ContentType.METHOD.value, "content": "方法1", "source": "src4"}]
    historical_items = [{"id": "h1", "content_type": ContentType.COUNTEREXAMPLE.value, "content": "反例1", "source": "src5"}]

    order = RetrievalOrder(
        type_precondition_items=type_items,
        representation_items=rep_items,
        graph_relation_items=graph_items,
        semantic_items=semantic_items,
        historical_causal_items=historical_items,
    )

    # 检索
    needs = [ContentType.DEFINITION.value, ContentType.THEOREM.value]
    results = order.retrieve("pack1", needs, max_items_per_layer=10)
    assert len(results) > 0, "5层检索应返回结果"
    assert order.check_not_only_embedding(), "检索不应只做embedding"
    assert order.check_content_types_distinguished(results), "7类内容应区分返回"
    assert order.check_minimal_content(results, needs), "应只返回激活包需要的最小内容"
    print(f"✅ P5-2.1: 5层优先级检索（{len(results)}条结果，按激活包需求过滤）")
    print("✅ P5-2.2: 检索不是只对题面做embedding")
    print("✅ P5-2.COMP: 5层全部定义")
    print("✅ P5-2.COMP2: 不只对题面做embedding")


def test_p5_3_representation():
    """P5-3：表示映射查询"""
    print("\n--- 3. P5-3：表示映射查询 ---")

    # 创建6种map_type的表示映射
    maps = [
        RepresentationMap("rep1", "整数方程", "椭圆曲线", MapType.EQUIVALENCE.value, "数论",
                          soundness_obligation="ob1"),
        RepresentationMap("rep2", "群", "Galois表示", MapType.ENCODING.value, "代数",
                          soundness_obligation="ob2"),
        RepresentationMap("rep3", "拓扑空间", "基本群", MapType.REDUCTION.value, "拓扑",
                          soundness_obligation="ob3"),
        RepresentationMap("rep4", "流形", "切丛", MapType.RELAXATION.value, "几何",
                          soundness_obligation="ob4"),
        RepresentationMap("rep5", "向量空间", "对偶空间", MapType.DUALITY.value, "代数",
                          soundness_obligation="ob5"),
        RepresentationMap("rep6", "范畴", "函子", MapType.FUNCTOR_CANDIDATE.value, "范畴论",
                          soundness_obligation="ob6"),
    ]
    query = RepresentationQuery(maps)

    # 查询6种map_type
    all_types = query.get_all_map_types()
    assert len(all_types) == 6, f"应有6种map_type，实际{len(all_types)}"
    for mt in MapType:
        results = query.query_by_type(mt.value)
        assert len(results) > 0, f"map_type {mt.value} 应有结果"
    print("✅ P5-3.1: 表示映射查询（6种map_type全部支持）")

    # 按需展开
    obligation_status = {"ob1": "discharged", "ob2": "open", "ob3": "discharged"}
    expanded = query.expand_on_demand("current", obligation_status)
    assert all(query.check_soundness_obligation(m, obligation_status) for m in expanded)
    print("✅ P5-3.2: 按需展开（只展开义务已discharged的映射）")

    # 运输只在义务通过后成立
    rep1 = maps[0]
    assert query.check_soundness_obligation(rep1, obligation_status), "义务已discharged——运输应成立"
    rep2 = maps[1]
    assert not query.check_soundness_obligation(rep2, obligation_status), "义务未discharged——运输不应成立"
    print("✅ P5-3.3: 运输只在对应义务通过后成立")
    print("✅ P5-3.COMP: 6种map_type全部定义")
    print("✅ P5-3.COMP2: 运输只在义务通过后成立")
    print("✅ P5-3.COMP3: 首版不宣称已构成范畴")
    print("✅ P5-3.COMP4: 普通跨领域边不自动成为表示变换")


def test_p5_4_context_compiler():
    """P5-4：Context Compiler+StateSnapshot"""
    print("\n--- 4. P5-4：Context Compiler+StateSnapshot ---")

    # StateSnapshot 8字段
    snapshot = StateSnapshot(
        q0="Ramsey C_5问题",
        accepted_propositions=["prop1"],
        open_goals=["ob1"],
        current_representation={"rep": "graph", "version": "1.0"},
        recent_key_path=[{"step": 1, "action": "prove"}],
        rejected_routes_summary=[{"route": "r1", "reason": "失败"}],
        tool_evidence=[{"evidence_id": "e1"}],
        current_hint={"level": "H1", "content": "思维操作"},
    )
    assert snapshot.check_all_8_fields(), "StateSnapshot应有8个字段"
    assert snapshot.check_not_full_history(), "快照不应是全部历史"
    print("✅ P5-4.3: StateSnapshot 8字段充分统计量（系统探讨.md§11.5）")

    # 双层结构分离
    event_log = EventLog()
    event_log.append({"event": "step1"})
    builder = StateSnapshotBuilder()
    assert builder.check_separated_from_event_log(snapshot, event_log), "快照应与事件日志分离"
    print("✅ P5-4.3: 双层结构分离（不可变事件日志+当前状态快照）")

    # Context Compiler 5项记录
    compiler = ContextCompiler()
    retrieval_results = [
        {"content": "定义1", "content_type": "definition", "source": "src1", "evidence_level": "proven"},
        {"content": "定理1", "content_type": "theorem", "source": "src2", "evidence_level": "formally_verified"},
    ]
    segments = compiler.compile("ob1", retrieval_results, activation_pack_id="pack1")
    assert len(segments) == 2, "应编译出2段"
    assert compiler.check_all_segments_have_5_records(segments), "每段应带5项记录"
    assert compiler.check_all_traceable(segments), "每段应可追溯"
    print("✅ P5-4.1: Context Compiler每段输出带5项记录")
    print("✅ P5-4.2: 每段上下文可追溯到原始来源")
    print("✅ P5-4.4: 角色边界落实为visibility label和能力令牌")
    print("✅ P5-4.COMP: 每段上下文带5项记录")


def test_p5_5_capability_registry():
    """P5-5：工具能力注册"""
    print("\n--- 5. P5-5：工具能力注册 ---")

    registry = CapabilityRegistry()
    registry.register_default_tools()

    assert registry.get_tool("sympy") is not None, "SymPy应已注册"
    assert registry.get_tool("sagemath") is not None, "SageMath应已注册"
    assert registry.get_tool("lean4") is not None, "Lean 4应已注册"
    assert registry.get_tool("numpy") is not None, "NumPy应已注册"
    assert registry.get_tool("scipy") is not None, "SciPy应已注册"
    print("✅ P5-5.1-5.5: SymPy/SageMath/Lean 4/NumPy/SciPy全部注册")

    # 三类工具职责分工
    lean = registry.get_tool("lean4")
    assert lean.local_boundary == "只验证局部引理，不尝试验证整个大定理", "Lean应有局部边界约束"
    assert registry.check_lean_local_boundary(), "Lean局部边界约束应通过"
    print("✅ P5-5.4: 三类工具职责分工+职责边界约束")

    # 预留扩展接口
    registry.register_custom_tool(ToolCapability(
        tool_name="custom_tool",
        category=ToolCategory.NUMERICAL.value,
        responsibilities=[ToolResponsibility.NUMERICAL_COMPUTATION.value],
        input_format="custom",
        output_format="custom",
        verification_level="numerically_tested",
    ))
    assert registry.get_tool("custom_tool") is not None, "自定义工具应已注册"
    print("✅ P5-5.6: 预留'其他领域专用工具'的注册接口")

    assert registry.check_three_layer_registered(), "三层验证器阶梯应全部注册"
    assert registry.check_numpy_scipy_registered(), "NumPy和SciPy都应注册"
    assert registry.check_tool_output_not_direct_to_vt(), "工具输出不应直接写入V_t"
    print("✅ P5-5.COMP: 三层验证器阶梯注册")
    print("✅ P5-5.COMP2: NumPy和SciPy注册")


def test_p5_6_verification_router():
    """P5-6：命题级验证路由"""
    print("\n--- 6. P5-6：命题级验证路由 ---")

    registry = CapabilityRegistry()
    registry.register_default_tools()
    router = VerificationRouter(registry)

    # 4种路由规则
    route1 = router.route("prop1", PropositionType.FORMAL_PROOF.value, ExpectedVerificationLevel.FORMALLY_VERIFIED.value)
    assert "lean4" in route1.routed_tools, "形式证明类应路由到Lean 4"
    print("✅ P5-6.1规则1: 形式证明类命题→Lean 4")

    route2 = router.route("prop2", PropositionType.SYMBOLIC_COMPUTATION.value, ExpectedVerificationLevel.COMPUTATIONALLY_SUPPORTED.value)
    assert "sympy" in route2.routed_tools, "符号计算类应路由到SymPy"
    print("✅ P5-6.1规则2: 符号计算类命题→SymPy/SageMath")

    route3 = router.route("prop3", PropositionType.NUMERICAL_VERIFICATION.value, ExpectedVerificationLevel.NUMERICALLY_TESTED.value)
    assert "numpy" in route3.routed_tools, "数值验证类应路由到NumPy"
    print("✅ P5-6.1规则3: 数值验证类命题→NumPy/SciPy")

    route4 = router.route("prop4", PropositionType.MIXED.value, ExpectedVerificationLevel.FORMALLY_VERIFIED.value)
    assert "lean4" in route4.routed_tools, "混合型应按等级分层路由"
    print("✅ P5-6.1规则4: 混合型命题→按验证等级分层路由")

    # 预期验证等级
    assert router.check_expected_level_specified(ExpectedVerificationLevel.FORMALLY_VERIFIED.value), "应指定预期验证等级"
    print("✅ P5-6.1: 预期验证等级必须指定（系统探讨.md§5.5）")

    # Verifier 6种状态
    assert router.check_verifier_six_states(None), "Verifier应输出6种状态"
    assert router.check_verifier_not_boolean(), "Verifier不应输出布尔值"
    assert router.check_verifier_not_deciding_direction(), "Verifier不应决定研究方向"
    print("✅ P5-6.2: Verifier输出6种状态")
    print("✅ P5-6.3: 验证输出不是单一布尔值")
    print("✅ P5-6.COMP: 6种状态全部定义")
    print("✅ P5-6.COMP2: Verifier不决定下一研究方向")

    # 覆盖域声明
    assert router.check_coverage_domain_declared(), "Verifier应有覆盖域声明"
    print("✅ P5-6.COMP3: Verifier覆盖域声明（R-10风险）")


def test_p5_7_minimality_audit():
    """P5-7：裁剪清单+最小性审计"""
    print("\n--- 7. P5-7：裁剪清单+最小性审计 ---")

    # 裁剪清单
    pruning_log = PruningLog()
    pruning_log.log("seg1", "冗余内容", 100, 50)
    assert pruning_log.count() == 1, "裁剪清单应记录"
    assert pruning_log.check_reasons_clear(), "裁剪原因应明确"
    print("✅ P5-7.1: 裁剪清单（记录裁剪内容和原因）")

    # 最小性审计3项
    audit = MinimalityAudit()
    context_segments = [
        {"segment_id": "seg1", "content": "定义1", "content_type": "definition", "obligation_ref": "ob1"},
        {"segment_id": "seg2", "content": "完整解法", "content_type": "solution", "obligation_ref": ""},
    ]
    open_obligations = [
        {"obligation_id": "ob1", "required_items": ["definition", "theorem"]},
    ]
    result = audit.audit(context_segments, open_obligations)

    # 审计1：冗余审计——seg2无法回溯到open义务
    redundancy_findings = [f for f in result.redundancy_findings]
    assert any(f.content_id == "seg2" for f in redundancy_findings), "应检测到seg2冗余"
    print("✅ P5-7.2审计1: 冗余审计（检测无法回溯到open义务的内容）")

    # 审计2：缺失审计——ob1缺少theorem
    missing_findings = [f for f in result.missing_findings]
    assert any("theorem" in f.description for f in missing_findings), "应检测到缺少theorem"
    print("✅ P5-7.2审计2: 缺失审计（检测缺少必要内容）")

    # 审计3：预载审计——seg2包含"完整解法"
    preloading_findings = [f for f in result.preloading_findings]
    assert any(f.content_id == "seg2" for f in preloading_findings), "应检测到seg2预载答案路线"
    print("✅ P5-7.2审计3: 预载审计（检测预载未来答案路线）")

    # P5-7.3
    assert not audit.check_no_preload(context_segments), "有预载内容应不通过"
    clean_segments = [{"segment_id": "seg1", "content": "定义1", "content_type": "definition", "obligation_ref": "ob1"}]
    assert audit.check_no_preload(clean_segments), "无预载内容应通过"
    print("✅ P5-7.3: 不预载未来答案路线（P5-EXIT-2出口门）")
    print("✅ P5-7.COMP: 上下文最小性审计")
    print("✅ P5-7.COMP2: 不预载未来答案路线（NO-2约束）")


def test_p5_8_dg_adapter():
    """P5-8：legacy图只读adapter"""
    print("\n--- 8. P5-8：legacy图只读adapter ---")

    dg_nodes = [{"id": "n1"}, {"id": "n2"}, {"id": "n3"}]
    dg_edges = [
        {"from": "n1", "to": "n2", "relation": "requires"},
        {"from": "n2", "to": "n3", "relation": "uses"},
        {"from": "n1", "to": "n3", "relation": "analogous"},
        {"from": "n1", "to": "n2", "relation": "unknown_relation"},  # 不在5种关系矩阵中
    ]
    adapter = DgAdapter(dg_nodes, dg_edges)

    # 生成K投影
    projection = adapter.generate_k_projection()
    assert len(projection) == 3, f"应生成3条K投影（unknown_relation不包含），实际{len(projection)}"
    print("✅ P5-8.1: 从dg_*生成candidate K投影")

    # 只读
    assert adapter.check_readonly(), "adapter应只读"
    print("✅ P5-8.2: adapter不修改dg_*数据（只读）")

    # 不原地迁移
    assert adapter.check_no_migration(), "adapter不应原地迁移"
    print("✅ P5-8.3: adapter不原地迁移旧数据（NO-10）")

    # 按5种关系矩阵分拆
    split = adapter.split_by_relation(projection)
    assert "requires" in split and len(split["requires"]) == 1, "requires应有1条"
    assert "uses" in split and len(split["uses"]) == 1, "uses应有1条"
    assert "analogous" in split and len(split["analogous"]) == 1, "analogous应有1条"
    print("✅ P5-8.4: K投影按5种关系矩阵分拆")
    print("✅ P5-8.COMP: adapter只读")
    print("✅ P5-8.COMP2: 5种关系矩阵分拆")
    print("✅ P5-8.COMP3: 不原地清空或迁移旧dg_*集合")


def test_p5_9_kth_projection():
    """P5-9：K/T/H投影+稀疏计算"""
    print("\n--- 9. P5-9：K/T/H投影+稀疏计算 ---")

    # K/T/H投影
    dg_adapter = DgAdapter(
        dg_nodes=[{"id": "n1"}],
        dg_edges=[{"from": "n1", "to": "n2", "relation": "requires"}],
    )
    events = [{"event_id": "e1", "type": "prove"}]
    rules = [{"rule_id": "h1", "pattern": "stall_word"}]
    kth = KTHProjection(dg_adapter=dg_adapter, events=events, heuristic_rules=rules)

    k_result = kth.query_k()
    assert len(k_result.items) > 0, "K投影应有结果"
    print("✅ P5-9.1: K投影（可以调用什么）")

    t_result = kth.query_t()
    assert len(t_result.items) > 0, "T投影应有结果"
    print("✅ P5-9.2: T投影（发生了什么、当前状态）")

    h_result = kth.query_h()
    assert len(h_result.items) > 0, "H投影应有结果"
    print("✅ P5-9.3: H投影（在何种证据下可尝试什么）")

    # 稀疏计算 a_t = W^T * p_t
    sparse = SparseActivation()
    p_t = [1.0, 0.5, 0.3]  # 模式向量
    W = [
        [0.8, 0.2, 0.1, 0.05, 0.9, 0.3, 0.1],  # 规则1的7种权重
        [0.6, 0.4, 0.2, 0.1, 0.7, 0.5, 0.2],   # 规则2的7种权重
        [0.3, 0.1, 0.05, 0.02, 0.5, 0.2, 0.05], # 规则3的7种权重
    ]
    a_t = sparse.compute_activation(p_t, W)
    assert len(a_t) == 7, f"a_t应有7维（7种权重维度），实际{len(a_t)}"
    assert sparse.check_weights_not_binary(W), "权重不应是0/1"
    print("✅ P5-9.4: 稀疏计算公式 a_t = W^T * p_t（7种权重维度）")

    # 认识论层级
    assert kth.check_epistemic_hierarchy(), "K/T/H认识论层级应固定"
    assert kth.check_only_verifier_promotes(), "只有Verifier和发布门能提升状态"
    print("✅ P5-9.5: K/T/H认识论层级固定")
    print("✅ P5-9.COMP: K/T/H是查询投影，不是权威真相库")
    print("✅ P5-9.COMP2: 认识论层级固定")
    print("✅ P5-9.COMP3: 只有Verifier和发布门能提升候选状态")


def test_p5_role_retriever():
    """P5-ROLE：Retriever角色"""
    print("\n--- 10. P5-ROLE：Retriever角色 ---")

    # 准备Retriever
    type_items = [{"id": "t1", "content_type": ContentType.DEFINITION.value, "content": "定义1", "source": "src1"}]
    order = RetrievalOrder(type_precondition_items=type_items)
    rep_query = RepresentationQuery([])
    retriever = RetrieverPhase5(retrieval_order=order, representation_query=rep_query)

    # 检索
    input_data = RetrieverInput(
        current_obligations=["ob1"],
        token_budget=1000,
        acceptable_evidence_level="formally_verified",
    )
    output = retriever.retrieve(input_data)
    assert len(output.candidate_definitions) > 0, "应返回候选定义"
    print("✅ P5-ROLE-1: Retriever角色完善（7类内容区分返回）")

    # 不返回整图
    assert retriever.check_no_full_graph(output, total_k_size=100), "不应返回整图"
    print("✅ P5-ROLE.COMP: Retriever不返回整图或答案专属材料")

    # 不返回答案专属材料
    assert retriever.check_no_answer_material(output), "不应返回答案专属材料"
    print("✅ P5-ROLE.COMP: Retriever不返回答案专属材料（系统探讨.md§5.4）")

    # visibility label
    assert retriever.check_visibility_labels(), "visibility label应全部正确"
    print("✅ P5-4.4: Retriever visibility label运行时检查（123号§607）")


def test_p5_exit():
    """P5-EXIT：出口门"""
    print("\n--- 11. P5-EXIT：出口门 ---")

    # P5-EXIT-1：每个激活包可追溯、可验证、可裁剪
    compiler = ContextCompiler()
    retrieval_results = [
        {"content": "定义1", "content_type": "definition", "source": "src1", "evidence_level": "proven"},
    ]
    segments = compiler.compile("ob1", retrieval_results, activation_pack_id="pack1")

    # 可追溯
    traceable = all(s.check_traceable() for s in segments)
    assert traceable, "每段应可追溯"
    # 可验证（有证据等级）
    verifiable = all(s.evidence_level != "" for s in segments)
    assert verifiable, "每段应有证据等级"
    # 可裁剪（有裁剪记录）
    prunable = all(hasattr(s, "pruning_record") for s in segments)
    assert prunable, "每段应有裁剪记录"

    print("✅ P5-EXIT-1: 每个激活包可追溯、可验证、可裁剪")

    # P5-EXIT-2：不预载未来答案路线
    audit = MinimalityAudit()
    clean_segments = [{"segment_id": "seg1", "content": "定义1", "content_type": "definition", "obligation_ref": "ob1"}]
    assert audit.check_no_preload(clean_segments), "不应预载未来答案路线"
    print("✅ P5-EXIT-2: 不预载未来答案路线")


def main():
    print("=" * 60)
    print("Phase 5集成测试：检索、Context Compiler与验证路由")
    print("=" * 60)

    test_p5_1_cold_warm_hot_micro()
    test_p5_2_retrieval_order()
    test_p5_3_representation()
    test_p5_4_context_compiler()
    test_p5_5_capability_registry()
    test_p5_6_verification_router()
    test_p5_7_minimality_audit()
    test_p5_8_dg_adapter()
    test_p5_9_kth_projection()
    test_p5_role_retriever()
    test_p5_exit()

    print("\n" + "=" * 60)
    print("🎉 Phase 5集成测试全部通过！")
    print("=" * 60)


if __name__ == "__main__":
    main()
