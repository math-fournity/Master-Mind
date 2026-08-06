#!/usr/bin/env python3
"""
重新设计schema，把212号文档中的所有数据集 + HF API的10000个 + 用户消息100+个
全部入库ArangoDB math_datasets集合。

v2 schema设计（共9类字段）：

1. 标识字段
   - _key: ArangoDB主键
   - repo_id: HF/GitHub仓库ID
   - platform: huggingface | github | web | internet_archive | z_library | springer
   - title: 数据集名称
   - doc_id: 212号文档中的编号（E1/F1等）
   - alt_names: 别名列表

2. 价值描述字段（核心）
   - description: 数据集是什么——完整描述
   - unique_value: 独特价值——为什么这个数据集重要
   - notes: 其他备注

3. 内容属性字段
   - problem_count: 题量
   - data_size: 数据大小
   - format: 数据格式列表 [parquet, jsonl, pdf, lean, tex, ...]
   - source_type: 来源类型 [competition, k12, research, synthetic, multimodal, formal, textbook]
   - math_domain: 数学门类列表 [analysis, algebra, geometry, number_theory, ...]
   - difficulty_level: 难度级别 [elementary, undergraduate, graduate, research, competition]
   - has_solutions: 是否有解答
   - solution_format: 解答格式 [answer_only, cot, proof, lean_code, detailed]
   - year_range: 覆盖年份范围

4. 来源归属字段
   - institution: 发布机构
   - publisher: 出版方
   - language: 语言列表
   - country: 国家

5. HF/GitHub元数据字段
   - downloads: HF下载量
   - likes: HF点赞数
   - tags: HF标签列表
   - task_categories: 任务类型
   - size_categories: 大小分类
   - license: 许可证
   - last_modified: 最后修改时间
   - created_at: 创建时间
   - tier: 按下载量分级 1|2|3|4|0

6. 获取字段
   - url: 直达链接
   - download_url: 下载链接
   - access_method: 获取方式 [direct, login, crawler, purchase, api]
   - access_difficulty: 获取难度 [low, medium, high]

7. 下载状态字段
   - download_status: [not_started, in_progress, completed, blocked, skipped]
   - download_date: 下载完成日期
   - local_path: 本地存放路径
   - local_size: 本地文件大小
   - file_count: 文件数量
   - download_notes: 下载备注

8. 项目相关性字段
   - priority: 下载优先级 [1, 2, 3, 4]
   - test_layer: 测试层级 [1, 2, 3, 4, 5]（对应§6.1分层测试策略）
   - anti_contamination: 是否适合抗污染测试
   - ai_baseline_score: AI基准得分（如有）

9. 入库管理字段
   - ingest_source: 入库来源 [hf_api, user_list, doc_212, hf_api+user_list, ...]
   - ingest_date: 入库日期
   - last_updated: 最后更新时间
"""
import json
import os
import re
from datetime import datetime
from arango import ArangoClient
from huggingface_hub import HfApi

# ===== 配置 =====
ARANGO_HOST = "http://localhost:8529"
ARANGO_DB = os.environ.get("ARANGO_DB", "xishujuzhen_math_glm52")
ARANGO_USER = os.environ.get("ARANGO_USER", "root")
ARANGO_PASS = os.environ.get("ARANGO_PASS", "REDACTED-DB-PASSWORD")
COLLECTION = "math_datasets"
INGEST_DATE = "2026-08-06"

BASE_PATH = "~/master-mind-glm5.2-worktree/knowledge/problem_banks"


def sanitize_key(s: str) -> str:
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', s)


def classify_tier(downloads: int) -> int:
    if downloads >= 10000: return 1
    elif downloads >= 1000: return 2
    elif downloads >= 100: return 3
    else: return 4


