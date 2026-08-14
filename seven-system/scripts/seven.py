#!/usr/bin/env python3
"""无需安装即可使用的 Seven System 统一入口。"""

from __future__ import annotations

import sys
from pathlib import Path


SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.cli import main  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(main())
