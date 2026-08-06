"""
Phase 7集成测试——表示运输、长证明和高级数学分析。

对应137号Phase 7 Check List（v4版本）。

测试覆盖：
- P7-1：表示映射12字段+6枚举+soundness义务+转换保真3项+费马链条4环节+groupoid 2限定词
- P7-2：费马案例3层阶梯+6条大师启发+3项能力区分+阶梯门控
- P7-3：3类等价判定+交换图+5运输对象
- P7-4：3项一致性检查+3步粘合+4种候选障碍+HoleTypeError
- P7-5：e-graph 4核心组件+equality saturation
- P7-6：轨迹嵌入+4种对齐方法+GeometryMisuseError
- P7-7：4限定词检查+持久同调+3基线比较
- P7-8：3限定词检查+3方向+3基线比较+分阶段顺序+防止过早包装+4误标注防线
- P7-MATH：3级别标注+自动验证+ManualLabelOverrideError
- P7-ROLE：Verifier覆盖域+8角色+CapabilityToken+PermissionError
- P7-EXIT：3量化比较+ExitGateFailureError+LabelDowngradeWarning
- P7-STOP：StopConditionTriggeredError+MislabelError
"""

import sys
import os

# 确保可以导入xishujuzhen模块
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))

from xishujuzhen.research_runtime.representation.representation_map import (
    RepresentationMap, MapType, RepresentationMapStore, MOTHER_CROSS_REP_EXAMPLES,
)
from xishujuzhen.research_runtime.representation.soundness_obligation import (
    SoundnessObligationTracker, SoundnessTransporter, SoundnessViolationError,
)
from xishujuzhen.research_runtime.representation.transport_fidelity import (
    TransportFidelityVerifier,
)
from xishujuzhen.research_runtime.representation.fermat_chain import (
    FermatChainBuilder, MasterHeuristicRecognizer, FermatLevelGate,
    CapabilityDistinctionChecker, FermatLevel, LevelOrderViolationError,
    FERMAT_CHAIN_SEGMENTS, MASTER_HEURISTICS, CAPABILITY_DISTINCTION,
    LEVEL1_INFERENCE_CHAIN, FERMAT_CHAIN_FORMS,
)
from xishujuzhen.research_runtime.representation.source_version import (
    SourceVersion, SourceVersionMonitor,
)
from xishujuzhen.research_runtime.representation.groupoid_check import (
    GroupoidChecker, GroupoidViolationError,
)
from xishujuzhen.research_runtime.representation.path_equivalence import (
    PathEquivalenceClassifier, ProofPath, ProofStep, EquivalenceClass,
)
from xishujuzhen.research_runtime.representation.commutative_diagram import (
    CommutativeDiagramVerifier, CommutativeSquare,
)
from xishujuzhen.research_runtime.representation.transport_objects import (
    ObjectTransporter, TransportableObject, TransportObjectType,
)
from xishujuzhen.research_runtime.representation.local_view import (
    LocalView, LocalViewConsistencyChecker, LayeredGluer,
)
from xishujuzhen.research_runtime.representation.hole_detector import (
    HoleDetector, CandidateHole, HoleType, HoleTypeError,
)
from xishujuzhen.research_runtime.representation.egraph import (
    EGraph, ENode, EClass, UnionFind, EqualitySaturation,
)
from xishujuzhen.research_runtime.representation.trajectory_alignment import (
    TrajectoryEmbedder, TrajectoryAligner, Trajectory, TrajectoryPoint,
)
from xishujuzhen.research_runtime.representation.geometry_guard import (
    GeometryGuard, GeometryMisuseError, GeometryPurpose,
)
from xishujuzhen.research_runtime.representation.tda_gate import (
    TDAGate, InsufficientFormalizationError,
)
from xishujuzhen.research_runtime.representation.persistent_homology import (
    PersistentHomology,
)
from xishujuzhen.research_runtime.representation.baseline_comparison import (
    BaselineComparator, BaselineComparisonResult,
    ExitGateFailureError, LabelDowngradeWarning, StopConditionTriggeredError,
)
from xishujuzhen.research_runtime.representation.hott_gate import HoTTGate
from xishujuzhen.research_runtime.representation.hott_directions import (
    HoTTDirections,
)
from xishujuzhen.research_runtime.representation.phase_gate import (
    PhaseGate, PrematureMathPackagingGuard,
)
from xishujuzhen.research_runtime.representation.mislabel_guard import (
    MislabelGuard, MislabelError, EmbeddingMisuseError,
)
from xishujuzhen.research_runtime.representation.math_label import (
    MathLabeler, MathLabel, ManualLabelOverrideError,
)


def run_test(name: str, test_fn):
    """运行单个测试。"""
    try:
        test_fn()
        print(f"✅ {name}")
        return True
    except Exception as e:
        print(f"❌ {name}: {e}")
        import traceback
        traceback.print_exc()
        return False


