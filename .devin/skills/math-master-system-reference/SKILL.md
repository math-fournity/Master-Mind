# math-master-system-reference

## Description

数学大师系统的操作级技术参考和星学方法论证据链。按需加载七步骤工作流、依赖图导入、arXiv查询、G'_topo生成、TopologyVerifier、三层提取、数学意识节点、种子推荐表、认知图查询命令、星学参考文档索引。

## 内容

### 方法论认识论位置

### 认识论位置

本方法论在 AI 史上的独特位置：

| 路径 | 工程化什么 | 不工程化什么 | 核心区别 |
|---|---|---|---|
| 1980s 专家系统 | 判断规则 + 推理过程 | — | 试图替代专家判断，失败了 |
| 2020s 大语言模型 | — | 判断本身 | 有判断力但无方向感 |
| 2020s RAG | 文档检索 | 思维路径 | 给资料但不给思维方向 |
| **xishujuzhen** | **"知道该判断什么"** | **判断本身** | **给思维方向但不替 AI 判断** |

与 chain-of-thought 的区别：CoT 是线性思维链（A→B→C→结论），xishujuzhen 是图结构思维网（有分叉、汇聚、螺旋上升的环路）。


### 星学参考索引

## 星学参考索引（方法论证据链，不是工作对象）

以下文档是星学项目中产生的**方法论资产**，对本项目有直接参考价值。它们不是数学项目的工作对象，但在设计数学领域的依赖图、知识系统结构、验证方案时，应作为方法论参考查阅。

**重要**：以下所有路径在星学项目中指向 `~/MOIRA_chinese_astrology-main/`，在本目录中已复制为相对路径（去掉前缀即可在本目录访问）。

### 核心方法论文档（最高参考价值）

