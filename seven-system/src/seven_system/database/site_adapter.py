"""WP-DB1L 只读逻辑站点 adapter 协议与 fake 实现。

只读 adapter 不暴露 raw driver、不执行写入、不应用 migration。
真实 Arango 连接只允许通过 ``seven_system.database.arango_port``；
本模块的 ``FakeLogicalSiteAdapter`` 专供测试使用，不连接任何真实数据库。
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, Mapping, Protocol

from .environment import EXPECTED_DATABASE
from .port import CollectionSnapshot


# 匹配 seven_<lower-ascii>_v<N> 的版本化集合名
_SEVEN_VERSIONED_RE = re.compile(r"^seven_[a-z0-9_]+_v[1-9][0-9]*$")

# 匹配 seven_ 前缀但可能未版本化的集合名
_SEVEN_PREFIX_RE = re.compile(r"^seven_")

# 题海 / system 集合前缀。DB1L允许同一逻辑数据库内存在这些既有集合，
# 但Seven自己的schema plan不得复用这些集合名。
_FORBIDDEN_PREFIXES = ("math_", "system_", "题", "question_", "problem_")


@dataclass(frozen=True)
class SiteFingerprint:
    """逻辑站点的不可变指纹——endpoint/server/driver/principal。"""

    endpoint: str
    server_version: str
    driver_name: str
    driver_version: str
    principal: str  # 已脱敏的用户名

    def as_dict(self) -> dict[str, Any]:
        return {
            "endpoint": self.endpoint,
            "server_version": self.server_version,
            "driver_name": self.driver_name,
            "driver_version": self.driver_version,
            "principal": self.principal,
        }

    @property
    def fingerprint_hash(self) -> str:
        from ..hashing import object_hash

        return object_hash(
            "SiteFingerprint",
            "site-fingerprint/v1",
            self.as_dict(),
        )


@dataclass(frozen=True)
class CatalogSnapshot:
    """只读 catalog 快照——所有集合及其索引。"""

    collections: tuple[CollectionSnapshot, ...]

    def as_dict(self) -> dict[str, Any]:
        return {
            "collections": [
                {
                    "name": col.name,
                    "collection_type": col.collection_type,
                    "indexes": [
                        {
                            "name": idx.name,
                            "type": idx.index_type,
                            "fields": list(idx.fields),
                            "unique": idx.unique,
                            "sparse": idx.sparse,
                        }
                        for idx in col.indexes
                    ],
                }
                for col in sorted(self.collections, key=lambda c: c.name)
            ],
        }

    @property
    def catalog_hash(self) -> str:
        from ..hashing import object_hash

        return object_hash(
            "CatalogSnapshot",
            "catalog-snapshot/v1",
            self.as_dict(),
        )

    @property
    def collection_names(self) -> tuple[str, ...]:
        return tuple(col.name for col in self.collections)


@dataclass(frozen=True)
class SevenCollectionEnumeration:
    """枚举 seven_*_vN 集合并检查冲突的结果。"""

    versioned_collections: tuple[str, ...]
    unversioned_seven_collections: tuple[str, ...]
    forbidden_collections: tuple[str, ...]
    conflicts: tuple[str, ...]

    def as_dict(self) -> dict[str, Any]:
        return {
            "versioned_collections": list(self.versioned_collections),
            "unversioned_seven_collections": list(self.unversioned_seven_collections),
            "forbidden_collections": list(self.forbidden_collections),
            "conflicts": list(self.conflicts),
        }


class LogicalSiteAdapter(Protocol):
    """只读逻辑站点 adapter 协议。

    实现者必须保证：
    - 零写入（read-only 权限）
    - 不暴露 raw driver
    - 不执行 migration / DDL
    """

    @property
    def database_name(self) -> str: ...

    def connect_readonly(self) -> None:
        """以只读模式连接；连接失败必须抛 DatabaseConnectionError。"""
        ...

    def current_database(self) -> str:
        """返回 CURRENT_DATABASE() 的值。"""
        ...

    def site_fingerprint(self) -> SiteFingerprint:
        """返回 endpoint/server/driver/principal 指纹。"""
        ...

    def catalog_snapshot(self) -> CatalogSnapshot:
        """返回完整只读 catalog 快照。"""
        ...

    def enumerate_seven_collections(self) -> SevenCollectionEnumeration:
        """枚举所有 seven_*_vN 集合并检查冲突。"""
        ...

    @property
    def write_count(self) -> int:
        """返回 adapter 生命周期内的写入计数（只读 adapter 必须为 0）。"""
        ...


def classify_collection(name: str) -> str:
    """将集合名分类为 versioned / unversioned_seven / forbidden / other。"""

    if _SEVEN_VERSIONED_RE.match(name):
        return "versioned"
    if _SEVEN_PREFIX_RE.match(name):
        return "unversioned_seven"
    for prefix in _FORBIDDEN_PREFIXES:
        if name.startswith(prefix):
            return "forbidden"
    return "other"


def enumerate_collections_from_catalog(
    catalog: CatalogSnapshot,
) -> SevenCollectionEnumeration:
    """从 catalog 快照枚举 seven_*_vN 集合并检查冲突。"""

    versioned: list[str] = []
    unversioned: list[str] = []
    forbidden: list[str] = []
    conflicts: list[str] = []

    for name in sorted(catalog.collection_names):
        category = classify_collection(name)
        if category == "versioned":
            versioned.append(name)
        elif category == "unversioned_seven":
            unversioned.append(name)
            conflicts.append(f"unversioned:{name}")
        elif category == "forbidden":
            forbidden.append(name)

    return SevenCollectionEnumeration(
        versioned_collections=tuple(versioned),
        unversioned_seven_collections=tuple(unversioned),
        forbidden_collections=tuple(forbidden),
        conflicts=tuple(conflicts),
    )


@dataclass
class FakeLogicalSiteAdapter:
    """测试用 fake adapter——不连接任何真实数据库。

    所有字段在构造时确定；``write_count`` 永远为 0（除非显式注入 fault）。
    """

    database_name_value: str = EXPECTED_DATABASE
    current_database_value: str = EXPECTED_DATABASE
    fingerprint: SiteFingerprint = field(
        default_factory=lambda: SiteFingerprint(
            endpoint="http://localhost:8529",
            server_version="arangodb-3.12.1",
            driver_name="python-arango",
            driver_version="8.1.0",
            principal="seven-readonly-user",
        )
    )
    catalog: CatalogSnapshot = field(default_factory=lambda: CatalogSnapshot(()))
    connected: bool = False
    write_count_value: int = 0
    connect_should_fail: bool = False

    @property
    def database_name(self) -> str:
        return self.database_name_value

    def connect_readonly(self) -> None:
        if self.connect_should_fail:
            from .errors import DatabaseConnectionError

            raise DatabaseConnectionError(
                "fake logical site adapter: simulated connection failure"
            )
        self.connected = True

    def current_database(self) -> str:
        if not self.connected:
            from .errors import DatabaseConnectionError

            raise DatabaseConnectionError(
                "fake logical site adapter: not connected"
            )
        return self.current_database_value

    def site_fingerprint(self) -> SiteFingerprint:
        if not self.connected:
            from .errors import DatabaseConnectionError

            raise DatabaseConnectionError(
                "fake logical site adapter: not connected"
            )
        return self.fingerprint

    def catalog_snapshot(self) -> CatalogSnapshot:
        if not self.connected:
            from .errors import DatabaseConnectionError

            raise DatabaseConnectionError(
                "fake logical site adapter: not connected"
            )
        return self.catalog

    def enumerate_seven_collections(self) -> SevenCollectionEnumeration:
        if not self.connected:
            from .errors import DatabaseConnectionError

            raise DatabaseConnectionError(
                "fake logical site adapter: not connected"
            )
        return enumerate_collections_from_catalog(self.catalog)

    @property
    def write_count(self) -> int:
        return self.write_count_value
