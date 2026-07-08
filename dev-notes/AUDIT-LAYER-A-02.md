# AUDIT-LAYER-A-02：四余定义审计

**审计日期**：2026-07-16
**审计项**：A2 四余定义
**TODO ID**：20.12
**状态**：❌ 发现两个严重错误，已修复

---

## 一、审计范围

核对 `core.py` 中罗睺、计都、月孛、紫炁四余的天文定义，对照：
1. Java MOIRA 原版实现
2. 传统文献定义（《星学大成》+ 历史考据）

---

## 二、Java MOIRA 原版实现

### 2.1 行星索引和 Swiss Ephemeris 映射

```
index 10: TRUE_NODE  → SE_TRUE_NODE    → 罗睺
index 11: INV_TRUE_NODE → -1 (computed) → 计都 = 罗睺 + 180°
index 12: PURPLE     → -1 (custom)     → 紫炁（自定义线性运动）
index 13: MEAN_APOG  → SE_MEAN_APOG    → 月孛（平均远地点）
```

### 2.2 罗睺/计都的 true_as_north 开关

```java
// ChartData.java:4886
if (Resource.getPrefInt("true_as_north") == 0) {
    // 交换 TRUE_NODE 和 INV_TRUE_NODE
    double val = sign_pos[TRUE_NODE];
    sign_pos[TRUE_NODE] = sign_pos[INV_TRUE_NODE];
    sign_pos[INV_TRUE_NODE] = val;
}
```

- `true_as_north=1`（默认）：不交换 → 罗睺=升交点（新法/汤若望法）
- `true_as_north=0`：交换 → 罗睺=降交点（旧法/传统星命家法）

### 2.3 紫炁的自定义线性运动

```properties
# moira_s.prop
sign_computation_type=..., 1, ...  # index 12 = 1 (自定义轨道)
purple_period=10227.1792           # 周期 ≈ 28年
purple_base_date=1975, 3, 13, 16, 0  # 基准日期
purple_base_degree=230.5           # 基准度数
```

计算方式：`position = base_degree + (360/period) * (jd - jd_base)`

### 2.4 月孛

`SE_MEAN_APOG`（平均远地点），周期 ≈ 8.85 年。

---

## 三、我们的 Python 实现（审计前）

```python
# core.py:21-23
"true_node_rohuo":   swe.TRUE_NODE,   # 罗睺
"mean_apog_ziqi":    swe.MEAN_APOG,   # 紫炁  ← 错误
"oscu_apog_yuebei":  swe.OSCU_APOG,   # 月孛  ← 错误
```

---

## 四、错误对比

| 四余 | Java MOIRA | Python（审计前） | 判定 |
|---|---|---|---|
| 罗睺 | `SE_TRUE_NODE`（真升交点） | `swe.TRUE_NODE` | ✅ 一致 |
| 计都 | 罗睺+180° | 罗睺+180° | ✅ 一致 |
| **紫炁** | **自定义线性运动**（28年周期） | `swe.MEAN_APOG`（平均远地点，8.85年周期） | **❌ 完全错误** |
| **月孛** | `SE_MEAN_APOG`（平均远地点） | `swe.OSCU_APOG`（osculating远地点） | **❌ 错误** |

### 4.1 紫炁错误的影响

- Java：紫炁周期 ≈ 28 年，简单线性运动
- Python：紫炁周期 ≈ 8.85 年（平均远地点），非线性运动
- **两者计算出的紫炁位置完全不同**，差距可达数十度
- 影响所有涉及紫炁的排盘、神煞、格局判断

### 4.2 月孛错误的影响

- Java：月孛 = 平均远地点（MEAN_APOG），平滑运动
- Python：月孛 = osculating远地点（OSCU_APOG），有波动
- **两者在多数时间接近，但会有数度差异**
- 影响所有涉及月孛的排盘、神煞、格局判断

---

## 五、传统文献考据

### 5.1 罗睺/计都定义的历史变迁

来源：维基百科"七政四馀" + 学术论文"从'罗、计'到'四余'"

| 时代 | 罗睺 | 计都 | 备注 |
|---|---|---|---|
| 唐初（印度传入） | 升交点 | 月球远地点 | 《七曜攘灾诀》 |
| 唐末宋初 | **降交点**（交初） | **升交点**（交中） | 旧法，星命家沿袭 |
| 清初（汤若望） | **升交点** | **降交点** | 新法 |
| 传统星命家 | 降交点 | 升交点 | 沿袭旧法 |

**我们的实现**：罗睺=升交点（新法），与 Java MOIRA 默认一致，但与传统星学大成/果老星宗的旧法**相反**。

**建议**：添加 `true_as_north` 选项支持旧法，默认保持新法（与 Java 一致）。

