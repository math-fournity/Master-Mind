# 研发文档索引——第六代系统的"晾衣架"

**来源**：从six/references.py转换（343号方案）
**维护规则**：新增研发文档时更新本索引；代码元素变更时更新对应映射

---

## 1. 研发过程文档清单

文档目录：`第六代系统研发过程文档/`

### 从grove repo复制的探索文档（303-309号）

| 编号 | 内容 |
|---|---|
| 303 | 非局部tell——引导树分叉位置的重新理解，脉络上任意点可分叉与非局部tell |
| 304 | FCA与工程方案的对应——形式概念分析为三层Pipe架构提供完备性证明和格遍历算法 |
| 305 | 非局部tell的识别价值——端到端实例（费马大定理/模分析无尽追逐） |
| 306 | 原语化AI数学工程系统设计（从grove repo复制） |
| 307 | 原语化方向（310号评审为跑偏——破坏推理AI独立性） |
| 308 | 亲眼看vms_test_1的thinking（Grove AI识别出PSLQ闭式追逐非局部trace） |
| 309 | trace-tell-hint命名——trace=辅助AI识别产物，tell=库中标准化描述，hint=方向提示 |

### worktree侧产生的文档（310号起）

| 编号 | 内容 |
|---|---|
| 310 | worktree侧对grove侧303-309号文档的评审——判断哪些方向有闪光点、哪些跑偏 |
| 311 | 并发Telling AI方案——Pipe 0简化（粗domain分类）+Pipe 2并行化（多Telling AI并行） |
| 312 | 第六代系统的两个核心问题——Trace识别与Trace→Tell匹配 |
| 313 | Tell分类学研究——建立第六代Tell的分类体系 |
| 314 | 第六代系统必须着力解决的三个问题——非局部tell库缺失/推理脉络格化/Tell分类学 |
| 315 | 第六代系统的完整工作流——从推理AI探索到引导树填充+完备性检查+Parser AI定义+脉络分析管线 |
| 316 | 第六代系统理想化工作过程——规范化完整描述（9个章节） |
| 317 | 第六代系统POC验证方案——20个POC三层组织 |
| 318 | 第六代系统流程Pipe图——Pipe命名与AI命名（Solver/Parser/Telling/Guide） |
| 319 | 第六代系统流程Pipe图——形式化定义（Python代码+dataclass）→原six/目录的源文档 |

### 2026-08-10新增（VMS-28系列POC验证）

| 编号 | 内容 |
|---|---|
| 320 | POC-VMS-28执行方案v0——用V4提示词做第一次POC |
| 321 | 提示词是核心资产——多套提示词并发+三处对齐同步 |
| 322 | V2提示词——FCA和Hasse图启发下的格化+trace识别 |
| 323 | V3提示词——7种反模式+为什么我们要拿trace+影响例子 |
| 324 | V4提示词——树状vs线性输入区分（方案C：基础共用+两个附加章节） |
| 325 | 多套提示词并发——不同提示词set各自验证、各自演进 |
| 326 | 三处对齐同步——A目录/B代码清单/C POC验证文档 |
| 327 | POC-VMS-28执行方案v1——用V4提示词做第一次POC |
| 328 | POC方案自包含标准——POC方案必须自包含、可审计、有来源索引 |
| 329 | POC-VMS-28执行方案v2——自包含版+VMS-28/28b验证结果+V5改进分析 |
| 330 | FCA数学语言类比与第六代系统术语规范化——21个术语的工程→FCA映射+5条规范化建议 |
| 331 | 待处理问题Checklist——A线VMS-28b成果处理+B线330号规范化建议执行 |

### 2026-08-11新增（三阶段架构+工程化）

