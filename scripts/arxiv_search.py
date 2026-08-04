#!/usr/bin/env python3
"""
arXiv API search script for the Mathematical Master System.
Queries arXiv API (free, no key needed) for recent papers in key math categories.
Saves metadata (id, title, authors, abstract, date, categories) to JSON.
"""
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
import time
import os
import sys

ARXIV_API = "https://export.arxiv.org/api/query"

# Key mathematical categories (32 arXiv math categories + selected cross-listed)
MATH_CATEGORIES = [
    "math.NT",   # Number Theory
    "math.CO",   # Combinatorics
    "math.AG",   # Algebraic Geometry
    "math.AT",   # Algebraic Topology
    "math.DG",   # Differential Geometry
    "math.GT",   # Geometric Topology
    "math.RT",   # Representation Theory
    "math.LO",   # Logic
    "math.PR",   # Probability
    "math.ST",   # Statistics
    "math.AP",   # Analysis of PDEs
    "math.CA",   # Classical Analysis
    "math.FA",   # Functional Analysis
    "math.OA",   # Operator Algebras
    "math.HO",   # History and Overview
    "math.KT",   # K-Theory and Homology
    "math.RA",   # Rings and Algebras
    "math.SP",   # Spectral Theory
    "math.SG",   # Symplectic Geometry
    "math.CV",   # Complex Variables
    "math.DS",   # Dynamical Systems
    "math.GN",   # General Topology
    "math.GR",   # Group Theory
    "math.MG",   # Metric Geometry
    "math.MP",   # Mathematical Physics
    "math.NA",   # Numerical Analysis
    "math.OC",   # Optimization and Control
    "math.QA",   # Quantum Algebra
]

def query_arxiv(category, max_results=50, start=0):
    """Query arXiv API for papers in a category, sorted by submission date (newest first)."""
    params = {
        "search_query": f"cat:{category}",
        "start": start,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = ARXIV_API + "?" + urllib.parse.urlencode(params)
    
    req = urllib.request.Request(url, headers={"User-Agent": "MathMasterSystem/1.0 (research collection)"})
    
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read().decode("utf-8")
    except Exception as e:
        print(f"  ERROR fetching {category}: {e}", file=sys.stderr)
        return []
    
    # Parse Atom XML
    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "arxiv": "http://arxiv.org/schemas/atom",
    }
    
    root = ET.fromstring(data)
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
        
        # Authors
        authors = []
        for author in entry.findall("atom:author", ns):
            name_el = author.find("atom:name", ns)
            if name_el is not None:
                authors.append(name_el.text)
        
        # Primary category
        primary_cat_el = entry.find("arxiv:primary_category", ns)
        primary_cat = primary_cat_el.get("term", "") if primary_cat_el is not None else ""
        
        # All categories
        all_cats = []
        for cat in entry.findall("atom:category", ns):
            all_cats.append(cat.get("term", ""))
        
        # Comment (may contain page count, journal ref)
        comment_el = entry.find("arxiv:comment", ns)
        comment = comment_el.text if comment_el is not None else ""
        
        # DOI
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
    
    return entries


def main():
    output_dir = "/data/master-mind/knowledge/arxiv"
    os.makedirs(output_dir, exist_ok=True)
    
    all_papers = {}
    per_category = {}
    
    for cat in MATH_CATEGORIES:
        print(f"Querying {cat}...", file=sys.stderr)
        entries = query_arxiv(cat, max_results=50)
        per_category[cat] = len(entries)
        
        for e in entries:
            # Only keep papers from 2023 onwards (after typical AI training cutoff)
            year = e["published"][:4] if e["published"] else ""
            if year >= "2023":
                all_papers[e["arxiv_id"]] = e
        
        # Rate limit: be polite, 3 seconds between requests
        time.sleep(3)
    
    # Save metadata
    metadata_path = os.path.join(output_dir, "metadata_2023_2026.json")
    with open(metadata_path, "w") as f:
        json.dump(list(all_papers.values()), f, indent=2, ensure_ascii=False)
    
    print(f"\n=== Summary ===", file=sys.stderr)
    print(f"Categories queried: {len(MATH_CATEGORIES)}", file=sys.stderr)
    for cat, count in sorted(per_category.items()):
        print(f"  {cat}: {count} entries", file=sys.stderr)
    print(f"Total unique papers (2023+): {len(all_papers)}", file=sys.stderr)
    print(f"Metadata saved to: {metadata_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
