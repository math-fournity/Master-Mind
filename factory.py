#!/usr/bin/env python3
"""
自动化工厂脚本

实现系统的完全自动化运行：
1. 动态Worker/Auditor管理
2. 自动任务发现和分配
3. 自我迭代机制
4. 非线性吸收策略
"""

import json
import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
import random

ROOT = Path(__file__).parent
TASKS_FILE = ROOT / "tasks.json"
RUNTIME_DIR = ROOT / "runtime"
CHECKPOINTS_DIR = RUNTIME_DIR / "checkpoints"
AUDIT_DIR = RUNTIME_DIR / "audit_logs"
FACTORY_STATE_FILE = RUNTIME_DIR / "factory_state.json"


class AutomationFactory:
    """自动化工厂：管理Worker/Auditor的生命周期"""
    
    def __init__(self):
        self.state = self.load_state()
        self.tasks = self.load_tasks()
        
    def load_state(self) -> Dict:
        """加载工厂状态"""
        if FACTORY_STATE_FILE.exists():
            with open(FACTORY_STATE_FILE, "r") as f:
                return json.load(f)
        return {
            "workers": {},
            "auditors": {},
            "created_at": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat()
        }
    
    def save_state(self):
        """保存工厂状态"""
        RUNTIME_DIR.mkdir(parents=True, exist_ok=True)
        self.state["last_updated"] = datetime.now().isoformat()
        with open(FACTORY_STATE_FILE, "w") as f:
            json.dump(self.state, f, ensure_ascii=False, indent=2)
    
    def load_tasks(self) -> Dict:
        """加载任务队列"""
        if TASKS_FILE.exists():
            with open(TASKS_FILE, "r") as f:
                return json.load(f)
        return {"version": "1.0", "workers": {}, "tasks": []}
    
    def save_tasks(self):
        """保存任务队列"""
        with open(TASKS_FILE, "w") as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=2)
    
    def discover_tasks_from_schema(self) -> List[Dict]:
        """从schema.json自动发现任务

        优先从 subsection 生成任务；section 没有 subsection 时回退到 section 粒度。
        task_id 从已有最大值+1 开始，避免与已完成任务冲突。
        """
        schema_file = ROOT / "dev-docs" / "原典" / "星平会海" / "schema.json"
        if not schema_file.exists():
            return []

        with open(schema_file, "r", encoding="utf-8") as f:
            schema = json.load(f)

        # 从已有任务中找到最大的 auto.N ID
        existing_auto_ids = []
        for t in self.tasks.get("tasks", []):
            tid = t.get("id", "")
            if tid.startswith("auto."):
                try:
                    existing_auto_ids.append(int(tid[5:]))
                except ValueError:
                    pass
        task_id = max(existing_auto_ids) + 1 if existing_auto_ids else 1

        tasks = []

        for volume in schema.get("volumes", []):
            vol_id = volume["id"]
            vol_title = volume["title"]

            for section in volume.get("sections", []):
                section_id = section["id"]
                section_title = section["title"]
                subsections = section.get("subsections", [])

                if subsections:
                    # 有 subsection：按 subsection 粒度生成任务
                    for subsection in subsections:
                        subsection_id = subsection["id"]
                        subsection_title = subsection["title"]
                        rules_count = len(subsection.get("rules", []))

                        task = {
                            "id": f"auto.{task_id}",
                            "title": f"考据: {subsection_id}",
                            "status": "queued",
                            "assigned_to": None,
                            "priority": "medium",
                            "search_preset": "先搜索",
                            "dependencies": [],
                            "section_id": subsection_id,
                            "rules_count": rules_count,
                            "created_at": datetime.now().isoformat(),
                            "updated_at": datetime.now().isoformat()
                        }

                        tasks.append(task)
                        task_id += 1
                else:
                    # 没有 subsection：按 section 粒度生成任务
                    rules_count = len(section.get("rules", []))
                    total_lines = section.get("end_line", 0) - section.get("start_line", 0) + 1

                    task = {
                        "id": f"auto.{task_id}",
                        "title": f"考据: {section_id}",
                        "status": "queued",
                        "assigned_to": None,
                        "priority": "medium",
                        "search_preset": "先搜索",
                        "dependencies": [],
                        "section_id": section_id,
                        "rules_count": rules_count,
                        "total_lines": total_lines,
                        "created_at": datetime.now().isoformat(),
                        "updated_at": datetime.now().isoformat()
                    }

                    tasks.append(task)
                    task_id += 1

        return tasks
    
    def discover_tasks_from_text(self) -> List[Dict]:
        """从文本文件自动发现任务（非线性策略）"""
        text_dir = ROOT / "dev-docs" / "原典" / "星平会海"
        
        # 非线性策略：随机打乱卷的顺序
        volumes = list(range(1, 11))
        random.shuffle(volumes)
        
        tasks = []
        task_id = 1
        
        for vol_num in volumes:
            file_path = text_dir / f"卷{vol_num}.txt"
            if not file_path.exists():
                continue
            
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            total_lines = len(lines)
            
            # 非线性策略：随机选择起始行
            if total_lines > 100:
                # 每个卷随机选择3-5个区间
                num_intervals = random.randint(3, 5)
                for _ in range(num_intervals):
                    start_line = random.randint(1, max(1, total_lines - 50))
                    end_line = min(start_line + random.randint(30, 100), total_lines)
                    
                    task = {
                        "id": f"text.{task_id}",
                        "title": f"文本考据: 卷{vol_num} (行{start_line}-{end_line})",
                        "status": "queued",
                        "assigned_to": None,
                        "priority": "medium",
                        "search_preset": "边做边搜索",
                        "dependencies": [],
                        "volume": vol_num,
                        "start_line": start_line,
                        "end_line": end_line,
                        "created_at": datetime.now().isoformat(),
                        "updated_at": datetime.now().isoformat()
                    }
                    
                    tasks.append(task)
                    task_id += 1
            else:
                # 小文件整体处理
                task = {
                    "id": f"text.{task_id}",
                    "title": f"文本考据: 卷{vol_num} (全文)",
                    "status": "queued",
                    "assigned_to": None,
                    "priority": "medium",
                    "search_preset": "先搜索",
                    "dependencies": [],
                    "volume": vol_num,
                    "start_line": 1,
                    "end_line": total_lines,
                    "created_at": datetime.now().isoformat(),
                    "updated_at": datetime.now().isoformat()
                }
                
                tasks.append(task)
                task_id += 1
        
        return tasks
    
    def auto_discover_tasks(self):
        """自动发现任务（合并schema和文本策略）"""
        print("自动发现任务...")

        schema_tasks = self.discover_tasks_from_schema()
        text_tasks = self.discover_tasks_from_text()

        # 合并任务，去重（基于 task ID 和 section_id 双重去重）
        existing_ids = {t["id"] for t in self.tasks["tasks"]}
        existing_section_ids = {t.get("section_id") for t in self.tasks["tasks"] if t.get("section_id")}

        new_tasks = []
        for task in schema_tasks + text_tasks:
            if task["id"] not in existing_ids:
                # 额外检查 section_id 去重（避免对同一 section 生成重复任务）
                sid = task.get("section_id")
                if sid and sid in existing_section_ids:
                    continue
                new_tasks.append(task)
                existing_ids.add(task["id"])
                if sid:
                    existing_section_ids.add(sid)

        self.tasks["tasks"].extend(new_tasks)
        self.save_tasks()

        print(f"发现 {len(new_tasks)} 个新任务")
        print(f"总任务数: {len(self.tasks['tasks'])}")
        
        return new_tasks
    
    def spawn_worker(self, worker_id: str = None) -> str:
        """动态创建Worker"""
        if worker_id is None:
            # 自动生成Worker ID
            existing = set(self.state["workers"].keys())
            i = 1
            while f"W{i}" in existing:
                i += 1
            worker_id = f"W{i}"
        
        # 更新状态
        self.state["workers"][worker_id] = {
            "status": "idle",
            "current_task": None,
            "created_at": datetime.now().isoformat()
        }
        
        # 更新tasks.json
        self.tasks["workers"][worker_id] = {
            "status": "idle",
            "current_task": None
        }
        
        self.save_state()
        self.save_tasks()
        
        print(f"✅ Worker {worker_id} 已创建")
        return worker_id
    
    def spawn_auditor(self, auditor_id: str = None) -> str:
        """动态创建Auditor"""
        if auditor_id is None:
            existing = set(self.state["auditors"].keys())
            i = 1
            while f"A{i}" in existing:
                i += 1
            auditor_id = f"A{i}"
        
        self.state["auditors"][auditor_id] = {
            "status": "idle",
            "current_audit": None,
            "created_at": datetime.now().isoformat()
        }
        
        self.save_state()
        
        print(f"✅ Auditor {auditor_id} 已创建")
        return auditor_id
    
    def assign_task_to_worker(self, worker_id: str, task_id: str):
        """分配任务给Worker"""
        # 查找任务
        task = None
        for t in self.tasks["tasks"]:
            if t["id"] == task_id:
                task = t
                break
        
        if not task:
            print(f"❌ 找不到任务 {task_id}")
            return False
        
        if task["status"] != "queued":
            print(f"❌ 任务 {task_id} 状态不是queued")
            return False
        
        # 分配任务
        task["status"] = "leased"
        task["assigned_to"] = worker_id
        task["updated_at"] = datetime.now().isoformat()
        
        self.tasks["workers"][worker_id]["status"] = "busy"
        self.tasks["workers"][worker_id]["current_task"] = task_id
        
        self.state["workers"][worker_id]["status"] = "busy"
        self.state["workers"][worker_id]["current_task"] = task_id
        
        self.save_tasks()
        self.save_state()
        
        print(f"✅ 任务 {task_id} 已分配给 Worker {worker_id}")
        return True
    
    def start_worker(self, worker_id: str, task_id: str):
        """启动Worker执行任务"""
        # 查找任务信息
        task = None
        for t in self.tasks["tasks"]:
            if t["id"] == task_id:
                task = t
                break
        
        if not task:
            print(f"❌ 找不到任务 {task_id}")
            return
        
        # 构建worker.sh命令
        cmd = [
            "./worker.sh",
            "--worker-id", worker_id,
            "--task-id", task_id,
            "--provider", os.environ.get("MOIRA_AGENT_PROVIDER", "opencode")
        ]
        
        # 添加section_id（如果有）
        if "section_id" in task:
            cmd.extend(["--section-id", task["section_id"]])
        
        # 添加行范围（如果有）
        if "start_line" in task and "end_line" in task:
            cmd.extend(["--start-line", str(task["start_line"]),
                       "--end-line", str(task["end_line"])])
        
        # 启动Worker
        print(f"启动 Worker {worker_id} 执行任务 {task_id}...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Worker {worker_id} 已启动")
        else:
            print(f"❌ Worker {worker_id} 启动失败: {result.stderr}")
    
    def auto_assign_tasks(self):
        """自动分配任务给空闲Worker"""
        # 找到空闲Worker
        idle_workers = [
            wid for wid, info in self.tasks["workers"].items()
            if info["status"] == "idle"
        ]
        
        if not idle_workers:
            print("没有空闲Worker")
            return
        
        # 找到可分配的任务
        queued_tasks = [
            t for t in self.tasks["tasks"]
            if t["status"] == "queued"
        ]
        
        if not queued_tasks:
            print("没有排队任务")
            return
        
        # 分配任务
        for worker_id in idle_workers[:len(queued_tasks)]:
            task = queued_tasks.pop(0)
            self.assign_task_to_worker(worker_id, task["id"])
            self.start_worker(worker_id, task["id"])
    
    def check_completion(self):
        """检查任务完成情况"""
        for worker_id, worker_info in self.state["workers"].items():
            if worker_info["status"] == "busy":
                task_id = worker_info["current_task"]
                
                # 检查tmux会话是否还存在
                session_name = f"worker-{worker_id}"
                result = subprocess.run(
                    ["tmux", "has-session", "-t", session_name],
                    capture_output=True,
                    text=True
                )
                
                if result.returncode != 0:
                    # 会话已结束，检查任务是否完成
                    task = None
                    for t in self.tasks["tasks"]:
                        if t["id"] == task_id:
                            task = t
                            break
                    
                    if task and task["status"] == "leased":
                        # 标记任务完成
                        task["status"] = "completed"
                        task["completed_at"] = datetime.now().isoformat()
                        task["updated_at"] = datetime.now().isoformat()
                        
                        # 释放Worker
                        self.tasks["workers"][worker_id]["status"] = "idle"
                        self.tasks["workers"][worker_id]["current_task"] = None
                        self.state["workers"][worker_id]["status"] = "idle"
                        self.state["workers"][worker_id]["current_task"] = None
                        
                        print(f"✅ 任务 {task_id} 已完成 (Worker {worker_id})")
        
        self.save_tasks()
        self.save_state()
    
    def run_cycle(self):
        """运行一个自动化周期"""
        print(f"\n{'='*60}")
        print(f"自动化周期 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}")
        
        # 1. 检查完成情况
        print("\n1. 检查任务完成情况...")
        self.check_completion()
        
        # 2. 自动分配任务
        print("\n2. 自动分配任务...")
        self.auto_assign_tasks()
        
        # 3. 统计状态
        queued = len([t for t in self.tasks["tasks"] if t["status"] == "queued"])
        leased = len([t for t in self.tasks["tasks"] if t["status"] == "leased"])
        completed = len([t for t in self.tasks["tasks"] if t["status"] == "completed"])
        
        print(f"\n3. 状态统计:")
        print(f"   排队: {queued}")
        print(f"   执行中: {leased}")
        print(f"   已完成: {completed}")
        print(f"   总计: {len(self.tasks['tasks'])}")
        
        return queued > 0 or leased > 0
    
    def run(self, max_cycles: int = 100):
        """运行自动化工厂"""
        print("=" * 60)
        print("启动自动化工厂")
        print("=" * 60)
        
        # 1. 自动发现任务
        self.auto_discover_tasks()
        
        # 2. 动态创建Worker
        num_workers = min(4, len([t for t in self.tasks["tasks"] if t["status"] == "queued"]))
        for i in range(num_workers):
            self.spawn_worker()
        
        # 3. 运行自动化周期
        cycle = 0
        while cycle < max_cycles:
            cycle += 1
            has_work = self.run_cycle()
            
            if not has_work:
                print("\n所有任务已完成！")
                break
            
            # 等待一段时间
            import time
            time.sleep(10)
        
        print("\n" + "=" * 60)
        print("自动化工厂运行结束")
        print("=" * 60)


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="自动化工厂脚本")
    parser.add_argument("--action", choices=["run", "discover", "spawn-worker", "spawn-auditor", "status"],
                       default="run", help="执行动作")
    parser.add_argument("--worker-id", help="Worker ID")
    parser.add_argument("--max-cycles", type=int, default=100, help="最大周期数")
    
    args = parser.parse_args()
    
    factory = AutomationFactory()
    
    if args.action == "run":
        factory.run(args.max_cycles)
    
    elif args.action == "discover":
        factory.auto_discover_tasks()
    
    elif args.action == "spawn-worker":
        factory.spawn_worker(args.worker_id)
    
    elif args.action == "spawn-auditor":
        factory.spawn_auditor()
    
    elif args.action == "status":
        print("工厂状态:")
        print(json.dumps(factory.state, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
