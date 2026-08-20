# RulePointers.md — 其他规则指针（完整版）

> **来源**：从 AGENTS.md 原始第728-756行外移（2026-08-19瘦身工程，392号方案）。AGENTS.md中保留精炼版+指向本文件的索引行。
> **定位**：所有rule文件指针、dev-docs文档指针、两套Pipe命名体系详细说明、POC系列文档详细描述的完整版。
> **加载时机**：当你要查某个具体rule的触发条件和核心约束、查某个dev-docs文档的内容摘要、查两套Pipe命名体系的详细说明、查POC系列文档的内容时，用read工具加载本文件。AGENTS.md中的精炼版只保留清单，本文件包含完整描述。
> **AGENTS.md索引**：AGENTS.md "外部文档索引"节有指向本文件的索引行。AGENTS.md "其他规则指针"节也有指向本文件的索引行。

---

### 其他规则指针

- **提示策略路线选择与Level连续谱**：详见 `dev-docs/214-v1-2026-08-06-提示策略路线选择与Level连续谱.md`。核心决策：走路线B（思维模式）而非路线A（堆砌知识）。
- **元组群guided-math-solving**：5个Skill详见 `.devin/rules/guided-math-solving.md`。
- **Tell分类学迭代审计铁律**：对已有profile做FCA再分析、Tell分类学修正时的SOP流程和版本化审计要求。详见 `.devin/rules/tell-taxonomy-iteration-audit.md`。**触发条件**：对已有profile做FCA再分析时；Tell分类学（`FCA学习笔记/08-先验Tell分类学.md`）需要修正时；用FCA理论审查分类学自洽性时。**核心约束**：再分析9步SOP + 版本化审计6条铁律（明面版本历史、四要素记录、覆盖性检查、版本总表、文件结构完整、关联文件同步）。
- **Tell分类学Schema维护铁律**：AGENTS.md中"Tell分类学Schema"节是跨压缩边界保真的核心，分类学修正后必须同步更新该节。详见 `.devin/rules/tell-taxonomy-schema-maintenance.md`。**触发条件**：Tell分类学版本号变化/段结构模式变化/domain变化/结构框架变化/观察Level参数变化/关键修正认知变化时。**核心约束**：08号文件和AGENTS.md Schema节必须一致，不一致即违反rule。
- **Tell分类学研究过程文档存放规则**：Tell分类学相关的研发过程文档（探索性、讨论性、评审性、方案演进性）记录到 `Tell分类学研究过程文档/`目录，不放在`第六代系统研发过程文档/`。编号从343号开始（333-340号已迁移至本目录，341-342号已被第六代研发过程文档占用）。**每次新增文档必须同步更新 `Tell分类学研究过程文档/README.md` 索引。** 详见 `.devin/rules/tell-taxonomy-research-docs.md`。
- **system/ 代码与 .ref 文件同步规则**：`system/` 中每个 `.py` 文件必须有同名 `.ref` 文件，内容是理解该模块需要参考的文档路径列表（相对 repo 根目录）。**改代码或改设计文档后都必须同步检查 .ref**——改了 `.py` 检查 `.ref` 是否还准确，改了设计文档检查引用该文档的 `.ref` 是否需要更新。详见 `.devin/rules/system-ref-sync.md`。
- **审计方法论**：F1-F15断层类型学、D1-D4深度等级、21审计维度，详见 `dev-docs/146-v4-2026-08-05-审计方法论手册-*.md`。
- **形式化思维规则**：从星学继承，适配数学。详见第一代技术说明书249号。
- **项目定位与核心假设**：数学大师制造项目，详见 `原语化AI数学工程系统设计/README.md`。核心假设从星学信念降级为可证伪假设，详见123号。
- **K维度多层知识结构（L1-L4）**：详见 `dev-docs/201号`系列。
- **AI在运行过程中的角色**：经典计算给候选，AI做最终判断。详见 `dev-docs/202号`。
- **Pipe监控SOP**：运行任何Pipe（分析/审计/选题）时，必须启动Monitor Pipe并行监控。**检查时用标准化脚本** `analysis-devin-failure-system/scripts/monitor_check.sh <batch_id>`，禁止inline编写检查命令。脚本输出4项检查：Monitor Pipe pane输出 / alerts集合 / 进程状态 / 进度。详见 `.devin/rules/pipeline-monitor-sop.md`。
- **审计Pipeline Rate Limit防护**：运行audit_launcher前必须检查当前devin cli进程数并据此设置并发（>8个进程时并发=1）。rate limit是账户级的，跨所有CLI实例共享。选题只用status=completed的审计结果。详见 `.devin/rules/audit-pipeline-rate-limit.md`。根因分析见 `dev-docs/388号`。
- **Mid-Hint实验选题数据链**：Pipe 1（分析2050条）→ Pipe 2（审计721个PASS_SELECTABLE）→ **Pipe 3（选题708条，产出47道YES候选+69道假朋友+30道边界）** → POC-0 CasePack精筛（✅v1已冻结·2026-08-17，6正迁移+4假朋友+2边界从Pipe 3精筛）。Pipe 3规模化运行已完成（2026-08-17），产出统计见 `analysis-devin-failure-system/output/selection-full1/selection_results_summary.json`。详见 `eight-system/HANDOFF.md`和`analysis-devin-failure-system/output/analysis_summary.md`和`audit-full1/audit_summary.md`。
- **Pipe 3选题系统（已扩展·2026-08-17·规模化运行完成）**：复用错题分析系统框架（audit_launcher的tmux架构+Redis队列+rate limit防护），新增`src/selection_collector.py`/`selection_launcher.py`/`selection_result_collector.py`+`run_selection_pipeline.py`+`templates/selection_agents_md.md`+`src/monitor_selection.py`+`scripts/monitor_check_selection.sh`。**已按412号方案扩展**——提示词模板增加POC Preparation Metadata节（6项POC准备数据字段），解析器增加6个新标签的解析和DB写入，collect加跨batch去重，monitor_selection.py提供POC字段质量监控。**规模化运行完成（2026-08-17）**：708/708题全部完成，0失败，0 XML解析失败，耗时约85分钟（5并发）。产出47道suitable=YES候选题+69道假朋友候选+30道边界候选，6字段填写率100%，逻辑一致性0问题（1个初始问题已修正）。YES题batch分布均匀（batch1:15/batch2:10/batch3:10/extended:12）。分类逻辑审查见`dev-docs/387号`§九。扩展方案见`Tell分类学研究过程文档/412号`。运行SOP见下方"### Pipe 3扩展运行SOP"小节。
- **MH第一圈(00995)已完成**：交互模式运行13分钟，AI用doubling construction解决n≡2(mod 4)卡点，答案5048。**重大发现：标准答案3800有误**——穷举代码`mean_int_search.py`的`row_options`只生成排序行，漏掉非排序行解空间，n=6错误判定IMPOSSIBLE。n=6构造已程序验证正确（1-36每个出现一次，所有行/列均值整数）。正确答案5048（S={1,...,100}\{2}）。详见`eight-system/runs/midhint/realtrack/00995/experiment_report.md`和`verification/README.md`。
- **题目纠错记录**：`dev-docs/389号`——集中记录所有发现标准答案有误的题目。**选题前必须先查本文档**。当前记录：polymath_00995（标准答案3800→5048）。ArangoDB `problem_profiles`集合中已更新正确答案。
- **两套Pipe命名体系统一说明（2026-08-17厘清）**：项目中存在两套Pipe命名体系，用了相同的编号但指不同的东西，必须区分：
  - **第六代系统Pipe体系**（AGENTS.md第1014-1018行定义）：Pipe 0 / Solver AI（推理AI做数学）→ Pipe 1 / Parser AI（分析脉络格化识别trace）→ Pipe 2 / Telling AI（trace匹配到tell库）→ Pipe 3 / Guide AI（hint变成引导树新边）。这是Grove核心循环的四Pipe架构。
  - **错题分析系统Pipe体系**（387号dev-docs目录定义）：Pipe 1（分析Pipe——判定d1/d2方向错误类型）→ Pipe 2（审计Pipe——检查分析结果质量属性）→ Pipe 3（选题Pipe——按Mid-Hint标准语义选题）。这是错题分析系统的三Pipe架构，**缺少Pipe 0**——因为bare AI跑题在系统外完成，输入是已经跑完的失败trace。
  - **两套体系的关系**：错题分析系统的Pipe 1是第六代系统Pipe 1的粗粒度简化版（判定d1/d2 vs 完整脉络格化识别trace）；错题分析系统的Pipe 2/3在第六代系统中没有对应（审计和语义选题是错题分析系统特有的）。两套体系不要混淆——提到"Pipe 1"时必须明确是哪个体系。
  - **完整流程的Pipe顺序**（统一视角）：Pipe 0 Solver AI跑题产出失败trace → Pipe 1识别d1/d2（方向错误？什么类型？）→ Pipe 2审计分析结果质量 → Pipe 3语义粗筛适合Mid-Hint的题 → POC-0 CasePack精筛→22道CasePack → POC-1因果取商深度分析→TellCore → POC-2~9六门审计+端到端闭环。详见396号§7.4"Pipe 3在识别端中的角色"和399号POC-0方案§4.1"与Pipe 3的接力关系"。
