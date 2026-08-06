"""
WorkspaceStore: 工作区读写接口

对应132号P2-2.3。

冻结声明（127号§2）：
- W_t只能由版本化Reducer按明确字段规则派生，不能被直接修改
- 临时假设进入F_t，不进入V_t
- 被拒绝路线进入D_t，不与representation共用R

边界情况（132号P2-2.3）：
- 空工作区
- 字段缺失
- 并发写入
- W_t不可直接修改（只能通过Reducer派生）
"""

import os
from typing import Optional, Dict, Any, List
from datetime import datetime, timezone
from arango import ArangoClient

from ..models.workspace import Workspace

DB_NAME = os.environ.get("ARANGO_DB", "xishujuzhen_math")
DB_USER = os.environ.get("ARANGO_USER", "root")
DB_PASS = os.environ.get("ARANGO_PASS", "REDACTED-DB-PASSWORD")
ARANGO_HOST = os.environ.get("ARANGO_HOST", "http://localhost:8529")


class WorkspaceStore:
    """
    工作区ArangoDB存储。

    W_t只能由版本化Reducer派生（P2-2.COMP2）。
    update_workspace拒绝直接修改W_t内容，只允许更新元数据。
    W_t内容的更新必须通过StateReducer派生新快照。
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
        self.col = self.db.collection("workspaces")

    def create_workspace(
        self,
        workspace_id: str,
        task_id: str,
        timestamp: Optional[str] = None,
    ) -> str:
        """
        创建空工作区。

        边界情况：空工作区（6类全部为空）、字段缺失（用默认值）。
        """
        if timestamp is None:
            timestamp = datetime.now(timezone.utc).isoformat()

        ws = Workspace(
            workspace_id=workspace_id,
            task_id=task_id,
            timestamp=timestamp,
        )
        doc = ws.to_dict()
        doc["_key"] = workspace_id
        result = self.col.insert(doc)
        return result["_key"]

    def create_workspace_from_dict(
        self,
        workspace_id: str,
        task_id: str,
        ws_dict: Dict[str, Any],
        timestamp: Optional[str] = None,
        reducer_version: str = "v1",
    ) -> str:
        """
        从Reducer派生的W_t字典创建工作区快照。

        这是W_t内容写入的唯一合法路径——通过版本化Reducer派生。
        直接修改W_t内容应走此路径（Reducer产生新快照），不走update_workspace。
        """
        if timestamp is None:
            timestamp = datetime.now(timezone.utc).isoformat()

        doc = {
            "_key": workspace_id,
            "workspace_id": workspace_id,
            "task_id": task_id,
            "timestamp": timestamp,
            "reducer_version": reducer_version,   # P2-2.COMP2: 版本化Reducer
            **ws_dict,
        }
        result = self.col.insert(doc)
        return result["_key"]

    def read_workspace(self, workspace_id: str) -> Optional[Dict[str, Any]]:
        """
        读取工作区。

        边界情况：workspace_id不存在（返回None）。
        """
        doc = self.col.get(workspace_id)
        if doc is None:
            return None
        # 移除ArangoDB内部字段
        doc.pop("_id", None)
        doc.pop("_rev", None)
        return doc

    def update_workspace_metadata(
        self,
        workspace_id: str,
        metadata: Dict[str, Any],
    ) -> bool:
        """
        更新工作区元数据（如timestamp、reducer_version）。

        注意：此方法不更新W_t内容（V_t/F_t/O_t/R_t/D_t/E_t）。
        W_t内容的更新必须通过create_workspace_from_dict创建新快照。
        直接修改W_t内容违反P2-2.COMP2冻结声明。
        """
        doc = self.col.get(workspace_id)
        if doc is None:
            return False

        # 只允许更新元数据字段，不允许更新W_t内容字段
        w_t_fields = {"V_t", "F_t", "O_t", "R_t", "D_t", "E_t"}
        for key in metadata:
            if key in w_t_fields:
                raise ValueError(
                    f"不能直接修改W_t内容字段 '{key}'——"
                    f"W_t只能由版本化Reducer派生（P2-2.COMP2冻结声明）。"
                    f"请通过create_workspace_from_dict创建新快照。"
                )

        doc.update(metadata)
        self.col.replace(doc)
        return True

    def list_workspaces(
        self,
        task_id: Optional[str] = None,
        limit: int = 100,
    ) -> List[Dict[str, Any]]:
        """
        列出工作区，可按task_id过滤。

        边界情况：无工作区、task_id无匹配。
        """
        if task_id:
            aql = "FOR ws IN workspaces FILTER ws.task_id == @task_id SORT ws.timestamp DESC LIMIT @limit RETURN ws"
            bind = {"task_id": task_id, "limit": limit}
        else:
            aql = "FOR ws IN workspaces SORT ws.timestamp DESC LIMIT @limit RETURN ws"
            bind = {"limit": limit}

        cursor = self.db.aql.execute(aql, bind_vars=bind)
        results = []
        for doc in cursor:
            doc.pop("_id", None)
            doc.pop("_rev", None)
            results.append(doc)
        return results

    def verify_w_t_separation(self, workspace_id: str) -> Dict[str, bool]:
        """
        验证V_t/F_t分离（P2-2.COMP3/COMP4）。

        检查：
        - 临时假设不在V_t中（P2-2.COMP3）
        - 被拒绝路线不在R_t中（P2-2.COMP4）

        返回各检查项的通过状态。
        """
        doc = self.read_workspace(workspace_id)
        if doc is None:
            return {"exists": False}

        v_t = doc.get("V_t", {})
        f_t = doc.get("F_t", {})
        r_t = doc.get("R_t", {})
        d_t = doc.get("D_t", {})

        # P2-2.COMP3: 临时假设进入F_t，不进入V_t
        v_all = set(v_t.get("verified_premises", []) +
                    v_t.get("verified_lemmas", []) +
                    v_t.get("verified_tool_results", []))
        f_temp = set(f_t.get("temporary_assumptions", []))
        v_f_overlap = v_all & f_temp

        # P2-2.COMP4: 被拒绝路线进入D_t，不与representation共用R
        r_all = set(r_t.get("active_representations", []) +
                    r_t.get("pending_transforms", []))
        d_rejected = set(d_t.get("rejected_branches", []))
        r_d_overlap = r_all & d_rejected

        return {
            "exists": True,
            "comp3_temp_not_in_v": len(v_f_overlap) == 0,   # 临时假设不在V_t
            "comp4_rejected_not_in_r": len(r_d_overlap) == 0,  # 被拒绝路线不在R_t
            "v_f_overlap": list(v_f_overlap),
            "r_d_overlap": list(r_d_overlap),
        }
