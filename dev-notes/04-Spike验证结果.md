## Spike 验证结果（2026-07-07）


### 结论：swisseph 核心层可脱离 GUI 独立运行，输出 JSON 行星位置。

### 验证内容

编译 `swisseph/*.java`（35 个文件）+ 2 个极简 stub（`FileIO`/`Message`），写 `SpikeChart.java`，输入生辰→输出七政四余天体恒星黄道 JSON。

- **星历路径对齐**：已建软链 `ephe -> moira_extra_files/ephe`（方式 A 落地）。
- **编码问题**：swisseph 源文件为 Latin-1 编码（含度数符号 0xF7/0xF8），编译需 `-encoding ISO-8859-1`。
- **stub 隔离**：swisseph 依赖 `base.FileIO.getURL`（文件名转 URL）和 `base.Message.info`（空操作）。用 2 个极简 stub 替代，不拖入 base 的完整依赖链（Resource/RuleEntry 等）。
  - `FileIO.getURL` 返回 `new File(file_name).toURI().toURL()`（本地文件 URL）。
  - `Message.info` 空操作。
- **编译顺序**：stub（UTF-8）→ swisseph（ISO-8859-1）→ SpikeChart（UTF-8），分三步因 javac 不支持混合 encoding。

### 验证输出（示例）

输入：`1990 5 15 3.5 116.4 39.9`（1990-05-15 03:30 UT，北京）

输出（节选）：
```json
{"input":{"date_ut":"1990-05-15T03.5000","jd":2448026.6458,"lon":116.4,"lat":39.9,"ayanamsa":"Lahiri","frame":"sidereal"},
 "bodies":{
   "sun":{"lon":30.328762,"lat":-3.6E-5,"dist":1.01082,"lon_speed":0.964321,...},
   "moon":{"lon":269.074694,"lat":-1.517331,"dist":0.00265,"lon_speed":12.276706,...},
   "mercury":{"lon":14.333944,...},
   "venus":{"lon":348.688608,...},
   "mars":{"lon":324.344951,...},
   "jupiter":{"lon":75.748988,...},
   "saturn":{"lon":271.529468,...},
   "true_node_rohuo":{"lon":286.542122,...},
   "mean_apog_ziqi":{"lon":207.713408,...},
   "oscu_apog_yuebei":{"lon":222.445271,...}
 }}
```

10 个天体（七政 + 四余：罗睺/计都=真北交点、紫炁=远地点、月孛=osc apog）全部 `ret=65858`（成功），数值合理。

### Spike 产物

| 路径 | 说明 |
|---|---|
| `spike/src/SpikeChart.java` | spike 主程序，输入生辰→输出 JSON |
| `spike/src/org/athomeprojects/base/FileIO.java` | stub，替代 base.FileIO |
| `spike/src/org/athomeprojects/base/Message.java` | stub，替代 base.Message |
| `build/spike/` | 编译产物 |
| `ephe` | 软链 → `moira_extra_files/ephe` |

### 对后续路径的启示

- **swisseph 包是干净可用的核心资产**，0 GUI 耦合，只需 2 个 stub 即可独立运行。
- **Calculate.java**（47 个 Resource 调用 + 1 个 Message.question）不能直接独立运行，但它的七政四余逻辑（恒星黄道、宫位、大限）是 MOIRA 的命理核心，值得后续剥离或用 Python 重写时参考。
- **后续路径倾向**：swisseph 做星历底座（已验证可用），上层七政四余命理逻辑（恒星黄道模式、宫位、大限）用 Python 重写或从 Calculate 剥离——待下一步决策。

