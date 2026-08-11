# 08-trace-tell-hint字典格式

**前置阅读**：01-基础概念/02-trace-tell-hint三步链路.md
**关联文件**：07-工程规格/06-ArangoDB-schema.md、03-hint端/01-hint字典的结构.md
**来源**：第五代说明书07-07、309号§5、333号§2.1

---

## §1 trace的JSON格式

```json
{
  "trace_id": "trace_001",
  "thinking_id": "thinking_20260810_001",
  "trace_text": "AI在数论域内反复尝试模分析未突破，未尝试跨域翻译",
  "trace_type": "非局部",
  "domain": "数论",
  "produced_by": "Telling_AI_数论",
  "timestamp": "2026-08-10T12:00:00Z"
}
```

---

## §2 tell的JSON格式

```json
{
  "tell_id": "tell_001",
  "tell_text": "AI未尝试从a^p+b^p=c^p构造椭圆曲线E: y²=x(x-a^p)(x+b^p)",
  "domain": "跨域",
  "大概念": "跨域桥接",
  "小概念": "同构之桥",
  "关联hint_id": ["hint_001", "hint_002", "hint_003"],
  "来源": "mathematics",
  "Level": 0.8
}
```

注意：`关联hint_id`是数组——一个tell可以关联多个hint（333号多对多关系）。

---

## §3 hint的JSON格式

```json
{
  "hint_id": "hint_001",
  "hint_text": "考虑构造Frey曲线 E: y²=x(x-a^p)(x+b^p)，将整数方程问题翻译到椭圆曲线领域",
  "Level": 0.8,
  "关联tell_id": ["tell_001", "tell_042"]
}
```

注意：`关联tell_id`是数组——一个hint可以被多个tell指到（333号多对多关系）。

---

## §4 trace→tell匹配关系的JSON格式

```json
{
  "trace_id": "trace_001",
  "tell_id": "tell_001",
  "match_score": 0.85,
  "确认状态": "confirmed"
}
```

---

## §5 tell→hint多对多关系的JSON格式

tell_hint_match集合（333号§2.1）：

```json
{
  "tell_id": "tell_001",
  "hint_id": "hint_001",
  "match_type": "primary"
}
```

```json
{
  "tell_id": "tell_001",
  "hint_id": "hint_002",
  "match_type": "secondary"
}
```

**多对多关系**：
- 一个tell_id可以关联多个hint_id——同一个trace识别结果可以触发多个不同的方向提示
- 一个hint_id也可以被多个tell_id关联——同一个方向提示可能被不同的识别结果触发

例如"同构之桥tell"可以对应"考虑椭圆曲线方向""考虑表示论方向""考虑代数几何方向"等多个hint；"考虑椭圆曲线方向"这个hint，可能被"同构之桥tell"触发，也可能被"代数变换tell"触发。

---

## §6 和第五代tell-hint字典格式的对比

- 新增trace格式（第五代没有trace概念）
- 新增trace→tell匹配关系格式
- 新增tell→hint多对多关系格式（第五代是一对一）
- tell的`关联hint_id`从单值变为数组
- hint的`关联tell_id`从单值变为数组

---

## §7 待后续完善的内容

1. match_type的字段值定义——primary/secondary/...的含义
2. 多对多关系下的hint选择策略——一个tell对应多个hint时，如何选择最合适的hint
3. 高Level概念解释库的JSON格式——三种解释文本的存储格式
