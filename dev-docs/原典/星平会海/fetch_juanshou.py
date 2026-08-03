#!/usr/bin/env python3
"""
补抓星平会海卷首（book/1422-1439）和卷一缺失篇目（book/1440-1443）。
复用 fetch_v3.py 的 curl + extract 模式。
"""
import os, re, subprocess, time, json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(BASE_DIR, "raw_卷首")
os.makedirs(RAW_DIR, exist_ok=True)

# 卷首：1422-1439，卷一缺失：1440-1443
BOOK_IDS = list(range(1422, 1444))

DELAY = 1.0  # 礼貌延迟

def curl_fetch(url):
    try:
        r = subprocess.run(
            ["curl", "-s", "-L", "--max-time", "15",
             "-H", "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
             url],
            capture_output=True, text=True, timeout=20
        )
        return r.stdout if r.returncode == 0 else ""
    except:
        return ""

def extract_article(html):
    """Extract text from <article> tag."""
    m = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
    if not m:
        return ""
    art = m.group(1)
    art = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', art, flags=re.DOTALL)
    art = re.sub(r'<[^>]+>', '\n', art)
    art = art.replace('&nbsp;', ' ').replace('&lt;', '<').replace('&gt;', '>')
    art = art.replace('&amp;', '&').replace('&quot;', '"').replace('&#8230;', '…')
    lines = [l.strip() for l in art.split('\n') if l.strip()]
    return '\n'.join(lines)

def find_max_page(html):
    pages = re.findall(r'/book/(\d+)_(\d+)\.html', html)
    if pages:
        return max(int(p) for _, p in pages)
    return 1

def extract_title(html):
    m = re.search(r'<title>(.*?)</title>', html)
    if m:
        return m.group(1).replace('-星平会海-算准网', '').strip()
    m = re.search(r'<h1[^>]*>(.*?)</h1>', html)
    if m:
        return re.sub(r'<[^>]+>', '', m.group(1)).strip()
    return ""

def main():
    print(f"补抓 {len(BOOK_IDS)} 个页面 (book/{BOOK_IDS[0]}-{BOOK_IDS[-1]})")
    print(f"输出目录: {RAW_DIR}\n")

    results = []
    for bid in BOOK_IDS:
        url = f"https://www.suanzhun.net/book/{bid}.html"
        html = curl_fetch(url)
        if not html or len(html) < 200:
            print(f"  [{bid}] FAIL (空响应)")
            results.append({"id": bid, "status": "fail"})
            time.sleep(DELAY)
            continue

        title = extract_title(html)
        max_page = find_max_page(html)
        text = extract_article(html)

        if text and len(text) > 30:
            fn = f"{bid}.txt"
            fp = os.path.join(RAW_DIR, fn)
            with open(fp, "w", encoding="utf-8") as f:
                f.write(f"Title: {title}\nURL: {url}\n\n{text}")
            preview = text[:60].replace('\n', ' ')
            print(f"  [{bid}] OK p1/{max_page} ({len(text)}c): {preview}...")
            results.append({"id": bid, "title": title, "status": "ok", "max_page": max_page})
        else:
            print(f"  [{bid}] EMPTY (title={title})")
            results.append({"id": bid, "title": title, "status": "empty"})

        # 抓分页
        for p in range(2, max_page + 1):
            time.sleep(DELAY)
            purl = f"https://www.suanzhun.net/book/{bid}_{p}.html"
            phtml = curl_fetch(purl)
            if phtml:
                ptext = extract_article(phtml)
                if ptext and len(ptext) > 30:
                    fn = f"{bid}_{p}.txt"
                    fp = os.path.join(RAW_DIR, fn)
                    with open(fp, "w", encoding="utf-8") as f:
                        f.write(f"Title: {title} (p{p})\nURL: {purl}\n\n{ptext}")
                    print(f"  [{bid}] p{p} OK ({len(ptext)}c)")
                else:
                    print(f"  [{bid}] p{p} EMPTY")
            else:
                print(f"  [{bid}] p{p} FAIL")

        time.sleep(DELAY)

    # 保存元数据
    meta_path = os.path.join(RAW_DIR, "fetch_meta.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    ok_count = sum(1 for r in results if r["status"] == "ok")
    print(f"\n完成: {ok_count}/{len(BOOK_IDS)} 成功")
    print(f"元数据: {meta_path}")

if __name__ == "__main__":
    main()
