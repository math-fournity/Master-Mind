# 91-工作系统升级方案·cognition基座安装到数学项目

> **文档定位**：把"稀疏矩阵/依赖图/拓扑验证/ArangoDB"基座安装到数学项目的工作系统自身上。这不是数学大师系统（目标系统）的文档，而是 AI 自己工作方式的元层面升级方案。
>
> **依据**：89号审计文档（星学对比）+ 90号愿景分析（经典计算展开）

## 一、升级目标

### 1.1 核心目标

把数学项目 AI 自己的工作认知建模为 ArangoDB 中的图结构（认知单元图），配以 CP1-CP6 工作流和 Hook 集成，实现：
- **工作前**：从种子认知单元出发，图遍历加载所有前置认知，验证覆盖
- **工作中**：认知落盘到 dev-docs/，新认知写入 ArangoDB
- **工作结束**：commit 后 git post-commit hook 打印 CP4 检查清单（从稀疏矩阵动态查询）+ 三层维护机制保障纪律

### 1.2 与星学项目的差异

| 维度 | 星学项目 | 数学项目 |
|---|---|---|
| 认知单元来源 | 218个 dev-docs → 64个认知单元 | 89个 dev-docs（80-90号）→ ~30个认知单元 |
| 目标系统图 | 星学依赖图（study-notes 结构） | 数学依赖图（dg_nodes/dg_edges，已有） |
| 工作认知图 | cognition_units（独立于目标系统图） | cognition_units（**与数学依赖图共享 ArangoDB 实例**） |
| 质量验证 | AQL 集合差集 | AQL 集合差集 + **TopologyVerifier**（拓扑确定性） |
| 意识节点 | 在 study-notes/星学意识/，不在 cognition_units | **意识节点同时存在于 cognition_units 和 dg_nodes** |
| G'_topo 生成 | meta AI 生成 | **经典计算生成骨架（L0+L1）+ AI 语义细化（L3）**（90号文档） |

### 1.3 超越星学的三个维度

1. **两套图共享 ArangoDB**：工作认知图（cognition_units）和数学依赖图（dg_nodes）在同一个 `xishujuzhen_math` 数据库中，认知单元可以引用数学依赖图的节点
2. **TopologyVerifier 作为质量验证**：星学只有 AQL 集合差集，数学项目有 TopologyVerifier 做拓扑确定性验证
3. **经典计算展开 G'_topo**：星学的 G'_topo 由 meta AI 生成，数学项目由经典计算生成骨架（90号文档）

## 二、认知单元设计

### 2.1 数学项目的认知单元（~30个）

基于 80-90 号文档积累的工作认知，设计以下认知单元：

#### core 类（核心方法论认知）

| cog_id | title | key_cognition | source_docs | current_version |
|---|---|---|---|---|
| `math_master_system` | 数学大师系统建设 | 依赖图提示→拓扑覆盖验证→KC忠实审计的完整工作流，核心信念"完美的提示词可以通过经典计算产生" | [80, 81] | v2 |
| `poc_methodology` | POC验证方法论 | 对照实验设计（A组教材 vs B'组依赖图JSON vs B组七步骤工作流），盲评打分，边际增益度量 | [84, 85, 87, 88] | v2 |
| `dependency_graph_prompt` | 依赖图提示方法 | 数学知识建模为依赖图（节点=步骤/意识，边=depends_on/calls），螺旋环路编码意识迭代，提示词是依赖图的文字展开 | [82, 83] | v1 |
| `topology_coverage` | 拓扑覆盖验证理论 | HoTT框架：依赖图G是拓扑结构，展开图G'是G的覆盖，审计是覆盖验证φ:G'→G，从文字随机到拓扑确定性 | [86, 78] | v1 |
| `seven_step_workflow` | 七步骤工作流 | 依赖图导入→G'_topo生成→拓扑验证→转译→KC审计→分析→分析覆盖审计，meta/normal分离，审计只做1次 | [86, 87, 88] | v1 |
| `arangodb_infra` | ArangoDB基础设施 | xishujuzhen_math数据库，12 collections + 3 graphs + 8索引，python-arango，共用星学实例 | [86] | v1 |
| `topology_verifier` | TopologyVerifier代码 | AQL集合差集实现拓扑覆盖验证，与领域无关，从星学到数学零修改复用，1次通过100%覆盖 | [86, 88] | v1 |
| `spiral_cognition` | 螺旋上升与意识节点 | 数学意识（不变量思维/局部-全局/逼近论/极端检验/数值检验）作为依赖图的意识节点，螺旋环路编码意识迭代 | [80, 82, 83] | v1 |
| `three_layer_extraction` | 三层提取方法论 | L1解题思路→L2数学思维（弥漫性模式）→L3新的思维方式（范式级），跨题复用增益验证 | [83] | v1 |
| `classic_expansion` | 经典计算展开愿景 | 经典计算负责G'_topo骨架展开（L0拓扑排序+L1类型推断），保证全覆盖，AI只做L3语义标注 | [90] | v1 |
| `work_system_upgrade` | 工作系统升级 | 把稀疏矩阵/依赖图/拓扑验证基座安装到工作系统自身，cognition_units+CP1-CP6+三hook | [89, 91] | v1 |
| `agents_management` | AGENTS.md管理 | 认知资产表索引，跨Session认知一致性，Memory Section + Handover Section | [89] | v1 |

