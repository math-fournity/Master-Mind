# 运行数字ID命名规范

**触发条件**：always-on——任何系统运行、测试、实验、审计存档时。

## 核心原则

**数据库的数字ID（入题序号/run_id）是为了保证每一次工作过程的全部运行产生的内容都是未来可查、可审计的。所以用入题工作的这次工作的数字ID命名这件事，应该在任何它应该出现的地方出现。**

## 数字ID必须出现的地方

### 1. 工作目录名

每次运行的工作目录必须以数字ID开头：

```
✅ palyground/absorb/vein_analysis/0004_imo2009p6/
✅ palyground/absorb/vein_analysis/0005_imo2009p6/
❌ /tmp/v8_test/                    ← 没有数字ID
❌ palyground/absorb/vein_analysis/imo2009p6/  ← 旧格式，没有数字ID
```

### 2. 数据库记录

每次运行的数据库记录（problem_entries/sessions等）必须包含数字ID字段：

```python
✅ record = {
    "_key": "0004_imo2009p6",
    "入题序号": 4,
    "problem_id": "imo2009p6",
    ...
}
❌ record = {
    "_key": "absorb_imo2009p6_1786426887185",  ← 只有时间戳，没有数字ID
    "入题序号": None,                           ← 缺失
    ...
}
```

### 3. 测试存档目录

审计存档目录必须以数字ID命名：

```
✅ system/tests/vein_analysis/runs/0004/
✅ system/tests/vein_analysis/runs/0005/
❌ system/tests/vein_analysis/runs/v8_test/   ← 没有数字ID
```

### 4. tmux session名

tmux session名必须包含数字ID：

```
✅ grade-0004-V8
✅ synth-0005
❌ v8_test                                 ← 没有数字ID
```

### 5. 日志文件名

日志文件名必须包含数字ID：

```
✅ three_phase_run0006.log
❌ v8_test.log                             ← 没有数字ID
```

### 6. 审计报告

审计报告必须标注数字ID：

```markdown
✅ # 审计报告——run_id=0005
❌ # 审计报告——V8测试                    ← 没有数字ID
```

## 单独测试某个组件时

单独测试某个组件（如V8格化）时，也必须分配数字ID。方法：

1. **从数据库获取下一个可用数字ID**——查problem_entries中最大的入题序号+1
2. **用数字ID命名测试目录**——如`palyground/absorb/vein_analysis/0008_imo2009p6_v8test/`
3. **在数据库创建记录**——即使只是测试，也创建problem_entries记录，标注status=test
4. **测试完成后存档**——测试产出存档到`system/tests/vein_analysis/runs/0008/`

**不要用`/tmp/`或无数字ID的目录做测试**——测试产出也是运行产生的内容，也需要未来可查可审计。

## 例外情况

只有以下情况可以不用数字ID：
- **baseline（当初4套POC）**——这是历史数据，当时没有数字ID规范。用`baseline/`目录名+版本号（V5/V7/V8/V10）标识。
- **纯代码开发**——不涉及系统运行时，如写代码、改提示词、改规则文件。

## 和运行痕迹全程保留规则的关系

运行痕迹全程保留规则（six-trace-preservation.md）要求"系统设计必须既要考虑运行逻辑，也要考虑痕迹保留"。本规则是痕迹保留的命名规范——数字ID是痕迹可查可审计的基础。没有数字ID的痕迹是找不到的，等于没有保留。
