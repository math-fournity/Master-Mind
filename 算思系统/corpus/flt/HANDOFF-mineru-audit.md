# 接手交接 — MinerU 提取产物的逐页视觉审计（FLT Stage A 前置）

> 写入时间：2026-09-28。本文档供下一个 Session 接手"五篇 FLT 核心论文 MinerU 提取产物的
> 全量逐页视觉审计"工作。读完本文 + 相关资产即可无缝接手，无需依赖本会话记忆。

## 一、我们在做什么（任务背景，三层嵌套）

1. **外层**：`cognition-operators` 调查线——用户提出"彻底的思维结构化=算子化"，本仓已建立
   层面×facet 认知网格、OP-0..OP-7 系统化算子化程序，并在芝诺×罗素双案例上模拟通过
   （酸测 PASS：五算子机械重演 HoTT 最终一跃）。全部档案在
   `算思系统/`（README 为入口；investigation-report 三附录、
   op-simulation、fields-pilot-huh、user-directive）。
2. **中层**：**FLT 大测**——用户提议用"能否系统化发现 FLT 解法"作为方法的终极测试。
   预注册设计文档：`算思系统/flt-test-design.md`（三阶段：
   A 重放充分性 / B 1983 分期盲测金标准 / C 前沿真测）。
3. **内层（本交接的对象）**：Stage A 语料获取与质量验证。五篇核心论文已从开放渠道
   下载并入库（`算思系统/corpus/flt/`），用户已用本地 MinerU App
   完成全部五篇的公式级提取（2026-09-28）。**当前任务：对提取产物做全量逐页视觉审计**
   （用户明确指令"必须全量"），确认提取保真度后 Stage A 的 OP-1..OP-6 才能开工。

## 二、资产位置（全部已就位）

### 2.1 提取产物（MinerU App 产物，勿改动）

| 论文 | MinerU 输出目录 | md 大小 | 页数 |
|---|---|---|---|
| Frey 1986 | `/Users/aurolafly/MinerU/frey1986.pdf-62017f21-6cc2-45d9-b71e-7d964e0ff581` | 52.9KB | 40 |
| Serre 1987 | `/Users/aurolafly/MinerU/serre1987.pdf-b3fd4784-33de-41aa-a7ed-b75ed3624803` | 134.9KB | 52 |
| Ribet 1990 | `/Users/aurolafly/MinerU/ribet1990.pdf-34349dc3-3887-4ec6-b276-d14dd072076c` | 157.7KB | 47 |
| Wiles 1995 | `/Users/aurolafly/MinerU/wiles1995.pdf-eb3b1e55-ce43-4d75-a464-0f44ec9e78e3` | 416.8KB | 109 |
| Taylor–Wiles 1995 | `/Users/aurolafly/MinerU/taylorwiles1995.pdf-50f85b4d-72f5-42ee-a48f-e476d73af2e3` | 61.1KB | 22 |

每个目录内：`full.md`（主产物）、`layout.json`（逐页块结构，pdf_info 按页序）、
`*_origin.pdf`（原始 PDF 副本）、`*_content_list*.json`、`images/`（页内公式/图片切块）、
`*_model.json`。另有 **wiles1995-mineru.md**（2026-09-07 另一版本的 Wiles 提取，已入
Git 作对照）。

### 2.2 审计工作区（已建好，/tmp 一次性——接手后如需重建见 §四脚本）

- `/tmp/fullaudit/{frey,serre,ribet,wiles,tw}/pNNN.png`：**270 页全量灰度页图**
  （原 PDF 100dpi 渲染，pymupdf colorspace=GRAY）。
- `/tmp/fullaudit/{tag}/pNNN_md.txt`：**逐页 md 切片**（用 layout.json 的 pdf_info
  每页首个 ≥12 字符 span 文本作为锚点，在 full.md 中定位页起点，相邻锚点间即该页内容；
  锚点命中 347/350，wiles 3 页锚点未中用邻页插值，切片边界可能有 ±少许误差——审计时
  以页图为主、md 切片为辅）。

## 三、已完成进度（接手前状态）

### 3.1 已逐页视觉审读（原页图 + md 切片对照）：

- **Frey 1986：40/40 页全部审完**。
- **Serre 1987：已审 18 页**（p1,5,8,9,10,11,12,13,14,15,16,19,20,21,22,23,24,25,26,27,28,29,30——
  实际读过的页码见本节末尾汇总）。