| 编号 | 内容 |
|---|---|
| 332 | POC-VMS-28c执行方案——机械化过程描述与程序验证完全格化 |
| 333 | 脉络分析Pipe内细化方案——格化与trace识别分离（三阶段架构：格化→程序枚举→综合分析） |
| 334 | 脉络分析新管线审计结果与改进方案——nonlocal trace退化修复+审计维度+历史运行对比 |
| 335 | V8格化session的thinking过大问题分析——保守方案（v1修订：方案D 2步文件拆分，验证不退化） |
| 336 | 综合分析阶段文件拆分流程控制方案——不会退化的4阶段拆分（验证大幅提升：trace 43→88） |
| 337 | 全管线验证计划——格化+综合分析双文件拆分（6个验证维度+通过标准） |
| 338 | 全管线非退化审计方案——各V各阶段历史对比（3层审计+7个历史轮次+文件版本追踪） |
| 339 | 研发资产管理改进方案——从文件版本追踪的痛苦中提炼（run_manifest.json+4层保证） |
| 340 | 子管线超时降级方案——不卡住整个系统（独立超时+至少1个通过即可+数据库记录+入口返回值） |
| 341 | 全流程日志方案——滚动日志到system/logs/（单文件1MB+目录500MB+循环滚动） |
| 342 | 系统时间意识方案——全管线全子管线运行时间记录（3层时间记录+数据库timing字段+耗时摘要） |
| 343 | six/合并到system/方案——system成为自包含的第六代系统（代码层+文档层+运行时层，终止six/维护） |

---

## 2. 代码元素到研发文档的映射

### 基础数据结构（system/schema.py）

| 代码位置 | 定义来源 | 关键字段来源 |
|---|---|---|
| `schema.py` → `Problem` | 第五代01-基础概念/04-两棵树.md | 无变化，继承第五代 |
| `schema.py` → `Hint` | 000号文档（引导树闭环-识别端结构定义） | hint_level→第五代03-hint端/02-hint的Level梯度.md；tell_id→315号§5阶段6 |
| `schema.py` → `Tell` | 000号文档（tell的四个成分） | branch_signal/branch_type/unexplored_diagnosis/direction_matching→000号；domain/trace_type/segment_pattern/specific_concept→313号§4.1；去特化→287号；存储方式→315号§4.1 |
| `schema.py` → `Trace` | 309号——trace-tell-hint命名 | level→314号问题2；trace_type→313号§4.1；is_branch_position→315号§6.2.2；全Level Trace→317号VMS-27 |
| `schema.py` → `MathSituation` | 第五代01-基础概念/04-两棵树.md | node_type→第五代root/internal/leaf_success/leaf_deadend/leaf_truncated |
| `schema.py` → `TreeEdge` | 第五代01-基础概念/04-两棵树.md | level→315号§1阶段8/316号§2.4；POC验证→317号VMS-26 |
| `schema.py` → `Thinking` | 第五代01-基础概念/03-引导树闭环.md | entry_hint→315号§5 |
| `schema.py` → `SolutionRecord` | 315号§6.2.1 | is_verified→315号§6.2.1 |

### 脉络相关数据结构（system/schema.py）

| 代码位置 | 定义来源 | 关键字段来源 |
|---|---|---|
| `schema.py` → `Vein` | 312号——Trace识别的两个核心问题之一 | structure→318号§4；branches→318号§4 |
| `schema.py` → `Segment` | 304号§8.9——格中元素=某个看法下的段 | segment_features→304号§8 |
| `schema.py` → `Branch` | 315号§6.2.2/318号§4 | chosen_path/unchosen_paths→000号 |
| `schema.py` → `LevelView` | 314号问题2——推理脉络的格化 | merged_segments→304号§8.7；格化方法→317号VMS-28/29/30 |

### Pipe 0: Solver AI（system/schema.py + system/process_solve.py）

| 代码位置 | 定义来源 | POC验证 |
|---|---|---|
| `schema.py` → `SolverInput` | 319号§1——Pipe 0的输入 | hint→315号§6.8/§6.2.2 |
| `schema.py` → `SolverOutput` | 319号§1——Pipe 0的输出 | final_status→第五代05-引导树闭环/04-停机条件.md |
| `process_solve.py` | 318号§2.1——Solver AI，推理探索 | 第五代已验证（VMS-0到VMS-8），第六代继承 |

### Pipe 1: Parser AI（system/vein_analysis.py）