# ===== 212号文档中的纸质来源（E1-E22）=====
DOC_212_PAPER_DATASETS = [
    {
        "doc_id": "E1", "title": "吉米多维奇《数学分析习题集》（中文版+解答）",
        "repo_id": "internet_archive/jimiduoweiqi", "platform": "internet_archive",
        "description": "俄罗斯数学分析经典习题集，覆盖数学分析全部分支（极限/连续/微分/积分/级数/多元函数/曲线积分/曲面积分）。中文版由高等教育出版社2010年翻译出版，配套费定晖6卷本完整解答。",
        "unique_value": "5000道分析习题+完整解答，是测试AI数学分析能力的经典基准。中文版抗污染价值高——AI训练数据中中文老版教材较少。",
        "problem_count": 5000, "format": ["pdf"], "source_type": ["textbook"],
        "math_domain": ["analysis"], "difficulty_level": ["undergraduate"],
        "has_solutions": True, "solution_format": ["detailed"],
        "institution": "莫斯科大学", "publisher": "高等教育出版社", "language": ["zh"], "country": "Russia/China",
        "url": "https://archive.org/details/jimiduoweiqi", "access_method": "direct", "access_difficulty": "low",
        "download_status": "completed", "download_date": "2026-08-06",
        "local_path": f"{BASE_PATH}/demidovich/jimiduoweiqi/", "local_size": "393MB", "file_count": 12,
        "download_notes": "12个PDF：习题集+经典解析+精选精解+题解6卷+全解6卷+学习指引3册",
        "priority": 1, "test_layer": 1, "anti_contamination": True,
    },
    {
        "doc_id": "E2", "title": "Demidovich《Problems in Mathematical Analysis》（英文版）",
        "repo_id": "internet_archive/demidovich_en", "platform": "internet_archive",
        "description": "吉米多维奇数学分析习题集的英文版，MIR出版社1970年出版。约3000道分析习题。",
        "unique_value": "英文版，与中文版互补，可对比AI在中英文数学题上的表现差异。",
        "problem_count": 3000, "format": ["pdf"], "source_type": ["textbook"],
        "math_domain": ["analysis"], "difficulty_level": ["undergraduate"],
        "has_solutions": True, "solution_format": ["answer_only"],
        "institution": "莫斯科大学", "publisher": "MIR Publishers", "language": ["en"], "country": "Russia",
        "url": "https://archive.org/details/demidovich", "access_method": "direct", "access_difficulty": "low",
        "download_status": "completed", "download_date": "2026-08-06",
        "local_path": f"{BASE_PATH}/demidovich/demidovich_en_1970.pdf", "local_size": "16MB", "file_count": 1,
        "priority": 1, "test_layer": 1, "anti_contamination": True,
    },
    {
        "doc_id": "E3", "title": "Berkeley Problems in Mathematics",
        "repo_id": "springer/berkeley_problems", "platform": "springer",
        "description": "加州大学伯克利分校数学系资格考试题集，约200道题，覆盖分析/代数/几何/拓扑/数论等。研究级难度。",
        "unique_value": "资格考试题——定位AI在研究生入学水平的能力边界。",
        "problem_count": 200, "format": ["pdf"], "source_type": ["research"],
        "math_domain": ["analysis", "algebra", "geometry", "topology", "number_theory"],
        "difficulty_level": ["graduate"], "has_solutions": True, "solution_format": ["detailed"],
        "institution": "UC Berkeley", "publisher": "Springer", "language": ["en"], "country": "USA",
        "access_method": "direct", "access_difficulty": "low",
        "download_status": "completed", "download_date": "2026-08-06",
        "local_path": f"{BASE_PATH}/springer_pbm/Berkeley_Problems.pdf", "local_size": "111KB", "file_count": 1,
        "priority": 2, "test_layer": 4, "anti_contamination": True,
    },
    {
        "doc_id": "E9", "title": "Komjáth & Totik《Problems and Theorems in Classical Set Theory》",
        "repo_id": "springer/komjath_set_theory", "platform": "springer",
        "description": "经典集合论问题集，约700道题，匈牙利数学传统（Pólya-Szegő-Lovász谱系）。覆盖集合论/组合集合论/无穷组合。",
        "unique_value": "集合论领域最全面的问题集，填补AI在集合论方向的能力测试空白。",
        "problem_count": 700, "format": ["pdf"], "source_type": ["textbook"],
        "math_domain": ["set_theory", "combinatorics"], "difficulty_level": ["undergraduate", "graduate"],
        "has_solutions": True, "solution_format": ["detailed"],
        "institution": "Eötvös Loránd University", "publisher": "Springer", "language": ["en"], "country": "Hungary",
        "access_method": "direct", "access_difficulty": "low",
        "download_status": "completed", "download_date": "2026-08-06",
        "local_path": f"{BASE_PATH}/springer_pbm/Komjath_Totik_Classical_Set_Theory.pdf", "local_size": "2.5MB", "file_count": 1,
        "priority": 2, "test_layer": 2, "anti_contamination": True,
    },
    {
        "doc_id": "E13", "title": "Engel《Problem-Solving Strategies》",
        "repo_id": "springer/engel_strategies", "platform": "internet_archive",
        "description": "IMO教练Arthur Engel写的竞赛策略教程，约300道题，按解题策略组织（不变量原理/极端原理/鸽巢原理/染色法等）。",
        "unique_value": "按策略组织而非按门类组织——测试AI是否掌握解题方法论而非只是知识。",
        "problem_count": 300, "format": ["pdf"], "source_type": ["competition"],
        "math_domain": ["combinatorics", "number_theory", "algebra", "geometry"],
        "difficulty_level": ["competition"], "has_solutions": True, "solution_format": ["detailed"],
        "institution": "IMO", "publisher": "Springer", "language": ["en"], "country": "Germany",
        "access_method": "direct", "access_difficulty": "low",
        "download_status": "completed", "download_date": "2026-08-06",
        "local_path": f"{BASE_PATH}/springer_pbm/Engel_Problem_Solving_Strategies.pdf", "local_size": "2.5MB", "file_count": 1,
        "priority": 2, "test_layer": 5, "anti_contamination": True,
    },
    {
        "doc_id": "E17", "title": "546个早期俄罗斯大学生数学竞赛题",
        "repo_id": "jingguan_zhijia/russian_546", "platform": "web",
        "description": "546道早期俄罗斯大学生数学竞赛题，覆盖代数/分析/几何/数论等。俄式竞赛风格，非标准题。",
        "unique_value": "俄罗斯大学生竞赛题——难度介于高中竞赛和研究级之间，AI训练数据中罕见。",
        "problem_count": 546, "format": ["pdf"], "source_type": ["competition"],
        "math_domain": ["analysis", "algebra", "geometry", "number_theory"],
        "difficulty_level": ["undergraduate", "competition"], "has_solutions": True,
        "institution": "俄罗斯大学", "language": ["zh"], "country": "Russia",
        "access_method": "login", "access_difficulty": "medium",
        "download_status": "completed", "download_date": "2026-08-06",
        "local_path": f"{BASE_PATH}/russian_546/russian_546_problems.pdf", "local_size": "192KB", "file_count": 1,
        "priority": 3, "test_layer": 2, "anti_contamination": True,
    },
    {
        "doc_id": "E18", "title": "莫斯科数学奥林匹克1993-2005",
        "repo_id": "math_ru/moscow_olympiad", "platform": "web",
        "description": "莫斯科数学奥林匹克1993-2005年真题，约300道题。俄文，非标准创新题。",
        "unique_value": "莫斯科MO以创新著称——题目不落俗套，测试AI的创造性思维。",
        "problem_count": 300, "format": ["pdf"], "source_type": ["competition"],
        "math_domain": ["combinatorics", "algebra", "geometry", "number_theory"],
        "difficulty_level": ["competition"], "has_solutions": True,
        "institution": "莫斯科数学会", "language": ["ru"], "country": "Russia",
        "url": "https://math.ru", "access_method": "direct", "access_difficulty": "low",
        "download_status": "completed", "download_date": "2026-08-06",
        "local_path": f"{BASE_PATH}/moscow_olympiad/MMO_1993_2005.pdf", "local_size": "98KB", "file_count": 1,
        "priority": 2, "test_layer": 5, "anti_contamination": True,
    },
    {
        "doc_id": "E19", "title": "丘成桐大学生数学竞赛2010-2025真题",
        "repo_id": "yau_contest/yau", "platform": "web",
        "description": "丘成桐大学生数学竞赛真题，约300+道题，6个方向：代数数论/几何拓扑/分析PDE/应用计算/概率统计/数学物理。中国最高水平大学生数学竞赛。",
        "unique_value": "中国最高水平大学生数学竞赛——研究级难度，覆盖全部数学方向。",
        "problem_count": 300, "format": ["pdf"], "source_type": ["competition"],
        "math_domain": ["algebra", "geometry", "topology", "analysis", "pde", "probability", "mathematical_physics"],
        "difficulty_level": ["graduate", "research"], "has_solutions": False,
        "institution": "丘成桐数学科学中心", "language": ["zh", "en"], "country": "China",
        "url": "https://yau-contest.com", "access_method": "login", "access_difficulty": "medium",
        "download_status": "in_progress", "download_notes": "部分已下载，需登录获取完整真题",
        "local_path": f"{BASE_PATH}/yau_contest/", "local_size": "24KB", "file_count": 3,
        "priority": 2, "test_layer": 4, "anti_contamination": True,
    },
    {
        "doc_id": "E22", "title": "TaichiLi/The-Collection-of-Mathematics-Problems",
        "repo_id": "TaichiLi/The-Collection-of-Mathematics-Problems", "platform": "github",
        "description": "GitHub开源数学题集，约1000+道题，覆盖数学分析/线性代数/概率/离散/复分析/信号与系统。含TeX源码。",
        "unique_value": "开源TeX源码——题目已是结构化文本，不需OCR。",
        "problem_count": 1000, "format": ["pdf", "tex"], "source_type": ["textbook"],
        "math_domain": ["analysis", "algebra", "probability", "discrete_math", "complex_analysis"],
        "difficulty_level": ["undergraduate"], "has_solutions": True,
        "language": ["zh"], "country": "China",
        "url": "https://github.com/TaichiLi/The-Collection-of-Mathematics-Problems",
        "access_method": "direct", "access_difficulty": "low",
        "download_status": "completed", "download_date": "2026-08-06",
        "local_path": f"{BASE_PATH}/taichili/", "local_size": "658KB", "file_count": 1,
        "priority": 2, "test_layer": 1, "anti_contamination": False,
    },
    {
        "doc_id": "E7", "title": "笹部贞市郎系列6本",
        "repo_id": "z_library/sasabe_series", "platform": "z_library",
        "description": "日本数学教育家笹部贞市郎的《問題解法辞典》系列6本：代数/几何/分析/解析几何/三角法/微积分。约15000-18000道题，覆盖初等数学全领域。中文版由上海教育出版社1982-1989出版。",
        "unique_value": "初等数学全领域覆盖最完整的题库——定位AI在哪个初等数学领域/难度开始做不出来。日文/中文老书，AI训练数据中罕见，抗污染价值极高。",
        "problem_count": 18000, "format": ["pdf"], "source_type": ["textbook"],
        "math_domain": ["algebra", "geometry", "analysis", "analytic_geometry", "trigonometry", "calculus"],
        "difficulty_level": ["elementary", "undergraduate"], "has_solutions": True, "solution_format": ["detailed"],
        "institution": "笹部贞市郎", "publisher": "上海教育出版社", "language": ["ja", "zh"], "country": "Japan/China",
        "access_method": "login", "access_difficulty": "high",
        "download_status": "blocked", "download_notes": "Z-Library需登录，待解决",
        "local_path": f"{BASE_PATH}/sasabe/", "local_size": "12KB", "file_count": 1,
        "priority": 1, "test_layer": 1, "anti_contamination": True,
    },
]


