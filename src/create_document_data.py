import os
import csv

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
OUTPUT_CSV = os.path.join(BASE_DIR, "data", "document_data.csv")

# --- Collect data ---
data = []
for filename in os.listdir(PROCESSED_DIR):
    if filename.endswith("_raw.txt"):
        file_path = os.path.join(PROCESSED_DIR, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            data.append({"filename": filename, "content": content})

# --- Write to CSV ---
with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["filename", "content"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print(f"✅ Document CSV created → {OUTPUT_CSV}")
