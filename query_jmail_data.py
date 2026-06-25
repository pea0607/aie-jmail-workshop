import duckdb

# Change this to search for any term in the VOL00009 volume
KEYWORD = "invoice"

# Connect to DuckDB — no local database needed, it runs entirely in memory
con = duckdb.connect()

# The Jmail Data API exposes parquet files over HTTPS.
# DuckDB can query them directly without downloading anything.
BASE_URL = "https://data.jmail.world"

print("=" * 55)
print("QUERY 1: Document counts per volume (full archive)")
print("=" * 55)

# This query scans the index file to show how many documents
# exist in each volume — useful for understanding the dataset's scale.
scale_query = f"""
SELECT
    volume,
    COUNT(*) AS document_count
FROM read_parquet('{BASE_URL}/documents-index/*.parquet')
GROUP BY volume
ORDER BY volume
"""

scale_df = con.execute(scale_query).df()
print(scale_df.to_string(index=False))

print()
print("=" * 55)
print(f"QUERY 2: Keyword search in VOL00009 — '{KEYWORD}'")
print("=" * 55)

# This query searches the full-text content of a single volume.
# Swap KEYWORD at the top of this file to search for anything you want.
keyword_query = f"""
SELECT
    doc_id,
    volume,
    content
FROM read_parquet('{BASE_URL}/documents-full/VOL00009.parquet')
WHERE lower(content) LIKE '%{KEYWORD.lower()}%'
LIMIT 10
"""

results_df = con.execute(keyword_query).df()

if results_df.empty:
    print(f"No documents matched '{KEYWORD}' in VOL00009.")
else:
    for _, row in results_df.iterrows():
        print(f"\nDoc ID : {row['doc_id']}")
        print(f"Volume : {row['volume']}")
        # Show a short excerpt around the match
        snippet = row["content"][:300].replace("\n", " ")
        print(f"Excerpt: {snippet}...")

print("\nDone.")
