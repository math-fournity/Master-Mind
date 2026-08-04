#!/usr/bin/env python3
"""
Retry script for categories that failed due to DNS/network errors.
Also handles categories that hit the 10000 API limit or timed out.
Reads which per-category files exist and retries missing ones.
"""
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
import time
import os
import sys

ARXIV_API = "https://export.arxiv.org/api/query"

ALL_CATEGORIES = [
    "math.NT", "math.CO", "math.AG", "math.AT", "math.DG", "math.GT",
    "math.RT", "math.LO", "math.PR", "math.ST", "math.AP", "math.CA",
    "math.FA", "math.OA", "math.HO", "math.KT", "math.RA", "math.SP",
    "math.SG", "math.CV", "math.DS", "math.GN", "math.GR", "math.MG",
    "math.MP", "math.NA", "math.OC", "math.QA",
    "cs.CC", "cs.LO", "cs.FL", "cs.DS", "cs.CG", "cs.GT", "cs.SC",
    "quant-ph", "math-ph", "hep-th",
    "stat.TH", "stat.ML",
    "nlin.CD", "nlin.SI", "nlin.AO", "nlin.PS",
]


def query_arxiv_page(category, start=0, max_results=100, retries=5):
    """Query one page with retry logic and 429 handling."""
    params = {
        "search_query": f"cat:{category}",
        "start": start,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = ARXIV_API + "?" + urllib.parse.urlencode(params)
    
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "MathMasterSystem/1.0 (research collection)"
            })
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = resp.read().decode("utf-8")
            return data
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = 60 * (attempt + 1)  # 60s, 120s, 180s, 240s, 300s
                print(f"  429 rate limited, waiting {wait}s (attempt {attempt+1}/{retries})", file=sys.stderr)
                time.sleep(wait)
            else:
                print(f"  HTTP {e.code}: {e}", file=sys.stderr)
                if attempt < retries - 1:
                    time.sleep(15 * (attempt + 1))
        except Exception as e:
            print(f"  Attempt {attempt+1}/{retries} failed: {e}", file=sys.stderr)
            if attempt < retries - 1:
                time.sleep(15 * (attempt + 1))
    return None


def parse_entries(data):
    """Parse Atom XML entries."""
    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "arxiv": "http://arxiv.org/schemas/atom",
        "opensearch": "http://a9.com/-/spec/opensearch/1.1/",
    }
    root = ET.fromstring(data)
    
    total_results_el = root.find("opensearch:totalResults", ns)
    total_results = int(total_results_el.text) if total_results_el is not None else 0
    
    entries = []
    for entry in root.findall("atom:entry", ns):
        arxiv_id_raw = entry.find("atom:id", ns)
        arxiv_id = arxiv_id_raw.text.split("/abs/")[-1] if arxiv_id_raw is not None else ""
        
        title_el = entry.find("atom:title", ns)
        title = title_el.text.strip().replace("\n", " ") if title_el is not None else ""
        
        summary_el = entry.find("atom:summary", ns)
        abstract = summary_el.text.strip().replace("\n", " ") if summary_el is not None else ""
        
        published_el = entry.find("atom:published", ns)
        published = published_el.text if published_el is not None else ""
        
        updated_el = entry.find("atom:updated", ns)
        updated = updated_el.text if updated_el is not None else ""
        
        authors = []
        for author in entry.findall("atom:author", ns):
            name_el = author.find("atom:name", ns)
            if name_el is not None:
                authors.append(name_el.text)
        
        primary_cat_el = entry.find("arxiv:primary_category", ns)
        primary_cat = primary_cat_el.get("term", "") if primary_cat_el is not None else ""
        
        all_cats = []
        for cat in entry.findall("atom:category", ns):
            all_cats.append(cat.get("term", ""))
        
        comment_el = entry.find("arxiv:comment", ns)
        comment = comment_el.text if comment_el is not None else ""
        
        doi_el = entry.find("arxiv:doi", ns)
        doi = doi_el.text if doi_el is not None else ""
        
        entries.append({
            "arxiv_id": arxiv_id,
            "title": title,
            "authors": authors,
            "abstract": abstract,
            "published": published,
            "updated": updated,
            "primary_category": primary_cat,
            "all_categories": all_cats,
            "comment": comment,
            "doi": doi,
            "html_url": f"https://arxiv.org/html/{arxiv_id}",
        })
    
    return entries, total_results