# ===== 212号文档中的纯电子化来源（F1-F17 + 2A.1-2A.10）=====
DOC_212_ELECTRONIC_DATASETS = [
    {
        "doc_id": "F1", "title": "MathNet", "repo_id": "ShadenA/MathNet", "platform": "huggingface",
        "description": "MIT等机构ICLR 2026论文发布的大规模多语言数学奥林匹克数据集。30,676道题，47个国家、17种语言、143个竞赛、1985-2025年。每题都有专家撰写的解答，来自官方国家队题册（非AoPS众包）。",
        "unique_value": "目前世界上最大的国际数学奥林匹克问题及解答的数字化开源数据库。非AoPS众包，而是官方国家队题册，质量有保证。AI基准：Gemini-3.1-Pro 78.4%，GPT-5 69.3%——连最强模型都做不全。",
        "problem_count": 30676, "format": ["parquet", "json"], "source_type": ["competition"],
        "math_domain": ["algebra", "geometry", "combinatorics", "number_theory"],
        "difficulty_level": ["competition"], "has_solutions": True, "solution_format": ["detailed", "proof"],
        "institution": "MIT", "language": ["en", "zh", "pt", "es", "fr", "it", "sr", "sl", "de", "ro", "ko", "nl", "ru", "mn", "mk", "pl", "hu"],
        "year_range": "1985-2025",
        "url": "https://huggingface.co/datasets/ShadenA/MathNet",
        "ai_baseline_score": "Gemini-3.1-Pro 78.4%, GPT-5 69.3%",
        "download_status": "in_progress", "download_notes": "GitHub仓库已clone(7.6MB)，HF数据698文件下载中",
        "local_path": f"{BASE_PATH}/mathnet/", "local_size": "100MB+", "file_count": 207,
        "priority": 1, "test_layer": 2, "anti_contamination": False,
    },
    {
        "doc_id": "F2", "title": "NuminaMath-1.5", "repo_id": "AI-MO/NuminaMath-1.5", "platform": "huggingface",
        "description": "AI-MO团队发布的NuminaMath第二版，896,215道题（约90万题）。Chain-of-Thought格式解答。来源：中国高中数学/中国竞赛/美国AMC-AIME/国际奥赛/AoPS论坛/不等式/数论。Apache 2.0许可。",
        "unique_value": "约11万道证明题（proof类型），是最适合测试AI数学推理能力的题型。中国竞赛题（cn_contest 29,944题）尤其有价值——中文来源，AI训练数据中较少。",
        "problem_count": 896215, "format": ["parquet"], "source_type": ["competition", "k12"],
        "math_domain": ["algebra", "geometry", "combinatorics", "number_theory", "inequalities"],
        "difficulty_level": ["competition", "elementary", "undergraduate"],
        "has_solutions": True, "solution_format": ["cot"],
        "institution": "AI-MO", "license": "apache-2.0",
        "url": "https://huggingface.co/datasets/AI-MO/NuminaMath-1.5",
        "download_status": "in_progress", "download_notes": "证明题子集下载中，已得15411题",
        "local_path": f"{BASE_PATH}/numina_math/", "local_size": "55MB", "file_count": 1,
        "priority": 1, "test_layer": 2, "anti_contamination": False,
    },
    {
        "doc_id": "F3", "title": "AoPS-Instruct / LiveAoPSBench", "repo_id": "DSL-Lab/aops", "platform": "github",
        "description": "从AoPS（Art of Problem Solving）论坛自动提取的600,000+问答对。LiveAoPSBench按时间戳分割，可检测AI是否因预训练暴露而'假会'。论文发现LLM在旧题上表现好但新题上显著下降。",
        "unique_value": "抗污染基准——按时间戳分割可检测AI是否真正具备推理能力还是只是记住了答案。含eval数据（aime24/amc23/aops_1224/math/olympiadbench/omni_math）共15501题。",
        "problem_count": 600000, "format": ["jsonl"], "source_type": ["competition"],
        "math_domain": ["algebra", "geometry", "combinatorics", "number_theory"],
        "difficulty_level": ["competition"], "has_solutions": True, "solution_format": ["detailed"],
        "url": "https://github.com/DSL-Lab/aops",
        "download_status": "completed", "download_date": "2026-08-06",
        "local_path": f"{BASE_PATH}/aops_instruct/", "local_size": "39MB", "file_count": 20,
        "download_notes": "含eval数据15501题",
        "priority": 1, "test_layer": 3, "anti_contamination": True,
    },
    {
        "doc_id": "F4", "title": "ConjectureBench", "repo_id": "bespokelabsai/conjecture-bench", "platform": "github",
        "description": "Bespoke Labs发布的15,000个开放数学问题（Open Mathematics Problems），全部带来源链接和LaTeX源码。这些是未解决的开放性问题。",
        "unique_value": "不是用来测试AI'能不能做出来'，而是测试AI'能不能提出有意义的猜想'——这是数学大师的核心能力之一。已下载5539个JSON问题。",
        "problem_count": 15000, "format": ["json", "latex"], "source_type": ["research"],
        "math_domain": ["number_theory", "algebra", "analysis", "combinatorics"],
        "difficulty_level": ["research"], "has_solutions": False,
        "institution": "Bespoke Labs",
        "url": "https://github.com/bespokelabsai/conjecture-bench",
        "download_status": "completed", "download_date": "2026-08-06",
        "local_path": f"{BASE_PATH}/conjecture_bench/", "local_size": "37MB", "file_count": 5539,
        "priority": 1, "test_layer": 4, "anti_contamination": False,
    },
    {
        "doc_id": "F5", "title": "awesome-math", "repo_id": "rossant/awesome-math", "platform": "github",
        "description": "GitHub上近万Star的纯数字化数学资源精选库。不是单一题库，而是所有免费数学资源的索引——免费开源PDF讲义、线上笔记、题集、互动百科。",
        "unique_value": "资源发现工具——可以从中发现更多细分领域的题库。",
        "format": ["md"], "source_type": ["research"],
        "url": "https://github.com/rossant/awesome-math",
        "download_status": "completed", "download_date": "2026-08-06",
        "local_path": f"{BASE_PATH}/awesome_math/", "local_size": "200KB", "file_count": 3,
        "priority": 3, "test_layer": 0, "anti_contamination": False,
    },
    {
        "doc_id": "F6", "title": "compfiles (Lean 4形式化IMO)", "repo_id": "dwrensha/compfiles", "platform": "github",
        "description": "将国际数学奥林匹克（IMO）题目转化为Lean 4编程语言的项目。520个Lean文件，每个包含一个IMO题目的形式化证明。计算机可验证的证明——连计算机都无法挑出毛病。",
        "unique_value": "形式化证明是AI数学推理的终极验证标准。如果AI的证明能通过Lean 4类型检查，那就是100%正确的——不需要人类评审。",
        "problem_count": 520, "format": ["lean"], "source_type": ["formal", "competition"],
        "math_domain": ["algebra", "geometry", "combinatorics", "number_theory"],
        "difficulty_level": ["competition"], "has_solutions": True, "solution_format": ["lean_code"],
        "url": "https://github.com/dwrensha/compfiles",
        "download_status": "completed", "download_date": "2026-08-06",
        "local_path": f"{BASE_PATH}/compfiles/", "local_size": "12MB", "file_count": 520,
        "priority": 1, "test_layer": 5, "anti_contamination": False,
    },
    {
        "doc_id": "F7", "title": "Evan Chen Olympiad Archive", "repo_id": "web_evanchen/olympiad", "platform": "web",
        "description": "著名竞赛教练Evan Chen整理的IMO/USAMO/USA TST/EGMO等竞赛题目和解答。PDF + LaTeX源码。IMO 1997-2026 + EGMO 2012-2026 + USAMO/USA TST等。",
        "unique_value": "LaTeX源码意味着题目已经是结构化文本，不需要OCR。Evan Chen的解答质量极高。",
        "problem_count": 300, "format": ["pdf", "tex"], "source_type": ["competition"],
        "math_domain": ["algebra", "geometry", "combinatorics", "number_theory"],
        "difficulty_level": ["competition"], "has_solutions": True, "solution_format": ["detailed"],
        "institution": "Evan Chen", "year_range": "1997-2026",
        "url": "https://web.evanchen.cc/problems.html",
        "download_status": "in_progress", "download_notes": "TeX 112个已下载(3.1MB)，PDF 206个下载中",
        "local_path": f"{BASE_PATH}/evan_chen/", "local_size": "28MB", "file_count": 135,
        "priority": 1, "test_layer": 5, "anti_contamination": False,
    },
    {
        "doc_id": "F8", "title": "Project Euler", "repo_id": "project_euler/archives", "platform": "web",
        "description": "全网最顶级的'算法+纯数'在线题库。800+题，每道题看似编程题，但实际需要数论/组合数学的极简公式。如果你无法在纸上用数论或组合数学得出极简公式，电脑算一百年也算不出答案。",
        "unique_value": "测试AI是否能发现'用数学公式把O(n)暴力搜索变成O(1)公式'——这是数学洞察力的纯粹测试。",
        "problem_count": 800, "format": ["web"], "source_type": ["research"],
        "math_domain": ["number_theory", "combinatorics", "algebra"],
        "difficulty_level": ["undergraduate", "research"],
        "has_solutions": True, "solution_format": ["detailed"],
        "url": "https://projecteuler.net/archives",
        "access_method": "crawler", "access_difficulty": "medium",
        "download_status": "not_started", "download_notes": "需写爬虫",
        "priority": 3, "test_layer": 4, "anti_contamination": False,
    },
    {
        "doc_id": "F10", "title": "UltraData-Math", "repo_id": "openbmb/UltraData-Math", "platform": "huggingface",
        "description": "清华大学OpenBMB团队×面壁智能2026年5月发布的数学预训练数据集。经过L1-L3极度严格清洗，剔除了废话和错解。含LaTeX完美排版。专门针对复杂数学题和逻辑推理题。",
        "unique_value": "L3级数据清洗是目前最高标准的质量控制。深思考数据版块包含完整的逻辑拆解和推导步骤。",
        "format": ["parquet"], "source_type": ["research", "synthetic"],
        "math_domain": ["algebra", "analysis", "geometry", "number_theory", "combinatorics"],
        "difficulty_level": ["undergraduate", "graduate"],
        "has_solutions": True, "solution_format": ["cot"],
        "institution": "Tsinghua", "language": ["zh", "en"],
        "url": "https://huggingface.co/datasets/openbmb/UltraData-Math",
        "download_status": "not_started",
        "priority": 1, "test_layer": 2, "anti_contamination": False,
    },
    {
        "doc_id": "F11", "title": "UltraData-SFT-2605", "repo_id": "openbmb/UltraData-SFT-2605", "platform": "huggingface",
        "description": "清华OpenBMB×面壁智能2026年5月发布的高质量微调数据集。含百万级深思考（Deep Thinking）样本。MiniCPM5模型用的微调数据。专门划分出了深思考数据版块，针对复杂的数学题和逻辑推理题。",
        "unique_value": "深思考数据——人类学习'如何严密推导解题'的究极神仙教辅。经过L3级清洗。",
        "format": ["parquet"], "source_type": ["research", "synthetic"],
        "has_solutions": True, "solution_format": ["cot"],
        "institution": "Tsinghua", "language": ["zh", "en"],
        "url": "https://huggingface.co/datasets/openbmb/UltraData-SFT-2605",
        "download_status": "not_started",
        "priority": 1, "test_layer": 2, "anti_contamination": False,
    },
    {
        "doc_id": "F12", "title": "We-Math 2.0 Standard", "repo_id": "We-Math/We-Math2.0-Standard", "platform": "huggingface",
        "description": "清华×北邮×腾讯2025年8月发布的视觉多模态数学题库。6,500+道带图表的数学题（几何图形/函数图/坐标系），491个细分知识点，1819条底层原理标注。对每道题的原理有显式标注。",
        "unique_value": "不是纯文本题库，而是面向'视觉数学推理'的标准数据集。知识体系全面，原理标注显式。",
        "problem_count": 6500, "format": ["parquet", "image"], "source_type": ["multimodal", "k12"],
        "math_domain": ["geometry", "algebra", "analytic_geometry"],
        "difficulty_level": ["elementary", "undergraduate"],
        "has_solutions": True, "solution_format": ["detailed"],
        "institution": "Tsinghua", "language": ["en", "zh"],
        "url": "https://huggingface.co/datasets/We-Math/We-Math2.0-Standard",
        "download_status": "not_started",
        "priority": 2, "test_layer": 2, "anti_contamination": False,
    },
    {
        "doc_id": "F13", "title": "MathGLM 5M", "repo_id": "jonathanasdf/MathGLM-dataset-5M", "platform": "huggingface",
        "description": "清华THUDM×北航×智谱AI 2024年发布的500万道数学题集。涵盖多步骤算术运算、文本描述数学题、视觉几何图表题，从小学到大学全覆盖。",
        "unique_value": "500万道题——目前公开可见的最大单一数学题库之一。涵盖从小学到大学的多模态数学题。",
        "problem_count": 5000000, "format": ["parquet"], "source_type": ["k12", "multimodal"],
        "math_domain": ["arithmetic", "algebra", "geometry", "analysis"],
        "difficulty_level": ["elementary", "undergraduate"],
        "has_solutions": True, "solution_format": ["cot"],
        "institution": "Tsinghua", "language": ["zh", "en"],
        "url": "https://huggingface.co/datasets/jonathanasdf/MathGLM-dataset-5M",
        "download_status": "not_started",
        "priority": 2, "test_layer": 2, "anti_contamination": False,
    },
    {
        "doc_id": "F14", "title": "FATE (Formal Algebra Theorem Evaluation)", "repo_id": "frenzymath/FATE", "platform": "github",
        "description": "北大×西湖大学×九坤AI4M团队发布的形式化代数评测集。FATE-M 150题（本科教材级）+ FATE-H 100题（研究生期末考级）+ FATE-X 100题（博士资格考试级及以上）= 350题。全部用Lean 4形式化，每题有PDF+JSON+Lean三种格式。",
        "unique_value": "极硬核。FATE-X是第一个超越Mathlib库覆盖范围的形式化基准。最强模型在FATE-H上pass@64仅3%，FATE-X上0%。这是测试AI在研究级数学上的终极基准。",
        "problem_count": 350, "format": ["lean", "pdf", "json"], "source_type": ["formal", "research"],
        "math_domain": ["abstract_algebra", "commutative_algebra"],
        "difficulty_level": ["undergraduate", "graduate", "research"],
        "has_solutions": True, "solution_format": ["lean_code"],
        "institution": "PKU", "ai_baseline_score": "FATE-H pass@64: 3%, FATE-X pass@64: 0%",
        "url": "https://github.com/frenzymath/FATE",
        "download_status": "in_progress",
        "local_path": f"{BASE_PATH}/fate/", "local_size": "36KB",
        "priority": 1, "test_layer": 4, "anti_contamination": True,
    },
    {
        "doc_id": "F15", "title": "MathX-5M", "repo_id": "Modotte/MathX-5M", "platform": "huggingface",
        "description": "目前公开可见的最大、最全的数学推理语料库。5,050,000道精心筛选的分步思维（Step-by-step）题目，从基础算术到微积分。每道题都有极度详尽的推理链条，答案经过RL验证。15.9GB。Apache 2.0。",
        "unique_value": "500万道分步思维题，RL验证答案——数据质量有保证。覆盖从基础算术到微积分的全范围。",
        "problem_count": 5050000, "data_size": "15.9GB", "format": ["parquet"], "source_type": ["research"],
        "math_domain": ["arithmetic", "algebra", "analysis", "calculus"],
        "difficulty_level": ["elementary", "undergraduate"],
        "has_solutions": True, "solution_format": ["cot"],
        "license": "apache-2.0",
        "url": "https://huggingface.co/datasets/Modotte/MathX-5M",
        "download_status": "not_started", "download_notes": "15.9GB，需确定是否全量下载",
        "priority": 2, "test_layer": 2, "anti_contamination": False,
    },
    {
        "doc_id": "F16", "title": "Math23K", "repo_id": "scnu203/math23k", "platform": "github",
        "description": "腾讯AI Lab发布的23,162道中文数学应用题。从网上爬取的纯中文真实应用数学题及答案，以一元一次方程为主。覆盖初高中、小学。",
        "unique_value": "最接地气的中国数学应用题库。适合测试AI的中文数学理解能力。",
        "problem_count": 23162, "format": ["json"], "source_type": ["k12"],
        "math_domain": ["algebra"], "difficulty_level": ["elementary"],
        "has_solutions": True, "solution_format": ["answer_only"],
        "institution": "Tencent", "language": ["zh"], "country": "China",
        "url": "https://github.com/scnu203/math23k",
        "download_status": "in_progress",
        "priority": 2, "test_layer": 1, "anti_contamination": False,
    },
    {
        "doc_id": "F17", "title": "InfiMM-WebMath-40B", "repo_id": "Infi-MM/InfiMM-WebMath-40B", "platform": "huggingface",
        "description": "79.1GB的海量图文混合数学题库，从网页文档中提取的文本+图像交错数据。中英双语。专为多模态大语言模型（MLLM）设计。",
        "unique_value": "侧重于真实世界里的图文混合数学题（类似拍照问解法的原始数据源）。适合测试多模态AI的数学推理能力。",
        "data_size": "79.1GB", "format": ["parquet", "image"], "source_type": ["multimodal"],
        "language": ["en", "zh"],
        "url": "https://huggingface.co/datasets/Infi-MM/InfiMM-WebMath-40B",
        "download_status": "not_started", "download_notes": "79.1GB太大，低优先",
        "priority": 4, "test_layer": 0, "anti_contamination": False,
    },
]


