#!/usr/bin/env python3
"""
Fetch arXiv HTML full text for selected papers and save as markdown.
Uses arxiv.org/html/<id> endpoint (free HTML rendering).
Selects papers across all categories for broad coverage.
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
        self.in_math = False
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
        elif tag == "a":
            pass  # ignore links
        elif tag in ("math", "mathml"):
            self.in_math = True
    
    def handle_endtag(self, tag):
        if tag in ("script", "style", "nav", "header", "footer"):
            self.skip = False
        if self.tag_stack and self.tag_stack[-1] == tag:
            self.tag_stack.pop()
        if tag in ("math", "mathml"):
            self.in_math = False
    
    def handle_data(self, data):
        if not self.skip:
            # Preserve math content
            text = data.strip()
            if text:
                self.result.append(text)
    
    def get_text(self):
        text = "".join(self.result)
        # Clean up excessive whitespace
        text = re.sub(r'\n{4,}', '\n\n\n', text)
        text = re.sub(r' {2,}', ' ', text)
        return text.strip()


def fetch_html(arxiv_id):
    """Fetch HTML content from arxiv.org/html/<id>."""
    # arxiv_id may have version suffix like 2608.02568v1
    # HTML URL format: https://arxiv.org/html/<id>
    url = f"https://arxiv.org/html/{arxiv_id}"
    
    req = urllib.request.Request(url, headers={
        "User-Agent": "MathMasterSystem/1.0 (research collection; mailto:research@example.com)"
    })
    
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", errors="replace")
        return html
    except Exception as e:
        return None


def html_to_markdown(html, paper_meta):
    """Convert HTML to markdown, preserving structure."""
    parser = HTMLToText()
    try:
        parser.feed(html)
    except Exception:
        pass
    text = parser.get_text()
    
    # Build markdown document
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


def select_papers(metadata_path, papers_per_category=3):
    """Select papers across categories for full text fetch."""
    with open(metadata_path) as f:
        papers = json.load(f)
    
    # Group by primary category
    by_cat = {}
    for p in papers:
        cat = p["primary_category"]
        if cat not in by_cat:
            by_cat[cat] = []
        by_cat[cat].append(p)
    
    # Select top N from each math category
    selected = []
    math_cats = [c for c in by_cat if c.startswith("math.")]
    
    for cat in sorted(math_cats):
        cat_papers = by_cat[cat]
        # Take the first N (most recent, since sorted by date)
        for p in cat_papers[:papers_per_category]:
            selected.append(p)
    
    return selected


def main():
    metadata_path = "/data/master-mind/knowledge/arxiv/metadata_2023_2026.json"
    output_dir = "/data/master-mind/knowledge/arxiv/fulltext"
    os.makedirs(output_dir, exist_ok=True)
    
    # Select papers
    selected = select_papers(metadata_path, papers_per_category=3)
    print(f"Selected {len(selected)} papers for full text fetch", file=sys.stderr)
    
    success = 0
    failed = 0
    
    for i, paper in enumerate(selected):
        arxiv_id = paper["arxiv_id"]
        # Clean ID for filename (remove version suffix for filename)
        clean_id = arxiv_id.split("v")[0] if "v" in arxiv_id[-3:] else arxiv_id
        cat = paper["primary_category"].replace(".", "_")
        filename = f"{cat}_{clean_id.replace('.', '_')}.md"
        filepath = os.path.join(output_dir, filename)
        
        if os.path.exists(filepath):
            print(f"[{i+1}/{len(selected)}] SKIP (exists): {arxiv_id}", file=sys.stderr)
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
        
        # Rate limit: 3 seconds between requests
        time.sleep(3)
    
    print(f"\n=== Done: {success} success, {failed} failed ===", file=sys.stderr)


if __name__ == "__main__":
    main()