### 5.2 紫炁的天文定义

来源：维基百科 + 学术论文

- 紫炁**没有明确的天文对应体**
- 可能源自闰法（19年7闰，28年约10闰）
- 周期约28年，与Java MOIRA的 `purple_period=10227.1792天` 一致
- **不是月球远地点**（平均远地点周期≈8.85年）

### 5.3 月孛的天文定义

- 月孛 = 月球远地点（继承自计都的原始定义）
- Java MOIRA 用 `SE_MEAN_APOG`（平均远地点）→ 正确
- Python 用 `SE_OSCU_APOG`（osculating远地点）→ 应改为 `SE_MEAN_APOG`

---

## 六、修复方案

### 6.1 紫炁修复

将 `swe.MEAN_APOG` 改为自定义线性运动，匹配 Java MOIRA 参数：
- 周期：10227.1792 天
- 基准日期：1975-03-13 16:00 UT
- 基准度数：230.5°

### 6.2 月孛修复

将 `swe.OSCU_APOG` 改为 `swe.MEAN_APOG`。

### 6.3 罗睺/计都

保持现状（与 Java MOIRA 默认一致），但添加 `true_as_north` 选项支持旧法。

---

## 七、验证

修复后对5个测试用例验证：
- 紫炁位置应与 Java MOIRA 一致（容差 0.01°）
- 月孛位置应与 Java MOIRA 一致（容差 0.01°）
- 罗睺/计都保持不变

### 7.1 基准点验证

用《授时历》1280年数据点（紫气在女二度≈285°恒星黄道）验证两个基准点：

| 基准 | 推算1280年紫炁恒星黄道 | 与女二度(285°)的差距 | 判定 |
|---|---|---|---|
| **Java MOIRA** (1975-03-13, 230.5°, 顺行) | 291.05° | **+6.05°** | ✅ 可接受（694年外推） |
| J2000.0 (290.1584°, 顺行) | 31.79° | -106.79° | ❌ 完全错误 |

**结论**：Java MOIRA 的基准更接近《授时历》数据，采用 Java 基准作为默认。

### 7.2 修复后验证结果

```
=== 四余位置验证（5个测试用例）===
日期                   罗睺           计都           紫炁           月孛
1990-05-15   3.5h  286.5423     106.5423     41.8393      207.7134
1985-01-01   0.0h  32.9440      212.9440     332.9165     349.4964
2000-06-15  12.0h  90.9807      270.9807     171.3889     258.0385
1975-03-13  16.0h  220.0458     40.0458      206.9894     310.5417
1988-12-25   6.0h  313.0595     133.0595     24.0510      151.2702

✅ 计都 = 罗睺 + 180° 验证通过
✅ 紫炁速度 ≈ 0.0352°/天 验证通过
✅ 紫炁线性运动公式验证通过
```

### 7.3 双模式验证

- `set_four_yu_mode(true_as_north=True)`（默认/新法）：罗睺=升交点 ✅
- `set_four_yu_mode(true_as_north=False)`（旧法）：罗睺=降交点，与新法计都交换 ✅
- `set_four_yu_mode(yuebei_mode='mean')`（默认）：月孛=MEAN_APOG ✅
- `set_four_yu_mode(yuebei_mode='oscu')`（可选）：月孛=OSCU_APOG ✅

---

## 八、修复内容

### 8.1 core.py 修改

1. **紫炁**：从 `swe.MEAN_APOG` 改为匀速线性运动
   - 周期：10227.1792 天（≈28年）
   - 基准：1975-03-13 16:00 UT，回归黄道 230.5°
   - sidereal 模式下减去 ayanamsa
   - 新增 `calc_ziqi()` 函数

2. **月孛**：从 `swe.OSCU_APOG` 改为 `swe.MEAN_APOG`
   - key 从 `oscu_apog_yuebei` 改为 `mean_apog_yuebei`
   - 保留 oscu 模式作为可选

3. **罗睺/计都**：添加 `true_as_north` 开关
   - True（默认/新法）：罗睺=升交点
   - False（旧法）：交换罗睺和计都

4. **新增**：`set_four_yu_mode()` 函数切换计算模式

### 8.2 受影响文件

- `qizheng/core.py`：BODIES 重构 + calc_ziqi + calc_all_bodies 重写
- `qizheng/spike_chart.py`：同步修复
- `qizheng/rectify.py`：添加紫炁反推支持
- `qizheng/render.py`：key 名替换
- `qizheng/svg_chart.py`：key 名替换

### 8.3 兼容性

- 紫炁 key 保持 `mean_apog_ziqi`（不变）
- 月孛 key 从 `oscu_apog_yuebei` 改为 `mean_apog_yuebei`（**breaking change**）
- 所有引用旧 key 的代码已同步更新
