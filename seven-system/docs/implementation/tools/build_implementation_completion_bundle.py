#!/usr/bin/env python3
"""Build a side-effect-free ImplementationCompletionBundle on stdout.

This tool is a mechanical candidate-bundle assembler.  It does not write to
CAS, update the work-package board, sign records, connect to databases, call
models, or launch a Solver.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
SEVEN_ROOT = HERE.parents[2]
SRC = SEVEN_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from seven_system.operations.implementation_bundle_evidence import (  # noqa: E402
    ImplementationBundleEvidenceError,
    build_side_effect_free_implementation_completion_bundle,
)


def _load_json_object(path: Path) -> dict:
    data = json.loads(path.read_text())
    if not isinstance(data, dict):
        raise ImplementationBundleEvidenceError(f"{path} is not a JSON object")
    return data


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="build_implementation_completion_bundle",
        description="Build a side-effect-free ImplementationCompletionBundle JSON on stdout.",
    )
    parser.add_argument("--bundle-input", required=True, type=Path)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--plan-sha256", required=True)
    parser.add_argument(
        "--dag",
        default=SEVEN_ROOT / "docs" / "implementation" / "work-package-dag.v1.json",
        type=Path,
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        bundle = build_side_effect_free_implementation_completion_bundle(
            bundle_input=_load_json_object(args.bundle_input),
            plan_path=args.plan,
            expected_plan_sha256=args.plan_sha256,
            dag_path=args.dag,
        )
    except (ImplementationBundleEvidenceError, OSError, json.JSONDecodeError) as error:
        print(json.dumps({"verdict": "FAIL", "error": str(error)}, ensure_ascii=False, sort_keys=True), file=sys.stderr)
        return 3

    print(json.dumps(bundle, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
