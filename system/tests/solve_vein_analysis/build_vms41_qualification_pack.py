"""Build the read-only authentic-source slice of the POC-VMS-41 pack.

This builder never mutates the high-concurrency Solver roots.  It validates two
frozen ATIF exports, deterministically extracts their agent reasoning paragraph
ranges, and writes new qualification fixtures only when every destination is
absent.  Synthetic cases and hidden acceptable sets are maintained separately.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_ROOT = (
    REPO_ROOT
    / "system"
    / "tests"
    / "solve_vein_analysis"
    / "qualification_fixtures"
    / "vms41"
)
SOURCE_ROOT = Path("/data/math-agent-glm5.2-tmux-agents-trajectory")
BUILDER_SCHEMA_VERSION = "solve-vein/vms41-source-pack-builder/v1"
PARAGRAPH_SPLIT_RE = re.compile(r"\n[ \t]*\n")

SOURCES: tuple[dict[str, Any], ...] = (
    {
        "case_id": "V41-REAL-SPIRAL",
        "fixture_dir": "real_spiral",
        "source_id": "p28a94bb9038347f8b5fc",
        "conversation_sha256": (
            "8a54cfe16b9e756dc3a3e464d5416febaa68fd983c8469552631f8c83e9cff0e"
        ),
        "reasoning_sha256": (
            "ebd095960ef7736a8843738c9f7816a667551c41133190111b84d2d98a085930"
        ),
        "paragraph_start_1_based": 133,
        "paragraph_end_1_based": 243,
    },
    {
        "case_id": "V41-REAL-BATTERY",
        "fixture_dir": "real_battery",
        "source_id": "pf3a7fa50dcf54bafbe7a",
        "conversation_sha256": (
            "495aaab620d2ae7bd1ea9e5af9d7fd7c880c1273d111387d480f1f21bc6c0c8f"
        ),
        "reasoning_sha256": (
            "6296cfe86c1e5ab8520cfec76ddebdfc6f60879273f2325f533f5f3ea3900d0b"
        ),
        "paragraph_start_1_based": 145,
        "paragraph_end_1_based": 260,
    },
)


class PackBuildError(RuntimeError):
    """A fail-closed pack construction error."""


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def canonical_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def _strict_agent_reasoning(document: Any) -> str:
    if not isinstance(document, dict) or not isinstance(document.get("steps"), list):
        raise PackBuildError("ATIF root or steps is invalid")
    candidates = [
        step.get("reasoning_content")
        for step in document["steps"]
        if isinstance(step, dict)
        and step.get("source") == "agent"
        and isinstance(step.get("reasoning_content"), str)
    ]
    if len(candidates) != 1 or not candidates[0]:
        raise PackBuildError(
            f"expected exactly one nonempty agent reasoning_content, got {len(candidates)}"
        )
    return candidates[0]


def _build_one(spec: dict[str, Any], builder_sha256: str) -> dict[str, Any]:
    conversation = (
        SOURCE_ROOT / spec["source_id"] / "exports" / "conversation.json"
    )
    if not conversation.is_file() or conversation.is_symlink():
        raise PackBuildError(f"source is not a regular file: {conversation}")
    conversation_bytes = conversation.read_bytes()
    if sha256_bytes(conversation_bytes) != spec["conversation_sha256"]:
        raise PackBuildError(f"conversation hash mismatch for {spec['case_id']}")
    try:
        document = json.loads(conversation_bytes)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise PackBuildError(f"invalid source JSON for {spec['case_id']}: {exc}") from exc
    reasoning = _strict_agent_reasoning(document)
    reasoning_bytes = reasoning.encode("utf-8")
    if sha256_bytes(reasoning_bytes) != spec["reasoning_sha256"]:
        raise PackBuildError(f"reasoning hash mismatch for {spec['case_id']}")
    paragraphs = [part.strip() for part in PARAGRAPH_SPLIT_RE.split(reasoning)]
    if any(not paragraph for paragraph in paragraphs):
        raise PackBuildError(f"empty paragraph after split for {spec['case_id']}")
    start = int(spec["paragraph_start_1_based"])
    end = int(spec["paragraph_end_1_based"])
    if not (1 <= start <= end <= len(paragraphs)):
        raise PackBuildError(
            f"paragraph selector {start}..{end} outside 1..{len(paragraphs)}"
        )
    excerpt = ("\n\n".join(paragraphs[start - 1 : end]) + "\n").encode("utf-8")
    fixture_dir = FIXTURE_ROOT / spec["fixture_dir"]
    raw_target = fixture_dir / "raw_solver_trajectory.txt"
    receipt_target = fixture_dir / "source-receipt.json"
    problem_target = fixture_dir / "problem.md"
    if not problem_target.is_file() or problem_target.is_symlink():
        raise PackBuildError(f"problem fixture is missing or unsafe: {problem_target}")
    for target in (raw_target, receipt_target):
        if target.exists() or target.is_symlink():
            raise PackBuildError(f"append-once destination exists: {target}")
    receipt = {
        "schema_version": "solve-vein/vms41-source-receipt/v1",
        "builder_schema_version": BUILDER_SCHEMA_VERSION,
        "builder_sha256": builder_sha256,
        "case_id": spec["case_id"],
        "source_id": spec["source_id"],
        "source_conversation_path": str(conversation),
        "source_conversation_sha256": spec["conversation_sha256"],
        "source_reasoning_sha256": spec["reasoning_sha256"],
        "source_reasoning_utf8_bytes": len(reasoning_bytes),
        "source_paragraph_count": len(paragraphs),
        "selector": {
            "kind": "blank_line_paragraph_closed_range",
            "split_regex": PARAGRAPH_SPLIT_RE.pattern,
            "strip_each_paragraph": True,
            "joiner": "\\n\\n",
            "terminal_newline": True,
            "start_1_based": start,
            "end_1_based": end,
        },
        "selected_paragraph_count": end - start + 1,
        "excerpt_utf8_bytes": len(excerpt),
        "excerpt_sha256": sha256_bytes(excerpt),
        "problem_sha256": sha256_bytes(problem_target.read_bytes()),
        "source_mutations": 0,
    }
    fixture_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix=f".{spec['fixture_dir']}-build-", dir=FIXTURE_ROOT
    ) as temporary:
        temp = Path(temporary)
        raw_temp = temp / raw_target.name
        receipt_temp = temp / receipt_target.name
        raw_temp.write_bytes(excerpt)
        receipt_temp.write_bytes(canonical_json_bytes(receipt))
        raw_temp.chmod(0o600)
        receipt_temp.chmod(0o600)
        os.replace(raw_temp, raw_target)
        os.replace(receipt_temp, receipt_target)
    return receipt


def main() -> int:
    builder_sha256 = sha256_bytes(Path(__file__).read_bytes())
    pack_receipt_path = FIXTURE_ROOT / "authentic-source-pack-receipt.json"
    if pack_receipt_path.exists() or pack_receipt_path.is_symlink():
        raise PackBuildError(f"append-once destination exists: {pack_receipt_path}")
    receipts = [_build_one(spec, builder_sha256) for spec in SOURCES]
    pack = {
        "schema_version": "solve-vein/vms41-authentic-source-pack-receipt/v1",
        "builder_schema_version": BUILDER_SCHEMA_VERSION,
        "builder_sha256": builder_sha256,
        "source_receipts": [
            {
                "case_id": receipt["case_id"],
                "source_receipt_ref": (
                    f"{next(spec['fixture_dir'] for spec in SOURCES if spec['case_id'] == receipt['case_id'])}"
                    "/source-receipt.json"
                ),
                "source_receipt_sha256": sha256_bytes(
                    canonical_json_bytes(receipt)
                ),
                "excerpt_sha256": receipt["excerpt_sha256"],
            }
            for receipt in receipts
        ],
        "source_mutations": 0,
    }
    pack_receipt_path.write_bytes(canonical_json_bytes(pack))
    pack_receipt_path.chmod(0o600)
    print(json.dumps(pack, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except PackBuildError as exc:
        print(f"PACK_BUILD_ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