| 代码位置 | 定义来源 | POC验证 |
|---|---|---|
| `vein_analysis.py` → `vein_analysis_three_phase()` | 333号——三阶段架构 | 0004-0013历史运行验证 |
| `vein_analysis.py` → `_phase1_grading()` | 333号——4并发格化 | VMS-28/28b/28c/28d/28e |
| `vein_analysis.py` → `_phase1_5_enumerate()` | 333号——程序枚举闭元素 | verify_lattice_completeness.py |
| `vein_analysis.py` → `_phase2_synthesis()` | 336号——综合分析4阶段拆分 | 0010-0013验证 |

### Pipe 2: Telling AI（待实现）

| 代码位置 | 定义来源 | POC验证 |
|---|---|---|
| 待实现 → `pipe_2_telling` | 318号§2.1——Telling AI，并发trace→tell匹配 | VMS-15并发Telling AI；VMS-25 Tell存储方案 |

### Pipe 3: Guide AI（待实现）

| 代码位置 | 定义来源 | POC验证 |
|---|---|---|
| 待实现 → `pipe_3_guide` | 318号§2.1——Guide AI，引导树填充 | VMS-17端到端工作流；VMS-18引导树妖娆生长；VMS-26两棵树Level问题 |

### 流程函数（system/process_solve.py + system/process_absorb.py）

| 代码位置 | 定义来源 | POC验证 |
|---|---|---|
| `process_solve.py` | 319号§1——Grove核心循环（解题引导） | VMS-17端到端工作流 |
| `process_absorb.py` | 319号§1——tell库增长循环（解答吸收） | VMS-16 Parser AI；VMS-19 tell库持续增长闭环 |

---

## 3. POC验证清单

### 第一层：基础能力验证（9个可并行）

| POC | 名称 | 验证什么 | 来源 | 依赖 |
|---|---|---|---|---|
| VMS-11 | 非局部trace识别 | 分析AI能否在中间Level识别出非局部trace | 303/305/314号 | - |
| VMS-12 | 推理脉络格化 | 能否用FCA格遍历算法系统化地找出所有有意义的Level视图 | 304/314号 | - |
| VMS-13 | Tell分类学基础 | 现有4164个tell的分类现状 | 313/314号 | - |
| VMS-20 | Pipe 0简化版 | 三种粗domain分类实现方式 | 311号§3.2 | - |
| VMS-24 | 当前方法局限性验证（基线） | 用第五代方法分析费马大定理，验证只输出三元组 | 314号§1.2 | - |
| VMS-27 | 已有产物二次分析 | 对现有455个profile做二次分析提取全Level Trace | 314/312号 | VMS-12 |
| VMS-28 | 方式A——AI做全部格化 | AI能否用直觉判断做格化 | 316号§5 | - |
| VMS-29 | 方式B——脚本做FCA格化 | 脚本用FCA格遍历算法枚举闭元素 | 316号§5 | - |
| VMS-30 | 方式C——AI做+FCA验证 | AI先做格化和trace识别，再用FCA验证 | 316号§5 | - |

### 第二层：管线验证（7个）

| POC | 名称 | 验证什么 | 来源 | 依赖 |
|---|---|---|---|---|
| VMS-14 | 脉络分析管线步骤1-4 | 脉络分析管线能否端到端运行 | 315/316号 | VMS-11+VMS-12 |
| VMS-15 | 并发Telling AI | 多个Devin CLI实例能否并发做trace→tell匹配 | 311/315号 | VMS-13 |
| VMS-16 | Parser AI解答吸收 | Parser AI能否从外部解答记录识别新(tell,hint) | 315/316号 | VMS-14 |
| VMS-21 | 分类维度结构验证 | Tell分类学用四层层次还是正交维度 | 313号§4.1 | VMS-13 |
| VMS-22 | FCA角色验证 | 用FCA定义分类体系还是验证完备性 | 313号§4.3 | VMS-13+VMS-21 |
| VMS-23 | 非局部tell库补充 | 重新分析现有455个profile补充非局部tell | 314号§2.1 | VMS-11 |
| VMS-25 | Tell存储方案 | tell存储在目录AGENTS.md文件中 | 315号§4.1 | VMS-13+VMS-21 |

### 第三层：系统验证（4个）

