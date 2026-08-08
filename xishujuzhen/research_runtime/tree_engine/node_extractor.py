"""NodeExtractor: 从AI的trajectory中提取树节点。

封装DevinCliParserProvider + 六元组提取，把AI的thinking/trajectory
转换为TreeNode写入TreeStore。

工作流程：
  1. 把trajectory按轮次分割（每个thinking round对应一个节点）
  2. 对每个轮次调用DevinCliParserProvider解析→ParseResult
  3. 每个ParseResult创建一个TreeNode，写入tree_store
  4. 返回创建的node_key列表

降级处理：如果parser解析失败（parse_confidence < 0.5），
仍创建节点但situation为空，situation_text用thinking原文前2000字符。
"""

import time
from typing import List, Optional, Dict, Any

from .tree_store import TreeStore, TreeNode, TreeEdge
from .sessions_db_reader import SessionsDBThinkingReader, ThinkingChunk
from ..parser.models import ParseRequest, ParseResult, TurnRecord
from ..parser.parser import MathParser
from ..parser.llm_parser import LLMParser
from ..realtime.devin_cli_parser import DevinCliParserProvider


# 降级阈值
FALLBACK_CONFIDENCE_THRESHOLD = 0.5
SITUATION_TEXT_MAX_CHARS = 2000
TRAJECTORY_SEGMENT_MAX_CHARS = 5000

# 增量提取的块大小配置
INCREMENTAL_CHUNK_MIN = 2000   # 块最小字符数
INCREMENTAL_CHUNK_MAX = 4000   # 块最大字符数


