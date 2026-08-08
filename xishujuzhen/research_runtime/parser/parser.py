"""
主解析器（整合模块）：260号§3.3协同架构。

流程：LLM粗解析 → SymPy验证 → 一致性检查 → 组装ParseResult。
置信度计算：parse_confidence = llm_confidence * sympy_factor。
"""

import json
import uuid
from datetime import datetime, timezone
from typing import List, Optional, Dict, Any, Callable

from ..models.event import SemanticEvent, EventFactory, RawEvent, SemanticEventType
from .models import (
    ParseRequest,
    ParseResult,
    MathObject,
    TrajectoryNode,
    TrajectoryEdge,
    SixTuple,
    VerifiedProp,
    Conjecture,
    Obligation,
    Representation,
    Evidence,
    UnsolvedProblem,
    TurnRecord,
)
from .llm_parser import LLMParser
from .sympy_verifier import SympyVerifier
from .consistency_checker import ConsistencyChecker


def _now_iso() -> str:
    """当前UTC时间的ISO 8601时间戳"""
    return datetime.now(timezone.utc).isoformat()


def _gen_id(prefix: str = "evt") -> str:
    """生成唯一ID"""
    return f"{prefix}_{uuid.uuid4().hex[:16]}"


# 14种语义事件类型的合法值集合
VALID_SEMANTIC_TYPES = {t.value for t in SemanticEventType}

# 10种节点类型的合法值集合
VALID_NODE_TYPES = {
    "observation", "claim", "representation", "subgoal", "candidate",
    "operation", "tool_result", "contradiction", "stall", "resolution",
}

# 类型模糊匹配映射
TYPE_FUZZY_MAP = {
    "derive": "resolution",
    "deduce": "resolution",
    "obtain": "resolution",
    "introduce": "representation",
    "define": "representation",
    "notice": "observation",
    "observe": "observation",
    "hypothesize": "candidate",
    "try": "test",
    "attempt": "test",
    "stuck": "stall",
    "give_up": "backtrack",
    "verify": "verification",
}


