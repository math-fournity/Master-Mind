"""mitmproxy addon: 流式实时截获devin cli的thinking内容并落盘。

核心机制：
- responseheaders hook在响应头到达时触发，设置flow.response.stream = callable
- 每个HTTP chunk到达时，callable被调用，实时解析Connect streaming protobuf
- 每解析出一个field 9（thinking chunk），立即写入实验目录的mitm/thinking_live.jsonl
- 这是真正的流式实时处理——不需要等响应完成

同时保留原有的response hook用于：
- 保存raw bytes到共享目录（事后分析）
- 记录API调用日志
- 对非GetChatMessage API的完整响应处理

数据落盘位置：
- 共享目录: _shared/mitm_raw/thinking_live.txt（所有实验的thinking流，可tail -f）
- 实验目录: <exp_id>/mitm/thinking_live.jsonl（按实验隔离的JSONL格式）
- 实验目录: <exp_id>/mitm/thinking_live.txt（人类可读格式，可tail -f）
"""
import os
import struct
import json
import time
from datetime import datetime
from mitmproxy import http

RAW_DIR = os.environ.get("MITM_RAW_DIR", "/tmp/devin_mitm_raw")
TRAJECTORY_BASE = os.environ.get("MITM_TRAJECTORY_BASE", "/data/grove-agents-trajectory")
os.makedirs(RAW_DIR, exist_ok=True)


# ============================================================
# protobuf解码（内联，避免import依赖）
# ============================================================

def _decode_varint(data, pos):
    result = 0
    shift = 0
    while pos < len(data):
        byte = data[pos]
        result |= (byte & 0x7F) << shift
        shift += 7
        pos += 1
        if not (byte & 0x80):
            break
    return result, pos

def _decode_protobuf(data):
    """解码protobuf message，返回[(field_num, type_name, value), ...]"""
    pos = 0
    results = []
    while pos < len(data):
        try:
            tag, pos = _decode_varint(data, pos)
            field_num = tag >> 3
            wire_type = tag & 0x07
            if wire_type == 0:
                value, pos = _decode_varint(data, pos)
                results.append((field_num, "varint", value))
            elif wire_type == 1:
                value = struct.unpack('<Q', data[pos:pos+8])[0]
                pos += 8
                results.append((field_num, "64bit", value))
            elif wire_type == 2:
                length, pos = _decode_varint(data, pos)
                if pos + length > len(data):
                    break
                value = data[pos:pos+length]
                pos += length
                try:
                    text = value.decode('utf-8')
                    if all(c.isprintable() or c in '\n\r\t' for c in text[:50]):
                        results.append((field_num, "string", text))
                    else:
                        nested = _decode_protobuf(value)
                        results.append((field_num, "message", nested))
                except:
                    try:
                        nested = _decode_protobuf(value)
                        results.append((field_num, "message", nested))
                    except:
                        results.append((field_num, "bytes", value.hex()[:100]))
            elif wire_type == 5:
                value = struct.unpack('<I', data[pos:pos+4])[0]
                pos += 4
                results.append((field_num, "32bit", value))
            else:
                break
        except:
            break
    return results


# ============================================================
# 流式Connect protocol解析器
# ============================================================

