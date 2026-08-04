#!/usr/bin/env python3
"""user_prompt_submit_hook_math.py —— 每次用户提问时从txt文件读取提醒并注入

用户每次提交消息时触发。从UserPromptSubmit.txt读取提醒内容，
注入到AI上下文。改提醒内容只需编辑txt文件，不用改代码。

模仿星学项目97号文档的v3方案（纯提醒，无硬门禁）。
"""
import sys
import os
import json


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        data = {}
    event = data.get("hook_event_name", "UserPromptSubmit")

    project_dir = os.environ.get("DEVIN_PROJECT_DIR", ".")
    reminder_path = os.path.join(project_dir, "xishujuzhen", "UserPromptSubmit.txt")

    try:
        with open(reminder_path, "r") as f:
            context = f.read().strip()
    except FileNotFoundError:
        context = "[工作系统提醒] 提醒文件UserPromptSubmit.txt未找到，请检查xishujuzhen/目录。"

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": event,
            "additionalContext": context
        }
    }, ensure_ascii=False))
    sys.exit(0)


if __name__ == "__main__":
    main()
