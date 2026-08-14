"""ActiveReleasePointer — active release 指针快照。

来自 WP-OP1：active release pointer、mid-Epoch 版本变更 = blocker、
release activation 需要 HumanGate。

关键约束（blocker）：
- mid-Epoch 版本变更 → OP_MID_EPOCH_VERSION_CHANGE
- release activation 未经过 HumanGate → OP_ACTIVE_RELEASE_NOT_GATED
- release 状态不在 OP_RELEASE_STATES → OP_RELEASE_STATE_INVALID

SIDE_EFFECT_FREE：纯内存模拟。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    OP_RELEASE_STATES,
    VerificationErrorCode as EC,
)


class ActiveReleasePointerError(Exception):
    """Active release pointer 错误。"""

    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


@dataclass
class ActiveReleasePointer:
    """Active release 指针快照。

    记录当前 active release 的版本、状态、绑定的 epoch。
    mid-Epoch 版本变更是 blocker。
    release activation 需要 HumanGate 签名。
    """

    pointer_id: str
    release_version: str
    state: str = "FROZEN"
    bound_epoch_id: str = ""
    human_gate_ref: str = ""
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "pointer_id": self.pointer_id,
            "release_version": self.release_version,
            "state": self.state,
            "bound_epoch_id": self.bound_epoch_id,
            "human_gate_ref": self.human_gate_ref,
            "content_hash": self.content_hash,
        }

    def compute_content_hash(self) -> str:
        d = self.to_dict()
        d["content_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()


class ActiveReleasePointerManager:
    """Active release pointer 管理器。

    管理 release pointer 的状态转换：
    FROZEN → ACTIVATION_REQUESTED → GATED → ACTIVATED
    或 FROZEN → ACTIVATION_REQUESTED → REJECTED

    mid-Epoch 版本变更是 blocker。
    activation 需要 HumanGate。

    SIDE_EFFECT_FREE：纯内存模拟。
    """

    def __init__(self) -> None:
        self._pointers: dict[str, ActiveReleasePointer] = {}
        self._active_pointer_id: str | None = None

    @property
    def pointers(self) -> list[ActiveReleasePointer]:
        return list(self._pointers.values())

    @property
    def active_pointer(self) -> ActiveReleasePointer | None:
        if self._active_pointer_id is None:
            return None
        return self._pointers.get(self._active_pointer_id)

    def create_pointer(
        self,
        *,
        pointer_id: str,
        release_version: str,
        bound_epoch_id: str,
    ) -> ActiveReleasePointer:
        """创建 frozen release pointer。"""
        if pointer_id in self._pointers:
            raise ActiveReleasePointerError(
                EC.REQUIRED_FIELD_MISSING,
                f"pointer {pointer_id} already exists",
            )
        ptr = ActiveReleasePointer(
            pointer_id=pointer_id,
            release_version=release_version,
            state="FROZEN",
            bound_epoch_id=bound_epoch_id,
        )
        ptr.content_hash = ptr.compute_content_hash()
        self._pointers[pointer_id] = ptr
        return ptr

    def request_activation(
        self,
        *,
        pointer_id: str,
    ) -> ActiveReleasePointer:
        """请求 activation：FROZEN → ACTIVATION_REQUESTED。"""
        ptr = self._pointers.get(pointer_id)
        if ptr is None:
            raise ActiveReleasePointerError(
                EC.REQUIRED_FIELD_MISSING,
                f"pointer {pointer_id} not found",
            )
        if ptr.state != "FROZEN":
            raise ActiveReleasePointerError(
                EC.OP_RELEASE_STATE_INVALID,
                f"pointer {pointer_id} state {ptr.state}, "
                f"cannot request activation",
            )
        ptr.state = "ACTIVATION_REQUESTED"
        ptr.content_hash = ptr.compute_content_hash()
        return ptr

    def gate_activation(
        self,
        *,
        pointer_id: str,
        human_gate_ref: str,
    ) -> ActiveReleasePointer:
        """经过 HumanGate：ACTIVATION_REQUESTED → GATED。

        需要 HumanGate 签名引用。
        """
        if not human_gate_ref:
            raise ActiveReleasePointerError(
                EC.OP_ACTIVE_RELEASE_NOT_GATED,
                f"pointer {pointer_id} activation requires HumanGate",
            )
        ptr = self._pointers.get(pointer_id)
        if ptr is None:
            raise ActiveReleasePointerError(
                EC.REQUIRED_FIELD_MISSING,
                f"pointer {pointer_id} not found",
            )
        if ptr.state != "ACTIVATION_REQUESTED":
            raise ActiveReleasePointerError(
                EC.OP_RELEASE_STATE_INVALID,
                f"pointer {pointer_id} state {ptr.state}, "
                f"cannot gate",
            )
        ptr.state = "GATED"
        ptr.human_gate_ref = human_gate_ref
        ptr.content_hash = ptr.compute_content_hash()
        return ptr

    def activate(self, pointer_id: str) -> ActiveReleasePointer:
        """激活：GATED → ACTIVATED。

        前置条件：必须经过 HumanGate（state=GATED）。
        """
        ptr = self._pointers.get(pointer_id)
        if ptr is None:
            raise ActiveReleasePointerError(
                EC.REQUIRED_FIELD_MISSING,
                f"pointer {pointer_id} not found",
            )
        if ptr.state != "GATED":
            raise ActiveReleasePointerError(
                EC.OP_ACTIVE_RELEASE_NOT_GATED,
                f"pointer {pointer_id} state {ptr.state}, "
                f"must be GATED before activation",
            )
        ptr.state = "ACTIVATED"
        ptr.content_hash = ptr.compute_content_hash()
        self._active_pointer_id = pointer_id
        return ptr

    def reject(self, pointer_id: str) -> ActiveReleasePointer:
        """拒绝：ACTIVATION_REQUESTED → REJECTED。"""
        ptr = self._pointers.get(pointer_id)
        if ptr is None:
            raise ActiveReleasePointerError(
                EC.REQUIRED_FIELD_MISSING,
                f"pointer {pointer_id} not found",
            )
        if ptr.state != "ACTIVATION_REQUESTED":
            raise ActiveReleasePointerError(
                EC.OP_RELEASE_STATE_INVALID,
                f"pointer {pointer_id} state {ptr.state}, "
                f"cannot reject",
            )
        ptr.state = "REJECTED"
        ptr.content_hash = ptr.compute_content_hash()
        return ptr

    def verify_no_mid_epoch_version_change(
        self,
        *,
        epoch_id: str,
    ) -> list[tuple[EC, str]]:
        """验证 mid-Epoch 无版本变更。

        检查：绑定到该 epoch 的 activated pointer 在 epoch 期间未被替换。
        """
        errors: list[tuple[EC, str]] = []
        activated_for_epoch = [
            p for p in self._pointers.values()
            if p.bound_epoch_id == epoch_id and p.state == "ACTIVATED"
        ]
        if len(activated_for_epoch) > 1:
            errors.append((
                EC.OP_MID_EPOCH_VERSION_CHANGE,
                f"epoch {epoch_id} has {len(activated_for_epoch)} "
                f"activated pointers (mid-epoch version change)",
            ))
        return errors

    def verify_activation_gated(self) -> list[tuple[EC, str]]:
        """验证所有 activated pointer 都经过 HumanGate。"""
        errors: list[tuple[EC, str]] = []
        for ptr in self._pointers.values():
            if ptr.state == "ACTIVATED" and not ptr.human_gate_ref:
                errors.append((
                    EC.OP_ACTIVE_RELEASE_NOT_GATED,
                    f"pointer {ptr.pointer_id} activated without "
                    f"HumanGate",
                ))
        return errors

    def verify_states(self) -> list[tuple[EC, str]]:
        """验证所有 pointer 状态合法。"""
        errors: list[tuple[EC, str]] = []
        for ptr in self._pointers.values():
            if ptr.state not in OP_RELEASE_STATES:
                errors.append((
                    EC.OP_RELEASE_STATE_INVALID,
                    f"pointer {ptr.pointer_id} state {ptr.state!r} "
                    f"invalid",
                ))
        return errors

    def verify_hashes(self) -> list[tuple[EC, str]]:
        """验证所有 pointer hash 有效。"""
        errors: list[tuple[EC, str]] = []
        for ptr in self._pointers.values():
            if not ptr.is_hash_valid:
                errors.append((
                    EC.OP_RELEASE_POINTER_HASH_MISMATCH,
                    f"pointer {ptr.pointer_id} content_hash invalid",
                ))
        return errors