| 文档 | 内容 | 对数学项目的参考价值 |
|---|---|---|
| `dev-docs/63-星学意识与螺旋上升的稀疏矩阵.md` | **整个方法论的起源**：从直觉画面到核心信念的完整对话记录。三维稀疏矩阵、两种环路、依赖图作为提示、数字化的大师、核心信念 | **必读**。数学项目的整个方法论框架来自这里 |
| `dev-docs/64-xishujuzhen-POC验证方案.md` ~ `dev-docs/77-xishujuzhen-POC8验证方案.md` | **POC1-8 完整验证体系**：从5节点小图到71节点大图、从静态分析到动态螺旋、从开环到闭环审计 | **必读**。数学项目的验证方案应参考这套实验设计 |
| `dev-docs/71-xishujuzhen-POC5验证结果.md` | POC-5 结果：边际增益+3.95，B组9.75 vs A组5.8 | 验证方法论的量化证据 |
| `dev-docs/73-xishujuzhen-POC6验证结果.md` | POC-6 结果：边际增益+5.92，交叉审计比AI自审更严格 | 交叉审计方法的参考 |
| `dev-docs/75-xishujuzhen-POC7验证结果.md` | POC-7 结果：边际增益+4.08，大规模依赖图可行（71节点100%覆盖） | 大规模可行性证据 |
| `dev-docs/69-xishujuzhen-POC4验证结果.md` | POC-4 结果：双宫联动+跨宫依赖场景，19节点25边，边际增益+3.20 | 复杂场景可行性证据 |
| `dev-docs/76-xishujuzhen闭环审计纠正流程优化方案.md` | 闭环审计流程：审计→反馈→修正→再审→直到无瑕疵，最大3轮 | 质量保证流程参考 |
| `dev-docs/78-xishujuzhen下一代工作流-从文字随机到拓扑覆盖.md` | **下一代工作流数学本质分析**：依赖图G是规范化拓扑结构，展开图G'是G的覆盖，审计是覆盖验证φ:G'→G。HoTT框架 | **高价值**。数学项目可能直接用到这套拓扑视角 |
| `dev-docs/79-xishujuzhen下一代工作流技术选型.md` | 技术选型：ArangoDB（多模型：图+文档+键值）作为依赖图数据库 | **技术架构基础**。数学版在此基础上新增 Lean 4/MathLib、SageMath、arXiv 管道，见 81 号文档 |
| `dev-docs/80-数学大师项目启动认知基础.md` | **项目启动认知**：成功的数学大师能解决什么问题（从具体计算到跨领域统一）、需要积累什么知识（P0经典/P1专题/P2前沿三层）、依赖图初始结构设计。是整个数学项目的认知起点 | **必读**。项目启动的认知基础 |
| `dev-docs/81-数学大师项目基础设施技术选型.md` | **数学版技术选型更新**：ArangoDB 保留 + 新增三层验证器阶梯（SymPy→SageMath→Lean 4）+ arXiv HTML 管道 + MathLib 依赖图导入 | **必读**。数学项目基础设施方案 |
| `dev-docs/82-题库作为数学思维积累方向.md` | **题库方法论**：解法路径=依赖图实证边、一题多解=图结构实证、跨领域映射边来源、难度梯度=POC阶梯、卡点=依赖图缺口发现、结构化格式、建设路径 | **必读**。题库是数学思维积累的主要方向 |
| `dev-docs/83-解法路径的三层提取与POC验证方案.md` | **三层提取方法论+POC**：L1解题思路（具体步骤）→L2数学思维（弥漫性模式，AI二次分析）→L3新的思维方式（范式级，改变图结构，AI三次分析）。三组对照POC（A=仅L1 / B=L1+L2 / C=L1+L2+L3），测试跨题近迁移和远迁移复用增益 | **必读**。L3是数学版相比星学版的本质增量 |
| `dev-docs/84-大师-POC-1验证方案.md` | **大师-POC-1正式方案**：矩条件极差题场景（第一问证明+第二问指数纠错），8节点10边依赖图（极端检验↔数值检验意识螺旋环路），A组（教材Markdown）vs B组（依赖图提示JSON）对照，5维评分。**核心测试点**：B组依赖图含"数值检验意识"节点，能否帮助AI发现第二问指数错误（-1/3应为-3/2）。原始题面来源：`~/Documents/Playground 2/docs_for_next_time/2026-03-06-矩条件极差题-详细推导与排错记录.md` | **必读**。数学版方法论验证的起点 |
| `dev-docs/85-大师-POC-1验证结果.md` | **大师-POC-1结果**：B组显著优于A组（综合5.00 vs 3.25，边际增益+1.75/5分制≈+3.50/10分制）。**核心发现**：两组都发现了指数错误，但只有B组给出了正确指数n^(-3/2)——A组将三点构型上界O(1/n)误认为下界，B组依赖图的"数值检验意识"节点和螺旋环路提示帮助其系统检验多个候选并正确区分上界与下界。验证了核心信念在数学领域成立 | **必读**。首个数学POC成功证据 |
| `dev-docs/86-从星学项目同步下一代工作流基础设施.md` | **从星学同步基础设施**：星学项目已完成POC-9（下一代工作流），拓扑覆盖验证1次通过100%覆盖。同步资产：①HoTT化理论（78号文档）——对数学更自然，数学对象本身就是拓扑结构；②TopologyVerifier代码——与领域无关，直接复用；③七步骤工作流——meta/normal分离，审计只做1次；④ArangoDB基础设施——共用星学实例。后续POC从文字对照升级为拓扑确定性验证 | **必读**。后续POC的方法论基础 |
| `dev-docs/87-大师-POC-2验证方案.md` | **大师-POC-2方案**：矩条件极差题第二问完整证明（n^(-3/2)下界），18节点25边2螺旋环路依赖图，采用七步骤工作流（ArangoDB + G'_topo + TopologyVerifier）。三组对照：A组（教材Markdown）vs B'组（依赖图JSON）vs B组（七步骤工作流）。8维15分制评分。验证H1-H5假设在数学领域是否成立 | **必读**。七步骤工作流在数学领域的首次验证 |
| `dev-docs/88-大师-POC-2验证结果.md` | **大师-POC-2结果**：B组显著优于A组（+4.9/15分制）和B'组（+3.5/15分制）。10分制边际增益：B vs A=+3.27，B vs B'=+2.34，B' vs A=+0.93。**核心发现**：B组唯一完成了稳定性方程5D=3√5(B_r-B_s)+2C_3的完整推导——这是A组和B'组都未能完成的关键突破。H1-H5全部验证通过。TopologyVerifier从星学到数学零修改复用，1次通过100%覆盖 | **必读**。七步骤工作流在数学领域成功验证 |
| `dev-docs/89-工作系统审计与升级方案-星学对比.md` | **工作系统审计**：审计星学项目已完成的工作系统升级（5层架构：运行时协议+Devin CLI集成+核心控制脚本+运行时工具+运行时状态），对比数学项目当前状态（几乎空白）。**结论**：有必要升级，但不是简单复制——数学项目有独特资产（七步骤工作流+ArangoDB+TopologyVerifier），应借鉴星学的运行时架构，同时在状态存储（ArangoDB替代JSON）、质量门控（集成TopologyVerifier）、自我迭代（从POC结果发现新意识节点）上超越星学。**第二次审计纠正**：真正的升级是 `xishujuzhen/cognition_*.py` 系列——把"稀疏矩阵/依赖图/拓扑验证/ArangoDB"基座安装到工作系统自身上，64个认知单元100条边，CP1-CP6工作流，三 hook 集成 | **必读**。工作系统升级的决策依据 |
| `dev-docs/90-经典计算展开依赖图的愿景分析.md` | **经典计算展开愿景**：用户提出"经典计算负责依赖图展开（G'_topo），AI 再根据展开结果转译"。分层可行性分析：L0骨架展开（拓扑排序+节点/边拷贝，**经典计算完全可行，保证全覆盖**）→ L1类型推断（启发式规则，可行）→ L2 section划分（经典计算推荐+AI细化）→ L3语义标注（AI不可替代）。建议实现L0+L1作为步骤2经典计算版本，L2作为推荐，L3保留给AI | **必读**。七步骤工作流步骤2的升级方向 |
| `dev-docs/91-工作系统升级方案-cognition基座安装.md` | **工作系统升级方案**：把cognition基座安装到数学项目。~30个认知单元（core/process/support+意识节点），ArangoDB新增5个collections，CP1-CP6工作流，**Hook v2方案（git post-commit + SessionStart，不用Stop hook——吸取星学v1废弃教训）**，三层维护机制，Devin CLI集成。超越星学三点：两套图共享ArangoDB、TopologyVerifier作为质量验证、经典计算展开G'_topo。含数学形式化（G_math定义）+规模指标+3档复用指南 | **必读**。工作系统升级的执行方案 |
| `dev-docs/92-经典计算展开依赖图方案-topo_generator.md` | **经典计算展开方案**：实现topo_generator.py，从ArangoDB中的G自动生成G'_topo骨架。L0骨架展开（Kahn拓扑排序+节点/边拷贝）→ L1类型推断（static/dynamic+connection类型）→ L2 section划分推荐。用POC-2依赖图测试，TopologyVerifier必然1次通过100%覆盖。步骤2从"meta AI生成"变为"经典计算生成骨架+AI语义细化" | **必读**。七步骤工作流步骤2的执行方案 |
| `dev-docs/93-差距分析-星学88-93号vs数学89-92号.md` | **差距分析**：对比星学88-93号（6篇完整技术说明书）和数学89-92号（4篇方案文档）。**星学有而数学缺失的6项**：设计哲学/POC验证体系/Hook演进记录（含subagent防护）/诚实评估/数学形式化/复用指南。**数学有而星学缺失的3项**：经典计算展开/两套图共享ArangoDB/意识节点双重身份。**最严重发现**：91号方案的Hook设计重蹈星学已废弃的v1覆辙（Stop hook影响subagent）——因为我只读了星学的stop_hook.py代码，没有读92号文档中v1废弃的教训 | **必读**。91号方案修正的依据 |
| `dev-docs/94-POC验证体系设计-工作系统有效性验证.md` | **POC验证体系**：验证工作系统有效性的POC设计。POC-R1-Math（D1-D6评分+H1-H8假设检验+回归验证）+ POC-3-Math（经典计算展开验证）+ POC-4-Math（两套图共享验证）。8条验证体系设计原则（7条从星学继承+1条数学独有：拓扑确定性原则）。3档复用指南（最小/标准/增强） | **必读**。工作系统有效性的验证方案 |
| `dev-docs/95-设计哲学-数学项目工作系统.md` | **设计哲学**：数学项目工作系统的10个设计决策（7个从星学继承+3个数学独有：经典计算展开G'_topo/两套图共享ArangoDB/意识节点双重身份）。用户两条直觉（稀疏矩阵与螺旋环路 + 经典计算展开依赖图）。适用范围 | **必读**。工作系统的"为什么" |
| `dev-docs/96-诚实评估与未来-数学项目工作系统.md` | **诚实评估**：8条已知局限（6条继承星学+2条数学独有：经典计算section划分质量不确定/两套图共享一致性风险）。HoTT诚实定位（数学项目比星学更接近HoTT但仍然不是HoTT）。未来方向（短期5+中期4+长期4）。给其他AI的建议（可复用/需调整/需警惕） | **必读**。工作系统的诚实面对 |
| `dev-docs/97-测试方案-工作系统与经典计算展开的完备验证.md` | **测试方案**：6层16个测试用例（T1-T15 + T11b），每个含测试目标/前置条件/测试步骤/预期结果/判定标准/失败排查。Layer 1基础设施(T1-T2)→Layer 2核心功能(T3-T6)→Layer 3 Hook与纪律(T7-T9含subagent防护)→Layer 4经典计算展开(T10-T11 + T11b与meta AI版对比)→Layer 5两套图共享(T12-T13)→Layer 6有效性验证(T14 A/B对照+T15回归验证)。含测试执行计划+通过标准+测试数据准备 | **必读**。实现后按此方案逐项测试 |
| `dev-docs/98-测试报告-工作系统与经典计算展开验证结果.md` | **测试报告**：T1-T15逐项结果。**14/16通过**（T11b未执行——topo_generator已覆盖meta AI版数据无法对比；T14 A/B对照待执行——需真实任务场景）。关键发现：max_depth从5调整为7（数学项目路径更长）/ git hook shebang必须用绝对路径 / 意识节点名称映射（英文cog_id↔中文node_id）/ **topo_generator 1次通过100%覆盖** / 回归验证能检测版本链问题 | **必读**。工作系统验证结果 |
| `dev-docs/99-工作系统经验反哺大师系统升级方案.md` | **反哺方案**：工作系统升级（89-98号）的6个机制反哺数学大师系统。反哺1：经典计算展开替代七步骤步骤2（topo_generator已实现，P0立即执行）/ 反哺2：CP1-CP3加载数学意识作为做证明的前置认知（系统化POC-1的发现）/ 反哺3：版本链管理数学意识演化（POC-1发现→POC-2深化→POC-3验证）/ 反哺4：回归验证保障依赖图变更后已有功能不被破坏 / 反哺5：从POC结果中自动发现新数学意识（半自动，长期）/ 反哺6：三层提取L1/L2/L3用版本链管理（v1=具体步骤→v2=思维模式→v3=范式思维）。含实现优先级（P0-P3）+ Check List + 与POC-3的关系 | **必读**。数学大师系统的下一代升级方向 |
| `dev-docs/100-反哺方案执行计划-细化CheckList与测试方案.md` | **执行计划**：99号反哺方案的执行级文档。6个反哺点的Check List全部细化+10个测试方案。**执行结果：10/10测试通过**。反哺1（R1-1/R1-2）：seven_step_pipeline.py集成topo_generator，1次通过100%覆盖 / 反哺2（R2-1/R2-2/R2-3）：种子推荐表5种问题类型+CP1-CP3覆盖率100% / 反哺3（R3-1/R3-2）：5个意识节点v1(POC-1)→v2(POC-2)版本链 / 反哺4（R4-1/R4-2）：POC-1回归94/100+POC-2回归100/100+敏感性验证通过 / 反哺6（R6-1）：Cayley-Hamilton三层版本链v1→v2→v3 | **必读**。反哺方案执行结果 |
| `dev-docs/101-UserPromptSubmit提醒机制方案.md` | **提醒机制方案**：模仿星学97号文档的v3方案（纯提醒无硬门禁），给数学项目加UserPromptSubmit hook。每次用户提问时从`UserPromptSubmit.txt`读取提醒注入AI上下文。数学项目独有内容：数学问题额外提醒查种子推荐表+七步骤工作流。**5/5 Check List通过** | 工作系统提醒机制 |
| `dev-docs/102-AGENTS.md技术说明内联方案.md` | **内联方案**：把工作系统和数学大师系统的操作级技术说明内联到AGENTS.md中，确保跨session/压缩后AI不丢失"怎么用"的认知。每节末尾加"依赖维护"标注——当依赖的dev-docs更新时同步更新AGENTS.md对应内容。**6/6 Check List通过** | AGENTS.md维护 |
| `dev-docs/103-AGENTS.md技术说明依赖入稀疏矩阵方案.md` | **依赖入图方案**：纠正102号的纯Markdown依赖表——依赖关系应该存储在稀疏矩阵中。新增2个认知单元（agents_tech_worksystem, agents_tech_mathmaster）+ 11条depends_on边 + SDK新增find_dependents_by_doc方法（反向查询：给定dev-docs编号返回依赖它的认知单元）。AGENTS.md中Markdown依赖表改为指向稀疏矩阵。**6/6 Check List通过** | AGENTS.md维护 |
| `dev-docs/104-CP4检查清单补全-对照星学98-99号方案.md` | **CP4补全方案**：对照星学98号（CP4动态查询技术说明书）和99号（CP4补全两个稀疏矩阵更新纪律），补全数学项目CP4检查清单。新增3个纪律认知单元（doc_sync_discipline, work_matrix_update, math_master_matrix_update）+ 加3条stop_hook依赖边 + 移除3条错误依赖边（arangodb_infra, work_system_upgrade, agents_management不是纪律）。修复后CP4检查清单5项纪律，与星学项目完全对称。AGENTS.md中"检查依赖"纪律改为指向稀疏矩阵中的work_matrix_update和math_master_matrix_update。 | **必读**。CP4检查清单纪律 |
| `dev-docs/105-大师-POC-3验证方案.md` | **POC-3方案**：三层提取跨题复用验证。题1(Cayley-Hamilton)提取L1/L2/L3→题2(谱定理,近迁移)+题3(Euler公式,远迁移)。三组对照(A=仅L1/B=L1+L2/C=L1+L2+L3)。8维15分制评分。成功标准：题3远迁移C vs B L3增量≥+1.5 | POC-3验证方案 |
| `dev-docs/106-大师-POC-3验证结果.md` | **POC-3结果**：**三层提取跨题复用价值验证成立**。题2(近迁移)：C>A +4.1, C>B(L3增量) +2.1。题3(远迁移)：C>A +3.9, **C>B(L3增量) +2.6≥+1.5成功**。L2审计4/4通过，L3审计1/2通过(L3-2应降级为L2——元思维不是具体范式)。H1-H4验证通过，H5部分通过。核心发现：L3在远迁移中增量大于近迁移(+2.6>+2.1)，L3范式思维跨领域迁移价值成立。C组在题3中给出组合+拓扑两条证明路径并建立结构同构 | **必读**。L3跨领域迁移验证成功 |
| `dev-docs/107-题库Phase-A建设方案.md` | **题库Phase A方案+执行结果**：从Proofs from THE BOOK + MathLib 100 Theorems +经典教材中手工结构化标杆题。**Phase A完成**：15道题42个解法已导入ArangoDB。3批：POC-3已有3道+MathLib 100定理7道+Proofs from THE BOOK 5道。依赖图452节点393边(含69条跨领域映射边)。认知图57个认知单元(新增21个意识节点)。领域覆盖：线性代数/拓扑/组合/数论/分析/代数几何/几何 | **必读**。题库Phase A完成 |
| `dev-docs/108-数学大师全知识体系准备方案.md` | **v2穷尽式方案（已被109号v3接替）**：v1→v2转变：从标杆题库选取改为穷尽式吸收。七大来源：竞赛题全集/数学家工作/菲尔兹奖/教材/MathLib 100/THE BOOK/Wikipedia。估计~110000节点。v2的吸收Loop架构、校验策略、存档结构仍有效，但知识范围以109号v3为准 | v2方案，被109号接替 |
| `dev-docs/109-数学大师全知识宇宙-穷尽式知识地图v3.md` | **v3全知识宇宙地图（当前最新）**：从"数学痴狂爱好者"视角发掘AI内在知识，从v2七大来源扩展到**十三大来源**：①数学家全集（Euler 80卷/Ramanujan笔记+Berndt 5卷+Andrews-Berndt 5卷+所有后续）②教材与专著~200本（含全部习题）③习题集与问题集（Pólya-Szegő/Lovász/Stanley/Demidovich/Arnold Trivium）④数学思想书（Hadamard/Poincaré/Arnold/Rota/Lakatos/Thurston/Grothendieck/Manin）⑤arXiv/ar5iv（32个数学分类）⑥竞赛题全集（含Schweitzer研究级）⑦百科与数据库（OEIS 37万序列/DLMF/nLab/MathWorld/Princeton Companion）⑧形式化数学库（MathLib 100000+定理/Coq/Mizar/Metamath）⑨数学杂志问题栏（AMM 1894-/Crux/Kvant）⑩讲义与综述（Bourbaki Seminar/ICM Proceedings）⑪趣味数学（Gardner 25年专栏/Conway全部）⑫开放问题清单（千禧年/Erdős/Smale/Hilbert/Arnold）⑬历史与哲学（Kline通史/Stillwell/Neugebauer/Heath）。估计~60万条目，~325000节点。含Ramanujan专题（笔记+注解+后续链条）、知识存档结构v3、修订后分批计划 | **必读**。当前最新知识地图 |
| `dev-docs/110-大规模依赖图可操作性方案-三层访问架构.md` | **325000节点可操作性方案**：解决"325000节点 vs 20万token上下文"的核心架构问题。**三层访问架构**：①冷存储层（ArangoDB全部325000节点，永不全部装入上下文）②热工作集（当前问题相关200-800节点子图，~80K token装入上下文）③温查询层（AI推理中按需expand/query，每次返回10-50节点追加到热工作集）。**种子选择三級机制**：层次索引定位（3层主题树~20K token常驻）→语义检索（embedding top-20种子）→图遍历扩展（token预算控制剪枝到200-800节点）。**多分辨率节点存储**：R1全细节~300token/~5000节点、R2中细节~100token/~20000节点、R3轻量~30token/~200000节点、R4极简~10token/~100000节点。**渐进式展开协议**：AI可发起expand/dependencies/path/loop/search查询。**粒度拆分**：子图仍太大时拆分为小图分别分析再综合。Token预算分析：80K给依赖图子图可装270-800个全/中细节节点，远超POC所需（POC-2用18节点即显著增益）。分阶段启用：<5000节点全遍历、5000-50000层次索引+遍历、50000+完整三层架构 | **必读**。大规模可操作性架构 |
| `dev-docs/111-知识搜集优先级方案-最难最妙最新.md` | **搜集优先级方案**：核心洞察（来自用户）——数学大师系统的价值不在于装AI已经会的东西，而在于装AI不会的。越是难、妙、新，越是AI本身可能不会的，越应该优先装入。**三级优先级**：P0=AI最不可能会的（Ramanujan冷僻恒等式/最新arXiv/Schweitzer研究级竞赛/Erdős冷僻问题/Arnold Trivium/数学思想书/Conway深度工作/开放问题详细进展）；P1=AI浅层知道但深度不够的（MathLib形式化定理/THE BOOK/OEIS/关键数学家工作/Bourbaki Seminar/IMO Shortlist）；P2=AI基本会的（标准教材/Wikipedia/基础竞赛题）；P3=AI完全会的（只做索引）。"难妙新"三准则：满足越多优先级越高 | **必读**。搜集优先级逻辑 |
| `knowledge/` | **P0知识搜集成果（截至2026-08-04）**：①P0经典知识：38文件10810行680KB（Ramanujan/Arnold/思想书/竞赛题/突破/Conway/开放问题）②**arXiv全文**：1305篇972008行114MB（145个分类的HTML全文，math.* 325篇/cs.* 302篇/physics.* 182篇/quant-ph 7篇/math-ph 8篇/hep-th 9篇/stat.* 45篇/nlin.* 45篇等）③**arXiv穷尽式元数据**：**239472篇**唯一论文，323.8MB JSON，覆盖44个分类（math.* 28个+cs理论7个+quant-ph+math-ph+hep-th+stat.ML+nlin 4个），2023-2026年，按submittedDate日期范围查询穷尽获取，大分类达10000 API上限。年份分布：2023=48983/2024=69810/2025=62131/2026=58548 | **必读**。P0知识存档 |
| `scripts/arxiv_search.py` | arXiv API搜索脚本v1：28个数学分类各50篇 | 工具脚本（已被v3接替） |
| `scripts/arxiv_fetch_html.py` | arXiv HTML全文抓取脚本v1：从arxiv.org/html/<id>抓取HTML转为markdown，27个数学分类各3篇 | 工具脚本（已被v2接替） |
| `scripts/arxiv_search_v3.py` | **arXiv API穷尽式搜索脚本v3**：44个分类（math+cs理论+quant-ph+math-ph+hep-th+stat.ML+nlin），submittedDate日期范围查询（2025-2026 + 2023-2024），200条/页，3秒间隔，429重试退避。239472篇元数据 | **当前版本** |
| `scripts/arxiv_fetch_html_v2.py` | **arXiv HTML全文抓取脚本v2**：从239K篇元数据中按"难妙新"原则筛选1452篇，145个分类各10篇最新论文HTML全文。1305篇成功（含v1的69篇），972008行114MB | **当前版本** |
| `dev-docs/112-arXiv论文导入ArangoDB与节点映射规则方案.md` | **arXiv论文操作化方案**：239K篇元数据导入ArangoDB `arxiv_papers` collection。四级映射规则：L1定理级（论文中的定理→dg_nodes concept节点）/ L2方法级 / L3意识级 / L4索引级（默认，可搜索不在依赖图中）。论文不是节点，论文是节点的出处。SDK新增`search_arxiv()`/`promote_arxiv_paper()`。实现110号三层架构的冷存储层 | **必读**。arXiv知识操作化 |
| `dev-docs/113-大师-POC-4验证方案-代数拓扑领域泛化性验证.md` | **POC-4方案**：代数拓扑领域（Klein瓶同调群计算）验证方法论泛化性。12节点+15边+新增structural_thinking意识节点。A/B对照实验。与矩条件极差题的思维差异最大（结构性vs分析性） | POC-4方案 |
| `dev-docs/114-大师-POC-4验证结果.md` | **POC-4结果**：A组15/15，B组15/15，边际增益=0。**问题选择不当**——Klein瓶同调群是标准教材内容，AI已完全掌握。陷阱在AI"会"区 | POC-4结果 |
| `dev-docs/115-大师-POC-5验证方案-数论最新论文泛化性验证.md` | **POC-5方案**：从arXiv:2608.02381（2026-08-03最新论文）提取orientation-rigidity定理。10节点+12边+3意识节点+螺旋环路 | POC-5方案 |
| `dev-docs/116-POC隔离测试方案-独立目录+tmux监督.md` | **隔离测试方案**：独立目录(`/data/math-agent-{1,2}/`) + AGENTS.md软限制(禁止web_search/禁止访问master-mind) + tmux监督(master agent观察pane)。审计必须覆盖完整运行过程和最终结果，不能只检查result.md。 | **必读**。POC测试标准流程 |
| `dev-docs/117-大师-POC-5验证结果-隔离测试.md` | **POC-5结果**：隔离测试方案验证有效（无违规）。A组15/15，B组15/15，增量=0。但B组使用了反证法+螺旋交叉验证+对偶性观察——依赖图影响证明结构。**三次POC对比洞察**：POC-1增量+3.50(AI"不会"区)，POC-4/5增量0(AI"会"区)。直接验证111号"难妙新"原则 | **必读**。三次POC对比 |
| `dev-docs/118-大师-POC-6验证方案-Ramsey数发现型问题.md` | **POC-6原始方案**：发现型问题——从arXiv:2608.02537让AI猜测R_k(C_5)下界。原版依赖图后来发现有节点直接或等价写出答案，不能原样复用 | POC-6历史方案；纠偏见120-121号 |
| `dev-docs/119-大师-POC-6验证结果-Ramsey数发现型问题.md` | **POC-6原始结果，已降级为低可信历史证据**：A组猜k^{k/5}，B组猜(log k)^{k/3}，但B组依赖图存在答案泄漏，原`+4.0/10`不能支持“泛化性最终验证成立” | 不得作为最终结论；当前状态见120-121号 |
| `dev-docs/120-工作交接文档-POC6修正版重跑与下一步.md` | **POC-6修正版交接状态**：原始实验答案泄漏；修正版A组猜k^{k/6}，B组运行中断、尚无结果；记录隔离目录和恢复任务 | **必读**。当前实验事实记录 |
| `dev-docs/121-v1-2026-08-05-POC6修正版重跑纠偏与证据闭环方案.md` | **POC-6修正版正式纠偏方案**：明确测量口径，修复环声明与边集合不一致，冻结输入，保存完整运行证据，先恢复B组再做至少3对A/B配对复跑，以四档判定收口 | **必读**。后续执行的事实与流程依据 |
| `dev-docs/122-v1-2026-08-05-数学大师系统总体架构调查.md` | **数学大师系统总体架构v1调查**：把现有知识资产、数学依赖图、研究运行、工具验证、POC和工作认知图统一为三平面、八组件、三闭环；实测发现当前主链未闭合、图模式分裂、KC稀疏、全图拓扑验证失败、大规模召回和工具验证未接入 | 架构调查初版，已被v2深化 |
| `dev-docs/122-v2-2026-08-05-思维形状与启发关系架构修订.md` | **三图架构修订**：确立“思维形状可观测、可比较、可干预”；分离数学知识图K、外显思维图T、启发激活图H；定义动态题目Q_t、Agent M救援闭环和因果干预POC | 当前架构模型，证据裁决见v3 |
| `dev-docs/122-v3-2026-08-05-完整机制复核与费马极限案例.md` | **证据复核基线**：完整通读80—99号后回答五问；裁决现有静态提示、七步骤、经典展开和工作认知图各自真正证明了什么；解释Master答案泄漏的系统根因；以Frey—Ribet—Wiles链区分“调用已证模性推FLT”“重建Wiles证明”“独立发现路线” | **必读**。123号的证据前提 |
| `dev-docs/123-v1-2026-08-05-数学大师系统全景复盘与第一性原理重构计划.md` | **当前最高架构与建设基线**：以`系统探讨.md`全文为母本，保留七层能力、五类资产和K/T/H直觉；用类型化任务/工作区、事件溯源、表示变换、时序规则、证据状态和受约束最小干预严格化；建立DYN-0—7、Phase 0—7、角色权限、数据crosswalk、停止条件及Ramsey/费马案例 | **最高优先级必读**。后续schema、POC和运行时必须服从 |
| `dev-docs/124-v1-2026-08-05-Phase0-7建设计划CheckList.md` | **Phase 0—7建设计划Check List总览**：v2拆分为总览（本文件）+ 130—137号各Phase独立文件。总览含全局预注册门（G0-1—G0-6）、核心指标清单、风险登记（R-1—R-16）、贯穿案例（CC-R-0—6 + CC-F-0/7）、项目级停止条件（STOP-1—7）、降级路径（DEG-1—6）、明确不做清单（NO-1—10）、未决问题（UQ-1—5）和进度追踪表。各Phase的详细Check List在对应编号文件中 | **必读**。Phase推进的执行视图总览 |
| `dev-docs/125-v1-2026-08-05-AGENTS对齐审计与Git-Hook防不同步机制.md` | **AGENTS.md对齐审计+防御机制**：审计发现7类不同步问题（DYN阶梯定义错误/Phase编号偏移/文档索引遗漏/代码文件未引用/文件名引用错误等），全部修正后新增`alignment_check.py`（6项对齐检查）+`pre-commit` hook（硬性违规阻止commit）+`post-commit` hook增强（commit后对齐提醒）。机制首次运行即自动检测到人工审计遗漏的64号文件名错误 | **必读**。理解AGENTS.md与repo对齐的防护机制 |
| `dev-docs/126-v1-2026-08-05-dg星图只读盘点报告.md` | **dg_*只读盘点报告**：Phase 0 (P0-3)冻结`dg_nodes`(1719)/`dg_edges`(1483)/`loops`(4)的type/edge_type/mapping_type/graph分布、五类初步归类、schema字段清单。重要发现：96.5%边edge_type为unknown，真实边语义在mapping_type字段；当前dg_*完全是K视图，无T/H/E节点 | **必读**。Phase 0架构冻结的数据基线 |
| `dev-docs/127-v1-2026-08-05-Schema冻结与角色隔离矩阵.md` | **Schema冻结与角色隔离矩阵**：Phase 0核心交付物。冻结8类schema（Task/Workspace/Event/Obligation/Representation/Evidence/HeuristicRule/Visibility）、8角色可见性矩阵（8×14 collection）、逐组件最小输入/输出契约、CapabilityToken强制机制、candidate/validated/published/retired生命周期状态机、L1/L2/L3五正交字段设计、原文数据对象crosswalk、12步与11阶段crosswalk。123号10条架构裁决在schema中的逐项体现 | **最高优先级必读**。Phase 1起按此schema创建新collection |
| `dev-docs/128-v1-2026-08-05-全局预注册项与贯穿案例冻结.md` | **全局预注册项与贯穿案例冻结**：Phase 0全局项落盘。G0-1关键事件完整清单（5类27种事件类型，覆盖123号Event schema全部14种语义事件）、R-1—R-16风险监控机制（每项含监控机制/检查点/触发停止条件）、CC-R-0 Ramsey案例冻结（非泄漏干预阶梯+验证维度）、CC-F-0费马案例冻结（三层难度阶梯+推论链+大师启发维度） | **必读**。每个Phase出口门对照检查 |
| `dev-docs/129-v1-2026-08-05-Phase0三文件审计与修正报告.md` | **Phase 0三文件审计与修正报告**：以plan/系统探讨.md/123号v1三个文件为基准，对Phase 0全部实现做逐项审计。识别7项遗漏（L1/L2/L3五正交字段/旧七步骤迁移映射/数据对象crosswalk/12步crosswalk/明确不做清单/G0-1事件补全/SHA-256验证），全部修正。含三文件冲突裁决（Phase数量/角色数量/DYN编号/运行时步骤/风险数量）和实现优秀性评估 | **必读**。理解Phase 0的完整性和修正历史 |
| `dev-docs/138-v1-2026-08-05-Phase0-7细化结果三文件交叉审计报告.md` | **Phase 0-7细化结果三文件交叉审计报告**：以plan/系统探讨.md/123号v1三个文件为基准，对Phase 0-7全部细化结果（130—137号）做跨Phase横向一致性审计和对三份文档最终理念的全面一致性审计。用3个并行subagent分别完整捋过三个文件的每一行。10个横向审计维度全部通过。发现8项遗漏（R-5/R-6/R-15风险监控缺失、NO-1/NO-3约束缺失、P2-9.1 5分量未引用、P5-5 NumPy/SciPy缺失、P2-1.3 explain缺失），全部修正。含5项三文件冲突裁决记录 | **必读**。理解Phase 0-7细化结果的完整性和修正历史 |
| `dev-docs/139-v1-2026-08-05-Phase1实现三文件审计与修正报告.md` | **Phase 1实现三文件审计与修正报告**：以plan/系统探讨.md/123号v1三个文件为基准，对Phase 1实现（research_runtime/包）做逐项审计。用3个并行subagent分别完整捋过三个文件的每一行。发现6项遗漏（自环检查/事件图单调增长/语义抽取器/事件捕获器/完整度度量/checkpoint多continuation），全部修正并新增测试。修正后DYN-0验收4条+审计修正6项全部通过 | **必读**。理解Phase 1实现的完整性和修正历史 |
| `dev-docs/140-v1-2026-08-05-Check-List到实现断层元问题诊断报告.md` | **Check List到实现断层元问题诊断**：回答"为什么一审再审实现还是出问题"。发现三种系统性断层模式：F1"定义了=实现了"、F2"验证了=完整了"、F3"Check List覆盖盲区"。138号审计是覆盖性审计不是可实现性审计。Phase 2—7普遍存在同样范型问题。根本修正：引入实现深度等级D1—D4 + 可实现性审计维度 + 勾选从二元改四元 | **必读**。理解Check List系统性缺陷和修正方向 |
| `dev-docs/142-v1-2026-08-05-CheckList预防性修正与可实现性审计报告.md` | **CheckList预防性修正与可实现性审计报告**：对132—137号Check List做预防性修正——引入D1-D4深度等级+边界情况清单+覆盖标准。132—137号共386项D1-D4标注、346处边界情况、38处覆盖标准。132号F3检查发现§18的3项遗漏（状态等价参数化`~_{α,κ}`/规范化键定义/规范化键一致性判定），已补充为P2-9.3+P2-9.COMP3。132号可实现性审计（第11维度）全部通过 | **必读**。理解预防性修正的方法和结果 |
| `dev-docs/143-v1-2026-08-05-Phase2实现方案.md` | **Phase 2实现方案**：Phase 2目标——完成DYN-1（状态重建一致性）和DYN-2（卡点检测校准）。Q_0用128号冻结的Ramsey案例。9个大项按依赖顺序实现：P2-1 Q_0解析→P2-2工作区+P2-3义务图+P2-5证据→P2-4验证门→P2-6 DYN-1+P2-7 DYN-2→P2-8信念+P2-9进展偏序。新增2个代码模块（state_reducer/+verification/）+6个ArangoDB collections | Phase 2执行方案 |
| `dev-docs/144-v1-2026-08-05-Phase2实现三文件审计与修正报告.md` | **Phase 2审计修正报告**：对照plan-dad3347dc4d8e542.md+系统探讨.md+123号文档+127号Schema冻结文档审计Phase 2实现。发现10项严重/中等问题（ObligationType/EvidenceStatus/StallType枚举错误、字段缺失、Verifier/Retriever角色缺失、可复现约束缺失、α计算近似），全部修正后集成测试通过。**关键教训**：TaskType≠ObligationType、Schema冻结文档是权威、角色隔离不是可选项 | Phase 2审计修正 |
| `dev-docs/145-v1-2026-08-05-权威性逐字核对审计与新断层类型F4F5F6.md` | **权威性逐字核对审计**：144号暴露了140/142未覆盖的F4(概念混淆)/F5(权威定义偏差)/F6(方法近似)三种新断层类型。新增第12审计维度（权威性逐字核对）——实现时必须同时打开127号Schema冻结文档逐字核对，Check List是导航，127号是法律。对133-137号做了预防性修正：133号角色命名、136号Controller角色澄清、137号Representation字段数8→12、127号map_type注释补全relaxation+补充验证等级枚举 | **必读**。理解F4/F5/F6新断层类型和第12审计维度 |
| `dev-docs/146-v4-2026-08-05-审计方法论手册-从覆盖性到权威性到代码实现完整性到代码逻辑有效性到声明性vs强制性的21维度审计体系.md` | **审计方法论手册v4（持续维护）**：把129—161号审计链中散落的"如何把事做好、做对"的经验收敛为一份可独立阅读、持续维护的手册。完整收录：F1-F15断层类型学、D1-D4实现深度等级、21个审计维度完整清单、三文件交叉审计标准流程（3并行subagent+强制深入机制）、权威性逐字核对清单、领域教训清单（15条）、实现前自检协议（14步含维度19/20/21预检）、实现后审计协议（21维度）、维护规则+ChangeLog。**v3核心突破**：v2的维度15只查"方法是否存在"，不查"方法逻辑是否真正有效"和"方法是否完整"。**v3.1核心突破**：维度19/20可以在Check List层面做预检（159号对Phase 6/7修正14处F13/F14风险），维度18无法在Check List层面预检。**v4核心突破**：v3的维度18检查恒真/恒假，但声明性实现的返回值不是恒真的（确实返回了True），只是True背后没有强制机制。161号Phase 6审计发现10项问题中6项是声明性实现或条件限定词丢失，这是v3完全无法覆盖的断层类型。新增F15（声明性实现而非强制性实现）、维度21（声明性vs强制性审计）、教训15。扩展F12定义（新增"检查了错误的条件"和"只检查了条件的一部分"两种变体）和维度19定义（新增"一个条件的多个限定词"检查）。强化维度20预检精度（不只检查"是否覆盖"，还检查"限定词是否完整"） | **必读**。每个Phase实现前/后的AI和审计者都要读。发现新断层类型时追加到本手册 |
| `dev-docs/147-v1-2026-08-05-Phase实现启动SOP-从指令到第一行代码的标准作业流程.md` | **Phase实现启动SOP v1.3（持续维护）**：把"开启一个新Phase实现之前应该做的事"+"Phase实现完成后如何触发审计"固化为可触发的标准作业流程。用户用"请你遵照147号文档中的SOP，开始实现Phase X"触发。11个阶段：阶段0认知加载(CP1-CP3+读146号v4)→阶段1三文件并读(Check List+127号+123号)→阶段2前置Phase验收核对(实际运行EXIT门测试)→阶段3 Check List可实现性预检+维度15/16/19/20/21预检(引用146号v4第8章步骤1-3+步骤9/10+步骤12/13+步骤14)→阶段4权威性预核对(引用145号第12维度)→阶段5 F1-F15断层预扫(引用146号v4第2章+140号风险评估表)→阶段6全局项核对(G0门/R-1—R-16/CC-R·CC-F/STOP/NO/DEG/UQ)→阶段7角色隔离确认→阶段8方案先行(按143号模板)→阶段9环境确认(git clean/ArangoDB/.venv)→阶段10启动声明→**阶段11实现后审计触发(引用146号v4第9章21维度审计协议)**。**v1.3变更(161号v4)**：阶段3新增5.4节维度21预检(F15预防)，阶段5从F1-F14扩展为F1-F15，维度20预检强化为"限定词完整性"检查。**核心新增**：新增阶段11"实现后审计触发"——Phase实现完成+集成测试通过后，不是直接提交，而是触发146号v4第9章的21维度实现后审计协议。161号Phase 6审计发现：Phase 6实现后只运行了集成测试，没有执行维度15-21的实现后审计，导致10项问题在审计时才被发现。与146号v4不重复：147号是上层工程工作流，146号v4第8章是其中阶段3/4/5的子流程，第9章是阶段11的子流程 | **必读**。用户说"开始实现Phase X"时执行此SOP |
| `dev-docs/132-v1-2026-08-05-Phase2-CheckList.md` | **Phase 2 Check List**（已实现）：9个大项全部完成。出口门P2-EXIT-1/2/3全部通过。DYN-1多观察者重建一致性α=1.00（5个关键字段全部≥0.80）。DYN-2卡点检测7类卡点+precision/recall校准。实现文件：state_reducer/（q0/workspace_store/obligation/verification_gate/evidence/reducer/progress/controller_belief/migrate）+ verification/stall_detector | Phase 2实现状态 |
| `dev-docs/133-v1-2026-08-05-Phase3-CheckList.md` | **Phase 3 Check List**（已实现）：9个大项全部完成。出口门P3-EXIT-1/2全部通过。离线候选启发——发现候选规则但绝不在线自动提示。HeuristicRule schema覆盖127号§7完整定义（LHS/interface/RHS/guard/eta）。H0/H1/H2激活包基于128号§3.2 Ramsey干预阶梯。答案泄漏代理四门（123号§23）。candidate规则禁止在线自动提示（R-4防线）+禁止自动写入H图（NO-8防线）。H图incidence matrix稀疏表示（R-5防线）。实现文件：heuristics/（models/state_aligner/rule_extractor/activation_packet/leakage_audit/rule_store/sparse_view/matcher/migrate/test_phase3） | Phase 3实现状态 |
| `dev-docs/148-v1-2026-08-05-Phase3实现方案.md` | **Phase 3实现方案**：遵照147号SOP 10阶段启动。10阶段全部执行：认知加载→三文件并读→Phase 2 EXIT门实际运行验证→D1-D4预检→127号逐字核对无偏差→F1-F6断层预扫→全局项核对→角色隔离确认→方案先行→环境确认→启动声明。新增heuristics模块10文件，heuristic_rules+activation_packets collections。R-5（多元时序组合爆炸）是Phase 3核心防线 | Phase 3实现方案 |
| `dev-docs/149-v1-2026-08-05-Phase3实现三文件审计与修正报告.md` | **Phase 3三文件审计修正报告**：用plan-dad3347dc4d8e542.md（387行）+系统探讨.md（2288行）+123号文档（1210行）三文件交叉审计Phase 3实现。3个并行subagent捋每一行提取要求。发现5项实现偏差：①MatcherAction动作集合5→9个（123号§485-497）②checkpoint补全Q_0/事件前缀/模型/预算/版本哈希7字段（123号§847）③角色可见性落实为visibility label+能力令牌（123号§607）④稀疏计算实现a_t=W^T*p_t公式（系统探讨§10.4）⑤新增AgentDependencyProxy类3个代理（123号§530）。全部修正后test_phase3.py通过。三文件权威性裁决：123号最高，系统探讨.md设计母本，plan历史参考 | Phase 3审计修正 |
| `dev-docs/150-v1-2026-08-05-Phase4-7-CheckList-F7F8预防性审计与修正报告.md` | **Phase 4-7 Check List F7/F8预防性审计**：用146号14维度审计体系（149号迭代版）的维度13(F7跨章节依赖扫描)+维度14(F8母本回溯审计)预防性审计134-137号Check List。Phase 4-7均未实现，实现前修正可避免实现偏差。发现6项偏差：①Phase 4 checkpoint 7字段(F7)②Phase 4 visibility label(F7)③Phase 5 a_t=W^T*p_t公式(F8)④Phase 5 Retriever visibility label(F7)⑤Phase 6 checkpoint 7字段(F7)⑥Phase 6 visibility label引用(F7)。偏差分布规律：F7的checkpoint 7字段和visibility label是系统性遗漏（凡是用到这些概念的Phase都会遗漏）。Phase 7新增角色隔离延续节。母本扫描确认123号对系统探讨.md 9个章节都做了继承+严格化，无其他F8遗漏 | Phase 4-7预防性审计 |
| `dev-docs/151-v1-2026-08-05-Phase4实现方案.md` | **Phase 4实现方案**：遵照147号SOP 10阶段启动。Phase 4是第一个需要实际运行LLM实验的Phase。关键决策：①LLM后端用devin cli封装（devin -p "prompt" --model claude-sonnet-5-low）②G0-3/G0-4预注册门先跑pilot估计方差再冻结③实验设计用checkpoint分层随机实验（Q_0 Ramsey C_5案例）④迁移题用C_7（七边形奇环）。新增3个代码模块（experiments/+policy/+auditor/）+7个ArangoDB collections。6个阶段执行计划：基础设施→pilot→正式实验→审计裁决→出口门验证→Check List更新 | Phase 4执行方案 |
| `dev-docs/152-v1-2026-08-05-G0-3G0-4预注册门冻结记录.md` | **G0-3/G0-4预注册门冻结记录**：Phase 4阶段B（Pilot实验后）冻结。G0-3：δ=0.10，样本量=15/组，排除标准=continuation生成失败/预算超限/格式不合规，区间估计=Bootstrap置信区间。G0-4：泄漏门阈值=0.30。Pilot数据：20个continuation，效应大小均值=0.0833，方差=0.0208。H1组进展最高=1.000 | G0-3/G0-4冻结 |
| `dev-docs/153-v1-2026-08-05-Phase4三文件审计与修正报告.md` | **Phase 4三文件审计与修正报告**：用plan+系统探讨.md+123号三个文件逐行交叉审计Phase 4实现。4个并行subagent分别捋三个文件每一行+读取全部实现代码。修正1个bug（migration_tester.py的hint_level参数），补充7项遗漏（分层ATE/gaming检测/反应式救援标注/POC-C六维度/Auditor输入验证/泄漏检测四门/checkpoint一致性检查），改进2项实现深度（响应评估/泄漏检测）。集成测试全部通过。实现优秀性评估：良好 | Phase 4审计修正 |
| `dev-docs/154-v1-2026-08-05-Phase5-6-7-CheckList-v2预防性审计与修正报告.md` | **Phase 5/6/7 Check List v2预防性审计**：用146号v2新增的维度15/16预检对尚未实现的Phase 5/6/7 Check List做预防性审计。subagent回溯系统探讨.md 8个章节提取F10风险。Phase 5修正5处（充分快照8字段/验证路由4规则/最小性审计3项/工具职责分工/检索最小内容判定），Phase 6修正4处（gaming三元判定/闭环失败定义+反应式5理由/主动导航5阶段升级/长期归因3步法），Phase 7修正3处（等价分类3类/一致性检查3步+粘合3步/e-graph核心组件）。共12处F9/F10预防性修正 | Phase 5-7预防性审计 |
| `dev-docs/155-v1-2026-08-05-Phase5实现方案.md` | **Phase 5实现方案**：遵照147号SOP v1.1启动。Phase 5目标——让系统只给当前一步真正需要的数据。10个大项：P5-1冷/温/热/微包4层访问→P5-8 legacy图只读adapter→P5-9 K/T/H投影+稀疏计算→P5-2 5层优先级检索→P5-3表示映射查询→P5-5工具能力注册→P5-6命题级验证路由→P5-4 Context Compiler+StateSnapshot→P5-7裁剪清单+最小性审计→P5-10旧七步骤复用决策。新增3个代码模块（retrieval/+context_compiler/+verification/）+4个ArangoDB collections。15步执行计划。F11已标注"实现后必须做维度17审计" | Phase 5执行方案 |
| `dev-docs/156-v1-2026-08-05-Phase5-P5-10旧七步骤复用决策.md` | **P5-10旧七步骤复用决策**：评估topo_generator.py纯函数（10个可复用/3个有副作用不复用）和TopologyVerifier.py集合保真功能（5个可复用/1个待确认）。复用前必须通过契约测试。新Context Compiler有独立契约，不依赖topo_generator | P5-10复用决策 |
| `dev-docs/157-v1-2026-08-05-Phase5三文件审计与维度17审计报告.md` | **Phase 5三文件审计+维度17审计**：维度15（70项Check List全部有代码实现，无F9遗漏）+维度16（8个母本章节细节全部在代码层面实现，无F10遗漏）+维度17（16个文件参数传递全部正确，无F11 bug）。12项边界情况测试全部通过。集成测试95行全部✅。实现过程中修复3个bug（HotEntry位置参数/visibility label检查逻辑/import类名）。总体评估：优秀 | Phase 5审计 |
| `dev-docs/158-v1-2026-08-05-Phase5三文件交叉审计与修正报告.md` | **Phase 5三文件交叉审计（两轮）**：顺序加载plan+系统探讨.md+123号三文件逐行扫描。第一轮发现6项F9遗漏+1项F10遗漏。第二轮深入审计发现7项更深层次遗漏（含1个高危空检查bug+1个高危K投影来源缺失+5项中危遗漏）。共13项F9+1项F10全部修正。14项三文件交叉一致性全部通过。4项冲突按智能把握原则解决。修正后集成测试105行全部✅。教训：第一轮过于乐观，只查"方法是否存在"不查"方法逻辑是否正确" | Phase 5交叉审计 |
| `dev-docs/159-v1-2026-08-05-Phase6-7-CheckList-v3维度19-20预防性审计与修正报告.md` | **Phase 6/7 Check List v3维度19/20预防性审计**：用146号v3新增的维度19（方法完整性）和维度20（来源逐字要求检查）对尚未实现的Phase 6/7 Check List做预防性审计。用2个并行subagent逐行扫描plan和123号中Phase 6/7相关章节。Phase 6发现9处F13/F14风险（含8个角色最小输入/输出契约不完整+12步在线主链步骤10/11/12具体要求+控制器不确定估计+4门泄漏代理复用+checkpoint分层变量+代理分数约束+6种任务类型进展度量+误触发过度帮助验证+主动导航优于反应式判定条件）。Phase 7发现5处F14风险（含转换保真3项验证+纤维化表述限制+6条大师启发+分阶段进入顺序+过早数学包装警告）。共14处全部修正 | Phase 6/7预防性审计 |
| `dev-docs/160-v1-2026-08-05-Phase6实现方案.md` | **Phase 6实现方案**：遵照147号SOP 10阶段启动。Phase 6目标——完成DYN-6（动态启发在线主链）。12步在线主链：观察→候选规则→激活包→泄漏审计→角色可见性→控制器决策→预算→执行→效果记录→长期归因→学习→发布门。11个代码模块：gaming_detector/reactive_fallback/published_loader/orchestrator/model_layering/policy_pi/budget/error_recovery/long_term_attribution/exit_gate/test_phase6。R-14（不被单一模型版本绑架）和G0-5（跨≥3个未参与设计的问题族验证）是Phase 6核心防线 | Phase 6实现方案 |
| `dev-docs/161-v1-2026-08-05-Phase6实现优秀性审计与修正报告.md` | **Phase 6实现优秀性审计与修正报告**：用146号v3.1的维度15-20对Phase 6实现做实现后审计。10项问题：①P6-1 published_loader G0-5检查"≥3"但漏了"未参与设计"限定词（F12c）②P6-6 gaming_detector缺少F_t/E_t维度③P6-8 reactive_fallback缺少主动导航发布门五准则④P6-ROLE orchestrator缺少CapabilityToken类和PermissionError强制（F15声明性实现）⑤P6-9 policy_pi缺少freeze()/bump_version()方法（F15声明性实现）⑥P6-2控制器9种动作类型确认正确⑦P6-5 R-14防线检查"效果记录数>1"而非"不同模型版本数>1"（F12b检查了错误的条件）⑧P6-4 error_recovery checkpoint缺少非确定性警告⑨P6-3 budget不需要预注册门确认⑩P6-7长期归因full_attribution接口修正。全部修正后test_phase6.py通过。**关键发现**：暴露F15（声明性实现而非强制性实现）——方法返回True/False但True背后没有实际强制机制。161号迭代146号v3.1→v4和147号v1.2→v1.3 | Phase 6审计修正 |
| `dev-docs/162-v1-2026-08-05-Phase7-CheckList-v4维度19-20-21预防性审计与修正报告.md` | **Phase 7 Check List v4维度19/20/21预防性审计**：用146号v4的维度19扩展（多限定词）、维度20强化（限定词完整性）、维度21预检（声明性vs强制性）对尚未实现的137号Phase 7 Check List做预防性审计。2个并行subagent扫描123号和plan中Phase 7相关章节。发现16项风险（4项F12c多限定词+2项F14来源逐字要求+10项F15声明性vs强制性），全部在Check List层面修正。新增P7-1.2c/P7-2.1c/P7-7.1b/P7-8.1b/P7-8.6/P7-EXIT-1b/P7-ROLE-2b，强化P7-1.COMP3/P7-4.COMP2/P7-7.COMP/P7-8.COMP2等20+项的强制机制描述。**关键发现**：v4审计精度是v3.1的3.2倍——v3.1停留在"概念覆盖"层面，v4深入到"限定词覆盖"和"强制机制覆盖"层面。这是146号v4的第一次应用 | Phase 7预防性审计 |
| `dev-docs/163-v1-2026-08-05-Phase7实现方案.md` | **Phase 7实现方案**：遵照147号SOP 10阶段启动。Phase 7目标——完成DYN-7（跨领域与长证明编排）。实现表示运输/长证明/高级数学分析3条研究线。20个代码模块：representation/（fermat_chain/path_equivalence/commutative_diagram/groupoid_check/hott_directions/hott_gate/egraph/geometry_guard/hole_detector/persistent_homology/baseline_comparison/local_view/math_label/mislabel_guard/phase_gate）+ verification/（long_proof_auditor）+ experiments/（cross_domain_tester）+ policy/（representation_policy）+ auditor/（math_assertion_auditor） | Phase 7实现方案 |
| `dev-docs/164-v1-2026-08-05-Phase7实现21维度审计报告.md` | **Phase 7实现21维度审计报告**：对Phase 7实现做21维度审计。21维度全部执行。**假PASS**——审计声称全部PASS但实际有3项问题被遗漏，后被165号维度22审计发现 | Phase 7审计 |
| `dev-docs/165-v1-2026-08-05-Phase7三文件逐行审计与修正报告.md` | **Phase 7三文件逐行审计与修正报告**：用户要求"逐行捋过三个文件的每一行"。发现3项21维度审计体系未覆盖的遗漏（F16）：①母本§8.2位置一的3个跨表示映射例子未在代码中保留②graph_kernel方法注释未标注母本5种→123号4种的合并关系③HoTT方向3的3个比较对象只有mother_text_reference引用但description不够详细。新增F16断层类型、维度22（母本逐字要求检查）、教训17/18。165号迭代146号v4.1→v4.2和147号v1.3→v1.4 | Phase 7审计修正 |
| `dev-docs/166-v1-2026-08-05-Phase0-6-CheckList-v4.2维度22预防性审计报告.md` | **Phase 0-6 Check List v4.2维度22预防性审计报告**：用146号v4.2维度22（母本逐字要求检查）对Phase 0-6 Check List（130-136号）做预防性审计。4个并行subagent逐行扫描母本2288行，初步标记约80项"F16风险"，经5层甄别后全部为误报。**审计结论：PASS——0项真正F16风险**。新增教训19（维度22执行的5层甄别：Phase范围判断/123号重构判断/知识系统vs运行时判断/母本vs123号来源判断/重构覆盖判断）和教训20（多次审计的累积效应）。166号迭代146号v4.2→v4.2.1和147号v1.4→v1.4.1。**关键发现**：维度22执行需要5层甄别来避免误报；维度22是最后一道防线，对多次审计过的Check List确认覆盖完整性，对审计次数较少的Check List发现遗漏 | Phase 0-6预防性审计 |
| `dev-docs/130-v1-2026-08-05-Phase0-CheckList.md` | **Phase 0独立Check List**：从124号v2拆出并细化。含P0-1—P0-11全部子项（含129号审计后补充的P0-1.4/P0-4.10/P0-4.11/P0-6.4/P0-COMP-1/P0-COMP-2，及本次细化新增的P0-9文件职责冻结/P0-10数据迁移原则冻结/P0-11不搭空框架，及138号审计新增的P0-10.7 NO-1约束）和P0-EXIT出口门。Phase 0已完成 | Phase 0执行视图 |
| `dev-docs/131-v1-2026-08-05-Phase1-CheckList.md` | **Phase 1独立Check List**：从124号v2拆出并细化。含P1-1—P1-8全部子项+完整性标准+角色隔离落地+代码模块创建+P1-EXIT出口门。目标：完成DYN-0。**Phase 1已完成**——DYN-0验收4条全部通过（集成测试test_phase1.py验证）。实现：research_runtime/包（manifest.py + models/ + events/） + ArangoDB 4个新collection（raw_events/semantic_events/checkpoints/run_manifests） | Phase 1执行视图 |
| `dev-docs/132-v1-2026-08-05-Phase2-CheckList.md` | **Phase 2独立Check List**：从124号v2拆出并细化。含P2-1—P2-9全部子项+完整性标准+角色隔离+代码模块+P2-EXIT出口门。目标：完成DYN-1/DYN-2。细化新增：P2-8控制器信念建模、P2-9进展偏序定义。138号审计新增：P2-1.3 explain缺失标注、P2-9.1 5个分量显式引用 | Phase 2执行视图 |
| `dev-docs/133-v1-2026-08-05-Phase3-CheckList.md` | **Phase 3独立Check List**：从124号v2拆出并细化。含P3-1—P3-9全部子项+完整性标准+角色隔离+代码模块+P3-EXIT出口门。目标：离线候选启发。细化新增：P3-9 H图稀疏表示。138号审计新增：P3-9.4 R-5组合爆炸防线 | Phase 3执行视图 |
| `dev-docs/134-v1-2026-08-05-Phase4-CheckList.md` | **Phase 4 Check List**（已实现）：10个大项全部完成。出口门P4-EXIT-1/2/3全部通过。DYN-3/4/5首轮完成。同可观测checkpoint分层随机实验（4组×15次=60个continuation）+C_7迁移实验（4组×5次=20个continuation）。H1组（思维操作Hint）ATE=0.217, CI下界=0.167>δ=0.10。C_7迁移效应=0.200。副作用率=0.000<阈值=0.30。Auditor 7项裁决全部覆盖。实现文件：experiments/（llm_backend/checkpoint_layer/treatment_groups/experiment_runner/effect_estimator/help_curve/migration_tester/side_effect_logger/pilot_runner/test_phase4）+policy/（constraint_optimizer）+auditor/（auditor/visibility_labels/capability_tokens/blind_evaluator） | Phase 4实现状态 |
| `dev-docs/135-v1-2026-08-05-Phase5-CheckList.md` | **Phase 5独立Check List**：从124号v2拆出并细化。含P5-1—P5-10全部子项+完整性标准+角色隔离+代码模块+P5-EXIT出口门。目标：检索、Context Compiler与验证路由。细化新增：P5-9 K/T/H投影实现、P5-10旧七步骤复用决策。138号审计新增：P5-1.5 R-15来源注册、P5-4.3 R-6上下文膨胀、P5-5.5 NumPy/SciPy注册 | Phase 5执行视图 |
| `dev-docs/136-v1-2026-08-05-Phase6-CheckList.md` | **Phase 6独立Check List**：从124号v2拆出并细化。含P6-1—P6-9全部子项+完整性标准+角色隔离+代码模块+P6-EXIT出口门+停止条件。目标：完成DYN-6。细化新增：P6-9受约束最小干预策略。138号审计新增：P6-2.4 R-5按需物化 | Phase 6执行视图 |
| `dev-docs/137-v1-2026-08-05-Phase7-CheckList.md` | **Phase 7独立Check List**：从124号v2拆出并细化。含P7-1—P7-8全部子项+完整性标准+数学主张标注级别+P7-EXIT出口门+停止条件。目标：完成DYN-7。细化新增：P7-MATH数学主张三级别标注。138号审计新增：P7-1.4 R-15来源版本监控 | Phase 7执行视图 |
| `xishujuzhen/arxiv_to_arangodb.py` | arXiv元数据→ArangoDB导入脚本：读取JSON批量导入239K篇+创建4个索引+验证 | 工具脚本 |
| `xishujuzhen/arangodb_init.py` | ArangoDB数据库初始化：创建xishujuzhen_math数据库+12 collections+3 graphs+8索引 | 基础设施脚本 |
| `xishujuzhen/topology_verifier.py` | 拓扑覆盖验证器：检查G'→G的节点/边/环路集合保真。**123号裁决：结构保真验证，不代表语义或数学正确** | legacy验证器 |
| `xishujuzhen/test_dependency_graph.py` | 依赖图回归测试。**123号裁决：legacy图回归，不作为动态研究系统验收** | legacy测试 |
| `xishujuzhen/import_math_graph_to_arangodb.py` | 数学依赖图→ArangoDB导入脚本 | 数据导入脚本 |
| `xishujuzhen/batch_extractor.py` | 批量提取器脚本 | 工具脚本 |
| `xishujuzhen/absorb_test_loop.py` | 吸收测试循环脚本 | 工具脚本 |
| `xishujuzhen/poc4_build_graph.py` | POC-4（Klein瓶同调群）依赖图构建脚本 | POC工具脚本 |
| `xishujuzhen/poc9_export_graph.py` | POC-9图导出脚本 | POC工具脚本 |
| `xishujuzhen/poc9_import_topo.py` | POC-9拓扑图导入脚本 | POC工具脚本 |
| `xishujuzhen/poc9_import_unfold_full.py` | POC-9完整展开图导入脚本 | POC工具脚本 |
| `xishujuzhen/poc9_prepare_translate_input.py` | POC-9转译输入准备脚本 | POC工具脚本 |