class NodeExtractor:
    """
    从AI的trajectory中提取树节点。

    用法：
        extractor = NodeExtractor(tree_store=store)
        node_keys = extractor.extract_nodes_from_trajectory(
            ai_instance_id="ai_1",
            problem_id="case_253",
            trajectory=thinking_text,
            entry_node_key=root_key,
            entry_edge=edge,
        )
    """

    def __init__(
        self,
        tree_store: TreeStore,
        math_parser: Optional[MathParser] = None,
        parser_timeout: int = 180,
    ):
        """
        Args:
            tree_store: 树存储实例
            math_parser: 解析器（默认创建DevinCliParserProvider）
            parser_timeout: parser超时秒数
        """
        self.tree_store = tree_store

        if math_parser is None:
            provider = DevinCliParserProvider(timeout=parser_timeout, max_retries=1)
            llm_parser = LLMParser(mock_response_provider=provider)
            self.math_parser = MathParser(llm_parser=llm_parser)
        else:
            self.math_parser = math_parser

        # 增量提取状态
        self._incremental_offset: int = 0       # 已提取到的字符offset
        self._incremental_parent_key: str = ""   # 上一个提取的节点key（下一个节点的父节点）
        self._incremental_parent_edge: Optional[str] = None  # entry_edge的key
        self._incremental_round_index: int = 0   # 轮次计数器
        self._incremental_buffer: str = ""       # 未处理的文本缓冲区（不够一个块的剩余部分）
        self._incremental_ai_id: str = ""
        self._incremental_problem_id: str = ""
        self._incremental_problem_text: str = ""
        self._incremental_all_keys: List[str] = []  # 所有提取的node_key

        # sessions.db reader（可选，替代MITM的thinking_readable.txt）
        self._db_reader: Optional[SessionsDBThinkingReader] = None

    def extract_nodes_from_trajectory(
        self,
        ai_instance_id: str,
        problem_id: str,
        trajectory: str,
        entry_node_key: str,
        entry_edge: Optional[TreeEdge] = None,
        problem_text: str = "",
    ) -> List[str]:
        """
        从trajectory提取节点，写入tree_store。

        Args:
            ai_instance_id: AI实例ID
            problem_id: 题目ID
            trajectory: AI的thinking文本（thinking_readable.txt内容）
            entry_node_key: AI从哪个节点开始探索
            entry_edge: AI沿哪条边进入（如从根开始则为None）
            problem_text: 题目原文（用于ParseRequest）

        Returns:
            创建的node_key列表
        """
        # 按轮次分割trajectory
        rounds = self._split_trajectory_into_rounds(trajectory)

        if not rounds:
            # 没有分割出轮次，把整个trajectory作为一个节点
            rounds = [trajectory]

        node_keys = []
        parent_node_key = entry_node_key
        parent_edge_key = entry_edge._key if entry_edge else None

        for i, round_text in enumerate(rounds):
            if not round_text or len(round_text.strip()) < 50:
                # 太短的轮次跳过
                continue

            # 解析这个轮次
            parse_result = self._parse_round(
                round_text, i, problem_text, parent_node_key
            )

            # 创建TreeNode
            node = self._create_node_from_parse(
                ai_instance_id=ai_instance_id,
                problem_id=problem_id,
                parse_result=parse_result,
                round_text=round_text,
                round_index=i,
                parent_edge_key=parent_edge_key,
                parent_node_key=parent_node_key,
            )

            # 写入tree_store
            node_key = self.tree_store.add_node(problem_id, node)
            node_keys.append(node_key)

            # 如果有entry_edge，更新edge的_to指向第一个节点
            if i == 0 and entry_edge and entry_edge._key:
                self._update_edge_target(entry_edge._key, node_key)

            # 下一个轮次的父节点是当前节点
            # 但同一AI内的轮次之间不需要新边——它们是同一节点的深化
            # 只有跨AI才需要边。同一AI的多个round合并为一条脉络上的多个节点
            # 节点之间用隐式连接（path_from_root自动处理）
            parent_node_key = node_key
            parent_edge_key = None  # 同一AI内的后续节点没有新边

        return node_keys

    # ============================================================
    # 增量提取（实时模式：AI运行过程中持续提取节点）
    # ============================================================

    def init_incremental(
        self,
        ai_instance_id: str,
        problem_id: str,
        entry_node_key: str,
        entry_edge: Optional[TreeEdge] = None,
        problem_text: str = "",
    ):
        """初始化增量提取状态。在AI启动后调用一次。"""
        self._incremental_offset = 0
        self._incremental_parent_key = entry_node_key
        self._incremental_parent_edge = entry_edge._key if entry_edge else None
        self._incremental_round_index = 0
        self._incremental_buffer = ""
        self._incremental_ai_id = ai_instance_id
        self._incremental_problem_id = problem_id
        self._incremental_problem_text = problem_text
        self._incremental_all_keys = []

    def extract_increment(self, full_thinking: str) -> List[str]:
        """
        增量提取：只处理新增的thinking文本，返回新创建的node_key列表。

        在AI运行过程中周期性调用。每次传入完整的thinking_readable.txt内容，
        本方法只处理上次offset之后的新增部分。

        Args:
            full_thinking: thinking_readable.txt的完整内容

        Returns:
            本次新创建的node_key列表（可能为空——新增内容不够一个块）
        """
        if not full_thinking or len(full_thinking) <= self._incremental_offset:
            return []

        # 提取新增部分
        new_text = full_thinking[self._incremental_offset:]
        self._incremental_offset = len(full_thinking)

        # 把新文本追加到缓冲区
        self._incremental_buffer += new_text

        # 从缓冲区中提取完整的块
        new_keys = []
        while len(self._incremental_buffer) >= INCREMENTAL_CHUNK_MAX:
            # 找到一个合适的分割点（优先在空行处分割）
            chunk, remaining = self._split_buffer_at_boundary()
            if not chunk:
                break

            self._incremental_buffer = remaining

            if len(chunk.strip()) < 50:
                continue

            # 解析并创建节点
            node_key = self._extract_single_chunk(chunk)
            if node_key:
                new_keys.append(node_key)
                self._incremental_all_keys.append(node_key)

        return new_keys

    def flush_incremental(self) -> List[str]:
        """
        刷新：把缓冲区中剩余的不完整块也提取出来。

        在AI终止后调用，确保最后的thinking片段不丢失。
        """
        if not self._incremental_buffer or len(self._incremental_buffer.strip()) < 50:
            return []

        chunk = self._incremental_buffer
        self._incremental_buffer = ""

        node_key = self._extract_single_chunk(chunk)
        if node_key:
            self._incremental_all_keys.append(node_key)
            return [node_key]
        return []

    def get_all_incremental_keys(self) -> List[str]:
        """获取增量提取过程中创建的所有node_key。"""
        return list(self._incremental_all_keys)

    # ============================================================
    # sessions.db模式（替代MITM：从sessions.db实时读取thinking）
    # ============================================================

    def init_sessions_db(
        self,
        ai_instance_id: str,
        problem_id: str,
        devin_session_id: str,
        entry_node_key: str,
        entry_edge: Optional[TreeEdge] = None,
        problem_text: str = "",
    ):
        """
        初始化sessions.db模式的增量提取。

        在AI启动后调用一次。后续用extract_from_sessions_db()轮询新thinking。

        Args:
            devin_session_id: devin cli的session ID
        """
        # 复用增量提取的状态
        self._incremental_offset = 0
        self._incremental_parent_key = entry_node_key
        self._incremental_parent_edge = entry_edge._key if entry_edge else None
        self._incremental_round_index = 0
        self._incremental_buffer = ""
        self._incremental_ai_id = ai_instance_id
        self._incremental_problem_id = problem_id
        self._incremental_problem_text = problem_text
        self._incremental_all_keys = []
        self._processed_node_ids = set()  # 已处理的sessions.db node_id，用于去重

        # 创建sessions.db reader
        self._db_reader = SessionsDBThinkingReader(devin_session_id)
        self._db_reader.init()

    def extract_from_sessions_db(self) -> List[str]:
        """
        从sessions.db轮询新thinking，提取为树节点。

        在AI运行过程中周期性调用。每次返回新创建的node_key列表。

        每个ThinkingChunk对应一个树节点——sessions.db的node边界
        就是天然的轮次边界，不需要像MITM模式那样按字符数切分。

        用_processed_node_ids去重，避免重复提取同一个thinking block。

        Returns:
            本次新创建的node_key列表（可能为空）
        """
        if self._db_reader is None:
            return []

        new_chunks = self._db_reader.poll_new_thinking()
        if not new_chunks:
            return []

        new_keys = []
        for chunk in new_chunks:
            # 去重：跳过已处理的node_id
            if chunk.node_id in self._processed_node_ids:
                continue

            thinking = chunk.thinking
            if not thinking or len(thinking.strip()) < 50:
                # 即使跳过也要记录node_id，避免重复poll
                self._processed_node_ids.add(chunk.node_id)
                continue

            # 每个chunk就是一个节点——sessions.db的node边界是天然的轮次边界
            node_key = self._extract_single_chunk(thinking)
            if node_key:
                new_keys.append(node_key)
                self._incremental_all_keys.append(node_key)
            self._processed_node_ids.add(chunk.node_id)

        return new_keys

    def flush_sessions_db(self) -> List[str]:
        """
        AI终止后调用：获取最后一批未处理的thinking块并提取为节点。
        """
        if self._db_reader is None:
            return []

        remaining_chunks = self._db_reader.flush()
        if not remaining_chunks:
            return []

        new_keys = []
        for chunk in remaining_chunks:
            thinking = chunk.thinking
            if not thinking or len(thinking.strip()) < 50:
                continue

            node_key = self._extract_single_chunk(thinking)
            if node_key:
                new_keys.append(node_key)
                self._incremental_all_keys.append(node_key)

        return new_keys

    def _split_buffer_at_boundary(self) -> tuple:
        """
        从缓冲区开头取一个INCRENTAL_CHUNK_MIN~MAX的块，
        优先在空行边界处分割。
        """
        buf = self._incremental_buffer

        # 如果缓冲区不超过MAX，直接返回全部
        if len(buf) <= INCREMENTAL_CHUNK_MAX:
            return buf, ""

        # 在MAX范围内找最后一个空行
        search_end = INCREMENTAL_CHUNK_MAX
        last_blank = buf.rfind("\n\n", 0, search_end)

        if last_blank > INCREMENTAL_CHUNK_MIN:
            return buf[:last_blank], buf[last_blank+2:]
        else:
            # 没有合适的空行，在MAX处硬切
            # 找最后一个换行符
            last_newline = buf.rfind("\n", 0, search_end)
            if last_newline > INCREMENTAL_CHUNK_MIN:
                return buf[:last_newline], buf[last_newline+1:]
            else:
                return buf[:INCREMENTAL_CHUNK_MAX], buf[INCREMENTAL_CHUNK_MAX:]

    def _extract_single_chunk(self, chunk: str) -> Optional[str]:
        """提取单个chunk为一个树节点。"""
        round_index = self._incremental_round_index
        self._incremental_round_index += 1

        # 解析
        parse_result = self._parse_round(
            chunk, round_index, self._incremental_problem_text,
            self._incremental_parent_key,
        )

        # 创建节点
        node = self._create_node_from_parse(
            ai_instance_id=self._incremental_ai_id,
            problem_id=self._incremental_problem_id,
            parse_result=parse_result,
            round_text=chunk,
            round_index=round_index,
            parent_edge_key=self._incremental_parent_edge,
            parent_node_key=self._incremental_parent_key,
        )

        # 写入tree_store
        node_key = self.tree_store.add_node(self._incremental_problem_id, node)

        # 如果有entry_edge，更新edge的_to指向第一个节点
        if round_index == 0 and self._incremental_parent_edge:
            self._update_edge_target(self._incremental_parent_edge, node_key)
            self._incremental_parent_edge = None  # 只更新一次

        # 更新父节点为当前节点（后续节点的父节点）
        self._incremental_parent_key = node_key

        return node_key

    def _split_trajectory_into_rounds(self, trajectory: str) -> List[str]:
        """
        把trajectory按轮次分割。

        策略：按连续空行分割成段落，然后合并成大约2000-4000字符的块。
        每个块对应一个树节点。

        这是一种简化策略——真正的轮次分割需要sessions.db的user消息边界。
        但在阶段2中，AI终止后批量提取时，我们只有thinking_readable.txt，
        没有sessions.db的轮次边界信息。所以按段落合并是合理的近似。

        关键：控制分块数量——每块2000-4000字符，避免parser调用过多。
        95KB thinking大约分成25-50个块，而不是83个。
        """
        if not trajectory:
            return []

        # 按连续空行分割成段落
        paragraphs = []
        current = []
        for line in trajectory.split("\n"):
            if line.strip() == "":
                if current:
                    paragraphs.append("\n".join(current))
                    current = []
            else:
                current.append(line)
        if current:
            paragraphs.append("\n".join(current))

        # 合并段落成2000-4000字符的块
        TARGET_MIN = 2000
        TARGET_MAX = 4000
        rounds = []
        buffer = []
        buffer_len = 0

        for p in paragraphs:
            if buffer_len + len(p) > TARGET_MAX and buffer:
                # 当前buffer已够大，输出
                rounds.append("\n".join(buffer))
                buffer = [p]
                buffer_len = len(p)
            else:
                buffer.append(p)
                buffer_len += len(p) + 1  # +1 for newline

            if buffer_len >= TARGET_MAX:
                rounds.append("\n".join(buffer))
                buffer = []
                buffer_len = 0

        if buffer:
            merged = "\n".join(buffer)
            if len(merged) > 50:
                rounds.append(merged)

        return rounds

    def _parse_round(
        self,
        round_text: str,
        round_index: int,
        problem_text: str,
        parent_node_key: str,
    ) -> ParseResult:
        """解析单个轮次，返回ParseResult。"""
        try:
            request = ParseRequest(
                agent_output=round_text[:8000],  # parser有token限制
                round_index=round_index,
                problem_text=problem_text,
                history=[],
                current_six_tuple=None,
                run_id=f"node_extract_{parent_node_key}",
                model_version="node_extractor",
                timestamp=str(time.time()),
            )
            return self.math_parser.parse(request)
        except Exception as e:
            print(f"[NodeExtractor] 解析轮次{round_index}失败: {e}")
            return None

    def _create_node_from_parse(
        self,
        ai_instance_id: str,
        problem_id: str,
        parse_result: Optional[ParseResult],
        round_text: str,
        round_index: int,
        parent_edge_key: Optional[str],
        parent_node_key: str = "",
    ) -> TreeNode:
        """从ParseResult创建TreeNode。含降级处理。"""

        if parse_result is None or parse_result.parse_confidence < FALLBACK_CONFIDENCE_THRESHOLD:
            # 降级：parser失败或置信度低
            return TreeNode(
                problem_id=problem_id,
                node_type="internal",
                situation={},  # 空六元组
                situation_text=round_text[:SITUATION_TEXT_MAX_CHARS],
                parent_edge_key=parent_edge_key,
                parent_node_key=parent_node_key,
                created_by_ai=ai_instance_id,
                trajectory_segment={
                    "thinking": round_text[:TRAJECTORY_SEGMENT_MAX_CHARS],
                    "round_index": round_index,
                    "parse_confidence": parse_result.parse_confidence if parse_result else 0.0,
                    "degraded": True,
                },
                status="growing",
            )

        # 正常：从ParseResult提取六元组和situation_text
        six_tuple = parse_result.six_tuple
        situation = {
            "V_t": [v.to_dict() if hasattr(v, "to_dict") else str(v) for v in six_tuple.V_t],
            "F_t": [str(f) for f in six_tuple.F_t],
            "O_t": [o.to_dict() if hasattr(o, "to_dict") else str(o) for o in six_tuple.O_t],
            "U_t": [u.to_dict() if hasattr(u, "to_dict") else str(u) for u in six_tuple.U_t],
            "T_t": [str(t) for t in getattr(six_tuple, "T_t", [])],
            "S_t": [str(s) for s in getattr(six_tuple, "S_t", [])],
        }

        # situation_text从semantic_events提取描述
        situation_text = self._extract_situation_text(parse_result, round_text)

        return TreeNode(
            problem_id=problem_id,
            node_type="internal",
            situation=situation,
            situation_text=situation_text,
            parent_edge_key=parent_edge_key,
            parent_node_key=parent_node_key,
            created_by_ai=ai_instance_id,
            trajectory_segment={
                "thinking": round_text[:TRAJECTORY_SEGMENT_MAX_CHARS],
                "round_index": round_index,
                "parse_confidence": parse_result.parse_confidence,
                "semantic_events_count": len(parse_result.semantic_events),
                "degraded": False,
            },
            status="growing",
        )

    def _extract_situation_text(self, parse_result: ParseResult, round_text: str) -> str:
        """从ParseResult提取自然语言处境描述。"""
        # 尝试从semantic_events的payload提取描述
        descriptions = []
        for event in parse_result.semantic_events:
            # SemanticEvent的payload字典中可能有description字段
            if hasattr(event, "payload") and isinstance(event.payload, dict):
                desc = event.payload.get("description", "")
                if desc:
                    descriptions.append(f"[{event.type}] {desc}")
                else:
                    # 用type+payload的简要信息
                    descriptions.append(f"[{event.type}] {str(event.payload)[:100]}")
            elif hasattr(event, "description"):
                desc = event.description
                if desc:
                    descriptions.append(desc)

        if descriptions:
            return "; ".join(descriptions)[:SITUATION_TEXT_MAX_CHARS]

        # 降级：用round_text前500字符
        return round_text[:500]

    def _update_edge_target(self, edge_key: str, node_key: str):
        """更新边的_to指向新创建的节点。"""
        to_path = f"tree_nodes/{node_key}"
        if self.tree_store.in_memory:
            doc = self.tree_store._memory["tree_edges"].get(edge_key)
            if doc:
                doc["_to"] = to_path
        else:
            col = self.tree_store.db.collection("tree_edges")
            doc = col.get(edge_key)
            if doc:
                doc["_to"] = to_path
                col.replace(doc)
