"""Verify immutable evidence after current-tree path and source evolution.

Frozen manifests keep their original repo-relative path identity.  A current
reconstruction may move the same bytes or evolve a source file, so validation
first checks the canonical current location and then the exact blob at a pinned
pre-reconstruction commit.  Neither path identity nor frozen bytes are rewritten.
"""

from __future__ import annotations

import hashlib
from pathlib import Path, PurePosixPath
import re
import subprocess
from typing import Callable


HISTORICAL_SOURCE_COMMIT = "3b2668404ce42a3bd6eacd76f0ed1a5cfe880769"
CURRENT_WORKTREE = "CURRENT_WORKTREE"
PINNED_GIT_COMMIT = "PINNED_GIT_COMMIT"
HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
PATH_REPLACEMENTS = (
    ("第六代系统提示词积累目录/", "prompts/absorb/"),
    ("第六代系统研发过程文档/", "docs/history/sixth-generation/rnd/"),
    ("第六代系统技术说明书/", "docs/history/sixth-generation/legacy-spec/"),
    ("Tell分类学研究过程文档/", "evidence/history/tell-research/"),
)

GitBlobReader = Callable[[str], bytes]


class HistoricalBindingError(RuntimeError):
    """A historical identity cannot be verified without weakening integrity."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


def reconstructed_current_path(historical_path: str) -> str:
    """Map a retired active-root identity to its canonical current location."""

    relative = _canonical_relative_path(historical_path, "historical_path")
    for old_prefix, current_prefix in PATH_REPLACEMENTS:
        if relative.startswith(old_prefix):
            return current_prefix + relative[len(old_prefix) :]
    return relative


def read_historical_git_blob(
    repository_root: Path,
    historical_path: str,
    *,
    historical_commit: str = HISTORICAL_SOURCE_COMMIT,
) -> bytes:
    """Read one exact historical blob without checking out or mutating Git state."""

    relative = _canonical_relative_path(historical_path, "historical_path")
    if not HEX40.fullmatch(historical_commit):
        raise HistoricalBindingError(
            "HISTORICAL_COMMIT_INVALID", repr(historical_commit)
        )
    try:
        result = subprocess.run(
            ["git", "show", f"{historical_commit}:{relative}"],
            cwd=repository_root,
            capture_output=True,
            check=False,
            timeout=10,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise HistoricalBindingError(
            "HISTORICAL_GIT_UNAVAILABLE", relative
        ) from exc
    if result.returncode != 0:
        raise HistoricalBindingError("HISTORICAL_GIT_BLOB_ABSENT", relative)
    return result.stdout


def list_historical_git_files(
    repository_root: Path,
    roots: tuple[str, ...],
    *,
    historical_commit: str = HISTORICAL_SOURCE_COMMIT,
) -> tuple[str, ...]:
    """List files below exact historical roots without consulting current paths."""

    if not roots:
        raise HistoricalBindingError("HISTORICAL_ROOTS_INVALID", "empty")
    canonical_roots = tuple(
        _canonical_relative_path(root.rstrip("/"), "historical_root") for root in roots
    )
    if not HEX40.fullmatch(historical_commit):
        raise HistoricalBindingError(
            "HISTORICAL_COMMIT_INVALID", repr(historical_commit)
        )
    try:
        result = subprocess.run(
            [
                "git",
                "ls-tree",
                "-r",
                "--name-only",
                "-z",
                historical_commit,
                "--",
                *canonical_roots,
            ],
            cwd=repository_root,
            capture_output=True,
            check=False,
            timeout=10,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise HistoricalBindingError(
            "HISTORICAL_GIT_UNAVAILABLE", repr(canonical_roots)
        ) from exc
    if result.returncode != 0:
        raise HistoricalBindingError(
            "HISTORICAL_GIT_TREE_UNAVAILABLE", repr(canonical_roots)
        )
    try:
        decoded = result.stdout.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise HistoricalBindingError(
            "HISTORICAL_GIT_TREE_INVALID", repr(canonical_roots)
        ) from exc
    paths = tuple(
        _canonical_relative_path(path, "historical_tree_member")
        for path in decoded.rstrip("\0").split("\0")
        if path
    )
    if not paths:
        raise HistoricalBindingError(
            "HISTORICAL_GIT_TREE_EMPTY", repr(canonical_roots)
        )
    if any(
        not any(path == root or path.startswith(f"{root}/") for root in canonical_roots)
        for path in paths
    ):
        raise HistoricalBindingError(
            "HISTORICAL_GIT_TREE_ESCAPED", repr(canonical_roots)
        )
    return tuple(sorted(set(paths)))


def validate_current_or_historical_binding(
    repository_root: Path,
    historical_path: str,
    expected_sha256: str,
    *,
    expected_size: int | None = None,
    current_path: str | None = None,
    historical_commit: str = HISTORICAL_SOURCE_COMMIT,
    git_blob_reader: GitBlobReader | None = None,
) -> str:
    """Verify current equivalent bytes or the immutable historical Git blob.

    The return value states which evidence source matched.  Current drift is not
    accepted as frozen evidence; it only causes validation to fall back to the
    pinned historical blob.
    """

    historical_relative = _canonical_relative_path(
        historical_path, "historical_path"
    )
    current_relative = _canonical_relative_path(
        current_path or reconstructed_current_path(historical_relative),
        "current_path",
    )
    if not isinstance(expected_sha256, str) or not HEX64.fullmatch(expected_sha256):
        raise HistoricalBindingError(
            "EXPECTED_SHA256_INVALID", repr(expected_sha256)
        )
    if expected_size is not None and (
        isinstance(expected_size, bool)
        or not isinstance(expected_size, int)
        or expected_size < 0
    ):
        raise HistoricalBindingError("EXPECTED_SIZE_INVALID", repr(expected_size))

    current = repository_root / Path(current_relative)
    if current.is_symlink():
        raise HistoricalBindingError("CURRENT_PATH_SYMLINK", current_relative)
    if current.exists() and not current.is_file():
        raise HistoricalBindingError("CURRENT_PATH_NOT_FILE", current_relative)
    if current.is_file():
        try:
            payload = current.read_bytes()
        except OSError as exc:
            raise HistoricalBindingError(
                "CURRENT_PATH_UNREADABLE", current_relative
            ) from exc
        if _payload_matches(payload, expected_sha256, expected_size):
            return CURRENT_WORKTREE

    if git_blob_reader is None:
        historical = read_historical_git_blob(
            repository_root,
            historical_relative,
            historical_commit=historical_commit,
        )
    else:
        try:
            historical = git_blob_reader(historical_relative)
        except HistoricalBindingError:
            raise
        except Exception as exc:
            raise HistoricalBindingError(
                "HISTORICAL_GIT_UNAVAILABLE", historical_relative
            ) from exc
        if not isinstance(historical, bytes):
            raise HistoricalBindingError(
                "HISTORICAL_GIT_PAYLOAD_INVALID", historical_relative
            )

    if hashlib.sha256(historical).hexdigest() != expected_sha256:
        raise HistoricalBindingError(
            "HISTORICAL_GIT_HASH_DRIFT", historical_relative
        )
    if expected_size is not None and len(historical) != expected_size:
        raise HistoricalBindingError(
            "HISTORICAL_GIT_SIZE_DRIFT", historical_relative
        )
    return PINNED_GIT_COMMIT


def _canonical_relative_path(value: object, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise HistoricalBindingError("PATH_INVALID", f"{label}: {value!r}")
    try:
        path = PurePosixPath(value)
    except (TypeError, ValueError) as exc:
        raise HistoricalBindingError("PATH_INVALID", f"{label}: {value!r}") from exc
    if (
        path.is_absolute()
        or ".." in path.parts
        or "." in path.parts
        or path.as_posix() != value
    ):
        raise HistoricalBindingError("PATH_INVALID", f"{label}: {value!r}")
    return value


def _payload_matches(
    payload: bytes,
    expected_sha256: str,
    expected_size: int | None,
) -> bool:
    return (
        (expected_size is None or len(payload) == expected_size)
        and hashlib.sha256(payload).hexdigest() == expected_sha256
    )
