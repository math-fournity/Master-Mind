#!/usr/bin/env python3
"""Synchronize WP-DOC0's generated traceability fields with frozen inputs."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
IMPL = HERE.parent
PLAN_PATH = IMPL / "wp-doc0-plan.v1.json"
INDEX_PATH = IMPL / "normative-requirement-index.v1.json"
DAG_PATH = IMPL / "work-package-dag.v1.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text())
    if not isinstance(value, dict):
        raise TypeError(f"{path.name} must contain a JSON object")
    return value


def synchronized_plan() -> dict[str, object]:
    plan = load(PLAN_PATH)
    index = load(INDEX_PATH)
    wp_id = str(plan["wp_id"])
    clauses = [
        item
        for item in index["clauses"]
        if isinstance(item, dict) and wp_id in item.get("consumer_wp_ids", [])
    ]
    plan["canonical_dag"] = {"ref": DAG_PATH.name, "sha256": sha256(DAG_PATH)}
    plan["normative_index_ref_and_hash"] = {"ref": INDEX_PATH.name, "sha256": sha256(INDEX_PATH)}
    plan["requirement_ids"] = sorted(
        str(item["requirement_id"])
        for item in index["requirement_catalog"]
        if isinstance(item, dict) and wp_id in item.get("applicable_wp_ids", [])
    )
    plan["normative_clause_ids"] = sorted(str(item["clause_id"]) for item in clauses)
    plan["normative_spec_refs_and_hashes"] = [
        {"ref": ref, "sha256": digest}
        for ref, digest in sorted(
            {
                (str(item["source_file"]), str(item["source_file_sha256"]))
                for item in clauses
            }
        )
    ]
    plan["plan_hash"] = None
    plan["plan_hash"] = hashlib.sha256(
        json.dumps(plan, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return plan


def rendered(plan: dict[str, object]) -> bytes:
    return (json.dumps(plan, ensure_ascii=False, indent=2) + "\n").encode()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = rendered(synchronized_plan())
    if args.check:
        if PLAN_PATH.read_bytes() != expected:
            print("STALE")
            return 1
        print("CURRENT")
        return 0
    PLAN_PATH.write_bytes(expected)
    print(
        json.dumps(
            {
                "status": "SYNCHRONIZED",
                "plan": str(PLAN_PATH),
                "sha256": sha256(PLAN_PATH),
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
