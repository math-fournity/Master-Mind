# 343号 · six/合并到system/方案——system成为自包含的第六代系统

**日期**：2026-08-11
**状态**：方案设计（基于git log和文件时间线调查）
**来源**：用户决策"倾向于合并six到system，不再维护six，尤其是system中有docs目录" + "system本身应该是自包含的第六代系统：从代码到文档，到运行时（runtime）"

---

## 1. 调查——git log时间线

### 1.1 six/的时间线

| 日期 | commit | 内容 |
|---|---|---|
| 2026-08-10 | f09fe1f | six/目录创建——第六代AI数学系统架构代码 |
| 2026-08-10 | 20fd546 | six/references.py——研发文档索引（晾衣架） |
| 2026-08-10 | be33130 | six/principles.py——解放思想设计原则 |
| 2026-08-10 | f37facb | six/reflection.py——反射设计原则 |
| 2026-08-10 | 07530ff | six/prompts.py——提示词是核心资产 |
| 2026-08-10 | 093a237 | six/types.py——VMS-28验证成功+V5提示词 |
| 2026-08-10 | b74755d | six/types.py——330号双轨术语落地 |
| 2026-08-10 | 6309a71 | six/verify_lattice_completeness.py——VMS-28c机械化过程描述 |
| 2026-08-10 | 9f14e4d | six/pipes.py——V8改进（VMS-28d） |
| 2026-08-10 | ff81103 | six/pipes.py + verify_lattice——V9改进（VMS-28e） |
| 2026-08-10 | e783414 | six/pipes.py——4并发方案决定 |
| 2026-08-11 | d320aa2 | git clean——所有six/文件一次性提交 |
| 2026-08-11 | 05cb148 | six/references.py——更新到342号（本次tag前同步） |

**关键发现**：six/的实质内容全部在2026-08-10创建，是VMS-28系列POC验证期间的产物。2026-08-11只有git clean和references.py更新。six/是"签名+docstring"的架构描述代码，从未被system/的运行代码import。

### 1.2 system/的时间线

| 日期 | commit | 内容 |
|---|---|---|
| 2026-08-10 | 83f9985 | system/目录开始有.ref文件 |
| 2026-08-11 | 1ce9ea6 | **system/vein_analysis.py——真正的运行代码** |
| 2026-08-11 | d320aa2 | git clean——system/__init__.py/schema.py/enter.py/solve.py等 |
| 2026-08-11 | 224d22a | **建立system/docs/目录**——系统设计说明书按模块组织 |
| 2026-08-11 | daa90c1 | 实现三阶段架构——格化与trace识别分离 |
| 2026-08-11 | e6bf36b | AGENTS模板内化——4个版本的AGENTS.md更新 |
| 2026-08-11 | a8977e5 | 数据库记录抓手 + IMO 2009 P6测试通过 |
| 2026-08-11 | 974470e | system/docs/vein_analysis.md——脉络分析模块设计说明书 |
| 2026-08-11 | 43071f0 | 336号——综合分析4阶段文件拆分 |
| 2026-08-11 | ab86de4 | 340+341号——超时降级+滚动日志 |
| 2026-08-11 | 4b055c0 | 342号——系统时间意识 |
| 2026-08-11 | 105fdc1 | 0013全管线运行验证通过 |

**关键发现**：system/的运行代码从2026-08-11才开始创建，但已经完全超越了six/的架构描述——system/有真正的运行实现（vein_analysis.py 1700+行），有数据库（db.py），有日志（log.py），有运行时资产（assets/中的AGENTS模板），有设计文档（docs/），有测试（tests/）。

### 1.3 AGENTS.md中早已写明的合并计划

AGENTS.md第223行（2026-08-11 d320aa2提交）：
> "与six/的关系：six/是架构描述代码（签名+docstring），system/是真正的物理实现。开始写system/代码时，six/是参考依据。**后续会逐步放弃six/目录，完全转入system/目录**——six/中的架构描述会被system/中的真正实现取代，最终six/不再被维护。"

**合并是计划内的，不是临时决定。**

---

## 2. system/是自包含的第六代系统

**定位**（需记录到AGENTS.md）：system/是自包含的第六代系统——从代码到文档，到运行时。

### 2.1 system/的三层结构

| 层 | 目录 | 内容 | 性质 |
|---|---|---|---|
| **代码层** | `*.py` + `.ref` + `.ai-check` | 真正运行的代码 + 文档引用 + 审计清单 | 代码 |
| **文档层** | `docs/` | 模块设计说明书（架构、接口、数据流、设计决策） | 文档 |
| **运行时层** | `assets/` | AGENTS模板、提示词模板——运行时复制到工作目录给AI Agent用 | 运行时资产 |

### 2.2 运行时实例

