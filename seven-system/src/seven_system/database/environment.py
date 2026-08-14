"""无默认值、在 client 构造前完成校验的 Arango 环境配置。"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping
from urllib.parse import urlsplit

from .errors import (
    DatabaseConfigurationError,
    DatabaseIdentityError,
    MissingDatabaseEnvironmentError,
)


EXPECTED_DATABASE = "xishujuzhen_math_glm52"
REQUIRED_ENVIRONMENT_KEYS = (
    "ARANGO_HOST",
    "ARANGO_DB",
    "ARANGO_USER",
    "ARANGO_PASS",
)


def _safe_endpoint(value: str) -> str:
    """只接受不携带凭据、path、query 或 fragment 的 HTTP(S) endpoint。"""

    try:
        parsed = urlsplit(value)
        port = parsed.port
    except ValueError:
        raise DatabaseConfigurationError(
            "ARANGO_HOST must be a credential-free HTTP(S) endpoint"
        ) from None
    valid = (
        parsed.scheme in {"http", "https"}
        and parsed.hostname is not None
        and parsed.username is None
        and parsed.password is None
        and parsed.path in {"", "/"}
        and not parsed.query
        and not parsed.fragment
        and port is not None
        and 1 <= port <= 65535
    )
    if not valid:
        raise DatabaseConfigurationError(
            "ARANGO_HOST must be a credential-free HTTP(S) host:port endpoint"
        )
    return value.rstrip("/")


@dataclass(frozen=True)
class DatabaseEnvironment:
    """已经通过固定数据库身份门的连接材料。

    `password` 不参与 repr；调用方若需记录配置只能使用 `redacted()`。
    """

    host: str
    database: str
    username: str
    password: str = field(repr=False)

    @classmethod
    def from_environ(cls, environ: Mapping[str, str]) -> "DatabaseEnvironment":
        missing = tuple(
            key
            for key in REQUIRED_ENVIRONMENT_KEYS
            if not isinstance(environ.get(key), str) or not environ[key].strip()
        )
        if missing:
            raise MissingDatabaseEnvironmentError(missing)

        # 必须在 endpoint/credentials 被传给任何 client factory 之前比较。
        if environ["ARANGO_DB"] != EXPECTED_DATABASE:
            raise DatabaseIdentityError(EXPECTED_DATABASE)

        host = _safe_endpoint(environ["ARANGO_HOST"].strip())
        username = environ["ARANGO_USER"].strip()
        password = environ["ARANGO_PASS"]
        if any(character in username for character in "\r\n\x00"):
            raise DatabaseConfigurationError("ARANGO_USER contains forbidden characters")
        if any(character in password for character in "\r\n\x00"):
            raise DatabaseConfigurationError("ARANGO_PASS contains forbidden characters")

        return cls(
            host=host,
            database=EXPECTED_DATABASE,
            username=username,
            password=password,
        )

    def redacted(self) -> dict[str, str]:
        return {
            "host": self.host,
            "database": self.database,
            "username": self.username,
            "password": "<redacted>",
        }
