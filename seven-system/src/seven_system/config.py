"""Seven System 的站点配置读取与静态校验。"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Optional

from .schema_validation import validate_schema


LIVE_MODES = {"golden_slice", "continuous", "fault_injection"}
ALL_MODES = LIVE_MODES | {"dry_run"}
SCHEMA_ROOT = Path(__file__).resolve().parents[2] / "schemas"


class ConfigError(ValueError):
    pass


def _mapping(value: Any, name: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ConfigError(f"{name} must be an object")
    return value


def _required_text(section: Mapping[str, Any], key: str, prefix: str) -> str:
    value = section.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ConfigError(f"{prefix}.{key} must be a non-empty string")
    return value


def _optional_path(section: Mapping[str, Any], key: str) -> Optional[Path]:
    value = section.get(key)
    if value in (None, ""):
        return None
    if not isinstance(value, str):
        raise ConfigError(f"{key} must be a path string or null")
    return Path(value)


def _boolean(
    section: Mapping[str, Any], key: str, prefix: str, *, default: bool
) -> bool:
    value = section.get(key, default)
    if not isinstance(value, bool):
        raise ConfigError(f"{prefix}.{key} must be a boolean")
    return value


@dataclass(frozen=True)
class SevenConfig:
    schema_version: str
    system_id: str
    mode: str
    repository_root: Path
    volume_root: Path
    data_root: Path
    minimum_free_bytes: int
    require_volume_readme: bool
    expected_database: str
    database_adapter: str
    allow_database_writes: bool
    database_capability_report: Optional[Path]
    redis_namespace: str
    harness_path: Path
    solver_work_root: Path
    trajectory_root: Path
    tool_policy: str
    launch_interval_seconds: float
    max_concurrency: int
    allow_live_solver_dispatch: bool
    safe_launch_capability_report: Optional[Path]
    no_tool_capability_report: Optional[Path]
    vault_root: Path
    answer_isolation_capability_report: Optional[Path]

    @classmethod
    def from_mapping(cls, raw: Mapping[str, Any]) -> "SevenConfig":
        storage = _mapping(raw.get("storage"), "storage")
        database = _mapping(raw.get("database"), "database")
        control = _mapping(raw.get("control"), "control")
        solver = _mapping(raw.get("solver"), "solver")
        answers = _mapping(raw.get("answers"), "answers")

        mode = _required_text(raw, "mode", "root")
        if mode not in ALL_MODES:
            raise ConfigError(f"mode must be one of {sorted(ALL_MODES)}")

        schema_version = _required_text(raw, "schema_version", "root")
        if schema_version != "seven-config/v1":
            raise ConfigError("root.schema_version must be seven-config/v1")

        minimum_free_bytes = storage.get("minimum_free_bytes", 0)
        if (
            isinstance(minimum_free_bytes, bool)
            or not isinstance(minimum_free_bytes, int)
            or minimum_free_bytes < 0
        ):
            raise ConfigError("storage.minimum_free_bytes must be a non-negative integer")

        launch_interval = solver.get("launch_interval_seconds")
        if isinstance(launch_interval, bool) or not isinstance(
            launch_interval, (int, float)
        ) or not math.isfinite(launch_interval):
            raise ConfigError(
                "solver.launch_interval_seconds must be a finite number"
            )

        max_concurrency = solver.get("max_concurrency")
        if (
            isinstance(max_concurrency, bool)
            or not isinstance(max_concurrency, int)
            or max_concurrency < 1
        ):
            raise ConfigError("solver.max_concurrency must be a positive integer")

        return cls(
            schema_version=schema_version,
            system_id=_required_text(raw, "system_id", "root"),
            mode=mode,
            repository_root=Path(_required_text(raw, "repository_root", "root")),
            volume_root=Path(_required_text(storage, "volume_root", "storage")),
            data_root=Path(_required_text(storage, "data_root", "storage")),
            minimum_free_bytes=minimum_free_bytes,
            require_volume_readme=_boolean(
                storage, "require_volume_readme", "storage", default=True
            ),
            expected_database=_required_text(database, "expected_database", "database"),
            database_adapter=_required_text(database, "adapter_contract", "database"),
            allow_database_writes=_boolean(
                database, "allow_writes", "database", default=False
            ),
            database_capability_report=_optional_path(database, "capability_report"),
            redis_namespace=_required_text(control, "redis_namespace", "control"),
            harness_path=Path(_required_text(solver, "harness_path", "solver")),
            solver_work_root=Path(_required_text(solver, "work_root", "solver")),
            trajectory_root=Path(_required_text(solver, "trajectory_root", "solver")),
            tool_policy=_required_text(solver, "tool_policy", "solver"),
            launch_interval_seconds=float(launch_interval),
            max_concurrency=max_concurrency,
            allow_live_solver_dispatch=_boolean(
                solver, "allow_live_dispatch", "solver", default=False
            ),
            safe_launch_capability_report=_optional_path(
                solver, "safe_launch_capability_report"
            ),
            no_tool_capability_report=_optional_path(
                solver, "no_tool_capability_report"
            ),
            vault_root=Path(_required_text(answers, "vault_root", "answers")),
            answer_isolation_capability_report=_optional_path(
                answers, "capability_report"
            ),
        )


def load_config(path: Path) -> SevenConfig:
    try:
        with path.open("r", encoding="utf-8") as handle:
            raw = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise ConfigError(f"cannot load config {path}: {exc}") from exc
    root = _mapping(raw, "root")
    schema_path = SCHEMA_ROOT / "runtime-config.schema.json"
    try:
        with schema_path.open("r", encoding="utf-8") as handle:
            schema = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise ConfigError(f"cannot load runtime config schema {schema_path}: {exc}") from exc
    if not isinstance(schema, dict):
        raise ConfigError("runtime config schema root must be an object")
    schema_errors = validate_schema(raw, schema)
    if schema_errors:
        raise ConfigError("runtime config schema validation failed: " + "; ".join(schema_errors))
    return SevenConfig.from_mapping(root)
