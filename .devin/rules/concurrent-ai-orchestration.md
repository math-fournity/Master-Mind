# 并发AI编排规则（always-on）

## 核心约束

**本机器最多同时运行2个推理AI实例。** 如果任务需要N个AI（N>2），必须用2个AI为一组串行编排完成。

## 适用范围

"推理AI实例"指通过solver-harness启动的devin cli实例（做题AI）。不包括：
- DevinCliParserProvider的`devin -p`单轮调用（parser角色，短时进程）
- Grove AI自身（即我，编排者）

## 编排策略

### 串行模式（阶段2，当前）

一次只启动1个推理AI，等它终止后再启动下一个。不需要并发管理。

### 2并发模式（阶段3，未来）

同时运行2个推理AI，在2棵不同的子树上探索。当任一AI终止时：
1. 提取该AI的trajectory节点写入树
2. 在终点节点检索方向
3. 立即启动新AI填补空位（保持2个AI在运行）

### N>2任务的处理

如果任务需要30个AI的探索量：
- 用2并发模式，分15批，每批2个AI
- 每批AI终止后整理树、检索方向、启动下一批
- 不是同时启动30个AI——那是资源不够的

## 资源约束原因

- mitmproxy共享端口18889，2个AI的流量通过work_dir_mapping区分，更多AI会增加匹配冲突
- sessions.db是单文件SQLite，并发写入有锁竞争
- 机器CPU/内存有限，2个devin cli实例已是合理上限
- tmux session管理复杂度随并发数增长

## 实现位置

- 串行编排：`scripts/serial_multi_ai.py`（当前）
- 2并发编排：未来实现`scripts/parallel_multi_ai.py`或`ai_manager.py`
- 并发数常量：`MAX_CONCURRENT_AI = 2`
