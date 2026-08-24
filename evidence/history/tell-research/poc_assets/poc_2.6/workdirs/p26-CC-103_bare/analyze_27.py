#!/usr/bin/env python3
"""
验证27点配置的最小性，并尝试构造基于引理的证明。
"""
from z3 import *
from itertools import combinations

def la2(p1,p2,p3):
    x1,y1=p1;x2,y2=p2;x3,y3=p3
    return abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))

def gen_tris(points):
    pts=list(points);tris=[]
    for i in range(len(pts)):
        for j in range(i+1,len(pts)):
            for k in range(j+1,len(pts)):
                if la2(pts[i],pts[j],pts[k])==6:
                    tris.append((pts[i],pts[j],pts[k]))
    return tris

def check(points):
    tris=gen_tris(points)
    if not tris: return 'NO_TRIS',len(tris)
    s=Solver()
    color={p:Int(f'c{p[0]}_{p[1]}') for p in points}
    for p in points: s.add(color[p]>=0,color[p]<=2)
    for t in tris:
        s.add(Not(And(color[t[0]]==color[t[1]],color[t[1]]==color[t[2]])))
    r=s.check()
    return ('UNSAT' if r==unsat else 'SAT'),len(tris)

# 27点配置
config27 = [(x,y) for x in range(7) for y in range(3)] + [(x,y) for x in [0,3,6] for y in [3,4]]
print(f"27点配置: {len(config27)} points")
st, nt = check(config27)
print(f"  {st}, {nt} triangles")

# 检查最小性
print("\n=== 删除单点 ===")
critical = []
for p in config27:
    sub = [q for q in config27 if q != p]
    st, nt = check(sub)
    if st == 'SAT':
        critical.append(p)
print(f"  Critical points: {len(critical)} / {len(config27)}")
if len(critical) < len(config27):
    print(f"  Non-critical points (can remove): {[p for p in config27 if p not in critical]}")

# 打印27点配置的形状
print("\n=== 配置形状 ===")
for y in range(4, -1, -1):
    row = ""
    for x in range(7):
        if (x,y) in config27:
            row += "X "
        else:
            row += ". "
    print(f"  y={y}: {row}")

# 分析27点配置中的面积-3三角形类型
print("\n=== 三角形类型分析 ===")
tris = gen_tris(config27)
types = {}
for t in tris:
    p1, p2, p3 = t
    # 计算所有边长的平方
    edges = []
    for a, b in [(p1,p2), (p1,p3), (p2,p3)]:
        dx, dy = b[0]-a[0], b[1]-a[1]
        edges.append((abs(dx), abs(dy)))
    edges.sort()
    key = tuple(edges)
    if key not in types:
        types[key] = 0
    types[key] += 1

for key, count in sorted(types.items(), key=lambda x: -x[1]):
    print(f"  边向量{key}: {count}个")

# 尝试更多变体
print("\n=== 27点配置变体 ===")
variants = [
    ("7x3 + cols(0,3,6)@y=3,4", [(x,y) for x in range(7) for y in range(3)] + [(x,y) for x in [0,3,6] for y in [3,4]]),
    ("7x3 + cols(0,2,4,6)@y=3,4", [(x,y) for x in range(7) for y in range(3)] + [(x,y) for x in [0,2,4,6] for y in [3,4]]),
    ("7x3 + cols(0,3,6)@y=3 + cols(0,3,6)@y=4", [(x,y) for x in range(7) for y in range(3)] + [(x,y) for x in [0,3,6] for y in [3,4]]),
    ("7x3 + col0,6@y=3,4", [(x,y) for x in range(7) for y in range(3)] + [(x,y) for x in [0,6] for y in [3,4]]),
    ("7x3 + col3@y=3,4", [(x,y) for x in range(7) for y in range(3)] + [(3,y) for y in [3,4]]),
    ("7x3 + col0@y=3,4 + col6@y=3,4", [(x,y) for x in range(7) for y in range(3)] + [(0,y) for y in [3,4]] + [(6,y) for y in [3,4]]),
]
for name, pts in variants:
    st, nt = check(pts)
    print(f"  {name}: {len(pts)}pts {nt}tris {st}")

# 尝试找到27点配置中更小的UNSAT子集
print("\n=== 27点贪心删点 ===")
current = set(config27)
changed = True
while changed:
    changed = False
    for p in list(current):
        trial = current - {p}
        st, _ = check(list(trial))
        if st == 'UNSAT':
            current = trial
            changed = True
print(f"  最小UNSAT子集: {len(current)} points")
for y in range(4, -1, -1):
    row = ""
    for x in range(7):
        if (x,y) in current:
            row += "X "
        else:
            row += ". "
    print(f"    y={y}: {row}")
sub_tris = gen_tris(list(current))
print(f"  Triangles: {len(sub_tris)}")
