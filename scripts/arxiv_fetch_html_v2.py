#!/usr/bin/env python3
"""
arXiv HTML full text fetcher v2.
- Reads from exhaustive metadata (239K papers, 44 categories)
- Fetches 10 most recent papers per category (vs 3 in v1)
- Covers ALL 44 categories including cs theory, quant-ph, math-ph, hep-th, nlin
- Skips papers already fetched in v1
"""
import urllib.request
import urllib.parse
import json
import re
import os
import sys
import time
from html.parser import HTMLParser

class HTMLToText(HTMLParser):
    """Simple HTML to text converter."""
    def __init__(self):
        super().__init__()
        self.result = []
        self.skip = False
        self.tag_stack = []
    
    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag)
        if tag in ("script", "style", "nav", "header", "footer"):
            self.skip = True
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.result.append("\n\n## ")
        elif tag == "p":
            self.result.append("\n\n")
        elif tag == "br":
            self.result.append("\n")
        elif tag == "li":
            self.result.append("\n- ")
    
    def handle_endtag(self, tag):
        if tag in ("script", "style", "nav", "header", "footer"):
            self.skip = False
        if self.tag_stack and self.tag_stack[-1] == tag:
            self.tag_stack.pop()
    
    def handle_data(self, data):
        if not self.skip:
            text = data.strip()
            if text:
                self.result.append(text)
    
    def get_text(self):
        text = "".join(self.result)
        text = re.sub(r'\n{4,}', '\n\n\n', text)
        text = re.sub(r' {2,}', ' ', text)
        return text.strip()


def fetch_html(arxiv_id, retries=3):
    """Fetch HTML content from arxiv.org/html/<id>."""
    url = f"https://arxiv.org/html/{arxiv_id}"
    
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "MathMasterSystem/1.0 (research collection)"
            })
            with urllib.request.urlopen(req, timeout=30) as resp:
                html = resp.read().decode("utf-8", errors="replace")
            return html
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = 60 * (attempt + 1)
                print(f"  429, waiting {wait}s", file=sys.stderr)
                time.sleep(wait)
            else:
                return None
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(5 * (attempt + 1))
    return None


def html_to_markdown(html, paper_meta):
    """Convert HTML to markdown."""
    parser = HTMLToText()
    try:
        parser.feed(html)
    except Exception:
        pass
    text = parser.get_text()
    
    md = f"# {paper_meta['title']}\n\n"
    md += f"**arXiv ID**: {paper_meta['arxiv_id']}\n"
    md += f"**Authors**: {', '.join(paper_meta['authors'])}\n"
    md += f"**Published**: {paper_meta['published'][:10]}\n"
    md += f"**Categories**: {', '.join(paper_meta['all_categories'])}\n"
    if paper_meta.get('comment'):
        md += f"**Comments**: {paper_meta['comment']}\n"
    if paper_meta.get('doi'):
        md += f"**DOI**: {paper_meta['doi']}\n"
    md += f"**HTML URL**: https://arxiv.org/html/{paper_meta['arxiv_id']}\n\n"
    md += f"## Abstract\n\n{paper_meta['abstract']}\n\n"
    md += f"## Full Text\n\n{text}\n"
    
    return md


def main():
    metadata_path = "/data/master-mind/knowledge/arxiv/metadata_all_2023plus.json"
    output_dir = "/data/master-mind/knowledge/arxiv/fulltext"
    os.makedirs(output_dir, exist_ok=True)
    
    # Load metadata
    print("Loading metadata...", file=sys.stderr)
    with open(metadata_path) as f:
        all_papers = json.load(f)
    print(f"Loaded {len(all_papers)} papers", file=sys.stderr)
    
    # Group by primary category
    by_cat = {}
    for p in all_papers:
        cat = p["primary_category"]
        if cat not in by_cat:
            by_cat[cat] = []
        by_cat[cat].append(p)
    
    # Sort each category by published date (newest first)
    for cat in by_cat:
        by_cat[cat].sort(key=lambda x: x["published"], reverse=True)
    
    # Find existing files to skip
    existing_ids = set()
    for f in os.listdir(output_dir):
        if f.endswith(".md"):
            # Extract arxiv_id from filename: cat_XXXX_XXXXXX.md
            parts = f.replace(".md", "").split("_")
            # Last two parts are the id (e.g. 2608_02568)
            if len(parts) >= 2:
                arxiv_id = parts[-2] + "." + parts[-1]
                existing_ids.add(arxiv_id)
    
    print(f"Already fetched: {len(existing_ids)} papers", file=sys.stderr)
    
    # Select papers: 10 per category, newest first, skip existing
    papers_per_category = 10
    selected = []
    
    for cat in sorted(by_cat.keys()):
        cat_papers = by_cat[cat]
        count = 0
        for p in cat_papers:
            clean_id = p["arxiv_id"].split("v")[0] if "v" in p["arxiv_id"][-3:] else p["arxiv_id"]
            if clean_id in existing_ids:
                continue
            selected.append(p)
            count += 1
            if count >= papers_per_category:
                break
    
    print(f"Selected {len(selected)} papers for full text fetch", file=sys.stderr)
    
    success = 0
    failed = 0
    
    for i, paper in enumerate(selected):
        arxiv_id = paper["arxiv_id"]
        clean_id = arxiv_id.split("v")[0] if "v" in arxiv_id[-3:] else arxiv_id
        cat = paper["primary_category"].replace(".", "_")
        filename = f"{cat}_{clean_id.replace('.', '_')}.md"
        filepath = os.path.join(output_dir, filename)
        
        if os.path.exists(filepath):
            success += 1
            continue
        
        print(f"[{i+1}/{len(selected)}] Fetching: {arxiv_id} ({paper['primary_category']})", file=sys.stderr)
        
        html = fetch_html(arxiv_id)
        if html is None or len(html) < 500:
            print(f"  FAILED: {arxiv_id}", file=sys.stderr)
            failed += 1
            time.sleep(3)
            continue
        
        md = html_to_markdown(html, paper)
        
        with open(filepath, "w") as f:
            f.write(md)
        
        lines = md.count("\n")
        print(f"  OK: {len(md)} chars, {lines} lines", file=sys.stderr)
        success += 1
        
        # Rate limit
        time.sleep(3)
    
    print(f"\n=== Done: {success} success, {failed} failed ===", file=sys.stderr)
    
    # Final stats
    total_files = len([f for f in os.listdir(output_dir) if f.endswith(".md")])
    total_lines = sum(1 for f in os.listdir(output_dir) if f.endswith(".md") for line in open(os.path.join(output_dir, f)))
    print(f"Total fulltext files: {total_files}", file=sys.stderr)
    print(f"Total lines: {total_lines}", file=sys.stderr)


if __name__ == "__main__":
    main()
