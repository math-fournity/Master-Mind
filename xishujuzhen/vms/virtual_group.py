#!/usr/bin/env python3
"""
虚拟群生成器 —— POC-VMS-0基础设施

生成不同结构/规模的虚拟群，随机化元素符号，
验证群公理，为虚拟题目生成和baseline测试提供基础。

支持群类型：
  - 循环群 C_n
  - 二面体群 D_n
  - 对称群 S_n（n≤4，乘法表不太大）
  - 直积群 C_a × C_b
  - 四元数群 Q_8

符号随机化：e保留为单位元，其余元素随机分配符号（α/β/γ/δ/... 或 x1/x2/...）。
"""

import json
import random
import string
import itertools
from itertools import product
from dataclasses import dataclass, field
from typing import Optional


# ============================================================
# 符号集
# ============================================================

GREEK_SYMBOLS = ['α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ',
                 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω']

LATIN_SYMBOLS = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

INDEXED_SYMBOLS = ['x₁', 'x₂', 'x₃', 'x₄', 'x₅', 'x₆', 'x₇', 'x₈', 'x₉', 'x₁₀',
                   'x₁₁', 'x₁₂', 'x₁₃', 'x₁₄', 'x₁₅', 'x₁₆', 'x₁₇', 'x₁₈', 'x₁₉', 'x₂₀',
                   'x₂₁', 'x₂₂', 'x₂₃', 'x₂₄']


def get_symbol_set(style: str, n: int) -> list[str]:
    """获取n个非单位元符号（不含e）。"""
    if style == 'greek':
        pool = GREEK_SYMBOLS
    elif style == 'latin':
        pool = LATIN_SYMBOLS
    elif style == 'indexed':
        pool = INDEXED_SYMBOLS
    else:
        pool = GREEK_SYMBOLS
    if n > len(pool):
        # fallback：用 s1, s2, ...
        return [f's{i+1}' for i in range(n)]
    return pool[:n]


# ============================================================
# 虚拟群数据结构
# ============================================================

@dataclass
class VirtualGroup:
    """一个虚拟群实例。"""
    gid: str                          # 群ID（如 VG_001）
    group_type: str                   # 结构类型：cyclic / dihedral / symmetric / direct_product / quaternion
    order: int                        # 阶
    elements: list[str]               # 元素符号列表（第一个是单位元 'e'）
    identity: str                     # 单位元符号（固定为 'e'）
    multiplication_table: dict        # 乘法表：{(a,b): c} 表示 a*b=c
    structure_params: dict            # 结构参数（如 n for C_n, D_n）
    symbol_style: str                 # 符号风格

    def to_dict(self) -> dict:
        return {
            'gid': self.gid,
            'group_type': self.group_type,
            'order': self.order,
            'elements': self.elements,
            'identity': self.identity,
            'multiplication_table': {f'{a}*{b}': c for (a, b), c in self.multiplication_table.items()},
            'structure_params': self.structure_params,
            'symbol_style': self.symbol_style,
        }

    def mult(self, a: str, b: str) -> str:
        return self.multiplication_table[(a, b)]

    def inverse(self, a: str) -> str:
        for b in self.elements:
            if self.multiplication_table[(a, b)] == self.identity:
                return b
        raise ValueError(f"No inverse for {a}")

    def power(self, a: str, n: int) -> str:
        if n == 0:
            return self.identity
        result = a
        for _ in range(n - 1):
            result = self.multiplication_table[(result, a)]
        return result

    def order_of_element(self, a: str) -> int:
        """计算元素a的阶。"""
        current = a
        for i in range(1, self.order + 1):
            if current == self.identity:
                return i
            current = self.multiplication_table[(current, a)]
        return self.order  # fallback


# ============================================================
# 群公理验证
# ============================================================

def verify_group_axioms(g: VirtualGroup) -> tuple[bool, str]:
    """验证群公理。返回 (是否通过, 失败原因)。"""
    elems = g.elements
    table = g.multiplication_table

    # 1. 封闭性
    for a in elems:
        for b in elems:
            if (a, b) not in table:
                return False, f"Not closed: ({a},{b}) not in table"
            if table[(a, b)] not in elems:
                return False, f"Not closed: {a}*{b}={table[(a,b)]} not in elements"

    # 2. 结合律
    for a in elems:
        for b in elems:
            for c in elems:
                lhs = table[(table[(a, b)], c)]
                rhs = table[(a, table[(b, c)])]
                if lhs != rhs:
                    return False, f"Not associative: ({a}*{b})*{c}={lhs} != {a}*({b}*{c})={rhs}"

    # 3. 单位元
    e = g.identity
    for a in elems:
        if table[(e, a)] != a:
            return False, f"Identity left: e*{a}={table[(e,a)]} != {a}"
        if table[(a, e)] != a:
            return False, f"Identity right: {a}*e={table[(a,e)]} != {a}"

    # 4. 逆元
    for a in elems:
        has_inv = False
        for b in elems:
            if table[(a, b)] == e and table[(b, a)] == e:
                has_inv = True
                break
        if not has_inv:
            return False, f"No inverse for {a}"

    return True, "OK"


# ============================================================
# 群生成器
# ============================================================

def _apply_symbols(internal_elems: list[int], symbol_style: str, rng: random.Random) -> list[str]:
    """把内部整数表示转换为随机化符号。internal_elems[0]=0 是单位元。"""
    n = len(internal_elems) - 1  # 非单位元个数
    symbols = get_symbol_set(symbol_style, n)
    rng.shuffle(symbols)
    # 0 → 'e', 其余按shuffle后的顺序分配
    mapping = {0: 'e'}
    for i, s in enumerate(symbols, 1):
        mapping[i] = s
    return [mapping[e] for e in internal_elems]


def _build_table_from_internal(internal_mult: dict, sym_map: dict[int, str]) -> dict:
    """从内部整数乘法表构建符号乘法表。"""
    return {(sym_map[a], sym_map[b]): sym_map[c]
            for (a, b), c in internal_mult.items()}


def gen_cyclic(n: int, gid: str, symbol_style: str, rng: random.Random) -> VirtualGroup:
    """生成循环群 C_n。内部表示：元素 0..n-1，运算 = (a+b) mod n。"""
    internal_elems = list(range(n))
    internal_mult = {(a, b): (a + b) % n for a in range(n) for b in range(n)}

    sym_map = {0: 'e'}
    symbols = get_symbol_set(symbol_style, n - 1)
    rng.shuffle(symbols)
    for i, s in enumerate(symbols, 1):
        sym_map[i] = s

    elems = [sym_map[e] for e in internal_elems]
    mult_table = _build_table_from_internal(internal_mult, sym_map)

    return VirtualGroup(
        gid=gid, group_type='cyclic', order=n,
        elements=elems, identity='e',
        multiplication_table=mult_table,
        structure_params={'n': n},
        symbol_style=symbol_style,
    )


def gen_dihedral(n: int, gid: str, symbol_style: str, rng: random.Random) -> VirtualGroup:
    """生成二面体群 D_n（阶2n）。内部表示：元素 (r^i, s^j)，i∈{0..n-1}, j∈{0,1}。
    内部整数编码：k = i + j*n，k∈{0..2n-1}。
    运算：r^i * r^k = r^(i+k mod n)，r^i * s^j = s^(j)，s * r = r^(-1) * s。
    (r^a s^b)(r^c s^d) = r^(a + (-1)^b * c) s^(b+d)
    """
    order = 2 * n
    internal_elems = list(range(order))

    def decode(k):
        return k % n, k // n  # (i, j)

    def encode(i, j):
        return i % n + j * n

    internal_mult = {}
    for a in range(order):
        for b in range(order):
            ai, aj = decode(a)
            bi, bj = decode(b)
            # (r^ai s^aj)(r^bi s^bj) = r^(ai + (-1)^aj * bi) s^(aj + bj)
            ci = (ai + ((-1) ** aj) * bi) % n
            cj = (aj + bj) % 2
            internal_mult[(a, b)] = encode(ci, cj)

    sym_map = {0: 'e'}
    symbols = get_symbol_set(symbol_style, order - 1)
    rng.shuffle(symbols)
    for i, s in enumerate(symbols, 1):
        sym_map[i] = s

    elems = [sym_map[e] for e in internal_elems]
    mult_table = _build_table_from_internal(internal_mult, sym_map)

    return VirtualGroup(
        gid=gid, group_type='dihedral', order=order,
        elements=elems, identity='e',
        multiplication_table=mult_table,
        structure_params={'n': n},
        symbol_style=symbol_style,
    )


def gen_symmetric(n: int, gid: str, symbol_style: str, rng: random.Random) -> VirtualGroup:
    """生成对称群 S_n。内部表示：排列 0..n!-1（lexicographic index）。"""
    from math import factorial
    order = factorial(n)

    # 生成所有排列
    perms = list(itertools.permutations(range(n)))
    assert len(perms) == order

    # 排列到索引的映射
    perm_to_idx = {p: i for i, p in enumerate(perms)}

    def compose(p, q):
        """p∘q: 先q后p。"""
        return tuple(p[q[i]] for i in range(n))

    internal_mult = {}
    for a in range(order):
        for b in range(order):
            c = compose(perms[a], perms[b])
            internal_mult[(a, b)] = perm_to_idx[c]

    sym_map = {0: 'e'}  # perms[0] = identity permutation
    symbols = get_symbol_set(symbol_style, order - 1)
    rng.shuffle(symbols)
    for i, s in enumerate(symbols, 1):
        sym_map[i] = s

    elems = [sym_map[e] for e in range(order)]
    mult_table = _build_table_from_internal(internal_mult, sym_map)

    return VirtualGroup(
        gid=gid, group_type='symmetric', order=order,
        elements=elems, identity='e',
        multiplication_table=mult_table,
        structure_params={'n': n},
        symbol_style=symbol_style,
    )


def gen_direct_product(a: int, b: int, gid: str, symbol_style: str, rng: random.Random) -> VirtualGroup:
    """生成直积群 C_a × C_b。内部表示：(i,j)，i∈{0..a-1}, j∈{0..b-1}。
    内部整数编码：k = i*b + j，k∈{0..a*b-1}。
    运算：分量加法 mod a/b。
    """
    order = a * b
    internal_elems = list(range(order))

    def decode(k):
        return k // b, k % b  # (i, j)

    def encode(i, j):
        return i * b + j

    internal_mult = {}
    for x in range(order):
        for y in range(order):
            xi, xj = decode(x)
            yi, yj = decode(y)
            internal_mult[(x, y)] = encode((xi + yi) % a, (xj + yj) % b)

    sym_map = {0: 'e'}
    symbols = get_symbol_set(symbol_style, order - 1)
    rng.shuffle(symbols)
    for i, s in enumerate(symbols, 1):
        sym_map[i] = s

    elems = [sym_map[e] for e in internal_elems]
    mult_table = _build_table_from_internal(internal_mult, sym_map)

    return VirtualGroup(
        gid=gid, group_type='direct_product', order=order,
        elements=elems, identity='e',
        multiplication_table=mult_table,
        structure_params={'a': a, 'b': b},
        symbol_style=symbol_style,
    )


def gen_quaternion(gid: str, symbol_style: str, rng: random.Random) -> VirtualGroup:
    """生成四元数群 Q_8。元素：{1, -1, i, -i, j, -j, k, -k}。
    内部编码：index = sign_bit * 4 + unit，其中 unit∈{0=1,1=i,2=j,3=k}，sign_bit∈{0=+,1=-}。
    即：0=1, 1=-1, 2=i, 3=-i, 4=j, 5=-j, 6=k, 7=-k。
    """
    # 四元数乘法规则：(sign_a, unit_a) * (sign_b, unit_b) = (sign_a*sign_b*sr, ur)
    # unit: 0=1, 1=i, 2=j, 3=k
    # unit_rule[ua][ub] = (result_unit, sign_factor)
    unit_rule = {
        (0, 0): (0, 1),   # 1*1 = 1
        (0, 1): (1, 1),   # 1*i = i
        (0, 2): (2, 1),   # 1*j = j
        (0, 3): (3, 1),   # 1*k = k
        (1, 0): (1, 1),   # i*1 = i
        (1, 1): (0, -1),  # i*i = -1
        (1, 2): (3, 1),   # i*j = k
        (1, 3): (2, -1),  # i*k = -j
        (2, 0): (2, 1),   # j*1 = j
        (2, 1): (3, -1),  # j*i = -k
        (2, 2): (0, -1),  # j*j = -1
        (2, 3): (1, 1),   # j*k = i
        (3, 0): (3, 1),   # k*1 = k
        (3, 1): (2, 1),   # k*i = j
        (3, 2): (1, -1),  # k*j = -i
        (3, 3): (0, -1),  # k*k = -1
    }

    def decode(idx):
        sign_bit = idx // 4  # 0=+, 1=-
        unit = idx % 4
        return sign_bit, unit

    def encode(sign_bit, unit):
        return sign_bit * 4 + unit

    internal_mult = {}
    for a in range(8):
        for b in range(8):
            sa, ua = decode(a)
            sb, ub = decode(b)
            ur, sf = unit_rule[(ua, ub)]
            # 总符号 = sign_a * sign_b * sign_factor
            # sign_a = +1 if sa=0, -1 if sa=1
            total_sign = ((-1) ** sa) * ((-1) ** sb) * sf
            result_sign_bit = 0 if total_sign > 0 else 1
            internal_mult[(a, b)] = encode(result_sign_bit, ur)

    sym_map = {0: 'e'}
    symbols = get_symbol_set(symbol_style, 7)
    rng.shuffle(symbols)
    for i, s in enumerate(symbols, 1):
        sym_map[i] = s

    elems = [sym_map[e] for e in range(8)]
    mult_table = _build_table_from_internal(internal_mult, sym_map)

    return VirtualGroup(
        gid=gid, group_type='quaternion', order=8,
        elements=elems, identity='e',
        multiplication_table=mult_table,
        structure_params={},
        symbol_style=symbol_style,
    )


# ============================================================
# 批量生成
# ============================================================

def generate_batch(count: int = 100, seed: int = 42) -> list[VirtualGroup]:
    """批量生成虚拟群。

    生成策略：
    - 覆盖4阶/6阶/8阶/12阶
    - 覆盖循环群/二面体群/对称群/直积群/四元数群
    - 符号随机化（greek/latin/indexed 随机选）
    """
    rng = random.Random(seed)

    # 生成模板池：(生成函数, 参数)
    templates = [
        # 4阶
        (gen_cyclic, {'n': 4}),
        (gen_direct_product, {'a': 2, 'b': 2}),   # Klein four-group
        # 6阶
        (gen_cyclic, {'n': 6}),
        (gen_dihedral, {'n': 3}),                  # D_3 ≅ S_3
        # 8阶
        (gen_cyclic, {'n': 8}),
        (gen_dihedral, {'n': 4}),                  # D_4
        (gen_direct_product, {'a': 2, 'b': 4}),    # C_2 × C_4
        (gen_direct_product, {'a': 2, 'b': 2}),    # C_2 × C_2 (4阶，但可以再生成一次)
        (gen_quaternion, {}),
        # 12阶
        (gen_cyclic, {'n': 12}),
        (gen_dihedral, {'n': 6}),                  # D_6
        (gen_direct_product, {'a': 3, 'b': 4}),    # C_3 × C_4 ≅ C_12
        (gen_direct_product, {'a': 2, 'b': 6}),    # C_2 × C_6
        # 对称群
        (gen_symmetric, {'n': 3}),                 # S_3 (6阶)
        (gen_symmetric, {'n': 4}),                 # S_4 (24阶)
    ]

    groups = []
    for i in range(count):
        gen_func, params = templates[i % len(templates)]
        symbol_style = rng.choice(['greek', 'latin', 'indexed'])
        gid = f'VG_{i+1:03d}'

        if gen_func == gen_cyclic:
            g = gen_cyclic(params['n'], gid, symbol_style, rng)
        elif gen_func == gen_dihedral:
            g = gen_dihedral(params['n'], gid, symbol_style, rng)
        elif gen_func == gen_symmetric:
            g = gen_symmetric(params['n'], gid, symbol_style, rng)
        elif gen_func == gen_direct_product:
            g = gen_direct_product(params['a'], params['b'], gid, symbol_style, rng)
        elif gen_func == gen_quaternion:
            g = gen_quaternion(gid, symbol_style, rng)
        else:
            continue

        # 验证群公理
        ok, reason = verify_group_axioms(g)
        if not ok:
            raise RuntimeError(f"Group {gid} failed verification: {reason}")

        groups.append(g)

    return groups


# ============================================================
# 群性质计算（供题目生成和答案验证使用）
# ============================================================

def find_subgroups(g: VirtualGroup) -> list[list[str]]:
    """找出所有子群。暴力枚举子集（阶≤24时可行）。"""
    from itertools import combinations

    elems = g.elements
    subgroups = []

    # 子群的阶必须整除群的阶（Lagrange）
    divisors = [d for d in range(1, g.order + 1) if g.order % d == 0]

    for d in divisors:
        for subset in combinations(elems, d):
            subset_set = set(subset)
            if g.identity not in subset_set:
                continue
            # 检查封闭性
            is_closed = True
            for a in subset:
                for b in subset:
                    if g.multiplication_table[(a, b)] not in subset_set:
                        is_closed = False
                        break
                if not is_closed:
                    break
            if is_closed:
                # 去重（排序后比较）
                sorted_sub = sorted(subset)
                if sorted_sub not in [sorted(s) for s in subgroups]:
                    subgroups.append(list(subset))

    return subgroups


def is_normal_subgroup(g: VirtualGroup, h: list[str]) -> bool:
    """判断H是否是G的正规子群。"""
    h_set = set(h)
    for g_elem in g.elements:
        for h_elem in h:
            # g * h * g^(-1)
            g_inv = g.inverse(g_elem)
            conj = g.mult(g.mult(g_elem, h_elem), g_inv)
            if conj not in h_set:
                return False
    return True


def find_center(g: VirtualGroup) -> list[str]:
    """求群的中心 Z(G) = {z ∈ G : ∀g, zg = gz}。"""
    center = []
    for z in g.elements:
        commutes = True
        for x in g.elements:
            if g.mult(z, x) != g.mult(x, z):
                commutes = False
                break
        if commutes:
            center.append(z)
    return center


def find_conjugacy_classes(g: VirtualGroup) -> list[list[str]]:
    """求共轭类。"""
    classes = []
    classified = set()

    for a in g.elements:
        if a in classified:
            continue
        # 计算a的共轭类
        conj_class = set()
        for x in g.elements:
            x_inv = g.inverse(x)
            conj = g.mult(g.mult(x, a), x_inv)
            conj_class.add(conj)
        classes.append(sorted(conj_class))
        classified.update(conj_class)

    return classes


def is_cyclic(g: VirtualGroup) -> bool:
    """判断群是否是循环群——寻找生成元。"""
    for a in g.elements:
        if a == g.identity:
            continue
        # 检查a是否生成整个群
        generated = {g.identity, a}
        current = a
        for _ in range(g.order - 1):
            current = g.mult(current, a)
            generated.add(current)
            if len(generated) == g.order:
                return True
    return False


def find_generators(g: VirtualGroup) -> list[str]:
    """找出所有生成元（如果是循环群）。"""
    gens = []
    for a in g.elements:
        if a == g.identity:
            continue
        generated = {g.identity, a}
        current = a
        for _ in range(g.order - 1):
            current = g.mult(current, a)
            generated.add(current)
            if len(generated) == g.order:
                gens.append(a)
                break
    return gens


def is_abelian(g: VirtualGroup) -> bool:
    """判断群是否是交换群。"""
    for a in g.elements:
        for b in g.elements:
            if g.mult(a, b) != g.mult(b, a):
                return False
    return True


# ============================================================
# 主函数：生成+验证+保存
# ============================================================

def main():
    import os

    print("=== POC-VMS-0: 虚拟群生成器 ===")

    # 生成100个虚拟群
    print("生成100个虚拟群...")
    groups = generate_batch(count=100, seed=42)

    # 统计
    type_counts = {}
    order_counts = {}
    for g in groups:
        type_counts[g.group_type] = type_counts.get(g.group_type, 0) + 1
        order_counts[g.order] = order_counts.get(g.order, 0) + 1

    print(f"\n群类型分布: {type_counts}")
    print(f"阶分布: {order_counts}")

    # 保存
    output_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'runs', 'vms_poc_0')
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, 'virtual_groups.json')
    with open(output_path, 'w') as f:
        json.dump([g.to_dict() for g in groups], f, ensure_ascii=False, indent=2)
    print(f"\n已保存到 {output_path}")

    # 打印前3个群的乘法表作为示例
    for g in groups[:3]:
        print(f"\n--- {g.gid} ({g.group_type}, order={g.order}) ---")
        print(f"元素: {g.elements}")
        print(f"乘法表:")
        header = "  * | " + " ".join(f"{e:>3}" for e in g.elements)
        print(header)
        print("  --+" + "-" * (len(header) - 3))
        for a in g.elements:
            row = f"  {a:>3} | " + " ".join(f"{g.mult(a, b):>3}" for b in g.elements)
            print(row)
        # 性质
        print(f"  交换群: {is_abelian(g)}")
        print(f"  循环群: {is_cyclic(g)}")
        print(f"  中心: {find_center(g)}")
        print(f"  共轭类: {find_conjugacy_classes(g)}")
        subs = find_subgroups(g)
        print(f"  子群({len(subs)}个): {subs}")

    print(f"\n=== 生成完成：{len(groups)}个虚拟群，全部通过群公理验证 ===")


if __name__ == '__main__':
    import itertools
    main()
