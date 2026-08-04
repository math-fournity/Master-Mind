#!/usr/bin/env python3
"""
arXiv exhaustive metadata collection v3.
- Date range query: 2025-01-01 to present (most valuable, AI training cutoff)
- max_results=200 per page (API maximum, halves request count)
- 3s intervals (arXiv minimum)
- 429 retry with 60s backoff
- Per-category JSON files for incremental processing
- Also collects 2023-2024 with separate query for completeness
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
    # Math (all 28)
    "math.NT", "math.CO", "math.AG", "math.AT", "math.DG", "math.GT",
    "math.RT", "math.LO", "math.PR", "math.ST", "math.AP", "math.CA",
    "math.FA", "math.OA", "math.HO", "math.KT", "math.RA", "math.SP",
    "math.SG", "math.CV", "math.DS", "math.GN", "math.GR", "math.MG",
    "math.MP", "math.NA", "math.OC", "math.QA",
    # CS theory
    "cs.CC", "cs.LO", "cs.FL", "cs.DS", "cs.CG", "cs.GT", "cs.SC",
    # Physics theory — natural computation
    "quant-ph", "math-ph", "hep-th",
    # Statistics
    "stat.TH", "stat.ML",
    # Nonlinear science — complex systems, chaos, integrable systems
    "nlin.CD", "nlin.SI", "nlin.AO", "nlin.PS",
]


def query_page(search_query, start=0, max_results=200, retries=5):
    """Query one page with retry and 429 handling."""
    params = {
        "search_query": search_query,
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
                wait = 60 * (attempt + 1)
                print(f"  429 rate limited, waiting {wait}s (attempt {attempt+1}/{retries})", file=sys.stderr)
                time.sleep(wait)
            else:
                print(f"  HTTP {e.code}", file=sys.stderr)
                if attempt < retries - 1:
                    time.sleep(15 * (attempt + 1))
        except Exception as e:
            print(f"  Attempt {attempt+1}/{retries} failed: {e}", file=sys.stderr)
            if attempt < retries - 1:
                time.sleep(15 * (attempt + 1))
    return None


def parse_entries(data):
    """Parse Atom XML."""
    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "arxiv": "http://arxiv.org/schemas/atom",
        "opensearch": "http://a9.com/-/spec/opensearch/1.1/",
    }
    root = ET.fromstring(data)
    
    total_el = root.find("opensearch:totalResults", ns)
    total = int(total_el.text) if total_el is not None else 0
    
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
        
        all_cats = [cat.get("term", "") for cat in entry.findall("atom:category", ns)]
        
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
    
    return entries, total


def collect_category_date_range(category, date_from, date_to, output_dir, label=""):
    """Collect papers in a date range for a category."""
    search_query = f"cat:{category} AND submittedDate:[{date_from} TO {date_to}]"
    
    # First page
    data = query_page(search_query, start=0, max_results=200)
    if data is None:
        return []
    
    entries, total = parse_entries(data)
    if total == 0:
        return []
    
    all_entries = list(entries)
    print(f"  [{label}] Total: {total}, page 0: {len(entries)}", file=sys.stderr)
    
    start = 200
    while start < total and start < 10000:
        time.sleep(3)
        
        data = query_page(search_query, start=start, max_results=200)
        if data is None:
            print(f"  Failed at start={start}", file=sys.stderr)
            break
        
        entries, _ = parse_entries(data)
        if not entries:
            break
        
        all_entries.extend(entries)
        print(f"  [{label}] Page start={start}: {len(entries)} (total fetched: {len(all_entries)})", file=sys.stderr)
        start += 200
    
    # Deduplicate
    seen = set()
    unique = []
    for e in all_entries:
        if e["arxiv_id"] not in seen:
            seen.add(e["arxiv_id"])
            unique.append(e)
    
    return unique


def main():
    output_dir = "/data/master-mind/knowledge/arxiv/metadata"
    os.makedirs(output_dir, exist_ok=True)
    
    # Date ranges
    # 2025-2026: most valuable (AI definitely doesn't know these)
    # 2023-2024: also valuable (may be partially in training data)
    date_ranges = [
        ("2025-2026", "20250101000000", "20261231235959"),
        ("2023-2024", "20230101000000", "20241231235959"),
    ]
    
    all_papers = {}
    per_category = {}
    
    for cat in ALL_CATEGORIES:
        cat_safe = cat.replace(".", "_")
        cat_path = os.path.join(output_dir, f"meta_{cat_safe}.json")
        
        # Skip if already done
        if os.path.exists(cat_path) and os.path.getsize(cat_path) > 10:
            with open(cat_path) as f:
                existing = json.load(f)
            if len(existing) > 0:
                print(f"\n=== {cat} (already done: {len(existing)}) ===", file=sys.stderr)
                per_category[cat] = len(existing)
                for e in existing:
                    all_papers[e["arxiv_id"]] = e
                continue
        
        print(f"\n=== {cat} ===", file=sys.stderr)
        cat_papers = []
        
        for label, date_from, date_to in date_ranges:
            entries = collect_category_date_range(cat, date_from, date_to, output_dir, label)
            cat_papers.extend(entries)
            time.sleep(2)
        
        # Deduplicate across date ranges
        seen = set()
        unique = []
        for e in cat_papers:
            if e["arxiv_id"] not in seen:
                seen.add(e["arxiv_id"])
                unique.append(e)
        
        per_category[cat] = len(unique)
        for e in unique:
            all_papers[e["arxiv_id"]] = e
        
        print(f"  Total unique for {cat}: {len(unique)}", file=sys.stderr)
        
        # Save per-category
        with open(cat_path, "w") as f:
            json.dump(unique, f, indent=2, ensure_ascii=False)
    
    # Save combined
    combined_path = "/data/master-mind/knowledge/arxiv/metadata_all_2023plus.json"
    with open(combined_path, "w") as f:
        json.dump(list(all_papers.values()), f, indent=2, ensure_ascii=False)
    
    print(f"\n\n=== FINAL SUMMARY ===", file=sys.stderr)
    total_sum = 0
    for cat in ALL_CATEGORIES:
        count = per_category.get(cat, 0)
        total_sum += count
        print(f"  {cat}: {count}", file=sys.stderr)
    print(f"\nSum per-category: {total_sum}", file=sys.stderr)
    print(f"Total unique papers: {len(all_papers)}", file=sys.stderr)
    print(f"Combined: {combined_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