def collect_category(category, output_dir):
    """Collect ALL papers from 2023+ in a category, with pagination and retries."""
    print(f"\n=== {category} ===", file=sys.stderr)
    
    data = query_arxiv_page(category, start=0, max_results=100)
    if data is None:
        print(f"  FAILED after retries", file=sys.stderr)
        return []
    
    entries, total = parse_entries(data)
    if total == 0:
        print(f"  No results", file=sys.stderr)
        return []
    
    print(f"  Total in arXiv: {total}", file=sys.stderr)
    
    all_entries = []
    for e in entries:
        if e["published"][:4] >= "2023":
            all_entries.append(e)
    
    print(f"  Page 0: {len(entries)} fetched, {len(all_entries)} from 2023+", file=sys.stderr)
    
    start = 100
    while start < total and start < 10000:
        time.sleep(5)  # 5s between pages to avoid 429
        
        data = query_arxiv_page(category, start=start, max_results=100)
        if data is None:
            print(f"  Failed at start={start}, stopping", file=sys.stderr)
            break
        
        entries, _ = parse_entries(data)
        if not entries:
            break
        
        oldest_year = min(e["published"][:4] for e in entries if e["published"])
        new_count = 0
        for e in entries:
            if e["published"][:4] >= "2023":
                all_entries.append(e)
                new_count += 1
        
        print(f"  Page start={start}: {len(entries)} fetched, {new_count} from 2023+, oldest={oldest_year}", file=sys.stderr)
        
        if oldest_year < "2023":
            print(f"  Reached pre-2023, stopping", file=sys.stderr)
            break
        
        start += 100
    
    # Deduplicate
    seen = set()
    unique = []
    for e in all_entries:
        if e["arxiv_id"] not in seen:
            seen.add(e["arxiv_id"])
            unique.append(e)
    
    print(f"  Total unique 2023+: {len(unique)}", file=sys.stderr)
    
    cat_safe = category.replace(".", "_")
    cat_path = os.path.join(output_dir, f"meta_{cat_safe}.json")
    with open(cat_path, "w") as f:
        json.dump(unique, f, indent=2, ensure_ascii=False)
    
    return unique


def main():
    output_dir = "/data/master-mind/knowledge/arxiv/metadata"
    os.makedirs(output_dir, exist_ok=True)
    
    # Find which categories need retry (no file or file is empty)
    need_retry = []
    already_done = []
    
    for cat in ALL_CATEGORIES:
        cat_safe = cat.replace(".", "_")
        cat_path = os.path.join(output_dir, f"meta_{cat_safe}.json")
        if os.path.exists(cat_path) and os.path.getsize(cat_path) > 10:
            with open(cat_path) as f:
                data = json.load(f)
            if len(data) > 0:
                already_done.append((cat, len(data)))
                continue
        need_retry.append(cat)
    
    print(f"Already done: {len(already_done)} categories", file=sys.stderr)
    for cat, count in already_done:
        print(f"  {cat}: {count} papers", file=sys.stderr)
    
    print(f"\nNeed retry: {len(need_retry)} categories", file=sys.stderr)
    for cat in need_retry:
        print(f"  {cat}", file=sys.stderr)
    
    if not need_retry:
        print("All categories done!", file=sys.stderr)
    else:
        all_papers = {}
        per_category_counts = {}
        
        for cat in need_retry:
            entries = collect_category(cat, output_dir)
            per_category_counts[cat] = len(entries)
            for e in entries:
                all_papers[e["arxiv_id"]] = e
            time.sleep(2)
        
        print(f"\n=== RETRY SUMMARY ===", file=sys.stderr)
        for cat, count in per_category_counts.items():
            print(f"  {cat}: {count}", file=sys.stderr)
        print(f"New papers from retry: {len(all_papers)}", file=sys.stderr)
    
    # Now merge ALL per-category files into combined metadata
    print(f"\n=== MERGING ALL CATEGORIES ===", file=sys.stderr)
    all_papers = {}
    for cat in ALL_CATEGORIES:
        cat_safe = cat.replace(".", "_")
        cat_path = os.path.join(output_dir, f"meta_{cat_safe}.json")
        if os.path.exists(cat_path):
            with open(cat_path) as f:
                entries = json.load(f)
            for e in entries:
                all_papers[e["arxiv_id"]] = e
            print(f"  {cat}: {len(entries)} -> merged", file=sys.stderr)
    
    combined_path = "/data/master-mind/knowledge/arxiv/metadata_all_2023plus.json"
    with open(combined_path, "w") as f:
        json.dump(list(all_papers.values()), f, indent=2, ensure_ascii=False)
    
    print(f"\n=== FINAL TOTAL: {len(all_papers)} unique papers ===", file=sys.stderr)
    print(f"Combined: {combined_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
