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

### 2026-08-14新增（解题侧非线性脉络分析）

| 编号 | 内容 |
|---|---|
| 344 | 解题侧非线性脉络分析理论——事件DAG、观察/分区层、FCA概念格三者分离，RCA-style关系尺度 |
| 345 | 独立实施方案——入题侧保护清单、严格轨迹合同、阶段门和独立代码/资产/测试命名空间 |
| 346 | POC-VMS-31预注册协议——线性、分叉、折返、真合流、复合五案例与F/T/D对照 |
| 347 | POC-VMS-31实验结果——离线结构PASS，raw thinking抽取与live接入NOT_TESTED |
| 348 | POC-VMS-32协议——三个认知角色、冻结fixture、GLM-5.2 High单次实跑与盲化评分 |
| 349 | POC-VMS-32结果——sandbox/权限/载体限流导致协议不可判，不外推角色无效 |
| 350 | POC-VMS-33协议——独立角色启动器、模型/环境/export/原子封存修订验证 |
| 351 | POC-VMS-33结果——sandbox自主模式仍拒绝文件写入，启动器修订不足 |
| 352 | POC-VMS-34协议——只读认知角色+机械响应封存备选；live调用暂停 |
| 353 | 入题侧Devin CLI回源——tmux/Popen、工作目录、模型写文件、DONE/export竞态与解题侧吸收边界 |
| 354 | POC-VMS-35协议——仅移除sandbox，复现来源侧文件写入合同的单因素实验 |
| 355 | Devin双运行档——sealed noninteractive与interactive tmux debug的证据分流 |
| 356 | POC-VMS-35结果——文件写入合同恢复，但总判INCONCLUSIVE且形成gold语义反例 |
| 357 | POC-VMS-36协议——tmux实时可观测、一次正常退出动作、export完整性Canary |
| 358 | POC-VMS-36结果——tmux可观测成功，但repo内workspace被自身deny规则拒绝，ABORTED/INCONCLUSIVE |
| 359 | POC-VMS-37协议——D盘专属外置workspace、同设备live/final bundle与正常完成验证 |
| 360 | POC-VMS-37结果——D盘/tmux/dangerous/exact model可用，但`Read(/Volumes/**)`自拒绝且attempt ID漂移，总体INCONCLUSIVE/ABORTED |
| 361 | POC-VMS-38协议——no-sandbox + dangerous/YOLO + 冻结AGENTS工作区权限与精确attempt身份的一次性tmux验证 |
| 362 | POC-VMS-38结果——调试执行合同SUPPORTED；严格输出/DONE/exact model/tool boundary/正常退出PASS，角色资格仍NOT TESTED；发现历史ATIF摘要0/15计数缺陷 |
| 363 | 解题侧总路线图与任务追踪——Devin AGENTS物理边界、S1—S7脉络核心、Trace/Tell/Hint积累、推理树/引导树、Grove闭环、Seven模拟/DB与golden slice |
| 364 | POC-VMS-39冻结协议——Devin `AGENTS.md`短控制面的官方回源、精确尺寸sentinel与ATIF effective visibility隔离实测 |
| 365 | POC-VMS-39最终结果——静态`rules show`完整到256 KiB；live 16,384 bytes full、16,385 bytes开始截断；四cell全树aggregate integrity PASS |
| 366 | POC-VMS-40冻结协议——五层真值、多视图关系、多轴State、不可拆分alternative与机械Evaluator |
| 367 | POC-VMS-40结果——MV1—MV6共26个candidate全部匹配预注册Verdict；离线确定性范围PASS |
| 368 | POC-VMS-41协议——四case未见样本、隐藏acceptable set、一次性Devin Event Extractor资格化与延迟评分 |
| 369 | POC-VMS-41结果——artifact/replay PASS但机械0/4、协议INCONCLUSIVE、profile NOT_QUALIFIED；事后诊断只作failure localization |
| 370 | Trace/Tell/Hint文件分片与逐项遍历——一个不可变items真值源、append-only分析/cursor、机械coverage与completion |
| 371 | POC-VMS-41R1修订协议——Candidate V2、occurrence/projection、typed path、时序状态、MERGE贡献与file-effect审计 |
| 372 | POC-VMS-41R1未见qualification pack冻结协议——6个未见case、阈值、盲审rubric、hidden acceptable set/reference/negative checks与零模型preexecution边界 |
| 373 | POC-VMS-41R1 live runner与盲审封存协议——零模型runner shell、workspace/public-hidden split、`--execute` fail-closed与授权前停止点 |
| 374 | POC-VMS-41R1 LiveRunPermit与盲审包计划——不可消费permit、Reviewer可见文件集、hidden join顺序与零副作用计划对象 |
| 375 | POC-VMS-41R1 sealed manual judgment合同——case/attempt绑定、盲审attestation、六轴Verdict与人工判断Schema |
| 376 | POC-VMS-41R1 hidden join simulator——synthetic manual judgment、fake/reference candidate、hidden mechanical join和development-only final verdict |
| 377 | POC-VMS-41R1 fake live bundle与盲审包materializer——Reviewer可见文件hash manifest、hidden隔离和非live输出声明 |
| 378 | POC-VMS-41R1 final qualification join receipt——materializer与hidden join按case/attempt/candidate hash合并，development-only final receipt和非资格化边界 |
| 379 | POC-VMS-41R1 fake bundle append-only dry-run——临时输出根真实写Reviewer可见文件、拒绝覆盖/repo根/symlink根和hidden泄露 |
| 380 | POC-VMS-42 State Normalizer预注册协议——多轴状态绑定、dictionary alias归一化、legacy projection与fail-closed反例 |
| 381 | POC-VMS-42 State Normalizer资格包冻结——public/hidden分离、reference/negative重放与零模型receipt |
| 382 | POC-VMS-42 State Normalizer hidden join——candidate bundle与hidden dictionary/acceptable set评分边界、negative保留和非资格化receipt |
| 383 | POC-VMS-42 State Normalizer reviewer judgment合同——public/candidate bundle盲审对象、hidden未见attestation与六轴Verdict |
| 384 | POC-VMS-42 State Normalizer final reviewer+hidden join——manual/hidden双面裁决合并、FAIL保留与非资格化final receipt |
| 385 | POC-VMS-42 State Normalizer unseen qualification extension——全新fixture扩展、新旧case/candidate ID不重叠、public/hidden隔离和非资格化extension receipt |
| 386 | POC-VMS-42 State Normalizer DAG writeback sidecar——PASS normalized bundle按DAG event_id/topological order生成不可变annotation bundle，不改写DAG本体 |
| 387 | POC-VMS-43 Trace Auditor结构审计——结构化DAG上的branch/failure/revisit/reuse/merge/recovery family观测与可选state sidecar一致性验证 |

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

