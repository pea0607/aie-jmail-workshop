import os
import json
from pathlib import Path
from dotenv import load_dotenv
import reducto

# Load REDUCTO_API_KEY from the .env file
load_dotenv()
api_key = os.getenv("REDUCTO_API_KEY")
if not api_key:
    raise ValueError("REDUCTO_API_KEY not set. Copy .env.example to .env and add your key.")

client = reducto.Reducto(api_key=api_key)

docs_dir = Path("docs")
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

pdf_files = sorted(docs_dir.glob("*.pdf"))
if not pdf_files:
    print("No PDFs found in /docs. Drop your files there and re-run.")
    exit()

for pdf_path in pdf_files:
    print(f"\n--- Parsing: {pdf_path.name} ---")

    # Upload the file and parse it. Reducto returns a structured list of chunks,
    # each with a block_type (e.g. text, table, figure) and its content.
    with open(pdf_path, "rb") as f:
        result = client.parse.file(file=f)

    chunks = result.result.chunks

    # Print a preview of each chunk so you can see what Reducto extracted
    for i, chunk in enumerate(chunks):
        print(f"  Chunk {i+1} | type: {chunk.block_type}")
        print(f"    {chunk.content[:200]}")  # truncate long content for readability

    # Save the full structured output as JSON alongside the source filename
    output_path = output_dir / f"{pdf_path.stem}.json"
    with open(output_path, "w") as out:
        json.dump([c.dict() for c in chunks], out, indent=2)

    print(f"  Saved → {output_path}")

print("\nDone. Check /output for the full JSON results.")