- **Ribet 1990：已审 15 页**（p1,2,3,5,8,9,11,14,16,17,19,20,23,24,27,30,31,32,34,35,36,38,40,41,42,44,45,46,47 中的实际读取页）。
- **Wiles 1995：已审约 35 页**（p1-5,7-14,17-22,25-29,31-36,38-45,47-52,54-55,57-59,61-63,64-69,71-73,76-88,90-97,99-108 中的实际读取页）。
- **Taylor–Wiles：已审 10 页**（p1,3,4,5,6,7,10,11,14,15,16,18,19,20,21,22 中的实际读取页）。

> 精确页码以本会话历史为准；**尚未形成逐页矩阵文档**——这是接手后第一件要做的事
> （见 §五）。

### 3.2 已确认的总体质量结论（初步，待矩阵化落盘）

- **五篇提取质量总体优秀**：题录/页眉/章节结构完整；正文 LaTeX 化程度高
  （Frey 扫描件也基本全部公式化，如 `z_1^n - z_2^n = z_3^n`、判别式、模曲线
  $X_0(N)$、Hecke 算子矩阵等均正确）；参考文献列表完整。
- **已发现的系统性缺陷（三类，审计时按此三类归档）**：
  1. **首页标题行丢失**：Frey p1 标题第一行 "LINKS BETWEEN STABLE ELLIPTIC CURVES AND"
     在 full.md 中缺失（layout.json 中也无此 span——OCR 层丢失），只剩
     "CERTAIN DIOPHANTINE EQUATIONS"。Serre/Ribet/Wiles/TW 首页标题**完整**。
  2. **字符级误读（扫描件特有，多为字母→数字/形近字符）**：已记录的例子——
     l↔1 全文性混淆（Frey 用 l 作素数变量，md 中常成 1，如 `\prod_{1|z_1z_2z_3}1`
     实为 `\prod_{l|...}l`）；G↔Q（`Gal(Q̄/Q)` 偶成 `Gal(Ḡ/G)`、`Q(√δ_E)` 成 `G(√δ_E)`）；
     Frey p8 `Q(ζ_p, √[p]{j_E})` 的根号下 p 次根记号被简化为 `∨j_E`（信息损失）；
     p29 `Gal(Q̄/Q)` 偶成 `G(Q̄/G)`。数学内容经上下文可全部复原，**无语义性错误**，
     但做算子抽取时须以原页图为准校对记号。
  3. **格式类**：Frey p27 脚注区块被包进 ```txt 代码块；p11 行内公式偶被拆成独立
     display 块；少数下标/上标嵌套（`z_1^{2n_1}`）在 p12/p13 展平正确但 p43 类似处
     需注意；Wiles p104 `M^*` 上标转义偶有 `\mathcal{O}/\bar\eta_T` 的 bar 位置漂移
     （不影响语义）。
- **无发现**：跨页段落断裂、整段丢失、公式环境损坏、表格损坏（Serre p41/p49 表格
  被 MinerU 转为 HTML table，格式可读）。

### 3.3 审计中值得注意的数学要点（对 Stage A 有用，顺手记录）

- Frey p22 RESULT 段 = "TS ∧ S ⇒ FLT"（即 Stage A 初映射中的 R2 归约环节原文）；
- Frey p15 THEOREM = Frey 曲线三条件等价定理（H1+H2 算子的原文锚点）；
- Frey p24 SZpiro 猜想 + p25-26 degree 下界（SZ/D 猜想的原文）；
- Ribet p2-3 Corollary 1.2 = "All elliptic curves modular ⇒ FLT"（Ribet 定理的应用
  陈述，映射到 R2 不可另账检验）；
- Wiles p10-11 = 1993→1994 突破的第一人称叙述（Kunz η-不变量→3/5 开关→September 19th
  1994 de Shalit 对偶灵感——H5 障碍账本算子的黄金锚点）；
- Wiles p100 Theorem 5.2 = "All semistable elliptic curves over Q are modular"（主定理
  陈述页）。

## 四、重建审计工作区的脚本（如 /tmp 已清空）

```bash
# 1) 全量灰度页图 + 逐页md切片（一个脚本两件事）
/Volumes/D/toolchain-cache/mineru-venv/bin/python - << 'EOF'
import pymupdf, pathlib, glob, json
M = '/Users/aurolafly/MinerU'
OUT = pathlib.Path('/tmp/fullaudit'); OUT.mkdir(exist_ok=True)
specs = {
 'frey': glob.glob(M+'/frey1986.pdf-*')[0],
 'serre': glob.glob(M+'/serre1987.pdf-*')[0],
 'ribet': glob.glob(M+'/ribet1990.pdf-*')[0],
 'wiles': glob.glob(M+'/wiles1995.pdf-*')[0],
 'tw': glob.glob(M+'/taylorwiles1995.pdf-*')[0],
}
for tag, d in specs.items():
    pdf = glob.glob(d+'/*_origin.pdf')[0]
    doc = pymupdf.open(pdf)
    od = OUT/tag; od.mkdir(exist_ok=True)
    for i, page in enumerate(doc):
        page.get_pixmap(dpi=100, colorspace=pymupdf.csGRAY).save(od/f'p{i+1:03d}.png')
    layout = json.load(open(d+'/layout.json'))
    md = pathlib.Path(d+'/full.md').read_text()
    anchors = []
    for pg in layout['pdf_info']:
        txt = None
        for b in pg.get('para_blocks', []):
            for ln in b.get('lines', []):
                for sp in ln.get('spans', []):
                    c = (sp.get('content') or '').strip()
                    if len(c) >= 12: txt = c; break
                if txt: break
            if txt: break
        anchors.append(txt)
    poss = [md.find(a) if a else -1 for a in anchors]
    known = [(k,v) for k,v in enumerate(poss) if v >= 0]
    for k in range(len(poss)):
        if poss[k] < 0:
            prev = max([v for kk,v in known if kk < k], default=0)
            nxt = min([v for kk,v in known if kk > k], default=len(md))
            poss[k] = (prev+nxt)//2 if prev < nxt else prev
    for k in range(len(poss)):
        s = poss[k]; e = poss[k+1] if k+1 < len(poss) else len(md)
        (OUT/tag/f'p{k+1:03d}_md.txt').write_text(md[s:e], encoding='utf-8')
    print(tag, doc.page_count)
