"""Content-addressed implementation receipts for solve-side analysis runs."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any, Iterable


PACKAGE_ROOT = Path(__file__).resolve().parent
REPOSITORY_ROOT = PACKAGE_ROOT.parents[1]
IMPLEMENTATION_SUFFIXES = frozenset({".py", ".ref", ".ai-check"})


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def implementation_tree_receipt(
    *,
    extra_files: Iterable[Path] = (),
) -> dict[str, Any]:
    """Hash the complete top-level package implementation plus explicit callers.

    Runtime outputs, caches, fixtures, and docs are intentionally separate artifact
    classes.  Every extra file must be inside the repository root and is sorted into
    the same canonical receipt as package files.
    """

    files = {
        path.resolve(strict=True)
        for path in PACKAGE_ROOT.iterdir()
        if path.is_file() and path.suffix in IMPLEMENTATION_SUFFIXES
    }
    for extra_file in extra_files:
        resolved = extra_file.resolve(strict=True)
        if not resolved.is_file() or not resolved.is_relative_to(REPOSITORY_ROOT):
            raise ValueError(f"implementation receipt file is outside the repo: {resolved}")
        files.add(resolved)
    ordered = sorted(files, key=lambda path: str(path.relative_to(REPOSITORY_ROOT)))
    entries = [
        {
            "path": str(path.relative_to(REPOSITORY_ROOT)),
            "sha256": sha256_file(path),
        }
        for path in ordered
    ]
    aggregate_bytes = "".join(
        f"{entry['sha256']}  {entry['path']}\n" for entry in entries
    ).encode("utf-8")
    return {
        "schema_version": "solve-vein/implementation-tree-receipt/v1",
        "files": entries,
        "aggregate_sha256": hashlib.sha256(aggregate_bytes).hexdigest(),
    }