# ===== 用户消息中的100+个数据集（带描述）=====
# 已在USER_LISTED_DATASETS中定义，这里补充description字段
USER_LISTED_DATASETS = [
    # 第一部分：大厂与顶尖高校 (1-20)
    {"repo_id": "nvidia/OpenMathReasoning", "platform": "huggingface", "title": "OpenMathReasoning",
     "description": "NVIDIA 2025/2026霸榜的320万道带极长思维链的奥数题。专门为训练顶级AI数学推理能力而建。",
     "unique_value": "NVIDIA出品，题量巨大，思维链极长，是目前最高质量的奥数训练数据之一。",
     "problem_count": 3200000, "source_type": ["competition"], "institution": "NVIDIA",
     "has_solutions": True, "solution_format": ["cot"], "difficulty_level": ["competition"]},
    {"repo_id": "nvidia/Nemotron-PrismMath", "platform": "huggingface", "title": "Nemotron-PrismMath",
     "description": "NVIDIA发布的100万道由大模型合成的新型结构化数学问题。",
     "unique_value": "合成数据——测试AI对新题型（非传统题库）的适应能力。",
     "problem_count": 1000000, "source_type": ["synthetic"], "institution": "NVIDIA",
     "has_solutions": True, "solution_format": ["cot"]},
    {"repo_id": "microsoft/orca-math-word-problems-200k", "platform": "huggingface", "title": "Orca-Math",
     "description": "微软发布的20万道质量极高、难度递进的数学应用题。",
     "unique_value": "微软出品，难度递进设计，适合定位AI在不同难度级别的通过率。",
     "problem_count": 200000, "source_type": ["k12"], "institution": "Microsoft",
     "has_solutions": True, "solution_format": ["cot"], "difficulty_level": ["elementary"]},
    {"repo_id": "deepmind/math_dataset", "platform": "huggingface", "title": "DeepMind Math Dataset",
     "description": "谷歌DeepMind用来测试模型的最经典200万道涵盖微积分、代数、多项式的综合题。",
     "unique_value": "DeepMind经典基准——最早的大规模数学推理评测集之一。",
     "problem_count": 2000000, "source_type": ["research"], "institution": "DeepMind",
     "has_solutions": True, "solution_format": ["answer_only"],
     "difficulty_level": ["undergraduate", "graduate"]},
    {"repo_id": "AI-MO/NuminaMath-CoT", "platform": "huggingface", "title": "NuminaMath-CoT",
     "description": "AI数学奥林匹克(AIMO)官方使用的百万级世界各国奥数推导集。NuminaMath-1.5的前身。",
     "unique_value": "AIMO官方数据——AI数学奥林匹克竞赛的训练/评测基准。",
     "source_type": ["competition"], "institution": "AI2",
     "has_solutions": True, "solution_format": ["cot"], "difficulty_level": ["competition"]},
    {"repo_id": "meta-math/MetaMathQA", "platform": "huggingface", "title": "MetaMathQA",
     "description": "剑桥大学等机构开源的39.5万道经典变体题库，极大拓宽了解题思路。基于GSM8K和MATH通过元数学变换生成。",
     "unique_value": "变体题——同一题的不同表述/参数/条件，测试AI是否真正理解还是只是记住。",
     "problem_count": 395000, "source_type": ["synthetic"], "institution": "Cambridge",
     "has_solutions": True, "solution_format": ["cot"]},
    {"repo_id": "amd/SAND-MATH", "platform": "huggingface", "title": "SAND-MATH",
     "description": "AMD开源的高难度合成数学题库，包含大量人类难以心算的复杂逻辑。",
     "unique_value": "AMD出品——硬件厂商的数学推理数据集，视角独特。",
     "source_type": ["synthetic"], "institution": "AMD",
     "has_solutions": True, "solution_format": ["cot"]},
    {"repo_id": "camel-ai/math", "platform": "huggingface", "title": "Camel Math",
     "description": "5万道通过多智能体对抗生成的'高等数学'多轮问答题。",
     "unique_value": "多智能体对抗生成——题目经过AI之间的博弈，质量可能高于单一生成。",
     "problem_count": 50000, "source_type": ["synthetic", "research"],
     "has_solutions": True, "solution_format": ["cot"], "difficulty_level": ["undergraduate"]},
    {"repo_id": "TIGER-Lab/MathInstruct", "platform": "huggingface", "title": "MathInstruct",
     "description": "26万道高质量中英双语指令微调数学题。",
     "unique_value": "中英双语——可对比AI在中英文数学题上的表现差异。",
     "problem_count": 260000, "source_type": ["research"], "language": ["en", "zh"],
     "has_solutions": True, "solution_format": ["cot"]},
    {"repo_id": "OpenDataArena/ODA-Math-460k", "platform": "huggingface", "title": "ODA-Math",
     "description": "46万道通过交叉验证、去重的高难度竞赛题。",
     "unique_value": "交叉验证+去重——数据质量有保证。",
     "problem_count": 460000, "source_type": ["competition"],
     "has_solutions": True, "solution_format": ["cot"], "difficulty_level": ["competition"]},
    {"repo_id": "Roman190928/MathReasoning-2750000", "platform": "huggingface", "title": "MathReasoning 2.75M",
     "description": "275万道格式对齐的数学推理题。",
     "unique_value": "格式对齐——便于批量处理和评测。",
     "problem_count": 2750000, "source_type": ["research"],
     "has_solutions": True, "solution_format": ["cot"]},
    {"repo_id": "nvidia/OpenMathInstruct-2", "platform": "huggingface", "title": "OpenMathInstruct-2",
     "description": "NVIDIA的又一力作，覆盖大量课本级习题。",
     "unique_value": "NVIDIA出品，课本级覆盖全面。",
     "source_type": ["k12", "textbook"], "institution": "NVIDIA",
     "has_solutions": True, "solution_format": ["cot"]},
    {"repo_id": "GAIR/LIMO", "platform": "huggingface", "title": "LIMO (Less Is More)",
     "description": "极其精简但难度极高的少数派精华数学推理集。'Less Is More'哲学——少量精选高难度题。",
     "unique_value": "少而精——证明少量高质量数据即可显著提升模型推理能力。",
     "source_type": ["research"], "has_solutions": True, "solution_format": ["cot"],
     "difficulty_level": ["competition", "research"]},
    {"repo_id": "allenai/RLVR-MATH", "platform": "huggingface", "title": "RLVR-MATH",
     "description": "艾伦AI研究所发布，带有奖励机制反馈的解题过程数据。",
     "unique_value": "RLVR（Reinforcement Learning with Verifiable Rewards）——带可验证奖励的强化学习数学数据。",
     "source_type": ["research"], "institution": "AllenAI",
     "has_solutions": True, "solution_format": ["cot"]},

    # 第二部分：竞赛级 (21-40)
    {"repo_id": "lighteval/MATH", "platform": "huggingface", "title": "Hendrycks MATH",
     "description": "伯克利大学Dan Hendrycks发布的12,500道高难度竞赛题（AMC/AIME级别）。按难度分级（Level 1-5）。",
     "unique_value": "最经典的数学推理基准之一——几乎所有AI数学评测都会用到的数据集。",
     "problem_count": 12500, "source_type": ["competition"], "institution": "Berkeley",
     "has_solutions": True, "solution_format": ["detailed"], "difficulty_level": ["competition"]},
    {"repo_id": "KbsdJames/Omni-MATH", "platform": "huggingface", "title": "Omni-MATH",
     "description": "专为极限数学推理打造的全难度竞赛集。",
     "unique_value": "全难度覆盖——从基础到极限难度。",
     "source_type": ["competition"], "has_solutions": True, "difficulty_level": ["competition"]},
    {"repo_id": "openai/prm800k", "platform": "github", "title": "PRM800K",
     "description": "OpenAI发布的人类过程验证标注（每个步骤评分）的经典竞赛题库。80万步推理步骤标注，每步标注Good/Bad。",
     "unique_value": "过程级标注——不是只标最终答案对错，而是每一步推导都评分。训练AI自己挑错的关键数据。",
     "problem_count": 800000, "source_type": ["competition"], "institution": "OpenAI",
     "has_solutions": True, "solution_format": ["process_reward"], "difficulty_level": ["competition"]},
    {"repo_id": "HuggingFaceH4/MATH-500", "platform": "huggingface", "title": "MATH-500",
     "description": "从MATH数据集中精选出来的最能代表高级推理的500道母题。HuggingFace官方维护。",
     "unique_value": "500道精选——快速评测AI数学推理能力的标准基准。下载量最高（18万次）。",
     "problem_count": 500, "source_type": ["competition"],
     "has_solutions": True, "solution_format": ["detailed"], "difficulty_level": ["competition"]},
    {"repo_id": "m-a-p/Gauss-Math", "platform": "huggingface", "title": "Gauss Math",
     "description": "MAP团队构建的覆盖广阔数学分支的优质题目。",
     "unique_value": "覆盖广阔——数学分支覆盖全面。",
     "source_type": ["research"], "has_solutions": True},
    {"repo_id": "doublelei/MuMath-Code", "platform": "huggingface", "title": "MuMath-Code",
     "description": "多语言竞赛数学题，最大的特点是'附带Python代码解法'。",
     "unique_value": "代码解法——测试AI是否能用代码验证数学推理。",
     "source_type": ["competition"], "has_solutions": True, "solution_format": ["cot", "code"]},
    {"repo_id": "allenai/math_qa", "platform": "huggingface", "title": "MathQA",
     "description": "大型高级数学文字题，不仅给答案，还给出了人类思考的逻辑公式。",
     "unique_value": "逻辑公式标注——展示人类思考过程。",
     "source_type": ["k12"], "institution": "AllenAI",
     "has_solutions": True, "solution_format": ["detailed"]},
    {"repo_id": "OlympiadBench", "platform": "huggingface", "title": "Olympiad-Bench",
     "description": "专门汇集各国最高水平物理、数学奥林匹克的全英文数据集。",
     "unique_value": "物理+数学奥林匹克——跨学科竞赛题。",
     "source_type": ["competition"], "has_solutions": True, "difficulty_level": ["competition"]},
    {"repo_id": "GSM-Plus", "platform": "huggingface", "title": "GSM-Plus",
     "description": "对经典GSM8K题目施加了多重变式（改数字、改条件）的题库，极度锻炼举一反三能力。",
     "unique_value": "变式题——测试AI是否真正理解题目结构还是只是记住答案。",
     "source_type": ["k12"], "has_solutions": True, "difficulty_level": ["elementary"]},
    {"repo_id": "Wenhu/TheoremQA", "platform": "huggingface", "title": "TheoremQA",
     "description": "涵盖800个理工科定理的高质量问答测试集。",
     "unique_value": "定理级——测试AI对数学定理的理解和应用能力。",
     "problem_count": 800, "source_type": ["research"], "has_solutions": True,
     "difficulty_level": ["undergraduate", "graduate"]},
    {"repo_id": "m-a-p/GaoKao-Math", "platform": "huggingface", "title": "高考数学精洗集",
     "description": "历年中国高考真题的大模型思维链解析版。",
     "unique_value": "中国高考——AI训练数据中较少的高质量中文数学题。",
     "source_type": ["competition"], "language": ["zh"], "country": "China",
     "has_solutions": True, "solution_format": ["cot"], "difficulty_level": ["undergraduate"]},
    {"repo_id": "shibing624/math23k", "platform": "huggingface", "title": "Math23K (HF镜像)",
     "description": "腾讯AI Lab的23,162道中文自然语言数学应用题经典库的HuggingFace镜像。",
     "unique_value": "中文应用题——测试AI的中文数学理解能力。",
     "problem_count": 23162, "source_type": ["k12"], "institution": "Tencent", "language": ["zh"],
     "has_solutions": True, "solution_format": ["answer_only"]},

    # 第三部分：多模态 (41-60)
    {"repo_id": "MathLLMs/MathVision", "platform": "huggingface", "title": "MATH-Vision (MathV)",
     "description": "高清多模态奥数题，3000+极难视听觉数学验证库。",
     "unique_value": "高清图片+极难题——多模态数学推理的高难度基准。",
     "problem_count": 3000, "source_type": ["multimodal", "competition"],
     "has_solutions": True, "difficulty_level": ["competition"]},
    {"repo_id": "MathLLMs/MathVision-Wild", "platform": "huggingface", "title": "MATH-Vision-Wild",
     "description": "真实拍摄的试卷图片数学题库——教AI看懂真实试卷。",
     "unique_value": "真实世界图片——测试AI在非理想化图片上的数学推理能力。",
     "source_type": ["multimodal"], "has_solutions": True},
    {"repo_id": "MathV360K", "platform": "huggingface", "title": "MathV360K",
     "description": "大规模的中文多模态数学题库，包含大量初高中带图试题。",
     "unique_value": "中文多模态——36万道带图中文数学题。",
     "problem_count": 360000, "source_type": ["multimodal", "k12"], "language": ["zh"],
     "has_solutions": True, "difficulty_level": ["elementary", "undergraduate"]},
    {"repo_id": "AI4Math/MathVista", "platform": "huggingface", "title": "MathVista",
     "description": "视觉数学推理基准——在视觉上下文中进行数学推理。",
     "unique_value": "视觉推理——测试AI在图表/图形语境下的数学能力。",
     "source_type": ["multimodal"], "has_solutions": True},
    {"repo_id": "huggingface/ChartQA", "platform": "huggingface", "title": "ChartQA",
     "description": "针对统计图表、直方图的数学计算与逻辑推理题。",
     "unique_value": "图表理解——测试AI从图表中提取数学信息的能力。",
     "source_type": ["multimodal"], "has_solutions": True},
    {"repo_id": "CLEVR-Math", "platform": "huggingface", "title": "CLEVR-Math",
     "description": "通过3D渲染图进行加减乘除和几何体特征提取的综合题库。",
     "unique_value": "3D渲染——在合成3D场景中测试数学推理。",
     "source_type": ["multimodal"], "has_solutions": True, "difficulty_level": ["elementary"]},
    {"repo_id": "MathVerse", "platform": "huggingface", "title": "MathVerse",
     "description": "要求模型在'没有文字'只有图形的情况下强行推理的超级难题库。",
     "unique_value": "纯视觉推理——去掉文字提示，测试AI是否真的能从图形中推理。",
     "source_type": ["multimodal"], "has_solutions": True, "difficulty_level": ["competition"]},
    {"repo_id": "derek-thomas/ScienceQA", "platform": "huggingface", "title": "ScienceQA (Math Subset)",
     "description": "包含大量带有示意图的科学与数学计算题。",
     "unique_value": "跨学科——科学与数学交叉的图文题。",
     "source_type": ["multimodal", "k12"], "has_solutions": True},

    # 第四部分：形式化 (61-80)
    {"repo_id": "leanprover-community/mathlib4", "platform": "github", "title": "Lean-Mathlib",
     "description": "世界最大的人类共同维护的高等数学机器证明代码库。Lean 4形式化的高等数学定理库。",
     "unique_value": "数学知识的形式化基石——所有Lean 4数学证明都依赖这个库。",
     "source_type": ["formal"], "format": ["lean"], "has_solutions": True, "solution_format": ["lean_code"],
     "difficulty_level": ["graduate", "research"]},
    {"repo_id": "openai/miniF2F", "platform": "github", "title": "miniF2F",
     "description": "OpenAI创建的用于测试AI是否能证明奥数题的形式化数据集。包含高中竞赛题和本科数学题，用Lean/Isabelle形式化。",
     "unique_value": "形式化数学的标准基准——所有AI定理证明器都会用到的测试集。",
     "source_type": ["formal", "competition"], "institution": "OpenAI", "format": ["lean", "isabelle"],
     "has_solutions": True, "solution_format": ["lean_code"], "difficulty_level": ["competition", "undergraduate"]},
    {"repo_id": "hoskinson-center/ProofNet", "platform": "huggingface", "title": "ProofNet",
     "description": "将本科高等数学定理转换为Lean代码的超级题库。",
     "unique_value": "本科数学形式化——填补本科级形式化基准的空白。",
     "source_type": ["formal"], "format": ["lean"], "has_solutions": True, "solution_format": ["lean_code"],
     "difficulty_level": ["undergraduate"]},
    {"repo_id": "lupantech/ineqmath", "platform": "github", "title": "ineqmath",
     "description": "专门解决'不等式证明（Inequality Proofs）'的高端开源库。",
     "unique_value": "不等式专项——不等式证明是数学竞赛的核心技能。",
     "source_type": ["formal"], "format": ["lean"], "has_solutions": True, "solution_format": ["lean_code"],
     "math_domain": ["inequalities"]},
    {"repo_id": "princeton-vl/CoqGym", "platform": "github", "title": "Coq-Gym",
     "description": "基于Coq语言的大型深度学习数学证明库。",
     "unique_value": "Coq生态——不同于Lean的形式化证明系统。",
     "source_type": ["formal"], "institution": "Princeton", "format": ["coq"],
     "has_solutions": True, "solution_format": ["coq_code"]},
    {"repo_id": "frenzymath/REAL-Prover", "platform": "github", "title": "REAL-Prover",
     "description": "北大开源的形式化检索与验证题目集。检索增强的Lean 4逐步定理证明器。",
     "unique_value": "检索增强证明——结合检索和形式化证明的方法。",
     "source_type": ["formal"], "institution": "PKU", "format": ["lean"],
     "has_solutions": True, "solution_format": ["lean_code"]},
    {"repo_id": "wellecks/naturalproofs", "platform": "github", "title": "NaturalProofs",
     "description": "连接自然语言与数学公式证明图谱的大型网络。",
     "unique_value": "自然语言↔形式化——桥接两种证明表示。",
     "source_type": ["formal", "research"], "has_solutions": True},

    # 第五部分：基础与反馈 (81-100)
    {"repo_id": "openai/gsm8k", "platform": "huggingface", "title": "GSM8K",
     "description": "OpenAI开源的最著名的小学至初中数学文字题库（8500道，人类极易看懂）。几乎所有AI数学评测的起点。",
     "unique_value": "数学推理评测的'Hello World'——最广泛使用的数学基准。",
     "problem_count": 8500, "source_type": ["k12"], "institution": "OpenAI",
     "has_solutions": True, "solution_format": ["cot"], "difficulty_level": ["elementary"]},
    {"repo_id": "SVAMP", "platform": "huggingface", "title": "SVAMP",
     "description": "包含很多极其容易掉入陷阱的'刁钻'基础数学题。",
     "unique_value": "陷阱题——测试AI是否会被表面相似但实际不同的题迷惑。",
     "source_type": ["k12"], "has_solutions": True, "difficulty_level": ["elementary"]},
    {"repo_id": "aqua_rat", "platform": "huggingface", "title": "AQuA-RAT",
     "description": "带有'Rationale（原理解释）'的多项选择代数词汇题库。",
     "unique_value": "原理解释——不仅给答案还给原理。",
     "source_type": ["k12"], "has_solutions": True, "solution_format": ["detailed"]},
    {"repo_id": "cognitivecomputations/dolphin-math", "platform": "huggingface", "title": "Dolphin-Math",
     "description": "由开源社区精心筛选调整的综合杂交数学训练集。",
     "unique_value": "社区精选——经过实践检验的训练数据。",
     "source_type": ["research"], "has_solutions": True, "solution_format": ["cot"]},
    {"repo_id": "cais/mmlu", "platform": "huggingface", "title": "MMLU (STEM/Math)",
     "description": "虽然是综合考试，但其College Math和High School Math子集全是标准好题。",
     "unique_value": "标准化考试——大学和高中数学的标准评测。",
     "source_type": ["research"], "has_solutions": True, "difficulty_level": ["undergraduate"]},
    {"repo_id": "amfo0o0/awesome-AI-Math-Datasets", "platform": "github", "title": "Awesome-AI-Math-Datasets",
     "description": "终极索引库，汇总了世界上所有最新的AI专用数学大题库索引。",
     "unique_value": "元索引——发现更多数据集的入口。",
     "source_type": ["research"]},

    # 超级聚合集（预训练级无监督语料）
    {"repo_id": "keirp/OpenWebMath", "platform": "huggingface", "title": "OpenWebMath",
     "description": "从Common Crawl中极其严苛地过滤出来的纯数学网页，14.7B Tokens。包含大量HTML转LaTeX的纯文本公式。Llama等模型数学能力的基石。",
     "unique_value": "预训练级语料——AI数学直觉的来源。",
     "data_size": "14.7B tokens", "source_type": ["research"], "format": ["json"],
     "has_solutions": False},
    {"repo_id": "GAIR/MathPile", "platform": "huggingface", "title": "MathPile",
     "description": "上海交大等开源的高质量数学预训练语料，9.5B高质量Token。汇集了纯文字版的数学教材、arXiv论文源码、Wikipedia数学词条等。",
     "unique_value": "上海交大出品——中文机构的预训练语料。",
     "data_size": "9.5B tokens", "source_type": ["research"], "institution": "SJTU", "format": ["json"],
     "has_solutions": False},
    {"repo_id": "EleutherAI/proof-pile-2", "platform": "huggingface", "title": "Proof-Pile-2",
     "description": "专为数学代码模型（如Llemma）打造，55B Tokens。包含了海量的数学论文（arXiv）、数学代码（GitHub）和纯数学网页。",
     "unique_value": "55B Tokens——最大的数学预训练语料之一。",
     "data_size": "55B tokens", "source_type": ["formal", "research"], "institution": "EleutherAI",
     "has_solutions": False},
    {"repo_id": "EleutherAI/algebraic-stack", "platform": "huggingface", "title": "AlgebraicStack",
     "description": "全网最全的形式化数学语言源码（Lean, Coq, Isabelle, LaTeX），11B Tokens。想让模型学会严密推导必用。",
     "unique_value": "形式化语言语料——训练AI形式化证明能力的预训练数据。",
     "data_size": "11B tokens", "source_type": ["formal"], "institution": "EleutherAI", "format": ["lean", "coq", "isabelle", "latex"],
     "has_solutions": False},

    # 合成指令微调集
    {"repo_id": "WizardLM/WizardMath", "platform": "huggingface", "title": "WizardMath",
     "description": "通过进化算法，把基础数学题变得越来越复杂（增加干扰条件、深化逻辑链）。Evol-Instruct方法。",
     "unique_value": "进化生成——测试AI在渐进复杂化题目上的表现。",
     "source_type": ["synthetic"], "has_solutions": True, "solution_format": ["cot"]},
    {"repo_id": "Opendi/MathScale-QA", "platform": "huggingface", "title": "MathScale-QA",
     "description": "极其震撼的200万道合成数学题！从少量种子题目出发，利用大模型构建了庞大的'概念图谱'，生成了人类根本没见过的新题目。",
     "unique_value": "概念图谱生成——AI生成的全新题目，人类没见过。",
     "problem_count": 2000000, "source_type": ["synthetic"], "has_solutions": True, "solution_format": ["cot"]},
    {"repo_id": "Opendi/MuggleMath", "platform": "huggingface", "title": "MuggleMath",
     "description": "30万道极高质量的合成推导题，专门为了让小模型（7B级别）拥有超越大模型的数学能力而清洗出来的精炼数据。",
     "unique_value": "小模型优化——证明少量精炼数据能让小模型超越大模型。",
     "problem_count": 300000, "source_type": ["synthetic"], "has_solutions": True, "solution_format": ["cot"]},
    {"repo_id": "glaiveai/glaive-math-qa", "platform": "huggingface", "title": "Glaive-Math-QA",
     "description": "10万道专门训练模型进行'多轮数学对话'的数据集。不仅仅是解题，还包含解释定理。",
     "unique_value": "多轮对话——测试AI在对话中逐步推理的能力。",
     "problem_count": 100000, "source_type": ["synthetic"], "has_solutions": True, "solution_format": ["cot"]},

    # 工具调用推理（TIR）
    {"repo_id": "AI-MO/NuminaMath-TIR", "platform": "huggingface", "title": "NuminaMath-TIR",
     "description": "AI奥赛冠军方案的数据集。所有文本解答不仅有文字推导，还穿插了Python代码块和执行结果。数万道极难数学题。",
     "unique_value": "TIR（Tool-Integrated Reasoning）——AI写代码+运行+继续推理的方法论。",
     "source_type": ["competition"], "has_solutions": True, "solution_format": ["cot", "code"],
     "difficulty_level": ["competition"]},
    {"repo_id": "microsoft/ToRA", "platform": "huggingface", "title": "ToRA-Math",
     "description": "微软开源的Tool-Integrated Reasoning Agent数据集，专门训练大模型像人类使用计算器一样解决高等数学。",
     "unique_value": "微软TIR——工具集成推理的官方数据集。",
     "source_type": ["research"], "institution": "Microsoft", "has_solutions": True, "solution_format": ["cot", "code"]},

    # RLHF/DPO反馈数据集
    {"repo_id": "peiyi9979/Math-Shepherd", "platform": "huggingface", "title": "Math-Shepherd",
     "description": "给数学推导过程打分的数据集！极其珍贵。对推导的'每一步'都进行了1到-1的标注，文本AI学了它就能自己挑错。",
     "unique_value": "过程级评分——训练AI自我纠错的关键数据。",
     "source_type": ["research"], "has_solutions": True, "solution_format": ["process_reward"]},
]