# =========================================================================
# P7-1：类型化representation_maps和soundness义务
# =========================================================================

def test_p7_1_1_representation_map_12_fields():
    """P7-1.1：RepresentationMap 12字段+6枚举。"""
    rep = RepresentationMap(
        rep_id="rep_001",
        source_form="整数方程",
        target_form="椭圆曲线",
        map_type="encoding",
        domain="数论",
        preconditions=["FLT反例"],
        forward_transport="Frey曲线构造",
        backward_transport="Frey曲线还原",
        preserved_invariants=["不可约性"],
        lost_information=["整数结构"],
        soundness_obligation="ob_001",
        evidence=["ev_001", "ev_002"],
    )
    d = rep.to_dict()
    # 12字段全部存在
    assert len(d) == 12, f"应有12字段，实际{len(d)}"
    # 6枚举
    assert len(MapType) == 6, f"应有6枚举，实际{len(MapType)}"
    # map_type正确
    assert rep.map_type == MapType.ENCODING
    # 不存在的map_type抛ValueError
    try:
        MapType.from_string("invalid_type")
        assert False, "应抛ValueError"
    except ValueError:
        pass


def test_p7_1_2_soundness_obligation_enforced():
    """P7-1.2/P7-1.COMP：soundness义务强制——义务未通过时运输抛SoundnessViolationError。"""
    tracker = SoundnessObligationTracker()
    transporter = SoundnessTransporter(tracker)
    transporter.register_obligation("ob_001")

    rep = RepresentationMap(
        rep_id="rep_001", source_form="A", target_form="B",
        map_type="equivalence", domain="test",
        forward_transport="f", soundness_obligation="ob_001",
    )

    # 义务未通过时运输→抛SoundnessViolationError
    try:
        transporter.transport(rep, source_object="test")
        assert False, "应抛SoundnessViolationError"
    except SoundnessViolationError:
        pass

    # 义务通过后运输成功
    tracker.mark_satisfied("ob_001", ["ev_001"])
    result = transporter.transport(rep, source_object="test")
    assert result["obligation_satisfied"] is True


def test_p7_1_2b_transport_fidelity_3_checks():
    """P7-1.2b：转换保真3项验证。"""
    verifier = TransportFidelityVerifier()
    rep = RepresentationMap(
        rep_id="rep_001", source_form="A", target_form="B",
        map_type="equivalence", domain="test",
        forward_transport="f", backward_transport="b",
        preserved_invariants=["inv1"],
        soundness_obligation="ob_001",
    )

    result = verifier.verify_fidelity(
        rep, source_object="x",
        forward_fn=lambda x: x + "_transported",
        backward_fn=lambda x: x.replace("_transported", ""),
        target_consistency_fn=lambda x: "_transported" in x,
        invariant_check_fn=lambda x, invs: True,
    )

    assert result.forward_fidelity is True
    assert result.backward_fidelity is True
    assert result.invariant_preservation is True
    assert result.all_passed is True


def test_p7_1_2c_fermat_chain_4_segments():
    """P7-1.2c：费马案例完整链条4环节。"""
    builder = FermatChainBuilder()
    display = builder.display_chain()
    assert display["chain_complete"] is True
    assert display["n_segments"] == 4
    # 4环节：整数方程→Frey曲线→Galois表示→模形式→更低level模形式
    assert len(display["forms_sequence"]) == 5


def test_p7_1_4_source_version_monitor():
    """P7-1.4：来源版本和撤稿状态监控。"""
    monitor = SourceVersionMonitor()
    monitor.register_source(SourceVersion(
        source_id="src_001", title="Test Paper", version="1.0",
        published_date="2026-01-01", retracted=False, license="MIT",
    ))
    monitor.register_source(SourceVersion(
        source_id="src_002", title="Retracted Paper", version="1.0",
        published_date="2026-01-01", retracted=True, retraction_date="2026-06-01",
    ))

    # 正常来源
    assert monitor.check_version("src_001")["has_version"] is True
    # 撤稿来源但仍在使用
    retraction = monitor.check_retraction("src_002", in_use=True)
    assert retraction["retracted"] is True
    assert retraction["in_use"] is True


def test_p7_1_comp3_groupoid_2_qualifiers():
    """P7-1.COMP3：groupoid 2限定词——可逆且复合封闭。"""
    checker = GroupoidChecker()
    # 可逆且复合封闭
    edges = [("A", "B", "e1"), ("B", "A", "e2"), ("A", "A", "e3"), ("B", "B", "e4")]
    # 注意：需要复合封闭——A→B和B→A存在，A→A也应存在
    result = checker.check_groupoid(edges)
    # 2限定词必须同时检查
    assert result["n_qualifiers_required"] == 2

    # 不满足2限定词时被称为groupoid→抛GroupoidViolationError
    bad_edges = [("A", "B", "e1")]  # 不可逆（无B→A）
    try:
        checker.assert_groupoid(bad_edges)
        assert False, "应抛GroupoidViolationError"
    except GroupoidViolationError:
        pass