### 解题侧非线性脉络（system/solve_vein_analysis/）

| 代码位置 | 定义来源 | 当前验证 |
|---|---|---|
| `models.py` → `ReasoningTrajectory/ReasoningDag` | 344号§3、345号数据合同 | POC-VMS-31五例+负向合同 |
| `fca.py` → `FormalContext/Next Closure` | 344号§4、346号§4.3 | Next Closure=对象子集穷举oracle |
| `pipeline.py` → graph/context/relational/trace | 344号§5、345号阶段设计 | 五例exact edge/trace/批增量PASS |
| `integrity.py` → implementation receipt | 345号artifact合同 | 单次run与POC均绑定精确实现树 |
| `cli.py` | 345号artifact与隔离门 | 原子封存、拒绝覆盖、零model/DB/Solver |
| `role_runtime.py` | 348、350、353、354、356号 | sandbox/no-sandbox分档；VMS-35三角色文件/export成功但未资格化 |
| `tmux_runtime.py` | 353、355、357、358号 | 私有socket/session、pane/health快照与abort已验证；repo外workspace待新版本 |
| `assets/solve_vein_analysis/` | 345、348、353-362号 | 0.3.0哈希PASS；VMS-38只支持interactive debug执行合同，prompt/manifest本身不声明角色live capability |
| `semantic_truth.py` | 344、345、356、362、366-367号 | 五层真值、多视图relation、多轴state、完整alternative和机械Verdict |
| `event_extraction_projection.py` | 369、371号 | V2 occurrence/projection、typed path、双时间状态、MERGE贡献frontier与路径搜索资源上限；26项离线回归PASS，未资格化模型 |
| `file_effect_audit.py` | 369、371号 | pre/post inventory+结构化provider events联合审计；15项离线回归PASS，真实CLI事件完备性未资格化 |
| `state_normalization.py` | 356、366、367、380号 | 多轴State Normalizer离线核心；2 case/4 candidate、8项core测试PASS，模型角色未资格化 |
| `tests/solve_vein_analysis/build_vms42_state_normalizer_pack.py` | 380、381号 | VMS-42零模型资格包构建器；public/hidden分离、2 reference/2 negative、7项pack测试PASS |
| `tests/solve_vein_analysis/vms42_state_normalizer_hidden_join.py` | 380-382号 | VMS-42 hidden join模拟器；reference bundle PASS但development-only，negative bundle FAIL并保留，8项测试PASS |
| `tests/solve_vein_analysis/vms42_state_normalizer_manual_judgment_contract.py` | 380-383号 | VMS-42 sealed reviewer judgment合同；绑定candidate bundle、hidden未见attestation、六轴Verdict，10项测试PASS |
| `tests/solve_vein_analysis/vms42_state_normalizer_final_join_receipt.py` | 380-384号 | VMS-42 final reviewer+hidden join receipt；manual/hidden任一FAIL则final FAIL，双PASS仍development-only，8项测试PASS |
| `tests/solve_vein_analysis/build_vms42_state_normalizer_unseen_pack.py` | 380-385号 | VMS-42 unseen qualification extension；2个全新case/4 candidate、新旧ID不重叠、public/hidden隔离、8项测试PASS |
| `state_normalized_dag.py` | 380、385、386号 | VMS-42 DAG writeback sidecar；PASS State Normalizer evaluation绑定DAG event，保持DAG不变并按拓扑输出annotation bundle，8项测试PASS |
| `trace_auditor.py` | 386、387号 | VMS-43 Trace Auditor结构审计；在已结构化DAG上观察非线性trace family，验证可选state sidecar hash/order兼容，10项测试PASS |
| `run_event_extractor_calibration.py` + `qualification_fixtures/vms41r1_calibration/` | 371号 | 13 candidate+6 file-effect开发场景逐轴零mismatch；manifest、受限mutation、tamper与symlink拒绝；永久`DEVELOPMENT_ONLY` |
| `build_vms41r1_qualification_pack.py` + `qualification_fixtures/vms41r1/` | 372号 | 6个未见qualification case、6个hidden reference candidate、4个negative mutation自检；public manifests不含答案/acceptable set；机械上限`PENDING_BLIND_MANUAL_AUDIT` |
| `freeze_vms41r1_event_extractor_preexecution.py` + `live_fixtures/poc_vms_41r1.freeze.json` | 371-372号 | 0.4.1角色资产、6个attempt IDs、qualification pack和hidden grader物证的零模型preexecution freeze；外部副作用授权全为0，live仍需新授权 |
| `tests/solve_vein_analysis/` | 346-387号 | `README.md`是全部测试/POC证据总索引；293 tests；VMS-39冻结profile cap=16,384 bytes；VMS-40离线6 case/26 candidate PASS；VMS-41封存为NOT_QUALIFIED；VMS-41R1 zero-model chain闭合但live未授权；VMS-42 State Normalizer链PASS；VMS-43 Trace Auditor结构审计PASS；VMS-44—52仍待预注册 |

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

