from __future__ import annotations

import json
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import patch


def build_site(tmp_path: Path, *, mode: str = "dry_run") -> tuple[Path, dict]:
    repository_root = tmp_path / "repo" / "seven-system"
    asset_root = repository_root / "assets" / "solver"
    asset_root.mkdir(parents=True)
    (asset_root / "AGENTS.md").write_text(
        "不要使用任何工具\n### PROOF COMPLETE\n### I CANNOT SOLVE THIS\n",
        encoding="utf-8",
    )

    volume_root = tmp_path / "volume"
    volume_root.mkdir()
    (volume_root / "README.md").write_text("test volume\n", encoding="utf-8")
    data_root = volume_root / "seven-system-data"
    data_root.mkdir()
    solver_work_root = data_root / "solver-work"
    trajectory_root = data_root / "trajectory"
    solver_work_root.mkdir()
    trajectory_root.mkdir()

    harness = tmp_path / "solver_harness.py"
    harness.write_text("# fixture\n", encoding="utf-8")

    payload = {
        "schema_version": "seven-config/v1",
        "system_id": "seven-system",
        "mode": mode,
        "repository_root": str(repository_root),
        "storage": {
            "volume_root": str(volume_root),
            "data_root": str(data_root),
            "minimum_free_bytes": 0,
            "require_volume_readme": True,
        },
        "database": {
            "expected_database": "xishujuzhen_math_glm52",
            "adapter_contract": "seven-database-port/v1",
            "allow_writes": False,
            "capability_report": None,
        },
        "control": {"redis_namespace": "evidence:seven:test:"},
        "solver": {
            "harness_path": str(harness),
            "work_root": str(solver_work_root),
            "trajectory_root": str(trajectory_root),
            "tool_policy": "forbid_all",
            "launch_interval_seconds": 3,
            "max_concurrency": 2,
            "allow_live_dispatch": False,
            "safe_launch_capability_report": None,
            "no_tool_capability_report": None,
        },
        "answers": {
            "vault_root": str(data_root / "vault"),
            "capability_report": None,
        },
    }
    config_path = tmp_path / "runtime.json"
    config_path.write_text(json.dumps(payload), encoding="utf-8")
    return config_path, payload


@contextmanager
def patched_site(payload: dict):
    with patch(
        "seven_system.preflight.ACTUAL_REPOSITORY_ROOT",
        Path(payload["repository_root"]),
    ), patch("seven_system.preflight.os.path.ismount", return_value=True):
        yield


def write_pass_capability(
    path: Path, name: str, *, subject_hash: str = "0" * 64
) -> None:
    required_claims = {
        "database": [
            "expected_database_fail_closed",
            "reads_have_no_schema_side_effects",
            "cas_and_unique_indexes_verified",
        ],
        "safe_launch": [
            "structured_argv_or_readonly_prompt_file",
            "single_canonical_prompt_render",
            "launch_receipt_is_persisted",
        ],
        "no_tool": [
            "tool_surface_removed_or_empty_registry",
            "missing_observation_fails_closed",
            "all_terminal_states_are_audited",
            "solver_has_no_db_or_vault_credentials",
        ],
        "answer_isolation": [
            "solver_cannot_access_vault",
            "role_views_are_minimum_privilege",
            "access_is_append_only_audited",
        ],
    }
    path.write_text(
        json.dumps(
            {
                "schema_version": "capability-report/v1",
                "capability": name,
                "verdict": "PASS",
                "generated_at": "2026-08-13T00:00:00Z",
                "subject_hash": subject_hash,
                "checks": [{"check_id": "fixture", "verdict": "PASS"}],
                "claims": {claim: True for claim in required_claims[name]},
            }
        ),
        encoding="utf-8",
    )