class StreamingThinkingParser:
    """流式解析Connect streaming protocol，实时提取thinking chunks。

    每个envelope: 1 byte flags + 4 bytes length (big-endian) + protobuf message
    thinking在protobuf field 9中（string类型，逐token流式）

    用法：
        parser = StreamingThinkingParser(exp_id, counter, log, thinking_log)
        flow.response.stream = parser.feed  # 每个chunk调用parser.feed
        # 流结束时parser.feed(b"")被调用
    """

    def __init__(self, exp_id, counter, api_name, log, thinking_log, shared_thinking_log):
        self.exp_id = exp_id
        self.counter = counter
        self.api_name = api_name
        self.log = log
        self.thinking_log = thinking_log
        self.shared_thinking_log = shared_thinking_log

        self.buffer = b""
        self.raw_accum = b""  # 累积所有raw bytes（用于事后保存）
        self.thinking_chunks = []
        self.tool_call_chunks = {}
        self.tool_call_order = []
        self.current_tc_id = None
        self.envelope_count = 0
        self.ts_start = datetime.now()

        # 实验目录的落盘路径
        self.exp_jsonl_path = None
        self.exp_txt_path = None
        self.exp_readable_path = None  # 人可阅读的连续文本
        if exp_id:
            exp_mitm_dir = os.path.join(TRAJECTORY_BASE, exp_id, "mitm")
            os.makedirs(exp_mitm_dir, exist_ok=True)
            self.exp_jsonl_path = os.path.join(exp_mitm_dir, "thinking_live.jsonl")
            self.exp_txt_path = os.path.join(exp_mitm_dir, "thinking_live.txt")
            self.exp_readable_path = os.path.join(exp_mitm_dir, "thinking_readable.txt")

        # 写人可阅读文件的开头标记
        if self.exp_readable_path:
            ts = datetime.now().strftime('%H:%M:%S')
            with open(self.exp_readable_path, "a") as f:
                f.write(f"\n{'='*60}\n")
                f.write(f"[{ts}] === Thinking Round {counter} START ===\n")
                f.write(f"{'='*60}\n")

    def feed(self, data: bytes) -> bytes:
        """mitmproxy调用的stream callable。每个chunk到达时调用。

        返回原始data（不修改转发给client的内容）。
        当data=b""时表示流结束。
        """
        if data:
            self.raw_accum += data
            self.buffer += data
            # 尝试从buffer中解析完整的envelope
            self._parse_buffer()
        else:
            # 流结束——写最终记录
            self._finish()
        return data  # 原样转发给client

    def _parse_buffer(self):
        """从buffer中解析所有完整的envelope。"""
        while len(self.buffer) >= 5:
            flags = self.buffer[0]
            length = struct.unpack('>I', self.buffer[1:5])[0]
            if len(self.buffer) < 5 + length:
                break  # 数据不完整，等下一个chunk
            msg_data = self.buffer[5:5 + length]
            self.buffer = self.buffer[5 + length:]
            self.envelope_count += 1
            self._process_envelope(flags, msg_data)

    def _process_envelope(self, flags, msg_data):
        """解码单个envelope的protobuf，提取thinking/tool_call chunks。"""
        decoded = _decode_protobuf(msg_data)
        for field_num, type_name, value in decoded:
            if field_num == 9 and type_name == "string":
                # thinking/content chunk——立即落盘
                self.thinking_chunks.append(value)
                self._write_thinking_chunk(value)
            elif field_num == 6 and type_name == "message":
                # tool_call chunk
                tc_id = None
                tc_name = ""
                tc_args = ""
                for fn, ft, fv in value:
                    if fn == 1 and ft == "string":
                        tc_id = fv
                    elif fn == 2 and ft == "string":
                        tc_name = fv
                    elif fn == 3 and ft == "string":
                        tc_args = fv
                if tc_id:
                    self.current_tc_id = tc_id
                    if tc_id not in self.tool_call_chunks:
                        self.tool_call_chunks[tc_id] = {"name": "", "args": ""}
                        self.tool_call_order.append(tc_id)
                    self.tool_call_chunks[tc_id]["name"] += tc_name
                    self.tool_call_chunks[tc_id]["args"] += tc_args
                    # tool_call第一个chunk立即落盘
                    self._write_tool_call(tc_id, tc_name, tc_args, is_start=True)
                elif self.current_tc_id:
                    self.tool_call_chunks[self.current_tc_id]["args"] += tc_args
                    # tool_call后续args chunk也落盘
                    self._write_tool_call(self.current_tc_id, "", tc_args, is_start=False)

    def _write_thinking_chunk(self, chunk: str):
        """实时写入单个thinking chunk到落盘文件。"""
        ts = datetime.now().strftime('%H:%M:%S.%f')[:-3]

        # 1. 共享目录的thinking_live.txt（token级碎片，可tail -f）
        self.shared_thinking_log.write(f"[{ts}] #{self.counter} exp={self.exp_id} chunk={len(self.thinking_chunks)} len={len(chunk)}\n")
        self.shared_thinking_log.write(f"  +{chunk}\n")
        self.shared_thinking_log.flush()

        # 2. 实验目录的thinking_live.txt（token级碎片，可tail -f）
        if self.exp_txt_path:
            with open(self.exp_txt_path, "a") as f:
                f.write(f"[{ts}] chunk={len(self.thinking_chunks)} +{chunk}\n")

        # 3. 实验目录的thinking_live.jsonl（JSONL格式，每个chunk一行）
        if self.exp_jsonl_path:
            record = {
                "timestamp": datetime.now().isoformat(),
                "counter": self.counter,
                "chunk_index": len(self.thinking_chunks),
                "type": "thinking_chunk",
                "content": chunk,
            }
            with open(self.exp_jsonl_path, "a") as f:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")

        # 4. 实验目录的thinking_readable.txt（人可阅读的连续文本，实时拼接追加）
        if self.exp_readable_path:
            with open(self.exp_readable_path, "a") as f:
                f.write(chunk)  # 直接追加token，不换行——形成连续文本

    def _write_tool_call(self, tc_id, name, args, is_start):
        """实时写入tool_call chunk到落盘文件。"""
        ts = datetime.now().strftime('%H:%M:%S.%f')[:-3]

        # 共享目录
        label = "START" if is_start else "ARGS"
        self.shared_thinking_log.write(f"[{ts}] #{self.counter} TOOL_{label}: {name}({args[:200]})\n")
        self.shared_thinking_log.flush()

        # 实验目录txt
        if self.exp_txt_path:
            with open(self.exp_txt_path, "a") as f:
                f.write(f"[{ts}] TOOL_{label}: {name}({args[:200]})\n")

        # 实验目录jsonl
        if self.exp_jsonl_path:
            record = {
                "timestamp": datetime.now().isoformat(),
                "counter": self.counter,
                "type": "tool_call_chunk",
                "tool_call_id": tc_id,
                "name": name,
                "args_chunk": args,
                "is_start": is_start,
            }
            with open(self.exp_jsonl_path, "a") as f:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")

        # 人可阅读文件：tool_call用分隔符标记
        if self.exp_readable_path and is_start:
            ts_short = datetime.now().strftime('%H:%M:%S')
            with open(self.exp_readable_path, "a") as f:
                f.write(f"\n\n--- [Tool Call: {name}] [{ts_short}] ---\n")
                if args:
                    f.write(f"args: {args}")
                    f.write("\n---\n")

    def _finish(self):
        """流结束时写最终汇总记录。"""
        thinking_full = "".join(self.thinking_chunks)
        elapsed = (datetime.now() - self.ts_start).total_seconds()

        # 共享目录汇总
        self.shared_thinking_log.write(
            f"[DONE] #{self.counter} exp={self.exp_id} "
            f"envelopes={self.envelope_count} "
            f"thinking_chunks={len(self.thinking_chunks)} "
            f"thinking_total={len(thinking_full)}chars "
            f"tool_calls={len(self.tool_call_chunks)} "
            f"elapsed={elapsed:.1f}s\n"
        )
        self.shared_thinking_log.flush()

        # 实验目录jsonl汇总
        if self.exp_jsonl_path:
            summary = {
                "timestamp": datetime.now().isoformat(),
                "counter": self.counter,
                "type": "stream_complete",
                "exp_id": self.exp_id,
                "envelopes": self.envelope_count,
                "thinking_chunks": len(self.thinking_chunks),
                "thinking_total_length": len(thinking_full),
                "thinking_full": thinking_full,
                "tool_calls": [
                    {"id": tc_id, "name": self.tool_call_chunks[tc_id]["name"],
                     "args": self.tool_call_chunks[tc_id]["args"]}
                    for tc_id in self.tool_call_order
                ],
                "elapsed_seconds": elapsed,
            }
            with open(self.exp_jsonl_path, "a") as f:
                f.write(json.dumps(summary, ensure_ascii=False) + "\n")

        # 人可阅读文件：写结束标记
        if self.exp_readable_path:
            ts = datetime.now().strftime('%H:%M:%S')
            with open(self.exp_readable_path, "a") as f:
                f.write(f"\n\n{'='*60}\n")
                f.write(f"[{ts}] === Thinking Round {self.counter} END ===\n")
                f.write(f"  thinking: {len(thinking_full)} chars, {len(self.thinking_chunks)} chunks\n")
                f.write(f"  tool_calls: {len(self.tool_call_chunks)}\n")
                f.write(f"  elapsed: {elapsed:.1f}s\n")
                f.write(f"{'='*60}\n")

        # capture.log
        self.log.write(
            f"  [STREAM DONE] thinking={len(thinking_full)}chars "
            f"chunks={len(self.thinking_chunks)} "
            f"envelopes={self.envelope_count} "
            f"tool_calls={len(self.tool_call_chunks)} "
            f"elapsed={elapsed:.1f}s\n"
        )
        self.log.flush()


