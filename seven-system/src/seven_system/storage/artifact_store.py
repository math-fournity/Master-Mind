"""最小 CompletionArtifactStore — GV0 建立的 D 盘 content-addressed append-once store。

复用 v0.1 storage.py 的 append-once 原语，硬化为：
- content-addressed（sha256 寻址）
- append-once（拒绝覆盖不同内容）
- hash/byte 校验（读取时重算 hash）
- 祖先/叶 symlink 拒绝
- repo/Home/`/tmp` fallback 拒绝
- D 盘 volume_root 强制

WP-VLT0 随后复用并扩展同一 CAS 核心，禁止另造第二套 bundle store。
本 store 不接收模型/Solver 输出、答案或 holdout，
也不能签 CAS/Vault 正式 CapabilityReport。
"""

from __future__ import annotations

import hashlib
import os
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ..hashing import canonical_json_bytes, file_sha256
from ..contracts.errors import VerificationErrorCode as EC


# 拒绝的 fallback 路径前缀
_FORBIDDEN_FALLBACK_PREFIXES: tuple[str, ...] = (
    str(Path.home()),
    "/tmp",
    "/var/tmp",
    "/private/tmp",
)


@dataclass(frozen=True)
class ArtifactRef:
    """content-addressed artifact 引用。"""

    ref: str  # 相对于 store root 的路径
    sha256: str
    size_bytes: int

    def to_dict(self) -> dict[str, str | int]:
        return {
            "ref": self.ref,
            "sha256": self.sha256,
            "size_bytes": self.size_bytes,
        }


