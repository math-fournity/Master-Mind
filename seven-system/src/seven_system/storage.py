"""不可覆盖的本地提交原语。

这里只实现 P0/P1 所需的单文件幂等提交。真实 Artifact bundle 的
live -> partial -> COMMITTED -> final 协议仍属于后续工作包。
"""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path
from typing import Any

from .hashing import canonical_json_bytes


class ContentConflictError(RuntimeError):
    """同一路径已经提交了不同内容。"""


def _bounded_path(path: Path, boundary_root: Path | None) -> Path:
    lexical = path.absolute()
    if lexical.is_symlink():
        raise ContentConflictError(f"refuse symlink destination: {lexical}")
    if boundary_root is None:
        return lexical

    root = boundary_root.absolute()
    if root.is_symlink():
        raise ContentConflictError(f"refuse symlink boundary: {root}")
    try:
        lexical.relative_to(root)
    except ValueError as exc:
        raise ContentConflictError(f"destination escapes boundary: {lexical}") from exc

    current = lexical.parent
    while current != root:
        if current.is_symlink():
            raise ContentConflictError(f"refuse symlink ancestor: {current}")
        parent = current.parent
        if parent == current:
            raise ContentConflictError(f"boundary is not an ancestor: {root}")
        current = parent
    resolved = lexical.resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError as exc:
        raise ContentConflictError(f"resolved destination escapes boundary: {resolved}") from exc
    return lexical


def _commit_bytes_once(
    path: Path, content: bytes, *, boundary_root: Path | None = None
) -> str:
    path = _bounded_path(path, boundary_root)
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.exists():
        if path.read_bytes() == content:
            return "ALREADY_COMMITTED"
        raise ContentConflictError(f"refuse to overwrite committed file: {path}")

    fd, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".partial", dir=path.parent
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        try:
            os.link(temporary, path)
        except FileExistsError:
            if path.read_bytes() == content:
                return "ALREADY_COMMITTED"
            raise ContentConflictError(f"concurrent content conflict: {path}")
        directory_fd = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
        return "COMMITTED"
    finally:
        temporary.unlink(missing_ok=True)


def commit_json_once(
    path: Path, payload: Any, *, boundary_root: Path | None = None
) -> str:
    return _commit_bytes_once(
        path, canonical_json_bytes(payload) + b"\n", boundary_root=boundary_root
    )


def commit_text_once(
    path: Path, text: str, *, boundary_root: Path | None = None
) -> str:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    if not normalized.endswith("\n"):
        normalized += "\n"
    return _commit_bytes_once(
        path, normalized.encode("utf-8"), boundary_root=boundary_root
    )


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)
