"""不暴露 raw driver 的 Strict DB port 协议与只读快照类型。"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


DATABASE_PORT_CONTRACT_VERSION = "seven-database-port/v1"


@dataclass(frozen=True)
class IndexSnapshot:
    name: str
    fields: tuple[str, ...]
    index_type: str
    unique: bool
    sparse: bool

    def semantic_tuple(self) -> tuple[object, ...]:
        return (
            self.name,
            self.index_type,
            self.fields,
            self.unique,
            self.sparse,
        )


@dataclass(frozen=True)
class CollectionSnapshot:
    name: str
    collection_type: str
    indexes: tuple[IndexSnapshot, ...]


class StrictDatabasePort(Protocol):
    """Seven 唯一业务 DB port；只有身份和无副作用读取。"""

    @property
    def database_name(self) -> str: ...

    def inspect_collection(self, name: str) -> CollectionSnapshot | None: ...


class DatabaseCatalogPort(StrictDatabasePort, Protocol):
    """兼容 planner 语义的窄别名；业务依赖名是 StrictDatabasePort。"""
