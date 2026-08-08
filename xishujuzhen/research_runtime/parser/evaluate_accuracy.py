"""
253号解析准确率评估脚本。

对比real_llm_responses（GLM-5.2真实解析结果）和gold_standard（人工标注正确答案），
计算260号§3.3.4的6项准确率指标：
1. 事件类型准确率：正确分类的事件数 / 总事件数
2. 数学对象提取率：正确提取的对象数 / Gold Standard中的对象数
3. SymPy验证通过率：通过验证的对象数 / 有sympy_expr的对象数
4. 六元组字段准确率：正确字段数 / 总字段数（6×轮数）
5. 前沿节点识别率：正确识别的轮数 / 总轮数
6. 卡点类型识别率：正确识别的轮数 / 有卡点的轮数

运行：
    cd ~/master-mind-glm5.2-worktree
    .venv/bin/python3 -m xishujuzhen.research_runtime.parser.evaluate_accuracy
"""

import sys
from typing import List, Tuple

from .test_data.gold_standard import GOLD_STANDARDS, get_gold_standard
from .test_data.real_llm_responses import REAL_RESPONSES, get_real_response
from .test_data.case_253 import QA_SEQUENCE


# ===========================================================================
# 对比辅助函数
# ===========================================================================

def _collect_math_objects(response: dict) -> List[dict]:
    """从响应中收集所有math_objects（跨事件）"""
    objects = []
    for evt in response.get("semantic_events", []):
        for mo in evt.get("math_objects", []):
            objects.append(mo)
    return objects


def _get_frontier_node(response: dict) -> dict:
    """获取响应中的前沿节点（is_frontier=True的节点）"""
    for node in response.get("trajectory_nodes", []):
        if node.get("is_frontier", False):
            return node
    return None


def _has_stall(response: dict) -> bool:
    """判断响应中是否有STALL类型的事件（即有卡点）"""
    for evt in response.get("semantic_events", []):
        if evt.get("type") == "STALL":
            return True
    return False


def _get_stall_type(response: dict) -> str:
    """
    获取卡点类型。

    返回：
    - "knowledge_gap"：知识瓶颈（U_t中有"知识瓶颈"或"badly approximable"）
    - "thinking_stall"：思维停滞（有STALL但不是知识瓶颈）
    - "none"：无卡点
    """
    if not _has_stall(response):
        return "none"

    # 检查U_t中是否有知识瓶颈标记
    for u in response.get("six_tuple", {}).get("U_t", []):
        desc = u.get("description", "")
        if "知识瓶颈" in desc or "badly approximable" in desc or "知识不足" in desc:
            return "knowledge_gap"

    # 检查parse_warnings中是否有知识瓶颈标记
    for w in response.get("parse_warnings", []):
        if "知识瓶颈" in w or "知识不足" in w:
            return "knowledge_gap"

    return "thinking_stall"


def _normalize_type(t: str) -> str:
    """归一化事件类型（大小写不敏感）"""
    return t.upper().strip() if t else ""


def _normalize_node_type(t: str) -> str:
    """归一化节点类型（小写）"""
    return t.lower().strip() if t else ""


def _descriptions_match(d1: str, d2: str) -> bool:
    """判断两个描述是否匹配（精确匹配或一方包含另一方）"""
    if d1 == d2:
        return True
    d1 = d1.strip()
    d2 = d2.strip()
    if d1 in d2 or d2 in d1:
        return True
    return False


def _math_objects_match(mo1: dict, mo2: dict) -> bool:
    """判断两个math_objects是否匹配（名称匹配+类型匹配）"""
    name1 = mo1.get("name", "")
    name2 = mo2.get("name", "")
    type1 = mo1.get("object_type", "")
    type2 = mo2.get("object_type", "")

    # 名称匹配（精确或包含）
    name_match = (
        name1 == name2
        or name1 in name2
        or name2 in name1
    )
    # 类型匹配
    type_match = (type1 == type2)

    return name_match and type_match


def _six_tuple_field_match(
    real_items: List[dict],
    gold_items: List[dict],
    key_field: str,
) -> Tuple[int, int]:
    """
    对比六元组某个字段的条目。

    Returns:
        (匹配数, gold中的条目数)
    """
    matched = 0
    for gold_item in gold_items:
        gold_key = gold_item.get(key_field, "")
        for real_item in real_items:
            real_key = real_item.get(key_field, "")
            if _descriptions_match(gold_key, real_key):
                matched += 1
                break
    return matched, len(gold_items)