### 解题侧新增POC

| POC | 名称 | 验证什么 | 结果 | 非主张 |
|---|---|---|---|---|
| VMS-31 | 非线性脉络FCA/RCA对照 | 结构化轨迹上的事件DAG、FCA闭包、关系尺度、trace与F/T/D投影损失 | 347号：离线结构PASS | raw thinking抽取、live载体、数据库、规模性能均未测试 |
| VMS-32 | Devin认知角色首次实跑 | 三角色能否按冻结资产写出可评分输出 | 349号：INCONCLUSIVE_PROTOCOL | 不证明角色无效 |
| VMS-33 | 角色启动器修订 | 独立config/model/export/sandbox能否恢复写入 | 351号：INCONCLUSIVE_PROTOCOL | 不证明sandbox是唯一原因 |
| VMS-34 | 机械响应封存备选 | 无写工具的marker响应方案 | 352号：PAUSED_BEFORE_LIVE_CALLS | 不含live证据 |
| VMS-35 | 来源侧文件写入合同复现 | no-sandbox单因素下三个角色写文件、DONE与export | 356号：文件合同受支持；总体INCONCLUSIVE | 不资格化角色，不证明强隔离 |
| VMS-36 | tmux交互调试Canary | 实时pane可观测、DONE后正常退出、export完整封存 | 358号：可观测PASS；自身workspace访问失败；总体INCONCLUSIVE/ABORTED | 永久DEVELOPMENT_ONLY；不资格化角色 |
| VMS-37 | D盘外置workspace tmux Canary | 修复VMS-36路径/deny冲突，验证输出、DONE、export和正常退出 | 360号：D盘与tmux可用，但全卷deny再次自拒绝，attempt ID也漂移；INCONCLUSIVE/ABORTED | 永久DEVELOPMENT_ONLY；不资格化角色 |
| VMS-38 | dangerous + AGENTS工作区权限 tmux Canary | 删除会自拒绝的广泛Read deny，用角色AGENTS约束workspace权限并机械绑定attempt ID | 362号：`SUPPORTED_WITHIN_DEBUG_CANARY`；D盘严格输出/DONE、exact model、13-step/7-call原始边界审计、唯一退出和exit 0全部成立 | 永久DEVELOPMENT_ONLY；不资格化角色；历史receipt的0/15摘要不可用 |
| VMS-39 | Devin `AGENTS.md`有效装载边界 | 静态loader与live ATIF是否一致、16 KiB附近精确截断位置 | 365号：冻结profile中16,384 bytes完整、16,385开始截断；aggregate integrity PASS | 不外推其他CLI/profile；不支持把AGENTS用作Tell/Trace数据仓库 |
| VMS-40 | 多视图脉络真值与AcceptableSet | occurrence、relation view、多轴state、alternative与机械Verdict | 367号：6 case/26 candidate零mismatch，离线确定性PASS | 不资格化任何模型角色 |
| VMS-41 | Event Extractor未见资格化 | 四case、隐藏acceptable set、一次性Devin one-shot与延迟评分 | 369号：artifact/replay PASS、机械0/4、INCONCLUSIVE_PROTOCOL、profile NOT_QUALIFIED；事后诊断已封存 | 人工非盲，只用于failure localization；原attempt不可重跑；不裁决模型全局能力 |

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