### 星学知识系统结构参考

| 文档 | 内容 | 对数学项目的参考价值 |
|---|---|---|
| `AGENTS-星学版.md` | **星学项目完整 AGENTS.md**：1056行，包含项目定位、四类载体分工、8个工作流入口、吸收范式、形式化思维规则、解释框架、维度/成熟度/可计算性 | **必读**。数学项目的 AGENTS.md 结构直接参考它 |
| `星学项目: dev-docs/56-新系统老系统吸收范式.md` | 新系统/老系统吸收范式第一版。**文件在星学项目目录**`~/MOIRA_chinese_astrology-main/dev-docs/`，不在数学项目dev-docs/中 | 知识系统建设范式参考 |
| `星学项目: dev-docs/57-新系统方案迭代与老方案更新.md` | 对吸收范式的8问审视。**文件在星学项目目录** | 知识系统迭代方法参考 |
| `星学项目: dev-docs/58-新系统迭代执行CheckList.md` | 可执行 CheckList 设计。**文件在星学项目目录** | Check List 设计参考 |
| `星学项目: dev-docs/59-AGENTS重构纠偏与高价值规则回收.md` | AGENTS 重构时的保全纪律。**文件在星学项目目录** | 本 AGENTS.md 重写时已遵循 |
| `星学项目: dev-docs/60-外部系统收敛与暂存规划.md` | 外部系统收敛决策。**文件在星学项目目录** | 知识边界管理参考 |
| `星学项目: dev-docs/13-七政四余形式化体系.md` | 形式化体系：算子+集合+命题。**文件在星学项目目录** | 数学形式化的直接参考 |

