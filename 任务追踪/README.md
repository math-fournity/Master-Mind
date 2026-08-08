# 任务追踪 · 工作线关系图（DAG）

> **本文件是`任务追踪/`目录的导航枢纽，记录各任务追踪文档之间的依赖关系。**
>
> **作用**：帮助新进入的AI理解"为什么有这么多任务追踪文档"、"它们之间是什么关系"、"我该从哪个开始读"。
>
> **维护规则**：新增任务追踪文档时，在本文件中登记节点和依赖边。依赖关系变化时更新本文件。

---

## 工作线DAG

```
                    253号检索机制验证（主线）
                    任务追踪/任务追踪.md
                       │
           ┌───────────┴───────────┐
           │                       │
           ▼                       ▼
    VMS-POC验证              Trajectory采集与
    （验证场景）              Solver-harness（实验基础设施）
    任务追踪/                 任务追踪/
    虚拟数学系统VMS-POC验证.md  trajectory采集与solver-harness.md
           │                       │
           └───────────┬───────────┘
                       │
                       ▼
              solver-harness为VMS和253号
              提供trajectory采集能力
```

## 依赖关系详表

| 上游工作线 | 下游工作线 | 依赖关系 | 说明 |
|---|---|---|---|
| 253号检索机制验证 | VMS-POC验证 | 253号需要VMS做超大规模验证 | 253号在单一案例上验证了检索机制可行性，VMS用虚拟数学系统在超大规模基座下验证泛化能力 |
| 253号检索机制验证 | Trajectory采集与solver-harness | 253号需要trajectory数据做实验 | 253号的检索机制验证需要AI的完整trajectory（thinking+tool_calls+results）作为输入 |
| VMS-POC验证 | Trajectory采集与solver-harness | VMS需要solver-harness采集trajectory | VMS的每个阶段都需要让AI解虚拟题并采集完整trajectory，solver-harness是实验基础设施 |
| Trajectory采集与solver-harness | VMS-POC验证 | solver-harness是为VMS打造的 | 用户从VMS工作线出发，发现需要trajectory采集能力，才启动了solver-harness工作线 |

## 工作线详情

### 253号检索机制验证（主线）

- **任务追踪**：`任务追踪/任务追踪.md`
- **目标**：验证"从认知图依赖图中检索Pattern"的检索机制
- **状态**：P0+P1原型验证完成，泛化验证待做
- **关键文档**：258号（检索机制设计）、260号（解析器攻关）、261号（验证状态提升计划）

### VMS-POC验证

- **任务追踪**：`任务追踪/虚拟数学系统VMS-POC验证.md`
- **目标**：用虚拟数学系统（HoTT同构于真实数学）在超大规模基座下验证检索能力
- **状态**：方案设计完成，7阶段全部未开始，前置工作（258号挑战类型分析）待执行
- **关键文档**：257号（进度追踪）、258号（挑战类型分析方案）、`原语化AI数学工程系统设计/07-验证/03-虚拟数学系统POC方案.md`
- **起源**：从253号主线出发——253号验证了单一案例，VMS做超大规模验证

### Trajectory采集与solver-harness

- **任务追踪**：`任务追踪/trajectory采集与solver-harness.md`
- **目标**：搭建完整的trajectory自动采集环境，在tmux中启动devin cli并自动采集所有数据
- **状态**：方案v1完成，实施待做
- **关键文档**：262号（调查结果）、263号（solver-harness方案v1）
- **起源**：从VMS工作线出发——VMS需要让AI解虚拟题并采集完整trajectory，发现现有trajectory采集手段不足（只有step级、无token级、数据散落AI可见），才启动了solver-harness工作线

## 起源链

```
253号检索机制验证
  → 需要超大规模验证场景
  → 启动VMS-POC验证工作线
    → 需要trajectory采集能力
    → 启动Trajectory采集与solver-harness工作线
```

## 如何使用本文件

**新Session的AI进入本repo后**：

1. **先读本文件**——了解有哪些工作线、它们之间是什么关系
2. **根据当前任务选择对应的工作线任务追踪文档**——如果要做VMS，读VMS任务追踪；如果要做solver-harness，读solver-harness任务追踪
3. **理解依赖**——如果上游工作线未完成，可能阻塞当前工作线（如solver-harness未完成会阻塞VMS的trajectory采集）
4. **新增工作线时**——在本文件中登记节点和依赖边