# ============================================================
# 实验匹配：从_req文件中提取work_dir，匹配实验
# ============================================================

def _build_workdir_mapping():
    """构建work_dir → exp_id映射表。"""
    mapping = {}
    try:
        for d in os.listdir(TRAJECTORY_BASE):
            if d == "_shared":
                continue
            info_path = os.path.join(TRAJECTORY_BASE, d, "session_info.json")
            if os.path.exists(info_path):
                try:
                    with open(info_path) as f:
                        info = json.load(f)
                    solver_dir = info.get("solver_dir")
                    if solver_dir:
                        mapping[solver_dir] = d
                except (json.JSONDecodeError, KeyError):
                    pass
    except Exception:
        pass
    return mapping

def _match_exp_from_req(req_content: bytes, workdir_mapping: dict) -> str:
    """从_req文件内容中提取work_dir路径，匹配实验。"""
    try:
        text = req_content.decode("utf-8", errors="replace")
        for work_dir, exp_id in workdir_mapping.items():
            if work_dir in text:
                return exp_id
    except Exception:
        pass
    return None


# ============================================================
# ProtoCapture addon
# ============================================================

class ProtoCapture:
    def __init__(self):
        self.counter = 0
        self.log = open(os.path.join(RAW_DIR, "capture.log"), "a", buffering=1)
        self.api_log = open(os.path.join(RAW_DIR, "api_log.txt"), "a", buffering=1)
        self.thinking_log = open(os.path.join(RAW_DIR, "thinking_live.txt"), "a", buffering=1)
        self.log.write(f"\n=== Capture started at {datetime.now()} ===\n")
        self.api_log.write(f"\n=== API log started at {datetime.now()} ===\n")
        self.thinking_log.write(f"\n=== Thinking live stream started at {datetime.now()} ===\n")
        self.api_stats = {}
        self.workdir_mapping_cache = None
        self.workdir_mapping_time = 0
        # 保存正在流式处理的parser（用于response hook中读取累积的raw bytes）
        self.active_parsers = {}  # flow_id → parser

    def _get_workdir_mapping(self, force_refresh=False):
        """获取work_dir映射表（缓存10秒，可强制刷新）。"""
        now = time.time()
        if force_refresh or self.workdir_mapping_cache is None or (now - self.workdir_mapping_time) > 10:
            self.workdir_mapping_cache = _build_workdir_mapping()
            self.workdir_mapping_time = now
        return self.workdir_mapping_cache

    # ============================================================
    # responseheaders hook：流式实时处理的核心
    # ============================================================

    def responseheaders(self, flow: http.HTTPFlow):
        """响应头到达时触发——在body之前。

        对GetChatMessage响应，设置flow.response.stream = callable，
        实现真正的流式实时thinking解码。
        """
        url = flow.request.url
        api_name = url.split("/")[-1] if "/" in url else url

        # 只对GetChatMessage做流式处理（thinking内容在这类响应中）
        if "ApiServerService" not in url:
            return
        if "GetChatMessage" not in api_name:
            return

        # 匹配实验
        req_content = flow.request.content or b""
        workdir_mapping = self._get_workdir_mapping()
        exp_id = _match_exp_from_req(req_content, workdir_mapping)

        # 匹配失败时强制刷新缓存重试（解决新实验刚启动时缓存过期问题）
        if exp_id is None and len(req_content) > 1000:
            workdir_mapping = self._get_workdir_mapping(force_refresh=True)
            exp_id = _match_exp_from_req(req_content, workdir_mapping)

        # 调试日志：记录匹配过程
        self.log.write(f"\n[DEBUG responseheaders] counter={self.counter+1} req_size={len(req_content)} exp_id={exp_id}\n")
        self.log.flush()

        self.counter += 1
        ts = datetime.now().strftime("%H%M%S_%f")

        # 创建流式解析器
        parser = StreamingThinkingParser(
            exp_id=exp_id,
            counter=self.counter,
            api_name=api_name,
            log=self.log,
            thinking_log=self.thinking_log,
            shared_thinking_log=self.thinking_log,
        )

        # 设置stream callable——每个chunk到达时调用parser.feed
        flow.response.stream = parser.feed

        # 保存parser供response hook使用
        self.active_parsers[id(flow)] = parser

        # 记录到capture.log
        self.log.write(f"\n[{self.counter}] STREAM START {ts} exp={exp_id}\n")
        self.log.write(f"  url: {url}\n")
        self.log.write(f"  api: {api_name}\n")
        self.log.write(f"  status: {flow.response.status_code}\n")
        self.log.flush()

        # 记录到thinking_live.txt
        self.thinking_log.write(f"\n[{self.counter}] === STREAM START {ts} exp={exp_id} ===\n")
        self.thinking_log.flush()

    # ============================================================
    # response hook：响应完成后处理（非流式API + 流式API的收尾）
    # ============================================================

    def response(self, flow: http.HTTPFlow):
        """响应完成后触发。

        对于流式处理的GetChatMessage：parser已经完成了实时解码，
        这里只保存raw bytes和记录API日志。

        对于非流式API：保存完整响应。
        """
        url = flow.request.url
        api_name = url.split("/")[-1] if "/" in url else url

        # 记录API调用日志
        # 对于流式响应，content可能为None——用parser的raw_accum
        parser = self.active_parsers.get(id(flow))
        if parser:
            resp_content = parser.raw_accum
        else:
            resp_content = flow.response.content or b""
        req_content = flow.request.content or b""

        self.api_log.write(
            f"{datetime.now().strftime('%H:%M:%S.%f')} | "
            f"{api_name} | "
            f"status={flow.response.status_code} | "
            f"resp_size={len(resp_content)} | "
            f"req_size={len(req_content)} | "
            f"content_type={flow.response.headers.get('content-type', '')} | "
            f"streamed={parser is not None}\n"
        )
        self.api_log.flush()

        # 只处理ApiServerService的API
        if "ApiServerService" not in url:
            return
        if "seat_manag" in url or "product_anal" in url:
            return

        self.api_stats[api_name] = self.api_stats.get(api_name, 0) + 1

        # 保存raw bytes
        ts = datetime.now().strftime("%H%M%S_%f")
        counter = parser.counter if parser else self.counter
        fname = f"chatmsg_{counter:03d}_{ts}.bin"
        fpath = os.path.join(RAW_DIR, fname)
        with open(fpath, "wb") as f:
            f.write(resp_content)

        # 保存request body
        req_fname = f"chatmsg_{counter:03d}_{ts}_req.bin"
        req_fpath = os.path.join(RAW_DIR, req_fname)
        with open(req_fpath, "wb") as f:
            f.write(req_content)

        if parser:
            # 流式处理已完成——parser已经在responseheaders阶段计数了
            self.log.write(f"  [SAVED] {fname} ({len(resp_content)} bytes)\n")
            self.log.flush()
            # 清理active_parsers
            del self.active_parsers[id(flow)]
        else:
            # 非流式API——记录到capture.log
            self.log.write(f"\n[{counter}] {fname} ({len(resp_content)} bytes)\n")
            self.log.write(f"  url: {url}\n")
            self.log.write(f"  api: {api_name}\n")
            self.log.write(f"  status: {flow.response.status_code}\n")
            self.log.write(f"  content-type: {flow.response.headers.get('content-type', '')}\n")
            self.log.write(f"  request: {req_fname} ({len(req_content)} bytes)\n")
            self.log.flush()

    def done(self):
        """打印API调用统计"""
        if self.api_stats:
            self.log.write(f"\n=== API call stats ===\n")
            for api, count in sorted(self.api_stats.items()):
                self.log.write(f"  {api}: {count}\n")
            self.log.flush()
        self.api_log.write(f"\n=== API stats: {self.api_stats} ===\n")
        self.api_log.flush()

addons = [ProtoCapture()]
