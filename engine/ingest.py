from pathlib import Path
from datetime import datetime

# Project folders
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "raw"
OUTPUT_DIR = BASE_DIR / "synthesized"

# Output file
OUTPUT_FILE = OUTPUT_DIR / "ingestion-batch.md"

# Find all Markdown files in raw/
items = sorted(RAW_DIR.glob("item-*.md"))

if not items:
    print("No raw items found.")
    exit()

# Create output folder if needed
OUTPUT_DIR.mkdir(exist_ok=True)

# Build ingestion document
today = datetime.now().strftime("%d-%m-%Y")

content = [
    "# Ingestion Batch",
    "",
    f"Date: {today}",
    f"Items ingested: {len(items)}",
    "",
    "## Raw Items",
    ""
]

for item in items:
    text = item.read_text(encoding="utf-8")

    content.append(f"### {item.name}")
    content.append("")
    content.append(text)
    content.append("")
    content.append("---")
    content.append("")

OUTPUT_FILE.write_text("\n".join(content), encoding="utf-8")

print(f"Successfully ingested {len(items)} items.")
print(f"Output: {OUTPUT_FILE}")