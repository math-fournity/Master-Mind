#!/usr/bin/env python3
"""poc1rev_driver.py — POC-1重审Step1独立提取实例驱动器（自包含）。"""
import json
import select
import subprocess
import sys
import time
from pathlib import Path

CWD = Path("/tmp/p275-1962-poc1rev")
OUT = CWD / "acp_out"
MODEL = "openrouter/stealth/ox-alpha"
EFFORT = "max"
SILENT = 300
MAXRT = 120 * 60
PROMPT_FILE = CWD / "prompt_extract_continue.md"


def send(proc, msg):
    proc.stdin.write((json.dumps(msg) + "\n").encode())
    proc.stdin.flush()


def read_msg(proc, timeout):
    r, _, _ = select.select([proc.stdout], [], [], timeout)
    if not r:
        return None
    line = proc.stdout.readline()
    if not line:
        return None
    try:
        return json.loads(line.decode())
    except json.JSONDecodeError:
        return None


def rpc(proc, method, params, rid, timeout=25):
    send(proc, {"jsonrpc": "2.0", "id": rid, "method": method, "params": params})
    dl = time.time() + timeout
    while time.time() < dl:
        m = read_msg(proc, 5)
        if m is None:
            continue
        if m.get("id") == rid and ("result" in m or "error" in m):
            return m
    return {"error": {"code": -1, "message": f"timeout {method}"}}


def assert_config(proc, sid, cid, value, rid, log):
    for method in ("session/set_config_option", "session/set_config"):
        resp = rpc(proc, method, {"sessionId": sid, "configId": cid, "value": value}, rid)
        if "error" in resp:
            msg = str(resp["error"].get("message", ""))[:200]
            if "method" in msg.lower() or "not found" in msg.lower():
                continue
            return False, {"step": cid, "error": msg}
        opts = resp.get("result", {}).get("configOptions", [])
        cur = next((o.get("currentValue") for o in opts if o.get("id") == cid), None)
        log[f"{cid}_echo"] = {"method": method, "configOptions": opts}
        if cur == value:
            return True, opts
        return False, {"step": cid, "error": f"echo mismatch set={value} echo={cur}"}
    return False, {"step": cid, "error": "no recognized method"}


def main():
    OUT.mkdir(exist_ok=True)
    prompt_text = PROMPT_FILE.read_text()
    stderr_log = open(OUT / "server_stderr.log", "wb")
    proc = subprocess.Popen(["opencode", "acp", "--cwd", str(CWD)],
                            stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                            stderr=stderr_log, bufsize=0)
    result = {"model": MODEL, "effort": EFFORT, "launch_assertions": {}}
    resp = rpc(proc, "initialize", {"protocolVersion": 1, "clientCapabilities": {}}, 1)
    result["protocolVersion"] = resp.get("result", {}).get("protocolVersion")
    resp = rpc(proc, "session/new", {"cwd": str(CWD), "mcpServers": []}, 2)
    sid = resp["result"]["sessionId"]
    result["sessionId"] = sid
    ok, info = assert_config(proc, sid, "model", MODEL, 10, result["launch_assertions"])
    if not ok:
        result["launch_assertions"]["FAILED"] = info
        (OUT / "launch_result.json").write_text(json.dumps(result, indent=2))
        print(f"FATAL model: {info}"); sys.exit(1)
    ok, info = assert_config(proc, sid, "effort", EFFORT, 11, result["launch_assertions"])
    if not ok:
        result["launch_assertions"]["FAILED"] = info
        (OUT / "launch_result.json").write_text(json.dumps(result, indent=2))
        print(f"FATAL effort: {info}"); sys.exit(1)
    (OUT / "launch_result.json").write_text(json.dumps(result, indent=2))
    print(f"[assert] model✓ effort=max✓ session={sid}", flush=True)

    tf = open(OUT / "thoughts.jsonl", "w")
    mf = open(OUT / "messages.jsonl", "w")
    tools_f = open(OUT / "tools.jsonl", "w")

    def dump(f, obj):
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")
        f.flush()

    send(proc, {"jsonrpc": "2.0", "id": 99, "method": "session/prompt",
                "params": {"sessionId": sid,
                           "prompt": [{"type": "text", "text": prompt_text}]}})
    print("[prompt] 已发送", flush=True)
    start = last = time.time()
    counts = {"thought": 0, "message": 0, "tool": 0}
    tools_state = {}
    prompt_response = None
    while True:
        if proc.poll() is not None:
            print("[done] opencode进程已退出", flush=True)
            break
        r, _, _ = select.select([proc.stdout], [], [], 5)
        now = time.time()
        if not r:
            pending = any(s not in ("completed", "error")
                          for s in tools_state.values())
            thr = 600 if pending else SILENT
            if now - last >= thr:
                print(f"[done] 静默{int(now-last)}s", flush=True)
                break
            if now - start >= MAXRT:
                send(proc, {"jsonrpc": "2.0", "method": "session/cancel",
                            "params": {"sessionId": sid}})
                result["cancelled"] = True
                break
            continue
        raw = proc.stdout.readline()
        if not raw:
            break
        last = now
        try:
            msg = json.loads(raw.decode())
        except json.JSONDecodeError:
            continue
        if msg.get("id") == 99 and ("result" in msg or "error" in msg):
            prompt_response = msg
            break
        upd = msg.get("params", {}).get("update", {})
        su = upd.get("sessionUpdate", "")
        ts = round(time.time() - start, 1)
        if su == "agent_thought_chunk":
            dump(tf, {"t": ts, "mid": upd.get("messageId"),
                      "text": upd.get("content", {}).get("text", "")})
            counts["thought"] += 1
        elif su == "agent_message_chunk":
            dump(mf, {"t": ts, "mid": upd.get("messageId"),
                      "text": upd.get("content", {}).get("text", "")})
            counts["message"] += 1
        elif su in ("tool_call", "tool_call_update"):
            tid, st = upd.get("toolCallId"), upd.get("status")
            if tid and st:
                tools_state[tid] = st
            dump(tools_f, {"t": ts, "kind": su, "title": upd.get("title"),
                           "status": st, "toolCallId": tid})
            counts["tool"] += 1
    for f in (tf, mf, tools_f):
        f.close()

    usage = (prompt_response or {}).get("result", {}).get("usage", {})
    ext = (CWD / "独立提取.md").exists()
    result.update({"counts": counts, "usage": usage,
                   "extraction_present": ext,
                   "duration_sec": round(time.time() - start, 1)})
    result["final_status"] = "EXTRACTION_DONE" if ext else "ENDED_NO_EXTRACTION"
    (OUT / "launch_result.json").write_text(json.dumps(result, indent=2))
    print(json.dumps({k: result[k] for k in
                      ("final_status", "counts", "extraction_present")},
                     ensure_ascii=False))
    try:
        send(proc, {"jsonrpc": "2.0", "id": 200, "method": "session/close",
                    "params": {"sessionId": sid}})
    except Exception:
        pass
    proc.terminate()
    return 0


if __name__ == "__main__":
    sys.exit(main())