def test_p7_1_comp2_not_category():
    """P7-1.COMP2：首版不宣称已构成范畴。"""
    checker = GroupoidChecker()
    result = checker.check_not_category()
    assert result["is_category"] is False
    assert len(result["upgrade_requirements"]) == 4


def test_p7_1_mother_cross_rep_examples():
    """P7-1母本细节：3个跨表示映射例子（母本§8.2位置一逐字保留）。"""
    # 母本§8.2位置一明确列出3个跨表示映射例子
    assert len(MOTHER_CROSS_REP_EXAMPLES) == 3
    examples = {(e["source"], e["target"]) for e in MOTHER_CROSS_REP_EXAMPLES}
    assert ("矩阵表示", "模表示") in examples
    assert ("组合表示", "拓扑表示") in examples
    assert ("整数方程", "椭圆曲线") in examples


# =========================================================================
# P7-2：费马型跨域模块编排
# =========================================================================

def test_p7_2_1_level1_inference_chain():
    """P7-2.1：Level 1推论链。"""
    assert len(LEVEL1_INFERENCE_CHAIN) == 9
    assert "假想FLT反例" in LEVEL1_INFERENCE_CHAIN
    assert "两路汇聚为矛盾" in LEVEL1_INFERENCE_CHAIN


def test_p7_2_1b_6_master_heuristics():
    """P7-2.1b：6条大师启发。"""
    assert len(MASTER_HEURISTICS) == 6
    recognizer = MasterHeuristicRecognizer()
    all_h = recognizer.get_all_heuristics()
    assert len(all_h) == 6

    # 把"谷山—志村"作为全部内容→拒绝
    check = recognizer.check_not_just_taniyama_shimura("谷山—志村")
    assert check["rejected"] is True


def test_p7_2_4_level_gate():
    """P7-2.4/P7-2.COMP：阶梯门控——Level N未通过时进入Level N+1抛LevelOrderViolationError。"""
    gate = FermatLevelGate()

    # Level 1总是可以进入
    assert gate.can_enter_level(FermatLevel.LEVEL_1) is True

    # Level 2需要Level 1通过
    assert gate.can_enter_level(FermatLevel.LEVEL_2) is False
    try:
        gate.enter_level(FermatLevel.LEVEL_2)
        assert False, "应抛LevelOrderViolationError"
    except LevelOrderViolationError:
        pass

    # Level 1通过后可以进入Level 2
    gate.mark_level_passed(FermatLevel.LEVEL_1)
    assert gate.can_enter_level(FermatLevel.LEVEL_2) is True

    # Level 3需要Level 1和2都通过
    try:
        gate.check_not_full_wiles(FermatLevel.LEVEL_3)
        assert False, "应抛LevelOrderViolationError"
    except LevelOrderViolationError:
        pass

    gate.mark_level_passed(FermatLevel.LEVEL_2)
    result = gate.check_not_full_wiles(FermatLevel.LEVEL_3)
    assert result["can_research_level_3"] is True


def test_p7_2_comp3_capability_distinction():
    """P7-2.COMP3：3项能力区分。"""
    checker = CapabilityDistinctionChecker()
    caps = checker.get_all_capabilities()
    assert len(caps) == 3


# =========================================================================
# P7-3：证明路径等价和交换图
# =========================================================================

def test_p7_3_1_path_equivalence_3_classes():
    """P7-3.1：3类等价判定。"""
    classifier = PathEquivalenceClassifier()

    # 改写等价：相同操作，变量名不同
    path_a = ProofPath("a", [
        ProofStep("s1", ["obj1"], "apply_lemma", {"x": "1"}),
    ])
    path_b = ProofPath("b", [
        ProofStep("s1", ["obj1"], "apply_lemma", {"y": "1"}),  # 变量名不同
    ])

    result = classifier.classify(path_a, path_b)
    assert result["equivalence_class"] in [
        EquivalenceClass.REWRITE_EQUIVALENT.value,
        EquivalenceClass.GRANULARITY_EQUIVALENT.value,
    ]


def test_p7_3_2_commutative_diagram():
    """P7-3.2：交换图验证。"""
    verifier = CommutativeDiagramVerifier()
    sq = CommutativeSquare(
        "sq1", "A", "B", "C", "D", "top", "bottom", "left", "right"
    )
    verifier.add_square(sq)
    result = verifier.verify_all_squares()
    assert result["n_squares"] == 1


