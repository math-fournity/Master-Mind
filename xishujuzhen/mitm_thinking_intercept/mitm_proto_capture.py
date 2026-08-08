"""mitmproxy addon: 捕获GetChatMessage的raw protobuf响应，保存到文件"""
import os
from datetime import datetime

RAW_DIR = os.environ.get("MITM_RAW_DIR", "/tmp/devin_mitm_raw")
os.makedirs(RAW_DIR, exist_ok=True)

class ProtoCapture:
    def __init__(self):
        self.counter = 0
        self.log = open(os.path.join(RAW_DIR, "capture.log"), "a", buffering=1)
        self.log.write(f"\n=== Capture started at {datetime.now()} ===\n")
        
    def response(self, flow):
        """捕获GetChatMessage的raw response bytes"""
        url = flow.request.url
        if "GetChatMessage" not in url:
            return
            
        self.counter += 1
        ts = datetime.now().strftime("%H%M%S_%f")
        fname = f"chatmsg_{self.counter:03d}_{ts}.bin"
        fpath = os.path.join(RAW_DIR, fname)
        
        # 保存raw bytes
        content = flow.response.content
        with open(fpath, "wb") as f:
            f.write(content)
        
        self.log.write(f"\n[{self.counter}] {fname} ({len(content)} bytes)\n")
        self.log.write(f"  url: {url}\n")
        self.log.write(f"  status: {flow.response.status_code}\n")
        self.log.write(f"  content-type: {flow.response.headers.get('content-type', '')}\n")
        self.log.flush()
        
        # 也保存request body
        req_fname = f"chatmsg_{self.counter:03d}_{ts}_req.bin"
        req_fpath = os.path.join(RAW_DIR, req_fname)
        with open(req_fpath, "wb") as f:
            f.write(flow.request.content)
        self.log.write(f"  request: {req_fname} ({len(flow.request.content)} bytes)\n")
        self.log.flush()

addons = [ProtoCapture()]
