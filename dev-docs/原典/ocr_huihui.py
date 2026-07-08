#!/usr/bin/env python3
"""
七政推步 PDF OCR 脚本
使用 ollama minicpm-v vision 模型对扫描件做 OCR

用法:
  python3 ocr_huihui.py input.pdf output.md [--start 0] [--end 10]

依赖:
  - ollama 服务运行中
  - minicpm-v 模型已拉取
  - PyMuPDF (pip3 install PyMuPDF)
"""

import sys
import os
import time
import json
import base64
import argparse
import subprocess
import fitz  # PyMuPDF


def pdf_page_to_image(pdf_path, page_num, dpi=200, tmp_dir="/tmp"):
    """将 PDF 指定页转为 PNG 图片"""
    doc = fitz.open(pdf_path)
    page = doc[page_num]
    pix = page.get_pixmap(dpi=dpi)
    img_path = os.path.join(tmp_dir, f"ocr_page_{page_num:04d}.png")
    pix.save(img_path)
    doc.close()
    return img_path


def ocr_image_ollama(image_path, model="minicpm-v"):
    """用 ollama vision 模型做 OCR"""
    # 读取图片并 base64 编码
    with open(image_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()

    # 构造 ollama API 请求
    prompt = (
        "请识别这张古籍扫描图片中的所有文字。"
        "这是中文古籍《七政推步》（明代回回历法），竖排繁体。"
        "请按从右到左、从上到下的阅读顺序输出文字。"
        "如果有表格，请保留表格结构（用 | 分隔列，用换行分隔行）。"
        "只输出识别到的文字内容，不要加解释说明。"
    )

    payload = {
        "model": model,
        "prompt": prompt,
        "images": [img_b64],
        "stream": False,
        "options": {
            "temperature": 0.1,  # 低温度，提高一致性
            "num_predict": 2000,
        },
    }

    # 调用 ollama API
    result = subprocess.run(
        ["curl", "-s", "http://localhost:11434/api/generate",
         "-H", "Content-Type: application/json",
         "-d", json.dumps(payload)],
        capture_output=True, text=True, timeout=120
    )

    if result.returncode != 0:
        return f"[OCR ERROR: {result.stderr}]"

    try:
        resp = json.loads(result.stdout)
        return resp.get("response", "[OCR ERROR: no response]")
    except json.JSONDecodeError as e:
        return f"[OCR ERROR: JSON parse failed: {e}]"


def ocr_pdf(pdf_path, output_path, start_page=0, end_page=None, model="minicpm-v"):
    """OCR 整个 PDF"""
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    doc.close()

    if end_page is None:
        end_page = total_pages

    print(f"PDF: {pdf_path}")
    print(f"总页数: {total_pages}, OCR 范围: {start_page+1}-{end_page}")
    print(f"模型: {model}")
    print()

    results = []
    for i in range(start_page, end_page):
        print(f"[{i+1}/{end_page}] 正在 OCR 第 {i+1} 页...", flush=True)
        start = time.time()

        # 转图片
        img_path = pdf_page_to_image(pdf_path, i, dpi=200)

        # OCR
        text = ocr_image_ollama(img_path, model)

        elapsed = time.time() - start
        print(f"  耗时: {elapsed:.1f}s, 识别字符: {len(text)}")

        results.append(f"## 第 {i+1} 页\n\n{text}\n\n---\n")

        # 清理临时图片
        os.unlink(img_path)

    # 写入输出文件
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# OCR 结果: {os.path.basename(pdf_path)}\n\n")
        f.write(f"- 来源: {pdf_path}\n")
        f.write(f"- 页数: {start_page+1}-{end_page}\n")
        f.write(f"- 模型: {model}\n")
        f.write(f"- 时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")
        for r in results:
            f.write(r)

    print(f"\n完成！结果已写入: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="七政推步 PDF OCR")
    parser.add_argument("input", help="输入 PDF 路径")
    parser.add_argument("output", help="输出 Markdown 路径")
    parser.add_argument("--start", type=int, default=0, help="起始页(0-based)")
    parser.add_argument("--end", type=int, default=None, help="结束页(0-based, exclusive)")
    parser.add_argument("--model", default="minicpm-v", help="ollama vision 模型名")
    args = parser.parse_args()

    ocr_pdf(args.input, args.output, args.start, args.end, args.model)