class CompletionArtifactStore:
    """最小 D 盘 content-addressed append-once store。

    用法：
        store = CompletionArtifactStore(
            root=Path("/data/seven-system-data/completion-bundles"),
            volume_root=Path("/data"),
        )
        ref = store.put_json({"schema_id": "seven/implementation-completion-bundle", ...})
        obj = store.get(ref.sha256)
    """

    def __init__(
        self,
        *,
        root: Path,
        volume_root: Path,
        test_only_allow_non_d_volume: bool = False,
    ) -> None:
        self._volume_root = self._validate_volume_root(
            volume_root,
            test_only_allow_non_d_volume=test_only_allow_non_d_volume,
        )
        self._root = self._validate_root(root, self._volume_root)

    @property
    def root(self) -> Path:
        return self._root

    @property
    def volume_root(self) -> Path:
        return self._volume_root

    @staticmethod
    def _validate_volume_root(
        volume_root: Path,
        *,
        test_only_allow_non_d_volume: bool = False,
    ) -> Path:
        """验证 volume_root 不是 symlink、不是 fallback 路径。"""
        absolute = volume_root.absolute()
        if absolute.is_symlink():
            raise _StoreError(
                EC.STORE_SYMLINK_REJECTED,
                f"volume_root is a symlink: {absolute}",
            )
        resolved = absolute.resolve()
        if not resolved.exists():
            raise _StoreError(
                EC.STORE_VOLUME_ROOT_INVALID,
                f"volume_root does not exist: {resolved}",
            )
        if not resolved.is_dir():
            raise _StoreError(
                EC.STORE_VOLUME_ROOT_INVALID,
                f"volume_root is not a directory: {resolved}",
            )

        # 生产 store 的批准物理卷固定为 /data。测试必须显式选择
        # test_only_allow_non_d_volume；该开关不得由任何CLI/API暴露。
        approved_d_root = Path("/data").resolve()
        if not test_only_allow_non_d_volume and resolved != approved_d_root:
            raise _StoreError(
                EC.STORE_FALLBACK_REJECTED,
                f"production volume_root must be {approved_d_root}, got {resolved}",
            )

        if not test_only_allow_non_d_volume:
            for prefix in _FORBIDDEN_FALLBACK_PREFIXES:
                if str(resolved).startswith(prefix):
                    raise _StoreError(
                        EC.STORE_FALLBACK_REJECTED,
                        f"production volume_root uses forbidden fallback prefix {prefix}: {resolved}",
                    )
        return resolved

    @staticmethod
    def _validate_root(root: Path, volume_root: Path) -> Path:
        """验证 root 在 volume_root 下、不是 symlink。"""
        absolute = root.absolute()
        if absolute.is_symlink():
            raise _StoreError(
                EC.STORE_SYMLINK_REJECTED,
                f"store root is a symlink: {absolute}",
            )
        resolved = absolute.resolve()
        vol_resolved = volume_root.resolve()
        try:
            resolved.relative_to(vol_resolved)
        except ValueError as exc:
            raise _StoreError(
                EC.STORE_FALLBACK_REJECTED,
                f"store root {resolved} is not under volume_root {vol_resolved}",
            ) from exc
        # 检查路径上每个祖先都不是 symlink
        current = resolved
        while current != vol_resolved:
            if current.is_symlink():
                raise _StoreError(
                    EC.STORE_SYMLINK_REJECTED,
                    f"symlink ancestor: {current}",
                )
            parent = current.parent
            if parent == current:
                break
            current = parent
        resolved.mkdir(parents=True, exist_ok=True)
        return resolved

    def _content_path(self, sha256: str) -> Path:
        """content-addressed 路径: <root>/<前2字符>/<完整hash>.json"""
        if not sha256 or len(sha256) != 64:
            raise _StoreError(
                EC.STORE_HASH_MISMATCH,
                f"invalid sha256: {sha256}",
            )
        return self._root / sha256[:2] / f"{sha256}.json"

    def put_json(self, payload: Any) -> ArtifactRef:
        """以 content-addressed 方式 append-once 写入 JSON 对象。

        返回 ArtifactRef。相同内容幂等返回已有引用。
        不同内容写入相同 hash 路径时拒绝（EC.STORE_OVERWRITE_CONFLICT）。
        """
        content = canonical_json_bytes(payload) + b"\n"
        digest = hashlib.sha256(content).hexdigest()
        path = self._content_path(digest)

        # 检查 symlink（叶和祖先）
        self._check_no_symlink(path)

        path.parent.mkdir(parents=True, exist_ok=True)

        if path.exists():
            if path.is_symlink():
                raise _StoreError(
                    EC.STORE_SYMLINK_REJECTED,
                    f"existing artifact is a symlink: {path}",
                )
            existing = path.read_bytes()
            if existing == content:
                return ArtifactRef(
                    ref=str(path.relative_to(self._root)),
                    sha256=digest,
                    size_bytes=len(content),
                )
            raise _StoreError(
                EC.STORE_OVERWRITE_CONFLICT,
                f"hash collision or content conflict at {path}: "
                f"existing {len(existing)}B vs new {len(content)}B",
            )

        # 原子写入：temp file + fsync + hard link
        fd, temp_name = tempfile.mkstemp(
            prefix=f".{digest[:16]}.", suffix=".partial", dir=path.parent
        )
        temp_path = Path(temp_name)
        try:
            with os.fdopen(fd, "wb") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
            try:
                os.link(temp_path, path)
            except FileExistsError:
                if path.is_symlink():
                    raise _StoreError(
                        EC.STORE_SYMLINK_REJECTED,
                        f"concurrent symlink at {path}",
                    )
                existing = path.read_bytes()
                if existing == content:
                    return ArtifactRef(
                        ref=str(path.relative_to(self._root)),
                        sha256=digest,
                        size_bytes=len(content),
                    )
                raise _StoreError(
                    EC.STORE_OVERWRITE_CONFLICT,
                    f"concurrent content conflict at {path}",
                )
            # fsync 目录
            dir_fd = os.open(path.parent, os.O_RDONLY)
            try:
                os.fsync(dir_fd)
            finally:
                os.close(dir_fd)
        finally:
            temp_path.unlink(missing_ok=True)

        return ArtifactRef(
            ref=str(path.relative_to(self._root)),
            sha256=digest,
            size_bytes=len(content),
        )

    def put_bytes(self, content: bytes) -> ArtifactRef:
        """以 content-addressed 方式 append-once 写入原始 bytes。"""
        digest = hashlib.sha256(content).hexdigest()
        path = self._content_path(digest)
        self._check_no_symlink(path)
        path.parent.mkdir(parents=True, exist_ok=True)

        if path.exists():
            if path.is_symlink():
                raise _StoreError(EC.STORE_SYMLINK_REJECTED, f"symlink: {path}")
            if path.read_bytes() == content:
                return ArtifactRef(
                    ref=str(path.relative_to(self._root)),
                    sha256=digest,
                    size_bytes=len(content),
                )
            raise _StoreError(EC.STORE_OVERWRITE_CONFLICT, f"conflict at {path}")

        fd, temp_name = tempfile.mkstemp(
            prefix=f".{digest[:16]}.", suffix=".partial", dir=path.parent
        )
        temp_path = Path(temp_name)
        try:
            with os.fdopen(fd, "wb") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
            try:
                os.link(temp_path, path)
            except FileExistsError:
                if path.read_bytes() == content:
                    return ArtifactRef(
                        ref=str(path.relative_to(self._root)),
                        sha256=digest,
                        size_bytes=len(content),
                    )
                raise _StoreError(EC.STORE_OVERWRITE_CONFLICT, f"concurrent conflict at {path}")
            dir_fd = os.open(path.parent, os.O_RDONLY)
            try:
                os.fsync(dir_fd)
            finally:
                os.close(dir_fd)
        finally:
            temp_path.unlink(missing_ok=True)

        return ArtifactRef(
            ref=str(path.relative_to(self._root)),
            sha256=digest,
            size_bytes=len(content),
        )

    def get(self, sha256: str) -> bytes:
        """读取并验证 content-addressed artifact。"""
        path = self._content_path(sha256)
        self._check_no_symlink(path)
        if not path.exists():
            raise _StoreError(EC.STORE_HASH_MISMATCH, f"artifact not found: {sha256}")
        content = path.read_bytes()
        actual_hash = hashlib.sha256(content).hexdigest()
        if actual_hash != sha256:
            raise _StoreError(
                EC.STORE_HASH_MISMATCH,
                f"hash mismatch: expected {sha256}, got {actual_hash}",
            )
        return content

    def get_json(self, sha256: str) -> Any:
        """读取并验证 JSON artifact。"""
        import json

        content = self.get(sha256)
        return json.loads(content)

    def verify(self, sha256: str) -> bool:
        """验证 artifact 存在且 hash 匹配。不抛异常。"""
        try:
            self.get(sha256)
            return True
        except _StoreError:
            return False

    def exists(self, sha256: str) -> bool:
        """检查 artifact 是否存在。"""
        path = self._content_path(sha256)
        return path.exists() and not path.is_symlink()

    def _check_no_symlink(self, path: Path) -> None:
        """检查路径本身和所有祖先（在 store root 下）不是 symlink。"""
        absolute = path.absolute()
        if absolute.is_symlink():
            raise _StoreError(
                EC.STORE_SYMLINK_REJECTED,
                f"leaf is a symlink: {absolute}",
            )
        current = absolute.parent
        while current != self._root:
            if current.is_symlink():
                raise _StoreError(
                    EC.STORE_SYMLINK_REJECTED,
                    f"ancestor symlink: {current}",
                )
            parent = current.parent
            if parent == current:
                break
            current = parent
        # 检查 store root 本身
        if self._root.is_symlink():
            raise _StoreError(
                EC.STORE_SYMLINK_REJECTED,
                f"store root is a symlink: {self._root}",
            )


class _StoreError(Exception):
    def __init__(self, code: VerificationErrorCode, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)