# ===========================================================================
# 逐轮对比
# ===========================================================================

def evaluate_round(round_index: int) -> dict:
    """
    对比单个A_i的real_response和gold_standard。

    Returns:
        包含各项对比结果的dict
    """
    real = get_real_response(round_index)
    gold = get_gold_standard(round_index)

    # ---- 1. 事件类型准确率 ----
    real_events = real.get("semantic_events", [])
    gold_events = gold.get("semantic_events", [])

    # 用最优匹配：对每个gold事件，在real事件中找类型匹配的
    real_types_used = set()
    event_type_correct = 0
    for gold_evt in gold_events:
        gold_type = _normalize_type(gold_evt.get("type", ""))
        gold_desc = gold_evt.get("description", "")
        best_idx = None
        for i, real_evt in enumerate(real_events):
            if i in real_types_used:
                continue
            real_type = _normalize_type(real_evt.get("type", ""))
            if real_type == gold_type:
                # 优先选描述也匹配的
                real_desc = real_evt.get("description", "")
                if _descriptions_match(gold_desc, real_desc):
                    best_idx = i
                    break
                if best_idx is None:
                    best_idx = i
        if best_idx is not None:
            event_type_correct += 1
            real_types_used.add(best_idx)

    event_type_total = len(gold_events)

    # ---- 2. 数学对象提取率 ----
    real_math_objects = _collect_math_objects(real)
    gold_math_objects = _collect_math_objects(gold)

    mo_matched = 0
    real_mo_used = set()
    for gold_mo in gold_math_objects:
        for i, real_mo in enumerate(real_math_objects):
            if i in real_mo_used:
                continue
            if _math_objects_match(gold_mo, real_mo):
                mo_matched += 1
                real_mo_used.add(i)
                break

    mo_total = len(gold_math_objects)

    # ---- 3. SymPy验证通过率 ----
    # 对real_response中有sympy_expr的math_objects，检查是否可被SymPy解析
    sympy_pass = 0
    sympy_total = 0
    for mo in real_math_objects:
        expr = mo.get("sympy_expr")
        if expr:
            sympy_total += 1
            if _check_sympy_parseable(expr):
                sympy_pass += 1

    # ---- 4. 六元组字段准确率 ----
    real_st = real.get("six_tuple", {})
    gold_st = gold.get("six_tuple", {})

    # V_t：对比statement
    v_match, v_total = _six_tuple_field_match(
        real_st.get("V_t", []), gold_st.get("V_t", []), "statement"
    )
    # F_t：对比statement
    f_match, f_total = _six_tuple_field_match(
        real_st.get("F_t", []), gold_st.get("F_t", []), "statement"
    )
    # O_t：对比description
    o_match, o_total = _six_tuple_field_match(
        real_st.get("O_t", []), gold_st.get("O_t", []), "description"
    )
    # R_t：对比name
    r_match, r_total = _six_tuple_field_match(
        real_st.get("R_t", []), gold_st.get("R_t", []), "name"
    )
    # E_t：对比content
    e_match, e_total = _six_tuple_field_match(
        real_st.get("E_t", []), gold_st.get("E_t", []), "content"
    )
    # U_t：对比description
    u_match, u_total = _six_tuple_field_match(
        real_st.get("U_t", []), gold_st.get("U_t", []), "description"
    )

    six_tuple_correct = v_match + f_match + o_match + r_match + e_match + u_match
    six_tuple_total = v_total + f_total + o_total + r_total + e_total + u_total

    # ---- 5. 前沿节点识别率 ----
    real_frontier = _get_frontier_node(real)
    gold_frontier = _get_frontier_node(gold)

    frontier_correct = False
    if real_frontier and gold_frontier:
        real_ftype = _normalize_node_type(real_frontier.get("type", ""))
        gold_ftype = _normalize_node_type(gold_frontier.get("type", ""))
        if real_ftype == gold_ftype:
            frontier_correct = True

    # ---- 6. 卡点类型识别率 ----
    real_stall_type = _get_stall_type(real)
    gold_stall_type = _get_stall_type(gold)
    has_stall = (_has_stall(gold))

    stall_correct = False
    if has_stall:
        stall_correct = (real_stall_type == gold_stall_type)

    return {
        "round_index": round_index,
        "event_type_correct": event_type_correct,
        "event_type_total": event_type_total,
        "mo_matched": mo_matched,
        "mo_total": mo_total,
        "sympy_pass": sympy_pass,
        "sympy_total": sympy_total,
        "six_tuple_correct": six_tuple_correct,
        "six_tuple_total": six_tuple_total,
        "v_match": v_match, "v_total": v_total,
        "f_match": f_match, "f_total": f_total,
        "o_match": o_match, "o_total": o_total,
        "r_match": r_match, "r_total": r_total,
        "e_match": e_match, "e_total": e_total,
        "u_match": u_match, "u_total": u_total,
        "frontier_correct": frontier_correct,
        "has_stall": has_stall,
        "stall_correct": stall_correct,
        "real_stall_type": real_stall_type,
        "gold_stall_type": gold_stall_type,
    }


