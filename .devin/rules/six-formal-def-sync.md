# 形式化定义同步原则

**触发条件**：修改任何数据结构（dataclass）或Pipe函数签名时。
**来源文档**：319号（形式化定义）、`six/types.py`、`six/pipes.py`、`six/references.py`

## 规则

修改任何数据结构（dataclass）或Pipe函数签名时，必须同步更新三处：

1. **`six/types.py`或`six/pipes.py`**中的代码定义
2. **319号文档**中的形式化定义
3. **`six/references.py`**中的映射

三处必须对齐同步，dataclass名称/字段名/函数名/参数名必须一致。

新增dataclass或Pipe函数时，在319号文档中添加形式化定义，在`__init__.py`的`__all__`中导出。
