"""Seven当前Schema子集的无依赖运行时校验器。

仅实现本目录Schema实际使用的JSON Schema 2020-12关键字。遇到未知关键字
不会据此放宽required/type/const等已声明约束；后续引入复杂Schema时必须扩展
本模块或显式采用完整validator，不能静默声称已校验。
"""

from __future__ import annotations

import re
from typing import Any


def _matches_type(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "null":
        return value is None
    return False


def validate_schema(value: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    errors: list[str] = []
    expected_type = schema.get("type")
    if expected_type is not None:
        allowed = [expected_type] if isinstance(expected_type, str) else expected_type
        if not isinstance(allowed, list) or not any(
            isinstance(item, str) and _matches_type(value, item) for item in allowed
        ):
            return [f"{path}: type mismatch; expected {allowed!r}"]

    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: value does not equal const")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: value is not in enum")

    if isinstance(value, str):
        minimum = schema.get("minLength")
        if isinstance(minimum, int) and len(value) < minimum:
            errors.append(f"{path}: string is shorter than minLength")
        pattern = schema.get("pattern")
        if isinstance(pattern, str) and re.search(pattern, value) is None:
            errors.append(f"{path}: string does not match pattern")

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        minimum = schema.get("minimum")
        if isinstance(minimum, (int, float)) and value < minimum:
            errors.append(f"{path}: number is below minimum")

    if isinstance(value, list):
        minimum = schema.get("minItems")
        maximum = schema.get("maxItems")
        if isinstance(minimum, int) and len(value) < minimum:
            errors.append(f"{path}: array is shorter than minItems")
        if isinstance(maximum, int) and len(value) > maximum:
            errors.append(f"{path}: array is longer than maxItems")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(value):
                errors.extend(validate_schema(item, item_schema, f"{path}[{index}]"))

    if isinstance(value, dict):
        required = schema.get("required", [])
        if isinstance(required, list):
            for key in required:
                if key not in value:
                    errors.append(f"{path}: missing required property {key!r}")
        properties = schema.get("properties", {})
        if isinstance(properties, dict):
            for key, child_schema in properties.items():
                if key in value and isinstance(child_schema, dict):
                    errors.extend(
                        validate_schema(value[key], child_schema, f"{path}.{key}")
                    )
            if schema.get("additionalProperties") is False:
                extras = set(value) - set(properties)
                for key in sorted(extras):
                    errors.append(f"{path}: unexpected property {key!r}")
            additional = schema.get("additionalProperties")
            if isinstance(additional, dict):
                for key in set(value) - set(properties):
                    errors.extend(
                        validate_schema(value[key], additional, f"{path}.{key}")
                    )
    return errors
