# Fields 试点 — June Huh 案例：原始语料 OP 执行与社区对照审计（2026-09-28）

> **研究对象**：June Huh 的获奖工作（Hodge 理论 ↔ 组合学之桥）的**原始语料**（本人 ICM 2022
> 报告、本人综述、AHK 原始论文）与**社区解读**（Kalai 官方 laudatio、中文社区综述、Quanta
> 报道），以及内部旧基线（本仓 349 号 web_search 二手综合）。
> **待检验命题**（用户 2026-09-28 指令）：(a) 层面×facet 网格在跨领域案例上的复用率；
> (b) "同构之桥"四字标签经算子化后的 AI 指导力扩容是否显著；(c) **以社区解读为对照，考察
> facet/层级系统化挖掘的完整性，乃至思维彻底结构化的正确性**（双向审计：我们看见社区没说
> 的什么；社区说了网格装不下的什么）。
> **方法**：OP-0..OP-6 在 Huh 案例上执行；语料全部入 Git（`corpus/`）；每条主张配语料锚点。
> **证据等级**：一手=Huh 本人文本与论文；二手=laudatio/综述/报道；349 号=内部旧基线（web_search
> 二手，明确降级）。ICM 报告 markdown 为文本级提取（公式未保真），公式级复跑待 MinerU 全通。

## 1. OP-0 语料冻结

| 语料 | 身份 | 锚点 |
|---|---|---|
| Kalai, *The Work of June Huh*（IMU 官方 laudatio） | 社区解读（官方） | corpus/laudatio-jh.pdf + .md |
| Huh, *Combinatorics and Hodge theory*（ICM 2022 报告） | 第一人称 | corpus/huh-icm2022.pdf + .md |
| Huh, *Combinatorial applications of the Hodge–Riemann relations*（arXiv:1711.11176） | 第一人称综述 | 摘要逐字入档："Why do natural and interesting sequences often turn out to be log-concave? …from the viewpoint of standard conjectures" |
| Adiprasito–Huh–Katz, *Hodge theory for combinatorial geometries*（arXiv:1511.02888） | 原始研究论文 | 摘要入档（63 页正文未逐字读——首期边界） |
| 中文社区综述（arXiv:2211.05724） | 社区解读 | 桥建立四步+四障碍提取记录（§2/§3 引用） |
| Quanta 报道（2022-07-05） | 第一人称引述+同行评价 | 提取记录（§2 F8、§4.3） |
| 本仓 349 号（2026-08-11） | 内部旧基线（web_search 二手） | 明确降级为对照物 |

## 2. OP-1/OP-2 facet 轮读与层面标定（Huh 工作）

| facet | 读到的核心内容 | 层面 | 锚点 |
|---|---|---|---|
| F1（攻击→**解释**角）* | 语义平移：悖论域的"攻击角"在此为"解释角"——Huh 的问题表述：**为什么自然有趣的序列总是 log-concave？** | L5 | arXiv:1711.11176 摘要 |
| F2 否定 | "almost all matroids are not realizable"——几何方法的适用性被否定，**驱动**纯组合重构 | L4 | 2211.05724 |
| F3 时间 | 慢思考/无意识酝酿（"at some point you just realize, oh, I know this"）；每天三小时 | L6 | Quanta |
| F4 经济性 | **Kähler package（PD+HL+HR 三件套）作为最大经济复用单元**：Huh 2015 列五例同形（Kähler 流形上同调/代数闭链环/McMullen 代数/组合交点上同调/Soergel 双模/拟阵 Chow 环） | L4/L5 | laudatio §4.2 |
| F5 自指 | 标准猜想的组合 appearances 与表示论/数论 appearances 的潜在联结（Kalai 结尾的"hope"） | L5 | laudatio §4.2 |
| F6 完成性 | 不可实现多数=桥的现实不可达 → AHK 以归纳+商代数+flips **完成构造** | L4 | 2211.05724 |
| F7 可表达性 | **核心算子所在**：Bergman fan / Chow ring / 拟阵交点上同调 = 让组合对象"能表达"Hodge 结构的代数替身 | L4 | 2211.05724；laudatio §4 |
| F8 现实映射 | "it feels like you're **grabbing something that's already there**, rather than creating"——发现的现实感第一人称 | L6 | Quanta |
| F9（反证→**反例检验**）* | 语义平移：augmented Chow ring "too big"、Möbius 代数不满足 PD/HL——**拒绝不达标替身** | L4 | 2211.05724 |
| F10 谱系 | Huh 本人的三基本思想来源（Sturmfels 热带线性空间 / Stanley 极化 Hodge / McMullen flip 连通性）+ laudatio 先驱链（Tessier/Khovanskii/De Concini–Procesi/Ardila–Klivans/Karu/Fulton–MacPherson） | L5 | laudatio §4.1 |
| F11 成本 | 替身"too big"=表达力过剩成本；Lefschetz 算子不来自 B¹(M)=结构不合身成本 | L4 | 2211.05724 |
| F12 语境 | 五对象同一 Kähler package=**语境无关性**——算子是语境不变量的又一实证（与主报告附录 C 呼应） | L5 | laudatio §4.2 |

*两处语义平移（F1/F9）为跨域适配本身的数据：facet 在非悖论域需一次显式平移——记入网格的
使用说明。