def test_p7_3_3_5_transport_objects():
    """P7-3.3：5运输对象。"""
    # 5种运输对象类型
    assert len(TransportObjectType) == 5
    types = {t.value for t in TransportObjectType}
    assert types == {"object", "theorem", "invariant", "obligation", "strategy"}

    transporter = ObjectTransporter()
    rep = RepresentationMap(
        rep_id="rep_001", source_form="A", target_form="B",
        map_type="equivalence", domain="test",
        forward_transport="f", soundness_obligation="ob_001",
        preserved_invariants=["inv1"],
    )

    objects = [
        TransportableObject("o1", TransportObjectType.OBJECT, "obj"),
        TransportableObject("o2", TransportObjectType.THEOREM, "thm"),
        TransportableObject("o3", TransportObjectType.INVARIANT, "inv"),
        TransportableObject("o4", TransportObjectType.OBLIGATION, "ob"),
        TransportableObject("o5", TransportObjectType.STRATEGY, "str"),
    ]

    result = transporter.transport_all_types(objects, rep)
    assert result["all_types_covered"] is True
    assert result["n_transported"] == 5


# =========================================================================
# P7-4：局部视图一致性与层式粘合
# =========================================================================

def test_p7_4_1_local_view_3_checks():
    """P7-4.1：3项一致性检查。"""
    checker = LocalViewConsistencyChecker()
    view_a = LocalView("a", {"x", "y"}, {("x", "y"): "rel1"})
    view_b = LocalView("b", {"y", "z"}, {("y", "z"): "rel2"})

    result = checker.full_check(view_a, view_b)
    assert result["all_3_checks_done"] is True
    # 重叠区域识别
    assert "overlap_check" in result
    # 一致性判定
    assert "consistency_check" in result
    # 冲突标记
    assert "conflict_marking" in result


def test_p7_4_2_layered_glue_3_steps():
    """P7-4.2：3步粘合。"""
    gluer = LayeredGluer()
    view_a = LocalView("a", {"x", "y"}, {("x", "y"): "rel1"})
    view_b = LocalView("b", {"y", "z"}, {("y", "z"): "rel2"})

    result = gluer.full_glue(view_a, view_b)
    assert result["all_3_steps_done"] is True
    # 粘合前置检查
    assert "pre_glue_check" in result
    # 合并非重叠区域
    assert "non_overlapping_merge" in result
    # 合并重叠区域
    assert "overlapping_merge" in result


def test_p7_4_3_4_hole_types():
    """P7-4.3：4种候选障碍。"""
    assert len(HoleType) == 4
    detector = HoleDetector()

    # 候选障碍1：无已验证接口
    h = detector.detect_no_verified_interface("region1", "ob1", [])
    assert h is not None
    assert h.hole_type == HoleType.NO_VERIFIED_INTERFACE

    # 候选障碍2：多路线停滞
    h = detector.detect_multi_route_stall(
        [["A", "B"], ["C", "D"]], "missing_construction"
    )
    assert h is not None
    assert h.hole_type == HoleType.MULTI_ROUTE_STALL


def test_p7_4_comp_hole_type_error():
    """P7-4.COMP：洞直接当作同调群元素→抛HoleTypeError。"""
    detector = HoleDetector()
    bad_hole = CandidateHole(
        "hole1", HoleType.NO_VERIFIED_INTERFACE, "test",
        candidate_nature="homology_element",  # 错误标注
    )
    try:
        detector.assert_candidate_obstacle(bad_hole)
        assert False, "应抛HoleTypeError"
    except HoleTypeError:
        pass


# =========================================================================
# P7-5：e-graph
# =========================================================================

def test_p7_5_1_egraph_4_components():
    """P7-5.1：e-graph 4核心组件。"""
    egraph = EGraph()
    # 4核心组件：EClass, ENode, UnionFind, rebuild
    assert hasattr(egraph, "add_enode")  # ENode + EClass
    assert hasattr(egraph, "_uf")        # UnionFind
    assert hasattr(egraph, "rebuild")    # rebuild

    # 添加节点
    eid1 = egraph.add_enode("leaf", [])
    eid2 = egraph.add_enode("leaf", [])
    eid3 = egraph.add_enode("add", [eid1, eid2])

    stats = egraph.stats()
    assert stats["n_eclasses"] >= 2
    assert stats["n_enodes"] >= 2

    # rebuild
    rebuild_result = egraph.rebuild()
    assert rebuild_result["rebuild_done"] is True


def test_p7_5_2_equality_saturation():
    """P7-5.2：equality saturation。"""
    egraph = EGraph()
    saturation = EqualitySaturation(egraph)
    saturation.add_rule("rule1", "pattern", "replacement")
    result = saturation.apply_rules(max_iterations=5)
    assert result["n_rules"] == 1
    assert "saturated" in result


# =========================================================================
# P7-6：几何/最优运输轨迹对齐
# =========================================================================

def test_p7_6_1_trajectory_embedding():
    """P7-6.1：轨迹嵌入。"""
    embedder = TrajectoryEmbedder()
    states = [{"x": 0.0, "y": 0.0}, {"x": 1.0, "y": 1.0}, {"x": 2.0, "y": 0.0}]
    traj = embedder.embed_state_sequence(states, ["x", "y"])
    assert len(traj.points) == 3

    velocities = embedder.compute_velocity(traj)
    assert len(velocities) == 2


