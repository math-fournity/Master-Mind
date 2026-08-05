"""
卡点检测 + 7类卡点 + 校准集

对应132号P2-7。

123号§32步骤7（诊断决策）：
- Controller判断是继续观察、提出诊断问题、调用工具、干预还是停止
- 不把所有停滞都视为应提示

7类卡点（系统探讨.md§15.3 + 123号§32）：
1. strategy_exhaustion: 策略耗尽——所有已知策略都尝试过
2. evidence_gap: 证据缺口——缺少关键证据
3. representation_stuck: 表示停滞——当前表示无法推进
4. obligation_deadlock: 义务死锁——循环依赖导致无法释放
5. budget_depletion: 预算耗尽——token/计算/工具预算不足
6. false_stall: 假性停滞——正常探索被误判为停滞
7. answer_leakage_risk: 答案泄漏风险——继续可能泄漏答案

冻结声明：
- 卡点检测基于工具证据和结构进展，不只相信自报（R-4风险防线）
- 测precision、recall、误触发时间和"把正常探索误判为停滞"的比例

边界情况：
- 无卡点（正常运行）
- 多种卡点同时出现
- 假性停滞（正常探索被误判）
- 自报停滞与工具进展不一致（gaming检测）
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
from arango import ArangoClient

DB_NAME = "xishujuzhen_math"
DB_USER = "root"
DB_PASS = "REDACTED-DB-PASSWORD"
ARANGO_HOST = "http://localhost:8529"


class StallType(str, Enum):
    """
    7类卡点（系统探讨.md§15.3 + 123号§32）。
    """
    STRATEGY_EXHAUSTION = "strategy_exhaustion"       # 策略耗尽
    EVIDENCE_GAP = "evidence_gap"                     # 证据缺口
    REPRESENTATION_STUCK = "representation_stuck"     # 表示停滞
    OBLIGATION_DEADLOCK = "obligation_deadlock"       # 义务死锁
    BUDGET_DEPLETION = "budget_depletion"             # 预算耗尽
    FALSE_STALL = "false_stall"                       # 假性停滞（正常探索被误判）
    ANSWER_LEAKAGE_RISK = "answer_leakage_risk"       # 答案泄漏风险


@dataclass
class StallDetection:
    """
    卡点检测结果。
    """
    stall_type: StallType
    confidence: float                         # 置信度0-1
    evidence: List[str] = field(default_factory=list)  # 检测证据（工具/结构进展）
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    is_self_reported: bool = False            # 是否为自报（R-4风险：需工具证据验证）

    def to_dict(self) -> dict:
        return {
            "stall_type": self.stall_type.value,
            "confidence": self.confidence,
            "evidence": self.evidence,
            "timestamp": self.timestamp,
            "is_self_reported": self.is_self_reported,
        }


@dataclass
class StallAnnotation:
    """
    人工标注校准集条目（P2-7.2）。
    """
    annotation_id: str
    run_id: str
    timestamp: str
    stall_type: StallType                     # 人工标注的卡点类型
    is_stall: bool                            # 人工判断是否真的停滞
    notes: str = ""

    def to_dict(self) -> dict:
        return {
            "annotation_id": self.annotation_id,
            "run_id": self.run_id,
            "timestamp": self.timestamp,
            "stall_type": self.stall_type.value,
            "is_stall": self.is_stall,
            "notes": self.notes,
        }


class StallDetector:
    """
    卡点检测器（DYN-2核心）。

    冻结声明：
    - 基于工具证据和结构进展，不只相信自报（R-4风险防线）
    - 不把所有停滞都视为应提示（123号§32步骤7）
    """

    def __init__(self):
        pass

    def detect(
        self,
        progress_history: List[Dict[str, Any]],
        budget: Dict[str, Any],
        obligations: Dict[str, Any],
        self_reported_stall: bool = False,
    ) -> List[StallDetection]:
        """
        从事件流和状态中检测卡点。

        参数：
        - progress_history: 进展向量历史列表
        - budget: 预算状态
        - obligations: 义务状态（含SCC信息）
        - self_reported_stall: Agent自报停滞

        返回检测到的卡点列表。
        """
        detections = []

        # 1. 策略耗尽——进展向量连续无改善
        if len(progress_history) >= 3:
            recent = progress_history[-3:]
            all_no_improve = all(p.get("relation", "") in ("equal", "worsened") for p in recent)
            if all_no_improve:
                detections.append(StallDetection(
                    stall_type=StallType.STRATEGY_EXHAUSTION,
                    confidence=0.8,
                    evidence=[f"连续{len(recent)}次进展无改善"],
                    is_self_reported=False,
                ))

        # 2. 证据缺口——活动候选数高但证据数低
        if progress_history:
            latest = progress_history[-1]
            v = latest.get("vector", {})
            u_t = v.get("u_t", 0)  # 无证据候选数
            if u_t > 5:  # 阈值可配置
                detections.append(StallDetection(
                    stall_type=StallType.EVIDENCE_GAP,
                    confidence=0.7,
                    evidence=[f"无证据活动候选数={u_t}"],
                    is_self_reported=False,
                ))

        # 3. 表示停滞——同一表示ID持续无进展
        # （需要representation_history，简化版用progress_history中的representation_id）
        rep_ids = [p.get("representation_id", "") for p in progress_history[-5:]]
        if len(rep_ids) >= 5 and len(set(rep_ids)) == 1:
            detections.append(StallDetection(
                stall_type=StallType.REPRESENTATION_STUCK,
                confidence=0.6,
                evidence=[f"同一表示{rep_ids[-1]}持续5步无变化"],
                is_self_reported=False,
            ))

        # 4. 义务死锁——SCC存在
        sccs = obligations.get("sccs", [])
        if sccs:
            detections.append(StallDetection(
                stall_type=StallType.OBLIGATION_DEADLOCK,
                confidence=0.9,
                evidence=[f"检测到{len(sccs)}个SCC（循环依赖）"],
                is_self_reported=False,
            ))

        # 5. 预算耗尽
        for budget_type, values in budget.items():
            remaining = values.get("remaining", 0)
            if remaining <= 0:
                detections.append(StallDetection(
                    stall_type=StallType.BUDGET_DEPLETION,
                    confidence=1.0,
                    evidence=[f"{budget_type}预算耗尽（remaining={remaining}）"],
                    is_self_reported=False,
                ))
                break  # 一种预算耗尽就够

        # 6. 假性停滞——自报停滞但工具有进展
        if self_reported_stall:
            # 检查最近进展向量是否有改善
            if progress_history:
                latest = progress_history[-1]
                if latest.get("relation", "") == "improved":
                    detections.append(StallDetection(
                        stall_type=StallType.FALSE_STALL,
                        confidence=0.85,
                        evidence=["自报停滞但进展向量有改善——可能是gaming（R-4风险）"],
                        is_self_reported=True,
                    ))

        # 7. 答案泄漏风险——简化版：如果Hint等级已达到H2
        # （完整版需要检查Hint内容是否接近答案等价）
        # 这里只做框架，实际检测在Phase 3-4完善

        return detections

    def classify(
        self,
        detections: List[StallDetection],
    ) -> Dict[str, Any]:
        """
        分类汇总检测结果。

        返回：
        - has_stall: 是否有真正的停滞
        - stall_types: 检测到的卡点类型
        - has_false_stall: 是否有假性停滞
        - needs_hint: 是否需要提示（不把所有停滞都视为应提示）
        """
        if not detections:
            return {
                "has_stall": False,
                "stall_types": [],
                "has_false_stall": False,
                "needs_hint": False,
                "action": "continue_observing",
            }

        # 过滤掉假性停滞
        real_stalls = [d for d in detections if d.stall_type != StallType.FALSE_STALL]
        false_stalls = [d for d in detections if d.stall_type == StallType.FALSE_STALL]

        # 假性停滞——不应提示
        if false_stalls and not real_stalls:
            return {
                "has_stall": False,
                "stall_types": [d.stall_type.value for d in detections],
                "has_false_stall": True,
                "needs_hint": False,
                "action": "continue_observing",  # 假性停滞——继续观察
                "gaming_warning": True,
            }

        # 真正的停滞——需要判断是否提示
        # 预算耗尽——停止而非提示
        budget_stalls = [d for d in real_stalls if d.stall_type == StallType.BUDGET_DEPLETION]
        if budget_stalls:
            return {
                "has_stall": True,
                "stall_types": [d.stall_type.value for d in detections],
                "has_false_stall": len(false_stalls) > 0,
                "needs_hint": False,
                "action": "stop_or_escalate",
            }

        # 其他停滞——可以提示
        return {
            "has_stall": True,
            "stall_types": [d.stall_type.value for d in detections],
            "has_false_stall": len(false_stalls) > 0,
            "needs_hint": True,
            "action": "ask_diagnostic_question",
        }


class StallAnnotationStore:
    """
    人工标注校准集存储（P2-7.2）。
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
        self.col = self.db.collection("stall_annotations")

    def insert_annotation(self, ann: StallAnnotation) -> str:
        """插入人工标注。"""
        doc = ann.to_dict()
        doc["_key"] = ann.annotation_id
        result = self.col.insert(doc)
        return result["_key"]

    def get_annotations_for_run(self, run_id: str) -> List[Dict[str, Any]]:
        """获取一个运行的所有标注。"""
        aql = "FOR a IN stall_annotations FILTER a.run_id == @run_id SORT a.timestamp RETURN a"
        cursor = self.db.aql.execute(aql, bind_vars={"run_id": run_id})
        results = []
        for doc in cursor:
            doc.pop("_id", None)
            doc.pop("_rev", None)
            results.append(doc)
        return results

    def compute_precision_recall(
        self,
        detector: StallDetector,
        run_id: str,
        progress_history: List[Dict[str, Any]],
        budget: Dict[str, Any],
        obligations: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        计算precision/recall/误触发时间/误判比例（P2-7.4）。

        precision = TP / (TP + FP)
        recall = TP / (TP + FN)
        误判比例 = FP / (FP + TN)  （把正常探索误判为停滞的比例）
        """
        # 获取人工标注
        annotations = self.get_annotations_for_run(run_id)
        if not annotations:
            return {
                "error": "无人工标注——无法计算precision/recall",
                "run_id": run_id,
            }

        # 人工标注的停滞时间点
        human_stalls = {a["timestamp"] for a in annotations if a["is_stall"]}
        human_non_stalls = {a["timestamp"] for a in annotations if not a["is_stall"]}

        # 检测器在每个标注时间点的检测结果
        # （简化版：用整个progress_history做一次检测，实际应按时间点分别检测）
        detections = detector.detect(progress_history, budget, obligations)
        detected_stall = len(detections) > 0

        # 简化版precision/recall计算
        # 实际版需要按时间点对齐
        tp = 0  # 检测到停滞且人工标注为停滞
        fp = 0  # 检测到停滞但人工标注为非停滞
        fn = 0  # 未检测到停滞但人工标注为停滞
        tn = 0  # 未检测到停滞且人工标注为非停滞

        for ann in annotations:
            # 简化：如果检测器检测到停滞且该标注是停滞，算TP
            # 实际应按时间点对齐
            if detected_stall and ann["is_stall"]:
                tp += 1
            elif detected_stall and not ann["is_stall"]:
                fp += 1
            elif not detected_stall and ann["is_stall"]:
                fn += 1
            else:
                tn += 1

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        false_alarm_rate = fp / (fp + tn) if (fp + tn) > 0 else 0.0  # 误判比例

        return {
            "run_id": run_id,
            "precision": precision,
            "recall": recall,
            "false_alarm_rate": false_alarm_rate,  # 把正常探索误判为停滞的比例
            "tp": tp,
            "fp": fp,
            "fn": fn,
            "tn": tn,
            "total_annotations": len(annotations),
        }