每次运行时，system/的代码会在`palyground/absorb/vein_analysis/{run_id}_{problem_id}/`下创建运行时实例：
- `phase1_grading/V5/AGENTS.md`——从`assets/vein_analysis/AGENTS_V5.md`复制
- `phase1_grading/V5/prompt.md`——从提示词积累目录复制
- `phase1_grading/V5/input.md`——解答文本
- `phase1_grading/V5/output.json`——AI产出
- `phase1_grading/V5/DONE.md`——完成信号

**这些运行时实例不是system/的一部分**——它们是system/运行时的产物，在palyground/中，.gitignore忽略。但它们的模板在system/assets/中。

---

## 3. six/各文件详细审查——基于git log和内容分析

### 3.1 verify_lattice_completeness.py——运行代码，移入system/

| 属性 | 值 |
|---|---|
| 创建时间 | 2026-08-10 (6309a71) |
| 最后修改 | 2026-08-10 (ff81103, V9三层验证) |
| 被谁调用 | system/vein_analysis.py中`VERIFY_SCRIPT = "six/verify_lattice_completeness.py"` |
| 状态 | **运行代码**，502行，被vein_analysis.py作为外部脚本调用 |
| 价值 | 高——唯一被运行代码调用的six/文件 |
| 去向 | → system/verify_lattice_completeness.py |
| 配套 | 新建system/verify_lattice_completeness.ref + .ai-check |

### 3.2 references.py——研发文档索引，转成docs

| 属性 | 值 |
|---|---|
| 创建时间 | 2026-08-10 (20fd546) |
| 最后修改 | 2026-08-11 (05cb148, 更新到342号) |
| 内容 | DOCS（303-342号文档清单）+ TYPE_REFS + POCS + CORE_PROBLEMS + FUNDAMENTAL_INSIGHT + THREE_PHASE_ARCHITECTURE + FILE_STAGED_FLOW + VEIN_ANALYSIS_AUDIT + TIMEOUT_DEGRADATION + SYSTEM_LOGGING + SYSTEM_TIMING |
| 状态 | **有价值**，刚更新到342号，是最完整的研发文档索引 |
| 过时部分 | TYPE_REFS中引用`six/types.py`需要改为`system/schema.py` |
| 去向 | → system/docs/references.md（转成md格式） |

### 3.3 types.py——dataclass过时，FCA对应说明有价值

| 属性 | 值 |
|---|---|
| 创建时间 | 2026-08-10 (f09fe1f) |
| 最后实质修改 | 2026-08-10 (b74755d, 330号双轨术语) |
| 内容 | 16个dataclass定义，docstring中有FCA对应说明 |
| 状态 | **dataclass过时**——system/schema.py已有更完整的dataclass（多了AnalysisInput/AnalysisOutput/MatchInput等） |
| 有价值部分 | docstring中的FCA对应说明（Segment=对象g∈G、LevelView=形式概念(A,B)等）——system/schema.py没有这些 |
| 去向 | FCA对应说明提取到system/docs/schema.md；删除dataclass |

### 3.4 pipes.py——函数全是NotImplementedError，验证历史有价值

| 属性 | 值 |
|---|---|
| 创建时间 | 2026-08-10 (f09fe1f) |
| 最后实质修改 | 2026-08-10 (e783414, 4并发方案) |
| 内容 | 4个Pipe函数 + 步骤5分叉函数，全是`raise NotImplementedError`，docstring记录VMS-28到28e验证历史 |
| 状态 | **函数过时**——全是空实现 |
| 过时部分 | VMS-28验证记录停在V9（实际用V10），4并发方案说V5/V7/V8/V9（实际V5/V7/V8/V10） |
| 有价值部分 | VMS-28到28e的验证历史摘要——记录了提示词从V4→V5→V7→V8→V9的演进和每个版本的验证结果 |
| 去向 | 验证历史摘要到system/docs/architecture.md §Pipe架构和验证历史（修正V9→V10）；删除函数 |

### 3.5 loops.py——完全过时

| 属性 | 值 |
|---|---|
| 创建时间 | 2026-08-10 (f09fe1f) |
| 最后修改 | 2026-08-10（从未实质修改） |
| 内容 | grove_core_loop() + tell_library_growth_loop() + 辅助函数，全是占位实现 |
| 状态 | **完全过时**——system/process_solve.py和system/process_absorb.py是真正的实现 |
| 去向 | 删除 |

### 3.6 principles.py——解放思想设计原则，不过时

| 属性 | 值 |
|---|---|
| 创建时间 | 2026-08-10 (be33130) |
| 最后修改 | 2026-08-10（从未实质修改） |
| 内容 | LIBERATION_PRINCIPLE（多种方式/多个AI/多个子pipe）+ SUBPIPE_EVOLUTION |
| 状态 | **不过时**——系统级设计原则，和实现无关 |
| 去向 | → system/docs/architecture.md §设计原则——解放思想 |

