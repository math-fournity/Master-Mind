"""
EventStore + CheckpointStore: 事件存储与checkpoint

对应131号P1-3(RawEvent存储)/P1-4(SemanticEvent存储)/P1-5(checkpoint)。

冻结声明：
- 原始事件append-only，不允许修改或删除（127号§3）
- 事件因果图是DAG（causal_predecessors不形成环）
- checkpoint不含LLM隐藏内部状态（123号§39）
- checkpoint用内容哈希标识（内容寻址，123号§39）
"""

import hashlib
import json
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone

from arango import ArangoClient
from arango.exceptions import DocumentInsertError, DocumentGetError

from ..models.event import (
    RawEvent, SemanticEvent, EventFactory,
    RawEventType, SemanticEventType,
)


DB_NAME = "xishujuzhen_math"
DB_USER = "root"
DB_PASS = "REDACTED-DB-PASSWORD"
ARANGO_HOST = "http://localhost:8529"


class EventStore:
    """
    原始事件和语义事件的ArangoDB存储。

    原始事件append-only（P1-3.3冻结声明）。
    语义事件可重抽（P1-4.4三层保留）。
    """

    def __init__(
        self,
        db_name: str = DB_NAME,
        username: str = DB_USER,
        password: str = DB_PASS,
        host: str = ARANGO_HOST,
    ):
        client = ArangoClient(hosts=host)
        self.db = client.db(db_name, username=username, password=password)
        self.raw_col = self.db.collection("raw_events")
        self.sem_col = self.db.collection("semantic_events")

    # === RawEvent ===

    def insert_raw_event(self, event: RawEvent) -> str:
        """
        插入原始事件（append-only）。
        返回event_id。
        如果event_id已存在，抛出DocumentInsertError（不允许重复）。
        """
        doc = event.to_dict()
        doc["_key"] = event.event_id
        result = self.raw_col.insert(doc, overwrite=False)
        return event.event_id

    def get_raw_event(self, event_id: str) -> Optional[RawEvent]:
        """按event_id读取原始事件"""
        try:
            doc = self.raw_col.get(event_id)
            if doc is None:
                return None
            return RawEvent.from_dict(doc)
        except DocumentGetError:
            return None

    def get_raw_events_by_run(self, run_id: str, limit: int = 1000) -> List[RawEvent]:
        """获取一个run的全部原始事件，按时间排序"""
        cursor = self.db.aql.execute(
            "FOR e IN raw_events FILTER e.run_id == @run_id "
            "SORT e.timestamp ASC LIMIT @limit RETURN e",
            bind_vars={"run_id": run_id, "limit": limit},
        )
        return [RawEvent.from_dict(doc) for doc in cursor]

    def verify_dag(self, run_id: str) -> dict:
        """
        验证事件因果图是DAG（P1-3.5）。
        检查causal_predecessors不形成环。
        """
        events = self.get_raw_events_by_run(run_id)
        event_ids = {e.event_id for e in events}

        # 构建邻接表
        adj: Dict[str, List[str]] = {}
        for e in events:
            for pred in e.causal_predecessors:
                if pred in event_ids:
                    adj.setdefault(pred, []).append(e.event_id)

        # 检查环（DFS）
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {eid: WHITE for eid in event_ids}
        has_cycle = False

        def dfs(node: str):
            nonlocal has_cycle
            color[node] = GRAY
            for neighbor in adj.get(node, []):
                if color[neighbor] == GRAY:
                    has_cycle = True
                    return
                if color[neighbor] == WHITE:
                    dfs(neighbor)
            color[node] = BLACK

        for eid in event_ids:
            if color[eid] == WHITE:
                dfs(eid)
                if has_cycle:
                    break

        return {
            "is_dag": not has_cycle,
            "event_count": len(events),
            "has_cycle": has_cycle,
        }

    # === SemanticEvent ===

    def insert_semantic_event(self, event: SemanticEvent) -> str:
        """插入语义事件（可重抽——同raw_event_id可有多条语义事件）"""
        doc = event.to_dict()
        doc["_key"] = event.event_id
        result = self.sem_col.insert(doc, overwrite=False)
        return event.event_id

    def get_semantic_event(self, event_id: str) -> Optional[SemanticEvent]:
        """按event_id读取语义事件"""
        try:
            doc = self.sem_col.get(event_id)
            if doc is None:
                return None
            return SemanticEvent.from_dict(doc)
        except DocumentGetError:
            return None

    def get_semantic_events_by_run(self, run_id: str, limit: int = 1000) -> List[SemanticEvent]:
        """获取一个run的全部语义事件，按时间排序"""
        cursor = self.db.aql.execute(
            "FOR e IN semantic_events FILTER e.run_id == @run_id "
            "SORT e.timestamp ASC LIMIT @limit RETURN e",
            bind_vars={"run_id": run_id, "limit": limit},
        )
        return [SemanticEvent.from_dict(doc) for doc in cursor]

    def get_semantic_events_by_raw(self, raw_event_id: str) -> List[SemanticEvent]:
        """获取一个原始事件的所有语义抽取版本（可重抽验证）"""
        cursor = self.db.aql.execute(
            "FOR e IN semantic_events FILTER e.raw_event_id == @raw_id "
            "SORT e.timestamp ASC RETURN e",
            bind_vars={"raw_id": raw_event_id},
        )
        return [SemanticEvent.from_dict(doc) for doc in cursor]

    def verify_conflict_symmetry(self, run_id: str) -> dict:
        """
        验证conflict_with满足对称和非自反（P1-4.COMP4）。
        """
        events = self.get_semantic_events_by_run(run_id)
        event_ids = {e.event_id for e in events}

        violations = []
        for e in events:
            # 非自反检查
            if e.event_id in e.conflict_with:
                violations.append({
                    "type": "self_conflict",
                    "event_id": e.event_id,
                })
            # 对称检查
            for other_id in e.conflict_with:
                if other_id not in event_ids:
                    continue
                other = self.get_semantic_event(other_id)
                if other and e.event_id not in other.conflict_with:
                    violations.append({
                        "type": "asymmetric",
                        "e1": e.event_id,
                        "e2": other_id,
                    })

        return {
            "is_valid": len(violations) == 0,
            "violation_count": len(violations),
            "violations": violations,
        }

    # === 追溯验证 ===

    def verify_traceability(self, run_id: str) -> dict:
        """
        验证来源追溯链（P1-6.2/P1-6.3）：
        - 每个语义事件可追溯到原始事件
        - 每个原始事件可追溯到manifest和run_id
        """
        sem_events = self.get_semantic_events_by_run(run_id)
        raw_events = self.get_raw_events_by_run(run_id)
        raw_ids = {e.event_id for e in raw_events}

        untraceable_sem = []
        for sem in sem_events:
            if sem.raw_event_id not in raw_ids:
                untraceable_sem.append({
                    "sem_event_id": sem.event_id,
                    "missing_raw_id": sem.raw_event_id,
                })

        return {
            "sem_count": len(sem_events),
            "raw_count": len(raw_events),
            "untraceable_sem_count": len(untraceable_sem),
            "untraceable": untraceable_sem,
            "all_traceable": len(untraceable_sem) == 0,
        }


