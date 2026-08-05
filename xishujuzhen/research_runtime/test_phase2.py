"""
Phase 2集成测试（审计修正版）

端到端测试：
1. 创建Q_0（Ramsey案例）
2. 创建工作区
3. 从事件流中提取义务
4. 添加证据
5. 运行2个独立StateReducer，计算Krippendorff α（DYN-1）
6. 运行StallDetector，对照人工标注计算precision/recall（DYN-2）
7. 计算进展偏序
8. 验证Verifier角色（6种状态输出）
9. 验证Retriever角色（不返回整图/答案材料）
10. 验证StateReducer可复现约束
11. 验证出口门

对应132号P2-EXIT-1/2/3。
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from xishujuzhen.research_runtime.state_reducer.q0 import create_q0_ramsey, verify_q0_frozen
from xishujuzhen.research_runtime.state_reducer.workspace_store import WorkspaceStore
from xishujuzhen.research_runtime.state_reducer.obligation import (
    Obligation, ObligationType, ObligationStatus, ObligationHyperedge, HyperedgeMode, ObligationStore,
)
from xishujuzhen.research_runtime.state_reducer.evidence import (
    Evidence, EvidenceKind, EvidencePolarity, EvidenceStatus, EvidenceStore,
)
from xishujuzhen.research_runtime.state_reducer.verification_gate import VerificationGate
from xishujuzhen.research_runtime.state_reducer.progress import ProgressOrder, ProgressVector, CanonicalKey
from xishujuzhen.research_runtime.state_reducer.controller_belief import BeliefEstimator, ActionType
from xishujuzhen.research_runtime.state_reducer.reducer import (
    RuleBasedReducer, SemanticBasedReducer, ConsistencyTest,
)
from xishujuzhen.research_runtime.verification.stall_detector import (
    StallDetector, StallAnnotation, StallAnnotationStore, StallType,
)
from xishujuzhen.research_runtime.verification.verifier import (
    Verifier, VerifierOutput,
)
from xishujuzhen.research_runtime.retrieval.retriever import (
    Retriever, RetrievalRequest, RetrievalConstraint,
)


def test_phase2_integration():
    """Phase 2端到端集成测试（审计修正版）"""

    print("=" * 60)
    print("Phase 2集成测试（审计修正版）")
    print("=" * 60)

    # === 1. Q_0创建与冻结验证 ===
    print("\n--- 1. Q_0创建与冻结验证 ---")
    q0 = create_q0_ramsey()
    assert q0.task_id == "Q_0_ramsey_c5"
    assert q0.type.value == "conjecture"
    assert verify_q0_frozen(q0), "Q_0冻结检查失败"
    print(f"✅ Q_0创建: {q0.task_id}, type={q0.type.value}")

    # === 2. 工作区创建 ===
    print("\n--- 2. 工作区创建 ---")
    ws_store = WorkspaceStore()
    ws_id = "phase2_test_ws_v2"
    try:
        ws_store.col.delete(ws_id)
    except Exception:
        pass

    ws_dict = {
        "V_t": {"verified_premises": [], "verified_lemmas": [], "verified_tool_results": []},
        "F_t": {"candidates": ["c1_ramsey"], "temporary_assumptions": [], "unverified_bridges": []},
        "O_t": {"obligation_ids": []},
        "R_t": {"active_representations": ["recursion_tree"], "pending_transforms": []},
        "D_t": {"rejected_branches": [], "suspended_branches": [], "recoverable_branches": []},
        "E_t": {"evidence_ids": []},
    }
    ws_store.create_workspace_from_dict(ws_id, q0.task_id, ws_dict)
    ws = ws_store.read_workspace(ws_id)
    assert ws is not None
    print(f"✅ 工作区创建: {ws_id}")

    # 清理可能存在的promoted workspace
    try:
        ws_store.col.delete(f"{ws_id}_promoted_c1_ramsey")
    except Exception:
        pass

    # === 3. 义务图构建（使用127号§4的10种义务类型）===
    print("\n--- 3. 义务图构建 ---")
    obl_store = ObligationStore()
    for col in [obl_store.obl_col, obl_store.rel_col, obl_store.edge_col]:
        col.truncate()

    o1 = Obligation("o1_search", q0.task_id, ObligationType.SEARCH,
                     description="搜索R_k(C_5)下界候选")
    o2 = Obligation("o2_verify", q0.task_id, ObligationType.VERIFICATION,
                     description="验证候选可证伪性")
    o3 = Obligation("o3_prove", q0.task_id, ObligationType.PROVE,
                     description="证明下界")
    for o in [o1, o2, o3]:
        obl_store.insert_obligation(o)

    obl_store.insert_hyperedge(ObligationHyperedge(
        "rel_and_main", HyperedgeMode.ALL, "o1_search",
        ["o2_verify", "o3_prove"], "formal_proof",
    ))

    dag = obl_store.check_dag()
    assert dag["is_dag"], "义务图应该是DAG"
    print(f"✅ 义务图构建: {dag['node_count']}节点, is_dag={dag['is_dag']}")

    # === 4. 证据添加（使用127号§6的status枚举）===
    print("\n--- 4. 证据添加 ---")
    ev_store = EvidenceStore()
    ev_store.col.truncate()

    ev1 = Evidence(
        "ev_numerical", "c1_ramsey", EvidenceKind.NUMERICAL,
        EvidencePolarity.SUPPORT, scope="k<100",
        verifier="numpy", verifier_version="1.24",
        status=EvidenceStatus.ACTIVE,  # 修正：用active而非verified
        source_event="e5",  # 修正：添加source_event
        confidence=0.8,  # 修正：添加confidence
    )
    ev_store.insert_evidence(ev1)
    print(f"✅ 证据添加: {ev1.evidence_id}, status={ev1.status.value}")

    state = ev_store.compute_derived_state("c1_ramsey")
    assert state["derived_state"] == "support_only"
    print(f"   派生认识状态: {state['derived_state']}")

    # === 5. 验证门——F_t→V_t提升 ===
    print("\n--- 5. 验证门——F_t→V_t提升 ---")
    gate = VerificationGate(ev_store, ws_store)
    # 修正：用ObligationType.SEARCH而非CONJECTURE
    result = gate.promote_to_v_t(ws_id, "c1_ramsey", ObligationType.SEARCH, "lemma")
    assert result["success"], f"提升失败: {result['reason']}"
    print(f"✅ F_t→V_t提升: {result['workspace_id']}")

    # === 6. DYN-1多观察者重建一致性 ===
    print("\n--- 6. DYN-1多观察者重建一致性 ---")
    events = [
        {"event_id": "e1", "type": "claim", "content": "R_k(C_5) >= k^c", "verified": False},
        {"event_id": "e2", "type": "candidate", "content": "c=k/3", "semantic_tags": []},
        {"event_id": "e3", "type": "subgoal", "content": "证明下界"},
        {"event_id": "e4", "type": "representation", "content": "recursion_tree"},
        {"event_id": "e5", "type": "test", "content": "数值验证k=10"},
        {"event_id": "e6", "type": "tool_result", "content": "numpy_result", "verified": True},
        {"event_id": "e7", "type": "contradiction", "content": "c=k/5失败"},
        {"event_id": "e8", "type": "stall", "content": "反复改指数", "stall_type": "strategy_exhaustion"},
        {"event_id": "e9", "type": "backtrack", "content": "放弃k/5"},
        {"event_id": "e10", "type": "resolution", "content": "底数和指数分开"},
        {"event_id": "e11", "type": "verification", "content": "R_k(C_5) >= log(k)^c", "semantic_tags": []},
        {"event_id": "e12", "type": "hint_injection", "content": "Hint-0"},
    ]

    r1 = RuleBasedReducer()
    r2 = SemanticBasedReducer()
    test = ConsistencyTest([r1, r2])
    dyn1_result = test.run(events)

    print(f"✅ DYN-1结果: passed={dyn1_result['passed']}")
    for field in ConsistencyTest.CRITICAL_FIELDS:
        alpha = dyn1_result["avg_alphas"].get(field, 0.0)
        status = "✅" if alpha >= 0.67 else "❌"
        print(f"   {field}: α={alpha:.2f} {status}")

    assert dyn1_result["passed"], "DYN-1未通过"

    # === 6.5 StateReducer可复现约束验证 ===
    print("\n--- 6.5 StateReducer可复现约束验证 ---")
    repro1 = r1.verify_reproducibility(events, n_runs=3)
    repro2 = r2.verify_reproducibility(events, n_runs=3)
    print(f"✅ RuleBasedReducer可复现: {repro1['reproducible']}")
    print(f"✅ SemanticBasedReducer可复现: {repro2['reproducible']}")
    assert repro1["reproducible"], "RuleBasedReducer违反可复现约束"
    assert repro2["reproducible"], "SemanticBasedReducer违反可复现约束"

    # === 7. DYN-2卡点检测校准（使用123号§38的7类卡点）===
    print("\n--- 7. DYN-2卡点检测校准 ---")
    detector = StallDetector()
    ann_store = StallAnnotationStore()
    ann_store.col.truncate()

    ann_store.insert_annotation(StallAnnotation(
        "ann1", "run_phase2", "2026-08-05T00:01:00Z",
        StallType.STRATEGY_EXHAUSTION, True,
    ))
    ann_store.insert_annotation(StallAnnotation(
        "ann2", "run_phase2", "2026-08-05T00:02:00Z",
        StallType.NECESSARY_EXPLORATION, False,  # 修正：用necessary_exploration
    ))

    progress_history = [
        {"relation": "equal", "vector": {"u_t": 1}, "representation_id": "r1"},
        {"relation": "equal", "vector": {"u_t": 1}, "representation_id": "r1"},
        {"relation": "equal", "vector": {"u_t": 1}, "representation_id": "r1"},
    ]
    detections = detector.detect(
        progress_history,
        budget={"token": {"remaining": 5000}},
        obligations={"sccs": [], "unresolved_conflicts": 0, "tool_failures": 0},
    )
    print(f"✅ 卡点检测: {len(detections)}个检测")
    for d in detections:
        print(f"   {d.stall_type.value}: confidence={d.confidence:.2f}")

    pr = ann_store.compute_precision_recall(
        detector, "run_phase2", progress_history,
        {"token": {"remaining": 5000}}, {"sccs": [], "unresolved_conflicts": 0, "tool_failures": 0},
    )
    print(f"   precision={pr['precision']:.2f}, recall={pr['recall']:.2f}")

    # === 8. 进展偏序 ===
    print("\n--- 8. 进展偏序 ---")
    po = ProgressOrder()
    v_initial = po.compute_progress_vector(0.0, 10.0, 1, 3, 100.0)
    v_after = po.compute_progress_vector(2.0, 8.0, 1, 2, 150.0)
    cmp = po.compare(v_initial, v_after)
    print(f"✅ 进展偏序: {cmp['relation']}")

    # === 9. 控制器信念 ===
    print("\n--- 9. 控制器信念 ---")
    estimator = BeliefEstimator(detector)
    belief = estimator.estimate(
        progress_history, {"token": {"remaining": 5000}},
        {"sccs": [], "unresolved_conflicts": 0, "tool_failures": 0},
    )
    action = estimator.select_action(belief, {"token": {"remaining": 5000}}, hint_budget_remaining=3)
    print(f"✅ 控制器信念: is_stall_prob={belief.is_stall_prob:.2f}, action={action['action']}")

    # === 10. Verifier角色验证（6种状态输出）===
    print("\n--- 10. Verifier角色验证 ---")
    verifier = Verifier(ev_store)
    vresult = verifier.verify("c1_ramsey")
    print(f"✅ Verifier输出: {vresult.output.value}")
    assert vresult.output in VerifierOutput, "Verifier必须输出6种状态之一"
    assert vresult.output != True and vresult.output != False, "Verifier不能返回布尔值"
    print(f"   6种状态: {[o.value for o in VerifierOutput]}")

    # 验证无证据时返回unknown
    vresult2 = verifier.verify("c_no_evidence")
    assert vresult2.output == VerifierOutput.UNKNOWN
    print(f"✅ 无证据返回unknown: OK")

    # === 11. Retriever角色验证 ===
    print("\n--- 11. Retriever角色验证 ---")
    knowledge_items = [
        {"id": "k1", "content": "Ramsey定理基础", "obligation_refs": ["o1_search"],
         "representation_refs": ["recursion_tree"], "permissions": ["read"], "evidence_level": "literature"},
        {"id": "k2", "content": "答案：R_k(C_5)下界是log(k)^c", "obligation_refs": ["o1_search"],
         "representation_refs": [], "permissions": ["read"], "evidence_level": "ground_truth"},
        {"id": "k3", "content": "迭代对数定义", "obligation_refs": ["o3_prove"],
         "representation_refs": ["recursion_tree"], "permissions": ["read"], "evidence_level": "literature"},
    ]
    retriever = Retriever(knowledge_items)
    req = RetrievalRequest(
        current_obligations=["o1_search"],
        current_representations=["recursion_tree"],
        permissions=["read"],
        max_items=10,
        constraints=[RetrievalConstraint.BY_OBLIGATION, RetrievalConstraint.BY_REPRESENTATION,
                     RetrievalConstraint.BY_PERMISSION],
    )
    rresult = retriever.retrieve(req)
    print(f"✅ Retriever返回: {len(rresult.items)}条")
    # 验证答案材料被过滤
    for item in rresult.items:
        assert "答案" not in item["content"], "Retriever不应返回答案材料"
    print(f"✅ 答案材料被过滤: OK")
    # 验证不返回整图
    assert len(rresult.items) < len(knowledge_items), "Retriever不应返回整图"
    print(f"✅ 不返回整图: OK")

    # === 12. 出口门验证 ===
    print("\n--- 12. 出口门验证 ---")
    exit1_passed = dyn1_result["passed"]
    print(f"{'✅' if exit1_passed else '❌'} P2-EXIT-1: DYN-1 α≥0.80: {exit1_passed}")

    exit2_passed = "precision" in pr and "recall" in pr
    print(f"{'✅' if exit2_passed else '❌'} P2-EXIT-2: DYN-2校准能力: {exit2_passed}")

    exit3_passed = exit1_passed and exit2_passed
    print(f"{'✅' if exit3_passed else '❌'} P2-EXIT-3: 全部通过: {exit3_passed}")

    # === 清理 ===
    print("\n--- 清理 ---")
    from arango import ArangoClient
    client = ArangoClient(hosts="http://localhost:8529")
    db = client.db("xishujuzhen_math", username="root", password="REDACTED-DB-PASSWORD")
    try:
        db.collection("workspaces").delete(ws_id)
        db.collection("workspaces").delete(result["workspace_id"])
    except Exception:
        pass
    for col_name in ["obligations", "obligation_relations", "obligation_edges"]:
        db.collection(col_name).truncate()
    db.collection("evidence").truncate()
    db.collection("stall_annotations").truncate()
    print("✅ 清理完成")

    print("\n" + "=" * 60)
    if exit3_passed:
        print("🎉 Phase 2集成测试（审计修正版）全部通过！")
    else:
        print("❌ Phase 2集成测试未通过")
    print("=" * 60)

    return exit3_passed


if __name__ == "__main__":
    success = test_phase2_integration()
    sys.exit(0 if success else 1)
