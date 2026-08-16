"""Deterministic fixtures and graders for Devin AGENTS.md visibility POCs.

This module never launches Devin.  It creates exact-size ASCII rule files and
grades a sealed ATIF export by comparing the original rule bytes with system
messages.  Model recall is secondary; exact effective-message inclusion is the
primary physical endpoint.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
from typing import Any, Iterable

from .role_runtime import inspect_export, sha256_file


AGENTS_LIMIT_SCHEMA_VERSION = "solve-vein/agents-limit-fixture/v1"
AGENTS_VISIBILITY_REPORT_SCHEMA_VERSION = "solve-vein/agents-visibility-report/v1"

CELL_SIZES: dict[str, int] = {
    "A16M1": 16_383,
    "A16": 16_384,
    "A16P1": 16_385,
    "A32": 32_768,
    "A64": 65_536,
    "A128": 131_072,
    "A256": 262_144,
}

_SENTINEL_PATTERN = re.compile(
    rb"^AGENTS_SENTINEL_([A-Z0-9]+)_([0-9]+)=([0-9a-f]{32})$",
    re.MULTILINE,
)


class AgentsLimitError(ValueError):
    """Fail-closed deterministic fixture or grading error."""


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _sentinel_value(cell_id: str, offset: int) -> str:
    return hashlib.sha256(
        f"POC-VMS-39:{cell_id}:{offset}:agents-visibility".encode("ascii")
    ).hexdigest()[:32]


def sentinel_offsets(size_bytes: int) -> tuple[int, ...]:
    """Return non-overlapping line starts that probe the 16 KiB boundary."""

    if size_bytes < 2_048:
        raise AgentsLimitError("fixture must be at least 2048 bytes")
    candidates = [512, 8_192, 15_872, 16_896, size_bytes // 2, size_bytes - 256]
    accepted: list[int] = []
    for offset in sorted(set(candidates)):
        if offset <= 256 or offset + 100 >= size_bytes:
            continue
        if accepted and offset - accepted[-1] < 128:
            continue
        accepted.append(offset)
    if len(accepted) < 3:
        raise AgentsLimitError("fixture has too few usable sentinel offsets")
    return tuple(accepted)


def generate_agents_fixture(cell_id: str) -> bytes:
    """Generate one exact-size, deterministic, ASCII-only AGENTS.md."""

    if cell_id not in CELL_SIZES:
        raise AgentsLimitError(f"unknown cell: {cell_id}")
    size_bytes = CELL_SIZES[cell_id]
    payload = bytearray(b"." * size_bytes)
    for index in range(79, size_bytes, 80):
        payload[index] = 0x0A
    header = (
        "# POC-VMS-39 isolated rule-visibility canary\n"
        "This workspace contains no repository, problem, solution, Tell, or Hint data.\n"
        "When TASK.md asks for the loaded canary values, use only rules already present "
        "in your context. Do not open, read, grep, list, or execute AGENTS.md.\n"
        "Write only agents-visibility-report.json and DONE.md inside this workspace.\n"
    ).encode("ascii")
    if len(header) >= 500:
        raise AssertionError("fixture header unexpectedly overlaps first sentinel")
    payload[: len(header)] = header
    for offset in sentinel_offsets(size_bytes):
        line = (
            f"AGENTS_SENTINEL_{cell_id}_{offset}="
            f"{_sentinel_value(cell_id, offset)}\n"
        ).encode("ascii")
        if offset + len(line) >= size_bytes:
            raise AssertionError("sentinel does not fit")
        payload[offset - 1] = 0x0A
        payload[offset : offset + len(line)] = line
    payload[-1] = 0x0A
    result = bytes(payload)
    if len(result) != size_bytes or not result.isascii():
        raise AssertionError("fixture size or encoding invariant failed")
    parsed = parse_sentinels(result)
    if len(parsed) != len(sentinel_offsets(size_bytes)):
        raise AssertionError("sentinel parse invariant failed")
    return result


def parse_sentinels(payload: bytes) -> tuple[dict[str, Any], ...]:
    rows: list[dict[str, Any]] = []
    for match in _SENTINEL_PATTERN.finditer(payload):
        cell_id = match.group(1).decode("ascii")
        declared_offset = int(match.group(2))
        actual_offset = match.start()
        value = match.group(3).decode("ascii")
        if declared_offset != actual_offset:
            raise AgentsLimitError(
                f"sentinel offset mismatch: declared={declared_offset}, actual={actual_offset}"
            )
        if value != _sentinel_value(cell_id, actual_offset):
            raise AgentsLimitError("sentinel value does not match deterministic contract")
        rows.append(
            {
                "cell_id": cell_id,
                "offset": actual_offset,
                "name": f"AGENTS_SENTINEL_{cell_id}_{actual_offset}",
                "value": value,
            }
        )
    return tuple(rows)


def fixture_manifest(cell_ids: Iterable[str] | None = None) -> dict[str, Any]:
    selected = tuple(cell_ids) if cell_ids is not None else tuple(CELL_SIZES)
    rows: list[dict[str, Any]] = []
    for cell_id in selected:
        payload = generate_agents_fixture(cell_id)
        rows.append(
            {
                "cell_id": cell_id,
                "exact_bytes": len(payload),
                "sha256": _sha256_bytes(payload),
                "sentinels": list(parse_sentinels(payload)),
            }
        )
    return {
        "schema_version": AGENTS_LIMIT_SCHEMA_VERSION,
        "poc_id": "POC-VMS-39",
        "encoding": "ASCII",
        "newline": "LF",
        "cells": rows,
    }


def write_fixture_exclusive(cell_id: str, destination: Path) -> dict[str, Any]:
    if destination.exists() or destination.is_symlink():
        raise AgentsLimitError(f"destination already exists: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    payload = generate_agents_fixture(cell_id)
    destination.write_bytes(payload)
    destination.chmod(0o600)
    return {
        "cell_id": cell_id,
        "path": str(destination),
        "exact_bytes": len(payload),
        "sha256": sha256_file(destination),
        "sentinels": list(parse_sentinels(payload)),
    }


def _load_atif(export_path: Path) -> tuple[dict[str, Any], list[str]]:
    if not export_path.is_file() or export_path.is_symlink():
        raise AgentsLimitError(f"export must be a regular file: {export_path}")
    try:
        value = json.loads(export_path.read_text())
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise AgentsLimitError(f"export is not valid JSON: {exc}") from exc
    if not isinstance(value, dict) or not isinstance(value.get("steps"), list):
        raise AgentsLimitError("export is not an ATIF object with steps")
    messages = [
        step["message"]
        for step in value["steps"]
        if isinstance(step, dict)
        and step.get("source") == "system"
        and isinstance(step.get("message"), str)
    ]
    if not messages:
        raise AgentsLimitError("export has no observable system messages")
    return value, messages


def _max_prefix_match(payload: bytes, messages: list[bytes]) -> int:
    anchor_length = min(128, len(payload))
    anchor = payload[:anchor_length]
    best = 0
    for message in messages:
        start = message.find(anchor)
        if start < 0:
            continue
        limit = min(len(payload), len(message) - start)
        matched = 0
        while matched < limit and message[start + matched] == payload[matched]:
            matched += 1
        best = max(best, matched)
    return best


def _max_suffix_match(payload: bytes, messages: list[bytes]) -> int:
    anchor_length = min(128, len(payload))
    anchor = payload[-anchor_length:]
    best = 0
    for message in messages:
        end = message.rfind(anchor)
        if end < 0:
            continue
        payload_index = len(payload) - anchor_length - 1
        message_index = end - 1
        matched = anchor_length
        while (
            payload_index >= 0
            and message_index >= 0
            and message[message_index] == payload[payload_index]
        ):
            matched += 1
            payload_index -= 1
            message_index -= 1
        best = max(best, matched)
    return best


def _full_consecutive_message_span(
    payload: bytes, messages: list[bytes]
) -> tuple[int, int] | None:
    """Return an inclusive consecutive-message span containing the payload.

    This endpoint is deliberately secondary to a single-message exact hit.  It
    exists so a deterministic loader split across adjacent system messages is
    not mislabeled as truncation.
    """

    for start in range(len(messages)):
        combined = bytearray()
        for end in range(start, len(messages)):
            combined.extend(messages[end])
            if end > start and payload in combined:
                return (start, end)
    return None


def _grade_model_report(
    expected_sentinels: tuple[dict[str, Any], ...], output_path: Path | None
) -> dict[str, Any]:
    if output_path is None or not output_path.is_file() or output_path.is_symlink():
        return {
            "status": "NOT_OBSERVED",
            "expected_count": len(expected_sentinels),
            "reported_count": 0,
            "matched_count": 0,
            "hallucinated_count": 0,
        }
    try:
        value = json.loads(output_path.read_text())
    except (UnicodeDecodeError, json.JSONDecodeError):
        return {
            "status": "INVALID_JSON",
            "expected_count": len(expected_sentinels),
            "reported_count": 0,
            "matched_count": 0,
            "hallucinated_count": 0,
        }
    reported = value.get("sentinels") if isinstance(value, dict) else None
    if not isinstance(reported, list):
        return {
            "status": "INVALID_SCHEMA",
            "expected_count": len(expected_sentinels),
            "reported_count": 0,
            "matched_count": 0,
            "hallucinated_count": 0,
        }
    expected_pairs = {(row["name"], row["value"]) for row in expected_sentinels}
    reported_pairs = {
        (row.get("name"), row.get("value"))
        for row in reported
        if isinstance(row, dict)
        and isinstance(row.get("name"), str)
        and isinstance(row.get("value"), str)
    }
    matched = expected_pairs & reported_pairs
    hallucinated = reported_pairs - expected_pairs
    return {
        "status": "VALID",
        "expected_count": len(expected_pairs),
        "reported_count": len(reported_pairs),
        "matched_count": len(matched),
        "hallucinated_count": len(hallucinated),
        "recall": len(matched) / len(expected_pairs) if expected_pairs else 1.0,
        "precision": (
            len(matched) / len(reported_pairs) if reported_pairs else 0.0
        ),
    }


def grade_agents_visibility(
    agents_path: Path, export_path: Path, output_path: Path | None = None
) -> dict[str, Any]:
    """Grade exact effective-message inclusion and secondary model recall."""

    if not agents_path.is_file() or agents_path.is_symlink():
        raise AgentsLimitError(f"AGENTS must be a regular file: {agents_path}")
    payload = agents_path.read_bytes()
    if not payload.isascii():
        raise AgentsLimitError("AGENTS fixture must remain ASCII")
    sentinels = parse_sentinels(payload)
    if not sentinels:
        raise AgentsLimitError("AGENTS fixture contains no sentinels")
    _, system_messages = _load_atif(export_path)
    system_bytes = [message.encode("utf-8") for message in system_messages]
    full_message_indexes = [
        index for index, message in enumerate(system_bytes) if payload in message
    ]
    multi_message_span = (
        None
        if full_message_indexes
        else _full_consecutive_message_span(payload, system_bytes)
    )
    fully_observed = bool(full_message_indexes or multi_message_span)
    prefix_bytes = (
        len(payload) if fully_observed else _max_prefix_match(payload, system_bytes)
    )
    suffix_bytes = (
        len(payload) if fully_observed else _max_suffix_match(payload, system_bytes)
    )
    sentinel_rows: list[dict[str, Any]] = []
    for row in sentinels:
        line = f"{row['name']}={row['value']}".encode("ascii")
        hits = [index for index, message in enumerate(system_bytes) if line in message]
        sentinel_rows.append({**row, "system_message_indexes": hits, "observed": bool(hits)})
    if full_message_indexes:
        primary_status = "FULL_EXACT_SINGLE_MESSAGE"
    elif multi_message_span:
        primary_status = "FULL_EXACT_MULTI_MESSAGE"
    elif prefix_bytes >= 128:
        primary_status = f"PREFIX_TRUNCATED_AT_{prefix_bytes}"
    elif suffix_bytes >= 128:
        primary_status = f"SUFFIX_ONLY_FROM_{len(payload) - suffix_bytes}"
    elif any(row["observed"] for row in sentinel_rows):
        primary_status = "TRANSFORMED_OR_PARTIAL"
    else:
        primary_status = "ABSENT"
    export_observation = inspect_export(export_path)
    return {
        "schema_version": AGENTS_VISIBILITY_REPORT_SCHEMA_VERSION,
        "poc_id": "POC-VMS-39",
        "agents_sha256": sha256_file(agents_path),
        "agents_exact_bytes": len(payload),
        "export_sha256": sha256_file(export_path),
        "system_message_count": len(system_messages),
        "system_message_utf8_bytes": [len(value) for value in system_bytes],
        "primary_status": primary_status,
        "full_exact_system_message_indexes": full_message_indexes,
        "full_exact_multi_message_span": (
            list(multi_message_span) if multi_message_span else None
        ),
        "longest_exact_prefix_bytes": prefix_bytes,
        "longest_exact_suffix_bytes": suffix_bytes,
        "sentinels": sentinel_rows,
        "model_report": _grade_model_report(sentinels, output_path),
        "export_observation": export_observation,
    }
