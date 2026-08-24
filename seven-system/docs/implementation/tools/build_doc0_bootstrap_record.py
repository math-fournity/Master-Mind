#!/usr/bin/env python3
"""Build a DOC0 bootstrap completion record from sealed local receipts.

The tool is intentionally stdout-only.  It does not write evidence files,
change work-package state, sign records, connect to databases, or call models.
Use shell redirection or a future CAS writer only after the generated JSON has
been reviewed under the appropriate work-package rules.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
SEVEN_ROOT = HERE.parents[2]
SRC = SEVEN_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from seven_system.operations.doc0_bootstrap_evidence import (  # noqa: E402
    Doc0BootstrapEvidenceError,
    build_doc0_bootstrap_completion_record,
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load_json(path: Path) -> dict:
    data = json.loads(path.read_text())
    if not isinstance(data, dict):
        raise Doc0BootstrapEvidenceError(f"{path} is not a JSON object")
    return data


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="build_doc0_bootstrap_record",
        description="Build a side-effect-free DOC0 bootstrap completion record JSON on stdout.",
    )
    parser.add_argument("--record-id", required=True)
    parser.add_argument("--doc-contract-receipt", required=True, type=Path)
    parser.add_argument("--doc-contract-ref", required=True)
    parser.add_argument("--doc0-test-receipt", required=True, type=Path)
    parser.add_argument("--doc0-test-ref", required=True)
    parser.add_argument("--created-at", required=True)
    parser.add_argument("--creator", required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        record = build_doc0_bootstrap_completion_record(
            record_id=args.record_id,
            doc_contract_receipt=_load_json(args.doc_contract_receipt),
            doc_contract_receipt_ref_and_hash={
                "ref": args.doc_contract_ref,
                "sha256": _sha256(args.doc_contract_receipt),
            },
            doc0_test_receipt=_load_json(args.doc0_test_receipt),
            doc0_test_receipt_ref_and_hash={
                "ref": args.doc0_test_ref,
                "sha256": _sha256(args.doc0_test_receipt),
            },
            created_at=args.created_at,
            creator=args.creator,
        )
    except (Doc0BootstrapEvidenceError, OSError, json.JSONDecodeError) as error:
        print(json.dumps({"verdict": "FAIL", "error": str(error)}, ensure_ascii=False, sort_keys=True), file=sys.stderr)
        return 3

    print(json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