### 星学 POC 验证方案完整列表

| POC | 文档 | 验证内容 |
|---|---|---|
| POC-1 | `dev-docs/64-xishujuzhen-POC验证方案.md` | 对照实验设计、5节点7边依赖图、5维度结构化评分 |
| POC-2 | `dev-docs/65-xishujuzhen-POC2验证方案.md` | 12节点16边扩展图、知识内容嵌入提示、配对审计 |
| POC-3 | `dev-docs/66-xishujuzhen-POC3验证方案.md` | AI自解读环节、双重提示、双重对照审计 |
| POC-4 | `dev-docs/68-xishujuzhen-POC4验证方案.md` | 双宫联动、19节点25边、跨宫依赖、空宫设计 |
| POC-5 | `dev-docs/70-xishujuzhen-POC5验证方案.md` | 静态+动态分析、30节点40边8跨宫依赖、静态螺旋环路 |
| POC-6 | `dev-docs/72-xishujuzhen-POC6验证方案.md` | A组知识缺失+交叉审计、独立AI实例审计 |
| POC-7 | `dev-docs/74-xishujuzhen-POC7验证方案.md` | 12限全量、71节点106边、动态螺旋三圈修正 |
| POC-8 | `dev-docs/77-xishujuzhen-POC8验证方案.md` | 闭环审计标准流程化、开环组vs闭环组对照 |

