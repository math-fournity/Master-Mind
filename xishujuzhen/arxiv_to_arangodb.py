#!/usr/bin/env python3
"""
arXiv metadata → ArangoDB importer.
Imports 239K papers from metadata_all_2023plus.json into arxiv_papers collection.
Creates indexes for category/date/author/keyword search.
"""
import json
import os
import sys
import time
from arango import ArangoClient

DB_NAME = os.environ.get("ARANGO_DB", "xishujuzhen_math")
ARANGO_HOST = os.environ.get("ARANGO_HOST", "http://localhost:8529")
ARANGO_USER = "root"
ARANGO_PASS = "REDACTED-DB-PASSWORD"
METADATA_PATH = "/data/master-mind/knowledge/arxiv/metadata_all_2023plus.json"
BATCH_SIZE = 5000


def get_db():
    client = ArangoClient(hosts=ARANGO_HOST)
    return client.db(DB_NAME, username=ARANGO_USER, password=ARANGO_PASS)


def ensure_collection(db):
    """Create arxiv_papers collection if not exists."""
    if not db.has_collection("arxiv_papers"):
        col = db.create_collection("arxiv_papers")
        print(f"Created collection: arxiv_papers")
    else:
        col = db.collection("arxiv_papers")
        print(f"Collection arxiv_papers already exists: {col.count()} docs")
    return col


def ensure_indexes(db, col):
    """Create indexes for search."""
    indexes_created = []

    # Persistent index on primary_category
    try:
        col.add_persistent_index(
            fields=["primary_category"],
            name="idx_primary_cat",
            storedValues=["title", "published", "arxiv_id"]
        )
        indexes_created.append("idx_primary_cat")
    except Exception as e:
        print(f"  idx_primary_cat: {e}")

    # Persistent index on published date
    try:
        col.add_persistent_index(
            fields=["published"],
            name="idx_published"
        )
        indexes_created.append("idx_published")
    except Exception as e:
        print(f"  idx_published: {e}")

    # Persistent index on mapping_level
    try:
        col.add_persistent_index(
            fields=["mapping_level"],
            name="idx_mapping_level",
            storedValues=["arxiv_id", "title"]
        )
        indexes_created.append("idx_mapping_level")
    except Exception as e:
        print(f"  idx_mapping_level: {e}")

    # Persistent index on has_fulltext
    try:
        col.add_persistent_index(
            fields=["has_fulltext"],
            name="idx_has_fulltext",
            storedValues=["arxiv_id", "primary_category"]
        )
        indexes_created.append("idx_has_fulltext")
    except Exception as e:
        print(f"  idx_has_fulltext: {e}")

    # ArangoSearch view for full-text search on title+abstract
    # (ArangoSearch is available in Community Edition)
    try:
        if not db.has_view("arxiv_search_view"):
            db.create_arango_search(
                name="arxiv_search_view",
                properties={
                    "links": {
                        "arxiv_papers": {
                            "fields": {
                                "title": {"analyzers": ["text_en"]},
                                "abstract": {"analyzers": ["text_en"]},
                                "authors": {"analyzers": ["identity"]}
                            }
                        }
                    }
                }
            )
            indexes_created.append("arxiv_search_view")
    except Exception as e:
        print(f"  arxiv_search_view: {e}")

    print(f"Indexes: {indexes_created}")
    return indexes_created


