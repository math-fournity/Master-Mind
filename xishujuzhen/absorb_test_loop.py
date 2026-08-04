#!/usr/bin/env python3
"""absorb_test_loop.py —— 大规模"吸收-测试"自动化Loop主控

按"渐进积累、迭代测试"原则，分批吸收数学知识进依赖图：
  1. 选题：从待吸收队列中取一批
  2. 提取：调度subagent做L1/L2/L3三层提取
  3. 导入：导入ArangoDB
  4. 测试：跑6项依赖图测试
  5. 判定：全通过→继续；有失败→停止

用法：
  python3 absorb_test_loop.py --batch 1   # 跑第1批
  python3 absorb_test_loop.py --status    # 查看当前状态
"""
import sys
import os
import json
import argparse
import subprocess

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 批次定义
BATCHES = {
    1: {
        "name": "代数（群论+环论+线性代数深化）",
        "domain": ["algebra"],
        "start_id": 16,
        "problems": [
            {"title": "Sylow第一定理", "statement": "若G是有限群，p^k整除|G|且p^(k+1)不整除|G|，则G有p^k阶子群", "domain": ["algebra", "group_theory"], "methods": ["群作用证明", "归纳证明", "置换群证明"]},
            {"title": "群同构基本定理", "statement": "若φ:G→H是满同态，则G/ker(φ)≅H", "domain": ["algebra", "group_theory"], "methods": ["直接构造", "商群定义"]},
            {"title": "Jordan标准型存在性", "statement": "复数域上任何方阵相似于Jordan矩阵", "domain": ["linear_algebra", "algebra"], "methods": ["不变子空间分解", "模论方法", "λ矩阵方法"]},
            {"title": "Hilbert基定理", "statement": "若R是Noether环，则R[x]也是Noether环", "domain": ["algebra", "commutative_algebra"], "methods": ["理想生成元", "Groebner基"]},
            {"title": "线性无关与基", "statement": "向量空间中任意线性无关集可扩充为基", "domain": ["linear_algebra", "algebra"], "methods": ["Zorn引理", "逐次扩充"]},
            {"title": "环的理想与商环", "statement": "若I是环R的理想，则R/I是环且自然映射是满同态", "domain": ["algebra", "ring_theory"], "methods": ["直接验证", "同态基本定理"]},
            {"title": "线性映射的秩-零度定理", "statement": "dim(ker T) + dim(im T) = dim V", "domain": ["linear_algebra", "algebra"], "methods": ["基扩充", "正交分解"]},
            {"title": "矩阵的可对角化判定", "statement": "A可对角化⟺ A有n个线性无关特征向量⟺ 最小多项式无重根", "domain": ["linear_algebra", "algebra"], "methods": ["特征多项式", "不变子空间", "最小多项式"]},
            {"title": "中国剩余定理（环论版）", "statement": "若I_1,...,I_k是环R的两两互素理想，则R/∩I_i≅∏R/I_i", "domain": ["algebra", "ring_theory"], "methods": ["同态构造", "投影映射"]},
            {"title": "对称多项式基本定理", "statement": "每个对称多项式可唯一表为初等对称多项式的多项式", "domain": ["algebra"], "methods": ["归纳构造", "字典序消元"]},
            {"title": "Cauchy定理（群论）", "statement": "若素数p整除|G|，则G中有p阶元素", "domain": ["algebra", "group_theory"], "methods": ["Sylow定理推论", "群作用", "归纳"]},
            {"title": "有限生成Abel群结构定理", "statement": "有限生成Abel群≅Z^r × Z/n1 × ... × Z/nk", "domain": ["algebra", "group_theory"], "methods": ["矩阵初等变换", "模论", "归纳"]},
            {"title": "行列式的乘性", "statement": "det(AB)=det(A)det(B)", "domain": ["linear_algebra", "algebra"], "methods": ["置换展开", "多重线性", "体积论证"]},
            {"title": "正定矩阵的判定", "statement": "实对称矩阵A正定⟺ 所有特征值为正⟺ 所有顺序主子式为正", "domain": ["linear_algebra", "algebra"], "methods": ["谱定理", "Sylvester准则", "Cholesky分解"]},
            {"title": "Noether环的等价条件", "statement": "R是Noether环⟺ 每个理想有限生成⟺ 升链条件", "domain": ["algebra", "commutative_algebra"], "methods": ["等价证明", "反证"]},
        ]
    },
    2: {
        "name": "数论（解析+代数）",
        "domain": ["number_theory"],
        "start_id": 31,
        "problems": [
            {"title": "Dirichlet定理", "statement": "若gcd(a,q)=1，则等差数列a, a+q, a+2q,...中有无穷多个素数", "domain": ["number_theory", "analytic_number_theory"], "methods": ["L函数", "解析延拓", "特征标"]},
            {"title": "素数定理", "statement": "π(x)~x/ln(x)", "domain": ["number_theory", "analytic_number_theory"], "methods": ["复分析", "Tauberian定理", "初等证明"]},
            {"title": "二次互反律", "statement": "(p/q)(q/p)=(-1)^((p-1)(q-1)/4)", "domain": ["number_theory", "algebra"], "methods": ["Gauss引理", "Eisenstein几何", "域论"]},
            {"title": "Fermat三平方定理", "statement": "n是三平方和⟺ n≠4^a(8b+7)", "domain": ["number_theory"], "methods": ["局部-全局", "恒等式构造", "Minkowski"]},
            {"title": "Dirichlet逼近定理", "statement": "对任意无理数α，存在无穷多p/q使|α-p/q|<1/q²", "domain": ["number_theory", "analysis"], "methods": ["鸽巢原理", "连分数", "Minkowski"]},
            {"title": "Pell方程", "statement": "x²-Dy²=1有正整数解（D非完全平方）", "domain": ["number_theory", "algebra"], "methods": ["连分数", "二次域单位群", "归纳"]},
            {"title": "算术基本定理", "statement": "每个正整数唯一分解为素数乘积", "domain": ["number_theory", "algebra"], "methods": ["Euclid引理", "归纳", "理想论"]},
            {"title": "Fermat大定理n=4", "statement": "x⁴+y⁴=z⁴无正整数解", "domain": ["number_theory"], "methods": ["无穷递降", "Fermat方法", "椭圆曲线"]},
            {"title": "Mersenne素数性质", "statement": "若2^p-1是素数则p是素数", "domain": ["number_theory"], "methods": ["反证", "代数恒等式"]},
            {"title": "模p的乘法群循环", "statement": "(Z/pZ)*是循环群（p素数）", "domain": ["number_theory", "algebra", "group_theory"], "methods": ["元素阶", "多项式根", "生成元构造"]},
            {"title": "Euler定理", "statement": "a^φ(n)≡1(mod n)（gcd(a,n)=1）", "domain": ["number_theory", "group_theory"], "methods": ["群论", "归纳", "Euler函数"]},
            {"title": "Fermat二平方补完", "statement": "n是两平方和⟺ n的4k+3型素因子都有偶指数", "domain": ["number_theory", "algebra"], "methods": ["Z[i]唯一分解", "局部-全局", "恒等式"]},
            {"title": "Quadratic Reciprocity的补充定律", "statement": "(-1/p)=(-1)^((p-1)/2), (2/p)=(-1)^((p²-1)/8)", "domain": ["number_theory"], "methods": ["Gauss引理", "Euler判别"]},
            {"title": "Liouville数（超越数构造）", "statement": "Σ10^(-n!)是超越数", "domain": ["number_theory", "analysis"], "methods": ["逼近下界", "构造反例"]},
            {"title": "素数无穷多个（Dirichlet特例q=1）", "statement": "素数有无穷多个——解析证明", "domain": ["number_theory", "analysis"], "methods": ["Euler乘积", "zeta函数", "反证"]},
        ]
    },
    3: {
        "name": "分析（实+复+调和+泛函）",
        "domain": ["analysis"],
        "start_id": 46,
        "problems": [
            {"title": "Heine-Borel定理", "statement": "R^n中集合紧致⟺ 有界闭", "domain": ["analysis", "topology"], "methods": ["有限覆盖", "序列紧致", "二分法"]},
            {"title": "Stone-Weierstrass定理", "statement": "C(X)中含常数且分离点的子代数稠密", "domain": ["analysis"], "methods": ["逼近论", "Weierstrass", "格理论"]},
            {"title": "开映射定理", "statement": "Banach空间间的有界线性满射是开映射", "domain": ["analysis", "functional_analysis"], "methods": ["Baire纲", "逆算子", "级数展开"]},
            {"title": "Hahn-Banach定理", "statement": "子空间上的有界线性泛函可保范延拓", "domain": ["analysis", "functional_analysis"], "methods": ["Zorn引理", "超滤子", "凸分析"]},
            {"title": "Riesz表示定理", "statement": "Hilbert空间上有界线性泛函=v·", "domain": ["analysis", "functional_analysis"], "methods": ["正交分解", "Riesz引理"]},
            {"title": "Lebesgue控制收敛定理", "statement": "若f_n→f a.e.且|f_n|≤g可积，则∫f_n→∫f", "domain": ["analysis", "measure_theory"], "methods": ["Fatou引理", "Egorov定理", "控制函数"]},
            {"title": "Fubini定理", "statement": "可积函数的重积分可交换积分顺序", "domain": ["analysis", "measure_theory"], "methods": ["σ-代数", "Tonelli", "绝对连续"]},
            {"title": "Cauchy积分公式", "statement": "f(z₀)=(1/2πi)∮f(z)/(z-z₀)dz", "domain": ["analysis", "complex_analysis"], "methods": ["留数", "Cauchy定理", "级数"]},
            {"title": "最大模原理", "statement": "非常数全纯函数的模在内部不取最大值", "domain": ["analysis", "complex_analysis"], "methods": ["调和函数", "开映射", "反证"]},
            {"title": "留数定理", "statement": "∮f(z)dz=2πi·ΣRes(f,z_k)", "domain": ["analysis", "complex_analysis"], "methods": ["Laurent展开", "Cauchy公式", "形变"]},
            {"title": "Phragmén-Lindelöf原理", "statement": "带扇形增长限制的全纯函数最大模原理", "domain": ["analysis", "complex_analysis"], "methods": ["辅助函数", "比较原理"]},
            {"title": "Plancherel定理", "statement": "Fourier变换是L²上的等距同构", "domain": ["analysis", "harmonic_analysis"], "methods": ["稠密性", "卷积逼近", "Parseval"]},
            {"title": "Poisson求和公式", "statement": "Σf(n)=Σf̂(n)（适当条件下）", "domain": ["analysis", "harmonic_analysis"], "methods": ["Fourier级数", "分布理论", "Poisson核"]},
            {"title": "闭图像定理", "statement": "Banach空间间线性算子有界⟺ 图像闭", "domain": ["analysis", "functional_analysis"], "methods": ["开映射定理", "投影", "Baire纲"]},
            {"title": "Arzelà-Ascoli定理", "statement": "函数族紧致⟺ 一致有界+等度连续", "domain": ["analysis", "topology"], "methods": ["对角线法", "紧致性", "等度连续"]},
        ]
    },
    # Batch 4-8 待定义——拓扑/几何/组合/逻辑/概率
}


