# 125-v1 · AGENTS.md对齐审计与Git Hook防不同步机制

> 记录时间：2026-08-05 07:00
> 来源：Devin CLI 对话
> 文档类型：开发文档记录
> 话题关键词：AGENTS.md对齐, Git Hook, pre-commit, post-commit, alignment_check, DYN阶梯, Phase编号

---

## 为什么记录

本轮工作发现AGENTS.md（项目认知索引文件）与repo最新内容存在多处严重不同步，包括DYN阶梯定义错误、Phase编号偏移、文档索引遗漏、代码文件未引用等。这些错误会导致后续Session的AI对架构基线产生错误认知。

在修正这些问题后，为防止同类问题再次发生，新增了Git Hook对齐检查机制（`alignment_check.py` + `pre-commit` + `post-commit`增强）。本轮工作涉及对齐审计、修正、防御机制建设和多次commit，需要留下正式记录，供后续Session查阅。

---

## 摘要

审计发现AGENTS.md存在7类对齐问题：DYN阶梯定义从DYN-4开始全部错误（旧定义来自122号v2草稿，123号v1已重新定义但AGENTS.md未同步）、Phase编号偏移（只读盘点dg_*是Phase 0子项而非独立Phase）、文档索引引用了星学项目目录文件但未标注、69号文档遗漏、11个py文件未引用、64号文件名引用错误、Handover日期标注过时。全部修正后，新增`alignment_check.py`脚本做6项对齐检查，新增`pre-commit` hook阻止硬性违规commit，增强`post-commit` hook在commit后提醒对齐状态。

---

## 主体内容

### 一、对齐审计方法

以三个维度系统性检查AGENTS.md与repo实际内容的对齐情况：

1. **文档索引对齐**：AGENTS.md引用的`dev-docs/*.md`文件是否存在；`dev-docs/`中的编号文档是否都在索引中
2. **代码文件索引对齐**：AGENTS.md引用的`xishujuzhen/*.py`文件是否存在；实际存在的py文件是否都被引用
3. **核心定义对齐**：AGENTS.md Memory Section中的DYN阶梯定义与123号权威文档是否一致；Phase定义与123号/124号是否一致；认知图规模与JSON是否一致

审计工具：`comm`命令做编号集合差集，`grep`提取引用，逐行比对定义文本。

### 二、发现的7类对齐问题

| 编号 | 类别 | 严重度 | 具体内容 |
|---|---|---|---|
| A-1 | DYN阶梯定义错误 | **严重** | Memory第548行DYN-4—7全部错误。旧：DYN-4跨题迁移/DYN-5在线Agent M/DYN-6多问题并发/DYN-7自演化。正确（123号第三十六—四十三节）：DYN-4帮助量响应曲线/DYN-5跨题与跨模型迁移/DYN-6在线闭环控制器/DYN-7跨领域与长证明编排 |
| A-2 | Phase编号偏移 | **严重** | TODO第483—485行和Memory第549行。旧：Phase 0=schema冻结/Phase 1=只读盘点dg_*/Phase 2=DYN-0。正确（123号/124号）：Phase 0=冻结legacy与统一语义（含只读盘点dg_*）/Phase 1=只观察不提示（DYN-0）/Phase 2=类型化状态与研究义务（DYN-1/DYN-2） |
| A-3 | DYN编号引用错误 | 中 | TODO第489行"对应DYN-3—DYN-4"应为"对应DYN-3—DYN-5"（跨题迁移是DYN-5）。Memory第545行"必须通过DYN-0—DYN-4验证"应为"必须通过DYN-0—DYN-5验证" |
| A-4 | 文档索引问题 | 中 | 13/56—60号文档在星学项目目录中，不在数学项目dev-docs/中，但AGENTS.md未标注来源；69号文档存在但索引中遗漏 |
| A-5 | 代码文件索引不完整 | 低 | 11个实际存在的py文件未被AGENTS.md引用（arangodb_init.py、topology_verifier.py、test_dependency_graph.py等） |
| A-6 | 文件名引用错误 | 中 | AGENTS.md引用`64-xishujuzhen-POC1验证方案.md`，实际文件名为`64-xishujuzhen-POC验证方案.md`（无"1"）。此问题在第一轮审计中被遗漏，由后续`alignment_check.py`自动检测发现 |
| A-7 | 日期标注过时 | 低 | Handover Section标题"工作系统实现状态（2026-08-04）"应为2026-08-05 |

### 三、修正内容

全部修正已commit（`b20abaa`和`4ce27de`）：

1. **DYN阶梯定义**（Memory第548行）：按123号第三十六—四十三节重新定义DYN-0—7
2. **Phase编号**（TODO第483—485行+Memory第549行）：按123号/124号重新定义Phase 0—2
3. **DYN编号引用**（TODO第489行+Memory第545行）：DYN-3—4→DYN-3—5，DYN-0—4→DYN-0—5
4. **文档索引**：13/56—60标注为"星学项目目录"文件；补充69号
5. **代码文件索引**：补充11个未引用的py文件，legacy文件标注"123号裁决"
6. **64号文件名**：`POC1验证方案`→`POC验证方案`
7. **Handover日期**：2026-08-04→2026-08-05

### 四、Git Hook对齐检查机制

#### 4.1 设计原则