### 星学实验执行模式参考

| 文档 | 内容 |
|---|---|
| `dev-docs/67-Subagent对照实验执行模式.md` | 双subagent并行对照、分阶段subagent、盲评、background模式、输出保存到文件 |



### 种子推荐表与认知图查询

### 种子推荐表

`xishujuzhen/seed_recommendation_table.json`——数学问题类型→推荐意识种子映射：

| 问题类型 | 推荐种子 |
|---|---|
| 极值/上下界问题 | numerical_check, extreme_testing, invariant_thinking, approximation_thinking |
| 证明构造问题 | invariant_thinking, local_global_thinking, seven_step_workflow |
| 跨领域问题 | local_global_thinking, invariant_thinking, spiral_cognition, three_layer_extraction |
| 逼近/误差分析 | approximation_thinking, numerical_check, extreme_testing |
| 一般证明问题 | seven_step_workflow, math_awareness_nodes |

**用法**：AI接到数学问题后，先查此表确定种子，再执行CP1-CP3。

### 认知图查询与审计

```bash
# 查统计
.venv/bin/python3 -c "from cognition_sdk_math import CognitionSDK; sdk=CognitionSDK(); print(sdk.get_stats())"

# 图遍历（从种子出发）
.venv/bin/python3 -c "from cognition_sdk_math import CognitionSDK; sdk=CognitionSDK(); print(sdk.traverse(['seven_step_workflow'], max_depth=7))"

# 全量审计
.venv/bin/python3 xishujuzhen/cognition_audit_math.py all

# POC回归验证
.venv/bin/python3 xishujuzhen/cognition_audit_math.py poc-regression --seeds <seeds> --ground-truth <cog_ids>
```

