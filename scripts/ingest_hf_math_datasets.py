#!/usr/bin/env python3
"""
从HuggingFace API批量获取math相关数据集的元数据，入库ArangoDB。
同时把用户消息中提到的100+个数据集也整理入库。

数据集schema:
{
  "_key": "hf_<repo_id_sanitized>",   # ArangoDB key
  "repo_id": "owner/name",            # HF/GitHub repo ID
  "platform": "huggingface"|"github"|"web",
  "title": "...",
  "description": "...",
  "downloads": 12345,                 # HF下载量
  "likes": 100,                       # HF点赞数
  "tags": ["math", "reasoning", ...],
  "task_categories": ["text-generation", ...],
  "size_categories": "1M<n<10M",
  "license": "apache-2.0",
  "last_modified": "2026-01-01",
  "created_at": "2025-06-01",
  "tier": 1|2|3|4,                    # 按下载量分级
  "problem_count": 5000000,           # 题量（如有）
  "data_size": "15.9GB",              # 数据大小（如有）
  "format": "parquet"|"jsonl"|"pdf"|"lean",
  "source_type": "competition"|"k12"|"research"|"synthetic"|"multimodal"|"formal",
  "institution": "MIT"|"Tsinghua"|"NVIDIA"|...,
  "language": ["en"]|["zh"]|["en","zh"],
  "url": "https://huggingface.co/datasets/...",
  "notes": "...",                     # 备注（独特价值等）
  "ingest_source": "hf_api"|"user_list",  # 入库来源
  "ingest_date": "2026-08-06"
}
"""
import json
import os
import re
import time
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


def sanitize_key(repo_id: str) -> str:
    """把repo_id转成合法的ArangoDB _key"""
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', repo_id)


def classify_tier(downloads: int) -> int:
    if downloads >= 10000:
        return 1
    elif downloads >= 1000:
        return 2
    elif downloads >= 100:
        return 3
    else:
        return 4


def fetch_hf_datasets_metadata():
    """从HF API获取math相关数据集的元数据"""
    api = HfApi()
    print("Fetching math datasets from HuggingFace API (limit=10000)...")

    datasets = list(api.list_datasets(search="math", sort="downloads", limit=10000))
    print(f"Found {len(datasets)} datasets")

    records = []
    for ds in datasets:
        tier = classify_tier(ds.downloads or 0)

        # 尝试获取更详细的元数据
        tags = list(ds.tags) if ds.tags else []
        task_cats = [t.replace("task_categories:", "") for t in tags if t.startswith("task_categories:")]
        size_cat = next((t.replace("size_categories:", "") for t in tags if t.startswith("size_categories:")), None)
        license_name = next((t.replace("license:", "") for t in tags if t.startswith("license:")), None)
        language = [t.replace("language:", "") for t in tags if t.startswith("language:")]

        record = {
            "_key": sanitize_key(f"hf_{ds.id}"),
            "repo_id": ds.id,
            "platform": "huggingface",
            "title": ds.id.split("/")[-1],
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
        }
        records.append(record)

    return records