class MathParser:
    """
    主解析器（260号§3.3）。

    协调LLM粗解析、SymPy验证、一致性检查三个子模块，
    组装最终的ParseResult。

    流程：
    1. LLM粗解析 → JSON
    2. SymPy验证 → 修正math_objects
    3. 一致性检查 → 警告
    4. 组装ParseResult

    置信度计算：parse_confidence = llm_confidence * sympy_factor
    """

    def __init__(
        self,
        llm_parser: Optional[LLMParser] = None,
        sympy_verifier: Optional[SympyVerifier] = None,
        consistency_checker: Optional[ConsistencyChecker] = None,
    ):
        self.llm_parser = llm_parser or LLMParser()
        self.sympy_verifier = sympy_verifier or SympyVerifier()
        self.consistency_checker = consistency_checker or ConsistencyChecker()

    def parse(self, request: ParseRequest) -> ParseResult:
        """
        解析工作智能体输出，返回ParseResult（260号§3.3）。

        Args:
            request: ParseRequest，包含agent_output、history、current_six_tuple等

        Returns:
            ParseResult，包含semantic_events、trajectory_nodes、
            trajectory_edges、six_tuple、置信度、验证标记、警告
        """
        all_warnings: List[str] = []

        # ---- 第一步：LLM粗解析 ----
        llm_output = self.llm_parser.parse(request)
        llm_warnings = llm_output.get("parse_warnings", [])
        all_warnings.extend(llm_warnings)

        # ---- 第二步：后处理LLM输出 ----
        # 提取并验证语义事件类型
        raw_events = llm_output.get("semantic_events", [])
        raw_nodes = llm_output.get("trajectory_nodes", [])
        raw_edges = llm_output.get("trajectory_edges", [])
        raw_six_tuple = llm_output.get("six_tuple", {})
        llm_confidence = llm_output.get("parse_confidence", 0.5)

        # ---- 第三步：SymPy验证 ----
        # 收集所有math_objects做SymPy验证
        all_math_objects: List[MathObject] = []
        for evt in raw_events:
            for mo in evt.get("math_objects", []):
                all_math_objects.append(MathObject.from_dict(mo))

        verified_math_objects = self.sympy_verifier.verify_batch(all_math_objects)
        sympy_warnings = self.sympy_verifier.warnings
        all_warnings.extend(sympy_warnings)

        # 计算sympy_factor
        sympy_factor = self.sympy_verifier.compute_sympy_factor(
            verified_math_objects
        )

        # 建立math_object名称到验证后对象的映射
        mo_by_name: Dict[str, MathObject] = {}
        for mo in verified_math_objects:
            mo_by_name[mo.name] = mo

        # ---- 第四步：构建SemanticEvent ----
        semantic_events, per_event_confidence, sympy_verified_list = (
            self._build_semantic_events(
                raw_events, verified_math_objects, request
            )
        )

        # ---- 第五步：构建TrajectoryNode和TrajectoryEdge ----
        trajectory_nodes, trajectory_edges = self._build_trajectory(
            raw_nodes, raw_edges, mo_by_name, request, semantic_events
        )

        # ---- 第六步：构建SixTuple ----
        six_tuple = self._build_six_tuple(
            raw_six_tuple, request, semantic_events
        )

        # ---- 第七步：一致性检查 ----
        consistency_warnings = self.consistency_checker.check(
            semantic_events, trajectory_nodes, six_tuple
        )
        all_warnings.extend(consistency_warnings)

        # ---- 第八步：计算最终置信度 ----
        parse_confidence = llm_confidence * sympy_factor

        return ParseResult(
            semantic_events=semantic_events,
            trajectory_nodes=trajectory_nodes,
            trajectory_edges=trajectory_edges,
            six_tuple=six_tuple,
            parse_confidence=parse_confidence,
            per_event_confidence=per_event_confidence,
            sympy_verified=sympy_verified_list,
            parse_warnings=all_warnings,
        )

    def _normalize_event_type(self, type_str: str) -> str:
        """
        类型校验和模糊匹配（260号§3.1.3）。

        检查type字段是否在14种语义事件类型枚举值中。
        不在枚举中的做模糊匹配。
        """
        type_lower = type_str.lower()
        if type_lower in VALID_SEMANTIC_TYPES:
            return type_lower
        # 模糊匹配
        if type_lower in TYPE_FUZZY_MAP:
            mapped = TYPE_FUZZY_MAP[type_lower]
            if mapped in VALID_SEMANTIC_TYPES:
                return mapped
        # 默认为OBSERVATION
        return SemanticEventType.OBSERVATION.value

    def _normalize_node_type(self, type_str: str) -> str:
        """节点类型校验和模糊匹配"""
        type_lower = type_str.lower()
        if type_lower in VALID_NODE_TYPES:
            return type_lower
        # 模糊匹配
        if type_lower in TYPE_FUZZY_MAP:
            mapped = TYPE_FUZZY_MAP[type_lower]
            if mapped in VALID_NODE_TYPES:
                return mapped
        # 默认为observation
        return "observation"

    def _build_semantic_events(
        self,
        raw_events: List[dict],
        verified_math_objects: List[MathObject],
        request: ParseRequest,
    ) -> tuple:
        """
        从LLM输出的raw_events构建SemanticEvent列表。

        复用已有的EventFactory创建SemanticEvent。
        """
        semantic_events: List[SemanticEvent] = []
        per_event_confidence: List[float] = []
        sympy_verified_list: List[bool] = []

        # 建立math_object名称到对象的映射
        mo_by_name: Dict[str, MathObject] = {}
        for mo in verified_math_objects:
            mo_by_name[mo.name] = mo

        # 为本轮事件创建一个虚拟RawEvent（解析器产出的事件
        # 没有对应的真实RawEvent，用一个虚拟的占位）
        virtual_raw = RawEvent(
            event_id=_gen_id("raw"),
            type="text_output",
            timestamp=_now_iso(),
            run_id=request.run_id,
            raw_payload={"agent_output": request.agent_output},
            content_hash="",
        )

        event_id_map: Dict[int, str] = {}  # 序号 → event_id

        for idx, raw_evt in enumerate(raw_events):
            event_type = self._normalize_event_type(raw_evt.get("type", "observation"))
            description = raw_evt.get("description", "")
            raw_text_span = raw_evt.get("raw_text_span", "")
            confidence = raw_evt.get("confidence", 0.8)
            depends_on = raw_evt.get("depends_on", [])

            # 关联math_objects（优先用SymPy验证后的版本）
            evt_math_objects: List[MathObject] = []
            for mo_entry in raw_evt.get("math_objects", []):
                if isinstance(mo_entry, dict):
                    # 完整dict：先按name查验证后的版本，找不到再从dict创建
                    mo_name = mo_entry.get("name", "")
                    if mo_name in mo_by_name:
                        evt_math_objects.append(mo_by_name[mo_name])
                    else:
                        evt_math_objects.append(MathObject.from_dict(mo_entry))
                elif isinstance(mo_entry, str) and mo_entry in mo_by_name:
                    evt_math_objects.append(mo_by_name[mo_entry])

            # 构建payload
            payload = {
                "description": description,
                "raw_text_span": raw_text_span,
                "round_index": request.round_index,
                "math_objects": [m.to_dict() for m in evt_math_objects],
            }

            # 生成event_id
            event_id = _gen_id("sem")
            event_id_map[idx] = event_id

            # 解析depends_on中的序号引用（如"event_7_1"）
            causal_preds: List[str] = []
            for dep in depends_on:
                if isinstance(dep, str) and dep in event_id_map.values():
                    causal_preds.append(dep)
                elif isinstance(dep, str) and dep.startswith("event_"):
                    # 解析 event_{round}_{seq} 格式
                    parts = dep.split("_")
                    if len(parts) == 3:
                        try:
                            seq = int(parts[2])
                            if seq in event_id_map:
                                causal_preds.append(event_id_map[seq])
                        except ValueError:
                            pass

            # 判断该事件的math_objects是否都通过SymPy验证
            evt_sympy_verified = (
                len(evt_math_objects) == 0
                or all(m.sympy_verified for m in evt_math_objects)
            )

            sem_event = EventFactory.create_semantic_event(
                raw_event=virtual_raw,
                semantic_type=event_type,
                payload=payload,
                causal_predecessors=causal_preds,
                confidence=confidence,
                source="hybrid_parser_v1",
            )

            # 用生成的event_id覆盖
            sem_event = SemanticEvent(
                event_id=event_id,
                raw_event_id=sem_event.raw_event_id,
                type=sem_event.type,
                timestamp=sem_event.timestamp,
                run_id=sem_event.run_id,
                payload=sem_event.payload,
                content_hash=sem_event.content_hash,
                causal_predecessors=sem_event.causal_predecessors,
                conflict_with=sem_event.conflict_with,
                confidence=sem_event.confidence,
                source=sem_event.source,
                workspace_ref=sem_event.workspace_ref,
                obligation_ref=sem_event.obligation_ref,
                evidence_ref=sem_event.evidence_ref,
            )

            semantic_events.append(sem_event)
            per_event_confidence.append(confidence)
            sympy_verified_list.append(evt_sympy_verified)

        return semantic_events, per_event_confidence, sympy_verified_list

    def _build_trajectory(
        self,
        raw_nodes: List[dict],
        raw_edges: List[dict],
        mo_by_name: Dict[str, MathObject],
        request: ParseRequest,
        semantic_events: List[SemanticEvent],
    ) -> tuple:
        """
        从LLM输出的raw_nodes和raw_edges构建TrajectoryNode和TrajectoryEdge。
        """
        nodes: List[TrajectoryNode] = []
        node_type_index: Dict[str, List[int]] = {}  # type → [indices]

        for idx, raw_node in enumerate(raw_nodes):
            node_type = self._normalize_node_type(raw_node.get("type", "observation"))
            content = raw_node.get("content", "")
            is_frontier = raw_node.get("is_frontier", False)
            confidence = raw_node.get("confidence", 0.8)

            # 关联math_objects（优先用SymPy验证后的版本）
            node_math_objects: List[MathObject] = []
            for mo_entry in raw_node.get("math_objects", []):
                if isinstance(mo_entry, dict):
                    mo_name = mo_entry.get("name", "")
                    if mo_name in mo_by_name:
                        node_math_objects.append(mo_by_name[mo_name])
                    else:
                        node_math_objects.append(MathObject.from_dict(mo_entry))
                elif isinstance(mo_entry, str) and mo_entry in mo_by_name:
                    node_math_objects.append(mo_by_name[mo_entry])

            node_id = f"node_{request.run_id}_{request.round_index}_{idx}"
            node = TrajectoryNode(
                node_id=node_id,
                type=node_type,
                round_index=request.round_index,
                content=content,
                math_objects=node_math_objects,
                is_frontier=is_frontier,
                confidence=confidence,
            )
            nodes.append(node)
            node_type_index.setdefault(node_type, []).append(idx)

        # 构建边
        edges: List[TrajectoryEdge] = []
        for raw_edge in raw_edges:
            source_type = raw_edge.get("source_type", "")
            target_type = raw_edge.get("target_type", "")
            edge_type = raw_edge.get("edge_type", "infer")
            description = raw_edge.get("description", "")

            # 通过type找到对应的node_id
            source_id = self._find_node_id_by_type(
                source_type, nodes, node_type_index
            )
            target_id = self._find_node_id_by_type(
                target_type, nodes, node_type_index
            )

            if source_id and target_id:
                edges.append(TrajectoryEdge(
                    source_id=source_id,
                    target_id=target_id,
                    edge_type=edge_type,
                    description=description,
                ))

        return nodes, edges

    def _find_node_id_by_type(
        self,
        node_type: str,
        nodes: List[TrajectoryNode],
        node_type_index: Dict[str, List[int]],
    ) -> Optional[str]:
        """通过节点类型找到第一个匹配的node_id"""
        if not node_type:
            return None
        indices = node_type_index.get(node_type, [])
        if indices:
            return nodes[indices[0]].node_id
        return None

    def _build_six_tuple(
        self,
        raw_six_tuple: dict,
        request: ParseRequest,
        semantic_events: List[SemanticEvent],
    ) -> SixTuple:
        """
        从LLM输出的raw_six_tuple构建SixTuple。

        如果有上一轮的六元组，做增量合并（V_t只增不减）。
        """
        # 解析LLM输出的六元组
        new_six_tuple = SixTuple.from_dict(raw_six_tuple)

        # 如果有上一轮六元组，做增量合并
        if request.current_six_tuple is not None:
            prev = request.current_six_tuple

            # V_t只增不减（260号§5.4.3）
            merged_v = list(prev.V_t)
            existing_v_set = {v.statement for v in merged_v}
            for v in new_six_tuple.V_t:
                if v.statement not in existing_v_set:
                    merged_v.append(v)
                    existing_v_set.add(v.statement)
            new_six_tuple.V_t = merged_v

            # R_t也只增不减
            merged_r = list(prev.R_t)
            existing_r_set = {r.name for r in merged_r}
            for r in new_six_tuple.R_t:
                if r.name not in existing_r_set:
                    merged_r.append(r)
                    existing_r_set.add(r.name)
            new_six_tuple.R_t = merged_r

            # O_t：合并，相似description的更新status
            merged_o: List[Obligation] = list(prev.O_t)
            for new_o in new_six_tuple.O_t:
                matched_idx = self._find_similar_obligation(
                    new_o, merged_o
                )
                if matched_idx is not None:
                    # 更新已有义务的status
                    existing = merged_o[matched_idx]
                    merged_o[matched_idx] = Obligation(
                        description=existing.description,
                        obligation_type=(
                            new_o.obligation_type or existing.obligation_type
                        ),
                        status=new_o.status,
                        depends_on=(
                            new_o.depends_on or existing.depends_on
                        ),
                    )
                else:
                    merged_o.append(new_o)
            new_six_tuple.O_t = merged_o

            # U_t：合并 + 移除已解决的
            # 如果本轮U_t为空，说明问题已解决，清空上一轮的U_t
            if len(new_six_tuple.U_t) == 0:
                new_six_tuple.U_t = []
            else:
                # 本轮有U_t：合并，相同/相似的保留
                merged_u: List[UnsolvedProblem] = []
                for u in prev.U_t:
                    # 检查本轮U_t中是否还有这个问题
                    if self._u_t_still_present(u, new_six_tuple.U_t):
                        merged_u.append(u)
                # 加上本轮新增的U_t
                existing_u_keys = {u.description for u in merged_u}
                for u in new_six_tuple.U_t:
                    if not any(
                        self._descriptions_similar(u.description, e)
                        for e in existing_u_keys
                    ):
                        merged_u.append(u)
                new_six_tuple.U_t = merged_u

            # E_t：合并
            merged_e = list(prev.E_t)
            new_six_tuple.E_t = merged_e + new_six_tuple.E_t

        return new_six_tuple

    @staticmethod
    def _descriptions_similar(desc1: str, desc2: str) -> bool:
        """
        判断两个描述是否相似（用于O_t/U_t合并时的去重）。

        精确匹配或一方包含另一方。
        """
        if desc1 == desc2:
            return True
        d1 = desc1.strip()
        d2 = desc2.strip()
        if d1 in d2 or d2 in d1:
            return True
        # 提取核心关键词比较
        return False

    def _find_similar_obligation(
        self, target: Obligation, obligations: List[Obligation]
    ) -> Optional[int]:
        """在已有义务列表中找与target相似的，返回索引"""
        for i, o in enumerate(obligations):
            if self._descriptions_similar(target.description, o.description):
                return i
        return None

    @staticmethod
    def _u_t_still_present(
        u: UnsolvedProblem, new_u_t: List[UnsolvedProblem]
    ) -> bool:
        """检查上一轮的U_t条目是否在本轮U_t中仍然存在"""
        for new_u in new_u_t:
            if MathParser._descriptions_similar(u.description, new_u.description):
                return True
        return False
