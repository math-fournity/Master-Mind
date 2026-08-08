"""
DevinCliAdapter：连接12步运行时和真实devin cli实例

替代Mock LLM，让orchestrator的12步循环真正跑起来。

工作方式：turn-by-turn orchestration
  1. 系统给devin cli一个数学问题 → devin -p "问题"
  2. 捕获devin cli的输出（从--export的conversation.json或stdout）
  3. 系统分析状态（StateReducer + StallDetector）
  4. 如果卡住，系统匹配规则、编译hint
  5. 下一turn：devin -p "之前的回答 + hint"（或devin -r恢复session）
  6. 重复2-5直到完成或预算耗尽

对应178-182号全程监控方案 + 136号Phase 6。
"""

import subprocess
import json
import os
import time
import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional, Dict, Any, List


@dataclass
class TurnRecord:
    """单turn记录"""
    turn_id: int
    prompt: str
    response: str
    session_id: str = ""
    timestamp: str = ""
    elapsed_seconds: float = 0.0
    export_path: str = ""
    prompt_hash: str = ""
    response_hash: str = ""
    token_metrics: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "turn_id": self.turn_id,
            "prompt": self.prompt,
            "response": self.response,
            "session_id": self.session_id,
            "timestamp": self.timestamp,
            "elapsed_seconds": self.elapsed_seconds,
            "export_path": self.export_path,
            "prompt_hash": self.prompt_hash,
            "response_hash": self.response_hash,
            "token_metrics": self.token_metrics,
        }


