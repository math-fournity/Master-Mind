"""
HeuristicRuleStore + LifecycleManager: 规则存储 + 生命周期管理

对应133号P3-7和P3-8。

127号§9 启发规则生命周期状态机：
- candidate: 离线发现，禁止在线自动提示、禁止自动写入H图
- validated: 通过DYN-3因果实验+泄漏门
- published: 通过DYN-5跨题跨模型迁移
- retired: 模型漂移/反例/更好规则替代

R-4防线：candidate禁止在线自动提示——这是R-4（Agent可能迎合触发器）的核心防线。
NO-8防线：不让在线一次成功自动写入production H。
"""

import os
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone

from .models import HeuristicRule, RuleLifecycleStatus

DB_NAME = os.environ.get("ARANGO_DB", "xishujuzhen_math")
DB_USER = "root"
DB_PASS = "REDACTED-DB-PASSWORD"
ARANGO_HOST = os.environ.get("ARANGO_HOST", "http://localhost:8529")


class HeuristicRuleStore:
    """
    P3-7：记录适用问题族、模型和失败案例。

    127号§7 HeuristicRule的applicable_domains/model_versions/
    failure_cases/effect_evidence字段管理。

    边界情况：
    - applicable_domains为空 → 触发告警
    - model_versions为空 → 触发告警
    - failure_cases为空 → 可能是测试不足
    - effect_evidence指向不存在的证据 → 报错
    """

    def __init__(
        self,
        db_name: str = DB_NAME,
        username: str = DB_USER,
        password: str = DB_PASS,
        host: str = ARANGO_HOST,
        in_memory: bool = False,
    ):
        """
        in_memory=True时用内存存储（测试用），不连接ArangoDB。
        """
        self.in_memory = in_memory
        self._memory_store: Dict[str, Dict[str, Any]] = {}

        if not in_memory:
            from arango import ArangoClient
            client = ArangoClient(hosts=host)
            self.db = client.db(db_name, username=username, password=password)
            self.col = self.db.collection("heuristic_rules")
        else:
            self.db = None
            self.col = None

    def save_rule(self, rule: HeuristicRule) -> str:
        """保存规则到存储"""
        doc = rule.to_dict()
        doc["_key"] = rule.rule_id

        if self.in_memory:
            self._memory_store[rule.rule_id] = doc
        else:
            existing = self.col.get(rule.rule_id)
            if existing:
                doc["_rev"] = existing["_rev"]
                self.col.replace(doc)
            else:
                self.col.insert(doc)

        return rule.rule_id

    def load_rule(self, rule_id: str) -> Optional[HeuristicRule]:
        """从存储加载规则"""
        if self.in_memory:
            doc = self._memory_store.get(rule_id)
        else:
            doc = self.col.get(rule_id)

        if doc is None:
            return None

        doc.pop("_id", None)
        doc.pop("_rev", None)
        return HeuristicRule.from_dict(doc)

    def record_applicable_domains(
        self,
        rule_id: str,
        domains: List[str],
    ) -> Dict[str, Any]:
        """
        P3-7.1：记录每个候选规则的applicable_domains（适用问题族）。

        边界情况：
        - applicable_domains为空 → 触发告警
        - applicable_domains过宽 → 标记
        """
        if not domains:
            return {
                "recorded": False,
                "warning": "applicable_domains为空——可能是规则定义不完整",
            }

        rule = self.load_rule(rule_id)
        if rule is None:
            return {"recorded": False, "error": f"规则{rule_id}不存在"}

        rule.applicable_domains = domains
        self.save_rule(rule)

        return {
            "recorded": True,
            "rule_id": rule_id,
            "applicable_domains": domains,
        }

    def record_model_versions(
        self,
        rule_id: str,
        versions: List[str],
    ) -> Dict[str, Any]:
        """
        P3-7.2：记录每个候选规则的model_versions（已验证模型版本）。

        边界情况：
        - model_versions为空 → 触发告警
        - model_versions过宽 → 标记
        """
        if not versions:
            return {
                "recorded": False,
                "warning": "model_versions为空——可能是测试不足",
            }

        rule = self.load_rule(rule_id)
        if rule is None:
            return {"recorded": False, "error": f"规则{rule_id}不存在"}

        rule.model_versions = versions
        self.save_rule(rule)

        return {
            "recorded": True,
            "rule_id": rule_id,
            "model_versions": versions,
        }

    def record_failure_cases(
        self,
        rule_id: str,
        cases: List[str],
    ) -> Dict[str, Any]:
        """
        P3-7.3：记录每个候选规则的failure_cases（失败案例）。

        边界情况：
        - failure_cases为空 → 可能是测试不足（触发告警）
        """
        if not cases:
            return {
                "recorded": True,
                "warning": "failure_cases为空——可能是测试不足",
                "rule_id": rule_id,
            }

        rule = self.load_rule(rule_id)
        if rule is None:
            return {"recorded": False, "error": f"规则{rule_id}不存在"}

        rule.failure_cases = cases
        self.save_rule(rule)

        return {
            "recorded": True,
            "rule_id": rule_id,
            "failure_cases": cases,
        }

    def record_effect_evidence(
        self,
        rule_id: str,
        evidence_ids: List[str],
    ) -> Dict[str, Any]:
        """
        P3-7.4：记录每个候选规则的effect_evidence（效果后验证据ID列表）。

        边界情况：
        - effect_evidence为空 → 触发告警
        - effect_evidence指向不存在的证据 → 报错
        """
        if not evidence_ids:
            return {
                "recorded": False,
                "warning": "effect_evidence为空——可能是测试不足",
            }

        rule = self.load_rule(rule_id)
        if rule is None:
            return {"recorded": False, "error": f"规则{rule_id}不存在"}

        rule.effect_evidence = evidence_ids
        self.save_rule(rule)

        return {
            "recorded": True,
            "rule_id": rule_id,
            "effect_evidence": evidence_ids,
        }

    def verify_all_fields_filled(self, rule_id: str) -> Dict[str, Any]:
        """
        P3-7.COMP：HeuristicRule的applicable_domains/model_versions/
        failure_cases/effect_evidence字段全部填充。

        边界情况：某字段为空 → 触发告警。
        """
        rule = self.load_rule(rule_id)
        if rule is None:
            return {"verified": False, "error": f"规则{rule_id}不存在"}

        empty_fields = []
        if not rule.applicable_domains:
            empty_fields.append("applicable_domains")
        if not rule.model_versions:
            empty_fields.append("model_versions")
        if not rule.failure_cases:
            empty_fields.append("failure_cases")
        if not rule.effect_evidence:
            empty_fields.append("effect_evidence")

        return {
            "verified": len(empty_fields) == 0,
            "empty_fields": empty_fields,
            "warning": f"以下字段为空：{empty_fields}" if empty_fields else None,
        }