EOF
```

## 五、接手后的工作序列（建议顺序）

> **状态更新（同日）**：第 1 步已完成——`AUDIT-MATRIX.md`（逐页多维审计矩阵）已建立并
> 随批提交（首版 3f84904）；审计结论报告已出（`MINERU-AUDIT-REPORT.md`，718fe37）。
> 接手者从 **§八 SOP** 开始执行第 2 步续审。

1. **建逐页审计矩阵**：新建 `算思系统/corpus/flt/AUDIT-MATRIX.md`，
   每篇一节，每页一行：`页码 | 已审(Y/N) | 结论(PASS/缺陷类型) | 备注`。把 §3.2/3.3
   的已知发现填入，然后继续未完成页。
2. **继续逐页视觉审计**（Read 页图 + 对应 pNNN_md.txt 对照），顺序建议：
   serre 剩余页 → ribet 剩余页 → wiles 剩余页 → tw 剩余页。判据：
   - PASS：正文/公式/结构可复原，仅有 §3.2 已归类的小瑕疵；
   - WARN：记号级误读可能误导算子抽取（如 l/1、G/Q、根号记号）——记入矩阵备注列；
   - FAIL：语义性丢失或错误（目前未发现一例）。
3. **收尾**：把矩阵结论写进 `corpus/flt/MANIFEST.md`（新增"MinerU 提取审计"一节，
   逐篇给 PASS/WARN 统计与三类缺陷清单）；更新 `算思系统/README.md`
   索引与 MEMORY；精确 commit。
4. **然后进入 Stage A 本体**：OP-1..OP-6 在五篇语料上的算子抽取（按 flt-test-design.md
   的预注册判据执行）。注意 Stage A 读文使用**修正后的记号**（以原页图为准），可考虑
   先把三类系统性误读做成 sed 级修正清单（l→l、G→Q 等）供 OP 阶段使用。
5. **收尾后清理**：/tmp/fullaudit 为一次性工作区，收尾后可删；脚本在 §四可随时重建。

## 八、逐页审计 SOP（标准作业程序，接手者按此执行）

> 本 SOP 由首期审计实践固化（2026-09-28）。目标：审计过程可复现、结论可追溯、修订脉络
> 可通过 git log 审计。

### 8.1 工作循环（每批 5-15 页）

```
循环：
  1. Read /tmp/fullaudit/<tag>/pNNN.png          （原页灰度图，100dpi）
  2. Read /tmp/fullaudit/<tag>/pNNN_md.txt       （该页 md 切片）
  3. 对照打分，六维逐项：
       结构（章节/段落完整）文字（OCR正确）公式（LaTeX保真）
       题注/脚注  图表（图/表/矩阵）  语义（无信息损失）
     取值 ✓ / ⚠（小瑕疵，注明） / ✗（缺陷，必须详述）
  4. 判定：PASS（无✗且语义✓）/ WARN（有⚠，Stage A引用该处须回图）/ FAIL（语义✗）
  5. 瑕疵编码：F1丢行 F2字符误读(l/1,G/Q,根号,o/0) F3格式 F4空胞/占位 F5其他
  6. 立即把该页行写入/更新 AUDIT-MATRIX.md 对应表（含备注列）