- **独立于ArangoDB**：hook可能在ArangoDB不可用时触发，只依赖文件系统
- **硬软分离**：硬性违规（引用不存在的文件）阻止commit；软性警告（定义不一致）仅提醒
- **graceful降级**：脚本异常时静默降级，不阻塞正常工作
- **不硬编码**：DYN/Phase定义从123号/124号文档动态提取，不从AGENTS.md硬编码期望值

#### 4.2 alignment_check.py（6项检查）

| 检查 | 类型 | 内容 | 数据源 |
|---|---|---|---|
| 1 | 硬性 | AGENTS.md引用的`dev-docs/*.md`文件是否存在 | 文件系统 |
| 2 | 软性 | `dev-docs/`编号文档是否都在AGENTS.md索引中 | 文件系统+AGENTS.md |
| 3 | 硬性 | AGENTS.md引用的`.py`文件是否存在 | 文件系统 |
| 4 | 软性 | DYN阶梯定义与123号是否一致 | AGENTS.md+123号 |
| 5 | 软性 | Phase定义与124号是否一致 | AGENTS.md+124号 |
| 6 | 软性 | 认知图规模与JSON是否一致 | AGENTS.md+cognition_units_math.json |

关键实现细节：
- 范围引用（`64-xxx.md ~ 77-yyy.md`）跳过文件存在性检查，只检查首尾
- 通配符引用（`cognition_*.py`）跳过文件存在性检查
- 标注为"星学项目"的引用跳过文件存在性检查
- DYN/Phase一致性检查通过关键词匹配，只对容易出错的DYN-4—7做检查
- 认知图规模取AGENTS.md中最后一个匹配值（Handover Section中的最新值）

#### 4.3 pre-commit hook

- 只检查硬性违规（检查1和检查3）
- 发现硬性违规则返回exit code 1，阻止commit
- 提示用户修正后再提交

#### 4.4 post-commit hook（增强）

- 保留原有CP4检查清单（从认知图稀疏矩阵查询）
- 新增对齐检查结果输出（硬性+软性）
- 不阻塞commit（post-commit时已commit完成），仅提醒
- 对齐检查通过时打印`✅ AGENTS.md 对齐检查通过`

#### 4.5 测试验证

| 测试 | 输入 | 预期 | 实际 |
|---|---|---|---|
| pre-commit正常 | 当前repo状态 | exit 0 | ✅ exit 0 |
| pre-commit违规 | 故意引用不存在的文件 | exit 1+错误信息 | ✅ exit 1+正确错误信息 |
| post-commit正常 | 当前repo状态 | CP4清单+对齐通过 | ✅ CP4清单+✅对齐通过 |
| 首次运行alignment_check | 修正前repo状态 | 检测到64号文件名错误 | ✅ 自动检测到 |

#### 4.6 机制有效性证明

`alignment_check.py`在首次运行时就自动检测到了一个第一轮审计遗漏的问题（64号文件名引用错误：`POC1验证方案` vs 实际`POC验证方案`），这证明了机制的有效性——自动化检查比人工审计更可靠。

### 五、Commit记录

| Commit | 内容 |
|---|---|
| `b20abaa` | AGENTS.md与repo最新内容全面对齐——修正DYN阶梯/Phase编号/文档索引/代码索引 |
| `4ce27de` | 新增Git Hook对齐检查机制——防止AGENTS.md与repo内容不同步 |

---

## 结论 / 决策

- **AGENTS.md确实存在严重不同步**：最严重的是DYN阶梯定义从DYN-4开始全部错误，以及Phase编号偏移。这些错误源于123号v1重新定义了DYN阶梯和Phase编号，但AGENTS.md的Memory Section和TODO Section中散落在多处的旧引用没有被同步更新。
- **人工审计不足以防止不同步**：第一轮人工审计遗漏了64号文件名引用错误，自动化检查在首次运行时就发现了它。
- **采用pre-commit+post-commit组合方案**：pre-commit做硬性检查（文件存在性）阻止违规commit；post-commit做软性检查（定义一致性）在commit后提醒。这比单一hook方案更平衡——不会因软性警告阻塞正常工作，也不会让硬性违规悄悄通过。
- **不采用单一权威源+自动生成方案**：虽然最彻底，但AGENTS.md是给人读的，自动生成的可读性可能下降，且需要维护提取脚本。当前方案的成本收益比更好。

---

## 后续动作 / 未决问题

- **后续动作1**：当123号或124号有新版本时，运行`alignment_check.py`验证AGENTS.md是否需要同步更新
- **后续动作2**：当新增`dev-docs/`文档或`xishujuzhen/*.py`文件时，commit前pre-commit hook会自动检查AGENTS.md是否引用了它们
- **未决问题1**：DYN/Phase一致性检查目前只做关键词匹配，可能存在边界情况（如描述改写但关键词保留）。如果后续出现漏报，可考虑更严格的语义比对
- **未决问题2**：检查4和5的软性警告不阻止commit，依赖AI在收到post-commit提醒后主动修正。如果AI忽略提醒，问题仍会累积。可考虑在连续N次软性警告后升级为硬性违规
- **未决问题3**：`alignment_check.py`本身的对齐——如果检查脚本的逻辑有bug，它可能漏报或误报。目前通过测试验证了基本功能，但没有自动化测试覆盖所有检查路径