def fetch_hf_datasets_metadata():
    """从HF API获取math相关数据集的元数据"""
    api = HfApi()
    print("Fetching math datasets from HuggingFace API (limit=10000)...")
    datasets = list(api.list_datasets(search="math", sort="downloads", limit=10000))
    print(f"Found {len(datasets)} datasets")

    records = []
    for ds in datasets:
        tier = classify_tier(ds.downloads or 0)
        tags = list(ds.tags) if ds.tags else []
        task_cats = [t.replace("task_categories:", "") for t in tags if t.startswith("task_categories:")]
        size_cat = next((t.replace("size_categories:", "") for t in tags if t.startswith("size_categories:")), None)
        license_name = next((t.replace("license:", "") for t in tags if t.startswith("license:")), None)
        language = [t.replace("language:", "") for t in tags if t.startswith("language:")]

        # 从title推断description
        title = ds.id.split("/")[-1]
        desc = f"HuggingFace数据集 {ds.id}，下载量{ds.downloads or 0}次。"

        record = {
            "_key": sanitize_key(f"hf_{ds.id}"),
            "repo_id": ds.id,
            "platform": "huggingface",
            "title": title,
            "description": desc,
            "downloads": ds.downloads or 0,
            "likes": ds.likes or 0,
            "tags": tags,
            "task_categories": task_cats,
            "size_categories": size_cat,
            "license": license_name,
            "last_modified": str(ds.last_modified) if ds.last_modified else None,
            "created_at": str(ds.created_at) if ds.created_at else None,
            "tier": tier,
            "language": language,
            "url": f"https://huggingface.co/datasets/{ds.id}",
            "ingest_source": "hf_api",
            "ingest_date": INGEST_DATE,
            "last_updated": INGEST_DATE,
            "download_status": "not_started",
        }
        records.append(record)
    return records