# ===== 用户消息中提到的数据集（100个 + 超级聚合集等）=====
USER_LISTED_DATASETS = [
    # 第一部分：大厂与顶尖高校的航母级数学推理库 (1-20)
    {"repo_id": "nvidia/OpenMathReasoning", "platform": "huggingface", "title": "OpenMathReasoning", "problem_count": 3200000, "source_type": "competition", "institution": "NVIDIA", "notes": "320万道带极长思维链的奥数题，2025/2026霸榜"},
    {"repo_id": "nvidia/Nemotron-PrismMath", "platform": "huggingface", "title": "Nemotron-PrismMath", "problem_count": 1000000, "source_type": "synthetic", "institution": "NVIDIA", "notes": "100万道大模型合成的新型结构化数学问题"},
    {"repo_id": "openbmb/UltraData-Math", "platform": "huggingface", "title": "UltraData-Math", "source_type": "research", "institution": "Tsinghua", "notes": "清华OpenBMB，含深度思考链，L3级清洗，LaTeX排版"},
    {"repo_id": "microsoft/orca-math-word-problems-200k", "platform": "huggingface", "title": "Orca-Math", "problem_count": 200000, "source_type": "k12", "institution": "Microsoft", "notes": "微软20万道质量极高、难度递进的数学应用题"},
    {"repo_id": "deepmind/math_dataset", "platform": "huggingface", "title": "DeepMind Math Dataset", "problem_count": 2000000, "source_type": "research", "institution": "DeepMind", "notes": "谷歌200万道涵盖微积分、代数、多项式的综合题"},
    {"repo_id": "AI-MO/NuminaMath-CoT", "platform": "huggingface", "title": "NuminaMath-CoT", "source_type": "competition", "institution": "AI2", "notes": "AIMO官方百万级各国奥数推导集"},
    {"repo_id": "jonathanasdf/MathGLM-dataset-5M", "platform": "huggingface", "title": "MathGLM 5M", "problem_count": 5000000, "source_type": "k12", "institution": "Tsinghua", "notes": "清华THUDM 500万题，小学到大学"},
    {"repo_id": "meta-math/MetaMathQA", "platform": "huggingface", "title": "MetaMathQA", "problem_count": 395000, "source_type": "synthetic", "institution": "Cambridge", "notes": "剑桥39.5万道经典变体题库"},
    {"repo_id": "amd/SAND-MATH", "platform": "huggingface", "title": "SAND-MATH", "source_type": "synthetic", "institution": "AMD", "notes": "AMD高难度合成数学题库"},
    {"repo_id": "StackMathQA", "platform": "huggingface", "title": "StackMathQA", "problem_count": 2000000, "source_type": "research", "notes": "Stack Exchange近200万道专业数学问答对"},
    {"repo_id": "camel-ai/math", "platform": "huggingface", "title": "Camel Math", "problem_count": 50000, "source_type": "research", "notes": "5万道多智能体对抗生成的高等数学多轮问答题"},
    {"repo_id": "TIGER-Lab/MathInstruct", "platform": "huggingface", "title": "MathInstruct", "problem_count": 260000, "source_type": "research", "notes": "26万道中英双语指令微调数学题"},
    {"repo_id": "OpenDataArena/ODA-Math-460k", "platform": "huggingface", "title": "ODA-Math", "problem_count": 460000, "source_type": "competition", "notes": "46万道交叉验证去重的高难度竞赛题"},
    {"repo_id": "DataMuncher-Labs/UltiMath", "platform": "huggingface", "title": "UltiMath", "source_type": "synthetic", "notes": "超大规模合成逻辑题库，3.7T Tokens"},
    {"repo_id": "Roman190928/MathReasoning-2750000", "platform": "huggingface", "title": "MathReasoning 2.75M", "problem_count": 2750000, "source_type": "research", "notes": "275万道格式对齐的数学推理题"},
    {"repo_id": "nvidia/OpenMathInstruct-2", "platform": "huggingface", "title": "OpenMathInstruct-2", "source_type": "k12", "institution": "NVIDIA", "notes": "NVIDIA覆盖大量课本级习题"},
    {"repo_id": "notbadai/math_reasoning", "platform": "huggingface", "title": "NotBadAI Math", "source_type": "research", "notes": "带强化学习反馈路径，标注常见错误"},
    {"repo_id": "Modotte/MathX-5M", "platform": "huggingface", "title": "MathX-5M", "problem_count": 5050000, "data_size": "15.9GB", "source_type": "research", "notes": "505万道分步思维题，RL验证答案，Apache 2.0"},
    {"repo_id": "GAIR/LIMO", "platform": "huggingface", "title": "LIMO", "source_type": "research", "notes": "极精简但难度极高的少数派精华推理集"},
    {"repo_id": "allenai/RLVR-MATH", "platform": "huggingface", "title": "RLVR-MATH", "source_type": "research", "institution": "AllenAI", "notes": "艾伦AI研究所，带奖励机制反馈的解题过程数据"},

    # 第二部分：竞赛级、奥林匹克与高教专区 (21-40)
    {"repo_id": "lighteval/MATH", "platform": "huggingface", "title": "Hendrycks MATH", "problem_count": 12500, "source_type": "competition", "institution": "Berkeley", "notes": "伯克利12500道高难度竞赛题（AMC/AIME级别）"},
    {"repo_id": "KbsdJames/Omni-MATH", "platform": "huggingface", "title": "Omni-MATH", "source_type": "competition", "notes": "专为极限数学推理打造的全难度竞赛集"},
    {"repo_id": "frenzymath/FATE", "platform": "github", "title": "FATE", "problem_count": 350, "source_type": "formal", "institution": "PKU", "format": "lean", "notes": "北大形式化代数，博士级，Lean 4，最强模型0%"},
    {"repo_id": "openai/prm800k", "platform": "github", "title": "PRM800K", "problem_count": 800000, "source_type": "competition", "institution": "OpenAI", "notes": "OpenAI人类过程验证标注（每步评分）的竞赛题库"},
    {"repo_id": "HuggingFaceH4/MATH-500", "platform": "huggingface", "title": "MATH 500", "problem_count": 500, "source_type": "competition", "notes": "MATH数据集精选500道母题"},
    {"repo_id": "marcus10000/AMC_AIME_problems", "platform": "huggingface", "title": "AMC/AIME Problem Sets", "source_type": "competition", "notes": "历年美国数学竞赛高清格式化整理"},
    {"repo_id": "m-a-p/Gauss-Math", "platform": "huggingface", "title": "Gauss Math", "source_type": "competition", "notes": "MAP团队覆盖广阔数学分支的优质题目"},
    {"repo_id": "doublelei/MuMath-Code", "platform": "huggingface", "title": "MuMath-Code", "source_type": "competition", "notes": "多语言竞赛数学题，附Python代码解法"},
    {"repo_id": "math_qa", "platform": "huggingface", "title": "MathQA", "source_type": "k12", "notes": "大型高级数学文字题，含人类思考逻辑公式"},
    {"repo_id": "OlympiadBench", "platform": "huggingface", "title": "Olympiad-Bench", "source_type": "competition", "notes": "各国最高水平物理、数学奥林匹克全英文数据集"},
    {"repo_id": "GSM-Plus", "platform": "huggingface", "title": "GSM-Plus", "source_type": "k12", "notes": "经典题多重变式（改数字、改条件），锻炼举一反三"},
    {"repo_id": "Wenhu/TheoremQA", "platform": "huggingface", "title": "TheoremQA", "problem_count": 800, "source_type": "research", "notes": "800个理工科定理的高质量问答测试集"},
    {"repo_id": "m-a-p/GaoKao-Math", "platform": "huggingface", "title": "高考数学精洗集", "source_type": "competition", "language": ["zh"], "notes": "历年中国高考真题的大模型思维链解析版"},
    {"repo_id": "asdiv", "platform": "huggingface", "title": "ASDiv", "source_type": "k12", "notes": "丰富多样的代数与应用数学文本题"},
    {"repo_id": "shibing624/math23k", "platform": "huggingface", "title": "Math23K", "problem_count": 23162, "source_type": "k12", "institution": "Tencent", "language": ["zh"], "notes": "腾讯23162道中文自然语言数学应用题"},

    # 第三部分：多模态视觉数学 (41-60)
    {"repo_id": "We-Math/We-Math2.0-Standard", "platform": "huggingface", "title": "We-Math 2.0 Standard", "problem_count": 6500, "source_type": "multimodal", "institution": "Tsinghua", "notes": "清华×北邮×腾讯，6500道视觉数学题，491知识点，1819条原理标注"},
    {"repo_id": "We-Math/We-Math2.0-Pro", "platform": "huggingface", "title": "We-Math 2.0 Pro", "source_type": "multimodal", "institution": "Tsinghua", "notes": "We-Math 2.0进阶版"},
    {"repo_id": "MathLLMs/MathVision", "platform": "huggingface", "title": "MATH-Vision", "problem_count": 3000, "source_type": "multimodal", "notes": "高清多模态奥数题，3000+极难视听觉数学验证库"},
    {"repo_id": "MathLLMs/MathVision-Wild", "platform": "huggingface", "title": "MATH-Vision-Wild", "source_type": "multimodal", "notes": "真实拍摄的试卷图片数学题库"},
    {"repo_id": "luokesb/Geometry3K", "platform": "github", "title": "Geometry3K", "source_type": "multimodal", "notes": "经典几何图文混合题库（含边长、角度标注）"},
    {"repo_id": "GeoQA", "platform": "github", "title": "GeoQA / UniGeo", "source_type": "multimodal", "notes": "平面几何定理的带图推理题"},
    {"repo_id": "Infi-MM/InfiMM-WebMath-40B", "platform": "huggingface", "title": "InfiMM-WebMath-40B", "data_size": "79.1GB", "source_type": "multimodal", "language": ["en","zh"], "notes": "40B超大型真实网页端图文数学题库"},
    {"repo_id": "MathV360K", "platform": "huggingface", "title": "MathV360K", "problem_count": 360000, "source_type": "multimodal", "language": ["zh"], "notes": "大规模中文多模态数学题库，含大量初高中带图试题"},
    {"repo_id": "huggingface/ChartQA", "platform": "huggingface", "title": "ChartQA", "source_type": "multimodal", "notes": "统计图表、直方图的数学计算与逻辑推理题"},
    {"repo_id": "IconQA", "platform": "huggingface", "title": "IconQA", "source_type": "multimodal", "notes": "看图说话式的趣味数学与空间逻辑推理"},
    {"repo_id": "CLEVR-Math", "platform": "huggingface", "title": "CLEVR-Math", "source_type": "multimodal", "notes": "3D渲染图进行加减乘除和几何体特征提取的综合题库"},
    {"repo_id": "MathVerse", "platform": "huggingface", "title": "MathVerse", "source_type": "multimodal", "notes": "要求在无文字只有图形的情况下强行推理的超级难题库"},
    {"repo_id": "derek-thomas/ScienceQA", "platform": "huggingface", "title": "ScienceQA (Math Subset)", "source_type": "multimodal", "notes": "含示意图的科学与数学计算题"},
    {"repo_id": "AI4Math/MathVista", "platform": "huggingface", "title": "MathVista", "source_type": "multimodal", "notes": "视觉数学推理基准"},

    # 第四部分：形式化数学与代码证明 (61-80)
    {"repo_id": "leanprover-community/mathlib4", "platform": "github", "title": "Lean-Mathlib", "source_type": "formal", "format": "lean", "notes": "世界最大的人类共同维护的高等数学机器证明代码库"},
    {"repo_id": "openai/miniF2F", "platform": "github", "title": "miniF2F", "source_type": "formal", "institution": "OpenAI", "format": "lean", "notes": "OpenAI测试AI是否能证明奥数题的形式化数据集"},
    {"repo_id": "hoskinson-center/ProofNet", "platform": "huggingface", "title": "ProofNet", "source_type": "formal", "format": "lean", "notes": "本科高等数学定理转换为Lean代码的超级题库"},
    {"repo_id": "dwrensha/compfiles", "platform": "github", "title": "compfiles", "problem_count": 520, "source_type": "formal", "format": "lean", "notes": "历届IMO真题用Lean 4写成的大合集"},
    {"repo_id": "lupantech/ineqmath", "platform": "github", "title": "ineqmath", "source_type": "formal", "format": "lean", "notes": "不等式证明的形式化开源库"},
    {"repo_id": "lean-dojo", "platform": "huggingface", "title": "Lean-Dojo-Data", "source_type": "formal", "format": "lean", "notes": "提取自百万行定理证明过程的拆解题库"},
    {"repo_id": "princeton-vl/CoqGym", "platform": "github", "title": "Coq-Gym", "source_type": "formal", "institution": "Princeton", "format": "coq", "notes": "基于Coq语言的大型深度学习数学证明库"},
    {"repo_id": "frenzymath/REAL-Prover", "platform": "github", "title": "REAL-Prover", "source_type": "formal", "institution": "PKU", "format": "lean", "notes": "北大形式化检索与验证题目集"},
    {"repo_id": "xinhaowang/lean-workbook", "platform": "huggingface", "title": "Lean-workbook", "source_type": "formal", "format": "lean", "notes": "高级微积分与代数练习作业本"},
    {"repo_id": "FormalGeo", "platform": "github", "title": "Formal-Geo", "source_type": "formal", "format": "lean", "notes": "平面几何完全形式化，计算机通过公理推导证明几何题"},
    {"repo_id": "wellecks/naturalproofs", "platform": "github", "title": "NaturalProofs", "source_type": "formal", "notes": "连接自然语言与数学公式证明图谱的大型网络"},

    # 第五部分：基础、对比反馈与专项题库 (81-100)
    {"repo_id": "openai/gsm8k", "platform": "huggingface", "title": "GSM8K", "problem_count": 8500, "source_type": "k12", "institution": "OpenAI", "notes": "最著名的小学至初中数学文字题库"},
    {"repo_id": "SVAMP", "platform": "huggingface", "title": "SVAMP", "source_type": "k12", "notes": "极易掉入陷阱的刁钻基础数学题"},
    {"repo_id": "aqua_rat", "platform": "huggingface", "title": "AQuA-RAT", "source_type": "k12", "notes": "带Rationale的多项选择代数词汇题库"},
    {"repo_id": "mawps", "platform": "huggingface", "title": "MAWPS", "source_type": "k12", "notes": "经典数学应用题库汇总"},
    {"repo_id": "cognitivecomputations/dolphin-math", "platform": "huggingface", "title": "Dolphin-Math", "source_type": "research", "notes": "开源社区精心筛选的综合杂交数学训练集"},
    {"repo_id": "fblgit/simple-math", "platform": "huggingface", "title": "Simple-Math", "source_type": "k12", "notes": "专注基础四则运算与代数变形"},
    {"repo_id": "garage-bAInd/Open-Platypus", "platform": "huggingface", "title": "Open-Platypus (Math Part)", "source_type": "research", "notes": "STEM领域交叉逻辑题"},
    {"repo_id": "cais/mmlu", "platform": "huggingface", "title": "MMLU (STEM/Math)", "source_type": "research", "notes": "College Math和High School Math子集"},
    {"repo_id": "bespokelabsai/conjecture-bench", "platform": "github", "title": "ConjectureBench", "problem_count": 15000, "source_type": "research", "notes": "15000个开放数学问题，测试猜想提出能力"},
    {"repo_id": "amfo0o0/awesome-AI-Math-Datasets", "platform": "github", "title": "Awesome-AI-Math-Datasets", "source_type": "research", "notes": "终极索引库，汇总世界上所有AI专用数学大题库索引"},

    # 超级聚合集（预训练级无监督语料）
    {"repo_id": "keirp/OpenWebMath", "platform": "huggingface", "title": "OpenWebMath", "data_size": "14.7B tokens", "source_type": "research", "notes": "从Common Crawl过滤的纯数学网页，14.7B Tokens"},
    {"repo_id": "GAIR/MathPile", "platform": "huggingface", "title": "MathPile", "data_size": "9.5B tokens", "source_type": "research", "institution": "SJTU", "notes": "上海交大9.5B高质量Token，含教材/arXiv/Wikipedia"},
    {"repo_id": "EleutherAI/proof-pile-2", "platform": "huggingface", "title": "Proof-Pile-2", "data_size": "55B tokens", "source_type": "formal", "institution": "EleutherAI", "notes": "55B Tokens，数学论文+数学代码+纯数学网页"},
    {"repo_id": "EleutherAI/algebraic-stack", "platform": "huggingface", "title": "AlgebraicStack", "data_size": "11B tokens", "source_type": "formal", "institution": "EleutherAI", "notes": "全网最全形式化数学语言源码（Lean/Coq/Isabelle/LaTeX）"},

    # 合成指令微调集
    {"repo_id": "WizardLM/WizardMath", "platform": "huggingface", "title": "WizardMath", "source_type": "synthetic", "notes": "进化算法把基础数学题变得越来越复杂"},
    {"repo_id": "Opendi/MathScale-QA", "platform": "huggingface", "title": "MathScale-QA", "problem_count": 2000000, "source_type": "synthetic", "notes": "200万道合成数学题，利用大模型构建概念图谱"},
    {"repo_id": "Opendi/MuggleMath", "platform": "huggingface", "title": "MuggleMath", "problem_count": 300000, "source_type": "synthetic", "notes": "30万道合成推导题，让7B模型超越大模型"},
    {"repo_id": "glaiveai/glaive-math-qa", "platform": "huggingface", "title": "Glaive-Math-QA", "problem_count": 100000, "source_type": "synthetic", "notes": "10万道多轮数学对话训练集"},

    # 工具调用推理（TIR）
    {"repo_id": "AI-MO/NuminaMath-TIR", "platform": "huggingface", "title": "NuminaMath-TIR", "source_type": "competition", "notes": "AI奥赛冠军方案，文字推导+Python代码块+执行结果"},
    {"repo_id": "microsoft/ToRA", "platform": "huggingface", "title": "ToRA-Math", "source_type": "research", "institution": "Microsoft", "notes": "微软Tool-Integrated Reasoning Agent数据集"},

    # RLHF/DPO反馈数据集
    {"repo_id": "peiyi9979/Math-Shepherd", "platform": "huggingface", "title": "Math-Shepherd", "source_type": "research", "notes": "给数学推导过程每步打分的数据集"},
    {"repo_id": "openai/prm800k", "platform": "huggingface", "title": "PRM-Math-800K", "problem_count": 800000, "source_type": "competition", "institution": "OpenAI", "notes": "OpenAI过程奖励模型数据，每步推导Good/Bad标记"},

    # 已在212号文档中记录的来源
    {"repo_id": "ShadenA/MathNet", "platform": "huggingface", "title": "MathNet", "problem_count": 30676, "source_type": "competition", "institution": "MIT", "notes": "ICLR 2026，47国17语言，30676题，官方国家队题册"},
    {"repo_id": "AI-MO/NuminaMath-1.5", "platform": "huggingface", "title": "NuminaMath-1.5", "problem_count": 896215, "source_type": "competition", "notes": "90万题，含11万证明题，CoT格式，Apache 2.0"},
    {"repo_id": "DSL-Lab/aops", "platform": "github", "title": "AoPS-Instruct", "problem_count": 600000, "source_type": "competition", "notes": "AoPS论坛600K QA pairs，抗污染时间戳基准"},
    {"repo_id": "rossant/awesome-math", "platform": "github", "title": "awesome-math", "source_type": "research", "notes": "GitHub纯数字化数学资源精选库，近万Star"},
    {"repo_id": "THUDM/MathGLM", "platform": "github", "title": "MathGLM (GitHub)", "source_type": "research", "institution": "Tsinghua", "notes": "清华THUDM MathGLM代码与数据集仓库"},
    {"repo_id": "We-Math/We-Math2.0", "platform": "github", "title": "We-Math 2.0 (GitHub)", "source_type": "multimodal", "institution": "Tsinghua", "notes": "We-Math 2.0数据集构建仓库"},
    {"repo_id": "scnu203/math23k", "platform": "github", "title": "Math23K (GitHub)", "problem_count": 23162, "source_type": "k12", "institution": "Tencent", "language": ["zh"], "notes": "腾讯Math23K GitHub仓库"},
    {"repo_id": "openbmb/UltraData-SFT-2605", "platform": "huggingface", "title": "UltraData-SFT-2605", "source_type": "research", "institution": "Tsinghua", "notes": "清华×面壁智能，含百万级深思考样本，MiniCPM5微调数据"},
]


