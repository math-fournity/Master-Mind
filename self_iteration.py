#!/usr/bin/env python3
"""
自我迭代引擎

实现系统的自我迭代机制：
1. 从吸收过程中发现新任务
2. 动态调整吸收策略
3. 非线性多维度吸收
4. 知识图谱构建
"""

import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Set, Tuple
import random
from collections import defaultdict

ROOT = Path(__file__).parent
TASKS_FILE = ROOT / "tasks.json"
RUNTIME_DIR = ROOT / "runtime"
STATE_FILE = RUNTIME_DIR / "iteration_state.json"
KNOWLEDGE_FILE = RUNTIME_DIR / "knowledge_graph.json"
STRATEGY_FILE = RUNTIME_DIR / "absorption_strategy.json"


class KnowledgeGraph:
    """知识图谱：记录已吸收的内容和发现的新概念"""
    
    def __init__(self):
        self.graph = self.load()
    
    def load(self) -> Dict:
        """加载知识图谱"""
        if KNOWLEDGE_FILE.exists():
            with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return {
            "operators": {},  # 算子
            "sets": {},  # 集合
            "propositions": {},  # 命题
            "relations": {},  # 关系
            "concepts": {},  # 概念
            "discovered": [],  # 新发现
            "last_updated": datetime.now().isoformat()
        }
    
    def save(self):
        """保存知识图谱"""
        RUNTIME_DIR.mkdir(parents=True, exist_ok=True)
        self.graph["last_updated"] = datetime.now().isoformat()
        with open(KNOWLEDGE_FILE, "w", encoding="utf-8") as f:
            json.dump(self.graph, f, ensure_ascii=False, indent=2)
    
    def add_operator(self, name: str, definition: Dict):
        """添加算子"""
        self.graph["operators"][name] = {
            "definition": definition,
            "discovered_at": datetime.now().isoformat()
        }
        self.save()
    
    def add_concept(self, name: str, concept_type: str, definition: Dict):
        """添加概念"""
        self.graph["concepts"][name] = {
            "type": concept_type,
            "definition": definition,
            "discovered_at": datetime.now().isoformat()
        }
        self.save()
    
    def add_discovery(self, discovery: Dict):
        """添加新发现"""
        self.graph["discovered"].append({
            **discovery,
            "discovered_at": datetime.now().isoformat()
        })
        self.save()
    
    def get_unknown_concepts(self) -> List[str]:
        """获取未知概念"""
        return [
            name for name, info in self.graph["concepts"].items()
            if info.get("status") == "unknown"
        ]
    
    def get_incomplete_operators(self) -> List[str]:
        """获取未完成的算子"""
        return [
            name for name, info in self.graph["operators"].items()
            if not info.get("complete", False)
        ]