def build_curated_records():
    """构建212号文档 + 用户列表中的数据集记录"""
    records = []
    for ds in DOC_212_PAPER_DATASETS + DOC_212_ELECTRONIC_DATASETS + USER_LISTED_DATASETS:
        repo_id = ds["repo_id"]
        platform = ds.get("platform", "huggingface")
        record = {
            "_key": sanitize_key(f"{platform}_{repo_id}"),
            "repo_id": repo_id,
            "platform": platform,
            "title": ds.get("title", repo_id),
            "description": ds.get("description", ""),
            "unique_value": ds.get("unique_value", ""),
            "notes": ds.get("notes", ""),
            "problem_count": ds.get("problem_count"),
            "data_size": ds.get("data_size"),
            "format": ds.get("format", []),
            "source_type": ds.get("source_type", ["unknown"]),
            "math_domain": ds.get("math_domain", []),
            "difficulty_level": ds.get("difficulty_level", []),
            "has_solutions": ds.get("has_solutions"),
            "solution_format": ds.get("solution_format", []),
            "year_range": ds.get("year_range"),
            "institution": ds.get("institution"),
            "publisher": ds.get("publisher"),
            "language": ds.get("language", ["en"]),
            "country": ds.get("country"),
            "license": ds.get("license"),
            "ai_baseline_score": ds.get("ai_baseline_score"),
            "url": ds.get("url", ""),
            "access_method": ds.get("access_method", "direct"),
            "access_difficulty": ds.get("access_difficulty", "low"),
            "download_status": ds.get("download_status", "not_started"),
            "download_date": ds.get("download_date"),
            "local_path": ds.get("local_path"),
            "local_size": ds.get("local_size"),
            "file_count": ds.get("file_count"),
            "download_notes": ds.get("download_notes", ""),
            "priority": ds.get("priority", 3),
            "test_layer": ds.get("test_layer", 0),
            "anti_contamination": ds.get("anti_contamination", False),
            "ingest_source": "doc_212+user_list",
            "ingest_date": INGEST_DATE,
            "last_updated": INGEST_DATE,
        }
        if ds.get("doc_id"):
            record["doc_id"] = ds["doc_id"]
        if not record["url"]:
            if platform == "huggingface":
                record["url"] = f"https://huggingface.co/datasets/{repo_id}"
            elif platform == "github":
                record["url"] = f"https://github.com/{repo_id}"
        records.append(record)
    return records


