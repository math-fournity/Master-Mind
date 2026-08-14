"""WP-VLT0 Vault 子包：deny-by-default 访问链。

复用 GV0 的 CompletionArtifactStore CAS 核心，不另造第二套 bundle store。
本包实现：

- Sensitivity registry：public/restricted/solution_bearing/holdout_bearing
- VaultAccessCapability：issuer 签发的最小能力（deny_by_default=true，无 READ_RAW_OBJECT）
- AccessDecision：逐请求重新验签、查撤销、nonce replay、时间窗
- ViewDerivation：sealed source → 精确 view → 精确 sink（机械派生，hashed）
- AccessEvent：append-only 结果账（sequence + previous-event hash）
- VaultBroker：编排完整访问链，不暴露 raw Vault 路径

模型/Solver/worker 只得到 opaque view_id/sink_id + derived bytes，
永远不接触 raw Vault filesystem 路径或 CAS URI。
"""

from .sensitivity import (
    SensitivityLevel,
    SensitivityRegistry,
)
from .access_capability import (
    VaultAccessCapability,
    verify_vault_access_capability,
)
from .access_decision import (
    AccessDecision,
    verify_access_decision,
)
from .view_derivation import (
    ViewDerivation,
    verify_view_derivation,
)
from .access_event import (
    AccessEvent,
    AccessEventLedger,
)
from .broker import VaultBroker

__all__ = [
    "SensitivityLevel",
    "SensitivityRegistry",
    "VaultAccessCapability",
    "verify_vault_access_capability",
    "AccessDecision",
    "verify_access_decision",
    "ViewDerivation",
    "verify_view_derivation",
    "AccessEvent",
    "AccessEventLedger",
    "VaultBroker",
]