def test_p7_6_2_4_alignment_methods():
    """P7-6.2：4种对齐方法。"""
    aligner = TrajectoryAligner()
    t1 = Trajectory("t1", [
        TrajectoryPoint(0.0, [0.0, 0.0]),
        TrajectoryPoint(1.0, [1.0, 1.0]),
    ])
    t2 = Trajectory("t2", [
        TrajectoryPoint(0.0, [0.0, 0.0]),
        TrajectoryPoint(1.0, [1.0, 1.0]),
    ])

    result = aligner.align_all_methods(t1, t2)
    assert result["n_methods"] == 4
    assert "frechet" in result
    assert "dtw" in result
    assert "optimal_transport" in result
    assert "graph_kernel" in result


def test_p7_6_comp_geometry_misuse_error():
    """P7-6.COMP：几何方法用于数学等价判定→抛GeometryMisuseError。"""
    guard = GeometryGuard()
    try:
        guard.assert_not_math_equivalence("math_equivalence")
        assert False, "应抛GeometryMisuseError"
    except GeometryMisuseError:
        pass

    # 合法用途
    result = guard.assert_purpose_legitimate("alignment")
    assert result["purpose_legitimate"] is True


# =========================================================================
# P7-7：数据充分后做TDA
# =========================================================================

def test_p7_7_1_tda_4_qualifiers():
    """P7-7.1/P7-7.1b：TDA数据充分性4限定词。"""
    gate = TDAGate()
    assert gate.check_all_qualifiers()["n_qualifiers_required"] == 4

    # 未全部满足时→抛InsufficientFormalizationError
    try:
        gate.assert_can_do_tda()
        assert False, "应抛InsufficientFormalizationError"
    except InsufficientFormalizationError:
        pass

    # 全部满足后可以通过
    gate.set_state_space(True)
    gate.set_adjacency(True)
    gate.set_scale(True)
    gate.set_equivalence_relation(True)
    result = gate.assert_can_do_tda()
    assert result["can_do_tda"] is True


def test_p7_7_2_persistent_homology():
    """P7-7.2：持久同调。"""
    gate = TDAGate()
    gate.set_state_space(True)
    gate.set_adjacency(True)
    gate.set_scale(True)
    gate.set_equivalence_relation(True)

    ph = PersistentHomology(tda_gate=gate)
    points = [[0.0, 0.0], [1.0, 0.0], [0.5, 1.0]]
    result = ph.compute_persistence(points)
    assert result["computed"] is True


def test_p7_7_3_baseline_comparison():
    """P7-7.3：3基线比较维度。"""
    comparator = BaselineComparator()
    result = comparator.compare(
        redundant_proofs_baseline=10,
        redundant_proofs_method=5,      # 减少5个重复证明类
        transport_consistency_baseline=0.8,
        transport_consistency_method=0.9,  # 一致性提升0.1
        cross_rep_migration_baseline=0.5,
        cross_rep_migration_method=0.5,    # 无提升
    )

    assert result.dim1_gain > 0   # 减少重复证明类
    assert result.dim2_gain > 0   # 运输一致性提升
    assert result.dim3_gain == 0  # 跨表示迁移无提升
    assert result.n_dimensions_with_gain == 2
    assert result.any_gain is True


# =========================================================================
# P7-8：只有形式对象充分时研究HoTT
# =========================================================================

def test_p7_8_1_hott_3_qualifiers():
    """P7-8.1/P7-8.1b：HoTT形式对象充分性3限定词。"""
    gate = HoTTGate()
    assert gate.check_all_qualifiers()["n_qualifiers_required"] == 3

    # 未全部满足时→抛InsufficientFormalizationError
    try:
        gate.assert_can_research_hott()
        assert False, "应抛InsufficientFormalizationError"
    except InsufficientFormalizationError:
        pass

    # 全部满足后可以通过
    gate.set_state_space(True)
    gate.set_equivalence_relation(True)
    gate.set_proof_representation(True)
    result = gate.assert_can_research_hott()
    assert result["can_research_hott"] is True


def test_p7_8_2_hott_3_directions():
    """P7-8.2：HoTT三个真实方向。"""
    directions = HoTTDirections()
    check = directions.check_all_preserved()
    assert check["n_directions"] == 3
    assert check["all_preserved"] is True


def test_p7_8_4_phase_gate():
    """P7-8.4：分阶段进入顺序。"""
    gate = PhaseGate()
    # 先行阶段未完成时不能进入成熟后阶段
    check = gate.can_enter_advanced("hott")
    assert check["can_enter"] is False

    # 完成先行阶段后可以进入
    for method in ["type_theory", "hypergraph", "event_structure", "causal_experiment", "operational_leakage"]:
        gate.mark_prerequisite_completed(method)
    check = gate.can_enter_advanced("hott")
    assert check["can_enter"] is True


