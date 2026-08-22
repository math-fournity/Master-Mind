#!/usr/bin/env python3
"""gen_prompts.py — POC-2.5c首批24份prompt生成器

真理源：first_batch_12_selection.md（12道清单）+ hintinstance_v02_I_mid_frozen.md（冻结Hint文本）。

题面拼装规则（2026-08-22核实三种来源后的结论）：
  - ArangoDB problem_text字段截断（500字符上限，实测有346/500两种断口），禁用
  - D盘problem.txt多数只含题面裸文、含约束块者也缺第3/4条与收尾句（残缺）
  - 历史round1 bare实际收到的prompt=题面+完整约束块，规范约束块提取自
    _pipe/problems/p8ab0cce440544224b15e/AGENTS.md（完整版唯一现役样例）
  故：prompt = 题面裸文(problem.txt去尾部空白) + 规范约束块。

输出：runs/<problem_id>__{T|C}/prompt.txt
  T组 = 冻结HintInstance块 + 分隔线 + 题面+约束块
  C组 = 题面+约束块（与T组hint后内容逐字一致）
"""

import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent / "batch1_prompts"
SOLVER_BASE = Path("/data/math-agent-glm5.2-tmux-agents-dir/p27-continuation")
CANONICAL_CONSTRAINTS = HERE.parent / "canonical_constraints_block.txt"

PROBLEMS = [
    "deepmath_103k_00006253",
    "deepmath_103k_00012700",
    "deepmath_103k_00017608",
    "deepmath_103k_00019730",
    "deepmath_103k_00000688",
    "amo_bench_00000006",
    "amo_bench_00000008",
    "deepmath_103k_00002077",
    "deepmath_103k_00003167",
    "deepmath_103k_00001678",
    "deepmath_103k_00006809",
    "deepmath_103k_00001747",
]

HINT_BLOCK = """> **策略提示（可选采用）**：
>
> 你在推导中得出的每一个新公式或关键结论，都值得用**一个你已经验证过的具体实例**做代入检验——特别是那些"看起来正好能推出你想要的结论"的时刻：过于顺利的矛盾往往藏着算术错误或被忽略的前提条件。
>
> 具体做法：
> 1. 手头保留一个已确认成立的实例（满足全部条件的具体取值），作为检验基准。
> 2. 每导出一个新公式，把它代入这个实例核对；不一致时不要丢弃公式——先定位是哪一步出了问题（抄反？漏因子？隐藏前提？），修复后在同一实例上复验。
> 3. 公式通过检验后，顺手标注它的适用条件——很多公式只在特定奇偶/整除前提下成立，提前记下可以避免后面的误用。
>
> 把这些检验结果随手记入你的解题笔记。

---


"""


def main():
    cons = CANONICAL_CONSTRAINTS.read_text()
    for pid in PROBLEMS:
        src = SOLVER_BASE / f"p27-full-{pid}" / "problem.txt"
        if not src.is_file():
            raise FileNotFoundError(f"题面缺失: {src}")
        body = src.read_text().rstrip()
        # 若磁盘文件已含（残缺）约束块，切掉后再拼规范块
        if "## 解题约束" in body:
            body = body[: body.index("## 解题约束")].rstrip()
        full_problem = body + "\n\n" + cons + "\n"
        if len(full_problem) < 450:
            raise ValueError(f"拼装后过短疑似异常: {pid} {len(full_problem)}B")
        for arm in ("T", "C"):
            rd = HERE / f"{pid}__{arm}"
            rd.mkdir(exist_ok=True)
            out = rd / "prompt.txt"
            if arm == "T":
                out.write_text(HINT_BLOCK + full_problem)
            else:
                out.write_text(full_problem)
            print(f"written {out.relative_to(HERE)} ({out.stat().st_size}B)")
    # T/C一致性断言：每题C组全文必须是T组去掉hint块的剩余部分
    for pid in PROBLEMS:
        t = (HERE / f"{pid}__T" / "prompt.txt").read_text()
        c = (HERE / f"{pid}__C" / "prompt.txt").read_text()
        assert t.endswith(c), f"T/C不一致: {pid}"
    print("done: 24 prompts, T/C suffix-consistency PASS")


if __name__ == "__main__":
    main()
