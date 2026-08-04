#!/usr/bin/env python3
"""batch_extractor.py —— 批量L1/L2/L3提取调度器

给定一批题目（题面+领域），调度subagent做三层提取：
  1. 每题一个subagent做L1提取（2-3种解法路径）
  2. 一个subagent批量做L2提取（从L1抽象思维模式）
  3. 一个subagent批量做L3提取（从多个L2综合范式思维）
  4. 格式化为标准JSON

用法：
  python3 batch_extractor.py --input problems_to_extract.json --output extracted.json
"""
import sys
import os
import json
import argparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def generate_extraction_prompt(problems):
    """生成给subagent的提取提示"""
    lines = []
    lines.append("你是一个数学三层提取AI。请对以下定理做三层提取（L1/L2/L3），输出为标准JSON格式。")
    lines.append("")
    lines.append(f"共{len(problems)}道定理：")
    lines.append("")
    for i, p in enumerate(problems):
        lines.append(f"{i+1}. **{p['title']}**：{p['statement']}")
        if p.get('methods'):
            lines.append(f"   解法提示：{', '.join(p['methods'])}")
        lines.append(f"   领域：{', '.join(p.get('domain', []))}")
    lines.append("")
    lines.append("对每道定理，提取：")
    lines.append("- L1：2-3种解法路径（每种4-7步，每步标注concept和action）")
    lines.append("- L2：从L1中抽象出的思维模式（标注evidence_step和applicable_domains，至少覆盖2个领域）")
    lines.append("- L3：范式级思维（必须改变图结构，连接不同领域，不是元思维模式）")
    lines.append("- cross_domain_edges：跨领域映射边")
    lines.append("")
    lines.append("输出格式为JSON数组，problem_id从指定编号开始，结构与Phase A相同。")
    lines.append("")
    lines.append("注意：")
    lines.append("- L2必须是弥漫性思维模式（在多个领域可调用），不是某题专属技巧")
    lines.append("- L3必须是具体范式（改变图结构，连接不同领域），不是元思维模式")
    lines.append("- 每道题至少2种解法")
    lines.append("")
    lines.append("把结果写入指定输出文件。")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="批量L1/L2/L3提取调度器")
    parser.add_argument("--input", required=True, help="待提取题目JSON文件")
    parser.add_argument("--output", required=True, help="输出文件路径")
    parser.add_argument("--start-id", type=int, default=1, help="起始problem_id编号")
    args = parser.parse_args()

    with open(args.input, 'r') as f:
        problems = json.load(f)

    # 给每道题加problem_id
    for i, p in enumerate(problems):
        p['problem_id'] = f"MATH-{args.start_id + i:03d}"

    prompt = generate_extraction_prompt(problems)
    print(f"生成提取提示：{len(problems)}道题")
    print(f"输出文件：{args.output}")
    print(f"提示长度：{len(prompt)}字符")
    print()
    print("提示内容预览（前500字符）：")
    print(prompt[:500])
    print("...")
    print()
    print("使用方法：把上面的提示发给subagent，让它做三层提取并写入输出文件。")
    print(f"命令示例：run_subagent(task='''{prompt[:200]}...''', output='{args.output}')")

    # 保存提示到文件供使用
    prompt_file = args.output.replace('.json', '_prompt.txt')
    with open(prompt_file, 'w') as f:
        f.write(prompt)
    print(f"\n完整提示已保存到：{prompt_file}")


if __name__ == "__main__":
    main()
