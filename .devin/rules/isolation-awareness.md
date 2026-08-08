# 隔离意识触发规则

## 触发条件

当Grove AI执行以下操作时，必须先过隔离检查清单：

1. **使用新的共享资源**——新数据库、新目录、新端口、新服务
2. **修改路径常量**——代码中的 `BASE_DIR`、`TRAJECTORY_BASE`、`WORK_DIR` 等
3. **创建子进程工作目录**——新的Solver/Parser/实验目录
4. **引入新的第三方依赖**——可能带来新的共享资源
5. **用户提到"隔离"、"isolation"、"分开"、"冲突"**
6. **迁移repo或clone到新位置**
7. **定期审计**——每隔一段工作后主动检查隔离状态

## 行动

触发时：
1. 加载 `.devin/skills/isolation-audit/SKILL.md`
2. 按其中的审计流程检查所有隔离层次
3. 发现隔离缺口时立即修复
4. 修复后更新 `dev-docs/269` 号文档的隔离演进历史

## 隔离的黄金法则

两个AI的任何资源标识（库名、目录名、session名、端口）都应**完全不同前缀**，不能只靠后缀区分。

## 隔离层次（快速回忆）

| 层次 | 资源 | Grove | 上游 |
|---|---|---|---|
| 1 文件系统 | repo目录 | `/data/master-mind-glm5.2-grove/` | `/data/master-mind/` |
| 2 数据库 | ArangoDB database | `grove_math` | `xishujuzhen_math` |
| 3 工作目录 | Solver/Parser/trajectory | `/data/grove-agents-*/` | `/data/math-agent-{1,2}/` |
| 4 进程 | tmux session | `harness-<exp-id>` | `<session>` |
| 5 网络 | 端口 | 共享8529/18889（通过DB/mapping区分） | 同左 |

## 详细文档

完整隔离经验、检查清单、演进历史见 `dev-docs/269-v0-2026-08-08-共享机器多AI隔离经验与持续维护清单.md`。
