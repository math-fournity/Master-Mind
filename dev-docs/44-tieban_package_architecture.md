# 铁板神数计算包架构设计

**文件**：`dev-docs/44-tieban_package_architecture.md`
**日期**：2026-07-08
**定位**：`qizheng/tieban/` 包的模块结构、依赖关系、复用策略。

---

## 一、包目录结构

```
qizheng/tieban/
├── __init__.py          # 包入口，暴露核心API
├── core.py              # 核心算法层（共享常量+查表+三元甲子+五虎五鼠）
├── schools/
│   ├── __init__.py
│   ├── base.py          # TiebanSchool 抽象基类
│   ├── nanpai.py        # 南派（日干支+时干支主算）
│   ├── beipai.py        # 北派（月干支+时干支主算，含八卦滚法）
│   ├── jiangnan.py      # 江南派（八卦加则+甲流度考刻）
│   └── zhongzhou.py     # 中州派（算盘数法，可选）
├── corpus/
│   ├── __init__.py
│   ├── tieba_text.json  # 12000条条文结构化数据
│   ├── category_index.json  # 分类索引（从tieban_category_index.json扩展）
│   └── lookup.py        # 数序→条文查找函数
├── enum_engine.py       # 180年日历遍历枚举引擎
├── parallel.py          # 铁板+七政并行推演框架
└── tests/
    ├── __init__.py
    ├── test_core.py     # 核心算法测试
    ├── test_schools.py  # 学派测试
    └── test_enum.py     # 枚举引擎测试
```

---

## 二、模块依赖关系

```
tieban/core.py（无外部依赖，纯查表+计算）
    ↑
    ├── tieban/schools/base.py（定义接口）
    │   ├── tieban/schools/nanpai.py（依赖core）
    │   ├── tieban/schools/beipai.py（依赖core）
    │   ├── tieban/schools/jiangnan.py（依赖core）
    │   └── tieban/schools/zhongzhou.py（依赖core）
    │
    ├── tieban/enum_engine.py（依赖core + schools + corpus）
    │
    └── tieban/parallel.py（依赖schools + qizheng.chart）

tieban/corpus/（独立，可并行开发）
```

---

## 三、复用策略

### 3.1 从 tieban_enum.py 复用

| 内容 | 位置 | 复用方式 |
|---|---|---|
| 太玄数表（天干/地支） | `core.py:24-31` | 直接提取，补全验证 |
| 先天八卦数 | `core.py:34-35` | 直接提取 |
| 后天八卦数（洛书） | `core.py:38-39` | 直接提取 |
| 天干配卦 | `core.py:42-46` | 直接提取 |
| 地支配卦 | `core.py:49-57` | 直接提取 |
| 八刻分配 | `core.py:60-63` | 直接提取 |
| 天干/地支列表 | `core.py:67-68` | 直接提取 |
| 六十甲子 | `core.py:71` | 直接提取 |
| 算法A | `core.py:81-90` | 提取，补全注释 |
| 算法B1（先天） | `core.py:98-123` | 提取，补全互卦 |
| 算法B2（后天） | `core.py:126-164` | 提取，修复互卦 |

### 3.2 从 qizheng/core.py 复用

| 内容 | 位置 | 复用方式 |
|---|---|---|
| 天干地支常量 | core.py TIAN_GAN/DI_ZHI | 导入 |
| 五行表 | core.py wuxing_* | 导入 |
| 六十甲子纳音 | core.py calc_na_yin() | 导入 |
| 四柱计算 | core.py calc_four_poles() | 枚举引擎调用 |

### 3.3 新增内容

| 内容 | 模块 | 说明 |
|---|---|---|
| 三元甲子判定 | core.py | 新增，八卦滚法关键维度 |
| 五虎遁元/五鼠遁元 | core.py | 新增，修复tieban_enum.py bug |
| 互卦完整计算 | core.py | 新增64卦重卦表，修复简化近似 |
| 八卦滚法完整实现 | core.py 或 schools/beipai.py | 新增，需考据验证 |
| 学派抽象基类 | schools/base.py | 新增 |
| 条文语料库 | corpus/ | 从raw_tieban_text.md提取 |

---

## 四、关键设计决策

### 4.1 学派差异的统一抽象

所有学派实现 `TiebanSchool` 接口：

```python
class TiebanSchool(ABC):
    @abstractmethod
    def name(self) -> str: ...

    @abstractmethod
    def compute_base(self, four_poles: dict, gender: str, yuan: str) -> int:
        """计算基本数"""
        ...

    @abstractmethod
    def expand(self, base_num: int, gender: str) -> list[int]:
        """展开为数序集合"""
        ...

    @abstractmethod
    def kaoke(self, base_num: int, father_zhi: str, mother_zhi: str) -> int:
        """考刻叠加"""
        ...
```

### 4.2 枚举引擎的分层

```
外层：三元甲子（3种）× 年干支（60种）= 180年
  中层：月支（12种），月干由年干推出
    内层：日干支（按公历实际天数遍历，约30天/月）
      最内层：时支（12种），时干由日干推出
        刻（8种，最内层外部变量）
```

### 4.3 条文存储格式

```json
{
  "id": 8222,
  "category": "妻妾",
  "sub_category": "合和",
  "text": "鸳鸯织就欲双飞",
  "source": "坤集",
  "volume": 3,
  "verse": 15
}
```

---

## 五、执行顺序

1. **core.py**（核心算法层）—— 所有模块的基础
2. **schools/base.py**（抽象基类）—— 定义接口
3. **schools/nanpai.py + beipai.py**（南北派）—— 优先实现两个主要学派
4. **corpus/**（条文语料库）—— 可与 schools 并行
5. **enum_engine.py**（枚举引擎）—— 依赖 core + schools + corpus
6. **parallel.py**（并行推演）—— 依赖 schools + qizheng.chart
7. **schools/jiangnan.py + zhongzhou.py**（江南派+中州派）—— 后续补充
