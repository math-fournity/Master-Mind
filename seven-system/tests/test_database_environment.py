from __future__ import annotations

import sys
import unittest
from pathlib import Path


SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.database.arango_port import ArangoDatabasePort  # noqa: E402
from seven_system.database.environment import (  # noqa: E402
    DatabaseEnvironment,
    EXPECTED_DATABASE,
)
from seven_system.database.errors import (  # noqa: E402
    CollectionNotAllowedError,
    DatabaseConfigurationError,
    DatabaseConnectionError,
    DatabaseIdentityError,
    MissingDatabaseEnvironmentError,
    SchemaConflictError,
)
from seven_system.database.migration import plan_migration  # noqa: E402


VALID_ENV = {
    "ARANGO_HOST": "http://localhost:8529",
    "ARANGO_DB": EXPECTED_DATABASE,
    "ARANGO_USER": "seven-test-user",
    "ARANGO_PASS": "ultra-secret-seven-password",
}


class _FakeClient:
    def __init__(self) -> None:
        self.db_calls: list[dict[str, object]] = []
        self.database = _FakeDatabase()

    def db(self, name: str, **kwargs: object) -> object:
        self.db_calls.append({"name": name, **kwargs})
        return self.database


class _FakeDatabase:
    def __init__(self, collections: dict[str, object] | None = None) -> None:
        self.driver_calls: list[tuple[str, str]] = []
        self.aql = _FakeAQL()
        self.collections = {} if collections is None else collections

    def has_collection(self, name: str) -> bool:
        self.driver_calls.append(("has_collection", name))
        return name in self.collections

    def collection(self, name: str) -> object:
        self.driver_calls.append(("collection", name))
        return self.collections[name]


class _FakeCollection:
    def __init__(self, indexes: list[dict[str, object]]) -> None:
        self._indexes = indexes

    def properties(self) -> dict[str, object]:
        return {"type": 2}

    def indexes(self) -> list[dict[str, object]]:
        return self._indexes


class _FakeAQL:
    def __init__(self, current_database: str = EXPECTED_DATABASE) -> None:
        self.current_database = current_database
        self.queries: list[str] = []

    def execute(self, query: str) -> object:
        self.queries.append(query)
        return iter((self.current_database,))