def build_user_listed_records():
    """把用户消息中提到的数据集构建成ArangoDB记录"""
    records = []
    for ds in USER_LISTED_DATASETS:
        repo_id = ds["repo_id"]
        platform = ds.get("platform", "huggingface")
        record = {
            "_key": sanitize_key(f"{platform}_{repo_id}"),
            "repo_id": repo_id,
            "platform": platform,
            "title": ds.get("title", repo_id),
            "problem_count": ds.get("problem_count"),
            "data_size": ds.get("data_size"),
            "source_type": ds.get("source_type", "unknown"),
            "institution": ds.get("institution"),
            "format": ds.get("format"),
            "language": ds.get("language", ["en"]),
            "notes": ds.get("notes", ""),
            "ingest_source": "user_list",
            "ingest_date": INGEST_DATE,
        }
        if platform == "huggingface":
            record["url"] = f"https://huggingface.co/datasets/{repo_id}"
        elif platform == "github":
            record["url"] = f"https://github.com/{repo_id}"
        records.append(record)
    return records


def merge_records(hf_records, user_records):
    """合并HF API记录和用户列表记录，去重"""
    merged = {}
    for r in hf_records:
        merged[r["repo_id"]] = r
    for r in user_records:
        rid = r["repo_id"]
        if rid in merged:
            # 合并：用户列表的元数据补充到HF记录中
            for k, v in r.items():
                if k in ("_key", "repo_id", "platform", "ingest_source", "ingest_date"):
                    continue
                if v is not None and (k not in merged[rid] or merged[rid][k] is None):
                    merged[rid][k] = v
            # 标记为两个来源都有
            merged[rid]["ingest_source"] = "hf_api+user_list"
            # 保留用户列表的notes
            if r.get("notes"):
                merged[rid]["notes"] = r["notes"]
        else:
            merged[rid] = r
    return list(merged.values())