#### process 类（POC验证过程认知）

| cog_id | title | key_cognition | source_docs | current_version |
|---|---|---|---|---|
| `poc1_execution` | 大师-POC-1验证 | 矩条件极差题第一问+第二问指数纠错，8节点10边，B组显著优于A组（+1.75/5分制），B组给出正确指数n^(-3/2) | [84, 85] | v1 |
| `poc2_execution` | 大师-POC-2验证 | 第二问完整证明，18节点25边2螺旋环路，七步骤工作流，B组显著优于A组（+3.27/10分制）和B'组（+2.34/10分制），B组唯一完成稳定性方程推导 | [87, 88] | v1 |
| `poc2_seven_steps` | POC-2七步骤执行 | 步骤2 meta AI生成G'_topo，步骤3 TopologyVerifier 1次通过100%覆盖，步骤5 KC审计94.4%忠实率，步骤7 分析覆盖100% | [88] | v1 |

#### support 类（支撑性认知）

| cog_id | title | key_cognition | source_docs | current_version |
|---|---|---|---|---|
| `math_awareness_nodes` | 数学意识节点库 | 不变量思维/局部-全局思维/逼近论思维/极端检验/数值检验意识，5个意识节点已在POC-1和POC-2中验证有效 | [80, 82, 85, 88] | v1 |
| `problem_database` | 题库建设方向 | 解法路径=依赖图实证边，一题多解=图结构实证，跨领域映射边来源，难度梯度=POC阶梯 | [82] | v1 |
| `blind_eval_method` | 盲评打分方法 | 评分subagent不知道哪个是A/B'/B，8维15分制，10分制归一化，边际增益度量 | [85, 88] | v1 |
| `subagent_file_issue` | Subagent写文件问题 | background subagent无法写入/Volumes路径，前台subagent可以但长prompt可能耗尽输出预算，需主Agent代写回退 | [85, 88] | v1 |

#### 意识节点（与数学依赖图共享）

| cog_id | title | key_cognition | source_docs |
|---|---|---|---|
| `invariant_thinking` | 不变量思维 | 矩恒等式在扰动下保持，寻找不变量是受约束极值问题的关键 | [80, 85, 88] |
| `local_global_thinking` | 局部-全局思维 | 从局部扰动到全局下界，紧性是局部到全局的桥梁 | [88] |
| `approximation_thinking` | 逼近论思维 | badly approximable是逼近论核心，二次无理数给出逼近下界 | [88] |
| `extreme_testing` | 极端检验 | 三点构型数值试探，极值构型是极端构型 | [85, 88] |
| `numerical_check` | 数值检验意识 | 用数值例子检验命题自洽性，区分上界与下界 | [85, 88] |

### 2.2 认知单元间的依赖边