- **非特化理论综合文档（396号）**：`Tell分类学研究过程文档/396-v0-2026-08-17-非特化理论综合-从钟形曲线最高点到认知Option与Pareto前沿.md`——把用户的Tell/Hint概念厘清（钟形曲线绑在Hint上不是Tell上）与GPT在371/372号看到的三层深化（Pareto前沿/认知Option/因果贡献证明）统一成一份完整认知。包含：GPT框架里两个不同的"从trace中读"（识别端从失败trace读分叉vs学习端从成功trace提取认知技能）、错题分析系统是识别端工程化实现、Pipe 3和POC-0的接力关系、GPT设计的POC系列状态（373号9个POC，POC-0/1已完成，POC-2~8未执行）。
- **POC系列审视文档（397号）**：`Tell分类学研究过程文档/397-v0-2026-08-17-GPT373号POC套装的逐个审视-完备性合理性与缺失项.md`——逐个审视373号9个POC的完备性和合理性，识别过度设计部分（POC-5首批过早/POC-7版本修订过重/CaseCard 30字段过多/评分表10维度过重）和GPT未考虑到的8项缺失（最关键：Hint非特化程度钟形曲线验证/识别端验证/基础因果效应验证）。建议修订后首批POC系列为11个POC。
- **POC自包含方案文档（398-409号）**：`Tell分类学研究过程文档/`下12份自包含POC方案文档（398号POC-2.5基础因果效应验证/399号POC-0 CasePack冻结/400号POC-0.5变形关系声明/401号POC-1因果取商增强版/402号POC-2可选择/403号POC-3.5 Hint非特化程度验证/404号POC-3可执行/405号POC-4可终止/406号POC-6可归责/407号POC-7可持续学习简化版/408号POC-8端到端闭环/409号POC-9识别端验证）。每份遵循398号样板的10节结构（§0规范/§1定位/§2理论背景/§3前置状态/§4输入/§5方法/§6输出/§7通过标准/§8被索引文档全文加载清单/§9执行约束/§10与其他POC关系），§8列出3-7份需全文加载的核心文档。**未来20万上下文的AI只加载某份POC方案+它§8清单的文档，就能完整执行这个POC，不需要用户另外指点。**

