# 系统资产分级与上下文预算管理

**触发条件**：设计或修改AI Agent的AGENTS.md内容时；设计或修改提示词文件时；向AI Agent发送直接提示词时；向system/添加新的资产文件时。always-on——任何涉及AI Agent输入内容设计的场景都必须遵守。

## 核心约束

**AGENTS.md、可复用提示词、分类学识别资产等都是system的资产。** 这些资产必须按分级原则放到正确的位置，不能随意堆放。直接发送给AI的提示词必须短小，大块内容必须放入文件中由AI加载。

## 三级资产分级

### 第1级：直接提示词——启动命令中直接发给AI的内容

**原则**：直接发送的提示词不应该是大块的。短启动提示词+提示词文件加载（见AI Agent启动规范rule）。

**限制**：
- 直接提示词不超过500字
- 只包含"加载什么文件、读取什么输入、产出写入哪里"的指令
- 不包含具体的分析要求、JSON schema、分类学知识等——这些放文件中

**正确示例**：
```
加载 {workdir}/prompt.md 中的提示词，读取 {workdir}/input.md 中的输入数据，
按提示词要求工作，完成后把产出写入 {workdir}/output.json 和 {workdir}/output.md
```

**错误示例**：
```
你是脉络分析AI，你的任务是...（30KB的完整提示词）...请分析input.md中的解答
```

### 第2级：文件——AI启动后加载的文件

**原则**：大块的要求、完整的提示词、分类学知识、题目和解答文本等，全部放入文件中。AI启动后加载文件获取这些内容。

**什么应该放入文件中**：
- ✅ 题目和解答文本——input.md
- ✅ 完整提示词（V5/V7/V8/V9等）——prompt.md
- ✅ 大块的要求和约束——AGENTS.md（实例运行版）
- ✅ 分类学识别资产——单独的分类学文件
- ✅ JSON schema定义——提示词文件中或单独的schema文件
- ✅ 程序验证脚本——verify_lattice_completeness.py等

**什么不应该放入文件中**（应该放在直接提示词中）：
- ❌ "加载哪个文件、产出写入哪里"的指令——这是直接提示词的内容
- ❌ 紧急的、必须立刻执行的指令——如"先读AGENTS.md再做事"

### 第3级：AGENTS.md——AI的指令和约束

**原则**：AGENTS.md是AI的角色定义、工作规范、产出要求。每个AI Agent的工作目录中都有一个AGENTS.md。

**实例运行的AGENTS.md应该包含**：
- ✅ AI的角色定义（你是谁、做什么）
- ✅ 工作规范（怎么工作、产出要求）
- ✅ 版本特定注意事项（V5/V7/V8/V9各自的特殊要求）
- ✅ 痕迹保留要求（产出必须落盘）
- ✅ 必须加载的文件清单（"使用前必须完整加载以下文件"）

**实例运行的AGENTS.md不应该包含**：
- ❌ 完整的分类学知识——放单独的分类学文件中，AGENTS.md只列"必须加载的分类学文件清单"
- ❌ 完整的提示词——放prompt.md中
- ❌ 题目和解答文本——放input.md中
- ❌ 系统的全局设计文档——AI不需要知道整个系统的设计，只需要知道自己的角色

## 分类学识别资产的处理

**当前问题**：Tell分类学Schema（AGENTS.md第913-993行，约80行）放在项目AGENTS.md中。随着分类学增长，这个节会越来越长，污染AGENTS.md。

**解决方案**：分类学识别资产从AGENTS.md中拆分到单独文件中。

**拆分原则**：
1. 每个分类学文件限制在**300行左右**
2. 如果单个分类学文件超过300行，必须拆分为多个文件
3. AGENTS.md中只保留"必须加载的分类学文件清单"——不保留分类学内容本身
4. AI在使用分类学之前，必须完整加载整个文件（不能只读一部分）

**分类学文件的拆分维度**：
- 按domain拆分——数论/代数/组合/几何/分析/跨域各一个文件
- 按段结构模式拆分——5大类各一个文件
- 按用途拆分——分类学Schema（结构定义）/ 识别指南（怎么用分类学识别trace）/ 案例库（具体例子）

**AI使用分类学文件的方式**：
```
# AGENTS.md中写：
## 必须加载的分类学文件
使用分类学识别trace之前，必须完整加载以下文件：
- taxonomy/schema.md（分类学结构定义，约100行）
- taxonomy/domain_algebra.md（代数域分类学，约200行）
- taxonomy/domain_number_theory.md（数论域分类学，约150行）
- ...（按需加载当前题目相关的domain文件）

# 直接提示词中写：
加载 {workdir}/AGENTS.md，按其中"必须加载的分类学文件"清单加载分类学文件，
然后加载 {workdir}/prompt.md 中的提示词...
```

