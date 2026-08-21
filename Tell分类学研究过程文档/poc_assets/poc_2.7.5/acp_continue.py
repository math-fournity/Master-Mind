#!/usr/bin/env python3
"""
POC-2.7.5 · 1962续传R2 —— opencode ACP客户端
=============================================
架构（与旧v1机械拼接的本质区别）：
- 整理者 = Master Agent本人（已通读round1全部87K thinking，按续传系统handover
  Pipe的8章节标准产出HANDOVER_R1.md）
- 推理者 = 经opencode ACP启动的新推理实例（openrouter/stealth/ox-alpha, effort=max）
- 本脚本只做通信与采集，不做内容整理

可靠性设计：
1. 两步断言（skill §3.8 U1教训：默认落big-pickle、effort默认low）：
   set model → 断言回显currentValue；set effort=max → 断言回显。
   任一失败立即中止，回显原文写入launch_assertions.json。
   方法名兼容探测：session/set_config_option（SDK 0.16.1）/ session/set_config（dev）。
2. 实时trajectory落盘：thought/message/tool三路jsonl逐条追加（防崩溃丢失），
   结束后 opencode export <sessionId> 作兜底副本。
3. 完成检测：prompt response（若返回）或通知流静默30秒；总保险120分钟→cancel。
4. 隔离区：cwd=/tmp/p275-1962-acp（无AGENTS.md祖先链，防止repo上下文污染推理）。
"""

import json
import select
import shutil
import subprocess
import sys
import time
from pathlib import Path

REPO = Path("~/master-mind-glm5.2-worktree")
POC_DIR = REPO / "Tell分类学研究过程文档/poc_assets/poc_2.7.5"
WORKDIR_REPO = POC_DIR / "workdirs/p275-1962"
HANDOVER_FILE = WORKDIR_REPO / "HANDOVER_R1.md"

CWD = Path("/tmp/p275-1962-acp")          # 隔离工作区
OUT = CWD / "acp_out"                      # trajectory落盘
MODEL = "openrouter/stealth/ox-alpha"
EFFORT = "max"
SILENT_DONE_SEC = 30
MAX_RUNTIME_SEC = 120 * 60

PROBLEM_TEXT = (
    "Determine all triples $(a, b, c)$ of positive integers for which "
    "$ab-c$, $bc-a$, and $ca-b$ are powers of $2$.\n\n"
    "Explanation: A power of $2$ is an integer of the form $2^n$, where $n$ "
    "denotes some nonnegative integer."
)


def build_prompt():
    handover = HANDOVER_FILE.read_text()
    return f"""你是一个数学解题专用推理实例。请忽略任何与此任务无关的工作流规范，专注解题。

# 任务背景

前一AI实例在思考本题时被输出上限截断。整理者（主控Agent）已将其全部思考过程
按8章节标准整理为交接文档。你的任务：**基于交接文档继续完成解答**——不要从头
重新探索，优先复用已闭环的论证，补齐剩余缺口，写出最终证明。

# 题目

{PROBLEM_TEXT}

# 交接文档（HANDOVER）

{handover}

# 给你的执行指令

1. 通读上方交接文档，特别是§7（截断卡点）和§8（下一步建议）。
2. 补齐剩余两个证明缺口（两偶一奇Case 3收尾 + 全奇情形一般证明）。
3. 将完整、自足的证明写入当前目录的 proof.md 文件，结尾以 \\boxed{{...}} 给出
   全部解三元组。
4. 可以用Python验证中间计算，但证明本身必须数学自足。
"""


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
    """发送request，读直到拿到匹配id的response（跳过中途通知）。"""
    send(proc, {"jsonrpc": "2.0", "id": rid, "method": method, "params": params})
    deadline = time.time() + timeout
    while time.time() < deadline:
        m = read_msg(proc, 5)
        if m is None:
            continue
        if m.get("id") == rid and ("result" in m or "error" in m):
            return m
        # 通知：丢弃（初始化阶段不采集）
    return {"error": {"code": -1, "message": f"timeout waiting {method}"}}


