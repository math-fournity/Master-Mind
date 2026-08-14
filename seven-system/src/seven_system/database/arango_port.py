"""python-arango 的私有 driver adapter。

只有本文件允许 import `arango`。`from_environment` 必须先完成固定数据库身份
检查；missing/wrong DB 路径不会 import driver、不会构造 client。
"""

from __future__ import annotations

import os
from collections.abc import Callable, Mapping
from typing import Any

from .environment import DatabaseEnvironment, EXPECTED_DATABASE
from .errors import (
    DatabaseConnectionError,
    DatabaseConfigurationError,
    DatabaseDriverUnavailableError,
    DatabaseIdentityError,
    SchemaConflictError,
)
from .port import CollectionSnapshot, IndexSnapshot
from .spec import validate_collection_name


class ArangoDatabasePort:
    def __init__(self) -> None:
        raise DatabaseConfigurationError(
            "ArangoDatabasePort must be created with from_environment()"
        )

    @classmethod
    def from_environment(
        cls,
        environ: Mapping[str, str] | None = None,
        *,
        client_factory: Callable[..., Any] | None = None,
    ) -> "ArangoDatabasePort":
        # 这行必须位于 driver import 和 factory call 之前。
        config = DatabaseEnvironment.from_environ(
            os.environ if environ is None else environ
        )

        if client_factory is None:
            try:
                from arango import ArangoClient  # type: ignore[import-not-found]
            except ImportError as exc:
                raise DatabaseDriverUnavailableError(
                    "python-arango is unavailable after configuration validation"
                ) from exc
            client_factory = ArangoClient

        try:
            client = client_factory(hosts=config.host)
            # verify=True 只验证已存在的目标数据库；这里没有 create_database path。
            database = client.db(
                config.database,
                username=config.username,
                password=config.password,
                verify=True,
            )
        except Exception:
            raise DatabaseConnectionError(
                "Arango client/database initialization failed after identity validation"
            ) from None
        try:
            current_databases = list(
                database.aql.execute("RETURN CURRENT_DATABASE()")
            )
        except Exception:
            raise DatabaseIdentityError(EXPECTED_DATABASE) from None
        if current_databases != [EXPECTED_DATABASE]:
            raise DatabaseIdentityError(EXPECTED_DATABASE)
        instance = object.__new__(cls)
        instance.__database_driver = database
        instance.__database_name = config.database
        return instance

    @property
    def database_name(self) -> str:
        return self.__database_name

    def inspect_collection(self, name: str) -> CollectionSnapshot | None:
        allowed = validate_collection_name(name)
        if not self.__database_driver.has_collection(allowed):
            return None
        collection = self.__database_driver.collection(allowed)
        properties = collection.properties()
        raw_type = properties.get("type", 2)
        collection_type = "edge" if raw_type in {3, "edge"} else "document"
        indexes: list[IndexSnapshot] = []
        for raw in collection.indexes():
            index_type = str(raw.get("type", ""))
            # primary 是Arango为document collection维护的系统索引；其他任何
            # 类型都必须进入snapshot，并由canonical planner显式拒绝。
            if index_type == "primary":
                continue
            name_value = raw.get("name")
            fields = raw.get("fields")
            if not isinstance(name_value, str) or not isinstance(fields, list) or not all(
                isinstance(field, str) for field in fields
            ):
                raise SchemaConflictError(
                    f"collection {allowed} returned a malformed persistent index"
                )
            indexes.append(
                IndexSnapshot(
                    name=name_value,
                    fields=tuple(fields),
                    index_type=index_type,
                    unique=raw.get("unique") is True,
                    sparse=raw.get("sparse") is True,
                )
            )
        return CollectionSnapshot(
            name=allowed,
            collection_type=collection_type,
            indexes=tuple(indexes),
        )