```
math_master_system → dependency_graph_prompt (depends_on)
math_master_system → poc_methodology (depends_on)
math_master_system → spiral_cognition (depends_on)
poc_methodology → poc1_execution (depends_on)
poc_methodology → poc2_execution (depends_on)
poc2_execution → poc2_seven_steps (depends_on)
poc2_seven_steps → seven_step_workflow (depends_on)
seven_step_workflow → topology_coverage (depends_on)
seven_step_workflow → arangodb_infra (depends_on)
seven_step_workflow → topology_verifier (depends_on)
seven_step_workflow → classic_expansion (depends_on)
topology_coverage → topology_verifier (depends_on)
dependency_graph_prompt → three_layer_extraction (depends_on)
dependency_graph_prompt → math_awareness_nodes (depends_on)
math_awareness_nodes → invariant_thinking (depends_on)
math_awareness_nodes → local_global_thinking (depends_on)
math_awareness_nodes → approximation_thinking (depends_on)
math_awareness_nodes → extreme_testing (depends_on)
math_awareness_nodes → numerical_check (depends_on)
work_system_upgrade → agents_management (depends_on)
work_system_upgrade → arangodb_infra (depends_on)
poc_methodology → blind_eval_method (depends_on)
poc2_execution → subagent_file_issue (depends_on)
spiral_cognition → math_awareness_nodes (calls)
three_layer_extraction → problem_database (calls)
math_master_system → problem_database (calls)
```

### 2.3 stop_hook 的 CP4 检查清单

```
stop_hook → agents_management (depends_on)  # AGENTS.md是否更新
stop_hook → work_system_upgrade (depends_on)  # 工作系统是否维护
stop_hook → arangodb_infra (depends_on)  # ArangoDB是否运行
```

## 三、ArangoDB Collections 设计

### 3.1 新增 collections（在 xishujuzhen_math 中）

| collection | 类型 | 内容 |
|---|---|---|
| `cognition_units` | document | 认知单元节点（~30个） |
| `cog_versions` | document | 版本节点（每个认知单元的各版本） |
| `cog_edges` | edge | 跨认知单元依赖边（~30条） |
| `cog_version_edges` | edge | 版本链边（evolves_to） |
| `cognition_tasks` | document | 任务集合（记录每次任务的认知覆盖验证） |

### 3.2 与已有 collections 的关系

| 已有 collection | 用途 | 与 cognition 的关系 |
|---|---|---|
| `dg_nodes` | 数学依赖图节点 | 意识节点同时存在于 dg_nodes 和 cognition_units |
| `dg_edges` | 数学依赖图边 | 数学依赖图的边，与 cog_edges 独立 |
| `kcs` | 知识内容 | 认知单元的 key_cognition 引用 kcs 的内容 |
| `loops` | 螺旋环路 | 数学依赖图的环路，与 cognition 无直接关系 |

### 3.3 初始化脚本

`xishujuzhen/cognition_init.py`：
1. 在 `xishujuzhen_math` 中创建 5 个新 collections
2. 导入认知单元 JSON
3. 建立版本链边
4. 建立依赖边
5. 验证导入结果

## 四、核心脚本设计

### 4.1 cognition_verifier_math.py

适配星学的 `cognition_verifier.py`，改动：
- 数据库名：`xishujuzhen_math`（星学是 `xishujuzhen`）
- 图遍历：从种子认知单元出发，沿 `cog_edges` 的 `depends_on` 边遍历
- **新增**：与 `dg_nodes` 的交叉引用——如果认知单元是意识节点，同时查询其在数学依赖图中的位置

### 4.2 cognition_sdk_math.py

适配星学的 `cognition_sdk.py`，改动：
- 数据库名：`xishujuzhen_math`
- **新增**：`get_stop_checklist` 查询 `stop_hook` 的依赖，返回 CP4 检查清单
- **新增**：`audit_topology_coverage` —— 不仅做 AQL 集合差集，还调用 TopologyVerifier 做拓扑覆盖验证
- **新增**：`cross_reference_dg` —— 查询认知单元在数学依赖图中的对应节点

### 4.3 cognition_checkpoint_math.py

