"""Strict DB 的 typed、secret-safe 错误。"""

from __future__ import annotations


class DatabaseContractError(RuntimeError):
    """所有 Seven 数据库契约错误的基类。"""


class DatabaseConfigurationError(DatabaseContractError):
    """显式环境配置缺失或格式不安全。"""


class MissingDatabaseEnvironmentError(DatabaseConfigurationError):
    def __init__(self, missing_keys: tuple[str, ...]) -> None:
        self.missing_keys = missing_keys
        super().__init__(
            "required database environment is missing: " + ", ".join(missing_keys)
        )


class DatabaseIdentityError(DatabaseConfigurationError):
    def __init__(self, expected_database: str) -> None:
        self.expected_database = expected_database
        # 故意不回显实际环境值；它可能来自污染的 secret/URI。
        super().__init__(
            f"ARANGO_DB does not exactly match the approved database "
            f"{expected_database!r}"
        )


class DatabaseDriverUnavailableError(DatabaseContractError):
    """通过身份门后仍无法加载 python-arango。"""


class DatabaseConnectionError(DatabaseContractError):
    """driver 初始化失败；消息不会转录可能含凭据的底层异常。"""


class CollectionNotAllowedError(DatabaseContractError):
    def __init__(self) -> None:
        # 不回显原字符串，避免日志控制字符/Unicode spoof 进入审计日志。
        super().__init__("collection is not in the fixed Seven v1 allowlist")


class SchemaConflictError(DatabaseContractError):
    """现存 collection/index 与 canonical spec 冲突，禁止自动修补。"""


class MigrationPlanMismatchError(DatabaseContractError):
    """批准的 plan/spec/现场快照发生漂移。"""
