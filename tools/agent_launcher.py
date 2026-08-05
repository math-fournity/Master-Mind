#!/usr/bin/env python3
"""Provider adapter for MOIRA Worker and Auditor agents."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def build_command(provider: str, prompt_file: Path, export_file: Path | None, mode: str) -> list[str]:
    if provider == "opencode":
        binary = shutil.which("opencode")
        if not binary:
            raise SystemExit("opencode is not installed or not on PATH")
        prompt = prompt_file.read_text(encoding="utf-8")
        return [binary, "run", "--auto", prompt]

    if provider == "devin":
        binary = shutil.which("devin")
        if not binary:
            raise SystemExit("devin is not installed or not on PATH")
        cmd = [binary]
        permission_mode = os.environ.get("MOIRA_DEVIN_PERMISSION_MODE")
        if permission_mode:
            cmd.extend(["--permission-mode", permission_mode])
        config = ROOT / ".devin" / "config.json"
        if config.is_file():
            cmd.extend(["--config", str(config)])
        if export_file is not None:
            ensure_parent(export_file)
            cmd.extend(["--export", str(export_file)])
        if mode == "print":
            cmd.extend(["--print", "--prompt-file", str(prompt_file)])
        else:
            cmd.extend(["--prompt-file", str(prompt_file)])
        return cmd

    raise SystemExit(f"unsupported provider: {provider}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Launch a MOIRA agent through opencode or Devin CLI")
    parser.add_argument("--role", required=True, choices=["worker", "auditor", "master"])
    parser.add_argument("--provider", default=os.environ.get("MOIRA_AGENT_PROVIDER", "opencode"), choices=["opencode", "devin"])
    parser.add_argument("--prompt-file", required=True)
    parser.add_argument("--export-file")
    parser.add_argument("--mode", default=os.environ.get("MOIRA_DEVIN_MODE", "print"), choices=["print", "interactive"])
    args = parser.parse_args()

    prompt_file = Path(args.prompt_file).expanduser().resolve()
    export_file = Path(args.export_file).expanduser().resolve() if args.export_file else None
    if not prompt_file.is_file():
        raise SystemExit(f"prompt file not found: {prompt_file}")

    cmd = build_command(args.provider, prompt_file, export_file, args.mode)
    log_dir = ROOT / "runtime" / "launcher_logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / f"{datetime.now().strftime('%Y%m%dT%H%M%S')}-{args.role}-{args.provider}.json"
    log_file.write_text(
        json.dumps(
            {
                "role": args.role,
                "provider": args.provider,
                "prompt_file": str(prompt_file),
                "export_file": str(export_file) if export_file else None,
                "mode": args.mode,
                "command": cmd[:1] + ["<args-redacted>"],
                "started_at": datetime.now().isoformat(timespec="seconds"),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    return subprocess.run(cmd, cwd=ROOT).returncode


if __name__ == "__main__":
    raise SystemExit(main())
