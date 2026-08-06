#!/usr/bin/env python3
"""一次性脚本：初始化 research_runtime 的 Phase 1-3 ArangoDB collections。

分别调用：
- xishujuzhen.research_runtime.events.migrate.create_event_collections
- xishujuzhen.research_runtime.state_reducer.migrate.create_state_collections
- xishujuzhen.research_runtime.heuristics.migrate.create_heuristics_collections

环境变量通过 .env 设置：ARANGO_DB/ARANGO_USER/ARANGO_PASS/ARANGO_HOST
"""
import os
import sys
import json

# 将项目根目录加入 sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 确保 source .env 后的环境变量已加载
assert os.environ.get("ARANGO_DB") == "xishujuzhen_math_glm52", (
    "请先 source .env，确保 ARANGO_DB=xishujuzhen_math_glm52"
)

from xishujuzhen.research_runtime.events.migrate import create_event_collections
from xishujuzhen.research_runtime.state_reducer.migrate import create_phase2_collections
from xishujuzhen.research_runtime.heuristics.migrate import create_phase3_collections


def main():
    results = {}
    for name, fn in [
        ("events", create_event_collections),
        ("state_reducer", create_phase2_collections),
        ("heuristics", create_phase3_collections),
    ]:
        print(f"=== 初始化 {name} collections ===")
        result = fn()
        results[name] = result
        print(f"  created: {result.get('created', [])}")
        print(f"  skipped: {result.get('skipped', [])}")
        if result.get('failed'):
            print(f"  failed:  {result.get('failed')}")

    print("\n=== 全部完成 ===")
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