适配星学的 `cognition_checkpoint.py`，CP1-CP6 工作流：
- CP1：种子选择（确定本次任务需要哪些种子认知单元）
- CP2：认知加载（AQL 图遍历）
- CP3：缺口检查
- CP4：认知捕获（新方法论/新依赖/新版本/新术语/临场脚本）
- CP5：认知图更新（新版本/新边写入 ArangoDB）
- CP6：任务-认知映射

### 4.4 cognition_audit_math.py

适配星学的 `cognition_audit.py`：
- 一键全量审计
- 版本链审计
- 图遍历完整性审计
- 覆盖率审计
- **新增**：拓扑覆盖审计（调用 TopologyVerifier）

### 4.5 cognition_import_math.py

适配星学的 `cognition_import.py`：
- 读取 `xishujuzhen/poc/cognition_units_math.json`
- 导入 ArangoDB `xishujuzhen_math` 的 5 个新 collections

## 五、Hook 设计（v2：git post-commit + SessionStart）

> **重要教训（来自星学92号文档）**：星学项目最初用 v1 方案（Devin Stop hook + UserPromptSubmit hook + flag 文件），实测发现 **Stop hook 会影响 subagent**——subagent 启动后被 block，长时间不返回。session_id 防护方案不可靠（subagent 可能共享 session_id 或为空）。v1 已废弃，改为 v2（git post-commit hook）。
>
> **本方案直接采用 v2**，不重蹈 v1 覆辙。理由：数学项目的 POC 执行大量使用 subagent（POC-2 的 A 组/B'组对照实验都靠 subagent），Stop hook 会阻断这些 subagent。

### 5.1 方案演进对照

| 维度 | v1（星学已废弃，本方案不采用） | v2（星学当前，本方案采用） |
|---|---|---|
| 影响subagent | **是（实测证实，subagent被block）** | 否（subagent不commit） |
| 触发时机 | AI尝试停止时 | commit后（=工作结束） |
| 需要flag文件 | 是（work_pending） | 不需要 |
| 需要session_id区分 | 是（且不可靠） | 不需要 |
| 需要stop_hook_active防死循环 | 是 | 不需要 |
| git clean检查 | 需要 | 不需要（已经在commit了） |
| 强制力 | 硬block | 提示（stdout输出） |
| Devin hooks | SessionStart + UserPromptSubmit + Stop | SessionStart + PostCompaction |
| Git hooks | 无 | post-commit |

**强制力降级的诚实说明**：v2 从"硬 block"降级为"提示"。AI 看到 CP4 检查清单后可以"看完就忽略"。这是 v2 的已知局限（见诚实评估文档）。三层维护机制（Layer 1/2/3）是弥补手段。

### 5.2 Devin hooks（保留2个，不含Stop和UserPromptSubmit）

**文件**：`.devin/hooks.v1.json`

```json
{
  "SessionStart": [
    {
      "matcher": "",
      "hooks": [
        {
          "type": "command",
          "command": ".venv/bin/python3 xishujuzhen/session_start_hook_math.py",
          "timeout": 10
        }
      ]
    }
  ],
  "PostCompaction": [
    {
      "matcher": "",
      "hooks": [
        {
          "type": "command",
          "command": ".venv/bin/python3 xishujuzhen/session_start_hook_math.py",
          "timeout": 10
        }
      ]
    }
  ]
}
```

**为什么不用 Stop hook 和 UserPromptSubmit hook**：
- Stop hook 影响 subagent（星学92号文档实测证实）
- UserPromptSubmit hook 的唯一作用是设置 work_pending flag——这是 v1 的配套机制，v2 不需要
- 数学项目的 POC 执行大量使用 subagent，Stop hook 的危害比星学更严重

### 5.3 session_start_hook_math.py

