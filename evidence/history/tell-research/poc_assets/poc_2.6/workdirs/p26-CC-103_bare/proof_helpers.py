#!/usr/bin/env python3
"""
验证关键引理和尝试构造更优雅的证明。
引理：{0,1,2,3,4}的任何3元子集都有间距∈{2,3}
"""
from itertools import combinations
from z3 import *

def la2(p1,p2,p3):
    x1,y1=p1;x2,y2=p2;x3,y3=p3
    return abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))

# 验证引理：5个共线点的任何3元子集有间距∈{2,3}
print("=== 引理验证：{0,1,2,3,4}的3元子集 ===")
for triple in combinations(range(5), 3):
    gaps = [triple[1]-triple[0], triple[2]-triple[1], triple[2]-triple[0]]
    has_23 = any(g in {2,3} for g in gaps)
    print(f"  {triple}: gaps={gaps}, has_gap_2or3={has_23}")

# 验证：7个共线点中，如果某色出现4+次，必有3个间距∈{2,3,6}
print("\n=== 引理2：7个点中4个同色必有间距∈{2,3,6} ===")
count_valid = 0
for quad in combinations(range(7), 4):
    # 检查quad的所有3元子集
    all_avoid = True
    for triple in combinations(quad, 3):
        gaps = [triple[1]-triple[0], triple[2]-triple[1], triple[2]-triple[0]]
        if any(g in {2,3,6} for g in gaps):
            all_avoid = False
            break
    if all_avoid:
        count_valid += 1
        print(f"  4-set {quad}: ALL triples avoid gaps 2,3,6!")
print(f"  4-sets where all triples avoid {{2,3,6}}: {count_valid} / {len(list(combinations(range(7),4)))}")

# 验证：7个点中3个同色且避免间距{2,3,6}的所有配置
print("\n=== 3点避免间距{2,3,6}的配置 ===")
valid_triples = []
for triple in combinations(range(7), 3):
    gaps = [triple[1]-triple[0], triple[2]-triple[1], triple[2]-triple[0]]
    if not any(g in {2,3,6} for g in gaps):
        valid_triples.append(triple)
        print(f"  {triple}: gaps={gaps}")
print(f"  Total valid triples: {len(valid_triples)}")

# 验证：3,3,1分布的唯一配置
print("\n=== 3,3,1分布检查 ===")
for t1 in valid_triples:
    for t2 in valid_triples:
        if set(t1) & set(t2):  # 不相交
            continue
        remaining = set(range(7)) - set(t1) - set(t2)
        if len(remaining) == 1:
            print(f"  {t1} + {t2} + {remaining}")

# 尝试更小的非矩形配置
print("\n=== 尝试非矩形配置 ===")
def check(points):
    pts=list(points);tris=[]
    for i in range(len(pts)):
        for j in range(i+1,len(pts)):
            for k in range(j+1,len(pts)):
                if la2(pts[i],pts[j],pts[k])==6:
                    tris.append((pts[i],pts[j],pts[k]))
    if not tris: return 'NO_TRIS',len(tris)
    s=Solver()
    color={p:Int(f'c{p[0]}_{p[1]}') for p in pts}
    for p in pts: s.add(color[p]>=0,color[p]<=2)
    for t in tris:
        s.add(Not(And(color[t[0]]==color[t[1]],color[t[1]]==color[t[2]])))
    r=s.check()
    return ('UNSAT' if r==unsat else 'SAT'),len(tris)

# 配置1：7x2 + 3x3（列0,3,6 × 行2,3,4）
config1 = [(x,y) for x in range(7) for y in range(2)] + [(x,y) for x in [0,3,6] for y in range(2,5)]
st,nt = check(config1)
print(f"  7x2 + 3x3 (cols 0,3,6): {len(config1)}pts {nt}tris {st}")

# 配置2：7x2 + 列0,2,3,4,6 × 行2,3,4
config2 = [(x,y) for x in range(7) for y in range(2)] + [(x,y) for x in [0,2,3,4,6] for y in range(2,5)]
st,nt = check(config2)
print(f"  7x2 + 5cols: {len(config2)}pts {nt}tris {st}")

# 配置3：7x3 + 列0,3,6 × 行3,4
config3 = [(x,y) for x in range(7) for y in range(3)] + [(x,y) for x in [0,3,6] for y in range(3,5)]
st,nt = check(config3)
print(f"  7x3 + 3cols: {len(config3)}pts {nt}tris {st}")

# 配置4：7x2 + 7x1（行0,1,2但行2只有部分列）
for extra_cols in [range(7), [0,2,3,4,6], [0,3,6], [0,1,3,5,6]]:
    config4 = [(x,y) for x in range(7) for y in range(2)] + [(x,2) for x in extra_cols]
    st,nt = check(config4)
    print(f"  7x2 + cols{list(extra_cols)}@y=2: {len(config4)}pts {nt}tris {st}")

# 配置5：十字形 - 列0,3,6全5行 + 行0,1全7列
config5 = [(x,y) for x in [0,3,6] for y in range(5)] + [(x,y) for x in range(7) for y in range(2) if x not in [0,3,6]]
st,nt = check(config5)
print(f"  Cross (3cols full + 2rows full): {len(config5)}pts {nt}tris {st}")
