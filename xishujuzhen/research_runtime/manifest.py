"""
manifest.py: 运行manifest创建与管理

对应131号P1-1。

manifest是123号§32步骤1（冻结）的实现：
保存题面、任务类型、成功条件、模型/工具、权限、K/H版本和manifest本身。

冻结声明（P1-1.4）：manifest创建后内容冻结，不允许修改。
R-1风险防线（P1-1.COMP2）：manifest包含hidden_cot_required: false字段。
"""

import os
import json
import hashlib
import uuid
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from pathlib import Path

from arango import ArangoClient

DB_NAME = os.environ.get("ARANGO_DB", "xishujuzhen_math")
DB_USER = os.environ.get("ARANGO_USER", "root")
DB_PASS = os.environ.get("ARANGO_PASS", "REDACTED-DB-PASSWORD")
ARANGO_HOST = os.environ.get("ARANGO_HOST", "http://localhost:8529")

# manifest落盘路径（P1-1.3）
RUNS_DIR = Path(__file__).parent / "runs"


@dataclass
class RunManifest:
    """
    运行manifest（123号§32步骤1冻结项）。

    manifest创建后内容冻结，不允许修改（P1-1.4）。
    hidden_cot_required固定为false（R-1风险防线，P1-1.COMP2）。
    """
    run_id: str
    task_id: str
    task_snapshot: Dict[str, Any]          # Q_0的完整快照（冻结）
    model_version: str
    tool_versions: Dict[str, str]
    budget: Dict[str, float]               # B_t: token/计算/工具/分支/Hint预算
    permissions: Dict[str, Any]            # M_t的权限部分
    k_version: str                         # K图版本（知识库快照哈希）
    h_version: str                         # H图版本（启发规则库快照哈希）
    hidden_cot_required: bool = False      # R-1风险防线：固定为false
    timestamp_start: str = ""
    timestamp_end: str = ""
    manifest_hash: str = ""                # manifest自身的内容哈希

    def __post_init__(self):
        if not self.timestamp_start:
            self.timestamp_start = datetime.now(timezone.utc).isoformat()
        if not self.manifest_hash:
            self.manifest_hash = self._compute_hash()

    def _compute_hash(self) -> str:
        """计算manifest内容哈希（不含hash字段自身）"""
        data = self.to_dict(exclude_hash=True)
        content = json.dumps(data, sort_keys=True, ensure_ascii=False).encode("utf-8")
        return hashlib.sha256(content).hexdigest()

    def to_dict(self, exclude_hash: bool = False) -> dict:
        d = {
            "run_id": self.run_id,
            "task_id": self.task_id,
            "task_snapshot": self.task_snapshot,
            "model_version": self.model_version,
            "tool_versions": self.tool_versions,
            "budget": self.budget,
            "permissions": self.permissions,
            "k_version": self.k_version,
            "h_version": self.h_version,
            "hidden_cot_required": self.hidden_cot_required,
            "timestamp_start": self.timestamp_start,
            "timestamp_end": self.timestamp_end,
        }
        if not exclude_hash:
            d["manifest_hash"] = self.manifest_hash
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "RunManifest":
        return cls(
            run_id=d["run_id"],
            task_id=d["task_id"],
            task_snapshot=d["task_snapshot"],
            model_version=d["model_version"],
            tool_versions=d["tool_versions"],
            budget=d["budget"],
            permissions=d["permissions"],
            k_version=d["k_version"],
            h_version=d["h_version"],
            hidden_cot_required=d.get("hidden_cot_required", False),
            timestamp_start=d.get("timestamp_start", ""),
            timestamp_end=d.get("timestamp_end", ""),
            manifest_hash=d.get("manifest_hash", ""),
        )

    def verify_frozen(self) -> bool:
        """验证manifest内容未被修改（hash一致性检查）"""
        return self._compute_hash() == self.manifest_hash


def create_manifest(
    task: dict,
    model_version: str,
    tool_versions: Dict[str, str],
    budget: Dict[str, float],
    permissions: Dict[str, Any],
    k_version: str = "",
    h_version: str = "",
    run_id: Optional[str] = None,
) -> RunManifest:
    """
    创建运行manifest（P1-1.1/P1-1.2）。

    参数：
    - task: Task schema的dict表示（Q_0快照）
    - model_version: 模型版本字符串
    - tool_versions: 工具版本清单 {tool_name: version}
    - budget: 预算 {token_budget, compute_budget, tool_budget, branch_budget, hint_budget}
    - permissions: 权限配置
    - k_version: K图版本哈希（知识库快照）
    - h_version: H图版本哈希（启发规则库快照）
    - run_id: 可选，不提供则自动生成

    返回：RunManifest对象
    """
    if run_id is None:
        run_id = f"run_{uuid.uuid4().hex[:16]}"

    manifest = RunManifest(
        run_id=run_id,
        task_id=task.get("task_id", ""),
        task_snapshot=task,
        model_version=model_version,
        tool_versions=tool_versions,
        budget=budget,
        permissions=permissions,
        k_version=k_version,
        h_version=h_version,
        hidden_cot_required=False,  # R-1风险防线：固定为false
    )

    return manifest


def save_manifest(manifest: RunManifest) -> str:
    """
    将manifest落盘到文件和ArangoDB（P1-1.3）。

    落盘两个位置：
    1. 文件：xishujuzhen/research_runtime/runs/<run_id>/manifest.json
    2. ArangoDB：run_manifests collection

    返回：manifest文件路径
    """
    # 1. 文件落盘
    run_dir = RUNS_DIR / manifest.run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = run_dir / "manifest.json"

    manifest_data = manifest.to_dict()
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, ensure_ascii=False, indent=2)

    # 2. ArangoDB落盘
    client = ArangoClient(hosts=ARANGO_HOST)
    db = client.db(DB_NAME, username=DB_USER, password=DB_PASS)

    doc = manifest.to_dict()
    doc["_key"] = manifest.run_id
    db.collection("run_manifests").insert(doc, overwrite=False)

    return str(manifest_path)


def load_manifest(run_id: str) -> Optional[RunManifest]:
    """从ArangoDB加载manifest"""
    client = ArangoClient(hosts=ARANGO_HOST)
    db = client.db(DB_NAME, username=DB_USER, password=DB_PASS)

    doc = db.collection("run_manifests").get(run_id)
    if doc is None:
        return None

    return RunManifest.from_dict({k: v for k, v in doc.items() if not k.startswith("_")})


def verify_manifest_frozen(run_id: str) -> dict:
    """
    验证manifest内容冻结（P1-1.4）。
    检查ArangoDB中的manifest hash与重新计算的hash是否一致。
    """
    manifest = load_manifest(run_id)
    if manifest is None:
        return {"exists": False, "is_frozen": False}

    return {
        "exists": True,
        "is_frozen": manifest.verify_frozen(),
        "manifest_hash": manifest.manifest_hash,
        "computed_hash": manifest._compute_hash(),
    }