| POC | 名称 | 验证什么 | 来源 | 依赖 |
|---|---|---|---|---|
| VMS-17 | 端到端工作流 | 完整的7阶段循环能否端到端运行 | 316号 | VMS-14+VMS-15 |
| VMS-18 | 引导树妖娆生长 | 引导树能否在不同Level上快速生出更多探索方向 | 315/316号 | VMS-17 |
| VMS-19 | tell库持续增长闭环 | 解题引导→解答吸收→解题引导闭环 | 315/316号 | VMS-16+VMS-17 |
| VMS-26 | 两棵树Level问题 | 非局部trace引入后的Level问题 | 315/316号 | VMS-17 |

---

## 4. 314号三个必须着力解决的问题

| 问题 | 描述 | 验证方法 | 来源 |
|---|---|---|---|
| 问题1（库侧） | 现有4164个tell全是第五代局部分析方法的产物，没有经过非局部分析。看不到：反证法/同构之桥/构造-分析-排除/模分析无尽追逐/辅助函数+非负性约束/构造必然逃逸的数 | VMS-24（基线）→VMS-11（新方法）→VMS-23（批量补充） | 314号§1-2 |
| 问题2（识别侧） | 推理脉络的格化——如何找出所有Level的脉络视图。n个节点的脉络有2^(n-1)种看法，不能全枚举。用FCA格遍历算法系统化地找出有意义的Level视图 | VMS-12→VMS-28/29/30（三种方式对比） | 314号§3-4 |
| 问题3（分类侧） | Tell的分类学——建立同时覆盖局部tell和非局部tell的分类体系。依赖问题1和问题2，但局部tell的分类部分可以独立先行 | VMS-13→VMS-21→VMS-22→VMS-25 | 314号§5-6 |

---

## 5. 系统的根本认知

**认知**：系统的目的不是让AI做出来，而是让两棵树生长出来，在过程中与正确解答的脉络相遇。

**来源**：315号§6.8（第五代设计文档调查）+第五代系统技术说明书

**带来的设计转变**：
1. 推理AI不需要停下接受提示
2. 系统与推理AI并行运行
3. hint的作用是让树分叉不是让AI做出来
4. 一个tell对应多个hint全选
5. 不需要汇总多Telling AI结果
6. 匹配失败存档启发Parser AI
7. 评测标准：树长得多完整（多妖娆）
8. 停机条件：某条脉络与正确解答相遇

---

## 6. 三阶段脉络分析架构

**定义来源**：333号——脉络分析Pipe内细化方案：格化与trace识别分离

| 阶段 | 函数 | 做什么 | 提示词/脚本 |
|---|---|---|---|
| 阶段1 格化 | `_phase1_grading` | 4并发格化（V5/V7/V8/V10），产出segments.json+formal_context.json | v5/v7/v8/v10_grading.md |
| 阶段1.5 程序枚举 | `_phase1_5_enumerate` | 用verify_lattice_completeness.py枚举闭元素 | system/verify_lattice_completeness.py |
| 阶段2 综合分析 | `_phase2_synthesis` | 1个devin cli读4版本格化结果+闭元素，做trace识别+审计+元反思 | synthesis.md |

**入口函数**：`vein_analysis_three_phase`
**运行脚本**：`system/run_imo2009p6_three_phase.py`

---

## 7. 文件拆分流程控制技术（335/336号）

**规则文件**：`.devin/rules/six-file-staged-flow.md`
**核心秘诀**：让AI一上来就先创建文件，把工作阶段的要求文件拆分，每次完整读取一个要求文件，填充一个输出文件
**设计原则**：不改变认知内容，只改变执行顺序

### V8应用（335号方案D——2步文件拆分）

| 步骤 | 做什么 | 产出 |
|---|---|---|
| step1 | 完整格化（段划分+所有特征标注） | segments.json |
| step2 | 矩阵构造（从segments.json提取特征构造I矩阵） | formal_context.json |

**退化教训**：4步方案曾导致退化（step1禁止标注特征→改变了认知内容→段数21 vs 32）；2步方案不退化（闭元素48=48）
**关键区别**：V8是"同一个认知过程"拆分——需要小心不改变认知内容

### 综合分析应用（336号——4阶段文件拆分）

