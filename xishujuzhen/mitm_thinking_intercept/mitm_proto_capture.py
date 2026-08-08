"""mitmproxy addon: 捕获devin cli API的raw protobuf响应，保存到文件。

截获所有ApiServerService的API调用（不只是GetChatMessage），
确保thinking内容不会因为通过其他API返回而遗漏。

关键改进：
- 用response hook（不是responseheaders）确保完整响应体被截获
- 记录所有API URL到api_log.txt用于调试
- Connect streaming协议的响应是分多个HTTP响应返回的
"""
import os
from datetime import datetime
from mitmproxy import http

RAW_DIR = os.environ.get("MITM_RAW_DIR", "/tmp/devin_mitm_raw")
os.makedirs(RAW_DIR, exist_ok=True)

class ProtoCapture:
    def __init__(self):
        self.counter = 0
        self.log = open(os.path.join(RAW_DIR, "capture.log"), "a", buffering=1)
        self.api_log = open(os.path.join(RAW_DIR, "api_log.txt"), "a", buffering=1)
        self.log.write(f"\n=== Capture started at {datetime.now()} ===\n")
        self.api_log.write(f"\n=== API log started at {datetime.now()} ===\n")
        self.api_stats = {}  # api_name → count

    def response(self, flow: http.HTTPFlow):
        """捕获所有ApiServerService API的raw response bytes"""
        url = flow.request.url
        api_name = url.split("/")[-1] if "/" in url else url

        # 记录所有API调用到api_log（不管是否截获）
        self.api_log.write(
            f"{datetime.now().strftime('%H:%M:%S.%f')} | "
            f"{api_name} | "
            f"status={flow.response.status_code} | "
            f"resp_size={len(flow.response.content or b'')} | "
            f"req_size={len(flow.request.content or b'')} | "
            f"content_type={flow.response.headers.get('content-type', '')}\n"
        )
        self.api_log.flush()

        # 只截获ApiServerService的API（包含thinking内容）
        if "ApiServerService" not in url:
            return
        if "seat_manag" in url or "product_anal" in url:
            return

        # 记录API调用统计
        self.api_stats[api_name] = self.api_stats.get(api_name, 0) + 1

        self.counter += 1
        ts = datetime.now().strftime("%H%M%S_%f")
        fname = f"chatmsg_{self.counter:03d}_{ts}.bin"
        fpath = os.path.join(RAW_DIR, fname)

        # 保存raw bytes
        content = flow.response.content or b""
        with open(fpath, "wb") as f:
            f.write(content)

        self.log.write(f"\n[{self.counter}] {fname} ({len(content)} bytes)\n")
        self.log.write(f"  url: {url}\n")
        self.log.write(f"  api: {api_name}\n")
        self.log.write(f"  status: {flow.response.status_code}\n")
        self.log.write(f"  content-type: {flow.response.headers.get('content-type', '')}\n")
        self.log.flush()

        # 也保存request body
        req_fname = f"chatmsg_{self.counter:03d}_{ts}_req.bin"
        req_fpath = os.path.join(RAW_DIR, req_fname)
        req_content = flow.request.content or b""
        with open(req_fpath, "wb") as f:
            f.write(req_content)
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
