# FLT 语料（Stage A）— 获取清单

> 获取日 2026-09-28。方法：BrowserOS（BrowserClaw）发现直链 + curl 拉取；身份验证=pymupdf
> 页数+首页题录逐篇核对。**五篇核心全部入库。**
>
> **2026-09-28 更新**：五篇已全部由用户本地 MinerU App 完成公式级提取（输出目录清单与
> 提取产物的**全量逐页视觉审计进度、方法、已发现缺陷、接手说明**见同目录
> `HANDOFF-mineru-audit.md`）。**全量逐页视觉审计已完成 270/270**（结论报告
> `MINERU-AUDIT-REPORT.md` 含续审附录；逐页六维明细 `AUDIT-MATRIX.md`）：
> PASS 249 / WARN 21 / **FAIL 0**——题录/结构/公式保真优秀，三类系统性瑕疵（Frey 首页
> 标题首行 OCR 丢失 + serre p2 一处脚注丢失、扫描件字符级误读 l↔1 与 G↔Q 与根号简化、
> 少量格式问题）均无语义性错误。**审计状态=全量完成；Stage A 准入判定=五篇全部 PASS**，
> 引用扫描件公式须对照原页图。

| 文件 | 身份（已验证） | 来源 | SHA256 前16 |
|---|---|---|---|
| wiles1995.pdf | Wiles, *Modular elliptic curves and Fermat's Last Theorem*, Annals 141 (1995) 443-551，109 页全文 | wstein.org 课程镜像 | a672f11b0acc33f8 |
| wiles1995-mineru.md | 同论文 MinerU 提取（真 LaTeX 自包含；用户本地 MinerU 2026-09-07 产物） | /Users/aurolafly/MinerU/ | aee678de37bad87d |
| taylorwiles1995.pdf | Taylor–Wiles, *Ring theoretic properties of certain Hecke algebras*, Annals 141 (1995)，22 页 | Taylor 本人主页 virtualmath1.stanford.edu/~rltaylor/hecke.pdf | 3a58acd02155b884 |
| ribet1990.pdf | Ribet, *On modular representations of Gal(Q̄/Q) arising from modular forms*（水平下降=ε猜想证明），Invent. Math. 100 (1990) 431-476，47 页 | Ribet 本人主页 math.berkeley.edu/~ribet/Articles/invent_100.pdf | 08f8ebfda40855d0 |
| serre1987.pdf | Serre, *Sur les représentations modulaires de degré 2 de Gal(Q̄/Q)*（ε猜想提出），Duke 54 (1987)，52 页 | 法兰西公学院官方媒体库 college-de-france.fr | 8048919db24dcb97 |
| **frey1986.pdf** | **Frey, *Links between stable elliptic curves and certain Diophantine equations*, Annales Universitatis Saraviensis 1 (1986) 1-40，40 页全文** | GitHub: FrancescaRossi/frey（经 MathOverflow #312565 被接受答案指引；注意正确出处是萨尔大学学报，非 Annals——常见误引） | 0f092a804000ad55 |

## 获取过程备注

- Frey 原文在合法学术索引（scholar.archive.org 3 命中均非原文）无 OA 副本；MathOverflow #312565
  （2018 年同样问题的提问）的被接受答案指向上述 GitHub 仓库——由 Francesca Rossi 上传的完整
  扫描（3.5MB，含作者手写页边注释痕迹）。
- 引用勘误：多数文献把 Frey 误引为 "Annals of Mathematics"；正确出处为 *Annales Universitatis
  Saraviensis*（数学史细节，对 Stage A 的引用保真有直接价值）。

## 待补（非阻塞）

- CSS 综合卷（Cornell–Silverman–Stevens 1997）：archive.org 出借/机构渠道，用户处置。
- 怀尔斯第一人称叙述（访谈/纪录片转写）：Quanta 类报道已够首期，深挖待用户。

## 版权

本地研究引用；公开上传前逐份过审查（上传 Gate）。