def transform_paper(paper):
    """Transform a metadata entry to arxiv_papers document."""
    arxiv_id = paper["arxiv_id"]
    clean_id = arxiv_id.split("v")[0] if "v" in arxiv_id[-3:] else arxiv_id
    doc_key = clean_id.replace(".", "_")

    # Check if fulltext exists
    fulltext_dir = "/data/master-mind/knowledge/arxiv/fulltext"
    cat_underscore = paper["primary_category"].replace(".", "_")
    fulltext_filename = f"{cat_underscore}_{clean_id.replace('.', '_')}.md"
    fulltext_path = os.path.join(fulltext_dir, fulltext_filename)
    has_fulltext = os.path.exists(fulltext_path)

    return {
        "_key": doc_key,
        "arxiv_id": arxiv_id,
        "clean_id": clean_id,
        "title": paper.get("title", ""),
        "authors": paper.get("authors", []),
        "abstract": paper.get("abstract", ""),
        "primary_category": paper.get("primary_category", ""),
        "all_categories": paper.get("all_categories", []),
        "published": paper.get("published", ""),
        "updated": paper.get("updated", ""),
        "doi": paper.get("doi", ""),
        "comment": paper.get("comment", ""),
        "journal_ref": paper.get("journal_ref", ""),
        "html_url": f"https://arxiv.org/html/{clean_id}",
        "has_fulltext": has_fulltext,
        "fulltext_path": fulltext_path if has_fulltext else "",
        "mapping_level": "L4",
        "linked_nodes": []
    }


def import_papers(db, col):
    """Import all papers in batches."""
    print(f"Loading metadata from {METADATA_PATH}...")
    with open(METADATA_PATH) as f:
        papers = json.load(f)
    print(f"Loaded {len(papers)} papers")

    # Check if already imported
    existing = col.count()
    if existing >= len(papers):
        print(f"Already imported {existing} docs, skipping import")
        return existing

    # If partial import, truncate and reimport
    if existing > 0:
        print(f"Partial import detected ({existing} docs), truncating...")
        col.truncate()
        print("Truncated.")

    total = 0
    batch = []
    for i, paper in enumerate(papers):
        doc = transform_paper(paper)
        batch.append(doc)

        if len(batch) >= BATCH_SIZE:
            result = col.import_bulk(batch, on_duplicate="update")
            total += len(batch)
            print(f"  Imported batch: {total}/{len(papers)} ({100*total/len(papers):.1f}%)")
            batch = []

    # Import remaining
    if batch:
        result = col.import_bulk(batch, on_duplicate="update")
        total += len(batch)
        print(f"  Imported final batch: {total}/{len(papers)}")

    print(f"Total imported: {total}")
    return total


def verify_import(db, col):
    """Verify import correctness."""
    count = col.count()
    print(f"\n=== Verification ===")
    print(f"Total documents: {count}")

    # Check primary categories
    print("\nPrimary categories (top 10):")
    for r in db.aql.execute("""
        FOR p IN arxiv_papers
        COLLECT cat = p.primary_category WITH COUNT INTO c
        SORT c DESC
        LIMIT 10
        RETURN {category: cat, count: c}
    """):
        print(f"  {r['category']}: {r['count']}")

    # Check fulltext availability
    print("\nFulltext availability:")
    for r in db.aql.execute("""
        FOR p IN arxiv_papers
        COLLECT ft = p.has_fulltext WITH COUNT INTO c
        RETURN {has_fulltext: ft, count: c}
    """):
        print(f"  has_fulltext={r['has_fulltext']}: {r['count']}")

    # Check year distribution
    print("\nYear distribution:")
    for r in db.aql.execute("""
        FOR p IN arxiv_papers
        COLLECT year = LEFT(p.published, 4) WITH COUNT INTO c
        SORT year
        RETURN {year: year, count: c}
    """):
        print(f"  {r['year']}: {r['count']}")

    # Test query: math.AG papers
    print("\nSample query: math.AG (latest 3):")
    for r in db.aql.execute("""
        FOR p IN arxiv_papers
        FILTER p.primary_category == "math.AG"
        SORT p.published DESC
        LIMIT 3
        RETURN {arxiv_id: p.arxiv_id, title: p.title, published: p.published}
    """):
        print(f"  {r['arxiv_id']}: {r['title'][:60]}... ({r['published'][:10]})")

    return count


def main():
    db = get_db()
    col = ensure_collection(db)
    ensure_indexes(db, col)

    start = time.time()
    total = import_papers(db, col)
    elapsed = time.time() - start
    print(f"\nImport completed in {elapsed:.1f}s ({total} papers, {total/elapsed:.0f} papers/s)")

    verify_import(db, col)

    print(f"\n=== Done ===")


if __name__ == "__main__":
    main()
