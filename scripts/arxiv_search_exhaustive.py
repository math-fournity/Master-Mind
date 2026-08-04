#!/usr/bin/env python3
"""
arXiv API exhaustive search v2.
- Expanded categories: math.*, cs theory, quant-ph, math-ph, hep-th, stat.*, nlin.*
- No per-category limit: paginate to get ALL papers from 2023 onwards
- Saves metadata to JSON, with per-category files for incremental processing
"""
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
import time
import os
import sys

ARXIV_API = "https://export.arxiv.org/api/query"

# All categories to exhaustively collect
# math.* (28) + cs theory (7) + physics theory (3) + stat (2) + nlin (4) = 44
ALL_CATEGORIES = [
    # Math (all 28)
    "math.NT", "math.CO", "math.AG", "math.AT", "math.DG", "math.GT",
    "math.RT", "math.LO", "math.PR", "math.ST", "math.AP", "math.CA",
    "math.FA", "math.OA", "math.HO", "math.KT", "math.RA", "math.SP",
    "math.SG", "math.CV", "math.DS", "math.GN", "math.GR", "math.MG",
    "math.MP", "math.NA", "math.OC", "math.QA",
    # CS theory
    "cs.CC",   # Computational Complexity
    "cs.LO",   # Logic in Computer Science
    "cs.FL",   # Formal Languages and Automata Theory
    "cs.DS",   # Data Structures and Algorithms
    "cs.CG",   # Computational Geometry
    "cs.GT",   # Computer Science and Game Theory
    "cs.SC",   # Symbolic Computation
    # Physics theory
    "quant-ph",  # Quantum Physics — natural computation
    "math-ph",   # Mathematical Physics
    "hep-th",    # High Energy Physics — Theory
    # Statistics
    "stat.TH",   # Statistics Theory
    "stat.ML",   # Machine Learning (statistical)
    # Nonlinear science
    "nlin.CD",   # Cellular Automata and Lattice Gases
    "nlin.SI",   # Exactly Solvable and Integrable Systems
    "nlin.AO",   # Adaptation and Self-Organizing Systems
    "nlin.PS",   # Pattern Formation and Solitons
]


def query_arxiv_page(category, start=0, max_results=100):
    """Query one page of arXiv API. Returns (entries, total_results)."""
    params = {
        "search_query": f"cat:{category}",
        "start": start,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = ARXIV_API + "?" + urllib.parse.urlencode(params)
    
    req = urllib.request.Request(url, headers={
        "User-Agent": "MathMasterSystem/1.0 (research collection)"
    })
    
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read().decode("utf-8")
    except Exception as e:
        print(f"  ERROR: {e}", file=sys.stderr)
        return [], 0
    
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
    """Collect ALL papers from 2023+ in a category, with pagination."""
    print(f"\n=== {category} ===", file=sys.stderr)
    
    # First page to get total count
    entries, total = query_arxiv_page(category, start=0, max_results=100)
    if total == 0:
        print(f"  No results for {category}", file=sys.stderr)
        return []
    
    print(f"  Total in arXiv: {total}", file=sys.stderr)
    
    all_entries = []
    # Filter for 2023+
    for e in entries:
        if e["published"][:4] >= "2023":
            all_entries.append(e)
    
    print(f"  Page 0: {len(entries)} fetched, {len(all_entries)} from 2023+", file=sys.stderr)
    
    # If the first page's oldest paper is still 2023+, keep paginating
    # But also stop if we've gone past 2023
    start = 100
    while start < total:
        # Rate limit
        time.sleep(3)
        
        entries, _ = query_arxiv_page(category, start=start, max_results=100)
        if not entries:
            print(f"  No more entries at start={start}", file=sys.stderr)
            break
        
        # Check if oldest entry in this page is before 2023
        oldest_year = min(e["published"][:4] for e in entries if e["published"])
        new_count = 0
        for e in entries:
            if e["published"][:4] >= "2023":
                all_entries.append(e)
                new_count += 1
        
        print(f"  Page start={start}: {len(entries)} fetched, {new_count} from 2023+, oldest={oldest_year}", file=sys.stderr)
        
        if oldest_year < "2023":
            print(f"  Reached pre-2023 papers, stopping", file=sys.stderr)
            break
        
        start += 100
        
        # Safety: arXiv API limits to 10000 results per query
        if start >= 10000:
            print(f"  Reached 10000 result API limit, stopping", file=sys.stderr)
            break
    
    # Deduplicate by arxiv_id
    seen = set()
    unique = []
    for e in all_entries:
        if e["arxiv_id"] not in seen:
            seen.add(e["arxiv_id"])
            unique.append(e)
    
    print(f"  Total unique 2023+ papers: {len(unique)}", file=sys.stderr)
    
    # Save per-category file
    cat_safe = category.replace(".", "_")
    cat_path = os.path.join(output_dir, f"meta_{cat_safe}.json")
    with open(cat_path, "w") as f:
        json.dump(unique, f, indent=2, ensure_ascii=False)
    
    return unique


def main():
    output_dir = "/data/master-mind/knowledge/arxiv/metadata"
    os.makedirs(output_dir, exist_ok=True)
    
    all_papers = {}
    per_category_counts = {}
    
    for cat in ALL_CATEGORIES:
        entries = collect_category(cat, output_dir)
        per_category_counts[cat] = len(entries)
        for e in entries:
            all_papers[e["arxiv_id"]] = e
        # Extra pause between categories
        time.sleep(2)
    
    # Save combined metadata
    combined_path = "/data/master-mind/knowledge/arxiv/metadata_all_2023plus.json"
    with open(combined_path, "w") as f:
        json.dump(list(all_papers.values()), f, indent=2, ensure_ascii=False)
    
    print(f"\n\n=== FINAL SUMMARY ===", file=sys.stderr)
    print(f"Categories: {len(ALL_CATEGORIES)}", file=sys.stderr)
    total_2023plus = 0
    for cat in ALL_CATEGORIES:
        count = per_category_counts.get(cat, 0)
        total_2023plus += count
        print(f"  {cat}: {count}", file=sys.stderr)
    print(f"\nTotal unique 2023+ papers: {len(all_papers)}", file=sys.stderr)
    print(f"Sum per-category (with cross-lists): {total_2023plus}", file=sys.stderr)
    print(f"Combined metadata: {combined_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