def assert_config(proc, sid, config_id, value, rid, log):
    """设置config并断言回显。返回(True, 回显)或(False, 错误信息)。"""
    tried = {}
    for method in ("session/set_config_option", "session/set_config"):
        resp = rpc(proc, method, {"sessionId": sid, "configId": config_id,
                                  "value": value}, rid)
        tried[method] = resp
        if "error" in resp:
            err = str(resp["error"].get("message", ""))[:200]
            if "method" in err.lower() or "not found" in err.lower():
                continue  # 方法名不识别，试下一个
            return False, {"step": config_id, "error": err, "tried": list(tried)}
        opts = resp.get("result", {}).get("configOptions", [])
        cur = next((o.get("currentValue") for o in opts if o.get("id") == config_id),
                   None)
        log[f"{config_id}_echo"] = {"method": method, "configOptions": opts}
        if cur == value:
            return True, opts
        return False, {"step": config_id,
                       "error": f"echo mismatch: set={value}, echo={cur}",
                       "tried": list(tried)}
    return False, {"step": config_id, "error": "no recognized method name",
                   "tried": list(tried)}


def main():
    CWD.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)

    prompt_text = build_prompt()
    (OUT / "prompt_sent.txt").write_text(prompt_text)

    stderr_log = open(OUT / "server_stderr.log", "wb")
    proc = subprocess.Popen(
        ["opencode", "acp", "--cwd", str(CWD)],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE,
        stderr=stderr_log, bufsize=0,
    )

    result = {"model": MODEL, "effort_target": EFFORT, "cwd": str(CWD)}

    # ---- initialize ----
    resp = rpc(proc, "initialize",
               {"protocolVersion": 1, "clientCapabilities": {}}, 1)
    pv = resp.get("result", {}).get("protocolVersion")
    print(f"[init] protocolVersion={pv}", flush=True)
    result["protocolVersion"] = pv

    # ---- session/new ----
    resp = rpc(proc, "session/new",
               {"cwd": str(CWD), "mcpServers": []}, 2)
    if "error" in resp:
        print(f"FATAL session/new: {resp['error']}")
        sys.exit(1)
    sid = resp["result"]["sessionId"]
    print(f"[session] {sid}", flush=True)
    result["sessionId"] = sid

    # ---- 两步断言：model → effort ----
    ok, info = assert_config(proc, sid, "model", MODEL, 10,
                             result.setdefault("launch_assertions", {}))
    if not ok:
        result["launch_assertions"]["FAILED"] = info
        (OUT / "launch_result.json").write_text(json.dumps(result, indent=2))
        print(f"FATAL model assertion: {info}")
        proc.terminate()
        sys.exit(1)
    print(f"[assert] model == {MODEL} ✓", flush=True)

    ok, info = assert_config(proc, sid, "effort", EFFORT, 11,
                             result["launch_assertions"])
    if not ok:
        result["launch_assertions"]["FAILED"] = info
        (OUT / "launch_result.json").write_text(json.dumps(result, indent=2))
        print(f"FATAL effort assertion: {info}")
        proc.terminate()
        sys.exit(1)
    print(f"[assert] effort == {EFFORT} ✓", flush=True)
    (OUT / "launch_result.json").write_text(json.dumps(result, indent=2))

    # ---- session/prompt ----
    thought_f = open(OUT / "thoughts.jsonl", "w")
    message_f = open(OUT / "messages.jsonl", "w")
    tools_f = open(OUT / "tools.jsonl", "w")

    def dump(fobj, obj):
        fobj.write(json.dumps(obj, ensure_ascii=False) + "\n")
        fobj.flush()

    send(proc, {"jsonrpc": "2.0", "id": 99, "method": "session/prompt",
                "params": {"sessionId": sid,
                           "prompt": [{"type": "text", "text": prompt_text}]}})
    print("[prompt] 已发送，进入通知采集…", flush=True)

    start = last = time.time()
    counts = {"thought": 0, "message": 0, "tool": 0}
    tools_state = {}
    prompt_response = None
    while True:
        r, _, _ = select.select([proc.stdout], [], [], 5)
        now = time.time()
        if not r:
            # 静默判定：有未完成的工具调用时放宽阈值（长计算不产chunk）
            pending = any(s not in ("completed", "error")
                          for s in tools_state.values())
            threshold = 600 if pending else SILENT_DONE_SEC
            if now - last >= threshold:
                print(f"[done] 通知流静默{int(now - last)}s"
                      f"（pending_tools={sum(pending for _ in [1] if pending)}）"
                      f"→ 判定完成", flush=True)
                break
            if now - start >= MAX_RUNTIME_SEC:
                send(proc, {"jsonrpc": "2.0", "method": "session/cancel",
                            "params": {"sessionId": sid}})
                result["cancelled"] = True
                print("[done] 触达最大时长 → cancel", flush=True)
                break
            continue
        raw = proc.stdout.readline()
        if not raw:
            print("[done] stdout关闭", flush=True)
            break
        last = now
        try:
            msg = json.loads(raw.decode())
        except json.JSONDecodeError:
            continue
        if msg.get("id") == 99 and ("result" in msg or "error" in msg):
            prompt_response = msg
            print(f"[done] prompt response: "
                  f"{str(msg.get('result', msg.get('error')))[:200]}", flush=True)
            break
        upd = msg.get("params", {}).get("update", {})
        su = upd.get("sessionUpdate", "")
        ts = round(time.time() - start, 1)
        if su == "agent_thought_chunk":
            txt = upd.get("content", {}).get("text", "")
            dump(thought_f, {"t": ts, "mid": upd.get("messageId"), "text": txt})
            counts["thought"] += 1
        elif su == "agent_message_chunk":
            txt = upd.get("content", {}).get("text", "")
            dump(message_f, {"t": ts, "mid": upd.get("messageId"), "text": txt})
            counts["message"] += 1
        elif su in ("tool_call", "tool_call_update"):
            tid = upd.get("toolCallId")
            st = upd.get("status")
            if tid and st:
                tools_state[tid] = st
            dump(tools_f, {"t": ts, "kind": su, "title": upd.get("title"),
                           "status": st, "toolCallId": tid})
            counts["tool"] += 1

    for f in (thought_f, message_f, tools_f):
        f.close()

    # ---- 结果判定 ----
    proof_path = CWD / "proof.md"
    proof_exists = proof_path.exists()
    boxed = proof_exists and "\\boxed" in proof_path.read_text()
    result.update({
        "counts": counts,
        "prompt_response": prompt_response,
        "proof_md_in_cwd": proof_exists,
        "boxed_found": boxed,
        "duration_sec": round(time.time() - start, 1),
    })
    status = "COMPLETED" if (proof_exists and boxed) else \
             "ENDED_WITHOUT_PROOF" if proof_exists else "NO_PROOF"
    result["final_status"] = status
    (OUT / "launch_result.json").write_text(json.dumps(result, indent=2))

    # ---- 兜底export + 产物回拷 ----
    exp = subprocess.run(["opencode", "export", sid], capture_output=True,
                         text=True, timeout=120)
    if exp.returncode == 0:
        (OUT / "opencode_export.json").write_text(exp.stdout)
        result["export_saved"] = True
    else:
        result["export_saved"] = False
        result["export_error"] = exp.stderr[:300]
    (OUT / "launch_result.json").write_text(json.dumps(result, indent=2))

    for name in ("proof.md",):
        src = CWD / name
        if src.exists():
            shutil.copy(src, WORKDIR_REPO / f"r2_{name}")

    print(json.dumps({k: result[k] for k in
                      ("final_status", "counts", "boxed_found",
                       "export_saved")}, ensure_ascii=False, indent=2))
    try:
        send(proc, {"jsonrpc": "2.0", "id": 200, "method": "session/close",
                    "params": {"sessionId": sid}})
    except Exception:
        pass
    proc.terminate()
    return 0


if __name__ == "__main__":
    sys.exit(main())