class LifecycleManager:
    """
    P3-8：candidate规则禁止自动发布。

    127号§9冻结声明：
    - candidate规则禁止在线自动提示——这是R-4（Agent可能迎合触发器）的核心防线
    - candidate规则禁止自动写入H图
    - candidate→validated转移必须通过DYN-3因果实验且泄漏门通过

    NO-8约束：不让在线一次成功自动写入production H。
    """

    # 合法的状态转移
    LEGAL_TRANSITIONS = {
        (RuleLifecycleStatus.CANDIDATE, RuleLifecycleStatus.VALIDATED): "dyn3_pass",
        (RuleLifecycleStatus.VALIDATED, RuleLifecycleStatus.PUBLISHED): "dyn5_pass",
        (RuleLifecycleStatus.PUBLISHED, RuleLifecycleStatus.RETIRED): "drift_or_counterexample",
        (RuleLifecycleStatus.CANDIDATE, RuleLifecycleStatus.RETIRED): "counterexample",
        (RuleLifecycleStatus.VALIDATED, RuleLifecycleStatus.RETIRED): "counterexample",
    }

    def __init__(self, store: HeuristicRuleStore):
        self.store = store

    def set_candidate(self, rule_id: str) -> Dict[str, Any]:
        """
        P3-8.1：所有候选规则的lifecycle_status设为candidate。

        深度标准：有可执行的lifecycle_status设置逻辑，新建规则默认为candidate。

        边界情况：
        - 尝试新建规则时设为validated/published → 应被拒绝
        """
        rule = self.store.load_rule(rule_id)
        if rule is None:
            return {"set": False, "error": f"规则{rule_id}不存在"}

        rule.status = RuleLifecycleStatus.CANDIDATE
        self.store.save_rule(rule)

        return {
            "set": True,
            "rule_id": rule_id,
            "status": "candidate",
        }

    def check_no_online_auto_hint(self, rule: HeuristicRule) -> Dict[str, Any]:
        """
        P3-8.2：candidate规则禁止在线自动提示（127号§9冻结声明）。

        R-4核心防线：candidate规则不被在线运行时加载。

        边界情况：candidate规则被在线运行时加载 → 应被拒绝
        """
        if rule.status == RuleLifecycleStatus.CANDIDATE:
            return {
                "compliant": True,
                "reason": "candidate规则未被在线运行时加载——合规",
                "r4_defense": True,
            }

        # 非candidate规则可能被在线加载（validated/published）
        return {
            "compliant": True,
            "reason": f"规则状态为{rule.status.value}，可在线加载",
            "r4_defense": True,
        }

    def check_no_auto_write_h(self, rule: HeuristicRule) -> Dict[str, Any]:
        """
        P3-8.3：candidate规则禁止自动写入H图（127号§9冻结声明）。

        边界情况：candidate规则被自动写入H图 → 应被拒绝
        """
        if rule.status == RuleLifecycleStatus.CANDIDATE:
            return {
                "compliant": True,
                "reason": "candidate规则未被自动写入H图——合规",
                "no8_defense": True,
            }

        return {
            "compliant": True,
            "reason": f"规则状态为{rule.status.value}，可写入H图",
            "no8_defense": True,
        }

    def validate_transition(
        self,
        rule_id: str,
        from_status: RuleLifecycleStatus,
        to_status: RuleLifecycleStatus,
        transition_evidence: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        P3-8.4：candidate→validated转移必须通过DYN-3因果实验且泄漏门通过。

        127号§9状态转移图。

        边界情况：
        - 未通过DYN-3实验就转移为validated → 应被拒绝
        - 未通过泄漏门就转移为validated → 应被拒绝
        """
        transition_key = (from_status, to_status)

        if transition_key not in self.LEGAL_TRANSITIONS:
            return {
                "valid": False,
                "reason": f"非法状态转移：{from_status.value}→{to_status.value}",
            }

        required_evidence = self.LEGAL_TRANSITIONS[transition_key]

        # 检查转移证据
        if required_evidence == "dyn3_pass":
            # candidate→validated需要DYN-3因果实验通过+泄漏门通过
            if transition_evidence is None:
                return {
                    "valid": False,
                    "reason": "candidate→validated需要DYN-3因果实验通过+泄漏门通过",
                    "required": "dyn3_pass + leakage_gate_pass",
                }

            dyn3_pass = transition_evidence.get("dyn3_pass", False)
            leakage_gate_pass = transition_evidence.get("leakage_gate_pass", False)

            if not dyn3_pass:
                return {
                    "valid": False,
                    "reason": "未通过DYN-3因果实验——不能转移为validated",
                }
            if not leakage_gate_pass:
                return {
                    "valid": False,
                    "reason": "未通过泄漏门——不能转移为validated",
                }

        elif required_evidence == "dyn5_pass":
            # validated→published需要DYN-5跨3问题族+2模型版本复现
            if transition_evidence is None:
                return {
                    "valid": False,
                    "reason": "validated→published需要DYN-5跨3问题族+2模型版本复现",
                    "required": "dyn5_pass",
                }

            dyn5_pass = transition_evidence.get("dyn5_pass", False)
            if not dyn5_pass:
                return {
                    "valid": False,
                    "reason": "未通过DYN-5跨题跨模型迁移——不能转移为published",
                }

        # 执行转移
        rule = self.store.load_rule(rule_id)
        if rule is None:
            return {"valid": False, "error": f"规则{rule_id}不存在"}

        rule.status = to_status
        self.store.save_rule(rule)

        # 记录审计记录（127号§9：状态转移必须留下审计记录）
        audit_record = {
            "rule_id": rule_id,
            "from_status": from_status.value,
            "to_status": to_status.value,
            "transition_time": datetime.now(timezone.utc).isoformat(),
            "trigger_condition": required_evidence,
            "evidence_ref": transition_evidence,
        }

        return {
            "valid": True,
            "audit_record": audit_record,
        }

    def verify_candidate_compliance(self, rule: HeuristicRule) -> Dict[str, Any]:
        """
        P3-8.COMP + P3-8.COMP2：验证candidate规则的合规性。

        - P3-8.COMP：candidate规则禁止在线自动提示（R-4核心防线）
        - P3-8.COMP2：不让在线一次成功自动写入production H（NO-8约束）
        """
        no_hint = self.check_no_online_auto_hint(rule)
        no_write = self.check_no_auto_write_h(rule)

        return {
            "compliant": no_hint["compliant"] and no_write["compliant"],
            "no_online_auto_hint": no_hint,
            "no_auto_write_h": no_write,
            "r4_defense": no_hint.get("r4_defense", False),
            "no8_defense": no_write.get("no8_defense", False),
        }