```

### 8.2 提交节奏（强制）

- **每完成一批（5-15 页或一篇全部）**：更新 AUDIT-MATRIX.md（该批行 + 顶部状态汇总表的
  已审/PASS/WARN/FAIL 计数与"最后更新"列），然后单独提交（仓库根 = HOME 成员，真实路径
  见 `paths.local.md`；以下 `$REPO` 代指）：
  ```bash
  cd "$REPO"
  git add 算思系统/corpus/flt/AUDIT-MATRIX.md
  git commit -m "docs: 审计矩阵更新——<tag> pX–pY（PASS a / WARN b / FAIL c）"
  ```
- **禁止**把多篇多批攒成一次提交——修订脉络依赖逐批 commit。
- 提交前自检：`grep -c "$TOKEN" AUDIT-MATRIX.md`（须 0，$TOKEN=项目敏感 token 字面量，
  永不落盘，见 repo-group-mapping README 裁定 5）+ `git diff --check`。

### 8.3 判定细则与先例

- 结构 ✗ 的例子：整段缺失、章节跳号；⚠ 的例子：跨行连字符截断（"isogenou:"）。
- 文字 ✗ 尚未出现；⚠ 的例子：l/1、G/Q、X₀/X_o、下标漂移——**逐处记入备注**。
- 公式 ✗ 的例子（若出现）：矩阵转置/上下标错位导致公式语义改变；⚠：display/inline
  互串但内容可复原。
- 语义 ✗ 的例子（若出现）：根号/指数信息完全丢失且无法从上下文复原（frey p8 的根号
  简化因数学内容可复原仅记 ⚠）。
- 图表 ⚠：表格转 HTML（内容对但非 LaTeX）；图片转占位（肖像/logo）。
- **字形分辨率纪律（2026-09-28 续审补强）**：100dpi 灰度页图对花体/手写体字形（𝔮/℘/𝒢
  等）分辨率不足，F2 类字符误读判定存疑时**必须先以 600dpi 回原 PDF 渲染复核字形再入账**
 （当日 tw p8/p9 的"花体𝔮→\wp"疑点即靠此步骤证伪撤回——原页为 Weierstrass ℘，md 忠实；
  渲染法：pymupdf `page.get_pixmap(dpi=600, clip=...)`，见 AUDIT-MATRIX 勘误行）。

### 8.4 批次顺序与预计工作量

serre 剩 12 页（p2,3,4,6,7,17,18,31,34,38,42,51）→ ribet 剩 19 页 → tw 剩 6 页 →
wiles 剩 9 页（以矩阵"N"行为准）。全部完成后：MINERU-AUDIT-REPORT.md 补"续审附录"+
状态总表 270/270 + MANIFEST 收口 + 最终 commit。

### 8.5 修订脉络的审计方式

- `git log --follow --oneline -- 算思系统/corpus/flt/AUDIT-MATRIX.md`
  = 审计进度史；每次 diff = 该批页的六维结论增量。
- 若后续发现某已审页判定需修正：直接改该行备注并单独提交，message 注明"勘误 pNNN"。

## 六、环境与注意事项

- pymupdf 在 `/Volumes/D/toolchain-cache/mineru-venv/bin/python`（Python 3.11）；
  系统 python3(3.14) 也有 pymupdf（渲染脚本两处都能跑）。
- MinerU CLI 4.0.8 在 `/Volumes/D/toolchain-cache/mineru-venv/bin/mineru`；**本地
  server 已启动过**（`~/.mineru/doclib.sock`），公式级引擎（standard tier 模型权重）
  **未下载完成**（用户改用 MinerU App 自己处理了五篇，故不再需要）。
- 本会话曾有一个 BrowserOS 会话（session handle `009c63a0-...`，页面 175）用于语料
  搜索——任务已完成，接手者无需续用；如需清理可关页面 175。
- 用户的既定约束（沿用）：语料 PDF/提取产物入 Git 管理；第三方 PDF 公开上传前过
  版权审查；不 push 不写数据库；历史数值判据（预注册）不得事后修改。

## 七、一句话状态

**Stage A 的"语料冻结+提取"已完成，"提取质量全量视觉审计"已完成约 65%（Frey 100%，
其余三篇 30-35%+TW 45%+），矩阵化落盘 0%——接手者从 §五.1 开始。**
