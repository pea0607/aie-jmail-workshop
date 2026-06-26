import os
import json
from pathlib import Path
from dotenv import load_dotenv
import reducto

load_dotenv()
api_key = os.getenv("REDUCTO_API_KEY")
if not api_key:
    raise ValueError("REDUCTO_API_KEY not set. Copy .env.example to .env and add your key.")

client = reducto.Reducto(api_key=api_key)

with open("schema.json") as f:
    schema = json.load(f)

docs_dir = Path("docs")
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

pdf_files = sorted(docs_dir.glob("*.pdf"))
if not pdf_files:
    print("No PDFs found in /docs. Drop your files there and re-run.")
    exit()

for pdf_path in pdf_files:
    print(f"\n--- Extracting: {pdf_path.name} ---")

    with open(pdf_path, "rb") as f:
        upload = client.upload(file=f, extension="pdf")

    result = client.extract.run(
        input=upload.file_id,
        instructions={"schema": schema},
    )

    data = result.result
    for key, value in data.items():
        print(f"  {key:<16} {value}")

    output_path = output_dir / f"{pdf_path.stem}_extracted.json"
    with open(output_path, "w") as out:
        json.dump(data, out, indent=2)

    print(f"  Saved → {output_path}")

print("\nDone. Check /output for the full JSON results.")
