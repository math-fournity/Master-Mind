#!/usr/bin/env python3
"""Build a side-effect-free WorkPackagePlan JSON on stdout.

This tool does not write files and does not authorize live work.  It exists so
that ordinary implementer-owned work packages can derive brittle plan fields
from the canonical DAG, NormativeRequirementIndex, and a verified signed
NormativeRequirementReviewRecord instead of hand-copying them.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
SEVEN_ROOT = HERE.parents[2]
SRC = SEVEN_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from seven_system.operations.work_package_plan_builder import (  # noqa: E402
    WorkPackagePlanBuilderError,
    build_side_effect_free_work_package_plan,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="build_work_package_plan",
        description="Build a side-effect-free ordinary WorkPackagePlan JSON on stdout.",
    )
    parser.add_argument("--plan-input", required=True, type=Path)
    parser.add_argument(
        "--dag",
        default=SEVEN_ROOT / "docs" / "implementation" / "work-package-dag.v1.json",
        type=Path,
    )
    parser.add_argument(
        "--normative-index",
        default=SEVEN_ROOT / "docs" / "implementation" / "normative-requirement-index.v1.json",
        type=Path,
    )
    parser.add_argument("--normative-review-record", required=True, type=Path)
    parser.add_argument("--normative-review-public-key-hex", required=True)
    args = parser.parse_args(argv)

    try:
        public_key_bytes = bytes.fromhex(args.normative_review_public_key_hex)
        if len(public_key_bytes) != 32:
            raise ValueError("normative-review-public-key-hex must encode exactly 32 Ed25519 raw public key bytes")
        plan_input = json.loads(args.plan_input.read_text(encoding="utf-8"))
        plan = build_side_effect_free_work_package_plan(
            plan_input=plan_input,
            dag_path=args.dag,
            normative_index_path=args.normative_index,
            normative_review_record_path=args.normative_review_record,
            normative_review_public_key_bytes=public_key_bytes,
        )
    except (ValueError, OSError, json.JSONDecodeError, WorkPackagePlanBuilderError) as exc:
        print(
            json.dumps(
                {
                    "status": "ERROR",
                    "error_type": type(exc).__name__,
                    "message": str(exc),
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            ),
            file=sys.stderr,
        )
        return 3

    print(json.dumps(plan, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