## 3. OP-3 算子抽取（H1–H5，七字段，逐个发证）

| # | 算子 | 动作 | 失败模式 | 发证 |
|---|---|---|---|---|
| H1 **骨架提取** | 从可实现情形提取纯组合骨架（"The geometry of realizable matroids often inspires purely combinatorial constructions"） | 骨架选错（借来的形状不含所需公理） | 2211.05724 |
| H2 **可表达替身构造** | 为不可实现对象构造满足目标公理的代数替身（Bergman fan→Chow ring→交点上同调的迭代） | 替身 too big / 缺关键算子来源 | 2211.05724 |
| H3 **公理形状复用** | 迁移的不是结论而是**定理形状**（Kähler 三件套整体搬运） | 只搬结论不搬形状（则 log-concavity 证不出） | laudatio §4.2；AHK 摘要 |
| H4 **形变保形归纳** | 降维归纳（Chow ring 商代数）+ flips 保 HL/HR——"不变量在受控形变下保持"的构造化 | 归纳步失去公理（flip 不保形即断） | laudatio §4.1(3)；2211.05724 |
| H5 **障碍账本** | 显式维护失败构造清单并逐个绕行（Möbius 代数→augmented ring→IC 的三连绕行） | 把失败构造当终点（账本关闭=研究停止） | 2211.05724 四障碍记录 |

**对照主报告 B1–B5（"同构之桥"五算子）**：H1⊂B1、H2⊂B1+B2、H3⊂B3、H4 为 B 族的领域特化、
H5 是 B 族没有的**新横切算子**（跨案例通用：HoTT 线的候选死亡记录即障碍账本的历史形态）。
**349 号标签对照**：其"类比迁移 #9"展开为 H1–H5 五算子×七字段——四字标签与算子族之间是
**1:35 的信息扩容**（5 算子×7 字段），且每个失败模式可执行（AI 可按字段检索/检验）——
"四个字太粗糙"得到定量刻画。

## 4. 对照审计（用户命题 c 的正面回答）

### 4.1 vs 349 号（内部旧基线）

349 号对 Huh 的归档："思维力：**类比迁移 #9**…AI 难以主动寻找'这个组合结构满足 Hodge 理论
公理'的洞察"。算子化后："难以主动寻找"被分解为 H1–H5 的**可执行步骤+已知失败模式+谱系
输入**（三基本思想的来源清单本身就是 H1 的输入接口）。结论：旧基线的判断方向对，但指导力
密度相差一个数量级——这正是本试点的核心量化结果。

### 4.2 vs laudatio（官方社区解读）

- **Kalai 叙述的重心**是输入谱系（三基本思想 + 先驱链）与结果清单；对 AHK 原创步骤只以
  "a large number of additional original (at times crazy) ideas"一笔带过。**我们的 H4/H5 恰好
  落在 laudatio 未展开处**（其内容来自社区综述与 AHK 摘要交叉）——网格看见了官方叙述的
  盲区，但第一人称深度不足（诚实标注：AHK 63 页正文未逐字读）。
- laudatio 有一处网格外信息（见 4.3）。

### 4.3 双向缺口（完整性+正确性检验）

**我们看到而社区未显式说的**：(a) 障碍账本（H5）作为方法核心——两份社区文本都记录了障碍
但都没把它命名为方法；(b) Kähler package 的语境不变量地位（F12 读法）。

**社区说了而网格初版装不下的（out-of-grid 检验）**：美学/品味维度——Ardila："Mathematicians
are a lot like artists in that really we're looking for beauty"、"He makes beautiful things"；
Huh："I like the solution even more than the problem"（laudatio 卷首语）。**新增 facet 候选
F13（美学/品味）**——从跨域语料涌现，恰好在主报告预言"网格可扩"的位置。
本次新语料观察约 30 条，网格外 1 条 → **out-of-grid 率 ≈ 3%**（首期单案例测量值）。

**正确性小酸测**：用 H1–H3 重演 Read 猜想历史路径（Quanta+laudatio §1）：奇点理论训练
（Hironaka 课堂）→ 构造代数簇使 log-concave 数字=色多项式系数（H1 骨架提取 + H3 形状复用
的 2009 特例）→ 与 laudatio §1 叙述一致。**通过**（单案例弱酸测，标注为方向性验证）。

## 5. 结论与边界

1. **网格复用率（命题 a）**：层面 6/6 全复用；facet 有效激活 11/12（F1/F9 需显式语义平移，
   F7 成为核心）+ 新候选 F13——跨域复用成立且带两次平移数据。
2. **指导力扩容（命题 b）**：四字标签→五算子×七字段，1:35 信息扩容，失败模式全部可执行。
3. **完整性/正确性（命题 c）**：out-of-grid 率≈3%（单案例），新 facet 候选 F13 涌现于预言
   位置；对照审计双向均有发现（我们见社区盲区 H5/F12；社区见网格外 F13）——**网格既不完备
   也不封闭，但缺口可测量、可扩**，与主报告附录 B/C 的设计一致。
4. **边界**：AHK 正文、ICM 报告公式级内容未读（待 MinerU 全通后复跑）；单案例样本；349 号
   的 68 人全景对照（每人的算子化）未做——那 是下一步规模化的对象。
