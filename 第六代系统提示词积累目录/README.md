# 第六代系统提示词积累目录

本目录积累第六代系统的所有提示词。提示词是系统的核心资产（321号），和代码同等重要。

## 目录结构

```
第六代系统提示词积累目录/
├── pipe_0_solver/                     # Pipe 0: Solver AI
│   └── set_A_context_hint/            # 套A：脉络+方向Q
├── pipe_1_parser/                     # Pipe 1: Parser AI
│   ├── step_1_analyze_vein/           # 步骤1：分析脉络
│   ├── step_2_grid_vein/              # 步骤2：格化脉络
│   │   ├── set_A_fca_hassee/          # 套A：用FCA/Hasse图启发
│   │   ├── set_B_pure_intuition/      # 套B：纯直觉，不用FCA
│   │   ├── set_C_example_guided/      # 套C：用具体例子引导
│   │   └── set_D_anti_pattern/        # 套D：用反模式引导
│   └── step_3_identify_traces/        # 步骤3：识别trace
├── pipe_2_telling/                    # Pipe 2: Telling AI
├── pipe_3_guide/                      # Pipe 3: Guide AI
└── step_5_branch/                     # 步骤5分叉
    ├── process_A/                     # 过程A
    └── process_B/                     # 过程B
```

## 命名规则

- **第一层**：Pipe阶段名（如`pipe_1_parser`）
- **第二层**：子pipe名（如`step_2_grid_vein`）——如果没有子pipe，省略这一层
- **第三层**：提示词套名（如`set_A_fca_hassee`）——格式为`set_<编号>_<简短描述>`
- **第四层**：版本文件（如`v1.md`、`v2.md`）+ `README.md`（这套提示词的设计思路）

## 版本 vs 套

- **版本（v1/v2/v3/...）**：同一套提示词的改进——同一设计思路的迭代
- **套（set_A/set_B/...）**：完全不同的提示词设计——用不同思路启发AI做同一件事

## 多套提示词并发（325号设计认知）

同一个Pipe阶段可能有多套提示词，并发给多个AI实例处理同一个输入：

```
同一个输入
  ├── AI实例1 + 套A提示词 → 产出1
  ├── AI实例2 + 套B提示词 → 产出2
  ├── AI实例3 + 套C提示词 → 产出3
  └── AI实例4 + 套D提示词 → 产出4
```

结果的两种流向：
1. **汇总**——取交集/并集/加权平均，得到更完整的产出
2. **各自流向下一个Pipe**——不汇总，各自独立驱动后续流程

## 维护规则

- 新增提示词套时，创建`set_<编号>_<简短描述>/`子目录，包含`README.md`和版本文件
- 改进提示词时，在同一套中新增版本文件（v1→v2→v3），旧版本保留
- 同步更新`six/prompts.py`中的`PROMPTS`清单
- 同步更新AGENTS.md中的提示词积累目录说明
