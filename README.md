python src/preprocessing.py
python src/create_document_data.py
python src/document_preprocessing.py
🧩 Phase 1: Preprocessing Pipeline Overview
🎯 Objective

Before any AI model or summarization algorithm can work, the documents (PDFs, DOCX, images, etc.) need to be converted into clean, machine-readable text.
This preprocessing phase ensures that all input data is consistent, clean, and ready for further NLP tasks like summarization or classification.

🗂 1️⃣ File: preprocessing.py
Purpose:

Extract text from multiple file formats such as .pdf, .docx, .jpg, and .png.

How it works:

Scans the data/raw/ folder for all input files.

Uses:

pdfplumber for reading PDFs

docx2txt for Word files

pytesseract and pdf2image for scanned PDFs or images (OCR)

Saves the extracted text into data/processed/ as separate .txt files (e.g., Resume_Piyush_raw.txt).

Output:

data/processed/<filename>_raw.txt

Example:

Input → Resume_Piyush.pdf
Output → Resume_Piyush_raw.txt

In short:

“This script converts all unstructured document formats into plain text files.”

🧾 2️⃣ File: create_document_data.py
Purpose:

Combine all the extracted .txt files into one structured dataset.

How it works:

Reads every _raw.txt file from data/processed/.

Stores filename and its full text content in a single CSV file.

Each row corresponds to one document.

Output:

data/document_data.csv

Columns:

filename	content
Resume_Piyush_raw.txt	"Piyush Wattamwar... JSPM College..."
In short:

“This script merges all individual text files into one centralized dataset, making it easy to process all documents together.”

✨ 3️⃣ File: document_preprocessing.py
Purpose:

Clean and normalize text for summarization.

How it works:

Reads the combined CSV from the previous step.

Performs:

Removal of unwanted symbols, numbers, and URLs

Fixes merged or concatenated words (e.g., “Builtaresponsive” → “Built a responsive”)

Removes extra spaces, newlines, and special characters

Converts text to lowercase if needed

Saves the cleaned version as document_cleaned.csv.

Output:

data/document_cleaned.csv (Ready for Summarization)
