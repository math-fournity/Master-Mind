#!/usr/bin/env python3
"""
主控脚本

实现系统的完全自动化运行：
1. 动态Worker/Auditor管理
2. 自动任务发现和分配
3. 自我迭代机制
4. 非线性吸收策略
5. 知识图谱构建
"""

import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
import time
import signal

ROOT = Path(__file__).parent
TASKS_FILE = ROOT / "tasks.json"
RUNTIME_DIR = ROOT / "runtime"
STATE_FILE = RUNTIME_DIR / "master_state.json"
FACTORY_SCRIPT = ROOT / "factory.py"
ITERATION_SCRIPT = ROOT / "self_iteration.py"


class MasterController:
    """主控控制器"""
    
    def __init__(self):
        self.state = self.load_state()
        self.running = True
        
        # 设置信号处理
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
    
    def signal_handler(self, signum, frame):
        """信号处理"""
        print("\n收到停止信号，正在优雅停止...")
        self.running = False
        self.graceful_shutdown()
    
    def load_state(self) -> Dict:
        """加载主控状态"""
        if STATE_FILE.exists():
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return {
            "status": "idle",
            "workers": {},
            "auditors": {},
            "current_cycle": 0,
            "total_discoveries": 0,
            "started_at": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat()
        }
    
    def save_state(self):
        """保存主控状态"""
        RUNTIME_DIR.mkdir(parents=True, exist_ok=True)
        self.state["last_updated"] = datetime.now().isoformat()
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(self.state, f, ensure_ascii=False, indent=2)
    
    def graceful_shutdown(self):
        """优雅停止"""
        print("\n执行优雅停止流程...")
        
        # 1. 停止所有Worker
        print("1. 停止所有Worker...")
        subprocess.run(["python3", FACTORY_SCRIPT, "--action", "status"], capture_output=True)
        
        # 2. 停止所有Auditor
        print("2. 停止所有Auditor...")
        # TODO: 实现Auditor停止
        
        # 3. 保存状态
        print("3. 保存状态...")
        self.save_state()
        
        # 4. 生成停止报告
        print("4. 生成停止报告...")
        self.generate_shutdown_report()
        
        print("优雅停止完成")
    
    def generate_shutdown_report(self):
        """生成停止报告"""
        report = {
            "shutdown_time": datetime.now().isoformat(),
            "shutdown_type": "graceful",
            "final_state": self.state,
            "summary": {
                "total_cycles": self.state["current_cycle"],
                "total_discoveries": self.state["total_discoveries"],
                "workers_used": len(self.state["workers"]),
                "auditors_used": len(self.state["auditors"])
            }
        }
        
        report_file = RUNTIME_DIR / f"shutdown_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        print(f"停止报告已保存: {report_file}")
    
    def run_cycle(self):
        """运行一个周期"""
        self.state["current_cycle"] += 1
        print(f"\n{'='*60}")
        print(f"周期 {self.state['current_cycle']} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}")
        
        # 1. 运行自我迭代
        print("\n1. 运行自我迭代...")
        result = subprocess.run(
            ["python3", ITERATION_SCRIPT, "--action", "iterate"],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        if result.stderr:
            print(f"迭代错误: {result.stderr}")
        
        # 2. 运行工厂
        print("\n2. 运行工厂...")
        result = subprocess.run(
            ["python3", FACTORY_SCRIPT, "--action", "run", "--max-cycles", "1"],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        if result.stderr:
            print(f"工厂错误: {result.stderr}")
        
        # 3. 检查完成情况
        print("\n3. 检查完成情况...")
        result = subprocess.run(
            ["python3", FACTORY_SCRIPT, "--action", "status"],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        
        # 4. 更新统计
        self.update_statistics()
        
        return self.should_continue()
    
    def update_statistics(self):
        """更新统计信息"""
        # 读取tasks.json
        if TASKS_FILE.exists():
            with open(TASKS_FILE, "r", encoding="utf-8") as f:
                tasks_data = json.load(f)
            
            # 统计新发现
            for task in tasks_data.get("tasks", []):
                if task.get("status") == "completed" and "discoveries" in task:
                    self.state["total_discoveries"] += len(task["discoveries"])
        
        self.save_state()
    
    def should_continue(self) -> bool:
        """判断是否应该继续"""
        # 检查是否有排队任务
        if TASKS_FILE.exists():
            with open(TASKS_FILE, "r", encoding="utf-8") as f:
                tasks_data = json.load(f)
            
            queued = len([t for t in tasks_data.get("tasks", []) if t.get("status") == "queued"])
            leased = len([t for t in tasks_data.get("tasks", []) if t.get("status") == "leased"])
            
            if queued > 0 or leased > 0:
                return True
        
        # 检查是否需要探索新维度
        iteration_result = subprocess.run(
            ["python3", ITERATION_SCRIPT, "--action", "status"],
            capture_output=True,
            text=True
        )
        
        if "探索新维度" in iteration_result.stdout:
            return True
        
        return False
    
    def run(self, max_cycles: int = 100):
        """运行主控"""
        print("=" * 60)
        print("启动主控")
        print("=" * 60)
        
        self.state["status"] = "running"
        self.state["started_at"] = datetime.now().isoformat()
        self.save_state()
        
        cycle = 0
        while cycle < max_cycles and self.running:
            if not self.run_cycle():
                print("\n所有任务已完成！")
                break
            
            cycle += 1
            
            # 等待一段时间
            time.sleep(10)
        
        self.state["status"] = "completed"
        self.save_state()
        
        print("\n" + "=" * 60)
        print("主控运行结束")
        print("=" * 60)
    
    def get_status(self) -> Dict:
        """获取状态"""
        return {
            "status": self.state["status"],
            "current_cycle": self.state["current_cycle"],
            "total_discoveries": self.state["total_discoveries"],
            "workers": self.state["workers"],
            "auditors": self.state["auditors"],
            "started_at": self.state["started_at"],
            "last_updated": self.state["last_updated"]
        }


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="主控脚本")
    parser.add_argument("--action", choices=["run", "status", "shutdown"],
                       default="run", help="执行动作")
    parser.add_argument("--max-cycles", type=int, default=100, help="最大周期数")
    
    args = parser.parse_args()
    
    controller = MasterController()
    
    if args.action == "run":
        controller.run(args.max_cycles)
    
    elif args.action == "status":
        status = controller.get_status()
        print("\n主控状态:")
        print(json.dumps(status, ensure_ascii=False, indent=2))
    
    elif args.action == "shutdown":
        controller.graceful_shutdown()


if __name__ == "__main__":
    main()