### 3.7 reflection.py——反射设计原则，不过时

| 属性 | 值 |
|---|---|
| 创建时间 | 2026-08-10 (f37facb) |
| 最后修改 | 2026-08-10（从未实质修改） |
| 内容 | REFLECTION_PRINCIPLE + ReflectionPoint + REFLECTION_DISTRIBUTION |
| 状态 | **不过时**——系统级设计原则，和实现无关 |
| 去向 | → system/docs/architecture.md §设计原则——反射 |

### 3.8 prompts.py——PROMPTS清单过时，PROMPT_DESIGN_PRINCIPLE有价值

| 属性 | 值 |
|---|---|
| 创建时间 | 2026-08-10 (07530ff) |
| 最后实质修改 | 2026-08-10 (ff81103, V9) |
| 内容 | PROMPTS清单（7个提示词，停V9）+ PROMPT_DESIGN_PRINCIPLE |
| 状态 | **PROMPTS清单过时**——停V9，实际用V10；提示词完整文本在"第六代系统提示词积累目录/" |
| 有价值部分 | PROMPT_DESIGN_PRINCIPLE——提示词是核心资产的设计认知 |
| 去向 | PROMPT_DESIGN_PRINCIPLE到system/docs/architecture.md §提示词设计认知；PROMPTS清单删除（提示词在提示词积累目录/） |

### 3.9 __init__.py——删除

| 属性 | 值 |
|---|---|
| 创建时间 | 2026-08-10 (f09fe1f) |
| 内容 | 包初始化，导出48个公共接口 |
| 状态 | **过时**——six/不存在后无意义 |
| 去向 | 删除 |

### 3.10 README.md——删除

| 属性 | 值 |
|---|---|
| 创建时间 | 2026-08-10 (f09fe1f) |
| 内容 | six/目录结构说明 |
| 状态 | **过时**——描述six/结构，合并后无意义 |
| 去向 | 删除 |

---

## 4. 合并方案

### 4.1 新建文件

| 文件 | 内容 | 来源 |
|---|---|---|
| `system/verify_lattice_completeness.py` | 闭元素枚举+三层验证 | six/verify_lattice_completeness.py原样移入 |
| `system/verify_lattice_completeness.ref` | 文档引用 | 新建——332号POC验证、FCA数学基础 |
| `system/verify_lattice_completeness.ai-check` | 审计清单 | 新建 |
| `system/docs/references.md` | 研发文档索引 | six/references.py转成md，TYPE_REFS中six/types.py→system/schema.py |
| `system/docs/architecture.md` | 系统架构文档 | 合并six/principles.py + reflection.py + prompts.py(PROMPT_DESIGN_PRINCIPLE) + pipes.py(验证历史摘要) + README.md(概述) |
| `system/docs/schema.md` | 数据结构设计说明书 | 新建——system/schema.py的模块文档 + six/types.py的FCA对应说明 |

### 4.2 修改文件

| 文件 | 修改内容 |
|---|---|
| `system/vein_analysis.py` | `VERIFY_SCRIPT = "six/verify_lattice_completeness.py"` → `"system/verify_lattice_completeness.py"` |
| `system/vein_analysis.ref` | 删除所有six/引用，加system/docs/references.md引用 |
| `system/vein_analysis.ai-check` | 如果有six/引用也更新 |
| `system/docs/vein_analysis.md` | §4.1中`six/verify_lattice_completeness.py` → `system/verify_lattice_completeness.py`；§8中`six/references.py` → `system/docs/references.md` |
| `system/docs/README.md` | 加入references.md、architecture.md、schema.md |
| `system/README.md` | 更新目录结构——加入verify_lattice_completeness.py，删除six/引用 |
| `system/schema.ref` | 加入system/docs/schema.md引用 |
| `AGENTS.md` | 见§4.3 |

### 4.3 AGENTS.md更新

1. **第208-231行**（系统代码存放规则节）：
   - 第223行"与six/的关系"整段删除——six/不再存在
   - 加入"system/是自包含的第六代系统"定位——代码层+文档层+运行时层

2. **第647-760行**（第六代系统架构代码节）：
   - 整节重写——从"six/目录是晾衣架"改为"system/是自包含的第六代系统"
   - 设计原则（解放思想+反射）引用改为system/docs/architecture.md
   - 提示词索引引用改为"第六代系统提示词积累目录/"（不再提six/prompts.py）
   - Schema晾衣架表格中six/types.py改为system/schema.py
   - 三处对齐同步（326号）中"six/prompts.py的PROMPTS清单"改为"system/docs/prompts索引（待建）"或直接删除B项（因为提示词积累目录已经是完整索引）

3. **第498行**（Tell分类学文档编号）：
   - 已修正为343号开始

4. **研发过程文档清单**：
   - 加入343号

