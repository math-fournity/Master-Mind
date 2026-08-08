# isolation-audit

## Description

共享机器多AI隔离审计工作流。按隔离层次逐层检查，发现缺口并修复。被 `isolation-awareness` 规则触发时加载。

## 触发条件

- `isolation-awareness` 规则触发
- 用户要求检查隔离状态
- 新增共享资源使用前
- 定期审计

## 审计流程

### Step 1：文件系统隔离检查

```bash
# 确认当前repo路径
pwd  # 应为 /data/master-mind-glm5.2-grove/

# 确认没有写入禁止路径
# 检查最近的git操作
git log --oneline -5  # 应都在grove repo内

# 确认旧worktree不再使用
grep -rl "master-mind-glm5.2-worktree" --include="*.py" --include="*.sh" . 2>/dev/null | grep -v "^./runs/" | grep -v "^./subagent-docs/"
# 期望：无活跃文件残留（AGENTS.md中的"禁止触碰"警告引用除外）
```

### Step 2：数据库隔离检查

```bash
# 确认环境变量
source .env
echo $ARANGO_DB  # 应输出 grove_math

# 确认和上游不同前缀
# grove_math vs xishujuzhen_math —— 完全不同前缀 ✅

# 确认代码默认值安全
grep -r "os.environ.get.*ARANGO_DB" --include="*.py" . | grep -v ".venv" | head -5
# 检查默认值是否是上游库名（危险）还是安全值

# 确认数据库存在且有数据
curl -s -u root:REDACTED-DB-PASSWORD "http://localhost:8529/_api/database" | python3 -c "import json,sys; print([d for d in json.load(sys.stdin)['result'] if 'grove' in d or 'xishujuzhen' in d])"
# 应看到 grove_math 和 xishujuzhen_math 并存
```

### Step 3：工作目录隔离检查

```bash
# 确认Grove目录存在
ls -d /data/grove-agents-dir/ /data/grove-agents-trajectory/ /data/grove-parser-1/ 2>/dev/null

# 确认代码引用正确
grep -rn "grove-agents-dir\|grove-agents-trajectory\|grove-parser" --include="*.py" . | grep -v ".venv" | head -10

# 确认无旧路径残留
grep -rl "math-agent-glm5.2-tmux-agents\|math-agent-glm5.2-parser" --include="*.py" --include="*.sh" --include="*.md" . 2>/dev/null | grep -v "^./runs/" | grep -v "^./subagent-docs/"
# 期望：无残留
```

### Step 4：进程隔离检查

```bash
# 检查tmux sessions
tmux list-sessions 2>/dev/null

# 确认Grove的session命名模式
# 应为 harness-<exp-id>，不与上游的 <session> 模式冲突
```

### Step 5：网络端口检查

```bash
# 检查ArangoDB端口
lsof -i :8529 | head -3

# 检查mitmproxy端口
lsof -i :18889 | head -3

# 如果要起新服务，检查端口占用
# lsof -i :<新端口>
```

### Step 6：全局配置检查

```bash
# mitmproxy addon副本是否同步
diff ~/.mitmproxy/mitm_proto_capture.py xishujuzhen/mitm_thinking_intercept/mitm_proto_capture.py
# 期望：无差异（或仅有路径常量差异，已同步）

# .env是否正确
cat .env
# 期望：ARANGO_DB=grove_math
```

### Step 7：新增资源隔离评估

如果本次审计是因为新增了共享资源：

1. 新资源是否和上游用了不同的标识？（库名/目录名/端口/session名）
2. 标识是否完全不同前缀？（不能只差后缀）
3. 代码默认值是否安全？（忘了source .env时应该报错而非静默写到上游）
4. 是否需要更新269号文档的隔离演进历史？
5. 是否需要更新isolation-awareness规则的隔离层次表？

### Step 8：生成审计报告

审计完成后，输出：
- 各层隔离状态（✅/⚠️/❌）
- 发现的缺口
- 修复建议
- 是否需要更新269号文档

## 修复流程

发现隔离缺口时：

1. **评估影响**——缺口是否已经导致数据污染？
2. **如果已污染**——评估是否需要数据迁移/恢复
3. **修复代码**——更新路径常量、数据库名等
4. **修复数据**——如果需要，迁移数据到新的隔离位置
5. **验证修复**——重新跑审计流程确认缺口已关闭
6. **更新文档**——在269号文档的隔离演进历史中记录本次修复
7. **commit**——提交所有变更

## 关键教训（从269号文档提炼）

1. **数据库名必须完全不同前缀**——`xishujuzhen_math_glm52` vs `xishujuzhen_math` 只差后缀是危险的
2. **目录名不应包含共享的模型名**——`math-agent-glm5.2-*` 如果上游也用glm5.2就会撞
3. **代码默认值应安全**——`os.environ.get("ARANGO_DB", "xishujuzhen_math")` 的默认值是上游库名，忘了source .env会静默写到上游
4. **复制而非移动**——有运行中进程依赖旧路径时，复制数据到新路径，旧路径保留到进程结束
5. **mitmproxy addon有live副本**——`~/.mitmproxy/mitm_proto_capture.py` 是repo文件的副本，更新repo文件后需同步更新live副本
