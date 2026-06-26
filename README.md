# AIE Workshop: How Jmail Leveraged Reducto

This workshop walks through two things: parsing real scanned documents with Reducto, and querying the Jmail dataset — a large archive of digitized mail — using DuckDB.

---

## Prerequisites

- Python 3.8+
- `pip`
- A Reducto API key → [studio.reducto.ai/api-keys](https://studio.reducto.ai/api-keys)

---

## Setup

```bash
git clone <this-repo>
cd <this-repo>
pip3 install -r requirements.txt
cp .env.example .env
# Open .env and paste your Reducto API key
```

---

## Part 1: Parse PDFs with Reducto

The `/docs` folder contains 5 documents as a sample set. You can also replace these or drop in your own PDFs. Run:

```bash
python3 parse_documents.py
```

This sends each PDF through the Reducto Parse API and saves the structured output as JSON in `/output`. The printed output shows each chunk's `block_type` and `content`.

---

## Part 2: Query the Jmail Dataset

```bash
python3 query_jmail_data.py
```

This connects to the Jmail Data API via DuckDB and runs two queries:
- A breakdown of document counts per volume across the full archive
- A keyword search over `VOL00009` — change the `KEYWORD` variable at the top of the file to search for anything you want

---

## Bonus: CLI & MCP Demo (live)

---

## Resources

- Reducto docs: [docs.reducto.ai](https://docs.reducto.ai)
- Jmail Data API: [data.jmail.world](https://data.jmail.world)
- Reducto Studio: [studio.reducto.ai](https://studio.reducto.ai)