def run_batch(batch_id):
    """运行一批吸收-测试"""
    batch = BATCHES.get(batch_id)
    if not batch:
        print(f"批次{batch_id}未定义")
        return False

    print(f"\n{'='*60}")
    print(f"批次{batch_id}: {batch['name']}")
    print(f"{'='*60}")
    print(f"题目数: {len(batch['problems'])}")
    print(f"起始ID: MATH-{batch['start_id']:03d}")

    # 保存题目清单
    batch_file = f"poc/poc3/batch_{batch_id}_input.json"
    with open(batch_file, 'w') as f:
        json.dump(batch['problems'], f, ensure_ascii=False, indent=2)
    print(f"题目清单保存到: {batch_file}")

    # 生成提取提示
    from batch_extractor import generate_extraction_prompt
    prompt = generate_extraction_prompt(batch['problems'])
    prompt_file = f"poc/poc3/batch_{batch_id}_prompt.txt"
    with open(prompt_file, 'w') as f:
        f.write(prompt)
    print(f"提取提示保存到: {prompt_file}")

    print(f"\n下一步：")
    print(f"1. 用subagent执行三层提取（提示文件: {prompt_file}）")
    print(f"2. 输出文件: poc/poc3/batch_{batch_id}_output.json")
    print(f"3. 导入ArangoDB")
    print(f"4. 跑测试: python3 test_dependency_graph.py")

    return True