### 数学大师系统技术说明

## 数学大师系统技术说明

> 本节是数学大师系统（目标系统——数学证明的依赖结构管理）的操作级技术说明。跨session/压缩后AI通过本节恢复"怎么用数学大师系统"的认知。完整方案见依赖文档。

### 七步骤工作流 [legacy-static]

> **[legacy-static]** 123号v1已将七步骤正式降为legacy静态重建器。保留静态知识图与提示展开价值，不再承担主运行时。主运行时改为12步事件溯源循环（观测→状态归约→候选规则匹配→受约束干预→验证→归因→回写）。旧七步骤的100%拓扑覆盖只证明结构保真，不证明语义或数学真值，也不证明动态思维矫正。

#### 旧七步骤→新12步运行时的迁移映射

> 来源：系统探讨.md第十二节 + plan + 123号第五十三节

| 旧步骤 | 新位置 | 说明 |
|---|---|---|
| 1.导入依赖图 | K图离线构建与发布 | 不再每轮运行时导入，K图是离线维护的 |
| 2.topo_generator | 局部激活包的结构编译器 | 不再全图展开，只编译当前卡点相关的最小结构 |
| 3.TopologyVerifier | 验证选定结构是否完整 | 只验证激活包的结构保真，不证明Hint正确 |
| 4.转译 | 增量Context Compiler | 只编译"当前卡点+一个最小操作+必要接口+可选工具" |
| 5.KC审计 | Hint注入前的知识忠实与泄漏审计 | 由Auditor角色执行，不是meta AI |
| 6.一次性分析 | 循环中的Solver step | Solver在12步循环中的步骤3和步骤10 |
| 7.最终覆盖审计 | 每轮进展审计+最终证明义务审计 | 由Verifier和Auditor分别执行 |

