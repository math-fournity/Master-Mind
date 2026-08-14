"""Isolated, machine-readable runner for the offline Strict DB contract.

This file is launched with ``python -I -S -B``.  It deliberately constructs
its own import path from ``__file__`` and emits one JSON object only after the
complete fixed suite has run without skips, errors, or failures.
"""

from __future__ import annotations

import io
import json
import sys
import unittest
from pathlib import Path


SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))
sys.path.insert(0, str(SYSTEM_ROOT))

TEST_MODULES = (
    "tests.test_database_environment",
    "tests.test_database_migration",
    "tests.test_database_spec",
)


def _flatten(suite: unittest.TestSuite) -> list[unittest.TestCase]:
    tests: list[unittest.TestCase] = []
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            tests.extend(_flatten(item))
        else:
            tests.append(item)
    return tests


def main() -> int:
    loader = unittest.TestLoader()
    suite = unittest.TestSuite(loader.loadTestsFromName(name) for name in TEST_MODULES)
    test_ids = sorted(test.id() for test in _flatten(suite))
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=0).run(suite)
    payload = {
        "schema_version": "strict-db-controlled-test-result/v1",
        "test_modules": list(TEST_MODULES),
        "test_ids": test_ids,
        "tests_run": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "skipped": len(result.skipped),
        "expected_failures": len(result.expectedFailures),
        "unexpected_successes": len(result.unexpectedSuccesses),
        "successful": result.wasSuccessful(),
    }
    print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
    clean = (
        result.wasSuccessful()
        and result.testsRun == len(test_ids)
        and result.testsRun > 0
        and not result.failures
        and not result.errors
        and not result.skipped
        and not result.expectedFailures
        and not result.unexpectedSuccesses
    )
    return 0 if clean else 1


if __name__ == "__main__":
    raise SystemExit(main())