def test_p7_8_5_premature_math_packaging():
    """P7-8.5：防止过早数学包装。"""
    guard = PrematureMathPackagingGuard()
    # 3项判定未全部满足时→拒绝
    try:
        guard.assert_not_premature()
        assert False, "应抛PermissionError"
    except PermissionError:
        pass

    # 全部满足后可以通过
    guard.set_sample_size(20)
    guard.set_state_space_complete(True)
    guard.set_baseline_feasible(True)
    result = guard.assert_not_premature()
    assert result["not_premature"] is True


def test_p7_8_comp4_mislabel_hott():
    """P7-8.COMP4：普通依赖图路径称为HoTT路径→抛MislabelError。"""
    guard = MislabelGuard()
    try:
        guard.assert_not_mislabel_hott("dependency_graph_path", "hott_path")
        assert False, "应抛MislabelError"
    except MislabelError:
        pass


def test_p7_8_comp5_mislabel_topology():
    """P7-8.COMP5：静态复制称为拓扑覆盖→抛MislabelError。"""
    guard = MislabelGuard()
    try:
        guard.assert_not_mislabel_topology("static_copy", "topology_cover")
        assert False, "应抛MislabelError"
    except MislabelError:
        pass


def test_p7_8_comp6_embedding_misuse():
    """P7-8.COMP6：embedding距离直接裁决数学等价→抛EmbeddingMisuseError。"""
    guard = MislabelGuard()
    try:
        guard.assert_not_embedding_misuse("embedding_distance", "math_equivalence")
        assert False, "应抛EmbeddingMisuseError"
    except EmbeddingMisuseError:
        pass


# =========================================================================
# P7-MATH：数学主张标注级别
# =========================================================================

def test_p7_math_3_labels():
    """P7-MATH-1：3级别标注。"""
    assert len(MathLabel) == 3
    labels = {l.value for l in MathLabel}
    assert labels == {"语义规格", "实验分析", "已实现"}


def test_p7_math_2_auto_verify():
    """P7-MATH-2：标注级别自动验证——手动覆盖→抛ManualLabelOverrideError。"""
    labeler = MathLabeler()
    try:
        labeler.set_label_manually("claim1", MathLabel.IMPLEMENTED)
        assert False, "应抛ManualLabelOverrideError"
    except ManualLabelOverrideError:
        pass

    # 自动确定
    label = labeler.auto_determine_label(
        "claim1", has_implementation=True, has_experiment=True,
        has_production_dependency=False,
    )
    assert label == MathLabel.EXPERIMENTAL


# =========================================================================
# P7-ROLE：角色隔离延续
# =========================================================================

def test_p7_role_capability_token():
    """P7-ROLE-2b：CapabilityToken强制机制——复用Phase 6。"""
    from xishujuzhen.research_runtime.auditor.capability_tokens import (
        CapabilityToken, CapabilityTokenVerifier,
    )
    verifier = CapabilityTokenVerifier()
    token = verifier.issue_auditor_token(run_id="phase7_test")

    # auditor可以读truth_vault
    access = verifier.verify_access(token, "truth_vault", "R")
    assert access["allowed"] is True

    # auditor可以写audit_verdicts
    access = verifier.verify_access(token, "audit_verdicts", "W")
    assert access["allowed"] is True

    # truth_vault仅auditor可读
    truth_access = verifier.verify_truth_vault_access(token)
    assert truth_access["allowed"] is True


def test_p7_role_orchestrator_enforce():
    """P7-ROLE-2b：orchestrator的enforce_role_access——复用Phase 6。"""
    from xishujuzhen.research_runtime.runtime.orchestrator import OnlineOrchestrator
    orch = OnlineOrchestrator()

    # auditor可以访问truth_vault
    result = orch.enforce_role_access("auditor", "truth_vault")
    assert result["access_granted"] is True

    # solver不能访问truth_vault→抛PermissionError
    try:
        orch.enforce_role_access("solver", "truth_vault")
        assert False, "应抛PermissionError"
    except PermissionError:
        pass


# =========================================================================
# P7-EXIT：出口门
# =========================================================================

def test_p7_exit_1_exit_gate():
    """P7-EXIT-1：3项比较中无任何一项有可测量增益→抛ExitGateFailureError。"""
    comparator = BaselineComparator()
    # 无增益
    no_gain_result = comparator.compare(
        redundant_proofs_baseline=10, redundant_proofs_method=10,
        transport_consistency_baseline=0.8, transport_consistency_method=0.8,
        cross_rep_migration_baseline=0.5, cross_rep_migration_method=0.5,
    )
    try:
        comparator.assert_exit_gate(no_gain_result)
        assert False, "应抛ExitGateFailureError"
    except ExitGateFailureError:
        pass

    # 有增益
    gain_result = comparator.compare(
        redundant_proofs_baseline=10, redundant_proofs_method=5,
        transport_consistency_baseline=0.8, transport_consistency_method=0.9,
        cross_rep_migration_baseline=0.5, cross_rep_migration_method=0.5,
    )
    result = comparator.assert_exit_gate(gain_result)
    assert result["exit_gate_passed"] is True


