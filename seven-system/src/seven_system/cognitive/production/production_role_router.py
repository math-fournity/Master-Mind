"""ProductionRoleRouter — 基于资格矩阵的生产路由。

来自 docs/implementation/05-execution-ports-and-carriers.md RoleQualificationMatrix 节：

资格规则：
- Router 只能选择合同中精确引用且 verdict=PASS、未过期、scope 满足本次运行的 cell；
  禁止通配符、前缀、同 provider 继承或"更强 profile 应当兼容"的推断
- 没有精确 PRODUCTION PASS cell → 生产 dispatch BLOCK（不 fallback 到另一个 carrier
  或 generic profile）
- 未合格 cell 路由 = blocker

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ...contracts.errors import (
    CW_ROUTER_DECISIONS,
    VerificationErrorCode as EC,
)
from ...contracts.completion_contract import VerificationResult
from .role_qualification_matrix import RoleQualificationMatrix, RoleQualificationCell


@dataclass(frozen=True)
class RouterDecision:
    """Router 路由决策结果。

    decision:
    - DISPATCH：找到精确 PRODUCTION PASS cell，可以 dispatch
    - BLOCK：无精确 PRODUCTION PASS cell，生产 dispatch 被阻断
    - BLOCK_UNQUALIFIED：cell 存在但未合格（非 PASS）
    - BLOCK_NO_PASS_CELL：该 role 无任何 PRODUCTION PASS cell
    - BLOCK_EXPIRED：cell 已过期
    """

    decision: str
    role_type_id: str
    carrier_id: str
    model_id: str
    cell: RoleQualificationCell | None = None
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)

    @property
    def is_dispatch(self) -> bool:
        return self.decision == "DISPATCH"

    @property
    def is_block(self) -> bool:
        return self.decision.startswith("BLOCK")

    def to_dict(self) -> dict[str, Any]:
        return {
            "decision": self.decision,
            "role_type_id": self.role_type_id,
            "carrier_id": self.carrier_id,
            "model_id": self.model_id,
            "cell_key": self.cell.cell_key if self.cell else None,
            "error_codes": [ec.value for ec in self.error_codes],
            "details": list(self.details),
        }


@dataclass
class ProductionRoleRouter:
    """ProductionRoleRouter — 基于资格矩阵的生产路由。

    只能选择 PRODUCTION scope 矩阵中 verdict=PASS、未过期、未失效的精确 cell。
    没有 PASS cell → BLOCK，不 fallback 到另一个 carrier 或 generic profile。
    """

    matrix: RoleQualificationMatrix

    def route(
        self,
        *,
        role_type_id: str,
        carrier_id: str,
        model_id: str,
        carrier_profile_hash: str,
    ) -> RouterDecision:
        """路由决策：查找精确 PRODUCTION PASS cell。

        精确匹配维度：role_type_id × carrier_id × model_id × carrier_profile_hash。
        不允许通配符、前缀、继承或"更强 profile 应当兼容"的推断。
        """
        errors: list[EC] = []
        details: list[str] = []

        # 矩阵必须是 PRODUCTION scope
        if not self.matrix.is_production:
            errors.append(EC.CW_QUALIFICATION_SCOPE_INVALID)
            details.append(
                f"router requires PRODUCTION scope, matrix has {self.matrix.qualification_scope}"
            )
            return RouterDecision(
                decision="BLOCK",
                role_type_id=role_type_id,
                carrier_id=carrier_id,
                model_id=model_id,
                error_codes=errors,
                details=details,
            )

        # 查找精确匹配的 cell
        matching_cells: list[RoleQualificationCell] = []
        for cell in self.matrix.cells:
            if cell.role_type_id != role_type_id:
                continue
            if cell.carrier_id != carrier_id:
                continue
            if cell.model_id != model_id:
                continue
            if cell.carrier_profile_ref_and_hash.get("sha256", "") != carrier_profile_hash:
                continue
            if not cell.is_production:
                continue
            matching_cells.append(cell)

        if not matching_cells:
            # 没有任何精确匹配的 PRODUCTION cell
            errors.append(EC.CW_NO_FALLBACK_CARRIER)
            details.append(
                f"no PRODUCTION cell for role={role_type_id} "
                f"carrier={carrier_id} model={model_id} "
                f"profile_hash={carrier_profile_hash[:16]}...; "
                f"no fallback to another carrier or generic profile"
            )
            return RouterDecision(
                decision="BLOCK_NO_PASS_CELL",
                role_type_id=role_type_id,
                carrier_id=carrier_id,
                model_id=model_id,
                error_codes=errors,
                details=details,
            )

        # 检查是否有 PASS cell
        pass_cells = [c for c in matching_cells if c.is_pass and not c.is_invalidated]
        if not pass_cells:
            # 有精确匹配的 cell 但没有 PASS
            # 检查是否过期
            expired_cells = [c for c in matching_cells if c.is_expired]
            if expired_cells:
                errors.append(EC.CW_CELL_EXPIRED)
                details.append(
                    f"cell for role={role_type_id} is EXPIRED, cannot dispatch"
                )
                return RouterDecision(
                    decision="BLOCK_EXPIRED",
                    role_type_id=role_type_id,
                    carrier_id=carrier_id,
                    model_id=model_id,
                    cell=expired_cells[0],
                    error_codes=errors,
                    details=details,
                )

            # 未合格
            non_pass = matching_cells[0]
            errors.append(EC.CW_UNQUALIFIED_CELL_ROUTED)
            details.append(
                f"cell for role={role_type_id} has verdict={non_pass.verdict}, "
                f"not PASS; unqualified cell routed = blocker"
            )
            return RouterDecision(
                decision="BLOCK_UNQUALIFIED",
                role_type_id=role_type_id,
                carrier_id=carrier_id,
                model_id=model_id,
                cell=non_pass,
                error_codes=errors,
                details=details,
            )

        # 检查 cell 是否有结论（PASS/NOT_TESTED/FAILED）
        chosen = pass_cells[0]
        if not chosen.has_conclusion:
            errors.append(EC.CW_CELL_CONCLUSION_MISSING)
            details.append(
                f"cell for role={role_type_id} has no conclusion "
                f"(verdict={chosen.verdict})"
            )
            return RouterDecision(
                decision="BLOCK",
                role_type_id=role_type_id,
                carrier_id=carrier_id,
                model_id=model_id,
                cell=chosen,
                error_codes=errors,
                details=details,
            )

        # 检查是否失效
        if chosen.is_invalidated:
            errors.append(EC.CW_CELL_INVALIDATED)
            details.append(
                f"cell for role={role_type_id} is invalidated: {chosen.invalidation_reason}"
            )
            return RouterDecision(
                decision="BLOCK",
                role_type_id=role_type_id,
                carrier_id=carrier_id,
                model_id=model_id,
                cell=chosen,
                error_codes=errors,
                details=details,
            )

        # DISPATCH
        return RouterDecision(
            decision="DISPATCH",
            role_type_id=role_type_id,
            carrier_id=carrier_id,
            model_id=model_id,
            cell=chosen,
        )

    def route_batch(
        self,
        requests: list[dict[str, str]],
    ) -> list[RouterDecision]:
        """批量路由。每个 request 是 {role_type_id, carrier_id, model_id, carrier_profile_hash}。"""
        results: list[RouterDecision] = []
        for req in requests:
            results.append(
                self.route(
                    role_type_id=req["role_type_id"],
                    carrier_id=req["carrier_id"],
                    model_id=req["model_id"],
                    carrier_profile_hash=req["carrier_profile_hash"],
                )
            )
        return results

    def verify_all_production_cells_have_conclusions(self) -> VerificationResult:
        """验证所有 PRODUCTION 启用的 cell 都有结论（PASS/NOT_TESTED/FAILED）。

        READY_FOR_AUDIT 最低产物：所有生产启用 role×profile×policy 格有结论。
        """
        errors: list[EC] = []
        details: list[str] = []

        for cell in self.matrix.cells:
            if not cell.is_production:
                continue
            if not cell.has_conclusion:
                errors.append(EC.CW_CELL_CONCLUSION_MISSING)
                details.append(
                    f"cell {cell.qualification_cell_id} (role={cell.role_type_id}) "
                    f"has no conclusion (verdict={cell.verdict})"
                )

        verdict = "PASS" if not errors else "FAIL"
        return VerificationResult(verdict=verdict, error_codes=errors, details=details)