def merge_records(hf_records, curated_records):
    """合并HF API记录和精选记录，去重"""
    merged = {}
    for r in hf_records:
        merged[r["repo_id"]] = r
    for r in curated_records:
        rid = r["repo_id"]
        if rid in merged:
            # 精选记录的元数据覆盖HF记录
            for k, v in r.items():
                if k in ("_key", "ingest_source", "ingest_date"):
                    continue
                if v is not None and v != [] and v != "":
                    merged[rid][k] = v
            merged[rid]["ingest_source"] = "hf_api+curated"
        else:
            merged[rid] = r
    return list(merged.values())


def ingest_to_arango(records):
    """批量写入ArangoDB"""
    client = ArangoClient(hosts=ARANGO_HOST)
    db = client.db(ARANGO_DB, username=ARANGO_USER, password=ARANGO_PASS)
    col = db.collection(COLLECTION)
    col.truncate()
    print(f"Truncated collection {COLLECTION}")

    batch_size = 500
    total = 0
    for i in range(0, len(records), batch_size):
        batch = records[i:i+batch_size]
        col.import_bulk(batch, on_duplicate="update")
        total += len(batch)
        print(f"  Inserted batch {i//batch_size + 1}: {len(batch)} records (total: {total})")

    print(f"\nTotal records ingested: {total}")
    return total