def test_p7_exit_1b_all_quantified():
    """P7-EXIT-1b：3个基线比较维度全部量化。"""
    comparator = BaselineComparator()
    result = comparator.compare(
        redundant_proofs_baseline=10, redundant_proofs_method=5,
        transport_consistency_baseline=0.8, transport_consistency_method=0.9,
        cross_rep_migration_baseline=0.5, cross_rep_migration_method=0.6,
    )
    quantified = comparator.all_dimensions_quantified(result)
    assert quantified["all_3_quantified"] is True


def test_p7_exit_2_label_downgrade():
    """P7-EXIT-2：标注为`已实现`但3项比较无增益→降级为`实验分析`。"""
    comparator = BaselineComparator()
    no_gain_result = comparator.compare(
        redundant_proofs_baseline=10, redundant_proofs_method=10,
        transport_consistency_baseline=0.8, transport_consistency_method=0.8,
        cross_rep_migration_baseline=0.5, cross_rep_migration_method=0.5,
    )
    downgrade = comparator.check_label_downgrade(no_gain_result, "已实现")
    assert downgrade["label_downgraded"] is True
    assert downgrade["downgraded_label"] == "实验分析"


# =========================================================================
# P7-STOP：停止条件
# =========================================================================

def test_p7_stop_1_stop_condition():
    """P7-STOP-1：3项基线比较中无任何一项有可测量增益→抛StopConditionTriggeredError。"""
    comparator = BaselineComparator()
    no_gain_result = comparator.compare(
        redundant_proofs_baseline=10, redundant_proofs_method=10,
        transport_consistency_baseline=0.8, transport_consistency_method=0.8,
        cross_rep_migration_baseline=0.5, cross_rep_migration_method=0.5,
    )
    try:
        comparator.assert_stop_condition(no_gain_result)
        assert False, "应抛StopConditionTriggeredError"
    except StopConditionTriggeredError:
        pass


def test_p7_stop_2_production_dependency_mislabel():
    """P7-STOP-2：标注为`语义规格`或`实验分析`的方法用于生产依赖→抛MislabelError。"""
    guard = MislabelGuard()
    try:
        guard.assert_not_production_dependency("语义规格")
        assert False, "应抛MislabelError"
    except MislabelError:
        pass

    try:
        guard.assert_not_production_dependency("实验分析")
        assert False, "应抛MislabelError"
    except MislabelError:
        pass

    # `已实现`可以用于生产依赖
    result = guard.assert_not_production_dependency("已实现")
    assert result["can_be_production_dependency"] is True


# =========================================================================
# 主测试入口
# =========================================================================

