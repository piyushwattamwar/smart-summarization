import os
import re
import csv

# --- Paths ---
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_CSV = os.path.join(PROJECT_ROOT, "data", "document_data.csv")
OUTPUT_CSV = os.path.join(PROJECT_ROOT, "data", "document_cleaned.csv")

# --- Enhanced text cleaning ---


def clean_text(text):
    # testWord -> test Word
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    text = re.sub(r'([a-z])([0-9])', r'\1 \2',
                  text)                # test1 -> test 1
    text = re.sub(r'([0-9])([a-zA-Z])', r'\1 \2',
                  text)             # 1test -> 1 test
    # HTMLCSSReact -> HTML CSS React
    text = re.sub(r'([A-Z]{2,})([A-Z][a-z])', r'\1 \2', text)
    # normalize spaces
    text = re.sub(r'\s+', ' ', text)
    # remove junk characters
    text = re.sub(r'[^a-zA-Z0-9.,;:\-\(\)\s]', '', text)
    return text.strip()


# --- Read CSV, clean content, write new CSV ---
if not os.path.exists(INPUT_CSV):
    print(f"⚠️ Error: Input CSV not found at {INPUT_CSV}")
else:
    with open(INPUT_CSV, 'r', encoding='utf-8', newline='') as infile, \
            open(OUTPUT_CSV, 'w', encoding='utf-8', newline='') as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ["cleaned_content"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            cleaned = clean_text(row['content'])
            row['cleaned_content'] = cleaned
            writer.writerow(row)

    print(f"✅ Document preprocessing completed → {OUTPUT_CSV}")
