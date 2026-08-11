# 第4步要求：形式上下文矩阵构造

## 你要做的

读取 `conventional_features.json` 和 `role_features.json`，合并所有特征，构造形式上下文矩阵(G,M,I)。

## 形式上下文 (G, M, I)

- **G** = 所有段的集合（从segments.json读取段id列表）
- **M** = 所有段的所有特征的去重并集（常规思维特征 + 关键实体角色特征）
- **I** = 关系矩阵（N×K的0/1矩阵，段i具有特征j则I[i][j]=1）

## 构造步骤

1. 从 `segments.json` 读取所有段id → 构成G
2. 从 `conventional_features.json` 读取所有常规思维特征 → 加入M
3. 从 `role_features.json` 读取所有关键实体角色特征 → 加入M
4. M = 常规特征和角色特征的去重并集
5. 对每个段i和每个特征j，判断段i是否具有特征j → 构成I矩阵

## 产出格式

### formal_context.json

```json
{
  "version": "V8",
  "phase": "grading",
  "step": 4,
  "G": ["段1", "段2", "段3"],
  "M": ["排序", "WLOG归约", "x的使用", "aₙ的使用", "鸽巢论证"],
  "I": [
    [1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1]
  ]
}
```

### 更新segments.json

同时更新 `segments.json`——把合并后的所有特征（常规+角色）填入每个段的features字段：

```json
{
  "version": "V8",
  "phase": "grading",
  "step": 4,
  "segments": [
    {
      "id": "段1",
      "content": "这段在做什么（简述）",
      "features": ["排序", "WLOG归约"]
    },
    {
      "id": "段2",
      "content": "这段在做什么（简述）",
      "features": ["x的使用", "aₙ的使用"]
    }
  ]
}
```

## 不做验证

**不要在thinking中做矩阵验证**——矩阵验证是程序的工作，verify_lattice_completeness.py会做。你只负责合并特征和构造矩阵。

## 完成后

填充完 `formal_context.json` 并更新 `segments.json` 后，创建 `step4_done.md`（空文件）作为完成标记。

然后创建 `DONE.md`（空文件）作为全部完成的信号。
