"""python-arango 的私有 driver adapter。

只有本文件允许 import `arango`。`from_environment` 必须先完成固定数据库身份
检查；missing/wrong DB 路径不会 import driver、不会构造 client。
"""

from __future__ import annotations

import os
from collections.abc import Callable, Mapping
from importlib import metadata
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
from .site_adapter import (
    CatalogSnapshot,
    SevenCollectionEnumeration,
    SiteFingerprint,
    enumerate_collections_from_catalog,
)


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
        instance.__current_database = current_databases[0]
        instance.__host = config.host
        instance.__username = config.username
        return instance

    @property
    def database_name(self) -> str:
        return self.__database_name

    def inspect_collection(self, name: str) -> CollectionSnapshot | None:
        allowed = validate_collection_name(name)
        if not self.__database_driver.has_collection(allowed):
            return None
        return self.__inspect_existing_collection(allowed)

    def __inspect_existing_collection(self, name: str) -> CollectionSnapshot:
        collection = self.__database_driver.collection(name)
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
                    f"collection {name} returned a malformed index"
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
            name=name,
            collection_type=collection_type,
            indexes=tuple(indexes),
        )

    def connect_readonly(self) -> None:
        """LogicalSiteAdapter compatibility: from_environment already connected."""

    def current_database(self) -> str:
        return self.__current_database

    def site_fingerprint(self) -> SiteFingerprint:
        try:
            server_version = str(self.__database_driver.version())
        except Exception:
            raise DatabaseConnectionError("Arango server version is not observable") from None
        try:
            driver_version = metadata.version("python-arango")
        except metadata.PackageNotFoundError:
            driver_version = "unknown"
        return SiteFingerprint(
            endpoint=self.__host,
            server_version=server_version,
            driver_name="python-arango",
            driver_version=driver_version,
            principal=self.__username,
        )

    def catalog_snapshot(self) -> CatalogSnapshot:
        try:
            raw_collections = list(self.__database_driver.collections())
        except Exception:
            raise DatabaseConnectionError("Arango collection catalog is not observable") from None
        collections: list[CollectionSnapshot] = []
        for raw in raw_collections:
            if not isinstance(raw, Mapping):
                raise SchemaConflictError("Arango collection catalog returned a malformed entry")
            name = raw.get("name")
            if not isinstance(name, str) or not name or any(ch in name for ch in "\r\n\x00"):
                raise SchemaConflictError("Arango collection catalog returned a malformed name")
            if name.startswith("_") or raw.get("system") is True:
                continue
            collections.append(self.__inspect_existing_collection(name))
        return CatalogSnapshot(collections=tuple(sorted(collections, key=lambda col: col.name)))

    def enumerate_seven_collections(self) -> SevenCollectionEnumeration:
        return enumerate_collections_from_catalog(self.catalog_snapshot())

    @property
    def write_count(self) -> int:
        return 0