**核心变化**：不是抛弃旧系统，而是把它从"整个运行时"降为"动态控制系统中的局部上下文编译与结构验证模块"。

数学大师系统的核心是七步骤工作流，通过`seven_step_pipeline.py`执行：

| 步骤 | 执行者 | 内容 | 命令 |
|---|---|---|---|
| 1 | 代码 | 依赖图G导入ArangoDB | `seven_step_pipeline.py --steps 1` |
| 2 | **经典计算** | **topo_generator.py生成G'_topo骨架（L0+L1+L2）** + AI语义细化（L3） | `seven_step_pipeline.py --steps 2` |
| 3 | 代码 | TopologyVerifier拓扑覆盖验证（1次通过100%覆盖） | `seven_step_pipeline.py --steps 3` |
| 4 | normal AI | 按G'_topo转译为大师提示词 | `seven_step_pipeline.py --steps 4` |
| 5 | meta AI | KC忠实审计（转译是否忠实于知识内容） | `seven_step_pipeline.py --steps 5` |
| 6 | normal AI | 在大师提示词引导下做数学证明 | `seven_step_pipeline.py --steps 6` |
| 7 | meta AI | 分析覆盖审计（分析是否覆盖G'_topo所有节点和边） | `seven_step_pipeline.py --steps 7` |