## 文件大小控制

### 300行限制

**单个资产文件限制在300行左右**。超过300行的文件必须拆分。

**为什么300行**：
- AI的上下文窗口约20万token（约15万词，约30万中文字符）
- 单个文件300行约6000-9000中文字符，约占上下文的2-3%
- 留出足够上下文给其他文件、AI的thinking、AI的产出
- 300行是一个文件可以被AI"完整理解"的上限——超过这个长度，AI可能只关注开头和结尾

**哪些文件受300行限制**：
- 分类学识别资产文件
- 提示词文件（V5/V7/V8/V9等）——如果超过300行，考虑拆分为多个提示词文件
- AGENTS.md（实例运行版）——如果超过300行，考虑拆分
- 不受限制：input.md（题目和解答文本可能很长，不强制拆分）、程序验证脚本（代码文件不按行数限制）

### 超长检测和警报

**脚本系统应该检测资产文件超长，并发出警报到数据库的警报列表中。**

**检测逻辑**：
```python
# system/file_size_monitor.py（待实现，TODO-13）
MAX_LINES = 300
MAX_CHARS = 9000  # 约300行中文字符

def check_file_size(file_path: str) -> dict:
    """检查单个文件是否超长"""
    with open(file_path, 'r') as f:
        content = f.read()
    lines = content.count('\n') + 1
    chars = len(content)
    is_overlong = lines > MAX_LINES or chars > MAX_CHARS
    return {
        "file_path": file_path,
        "lines": lines,
        "chars": chars,
        "is_overlong": is_overlong,
        "severity": "warning" if is_overlong else "ok",
    }

def scan_asset_files(asset_dirs: list) -> list:
    """扫描所有资产文件，返回超长文件列表"""
    alerts = []
    for d in asset_dirs:
        for root, dirs, files in os.walk(d):
            for f in files:
                if f.endswith(('.md', '.txt')):
                    path = os.path.join(root, f)
                    result = check_file_size(path)
                    if result["is_overlong"]:
                        alerts.append(result)
    return alerts
```

**警报存储**：超长文件警报写入数据库的`alerts`表（TODO-14），后续检查的AI可以看到。

**alerts表字段**（TODO-14）：
- alert_id, alert_type("file_overlong"), file_path, lines, chars, detected_at, resolved_at, resolved_by

## 和其他规则的关系

- 和`six-ai-agent-launch.md`的关系：AI Agent启动规范定义"短启动提示词+提示词文件加载"，本rule定义"什么放直接提示词、什么放文件、什么放AGENTS.md"——两者配合使用。
- 和`six-trace-preservation.md`的关系：资产文件本身是痕迹保留的一部分——AI使用了哪些文件、文件的版本是什么，都需要记录。
- 和`six-dual-check-mechanism.md`的关系：文件超长检测是"代码能检查的"部分——脚本自动检测，不需要AI检查。AI检查的是"文件内容质量"。

## 固定资产的积累目录

固定内容（AGENTS.md模板、提示词等）在积累目录中管理，运行时复制到工作目录：

| 资产类型 | 积累目录 | 运行时复制到 |
|---|---|---|
| 脉络分析AI的AGENTS.md模板 | `system/assets/vein_analysis/AGENTS_V{5,7,8,9}.md` | 工作目录的`AGENTS.md` |
| 脉络分析提示词 | `第六代系统提示词积累目录/pipe_1_parser/step_2_grid_vein/...` | 工作目录的`prompt.md` |

**积累目录的管理原则**：
- 修改固定内容时，修改积累目录中的文件，不修改运行时工作目录中的副本
- 积累目录中的文件受300行限制（除提示词外——提示词是完整操作指南，拆分影响连贯性）
- 新增资产类型时，在`system/assets/`下创建新的子目录

## 数据库记录——运行时信息的抓手

运行时产生的动态信息（工作目录路径、会话ID、AI实例ID、产出路径等）写入数据库，不写入文件：

| 数据库集合 | 内容 | 查找方法 |
|---|---|---|
| `problem_entries` | 题目录入记录——每道题入题一条记录 | `db.find_problem_entries_by_problem_id(problem_id)` |
| `sessions` | 会话记录——每次入题或解题一条记录 | 按problem_id或session_type查找 |
| `ai_instances` | AI实例记录——每个devin cli实例一条记录 | 按session_id查找 |

**数据库操作统一通过`system/db.py`模块**，不直接操作ArangoDB客户端。其他模块（vein_analysis.py等）通过db.py读写数据库。