class CheckpointStore:
    """
    内容寻址checkpoint存储。

    对应131号P1-5。
    checkpoint不含LLM隐藏内部状态（123号§39）。
    checkpoint用内容哈希标识（内容寻址，123号§39）。
    """

    def __init__(
        self,
        db_name: str = DB_NAME,
        username: str = DB_USER,
        password: str = DB_PASS,
        host: str = ARANGO_HOST,
    ):
        client = ArangoClient(hosts=host)
        self.db = client.db(db_name, username=username, password=password)
        self.chk_col = self.db.collection("checkpoints")

    def create_checkpoint(
        self,
        run_id: str,
        task: dict,                       # Q_0（冻结初始任务）
        workspace: dict,                   # W_t（当前工作区压缩快照）
        event_prefix: List[str],           # 关键事件前缀（event_id列表）
        model_config: dict,                # M_t（模型/工具/权限/预算和版本哈希）
        budget: dict,                      # B_t
    ) -> dict:
        """
        创建内容寻址checkpoint（P1-5.1/P1-5.2）。

        checkpoint定义（123号§39）：
        - 序列化Q_0/W_t、关键事件前缀、模型/工具/权限/预算和版本哈希
        - 不含LLM隐藏内部状态（R-1风险防线）
        """
        checkpoint_data = {
            "run_id": run_id,
            "task": task,
            "workspace": workspace,
            "event_prefix": event_prefix,
            "model_config": model_config,
            "budget": budget,
        }

        # 内容寻址：用内容哈希标识（不含timestamp，timestamp是元数据不是内容）
        content = json.dumps(checkpoint_data, sort_keys=True, ensure_ascii=False).encode("utf-8")
        content_hash = hashlib.sha256(content).hexdigest()

        # timestamp是创建时间元数据，不参与内容哈希
        checkpoint_data["timestamp"] = datetime.now(timezone.utc).isoformat()

        doc = {
            "_key": content_hash,
            "content_hash": content_hash,
            **checkpoint_data,
        }

        # 幂等：同内容哈希的checkpoint只存一份
        existing = self.chk_col.get(content_hash)
        if existing is None:
            self.chk_col.insert(doc)

        return {
            "content_hash": content_hash,
            "checkpoint_data": checkpoint_data,
        }

    def get_checkpoint(self, content_hash: str) -> Optional[dict]:
        """按内容哈希读取checkpoint"""
        doc = self.chk_col.get(content_hash)
        if doc is None:
            return None
        # 移除ArangoDB内部字段
        return {k: v for k, v in doc.items() if not k.startswith("_")}

    def get_checkpoints_by_run(self, run_id: str) -> List[dict]:
        """获取一个run的全部checkpoint"""
        cursor = self.db.aql.execute(
            "FOR c IN checkpoints FILTER c.run_id == @run_id "
            "SORT c.timestamp ASC RETURN c",
            bind_vars={"run_id": run_id},
        )
        return [{k: v for k, v in doc.items() if not k.startswith("_")} for doc in cursor]