**一键执行步骤1-3**（经典计算部分）：
```bash
.venv/bin/python3 xishujuzhen/seven_step_pipeline.py --steps 1,2,3
```

**步骤2的升级**（反哺1）：从"meta AI生成G'_topo"升级为"经典计算生成骨架+AI语义细化"。经典计算保证全覆盖，AI只做L3语义标注（section命名、spiral类型确认）。

### 依赖图导入ArangoDB

依赖图G存储在ArangoDB的`xishujuzhen_math`数据库中：
- `dg_nodes`：节点集（1719个，7种type：concept/domain_concept/paradigm/problem/substep/意识/step）——详见126号只读盘点报告
- `dg_edges`：边集（1483个，edge_type以unknown为主但mapping_type有40+种映射类型）——详见126号只读盘点报告
- `loops`：螺旋环路（4个，含圈数）
- `arxiv_papers`：**arXiv论文库**（239472篇元数据，2023-2026年，44个分类）。支持按分类/日期/作者/关键词查询。每篇论文有mapping_level（L1定理级/L2方法级/L3意识级/L4索引级）和linked_nodes（关联的dg_nodes）。详见112号方案。

### arXiv论文查询

```bash
# 按分类查询
.venv/bin/python3 -c "import sys; sys.path.insert(0,'xishujuzhen'); from cognition_sdk_math import CognitionSDK; [print(p['arxiv_id'],p['title'][:50]) for p in CognitionSDK().search_arxiv(category='math.AG', limit=5)]"

# 关键词搜索
.venv/bin/python3 -c "import sys; sys.path.insert(0,'xishujuzhen'); from cognition_sdk_math import CognitionSDK; [print(p['arxiv_id'],p['title'][:50]) for p in CognitionSDK().search_arxiv(keyword='Ramanujan', limit=5)]"

# 有全文的论文
.venv/bin/python3 -c "import sys; sys.path.insert(0,'xishujuzhen'); from cognition_sdk_math import CognitionSDK; [print(p['arxiv_id'],p['title'][:50]) for p in CognitionSDK().search_arxiv(has_fulltext=True, limit=5)]"

# 提升论文映射级别（L4→L1/L2/L3）
.venv/bin/python3 -c "import sys; sys.path.insert(0,'xishujuzhen'); from cognition_sdk_math import CognitionSDK; print(CognitionSDK().promote_arxiv_paper('2607.27504','L1','Ramanujan_airy_asymptotics'))"
```

### G'_topo生成（经典计算展开）

`topo_generator.py`从G自动生成G'_topo骨架：
- L0骨架展开：节点集+边集直接拷贝（拓扑同构保证全覆盖）+ Kahn拓扑排序确定traversal_order
- L1类型推断：static/dynamic + connection类型（linear/shortcut/cross_section）
- L2 section划分：按依赖链长度分段+意识节点处理
- L3语义标注（AI）：section命名、spiral_static/dynamic最终确认

### TopologyVerifier拓扑覆盖验证（结构保真验证）

> **[结构保真验证]** TopologyVerifier验证的是输出骨架不遗漏输入图节点/边（结构保真），不代表语义或数学正确。100%拓扑覆盖只证明结构完整性，不证明语义真值、数学正确性或动态思维矫正效果。

`topology_verifier.py`验证G'_topo是否覆盖G：
- 节点覆盖：ut_nodes vs dg_nodes的集合差集
- 边覆盖：ut_edges vs dg_edges的集合差集
- 螺旋环路：圈数是否保持
- 结果：passed=True + 100%覆盖 = 结构保真通过（不代表语义或数学正确）

### 三层提取（L1/L2/L3）

83号文档设计的三层提取，L1/L2/L3是提取层次（解题思路→数学思维→范式思维），不是版本号。版本链用v1/v2/v3等独立编号，与L1/L2/L3无映射关系。

| 层次 | 内容 | 复用范围 |
|---|---|---|
| L1解题思路 | 具体步骤序列 | 类似题 |
| L2数学思维 | 从L1抽象出的思维模式（AI二次分析） | 跨题、跨领域 |
| L3范式思维 | 从多个L2综合出的范式（AI三次分析） | 改变图结构 |

**版本链操作**（版本号独立于L1/L2/L3层次）：
```bash
# 添加新版本
.venv/bin/python3 -c "from cognition_sdk_math import CognitionSDK; sdk=CognitionSDK(); sdk.add_version('<cog_id>', 'v2', '<doc>', '<summary>', version_order=2); sdk.update_current_version('<cog_id>', 'v2')"
```

**current_version反映文档版本**，与L1/L2/L3提取层次无映射关系。

### 数学意识节点（5个）

| 意识节点 | cog_id | 说明 |
|---|---|---|
| 不变量思维 | invariant_thinking | 识别什么是不变量，在扰动下保持 |
| 局部-全局思维 | local_global_thinking | 局部性质推出全局性质 |
| 逼近论思维 | approximation_thinking | 分析逼近精度和误差阶 |
| 极端检验 | extreme_testing | 在极端构型下验证命题 |
| 数值检验意识 | numerical_check | 用数值例子检验命题自洽性 |

**双重身份**：每个意识节点同时在cognition_units（工作认知）和dg_nodes（数学依赖图）中有记录。

**版本链状态**：5个意识节点都有v1(POC-1发现)→v2(POC-2深化)版本链，current_version=v2。

### 依赖维护

本节的依赖关系存储在认知图稀疏矩阵中（认知单元 `agents_tech_mathmaster`）：
- source_docs: [83, 85, 86, 88, 90, 92, 99, 100]
- depends_on: seven_step_workflow, classic_expansion, topology_verifier, topology_coverage, three_layer_extraction, math_awareness_nodes, spiral_cognition

**查依赖**：`cognition_sdk_math.py traverse(['agents_tech_mathmaster'])`
**反向查询**（当某个dev-docs更新时，查哪些技术说明节需要同步）：
```bash
.venv/bin/python3 -c "import sys; sys.path.insert(0,'xishujuzhen'); from cognition_sdk_math import CognitionSDK; [print(u['cog_id'],u['title']) for u in CognitionSDK().find_dependents_by_doc(88)]"
```