def show_status():
    """显示当前状态"""
    from cognition_sdk_math import CognitionSDK
    sdk = CognitionSDK()

    n_nodes = list(sdk.db.aql.execute('RETURN COUNT(dg_nodes)'))[0]
    n_edges = list(sdk.db.aql.execute('RETURN COUNT(dg_edges)'))[0]
    n_problems = list(sdk.db.aql.execute('RETURN COUNT(problems)'))[0]
    n_solutions = list(sdk.db.aql.execute('RETURN COUNT(solutions)'))[0]
    n_cog = list(sdk.db.aql.execute('RETURN COUNT(cognition_units)'))[0]

    domains = list(sdk.db.aql.execute(
        'FOR n IN dg_nodes FILTER n.type=="concept" COLLECT d=n.domain WITH COUNT INTO c SORT c DESC RETURN {domain:d, count:c}'))

    print(f"\n{'='*60}")
    print(f"依赖图当前状态")
    print(f"{'='*60}")
    print(f"题库: {n_problems}道题, {n_solutions}个解法")
    print(f"依赖图: {n_nodes}节点, {n_edges}边")
    print(f"认知图: {n_cog}个认知单元")
    print(f"\n领域覆盖:")
    for d in domains:
        if d['domain']:
            print(f"  {d['domain']}: {d['count']}个concept")

    print(f"\n批次进度:")
    for bid, batch in sorted(BATCHES.items()):
        # 检查这批的题目是否已在problems中
        start = batch['start_id']
        count = len(batch['problems'])
        existing = list(sdk.db.aql.execute(
            'FOR p IN problems FILTER p.problem_id >= @start AND p.problem_id < @end RETURN p.problem_id',
            bind_vars={"start": f"MATH-{start:03d}", "end": f"MATH-{start+count:03d}"}))
        status = "✅ 完成" if len(existing) == count else f"⏳ {len(existing)}/{count}"
        print(f"  Batch {bid}: {batch['name']} - {status}")


def main():
    parser = argparse.ArgumentParser(description="大规模吸收-测试自动化Loop主控")
    parser.add_argument("--batch", type=int, help="运行指定批次")
    parser.add_argument("--status", action="store_true", help="显示当前状态")
    args = parser.parse_args()

    if args.status:
        show_status()
    elif args.batch:
        run_batch(args.batch)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