def _check_sympy_parseable(expr: str) -> bool:
    """检查SymPy表达式是否可被解析"""
    try:
        import sympy as sp
        # 处理Eq(...)格式
        expr_clean = expr.strip()
        if expr_clean.startswith("Eq("):
            # 用sympify尝试解析Eq表达式
            # 替换Rational为sp.Rational
            expr_clean = expr_clean.replace("Rational(", "sp.Rational(")
            sp.sympify(expr_clean, locals={"sp": sp, "Rational": sp.Rational})
        else:
            expr_clean = expr_clean.replace("Rational(", "sp.Rational(")
            sp.sympify(expr_clean, locals={"sp": sp, "Rational": sp.Rational})
        return True
    except Exception:
        return False


# ===========================================================================
# 汇总评估
# ===========================================================================

def evaluate_all() -> dict:
    """
    对A1-A10全部做对比，汇总6项指标。

    Returns:
        包含汇总指标的dict
    """
    round_results = []
    for i in range(1, 11):
        result = evaluate_round(i)
        round_results.append(result)

    # 汇总
    total_event_correct = sum(r["event_type_correct"] for r in round_results)
    total_event_total = sum(r["event_type_total"] for r in round_results)

    total_mo_matched = sum(r["mo_matched"] for r in round_results)
    total_mo_total = sum(r["mo_total"] for r in round_results)

    total_sympy_pass = sum(r["sympy_pass"] for r in round_results)
    total_sympy_total = sum(r["sympy_total"] for r in round_results)

    total_st_correct = sum(r["six_tuple_correct"] for r in round_results)
    total_st_total = sum(r["six_tuple_total"] for r in round_results)

    total_frontier_correct = sum(1 for r in round_results if r["frontier_correct"])
    total_frontier_total = len(round_results)

    stall_rounds = [r for r in round_results if r["has_stall"]]
    total_stall_correct = sum(1 for r in stall_rounds if r["stall_correct"])
    total_stall_total = len(stall_rounds)

    return {
        "round_results": round_results,
        "event_type_accuracy": (total_event_correct, total_event_total),
        "math_object_extraction": (total_mo_matched, total_mo_total),
        "sympy_verification": (total_sympy_pass, total_sympy_total),
        "six_tuple_accuracy": (total_st_correct, total_st_total),
        "frontier_identification": (total_frontier_correct, total_frontier_total),
        "stall_identification": (total_stall_correct, total_stall_total),
    }


# ===========================================================================
# 输出格式化
# ===========================================================================

def _pct(correct: int, total: int) -> str:
    """计算百分比"""
    if total == 0:
        return "N/A"
    return f"{correct/total*100:.1f}%"


def _mark(value: float, threshold: float) -> str:
    """达标标记"""
    return "✅" if value >= threshold else "❌"