def ingest_to_arango(records):
    """批量写入ArangoDB"""
    client = ArangoClient(hosts=ARANGO_HOST)
    db = client.db(ARANGO_DB, username=ARANGO_USER, password=ARANGO_PASS)
    col = db.collection(COLLECTION)

    # 先清空（重新入库）
    col.truncate()
    print(f"Truncated collection {COLLECTION}")

    # 批量插入
    batch_size = 500
    total = 0
    for i in range(0, len(records), batch_size):
        batch = records[i:i+batch_size]
        result = col.import_bulk(batch, on_duplicate="update")
        total += len(batch)
        print(f"  Inserted batch {i//batch_size + 1}: {len(batch)} records (total: {total})")

    print(f"\nTotal records ingested: {total}")
    return total


def print_stats(records):
    """打印统计信息"""
    print("\n===== 统计信息 =====")
    print(f"总数据集数: {len(records)}")

    # 按platform
    platforms = {}
    for r in records:
        p = r.get("platform", "unknown")
        platforms[p] = platforms.get(p, 0) + 1
    print(f"按平台: {platforms}")

    # 按tier
    tiers = {}
    for r in records:
        t = r.get("tier", 0)
        tiers[t] = tiers.get(t, 0) + 1
    print(f"按Tier: {tiers}")

    # 按source_type
    types = {}
    for r in records:
        t = r.get("source_type", "unknown")
        types[t] = types.get(t, 0) + 1
    print(f"按来源类型: {types}")

    # 按institution
    insts = {}
    for r in records:
        inst = r.get("institution")
        if inst:
            insts[inst] = insts.get(inst, 0) + 1
    print(f"按机构(top10): {dict(sorted(insts.items(), key=lambda x: -x[1])[:10])}")

    # 有题量信息的
    with_count = [r for r in records if r.get("problem_count")]
    total_problems = sum(r["problem_count"] for r in with_count if r["problem_count"])
    print(f"有题量信息的数据集: {len(with_count)}")
    print(f"已知题量总和: {total_problems:,}")


def main():
    print("===== Step 1: 从HuggingFace API获取math数据集元数据 =====")
    hf_records = fetch_hf_datasets_metadata()

    print(f"\n===== Step 2: 构建用户列表数据集记录 =====")
    user_records = build_user_listed_records()
    print(f"用户列表数据集: {len(user_records)}")

    print(f"\n===== Step 3: 合并去重 =====")
    merged = merge_records(hf_records, user_records)
    print(f"合并后总数: {len(merged)}")

    print(f"\n===== Step 4: 入库ArangoDB =====")
    ingest_to_arango(merged)

    print_stats(merged)

    # 保存完整列表到JSON文件
    output_path = "~/master-mind-glm5.2-worktree/knowledge/problem_banks/math_datasets_catalog.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
    print(f"\n完整目录已保存到: {output_path}")


if __name__ == "__main__":
    main()