```python
"""SessionStart + PostCompaction hook —— 注入工作系统提醒

触发时机：Devin session 启动时、上下文压缩后
作用：注入认知图统计 + 工作纪律提醒
不影响 subagent：SessionStart 只注入 additionalContext，不 block
"""
import sys, os, json

def main():
    data = json.load(sys.stdin)
    event = data.get('hook_event_name', 'SessionStart')
    project_dir = os.environ.get('DEVIN_PROJECT_DIR', '.')
    stats_text = get_stats_text(project_dir)

    context = f"""[工作系统提醒 · {event}]
本项目使用认知图工作系统（ArangoDB稀疏矩阵）。
{stats_text}
工作纪律：
- 工作前：用 cognition_checkpoint_math.py start --seeds <cog_id> 加载认知
- 工作中：认知落盘到 dev-docs/，新术语追加到词汇表
- 工作结束：commit 后 git post-commit hook 会打印 CP4 检查清单
- 临场脚本：可复用的脚本必须沉淀到 cognition_sdk_math.py"""

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": event,
            "additionalContext": context
        }
    }))
    sys.exit(0)

def get_stats_text(project_dir):
    try:
        sys.path.insert(0, os.path.join(project_dir, 'xishujuzhen'))
        from cognition_sdk_math import CognitionSDK
        sdk = CognitionSDK()
        stats = sdk.get_stats()
        return f"认知图：{stats['total_units']}个认知单元，{stats['total_edges']}条边。"
    except Exception:
        return "（ArangoDB未运行，认知图不可用。如需认知加载，先 docker start arangodb）"

if __name__ == '__main__':
    main()
```

### 5.4 git post-commit hook（CP4 检查清单）

**文件**：`xishujuzhen/githooks/post-commit`
**配置**：`git config core.hooksPath xishujuzhen/githooks`

```python
#!/path/to/.venv/bin/python3
"""Git post-commit hook —— CP4 检查清单提醒

每次 git commit 后触发。通过 SDK 查询 stop_hook 认知单元的依赖，
打印 CP4 检查清单到 stdout（Devin 在 exec 输出中可见）。

不影响 subagent：subagent 不 commit，所以不触发此 hook。
检查清单不硬编码，从稀疏矩阵动态获取。
"""
import sys, os, subprocess

def main():
    result = subprocess.run(['git', 'rev-parse', '--show-toplevel'],
                            capture_output=True, text=True)
    project_dir = result.stdout.strip()
    checklist = get_checklist(project_dir)
    if not checklist:
        return  # SDK 不可用时 graceful 降级

    print("\n" + "=" * 60)
    print("CP4工作结束检查清单（从认知图稀疏矩阵查询）")
    print("=" * 60)
    for i, item in enumerate(checklist, 1):
        title = item.get('title', item.get('cog_id', ''))
        cognition = item.get('key_cognition', '')
        docs = item.get('source_docs', [])
        doc_str = f"（载体文档: {', '.join(str(d) for d in docs)}）" if docs else ""
        print(f"  □ {i}. {title}: {cognition} {doc_str}")
    print("=" * 60 + "\n")

def get_checklist(project_dir):
    try:
        sys.path.insert(0, os.path.join(project_dir, 'xishujuzhen'))
        from cognition_sdk_math import CognitionSDK
        sdk = CognitionSDK()
        return sdk.get_stop_checklist('stop_hook')
    except Exception:
        return []  # 静默降级

if __name__ == '__main__':
    main()
```

**关键实现细节**：
- shebang 用绝对路径指向 .venv 的 python3（git hook 的 PATH 可能不包含 .venv）
- 检查清单从 SDK 动态查询，不硬编码
- SDK 不可用时 graceful 降级（静默不输出，不阻塞 commit）
- 不影响 subagent（subagent 不 commit）

### 5.5 三层维护机制

Hook 是强制纪律的一部分，完整的纪律保障是三层叠加：

#### 以"术语维护"为例

| 层 | 机制 | 实现 | 作用 |
|---|---|---|---|
| Layer 1 | CP4 提示 | cognition_checkpoint_math.py 在 CP4 时打印"新术语？→追加到词汇表" | 工作结束时提醒 |
| Layer 2 | AGENTS.md 约束 | AGENTS.md 中写明"新术语必须追加到词汇表" | always-on 约束 |
| Layer 3 | 认知图依赖 | 所有 core 认知单元 depends_on glossary 节点 | 图遍历时必经 |

