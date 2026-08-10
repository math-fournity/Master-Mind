# 反射原则

**触发条件**：设计或修改six/中任何Pipe函数时。
**来源文档**：`six/reflection.py`

## 规则

设计或修改任何Pipe函数时，考虑这个Pipe需不需要反射点——在合适的地方插入`reflect_xxx()`子函数。

反射点在`reflection.py`的`REFLECTION_DISTRIBUTION`中记录。系统运行时积累反射数据，反射结果反馈到提示词/分类体系/数据结构/Pipe衔接。

反射的三层对象：
1. 反射自己的产出——trace是否准确、tell是否合理、hint是否有效
2. 反射自己的流程——Pipe之间的衔接是否顺畅、步骤是否有冗余或缺失
3. 反射自己的认知——对数学思维的理解、对trace/tell/hint的定义、对格化的方法