def main():
    print("=" * 60)
    print("Phase 7集成测试——表示运输、长证明和高级数学分析")
    print("=" * 60)

    tests = [
        # P7-1
        ("P7-1.1: RepresentationMap 12字段+6枚举", test_p7_1_1_representation_map_12_fields),
        ("P7-1.2: soundness义务强制（SoundnessViolationError）", test_p7_1_2_soundness_obligation_enforced),
        ("P7-1.2b: 转换保真3项验证", test_p7_1_2b_transport_fidelity_3_checks),
        ("P7-1.2c: 费马链条4环节", test_p7_1_2c_fermat_chain_4_segments),
        ("P7-1.4: 来源版本和撤稿状态监控", test_p7_1_4_source_version_monitor),
        ("P7-1.COMP3: groupoid 2限定词（GroupoidViolationError）", test_p7_1_comp3_groupoid_2_qualifiers),
        ("P7-1.COMP2: 首版不宣称已构成范畴", test_p7_1_comp2_not_category),
        ("P7-1母本: 3个跨表示映射例子", test_p7_1_mother_cross_rep_examples),

        # P7-2
        ("P7-2.1: Level 1推论链", test_p7_2_1_level1_inference_chain),
        ("P7-2.1b: 6条大师启发", test_p7_2_1b_6_master_heuristics),
        ("P7-2.4: 阶梯门控（LevelOrderViolationError）", test_p7_2_4_level_gate),
        ("P7-2.COMP3: 3项能力区分", test_p7_2_comp3_capability_distinction),

        # P7-3
        ("P7-3.1: 3类等价判定", test_p7_3_1_path_equivalence_3_classes),
        ("P7-3.2: 交换图验证", test_p7_3_2_commutative_diagram),
        ("P7-3.3: 5运输对象", test_p7_3_3_5_transport_objects),

        # P7-4
        ("P7-4.1: 局部视图3项一致性检查", test_p7_4_1_local_view_3_checks),
        ("P7-4.2: 层式粘合3步", test_p7_4_2_layered_glue_3_steps),
        ("P7-4.3: 4种候选障碍", test_p7_4_3_4_hole_types),
        ("P7-4.COMP: 洞直接当作同调群元素（HoleTypeError）", test_p7_4_comp_hole_type_error),

        # P7-5
        ("P7-5.1: e-graph 4核心组件", test_p7_5_1_egraph_4_components),
        ("P7-5.2: equality saturation", test_p7_5_2_equality_saturation),

        # P7-6
        ("P7-6.1: 轨迹嵌入", test_p7_6_1_trajectory_embedding),
        ("P7-6.2: 4种对齐方法", test_p7_6_2_4_alignment_methods),
        ("P7-6.COMP: 几何方法用途限制（GeometryMisuseError）", test_p7_6_comp_geometry_misuse_error),

        # P7-7
        ("P7-7.1: TDA数据充分性4限定词（InsufficientFormalizationError）", test_p7_7_1_tda_4_qualifiers),
        ("P7-7.2: 持久同调", test_p7_7_2_persistent_homology),
        ("P7-7.3: 3基线比较维度", test_p7_7_3_baseline_comparison),

        # P7-8
        ("P7-8.1: HoTT形式对象充分性3限定词", test_p7_8_1_hott_3_qualifiers),
        ("P7-8.2: HoTT三个真实方向", test_p7_8_2_hott_3_directions),
        ("P7-8.4: 分阶段进入顺序", test_p7_8_4_phase_gate),
        ("P7-8.5: 防止过早数学包装", test_p7_8_5_premature_math_packaging),
        ("P7-8.COMP4: 普通依赖图路径称为HoTT路径（MislabelError）", test_p7_8_comp4_mislabel_hott),
        ("P7-8.COMP5: 静态复制称为拓扑覆盖（MislabelError）", test_p7_8_comp5_mislabel_topology),
        ("P7-8.COMP6: embedding距离裁决数学等价（EmbeddingMisuseError）", test_p7_8_comp6_embedding_misuse),

        # P7-MATH
        ("P7-MATH-1: 3级别标注", test_p7_math_3_labels),
        ("P7-MATH-2: 标注级别自动验证（ManualLabelOverrideError）", test_p7_math_2_auto_verify),

        # P7-ROLE
        ("P7-ROLE-2b: CapabilityToken强制机制", test_p7_role_capability_token),
        ("P7-ROLE-2b: orchestrator enforce_role_access（PermissionError）", test_p7_role_orchestrator_enforce),

        # P7-EXIT
        ("P7-EXIT-1: 出口门验证（ExitGateFailureError）", test_p7_exit_1_exit_gate),
        ("P7-EXIT-1b: 3基线比较维度全部量化", test_p7_exit_1b_all_quantified),
        ("P7-EXIT-2: 标注降级检查", test_p7_exit_2_label_downgrade),

        # P7-STOP
        ("P7-STOP-1: 停止条件（StopConditionTriggeredError）", test_p7_stop_1_stop_condition),
        ("P7-STOP-2: 生产依赖误标注（MislabelError）", test_p7_stop_2_production_dependency_mislabel),
    ]

    passed = 0
    failed = 0

    # 按大项分组打印
    current_section = None
    sections = {
        "P7-1": "--- 1. P7-1：类型化representation_maps和soundness义务 ---",
        "P7-2": "--- 2. P7-2：费马型跨域模块编排 ---",
        "P7-3": "--- 3. P7-3：证明路径等价和交换图 ---",
        "P7-4": "--- 4. P7-4：局部视图一致性与层式粘合 ---",
        "P7-5": "--- 5. P7-5：e-graph等价表达式管理 ---",
        "P7-6": "--- 6. P7-6：几何/最优运输轨迹对齐 ---",
        "P7-7": "--- 7. P7-7：数据充分后做TDA ---",
        "P7-8": "--- 8. P7-8：只有形式对象充分时研究HoTT ---",
        "P7-MATH": "--- 9. P7-MATH：数学主张标注级别 ---",
        "P7-ROLE": "--- 10. P7-ROLE：角色隔离延续 ---",
        "P7-EXIT": "--- 11. P7-EXIT：出口门 ---",
        "P7-STOP": "--- 12. P7-STOP：停止条件 ---",
    }

    for name, test_fn in tests:
        # 确定当前大项
        section_key = name.split(":")[0]
        if section_key != current_section:
            current_section = section_key
            if section_key in sections:
                print(f"\n{sections[section_key]}")

        if run_test(name, test_fn):
            passed += 1
        else:
            failed += 1

    print("\n" + "=" * 60)
    if failed == 0:
        print(f"🎉 Phase 7集成测试全部通过！({passed}/{passed + failed})")
    else:
        print(f"⚠️  Phase 7集成测试有{failed}项失败 ({passed}通过/{passed + failed}总计)")
    print("=" * 60)

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