class DatabaseEnvironmentTests(unittest.TestCase):
    def test_raw_driver_constructor_is_not_a_public_bypass(self) -> None:
        with self.assertRaises(DatabaseConfigurationError):
            ArangoDatabasePort()

    def test_missing_environment_constructs_zero_clients(self) -> None:
        constructed: list[object] = []

        def factory(**kwargs: object) -> object:
            constructed.append(kwargs)
            return _FakeClient()

        with self.assertRaises(MissingDatabaseEnvironmentError) as raised:
            ArangoDatabasePort.from_environment({}, client_factory=factory)
        self.assertEqual(constructed, [])
        self.assertIn("ARANGO_DB", raised.exception.missing_keys)

    def test_wrong_database_constructs_zero_clients_and_hides_actual_value(self) -> None:
        secret_wrong_database = "wrong-db-with-secret-token"
        environment = {**VALID_ENV, "ARANGO_DB": secret_wrong_database}
        constructed: list[object] = []

        def factory(**kwargs: object) -> object:
            constructed.append(kwargs)
            return _FakeClient()

        with self.assertRaises(DatabaseIdentityError) as raised:
            ArangoDatabasePort.from_environment(
                environment, client_factory=factory
            )
        self.assertEqual(constructed, [])
        self.assertNotIn(secret_wrong_database, str(raised.exception))

    def test_environment_has_no_defaults_and_redacts_password(self) -> None:
        config = DatabaseEnvironment.from_environ(VALID_ENV)
        rendered = repr(config) + str(config.redacted())
        self.assertNotIn(VALID_ENV["ARANGO_PASS"], rendered)
        self.assertEqual(config.redacted()["password"], "<redacted>")
        self.assertEqual(config.database, EXPECTED_DATABASE)

    def test_endpoint_rejects_embedded_credentials_without_leaking_them(self) -> None:
        secret = "endpoint-secret"
        environment = {
            **VALID_ENV,
            "ARANGO_HOST": f"http://user:{secret}@localhost:8529",
        }
        with self.assertRaises(DatabaseConfigurationError) as raised:
            DatabaseEnvironment.from_environ(environment)
        self.assertNotIn(secret, str(raised.exception))

    def test_invalid_password_error_does_not_echo_secret(self) -> None:
        secret = "password-that-must-not-leak\n"
        with self.assertRaises(DatabaseConfigurationError) as raised:
            DatabaseEnvironment.from_environ(
                {**VALID_ENV, "ARANGO_PASS": secret}
            )
        self.assertNotIn(secret.strip(), str(raised.exception))

    def test_valid_environment_constructs_exactly_one_client(self) -> None:
        clients: list[_FakeClient] = []

        def factory(**kwargs: object) -> object:
            self.assertEqual(kwargs, {"hosts": VALID_ENV["ARANGO_HOST"]})
            client = _FakeClient()
            clients.append(client)
            return client

        port = ArangoDatabasePort.from_environment(VALID_ENV, client_factory=factory)
        self.assertEqual(port.database_name, EXPECTED_DATABASE)
        self.assertEqual(len(clients), 1)
        self.assertEqual(clients[0].db_calls[0]["name"], EXPECTED_DATABASE)
        self.assertTrue(clients[0].db_calls[0]["verify"])
        self.assertEqual(
            clients[0].database.aql.queries,
            ["RETURN CURRENT_DATABASE()"],
        )
        self.assertFalse(hasattr(port, "driver"))
        self.assertFalse(hasattr(port, "database"))
        self.assertFalse(hasattr(port, "_migration_create_collection"))
        self.assertFalse(hasattr(port, "_migration_create_index"))

    def test_current_database_mismatch_is_rejected_after_connection(self) -> None:
        client = _FakeClient()
        client.database.aql = _FakeAQL("_system")
        with self.assertRaises(DatabaseIdentityError):
            ArangoDatabasePort.from_environment(
                VALID_ENV,
                client_factory=lambda **kwargs: client,
            )

    def test_driver_failure_does_not_leak_password_or_cause(self) -> None:
        secret = VALID_ENV["ARANGO_PASS"]

        def failing_factory(**kwargs: object) -> object:
            raise RuntimeError(f"driver echoed {secret}")

        with self.assertRaises(DatabaseConnectionError) as raised:
            ArangoDatabasePort.from_environment(
                VALID_ENV,
                client_factory=failing_factory,
            )
        self.assertNotIn(secret, str(raised.exception))
        self.assertIsNone(raised.exception.__cause__)

    def test_unknown_and_unicode_collections_never_reach_driver(self) -> None:
        client = _FakeClient()

        def factory(**kwargs: object) -> object:
            return client

        port = ArangoDatabasePort.from_environment(VALID_ENV, client_factory=factory)
        for collection in (
            "seven_records_v2",
            "ѕeven_records_v1",  # Cyrillic small dze, not ASCII s.
            "seven_records_v1\u200b",
        ):
            with self.subTest(collection=collection):
                with self.assertRaises(CollectionNotAllowedError) as raised:
                    port.inspect_collection(collection)
                self.assertNotIn(collection, str(raised.exception))
        self.assertEqual(client.database.driver_calls, [])

    def test_nonpersistent_user_index_is_not_hidden_from_planner(self) -> None:
        client = _FakeClient()
        client.database = _FakeDatabase(
            {
                "seven_alerts_v1": _FakeCollection(
                    [
                        {
                            "type": "primary",
                            "name": "primary",
                            "fields": ["_key"],
                            "unique": True,
                            "sparse": False,
                        },
                        {
                            "type": "ttl",
                            "name": "unexpected_ttl",
                            "fields": ["expires_at"],
                            "unique": False,
                            "sparse": True,
                        },
                    ]
                )
            }
        )
        port = ArangoDatabasePort.from_environment(
            VALID_ENV,
            client_factory=lambda **kwargs: client,
        )
        with self.assertRaises(SchemaConflictError) as raised:
            plan_migration(port)
        self.assertIn("outside the canonical spec", str(raised.exception))


if __name__ == "__main__":
    unittest.main()
