#!/usr/bin/env python3
"""session_start_hook_math.py —— SessionStart + PostCompaction hook

触发时机：Devin session启动时、上下文压缩后
作用：注入认知图统计 + 工作纪律提醒
不影响subagent：SessionStart只注入additionalContext，不block
"""
import sys
import os
import json


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        data = {}
    event = data.get("hook_event_name", "SessionStart")
    project_dir = os.environ.get("DEVIN_PROJECT_DIR", ".")
    stats_text = get_stats_text(project_dir)

    context = f"""[工作系统提醒 · {event}]
本项目使用认知图工作系统（ArangoDB稀疏矩阵）。
{stats_text}
工作纪律：
- 工作前：用 cognition_checkpoint_math.py start --seeds <cog_id> 加载认知
- 工作中：认知落盘到 dev-docs/，新术语追加到词汇表
- 工作结束：commit 后 git post-commit hook 会打印 CP4 检查清单
- 临场脚本：可复用的脚本必须沉淀到 cognition_sdk_math.py"""

    output = {
        "hookSpecificOutput": {
            "hookEventName": event,
            "additionalContext": context,
        }
    }
    print(json.dumps(output))
    sys.exit(0)


def get_stats_text(project_dir):
    try:
        sys.path.insert(0, os.path.join(project_dir, "xishujuzhen"))
        from cognition_sdk_math import CognitionSDK
        sdk = CognitionSDK()
        stats = sdk.get_stats()
        return (f"认知图：{stats['total_units']}个认知单元，"
                f"{stats['total_edges']}条边。")
    except Exception:
        return "（ArangoDB未运行或认知图未初始化，认知加载不可用。如需认知加载，先 docker start arangodb）"


if __name__ == "__main__":
    main()