def print_stats(records):
    print("\n===== 统计信息 =====")
    print(f"总数据集数: {len(records)}")

    platforms = {}
    for r in records:
        p = r.get("platform", "unknown")
        platforms[p] = platforms.get(p, 0) + 1
    print(f"按平台: {platforms}")

    tiers = {}
    for r in records:
        t = r.get("tier", 0)
        tiers[t] = tiers.get(t, 0) + 1
    print(f"按Tier: {tiers}")

    # 有描述的
    with_desc = [r for r in records if r.get("description") and len(r["description"]) > 50]
    print(f"有详细描述的数据集: {len(with_desc)}")

    # 有下载状态的
    statuses = {}
    for r in records:
        s = r.get("download_status", "not_started")
        statuses[s] = statuses.get(s, 0) + 1
    print(f"按下载状态: {statuses}")

    # 有题量的
    with_count = [r for r in records if r.get("problem_count")]
    total_problems = sum(r["problem_count"] for r in with_count if r["problem_count"])
    print(f"有题量信息的数据集: {len(with_count)}")
    print(f"已知题量总和: {total_problems:,}")

    # 有local_path的
    with_path = [r for r in records if r.get("local_path")]
    print(f"有本地路径的数据集: {len(with_path)}")


def main():
    print("===== Step 1: 从HuggingFace API获取math数据集元数据 =====")
    hf_records = fetch_hf_datasets_metadata()

    print(f"\n===== Step 2: 构建212号文档+用户列表精选记录 =====")
    curated = build_curated_records()
    print(f"精选记录: {len(curated)}")

    print(f"\n===== Step 3: 合并去重 =====")
    merged = merge_records(hf_records, curated)
    print(f"合并后总数: {len(merged)}")

    print(f"\n===== Step 4: 入库ArangoDB =====")
    ingest_to_arango(merged)

    print_stats(merged)

    output_path = f"{BASE_PATH}/math_datasets_catalog_v2.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
    print(f"\n完整目录已保存到: {output_path}")


if __name__ == "__main__":
    main()