| 步骤 | 做什么 | 产出 |
|---|---|---|
| step1 | 对比+回溯检查 | comparison.json |
| step2 | 闭元素解读+跨闭元素元模式 | closed_element_traces.json |
| step3 | nonlocal+ccm+global trace | content_based_traces.json |
| step4 | 审计+合并+AI优势+关键实体+元反思 | output.json+output.md |

**验证结果**：不仅没有退化，还大幅提升（trace 43→88，AI优势 7→20）
**关键区别**：综合分析是"不同的认知工作"拆分——天然不改变认知内容，且每步更专注→更细致→更多trace

### V8 vs 综合分析对比

- **V8**：同一个认知过程拆分→需要小心不改变认知内容→闭元素数量不变
- **综合分析**：不同认知工作拆分→天然不改变认知内容→每步更专注→trace数量翻倍

---

## 8. 脉络分析审计（334号）

**审计脚本**：`system/tests/vein_analysis/run_full_pipeline_audit.py`

**审计维度**：
1. trace数量（vs baseline/历史运行）
2. trace类型分布（local/nonlocal/global/cross_case_merge/cross_element_meta_pattern）
3. 闭元素数量
4. AI优势元素数量
5. 元反思trace数量

**历史运行**：

| 运行 | trace数 | 说明 |
|---|---|---|
| 0004 | 11 | 三阶段架构第一次运行 |
| 0005 | 43 | 三阶段架构第二次运行（原版V8+原版综合分析） |
| 0008 | 19 | V8方案D测试+global trace退化发现（global=0） |
| 0009 | 43 | global trace修复后（global=7） |
| 0010 | 88 | 综合分析4阶段拆分测试（大幅提升） |
| 0011 | 48 | 首次完整管线4阶段拆分运行（V10闭元素退化26，非系统退化） |
| 0012 | - | 非tmux模式运行被kill——不完整，归档已删除 |
| 0013 | 65 | tmux模式+340/341/342号方案验证——0退化点，总耗时1020秒 |

**退化判定标准**：trace数量<80%或trace类型<70%为退化
**迭代终止条件**：无真正退化（baseline并集导致的假退化不算）

---

## 9. 子管线超时降级（340号）

**定义来源**：340号——子管线超时降级方案
**超时计算函数**：`_calc_grading_timeout(solution_text)`——按文本长度计算

| 文本长度 | 超时阈值 |
|---|---|
| <2000字符 | 600秒（10分钟） |
| 2000-5000字符 | 900秒（15分钟） |
| 5000-10000字符 | 1200秒（20分钟） |
| >10000字符 | 1800秒（30分钟） |

**降级逻辑**：每个版本独立超时，至少1个通过即可继续，超时版本自动kill进程
**数据库字段**：`phase1_success_versions` / `phase1_failed_versions` / `phase1_results`
**所有版本失败**：`AnalysisOutput.all_failed=True` → 入口脚本`sys.exit(1)`

---

## 10. 全流程日志（341号）

**模块**：`system/log.py`
**日志目录**：`system/logs/`（.gitignore忽略）
**滚动策略**：RotatingFileHandler——单文件1MB，最多500个备份（500MB）
**日志格式**：`[timestamp] [level] [module] message`
**输出**：同时输出到文件（DEBUG以上）和stdout（INFO以上）

---

## 11. 系统时间意识（342号）

**3层时间记录**：

| 层 | 内容 |
|---|---|
| 第1层 日志时间戳 | 341号方案——每条日志带时间戳+关键位置耗时统计 |
| 第2层 数据库timing字段 | problem_entries.timing——全管线全子管线结构化时间记录 |
| 第3层 耗时摘要表 | 运行结束打印各阶段各版本各step耗时 |

**timing字段结构**：
- `total_duration_sec`：总耗时
- `phase1_grading.duration_sec` + `versions.{V5/V7/V8/V10}.duration_sec`：格化阶段+各版本耗时
- `phase1_5_enumerate.duration_sec` + `versions.{V7/V8/V10}.closed_elements_count`：枚举阶段+各版本闭元素数
- `phase2_synthesis.duration_sec` + `steps.{step1-4}.duration_sec`：综合分析+4阶段拆分各步耗时

**综合4阶段耗时计算**：通过中间文件mtime计算（comparison/closed_element_traces/content_based_traces/output）
