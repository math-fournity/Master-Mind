#!/usr/bin/env python3
"""MOIRA nonlinear AI runtime capsule for Devin CLI.

The goal is not to replace master.py. This script gives Devin a fresh,
machine-derived control context before it acts.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(os.environ.get("DEVIN_PROJECT_DIR", Path(__file__).resolve().parents[1])).resolve()
PROTOCOL_DIR = ROOT / "ai-runtime" / "protocol"
TASKS_FILE = ROOT / "tasks.json"
RUNTIME_DIR = ROOT / "runtime"


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {"_error": f"invalid json: {exc}", "_path": str(path)}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load_tasks() -> dict[str, Any]:
    return read_json(TASKS_FILE, {"version": "missing", "workers": {}, "tasks": []})


def task_counts(tasks_data: dict[str, Any]) -> dict[str, int]:
    return dict(Counter(str(task.get("status", "unknown")) for task in tasks_data.get("tasks", [])))


def worker_counts(tasks_data: dict[str, Any]) -> dict[str, int]:
    return dict(Counter(str(worker.get("status", "unknown")) for worker in tasks_data.get("workers", {}).values()))


def protocol_audit() -> dict[str, Any]:
    anchors_path = PROTOCOL_DIR / "agent-anchors.json"
    briefs_path = PROTOCOL_DIR / "command-briefs.json"
    manifest_path = PROTOCOL_DIR / "runtime-manifest.json"
    anchors = read_json(anchors_path, {"anchors": []})
    briefs = read_json(briefs_path, {"briefs": {}})
    manifest = read_json(manifest_path, {})
    issues: list[dict[str, Any]] = []
    anchor_results: list[dict[str, Any]] = []

    for anchor in anchors.get("anchors", []):
        source = ROOT / anchor.get("file", "")
        heading = anchor.get("heading", "")
        if not source.is_file():
            issues.append({"kind": "missing_anchor_file", "anchor_id": anchor.get("anchor_id"), "file": relative(source)})
            anchor_results.append({**anchor, "status": "missing_file"})
            continue
        text = source.read_text(encoding="utf-8", errors="replace")
        if heading not in text:
            issues.append(
                {
                    "kind": "missing_anchor_heading",
                    "anchor_id": anchor.get("anchor_id"),
                    "file": relative(source),
                    "heading": heading,
                }
            )
            anchor_results.append({**anchor, "status": "missing_heading"})
        else:
            anchor_results.append({**anchor, "status": "ok"})

    source_files = [anchors_path, briefs_path, manifest_path, ROOT / "AGENTS.md", ROOT / "worker_prompt.py"]
    source_hashes = {
        relative(path): sha256_file(path)
        for path in source_files
        if path.is_file()
    }
    material = {
        "anchors": anchors,
        "briefs": briefs,
        "manifest": manifest,
        "source_hashes": source_hashes,
    }
    protocol_hash = hashlib.sha256(
        json.dumps(material, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    return {
        "schema_version": "moira.protocol-audit.v1",
        "verdict": "PASS" if not issues else "FAIL",
        "remainder": len(issues),
        "protocol_hash": protocol_hash,
        "anchor_count": len(anchors.get("anchors", [])),
        "brief_count": len(briefs.get("briefs", {})),
        "anchors": anchor_results,
        "issues": issues,
    }


def nonlinear_state() -> dict[str, Any]:
    iteration = read_json(RUNTIME_DIR / "iteration_state.json", {})
    strategy = read_json(RUNTIME_DIR / "absorption_strategy.json", {})
    knowledge = read_json(RUNTIME_DIR / "knowledge_graph.json", {})
    dimensions = strategy.get("dimensions", {})
    coverage = {
        name: info.get("coverage", 0)
        for name, info in dimensions.items()
        if isinstance(info, dict)
    }
    lowest = sorted(coverage.items(), key=lambda item: item[1])[:3]
    concepts = knowledge.get("concepts", {})
    unknown_concepts = [
        name for name, info in concepts.items()
        if isinstance(info, dict) and info.get("status") == "unknown"
    ]
    return {
        "current_phase": strategy.get("current_phase", "unknown"),
        "iteration_count": iteration.get("iteration_count", strategy.get("iteration_count", 0)),
        "dimension_coverage": coverage,
        "lowest_coverage_dimensions": [{"dimension": name, "coverage": value} for name, value in lowest],
        "discoveries_count": len(knowledge.get("discovered", [])),
        "unknown_concepts_count": len(unknown_concepts),
    }


def derive_stop_policy(counts: dict[str, int], workers: dict[str, int], audit: dict[str, Any]) -> tuple[str, str]:
    if audit["verdict"] != "PASS":
        return "REVIEW_REQUIRED", "Protocol anchors drifted. Repair ai-runtime/protocol before trusting Devin guidance."
    failed = sum(counts.get(status, 0) for status in ("failed", "blocked", "error"))
    if failed:
        return "REVIEW_REQUIRED", "Failed or blocked tasks exist. Read evidence before retry or stop."
    queued = counts.get("queued", 0)
    leased = counts.get("leased", 0) + counts.get("in_progress", 0)
    busy = workers.get("busy", 0)
    if queued or leased or busy:
        return "CONTINUE_REQUIRED", f"queued={queued}, leased_or_in_progress={leased}, busy_workers={busy}."
    return "STOP_ALLOWED", "No queued tasks, leased tasks or busy Workers are visible in tasks.json."


def command_brief(role: str) -> dict[str, Any]:
    registry = read_json(PROTOCOL_DIR / "command-briefs.json", {"briefs": {}})
    brief = registry.get("briefs", {}).get(role)
    return {
        "schema_version": registry.get("schema_version", "moira.command-briefs.v1"),
        "role": role,
        "found": brief is not None,
        "brief": brief,
    }


def build_capsule(role: str = "master") -> dict[str, Any]:
    tasks_data = load_tasks()
    counts = task_counts(tasks_data)
    workers = worker_counts(tasks_data)
    audit = protocol_audit()
    stop_policy, stop_reason = derive_stop_policy(counts, workers, audit)
    return {
        "schema_version": "moira.runtime-capsule.v1",
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "project": "MOIRA Chinese Astrology",
        "role": role,
        "runtime_contract": {
            "AGENTS.md": "static constitution and philosophy anchor",
            "ai-runtime/protocol": "machine-audited runtime law",
            "tasks.json": "execution task ledger",
            "dev-docs/todos.json": "TODO truth ledger",
            "runtime": "checkpoints, audit logs, nonlinear state and evidence",
        },
        "protocol": {
            "verdict": audit["verdict"],
            "remainder": audit["remainder"],
            "hash": audit["protocol_hash"],
        },
        "task_status_counts": counts,
        "worker_status_counts": workers,
        "nonlinear_state": nonlinear_state(),
        "stop_policy": stop_policy,
        "stop_reason": stop_reason,
        "active_anchors": [
            {
                "anchor_id": anchor["anchor_id"],
                "severity": anchor["severity"],
                "summary": anchor["summary"],
                "status": anchor["status"],
            }
            for anchor in audit["anchors"]
            if role in anchor.get("roles", [])
        ],
        "role_brief": command_brief(role),
        "next_required_action": next_required_action(stop_policy, role),
    }


def next_required_action(stop_policy: str, role: str) -> str:
    if stop_policy == "REVIEW_REQUIRED":
        return "Repair protocol drift or inspect failed evidence before launching more agents."
    if role == "worker":
        return "Absorb the assigned bounded source package and checkpoint dimensions, maturity and computability."
    if role == "auditor":
        return "Audit Worker output against SOP三要素 and write PASS/PARTIAL/FAIL/BLOCKED evidence."
    if stop_policy == "CONTINUE_REQUIRED":
        return "Continue supervising queued, leased and busy work; do not stop from terminal quietness."
    return "If a human-level project gate also agrees, prepare a final report."


def render_text(capsule: dict[str, Any]) -> str:
    nonlinear = capsule["nonlinear_state"]
    lines = [
        "MOIRA runtime capsule",
        f"generated_at: {capsule['generated_at']}",
        f"role: {capsule['role']}",
        f"protocol: {capsule['protocol']['verdict']} remainder={capsule['protocol']['remainder']}",
        f"tasks: {capsule['task_status_counts']}",
        f"workers: {capsule['worker_status_counts']}",
        f"nonlinear_phase: {nonlinear['current_phase']} iteration={nonlinear['iteration_count']}",
        f"lowest_dimensions: {nonlinear['lowest_coverage_dimensions']}",
        f"stop_policy: {capsule['stop_policy']}",
        f"stop_reason: {capsule['stop_reason']}",
        f"next_required_action: {capsule['next_required_action']}",
        "active_anchors:",
    ]
    for anchor in capsule["active_anchors"]:
        lines.append(f"- {anchor['anchor_id']} [{anchor['status']}]: {anchor['summary']}")
    return "\n".join(lines)


def hook_output(event: str, role: str) -> int:
    capsule = build_capsule(role)
    text = render_text(capsule)
    if event == "Stop" and capsule["stop_policy"] != "STOP_ALLOWED":
        print(
            json.dumps(
                {
                    "decision": "block",
                    "reason": f"MOIRA stop gate says {capsule['stop_policy']}: {capsule['stop_reason']}",
                    "hookSpecificOutput": {
                        "hookEventName": event,
                        "additionalContext": text,
                    },
                },
                ensure_ascii=False,
            )
        )
        return 2
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": event,
                    "additionalContext": text,
                }
            },
            ensure_ascii=False,
        )
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="MOIRA nonlinear AI runtime")
    sub = parser.add_subparsers(dest="command", required=True)

    capsule_parser = sub.add_parser("capsule")
    capsule_parser.add_argument("--role", default="master", choices=["master", "worker", "auditor"])
    capsule_parser.add_argument("--format", default="json", choices=["json", "text"])

    audit_parser = sub.add_parser("protocol-audit")
    audit_parser.add_argument("--format", default="json", choices=["json", "text"])

    brief_parser = sub.add_parser("brief")
    brief_parser.add_argument("role", choices=["master", "worker", "auditor", "stop"])

    hook_parser = sub.add_parser("hook")
    hook_parser.add_argument("event")
    hook_parser.add_argument("--role", default="master", choices=["master", "worker", "auditor"])

    sub.add_parser("validate")

    args = parser.parse_args()
    if args.command == "capsule":
        capsule = build_capsule(args.role)
        print(render_text(capsule) if args.format == "text" else json.dumps(capsule, ensure_ascii=False, indent=2))
        return 0
    if args.command == "protocol-audit":
        audit = protocol_audit()
        if args.format == "text":
            print(f"{audit['verdict']} remainder={audit['remainder']} anchors={audit['anchor_count']} briefs={audit['brief_count']}")
            for issue in audit["issues"]:
                print(json.dumps(issue, ensure_ascii=False))
        else:
            print(json.dumps(audit, ensure_ascii=False, indent=2))
        return 0 if audit["verdict"] == "PASS" else 1
    if args.command == "brief":
        print(json.dumps(command_brief(args.role), ensure_ascii=False, indent=2))
        return 0
    if args.command == "hook":
        return hook_output(args.event, args.role)
    if args.command == "validate":
        audit = protocol_audit()
        capsule = build_capsule("master")
        print(render_text(capsule))
        return 0 if audit["verdict"] == "PASS" else 1
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
