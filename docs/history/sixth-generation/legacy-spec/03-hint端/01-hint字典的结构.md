# 01-hint字典的结构

**前置阅读**：01-基础概念/02-trace-tell-hint三步链路.md
**关联文件**：03-hint端/02-hint的Level梯度.md、07-工程规格/08-trace-tell-hint字典格式.md
**来源**：第五代说明书03-01、281号（高Level Hint的工程化）、333号（tell-hint多对多关系）

---

## §1 高Level方向→分领域low level化→翻译方向

hint字典的结构是从高Level方向到分领域low level化再到具体翻译方向的三层结构（继承自第五代）。

---

## §2 24+个翻译方向的穷举

（继承自第五代）

---

## §3 tell和hint的多对多关系

### §3.1 多对多关系

hint字典中一个tell_id可以关联多个hint_id，一个hint_id也可以被多个tell_id关联（333号）。

- 一个tell对应多个hint——同一个trace识别结果可以触发多个不同的方向提示
- 一个hint被多个tell指到——同一个方向提示可能被不同的识别结果触发

### §3.2 高Level hint的分领域low level化

"同构之桥"作为高Level hint方向，它的low level化不是单一的，而是分领域的：
- 数论领域的low level化——构造Frey曲线
- 代数几何领域的low level化——分析椭圆曲线性质
- 表示论领域的low level化——构造Galois表示

每个low level化都是一个独立的hint，它们共享"同构之桥"这个高Level方向名，但具体内容不同。

---

## §4 hint字典在第六代中的角色变化

hint仍然是从库里取出的，不是辅助AI现场生成的。但取出的触发条件变了——从"Pipe 2选定的tell"变为"汇总AI精筛的tell"。

---

## §5 待后续完善的内容

1. tell_hint_match多对多关系的具体schema
2. 高Level hint的分领域low level化的具体格式
3. 多对多关系下的hint选择策略
