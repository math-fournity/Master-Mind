# 第2步要求：形式上下文矩阵构造

## 你要做的

读取 `segments.json`（你已经在第1步完成的格化），从所有段的features中提取特征集合，构造形式上下文矩阵(G,M,I)。

**这一步只做机械的矩阵构造**——不做任何格化判断，不做验证。

## 构造步骤

1. 从 `segments.json` 读取所有段id → 构成G
2. 从 `segments.json` 的所有段的features中提取所有特征 → 去重并集 → 构成M
3. 对每个段i和每个特征j，判断段i的features中是否包含特征j → 构成I矩阵
   - I[i][j] = 1 如果段i的features包含特征j
   - I[i][j] = 0 如果段i的features不包含特征j

## 产出格式

填充 `formal_context.json`，格式如下：

```json
{
  "version": "V8",
  "phase": "grading",
  "step": 2,
  "G": ["段1", "段2", "段3"],
  "M": ["排序", "WLOG归约", "x的使用", "aₙ的使用", "鸽巢论证"],
  "I": [
    [1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1]
  ]
}
```

## 不做验证

**不要在thinking中做矩阵验证**——矩阵验证是程序的工作，verify_lattice_completeness.py会做。你只负责从segments.json提取特征和构造矩阵。

## 完成后

填充完 `formal_context.json` 后，创建 `step2_done.md`（空文件）作为完成标记。

然后创建 `DONE.md`（空文件）作为全部完成的信号。