**三层叠加效果**：Layer 3 让 AI 在"加载认知时"就经过 glossary 节点（不可能不知道它的存在），Layer 2 让 AI"知道"维护术语是硬性要求，Layer 1 让 AI 在工作结束时"想起"要检查术语。

#### 以"SDK 沉淀"为例

| 层 | 机制 | 实现 | 作用 |
|---|---|---|---|
| Layer 1 | CP4 提示 + post-commit hook | cognition_checkpoint_math.py 在 CP4 时打印"临场脚本？→沉淀到 cognition_sdk_math.py" | 工作结束时提醒 |
| Layer 2 | AGENTS.md 约束 | AGENTS.md 中写明"临场脚本沉淀纪律" | always-on 约束 |
| Layer 3 | 认知图依赖 | engineering_details depends_on sdk_maintenance | 图遍历时经过 |

#### 以"CP4 检查清单"为例

| 层 | 机制 | 实现 | 作用 |
|---|---|---|---|
| Layer 1 | post-commit hook | commit 后打印 CP4 检查清单 | commit 时提醒 |
| Layer 2 | AGENTS.md 约束 | AGENTS.md 中写明"必须 commit"+"CP4 检查" | always-on 约束 |
| Layer 3 | 认知图依赖 | stop_hook depends_on glossary + sdk_maintenance + agents_management | 检查清单内容来源 |

### 5.6 subagent 防护

**v2 的天然防护**：v2 用 git post-commit hook。subagent 通常不 commit（subagent_explore 是只读的，subagent_general 改文件后由主 session commit），所以不触发 post-commit hook。

**SessionStart hook 对 subagent 的影响**：SessionStart hook 在 subagent 启动时也会触发，注入工作系统提醒。这是**期望行为**——subagent 也需要知道工作系统的存在。而且 SessionStart 只是注入 additionalContext，不 block，不影响 subagent 的正常工作。

### 5.7 stop_hook 认知单元的 CP4 检查清单

```
stop_hook（process类）
  depends_on → glossary（support类）           → 术语更新检查
  depends_on → sdk_maintenance（support类）      → 临场脚本沉淀检查
  depends_on → agents_management（core类）       → AGENTS.md 更新检查
```

**未来加新纪律**：只需在 ArangoDB 中加一条边：

```python
sdk.add_edge('stop_hook', 'new_discipline', 'depends_on')
```

post-commit hook 脚本不用改，下次 commit 自动显示新纪律。

## 六、Devin CLI 集成

### 6.1 .devin/config.json

```json
{
  "permissions": {
    "allow": [
      "Read(**)",
      "Exec(git status)",
      "Exec(git diff)",
      "Exec(git rev-parse)",
      "Exec(.venv/bin/python3 xishujuzhen/cognition_checkpoint_math.py)",
      "Exec(.venv/bin/python3 xishujuzhen/cognition_audit_math.py)",
      "Exec(.venv/bin/python3 xishujuzhen/topology_verifier.py)"
    ],
    "ask": [
      "Write(**)",
      "Exec(git)",
      "Exec(tmux)"
    ],
    "deny": [
      "Write(.git/**)",
      "Exec(sudo)",
      "Exec(rm -rf /)"
    ]
  }
}
```

### 6.2 .devin/skills/

删除星学的 moira-* skills，创建数学项目的 skills：

| skill | 功能 |
|---|---|
| `math-runtime` | 读取认知图 capsule，工作前加载认知 |
| `math-worker` | 执行一个有界的数学研究任务（如 POC 的一个步骤） |
| `math-auditor` | 审计 Worker 输出是否通过语义和拓扑门控 |

## 七、Check List

### 阶段1：认知单元图构建
- [ ] 编写 `cognition_units_math.json`（~30个认知单元，~30条边）
- [ ] 编写 `cognition_init_math.py`（创建 collections + 导入）
- [ ] 运行初始化，验证导入结果
- [ ] 编写 `cognition_verifier_math.py`
- [ ] 测试图遍历：从 `math_master_system` 出发，验证覆盖所有前置认知