class DevinCliAdapter:
    """
    连接12步运行时和真实devin cli实例。

    每turn调用devin -p，捕获输出，返回给orchestrator。
    可选--export导出完整conversation.json。
    可选--resume恢复之前的session（保持devin cli内部上下文）。

    使用方法：
        adapter = DevinCliAdapter(run_dir="runs/run_001")
        # 第1turn：给数学问题
        response = adapter.send("猜测R_k(C_4)的下界...")
        # 第2turn：给hint
        response = adapter.send("提示：考虑C_4的二部结构...")

    冻结声明（123号§49 + §44）：
    - 模型版本在run期间不变
    - 每turn的--export导出到run_dir
    - session_id从第1turn的导出文件中提取
    """

    # 数学大师Solver的工作目录——独立于Master repo，避免工作系统规则劫持
    # 这些目录有专门的AGENTS.md，只定义Solver角色，禁用web_search
    SOLVER_WORK_DIRS = [
        "/data/math-agent-glm5.2-1",
        "/data/math-agent-glm5.2-2",
        "/data/math-agent-glm5.2-3",
    ]

    def __init__(
        self,
        run_dir: str,
        model: str = "glm-5-2",
        export: bool = True,
        timeout: int = 300,
        work_dir: Optional[str] = None,
    ):
        """
        Args:
            run_dir: run目录路径（存放conversation.json等，在Master repo内）
            model: devin cli模型
            export: 是否使用--export导出conversation.json
            timeout: 单turn超时秒数
            work_dir: devin cli的工作目录（Solver的AGENTS.md所在目录）
                      如果为None，自动选择第一个可用的SOLVER_WORK_DIRS
        """
        self.run_dir = run_dir
        self.model = model
        self.export = export
        self.timeout = timeout
        self.turn_count = 0
        self.session_id: Optional[str] = None
        self.turn_history: List[TurnRecord] = []

        # 确保run目录存在
        os.makedirs(run_dir, exist_ok=True)

        # 选择Solver工作目录
        if work_dir:
            self.work_dir = work_dir
        else:
            # 自动选择第一个存在的目录
            self.work_dir = self.SOLVER_WORK_DIRS[0]
            for d in self.SOLVER_WORK_DIRS:
                if os.path.isdir(d) and os.path.exists(os.path.join(d, "AGENTS.md")):
                    self.work_dir = d
                    break

    def send(self, prompt: str, is_hint: bool = False) -> TurnRecord:
        """
        发送prompt到devin cli，返回turn记录。

        Args:
            prompt: 发送给devin cli的prompt
            is_hint: 是否是hint turn（影响prompt构造方式）

        Returns:
            TurnRecord包含response、session_id、metrics等
        """
        self.turn_count += 1
        turn_id = self.turn_count

        # 构造devin cli命令
        # export路径必须是绝对路径——因为devin cli的cwd是work_dir（外部目录），不是run_dir
        export_path = os.path.abspath(os.path.join(self.run_dir, f"turn_{turn_id}_conversation.json"))

        cmd = ["devin", "-p", prompt, "--model", self.model, "--respect-workspace-trust", "false",
               "--permission-mode", "dangerous"]

        if self.export:
            cmd.extend(["--export", export_path])

        # 如果有session_id且不是第1turn，尝试resume
        # 注意：-r和-p的组合行为需要验证，暂不使用
        # if self.session_id:
        #     cmd.extend(["-r", self.session_id])

        # 执行——在Solver工作目录中运行devin cli
        start = time.time()
        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=self.timeout,
                cwd=self.work_dir,
            )
            elapsed = time.time() - start
        except subprocess.TimeoutExpired:
            elapsed = time.time() - start
            record = TurnRecord(
                turn_id=turn_id,
                prompt=prompt,
                response="[TIMEOUT]",
                timestamp=datetime.now(timezone.utc).isoformat(),
                elapsed_seconds=elapsed,
                export_path=export_path if self.export else "",
            )
            self.turn_history.append(record)
            return record

        response_text = result.stdout.strip()
        if result.returncode != 0:
            response_text = f"[ERROR returncode={result.returncode}] {result.stderr[:200]}\n{response_text}"

        # 从export文件提取session_id和metrics
        session_id = ""
        token_metrics = {}
        if self.export and os.path.exists(export_path):
            try:
                with open(export_path) as f:
                    conv = json.load(f)
                session_id = conv.get("session_id", "")
                token_metrics = conv.get("final_metrics", {})
                # 第1turn提取session_id
                if turn_id == 1 and session_id:
                    self.session_id = session_id
            except (json.JSONDecodeError, IOError):
                pass

        # 构造turn记录
        prompt_hash = hashlib.sha256(prompt.encode()).hexdigest()[:16]
        response_hash = hashlib.sha256(response_text.encode()).hexdigest()[:16]

        record = TurnRecord(
            turn_id=turn_id,
            prompt=prompt,
            response=response_text,
            session_id=session_id,
            timestamp=datetime.now(timezone.utc).isoformat(),
            elapsed_seconds=elapsed,
            export_path=export_path if self.export else "",
            prompt_hash=prompt_hash,
            response_hash=response_hash,
            token_metrics=token_metrics,
        )
        self.turn_history.append(record)
        return record

    def get_last_response(self) -> str:
        """获取最近一次turn的response"""
        if self.turn_history:
            return self.turn_history[-1].response
        return ""

    def get_total_tokens(self) -> Dict[str, int]:
        """获取所有turn的累计token消耗"""
        total = {"total_prompt_tokens": 0, "total_completion_tokens": 0, "total_cached_tokens": 0, "total_steps": 0}
        for turn in self.turn_history:
            for key in total:
                total[key] += turn.token_metrics.get(key, 0)
        return total

    def save_turn_log(self) -> str:
        """保存所有turn记录到run_dir"""
        log_path = os.path.join(self.run_dir, "turn_log.json")
        with open(log_path, "w") as f:
            json.dump(
                {
                    "run_dir": self.run_dir,
                    "model": self.model,
                    "session_id": self.session_id,
                    "total_turns": len(self.turn_history),
                    "total_tokens": self.get_total_tokens(),
                    "turns": [t.to_dict() for t in self.turn_history],
                },
                f, indent=2, ensure_ascii=False
            )
        return log_path