def main() -> int:
    print()
    print("=" * 60)
    print("=== 253号解析准确率评估 ===")
    print("=" * 60)
    print()

    results = evaluate_all()
    round_results = results["round_results"]

    # ---- 逐轮对比 ----
    print("--- 逐轮对比 ---")
    for r in round_results:
        i = r["round_index"]
        evt_ok = "✅" if r["event_type_correct"] == r["event_type_total"] else "⚠️"
        mo_ok = "✅" if r["mo_matched"] == r["mo_total"] else "⚠️"
        st_pct = r["six_tuple_correct"] / r["six_tuple_total"] * 100 if r["six_tuple_total"] > 0 else 100
        st_ok = "✅" if st_pct >= 75 else "⚠️"
        ft_ok = "✅" if r["frontier_correct"] else "❌"

        stall_str = ""
        if r["has_stall"]:
            stall_ok = "✅" if r["stall_correct"] else "❌"
            stall_str = f", 卡点 {r['real_stall_type']} {stall_ok}"

        print(
            f"A{i}: 事件类型 {r['event_type_correct']}/{r['event_type_total']} {evt_ok}, "
            f"数学对象 {r['mo_matched']}/{r['mo_total']} {mo_ok}, "
            f"六元组 {r['six_tuple_correct']}/{r['six_tuple_total']} {st_ok}, "
            f"前沿节点 {ft_ok}{stall_str}"
        )

    print()

    # ---- 汇总指标 ----
    print("--- 汇总指标 ---")
    evt_c, evt_t = results["event_type_accuracy"]
    mo_c, mo_t = results["math_object_extraction"]
    sym_c, sym_t = results["sympy_verification"]
    st_c, st_t = results["six_tuple_accuracy"]
    ft_c, ft_t = results["frontier_identification"]
    stall_c, stall_t = results["stall_identification"]

    evt_pct = evt_c / evt_t * 100 if evt_t > 0 else 0
    mo_pct = mo_c / mo_t * 100 if mo_t > 0 else 0
    sym_pct = sym_c / sym_t * 100 if sym_t > 0 else 0
    st_pct = st_c / st_t * 100 if st_t > 0 else 0
    ft_pct = ft_c / ft_t * 100 if ft_t > 0 else 0
    stall_pct = stall_c / stall_t * 100 if stall_t > 0 else 0

    print(f"事件类型准确率: {evt_c}/{evt_t} = {_pct(evt_c, evt_t)}")
    print(f"数学对象提取率: {mo_c}/{mo_t} = {_pct(mo_c, mo_t)}")
    print(f"SymPy验证通过率: {sym_c}/{sym_t} = {_pct(sym_c, sym_t)}")
    print(f"六元组字段准确率: {st_c}/{st_t} = {_pct(st_c, st_t)}")
    print(f"前沿节点识别率: {ft_c}/{ft_t} = {_pct(ft_c, ft_t)}")
    print(f"卡点类型识别率: {stall_c}/{stall_t} = {_pct(stall_c, stall_t)}")

    print()

    # ---- 评估结论 ----
    print("--- 评估结论 ---")
    print("最低可接受值达标情况:")
    print(f"  事件类型 ≥70%: {_mark(evt_pct, 70)} ({evt_pct:.1f}%)")
    print(f"  数学对象 ≥80%: {_mark(mo_pct, 80)} ({mo_pct:.1f}%)")
    print(f"  SymPy验证 ≥75%: {_mark(sym_pct, 75)} ({sym_pct:.1f}%)")
    print(f"  六元组 ≥65%: {_mark(st_pct, 65)} ({st_pct:.1f}%)")
    print(f"  前沿节点 ≥80%: {_mark(ft_pct, 80)} ({ft_pct:.1f}%)")
    print(f"  卡点类型 ≥70%: {_mark(stall_pct, 70)} ({stall_pct:.1f}%)")

    print()
    print("目标值达标情况:")
    print(f"  事件类型 ≥80%: {_mark(evt_pct, 80)} ({evt_pct:.1f}%)")
    print(f"  数学对象 ≥90%: {_mark(mo_pct, 90)} ({mo_pct:.1f}%)")
    print(f"  SymPy验证 ≥85%: {_mark(sym_pct, 85)} ({sym_pct:.1f}%)")
    print(f"  六元组 ≥75%: {_mark(st_pct, 75)} ({st_pct:.1f}%)")
    print(f"  前沿节点 ≥90%: {_mark(ft_pct, 90)} ({ft_pct:.1f}%)")
    print(f"  卡点类型 ≥80%: {_mark(stall_pct, 80)} ({stall_pct:.1f}%)")

    print()

    # 判断是否全部达标最低可接受值
    min_thresholds = {
        "事件类型": (evt_pct, 70),
        "数学对象": (mo_pct, 80),
        "SymPy验证": (sym_pct, 75),
        "六元组": (st_pct, 65),
        "前沿节点": (ft_pct, 80),
        "卡点类型": (stall_pct, 70),
    }
    all_min_pass = all(pct >= thr for pct, thr in min_thresholds.values())

    if all_min_pass:
        print("🎉 所有指标达到最低可接受值！解析质量可用。")
        return 0
    else:
        failed = [name for name, (pct, thr) in min_thresholds.items() if pct < thr]
        print(f"⚠️  以下指标未达最低可接受值: {', '.join(failed)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