### 4.4 删除文件

```
six/  （整个目录）
```

---

## 5. 合并后的system/结构

```
system/
├── __init__.py / .ref / .ai-check          # 包初始化
├── README.md                                # 目录规范（更新）
├── TODO.md
├── schema.py / .ref / .ai-check            # 数据结构定义（运行代码）
├── db.py / .ref / .ai-check                # ArangoDB封装
├── db_schema.py / .ref / .ai-check         # 数据库schema
├── log.py / .ref                            # 日志模块（341号）
├── enter.py / .ref / .ai-check             # 入题入口
├── solve.py / .ref / .ai-check             # 解题入口
├── process_absorb.py / .ref / .ai-check    # 解答吸收过程
├── process_solve.py / .ref / .ai-check     # 解题引导过程
├── vein_analysis.py / .ref / .ai-check     # 脉络分析（核心）
├── verify_lattice_completeness.py / .ref / .ai-check  # ← 从six/移入
├── run_imo2009p6_three_phase.py            # 运行脚本
├── run_imo2009p6.py                        # 运行脚本
├── assets/                                  # 运行时资产层
│   └── vein_analysis/
│       ├── AGENTS_V5.md                    # V5的AGENTS模板（运行时复制到工作目录）
│       ├── AGENTS_V7.md
│       ├── AGENTS_V8.md
│       ├── AGENTS_V9.md                    # 保留（历史版本）
│       ├── AGENTS_V10.md
│       └── AGENTS_synthesis.md
├── docs/                                    # 文档层
│   ├── README.md                            # 文档索引
│   ├── architecture.md                      # ← 新建（设计原则+反射+提示词认知+Pipe验证历史）
│   ├── references.md                        # ← 新建（研发文档索引，从references.py转成md）
│   ├── schema.md                            # ← 新建（数据结构设计+FCA对应说明）
│   └── vein_analysis.md                     # 已有（更新six/引用）
├── logs/                                    # 日志目录（341号，.gitignore忽略）
└── tests/                                   # 测试
    └── vein_analysis/
        ├── run_full_pipeline_audit.py      # 338号审计脚本
        ├── run_poc_no_loss.py              # POC验证脚本
        ├── baseline/                       # 基线数据
        └── runs/                           # 历史运行归档
            ├── 0004/
            ├── 0005/
            └── ... 0013/
```

**三层结构明确**：
- **代码层**：`*.py` + `.ref` + `.ai-check`——真正运行的代码
- **文档层**：`docs/`——模块设计说明书
- **运行时层**：`assets/`——AGENTS模板等运行时资产

---

## 6. 实现计划

| 步骤 | 内容 | 文件 |
|---|---|---|
| 1 | 移动verify_lattice_completeness.py到system/ | system/verify_lattice_completeness.py |
| 2 | 创建verify_lattice_completeness.ref和.ai-check | system/verify_lattice_completeness.ref, .ai-check |
| 3 | 修改vein_analysis.py中的VERIFY_SCRIPT路径 | system/vein_analysis.py |
| 4 | 创建system/docs/references.md（从references.py转换） | system/docs/references.md |
| 5 | 创建system/docs/architecture.md（合并principles+reflection+prompts认知+pipes验证历史） | system/docs/architecture.md |
| 6 | 创建system/docs/schema.md（数据结构设计+FCA对应说明） | system/docs/schema.md |
| 7 | 更新system/docs/README.md——加入新文档 | system/docs/README.md |
| 8 | 更新system/docs/vein_analysis.md——six/引用改为system/ | system/docs/vein_analysis.md |
| 9 | 更新system/README.md——目录结构+删除six/引用 | system/README.md |
| 10 | 更新vein_analysis.ref——删除six/引用 | system/vein_analysis.ref |
| 11 | 更新schema.ref——加入docs/schema.md | system/schema.ref |
| 12 | 更新AGENTS.md——system自包含定位+删除six/节+更新Schema表 | AGENTS.md |
| 13 | 删除six/目录 | git rm -r six/ |
| 14 | 验证——vein_analysis导入测试+VERIFY_SCRIPT路径 | python3 -c "from system.vein_analysis import ..." |
| 15 | commit | - |

---

## 7. 风险评估

| 风险 | 等级 | 缓解 |
|---|---|---|
| verify_lattice_completeness.py路径改错导致运行失败 | 低 | 步骤14验证导入 |
| references.py转md丢失信息 | 低 | 保留所有字段内容，只是格式从Python字典转md表格 |
| architecture.md合并后太长 | 中 | 按§分节，加目录 |
| AGENTS.md遗漏six/引用 | 低 | grep检查 |
| schema.md的FCA对应说明和schema.py的字段不一致 | 中 | 仔细核对——schema.py是运行定义，schema.md是设计说明，FCA对应说明标注"设计层面的FCA映射" |