### 阶段2：SDK 和检查点
- [ ] 编写 `cognition_sdk_math.py`（查询/审计/修复 + TopologyVerifier集成）
- [ ] 编写 `cognition_checkpoint_math.py`（CP1-CP6）
- [ ] 测试 CP1-CP3：`cognition_checkpoint_math.py start --seeds math_master_system,poc_methodology`
- [ ] 测试 CP4-CP6：`cognition_checkpoint_math.py end --task "测试" --seeds ... --loaded ...`

### 阶段3：审计 CLI
- [ ] 编写 `cognition_audit_math.py`
- [ ] 测试一键全量审计：`cognition_audit_math.py all`
- [ ] 测试拓扑覆盖审计：`cognition_audit_math.py topology`

### 阶段4：三 Hook
- [ ] 编写 `session_start_hook_math.py`
- [ ] 编写 `prompt_hook_math.py`
- [ ] 编写 `stop_hook_math.py`
- [ ] 编写 `.devin/hooks.v1.json`
- [ ] 测试 SessionStart hook：注入认知图统计
- [ ] 测试 Stop hook：第一次 block + CP4 检查清单，第二次 git clean

### 阶段5：Devin CLI 集成
- [ ] 更新 `.devin/config.json`（权限配置）
- [ ] 删除星学的 moira-* skills
- [ ] 创建数学项目的 math-* skills
- [ ] 端到端测试：新 session 启动 → capsule 注入 → 工作前 CP1-CP3 → 工作 → 工作后 CP4-CP6 → Stop hook

### 阶段6：与七步骤工作流集成
- [ ] 在 POC 执行前用 `cognition_checkpoint_math.py start` 加载认知
- [ ] 在 POC 执行后用 `cognition_checkpoint_math.py end` 捕获新认知
- [ ] 新 POC 经验自动写入 cognition_units 版本链
- [ ] TopologyVerifier 集成到审计流程

## 八、与方案2（经典计算展开）的关系

方案2（92号文档）实现 `topo_generator.py`——经典计算生成 G'_topo 骨架。这是七步骤工作流步骤2 的升级，与方案1的关系：

| 方案1组件 | 方案2组件 | 关系 |
|---|---|---|
| `seven_step_workflow` 认知单元 | `topo_generator.py` | 方案2升级了方案1中 seven_step_workflow 的步骤2 |
| `cognition_sdk_math.py` | `topo_generator.py` | 方案2的 topo_generator 可以被 SDK 调用 |
| CP4 检查清单 | G'_topo 全覆盖 | 方案2的 L0 保证全覆盖，是 CP4 的一个检查项 |

两个方案可以并行实现，最终集成。

## 九、数学形式化

### 9.1 认知图的形式化定义

认知图是一个有向图：

```
G_math = (V, E, L, T, φ, S)

V = {v₁, v₂, ..., vₙ}              # 认知单元集合（节点），n≈30
E ⊆ V × V                          # 依赖边集合，|E|≈30
L: V → {core, process, support}    # 分类标签函数
T: V → ℕ                           # 版本链函数（v → 版本序列）
φ: V → P(D)                        # 载体文档函数（v → dev-docs编号集合）
S: V → {active, superseded, archived}  # 状态函数
```

### 9.2 图遍历的数学表达

从种子集合S出发，沿depends_on边遍历，找到所有前置认知：

```
traverse(S, max_depth) = {v | ∃ path from s to v, s ∈ S, length(path) ≤ max_depth}
```

用AQL实现：`FOR v, e, p IN 0..@max_depth ANY seed cog_edges FILTER e.edge_type == 'depends_on'`

### 9.3 覆盖验证的数学表达

集合差集：task_cogs - loaded_cogs = gaps

```python
task_ids = {c["cog_id"] for c in task_cogs}
loaded_set = set(loaded_cog_ids)
uncovered = task_ids - loaded_set  # 集合差集
```

**诚实说明**：这是朴素集合论，不是HoTT级别的拓扑覆盖验证。详见96号文档的HoTT诚实定位。

### 9.4 版本链的数学结构

