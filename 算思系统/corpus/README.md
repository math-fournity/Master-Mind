# Corpus — 调查语料资产（Git 追踪）

> 职责： cognition-operators 调查线的**原始语料与提取产物**，全部入 Git 管理与追踪（用户
> 2026-09-28 裁定："下载到 tmp 是不行的，应作为项目的资产包的一部分进行 git 管理和追踪"）。
> 提取工具链：pymupdf4llm（文本级，本批已用）；MinerU 4.0.8（公式级，已安装于
> /Volumes/D/toolchain-cache/mineru-venv，模型权重下载与验证待完成）。

## Fields 试点（June Huh 案例）语料清单

| 文件 | 类型 | 来源 | 下载日 | SHA256（前16） |
|---|---|---|---|---|
| `laudatio-jh.pdf` | 社区解读（官方） | IMU 官网 Kalai laudatio | 2026-09-28 | 52df8e3ced6dab75 |
| `laudatio-jh.md` | 上述的文本级提取 | pymupdf4llm | 2026-09-28 | - |
| `huh-icm2022.pdf` | 第一人称（ICM 2022 报告） | Huh Princeton 主页 | 2026-09-28 | 8d03772c03758705 |
| `huh-icm2022.md` | 上述的文本级提取（公式未保真） | pymupdf4llm | 2026-09-28 | - |

## 批 2（分层抽样三案例）语料清单

| 文件 | 类型 | 来源 | SHA256（前16） |
|---|---|---|---|
| `fields-batch2/laudatio-mv.pdf` + `.md` | 社区解读（官方）：Henry Cohn 论 Viazovska | IMU 官网 | e38ff650188c331a |
| `fields-batch2/viazovska-sphere-packing-1603.04246.pdf` + `.md` | 一手原始论文（E8 球堆积，Annals 2017） | arXiv 经 BrowserOS 下载（1603.04246v2） | f9f3a16da44702bb |
| `fields-batch2/laudatio-jm.pdf` + `.md` | 社区解读（官方）：Kannan Soundararajan 论 Maynard | IMU 官网 | eff073712ebb33d2 |
| `fields-batch2/maynard-1311.4600.pdf` + `.md` | 一手原始论文（Small gaps between primes） | arXiv（curl） | dce1a7a03004186f |
| `fields-batch2/scholze-perfectoid-1111.4914.pdf` + `.md` | 一手原始论文（Perfectoid spaces，IHES） | arXiv 经 BrowserOS 下载（51 页核验） | 065441a872c58615 |
| `fields-batch2/bhatt-perfectoid-notices.pdf` + `.md` | 社区解读：Bhatt "What is...a Perfectoid Space?"（Notices AMS 2014-09） | ams.org | 205df6fcee997d79 |

全部 PDF 的 SHA256 完整值见 `MANIFEST.sha256`。

## 下载通道记录（诚实边界）

- IMU 官网 2022 laudatio、arXiv、ams.org：直接可达（curl / BrowserOS 均可）。
- **Scholze 2018 laudatio（Michael Rapoport, "The work of Peter Scholze"）不可达**：唯一来源
  `eta.impa.br`（ICM 2018 门户 description/screen_share 两个按钮均指向该主机）在本机网络不可
  达（curl 与 BrowserOS 一致失败），Web Archive 无快照，IMU 无自托管副本（两个 proceedings
  URL 模式均 404）。该槽位由 Bhatt Notices 文替代，缺口已登记，留待网络条件变化后补取。
- 经验：arXiv PDF 的 export.arxiv.org 直链在本网络部分超时；BrowserOS 浏览器下载（abs 页 →
  View PDF → 查看器 Download 按钮）稳定可用，已作为首选通道。

## 网络语料（URL 锚点，未落盘全文的以提取记录形式存于试点报告）

arXiv:2211.05724（社区综述，HTML 提取记录在试点报告 §1）、arXiv:1711.11176（Huh 本人综述）、
arXiv:1511.02888（AHK 原始论文）、Quanta 报道（2022-07-05）。

## 版权与上传注意

PDF 为第三方公开发布物，版权归 IMU / 作者 / 相关出版方。本地 Git 管理用于研究引用符合其
公开发布意图；**公开上传（Master-Mind 同步）前须过版权审查**——已列入上传 Gate 待办
（第三方 PDF 的再分发授权逐份确认，或上传时以 URL+哈希清单替代原件）。

## 工具链状态

- pymupdf4llm 1.28.2：文本级提取已投产（本目录全部 .md）。
- MinerU 4.0.8：已安装于 `/Volumes/D/toolchain-cache/mineru-venv`（uv + Python 3.11 + 清华镜像）；
  basic 层权重 12 文件已下载完成（2026-09-28）；**公式级提取尚未验证运行**（模型加载/首次推理
  未执行），ICM 报告公式级复跑为下一步。