class AbsorptionStrategy:
    """吸收策略：动态调整吸收方式"""
    
    def __init__(self, knowledge: KnowledgeGraph):
        self.knowledge = knowledge
        self.strategy = self.load()
    
    def load(self) -> Dict:
        """加载吸收策略"""
        if STRATEGY_FILE.exists():
            with open(STRATEGY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return {
            "current_phase": "exploration",  # exploration -> deepening -> integration
            "dimensions": {
                "operator": {"priority": 1, "coverage": 0},
                "set": {"priority": 2, "coverage": 0},
                "proposition": {"priority": 3, "coverage": 0},
                "state": {"priority": 4, "coverage": 0},
                "time": {"priority": 5, "coverage": 0},
                "system": {"priority": 6, "coverage": 0}
            },
            "nonlinear_weights": {
                "randomness": 0.3,
                "priority": 0.4,
                "coverage": 0.3
            },
            "iteration_count": 0,
            "last_updated": datetime.now().isoformat()
        }
    
    def save(self):
        """保存吸收策略"""
        RUNTIME_DIR.mkdir(parents=True, exist_ok=True)
        self.strategy["last_updated"] = datetime.now().isoformat()
        with open(STRATEGY_FILE, "w", encoding="utf-8") as f:
            json.dump(self.strategy, f, ensure_ascii=False, indent=2)
    
    def update_phase(self):
        """更新吸收阶段"""
        # 检查各维度覆盖率
        total_coverage = sum(d["coverage"] for d in self.strategy["dimensions"].values())
        avg_coverage = total_coverage / len(self.strategy["dimensions"])
        
        if avg_coverage < 0.3:
            self.strategy["current_phase"] = "exploration"
        elif avg_coverage < 0.7:
            self.strategy["current_phase"] = "deepening"
        else:
            self.strategy["current_phase"] = "integration"
        
        self.save()
    
    def calculate_task_priority(self, task: Dict) -> float:
        """计算任务优先级（非线性）"""
        priority = 0.0
        
        # 1. 基础优先级
        if task.get("priority") == "high":
            priority += 0.4
        elif task.get("priority") == "medium":
            priority += 0.2
        else:
            priority += 0.1
        
        # 2. 维度优先级
        section_id = task.get("section_id", "")
        for dim_name, dim_info in self.strategy["dimensions"].items():
            if dim_name in section_id:
                priority += dim_info["priority"] * 0.1
        
        # 3. 随机性（非线性）
        random_factor = random.random() * self.strategy["nonlinear_weights"]["randomness"]
        priority += random_factor
        
        # 4. 覆盖率权重（优先选择覆盖率低的维度）
        for dim_name, dim_info in self.strategy["dimensions"].items():
            if dim_name in section_id:
                coverage_factor = (1 - dim_info["coverage"]) * self.strategy["nonlinear_weights"]["coverage"]
                priority += coverage_factor
        
        return priority
    
    def update_coverage(self, dimension: str, coverage_delta: float):
        """更新维度覆盖率"""
        if dimension in self.strategy["dimensions"]:
            current = self.strategy["dimensions"][dimension]["coverage"]
            self.strategy["dimensions"][dimension]["coverage"] = min(1.0, current + coverage_delta)
            self.save()
    
    def should_explore_new_dimension(self) -> Tuple[bool, str]:
        """是否应该探索新维度"""
        # 找到覆盖率最低的维度
        min_coverage = 1.0
        target_dim = None
        
        for dim_name, dim_info in self.strategy["dimensions"].items():
            if dim_info["coverage"] < min_coverage:
                min_coverage = dim_info["coverage"]
                target_dim = dim_name
        
        # 如果覆盖率低于阈值，探索新维度
        if min_coverage < 0.2:
            return True, target_dim
        
        return False, None


class SelfIterationEngine:
    """自我迭代引擎"""
    
    def __init__(self):
        self.knowledge = KnowledgeGraph()
        self.strategy = AbsorptionStrategy(self.knowledge)
        self.state = self.load_state()
    
    def load_state(self) -> Dict:
        """加载迭代状态"""
        if STATE_FILE.exists():
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return {
            "iteration_count": 0,
            "discoveries": [],
            "new_tasks_generated": [],
            "last_iteration": datetime.now().isoformat()
        }
    
    def save_state(self):
        """保存迭代状态"""
        RUNTIME_DIR.mkdir(parents=True, exist_ok=True)
        self.state["last_iteration"] = datetime.now().isoformat()
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(self.state, f, ensure_ascii=False, indent=2)
    
    def analyze_absorption_result(self, result: Dict) -> Dict:
        """分析吸收结果，发现新任务"""
        new_tasks = []
        discoveries = []
        
        # 1. 检查新发现的算子
        if "new_operators" in result:
            for op in result["new_operators"]:
                self.knowledge.add_operator(op["name"], op["definition"])
                discoveries.append({
                    "type": "operator",
                    "name": op["name"],
                    "description": f"发现新算子: {op['name']}"
                })
        
        # 2. 检查新发现的概念
        if "new_concepts" in result:
            for concept in result["new_concepts"]:
                self.knowledge.add_concept(
                    concept["name"],
                    concept["type"],
                    concept["definition"]
                )
                discoveries.append({
                    "type": "concept",
                    "name": concept["name"],
                    "description": f"发现新概念: {concept['name']}"
                })
        
        # 3. 检查需要深入研究的内容
        if "need_deepening" in result:
            for item in result["need_deepening"]:
                new_task = {
                    "id": f"deep.{len(new_tasks) + 1}",
                    "title": f"深入研究: {item['topic']}",
                    "status": "queued",
                    "priority": "high",
                    "search_preset": "先搜索",
                    "dependencies": [],
                    "created_at": datetime.now().isoformat(),
                    "updated_at": datetime.now().isoformat(),
                    "source": result.get("source_task_id"),
                    "reason": item.get("reason")
                }
                new_tasks.append(new_task)
        
        # 4. 检查跨体系关联
        if "cross_system_relations" in result:
            for relation in result["cross_system_relations"]:
                self.knowledge.graph["relations"][relation["name"]] = {
                    "definition": relation["definition"],
                    "systems": relation["systems"],
                    "discovered_at": datetime.now().isoformat()
                }
                discoveries.append({
                    "type": "relation",
                    "name": relation["name"],
                    "description": f"发现跨体系关系: {relation['name']}"
                })
        
        # 5. 更新策略
        if "coverage_update" in result:
            for dim, delta in result["coverage_update"].items():
                self.strategy.update_coverage(dim, delta)
        
        self.knowledge.save()
        self.strategy.save()
        
        return {
            "new_tasks": new_tasks,
            "discoveries": discoveries
        }
    
    def generate_nonlinear_tasks(self, count: int = 5) -> List[Dict]:
        """非线性生成新任务"""
        tasks = []
        
        # 策略1：探索新维度
        should_explore, target_dim = self.strategy.should_explore_new_dimension()
        if should_explore and target_dim:
            task = {
                "id": f"explore.{len(tasks) + 1}",
                "title": f"探索新维度: {target_dim}",
                "status": "queued",
                "priority": "high",
                "search_preset": "先搜索",
                "dependencies": [],
                "created_at": datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat(),
                "dimension": target_dim,
                "reason": f"维度 {target_dim} 覆盖率过低，需要探索"
            }
            tasks.append(task)
        
        # 策略2：深化未完成的算子
        incomplete_ops = self.knowledge.get_incomplete_operators()
        for op_name in incomplete_ops[:2]:
            task = {
                "id": f"deepen.{len(tasks) + 1}",
                "title": f"深化算子: {op_name}",
                "status": "queued",
                "priority": "medium",
                "search_preset": "边做边搜索",
                "dependencies": [],
                "created_at": datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat(),
                "operator": op_name,
                "reason": f"算子 {op_name} 定义不完整"
            }
            tasks.append(task)
        
        # 策略3：研究未知概念
        unknown_concepts = self.knowledge.get_unknown_concepts()
        for concept_name in unknown_concepts[:2]:
            task = {
                "id": f"concept.{len(tasks) + 1}",
                "title": f"研究概念: {concept_name}",
                "status": "queued",
                "priority": "medium",
                "search_preset": "先搜索",
                "dependencies": [],
                "created_at": datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat(),
                "concept": concept_name,
                "reason": f"概念 {concept_name} 类型未知"
            }
            tasks.append(task)
        
        # 策略4：随机探索（非线性）
        if len(tasks) < count:
            random_tasks = [
                {
                    "id": f"random.{len(tasks) + 1}",
                    "title": f"随机探索: 第{random.randint(1, 10)}卷",
                    "status": "queued",
                    "priority": "low",
                    "search_preset": "边做边搜索",
                    "dependencies": [],
                    "created_at": datetime.now().isoformat(),
                    "updated_at": datetime.now().isoformat(),
                    "volume": random.randint(1, 10),
                    "reason": "非线性随机探索"
                }
                for _ in range(count - len(tasks))
            ]
            tasks.extend(random_tasks)
        
        return tasks[:count]
    
    def run_iteration(self):
        """运行一次迭代"""
        print(f"\n{'='*60}")
        print(f"自我迭代周期 {self.state['iteration_count'] + 1}")
        print(f"{'='*60}")
        
        # 1. 更新策略阶段
        self.strategy.update_phase()
        print(f"\n当前阶段: {self.strategy.strategy['current_phase']}")
        
        # 2. 生成非线性任务
        new_tasks = self.generate_nonlinear_tasks()
        print(f"\n生成 {len(new_tasks)} 个新任务")
        
        # 3. 保存状态
        self.state["iteration_count"] += 1
        self.state["new_tasks_generated"].extend([
            {"task_id": t["id"], "title": t["title"], "generated_at": datetime.now().isoformat()}
            for t in new_tasks
        ])
        self.save_state()
        
        # 4. 返回新任务
        return new_tasks
    
    def get_status(self) -> Dict:
        """获取迭代状态"""
        return {
            "iteration_count": self.state["iteration_count"],
            "current_phase": self.strategy.strategy["current_phase"],
            "dimensions_coverage": {
                dim: info["coverage"]
                for dim, info in self.strategy.strategy["dimensions"].items()
            },
            "knowledge_stats": {
                "operators": len(self.knowledge.graph["operators"]),
                "concepts": len(self.knowledge.graph["concepts"]),
                "relations": len(self.knowledge.graph["relations"]),
                "discoveries": len(self.knowledge.graph["discovered"])
            },
            "last_iteration": self.state["last_iteration"]
        }


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="自我迭代引擎")
    parser.add_argument("--action", choices=["iterate", "status", "discover"],
                       default="iterate", help="执行动作")
    parser.add_argument("--count", type=int, default=5, help="生成任务数量")
    
    args = parser.parse_args()
    
    engine = SelfIterationEngine()
    
    if args.action == "iterate":
        new_tasks = engine.run_iteration()
        
        # 保存新任务到tasks.json
        tasks_file = ROOT / "tasks.json"
        if tasks_file.exists():
            with open(tasks_file, "r", encoding="utf-8") as f:
                tasks_data = json.load(f)
        else:
            tasks_data = {"version": "1.0", "workers": {}, "tasks": []}
        
        tasks_data["tasks"].extend(new_tasks)
        
        with open(tasks_file, "w", encoding="utf-8") as f:
            json.dump(tasks_data, f, ensure_ascii=False, indent=2)
        
        print(f"\n已保存 {len(new_tasks)} 个新任务到 tasks.json")
    
    elif args.action == "status":
        status = engine.get_status()
        print("\n迭代状态:")
        print(json.dumps(status, ensure_ascii=False, indent=2))
    
    elif args.action == "discover":
        new_tasks = engine.generate_nonlinear_tasks(args.count)
        print(f"\n生成 {len(new_tasks)} 个新任务:")
        for task in new_tasks:
            print(f"  - {task['id']}: {task['title']}")


if __name__ == "__main__":
    main()