```
版本链(v) = [version_1, version_2, ..., version_n]

其中 version_i = (version, doc, summary, version_order)

current_version(v) = version_n  （最新版本）
```

在HoTT框架下，版本链对应高阶路径（Higher Path）——认知的演化路径。但实际实现是时序图，不是HoTT。

### 9.5 规模指标

| 指标 | 数值 | 说明 |
|---|---|---|
| 认知单元总数 | ~30 | 12 core + 3 process + 4 support + 5意识 + ~6其他 |
| 依赖边总数 | ~30 | depends_on为主 |
| 版本记录总数 | ~35 | 大部分认知单元v1，少数v2+ |
| 载体文档总数 | 17 | 80-96号dev-docs |
| 压缩比（文档:认知单元） | ~0.57:1 | 注意：数学项目文档少但每份信息密度高，压缩比<1是正常的 |
| 稀疏度（边/(节点×节点)） | ~3.4% | 30/(30×29)，与星学3.2%接近 |

**与星学的规模对比**：

| 指标 | 星学 | 数学 | 说明 |
|---|---|---|---|
| 认知单元 | 67 | ~30 | 数学项目积累少，认知单元自然少 |
| 边 | 141 | ~30 | 同上 |
| 载体文档 | 218 | 17 | 数学项目文档少但信息密度高 |
| 压缩比 | 3.3:1 | ~0.57:1 | 数学项目每个文档平均不到1个认知单元——因为文档本身已经是认知单元级别的 |

## 十、其他AI如何复用

### 10.1 最小实现

如果只需要基本的认知图管理：

1. **arangodb_init_math.py**：创建数据库和集合（可简化，不需要三层图）
2. **cognition_verifier_math.py**：实现`get_task_cognition`和`verify_cognition_coverage`
3. **cognition_sdk_math.py**：实现`list_units`, `get_unit`, `traverse`, `get_deps`
4. **cognition_checkpoint_math.py**：实现`start`和`end`命令

不需要：topology_verifier.py（三层图验证）、topo_generator.py（经典计算展开）、audit_poc_regression（POC回归评分）

### 10.2 完整实现

需要完整的审计和Hook强制：

1. 上述最小实现
2. **cognition_audit_math.py**：实现`all`, `version-chain`, `graph-completeness`, `coverage`命令
3. **session_start_hook_math.py**：SessionStart + PostCompaction hook
4. **githooks/post-commit**：git post-commit hook
5. 配置`git config core.hooksPath`和Devin hooks.v1.json
6. 三层维护机制（CP4提示+AGENTS.md约束+认知图依赖）

### 10.3 增强实现

需要拓扑覆盖验证和经典计算展开（数学项目独有）：

1. 上述完整实现
2. **topology_verifier.py**：四层覆盖验证（已有，从星学零修改复用）
3. **topo_generator.py**：经典计算展开G'_topo骨架（92号方案）
4. ArangoDB初始化三层图集合（dg/ut/uf）
5. 螺旋环路检测和验证
6. 两套图共享ArangoDB（cognition_units + dg_nodes）
7. 意识节点双重身份（cognition_units + dg_nodes）

### 10.4 关键实现细节

1. **ArangoDB连接**：默认localhost:8529，用户名root，密码在代码中硬编码（生产环境应改用环境变量）
2. **AQL图遍历**：用`FOR v, e, p IN 0..max_depth ANY seed cog_edges`，注意`FILTER e.edge_type == 'depends_on'`
3. **集合差集**：Python的set操作`task_ids - loaded_set`，简单但有效
4. **版本链**：cog_versions集合按version_order排序，current_version指向最新
5. **Hook的shebang**：git hook必须用绝对路径的python3，不能用`#!/usr/bin/env python3`（PATH不同）
6. **graceful降级**：所有Hook脚本在SDK不可用时静默降级，不阻塞工作流
7. **不要用Stop hook**：会影响subagent（星学92号文档实测证实）
8. **两套图集合名隔离**：cognition_units/cog_edges/cog_versions与dg_nodes/dg_edges/loops无重名
9. **意识节点一致性**：cognition_units和dg_nodes中的意识节点需要一致性验证（POC-4-Math）
