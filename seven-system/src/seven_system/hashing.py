"""版本化、可重放的对象哈希。"""

from __future__ import annotations

import hashlib
import json
import unicodedata
from pathlib import Path
from typing import Any


HASH_SPEC_VERSION = "seven-hash-v1"


def _normalize(value: Any) -> Any:
    if isinstance(value, str):
        normalized = unicodedata.normalize("NFC", value)
        return normalized.replace("\r\n", "\n").replace("\r", "\n")
    if isinstance(value, list):
        return [_normalize(item) for item in value]
    if isinstance(value, tuple):
        return [_normalize(item) for item in value]
    if isinstance(value, dict):
        return {str(key): _normalize(item) for key, item in value.items()}
    return value


def canonical_json_bytes(payload: Any) -> bytes:
    """返回确定性的 UTF-8 JSON；数组顺序保持不变。"""

    return json.dumps(
        _normalize(payload),
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def object_hash(object_type: str, schema_version: str, payload: Any) -> str:
    prefix = (
        f"{object_type}\0{schema_version}\0{HASH_SPEC_VERSION}\0"
    ).encode("utf-8")
    return hashlib.sha256(prefix + canonical_json_bytes(payload)).hexdigest()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()
